# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Downstream-only public command validation coverage for vendored handoffctl."""

from __future__ import annotations

import argparse
import contextlib
import fcntl
import io
import sys
import tempfile
import time
import unittest
from collections.abc import Callable
from pathlib import Path
from typing import cast
from unittest.mock import patch

from tools import (
    autonomy_limits,
    campaign_runtime,
    change_drift,
    execution_envelope,
    handoffctl,
    production_upgrade_binding,
    resume_card_runtime,
    retry_circuit,
    upgrade_commands,
)


def make_envelope() -> dict[str, object]:
    return {
        "schema_version": 1,
        "envelope_id": "AR-0001-e1",
        "envelope_revision": 1,
        "task": "AR-0001",
        "task_revision": 7,
        "spec_ref": "specs/AR-0001.json",
        "spec_revision": 2,
        "outputs": [{"id": "implementation", "description": "bounded output"}],
        "non_goals": ["preserve restrictions"],
        "path_scope": {"read": ["src"], "write": ["src"]},
        "command_classes": {"test": {"allowed": True, "timeout_seconds": 60}},
        "evidence": [{"id": "tests", "class": "contract-test", "required": True}],
        "stop_conditions": [{"id": "scope", "kind": "deny"}],
    }


class HandoffctlPublicValidationEdgeTests(unittest.TestCase):
    """Exercise public commands with a private coordinator lock domain."""

    def setUp(self) -> None:
        self.directory = tempfile.TemporaryDirectory()
        self.root = Path(self.directory.name)
        runtime = self.root / ".runtime"
        runtime.mkdir(mode=0o700)
        self.globals = patch.multiple(
            handoffctl,
            ROOT=self.root,
            RUNTIME=runtime,
            LOCK=runtime / "state.lock",
        )
        self.globals.start()

    def tearDown(self) -> None:
        self.globals.stop()
        self.directory.cleanup()

    def test_fenced_run_rejects_invalid_retry_window_and_envelope_timeout(self) -> None:
        args = argparse.Namespace(
            task="AR-0001",
            owner="worker",
            command=["true"],
            timeout_seconds=5,
            retry_window=0,
        )
        with (
            patch.object(handoffctl, "backend_selection", return_value={"backend": "sqlite"}),
            patch.object(handoffctl, "require_active_owner", return_value={}),
            patch.object(retry_circuit, "_window", side_effect=ValueError("bad window")),
            self.assertRaisesRegex(RuntimeError, "bad window"),
        ):
            handoffctl._cmd_run_fenced(args)
        args.retry_window = 3
        with (
            patch.object(handoffctl, "backend_selection", return_value={"backend": "sqlite"}),
            patch.object(handoffctl, "require_active_owner", return_value={}),
            patch.object(handoffctl, "run_envelope_timeout", return_value=1.0),
            self.assertRaisesRegex(RuntimeError, "exceeds envelope limit"),
        ):
            handoffctl._cmd_run_fenced(args)

    def test_binding_artifact_path_rejects_unsafe_and_accepts_regular_files(self) -> None:
        target = self.root / "spec.json"
        target.write_text("{}", encoding="utf-8")
        self.assertIsNone(
            handoffctl.binding_artifact_path(argparse.Namespace(spec_ref=None), "bind-spec")
        )
        self.assertIsNone(
            handoffctl.binding_artifact_path(
                argparse.Namespace(spec_ref="../spec.json"), "bind-spec"
            )
        )
        self.assertIsNone(
            handoffctl.binding_artifact_path(
                argparse.Namespace(spec_ref="missing.json"), "bind-spec"
            )
        )
        self.assertEqual(
            target,
            handoffctl.binding_artifact_path(argparse.Namespace(spec_ref="spec.json"), "bind-spec"),
        )
        directory = self.root / "directory"
        directory.mkdir()
        self.assertIsNone(
            handoffctl.binding_artifact_path(argparse.Namespace(spec_ref="directory"), "bind-spec")
        )
        link = self.root / "link.json"
        link.symlink_to(target)
        self.assertIsNone(
            handoffctl.binding_artifact_path(argparse.Namespace(spec_ref="link.json"), "bind-spec")
        )
        oversized = self.root / "oversized.json"
        with oversized.open("wb") as stream:
            stream.truncate(4_194_305)
        self.assertIsNone(
            handoffctl.binding_artifact_path(
                argparse.Namespace(spec_ref="oversized.json"), "bind-spec"
            )
        )

    def test_bind_envelope_candidate_rejects_identity_and_revision_mismatches(self) -> None:
        candidate = make_envelope()
        meta: dict[str, object] = {
            "spec_ref": "specs/AR-0001.json",
            "spec_revision": 2,
            "task_revision": 7,
        }
        args = argparse.Namespace(task="AR-0001", envelope_ref="env.json", envelope_revision=1)
        cases: tuple[tuple[Callable[[dict[str, object]], object], str], ...] = (
            (lambda item: item.update(spec_ref="other.json"), "task or spec"),
            (lambda item: item.update(task_revision=4), "task revision"),
            (lambda item: item.update(spec_revision=3), "spec revision"),
            (lambda item: item.update(envelope_revision=2), "envelope revision"),
        )
        for mutate, message in cases:
            item = dict(candidate)
            mutate(item)
            with (
                patch.object(execution_envelope, "load", return_value=(item, "", [])),
                self.assertRaisesRegex(RuntimeError, message),
            ):
                handoffctl.bind_envelope_candidate(args, meta)

    def test_snapshot_rejects_validation_and_backend_races(self) -> None:
        for label, selections, errors, message in (
            (
                "invalid-view",
                [{"backend": "sqlite"}, {"backend": "sqlite"}],
                ["CURRENT.md is stale"],
                "snapshot refused",
            ),
            (
                "backend-changed",
                [{"backend": "sqlite"}, {"backend": "git"}],
                [],
                "BACKEND_CHANGED",
            ),
        ):
            with (
                self.subTest(label=label),
                patch.object(handoffctl, "backend_selection", side_effect=selections),
                patch.object(handoffctl, "validate", return_value=errors),
                patch.object(handoffctl, "print_snapshot_under_lock") as rendered,
                self.assertRaisesRegex(RuntimeError, message),
            ):
                handoffctl.cmd_snapshot()
            rendered.assert_not_called()

    def test_envelope_preflight_and_timeout_fail_closed(self) -> None:
        args = argparse.Namespace(
            task="AR-0042", owner="worker", command_class="test", scope_path=[]
        )
        with patch.object(handoffctl, "locate", return_value=(None, {"id": "AR-0042"}, "")):
            self.assertEqual(
                (False, "WORKTREE_BINDING_REQUIRED", "bound execution requires a worktree", None),
                handoffctl.execution_preflight(args),
            )

        bound = argparse.Namespace(task="AR-0042", command_class=None)
        with (
            patch.object(
                handoffctl,
                "locate",
                return_value=(None, {"id": "AR-0042", "execution_envelope_ref": "env"}, ""),
            ),
            self.assertRaisesRegex(RuntimeError, "requires --command-class"),
        ):
            handoffctl.run_envelope_timeout(bound)

        rejected = argparse.Namespace(task="AR-0042", command_class="test", scope_path=[])
        with (
            patch.object(handoffctl, "locate", return_value=(None, {"id": "AR-0042"}, "")),
            patch.object(
                handoffctl,
                "execution_preflight",
                return_value=(False, "PATH_SCOPE_UNAVAILABLE", "missing scope", None),
            ),
            self.assertRaisesRegex(RuntimeError, "PATH_SCOPE_UNAVAILABLE: missing scope"),
        ):
            handoffctl.run_envelope_timeout(rejected)

    def test_preflight_rendering_releases_resources_for_both_outcomes(self) -> None:
        for allowed, as_json, expected_status, expected in (
            (True, False, 0, "OK: ready"),
            (False, True, 2, '"code":"DENIED"'),
        ):
            with (
                self.subTest(allowed=allowed, as_json=as_json),
                patch.object(
                    handoffctl,
                    "execution_preflight",
                    return_value=(allowed, "OK" if allowed else "DENIED", "ready", 42.0),
                ),
                patch.object(handoffctl, "release_envelope_worktree") as release,
                contextlib.redirect_stdout(io.StringIO()) as output,
            ):
                status = handoffctl.print_execution_preflight(argparse.Namespace(json=as_json))
            self.assertEqual(expected_status, status)
            self.assertIn(expected, output.getvalue())
            release.assert_called_once()

    def test_upgrade_apply_requires_binding_before_contract_access(self) -> None:
        args = argparse.Namespace(
            upgrade_action="apply", binding=None, contract=Path("missing.json")
        )
        with (
            patch.object(handoffctl, "backend_selection", return_value={"backend": "sqlite"}),
            self.assertRaisesRegex(RuntimeError, "require --binding"),
        ):
            handoffctl.cmd_upgrade(args)

    def test_doctor_and_analytics_report_public_backend_errors(self) -> None:
        with (
            patch.object(handoffctl, "backend_selection", return_value={"backend": "git"}),
            contextlib.redirect_stdout(io.StringIO()) as output,
        ):
            self.assertEqual(1, handoffctl.cmd_doctor(live=False))
        self.assertIn("ERROR:", output.getvalue())

        with (
            patch.object(handoffctl, "backend_selection", return_value={"backend": "git"}),
            self.assertRaisesRegex(RuntimeError, "board requires the SQLite authority"),
        ):
            handoffctl.cmd_board()

    def test_main_rejects_invalid_public_command_arguments_before_binding(self) -> None:
        argv = ["handoffctl", "preflight", "AR-0042", "--owner", "worker", "--command-class", "bad"]
        with (
            patch.object(sys, "argv", argv),
            patch.object(handoffctl, "assert_project_binding") as bound,
            self.assertRaises(SystemExit) as exited,
            contextlib.redirect_stderr(io.StringIO()),
        ):
            handoffctl.main()
        self.assertEqual(2, exited.exception.code)
        bound.assert_not_called()

    def test_dispatch_side_effect_reconcile_and_unknown_are_explicit(self) -> None:
        reconcile = argparse.Namespace(cmd="reconcile", commit=True, push=False)
        unknown = argparse.Namespace(cmd="not-a-command")
        with patch.object(handoffctl, "reconcile") as operation:
            self.assertTrue(handoffctl.dispatch_side_effect_command(reconcile))
            self.assertFalse(handoffctl.dispatch_side_effect_command(unknown))
        operation.assert_called_once_with(do_commit=True, push=False)

    def test_dispatch_side_effect_routes_all_bounded_mutations(self) -> None:
        cases: tuple[tuple[str, dict[str, object], str], ...] = (
            ("reconcile", {"commit": True, "push": False}, "reconcile"),
            ("checkpoint", {}, "cmd_checkpoint"),
            ("rollback", {}, "cmd_rollback"),
            ("render-status", {"check": True}, "cmd_render_status"),
            ("migrate", {}, "cmd_migrate"),
        )
        for command, values, handler_name in cases:
            with self.subTest(command=command):
                args = argparse.Namespace(cmd=command, **values)
                with patch.object(handoffctl, handler_name) as handler:
                    self.assertTrue(handoffctl.dispatch_side_effect_command(args))
                handler.assert_called_once()

    def test_dispatch_read_only_routes_public_views(self) -> None:
        cases: tuple[tuple[str, dict[str, object], str], ...] = (
            ("snapshot", {"task": "AR-0001"}, "cmd_snapshot"),
            ("board", {}, "cmd_board"),
            ("metrics", {}, "cmd_metrics"),
        )
        for command, values, handler_name in cases:
            with self.subTest(command=command):
                args = argparse.Namespace(cmd=command, **values)
                with patch.object(handoffctl, handler_name) as handler:
                    self.assertEqual(0, handoffctl.dispatch_read_only_command(args))
                handler.assert_called_once()

        resume_args = argparse.Namespace(cmd="resume-card")
        with patch.object(resume_card_runtime, "dispatch", return_value=7) as dispatch:
            self.assertEqual(7, handoffctl.dispatch_read_only_command(resume_args))
        dispatch.assert_called_once()

        preflight_args = argparse.Namespace(cmd="preflight")
        with patch.object(handoffctl, "print_execution_preflight", return_value=2) as render:
            self.assertEqual(2, handoffctl.dispatch_read_only_command(preflight_args))
        render.assert_called_once_with(preflight_args)

        campaign_args = argparse.Namespace(cmd="campaign")
        with patch.object(campaign_runtime, "dispatch", return_value=8) as dispatch:
            self.assertEqual(8, handoffctl.dispatch_read_only_command(campaign_args))
        dispatch.assert_called_once()

    def test_upgrade_consume_passes_the_complete_runtime_identity(self) -> None:
        args = argparse.Namespace(
            upgrade_action="consume",
            selector="runtime-selector.json",
            releases_root="releases",
            source_commit="commit",
            tag_ref="refs/tags/v1",
            tag_object="tag-object",
            signature_sha256="signature",
            trust_policy_sha256="policy",
            vendor_manifest_sha256="vendor",
            manifest_digest="manifest",
            runtime_command=["python", "-m", "service"],
        )
        with patch.object(
            upgrade_commands, "consume_selected_runtime_command", return_value=9
        ) as consume:
            self.assertEqual(9, handoffctl.cmd_upgrade(args))
        identity = consume.call_args.args[2]
        self.assertEqual("commit", identity.source_commit)
        self.assertEqual("refs/tags/v1", identity.tag_ref)
        consume.assert_called_once_with(
            Path("runtime-selector.json"),
            Path("releases"),
            identity,
            "manifest",
            ("python", "-m", "service"),
        )

    def test_upgrade_mutations_resolve_backend_live_bindings_before_execution(self) -> None:
        for backend, resolver_name in (
            ("sqlite", "resolve_sqlite_live_binding"),
            ("git", "resolve_git_live_binding"),
        ):
            with self.subTest(backend=backend):
                args = argparse.Namespace(
                    upgrade_action="apply",
                    binding="binding.json",
                    contract="contract.json",
                )
                with (
                    patch.object(
                        handoffctl, "backend_selection", return_value={"backend": backend}
                    ),
                    patch.object(upgrade_commands, "_read_contract", return_value={"version": 1}),
                    patch.object(
                        upgrade_commands,
                        "_read_runtime_binding",
                        return_value={"backend": backend},
                    ),
                    patch.object(
                        production_upgrade_binding,
                        resolver_name,
                        return_value={"live": backend},
                    ) as resolve,
                    patch.object(
                        upgrade_commands, "execute_upgrade_command", return_value=10
                    ) as execute,
                ):
                    self.assertEqual(10, handoffctl.cmd_upgrade(args))
                resolve.assert_called_once()
                execute.assert_called_once_with(
                    "apply", Path("contract.json"), backend, Path("binding.json"), {"live": backend}
                )

    def test_execution_lock_timeout_and_invalid_task_id_fail_closed(self) -> None:
        with self.assertRaisesRegex(RuntimeError, "invalid task execution fence"):
            handoffctl.task_execution_lock_path("not-a-task")
        with (
            patch.object(fcntl, "flock", side_effect=[BlockingIOError(), None]),
            self.assertRaisesRegex(handoffctl.LockTimeoutError, "LOCK_TIMEOUT"),
            handoffctl.task_execution_locked("AR-0001", exclusive=True, timeout=0),
        ):
            self.fail("lock acquisition unexpectedly succeeded")

    def test_external_observation_retries_then_reports_bounded_failure(self) -> None:
        with (
            patch.object(handoffctl, "run", side_effect=RuntimeError("unavailable")),
            patch.object(time, "sleep") as sleep,
            self.assertRaisesRegex(handoffctl.ExternalObservationError, "after 3 attempts"),
        ):
            handoffctl.run_github_observation(["gh", "api", "user"])
        self.assertEqual(2, sleep.call_count)

    def test_execution_preflight_rejects_invalid_binding_and_missing_envelope(self) -> None:
        args = argparse.Namespace(
            task="AR-0001",
            owner="worker",
            command_class="test",
            scope_path=[],
        )
        with (
            patch.object(handoffctl, "locate", return_value=(None, {"worktree_key": "bad"}, "")),
            patch.object(
                change_drift,
                "bound_worktree",
                side_effect=RuntimeError("stale worktree"),
            ),
            patch.object(handoffctl, "config", return_value={"projects_root": str(self.root)}),
        ):
            self.assertEqual(
                (False, "WORKTREE_BINDING_INVALID", "stale worktree", None),
                handoffctl.execution_preflight(args),
            )

        with (
            patch.object(handoffctl, "locate", return_value=(None, {"worktree_key": "bound"}, "")),
            patch.object(handoffctl, "config", return_value={"projects_root": str(self.root)}),
            patch.object(
                change_drift,
                "bound_worktree",
                return_value=contextlib.nullcontext(self.root / "123"),
            ),
            patch.object(
                execution_envelope,
                "preflight",
                return_value=argparse.Namespace(allowed=True, code="OK", detail="ready"),
            ),
        ):
            self.assertEqual(
                (False, "ENVELOPE_INVALID", "durable execution envelope is missing", None),
                handoffctl.execution_preflight(args),
            )

    def test_execution_preflight_rejects_envelope_digest_mismatch(self) -> None:
        args = argparse.Namespace(
            task="AR-0001",
            owner="worker",
            command_class="test",
            scope_path=[],
        )
        envelope = make_envelope()
        meta = {
            "worktree_key": "bound",
            "execution_envelope": envelope,
            "execution_envelope_digest": "sha256:stale",
        }
        allowed = argparse.Namespace(allowed=True, code="OK", detail="ready")
        with (
            patch.object(handoffctl, "locate", return_value=(None, meta, "")),
            patch.object(handoffctl, "config", return_value={"projects_root": str(self.root)}),
            patch.object(
                change_drift,
                "bound_worktree",
                return_value=contextlib.nullcontext(self.root / "123"),
            ),
            patch.object(execution_envelope, "preflight", return_value=allowed),
        ):
            self.assertEqual(
                (False, "ENVELOPE_INVALID", "durable execution envelope digest mismatches", None),
                handoffctl.execution_preflight(args),
            )

    def test_execution_preflight_releases_denied_and_scope_error_worktrees(self) -> None:
        args = argparse.Namespace(
            task="AR-0001",
            owner="worker",
            command_class="test",
            scope_path=[],
        )
        meta = {"worktree_key": "bound"}
        denied = argparse.Namespace(allowed=False, code="DENIED", detail="policy")
        with (
            patch.object(handoffctl, "locate", return_value=(None, meta, "")),
            patch.object(handoffctl, "config", return_value={"projects_root": str(self.root)}),
            patch.object(
                change_drift,
                "bound_worktree",
                return_value=contextlib.nullcontext(self.root / "123"),
            ),
            patch.object(execution_envelope, "preflight", return_value=denied),
        ):
            self.assertEqual(
                (False, "DENIED", "policy", None),
                handoffctl.execution_preflight(args),
            )

        envelope = make_envelope()
        second_meta: dict[str, object] = {
            "worktree_key": "bound",
            "execution_envelope": envelope,
            "execution_envelope_digest": execution_envelope.canonical_digest(envelope),
        }
        with (
            patch.object(handoffctl, "locate", return_value=(None, second_meta, "")),
            patch.object(handoffctl, "config", return_value={"projects_root": str(self.root)}),
            patch.object(
                change_drift,
                "bound_worktree",
                return_value=contextlib.nullcontext(self.root / "123"),
            ),
            patch.object(
                execution_envelope,
                "preflight",
                return_value=argparse.Namespace(allowed=True, code="OK", detail="ready"),
            ),
            patch.object(handoffctl, "prepare_envelope_mounts", side_effect=RuntimeError("scope")),
        ):
            self.assertEqual(
                (False, "PATH_SCOPE_UNAVAILABLE", "scope", None),
                handoffctl.execution_preflight(args),
            )

    def test_prepare_envelope_mounts_records_source_write_scope(self) -> None:
        envelope = make_envelope()
        command_classes = cast(dict[str, dict[str, object]], envelope["command_classes"])
        command_classes["source-write"] = {"allowed": True, "timeout_seconds": 60}
        args = argparse.Namespace(
            command_class="source-write",
            scope_path=["src"],
            authorize_external_side_effects=False,
        )
        with patch.object(handoffctl, "envelope_scope_path") as scope:
            rule = handoffctl.prepare_envelope_mounts(args, envelope, Path("123"), object())
        self.assertEqual({"allowed": True, "timeout_seconds": 60}, rule)
        self.assertEqual(2, scope.call_count)
        self.assertEqual(["src"], args._envelope_write_scope)
        self.assertEqual(["src"], args._envelope_read_scope)

    def test_worker_identity_and_private_title_validation_fail_closed(self) -> None:
        with self.assertRaisesRegex(RuntimeError, "positive --worker-pid"):
            handoffctl.claimed_process_identity(
                argparse.Namespace(worker_pid=0, worker_start_time=1)
            )
        with (
            patch.object(handoffctl, "process_start_time", return_value=None),
            self.assertRaisesRegex(RuntimeError, "not a live matching process"),
        ):
            handoffctl.claimed_process_identity(
                argparse.Namespace(worker_pid=123, worker_start_time=1)
            )
        self.assertIsNone(handoffctl.process_start_time(-1))
        with patch.object(handoffctl, "private_text_errors", return_value=["private"]):
            self.assertEqual(
                ["AR-0001: privacy-unsafe short_title"],
                handoffctl.short_title_errors(Path("task.json"), "AR-0001", "safe"),
            )

    def test_missing_runtime_config_is_rejected(self) -> None:
        with (
            patch.object(handoffctl, "CONFIG", self.root / "missing.json"),
            self.assertRaisesRegex(RuntimeError, "missing private runtime config"),
        ):
            handoffctl.config()

    def test_worker_scope_rejects_unreadable_and_invalid_boot_identity(self) -> None:
        with (
            patch.object(Path, "read_text", side_effect=OSError("unreadable")),
            self.assertRaisesRegex(
                RuntimeError, "cannot independently read worker execution scope"
            ),
        ):
            handoffctl.worker_execution_scope()

    def test_preflight_timeout_is_rendered_and_run_requires_scope_defaults(self) -> None:
        args = argparse.Namespace(json=True)
        with (
            patch.object(
                handoffctl,
                "execution_preflight",
                return_value=(True, "OK", "ready", 30.0),
            ),
            patch.object(handoffctl, "release_envelope_worktree"),
            contextlib.redirect_stdout(io.StringIO()) as output,
        ):
            self.assertEqual(0, handoffctl.print_execution_preflight(args))
        self.assertIn('"timeout_seconds":30.0', output.getvalue())

        run_args = argparse.Namespace(task="AR-0001", command_class="test")
        with (
            patch.object(
                handoffctl,
                "locate",
                return_value=(None, {"execution_envelope_ref": "env"}, ""),
            ),
            patch.object(
                handoffctl,
                "execution_preflight",
                return_value=(True, "OK", "ready", 30.0),
            ),
        ):
            self.assertEqual(30.0, handoffctl.run_envelope_timeout(run_args))
        self.assertEqual([], run_args.scope_path)
        with (
            patch.object(Path, "read_text", return_value="not-a-uuid"),
            self.assertRaisesRegex(RuntimeError, "invalid boot identity"),
        ):
            handoffctl.worker_execution_scope()

    def test_task_lock_retries_once_before_acquiring(self) -> None:
        with (
            patch.object(fcntl, "flock", side_effect=[BlockingIOError(), None, None]),
            patch.object(time, "monotonic", side_effect=[0.0, 0.0, 2.0]),
            patch.object(time, "sleep") as sleep,
            handoffctl.task_execution_locked("AR-0001", exclusive=True, timeout=1),
        ):
            pass
        sleep.assert_called_once()

    def test_dispatch_returning_command_routes_lifecycle_handlers(self) -> None:
        with patch.object(handoffctl, "dispatch_roles_command", return_value=3) as roles:
            self.assertEqual(
                3, handoffctl.dispatch_returning_command(argparse.Namespace(cmd="roles"))
            )
        roles.assert_called_once()

        with patch.object(handoffctl, "dispatch_retry_circuit", return_value=4) as retry:
            self.assertEqual(
                4, handoffctl.dispatch_returning_command(argparse.Namespace(cmd="retry-circuit"))
            )
        retry.assert_called_once()

        with patch.object(autonomy_limits, "dispatch", return_value=5) as autonomy:
            self.assertEqual(
                5, handoffctl.dispatch_returning_command(argparse.Namespace(cmd="autonomy-limits"))
            )
        autonomy.assert_called_once()

        with patch.object(handoffctl, "cmd_doctor", return_value=6) as doctor:
            args = argparse.Namespace(cmd="doctor", live=True)
            self.assertEqual(6, handoffctl.dispatch_returning_command(args))
        doctor.assert_called_once_with(live=True)

        with patch.object(handoffctl, "cmd_upgrade", return_value=7) as upgrade:
            args = argparse.Namespace(cmd="upgrade")
            self.assertEqual(7, handoffctl.dispatch_returning_command(args))
        upgrade.assert_called_once_with(args)
        self.assertIsNone(handoffctl.dispatch_returning_command(argparse.Namespace(cmd="unknown")))
