# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Negative-path tests for online SQLite backup and restore."""

from __future__ import annotations

import importlib.util
import multiprocessing
import os
import signal
import sqlite3
import unittest
from contextlib import closing
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import cast
from unittest.mock import MagicMock, patch

from tools.lifecycle_session import _issue
from tools.sqlite_authority_adapter import SQLiteAuthorityAdapter

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("sqlite_backup", ROOT / "tools/sqlite_backup.py")
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
BackupError = MODULE.BackupError
backup_database = MODULE.backup_database
restore_database = MODULE.restore_database
write_manifest = MODULE.write_manifest

BINDING = {
    "project_id": "11111111-1111-4111-8111-111111111111",
    "state_repository": "owner/state",
    "product_repository": "owner/product",
}


def create_database(path: Path, *, body: str = "before") -> None:
    connection = sqlite3.connect(path)
    connection.executescript(
        """
        CREATE TABLE metadata(key TEXT PRIMARY KEY, value TEXT NOT NULL);
        CREATE TABLE records(id INTEGER PRIMARY KEY, body TEXT NOT NULL);
        """
    )
    connection.executemany(
        "INSERT INTO metadata VALUES (?, ?)",
        [
            ("schema_version", "1"),
            ("backend", "sqlite"),
            ("project_id", BINDING["project_id"]),
            ("state_repository", BINDING["state_repository"]),
            ("product_repository", BINDING["product_repository"]),
            ("state", "active"),
        ],
    )
    connection.execute("INSERT INTO records(body) VALUES (?)", (body,))
    connection.commit()
    connection.close()


def _backup_then_crash_after_replace(source: str, destination: str) -> None:
    """Kill the worker after atomic replacement and before directory fsync."""

    def crash(_directory: Path) -> None:
        os.kill(os.getpid(), signal.SIGKILL)

    with patch.object(MODULE, "_fsync_directory", side_effect=crash):
        MODULE._install(Path(source), Path(destination), BINDING)


def _manifest_then_crash_before_directory_fsync(path: str, manifest: dict[str, object]) -> None:
    """Kill after manifest replacement and before its directory durability barrier."""

    def crash(_directory: Path) -> None:
        os.kill(os.getpid(), signal.SIGKILL)

    with patch.object(MODULE, "_fsync_directory", side_effect=crash):
        write_manifest(Path(path), manifest)


def _restore_then_crash_after_replace(
    backup: str, destination: str, manifest: dict[str, object]
) -> None:
    """Kill after verified restore replacement and before directory fsync."""

    def crash(_directory: Path) -> None:
        os.kill(os.getpid(), signal.SIGKILL)

    with patch.object(MODULE, "_fsync_directory", side_effect=crash):
        restore_database(Path(backup), Path(destination), manifest, BINDING, quiesced=True)


def _write_then_crash_with_wal(path: str, ready: str) -> None:
    connection = sqlite3.connect(path)
    try:
        connection.execute("PRAGMA journal_mode=WAL")
        connection.execute("BEGIN IMMEDIATE")
        connection.execute("UPDATE records SET body='uncommitted' WHERE id=1")
        Path(ready).write_text("ready\n", encoding="utf-8")
        os.kill(os.getpid(), signal.SIGKILL)
    finally:  # pragma: no cover - process is deliberately killed
        connection.close()


class SQLiteBackupTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.source = self.root / "source.sqlite3"
        create_database(self.source)

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def test_online_backup_manifest_and_restore_round_trip(self) -> None:
        backup = self.root / "backup.sqlite3"
        manifest = backup_database(self.source, backup, BINDING)
        self.assertTrue(manifest["wal_consistent"])
        destination = self.root / "restored.sqlite3"
        restore_database(backup, destination, manifest, BINDING, quiesced=True)
        with closing(sqlite3.connect(destination)) as connection:
            self.assertEqual("before", connection.execute("SELECT body FROM records").fetchone()[0])
        manifest_path = self.root / "backup-manifest.json"
        write_manifest(manifest_path, manifest)
        self.assertIn('"kind": "sqlite-online-backup"', manifest_path.read_text())

    def test_adapter_bound_wrappers_and_foreign_session_reject(self) -> None:
        """Legacy functions remain compatibility-only when no session is supplied."""
        self.source.chmod(0o600)
        adapter = SQLiteAuthorityAdapter(self.source)
        backup = self.root / "bound-backup.sqlite3"
        manifest = adapter.backup_bound(backup, BINDING)
        adapter.restore_bound(backup, self.root / "bound-restored.sqlite3", manifest, BINDING)
        foreign_path = self.root / "foreign.sqlite3"
        foreign_path.touch(mode=0o600)
        foreign = SQLiteAuthorityAdapter(foreign_path)
        with self.assertRaises(BackupError):
            MODULE.backup_database(
                self.source,
                self.root / "foreign-backup.sqlite3",
                BINDING,
                session=foreign.lifecycle_session(),
                owner=adapter,
            )

    def test_bound_restore_rejects_same_byte_backup_symlink_before_install(self) -> None:
        self.source.chmod(0o600)
        adapter = SQLiteAuthorityAdapter(self.source)
        backup = self.root / "bound-backup.sqlite3"
        manifest = adapter.backup_bound(backup, BINDING)
        original = self.root / "original-backup.sqlite3"
        original_integrity = MODULE._integrity

        def replace_after_integrity(path: Path, binding: dict[str, object]) -> None:
            original_integrity(path, binding)
            backup.rename(original)
            backup.symlink_to(original)

        destination = self.root / "bound-restored.sqlite3"
        with (
            patch.object(MODULE, "_integrity", side_effect=replace_after_integrity),
            self.assertRaisesRegex(BackupError, "changed before install"),
        ):
            MODULE.restore_database(
                backup,
                destination,
                manifest,
                BINDING,
                quiesced=True,
                session=_issue(adapter, backup),
                owner=adapter,
            )
        self.assertFalse(destination.exists())
        self.assertFalse(list(self.root.glob(".coordinator-*")))

    def test_fresh_restore_fault_then_retry_preserves_verified_sqlite_lifecycle(self) -> None:
        backup = self.root / "backup.sqlite3"
        manifest = backup_database(self.source, backup, BINDING)
        with closing(sqlite3.connect(self.source)) as connection:
            source_dump = list(connection.iterdump())
        manifest_snapshot = dict(manifest)
        destination = self.root / "fresh.sqlite3"
        with (
            patch.object(Path, "replace", side_effect=OSError("publication interrupted")),
            self.assertRaisesRegex(BackupError, "online SQLite backup or installation failed"),
        ):
            restore_database(backup, destination, manifest, BINDING, quiesced=True)
        self.assertFalse(destination.exists())
        self.assertFalse(list(self.root.glob(".coordinator-*")))
        self.assertEqual(manifest_snapshot, manifest)
        restore_database(backup, destination, manifest, BINDING, quiesced=True)
        with closing(sqlite3.connect(destination)) as connection:
            self.assertEqual(source_dump, list(connection.iterdump()))

    def test_fresh_clone_restore_preserves_verified_sqlite_authority_equivalence(self) -> None:
        """A clean restore preserves the verified authority view, not just bytes."""
        source_digest = MODULE._digest(self.source)
        with closing(sqlite3.connect(self.source)) as connection:
            source_schema = list(
                connection.execute(
                    "SELECT type, name, tbl_name, sql FROM sqlite_master "
                    "WHERE name NOT LIKE 'sqlite_%' ORDER BY type, name"
                )
            )
            source_rows = list(connection.execute("SELECT key, value FROM metadata ORDER BY key"))
            source_records = list(connection.execute("SELECT id, body FROM records ORDER BY id"))

        backup = self.root / "backup.sqlite3"
        manifest = backup_database(self.source, backup, BINDING)
        verified_manifest = MODULE.verify_backup(backup, manifest, BINDING)
        destination = self.root / "fresh-clone" / "authority.sqlite3"
        restore_database(backup, destination, verified_manifest, BINDING, quiesced=True)

        self.assertEqual(source_digest, MODULE._digest(self.source))
        self.assertEqual(manifest["database_sha256"], MODULE._digest(destination))
        with closing(sqlite3.connect(destination)) as connection:
            self.assertEqual(
                source_schema,
                list(
                    connection.execute(
                        "SELECT type, name, tbl_name, sql FROM sqlite_master "
                        "WHERE name NOT LIKE 'sqlite_%' ORDER BY type, name"
                    )
                ),
            )
            self.assertEqual(
                source_rows,
                list(connection.execute("SELECT key, value FROM metadata ORDER BY key")),
            )
            self.assertEqual(
                source_records,
                list(connection.execute("SELECT id, body FROM records ORDER BY id")),
            )
        self.assertFalse(Path(str(destination) + "-wal").exists())
        self.assertFalse(Path(str(destination) + "-shm").exists())
        self.assertFalse(list(destination.parent.glob(".coordinator-*")))

    def test_restore_requires_quiescence_and_refuses_existing_backup(self) -> None:
        backup = self.root / "backup.sqlite3"
        manifest = backup_database(self.source, backup, BINDING)
        with self.assertRaises(BackupError):
            restore_database(
                backup, self.root / "restored.sqlite3", manifest, BINDING, quiesced=False
            )
        with self.assertRaises(BackupError):
            backup_database(self.source, backup, BINDING)

    def test_restore_rejects_live_destination_sidecars(self) -> None:
        backup = self.root / "backup.sqlite3"
        manifest = backup_database(self.source, backup, BINDING)
        (self.root / "restored.sqlite3-wal").write_bytes(b"live")
        with self.assertRaises(BackupError):
            restore_database(
                backup, self.root / "restored.sqlite3", manifest, BINDING, quiesced=True
            )

    def test_restore_clears_checkpointed_stale_sidecars(self) -> None:
        backup = self.root / "backup.sqlite3"
        manifest = backup_database(self.source, backup, BINDING)
        destination = self.root / "restored.sqlite3"
        create_database(destination, body="stale")
        ready = self.root / "writer.ready"
        process = multiprocessing.get_context("fork").Process(
            target=_write_then_crash_with_wal,
            args=(str(destination), str(ready)),
        )
        process.start()
        for _ in range(100):
            if ready.exists():
                break
            process.join(0.05)
        process.join(timeout=10)
        self.assertEqual(-signal.SIGKILL, process.exitcode)

        restore_database(backup, destination, manifest, BINDING, quiesced=True)

        self.assertFalse(Path(str(destination) + "-wal").exists())
        self.assertFalse(Path(str(destination) + "-shm").exists())
        with closing(sqlite3.connect(destination)) as connection:
            self.assertEqual("before", connection.execute("SELECT body FROM records").fetchone()[0])

    def test_invalid_restore_does_not_recover_destination_sidecars(self) -> None:
        backup = self.root / "backup.sqlite3"
        manifest = backup_database(self.source, backup, BINDING)
        destination = self.root / "restored.sqlite3"
        create_database(destination, body="stale")
        ready = self.root / "writer.ready"
        process = multiprocessing.get_context("fork").Process(
            target=_write_then_crash_with_wal,
            args=(str(destination), str(ready)),
        )
        process.start()
        for _ in range(100):
            if ready.exists():
                break
            process.join(0.05)
        process.join(timeout=10)
        self.assertEqual(-signal.SIGKILL, process.exitcode)
        invalid = dict(manifest)
        invalid["database_sha256"] = "0" * 64

        with self.assertRaises(BackupError):
            restore_database(backup, destination, invalid, BINDING, quiesced=True)

        self.assertTrue(Path(str(destination) + "-wal").exists())
        self.assertTrue(Path(str(destination) + "-shm").exists())

    def test_restore_rejects_hard_linked_sidecar(self) -> None:
        backup = self.root / "backup.sqlite3"
        manifest = backup_database(self.source, backup, BINDING)
        destination = self.root / "restored.sqlite3"
        create_database(destination, body="stale")
        sidecar_source = self.root / "sidecar-source"
        sidecar_source.write_bytes(b"")
        os.link(sidecar_source, Path(str(destination) + "-wal"))

        with self.assertRaisesRegex(BackupError, "unsafe"):
            restore_database(backup, destination, manifest, BINDING, quiesced=True)

        self.assertTrue(sidecar_source.exists())

    def test_restore_rejects_broken_symlink_sidecar(self) -> None:
        backup = self.root / "backup.sqlite3"
        manifest = backup_database(self.source, backup, BINDING)
        destination = self.root / "restored.sqlite3"
        create_database(destination, body="stale")
        sidecar = Path(str(destination) + "-wal")
        sidecar.symlink_to(self.root / "missing-sidecar")

        with self.assertRaisesRegex(BackupError, "unsafe"):
            restore_database(backup, destination, manifest, BINDING, quiesced=True)

        self.assertTrue(sidecar.is_symlink())

    def test_sidecar_cleanup_rejects_identity_and_filesystem_failures(self) -> None:
        sidecar = self.root / "authority.sqlite3-wal"
        sidecar.write_bytes(b"")
        identity = MODULE._sidecar_identity(sidecar, "sidecar")
        assert identity is not None
        parent = MODULE._parent_identity(sidecar)

        with self.assertRaisesRegex(BackupError, "parent identity"):
            MODULE._remove_sidecar(sidecar, identity, (0, 0))
        with self.assertRaisesRegex(BackupError, "sidecar identity"):
            MODULE._remove_sidecar(sidecar, (0, 0), parent)
        with (
            patch.object(MODULE.os, "open", side_effect=OSError("open failed")),
            self.assertRaisesRegex(BackupError, "failed to remove"),
        ):
            MODULE._remove_sidecar(sidecar, identity, parent)
        with (
            patch.object(MODULE.os, "unlink", side_effect=OSError("unlink failed")),
            self.assertRaisesRegex(BackupError, "failed to remove"),
        ):
            MODULE._remove_sidecar(sidecar, identity, parent)
        with (
            patch.object(MODULE.os, "unlink", side_effect=FileNotFoundError),
            self.assertRaisesRegex(BackupError, "disappeared"),
        ):
            MODULE._remove_sidecar(sidecar, identity, parent)

    def test_recovery_rejects_checkpoint_errors_and_cleanup_failures(self) -> None:
        backup = self.root / "backup.sqlite3"
        backup_database(self.source, backup, BINDING)
        destination = self.root / "restored.sqlite3"
        create_database(destination, body="stale")
        sidecar = Path(str(destination) + "-wal")
        sidecar.write_bytes(b"")

        with (
            patch.object(MODULE.sqlite3, "connect", side_effect=sqlite3.Error("open failed")),
            self.assertRaisesRegex(BackupError, "could not checkpoint"),
        ):
            MODULE._recover_checkpointed_sidecars(destination)

        class CheckpointConnection:
            def execute(self, _statement: str) -> CheckpointConnection:
                return self

            def fetchone(self) -> tuple[int, int, int]:
                return (0, 0, 0)

            def close(self) -> None:
                pass

        with (
            patch.object(MODULE.sqlite3, "connect", return_value=CheckpointConnection()),
            patch.object(MODULE, "_remove_sidecar", side_effect=BackupError("cleanup failed")),
            self.assertRaisesRegex(BackupError, "cleanup failed"),
        ):
            MODULE._recover_checkpointed_sidecars(destination)

        with (
            patch.object(MODULE.sqlite3, "connect", return_value=CheckpointConnection()),
            patch.object(MODULE, "_remove_sidecar", side_effect=OSError("cleanup failed")),
            self.assertRaisesRegex(BackupError, "failed to remove checkpointed"),
        ):
            MODULE._recover_checkpointed_sidecars(destination)

    def test_sqlite_backup_rejects_path_identity_and_publication_races(self) -> None:
        unavailable = MagicMock()
        unavailable.parent.stat.side_effect = OSError("parent unavailable")
        with self.assertRaisesRegex(BackupError, "parent is unavailable"):
            MODULE._parent_identity(unavailable)

        source = MagicMock()
        source.exists.return_value = True
        source.is_symlink.return_value = False
        source.is_file.return_value = True
        source.stat.side_effect = OSError("source disappeared")
        with self.assertRaisesRegex(BackupError, "source database disappeared"):
            MODULE._source_identity(source)

        mock_destination = MagicMock()
        mock_destination.exists.return_value = True
        mock_destination.is_symlink.return_value = False
        mock_destination.is_file.return_value = True
        mock_destination.stat.side_effect = OSError("destination disappeared")
        with self.assertRaisesRegex(BackupError, "existing destination disappeared"):
            MODULE._destination_identity(mock_destination)

        manifest = MagicMock()
        manifest.exists.return_value = True
        manifest.is_symlink.return_value = False
        manifest.is_file.return_value = True
        manifest.stat.side_effect = OSError("manifest disappeared")
        with self.assertRaisesRegex(BackupError, "existing SQLite manifest disappeared"):
            MODULE._manifest_identity(manifest)

        sidecar = MagicMock()
        sidecar.lstat.side_effect = OSError("sidecar unavailable")
        with self.assertRaisesRegex(BackupError, "sidecar metadata is unavailable"):
            MODULE._sidecar_identity(sidecar, "sidecar")

        destination = self.root / "destination.sqlite3"
        destination.write_bytes(b"destination")
        wal = Path(str(destination) + "-wal")
        wal.write_bytes(b"")

        with patch.object(MODULE.sqlite3, "connect") as connect:
            connection = connect.return_value
            connection.execute.return_value.fetchone.return_value = (1, 0, 0)
            with self.assertRaisesRegex(BackupError, "checkpointed destination"):
                MODULE._recover_checkpointed_sidecars(destination)

        destination.unlink()
        wal.unlink()
        create_database(destination)
        wal.write_bytes(b"")
        with (
            patch.object(MODULE.sqlite3, "connect") as connect,
            patch.object(MODULE, "_parent_identity", side_effect=[(1, 1), (2, 2)]),
            self.assertRaisesRegex(BackupError, "parent identity changed"),
        ):
            connect.return_value.execute.return_value.fetchone.return_value = (0, 0, 0)
            MODULE._recover_checkpointed_sidecars(destination)

    def test_sqlite_backup_rejects_install_and_manifest_races(self) -> None:
        destination = self.root / "destination.sqlite3"
        with (
            patch.object(MODULE.tempfile, "mkstemp", side_effect=OSError("no temp file")),
            self.assertRaisesRegex(BackupError, "allocate temporary"),
        ):
            MODULE._install(self.source, destination, BINDING)

        backup = self.root / "backup.sqlite3"
        manifest = backup_database(self.source, backup, BINDING)
        with (
            patch.object(MODULE, "_backup_identity", side_effect=[(1, 1), (2, 2)]),
            self.assertRaisesRegex(BackupError, "changed during verification"),
        ):
            MODULE.verify_backup(backup, manifest, BINDING)

        manifest_path = self.root / "manifest.json"
        with (
            patch.object(MODULE, "_manifest_identity", side_effect=[None, (1, 1)]),
            self.assertRaisesRegex(BackupError, "manifest changed"),
        ):
            write_manifest(manifest_path, manifest)

    def test_verify_rejects_live_backup_sidecars(self) -> None:
        backup = self.root / "backup.sqlite3"
        manifest = backup_database(self.source, backup, BINDING)
        (self.root / "backup.sqlite3-wal").write_bytes(b"live")
        with self.assertRaisesRegex(BackupError, "backup database has live WAL sidecars"):
            MODULE.verify_backup(backup, manifest, BINDING)
        (self.root / "backup.sqlite3-wal").unlink()

    def test_verify_rejects_backup_replacement_during_integrity(self) -> None:
        backup = self.root / "backup.sqlite3"
        manifest = backup_database(self.source, backup, BINDING)
        replacement_source = self.root / "replacement-source.sqlite3"
        create_database(replacement_source, body="replacement")
        replacement = self.root / "replacement.sqlite3"
        backup_database(replacement_source, replacement, BINDING)
        original = self.root / "original-backup.sqlite3"
        original_integrity = MODULE._integrity

        def replace_after_integrity(path: Path, binding: dict[str, object]) -> None:
            original_integrity(path, binding)
            if path == backup:
                backup.rename(original)
                backup.symlink_to(replacement)

        with (
            patch.object(MODULE, "_integrity", side_effect=replace_after_integrity),
            self.assertRaisesRegex(BackupError, "backup database"),
        ):
            MODULE.verify_backup(backup, manifest, BINDING)
        self.assertFalse(list(self.root.glob(".coordinator-*")))

    def test_manifest_unknown_fields_fail_closed(self) -> None:
        backup = self.root / "backup.sqlite3"
        manifest = backup_database(self.source, backup, BINDING)
        manifest["extra"] = True
        with self.assertRaises(BackupError):
            restore_database(
                backup, self.root / "restored.sqlite3", manifest, BINDING, quiesced=True
            )

    def test_failed_replace_preserves_existing_destination(self) -> None:
        backup = self.root / "backup.sqlite3"
        manifest = backup_database(self.source, backup, BINDING)
        destination = self.root / "restored.sqlite3"
        create_database(destination, body="known-good")
        with (
            patch.object(Path, "replace", side_effect=OSError("replace failed")),
            self.assertRaises(BackupError),
        ):
            restore_database(backup, destination, manifest, BINDING, quiesced=True)
        with closing(sqlite3.connect(destination)) as connection:
            self.assertEqual(
                "known-good", connection.execute("SELECT body FROM records").fetchone()[0]
            )

    def test_process_death_after_backup_replace_reopens_complete_destination(self) -> None:
        destination = self.root / "restored.sqlite3"
        create_database(destination, body="known-good")
        process = multiprocessing.get_context("fork").Process(
            target=_backup_then_crash_after_replace,
            args=(str(self.source), str(destination)),
        )
        process.start()
        process.join(timeout=10)
        self.assertEqual(-signal.SIGKILL, process.exitcode)
        self.assertFalse(process.is_alive())
        MODULE._integrity(destination, BINDING)
        with closing(sqlite3.connect(destination)) as connection:
            self.assertEqual("before", connection.execute("SELECT body FROM records").fetchone()[0])

    def test_process_death_after_manifest_replace_reopens_verified_control(self) -> None:
        backup = self.root / "backup.sqlite3"
        manifest = backup_database(self.source, backup, BINDING)
        manifest_path = self.root / "backup-manifest.json"
        process = multiprocessing.get_context("fork").Process(
            target=_manifest_then_crash_before_directory_fsync,
            args=(str(manifest_path), manifest),
        )
        process.start()
        process.join(timeout=10)
        self.assertEqual(-signal.SIGKILL, process.exitcode)
        self.assertFalse(process.is_alive())
        reopened = MODULE.json.loads(manifest_path.read_text(encoding="utf-8"))
        MODULE._validate_manifest(reopened)
        self.assertEqual(manifest["database_sha256"], reopened["database_sha256"])

    def test_ambiguous_restore_reopens_and_idempotently_retries(self) -> None:
        backup = self.root / "backup.sqlite3"
        manifest = backup_database(self.source, backup, BINDING)
        destination = self.root / "restored.sqlite3"
        create_database(destination, body="known-good")
        process = multiprocessing.get_context("fork").Process(
            target=_restore_then_crash_after_replace,
            args=(str(backup), str(destination), manifest),
        )
        process.start()
        process.join(timeout=10)
        self.assertEqual(-signal.SIGKILL, process.exitcode)
        self.assertFalse(process.is_alive())
        MODULE._integrity(destination, BINDING)
        self.assertEqual(manifest["database_sha256"], MODULE._digest(destination))
        restore_database(backup, destination, manifest, BINDING, quiesced=True)
        MODULE._integrity(destination, BINDING)
        self.assertEqual(manifest["database_sha256"], MODULE._digest(destination))

    def test_failed_directory_fsync_restores_existing_destination(self) -> None:
        backup = self.root / "backup.sqlite3"
        manifest = backup_database(self.source, backup, BINDING)
        destination = self.root / "restored.sqlite3"
        create_database(destination, body="known-good")
        with (
            patch.object(MODULE, "_fsync_directory", side_effect=[OSError("fsync failed"), None]),
            self.assertRaises(BackupError),
        ):
            restore_database(backup, destination, manifest, BINDING, quiesced=True)
        with closing(sqlite3.connect(destination)) as connection:
            self.assertEqual(
                "known-good", connection.execute("SELECT body FROM records").fetchone()[0]
            )

    def test_cleanup_failure_is_reported_fail_closed(self) -> None:
        backup = self.root / "backup.sqlite3"
        with (
            patch.object(MODULE, "_unlink", side_effect=BackupError("cleanup failed")),
            self.assertRaises(BackupError),
        ):
            backup_database(self.source, backup, BINDING)
        self.assertTrue(backup.exists())

    def test_atomic_manifest_replace_and_fsync_failures_are_reported(self) -> None:
        backup = self.root / "backup.sqlite3"
        manifest = backup_database(self.source, backup, BINDING)
        manifest_path = self.root / "manifest.json"
        with (
            patch.object(MODULE, "_fsync_directory", side_effect=OSError("fsync failed")),
            self.assertRaises(BackupError),
        ):
            write_manifest(manifest_path, manifest)

    def test_manifest_tampering_and_corruption_fail_closed(self) -> None:
        backup = self.root / "backup.sqlite3"
        manifest = backup_database(self.source, backup, BINDING)
        manifest["database_sha256"] = "0" * 64
        with self.assertRaises(BackupError):
            restore_database(
                backup, self.root / "restored.sqlite3", manifest, BINDING, quiesced=True
            )
        backup.write_bytes(b"not sqlite")
        with self.assertRaises(BackupError):
            restore_database(
                backup, self.root / "restored.sqlite3", manifest, BINDING, quiesced=True
            )

    def test_binding_mismatch_fails_before_backup(self) -> None:
        wrong = dict(BINDING, project_id="22222222-2222-4222-8222-222222222222")
        with self.assertRaises(BackupError):
            backup_database(self.source, self.root / "backup.sqlite3", wrong)

    def test_malformed_source_and_corrupt_backup_fail_closed(self) -> None:
        malformed = self.root / "malformed.sqlite3"
        sqlite3.connect(malformed).close()
        with self.assertRaises(BackupError):
            backup_database(malformed, self.root / "backup.sqlite3", BINDING)
        with self.assertRaises(BackupError):
            MODULE._integrity(self.root / "missing.sqlite3", BINDING)

    def test_foreign_key_integrity_failure_is_rejected(self) -> None:
        invalid = self.root / "invalid.sqlite3"
        with closing(sqlite3.connect(invalid)) as connection, connection:
            connection.executescript(
                "CREATE TABLE metadata(key TEXT PRIMARY KEY, value TEXT NOT NULL);"
                "CREATE TABLE parent(id INTEGER PRIMARY KEY);"
                "CREATE TABLE child(parent_id INTEGER REFERENCES parent(id));"
            )
            connection.executemany(
                "INSERT INTO metadata VALUES (?, ?)",
                [
                    ("schema_version", "1"),
                    ("backend", "sqlite"),
                    ("project_id", BINDING["project_id"]),
                    ("state_repository", BINDING["state_repository"]),
                    ("product_repository", BINDING["product_repository"]),
                    ("state", "active"),
                ],
            )
            connection.execute("INSERT INTO child VALUES (99)")
        with self.assertRaises(BackupError):
            MODULE._integrity(invalid, BINDING)

    def test_cleanup_and_preservation_failures_are_normalized(self) -> None:
        with (
            patch.object(Path, "unlink", side_effect=OSError("unlink failed")),
            self.assertRaises(BackupError),
        ):
            MODULE._unlink(self.root / "temporary.sqlite3")
        destination = self.root / "restored.sqlite3"
        create_database(destination, body="known-good")
        with (
            patch.object(MODULE.os, "link", side_effect=OSError("link failed")),
            self.assertRaises(BackupError),
        ):
            MODULE._backup_existing(destination)

    def test_restore_failure_is_classified_as_ambiguous(self) -> None:
        destination = self.root / "restored.sqlite3"
        previous = self.root / "previous.sqlite3"
        previous.write_bytes(b"known-good")
        with (
            patch.object(Path, "replace", side_effect=OSError("restore failed")),
            self.assertRaisesRegex(BackupError, "authority restore was ambiguous"),
        ):
            MODULE._restore_existing(destination, previous)

    def test_manifest_verification_claims_are_strict(self) -> None:
        backup = self.root / "backup.sqlite3"
        manifest = backup_database(self.source, backup, BINDING)
        manifest["wal_consistent"] = False
        with self.assertRaisesRegex(BackupError, "invalid verification claims"):
            write_manifest(self.root / "manifest.json", manifest)

    def test_failed_install_without_prior_destination_removes_new_authority(self) -> None:
        backup = self.root / "backup.sqlite3"
        manifest = backup_database(self.source, backup, BINDING)
        destination = self.root / "restored.sqlite3"
        with (
            patch.object(MODULE, "_fsync_directory", side_effect=OSError("fsync failed")),
            self.assertRaises(BackupError),
        ):
            restore_database(backup, destination, manifest, BINDING, quiesced=True)
        self.assertFalse(destination.exists())

    def test_source_symlink_is_rejected(self) -> None:
        link = self.root / "source-link.sqlite3"
        link.symlink_to(self.source)
        with self.assertRaises(BackupError):
            backup_database(link, self.root / "backup.sqlite3", BINDING)

    def test_symlinked_destination_parent_is_rejected_before_install(self) -> None:
        real_parent = self.root / "real-parent"
        real_parent.mkdir()
        linked_parent = self.root / "linked-parent"
        linked_parent.symlink_to(real_parent, target_is_directory=True)
        with self.assertRaisesRegex(BackupError, "parent must not contain symlinks"):
            backup_database(self.source, linked_parent / "backup.sqlite3", BINDING)

        backup = self.root / "backup.sqlite3"
        manifest = backup_database(self.source, backup, BINDING)
        destination = linked_parent / "restored.sqlite3"
        with self.assertRaisesRegex(BackupError, "parent must not contain symlinks"):
            restore_database(backup, destination, manifest, BINDING, quiesced=True)
        self.assertFalse((real_parent / "restored.sqlite3").exists())

    def test_symlinked_manifest_parent_is_rejected_before_publication(self) -> None:
        backup = self.root / "backup.sqlite3"
        manifest = backup_database(self.source, backup, BINDING)
        real_parent = self.root / "manifest-parent"
        real_parent.mkdir()
        linked_parent = self.root / "manifest-link"
        linked_parent.symlink_to(real_parent, target_is_directory=True)
        with self.assertRaisesRegex(BackupError, "parent must not contain symlinks"):
            write_manifest(linked_parent / "manifest.json", manifest)
        self.assertFalse((real_parent / "manifest.json").exists())

    def test_parent_identity_drift_fails_before_sqlite_publication(self) -> None:
        backup = self.root / "backup.sqlite3"
        manifest = backup_database(self.source, backup, BINDING)
        destination = self.root / "restored.sqlite3"
        with (
            patch.object(MODULE, "_parent_identity", side_effect=[(1, 1), (1, 2)]),
            self.assertRaisesRegex(BackupError, "parent identity changed"),
        ):
            restore_database(backup, destination, manifest, BINDING, quiesced=True)
        self.assertFalse(destination.exists())
        manifest_path = self.root / "manifest.json"
        with (
            patch.object(MODULE, "_parent_identity", side_effect=[(1, 1), (1, 2)]),
            self.assertRaisesRegex(BackupError, "parent identity changed"),
        ):
            write_manifest(manifest_path, manifest)
        self.assertFalse(manifest_path.exists())

    def test_existing_destination_swap_during_preservation_fails_closed(self) -> None:
        backup = self.root / "backup.sqlite3"
        manifest = backup_database(self.source, backup, BINDING)
        destination = self.root / "restored.sqlite3"
        create_database(destination, body="preserved")
        original = self.root / "original-destination.sqlite3"
        foreign = self.root / "foreign.sqlite3"
        create_database(foreign, body="foreign")
        original_link = MODULE.os.link
        swapped = False

        def swap_before_link(source: Path, target: Path) -> None:
            nonlocal swapped
            if not swapped:
                swapped = True
                destination.rename(original)
                destination.symlink_to(foreign)
            original_link(source, target)

        with (
            patch.object(MODULE.os, "link", side_effect=swap_before_link),
            self.assertRaisesRegex(BackupError, "existing destination"),
        ):
            restore_database(backup, destination, manifest, BINDING, quiesced=True)
        with closing(sqlite3.connect(original)) as connection:
            self.assertEqual(
                "preserved", connection.execute("SELECT body FROM records").fetchone()[0]
            )
        with closing(sqlite3.connect(foreign)) as connection:
            self.assertEqual(
                "foreign", connection.execute("SELECT body FROM records").fetchone()[0]
            )
        self.assertTrue(destination.is_symlink())
        self.assertFalse(list(self.root.glob(".coordinator-*")))
        destination.unlink()
        restore_database(backup, destination, manifest, BINDING, quiesced=True)
        with closing(sqlite3.connect(destination)) as connection:
            self.assertEqual("before", connection.execute("SELECT body FROM records").fetchone()[0])

    def test_destination_creation_before_publication_fails_closed(self) -> None:
        backup = self.root / "backup.sqlite3"
        manifest = backup_database(self.source, backup, BINDING)
        destination = self.root / "restored.sqlite3"
        original_backup_existing = MODULE._backup_existing
        swapped = False

        def create_before_publish(path: Path) -> Path | None:
            nonlocal swapped
            previous = cast(Path | None, original_backup_existing(path))
            if not swapped:
                swapped = True
                create_database(destination, body="attacker")
            return previous

        with (
            patch.object(MODULE, "_backup_existing", side_effect=create_before_publish),
            self.assertRaisesRegex(BackupError, "existing destination"),
        ):
            restore_database(backup, destination, manifest, BINDING, quiesced=True)
        with closing(sqlite3.connect(destination)) as connection:
            self.assertEqual(
                "attacker", connection.execute("SELECT body FROM records").fetchone()[0]
            )
        self.assertFalse(list(self.root.glob(".coordinator-*")))

    def test_real_destination_swap_at_publication_boundary_fails_closed(self) -> None:
        backup = self.root / "backup.sqlite3"
        manifest = backup_database(self.source, backup, BINDING)
        destination = self.root / "restored.sqlite3"
        create_database(destination, body="preserved")
        original = self.root / "original-destination.sqlite3"
        foreign = self.root / "foreign.sqlite3"
        create_database(foreign, body="foreign")

        def swap_at_boundary(_path: Path) -> None:
            destination.rename(original)
            destination.symlink_to(foreign)

        with (
            patch.object(MODULE, "_before_destination_publish", side_effect=swap_at_boundary),
            self.assertRaisesRegex(BackupError, "existing destination"),
        ):
            restore_database(backup, destination, manifest, BINDING, quiesced=True)
        with closing(sqlite3.connect(original)) as connection:
            self.assertEqual(
                "preserved", connection.execute("SELECT body FROM records").fetchone()[0]
            )
        with closing(sqlite3.connect(foreign)) as connection:
            self.assertEqual(
                "foreign", connection.execute("SELECT body FROM records").fetchone()[0]
            )
        self.assertTrue(destination.is_symlink())
        self.assertFalse(list(self.root.glob(".coordinator-*")))

    def test_real_manifest_swap_at_publication_boundary_fails_closed(self) -> None:
        backup = self.root / "backup.sqlite3"
        manifest = backup_database(self.source, backup, BINDING)
        path = self.root / "manifest.json"
        write_manifest(path, manifest)
        original = self.root / "original-manifest.json"
        foreign = self.root / "foreign-manifest.json"
        write_manifest(foreign, manifest)

        def swap_at_boundary(_path: Path) -> None:
            path.rename(original)
            path.symlink_to(foreign)

        with (
            patch.object(MODULE, "_before_manifest_publish", side_effect=swap_at_boundary),
            self.assertRaisesRegex(BackupError, "existing SQLite manifest"),
        ):
            write_manifest(path, manifest)
        self.assertTrue(path.is_symlink())
        self.assertTrue(original.is_file())
        self.assertTrue(foreign.is_file())
        self.assertFalse(list(self.root.glob(".coordinator-manifest-*")))
        path.unlink()
        write_manifest(path, manifest)
        self.assertEqual(path.read_text(encoding="utf-8"), (original).read_text(encoding="utf-8"))

    def test_parent_swap_before_existing_destination_preservation_is_safe(self) -> None:
        backup = self.root / "backup.sqlite3"
        manifest = backup_database(self.source, backup, BINDING)
        parent = self.root / "destination-parent"
        parent.mkdir()
        destination = parent / "restored.sqlite3"
        create_database(destination, body="preserved")
        moved = self.root / "moved-parent"
        redirect = self.root / "redirect-parent"
        redirect.mkdir()
        original_identity = MODULE._parent_identity
        calls = 0

        def swap_after_copy(path: Path) -> tuple[int, int]:
            nonlocal calls
            calls += 1
            identity = cast(tuple[int, int], original_identity(path))
            if calls == 3:
                parent.rename(moved)
                parent.symlink_to(redirect, target_is_directory=True)
                return cast(tuple[int, int], original_identity(path))
            return identity

        with (
            patch.object(MODULE, "_parent_identity", side_effect=swap_after_copy),
            self.assertRaisesRegex(BackupError, "parent identity changed"),
        ):
            restore_database(backup, destination, manifest, BINDING, quiesced=True)
        with closing(sqlite3.connect(moved / destination.name)) as connection:
            self.assertEqual(
                "preserved", connection.execute("SELECT body FROM records").fetchone()[0]
            )
        self.assertFalse(list(redirect.glob(".coordinator-*")))
        self.assertFalse((redirect / destination.name).exists())

    def test_real_parent_swap_before_install_allocation_fails_closed(self) -> None:
        backup = self.root / "backup.sqlite3"
        manifest = backup_database(self.source, backup, BINDING)
        parent = self.root / "destination-parent"
        parent.mkdir()
        destination = parent / "restored.sqlite3"
        create_database(destination, body="preserved")
        moved = self.root / "moved-parent"
        redirect = self.root / "redirect-parent"
        redirect.mkdir()
        original_identity = MODULE._parent_identity
        swapped = False

        def swap_parent(path: Path) -> tuple[int, int]:
            nonlocal swapped
            identity = cast(tuple[int, int], original_identity(path))
            if not swapped:
                swapped = True
                parent.rename(moved)
                parent.symlink_to(redirect, target_is_directory=True)
            return identity

        with (
            patch.object(MODULE, "_parent_identity", side_effect=swap_parent),
            self.assertRaisesRegex(BackupError, "parent identity changed"),
        ):
            restore_database(backup, destination, manifest, BINDING, quiesced=True)
        self.assertTrue((moved / destination.name).is_file())
        with closing(sqlite3.connect(moved / destination.name)) as connection:
            self.assertEqual(
                "preserved", connection.execute("SELECT body FROM records").fetchone()[0]
            )
        self.assertFalse(list(redirect.glob(".coordinator-*")))
        self.assertFalse((redirect / destination.name).exists())
        self.assertFalse((redirect / f"{destination.name}-wal").exists())
        self.assertFalse((redirect / f"{destination.name}-shm").exists())

    def test_real_parent_swap_before_manifest_allocation_fails_closed(self) -> None:
        backup = self.root / "backup.sqlite3"
        manifest = backup_database(self.source, backup, BINDING)
        parent = self.root / "manifest-parent"
        parent.mkdir()
        manifest_path = parent / "manifest.json"
        moved = self.root / "moved-manifest-parent"
        redirect = self.root / "redirect-manifest-parent"
        redirect.mkdir()
        original_identity = MODULE._parent_identity
        swapped = False

        def swap_parent(path: Path) -> tuple[int, int]:
            nonlocal swapped
            identity = cast(tuple[int, int], original_identity(path))
            if not swapped:
                swapped = True
                parent.rename(moved)
                parent.symlink_to(redirect, target_is_directory=True)
            return identity

        with (
            patch.object(MODULE, "_parent_identity", side_effect=swap_parent),
            self.assertRaisesRegex(BackupError, "parent identity changed"),
        ):
            write_manifest(manifest_path, manifest)
        self.assertFalse((moved / manifest_path.name).exists())
        self.assertFalse(list(redirect.glob(".coordinator-*")))
        self.assertFalse((redirect / manifest_path.name).exists())

    def test_source_replacement_during_backup_fails_closed(self) -> None:
        destination = self.root / "backup.sqlite3"
        moved = self.root / "moved-source.sqlite3"
        replacement = self.root / "replacement.sqlite3"
        create_database(replacement, body="replacement")
        original_copy = MODULE._copy_online
        swapped = False

        def swap_after_copy(source: Path, temporary: Path, binding: dict[str, object]) -> None:
            nonlocal swapped
            original_copy(source, temporary, binding)
            if not swapped:
                swapped = True
                self.source.rename(moved)
                self.source.symlink_to(replacement)

        with (
            patch.object(MODULE, "_copy_online", side_effect=swap_after_copy),
            self.assertRaisesRegex(BackupError, "source database"),
        ):
            backup_database(self.source, destination, BINDING)
        self.assertFalse(destination.exists())
        self.assertTrue(moved.is_file())
        self.assertTrue(self.source.is_symlink())
        self.assertFalse(list(self.root.glob(".coordinator-*")))

    def test_source_disappearance_during_backup_fails_closed(self) -> None:
        destination = self.root / "backup.sqlite3"
        moved = self.root / "disappeared-source.sqlite3"
        original_copy = MODULE._copy_online

        def remove_after_copy(source: Path, temporary: Path, binding: dict[str, object]) -> None:
            original_copy(source, temporary, binding)
            self.source.rename(moved)

        with (
            patch.object(MODULE, "_copy_online", side_effect=remove_after_copy),
            self.assertRaisesRegex(BackupError, "source database disappeared"),
        ):
            backup_database(self.source, destination, BINDING)
        self.assertFalse(destination.exists())
        self.assertTrue(moved.is_file())
        self.assertFalse(self.source.exists())
        self.assertFalse(list(self.root.glob(".coordinator-*")))

    def test_backup_replacement_during_restore_fails_closed(self) -> None:
        backup = self.root / "backup.sqlite3"
        manifest = backup_database(self.source, backup, BINDING)
        replacement_source = self.root / "replacement-source.sqlite3"
        create_database(replacement_source, body="replacement")
        replacement = self.root / "replacement.sqlite3"
        replacement_manifest = backup_database(replacement_source, replacement, BINDING)
        del replacement_manifest
        destination = self.root / "restored.sqlite3"
        original_integrity = MODULE._integrity

        def replace_after_integrity(path: Path, binding: dict[str, object]) -> None:
            original_integrity(path, binding)
            if path == backup:
                backup.unlink()
                replacement.rename(backup)

        with (
            patch.object(MODULE, "_integrity", side_effect=replace_after_integrity),
            self.assertRaisesRegex(BackupError, "backup database changed"),
        ):
            restore_database(backup, destination, manifest, BINDING, quiesced=True)
        self.assertFalse(destination.exists())
        self.assertFalse(list(self.root.glob(".coordinator-*")))

    def test_backup_disappearance_during_restore_is_backup_error(self) -> None:
        backup = self.root / "backup.sqlite3"
        manifest = backup_database(self.source, backup, BINDING)
        destination = self.root / "restored.sqlite3"
        original_integrity = MODULE._integrity

        def remove_after_integrity(path: Path, binding: dict[str, object]) -> None:
            original_integrity(path, binding)
            if path == backup:
                backup.unlink()

        with (
            patch.object(MODULE, "_integrity", side_effect=remove_after_integrity),
            self.assertRaisesRegex(BackupError, "backup database disappeared"),
        ):
            restore_database(backup, destination, manifest, BINDING, quiesced=True)
        self.assertFalse(destination.exists())
        self.assertFalse(list(self.root.glob(".coordinator-*")))

    def test_sidecar_appearing_before_restore_publication_fails_closed(self) -> None:
        backup = self.root / "backup.sqlite3"
        manifest = backup_database(self.source, backup, BINDING)
        destination = self.root / "restored.sqlite3"

        def create_sidecar(_path: Path) -> None:
            Path(str(destination) + "-wal").write_bytes(b"live")

        with (
            patch.object(MODULE, "_before_destination_publish", side_effect=create_sidecar),
            self.assertRaisesRegex(BackupError, "sidecar appeared"),
        ):
            restore_database(backup, destination, manifest, BINDING, quiesced=True)
        self.assertFalse(destination.exists())
        self.assertFalse(list(self.root.glob(".coordinator-*")))
        Path(str(destination) + "-wal").unlink()

    def test_verify_backup_disappearance_during_hash_is_backup_error(self) -> None:
        backup = self.root / "backup.sqlite3"
        manifest = backup_database(self.source, backup, BINDING)
        original_digest = MODULE._digest

        def remove_before_hash(path: Path) -> str:
            backup.unlink()
            return cast(str, original_digest(path))

        with (
            patch.object(MODULE, "_digest", side_effect=remove_before_hash),
            self.assertRaisesRegex(BackupError, "disappeared while hashing"),
        ):
            MODULE.verify_backup(backup, manifest, BINDING)
        self.assertFalse(list(self.root.glob(".coordinator-*")))


if __name__ == "__main__":
    unittest.main()
