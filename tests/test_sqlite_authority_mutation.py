# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Hostile tests for the isolated SQLite authority commit capability."""

from __future__ import annotations

import multiprocessing
import os
import shutil
import signal
import sqlite3
import tempfile
import unittest
from contextlib import closing
from pathlib import Path
from typing import Any, cast
from unittest.mock import patch

from tools.authority_neutral_commit import CommitAdmissionBundle
from tools.sqlite_authority_mutation import (
    SQLiteCommitCapability,
    SQLiteMutationAmbiguousError,
    SQLiteMutationError,
    SQLiteMutationRejectedError,
)


def _sqlite_commit_then_kill_worker(
    db_text: str,
    expected_db: tuple[int, int],
    expected_wal: tuple[int, int] | None,
    expected_shm: tuple[int, int] | None,
) -> None:
    db = Path(db_text)
    admission = CommitAdmissionBundle(
        backend="sqlite",
        target="new",
        operation_id="op-process-death:commit",
        fencing_token="fence-process-death",  # noqa: S106
        state_revision=1,
        barrier_id="barrier-process-death",
        artifact_identity="artifact-1",
        manifest_identity="manifest-1",
        selector_identity="selector-1",
        runtime_identity="runtime-1",
    )

    class KillAfterCommitConnection:
        def __init__(self, connection: sqlite3.Connection) -> None:
            self._connection = connection

        def commit(self) -> None:
            self._connection.commit()
            os.kill(os.getpid(), signal.SIGKILL)

        def rollback(self) -> None:
            self._connection.rollback()

        def close(self) -> None:
            self._connection.close()

        def execute(self, *args: Any, **kwargs: Any) -> Any:
            return self._connection.execute(*args, **kwargs)

    def connector(*args: Any, **kwargs: Any) -> KillAfterCommitConnection:
        return KillAfterCommitConnection(sqlite3.connect(*args, **kwargs))

    def update(connection: sqlite3.Connection) -> None:
        connection.execute("UPDATE state SET value='new' WHERE id=1")

    SQLiteCommitCapability(
        db,
        admission=admission,
        admission_reread=lambda: admission.__dict__,
        expected_db_identity=expected_db,
        expected_wal_identity=expected_wal,
        expected_shm_identity=expected_shm,
        connector=cast(Any, connector),
    ).commit(cast(Any, update))


def _stale_owner_sqlite_worker(
    db_text: str,
    expected_db: tuple[int, int],
    expected_wal: tuple[int, int] | None,
    expected_shm: tuple[int, int] | None,
    owner_file_text: str,
    ready: Any,
    proceed: Any,
    result_queue: Any,
) -> None:
    db = Path(db_text)
    owner_file = Path(owner_file_text)
    admission = CommitAdmissionBundle(
        backend="sqlite",
        target="new",
        operation_id="op-stale-owner:commit",
        fencing_token="fence-1",  # noqa: S106
        state_revision=1,
        barrier_id="barrier-stale-owner",
        artifact_identity="artifact-1",
        manifest_identity="manifest-1",
        selector_identity="selector-1",
        runtime_identity="runtime-1",
    )

    def reread() -> dict[str, object]:
        current = dict(admission.__dict__)
        current["fencing_token"] = owner_file.read_text(encoding="utf-8")
        return current

    capability = SQLiteCommitCapability(
        db,
        admission=admission,
        admission_reread=reread,
        expected_db_identity=expected_db,
        expected_wal_identity=expected_wal,
        expected_shm_identity=expected_shm,
    )
    ready.set()
    proceed.wait(5)

    def update(connection: sqlite3.Connection) -> None:
        connection.execute("UPDATE state SET value='unexpected' WHERE id=1")

    try:
        capability.commit(update)
    except SQLiteMutationRejectedError:
        result_queue.put("rejected")
    except BaseException as error:
        result_queue.put(f"unexpected:{type(error).__name__}")
    else:
        result_queue.put("committed")


def _pre_effect_sqlite_death_worker(
    db_text: str,
    expected_db: tuple[int, int],
    expected_wal: tuple[int, int] | None,
    expected_shm: tuple[int, int] | None,
) -> None:
    db = Path(db_text)
    admission = CommitAdmissionBundle(
        backend="sqlite",
        target="new",
        operation_id="op-pre-effect-death:commit",
        fencing_token="fence-pre-effect-death",  # noqa: S106
        state_revision=1,
        barrier_id="barrier-pre-effect-death",
        artifact_identity="artifact-1",
        manifest_identity="manifest-1",
        selector_identity="selector-1",
        runtime_identity="runtime-1",
    )
    SQLiteCommitCapability(
        db,
        admission=admission,
        admission_reread=lambda: admission.__dict__,
        expected_db_identity=expected_db,
        expected_wal_identity=expected_wal,
        expected_shm_identity=expected_shm,
    )
    os.kill(os.getpid(), signal.SIGKILL)


class SQLiteCommitCapabilityTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.db = self.root / "authority.sqlite"
        with closing(sqlite3.connect(self.db)) as connection, connection:
            connection.execute("PRAGMA journal_mode=WAL")
            connection.execute("CREATE TABLE state (id INTEGER PRIMARY KEY, value TEXT NOT NULL)")
            connection.execute("INSERT INTO state VALUES (1, 'old')")
        # Keep WAL/SHM identities materialized for the duration of each hostile case.
        self.keepalive = sqlite3.connect(self.db)
        self.keepalive.execute("PRAGMA wal_autocheckpoint=0")
        self.keepalive.execute("PRAGMA user_version=1")
        self.keepalive.commit()
        self._admission = CommitAdmissionBundle(
            backend="sqlite",
            target="new",
            operation_id="op-1:commit",
            fencing_token="fence-1",  # noqa: S106
            state_revision=1,
            barrier_id="barrier-1",
            artifact_identity="artifact-1",
            manifest_identity="manifest-1",
            selector_identity="selector-1",
            runtime_identity="runtime-1",
        )

    def tearDown(self) -> None:
        self.keepalive.close()
        self.temp.cleanup()

    def _capability(self) -> SQLiteCommitCapability:
        def identity(path: Path) -> tuple[int, int] | None:
            try:
                status = path.lstat()
            except FileNotFoundError:
                return None
            return status.st_dev, status.st_ino

        return SQLiteCommitCapability(
            self.db,
            admission=self._admission,
            admission_reread=lambda: self._admission.__dict__,
            expected_db_identity=identity(self.db),  # type: ignore[arg-type]
            expected_wal_identity=identity(self.db.with_name("authority.sqlite-wal")),
            expected_shm_identity=identity(self.db.with_name("authority.sqlite-shm")),
        )

    def test_commits_effect_and_verifies_integrity(self) -> None:
        def update(connection: sqlite3.Connection) -> None:
            connection.execute("UPDATE state SET value='new' WHERE id=1")

        result = self._capability().commit(update)
        self.assertEqual(
            (
                "sqlite",
                "new",
                "op-1:commit",
                1,
                "barrier-1",
                "artifact-1",
                "manifest-1",
                "selector-1",
                "runtime-1",
                "fence-1",
            ),
            (
                result.backend,
                result.target,
                result.operation_id,
                result.state_revision,
                result.barrier_id,
                result.artifact_identity,
                result.manifest_identity,
                result.selector_identity,
                result.runtime_identity,
                result.fencing_token,
            ),
        )
        self.assertEqual("ok", result.integrity_check)
        with closing(sqlite3.connect(self.db)) as connection, connection:
            self.assertEqual(("new",), connection.execute("SELECT value FROM state").fetchone())

    def test_effect_runs_with_full_synchronous_durability(self) -> None:
        observed: list[int] = []

        def update(connection: sqlite3.Connection) -> None:
            observed.append(int(connection.execute("PRAGMA synchronous").fetchone()[0]))
            connection.execute("UPDATE state SET value='full-sync' WHERE id=1")

        result = self._capability().commit(update)

        self.assertEqual("ok", result.integrity_check)
        self.assertEqual([2], observed)
        with closing(sqlite3.connect(self.db)) as connection, connection:
            self.assertEqual(
                ("full-sync",), connection.execute("SELECT value FROM state").fetchone()
            )

    def test_post_commit_verification_closes_its_connection(self) -> None:
        real_connect = sqlite3.connect
        closed = False

        class TrackingConnection:
            def __init__(self, connection: sqlite3.Connection) -> None:
                self._connection = connection

            def __enter__(self) -> TrackingConnection:
                self._connection.__enter__()
                return self

            def __exit__(self, *args: Any) -> bool | None:
                return self._connection.__exit__(*args)

            def close(self) -> None:
                nonlocal closed
                closed = True
                self._connection.close()

            def __getattr__(self, name: str) -> object:
                return getattr(self._connection, name)

        def verification_connector(*args: Any, **kwargs: Any) -> TrackingConnection:
            return TrackingConnection(real_connect(*args, **kwargs))

        def update(connection: sqlite3.Connection) -> None:
            connection.execute("UPDATE state SET value='closed'")

        with patch.object(sqlite3, "connect", side_effect=verification_connector):
            self._capability().commit(update)
        self.assertTrue(closed)

    def test_capability_is_single_use_but_fresh_capability_reopens(self) -> None:
        capability = self._capability()

        def first_update(connection: sqlite3.Connection) -> None:
            connection.execute("UPDATE state SET value='first'")

        capability.commit(first_update)

        called = False

        def replay(connection: sqlite3.Connection) -> None:
            nonlocal called
            called = True
            connection.execute("UPDATE state SET value='replayed'")

        with self.assertRaisesRegex(SQLiteMutationError, "already consumed"):
            capability.commit(replay)
        self.assertFalse(called)

        reopened_admission = CommitAdmissionBundle(
            backend="sqlite",
            target="new",
            operation_id="op-2:commit",
            fencing_token="fence-2",  # noqa: S106
            state_revision=2,
            barrier_id="barrier-2",
            artifact_identity="artifact-1",
            manifest_identity="manifest-1",
            selector_identity="selector-1",
            runtime_identity="runtime-1",
        )
        self._admission = reopened_admission

        def second_update(connection: sqlite3.Connection) -> None:
            connection.execute("UPDATE state SET value='second'")

        self._capability().commit(second_update)
        with closing(sqlite3.connect(self.db)) as connection, connection:
            self.assertEqual(("second",), connection.execute("SELECT value FROM state").fetchone())

    def test_independent_process_death_after_effect_requires_fresh_capability(self) -> None:
        capability = self._capability()
        context = multiprocessing.get_context("fork")
        worker = context.Process(
            target=_sqlite_commit_then_kill_worker,
            args=(
                str(self.db),
                capability._db_identity,
                capability._wal_identity,
                capability._shm_identity,
            ),
        )
        worker.start()
        worker.join(10)
        self.assertEqual(-signal.SIGKILL, worker.exitcode)

        with closing(sqlite3.connect(self.db)) as connection, connection:
            self.assertEqual(("new",), connection.execute("SELECT value FROM state").fetchone())

        self._admission = CommitAdmissionBundle(
            backend="sqlite",
            target="new",
            operation_id="op-process-death-reopen:commit",
            fencing_token="fence-process-death-reopen",  # noqa: S106
            state_revision=2,
            barrier_id="barrier-process-death-reopen",
            artifact_identity="artifact-1",
            manifest_identity="manifest-1",
            selector_identity="selector-1",
            runtime_identity="runtime-1",
        )

        def reopen(connection: sqlite3.Connection) -> None:
            connection.execute("UPDATE state SET value='reopened' WHERE id=1")

        result = self._capability().commit(reopen)
        self.assertEqual("ok", result.integrity_check)
        with closing(sqlite3.connect(self.db)) as connection, connection:
            self.assertEqual(
                ("reopened",), connection.execute("SELECT value FROM state").fetchone()
            )

    def test_independent_process_stale_owner_replacement_rejects_before_effect(self) -> None:
        owner_file = self.root / "owner-fence"
        owner_file.write_text("fence-1", encoding="utf-8")
        capability = self._capability()
        context = multiprocessing.get_context("fork")
        ready = context.Event()
        proceed = context.Event()
        result_queue = context.Queue()
        worker = context.Process(
            target=_stale_owner_sqlite_worker,
            args=(
                str(self.db),
                capability._db_identity,
                capability._wal_identity,
                capability._shm_identity,
                str(owner_file),
                ready,
                proceed,
                result_queue,
            ),
        )
        worker.start()
        self.assertTrue(ready.wait(5))
        owner_file.write_text("foreign-fence", encoding="utf-8")
        proceed.set()
        worker.join(10)
        self.assertEqual(0, worker.exitcode)
        self.assertEqual("rejected", result_queue.get(timeout=2))
        with closing(sqlite3.connect(self.db)) as connection, connection:
            self.assertEqual(("old",), connection.execute("SELECT value FROM state").fetchone())

    def test_independent_process_death_before_effect_allows_fresh_capability(self) -> None:
        capability = self._capability()
        context = multiprocessing.get_context("fork")
        worker = context.Process(
            target=_pre_effect_sqlite_death_worker,
            args=(
                str(self.db),
                capability._db_identity,
                capability._wal_identity,
                capability._shm_identity,
            ),
        )
        worker.start()
        worker.join(10)
        self.assertEqual(-signal.SIGKILL, worker.exitcode)
        with closing(sqlite3.connect(self.db)) as connection, connection:
            self.assertEqual(("old",), connection.execute("SELECT value FROM state").fetchone())

        self._admission = CommitAdmissionBundle(
            backend="sqlite",
            target="new",
            operation_id="op-pre-effect-reopen:commit",
            fencing_token="fence-pre-effect-reopen",  # noqa: S106
            state_revision=2,
            barrier_id="barrier-pre-effect-reopen",
            artifact_identity="artifact-1",
            manifest_identity="manifest-1",
            selector_identity="selector-1",
            runtime_identity="runtime-1",
        )

        def reopen(connection: sqlite3.Connection) -> None:
            connection.execute("UPDATE state SET value='reopened' WHERE id=1")

        result = self._capability().commit(reopen)
        self.assertEqual("ok", result.integrity_check)
        with closing(sqlite3.connect(self.db)) as connection, connection:
            self.assertEqual(
                ("reopened",), connection.execute("SELECT value FROM state").fetchone()
            )

    def test_rejects_termination_during_initial_authority_ancestor_identity(self) -> None:
        with (
            patch.object(
                SQLiteCommitCapability,
                "_ancestor_identities_for",
                side_effect=KeyboardInterrupt("injected termination"),
            ),
            self.assertRaisesRegex(SQLiteMutationRejectedError, "identity capture was rejected"),
        ):
            self._capability()

    def test_rejects_termination_during_initial_authority_path_normalization(self) -> None:
        with (
            patch.object(Path, "absolute", side_effect=KeyboardInterrupt("injected termination")),
            self.assertRaisesRegex(SQLiteMutationRejectedError, "identity capture was rejected"),
        ):
            self._capability()

    def test_rejects_sidecar_identity_drift_before_effect(self) -> None:
        capability = self._capability()
        wal = self.db.with_name("authority.sqlite-wal")
        wal.unlink(missing_ok=True)

        def update(connection: sqlite3.Connection) -> None:
            connection.execute("UPDATE state SET value='bad'")

        with self.assertRaisesRegex(SQLiteMutationRejectedError, "WAL identity changed"):
            capability.commit(update)

    def test_rejects_sidecar_identity_read_error_before_effect(self) -> None:
        capability = self._capability()
        called = False

        def update(connection: sqlite3.Connection) -> None:
            nonlocal called
            called = True
            connection.execute("UPDATE state SET value='bad'")

        with (
            patch.object(Path, "lstat", side_effect=OSError("identity unavailable")),
            self.assertRaisesRegex(SQLiteMutationRejectedError, "sidecar identity is unavailable"),
        ):
            capability.commit(update)
        self.assertFalse(called)

    def test_rejects_nonregular_authority_identity_before_effect(self) -> None:
        capability = self._capability()
        wal = self.db.with_name("authority.sqlite-wal")
        replacement = self.root / "replacement.wal"
        replacement.write_bytes(b"replacement")
        wal.unlink()
        wal.symlink_to(replacement)
        called = False

        def update(connection: sqlite3.Connection) -> None:
            nonlocal called
            called = True
            connection.execute("UPDATE state SET value='bad'")

        with self.assertRaisesRegex(SQLiteMutationRejectedError, "not a regular private file"):
            capability.commit(update)
        self.assertFalse(called)

    def test_rejects_symlinked_authority_path_before_effect(self) -> None:
        original = self._capability()
        alias = self.root / "authority-alias.sqlite"
        alias.symlink_to(self.db)
        called = False

        def update(connection: sqlite3.Connection) -> None:
            nonlocal called
            called = True
            connection.execute("UPDATE state SET value='bad'")

        capability = SQLiteCommitCapability(
            alias,
            admission=self._admission,
            admission_reread=lambda: self._admission.__dict__,
            expected_db_identity=original._db_identity,
            expected_wal_identity=original._wal_identity,
            expected_shm_identity=original._shm_identity,
        )
        with self.assertRaisesRegex(SQLiteMutationRejectedError, "not a regular private file"):
            capability.commit(update)
        self.assertFalse(called)

    def test_rejects_authority_parent_replacement_before_effect(self) -> None:
        capability = self._capability()
        relocated_root = self.root.parent / f"{self.root.name}-parent-replaced"
        self.root.rename(relocated_root)
        self.root.mkdir()
        called = False

        def update(connection: sqlite3.Connection) -> None:
            nonlocal called
            called = True
            connection.execute("UPDATE state SET value='bad'")

        with self.assertRaisesRegex(SQLiteMutationRejectedError, "ancestor identity changed"):
            capability.commit(update)
        self.assertFalse(called)

    def test_rejects_authority_ancestor_replacement_before_effect(self) -> None:
        outer = self.root.parent / f"{self.root.name}-outer"
        inner = outer / "inner"
        inner.mkdir(parents=True)
        relocated_root = inner / "root"
        self.root.rename(relocated_root)
        self.db = relocated_root / "authority.sqlite"
        capability = self._capability()
        replacement = outer.parent / f"{outer.name}-replaced"
        outer.rename(replacement)
        outer.mkdir()
        called = False

        def update(connection: sqlite3.Connection) -> None:
            nonlocal called
            called = True
            connection.execute("UPDATE state SET value='bad'")

        with self.assertRaisesRegex(SQLiteMutationRejectedError, "ancestor identity changed"):
            capability.commit(update)
        self.assertFalse(called)

    def test_rejects_symlinked_authority_ancestor_before_effect(self) -> None:
        outer = self.root.parent / f"{self.root.name}-symlink-outer"
        inner = outer / "inner"
        inner.mkdir(parents=True)
        relocated_root = inner / "root"
        self.root.rename(relocated_root)
        self.db = relocated_root / "authority.sqlite"
        capability = self._capability()
        replacement = outer.parent / f"{outer.name}-target"
        outer.rename(replacement)
        outer.symlink_to(replacement, target_is_directory=True)
        called = False

        def update(connection: sqlite3.Connection) -> None:
            nonlocal called
            called = True
            connection.execute("UPDATE state SET value='bad'")

        with self.assertRaisesRegex(SQLiteMutationRejectedError, "ancestor identity changed"):
            capability.commit(update)
        self.assertFalse(called)

    def test_rejects_connector_oserror_before_effect(self) -> None:
        called = False

        def connector(*_args: Any, **_kwargs: Any) -> sqlite3.Connection:
            raise OSError("injected connector failure")

        def update(connection: sqlite3.Connection) -> None:
            nonlocal called
            called = True
            connection.execute("UPDATE state SET value='bad'")

        capability = SQLiteCommitCapability(
            self.db,
            admission=self._admission,
            admission_reread=lambda: self._admission.__dict__,
            expected_db_identity=self._capability()._db_identity,
            expected_wal_identity=self._capability()._wal_identity,
            expected_shm_identity=self._capability()._shm_identity,
            connector=connector,
        )
        with self.assertRaisesRegex(
            SQLiteMutationRejectedError, "connection was rejected before effect"
        ):
            capability.commit(update)
        self.assertFalse(called)

    def test_rejects_sqlite_setup_error_before_effect(self) -> None:
        real_connect = sqlite3.connect
        called = False

        class SetupFailingConnection:
            def __init__(self, connection: sqlite3.Connection) -> None:
                self._connection = connection

            def execute(self, sql: str, *args: Any) -> sqlite3.Cursor:
                if sql == "PRAGMA foreign_keys=ON":
                    raise sqlite3.OperationalError("injected setup failure")
                return self._connection.execute(sql, *args)

            def __getattr__(self, name: str) -> object:
                return getattr(self._connection, name)

        def connector(*args: Any, **kwargs: Any) -> sqlite3.Connection:
            return cast(sqlite3.Connection, SetupFailingConnection(real_connect(*args, **kwargs)))

        def update(connection: sqlite3.Connection) -> None:
            nonlocal called
            called = True
            connection.execute("UPDATE state SET value='bad'")

        capability = SQLiteCommitCapability(
            self.db,
            admission=self._admission,
            admission_reread=lambda: self._admission.__dict__,
            expected_db_identity=self._capability()._db_identity,
            expected_wal_identity=self._capability()._wal_identity,
            expected_shm_identity=self._capability()._shm_identity,
            connector=connector,
        )
        with self.assertRaisesRegex(
            SQLiteMutationRejectedError, "setup was rejected before effect"
        ):
            capability.commit(update)
        self.assertFalse(called)

    def test_rejects_authority_replacement_after_connect_before_effect(self) -> None:
        real_connect = sqlite3.connect
        replaced = False

        def replacing_connector(*args: Any, **kwargs: Any) -> sqlite3.Connection:
            nonlocal replaced
            connection = real_connect(*args, **kwargs)
            if not replaced:
                replacement = self.root / "replacement.sqlite"
                shutil.copy2(self.db, replacement)
                replacement.replace(self.db)
                replaced = True
            return cast(sqlite3.Connection, connection)

        called = False

        def update(connection: sqlite3.Connection) -> None:
            nonlocal called
            called = True
            connection.execute("UPDATE state SET value='bad'")

        capability = SQLiteCommitCapability(
            self.db,
            admission=self._admission,
            admission_reread=lambda: self._admission.__dict__,
            expected_db_identity=self._capability()._db_identity,
            expected_wal_identity=self._capability()._wal_identity,
            expected_shm_identity=self._capability()._shm_identity,
            connector=replacing_connector,
        )
        with self.assertRaisesRegex(SQLiteMutationRejectedError, "database identity changed"):
            capability.commit(update)
        self.assertTrue(replaced)
        self.assertFalse(called)

    def test_classifies_sqlite_errors_as_ambiguous(self) -> None:
        def invalid(connection: sqlite3.Connection) -> None:
            connection.execute("UPDATE missing SET x=1")

        with self.assertRaises(SQLiteMutationAmbiguousError):
            self._capability().commit(invalid)

    def test_classifies_effect_oserror_as_ambiguous(self) -> None:
        def failing_effect(_connection: sqlite3.Connection) -> None:
            raise OSError("injected effect failure")

        with self.assertRaisesRegex(SQLiteMutationAmbiguousError, "commit outcome is ambiguous"):
            self._capability().commit(failing_effect)

    def test_ambiguous_effect_consumes_capability_and_cannot_retry(self) -> None:
        capability = self._capability()

        def failing_effect(_connection: sqlite3.Connection) -> None:
            raise OSError("injected effect uncertainty")

        with self.assertRaisesRegex(SQLiteMutationAmbiguousError, "commit outcome is ambiguous"):
            capability.commit(failing_effect)

        called = False

        def retry(_connection: sqlite3.Connection) -> None:
            nonlocal called
            called = True

        with self.assertRaisesRegex(SQLiteMutationError, "already consumed"):
            capability.commit(retry)
        self.assertFalse(called)

    def test_classifies_arbitrary_effect_exception_as_ambiguous(self) -> None:
        def failing_effect(_connection: sqlite3.Connection) -> None:
            raise RuntimeError("injected effect failure")

        with self.assertRaisesRegex(SQLiteMutationAmbiguousError, "commit outcome is ambiguous"):
            self._capability().commit(failing_effect)

    def test_classifies_termination_effect_exception_as_ambiguous(self) -> None:
        def terminating_effect(_connection: sqlite3.Connection) -> None:
            raise KeyboardInterrupt("injected termination")

        with self.assertRaisesRegex(SQLiteMutationAmbiguousError, "commit outcome is ambiguous"):
            self._capability().commit(terminating_effect)

    def test_classifies_termination_connector_as_ambiguous(self) -> None:
        def terminating_connector(*_args: Any, **_kwargs: Any) -> sqlite3.Connection:
            raise KeyboardInterrupt("injected termination")

        def update(_connection: sqlite3.Connection) -> None:
            raise AssertionError("effect must not run")

        with self.assertRaisesRegex(SQLiteMutationAmbiguousError, "commit outcome is ambiguous"):
            SQLiteCommitCapability(
                self.db,
                admission=self._admission,
                admission_reread=lambda: self._admission.__dict__,
                expected_db_identity=self._capability()._db_identity,
                expected_wal_identity=self._capability()._wal_identity,
                expected_shm_identity=self._capability()._shm_identity,
                connector=terminating_connector,
            ).commit(update)

    def test_classifies_termination_admission_reread_as_rejected(self) -> None:
        baseline = self._capability()

        def terminating_reread() -> dict[str, object]:
            raise KeyboardInterrupt("injected termination")

        capability = SQLiteCommitCapability(
            self.db,
            admission=self._admission,
            admission_reread=terminating_reread,
            expected_db_identity=baseline._db_identity,
            expected_wal_identity=baseline._wal_identity,
            expected_shm_identity=baseline._shm_identity,
        )

        def update(_connection: sqlite3.Connection) -> None:
            raise AssertionError("effect must not run")

        with self.assertRaisesRegex(SQLiteMutationRejectedError, "admission reread was rejected"):
            capability.commit(update)

    def test_classifies_termination_filesystem_identity_reread_as_rejected(self) -> None:
        capability = self._capability()

        def update(_connection: sqlite3.Connection) -> None:
            raise AssertionError("effect must not run")

        with (
            patch.object(
                SQLiteCommitCapability,
                "_identity",
                side_effect=KeyboardInterrupt("injected termination"),
            ),
            self.assertRaisesRegex(
                SQLiteMutationRejectedError, "filesystem identity reread was rejected"
            ),
        ):
            capability.commit(update)

    def test_classifies_post_commit_identity_drift_as_ambiguous(self) -> None:
        replacement = self.root / "replacement.sqlite"

        def update(connection: sqlite3.Connection) -> None:
            connection.execute("UPDATE state SET value='new' WHERE id=1")
            shutil.copy2(self.db, replacement)
            replacement.replace(self.db)

        with self.assertRaisesRegex(
            SQLiteMutationAmbiguousError, "post-commit verification is ambiguous"
        ):
            self._capability().commit(update)

    def test_post_commit_admission_drift_requires_fresh_capability(self) -> None:
        admission = self._admission
        stale = dict(admission.__dict__)
        stale["fencing_token"] = "replaced-owner"  # noqa: S105
        reads = 0

        def reread() -> dict[str, object]:
            nonlocal reads
            reads += 1
            return admission.__dict__ if reads == 1 else stale

        def update(connection: sqlite3.Connection) -> None:
            connection.execute("UPDATE state SET value='new' WHERE id=1")

        capability = SQLiteCommitCapability(
            self.db,
            admission=admission,
            admission_reread=reread,
            expected_db_identity=self._capability()._db_identity,
            expected_wal_identity=self._capability()._wal_identity,
            expected_shm_identity=self._capability()._shm_identity,
        )
        with self.assertRaisesRegex(SQLiteMutationAmbiguousError, "post-commit admission"):
            capability.commit(update)
        self.assertEqual(2, reads)
        with closing(sqlite3.connect(self.db)) as connection, connection:
            self.assertEqual(("new",), connection.execute("SELECT value FROM state").fetchone())

        self._admission = CommitAdmissionBundle(
            backend="sqlite",
            target="new",
            operation_id="op-recovered:commit",
            fencing_token="fence-recovered",  # noqa: S106
            state_revision=2,
            barrier_id="barrier-recovered",
            artifact_identity="artifact-1",
            manifest_identity="manifest-1",
            selector_identity="selector-1",
            runtime_identity="runtime-1",
        )

        def recovered(connection: sqlite3.Connection) -> None:
            connection.execute("UPDATE state SET value='recovered' WHERE id=1")

        result = self._capability().commit(recovered)
        self.assertEqual("ok", result.integrity_check)
        with closing(sqlite3.connect(self.db)) as connection, connection:
            self.assertEqual(
                ("recovered",), connection.execute("SELECT value FROM state").fetchone()
            )

    def test_classifies_post_commit_integrity_failure_as_ambiguous(self) -> None:  # noqa: C901
        real_connect = sqlite3.connect

        class BadIntegrityCursor:
            def __init__(self, value: object) -> None:
                self._value = value

            def fetchone(self) -> tuple[object]:
                return (self._value,)

            def fetchall(self) -> list[object]:
                return []

        class BadIntegrityConnection:
            def __init__(self, connection: sqlite3.Connection) -> None:
                self._connection = connection

            def __enter__(self) -> BadIntegrityConnection:
                self._connection.__enter__()
                return self

            def __exit__(self, *args: Any) -> bool | None:
                return self._connection.__exit__(*args)

            def close(self) -> None:
                self._connection.close()

            def execute(self, sql: str, *args: Any) -> object:
                if sql == "PRAGMA integrity_check":
                    return BadIntegrityCursor("database disk image is malformed")
                return self._connection.execute(sql, *args)

        def verification_connector(*args: Any, **kwargs: Any) -> BadIntegrityConnection:
            return BadIntegrityConnection(real_connect(*args, **kwargs))

        with (
            patch.object(sqlite3, "connect", side_effect=verification_connector),
            self.assertRaisesRegex(
                SQLiteMutationAmbiguousError, "post-commit integrity is invalid"
            ),
        ):

            def update(connection: sqlite3.Connection) -> None:
                connection.execute("UPDATE state SET value='new'")

            self._capability().commit(update)

    def test_classifies_identity_drift_after_verification_close_as_ambiguous(self) -> None:
        real_connect = sqlite3.connect
        root = self.root
        db = self.db

        class ReplacingVerificationConnection:
            def __init__(self, connection: sqlite3.Connection) -> None:
                self._connection = connection

            def __enter__(self) -> sqlite3.Connection:
                return self._connection.__enter__()

            def __exit__(self, *args: Any) -> bool | None:
                result = self._connection.__exit__(*args)
                replacement = root / "replacement.sqlite"
                shutil.copy2(db, replacement)
                replacement.replace(db)
                return result

            def __getattr__(self, name: str) -> object:
                return getattr(self._connection, name)

        def verification_connector(*args: Any, **kwargs: Any) -> ReplacingVerificationConnection:
            return ReplacingVerificationConnection(real_connect(*args, **kwargs))

        with (
            patch.object(sqlite3, "connect", side_effect=verification_connector),
            self.assertRaisesRegex(
                SQLiteMutationAmbiguousError, "post-commit verification is ambiguous"
            ),
        ):

            def update(connection: sqlite3.Connection) -> None:
                connection.execute("UPDATE state SET value='new'")

            self._capability().commit(update)

    def test_classifies_post_commit_verification_termination_as_ambiguous(self) -> None:
        with (
            patch.object(sqlite3, "connect", side_effect=KeyboardInterrupt("injected termination")),
            self.assertRaisesRegex(
                SQLiteMutationAmbiguousError, "post-commit verification is ambiguous"
            ),
        ):

            def update(connection: sqlite3.Connection) -> None:
                connection.execute("UPDATE state SET value='new'")

            self._capability().commit(update)

    def test_classifies_connection_close_failure_as_ambiguous(self) -> None:
        real_connect = sqlite3.connect

        class CloseFailingConnection:
            def __init__(self, connection: sqlite3.Connection) -> None:
                self._connection = connection

            def __getattr__(self, name: str) -> object:
                return getattr(self._connection, name)

            def close(self) -> None:
                self._connection.close()
                raise sqlite3.OperationalError("injected close failure")

        def connector(*args: Any, **kwargs: Any) -> sqlite3.Connection:
            return cast(sqlite3.Connection, CloseFailingConnection(real_connect(*args, **kwargs)))

        def update(connection: sqlite3.Connection) -> None:
            connection.execute("UPDATE state SET value='new'")

        with self.assertRaisesRegex(
            SQLiteMutationAmbiguousError, "connection close outcome is ambiguous"
        ):
            SQLiteCommitCapability(
                self.db,
                admission=self._admission,
                admission_reread=lambda: self._admission.__dict__,
                expected_db_identity=self._capability()._db_identity,
                expected_wal_identity=self._capability()._wal_identity,
                expected_shm_identity=self._capability()._shm_identity,
                connector=connector,
            ).commit(update)

    def test_classifies_oserror_connection_close_failure_as_ambiguous(self) -> None:
        real_connect = sqlite3.connect

        class CloseFailingConnection:
            def __init__(self, connection: sqlite3.Connection) -> None:
                self._connection = connection

            def __getattr__(self, name: str) -> object:
                return getattr(self._connection, name)

            def close(self) -> None:
                self._connection.close()
                raise OSError("injected close failure")

        def connector(*args: Any, **kwargs: Any) -> sqlite3.Connection:
            return cast(sqlite3.Connection, CloseFailingConnection(real_connect(*args, **kwargs)))

        def update(connection: sqlite3.Connection) -> None:
            connection.execute("UPDATE state SET value='new'")

        with self.assertRaisesRegex(
            SQLiteMutationAmbiguousError, "connection close outcome is ambiguous"
        ):
            SQLiteCommitCapability(
                self.db,
                admission=self._admission,
                admission_reread=lambda: self._admission.__dict__,
                expected_db_identity=self._capability()._db_identity,
                expected_wal_identity=self._capability()._wal_identity,
                expected_shm_identity=self._capability()._shm_identity,
                connector=connector,
            ).commit(update)

    def test_classifies_termination_connection_close_failure_as_ambiguous(self) -> None:
        real_connect = sqlite3.connect

        class CloseFailingConnection:
            def __init__(self, connection: sqlite3.Connection) -> None:
                self._connection = connection

            def __getattr__(self, name: str) -> object:
                return getattr(self._connection, name)

            def close(self) -> None:
                self._connection.close()
                raise KeyboardInterrupt("injected termination")

        def connector(*args: Any, **kwargs: Any) -> sqlite3.Connection:
            return cast(sqlite3.Connection, CloseFailingConnection(real_connect(*args, **kwargs)))

        def update(connection: sqlite3.Connection) -> None:
            connection.execute("UPDATE state SET value='new'")

        with self.assertRaisesRegex(
            SQLiteMutationAmbiguousError, "connection close outcome is ambiguous"
        ):
            SQLiteCommitCapability(
                self.db,
                admission=self._admission,
                admission_reread=lambda: self._admission.__dict__,
                expected_db_identity=self._capability()._db_identity,
                expected_wal_identity=self._capability()._wal_identity,
                expected_shm_identity=self._capability()._shm_identity,
                connector=connector,
            ).commit(update)

    def test_classifies_rollback_failure_as_ambiguous(self) -> None:
        real_connect = sqlite3.connect

        class RollbackFailingConnection:
            def __init__(self, connection: sqlite3.Connection) -> None:
                self._connection = connection

            def __getattr__(self, name: str) -> object:
                return getattr(self._connection, name)

            def rollback(self) -> None:
                raise sqlite3.OperationalError("injected rollback failure")

        def connector(*args: Any, **kwargs: Any) -> sqlite3.Connection:
            return cast(
                sqlite3.Connection,
                RollbackFailingConnection(real_connect(*args, **kwargs)),
            )

        def invalid(connection: sqlite3.Connection) -> None:
            connection.execute("UPDATE missing SET x=1")

        with self.assertRaisesRegex(SQLiteMutationAmbiguousError, "rollback outcome is ambiguous"):
            capability = SQLiteCommitCapability(
                self.db,
                admission=self._admission,
                admission_reread=lambda: self._admission.__dict__,
                expected_db_identity=self._capability()._db_identity,
                expected_wal_identity=self._capability()._wal_identity,
                expected_shm_identity=self._capability()._shm_identity,
                connector=connector,
            )
            capability.commit(invalid)

    def test_classifies_oserror_rollback_failure_as_ambiguous(self) -> None:
        real_connect = sqlite3.connect

        class RollbackFailingConnection:
            def __init__(self, connection: sqlite3.Connection) -> None:
                self._connection = connection

            def __getattr__(self, name: str) -> object:
                return getattr(self._connection, name)

            def rollback(self) -> None:
                raise OSError("injected rollback failure")

        def connector(*args: Any, **kwargs: Any) -> sqlite3.Connection:
            return cast(
                sqlite3.Connection, RollbackFailingConnection(real_connect(*args, **kwargs))
            )

        def invalid(connection: sqlite3.Connection) -> None:
            connection.execute("UPDATE missing SET x=1")

        with self.assertRaisesRegex(SQLiteMutationAmbiguousError, "rollback outcome is ambiguous"):
            SQLiteCommitCapability(
                self.db,
                admission=self._admission,
                admission_reread=lambda: self._admission.__dict__,
                expected_db_identity=self._capability()._db_identity,
                expected_wal_identity=self._capability()._wal_identity,
                expected_shm_identity=self._capability()._shm_identity,
                connector=connector,
            ).commit(invalid)

    def test_classifies_termination_rollback_failure_as_ambiguous(self) -> None:
        real_connect = sqlite3.connect

        class RollbackFailingConnection:
            def __init__(self, connection: sqlite3.Connection) -> None:
                self._connection = connection

            def __getattr__(self, name: str) -> object:
                return getattr(self._connection, name)

            def rollback(self) -> None:
                raise KeyboardInterrupt("injected termination")

        def connector(*args: Any, **kwargs: Any) -> sqlite3.Connection:
            return cast(
                sqlite3.Connection,
                RollbackFailingConnection(real_connect(*args, **kwargs)),
            )

        def invalid(connection: sqlite3.Connection) -> None:
            connection.execute("UPDATE missing SET x=1")

        with self.assertRaisesRegex(SQLiteMutationAmbiguousError, "rollback outcome is ambiguous"):
            SQLiteCommitCapability(
                self.db,
                admission=self._admission,
                admission_reread=lambda: self._admission.__dict__,
                expected_db_identity=self._capability()._db_identity,
                expected_wal_identity=self._capability()._wal_identity,
                expected_shm_identity=self._capability()._shm_identity,
                connector=connector,
            ).commit(invalid)

    def test_rejects_stale_admission_reread_before_effect(self) -> None:
        stale = dict(self._admission.__dict__)
        stale["state_revision"] = 2
        capability = SQLiteCommitCapability(
            self.db,
            admission=self._admission,
            admission_reread=lambda: stale,
            expected_db_identity=self._capability()._db_identity,
            expected_wal_identity=self._capability()._wal_identity,
            expected_shm_identity=self._capability()._shm_identity,
        )
        called = False

        def update(connection: sqlite3.Connection) -> None:
            nonlocal called
            called = True
            connection.execute("UPDATE state SET value='bad'")

        with self.assertRaisesRegex(SQLiteMutationRejectedError, "admission identity changed"):
            capability.commit(update)
        self.assertFalse(called)
        with closing(sqlite3.connect(self.db)) as connection, connection:
            self.assertEqual(("old",), connection.execute("SELECT value FROM state").fetchone())

    def test_rejects_every_admission_identity_drift_before_effect(self) -> None:
        admission = self._admission
        changes: dict[str, object] = {
            "backend": "git",
            "target": "rollback",
            "operation_id": "foreign-operation",
            "fencing_token": "foreign-fence",
            "state_revision": 2,
            "barrier_id": "foreign-barrier",
            "artifact_identity": "foreign-artifact",
            "manifest_identity": "foreign-manifest",
            "selector_identity": "foreign-selector",
            "runtime_identity": "foreign-runtime",
        }

        for field, value in changes.items():
            stale = dict(admission.__dict__)
            stale[field] = value
            called = False

            def update(connection: sqlite3.Connection) -> None:
                nonlocal called
                called = True
                connection.execute("UPDATE state SET value='bad'")

            def read_stale(value: dict[str, object] = stale) -> dict[str, object]:
                return value

            capability = SQLiteCommitCapability(
                self.db,
                admission=admission,
                admission_reread=read_stale,
                expected_db_identity=self._capability()._db_identity,
                expected_wal_identity=self._capability()._wal_identity,
                expected_shm_identity=self._capability()._shm_identity,
            )
            with (
                self.subTest(field=field),
                self.assertRaisesRegex(SQLiteMutationRejectedError, "admission identity changed"),
            ):
                capability.commit(update)
            self.assertFalse(called)
            with closing(sqlite3.connect(self.db)) as connection, connection:
                self.assertEqual(("old",), connection.execute("SELECT value FROM state").fetchone())


if __name__ == "__main__":
    unittest.main()
