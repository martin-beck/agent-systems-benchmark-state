# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Durable opt-in receipt intent tests; queued is never completed."""

from __future__ import annotations

import json
import os
import sqlite3
import tempfile
import unittest
import uuid
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from unittest.mock import patch

from tools.fast_receipts import ReceiptConflictError, ReceiptStore


def _independent_enqueue(arguments: tuple[str, str, int]) -> tuple[str, str]:
    path, project_id, worker = arguments
    store = ReceiptStore(Path(path), project_id)
    try:
        receipt = store.enqueue_heartbeat(
            key=f"worker-{worker}:heartbeat",
            task=f"AR-{worker:04d}",
            owner=f"worker-{worker}",
            expected_revision=1,
            lease_minutes=20,
        )
        return str(receipt["receipt_id"]), str(receipt["phase"])
    finally:
        store.close()


def _same_key_enqueue(arguments: tuple[str, str]) -> str:
    path, project_id = arguments
    store = ReceiptStore(Path(path), project_id)
    try:
        receipt = store.enqueue_heartbeat(
            key="shared:heartbeat:1",
            task="AR-0120",
            owner="worker-a",
            expected_revision=1,
            lease_minutes=20,
        )
        return str(receipt["receipt_id"])
    finally:
        store.close()


class FastReceiptTests(unittest.TestCase):
    def setUp(self) -> None:
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.path = Path(self.directory.name) / "private" / "receipts.sqlite3"
        self.project_id = str(uuid.uuid4())

    def store(self) -> ReceiptStore:
        result = ReceiptStore(self.path, self.project_id)
        self.addCleanup(result.close)
        return result

    def submit(self, store: ReceiptStore, **changes: object) -> dict[str, object]:
        fields: dict[str, object] = {
            "key": "worker-a:heartbeat:1",
            "task": "AR-0120",
            "owner": "worker-a",
            "expected_revision": 1,
            "lease_minutes": 20,
        }
        fields.update(changes)
        return store.enqueue_heartbeat(**fields)  # type: ignore[arg-type]

    def test_retry_returns_same_durable_queued_receipt_after_reopen(self) -> None:
        first_store = self.store()
        first = self.submit(first_store)
        self.assertEqual("queued-local", first["phase"])
        self.assertEqual("heartbeat", first["operation"])
        first_store.close()
        reopened = self.store()
        second = self.submit(reopened)
        self.assertEqual(first["receipt_id"], second["receipt_id"])
        self.assertEqual(first, reopened.read(str(first["receipt_id"])))

    def test_same_key_different_input_rejects_without_new_intent(self) -> None:
        store = self.store()
        first = self.submit(store)
        with self.assertRaises(ReceiptConflictError):
            self.submit(store, lease_minutes=21)
        with self.assertRaises(ReceiptConflictError):
            self.submit(store, expected_revision=2)
        self.assertEqual(first, store.read(str(first["receipt_id"])))
        count = store.connection.execute("SELECT count(*) FROM intents").fetchone()[0]
        self.assertEqual(1, count)

    def test_promote_intent_is_canonical_and_conflict_fenced(self) -> None:
        store = self.store()
        first = store.enqueue_promote(
            key="worker-a:promote:1",
            task="AR-0120",
            expected_revision=1,
            note="Dependencies verified.",
        )
        self.assertEqual("promote", first["operation"])
        self.assertEqual("queued-local", first["phase"])
        payload = json.loads(str(first["payload_json"]))
        self.assertEqual(
            {
                "expected_revision": 1,
                "note": "Dependencies verified.",
                "operation": "promote",
                "project_id": self.project_id,
                "task": "AR-0120",
            },
            payload,
        )
        self.assertEqual(
            first["receipt_id"],
            store.enqueue_promote(
                key="worker-a:promote:1",
                task="AR-0120",
                expected_revision=1,
                note="Dependencies verified.",
            )["receipt_id"],
        )
        with self.assertRaises(ReceiptConflictError):
            store.enqueue_promote(
                key="worker-a:promote:1",
                task="AR-0120",
                expected_revision=1,
                note="Changed note.",
            )

    def test_update_intent_is_closed_canonical_and_conflict_fenced(self) -> None:
        store = self.store()
        first = store.enqueue_update(
            key="worker-a:update:1",
            task="AR-0120",
            owner="worker-a",
            expected_revision=1,
            changes={"next_action": "Run the focused test.", "priority": "P1"},
            note="Refined the execution plan.",
        )
        self.assertEqual("update", first["operation"])
        self.assertEqual(
            {
                "changes": {"next_action": "Run the focused test.", "priority": "P1"},
                "expected_revision": 1,
                "note": "Refined the execution plan.",
                "operation": "update",
                "owner": "worker-a",
                "project_id": self.project_id,
                "task": "AR-0120",
            },
            json.loads(str(first["payload_json"])),
        )
        self.assertEqual(
            first["receipt_id"],
            store.enqueue_update(
                key="worker-a:update:1",
                task="AR-0120",
                owner="worker-a",
                expected_revision=1,
                changes={"priority": "P1", "next_action": "Run the focused test."},
                note="Refined the execution plan.",
            )["receipt_id"],
        )
        with self.assertRaises(ReceiptConflictError):
            store.enqueue_update(
                key="worker-a:update:1",
                task="AR-0120",
                owner="worker-a",
                expected_revision=1,
                changes={"priority": "P2"},
                note="Refined the execution plan.",
            )

    def test_update_rejects_empty_nonactive_and_unbounded_changes(self) -> None:
        store = self.store()
        invalid_changes: tuple[dict[str, dict[str, str]], ...] = (
            {"changes": {}},
            {"changes": {"status": "done"}},
            {"changes": {"priority": "invalid"}},
            {"changes": {"owner": "injected"}},
            {"changes": {"summary": "x" * 4001}},
            {"changes": {"summary": "bad\x00value"}},
            {"changes": {"next_action": "x" * 1025}},
            {"changes": {"next_action": "line\nbreak"}},
        )
        for values in invalid_changes:
            with self.subTest(values=values), self.assertRaises(ValueError):
                store.enqueue_update(
                    key="worker-a:update:1",
                    task="AR-0120",
                    owner="worker-a",
                    expected_revision=1,
                    note="Refined.",
                    **values,
                )

    def test_claim_intent_is_canonical_and_conflict_fenced(self) -> None:
        store = self.store()
        first = store.enqueue_claim(
            key="worker-a:claim:1",
            task="AR-0120",
            owner="worker-a",
            expected_revision=1,
            lease_minutes=20,
        )
        self.assertEqual("claim", first["operation"])
        self.assertEqual(
            {
                "expected_revision": 1,
                "lease_minutes": 20,
                "operation": "claim",
                "owner": "worker-a",
                "project_id": self.project_id,
                "task": "AR-0120",
            },
            json.loads(str(first["payload_json"])),
        )
        with self.assertRaises(ReceiptConflictError):
            store.enqueue_claim(
                key="worker-a:claim:1",
                task="AR-0120",
                owner="worker-b",
                expected_revision=1,
                lease_minutes=20,
            )

    def test_claim_identity_is_canonical_and_requires_a_complete_pair(self) -> None:
        store = self.store()
        identity = store.enqueue_claim(
            key="worker-a:claim:identity",
            task="AR-0120",
            owner="worker-a",
            expected_revision=1,
            lease_minutes=20,
            worker_pid=123,
            worker_start_time=456,
        )
        self.assertEqual(
            {"worker_pid": 123, "worker_start_time": 456},
            {
                key: value
                for key, value in json.loads(str(identity["payload_json"])).items()
                if key.startswith("worker_")
            },
        )
        with self.assertRaises(ValueError):
            store.enqueue_claim(
                key="worker-a:claim:incomplete",
                task="AR-0120",
                owner="worker-a",
                expected_revision=1,
                lease_minutes=20,
                worker_pid=123,
            )

    def test_promote_rejects_invalid_note_and_revision_without_row(self) -> None:
        store = self.store()
        for values in (
            {"key": "bad key", "task": "AR-0120", "expected_revision": 1, "note": "note"},
            {
                "key": "worker-a:promote:1",
                "task": "AR-0120",
                "expected_revision": 0,
                "note": "note",
            },
            {"key": "worker-a:promote:1", "task": "AR-0120", "expected_revision": 1, "note": ""},
            {
                "key": "worker-a:promote:1",
                "task": "AR-0120",
                "expected_revision": 1,
                "note": "x" * 4097,
            },
        ):
            with self.subTest(values=values), self.assertRaises(ValueError):
                store.enqueue_promote(**values)  # type: ignore[arg-type]
        self.assertEqual(0, store.connection.execute("SELECT count(*) FROM intents").fetchone()[0])

    def test_invalid_intent_never_creates_row(self) -> None:
        store = self.store()
        for change in (
            {"key": "../escape"},
            {"task": "../foreign"},
            {"owner": "worker with spaces"},
            {"expected_revision": 0},
            {"lease_minutes": 0},
            {"lease_minutes": 1441},
        ):
            with self.subTest(change=change), self.assertRaises(ValueError):
                self.submit(store, **change)
        self.assertEqual(0, store.connection.execute("SELECT count(*) FROM intents").fetchone()[0])

    def test_foreign_project_cannot_open_bound_database(self) -> None:
        store = self.store()
        self.submit(store)
        with self.assertRaisesRegex(RuntimeError, "different project"):
            ReceiptStore(self.path, str(uuid.uuid4()))

    def test_symlinked_database_is_rejected(self) -> None:
        self.path.parent.mkdir(mode=0o700)
        target = self.path.parent / "target"
        target.write_text("not a database")
        self.path.symlink_to(target)
        with self.assertRaisesRegex(RuntimeError, "symlink"):
            ReceiptStore(self.path, self.project_id)

    def test_nonprivate_parent_is_rejected(self) -> None:
        self.path.parent.mkdir(mode=0o777)
        self.path.parent.chmod(0o755)
        with self.assertRaisesRegex(RuntimeError, "not private"):
            ReceiptStore(self.path, self.project_id)

    def test_first_creation_syncs_new_parent_and_database_entries(self) -> None:
        with patch("tools.fast_receipts.os.fsync", wraps=os.fsync) as sync:
            self.store()
        self.assertGreaterEqual(sync.call_count, 3)

    def test_failed_first_directory_sync_never_acknowledges_intent(self) -> None:
        with (
            patch("tools.fast_receipts.os.fsync", side_effect=OSError("sync failed")),
            self.assertRaisesRegex(OSError, "sync failed"),
        ):
            ReceiptStore(self.path, self.project_id)
        self.assertFalse(self.path.exists())
        synced: list[tuple[int, int]] = []
        real_sync = os.fsync

        def record_sync(descriptor: int) -> None:
            info = os.fstat(descriptor)
            synced.append((info.st_dev, info.st_ino))
            real_sync(descriptor)

        with patch("tools.fast_receipts.os.fsync", side_effect=record_sync):
            self.store()
        ancestor = self.path.parent.parent.stat()
        self.assertIn((ancestor.st_dev, ancestor.st_ino), synced)

    def test_existing_hardlink_is_rejected(self) -> None:
        self.path.parent.mkdir(mode=0o700)
        original = self.path.parent / "other"
        original.write_bytes(b"")
        original.chmod(0o600)
        os.link(original, self.path)
        with self.assertRaisesRegex(RuntimeError, "private regular owned"):
            ReceiptStore(self.path, self.project_id)

    def test_database_replacement_is_rejected_before_enqueue(self) -> None:
        store = self.store()
        original = self.path.parent / "original"
        self.path.rename(original)
        self.path.write_bytes(b"replacement")
        self.path.chmod(0o600)
        with self.assertRaisesRegex(RuntimeError, "identity changed"):
            self.submit(store)

    def test_unsafe_wal_sidecar_is_rejected_before_enqueue(self) -> None:
        store = self.store()
        target = self.path.parent / "target"
        target.write_bytes(b"not a wal")
        wal = Path(str(self.path) + "-wal")
        wal.unlink(missing_ok=True)
        wal.symlink_to(target)
        with self.assertRaisesRegex(RuntimeError, "sidecar is unsafe"):
            self.submit(store)

    def test_private_wal_sidecar_replacement_is_detected(self) -> None:
        store = self.store()
        replacement = self.path.parent / "replacement-wal"
        replacement.write_bytes(b"replacement")
        replacement.chmod(0o600)
        replacement.replace(Path(str(self.path) + "-wal"))
        with self.assertRaisesRegex(RuntimeError, "sidecar identity changed"):
            self.submit(store)

    def test_rejects_nonlocal_filesystem_before_database_open(self) -> None:
        with (
            patch(
                "tools.fast_receipts.require_local_filesystem",
                side_effect=RuntimeError("SQLITE_UNSUPPORTED_FILESYSTEM"),
            ),
            self.assertRaisesRegex(RuntimeError, "SQLITE_UNSUPPORTED_FILESYSTEM"),
        ):
            ReceiptStore(self.path, self.project_id)
        self.assertFalse(self.path.exists())

    def test_unsupported_sqlite_and_schema_fail_before_queue_admission(self) -> None:
        with (
            patch("tools.fast_receipts.sqlite3.sqlite_version_info", (3, 36, 0)),
            self.assertRaisesRegex(RuntimeError, "SQLITE_VERSION_UNSUPPORTED"),
        ):
            ReceiptStore(self.path, self.project_id)
        self.assertFalse(self.path.exists())
        self.path.parent.mkdir(mode=0o700)
        with sqlite3.connect(self.path) as connection:
            connection.execute("PRAGMA user_version=2")
        self.path.chmod(0o600)
        with self.assertRaisesRegex(RuntimeError, "unsupported receipt database schema"):
            ReceiptStore(self.path, self.project_id)

    def test_invalid_ids_codes_and_missing_outcomes_fail_closed(self) -> None:
        store = self.store()
        unknown = uuid.uuid4().hex
        with self.assertRaisesRegex(ValueError, "invalid receipt id"):
            store.read("not-an-id")
        with self.assertRaisesRegex(ValueError, "invalid receipt id"):
            store._finish_running("not-an-id", "rejected")
        with self.assertRaisesRegex(ValueError, "invalid rejection code"):
            store.record_rejection(unknown, "bad code")
        with self.assertRaisesRegex(ValueError, "invalid ambiguity code"):
            store.record_ambiguity(unknown, "bad code")
        with self.assertRaisesRegex(ValueError, "invalid observed remote oid"):
            store.record_remote_observation(unknown, "not-an-oid")
        with self.assertRaisesRegex(ValueError, "invalid publication failure code"):
            store.record_publication_failure(unknown, "bad code")
        with self.assertRaisesRegex(RuntimeError, "unknown receipt"):
            store.record_rejection(unknown, "ADMISSION_REJECTED")
        with self.assertRaisesRegex(RuntimeError, "not locally completed"):
            store.record_publication_failure(unknown, "REMOTE_UNAVAILABLE")

    def test_rejects_non_wal_connection(self) -> None:
        memory = sqlite3.connect(":memory:", isolation_level=None)
        with (
            patch("tools.fast_receipts.sqlite3.connect", return_value=memory),
            self.assertRaisesRegex(RuntimeError, "SQLITE_WAL_UNAVAILABLE"),
        ):
            ReceiptStore(self.path, self.project_id)

    def test_sixteen_independent_submitters_preserve_all_intents(self) -> None:
        store = self.store()
        arguments = [(str(self.path), self.project_id, worker) for worker in range(16)]
        with ProcessPoolExecutor(max_workers=16) as executor:
            results = list(executor.map(_independent_enqueue, arguments))
        self.assertEqual(16, len({receipt_id for receipt_id, _ in results}))
        self.assertTrue(all(phase == "queued-local" for _, phase in results))
        count = store.connection.execute("SELECT count(*) FROM intents").fetchone()[0]
        self.assertEqual(16, count)

    def test_cold_sixteen_processes_initialize_one_wal_queue(self) -> None:
        arguments = [(str(self.path), self.project_id, worker) for worker in range(16)]
        with ProcessPoolExecutor(max_workers=16) as executor:
            results = list(executor.map(_independent_enqueue, arguments))
        self.assertEqual(16, len({receipt_id for receipt_id, _ in results}))
        self.assertTrue(all(phase == "queued-local" for _, phase in results))
        with ReceiptStore(self.path, self.project_id) as store:
            count = store.connection.execute("SELECT count(*) FROM intents").fetchone()[0]
        self.assertEqual(16, count)

    def test_hot_open_skips_schema_write_transaction(self) -> None:
        original = self.store()
        queued = self.submit(original)
        original.close()
        with (
            patch.object(ReceiptStore, "_initialize", side_effect=AssertionError("cold init")),
            ReceiptStore(self.path, self.project_id) as reopened,
        ):
            current = reopened.read(str(queued["receipt_id"]))
        assert current is not None
        self.assertEqual("queued-local", current["phase"])

    def test_initialized_queue_without_project_binding_fails_closed(self) -> None:
        original = self.store()
        original.close()
        connection = sqlite3.connect(self.path)
        connection.execute("DELETE FROM receipt_binding")
        connection.commit()
        connection.close()
        with self.assertRaisesRegex(RuntimeError, "no project binding"):
            ReceiptStore(self.path, self.project_id)

    def test_sixteen_independent_retries_share_one_receipt(self) -> None:
        store = self.store()
        arguments = [(str(self.path), self.project_id)] * 16
        with ProcessPoolExecutor(max_workers=16) as executor:
            receipt_ids = list(executor.map(_same_key_enqueue, arguments))
        self.assertEqual(1, len(set(receipt_ids)))
        count = store.connection.execute("SELECT count(*) FROM intents").fetchone()[0]
        self.assertEqual(1, count)

    def test_queued_intent_cannot_be_reported_as_local_commit(self) -> None:
        store = self.store()
        queued = self.submit(store)
        receipt_id = str(queued["receipt_id"])
        with self.assertRaisesRegex(RuntimeError, "not running"):
            store.record_local_commit(receipt_id, "a" * 40, 2)
        current = store.read(receipt_id)
        assert current is not None
        self.assertEqual("queued-local", current["phase"])

    def test_reservation_and_local_commit_are_fenced_and_idempotent(self) -> None:
        store = self.store()
        queued = self.submit(store)
        receipt_id = str(queued["receipt_id"])
        reserved = store.claim_next()
        assert reserved is not None
        self.assertEqual(receipt_id, reserved["receipt_id"])
        self.assertEqual("running", reserved["phase"])
        self.assertIsNone(store.claim_next())
        with self.assertRaisesRegex(ValueError, "revision"):
            store.record_local_commit(receipt_id, "a" * 40, 3)
        with self.assertRaisesRegex(ValueError, "commit evidence"):
            store.record_local_commit(receipt_id, "not-an-oid", 2)
        local = store.record_local_commit(receipt_id, "a" * 40, 2)
        self.assertEqual("completed-local", local["phase"])
        self.assertEqual("a" * 40, local["commit_oid"])
        self.assertEqual(local, store.record_local_commit(receipt_id, "a" * 40, 2))
        with self.assertRaises(ReceiptConflictError):
            store.record_local_commit(receipt_id, "b" * 40, 2)

    def test_rejected_and_ambiguous_outcomes_do_not_become_local(self) -> None:
        store = self.store()
        rejected = self.submit(store, key="rejected")
        store.claim_next()
        rejected_id = str(rejected["receipt_id"])
        self.assertEqual("rejected", store.record_rejection(rejected_id, "STALE_REVISION")["phase"])
        with self.assertRaisesRegex(RuntimeError, "not running"):
            store.record_local_commit(rejected_id, "a" * 40, 2)
        ambiguous = self.submit(store, key="ambiguous")
        store.claim_next()
        ambiguous_id = str(ambiguous["receipt_id"])
        self.assertEqual(
            "ambiguous", store.record_ambiguity(ambiguous_id, "COMMIT_UNKNOWN")["phase"]
        )
        self.assertIsNone(store.claim_next())

    def test_remote_receipt_requires_local_commit_and_exact_observation(self) -> None:
        store = self.store()
        queued = self.submit(store)
        receipt_id = str(queued["receipt_id"])
        with self.assertRaisesRegex(RuntimeError, "no local commit"):
            store.record_remote_observation(receipt_id, "b" * 40)
        store.claim_next()
        store.record_local_commit(receipt_id, "a" * 40, 2)
        self.assertEqual(1, len(store.pending_publication()))
        pending = store.record_publication_failure(receipt_id, "REMOTE_UNAVAILABLE")
        self.assertEqual("completed-local", pending["phase"])
        self.assertEqual("REMOTE_UNAVAILABLE", pending["publication_error"])
        remote = store.record_remote_observation(receipt_id, "b" * 40)
        self.assertEqual("published-remote", remote["phase"])
        self.assertEqual("b" * 40, remote["remote_oid"])
        self.assertIsNotNone(remote["remote_observed_at"])
        self.assertEqual([], store.pending_publication())
        self.assertEqual(remote, store.record_remote_observation(receipt_id, "b" * 40))
        with self.assertRaises(ReceiptConflictError):
            store.record_remote_observation(receipt_id, "c" * 40)


if __name__ == "__main__":
    unittest.main()
