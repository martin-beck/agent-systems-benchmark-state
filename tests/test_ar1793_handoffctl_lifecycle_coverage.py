# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Direct mocked coverage for handoffctl lifecycle admission boundaries."""

from __future__ import annotations

import argparse
import contextlib
import subprocess
import unittest
from pathlib import Path
from typing import Any
from unittest.mock import MagicMock, patch

from tools import handoffctl, predicate_ledger


def active_meta(**changes: object) -> dict[str, Any]:
    """Return a minimal current claim suitable for lifecycle admission tests."""
    meta: dict[str, Any] = {
        "id": "AR-1793",
        "owner": "worker-a",
        "status": "in_progress",
        "claim_expires": "2999-01-01T00:00:00+00:00",
        "task_revision": 7,
        "branch": "",
        "worktree_key": "",
    }
    meta.update(changes)
    return meta


def binding_args(**changes: object) -> argparse.Namespace:
    """Return one first-bind request with a matching owner and revision."""
    values: dict[str, Any] = {
        "task": "AR-1793",
        "owner": "worker-a",
        "expected_revision": 7,
        "branch": "feature/ar-1793",
        "worktree_key": "ar1793-worker",
    }
    values.update(changes)
    return argparse.Namespace(**values)


class BindSpecAdmissionCoverageTests(unittest.TestCase):
    """Exercise every bind-spec rejection without touching coordinator state."""

    def test_bind_spec_rejections_preserve_unbound_metadata(self) -> None:
        args = binding_args(spec_ref="specs/ar1793.json", spec_revision=3)
        cases: tuple[tuple[str, dict[str, object], str], ...] = (
            ("wrong-owner", {"owner": "worker-b"}, "owned by worker-b"),
            ("inactive", {"status": "open"}, "active task"),
            ("expired", {"claim_expires": "2000-01-01T00:00:00+00:00"}, "unexpired"),
            ("invalid-expiry", {"claim_expires": "not-a-date"}, "unexpired"),
            ("stale", {"task_revision": 8}, "stale revision"),
            ("spec-ref", {"spec_ref": "specs/old.json"}, "unbound task spec"),
            ("spec-revision", {"spec_revision": 2}, "unbound task spec"),
            ("acceptance", {"spec_acceptance": {}}, "unbound task spec"),
        )
        with patch.object(handoffctl, "require_role_admission"):
            for label, changes, message in cases:
                with self.subTest(label=label):
                    meta = active_meta(**changes)
                    before = dict(meta)
                    with self.assertRaisesRegex(RuntimeError, message):
                        handoffctl.apply_bind_spec(args, meta, None)
                    self.assertEqual(before, meta)

    def test_bind_spec_role_and_spec_validation_fail_closed_before_write(self) -> None:
        args = binding_args(spec_ref="specs/ar1793.json", spec_revision=3)
        meta = active_meta()
        with (
            patch.object(handoffctl, "require_role_admission", side_effect=RuntimeError("denied")),
            self.assertRaisesRegex(RuntimeError, "denied"),
        ):
            handoffctl.apply_bind_spec(args, meta, None)
        self.assertNotIn("spec_ref", meta)
        with (
            patch.object(handoffctl, "require_role_admission"),
            patch.object(handoffctl, "task_spec_errors", return_value=["digest mismatch"]),
            self.assertRaisesRegex(RuntimeError, "task spec is invalid: digest mismatch"),
        ):
            handoffctl.apply_bind_spec(args, meta, None)
        self.assertNotIn("spec_ref", meta)

    def test_bind_spec_success_writes_only_the_immutable_reference(self) -> None:
        args = binding_args(spec_ref="specs/ar1793.json", spec_revision=3)
        meta = active_meta()
        with (
            patch.object(handoffctl, "require_role_admission"),
            patch.object(handoffctl, "task_spec_errors", return_value=[]),
        ):
            result = handoffctl.apply_bind_spec(args, meta, None)
        self.assertEqual("Bound task spec specs/ar1793.json revision 3.", result)
        self.assertEqual("specs/ar1793.json", meta["spec_ref"])
        self.assertEqual(3, meta["spec_revision"])


