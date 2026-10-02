# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Hostile tests for the durable SQLite WAL/SHM lifecycle record."""

from __future__ import annotations

import json
import os
import sqlite3
import tempfile
import unittest
from pathlib import Path
from typing import Any
from unittest import mock

from tools.rollback_control_store import ControlStoreError, SQLiteRollbackControlStore
from tools.sqlite_wal_lifecycle import (
    SIDECAR_SUFFIXES,
    WALLifecycleError,
    WALLifecycleStore,
    _digest,
)

PROJECT = "11111111-1111-4111-8111-111111111111"


class WALLifecycleTests(unittest.TestCase):
    def _store(self, root: Path) -> tuple[WALLifecycleStore, Path]:
        database = root / "control.sqlite"
        database.touch(mode=0o600)
        database.chmod(0o600)
        identity = database.stat()
        record = WALLifecycleStore(
            root / ".control.sqlite.lifecycle.json",
            PROJECT,
            (identity.st_dev, identity.st_ino),
        )
        record.initialize()
        return record, database

    def _sidecars(self, database: Path) -> None:
        for suffix in SIDECAR_SUFFIXES:
            sidecar = Path(f"{database}{suffix}")
            sidecar.write_bytes(b"journal")
            sidecar.chmod(0o600)

    def _write_payload(self, record: WALLifecycleStore, payload: dict[str, Any]) -> None:
        payload["record_digest"] = _digest(
            {key: value for key, value in payload.items() if key != "record_digest"}
        )
        record.path.write_text(json.dumps(payload))
        record.path.chmod(0o600)

    def test_record_schema_and_binding_validation_is_fail_closed(self) -> None:
        variants: list[tuple[dict[str, Any], str]] = [
            ({"schema_version": 99}, "unsupported"),
            ({"project_id": "other"}, "project binding"),
            ({"database_identity": [1, 2]}, "database identity"),
            ({"authority_identity": [3, 4]}, "authority identity"),
            ({"journal_mode": "delete"}, "state is invalid"),
            ({"generation": -1}, "generation is invalid"),
            ({"generation": True}, "generation is invalid"),
            ({"sidecars": []}, "sidecars are invalid"),
            ({"sidecars": {"-wal": None}}, "sidecars are invalid"),
            (
                {"sidecars": {"-wal": {"device": 1, "inode": 2, "size": -1}, "-shm": None}},
                "sidecar identity is invalid",
            ),
            (
                {
                    "state": "absent",
                    "sidecars": {"-wal": {"device": 1, "inode": 2, "size": 3}, "-shm": None},
                },
                "absent WAL lifecycle",
            ),
        ]
        for changes, message in variants:
            with self.subTest(message=message), tempfile.TemporaryDirectory() as directory:
                record, _ = self._store(Path(directory))
                payload = json.loads(record.path.read_text())
                payload.update(changes)
                self._write_payload(record, payload)
                with self.assertRaisesRegex(WALLifecycleError, message):
                    record.validate()

    def test_record_file_and_publication_safety_errors(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            record, _ = self._store(root)
            record.path.chmod(0o644)
            with self.assertRaisesRegex(WALLifecycleError, "unsafe"):
                record.validate()
            record.path.unlink()
            record.path.symlink_to(root / "missing")
            with self.assertRaises(WALLifecycleError):
                record.validate()

            record.path.unlink()
            with (
                mock.patch("tools.sqlite_wal_lifecycle.os.rename", side_effect=OSError("rename")),
                self.assertRaisesRegex(WALLifecycleError, "ambiguous"),
            ):
                record._publish(record._record("absent", 0, dict.fromkeys(SIDECAR_SUFFIXES)))

    def test_missing_and_unsafe_sidecars_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            record, database = self._store(Path(directory))
            parent = os.open(database.parent, os.O_RDONLY | os.O_DIRECTORY)
            try:
                with self.assertRaisesRegex(WALLifecycleError, "unavailable"):
                    record.mark_active(parent, database.name)
                self._sidecars(database)
                Path(f"{database}-wal").unlink()
                Path(f"{database}-wal").symlink_to(database)
                with self.assertRaisesRegex(WALLifecycleError, "unavailable"):
                    record.mark_active(parent, database.name)
            finally:
                os.close(parent)

    def test_invalid_transition_and_initialization_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            record, database = self._store(root)
            with self.assertRaisesRegex(WALLifecycleError, "state is invalid"):
                record._record("unknown", 0, dict.fromkeys(SIDECAR_SUFFIXES))
            parent = os.open(root, os.O_RDONLY | os.O_DIRECTORY)
            try:
                with self.assertRaisesRegex(WALLifecycleError, "requires an active"):
                    record.mark_clean_checkpointed(parent, database.name)
            finally:
                os.close(parent)
            record.initialize()

    def test_authority_identity_is_bound(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            database = root / "control.sqlite"
            database.touch(mode=0o600)
            identity = database.stat()
            record = WALLifecycleStore(
                root / ".lifecycle.json", PROJECT, (identity.st_dev, identity.st_ino), (7, 8)
            )
            record.initialize()
            self.assertEqual([7, 8], record.read()["authority_identity"])

    def test_lifecycle_transitions_bind_sidecars_and_checkpoint(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            record, database = self._store(Path(directory))
            self.assertEqual("absent", record.read()["state"])
            self._sidecars(database)
            parent = os.open(database.parent, os.O_RDONLY | os.O_DIRECTORY)
            try:
                active = record.mark_active(parent, database.name)
                self.assertEqual("active", active["state"])
                self.assertEqual(1, active["generation"])
                self.assertEqual(active, record.mark_active(parent, database.name))
                for suffix in SIDECAR_SUFFIXES:
                    Path(f"{database}{suffix}").unlink()
                clean = record.mark_clean_checkpointed(parent, database.name)
            finally:
                os.close(parent)
            self.assertEqual("clean_checkpointed", clean["state"])
            self.assertEqual(1, clean["generation"])

    def test_active_replacement_requires_reconciliation_permission(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            record, database = self._store(Path(directory))
            self._sidecars(database)
            parent = os.open(database.parent, os.O_RDONLY | os.O_DIRECTORY)
            try:
                record.mark_active(parent, database.name)
                replacement = Path(f"{database}-wal")
                replacement.unlink()
                replacement.write_bytes(b"replacement")
                replacement.chmod(0o600)
                with self.assertRaisesRegex(WALLifecycleError, "identity changed"):
                    record.mark_active(parent, database.name)
                record.mark_active(parent, database.name, allow_rebind=True)
            finally:
                os.close(parent)

    def test_record_tamper_and_impossible_state_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            record, _ = self._store(root)
            payload = json.loads(record.path.read_text())
            payload["state"] = "active"
            record.path.write_text(json.dumps(payload))
            record.path.chmod(0o600)
            with self.assertRaisesRegex(WALLifecycleError, "digest"):
                record.validate()
            payload["record_digest"] = "sha256:" + "0" * 64
            record.path.write_text(json.dumps(payload))
            record.path.chmod(0o600)
            with self.assertRaisesRegex(WALLifecycleError, "digest"):
                record.validate()

    def test_control_store_checkpoint_publishes_clean_lifecycle(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            control = SQLiteRollbackControlStore(root / "control.sqlite", PROJECT)
            control.checkpoint_wal()
            lifecycle = root / ".control.sqlite.lifecycle.json"
            self.assertEqual("clean_checkpointed", json.loads(lifecycle.read_text())["state"])
            with control._connection():
                pass
            self.assertEqual("active", json.loads(lifecycle.read_text())["state"])

    def test_invalid_lifecycle_is_rejected_before_sqlite_schema_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            control = SQLiteRollbackControlStore(root / "control.sqlite", PROJECT)
            payload = json.loads(control._lifecycle.path.read_text())
            payload["state"] = "active"
            control._lifecycle.path.write_text(json.dumps(payload))
            control._lifecycle.path.chmod(0o600)
            with self.assertRaisesRegex(ControlStoreError, "digest"), control._connection():
                pass
            with sqlite3.connect(control.path) as connection:
                tables = connection.execute(
                    "SELECT name FROM sqlite_master WHERE type='table'"
                ).fetchall()
            self.assertEqual([], tables)

    def test_missing_lifecycle_record_is_not_recreated_for_existing_database(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            control = SQLiteRollbackControlStore(root / "control.sqlite", PROJECT)
            with control._connection():
                pass
            lifecycle = control._lifecycle.path
            lifecycle.unlink()
            with (
                self.assertRaisesRegex(ControlStoreError, "lifecycle record is unavailable"),
                control._connection(),
            ):
                pass
            reopened = SQLiteRollbackControlStore(root / "control.sqlite", PROJECT)
            with (
                self.assertRaisesRegex(ControlStoreError, "lifecycle record is unavailable"),
                reopened._connection(),
            ):
                pass

    def test_active_missing_sidecars_requires_explicit_reconciliation(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            control = SQLiteRollbackControlStore(root / "control.sqlite", PROJECT)
            with control.operation_lock(), control._connection():
                pass
            lifecycle = control._lifecycle
            self.assertEqual("active", lifecycle.read()["state"])
            lifecycle._publish(lifecycle._record("active", 1, dict.fromkeys(SIDECAR_SUFFIXES)))
            control.reconcile_wal_lifecycle()
            self.assertEqual("clean_checkpointed", lifecycle.read()["state"])

    def test_control_store_lifecycle_branches_are_fail_closed_and_reconciled(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            control = SQLiteRollbackControlStore(root / "control.sqlite", PROJECT)
            lifecycle = control._lifecycle
            lifecycle._publish(lifecycle._record("active", 1, dict.fromkeys(SIDECAR_SUFFIXES)))
            control.checkpoint_wal()
            self.assertEqual("clean_checkpointed", lifecycle.read()["state"])

            with control.operation_lock():
                with self.assertRaisesRegex(ControlStoreError, "non-reentrant"):
                    control.checkpoint_wal()
                with self.assertRaisesRegex(ControlStoreError, "non-reentrant"):
                    control.reconcile_wal_lifecycle()

            with (
                mock.patch.object(
                    control._lifecycle,
                    "validate",
                    side_effect=WALLifecycleError("injected lifecycle failure"),
                ),
                self.assertRaisesRegex(ControlStoreError, "injected lifecycle"),
            ):
                control.checkpoint_wal()
            with (
                mock.patch.object(
                    control._lifecycle,
                    "validate",
                    side_effect=WALLifecycleError("injected lifecycle failure"),
                ),
                self.assertRaisesRegex(ControlStoreError, "injected lifecycle"),
            ):
                control.reconcile_wal_lifecycle()

            connection = sqlite3.connect(control.path)
            with (
                mock.patch.object(
                    control,
                    "_connection",
                    return_value=connection,
                ),
                mock.patch.object(
                    control,
                    "_sidecar_identities",
                    return_value={"-wal": object(), "-shm": object()},
                ),
                mock.patch.object(control._lifecycle, "mark_active") as mark_active,
            ):
                control.checkpoint_wal()
                control.reconcile_wal_lifecycle()
                self.assertEqual(2, mark_active.call_count)
            connection.close()


if __name__ == "__main__":
    unittest.main()
