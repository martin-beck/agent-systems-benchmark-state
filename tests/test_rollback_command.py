# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Failure-matrix tests for the coordinated rollback command."""

import argparse
import subprocess
import tempfile
import unittest
from contextlib import ExitStack
from pathlib import Path
from typing import Any
from unittest.mock import patch

from tools import handoffctl as core
from tools.checkpoint_records import append_checkpoint, build_checkpoint, load_checkpoints
from tools.rollback_records import append_record, build_record, latest_for_checkpoint


def task() -> dict[str, object]:
    return {
        "id": "AR-0001",
        "task_revision": 3,
        "status": "open",
        "owner": "",
        "claim_expires": "",
        "checkpoint_commit": "",
        "spec_ref": "plans/AR-0001.md",
        "spec_acceptance": {"evidence_ref": "PR-1"},
    }


class RollbackCommandTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.product = self.root / "product"
        self.product.mkdir()
        self.old_root = core.ROOT
        self.old_backend = core.BACKEND_CONFIG
        core.ROOT = self.root
        core.BACKEND_CONFIG = self.root / "coordinator.backend.json"
        core.BACKEND_CONFIG.write_text('{"backend":"git","project_id":"x","schema_version":1}')
        record = build_checkpoint(task(), "body", "a" * 40, "now")
        append_checkpoint(self.root, record)
        self.checkpoint = str(record["name"])

    def tearDown(self) -> None:
        core.ROOT = self.old_root
        core.BACKEND_CONFIG = self.old_backend
        self.temporary.cleanup()

    def args(self) -> argparse.Namespace:
        return argparse.Namespace(checkpoint=self.checkpoint)

    def patches(self, revert: object) -> tuple[Any, ...]:
        revert_patch = (
            patch.object(core, "_revert_product", side_effect=revert)
            if isinstance(revert, BaseException)
            else patch.object(core, "_revert_product", return_value=revert)
        )
        return (
            patch.object(core, "dirty_state_paths", return_value=[]),
            patch.object(
                core, "configured_product_checkout", return_value=(self.root, self.product)
            ),
            patch.object(core, "project_binding", return_value={}),
            patch.object(
                core,
                "all_tasks",
                return_value=[(self.root / "tasks/AR-0001.md", task(), "body")],
            ),
            patch.object(core, "commit", return_value=True),
            patch.object(core, "push_replica"),
            patch.object(core, "_product_commit_for_checkpoint", return_value="b" * 40),
            revert_patch,
            patch.object(core, "mutate"),
            patch.object(core, "reconcile"),
        )

    def test_product_failure_is_durably_ambiguous_and_not_repeatable(self) -> None:
        with (
            self.assertRaisesRegex(RuntimeError, "recovery is required"),
            self._entered(RuntimeError("crash")),
        ):
            core.cmd_rollback(self.args())
        record = latest_for_checkpoint(self.root, self.checkpoint)
        self.assertIsNotNone(record)
        assert record is not None
        self.assertEqual("ambiguous", record["status"])
        with (
            self.assertRaisesRegex(RuntimeError, "explicit ambiguous recovery"),
            self._entered("unused"),
        ):
            core.cmd_rollback(self.args())

    def test_completed_operation_rejects_double_restore(self) -> None:
        with self._entered("c" * 40):
            core.cmd_rollback(self.args())
        record = latest_for_checkpoint(self.root, self.checkpoint)
        self.assertIsNotNone(record)
        assert record is not None
        self.assertEqual("rollback_completed", record["status"])
        with self.assertRaisesRegex(RuntimeError, "already completed"), self._entered("unused"):
            core.cmd_rollback(self.args())

    def test_apply_rollback_restores_checkpoint_metadata_and_clears_claim(self) -> None:
        checkpoint = build_checkpoint(task(), "body", "a" * 40, "now")
        checkpoint["state"]["status"] = "in_progress"
        checkpoint["state"]["summary"] = "checkpoint summary"
        metadata = task()
        metadata.update({"task_revision": 9, "owner": "", "claim_expires": ""})
        arguments = argparse.Namespace(rollback_checkpoint=checkpoint)
        with patch.object(core, "require_role_admission"):
            note = core.apply_rollback(arguments, metadata)
        self.assertEqual("open", metadata["status"])
        self.assertEqual("", metadata["owner"])
        self.assertEqual("checkpoint summary", metadata["summary"])
        self.assertEqual("a" * 40, metadata["checkpoint_commit"])
        self.assertIn("AR-0001-r0003", note)

    def test_product_helpers_reject_dirty_and_non_ancestor_states(self) -> None:
        dirty = subprocess.CompletedProcess([], 0, stdout=" M file\n", stderr="")
        with (
            patch.object(core, "run", return_value=dirty),
            self.assertRaisesRegex(RuntimeError, "clean product"),
        ):
            core._product_commit_for_checkpoint(self.product, "a" * 40)

        clean = [
            subprocess.CompletedProcess([], 0, stdout="", stderr=""),
            subprocess.CompletedProcess([], 0, stdout="", stderr=""),
            subprocess.CompletedProcess([], 0, stdout="a" * 40 + "\n", stderr=""),
        ]
        with patch.object(core, "run", side_effect=clean):
            self.assertEqual("a" * 40, core._product_commit_for_checkpoint(self.product, "a" * 40))
        outputs = [
            subprocess.CompletedProcess([], 0, stdout="", stderr=""),
            subprocess.CompletedProcess([], 0, stdout="", stderr=""),
            subprocess.CompletedProcess([], 0, stdout="b" * 40 + "\n", stderr=""),
            subprocess.CompletedProcess([], 1, stdout="", stderr=""),
        ]
        with (
            patch.object(core, "run", side_effect=outputs),
            self.assertRaisesRegex(RuntimeError, "not an ancestor"),
        ):
            core._product_commit_for_checkpoint(self.product, "a" * 40)

    def test_product_revert_commits_the_inverse_range(self) -> None:
        outputs = [
            subprocess.CompletedProcess([], 0, stdout="", stderr=""),
            subprocess.CompletedProcess([], 0, stdout="", stderr=""),
            subprocess.CompletedProcess([], 0, stdout="c" * 40 + "\n", stderr=""),
        ]
        with patch.object(core, "run", side_effect=outputs) as mocked:
            self.assertEqual("c" * 40, core._revert_product(self.product, "a" * 40, "b" * 40))
        self.assertEqual(3, mocked.call_count)

    def test_apply_rollback_rejects_active_or_mismatched_checkpoint(self) -> None:
        checkpoint = build_checkpoint(task(), "body", "a" * 40, "now")
        args = argparse.Namespace(rollback_checkpoint=checkpoint)
        with self.assertRaisesRegex(RuntimeError, "active claim"):
            core.apply_rollback(args, {**task(), "owner": "worker"})
        wrong = {**task(), "id": "AR-0002"}
        with self.assertRaisesRegex(RuntimeError, "does not match"):
            core.apply_rollback(args, wrong)

    def test_product_revert_noop_and_journal_commit_failure(self) -> None:
        self.assertEqual("a" * 40, core._revert_product(self.product, "a" * 40, "a" * 40))
        record = build_checkpoint(task(), "body", "a" * 40, "now")
        operation = build_record(record, "b" * 40, "now")
        with (
            patch.object(core, "append_record"),
            patch.object(core, "commit", return_value=False),
            self.assertRaisesRegex(RuntimeError, "journal state was not committed"),
        ):
            core._rollback_commit(self.root, operation, "planned")

    def test_state_publication_failure_is_ambiguous(self) -> None:
        with (
            self._entered("c" * 40),
            patch.object(core, "mutate", side_effect=RuntimeError("state")),
            self.assertRaisesRegex(RuntimeError, "recovery is required"),
        ):
            core.cmd_rollback(self.args())

    def test_reconcile_authorizes_completion_at_recorded_rollback_head(self) -> None:
        with (
            self._entered("c" * 40),
            patch.object(core, "mutate", side_effect=RuntimeError("state")),
            self.assertRaisesRegex(RuntimeError, "recovery is required"),
        ):
            core.cmd_rollback(self.args())
        arguments = self.args()
        arguments.reconcile = True
        with (
            self._entered("c" * 40),
            patch.object(core, "_product_commit_for_checkpoint", return_value="c" * 40),
        ):
            core.cmd_rollback(arguments)
        record = latest_for_checkpoint(self.root, self.checkpoint)
        self.assertIsNotNone(record)
        assert record is not None
        self.assertEqual("rollback_completed", record["status"])

    def test_reconcile_rejects_changed_product_heads(self) -> None:
        checkpoint = build_checkpoint(task(), "body", "a" * 40, "now")
        previous = build_record(
            checkpoint,
            "b" * 40,
            "now",
            status="ambiguous",
            rollback_commit="c" * 40,
        )
        arguments = argparse.Namespace(reconcile=True)
        with self.assertRaisesRegex(RuntimeError, "does not match rollback commit"):
            core._start_rollback(arguments, checkpoint, self.product, "b" * 40, previous)
        previous = build_record(checkpoint, "b" * 40, "now", status="ambiguous")
        with self.assertRaisesRegex(RuntimeError, "changed during ambiguous"):
            core._start_rollback(arguments, checkpoint, self.product, "c" * 40, previous)

    def test_restore_started_requires_explicit_reconcile(self) -> None:
        checkpoint = load_checkpoints(self.root)[0]
        previous = build_record(checkpoint, "b" * 40, "now", status="restore_started")
        append_record(self.root, previous)
        with (
            patch("tools.handoffctl.load_checkpoints", return_value=[checkpoint]),
            patch.object(core, "latest_for_checkpoint", return_value=previous),
            patch.object(core, "dirty_state_paths", return_value=[]),
            patch.object(core, "project_binding", return_value={}),
            patch.object(
                core, "configured_product_checkout", return_value=(self.root, self.product)
            ),
            patch.object(core, "_product_commit_for_checkpoint", return_value="b" * 40),
            self.assertRaisesRegex(RuntimeError, "explicit ambiguous recovery"),
        ):
            core._rollback_target(argparse.Namespace(checkpoint=self.checkpoint))

    def test_rollback_rejects_unsupported_backend_dirty_state_and_unknown_ref(self) -> None:
        with (
            patch.object(core, "backend_selection", return_value={"backend": "sqlite"}),
            self.assertRaisesRegex(RuntimeError, "Git authority"),
        ):
            core.cmd_rollback(self.args())
        with (
            patch.object(core, "dirty_state_paths", return_value=["dirty"]),
            self.assertRaisesRegex(RuntimeError, "clean state"),
        ):
            core.cmd_rollback(argparse.Namespace(checkpoint="AR-0001-r9999"))
        with (
            patch.object(core, "dirty_state_paths", return_value=[]),
            self.assertRaisesRegex(RuntimeError, "unknown checkpoint"),
        ):
            core.cmd_rollback(argparse.Namespace(checkpoint="AR-0001-r9999"))

    def _entered(self, revert: object) -> ExitStack:
        patches = self.patches(revert)
        stack = ExitStack()
        for item in patches:
            stack.enter_context(item)
        return stack


if __name__ == "__main__":
    unittest.main()