class WorktreeBindingCoverageTests(unittest.TestCase):
    """Cover binding validators and the exact replay admission boundary."""

    def test_branch_validator_checks_git_result_and_timeout(self) -> None:
        valid = subprocess.CompletedProcess([], 0, stdout="feature/ar-1793\n", stderr="")
        wrong_output = subprocess.CompletedProcess([], 0, stdout="other\n", stderr="")
        rejected = subprocess.CompletedProcess([], 1, stdout="", stderr="")
        with patch.object(handoffctl, "run", side_effect=[valid, wrong_output, rejected]):
            self.assertTrue(handoffctl.valid_binding_branch("feature/ar-1793"))
            self.assertFalse(handoffctl.valid_binding_branch("feature/ar-1793"))
            self.assertFalse(handoffctl.valid_binding_branch("feature/ar-1793"))
        with patch.object(handoffctl, "run", side_effect=handoffctl.SubprocessTimeoutError("late")):
            self.assertFalse(handoffctl.valid_binding_branch("feature/ar-1793"))
        self.assertFalse(handoffctl.valid_binding_branch("DETACHED"))
        self.assertFalse(handoffctl.valid_binding_branch("x" * 129))

    def test_worktree_validator_and_admission_rejections_are_fail_closed(self) -> None:
        args = binding_args()
        with patch.object(
            handoffctl,
            "config",
            return_value={"projects_root": "/projects", "product_worktree": "product"},
        ):
            self.assertTrue(handoffctl.valid_binding_worktree("ar1793-worker"))
            self.assertFalse(handoffctl.valid_binding_worktree("product"))
        with patch.object(
            handoffctl,
            "config",
            side_effect=[{"product_worktree": "product"}, RuntimeError("unavailable")],
        ):
            self.assertTrue(handoffctl.valid_binding_worktree("ar1793-worker"))
        failures: tuple[
            tuple[str, bool, bool, list[tuple[Path, dict[str, Any], str]], str], ...
        ] = (
            ("branch", False, True, [], "branch is invalid"),
            ("worktree", True, False, [], "worktree key is invalid"),
            (
                "conflict",
                True,
                True,
                [(Path("other.md"), active_meta(id="AR-1794", branch=args.branch), "")],
                "identity conflicts",
            ),
        )
        for label, branch_valid, worktree_valid, tasks, message in failures:
            with (
                self.subTest(label=label),
                patch.object(handoffctl, "require_active_binding_owner"),
                patch.object(handoffctl, "valid_binding_branch", return_value=branch_valid),
                patch.object(handoffctl, "valid_binding_worktree", return_value=worktree_valid),
                self.assertRaisesRegex(RuntimeError, message),
            ):
                handoffctl.require_bind_worktree_admission(args, active_meta(), tasks)

    def test_worktree_exact_replay_is_idempotent_but_partial_legacy_data_is_rejected(self) -> None:
        args = binding_args()
        with (
            patch.object(handoffctl, "require_active_binding_owner"),
            patch.object(handoffctl, "valid_binding_branch", return_value=True),
            patch.object(handoffctl, "valid_binding_worktree", return_value=True),
            self.assertRaisesRegex(handoffctl.IdempotentMutationError, "already bound"),
        ):
            handoffctl.require_bind_worktree_admission(
                args, active_meta(branch=args.branch, worktree_key=args.worktree_key), []
            )
        with (
            patch.object(handoffctl, "require_active_binding_owner"),
            patch.object(handoffctl, "valid_binding_branch", return_value=True),
            patch.object(handoffctl, "valid_binding_worktree", return_value=True),
            self.assertRaisesRegex(RuntimeError, "empty legacy"),
        ):
            handoffctl.require_bind_worktree_admission(args, active_meta(branch=args.branch), [])


