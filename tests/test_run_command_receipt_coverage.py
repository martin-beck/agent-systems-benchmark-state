# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Focused failure-path coverage for command completion and receipts."""

from __future__ import annotations

import argparse
import unittest

from tools import execution_receipt, run_command


class _Diffs:
    def diff_bytes(self, _root: object) -> int:
        return 17


class _Runtime:
    ROOT = object()
    PostCommandReconcileError = type("PostCommandReconcileError", (RuntimeError,), {})

    def __init__(
        self,
        *,
        execution_id: str | None = None,
        timed_out: bool = False,
        returncode: int = 0,
        append_error: bool = False,
        reconcile_error: bool = False,
        fence_error: bool = False,
    ) -> None:
        self.execution_id = execution_id
        self.timed_out = timed_out
        self.returncode = returncode
        self.append_error = append_error
        self.reconcile_error = reconcile_error
        self.fence_error = fence_error
        self.revision = 7
        self.calls: list[str] = []
        self.al = _Diffs()

    def _cmd_run_fenced(
        self, _args: argparse.Namespace
    ) -> tuple[object, str, float, bool, int, str | None, int]:
        if self.fence_error:
            raise RuntimeError("fence failed")
        return (
            object(),
            "a" * 64,
            2.5,
            self.timed_out,
            self.returncode,
            self.execution_id,
            self.revision,
        )

    def release_envelope_worktree(self, _args: argparse.Namespace) -> None:
        self.calls.append("release")

    def now(self) -> str:
        return "2026-10-13T12:00:00+00:00"

    def locate(self, _task: str) -> tuple[None, dict[str, int], str]:
        return None, {"task_revision": self.revision}, ""

    def mutate(self, args: argparse.Namespace, kind: str, _policy: object) -> None:
        self.calls.append(kind)
        if kind == "retry-circuit-resolve":
            self.retry_failure = args.retry_circuit_failure
        if kind == "autonomy-limits-record":
            self.autonomy = (
                args.autonomy_returncode,
                args.autonomy_diff_bytes,
                args._autonomy_limits_phase,
            )
        if kind in {"update", "execution-finish"}:
            self.update = args
        self.revision += 1

    def append_command_result(self, *_args: object) -> None:
        self.calls.append("journal")
        if self.append_error:
            raise OSError("journal unavailable")

    def backend_selection(self) -> dict[str, str]:
        return {"backend": "git"}

    def require_policy_unchanged(self, _root: object, _policy: object) -> None:
        self.calls.append("policy")

    def reconcile(self, **kwargs: object) -> None:
        self.calls.append("reconcile")
        self.reconcile_kwargs = kwargs
        if self.reconcile_error:
            raise OSError("push rejected")


def _args(**extra: object) -> argparse.Namespace:
    values: dict[str, object] = {"task": "AR-0001", "owner": "worker", "command": ["true"]}
    values.update(extra)
    return argparse.Namespace(**values)


class RunCommandCoverageTests(unittest.TestCase):
    def test_fence_failure_still_releases_worktree(self) -> None:
        runtime = _Runtime(fence_error=True)
        with self.assertRaisesRegex(RuntimeError, "fence failed"):
            run_command.cmd_run(runtime, _args())
        self.assertEqual(["release"], runtime.calls)

    def test_retry_requires_resolution_revision_and_records_timeout_classification(self) -> None:
        missing = _Runtime(returncode=75)
        with self.assertRaisesRegex(RuntimeError, "missing its resolution revision"):
            run_command.cmd_run(missing, _args(retry_circuit_reservation="r"))
        self.assertEqual(["release"], missing.calls)

        runtime = _Runtime(timed_out=True, returncode=124)
        arguments = _args(retry_circuit_reservation="r", retry_circuit_resolution_revision=7)
        self.assertEqual(124, run_command.cmd_run(runtime, arguments))
        self.assertEqual("SUBPROCESS_TIMEOUT", runtime.retry_failure)
        self.assertIn("deadline=2.5s", runtime.update.note)

    def test_autonomy_recording_and_git_reconcile_use_the_current_revision(self) -> None:
        runtime = _Runtime(returncode=75)
        arguments = _args(autonomy_limits_policy=object())
        self.assertEqual(75, run_command.cmd_run(runtime, arguments))
        self.assertEqual((75, 17, "record"), runtime.autonomy)
        self.assertTrue(runtime.reconcile_kwargs["do_commit"])
        self.assertTrue(runtime.reconcile_kwargs["push"])

    def test_bound_journal_and_reconcile_failures_are_explicit(self) -> None:
        journal = _Runtime(execution_id="b" * 32, append_error=True)
        with self.assertRaisesRegex(RuntimeError, "EXECUTION_RESULT_UNKNOWN"):
            run_command.cmd_run(journal, _args())
        self.assertEqual(["release", "execution-result", "journal"], journal.calls)

        reconciliation = _Runtime(reconcile_error=True)
        with self.assertRaisesRegex(
            _Runtime.PostCommandReconcileError, "COMMAND_RECORDED_POST_RECONCILE_FAILED"
        ):
            run_command.cmd_run(reconciliation, _args())


class ExecutionReceiptCoverageTests(unittest.TestCase):
    def test_valid_and_matches_reject_malformed_identity_and_timestamps(self) -> None:
        reservation = {
            "execution_id": "a" * 32,
            "owner": "worker",
            "envelope_digest": "sha256:" + "b" * 64,
            "argv_digest": "c" * 64,
        }
        arguments = argparse.Namespace(
            execution_id="a" * 32,
            owner="worker",
            classification="EXIT",
            returncode=0,
            recorded_at="2026-10-13T12:00:00Z",
        )
        receipt = execution_receipt.build(reservation, arguments)
        self.assertTrue(execution_receipt.valid(receipt))
        self.assertTrue(execution_receipt.matches(reservation, receipt))
        self.assertFalse(execution_receipt.valid([receipt]))
        self.assertFalse(execution_receipt.valid({**receipt, "recorded_at": "not-a-time"}))
        self.assertFalse(execution_receipt.valid({**receipt, "returncode": True}))
        self.assertFalse(execution_receipt.matches({**reservation, "owner": "other"}, receipt))

    def test_build_rejects_reservation_identity_mismatch(self) -> None:
        reservation = {
            "execution_id": "a" * 32,
            "owner": "worker",
            "envelope_digest": "sha256:" + "b" * 64,
            "argv_digest": "c" * 64,
        }
        arguments = argparse.Namespace(
            execution_id="d" * 32,
            owner="worker",
            classification="EXIT",
            returncode=0,
            recorded_at="2026-10-13T12:00:00+00:00",
        )
        with self.assertRaisesRegex(ValueError, "reservation no longer matches"):
            execution_receipt.build(reservation, arguments)
        arguments.execution_id = "a" * 32
        arguments.owner = "other"
        with self.assertRaisesRegex(ValueError, "owner does not match"):
            execution_receipt.build(reservation, arguments)

    def test_build_rejects_invalid_terminal_result(self) -> None:
        reservation = {
            "execution_id": "a" * 32,
            "owner": "worker",
            "envelope_digest": "sha256:" + "b" * 64,
            "argv_digest": "c" * 64,
        }
        arguments = argparse.Namespace(
            execution_id="a" * 32,
            owner="worker",
            classification="NOT_A_RESULT",
            returncode=0,
            recorded_at="2026-10-13T12:00:00+00:00",
        )
        with self.assertRaisesRegex(ValueError, "invalid execution result"):
            execution_receipt.build(reservation, arguments)
