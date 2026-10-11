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
        if mode != "wal" or version != 3:
            return False
        binding = self.connection.execute(
            "SELECT project_id FROM receipt_binding WHERE singleton=1"
        ).fetchone()
        if binding is None:
            raise RuntimeError("receipt database has no project binding")
        if binding["project_id"] != self.project_id:
            raise RuntimeError("receipt database is bound to a different project")
        return True

    def _initialize(self) -> None:
        try:
            self.connection.execute("BEGIN IMMEDIATE")
            version = self.connection.execute("PRAGMA user_version").fetchone()[0]
            if version not in (0, 3):
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
            self.connection.execute("PRAGMA user_version=3")
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