class LifecycleRecoveryCoverageTests(unittest.TestCase):
    """Prove recovery and acceptance stop at their lifecycle gates."""

    def test_bound_execution_transitions_preserve_receipt_and_recovery_fences(self) -> None:
        digest = "sha256:" + "a" * 64
        argv_digest = "b" * 64
        start = argparse.Namespace(
            task="AR-1793",
            owner="worker-a",
            expected_revision=7,
            execution_id="c" * 32,
            execution_expires_at="2999-01-01T00:00:00+00:00",
            command_class="test",
            scope_digest="sha256:" + "d" * 64,
            argv_digest=argv_digest,
        )
        meta = active_meta(
            execution_envelope={"envelope_id": "AR-1793-e1"},
            execution_envelope_digest=digest,
        )
        with patch.object(handoffctl, "require_active_binding_owner"):
            self.assertEqual(
                "Reserved bound execution " + "c" * 32 + ".",
                handoffctl.apply_execution_start(start, meta),
            )
        reservation = meta["execution_reservation"]
        self.assertEqual(start.execution_id, reservation["execution_id"])
        with (
            patch.object(handoffctl, "require_active_binding_owner"),
            self.assertRaisesRegex(RuntimeError, "live execution"),
        ):
            handoffctl.apply_execution_start(start, meta)

        receipt = argparse.Namespace(
            task="AR-1793",
            owner="worker-a",
            expected_revision=7,
            execution_id=start.execution_id,
            classification="EXIT",
            returncode=0,
            recorded_at="2026-10-13T00:00:00+00:00",
        )
        self.assertEqual(
            "Recorded execution result " + start.execution_id + ".",
            handoffctl.apply_execution_result(receipt, meta),
        )
        with self.assertRaisesRegex(handoffctl.IdempotentMutationError, "already recorded"):
            handoffctl.apply_execution_result(receipt, meta)
        finish = argparse.Namespace(
            task="AR-1793",
            owner="worker-a",
            expected_revision=7,
            execution_id=start.execution_id,
            note="execution finished",
        )
        self.assertEqual("execution finished", handoffctl.apply_execution_finish(finish, meta))
        self.assertNotIn("execution_reservation", meta)

        expired = active_meta(
            execution_reservation={
                **reservation,
                "expires_at": "2000-01-01T00:00:00+00:00",
            },
            execution_result={
                "execution_id": start.execution_id,
                "owner": "worker-a",
                "envelope_digest": digest,
                "argv_digest": argv_digest,
                "classification": "EXIT",
                "returncode": 0,
                "recorded_at": "2026-10-13T00:00:00+00:00",
            },
        )
        with patch.object(handoffctl, "require_claimed_worker_absent"):
            self.assertEqual(
                "Recovered completed execution " + start.execution_id + ".",
                handoffctl.apply_recover_execution(
                    argparse.Namespace(expected_revision=7), expired
                ),
            )
        self.assertNotIn("execution_reservation", expired)
        with self.assertRaisesRegex(RuntimeError, "valid reservation"):
            handoffctl.apply_recover_execution(
                argparse.Namespace(expected_revision=7), active_meta()
            )

    def test_accept_requires_current_active_spec_and_admitted_evidence(self) -> None:
        args = argparse.Namespace(
            task="AR-1793",
            owner="worker-a",
            expected_revision=7,
            evidence_class="quality",
            evidence_ref="tests/ar1793",
            evidence_digest="sha256:" + "a" * 64,
            note="evidence accepted",
        )
        cases = (
            ("owner", active_meta(owner="worker-b", spec_ref="x", spec_revision=1), "owned by"),
            ("inactive", active_meta(status="open", spec_ref="x", spec_revision=1), "active task"),
            (
                "stale",
                active_meta(spec_ref="x", spec_revision=1, task_revision=8),
                "stale revision",
            ),
        )
        with patch.object(handoffctl, "require_role_admission"):
            for label, meta, message in cases:
                with self.subTest(label=label), self.assertRaisesRegex(RuntimeError, message):
                    handoffctl.apply_accept(args, meta, None)
        best_effort = active_meta()
        with patch.object(handoffctl, "require_role_admission"):
            handoffctl.apply_accept(args, best_effort, None)
        self.assertEqual("best_effort", best_effort["spec_acceptance"]["match"])
        meta = active_meta(spec_ref="x", spec_revision=1)
        with (
            patch.object(handoffctl, "require_role_admission"),
            patch.object(
                predicate_ledger, "done_admission_error", return_value="evidence rejected"
            ),
            self.assertRaisesRegex(RuntimeError, "evidence rejected"),
        ):
            handoffctl.apply_accept(args, meta, None)
        self.assertEqual("pass", meta["spec_acceptance"]["status"])

    def test_recover_expired_restores_current_snapshot_and_rejects_future_session(self) -> None:
        args = argparse.Namespace(task="AR-1793", expected_revision=7, note="lease expired")
        recovered = active_meta(claim_expires="2000-01-01T00:00:00+00:00", claim_process={"pid": 5})
        records = [{"task_revision": 7, "next_action": "Reconcile durable state."}]
        store = MagicMock()
        store.load_session_records.return_value = records
        with (
            patch.object(handoffctl, "storage_backend", return_value=store),
            patch.object(handoffctl, "validate_session_record"),
        ):
            result = handoffctl.apply_recover_expired(args, recovered, [])
        self.assertEqual(
            "Recovered expired claim formerly owned by worker-a. lease expired", result
        )
        self.assertEqual("Reconcile durable state.", recovered["next_action"])
        self.assertEqual("open", recovered["status"])
        self.assertEqual("", recovered["owner"])
        self.assertNotIn("claim_process", recovered)
        future_store = MagicMock()
        future_store.load_session_records.return_value = [
            {"task_revision": 8, "next_action": "bad"}
        ]
        with (
            patch.object(handoffctl, "storage_backend", return_value=future_store),
            patch.object(handoffctl, "validate_session_record"),
            self.assertRaisesRegex(RuntimeError, "newer than the task"),
        ):
            handoffctl.apply_recover_expired(
                args, active_meta(claim_expires="2000-01-01T00:00:00+00:00"), []
            )


