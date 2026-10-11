# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""ASB-owned negative coverage for fast receipt durability and publication."""

from __future__ import annotations

import json
import os
import stat
import tempfile
import unittest
import uuid
from pathlib import Path
from typing import Any
from unittest.mock import MagicMock, patch

from tools import fast_receipt_worker as worker
from tools.fast_receipts import ReceiptConflictError, ReceiptStore, validate_update_changes


class FastReceiptInputCoverageTests(unittest.TestCase):
    def test_update_change_validator_rejects_typed_and_control_character_inputs(self) -> None:
        invalid: tuple[object, ...] = (
            None,
            [],
            {"status": 1},
            {"priority": "P5"},
            {"summary": ""},
            {"next_action": "contains\x00nul"},
        )
        for changes in invalid:
            with (
                self.subTest(changes=changes),
                self.assertRaisesRegex(ValueError, "invalid fast update changes"),
            ):
                validate_update_changes(changes)

    def test_worker_rejects_noncanonical_update_intent_before_mutation(self) -> None:
        payload = {
            "changes": {"priority": "P1"},
            "expected_revision": 1,
            "note": "Bounded update.",
            "operation": "update",
            "owner": "worker-a",
            "project_id": str(uuid.uuid4()),
            "task": "AR-1793",
        }
        text = json.dumps(payload, sort_keys=True, separators=(",", ":"))
        intent: dict[str, Any] = {
            "payload_json": text + " ",
            "input_digest": "0" * 64,
            "project_id": payload["project_id"],
            "task_id": payload["task"],
            "expected_revision": 1,
        }
        with self.assertRaisesRegex(RuntimeError, "canonical typed fields"):
            worker._validated_intent(intent)


class ReceiptStoreGuardCoverageTests(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.store = ReceiptStore(
            Path(temporary.name) / "private" / "fast-receipts.sqlite3", str(uuid.uuid4())
        )
        self.addCleanup(self.store.close)

    def test_remote_observation_refuses_a_conflicting_retry(self) -> None:
        queued = self.store.enqueue_heartbeat(
            key="worker-a:heartbeat:1",
            task="AR-1793",
            owner="worker-a",
            expected_revision=1,
            lease_minutes=20,
        )
        receipt_id = str(queued["receipt_id"])
        self.store.claim_next()
        self.store.record_local_commit(receipt_id, "a" * 40, 2)
        self.store.record_remote_observation(receipt_id, "b" * 40)
        with self.assertRaisesRegex(ReceiptConflictError, "another observation"):
            self.store.record_remote_observation(receipt_id, "c" * 40)

    def test_sidecar_guard_rejects_a_nonprivate_file(self) -> None:
        unsafe_sidecar = os.stat_result(
            (stat.S_IFREG | 0o604, 1, 1, 1, os.geteuid(), 0, 0, 0, 0, 0)
        )

        with (
            patch("tools.fast_receipts.os.stat", return_value=unsafe_sidecar),
            self.assertRaisesRegex(RuntimeError, "sidecar is unsafe"),
        ):
            self.store._assert_sidecars()


class PublicationRecoveryCoverageTests(unittest.TestCase):
    def test_timeout_marks_local_receipt_then_allows_a_later_remote_retry(self) -> None:
        receipt_id = "a" * 32
        local = {"receipt_id": receipt_id, "phase": "completed-local"}
        timeout_result = {**local, "publication_error": "PUBLICATION_TIMEOUT"}
        remote_result = {"receipt_id": receipt_id, "phase": "published-remote"}
        store = MagicMock()
        store.pending_publication.return_value = [local]
        store.read.return_value = local
        store.record_publication_failure.return_value = timeout_result
        core = MagicMock()
        core.SubprocessTimeoutError = TimeoutError
        with (
            patch.object(worker, "_require_bound_store"),
            patch.object(worker, "_publish_selected", side_effect=TimeoutError("bounded")),
        ):
            self.assertEqual([timeout_result], worker.publish_pending(core, store))
        store.record_publication_failure.assert_called_once_with(receipt_id, "PUBLICATION_TIMEOUT")
        with (
            patch.object(worker, "_require_bound_store"),
            patch.object(worker, "_publish_selected", return_value=[remote_result]) as publish,
        ):
            self.assertEqual([remote_result], worker.publish_pending(core, store))
        publish.assert_called_once_with(core, store, [local])


if __name__ == "__main__":
    unittest.main()
