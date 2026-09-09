# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""SQLite WAL storage for handoffctl using only Python's standard library."""

from __future__ import annotations

import json
import os
import sqlite3
import tempfile
from collections.abc import Callable, Iterator, Sequence
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Protocol, cast

type Meta = dict[str, Any]
type Task = tuple[Path, Meta, str]
SCHEMA_VERSION = 1
BUSY_TIMEOUT_MS = 10_000
DURABILITY = "FULL"
NETWORK_FILESYSTEMS = frozenset(
    {"9p", "afs", "ceph", "cifs", "fuse.sshfs", "gfs2", "glusterfs", "nfs", "nfs4", "smb3"}
)


class StorageContentionError(RuntimeError):
    """A bounded SQLite writer wait expired."""


class StorageCorruptionError(RuntimeError):
    """SQLite reported corruption or a malformed authoritative record."""


class Backend(Protocol):
    """Contract shared by authoritative storage implementations."""

    name: str

    def load_tasks(self) -> list[Task]: ...

    def append_command_result(
        self,
        task_id: str,
        owner: str,
        command_hash: str,
        returncode: int,
        classification: str,
        recorded_at: str,
    ) -> None: ...


def _mount_type(path: Path, mountinfo: str | None = None) -> str | None:
    """Return the longest matching Linux mount type, when observable."""
    if mountinfo is None:
        try:
            mountinfo = Path("/proc/self/mountinfo").read_text()
        except OSError:
            return None
    resolved = str(path.resolve())
    best: tuple[int, str] | None = None
    for line in mountinfo.splitlines():
        left, marker, right = line.partition(" - ")
        if not marker:
            continue
        fields, after = left.split(), right.split()
        if len(fields) < 5 or not after:
            continue
        mount = fields[4].replace("\\040", " ").replace("\\134", "\\")
        matches = resolved == mount or resolved.startswith(mount.rstrip("/") + "/")
        if matches and (best is None or len(mount) > best[0]):
            best = (len(mount), after[0])
    return None if best is None else best[1]


def require_local_filesystem(path: Path, mountinfo: str | None = None) -> None:
    """Fail closed for filesystem types known not to support SQLite WAL safely."""
    filesystem = _mount_type(path.parent, mountinfo)
    if filesystem is not None and filesystem.lower() in NETWORK_FILESYSTEMS:
        raise RuntimeError(f"SQLITE_UNSUPPORTED_FILESYSTEM: WAL is not supported on {filesystem}")


def _translate(error: sqlite3.Error) -> RuntimeError:
    code = getattr(error, "sqlite_errorcode", None)
    primary = None if code is None else code & 0xFF
    if primary in {sqlite3.SQLITE_BUSY, sqlite3.SQLITE_LOCKED} or any(
        value in str(error).lower() for value in ("locked", "busy")
    ):
        return StorageContentionError(f"SQLITE_BUSY_TIMEOUT after {BUSY_TIMEOUT_MS / 1000:.1f}s")
    if (
        primary in {sqlite3.SQLITE_CORRUPT, sqlite3.SQLITE_NOTADB}
        or "malformed" in str(error).lower()
    ):
        return StorageCorruptionError("SQLITE_CORRUPT: coordinator database is unreadable")
    if primary == sqlite3.SQLITE_FULL:
        return RuntimeError("SQLITE_STORAGE_FULL: no database space remains")
    if primary == sqlite3.SQLITE_READONLY:
        return RuntimeError("SQLITE_READ_ONLY: coordinator database is not writable")
    if primary == sqlite3.SQLITE_IOERR:
        return RuntimeError(f"SQLITE_IO_ERROR: {error}")
    return RuntimeError(f"SQLITE_ERROR: {error}")


def _require_database(path: Path) -> None:
    """Validate runtime and path prerequisites before opening SQLite."""
    if sqlite3.sqlite_version_info < (3, 37, 0):
        raise RuntimeError("SQLITE_VERSION_UNSUPPORTED: SQLite 3.37 or newer is required")
    require_local_filesystem(path)
    if path.is_symlink():
        raise RuntimeError("refusing symlink coordinator database")
    if not path.exists():
        raise RuntimeError("SQLITE_MISSING: authoritative coordinator database is missing")