class ConsistentReadAndDispatchCoverageTests(unittest.TestCase):
    """Cover bounded observation retries and command-dispatch boundaries."""

    def test_git_doctor_retries_only_stale_live_projection_errors(self) -> None:
        lock = contextlib.nullcontext()
        with (
            patch.object(handoffctl, "published_observation_ticket", side_effect=[1, 2, 2, 2]),
            patch.object(handoffctl, "config", return_value={"github_repository": "owner/repo"}),
            patch.object(handoffctl, "project_binding", return_value={"project_id": "id"}),
            patch.object(handoffctl, "project_scan", return_value={}) as scan,
            patch.object(handoffctl, "locked", return_value=lock),
            patch.object(handoffctl, "backend_selection", return_value={"backend": "git"}),
            patch.object(
                handoffctl,
                "doctor_checks",
                side_effect=[["PROJECT_STATE.md is stale"], []],
            ),
        ):
            self.assertEqual([], handoffctl.git_doctor_checks(live=True))
        self.assertEqual(2, scan.call_count)

    def test_snapshot_retries_ticket_change_then_prints_one_validated_view(self) -> None:
        lock = contextlib.nullcontext()
        printer = MagicMock()
        with (
            patch.object(handoffctl, "backend_selection", return_value={"backend": "git"}),
            patch.object(handoffctl, "CONFIG", MagicMock(exists=MagicMock(return_value=False))),
            patch.object(handoffctl, "published_observation_ticket", side_effect=[3, 4, 4, 4]),
            patch.object(handoffctl, "project_scan", return_value={}) as scan,
            patch.object(handoffctl, "locked", return_value=lock),
            patch.object(handoffctl, "validate", return_value=[]),
            patch.object(handoffctl, "print_snapshot_under_lock", printer),
        ):
            handoffctl.cmd_snapshot("AR-1793")
        self.assertEqual(2, scan.call_count)
        printer.assert_called_once_with("AR-1793", False)

    def test_dispatch_returns_upgrade_result_and_upgrade_requires_binding_before_reads(
        self,
    ) -> None:
        args = argparse.Namespace(cmd="upgrade")
        with patch.object(handoffctl, "cmd_upgrade", return_value=23) as command:
            self.assertEqual(23, handoffctl.dispatch_bound_standard_command(args))
        command.assert_called_once_with(args)
        missing_binding = argparse.Namespace(
            upgrade_action="apply", binding=None, contract=Path("x")
        )
        with (
            patch.object(handoffctl, "backend_selection", return_value={"backend": "git"}),
            self.assertRaisesRegex(RuntimeError, "require --binding"),
        ):
            handoffctl.cmd_upgrade(missing_binding)


class LegacyBindingRepairCoverageTests(unittest.TestCase):
    """Prove the narrow legacy worktree repair preserves every safety fence."""

    def test_repair_legacy_binding_clears_only_the_exact_stale_key(self) -> None:
        args = argparse.Namespace(
            task="AR-1793",
            expected_revision=7,
            expected_branch="codex/ar1793",
            worktree_key="asb-state-ar1793",
            note="rebind to the current isolated worktree",
        )
        meta = {
            "id": "AR-1793",
            "task_revision": 7,
            "status": "open",
            "owner": "",
            "claim_expires": "",
            "branch": "codex/ar1793",
            "worktree_key": args.worktree_key,
        }
        self.assertEqual(
            args.note,
            handoffctl.apply_repair_legacy_binding(args, meta, []),
        )
        self.assertEqual("", meta["worktree_key"])

    def test_repair_legacy_binding_rejects_each_unsafe_state(self) -> None:
        args = argparse.Namespace(
            task="AR-1793",
            expected_revision=7,
            expected_branch="codex/ar1793",
            worktree_key="asb-state-ar1793",
            note="repair",
        )
        base = {
            "id": "AR-1793",
            "task_revision": 7,
            "status": "open",
            "owner": "",
            "claim_expires": "",
            "branch": "codex/ar1793",
            "worktree_key": args.worktree_key,
        }
        cases: tuple[tuple[str, argparse.Namespace, dict[str, object], str], ...] = (
            (
                "stale",
                argparse.Namespace(**{**vars(args), "expected_revision": 8}),
                {},
                "stale revision",
            ),
            ("active", args, {"status": "in_progress", "owner": "worker-a"}, "inactive, unowned"),
            ("leased", args, {"claim_expires": "2999-01-01T00:00:00+00:00"}, "inactive, unowned"),
            ("branch", args, {"branch": "codex/other"}, "branch does not match"),
            ("key", args, {"worktree_key": "other"}, "does not match"),
            (
                "blank-note",
                argparse.Namespace(**{**vars(args), "note": "  "}),
                {},
                "must not be empty",
            ),
        )
        for label, request, changes, message in cases:
            with self.subTest(label=label):
                meta = {**base, **changes}
                before = dict(meta)
                with self.assertRaisesRegex(RuntimeError, message):
                    handoffctl.apply_repair_legacy_binding(request, meta, [])
                self.assertEqual(before, meta)


if __name__ == "__main__":
    unittest.main()
