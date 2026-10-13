# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Private durable intents for the opt-in Git receipt protocol.

This module does not execute transitions or issue completion acknowledgements.
Only a bound service may turn an intent into a signed authority commit.
"""

from __future__ import annotations

import fcntl
import hashlib
import json
import os
import re
import sqlite3
import stat
import uuid
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path
from typing import Any

if __package__:
    from .sqlite_storage import require_local_filesystem
else:  # pragma: no cover - direct vendored import
    from sqlite_storage import require_local_filesystem  # type: ignore[import-not-found,no-redef]

_TOKEN = re.compile(r"[A-Za-z0-9._:-]{1,128}\Z")
_PRIORITIES = frozenset(("P0", "P1", "P2", "P3", "P4"))
_MAX_SUMMARY = 4000
_MAX_NEXT_ACTION = 1024
_PHASE_QUEUED = "queued-local"
_PHASE_RUNNING = "running"
_PHASE_LOCAL = "completed-local"
_PHASE_REMOTE = "published-remote"
_PHASE_REJECTED = "rejected"
_PHASE_AMBIGUOUS = "ambiguous"
_COMMIT = re.compile(r"[0-9a-f]{40}\Z")
_PUBLICATION_QUEUED = "queued"
_PUBLICATION_PUBLISHING = "publishing"
_PUBLICATION_PUBLISHED = "published"
_PUBLICATION_REJECTED = "rejected"
_PUBLICATION_AMBIGUOUS = "ambiguous"


class ReceiptConflictError(RuntimeError):
    """One idempotency key was submitted with different canonical content."""


def validate_update_changes(changes: object) -> dict[str, str]:
    """Accept only an update that strict task and session validation can commit."""
    allowed = {"status", "priority", "summary", "next_action"}
    if (
        not isinstance(changes, dict)
        or not changes
        or set(changes) - allowed
        or not all(
            isinstance(name, str) and isinstance(value, str) for name, value in changes.items()
        )
        or (
            "summary" in changes
            and (not 1 <= len(changes["summary"]) <= _MAX_SUMMARY or "\x00" in changes["summary"])
        )
        or (
            "next_action" in changes
            and (
                not 1 <= len(changes["next_action"]) <= _MAX_NEXT_ACTION
                or "\x00" in changes["next_action"]
                or "\n" in changes["next_action"]
            )
        )
        or changes.get("status") not in {None, "in_progress"}
        or changes.get("priority") not in {None, *_PRIORITIES}
    ):
        raise ValueError("invalid fast update changes")
    return changes


class ReceiptStore:
    """A per-Git-common-directory SQLite WAL intent queue."""

    def __init__(self, path: Path, project_id: str) -> None:
        uuid.UUID(project_id)
        self.project_id = project_id
        self.path = path
        if sqlite3.sqlite_version_info < (3, 37, 0):
            raise RuntimeError("SQLITE_VERSION_UNSUPPORTED: SQLite 3.37 or newer is required")
        require_local_filesystem(path)
        self._parent_fd, self._database_fd = self._open_private_path()
        self._sidecar_fds: dict[str, int] = {}
        try:
            self.connection = sqlite3.connect(path, timeout=10, isolation_level=None)
            self.connection.row_factory = sqlite3.Row
            self.connection.execute("PRAGMA busy_timeout=10000")
            if not self._schema_ready():
                fcntl.flock(self._database_fd, fcntl.LOCK_EX)
                try:
                    if not self._schema_ready():
                        mode = str(
                            self.connection.execute("PRAGMA journal_mode=WAL").fetchone()[0]
                        ).lower()
                        if mode != "wal":
                            raise RuntimeError("SQLITE_WAL_UNAVAILABLE: journal mode is not WAL")
                        self._initialize()
                finally:
                    fcntl.flock(self._database_fd, fcntl.LOCK_UN)
            self.connection.execute("PRAGMA synchronous=FULL")
            self._assert_path()
            self._retain_sidecars()
            os.fsync(self._parent_fd)
            self._closed = False
        except BaseException:
            if hasattr(self, "connection"):
                self.connection.close()
            for descriptor in self._sidecar_fds.values():
                os.close(descriptor)
            os.close(self._database_fd)
            os.close(self._parent_fd)
            raise

    def _open_private_path(self) -> tuple[int, int]:
        parent = self.path.parent
        parent.mkdir(mode=0o700, exist_ok=True)
        ancestor_fd = os.open(parent.parent, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
        try:
            os.fsync(ancestor_fd)
        finally:
            os.close(ancestor_fd)
        info = parent.lstat()
        if not stat.S_ISDIR(info.st_mode) or info.st_uid != os.geteuid() or info.st_mode & 0o077:
            raise RuntimeError("receipt directory is not private")
        if self.path.is_symlink():
            raise RuntimeError("receipt database must not be a symlink")
        parent_fd = os.open(parent, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
        try:
            try:
                database_fd = os.open(
                    self.path.name,
                    os.O_RDWR | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW,
                    0o600,
                    dir_fd=parent_fd,
                )
            except FileExistsError:
                database_fd = os.open(self.path.name, os.O_RDWR | os.O_NOFOLLOW, dir_fd=parent_fd)
            info = os.fstat(database_fd)
            if (
                not stat.S_ISREG(info.st_mode)
                or info.st_uid != os.geteuid()
                or info.st_nlink != 1
                or stat.S_IMODE(info.st_mode) != 0o600
            ):
                os.close(database_fd)
                raise RuntimeError("receipt database is not a private regular owned file")
            os.fsync(parent_fd)
            return parent_fd, database_fd
        except BaseException:
            os.close(parent_fd)
            raise

    def _assert_path(self) -> None:
        self._assert_database_path()
        self._assert_sidecars()

    def _assert_database_path(self) -> None:
        parent = os.fstat(self._parent_fd)
        current_parent = self.path.parent.lstat()
        database = os.fstat(self._database_fd)
        current_database = os.stat(self.path.name, dir_fd=self._parent_fd, follow_symlinks=False)
        if (
            (parent.st_dev, parent.st_ino) != (current_parent.st_dev, current_parent.st_ino)
            or current_parent.st_uid != os.geteuid()
            or stat.S_IMODE(current_parent.st_mode) & 0o077
            or (database.st_dev, database.st_ino)
            != (current_database.st_dev, current_database.st_ino)
            or not stat.S_ISREG(current_database.st_mode)
            or current_database.st_nlink != 1
            or stat.S_IMODE(current_database.st_mode) != 0o600
        ):
            raise RuntimeError("receipt database path identity changed")

    def _assert_sidecars(self) -> None:
        for suffix in ("-wal", "-shm"):
            try:
                sidecar = os.stat(
                    self.path.name + suffix, dir_fd=self._parent_fd, follow_symlinks=False
                )
            except FileNotFoundError:
                continue
            if (
                not stat.S_ISREG(sidecar.st_mode)
                or sidecar.st_uid != os.geteuid()
                or sidecar.st_nlink != 1
                or stat.S_IMODE(sidecar.st_mode) != 0o600
            ):
                raise RuntimeError("receipt database sidecar is unsafe")
            retained = self._sidecar_fds.get(suffix)
            if retained is not None:
                status = os.fstat(retained)
                if (status.st_dev, status.st_ino) != (sidecar.st_dev, sidecar.st_ino):
                    raise RuntimeError("receipt database sidecar identity changed")

    def _retain_sidecars(self) -> None:
        for suffix in ("-wal", "-shm"):
            try:
                descriptor = os.open(
                    self.path.name + suffix,
                    os.O_RDWR | os.O_NOFOLLOW,
                    dir_fd=self._parent_fd,
                )
            except OSError as error:
                raise RuntimeError("receipt WAL sidecar is unavailable") from error
            self._sidecar_fds[suffix] = descriptor
        self._assert_path()

    def _schema_ready(self) -> bool:
        """Hot opens do not acquire the SQLite write transaction or change WAL mode."""
        try:
            mode = str(self.connection.execute("PRAGMA journal_mode").fetchone()[0]).lower()
            version = self.connection.execute("PRAGMA user_version").fetchone()[0]
        except sqlite3.OperationalError as error:
            if "locked" not in str(error).lower():
                raise
            return False
        if mode != "wal" or version != 5:
            return False
        binding = self.connection.execute(
            "SELECT project_id FROM receipt_binding WHERE singleton=1"
        ).fetchone()
        if binding is None:
            raise RuntimeError("receipt database has no project binding")
        if binding["project_id"] != self.project_id:
            raise RuntimeError("receipt database is bound to a different project")
        required = {
            "intents": {
                "receipt_id",
                "project_id",
                "idempotency_key",
                "operation",
                "task_id",
                "expected_revision",
                "payload_json",
                "input_digest",
                "phase",
                "started_at",
                "commit_oid",
                "result_revision",
                "error_code",
                "remote_oid",
                "remote_observed_at",
                "publication_error",
                "created_at",
            },
            "publication_jobs": {
                "job_id",
                "project_id",
                "idempotency_key",
                "candidate_oid",
                "expected_remote_oid",
                "phase",
                "publisher_lease",
                "publisher_lease_expires",
                "observed_remote_oid",
                "error_code",
                "created_at",
                "updated_at",
            },
            "publication_request_keys": {
                "project_id",
                "idempotency_key",
                "job_id",
                "candidate_oid",
                "expected_remote_oid",
            },
        }
        for table, columns in required.items():
            found = {
                str(row[1])
                for row in self.connection.execute(f"PRAGMA table_info({table})").fetchall()
            }
            if not columns <= found:
                return False
        jobs_unique = self._has_unique_index("publication_jobs", ("project_id", "candidate_oid"))
        keys_unique = self._has_unique_index(
            "publication_request_keys", ("project_id", "idempotency_key")
        )
        return jobs_unique and keys_unique

    def _has_unique_index(self, table: str, columns: tuple[str, ...]) -> bool:
        for row in self.connection.execute(f"PRAGMA index_list({table})").fetchall():
            if not row[2]:
                continue
            name = str(row[1])
            indexed = tuple(
                str(item[2])
                for item in self.connection.execute(f"PRAGMA index_info({name})").fetchall()
            )
            if indexed == columns:
                return True
        return False

    def _initialize(self) -> None:
        try:
            self.connection.execute("BEGIN IMMEDIATE")
            version = self.connection.execute("PRAGMA user_version").fetchone()[0]
            if version not in (0, 3, 4, 5):
                raise RuntimeError("unsupported receipt database schema")
            self.connection.execute(
                """CREATE TABLE IF NOT EXISTS receipt_binding (
                    singleton INTEGER PRIMARY KEY CHECK (singleton = 1),
                    project_id TEXT NOT NULL
                )"""
            )
            binding = self.connection.execute(
                "SELECT project_id FROM receipt_binding WHERE singleton=1"
            ).fetchone()
            if binding is None:
                self.connection.execute(
                    "INSERT INTO receipt_binding(singleton, project_id) VALUES (1, ?)",
                    (self.project_id,),
                )
            elif binding["project_id"] != self.project_id:
                raise RuntimeError("receipt database is bound to a different project")
            self.connection.execute(
                """CREATE TABLE IF NOT EXISTS intents (
                    receipt_id TEXT PRIMARY KEY,
                    project_id TEXT NOT NULL,
                    idempotency_key TEXT NOT NULL,
                    operation TEXT NOT NULL,
                    task_id TEXT NOT NULL,
                    expected_revision INTEGER NOT NULL,
                    payload_json TEXT NOT NULL,
                    input_digest TEXT NOT NULL,
                    phase TEXT NOT NULL CHECK (
                        phase IN ('queued-local', 'running', 'completed-local',
                                  'published-remote', 'rejected', 'ambiguous')
                    ),
                    started_at TEXT,
                    commit_oid TEXT,
                    result_revision INTEGER,
                    error_code TEXT,
                    remote_oid TEXT,
                    remote_observed_at TEXT,
                    publication_error TEXT,
                    created_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),
                    UNIQUE(project_id, idempotency_key)
                )"""
            )
            self.connection.execute(
                """CREATE TABLE IF NOT EXISTS publication_jobs (
                    job_id TEXT PRIMARY KEY,
                    project_id TEXT NOT NULL,
                    idempotency_key TEXT NOT NULL,
                    candidate_oid TEXT NOT NULL,
                    expected_remote_oid TEXT NOT NULL,
                    phase TEXT NOT NULL CHECK (
                        phase IN ('queued', 'publishing', 'published', 'rejected', 'ambiguous')
                    ),
                    publisher_lease TEXT,
                    publisher_lease_expires TEXT,
                    observed_remote_oid TEXT,
                    error_code TEXT,
                    created_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),
                    updated_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),
                    UNIQUE(project_id, idempotency_key),
                    UNIQUE(project_id, candidate_oid)
                )"""
            )
            self.connection.execute(
                """CREATE TABLE IF NOT EXISTS publication_request_keys (
                    project_id TEXT NOT NULL,
                    idempotency_key TEXT NOT NULL,
                    job_id TEXT NOT NULL,
                    candidate_oid TEXT NOT NULL,
                    expected_remote_oid TEXT NOT NULL,
                    PRIMARY KEY (project_id, idempotency_key),
                    FOREIGN KEY (job_id) REFERENCES publication_jobs(job_id)
                )"""
            )
            self.connection.execute("PRAGMA user_version=5")
            if not self._schema_ready():
                raise RuntimeError("receipt database schema is incomplete")
            self.connection.execute(
                """INSERT OR IGNORE INTO publication_request_keys
                (project_id, idempotency_key, job_id, candidate_oid, expected_remote_oid)
                SELECT project_id, idempotency_key, job_id, candidate_oid, expected_remote_oid
                FROM publication_jobs"""
            )
            self._assert_path()
            self.connection.execute("COMMIT")
        except BaseException:
            self.connection.execute("ROLLBACK")
            raise
        self._assert_path()

    def close(self) -> None:
        if self._closed:
            return
        self._closed = True
        self.connection.close()
        for descriptor in self._sidecar_fds.values():
            os.close(descriptor)
        os.close(self._database_fd)
        os.close(self._parent_fd)

    def __enter__(self) -> ReceiptStore:
        return self

    def __exit__(self, _kind: object, _value: object, _traceback: object) -> None:
        self.close()

    @contextmanager
    def _transaction(self) -> Iterator[None]:
        self._assert_path()
        self.connection.execute("BEGIN IMMEDIATE")
        committed = False
        try:
            yield
            self._assert_path()
            self.connection.execute("COMMIT")
            committed = True
            self._assert_path()
        except BaseException:
            if not committed:
                self.connection.execute("ROLLBACK")
            raise

    def enqueue_heartbeat(
        self,
        *,
        key: str,
        task: str,
        owner: str,
        expected_revision: int,
        lease_minutes: int,
    ) -> dict[str, Any]:
        """Fsync a typed intent; no task transition has happened at return."""
        if not _TOKEN.fullmatch(key) or not _TOKEN.fullmatch(task):
            raise ValueError("invalid receipt key or task")
        if not _TOKEN.fullmatch(owner):
            raise ValueError("invalid owner")
        if expected_revision < 1 or not 1 <= lease_minutes <= 1440:
            raise ValueError("invalid revision or lease")
        payload = {
            "expected_revision": expected_revision,
            "lease_minutes": lease_minutes,
            "operation": "heartbeat",
            "owner": owner,
            "project_id": self.project_id,
            "task": task,
        }
        return self._enqueue(
            key=key, task=task, expected_revision=expected_revision, payload=payload
        )

    def enqueue_claim(
        self,
        *,
        key: str,
        task: str,
        owner: str,
        expected_revision: int,
        lease_minutes: int,
        worker_pid: int | None = None,
        worker_start_time: int | None = None,
    ) -> dict[str, Any]:
        """Fsync a revision-fenced claim intent; authority admission stays strict."""
        if not _TOKEN.fullmatch(key) or not _TOKEN.fullmatch(task):
            raise ValueError("invalid receipt key or task")
        if not _TOKEN.fullmatch(owner):
            raise ValueError("invalid owner")
        if expected_revision < 1 or not 1 <= lease_minutes <= 1440:
            raise ValueError("invalid revision or lease")
        if (worker_pid is None) != (worker_start_time is None) or (
            worker_pid is not None
            and (
                type(worker_pid) is not int
                or worker_pid <= 0
                or type(worker_start_time) is not int
                or worker_start_time < 0
            )
        ):
            raise ValueError("invalid claim worker identity")
        payload = {
            "expected_revision": expected_revision,
            "lease_minutes": lease_minutes,
            "operation": "claim",
            "owner": owner,
            "project_id": self.project_id,
            "task": task,
        }
        if worker_pid is not None:
            payload["worker_pid"] = worker_pid
            payload["worker_start_time"] = worker_start_time
        return self._enqueue(
            key=key, task=task, expected_revision=expected_revision, payload=payload
        )

    def enqueue_promote(
        self, *, key: str, task: str, expected_revision: int, note: str
    ) -> dict[str, Any]:
        """Fsync a fenced promote intent; strict dependency admission is deferred."""
        if not isinstance(note, str) or not 1 <= len(note) <= 4096 or "\x00" in note:
            raise ValueError("invalid promote note")
        payload = {
            "expected_revision": expected_revision,
            "note": note,
            "operation": "promote",
            "project_id": self.project_id,
            "task": task,
        }
        return self._enqueue(
            key=key, task=task, expected_revision=expected_revision, payload=payload
        )

    def enqueue_update(
        self,
        *,
        key: str,
        task: str,
        owner: str,
        expected_revision: int,
        changes: dict[str, str],
        note: str,
    ) -> dict[str, Any]:
        """Fsync a closed owner-held metadata update for later strict admission."""
        if (
            not _TOKEN.fullmatch(key)
            or not _TOKEN.fullmatch(task)
            or not _TOKEN.fullmatch(owner)
            or not isinstance(expected_revision, int)
            or isinstance(expected_revision, bool)
            or expected_revision < 1
            or not isinstance(note, str)
            or not 1 <= len(note) <= 4096
            or "\x00" in note
        ):
            raise ValueError("invalid update receipt intent")
        try:
            validated_changes = validate_update_changes(changes)
        except ValueError as error:
            raise ValueError("invalid update receipt intent") from error
        payload = {
            "changes": dict(sorted(validated_changes.items())),
            "expected_revision": expected_revision,
            "note": note,
            "operation": "update",
            "owner": owner,
            "project_id": self.project_id,
            "task": task,
        }
        return self._enqueue(
            key=key, task=task, expected_revision=expected_revision, payload=payload
        )

    def _enqueue(
        self, *, key: str, task: str, expected_revision: int, payload: dict[str, Any]
    ) -> dict[str, Any]:
        """Store one canonical, operation-closed intent under its idempotency key."""
        if not _TOKEN.fullmatch(key) or not _TOKEN.fullmatch(task) or expected_revision < 1:
            raise ValueError("invalid receipt key, task, or revision")
        canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
        digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
        operation = payload.get("operation")
        if not isinstance(operation, str):
            raise ValueError("invalid receipt operation")
        with self._transaction():
            existing = self.connection.execute(
                "SELECT * FROM intents WHERE project_id=? AND idempotency_key=?",
                (self.project_id, key),
            ).fetchone()
            if existing is None:
                receipt_id = uuid.uuid4().hex
                self.connection.execute(
                    """INSERT INTO intents
                    (receipt_id, project_id, idempotency_key, operation, task_id,
                     expected_revision, payload_json, input_digest, phase)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                    (
                        receipt_id,
                        self.project_id,
                        key,
                        operation,
                        task,
                        expected_revision,
                        canonical,
                        digest,
                        _PHASE_QUEUED,
                    ),
                )
                existing = self.connection.execute(
                    "SELECT * FROM intents WHERE receipt_id=?", (receipt_id,)
                ).fetchone()
            if existing is None:
                raise RuntimeError("receipt insert was not visible")
            if existing["input_digest"] != digest or existing["payload_json"] != canonical:
                raise ReceiptConflictError("idempotency key already binds different input")
            return dict(existing)

    def claim_next(self) -> dict[str, Any] | None:
        """Reserve one queued intent; a crashed reservation is not replayed blindly."""
        with self._transaction():
            selected = self.connection.execute(
                """SELECT receipt_id FROM intents
                WHERE project_id=? AND phase=?
                ORDER BY created_at, rowid LIMIT 1""",
                (self.project_id, _PHASE_QUEUED),
            ).fetchone()
            if selected is None:
                return None
            receipt_id = str(selected["receipt_id"])
            self.connection.execute(
                """UPDATE intents SET phase=?, started_at=strftime('%Y-%m-%dT%H:%M:%fZ','now')
                WHERE receipt_id=? AND project_id=? AND phase=?""",
                (_PHASE_RUNNING, receipt_id, self.project_id, _PHASE_QUEUED),
            )
            row = self.connection.execute(
                "SELECT * FROM intents WHERE receipt_id=? AND project_id=?",
                (receipt_id, self.project_id),
            ).fetchone()
            if row is None or row["phase"] != _PHASE_RUNNING:
                raise RuntimeError("receipt reservation was not visible")
            return dict(row)

    def _finish_running(
        self,
        receipt_id: str,
        phase: str,
        *,
        commit_oid: str | None = None,
        result_revision: int | None = None,
        error_code: str | None = None,
    ) -> dict[str, Any]:
        if not re.fullmatch(r"[0-9a-f]{32}", receipt_id):
            raise ValueError("invalid receipt id")
        with self._transaction():
            row = self.connection.execute(
                "SELECT * FROM intents WHERE receipt_id=? AND project_id=?",
                (receipt_id, self.project_id),
            ).fetchone()
            if row is None:
                raise RuntimeError("unknown receipt")
            if row["phase"] == phase:
                if (
                    row["commit_oid"] != commit_oid
                    or row["result_revision"] != result_revision
                    or row["error_code"] != error_code
                ):
                    raise ReceiptConflictError("receipt outcome differs")
            elif row["phase"] != _PHASE_RUNNING:
                raise RuntimeError("receipt is not running")
            else:
                self.connection.execute(
                    """UPDATE intents SET phase=?, commit_oid=?, result_revision=?,
                    error_code=? WHERE receipt_id=? AND project_id=? AND phase=?""",
                    (
                        phase,
                        commit_oid,
                        result_revision,
                        error_code,
                        receipt_id,
                        self.project_id,
                        _PHASE_RUNNING,
                    ),
                )
            current = self.connection.execute(
                "SELECT * FROM intents WHERE receipt_id=? AND project_id=?",
                (receipt_id, self.project_id),
            ).fetchone()
            if current is None or current["phase"] != phase:
                raise RuntimeError("receipt outcome was not visible")
            return dict(current)

    def record_local_commit(
        self, receipt_id: str, commit_oid: str, result_revision: int
    ) -> dict[str, Any]:
        """Record a service-verified signed commit, never just a queued intent."""
        if not _COMMIT.fullmatch(commit_oid) or result_revision < 2:
            raise ValueError("invalid local commit evidence")
        receipt = self.read(receipt_id)
        if receipt is None or result_revision != receipt["expected_revision"] + 1:
            raise ValueError("commit revision does not match queued fence")
        return self._finish_running(
            receipt_id, _PHASE_LOCAL, commit_oid=commit_oid, result_revision=result_revision
        )

    def record_rejection(self, receipt_id: str, error_code: str) -> dict[str, Any]:
        if not _TOKEN.fullmatch(error_code):
            raise ValueError("invalid rejection code")
        return self._finish_running(receipt_id, _PHASE_REJECTED, error_code=error_code)

    def record_ambiguity(self, receipt_id: str, error_code: str) -> dict[str, Any]:
        if not _TOKEN.fullmatch(error_code):
            raise ValueError("invalid ambiguity code")
        return self._finish_running(receipt_id, _PHASE_AMBIGUOUS, error_code=error_code)

    def read(self, receipt_id: str) -> dict[str, Any] | None:
        if not re.fullmatch(r"[0-9a-f]{32}", receipt_id):
            raise ValueError("invalid receipt id")
        self._assert_path()
        row = self.connection.execute(
            "SELECT * FROM intents WHERE project_id=? AND receipt_id=?",
            (self.project_id, receipt_id),
        ).fetchone()
        self._assert_path()
        return None if row is None else dict(row)

    def running(self) -> list[dict[str, Any]]:
        """List interrupted reservations for single-service startup recovery."""
        self._assert_path()
        rows = self.connection.execute(
            "SELECT * FROM intents WHERE project_id=? AND phase=? ORDER BY started_at, rowid",
            (self.project_id, _PHASE_RUNNING),
        ).fetchall()
        self._assert_path()
        return [dict(row) for row in rows]

    def pending_publication(self) -> list[dict[str, Any]]:
        self._assert_path()
        rows = self.connection.execute(
            "SELECT * FROM intents WHERE project_id=? AND phase=? ORDER BY created_at, rowid",
            (self.project_id, _PHASE_LOCAL),
        ).fetchall()
        self._assert_path()
        return [dict(row) for row in rows]

    def record_remote_observation(self, receipt_id: str, remote_oid: str) -> dict[str, Any]:
        """Store a service-verified exact remote ref observation."""
        if not _COMMIT.fullmatch(remote_oid):
            raise ValueError("invalid observed remote oid")
        with self._transaction():
            row = self.connection.execute(
                "SELECT * FROM intents WHERE project_id=? AND receipt_id=?",
                (self.project_id, receipt_id),
            ).fetchone()
            if row is None or row["phase"] not in (_PHASE_LOCAL, _PHASE_REMOTE):
                raise RuntimeError("receipt has no local commit to publish")
            if row["phase"] == _PHASE_REMOTE and row["remote_oid"] != remote_oid:
                raise ReceiptConflictError("remote receipt already binds another observation")
            if row["phase"] == _PHASE_LOCAL:
                self.connection.execute(
                    """UPDATE intents SET phase=?, remote_oid=?,
                    remote_observed_at=strftime('%Y-%m-%dT%H:%M:%fZ','now'),
                    publication_error=NULL WHERE project_id=? AND receipt_id=?""",
                    (_PHASE_REMOTE, remote_oid, self.project_id, receipt_id),
                )
            current = self.connection.execute(
                "SELECT * FROM intents WHERE project_id=? AND receipt_id=?",
                (self.project_id, receipt_id),
            ).fetchone()
            if current is None:
                raise RuntimeError("remote receipt was not visible")
            return dict(current)

    def record_publication_failure(self, receipt_id: str, code: str) -> dict[str, Any]:
        if not _TOKEN.fullmatch(code):
            raise ValueError("invalid publication failure code")
        with self._transaction():
            self.connection.execute(
                """UPDATE intents SET publication_error=?
                WHERE project_id=? AND receipt_id=? AND phase=?""",
                (code, self.project_id, receipt_id, _PHASE_LOCAL),
            )
            row = self.connection.execute(
                "SELECT * FROM intents WHERE project_id=? AND receipt_id=?",
                (self.project_id, receipt_id),
            ).fetchone()
            if row is None or row["phase"] != _PHASE_LOCAL:
                raise RuntimeError("receipt is not locally completed")
            return dict(row)

    def admit_publication(
        self, *, key: str, candidate_oid: str, expected_remote_oid: str
    ) -> dict[str, Any]:
        """Durably admit one protected-main candidate before any remote I/O.

        Candidate identity is global per bound project.  A retry under the
        same key must retain its exact descriptor; a second key may discover
        the existing identical candidate but can never create a second job.
        A changed remote base is intentionally a different descriptor and
        requires a newly rebuilt candidate rather than an unsafe replay.
        """
        if (
            not _TOKEN.fullmatch(key)
            or not _COMMIT.fullmatch(candidate_oid)
            or not _COMMIT.fullmatch(expected_remote_oid)
            or candidate_oid == expected_remote_oid
        ):
            raise ValueError("invalid publication admission")
        with self._transaction():
            by_key = self.connection.execute(
                """SELECT publication_jobs.* FROM publication_request_keys
                JOIN publication_jobs ON publication_jobs.job_id=publication_request_keys.job_id
                WHERE publication_request_keys.project_id=?
                AND publication_request_keys.idempotency_key=?""",
                (self.project_id, key),
            ).fetchone()
            if by_key is not None:
                if (
                    by_key["candidate_oid"] != candidate_oid
                    or by_key["expected_remote_oid"] != expected_remote_oid
                ):
                    raise ReceiptConflictError("publication key already binds different input")
                return dict(by_key)
            by_candidate = self.connection.execute(
                """SELECT * FROM publication_jobs
                WHERE project_id=? AND candidate_oid=?""",
                (self.project_id, candidate_oid),
            ).fetchone()
            if by_candidate is not None:
                if by_candidate["expected_remote_oid"] != expected_remote_oid:
                    raise ReceiptConflictError("candidate already binds another remote base")
                self.connection.execute(
                    """INSERT INTO publication_request_keys
                    (project_id, idempotency_key, job_id, candidate_oid, expected_remote_oid)
                    VALUES (?, ?, ?, ?, ?)""",
                    (
                        self.project_id,
                        key,
                        by_candidate["job_id"],
                        candidate_oid,
                        expected_remote_oid,
                    ),
                )
                return dict(by_candidate)
            job_id = uuid.uuid4().hex
            self.connection.execute(
                """INSERT INTO publication_jobs
                (job_id, project_id, idempotency_key, candidate_oid, expected_remote_oid, phase)
                VALUES (?, ?, ?, ?, ?, ?)""",
                (
                    job_id,
                    self.project_id,
                    key,
                    candidate_oid,
                    expected_remote_oid,
                    _PUBLICATION_QUEUED,
                ),
            )
            self.connection.execute(
                """INSERT INTO publication_request_keys
                (project_id, idempotency_key, job_id, candidate_oid, expected_remote_oid)
                VALUES (?, ?, ?, ?, ?)""",
                (self.project_id, key, job_id, candidate_oid, expected_remote_oid),
            )
            row = self.connection.execute(
                "SELECT * FROM publication_jobs WHERE project_id=? AND job_id=?",
                (self.project_id, job_id),
            ).fetchone()
            if row is None:
                raise RuntimeError("publication admission was not visible")
            return dict(row)

    def read_publication(self, job_id: str) -> dict[str, Any] | None:
        if not re.fullmatch(r"[0-9a-f]{32}", job_id):
            raise ValueError("invalid publication job id")
        self._assert_path()
        row = self.connection.execute(
            "SELECT * FROM publication_jobs WHERE project_id=? AND job_id=?",
            (self.project_id, job_id),
        ).fetchone()
        self._assert_path()
        return None if row is None else dict(row)

    def publication_for_candidate(self, candidate_oid: str) -> dict[str, Any] | None:
        if not _COMMIT.fullmatch(candidate_oid):
            raise ValueError("invalid publication candidate")
        self._assert_path()
        row = self.connection.execute(
            """SELECT * FROM publication_jobs
            WHERE project_id=? AND candidate_oid=?""",
            (self.project_id, candidate_oid),
        ).fetchone()
        self._assert_path()
        return None if row is None else dict(row)

    def recoverable_publications(self) -> list[dict[str, Any]]:
        """Return nonterminal jobs for a fresh remote observation and head decision."""
        self._assert_path()
        rows = self.connection.execute(
            """SELECT * FROM publication_jobs WHERE project_id=?
            AND (phase=? OR phase=? OR (phase=? AND publisher_lease_expires <
                 strftime('%Y-%m-%dT%H:%M:%fZ','now')))
            ORDER BY created_at, job_id""",
            (
                self.project_id,
                _PUBLICATION_QUEUED,
                _PUBLICATION_AMBIGUOUS,
                _PUBLICATION_PUBLISHING,
            ),
        ).fetchall()
        self._assert_path()
        return [dict(row) for row in rows]

    def resolve_superseded_publication(
        self, job_id: str, *, observed_remote_oid: str
    ) -> dict[str, Any]:
        """Terminally resolve a queued candidate that is no longer local main."""
        if not re.fullmatch(r"[0-9a-f]{32}", job_id) or not _COMMIT.fullmatch(observed_remote_oid):
            raise ValueError("invalid superseded publication resolution")
        with self._transaction():
            row = self.connection.execute(
                "SELECT * FROM publication_jobs WHERE project_id=? AND job_id=?",
                (self.project_id, job_id),
            ).fetchone()
            if row is None:
                raise RuntimeError("unknown publication job")
            if row["phase"] != _PUBLICATION_QUEUED:
                raise RuntimeError("publication job is not queued")
            if observed_remote_oid == row["candidate_oid"]:
                phase, error = _PUBLICATION_PUBLISHED, None
            elif observed_remote_oid == row["expected_remote_oid"]:
                phase, error = _PUBLICATION_REJECTED, "LOCAL_HEAD_SUPERSEDED"
            else:
                phase, error = _PUBLICATION_REJECTED, "REMOTE_BASE_CHANGED"
            updated = self.connection.execute(
                """UPDATE publication_jobs SET phase=?, observed_remote_oid=?, error_code=?,
                updated_at=strftime('%Y-%m-%dT%H:%M:%fZ','now')
                WHERE project_id=? AND job_id=? AND phase=?""",
                (phase, observed_remote_oid, error, self.project_id, job_id, _PUBLICATION_QUEUED),
            )
            if updated.rowcount != 1:
                raise RuntimeError("publication job changed while resolving")
            resolved = self.connection.execute(
                "SELECT * FROM publication_jobs WHERE project_id=? AND job_id=?",
                (self.project_id, job_id),
            ).fetchone()
            if resolved is None or resolved["phase"] != phase:
                raise RuntimeError("publication resolution was not visible")
            return dict(resolved)

    def claim_publication(self, job_id: str, *, lease: str) -> dict[str, Any] | None:
        """Lease one queued job; a caller owns at most its returned lease token."""
        if not re.fullmatch(r"[0-9a-f]{32}", job_id) or not re.fullmatch(r"[0-9a-f]{32}", lease):
            raise ValueError("invalid publication claim")
        with self._transaction():
            row = self.connection.execute(
                "SELECT * FROM publication_jobs WHERE project_id=? AND job_id=?",
                (self.project_id, job_id),
            ).fetchone()
            if row is None:
                return None
            if row["phase"] != _PUBLICATION_QUEUED:
                return None
            self.connection.execute(
                """UPDATE publication_jobs SET phase=?, publisher_lease=?,
                publisher_lease_expires=strftime('%Y-%m-%dT%H:%M:%fZ','now','+60 seconds'),
                error_code=NULL, updated_at=strftime('%Y-%m-%dT%H:%M:%fZ','now')
                WHERE project_id=? AND job_id=? AND phase=?""",
                (_PUBLICATION_PUBLISHING, lease, self.project_id, job_id, _PUBLICATION_QUEUED),
            )
            claimed = self.connection.execute(
                "SELECT * FROM publication_jobs WHERE project_id=? AND job_id=?",
                (self.project_id, job_id),
            ).fetchone()
            if claimed is None or claimed["phase"] != _PUBLICATION_PUBLISHING:
                raise RuntimeError("publication claim was not visible")
            return dict(claimed)

    def finish_publication(
        self,
        job_id: str,
        *,
        lease: str,
        phase: str,
        observed_remote_oid: str | None = None,
        error_code: str | None = None,
    ) -> dict[str, Any]:
        """Record a verified terminal remote outcome for the owning publisher."""
        if (
            not re.fullmatch(r"[0-9a-f]{32}", job_id)
            or not re.fullmatch(r"[0-9a-f]{32}", lease)
            or phase not in {_PUBLICATION_PUBLISHED, _PUBLICATION_REJECTED, _PUBLICATION_AMBIGUOUS}
            or (observed_remote_oid is not None and not _COMMIT.fullmatch(observed_remote_oid))
            or (error_code is not None and not _TOKEN.fullmatch(error_code))
            or (phase == _PUBLICATION_PUBLISHED and observed_remote_oid is None)
            or (phase == _PUBLICATION_AMBIGUOUS and observed_remote_oid is not None)
            or (phase != _PUBLICATION_PUBLISHED and error_code is None)
        ):
            raise ValueError("invalid publication outcome")
        with self._transaction():
            row = self.connection.execute(
                "SELECT * FROM publication_jobs WHERE project_id=? AND job_id=?",
                (self.project_id, job_id),
            ).fetchone()
            if row is None:
                raise RuntimeError("unknown publication job")
            if row["phase"] == phase:
                if (
                    row["publisher_lease"] != lease
                    or row["observed_remote_oid"] != observed_remote_oid
                    or row["error_code"] != error_code
                ):
                    raise ReceiptConflictError("publication outcome differs")
                return dict(row)
            if row["phase"] != _PUBLICATION_PUBLISHING or row["publisher_lease"] != lease:
                raise RuntimeError("publication job is not owned by this publisher")
            if phase == _PUBLICATION_PUBLISHED and observed_remote_oid != row["candidate_oid"]:
                raise ValueError("published observation must equal candidate")
            self._finish_owned_publication(job_id, lease, phase, observed_remote_oid, error_code)
            finished = self.connection.execute(
                "SELECT * FROM publication_jobs WHERE project_id=? AND job_id=?",
                (self.project_id, job_id),
            ).fetchone()
            if finished is None or finished["phase"] != phase:
                raise RuntimeError("publication outcome was not visible")
            return dict(finished)

    def _finish_owned_publication(
        self,
        job_id: str,
        lease: str,
        phase: str,
        observed_remote_oid: str | None,
        error_code: str | None,
    ) -> None:
        """Atomically fence a terminal write against expiry of its publisher lease."""
        updated = self.connection.execute(
            """UPDATE publication_jobs SET phase=?, observed_remote_oid=?, error_code=?,
            publisher_lease_expires=NULL, updated_at=strftime('%Y-%m-%dT%H:%M:%fZ','now')
            WHERE project_id=? AND job_id=? AND phase=? AND publisher_lease=?
            AND publisher_lease_expires >= strftime('%Y-%m-%dT%H:%M:%fZ','now')""",
            (
                phase,
                observed_remote_oid,
                error_code,
                self.project_id,
                job_id,
                _PUBLICATION_PUBLISHING,
                lease,
            ),
        )
        if updated.rowcount == 1:
            return
        current = self.connection.execute(
            "SELECT * FROM publication_jobs WHERE project_id=? AND job_id=?",
            (self.project_id, job_id),
        ).fetchone()
        if (
            current is not None
            and current["phase"] == _PUBLICATION_PUBLISHING
            and current["publisher_lease"] == lease
        ):
            raise RuntimeError("publication lease has expired")
        raise RuntimeError("publication job changed while finishing")

    def recover_publication(self, job_id: str, *, observed_remote_oid: str) -> dict[str, Any]:
        """Resolve an expired or ambiguous publish only from a fresh ref observation.

        A recovered job returns to the queue only when the observed ref is the
        exact immutable base.  A candidate observation is durable success;
        every other observed head is a truthful rejection.  This deliberately
        forbids blind timeout retries.
        """
        if not re.fullmatch(r"[0-9a-f]{32}", job_id) or not _COMMIT.fullmatch(observed_remote_oid):
            raise ValueError("invalid publication recovery")
        with self._transaction():
            row = self.connection.execute(
                "SELECT * FROM publication_jobs WHERE project_id=? AND job_id=?",
                (self.project_id, job_id),
            ).fetchone()
            if row is None:
                raise RuntimeError("unknown publication job")
            if row["phase"] not in {_PUBLICATION_PUBLISHING, _PUBLICATION_AMBIGUOUS}:
                raise RuntimeError("publication job is not recoverable")
            if observed_remote_oid == row["candidate_oid"]:
                phase, error = _PUBLICATION_PUBLISHED, None
            elif observed_remote_oid == row["expected_remote_oid"]:
                phase, error = _PUBLICATION_QUEUED, None
            else:
                phase, error = _PUBLICATION_REJECTED, "REMOTE_BASE_CHANGED"
            updated = self.connection.execute(
                """UPDATE publication_jobs SET phase=?, publisher_lease=NULL,
                publisher_lease_expires=NULL, observed_remote_oid=?, error_code=?,
                updated_at=strftime('%Y-%m-%dT%H:%M:%fZ','now')
                WHERE project_id=? AND job_id=? AND
                (phase=? OR (phase=? AND publisher_lease_expires <
                 strftime('%Y-%m-%dT%H:%M:%fZ','now')))""",
                (
                    phase,
                    observed_remote_oid,
                    error,
                    self.project_id,
                    job_id,
                    _PUBLICATION_AMBIGUOUS,
                    _PUBLICATION_PUBLISHING,
                ),
            )
            if updated.rowcount != 1:
                current = self.connection.execute(
                    "SELECT phase FROM publication_jobs WHERE project_id=? AND job_id=?",
                    (self.project_id, job_id),
                ).fetchone()
                if current is not None and current["phase"] == _PUBLICATION_PUBLISHING:
                    raise RuntimeError("publication lease is still active")
                raise RuntimeError("publication job changed while recovering")
            recovered = self.connection.execute(
                "SELECT * FROM publication_jobs WHERE project_id=? AND job_id=?",
                (self.project_id, job_id),
            ).fetchone()
            if recovered is None or recovered["phase"] != phase:
                raise RuntimeError("publication recovery was not visible")
            return dict(recovered)