class SQLiteBackend:
    """Authoritative embedded backend with transactional revision fencing."""

    name = "sqlite"

    def __init__(self, path: Path, binding: Meta, tasks_root: Path) -> None:
        self.path = path
        self.binding = binding
        self.tasks_root = tasks_root

    def _connect(self, *, read_only: bool = False) -> sqlite3.Connection:
        _require_database(self.path)
        target = f"file:{self.path}?mode=ro" if read_only else str(self.path)
        connection: sqlite3.Connection | None = None
        try:
            connection = sqlite3.connect(
                target, timeout=BUSY_TIMEOUT_MS / 1000, isolation_level=None, uri=read_only
            )
            connection.row_factory = sqlite3.Row
            connection.execute(f"PRAGMA busy_timeout={BUSY_TIMEOUT_MS}")
            connection.execute("PRAGMA foreign_keys=ON")
            if not read_only:
                mode = str(connection.execute("PRAGMA journal_mode=WAL").fetchone()[0]).lower()
                if mode != "wal":
                    raise RuntimeError("SQLITE_WAL_UNAVAILABLE: journal mode is not WAL")
                connection.execute(f"PRAGMA synchronous={DURABILITY}")
            self._verify_binding(connection)
            return connection
        except sqlite3.Error as error:
            if connection is not None:
                connection.close()
            raise _translate(error) from error
        except Exception:
            if connection is not None:
                connection.close()
            raise

    def _verify_binding(self, connection: sqlite3.Connection) -> None:
        try:
            rows = dict(connection.execute("SELECT key, value FROM metadata"))
        except sqlite3.Error as error:
            raise _translate(error) from error
        expected = {
            "schema_version": str(SCHEMA_VERSION),
            "backend": "sqlite",
            "project_id": str(self.binding["project_id"]),
            "state_repository": str(self.binding["state_repository"]),
            "product_repository": str(self.binding["product_repository"]),
        }
        if any(rows.get(key) != value for key, value in expected.items()):
            raise RuntimeError("SQLITE_BINDING_MISMATCH: database belongs to another project")
        if rows.get("state") != "active":
            raise RuntimeError("SQLITE_BACKEND_INACTIVE: retry using the selected backend")

    @contextmanager
    def transaction(self) -> Iterator[sqlite3.Connection]:
        connection = self._connect()
        try:
            connection.execute("BEGIN IMMEDIATE")
            state = connection.execute("SELECT value FROM metadata WHERE key='state'").fetchone()
            if state is None or state[0] != "active":
                raise RuntimeError("SQLITE_BACKEND_INACTIVE: retry using the selected backend")
            yield connection
            connection.commit()
        except sqlite3.Error as error:
            connection.rollback()
            raise _translate(error) from error
        except Exception:
            connection.rollback()
            raise
        finally:
            connection.close()

    def _load(self, connection: sqlite3.Connection) -> list[Task]:
        result: list[Task] = []
        for row in connection.execute(
            "SELECT filename, meta_json, body, revision FROM tasks ORDER BY id"
        ):
            try:
                meta = cast(Meta, json.loads(row["meta_json"]))
            except json.JSONDecodeError as error:
                raise StorageCorruptionError("SQLITE_CORRUPT: invalid task JSON") from error
            if meta.get("task_revision") != row["revision"]:
                raise StorageCorruptionError("SQLITE_CORRUPT: task revision columns disagree")
            result.append((self.tasks_root / str(row["filename"]), meta, str(row["body"])))
        return result

    def load_tasks(self) -> list[Task]:
        connection = self._connect(read_only=True)
        try:
            return self._load(connection)
        except sqlite3.Error as error:
            raise _translate(error) from error
        finally:
            connection.close()

    def mutate(
        self,
        task_id: str,
        expected_revision: int,
        kind: str,
        at: str,
        transition: Callable[[Meta, list[Task]], tuple[str, str]],
    ) -> None:
        """Apply one transition and CAS the authoritative revision in one transaction."""
        with self.transaction() as connection:
            tasks = self._load(connection)
            selected = next((task for task in tasks if task[1]["id"] == task_id), None)
            if selected is None:
                raise RuntimeError(f"unknown task {task_id}")
            _, meta, body = selected
            current = int(meta["task_revision"])
            if current != expected_revision:
                raise RuntimeError(
                    f"stale revision: expected {expected_revision}, current {current}"
                )
            note, body = transition(meta, tasks)
            meta["task_revision"] = current + 1
            meta["updated_at"] = at
            cursor = connection.execute(
                """UPDATE tasks SET meta_json=?, body=?, revision=?, status=?, owner=?,
                   claim_expires=?, branch=?, worktree_key=?, updated_at=?
                   WHERE id=? AND revision=?""",
                (
                    json.dumps(meta, sort_keys=True),
                    body,
                    meta["task_revision"],
                    meta["status"],
                    meta.get("owner", ""),
                    meta.get("claim_expires", ""),
                    meta.get("branch", ""),
                    meta.get("worktree_key", ""),
                    meta["updated_at"],
                    task_id,
                    current,
                ),
            )
            if cursor.rowcount != 1:
                raise RuntimeError("SQLITE_CONFLICT: exact-revision update lost its fence")
            connection.execute("DELETE FROM dependencies WHERE task_id=?", (task_id,))
            connection.executemany(
                "INSERT INTO dependencies(task_id, dependency_id) VALUES (?, ?)",
                [(task_id, value) for value in meta.get("depends_on", [])],
            )
            connection.execute(
                """INSERT INTO events(task_id, revision, kind, recorded_at, note)
                   VALUES (?, ?, ?, ?, ?)""",
                (task_id, meta["task_revision"], kind, at, note),
            )

    def update_observations(self, observations: dict[str, Meta], at: str) -> None:
        """Persist changed live worktree observations in one transaction."""
        with self.transaction() as connection:
            for _, meta, body in self._load(connection):
                key = str(meta.get("worktree_key", ""))
                if not key or key not in observations:
                    continue
                item = observations[key]
                values = {
                    "observed_branch": item["branch"],
                    "observed_head": item["head"],
                    "observed_dirty": item["dirty"],
                }
                if all(meta.get(name) == value for name, value in values.items()):
                    continue
                current = int(meta["task_revision"])
                meta.update(values)
                meta["task_revision"] = current + 1
                meta["updated_at"] = at
                cursor = connection.execute(
                    """UPDATE tasks SET meta_json=?, body=?, revision=?, status=?, owner=?,
                       claim_expires=?, branch=?, worktree_key=?, updated_at=?
                       WHERE id=? AND revision=?""",
                    (
                        json.dumps(meta, sort_keys=True),
                        body,
                        meta["task_revision"],
                        meta["status"],
                        meta.get("owner", ""),
                        meta.get("claim_expires", ""),
                        meta.get("branch", ""),
                        meta.get("worktree_key", ""),
                        meta["updated_at"],
                        meta["id"],
                        current,
                    ),
                )
                if cursor.rowcount != 1:
                    raise RuntimeError("SQLITE_CONFLICT: observation update lost its fence")
                connection.execute(
                    """INSERT INTO events(task_id, revision, kind, recorded_at, note)
                       VALUES (?, ?, 'reconcile', ?, ?)""",
                    (meta["id"], meta["task_revision"], at, "Recorded live worktree state."),
                )

    def append_command_result(
        self,
        task_id: str,
        owner: str,
        command_hash: str,
        returncode: int,
        classification: str,
        recorded_at: str,
    ) -> None:
        """Commit command evidence independently before reconciliation can fail."""
        with self.transaction() as connection:
            connection.execute(
                """INSERT INTO command_results
                   (task_id, owner, argv_sha256, returncode, classification, recorded_at)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (task_id, owner, command_hash, returncode, classification, recorded_at),
            )

    def retire(
        self,
        project: Callable[[list[Task]], None],
        switch_selector: Callable[[], None],
    ) -> None:
        """Fence pending writers, export one snapshot, then atomically retire authority."""
        with self.transaction() as connection:
            project(self._load(connection))
            connection.execute("UPDATE metadata SET value='retired' WHERE key='state'")
            switch_selector()

    def integrity_errors(self) -> list[str]:
        connection = self._connect(read_only=True)
        try:
            result = str(connection.execute("PRAGMA integrity_check").fetchone()[0])
            foreign = list(connection.execute("PRAGMA foreign_key_check"))
            errors = [] if result == "ok" else [f"SQLITE_CORRUPT: {result}"]
            if foreign:
                errors.append("SQLITE_CORRUPT: foreign-key violations")
            return errors
        finally:
            connection.close()


SCHEMA = """
CREATE TABLE metadata(key TEXT PRIMARY KEY, value TEXT NOT NULL) STRICT;
CREATE TABLE tasks(
 id TEXT PRIMARY KEY CHECK(id GLOB 'AR-[0-9][0-9][0-9][0-9]'), filename TEXT NOT NULL UNIQUE,
 meta_json TEXT NOT NULL CHECK(json_valid(meta_json)), body TEXT NOT NULL,
 revision INTEGER NOT NULL CHECK(revision >= 1),
 status TEXT NOT NULL CHECK(status IN
   ('in_progress','open','blocked','planned','future','done','cancelled','superseded')),
 owner TEXT NOT NULL, claim_expires TEXT NOT NULL, branch TEXT NOT NULL,
 worktree_key TEXT NOT NULL, updated_at TEXT NOT NULL,
 CHECK((status='in_progress' AND owner<>'' AND claim_expires<>'') OR
       (status<>'in_progress' AND owner='' AND claim_expires=''))
) STRICT;
CREATE UNIQUE INDEX one_active_owner ON tasks(owner) WHERE status='in_progress' AND owner<>'';
CREATE UNIQUE INDEX one_active_branch ON tasks(branch) WHERE status='in_progress' AND branch<>'';
CREATE UNIQUE INDEX one_active_worktree ON tasks(worktree_key)
 WHERE status='in_progress' AND worktree_key<>'';
CREATE TABLE dependencies(task_id TEXT NOT NULL REFERENCES tasks(id) ON DELETE CASCADE,
 dependency_id TEXT NOT NULL REFERENCES tasks(id), PRIMARY KEY(task_id, dependency_id),
 CHECK(task_id<>dependency_id)) STRICT;
CREATE TABLE events(sequence INTEGER PRIMARY KEY AUTOINCREMENT,
 task_id TEXT NOT NULL REFERENCES tasks(id), revision INTEGER NOT NULL, kind TEXT NOT NULL,
 recorded_at TEXT NOT NULL, note TEXT NOT NULL, UNIQUE(task_id, revision)) STRICT;
CREATE TABLE command_results(sequence INTEGER PRIMARY KEY AUTOINCREMENT,
 task_id TEXT NOT NULL REFERENCES tasks(id), owner TEXT NOT NULL,
 argv_sha256 TEXT NOT NULL CHECK(length(argv_sha256)=64), returncode INTEGER NOT NULL,
 classification TEXT NOT NULL, recorded_at TEXT NOT NULL) STRICT;
CREATE TABLE migrations(sequence INTEGER PRIMARY KEY AUTOINCREMENT, source_backend TEXT NOT NULL,
 source_checkpoint TEXT NOT NULL, imported_at TEXT NOT NULL,
 finalized INTEGER NOT NULL DEFAULT 0 CHECK(finalized IN (0,1))) STRICT;
CREATE TABLE checkpoints(name TEXT PRIMARY KEY, revision INTEGER NOT NULL,
 recorded_at TEXT NOT NULL) STRICT;
"""


def create_database(
    path: Path,
    binding: Meta,
    tasks: Sequence[Task],
    *,
    imported_at: str,
    source_backend: str,
    source_checkpoint: str,
    command_results: Sequence[Meta] = (),
) -> None:
    """Build a complete database beside its final target and install atomically."""
    require_local_filesystem(path)
    path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(
        prefix=".coordinator.", suffix=".sqlite3", dir=path.parent
    )
    os.close(descriptor)
    temporary_path = Path(temporary)
    try:
        connection = sqlite3.connect(temporary_path, isolation_level=None)
        try:
            connection.execute("PRAGMA foreign_keys=ON")
            connection.execute("PRAGMA journal_mode=WAL")
            connection.execute(f"PRAGMA synchronous={DURABILITY}")
            connection.executescript(SCHEMA)
            connection.execute("BEGIN IMMEDIATE")
            metadata = {
                "schema_version": str(SCHEMA_VERSION),
                "backend": "sqlite",
                "project_id": str(binding["project_id"]),
                "state_repository": str(binding["state_repository"]),
                "product_repository": str(binding["product_repository"]),
                "state": "active",
            }
            connection.executemany("INSERT INTO metadata VALUES (?, ?)", metadata.items())
            for filename, meta, body in tasks:
                connection.execute(
                    "INSERT INTO tasks VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (
                        meta["id"],
                        filename.name,
                        json.dumps(meta, sort_keys=True),
                        body,
                        meta["task_revision"],
                        meta["status"],
                        meta.get("owner", ""),
                        meta.get("claim_expires", ""),
                        meta.get("branch", ""),
                        meta.get("worktree_key", ""),
                        meta["updated_at"],
                    ),
                )
            for _, meta, _ in tasks:
                connection.executemany(
                    "INSERT INTO dependencies VALUES (?, ?)",
                    [(meta["id"], value) for value in meta.get("depends_on", [])],
                )
                connection.execute(
                    """INSERT INTO events(task_id, revision, kind, recorded_at, note)
                       VALUES (?, ?, 'import', ?, ?)""",
                    (
                        meta["id"],
                        meta["task_revision"],
                        imported_at,
                        "Imported authoritative task record.",
                    ),
                )
            connection.execute(
                """INSERT INTO migrations(source_backend, source_checkpoint, imported_at)
                   VALUES (?, ?, ?)""",
                (source_backend, source_checkpoint, imported_at),
            )
            connection.executemany(
                """INSERT INTO command_results
                   (task_id, owner, argv_sha256, returncode, classification, recorded_at)
                   VALUES (:task, :owner, :argv_sha256, :returncode, :classification, :at)""",
                command_results,
            )
            connection.commit()
            connection.execute("PRAGMA wal_checkpoint(TRUNCATE)")
        finally:
            connection.close()
        temporary_path.chmod(0o600)
        temporary_path.replace(path)
        directory = os.open(path.parent, os.O_DIRECTORY)
        try:
            os.fsync(directory)
        finally:
            os.close(directory)
    except sqlite3.Error as error:
        raise _translate(error) from error
    finally:
        temporary_path.unlink(missing_ok=True)
        Path(str(temporary_path) + "-wal").unlink(missing_ok=True)
        Path(str(temporary_path) + "-shm").unlink(missing_ok=True)
