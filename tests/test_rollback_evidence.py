# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

import json
import os
import sqlite3
import subprocess
import tempfile
import unittest
from collections.abc import Mapping
from pathlib import Path
from typing import Any, cast
from unittest.mock import patch

from tools.git_authority_adapter import GitAuthorityAdapter
from tools.git_backup import BackupError as GitBackupError
from tools.git_backup import create_backup
from tools.rollback_control_store import (
    AuthorityRuntimeRereader,
    ControlStoreError,
    SQLiteAuthorityRuntimeState,
    SQLiteControlStoreAdapter,
    SQLiteRollbackControlStore,
)
from tools.rollback_evidence import BackupObservation, RollbackEvidenceError
from tools.sqlite_authority_adapter import SQLiteAuthorityAdapter, SQLiteAuthorityError
from tools.sqlite_backup import BackupError as SQLiteBackupError
from tools.sqlite_backup import backup_database
from tools.upgrade_engine import (
    BoundRollbackCapability,
    PhaseContext,
    RollbackAuthorizationCapability,
    SQLiteRollbackObservationCapability,
    UpgradeError,
)

PROJECT = "11111111-1111-4111-8111-111111111111"


class NoopAuthorityRuntimeRereader(AuthorityRuntimeRereader):
    def reread_rollback(
        self, context: Mapping[str, object], _result: Mapping[str, object]
    ) -> SQLiteAuthorityRuntimeState:
        return SQLiteAuthorityRuntimeState(
            backend="sqlite",
            project_id=str(context["project_id"]),
            authority_revision=str(context["authority_revision"]),
            fencing_token=str(context["fencing_token"]),
            target="rollback",
            integrity_check="ok",
            foreign_key_violations=0,
            backend_roundtrip="sqlite",
        )


