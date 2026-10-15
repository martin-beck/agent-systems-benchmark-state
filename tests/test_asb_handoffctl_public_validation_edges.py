# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Downstream-only public command validation coverage for vendored handoffctl."""

from __future__ import annotations

import argparse
import contextlib
import io
import sys
import tempfile
import unittest
from collections.abc import Callable
from pathlib import Path
from unittest.mock import patch

from tools import (
    autonomy_limits,
    execution_envelope,
    handoffctl,
    resume_card_runtime,
    retry_circuit,
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
        meta = {
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
