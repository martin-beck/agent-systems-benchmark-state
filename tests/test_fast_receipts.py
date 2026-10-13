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

    def test_v3_queue_migrates_to_publication_schema_without_losing_receipts(self) -> None:
        self.path.parent.mkdir(mode=0o700)
        self.path.parent.chmod(0o700)
        receipt_id = uuid.uuid4().hex
        connection = sqlite3.connect(self.path)
        connection.execute("PRAGMA journal_mode=WAL")
        connection.executescript(
            """CREATE TABLE receipt_binding (
                   singleton INTEGER PRIMARY KEY CHECK (singleton = 1),
                   project_id TEXT NOT NULL
               );
               CREATE TABLE intents (
                   receipt_id TEXT PRIMARY KEY,
                   project_id TEXT NOT NULL,
                   idempotency_key TEXT NOT NULL,
                   operation TEXT NOT NULL,
                   task_id TEXT NOT NULL,
                   expected_revision INTEGER NOT NULL,
                   payload_json TEXT NOT NULL,
                   input_digest TEXT NOT NULL,
                   phase TEXT NOT NULL,
                   started_at TEXT,
                   commit_oid TEXT,
                   result_revision INTEGER,
                   error_code TEXT,
                   remote_oid TEXT,
                   remote_observed_at TEXT,
                   publication_error TEXT,
                   created_at TEXT NOT NULL,
                   UNIQUE(project_id, idempotency_key)
               );"""
        )
        payload = json.dumps({"operation": "heartbeat", "project_id": self.project_id})
        connection.execute(
            "INSERT INTO receipt_binding(singleton, project_id) VALUES (1, ?)",
            (self.project_id,),
        )
        connection.execute(
            """INSERT INTO intents
            (receipt_id, project_id, idempotency_key, operation, task_id, expected_revision,
             payload_json, input_digest, phase, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                receipt_id,
                self.project_id,
                "legacy:heartbeat:1",
                "heartbeat",
                "AR-0120",
                1,
                payload,
                "a" * 64,
                "queued-local",
                "2026-10-11T00:00:00.000Z",
            ),
        )
        connection.execute("PRAGMA user_version=3")
        connection.commit()
        connection.close()
        self.path.chmod(0o600)
        for suffix in ("-wal", "-shm"):
            sidecar = self.path.with_name(self.path.name + suffix)
            if sidecar.exists():
                sidecar.chmod(0o600)
        with ReceiptStore(self.path, self.project_id) as migrated:
            self.assertEqual(5, migrated.connection.execute("PRAGMA user_version").fetchone()[0])
            legacy = migrated.read(receipt_id)
            assert legacy is not None
            self.assertEqual("queued-local", legacy["phase"])
            self.assertEqual("legacy:heartbeat:1", legacy["idempotency_key"])
            tables = {
                row[0]
                for row in migrated.connection.execute(
                    "SELECT name FROM sqlite_master WHERE type='table'"
                ).fetchall()
            }
        self.assertTrue({"publication_jobs", "publication_request_keys"} <= tables)

    def test_incomplete_current_schema_recovers_required_table(self) -> None:
        original = self.store()
        original.close()
        connection = sqlite3.connect(self.path)
        connection.execute("DROP TABLE publication_request_keys")
        connection.commit()
        connection.close()
        with ReceiptStore(self.path, self.project_id) as repaired:
            tables = {
                row[0]
                for row in repaired.connection.execute(
                    "SELECT name FROM sqlite_master WHERE type='table'"
                ).fetchall()
            }
        self.assertIn("publication_request_keys", tables)

    def test_current_schema_with_missing_publication_columns_fails_closed(self) -> None:
        original = self.store()
        original.close()
        connection = sqlite3.connect(self.path)
        connection.execute("DROP TABLE publication_request_keys")
        connection.execute("DROP TABLE publication_jobs")
        connection.execute(
            "CREATE TABLE publication_jobs (job_id TEXT PRIMARY KEY, project_id TEXT NOT NULL)"
        )
        connection.commit()
        connection.close()
        with self.assertRaisesRegex(RuntimeError, "schema is incomplete"):
            ReceiptStore(self.path, self.project_id)

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

    def test_publication_admission_is_candidate_idempotent_and_base_fenced(self) -> None:
        store = self.store()
        first = store.admit_publication(
            key="publisher-a:1", candidate_oid="a" * 40, expected_remote_oid="b" * 40
        )
        self.assertEqual("queued", first["phase"])
        self.assertEqual(
            first,
            store.admit_publication(
                key="publisher-a:1", candidate_oid="a" * 40, expected_remote_oid="b" * 40
            ),
        )
        reused = store.admit_publication(
            key="publisher-b:1", candidate_oid="a" * 40, expected_remote_oid="b" * 40
        )
        self.assertEqual(first["job_id"], reused["job_id"])
        with self.assertRaises(ReceiptConflictError):
            store.admit_publication(
                key="publisher-b:1", candidate_oid="c" * 40, expected_remote_oid="b" * 40
            )
        with self.assertRaises(ReceiptConflictError):
            store.admit_publication(
                key="publisher-a:1", candidate_oid="c" * 40, expected_remote_oid="b" * 40
            )
        with self.assertRaises(ReceiptConflictError):
            store.admit_publication(
                key="publisher-c:1", candidate_oid="a" * 40, expected_remote_oid="c" * 40
            )
        count = store.connection.execute("SELECT count(*) FROM publication_jobs").fetchone()[0]
        self.assertEqual(1, count)

    def test_publication_lookup_claim_and_recovery_reject_bad_or_unknown_inputs(self) -> None:
        store = self.store()
        with self.assertRaises(ValueError):
            store.read_publication("not-a-job")
        with self.assertRaises(ValueError):
            store.publication_for_candidate("not-an-oid")
        self.assertIsNone(store.publication_for_candidate("a" * 40))
        self.assertIsNone(store.read_publication("1" * 32))
        with self.assertRaises(ValueError):
            store.claim_publication("not-a-job", lease="1" * 32)
        with self.assertRaises(ValueError):
            store.claim_publication("1" * 32, lease="not-a-lease")
        self.assertIsNone(store.claim_publication("1" * 32, lease="1" * 32))
        with self.assertRaises(ValueError):
            store.recover_publication("not-a-job", observed_remote_oid="a" * 40)
        with self.assertRaises(ValueError):
            store.recover_publication("1" * 32, observed_remote_oid="not-an-oid")
        with self.assertRaisesRegex(RuntimeError, "unknown publication job"):
            store.recover_publication("1" * 32, observed_remote_oid="a" * 40)

    def test_superseded_resolution_covers_exact_and_invalid_job_states(self) -> None:
        store = self.store()
        with self.assertRaises(ValueError):
            store.resolve_superseded_publication("not-a-job", observed_remote_oid="a" * 40)
        with self.assertRaisesRegex(RuntimeError, "unknown publication job"):
            store.resolve_superseded_publication("1" * 32, observed_remote_oid="a" * 40)
        exact = store.admit_publication(
            key="publisher-a:exact", candidate_oid="a" * 40, expected_remote_oid="b" * 40
        )
        resolved = store.resolve_superseded_publication(
            str(exact["job_id"]), observed_remote_oid="a" * 40
        )
        self.assertEqual("published", resolved["phase"])
        changed = store.admit_publication(
            key="publisher-a:changed", candidate_oid="c" * 40, expected_remote_oid="d" * 40
        )
        rejected = store.resolve_superseded_publication(
            str(changed["job_id"]), observed_remote_oid="e" * 40
        )
        self.assertEqual("REMOTE_BASE_CHANGED", rejected["error_code"])
        with self.assertRaisesRegex(RuntimeError, "not queued"):
            store.resolve_superseded_publication(
                str(changed["job_id"]), observed_remote_oid="e" * 40
            )

    def test_publication_outcome_conflicts_and_terminal_recovery_fail_closed(self) -> None:
        store = self.store()
        admitted = store.admit_publication(
            key="publisher-a:terminal", candidate_oid="a" * 40, expected_remote_oid="b" * 40
        )
        job_id = str(admitted["job_id"])
        with self.assertRaises(ValueError):
            store.finish_publication(job_id, lease="1" * 32, phase="unknown")
        with self.assertRaisesRegex(RuntimeError, "not owned"):
            store.finish_publication(
                job_id, lease="1" * 32, phase="published", observed_remote_oid="a" * 40
            )
        store.claim_publication(job_id, lease="1" * 32)
        store.finish_publication(
            job_id, lease="1" * 32, phase="published", observed_remote_oid="a" * 40
        )
        with self.assertRaises(ReceiptConflictError):
            store.finish_publication(
                job_id, lease="1" * 32, phase="published", observed_remote_oid="b" * 40
            )
        with self.assertRaisesRegex(RuntimeError, "not recoverable"):
            store.recover_publication(job_id, observed_remote_oid="a" * 40)

    def test_publication_transition_races_and_visibility_fail_closed(self) -> None:
        store = self.store()
        admitted = store.admit_publication(
            key="publisher-a:resolve-race", candidate_oid="a" * 40, expected_remote_oid="b" * 40
        )
        job_id = str(admitted["job_id"])
        store.connection.execute(
            """CREATE TRIGGER publication_resolve_race BEFORE UPDATE ON publication_jobs
            WHEN OLD.phase = 'queued' BEGIN SELECT RAISE(IGNORE); END"""
        )
        with self.assertRaisesRegex(RuntimeError, "changed while resolving"):
            store.resolve_superseded_publication(job_id, observed_remote_oid="b" * 40)
        store.connection.execute("DROP TRIGGER publication_resolve_race")
        store.claim_publication(job_id, lease="1" * 32)
        store.connection.execute(
            """CREATE TRIGGER publication_finish_race BEFORE UPDATE ON publication_jobs
            WHEN OLD.phase = 'publishing' BEGIN
                UPDATE publication_jobs SET phase='rejected' WHERE job_id=OLD.job_id;
                SELECT RAISE(IGNORE);
            END"""
        )
        with self.assertRaisesRegex(RuntimeError, "changed while finishing"):
            store.finish_publication(
                job_id, lease="1" * 32, phase="published", observed_remote_oid="a" * 40
            )
        store.connection.execute("DROP TRIGGER publication_finish_race")

    def test_publication_completion_and_recovery_visibility_fail_closed(self) -> None:
        store = self.store()
        admitted = store.admit_publication(
            key="publisher-a:finish-visibility",
            candidate_oid="a" * 40,
            expected_remote_oid="b" * 40,
        )
        job_id = str(admitted["job_id"])
        store.claim_publication(job_id, lease="1" * 32)
        store.connection.execute(
            """CREATE TRIGGER publication_finish_visibility AFTER UPDATE ON publication_jobs
            WHEN NEW.phase = 'published' BEGIN
                DELETE FROM publication_jobs WHERE job_id=NEW.job_id;
            END"""
        )
        with self.assertRaisesRegex(RuntimeError, "outcome was not visible"):
            store.finish_publication(
                job_id, lease="1" * 32, phase="published", observed_remote_oid="a" * 40
            )
        store.connection.execute("DROP TRIGGER publication_finish_visibility")
        ambiguous = store.admit_publication(
            key="publisher-a:recover-visibility",
            candidate_oid="c" * 40,
            expected_remote_oid="d" * 40,
        )
        ambiguous_id = str(ambiguous["job_id"])
        store.claim_publication(ambiguous_id, lease="2" * 32)
        store.finish_publication(
            ambiguous_id, lease="2" * 32, phase="ambiguous", error_code="PUSH_TIMEOUT"
        )
        store.connection.execute(
            """CREATE TRIGGER publication_recover_visibility AFTER UPDATE ON publication_jobs
            WHEN NEW.phase = 'published' BEGIN
                DELETE FROM publication_jobs WHERE job_id=NEW.job_id;
            END"""
        )
        with self.assertRaisesRegex(RuntimeError, "recovery was not visible"):
            store.recover_publication(ambiguous_id, observed_remote_oid="c" * 40)
        store.connection.execute("DROP TRIGGER publication_recover_visibility")

    def test_publication_claim_has_one_owner_and_truthful_terminal_outcome(self) -> None:
        store = self.store()
        admitted = store.admit_publication(
            key="publisher-a:1", candidate_oid="a" * 40, expected_remote_oid="b" * 40
        )
        job_id = str(admitted["job_id"])
        lease = "1" * 32
        claimed = store.claim_publication(job_id, lease=lease)
        assert claimed is not None
        self.assertEqual("publishing", claimed["phase"])
        self.assertEqual(lease, claimed["publisher_lease"])
        self.assertIsNone(store.claim_publication(job_id, lease="2" * 32))
        with self.assertRaisesRegex(RuntimeError, "not owned"):
            store.finish_publication(
                job_id,
                lease="2" * 32,
                phase="published",
                observed_remote_oid="c" * 40,
            )
        with self.assertRaises(ValueError):
            store.finish_publication(job_id, lease=lease, phase="published")
        with self.assertRaises(ValueError):
            store.finish_publication(
                job_id,
                lease=lease,
                phase="published",
                observed_remote_oid="c" * 40,
            )
        finished = store.finish_publication(
            job_id,
            lease=lease,
            phase="published",
            observed_remote_oid="a" * 40,
        )
        self.assertEqual("published", finished["phase"])
        self.assertEqual("a" * 40, finished["observed_remote_oid"])
        self.assertEqual(
            finished,
            store.finish_publication(
                job_id,
                lease=lease,
                phase="published",
                observed_remote_oid="a" * 40,
            ),
        )

    def test_publication_ambiguous_outcome_cannot_be_claimed_or_rewritten(self) -> None:
        store = self.store()
        admitted = store.admit_publication(
            key="publisher-a:1", candidate_oid="a" * 40, expected_remote_oid="b" * 40
        )
        job_id = str(admitted["job_id"])
        lease = "1" * 32
        store.claim_publication(job_id, lease=lease)
        ambiguous = store.finish_publication(
            job_id, lease=lease, phase="ambiguous", error_code="PUSH_TIMEOUT"
        )
        self.assertEqual("ambiguous", ambiguous["phase"])
        self.assertIsNone(store.claim_publication(job_id, lease="2" * 32))
        with self.assertRaises(RuntimeError):
            store.finish_publication(
                job_id,
                lease=lease,
                phase="published",
                observed_remote_oid="c" * 40,
            )

    def test_remote_advanced_rejection_records_the_observed_head(self) -> None:
        store = self.store()
        admitted = store.admit_publication(
            key="publisher-a:1", candidate_oid="a" * 40, expected_remote_oid="b" * 40
        )
        job_id = str(admitted["job_id"])
        lease = "1" * 32
        store.claim_publication(job_id, lease=lease)
        rejected = store.finish_publication(
            job_id,
            lease=lease,
            phase="rejected",
            observed_remote_oid="c" * 40,
            error_code="REMOTE_ADVANCED",
        )
        self.assertEqual("rejected", rejected["phase"])
        self.assertEqual("c" * 40, rejected["observed_remote_oid"])
        self.assertEqual("REMOTE_ADVANCED", rejected["error_code"])

    def test_expired_publication_lease_cannot_report_success(self) -> None:
        store = self.store()
        admitted = store.admit_publication(
            key="publisher-a:1", candidate_oid="a" * 40, expected_remote_oid="b" * 40
        )
        job_id = str(admitted["job_id"])
        lease = "1" * 32
        store.claim_publication(job_id, lease=lease)
        store.connection.execute(
            "UPDATE publication_jobs SET publisher_lease_expires='2000-01-01T00:00:00.000Z' "
            "WHERE job_id=?",
            (job_id,),
        )
        with self.assertRaisesRegex(RuntimeError, "lease has expired"):
            store.finish_publication(
                job_id,
                lease=lease,
                phase="published",
                observed_remote_oid="a" * 40,
            )

    def test_ambiguous_publication_recovers_only_from_a_fresh_exact_observation(self) -> None:
        store = self.store()
        admitted = store.admit_publication(
            key="publisher-a:1", candidate_oid="a" * 40, expected_remote_oid="b" * 40
        )
        job_id = str(admitted["job_id"])
        lease = "1" * 32
        store.claim_publication(job_id, lease=lease)
        store.finish_publication(job_id, lease=lease, phase="ambiguous", error_code="PUSH_TIMEOUT")
        requeued = store.recover_publication(job_id, observed_remote_oid="b" * 40)
        self.assertEqual("queued", requeued["phase"])
        claimed = store.claim_publication(job_id, lease="2" * 32)
        assert claimed is not None
        store.finish_publication(
            job_id, lease="2" * 32, phase="ambiguous", error_code="PUSH_TIMEOUT"
        )
        published = store.recover_publication(job_id, observed_remote_oid="a" * 40)
        self.assertEqual("published", published["phase"])

    def test_recovery_rejects_foreign_head_and_active_lease(self) -> None:
        store = self.store()
        admitted = store.admit_publication(
            key="publisher-a:1", candidate_oid="a" * 40, expected_remote_oid="b" * 40
        )
        job_id = str(admitted["job_id"])
        store.claim_publication(job_id, lease="1" * 32)
        with self.assertRaisesRegex(RuntimeError, "still active"):
            store.recover_publication(job_id, observed_remote_oid="b" * 40)
        store.connection.execute(
            "UPDATE publication_jobs SET publisher_lease_expires='2000-01-01T00:00:00.000Z' "
            "WHERE job_id=?",
            (job_id,),
        )
        rejected = store.recover_publication(job_id, observed_remote_oid="c" * 40)
        self.assertEqual("rejected", rejected["phase"])
        self.assertEqual("REMOTE_BASE_CHANGED", rejected["error_code"])

    def test_receipt_visibility_fences_roll_back_each_partial_persistence_write(self) -> None:
        store = self.store()
        store.connection.execute(
            """CREATE TRIGGER receipt_insert_invisible AFTER INSERT ON intents BEGIN
            DELETE FROM intents WHERE receipt_id=NEW.receipt_id;
            END"""
        )
        with self.assertRaisesRegex(RuntimeError, "insert was not visible"):
            self.submit(store)
        store.connection.execute("DROP TRIGGER receipt_insert_invisible")
        self.assertEqual(0, store.connection.execute("SELECT count(*) FROM intents").fetchone()[0])

        queued = self.submit(store)
        receipt_id = str(queued["receipt_id"])
        store.connection.execute(
            """CREATE TRIGGER receipt_claim_invisible BEFORE UPDATE ON intents
            WHEN OLD.phase = 'queued-local' BEGIN SELECT RAISE(IGNORE); END"""
        )
        with self.assertRaisesRegex(RuntimeError, "reservation was not visible"):
            store.claim_next()
        store.connection.execute("DROP TRIGGER receipt_claim_invisible")
        current = store.read(receipt_id)
        assert current is not None
        self.assertEqual("queued-local", current["phase"])

        store.claim_next()
        store.connection.execute(
            """CREATE TRIGGER receipt_finish_invisible BEFORE UPDATE ON intents
            WHEN OLD.phase = 'running' BEGIN SELECT RAISE(IGNORE); END"""
        )
        with self.assertRaisesRegex(RuntimeError, "outcome was not visible"):
            store.record_local_commit(receipt_id, "a" * 40, 2)
        store.connection.execute("DROP TRIGGER receipt_finish_invisible")
        current = store.read(receipt_id)
        assert current is not None
        self.assertEqual("running", current["phase"])

        local = store.record_local_commit(receipt_id, "a" * 40, 2)
        store.connection.execute(
            """CREATE TRIGGER receipt_remote_invisible AFTER UPDATE ON intents
            WHEN NEW.phase = 'published-remote' BEGIN
            DELETE FROM intents WHERE receipt_id=NEW.receipt_id;
            END"""
        )
        with self.assertRaisesRegex(RuntimeError, "remote receipt was not visible"):
            store.record_remote_observation(receipt_id, "b" * 40)
        store.connection.execute("DROP TRIGGER receipt_remote_invisible")
        self.assertEqual(local, store.read(receipt_id))

    def test_recovery_lists_are_durable_and_exclude_active_or_terminal_publications(self) -> None:
        store = self.store()
        queued = self.submit(store, key="queued")
        running = self.submit(store, key="running")
        first = store.claim_next()
        second = store.claim_next()
        assert first is not None and second is not None
        self.assertEqual(str(queued["receipt_id"]), first["receipt_id"])
        self.assertEqual(str(running["receipt_id"]), second["receipt_id"])
        self.assertEqual(
            [str(queued["receipt_id"]), str(running["receipt_id"])],
            [item["receipt_id"] for item in store.running()],
        )
        store.record_local_commit(str(queued["receipt_id"]), "a" * 40, 2)
        self.assertEqual(
            [str(queued["receipt_id"])],
            [item["receipt_id"] for item in store.pending_publication()],
        )

        queued_job = store.admit_publication(
            key="recovery:queued", candidate_oid="b" * 40, expected_remote_oid="c" * 40
        )
        ambiguous_job = store.admit_publication(
            key="recovery:ambiguous", candidate_oid="d" * 40, expected_remote_oid="e" * 40
        )
        active_job = store.admit_publication(
            key="recovery:active", candidate_oid="f" * 40, expected_remote_oid="0" * 40
        )
        expired_job = store.admit_publication(
            key="recovery:expired", candidate_oid="1" * 40, expected_remote_oid="2" * 40
        )
        terminal_job = store.admit_publication(
            key="recovery:terminal", candidate_oid="3" * 40, expected_remote_oid="4" * 40
        )
        store.claim_publication(str(ambiguous_job["job_id"]), lease="a" * 32)
        store.finish_publication(
            str(ambiguous_job["job_id"]),
            lease="a" * 32,
            phase="ambiguous",
            error_code="PUSH_TIMEOUT",
        )
        store.claim_publication(str(active_job["job_id"]), lease="b" * 32)
        store.claim_publication(str(expired_job["job_id"]), lease="c" * 32)
        store.connection.execute(
            "UPDATE publication_jobs SET publisher_lease_expires='2000-01-01T00:00:00.000Z' "
            "WHERE job_id=?",
            (str(expired_job["job_id"]),),
        )
        store.claim_publication(str(terminal_job["job_id"]), lease="d" * 32)
        store.finish_publication(
            str(terminal_job["job_id"]),
            lease="d" * 32,
            phase="rejected",
            error_code="REMOTE_ADVANCED",
        )
        self.assertEqual(
            {str(queued_job["job_id"]), str(ambiguous_job["job_id"]), str(expired_job["job_id"])},
            {item["job_id"] for item in store.recoverable_publications()},
        )

    def test_publication_visibility_and_recovery_races_leave_no_false_outcome(self) -> None:
        store = self.store()
        store.connection.execute(
            """CREATE TRIGGER publication_admission_invisible AFTER INSERT ON publication_jobs BEGIN
            DELETE FROM publication_jobs WHERE job_id=NEW.job_id;
            END"""
        )
        with self.assertRaisesRegex(RuntimeError, "admission was not visible"):
            store.admit_publication(
                key="visibility:admit", candidate_oid="a" * 40, expected_remote_oid="b" * 40
            )
        store.connection.execute("DROP TRIGGER publication_admission_invisible")
        self.assertEqual(
            0, store.connection.execute("SELECT count(*) FROM publication_jobs").fetchone()[0]
        )

        admitted = store.admit_publication(
            key="visibility:claim", candidate_oid="c" * 40, expected_remote_oid="d" * 40
        )
        job_id = str(admitted["job_id"])
        store.connection.execute(
            """CREATE TRIGGER publication_claim_invisible AFTER UPDATE ON publication_jobs
            WHEN NEW.phase = 'publishing' BEGIN
            DELETE FROM publication_jobs WHERE job_id=NEW.job_id;
            END"""
        )
        with self.assertRaisesRegex(RuntimeError, "claim was not visible"):
            store.claim_publication(job_id, lease="1" * 32)
        store.connection.execute("DROP TRIGGER publication_claim_invisible")
        current = store.read_publication(job_id)
        assert current is not None
        self.assertEqual("queued", current["phase"])

        store.claim_publication(job_id, lease="1" * 32)
        store.connection.execute(
            "UPDATE publication_jobs SET publisher_lease_expires='2000-01-01T00:00:00.000Z' "
            "WHERE job_id=?",
            (job_id,),
        )
        store.connection.execute(
            """CREATE TRIGGER publication_recover_race BEFORE UPDATE ON publication_jobs
            WHEN OLD.phase = 'publishing' BEGIN
            UPDATE publication_jobs SET phase='rejected' WHERE job_id=OLD.job_id;
            SELECT RAISE(IGNORE);
            END"""
        )
        with self.assertRaisesRegex(RuntimeError, "changed while recovering"):
            store.recover_publication(job_id, observed_remote_oid="d" * 40)
        store.connection.execute("DROP TRIGGER publication_recover_race")
        current = store.read_publication(job_id)
        assert current is not None
        self.assertEqual("publishing", current["phase"])

    def test_sidecar_open_failure_closes_initialization_without_admitting_a_store(self) -> None:
        real_open = os.open

        def reject_sidecar(
            path: str | bytes | os.PathLike[str] | os.PathLike[bytes],
            *args: object,
            **kwargs: object,
        ) -> int:
            if os.fsdecode(os.fspath(path)).endswith(("-wal", "-shm")):
                raise OSError("sidecar unavailable")
            return real_open(path, *args, **kwargs)  # type: ignore[arg-type]

        with (
            patch("tools.fast_receipts.os.open", side_effect=reject_sidecar),
            self.assertRaisesRegex(RuntimeError, "WAL sidecar is unavailable"),
        ):
            ReceiptStore(self.path, self.project_id)

    def test_claim_and_update_reject_boolean_and_malformed_inputs_before_enqueue(self) -> None:
        store = self.store()
        invalid_claims = (
            {"expected_revision": 0},
            {"worker_pid": True, "worker_start_time": 1},
            {"worker_pid": 1, "worker_start_time": -1},
        )
        for changes in invalid_claims:
            with (
                self.subTest(changes=changes),
                self.assertRaisesRegex(ValueError, "worker|revision"),
            ):
                claim = {
                    "key": "worker-a:claim:invalid",
                    "task": "AR-0120",
                    "owner": "worker-a",
                    "expected_revision": 1,
                    "lease_minutes": 20,
                }
                claim.update(changes)
                store.enqueue_claim(**claim)  # type: ignore[arg-type]
        for update_changes in (
            {"expected_revision": True},
            {"note": "contains\x00nul"},
            {"owner": "not valid"},
        ):
            with (
                self.subTest(changes=update_changes),
                self.assertRaisesRegex(ValueError, "update receipt"),
            ):
                update = {
                    "key": "worker-a:update:invalid",
                    "task": "AR-0120",
                    "owner": "worker-a",
                    "expected_revision": 1,
                    "changes": {"priority": "P1"},
                    "note": "ordinary note",
                }
                update.update(update_changes)
                store.enqueue_update(**update)  # type: ignore[arg-type]
        self.assertEqual(0, store.connection.execute("SELECT count(*) FROM intents").fetchone()[0])

    def test_publication_admission_and_finish_fail_closed_for_invalid_or_missing_jobs(self) -> None:
        store = self.store()
        for changes in (
            {"key": "invalid key", "candidate_oid": "a" * 40, "expected_remote_oid": "b" * 40},
            {
                "key": "publisher:invalid",
                "candidate_oid": "not-an-oid",
                "expected_remote_oid": "b" * 40,
            },
            {
                "key": "publisher:invalid",
                "candidate_oid": "a" * 40,
                "expected_remote_oid": "a" * 40,
            },
        ):
            with (
                self.subTest(changes=changes),
                self.assertRaisesRegex(ValueError, "publication admission"),
            ):
                store.admit_publication(**changes)
        with self.assertRaisesRegex(RuntimeError, "unknown publication job"):
            store.finish_publication(
                "1" * 32,
                lease="2" * 32,
                phase="rejected",
                error_code="REMOTE_ADVANCED",
            )
        self.assertEqual(
            0, store.connection.execute("SELECT count(*) FROM publication_jobs").fetchone()[0]
        )

    def test_superseded_resolution_visibility_failure_rolls_back_the_outcome(self) -> None:
        store = self.store()
        admitted = store.admit_publication(
            key="visibility:superseded", candidate_oid="a" * 40, expected_remote_oid="b" * 40
        )
        job_id = str(admitted["job_id"])
        store.connection.execute(
            """CREATE TRIGGER publication_resolution_invisible AFTER UPDATE ON publication_jobs
            WHEN NEW.phase = 'rejected' BEGIN
            DELETE FROM publication_jobs WHERE job_id=NEW.job_id;
            END"""
        )
        with self.assertRaisesRegex(RuntimeError, "resolution was not visible"):
            store.resolve_superseded_publication(job_id, observed_remote_oid="c" * 40)
        store.connection.execute("DROP TRIGGER publication_resolution_invisible")
        current = store.read_publication(job_id)
        assert current is not None
        self.assertEqual("queued", current["phase"])

    def test_nonunique_and_nonmatching_indexes_do_not_satisfy_publication_schema(self) -> None:
        store = self.store()
        store.connection.execute("CREATE INDEX intents_task_nonunique ON intents(task_id)")
        self.assertFalse(store._has_unique_index("intents", ("task_id",)))
        self.assertFalse(store._has_unique_index("intents", ("missing_column",)))

    def test_claim_and_private_enqueue_reject_invalid_descriptors_before_writes(self) -> None:
        store = self.store()
        with self.assertRaisesRegex(ValueError, "invalid owner"):
            store.enqueue_claim(
                key="worker-a:claim:bad-owner",
                task="AR-0120",
                owner="owner with spaces",
                expected_revision=1,
                lease_minutes=20,
            )
        with self.assertRaisesRegex(ValueError, "invalid receipt operation"):
            store._enqueue(
                key="worker-a:unknown-operation",
                task="AR-0120",
                expected_revision=1,
                payload={},
            )
        self.assertEqual(0, store.connection.execute("SELECT count(*) FROM intents").fetchone()[0])


if __name__ == "__main__":
    unittest.main()