class RollbackEvidenceTests(unittest.TestCase):
    def test_backup_observation_rejects_non_paths_and_unavailable_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            backup = root / "backup"
            manifest = root / "manifest.json"
            backup.write_bytes(b"backup")
            manifest.write_text("{", encoding="utf-8")
            with self.assertRaisesRegex(RollbackEvidenceError, "must be paths"):
                BackupObservation.from_artifacts(
                    cast(Any, str(backup)),
                    manifest,
                    control_store_identity="1:2",
                    control_store_revision=1,
                )
            with self.assertRaisesRegex(RollbackEvidenceError, "unavailable"):
                BackupObservation.from_artifacts(
                    backup,
                    manifest,
                    control_store_identity="1:2",
                    control_store_revision=1,
                )

    def test_backup_observation_rejects_replacement_during_stat_recheck(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            backup = root / "backup"
            manifest = root / "manifest.json"
            backup.write_bytes(b"backup")
            manifest.write_text("{}", encoding="utf-8")
            original_backup_stat = backup.stat()
            original_manifest_stat = manifest.stat()
            changed_values = list(original_backup_stat)
            changed_values[1] += 1
            changed = os.stat_result(changed_values)
            calls = 0

            def stat_with_replacement(path: Path, **_kwargs: object) -> object:
                nonlocal calls
                if path == backup:
                    calls += 1
                    return original_backup_stat if calls == 1 else changed
                return original_manifest_stat

            with (
                patch("pathlib.Path.stat", autospec=True, side_effect=stat_with_replacement),
                self.assertRaisesRegex(RollbackEvidenceError, "replaced"),
            ):
                BackupObservation.from_artifacts(
                    backup,
                    manifest,
                    control_store_identity="1:2",
                    control_store_revision=1,
                )

    def test_adapters_invoke_real_backend_backup_verifiers(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            repo = root / "repo"
            repo.mkdir()
            for args in (
                ("init", "-q"),
                ("config", "user.email", "test@example.invalid"),
                ("config", "user.name", "test"),
            ):
                subprocess.run(["git", *args], cwd=repo, check=True)  # noqa: S603, S607
            (repo / "state").write_text("ok\n", encoding="utf-8")
            subprocess.run(["git", "add", "state"], cwd=repo, check=True)  # noqa: S607
            subprocess.run(["git", "commit", "-qm", "initial"], cwd=repo, check=True)  # noqa: S607
            git_backup = create_backup(repo, root / "git-backup", quiesced=True)
            self.assertTrue(GitAuthorityAdapter.verify_backup_artifact(git_backup)["verified"])
            (git_backup / "refs.txt").write_text("tampered\n", encoding="utf-8")
            with self.assertRaises(GitBackupError):
                GitAuthorityAdapter.verify_backup_artifact(git_backup)

            binding = {
                "project_id": PROJECT,
                "state_repository": "owner/state",
                "product_repository": "owner/product",
            }
            source = root / "source.sqlite"
            connection = sqlite3.connect(source)
            connection.executescript(
                "CREATE TABLE metadata(key TEXT PRIMARY KEY, value TEXT NOT NULL);"
                "CREATE TABLE records(id INTEGER PRIMARY KEY, body TEXT NOT NULL);"
            )
            connection.executemany(
                "INSERT INTO metadata VALUES (?, ?)",
                [
                    ("schema_version", "1"),
                    ("backend", "sqlite"),
                    ("project_id", PROJECT),
                    ("state_repository", "owner/state"),
                    ("product_repository", "owner/product"),
                    ("state", "active"),
                ],
            )
            connection.execute("INSERT INTO records(body) VALUES ('ok')")
            connection.commit()
            connection.close()
            sqlite_backup = root / "sqlite-backup.sqlite"
            manifest = backup_database(source, sqlite_backup, binding)
            self.assertEqual(
                manifest,
                SQLiteAuthorityAdapter.verify_backup_artifact(sqlite_backup, manifest, binding),
            )
            with self.assertRaises(SQLiteBackupError):
                SQLiteAuthorityAdapter.verify_backup_artifact(
                    sqlite_backup, {**manifest, "database_sha256": "0" * 64}, binding
                )
            sqlite_backup.write_bytes(b"tampered")
            with self.assertRaises(SQLiteBackupError):
                SQLiteAuthorityAdapter.verify_backup_artifact(sqlite_backup, manifest, binding)

    def test_initialized_sqlite_control_store_binds_observation_identity(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            authority = root / "authority.sqlite"
            authority.write_bytes(b"SQLite format 3\x00")
            authority.chmod(0o600)
            control = SQLiteRollbackControlStore(root / "control.sqlite", PROJECT, authority)
            context = {
                "schema_version": 2,
                "backend": "sqlite",
                "project_id": PROJECT,
                "operation_id": "op-1",
                "state_revision": 1,
                "authority_revision": "authority-1",
                "fencing_token": "fence-1",
                "fencing_owner": "owner-1",
                "durable_barrier_id": "barrier-1",
                "artifact_root": str(root),
                "source": str(authority),
                "destination": str(root / "backup.bin"),
                "manifest": str(root / "manifest.json"),
                "selector_ref": ".runtime/runtime-selector.json",
                "barrier_identity_digest": "0" * 64,
                "target": "rollback",
                "envelope_digest": "0" * 64,
            }
            from tools.upgrade_identity import canonical_barrier_digest, canonical_envelope_digest

            context["barrier_identity_digest"] = canonical_barrier_digest(context)
            context["envelope_digest"] = canonical_envelope_digest(context)
            record = {**context, "status": "held", "revision": 1}
            control.cas(0, record)
            backup = root / "backup.bin"
            manifest = root / "manifest.json"
            backup.write_bytes(b"backup")
            manifest.write_text(json.dumps({"version": 1}), encoding="utf-8")
            adapter = SQLiteControlStoreAdapter(
                SQLiteAuthorityAdapter(authority),
                control,
                NoopAuthorityRuntimeRereader(),
            )
            observation = adapter.observe_backup_identity(backup, manifest, context)
            capability = SQLiteRollbackObservationCapability.bind(
                PhaseContext(**cast(dict[str, Any], context)), adapter
            )
            observed_again = capability.observe(context)
            self.assertEqual(observation, observed_again)
            bound = BoundRollbackCapability.bind(
                PhaseContext(**cast(dict[str, Any], context)),
                adapter,
                object(),
                lease=object(),
                admission_recheck=object(),
            )
            authorization = RollbackAuthorizationCapability.bind(
                PhaseContext(**cast(dict[str, Any], context)), bound
            )
            before = (root / "control.sqlite").read_bytes()
            with self.assertRaisesRegex(UpgradeError, "not enabled"):
                authorization.preflight(context, capability)
            self.assertEqual(before, (root / "control.sqlite").read_bytes())
            with self.assertRaisesRegex(UpgradeError, "identity mismatch"):
                capability.observe({**context, "operation_id": "foreign"})
            stat = control.control_store_path.stat()
            self.assertEqual(f"{stat.st_dev}:{stat.st_ino}", observation.control_store_identity)
            self.assertEqual(1, observation.control_store_revision)
            control.cas(1, {**record, "status": "ambiguous", "revision": 2})
            with self.assertRaises(ControlStoreError):
                adapter.observe_backup_identity(backup, manifest, context)
            self.assertFalse(control.operation_owned_by_current_thread)
            with control.operation_lock():
                pass

    def test_observation_rejects_control_store_stat_failure_and_bad_revision(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            authority = root / "authority.sqlite"
            authority.write_bytes(b"SQLite format 3\x00")
            authority.chmod(0o600)
            control = SQLiteRollbackControlStore(root / "control.sqlite", PROJECT, authority)
            adapter = SQLiteControlStoreAdapter(
                SQLiteAuthorityAdapter(authority), control, NoopAuthorityRuntimeRereader()
            )
            context = {"operation_id": "missing", "backend": "sqlite", "target": "rollback"}
            backup = root / "backup"
            manifest = root / "manifest.json"
            backup.write_bytes(b"backup")
            manifest.write_text("{}", encoding="utf-8")
            original_stat = Path.stat

            def fail_control_stat(path: Path, *, follow_symlinks: bool = True) -> os.stat_result:
                if path == control.control_store_path:
                    raise OSError("gone")
                return original_stat(path, follow_symlinks=follow_symlinks)

            with (
                patch.object(
                    control, "_verify_rollback_context_locked", return_value={"revision": 1}
                ),
                patch("pathlib.Path.stat", autospec=True, side_effect=fail_control_stat),
                self.assertRaisesRegex(ControlStoreError, "identity reread failed"),
            ):
                adapter.observe_backup_identity(backup, manifest, context)
            self.assertFalse(control.operation_owned_by_current_thread)
            with control.operation_lock():
                pass
            with (
                patch.object(
                    control, "_verify_rollback_context_locked", return_value={"revision": "one"}
                ),
                self.assertRaisesRegex(ControlStoreError, "identity is invalid"),
            ):
                adapter.observe_backup_identity(backup, manifest, context)
            self.assertFalse(control.operation_owned_by_current_thread)
            with control.operation_lock():
                pass

    def test_initialized_control_store_inode_replacement_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            authority = root / "authority.sqlite"
            authority.write_bytes(b"SQLite format 3\x00")
            authority.chmod(0o600)
            control = SQLiteRollbackControlStore(root / "control.sqlite", PROJECT, authority)
            replacement = root / "replacement.sqlite"
            replacement.write_bytes(b"replaced")
            control.control_store_path.replace(replacement)
            with self.assertRaises(ControlStoreError):
                control.snapshot("op-1")

    def test_sqlite_sidecar_replacement_is_rejected_after_initialization(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            authority = root / "authority.sqlite"
            authority.write_bytes(b"SQLite format 3\x00")
            authority.chmod(0o600)
            adapter = SQLiteAuthorityAdapter(authority)
            wal = authority.with_name("authority.sqlite-wal")
            wal.write_bytes(b"replacement")
            wal.chmod(0o600)
            with self.assertRaises(SQLiteAuthorityError):
                adapter.snapshot(
                    "rollback",
                    {
                        "schema_version": 2,
                        "backend": "sqlite",
                        "project_id": PROJECT,
                        "operation_id": "op-1",
                        "state_revision": 1,
                        "authority_revision": "authority-1",
                        "fencing_token": "fence-1",
                        "fencing_owner": "owner-1",
                        "durable_barrier_id": "barrier-1",
                        "artifact_root": str(root),
                        "source": str(authority),
                        "destination": str(root / "backup"),
                        "manifest": str(root / "manifest"),
                        "barrier_identity_digest": "0" * 64,
                        "target": "rollback",
                        "envelope_digest": "0" * 64,
                    },
                )

    def test_initialized_adapters_observe_identical_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / ".git").mkdir()
            backup = root / "backup.bin"
            manifest = root / "manifest.json"
            backup.write_bytes(b"immutable-backup")
            manifest.write_text(json.dumps({"version": 1}), encoding="utf-8")
            git = GitAuthorityAdapter(root)
            database = root / "authority.sqlite"
            database.write_bytes(b"SQLite format 3\x00")
            database.chmod(0o600)
            sqlite = SQLiteAuthorityAdapter(database)
            git_observation = git.observe_backup_identity(
                backup, manifest, control_store_identity="store-1", control_store_revision=1
            )
            sqlite_observation = sqlite.observe_backup_identity(
                backup, manifest, control_store_identity="store-1", control_store_revision=1
            )
            self.assertEqual(git_observation, sqlite_observation)
            backup.write_bytes(b"replaced-backup")
            self.assertNotEqual(
                git_observation.backup_bytes_digest,
                git.observe_backup_identity(
                    backup, manifest, control_store_identity="store-1", control_store_revision=1
                ).backup_bytes_digest,
            )
            manifest.write_text(json.dumps({"version": 2}), encoding="utf-8")
            self.assertNotEqual(
                git_observation.manifest_digest,
                sqlite.observe_backup_identity(
                    backup, manifest, control_store_identity="store-1", control_store_revision=1
                ).manifest_digest,
            )

    def test_observation_rejects_tampered_manifest_and_cas_facts(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            backup = root / "backup.bin"
            manifest = root / "manifest.json"
            backup.write_bytes(b"backup")
            manifest.write_text("[]", encoding="utf-8")
            with self.assertRaises(RollbackEvidenceError):
                GitAuthorityAdapter.observe_backup_identity(
                    backup, manifest, control_store_identity="store", control_store_revision=1
                )
            manifest.write_text("{}", encoding="utf-8")
            with self.assertRaises(RollbackEvidenceError):
                GitAuthorityAdapter.observe_backup_identity(
                    backup, manifest, control_store_identity="", control_store_revision=1
                )
            with self.assertRaises(RollbackEvidenceError):
                GitAuthorityAdapter.observe_backup_identity(
                    backup, manifest, control_store_identity="store", control_store_revision=True
                )
