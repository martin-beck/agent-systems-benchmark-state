# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""SQLite WAL storage for handoffctl using only Python's standard library."""

from __future__ import annotations

import hashlib
import json
import os
import re
import sqlite3
import stat
import tempfile
from collections.abc import Callable, Iterator, Sequence
from contextlib import AbstractContextManager, contextmanager, nullcontext
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Protocol, cast

if __package__:
    from .session_records import validate_session_record
else:  # pragma: no cover - direct script import
    from session_records import validate_session_record  # type: ignore[import-not-found,no-redef]

type Meta = dict[str, Any]
type Task = tuple[Path, Meta, str]
SCHEMA_VERSION = 1
BUSY_TIMEOUT_MS = 10_000
DURABILITY = "FULL"
NETWORK_FILESYSTEMS = frozenset(
    {"9p", "afs", "ceph", "cifs", "fuse.sshfs", "gfs2", "glusterfs", "nfs", "nfs4", "smb3"}
)
_FACTORY_SENTINEL = object()
_SHA256_DIGEST = re.compile(r"sha256:[0-9a-f]{64}$")
_PUBLICATION_KEY = re.compile(r"[0-9a-f]{64}$")
_COMMENT_ID = re.compile(r"[1-9][0-9]{0,18}$")
_BARE_SHA256 = re.compile(r"[0-9a-f]{64}$")
_EXECUTION_ID = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$")
_TASK_ID = re.compile(r"AR-[0-9]{4}$")
_EXECUTION_RESULT_CLASSIFICATIONS = frozenset({"EXIT", "SUBPROCESS_TIMEOUT"})
_PUBLICATION_STATUSES = frozenset(
    {
        "published",
        "already_published",
        "dry_run",
        "deferred_unavailable",
        "deferred_unauthorized",
        "deferred_timeout",
        "deferred_conflict",
        "deferred_wrong_identity",
        "deferred_closed",
        "deferred_moved",
        "ambiguous",
    }
)


class StorageContentionError(RuntimeError):
    """A bounded SQLite writer wait expired."""


class StorageCorruptionError(RuntimeError):
    """SQLite reported corruption or a malformed authoritative record."""


class SQLiteBackendBinding:
    """Immutable, adapter-issued binding for a durable SQLite session.

    Legacy ``SQLiteBackend`` construction remains intentionally unbound.  A
    bound backend can only be issued from the concrete control-store and
    barrier-session pair, so metadata supplied by a caller cannot manufacture
    authority or fencing facts.

    The capability is an identity/read-consistency contract only.  It grants
    no mutation authorization, lock ownership, or fencing authority; those
    remain responsibilities of the control-store adapter.  Transactional
    integration is intentionally deferred to a later slice.
    """

    __slots__ = (
        "_control_store",
        "_descriptor_identity",
        "_fence",
        "_owner",
        "_path",
        "_project_id",
        "_revision",
        "_session",
    )
    _control_store: Any
    _descriptor_identity: tuple[int, int]
    _fence: str
    _owner: str
    _path: Path
    _project_id: str
    _revision: int
    _session: Any

    def __init__(
        self, control_store: Any, session: Any, state: Any, capability: object | None = None
    ) -> None:
        if capability is not _FACTORY_SENTINEL:
            raise TypeError("SQLiteBackendBinding must be issued by bind()")
        object.__setattr__(self, "_control_store", control_store)
        object.__setattr__(self, "_session", session)
        object.__setattr__(self, "_path", Path(control_store.control_store_path))
        object.__setattr__(self, "_project_id", state.identity.project_id)
        object.__setattr__(self, "_owner", state.identity.fencing_owner)
        object.__setattr__(self, "_fence", state.identity.fencing_token)
        object.__setattr__(self, "_revision", state.revision)
        object.__setattr__(self, "_descriptor_identity", control_store._control_identity)

    def __setattr__(self, name: str, value: object) -> None:
        raise AttributeError("SQLiteBackendBinding is immutable")

    @classmethod
    def bind(cls, control_store: Any, session: Any) -> SQLiteBackendBinding:
        if not hasattr(control_store, "control_store_path") or not hasattr(session, "snapshot"):
            raise TypeError("SQLiteBackendBinding requires concrete SQLite stores")
        if getattr(session, "_control", None) is not control_store:
            raise ValueError("session is bound to a foreign control store")
        state = session.snapshot()
        if state is None or state.status != "held":
            raise ValueError("an active durable session is required")
        return cls(control_store, session, state, _FACTORY_SENTINEL)

    @property
    def path(self) -> Path:
        return self._path

    @property
    def project_id(self) -> str:
        return self._project_id

    @property
    def fencing_owner(self) -> str:
        return self._owner

    @property
    def fence(self) -> str:
        return self._fence

    @property
    def fencing_token(self) -> str:
        """Compatibility alias for consumers of the durable fence value."""
        return self._fence

    @property
    def revision(self) -> int:
        return self._revision

    @property
    def descriptor_identity(self) -> tuple[int, int]:
        return self._descriptor_identity

    def assert_current(self) -> None:
        if self._control_store._control_identity != self._descriptor_identity:
            raise RuntimeError("SQLite backend descriptor identity changed")
        try:
            if self._session.operation_owned_by_current_thread:
                # LockDomainScope already owns common -> control -> authority.
                # Re-entering snapshot() would violate the non-reentrant
                # control-lock contract at the mutation boundary.
                state = self._session.snapshot_owned_by_caller()
            else:
                state = self._session.snapshot()
        except Exception as error:
            raise RuntimeError("SQLite backend binding reread failed") from error
        if state is None or state.status != "held":
            raise RuntimeError("SQLite backend session is no longer active")
        identity = state.identity
        if (
            identity.project_id != self._project_id
            or identity.fencing_owner != self._owner
            or identity.fencing_token != self._fence
            or state.revision != self._revision
        ):
            raise RuntimeError("SQLite backend session identity changed")


class SQLiteAuthorityBinding:
    """Immutable dual binding for control-session and authority descriptors."""

    __slots__ = ("_control", "_identity", "_parent_identity", "_path")
    _control: SQLiteBackendBinding
    _identity: tuple[int, int]
    _parent_identity: tuple[int, int]
    _path: Path

    def __init__(
        self,
        control: SQLiteBackendBinding,
        path: Path,
        identity: tuple[int, int],
        parent_identity: tuple[int, int],
        sentinel: object,
    ) -> None:
        if sentinel is not _FACTORY_SENTINEL:
            raise TypeError("SQLiteAuthorityBinding must be issued by bind()")
        object.__setattr__(self, "_control", control)
        object.__setattr__(self, "_path", path)
        object.__setattr__(self, "_identity", identity)
        object.__setattr__(self, "_parent_identity", parent_identity)

    def __setattr__(self, name: str, value: object) -> None:
        raise AttributeError("SQLiteAuthorityBinding is immutable")

    @classmethod
    def bind(
        cls, control: SQLiteBackendBinding, authority: Path, scope: object
    ) -> SQLiteAuthorityBinding:
        from tools.lock_domain_scope import LockDomainScope

        if not isinstance(control, SQLiteBackendBinding):
            raise TypeError("control binding is required")
        if not isinstance(scope, LockDomainScope):
            raise TypeError("authority binding requires adapter-owned LockDomainScope")
        path = authority.absolute()
        if (
            getattr(getattr(scope, "_session_store", None), "_control", None)
            is not control._control_store
        ):
            raise ValueError("authority binding scope uses a foreign control store")
        if getattr(getattr(scope, "_authority_fence", None), "control_store", None) != control.path:
            raise ValueError("authority binding scope uses a foreign control store")
        fenced_authority = getattr(getattr(scope, "_authority_fence", None), "authority", None)
        if not isinstance(fenced_authority, Path) or fenced_authority.absolute() != path:
            raise ValueError("authority binding path does not match the admission scope authority")
        if path.is_symlink() or not path.is_file():
            raise ValueError("authority must be a regular non-symlink file")
        parent_status = path.parent.stat()
        status = path.stat()
        return cls(
            control,
            path,
            (status.st_dev, status.st_ino),
            (parent_status.st_dev, parent_status.st_ino),
            _FACTORY_SENTINEL,
        )

    @property
    def path(self) -> Path:
        return self._path

    @property
    def descriptor_identity(self) -> tuple[int, int]:
        return self._identity

    @staticmethod
    def _assert_parent_identity(
        path: Path, expected: tuple[int, int], observed: tuple[int, int] | None = None
    ) -> None:
        if observed is None:
            try:
                status = path.parent.stat()
            except OSError as error:
                raise RuntimeError("SQLite authority parent identity unavailable") from error
            actual = (status.st_dev, status.st_ino)
        else:
            actual = observed
        if actual != expected:
            raise RuntimeError("SQLite authority parent identity changed")

    def assert_current(self) -> None:
        self._control.assert_current()
        try:
            if self._path.is_symlink():
                raise RuntimeError("SQLite authority descriptor is a symlink")
            parent = self._path.parent.stat()
            status = self._path.stat()
        except OSError as error:
            raise RuntimeError("SQLite authority descriptor reread failed") from error
        self._assert_parent_identity(
            self._path, self._parent_identity, (parent.st_dev, parent.st_ino)
        )
        if (status.st_dev, status.st_ino) != self._identity:
            raise RuntimeError("SQLite authority descriptor identity changed")

    @staticmethod
    def _open_retained(parent: int, name: str, label: str) -> tuple[int, tuple[int, int]]:
        try:
            descriptor = os.open(name, os.O_RDWR | os.O_NOFOLLOW, dir_fd=parent)
        except OSError as error:
            raise RuntimeError(f"SQLite authority {label} is unavailable") from error
        status = os.fstat(descriptor)
        if (
            not stat.S_ISREG(status.st_mode)
            or status.st_nlink != 1
            or status.st_uid != os.geteuid()
            or stat.S_IMODE(status.st_mode) != 0o600
        ):
            os.close(descriptor)
            raise RuntimeError(f"SQLite authority {label} is unsafe")
        return descriptor, (status.st_dev, status.st_ino)

    @staticmethod
    def _assert_retained(
        parent: int,
        name: str,
        descriptor: int,
        expected: tuple[int, int],
        label: str,
    ) -> None:
        retained = os.fstat(descriptor)
        try:
            current = os.stat(name, dir_fd=parent, follow_symlinks=False)
        except OSError as error:
            raise RuntimeError(f"SQLite authority {label} is unavailable") from error
        if (
            not stat.S_ISREG(current.st_mode)
            or current.st_nlink != 1
            or current.st_uid != os.geteuid()
            or stat.S_IMODE(current.st_mode) != 0o600
            or stat.S_IMODE(retained.st_mode) != 0o600
            or (retained.st_dev, retained.st_ino) != expected
            or (current.st_dev, current.st_ino) != expected
        ):
            raise RuntimeError(f"SQLite authority {label} identity changed")

    @classmethod
    def _open_sidecar_set(
        cls, parent: int, path: Path
    ) -> tuple[dict[str, int], dict[str, tuple[int, int]]]:
        descriptors: dict[str, int] = {}
        identities: dict[str, tuple[int, int]] = {}
        try:
            for suffix in ("-wal", "-shm"):
                descriptor, identity = cls._open_retained(parent, path.name + suffix, "sidecar")
                descriptors[suffix] = descriptor
                identities[suffix] = identity
        except Exception:
            for descriptor in descriptors.values():
                os.close(descriptor)
            raise
        return descriptors, identities

    @classmethod
    def _assert_retained_set(
        cls,
        parent: int,
        path: Path,
        authority_descriptor: int,
        authority_identity: tuple[int, int],
        descriptors: dict[str, int],
        identities: dict[str, tuple[int, int]],
    ) -> None:
        cls._assert_retained(
            parent, path.name, authority_descriptor, authority_identity, "descriptor"
        )
        for suffix, descriptor in descriptors.items():
            cls._assert_retained(
                parent, path.name + suffix, descriptor, identities[suffix], "sidecar"
            )

    @staticmethod
    @contextmanager
    def _hold_path_sidecars(
        path: Path, assert_authority: Callable[[], None]
    ) -> Iterator[Callable[[], None]]:
        """Retain and recheck active WAL/SHM descriptors for one transaction."""
        parent_descriptor = -1
        authority_descriptor = -1
        descriptors: dict[str, int] = {}
        identities: dict[str, tuple[int, int]] = {}
        try:
            parent_descriptor = os.open(path.parent, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
            parent_status = os.fstat(parent_descriptor)
            parent_identity = (parent_status.st_dev, parent_status.st_ino)
            authority_descriptor, authority_identity = SQLiteAuthorityBinding._open_retained(
                parent_descriptor, path.name, "descriptor"
            )
            descriptors, identities = SQLiteAuthorityBinding._open_sidecar_set(
                parent_descriptor, path
            )

            def assert_current() -> None:
                assert_authority()
                current_parent = os.fstat(parent_descriptor)
                if (current_parent.st_dev, current_parent.st_ino) != parent_identity:
                    raise RuntimeError("SQLite authority sidecar parent identity changed")
                SQLiteAuthorityBinding._assert_retained_set(
                    parent_descriptor,
                    path,
                    authority_descriptor,
                    authority_identity,
                    descriptors,
                    identities,
                )

            assert_current()
            yield assert_current
        finally:
            for descriptor in descriptors.values():
                os.close(descriptor)
            if authority_descriptor >= 0:
                os.close(authority_descriptor)
            if parent_descriptor >= 0:
                os.close(parent_descriptor)

    def hold_sidecars(self) -> AbstractContextManager[Callable[[], None]]:
        """Bind one dual-authority transaction to its live sidecars."""
        return self._hold_path_sidecars(self._path, self.assert_current)


class SQLiteMutationBinding:
    """Provisioned authority binding for ordinary released-state writers.

    Upgrade admission uses ``SQLiteAuthorityBinding`` and a held session. Normal
    coordinator writes run while the durable barrier is released, so they need
    the same descriptor/sidecar identity protection without manufacturing a
    held upgrade session.
    """

    __slots__ = ("_fence", "_identity", "_parent_identity", "_path")
    _fence: Any
    _identity: tuple[int, int]
    _parent_identity: tuple[int, int]
    _path: Path

    def __init__(
        self,
        fence: Any,
        path: Path,
        identity: tuple[int, int],
        parent_identity: tuple[int, int],
        sentinel: object,
    ) -> None:
        if sentinel is not _FACTORY_SENTINEL:
            raise TypeError("SQLiteMutationBinding must be issued by its factory")
        object.__setattr__(self, "_fence", fence)
        object.__setattr__(self, "_path", path)
        object.__setattr__(self, "_identity", identity)
        object.__setattr__(self, "_parent_identity", parent_identity)

    def __setattr__(self, name: str, value: object) -> None:
        raise AttributeError("SQLiteMutationBinding is immutable")

    @classmethod
    def bind(cls, fence: Any, authority: Path) -> SQLiteMutationBinding:
        from tools.mutation_fence import MutationFence

        if not isinstance(fence, MutationFence):
            raise TypeError("concrete mutation fence is required")
        path = authority.absolute()
        if fence.authority.absolute() != path:
            raise ValueError("mutation fence authority does not match database")
        fence.verify_binding()
        if path.is_symlink() or not path.is_file():
            raise ValueError("authority must be a regular non-symlink file")
        parent_status = path.parent.stat()
        status = path.stat()
        return cls(
            fence,
            path,
            (status.st_dev, status.st_ino),
            (parent_status.st_dev, parent_status.st_ino),
            _FACTORY_SENTINEL,
        )

    def assert_current(self) -> None:
        self._fence.verify_binding()
        try:
            parent = self._path.parent.stat()
            status = self._path.stat()
        except OSError as error:
            raise RuntimeError("SQLite authority descriptor reread failed") from error
        if (parent.st_dev, parent.st_ino) != self._parent_identity:
            raise RuntimeError("SQLite authority parent identity changed")
        if (status.st_dev, status.st_ino) != self._identity:
            raise RuntimeError("SQLite authority descriptor identity changed")

    @property
    def path(self) -> Path:
        return self._path

    def hold_sidecars(self) -> AbstractContextManager[Callable[[], None]]:
        return SQLiteAuthorityBinding._hold_path_sidecars(self._path, self.assert_current)


class Backend(Protocol):
    """Contract shared by authoritative storage implementations."""

    name: str

    def load_tasks(self) -> list[Task]: ...

    def load_session_records(self, task_id: str | None = None) -> list[Meta]: ...

    def load_checkpoint_records(self, task_id: str | None = None) -> list[Meta]: ...

    def has_command_result(self, task_id: str, owner: str, argv_sha256: str) -> bool: ...

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

    def __init__(
        self,
        path: Path,
        binding: Meta,
        tasks_root: Path,
        mutation_scope: Callable[[], AbstractContextManager[object]] | None = None,
        backend_binding: SQLiteBackendBinding
        | SQLiteAuthorityBinding
        | SQLiteMutationBinding
        | None = None,
        _admission_capability: object | None = None,
    ) -> None:
        self.path = path
        self.binding = binding
        self.tasks_root = tasks_root
        self.mutation_scope = mutation_scope
        if backend_binding is not None:
            if _admission_capability is not _FACTORY_SENTINEL:
                raise ValueError("bound SQLite backend must be created by its adapter factory")
            if not isinstance(
                backend_binding,
                (SQLiteBackendBinding, SQLiteAuthorityBinding, SQLiteMutationBinding),
            ):
                raise TypeError("backend_binding must be an SQLite binding capability")
            if backend_binding.path != path:
                raise ValueError("backend binding targets a different database")
            if mutation_scope is None:
                raise ValueError("bound SQLite backend requires a provisioned mutation scope")
        self.backend_binding = backend_binding

    def _connect(self, *, read_only: bool = False) -> sqlite3.Connection:
        _require_database(self.path)
        if self.backend_binding is not None:
            self.backend_binding.assert_current()
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

    def _assert_mutation_binding(self) -> None:
        """Re-read the optional durable capability at each mutation boundary.

        The capability is an identity fence, not authorization.  Authorization
        and lock ordering remain provided by ``mutation_scope`` and the
        control-store adapter; this hook only rejects stale or ambiguous
        durable sessions before and after a transaction's effects.
        """
        if self.backend_binding is not None:
            self.backend_binding.assert_current()

    @contextmanager
    def _transaction(self) -> Iterator[sqlite3.Connection]:
        if self.backend_binding is not None and not isinstance(
            self.backend_binding, (SQLiteAuthorityBinding, SQLiteMutationBinding)
        ):
            raise RuntimeError("mutating SQLite backend requires dual authority binding")
        connection = self._connect()
        try:
            connection.execute("BEGIN IMMEDIATE")
            sidecar_scope = (
                self.backend_binding.hold_sidecars()
                if isinstance(self.backend_binding, SQLiteAuthorityBinding)
                else SQLiteAuthorityBinding._hold_path_sidecars(self.path, lambda: None)
            )
            with sidecar_scope as assert_sidecars:
                state = connection.execute(
                    "SELECT value FROM metadata WHERE key='state'"
                ).fetchone()
                if state is None or state[0] != "active":
                    raise RuntimeError("SQLITE_BACKEND_INACTIVE: retry using the selected backend")
                self._assert_mutation_binding()
                yield connection
                self._assert_mutation_binding()
                assert_sidecars()
                connection.commit()
                assert_sidecars()
        except sqlite3.Error as error:
            connection.rollback()
            raise _translate(error) from error
        except Exception:
            connection.rollback()
            raise
        finally:
            connection.close()

    @contextmanager
    def transaction(self) -> Iterator[sqlite3.Connection]:
        """Run the mutation under the optional provisioned fence scope."""
        scope = self.mutation_scope() if self.mutation_scope is not None else nullcontext()
        with scope, self._transaction() as connection:
            yield connection

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
        session_record: Meta | None = None,
        session_factory: Callable[[Meta], Meta] | None = None,
        checkpoint_factory: Callable[[Meta], Meta] | None = None,
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
            checkpoint_record = checkpoint_factory(meta) if checkpoint_factory is not None else None
            if checkpoint_record is not None:
                connection.execute(
                    """CREATE TABLE IF NOT EXISTS checkpoint_records(
                       sequence INTEGER PRIMARY KEY AUTOINCREMENT,
                       task_id TEXT NOT NULL REFERENCES tasks(id) ON DELETE CASCADE,
                       task_revision INTEGER NOT NULL,
                       record_json TEXT NOT NULL CHECK(json_valid(record_json)),
                       recorded_at TEXT NOT NULL,
                       UNIQUE(task_id, task_revision)) STRICT"""
                )
                connection.execute(
                    """INSERT INTO checkpoint_records
                       (task_id, task_revision, record_json, recorded_at)
                       VALUES (?, ?, ?, ?)""",
                    (
                        task_id,
                        int(checkpoint_record["task_revision"]),
                        json.dumps(checkpoint_record, sort_keys=True, separators=(",", ":")),
                        str(checkpoint_record["recorded_at"]),
                    ),
                )
                connection.execute(
                    """DELETE FROM checkpoint_records
                       WHERE task_id=? AND sequence NOT IN
                       (SELECT sequence FROM checkpoint_records WHERE task_id=?
                        ORDER BY sequence DESC LIMIT 16)""",
                    (task_id, task_id),
                )
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
            if session_factory is not None:
                session_record = session_factory(meta)
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
            if session_record is not None:
                connection.execute(
                    """CREATE TABLE IF NOT EXISTS session_records(
                       sequence INTEGER PRIMARY KEY AUTOINCREMENT,
                       task_id TEXT NOT NULL REFERENCES tasks(id) ON DELETE CASCADE,
                       task_revision INTEGER NOT NULL,
                       record_json TEXT NOT NULL CHECK(json_valid(record_json)),
                       recorded_at TEXT NOT NULL,
                       UNIQUE(task_id, task_revision)) STRICT"""
                )
                connection.execute(
                    """INSERT INTO session_records
                       (task_id, task_revision, record_json, recorded_at)
                       VALUES (?, ?, ?, ?)""",
                    (
                        task_id,
                        int(session_record["task_revision"]),
                        json.dumps(session_record, sort_keys=True, separators=(",", ":")),
                        str(session_record["recorded_at"]),
                    ),
                )
                connection.execute(
                    """DELETE FROM session_records
                       WHERE task_id=? AND sequence NOT IN
                       (SELECT sequence FROM session_records WHERE task_id=?
                        ORDER BY sequence DESC LIMIT 32)""",
                    (task_id, task_id),
                )

    def load_session_records(self, task_id: str | None = None) -> list[Meta]:
        """Load bounded session records from the authoritative SQLite store."""
        connection = self._connect(read_only=True)
        try:
            try:
                rows = connection.execute(
                    """SELECT task_id, task_revision, record_json FROM session_records
                       WHERE (? IS NULL OR task_id=?) ORDER BY sequence""",
                    (task_id, task_id),
                )
            except sqlite3.OperationalError as error:
                if "no such table" not in str(error).lower():
                    raise
                return []
            records: list[Meta] = []
            for row in rows:
                value = json.loads(str(row["record_json"]))
                if not isinstance(value, dict):
                    raise StorageCorruptionError("SQLITE_CORRUPT: invalid session record")
                try:
                    validate_session_record(value)
                except ValueError as error:
                    raise StorageCorruptionError(
                        "SQLITE_CORRUPT: invalid session record"
                    ) from error
                if value["task"] != str(row["task_id"]) or value["task_revision"] != int(
                    row["task_revision"]
                ):
                    raise StorageCorruptionError("SQLITE_CORRUPT: session record identity mismatch")
                records.append(cast(Meta, value))
            return records
        except json.JSONDecodeError as error:
            raise StorageCorruptionError("SQLITE_CORRUPT: invalid session JSON") from error
        except sqlite3.Error as error:
            raise _translate(error) from error
        finally:
            connection.close()

    def load_checkpoint_records(self, task_id: str | None = None) -> list[Meta]:
        """Load bounded checkpoint records from the authoritative SQLite store."""
        connection = self._connect(read_only=True)
        try:
            try:
                rows = connection.execute(
                    """SELECT record_json FROM checkpoint_records
                       WHERE (? IS NULL OR task_id=?) ORDER BY sequence""",
                    (task_id, task_id),
                )
            except sqlite3.OperationalError as error:
                if "no such table" not in str(error).lower():
                    raise
                return []
            records: list[Meta] = []
            for row in rows:
                value = json.loads(str(row["record_json"]))
                if not isinstance(value, dict):
                    raise StorageCorruptionError("SQLITE_CORRUPT: invalid checkpoint record")
                records.append(cast(Meta, value))
            return records
        except json.JSONDecodeError as error:
            raise StorageCorruptionError("SQLITE_CORRUPT: invalid checkpoint JSON") from error
        except sqlite3.Error as error:
            raise _translate(error) from error
        finally:
            connection.close()

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

    def has_command_result(self, task_id: str, owner: str, argv_sha256: str) -> bool:
        """Check for exact command evidence without opening a writer transaction."""
        connection = self._connect(read_only=True)
        try:
            row = connection.execute(
                """SELECT 1 FROM command_results
                   WHERE task_id=? AND owner=? AND argv_sha256=? LIMIT 1""",
                (task_id, owner, argv_sha256),
            ).fetchone()
            return row is not None
        except sqlite3.Error as error:
            raise _translate(error) from error
        finally:
            connection.close()

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

    @staticmethod
    def _issue_series_state_digest(tasks: Sequence[Task]) -> str:
        snapshot = [
            {
                "depends_on": meta.get("depends_on", []),
                "id": meta["id"],
                "parent_task_ref": meta.get("parent_task_ref", ""),
                "status": meta["status"],
                "task_revision": meta["task_revision"],
            }
            for _path, meta, _body in sorted(tasks, key=lambda task: str(task[1]["id"]))
        ]
        encoded = json.dumps(snapshot, separators=(",", ":"), sort_keys=True).encode("utf-8")
        return "sha256:" + hashlib.sha256(encoded).hexdigest()

    @staticmethod
    def _ensure_issue_series_schema(connection: sqlite3.Connection) -> None:
        """Install the additive series tables for databases created before this feature."""
        # sqlite3.executescript() commits an active transaction before running
        # its script.  These individual DDL statements retain the enclosing
        # BEGIN IMMEDIATE transaction, so a legacy-schema upgrade and series
        # creation either commit together or roll back together.
        for statement in ISSUE_SERIES_STATEMENTS:
            connection.execute(statement)

    @staticmethod
    def _ensure_execution_envelope_schema(connection: sqlite3.Connection) -> None:
        """Install immutable execution receipts without rewriting task state."""
        # Keep every DDL statement inside the caller's transaction: a failed
        # legacy upgrade must leave neither receipt table behind.
        for statement in EXECUTION_ENVELOPE_STATEMENTS:
            connection.execute(statement)

    @staticmethod
    def _normalize_execution_envelope(envelope: Meta) -> Meta:
        """Return the exact privacy-safe intent shape accepted by durable storage."""
        required = {
            "schema_version",
            "execution_id",
            "task",
            "task_revision",
            "owner",
            "claim_expires",
            "worktree_key",
            "branch",
            "spec_ref",
            "spec_revision",
            "policy_digest",
            "argv_sha256",
            "timeout_seconds",
            "created_at",
        }
        if set(envelope) != required:
            raise ValueError("execution envelope has unexpected fields")
        execution_id = envelope["execution_id"]
        task_id = envelope["task"]
        revision = envelope["task_revision"]
        if (
            type(envelope["schema_version"]) is not int
            or envelope["schema_version"] != 1
            or not isinstance(execution_id, str)
            or not _EXECUTION_ID.fullmatch(execution_id)
            or not isinstance(task_id, str)
            or not _TASK_ID.fullmatch(task_id)
            or isinstance(revision, bool)
            or not isinstance(revision, int)
            or revision < 1
        ):
            raise ValueError("execution envelope has invalid identity")
        text_fields = ("owner", "claim_expires", "worktree_key", "branch", "created_at")
        if any(
            not isinstance(envelope[field], str)
            or not envelope[field]
            or "\n" in envelope[field]
            or "\r" in envelope[field]
            for field in text_fields
        ):
            raise ValueError("execution envelope has unsafe text field")
        spec_ref = envelope["spec_ref"]
        spec_revision = envelope["spec_revision"]
        if (spec_ref is None) != (spec_revision is None):
            raise ValueError("execution envelope has incomplete spec binding")
        if spec_ref is not None and (
            not isinstance(spec_ref, str)
            or not spec_ref
            or "\n" in spec_ref
            or "\r" in spec_ref
            or isinstance(spec_revision, bool)
            or not isinstance(spec_revision, int)
            or spec_revision < 1
        ):
            raise ValueError("execution envelope has invalid spec binding")
        for field in ("policy_digest", "argv_sha256"):
            value = envelope[field]
            if not isinstance(value, str) or not _BARE_SHA256.fullmatch(value):
                raise ValueError(f"execution envelope has invalid {field}")
        timeout = envelope["timeout_seconds"]
        if isinstance(timeout, bool) or not isinstance(timeout, (int, float)) or timeout <= 0:
            raise ValueError("execution envelope has invalid timeout")
        return {
            "schema_version": 1,
            "execution_id": execution_id,
            "task": task_id,
            "task_revision": revision,
            "owner": envelope["owner"],
            "claim_expires": envelope["claim_expires"],
            "worktree_key": envelope["worktree_key"],
            "branch": envelope["branch"],
            "spec_ref": spec_ref,
            "spec_revision": spec_revision,
            "policy_digest": envelope["policy_digest"],
            "argv_sha256": envelope["argv_sha256"],
            "timeout_seconds": float(timeout),
            "created_at": envelope["created_at"],
        }

    @staticmethod
    def _normalize_execution_result(result: Meta) -> Meta:
        """Return one terminal execution outcome; raw subprocess data is excluded."""
        required = {"schema_version", "execution_id", "classification", "returncode", "recorded_at"}
        if set(result) != required:
            raise ValueError("execution result has unexpected fields")
        execution_id = result["execution_id"]
        classification = result["classification"]
        returncode = result["returncode"]
        recorded_at = result["recorded_at"]
        if (
            type(result["schema_version"]) is not int
            or result["schema_version"] != 1
            or not isinstance(execution_id, str)
            or not _EXECUTION_ID.fullmatch(execution_id)
            or not isinstance(classification, str)
            or classification not in _EXECUTION_RESULT_CLASSIFICATIONS
            or isinstance(returncode, bool)
            or not isinstance(returncode, int)
            or not isinstance(recorded_at, str)
            or not recorded_at
            or "\n" in recorded_at
            or "\r" in recorded_at
        ):
            raise ValueError("execution result has invalid fields")
        return {
            "schema_version": 1,
            "execution_id": execution_id,
            "classification": classification,
            "returncode": returncode,
            "recorded_at": recorded_at,
        }

    def load_execution_envelopes(self, task_id: str | None = None) -> list[Meta]:
        """Load immutable intent records in deterministic task/time/identity order."""
        connection = self._connect(read_only=True)
        try:
            try:
                rows = connection.execute(
                    """SELECT envelope_json FROM execution_envelopes
                       WHERE (? IS NULL OR task_id=?)
                       ORDER BY task_id, created_at, execution_id""",
                    (task_id, task_id),
                )
            except sqlite3.OperationalError as error:
                if "no such table" not in str(error).lower():
                    raise
                return []
            records: list[Meta] = []
            for row in rows:
                try:
                    value = json.loads(str(row["envelope_json"]))
                except json.JSONDecodeError as error:
                    raise StorageCorruptionError(
                        "SQLITE_CORRUPT: invalid execution envelope"
                    ) from error
                if not isinstance(value, dict):
                    raise StorageCorruptionError("SQLITE_CORRUPT: invalid execution envelope")
                try:
                    records.append(self._normalize_execution_envelope(cast(Meta, value)))
                except ValueError as error:
                    raise StorageCorruptionError(
                        "SQLITE_CORRUPT: invalid execution envelope"
                    ) from error
            return records
        except sqlite3.Error as error:
            raise _translate(error) from error
        finally:
            connection.close()

    def record_execution_envelope(self, envelope: Meta) -> Meta:
        """Durably record one exact intent; duplicate identities must be byte-equivalent."""
        normalized = self._normalize_execution_envelope(envelope)
        canonical = json.dumps(normalized, sort_keys=True, separators=(",", ":"))
        with self.transaction() as connection:
            self._ensure_execution_envelope_schema(connection)
            existing = connection.execute(
                "SELECT envelope_json FROM execution_envelopes WHERE execution_id=?",
                (normalized["execution_id"],),
            ).fetchone()
            if existing is not None:
                if str(existing["envelope_json"]) != canonical:
                    raise RuntimeError("execution envelope conflicts with durable record")
                return normalized
            connection.execute(
                """INSERT INTO execution_envelopes(
                       execution_id, task_id, task_revision, owner, claim_expires,
                       worktree_key, branch, spec_ref, spec_revision, policy_digest,
                       argv_sha256, timeout_seconds, created_at, envelope_json
                   ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (
                    normalized["execution_id"],
                    normalized["task"],
                    normalized["task_revision"],
                    normalized["owner"],
                    normalized["claim_expires"],
                    normalized["worktree_key"],
                    normalized["branch"],
                    normalized["spec_ref"],
                    normalized["spec_revision"],
                    normalized["policy_digest"],
                    normalized["argv_sha256"],
                    normalized["timeout_seconds"],
                    normalized["created_at"],
                    canonical,
                ),
            )
        return normalized

    def begin_execution_envelope(self, envelope: Meta) -> tuple[bool, Meta | None]:
        """Atomically reserve a launch, or return its existing terminal receipt.

        A prior intent without a result is deliberately reported as uncertain:
        replaying an arbitrary subprocess could duplicate an external effect.
        """
        normalized = self._normalize_execution_envelope(envelope)
        canonical = json.dumps(normalized, sort_keys=True, separators=(",", ":"))
        with self.transaction() as connection:
            self._ensure_execution_envelope_schema(connection)
            existing = connection.execute(
                "SELECT envelope_json FROM execution_envelopes WHERE execution_id=?",
                (normalized["execution_id"],),
            ).fetchone()
            if existing is None:
                connection.execute(
                    """INSERT INTO execution_envelopes(
                           execution_id, task_id, task_revision, owner, claim_expires,
                           worktree_key, branch, spec_ref, spec_revision, policy_digest,
                           argv_sha256, timeout_seconds, created_at, envelope_json
                       ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                    (
                        normalized["execution_id"],
                        normalized["task"],
                        normalized["task_revision"],
                        normalized["owner"],
                        normalized["claim_expires"],
                        normalized["worktree_key"],
                        normalized["branch"],
                        normalized["spec_ref"],
                        normalized["spec_revision"],
                        normalized["policy_digest"],
                        normalized["argv_sha256"],
                        normalized["timeout_seconds"],
                        normalized["created_at"],
                        canonical,
                    ),
                )
                return True, None
            if str(existing["envelope_json"]) != canonical:
                raise RuntimeError("execution envelope conflicts with durable record")
            result = connection.execute(
                "SELECT result_json FROM execution_results WHERE execution_id=?",
                (normalized["execution_id"],),
            ).fetchone()
            if result is None:
                return False, None
            try:
                value = json.loads(str(result["result_json"]))
            except json.JSONDecodeError as error:
                raise StorageCorruptionError("SQLITE_CORRUPT: invalid execution result") from error
            if not isinstance(value, dict):
                raise StorageCorruptionError("SQLITE_CORRUPT: invalid execution result")
            return False, self._normalize_execution_result(cast(Meta, value))

    def load_execution_results(self, task_id: str | None = None) -> list[Meta]:
        """Load terminal outcomes in the same deterministic order as intent projection."""
        connection = self._connect(read_only=True)
        try:
            try:
                rows = connection.execute(
                    """SELECT result_json FROM execution_results AS result
                       JOIN execution_envelopes AS intent
                         ON intent.execution_id=result.execution_id
                       WHERE (? IS NULL OR intent.task_id=?)
                       ORDER BY intent.task_id, intent.created_at, result.execution_id""",
                    (task_id, task_id),
                )
            except sqlite3.OperationalError as error:
                if "no such table" not in str(error).lower():
                    raise
                return []
            records: list[Meta] = []
            for row in rows:
                try:
                    value = json.loads(str(row["result_json"]))
                except json.JSONDecodeError as error:
                    raise StorageCorruptionError(
                        "SQLITE_CORRUPT: invalid execution result"
                    ) from error
                if not isinstance(value, dict):
                    raise StorageCorruptionError("SQLITE_CORRUPT: invalid execution result")
                try:
                    records.append(self._normalize_execution_result(cast(Meta, value)))
                except ValueError as error:
                    raise StorageCorruptionError(
                        "SQLITE_CORRUPT: invalid execution result"
                    ) from error
            return records
        except sqlite3.Error as error:
            raise _translate(error) from error
        finally:
            connection.close()

    def record_execution_result(self, result: Meta) -> Meta:
        """Append one terminal outcome only after its durable execution intent exists."""
        normalized = self._normalize_execution_result(result)
        canonical = json.dumps(normalized, sort_keys=True, separators=(",", ":"))
        with self.transaction() as connection:
            self._ensure_execution_envelope_schema(connection)
            intent = connection.execute(
                "SELECT 1 FROM execution_envelopes WHERE execution_id=?",
                (normalized["execution_id"],),
            ).fetchone()
            if intent is None:
                raise RuntimeError("execution result lacks a durable intent")
            existing = connection.execute(
                "SELECT result_json FROM execution_results WHERE execution_id=?",
                (normalized["execution_id"],),
            ).fetchone()
            if existing is not None:
                if str(existing["result_json"]) != canonical:
                    raise RuntimeError("execution result conflicts with durable record")
                return normalized
            connection.execute(
                """INSERT INTO execution_results(
                       execution_id, classification, returncode, recorded_at, result_json
                   ) VALUES (?, ?, ?, ?, ?)""",
                (
                    normalized["execution_id"],
                    normalized["classification"],
                    normalized["returncode"],
                    normalized["recorded_at"],
                    canonical,
                ),
            )
        return normalized

    def load_issue_series(self) -> list[Meta]:
        """Return authoritative local issue-series receipts in deterministic identity order."""
        connection = self._connect(read_only=True)
        try:
            try:
                rows = connection.execute(
                    """SELECT repository, issue_number, manifest_json, manifest_digest
                       FROM issue_series ORDER BY repository, issue_number"""
                )
            except sqlite3.OperationalError as error:
                if "no such table" not in str(error).lower():
                    raise
                return []
            records: list[Meta] = []
            for row in rows:
                try:
                    manifest = json.loads(str(row["manifest_json"]))
                except json.JSONDecodeError as error:
                    raise StorageCorruptionError(
                        "SQLITE_CORRUPT: invalid issue-series JSON"
                    ) from error
                if not isinstance(manifest, dict):
                    raise StorageCorruptionError("SQLITE_CORRUPT: invalid issue-series manifest")
                records.append(
                    {
                        "manifest": manifest,
                        "manifest_digest": str(row["manifest_digest"]),
                        "series_identity": {
                            "repository": str(row["repository"]),
                            "issue_number": int(row["issue_number"]),
                        },
                    }
                )
            return records
        except sqlite3.Error as error:
            raise _translate(error) from error
        finally:
            connection.close()

    @staticmethod
    def _issue_series_publication_identity(receipt: Meta) -> tuple[str, int]:
        """Extract the normalized local manifest identity from a receipt."""
        identity = receipt.get("series_identity")
        if not isinstance(identity, dict):
            raise ValueError("issue-series publication lacks series identity")
        repository = identity.get("repository")
        issue_number = identity.get("issue_number")
        if (
            not isinstance(repository, str)
            or not repository.startswith("github.com/")
            or repository != repository.lower()
            or "\n" in repository
            or "\r" in repository
        ):
            raise ValueError("issue-series publication has unsafe repository identity")
        if isinstance(issue_number, bool) or not isinstance(issue_number, int) or issue_number < 1:
            raise ValueError("issue-series publication has invalid issue number")
        return repository, issue_number

    @staticmethod
    def _normalize_issue_series_publication(receipt: Meta, recorded_at: str) -> Meta:
        """Return the small, local receipt shape permitted in durable storage."""
        repository, issue_number = SQLiteBackend._issue_series_publication_identity(receipt)
        digest = receipt.get("manifest_digest")
        key = receipt.get("publication_key")
        status = receipt.get("status")
        comment_id = receipt.get("comment_id")
        if not isinstance(digest, str) or not _SHA256_DIGEST.fullmatch(digest):
            raise ValueError("issue-series publication has invalid manifest digest")
        if not isinstance(key, str) or not _PUBLICATION_KEY.fullmatch(key):
            raise ValueError("issue-series publication has invalid publication key")
        expected_key = hashlib.sha256(
            f"issue-series-publication-v1\0{repository}\0{issue_number}\0{digest}".encode()
        ).hexdigest()
        if key != expected_key:
            raise ValueError("issue-series publication key disagrees with its identity")
        if not isinstance(status, str) or status not in _PUBLICATION_STATUSES:
            raise ValueError("issue-series publication has invalid status")
        if comment_id is not None and (
            not isinstance(comment_id, str) or not _COMMENT_ID.fullmatch(comment_id)
        ):
            raise ValueError("issue-series publication has invalid comment identifier")
        if status not in {"published", "already_published"} and comment_id is not None:
            raise ValueError("deferred issue-series publication cannot carry a comment identifier")
        if not isinstance(recorded_at, str) or not recorded_at or "\n" in recorded_at:
            raise ValueError("issue-series publication has invalid recorded time")
        return {
            "series_identity": {"repository": repository, "issue_number": issue_number},
            "manifest_digest": digest,
            "publication_key": key,
            "status": status,
            "comment_id": comment_id,
            "recorded_at": recorded_at,
        }

    def load_issue_series_publications(self) -> list[Meta]:
        """Return normalized publication receipts in deterministic identity order."""
        connection = self._connect(read_only=True)
        try:
            try:
                rows = connection.execute(
                    """SELECT repository, issue_number, manifest_digest, publication_key,
                              status, comment_id, recorded_at
                       FROM issue_series_publications
                       ORDER BY repository, issue_number, manifest_digest, publication_key"""
                )
            except sqlite3.OperationalError as error:
                if "no such table" not in str(error).lower():
                    raise
                return []
            return [
                {
                    "series_identity": {
                        "repository": str(row["repository"]),
                        "issue_number": int(row["issue_number"]),
                    },
                    "manifest_digest": str(row["manifest_digest"]),
                    "publication_key": str(row["publication_key"]),
                    "status": str(row["status"]),
                    "comment_id": row["comment_id"],
                    "recorded_at": str(row["recorded_at"]),
                }
                for row in rows
            ]
        except sqlite3.Error as error:
            raise _translate(error) from error
        finally:
            connection.close()

    def record_issue_series_publication(
        self,
        receipt_or_repository: Meta | str,
        issue_number: int | None = None,
        record: Meta | None = None,
        *,
        recorded_at: str | None = None,
    ) -> Meta:
        """Atomically persist one normalized publication receipt or return its exact replay.

        A duplicate identity or correlation key is idempotent only when every
        normalized fact agrees.  This avoids silently converting an uncertain
        request into a different durable outcome.

        The ``repository, issue_number, record`` form is a narrow adapter for
        the command layer.  Its optional renderer digest is intentionally not
        copied to durable storage; the local manifest digest is the binding
        fact.  Direct callers pass the complete normalized receipt and an
        explicit ``recorded_at`` value.
        """
        if isinstance(receipt_or_repository, str):
            if issue_number is None or record is None or recorded_at is not None:
                raise ValueError("issue-series publication adapter arguments are incomplete")
            receipt: Meta = {
                "series_identity": {
                    "repository": receipt_or_repository,
                    "issue_number": issue_number,
                },
                "manifest_digest": record.get("manifest_digest"),
                "publication_key": record.get("publication_key"),
                "status": record.get("status"),
                "comment_id": record.get("comment_id") or None,
            }
            timestamp = datetime.now(UTC).isoformat()
        else:
            if issue_number is not None or record is not None or recorded_at is None:
                raise ValueError(
                    "issue-series publication receipt requires an explicit recorded time"
                )
            receipt = receipt_or_repository
            timestamp = recorded_at
        normalized = self._normalize_issue_series_publication(receipt, timestamp)
        identity = cast(Meta, normalized["series_identity"])
        repository = str(identity["repository"])
        issue_number = int(identity["issue_number"])
        digest = str(normalized["manifest_digest"])
        key = str(normalized["publication_key"])
        with self.transaction() as connection:
            self._ensure_issue_series_schema(connection)
            manifest = connection.execute(
                """SELECT manifest_digest FROM issue_series
                   WHERE repository=? AND issue_number=?""",
                (repository, issue_number),
            ).fetchone()
            if manifest is None or str(manifest["manifest_digest"]) != digest:
                raise RuntimeError("issue-series publication does not match a local manifest")
            existing = connection.execute(
                """SELECT repository, issue_number, manifest_digest, publication_key,
                              status, comment_id, recorded_at
                       FROM issue_series_publications
                       WHERE (repository=? AND issue_number=? AND manifest_digest=?)
                          OR publication_key=?""",
                (repository, issue_number, digest, key),
            ).fetchone()
            if existing is not None:
                replay = {
                    "series_identity": {
                        "repository": str(existing["repository"]),
                        "issue_number": int(existing["issue_number"]),
                    },
                    "manifest_digest": str(existing["manifest_digest"]),
                    "publication_key": str(existing["publication_key"]),
                    "status": str(existing["status"]),
                    "comment_id": existing["comment_id"],
                    "recorded_at": str(existing["recorded_at"]),
                }
                if {key: value for key, value in replay.items() if key != "recorded_at"} != {
                    key: value for key, value in normalized.items() if key != "recorded_at"
                }:
                    raise RuntimeError(
                        "issue-series publication receipt conflicts with durable record"
                    )
                return replay
            connection.execute(
                """INSERT INTO issue_series_publications(
                       repository, issue_number, manifest_digest, publication_key,
                       status, comment_id, recorded_at
                   ) VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (
                    repository,
                    issue_number,
                    digest,
                    key,
                    normalized["status"],
                    normalized["comment_id"],
                    timestamp,
                ),
            )
        return normalized

    def resolve_issue_series_publication(
        self, repository: str, issue_number: int, record: Meta
    ) -> Meta:
        """Replace only a pre-call ambiguous receipt with one normalized outcome."""
        receipt: Meta = {
            "series_identity": {"repository": repository, "issue_number": issue_number},
            "manifest_digest": record.get("manifest_digest"),
            "publication_key": record.get("publication_key"),
            "status": record.get("status"),
            "comment_id": record.get("comment_id") or None,
        }
        normalized = self._normalize_issue_series_publication(
            receipt, datetime.now(UTC).isoformat()
        )
        identity = cast(Meta, normalized["series_identity"])
        with self.transaction() as connection:
            existing = connection.execute(
                """SELECT status FROM issue_series_publications
                   WHERE repository=? AND issue_number=?
                     AND manifest_digest=? AND publication_key=?""",
                (
                    identity["repository"],
                    identity["issue_number"],
                    normalized["manifest_digest"],
                    normalized["publication_key"],
                ),
            ).fetchone()
            if existing is None:
                raise RuntimeError("issue-series publication reservation is missing")
            if str(existing["status"]) in {"published", "already_published"}:
                if (
                    str(existing["status"]) != str(normalized["status"])
                    or existing["comment_id"] != normalized["comment_id"]
                ):
                    raise RuntimeError("issue-series publication receipt is already final")
                return normalized
            connection.execute(
                """UPDATE issue_series_publications SET status=?, comment_id=?, recorded_at=?
                   WHERE repository=? AND issue_number=?
                     AND manifest_digest=? AND publication_key=?""",
                (
                    normalized["status"],
                    normalized["comment_id"],
                    normalized["recorded_at"],
                    identity["repository"],
                    identity["issue_number"],
                    normalized["manifest_digest"],
                    normalized["publication_key"],
                ),
            )
        return normalized

    def create_issue_series(
        self,
        receipt: Meta,
        created: Sequence[Task],
        *,
        expected_state_digest: str,
        recorded_at: str,
    ) -> None:
        """Create a whole validated series in the same SQLite transaction and CAS fence."""
        identity = cast(Meta, receipt["series_identity"])
        repository = str(identity["repository"])
        issue_number = int(identity["issue_number"])
        manifest = cast(Meta, receipt["manifest"])
        manifest_digest = str(receipt["manifest_digest"])
        with self.transaction() as connection:
            self._ensure_issue_series_schema(connection)
            current = self._load(connection)
            if self._issue_series_state_digest(current) != expected_state_digest:
                raise RuntimeError("STALE_STATE: re-run issue-series plan before create")
            if (
                connection.execute(
                    "SELECT 1 FROM issue_series WHERE repository=? AND issue_number=?",
                    (repository, issue_number),
                ).fetchone()
                is not None
            ):
                raise RuntimeError("issue-series manifest identity already exists")
            current_ids = {str(meta["id"]) for _path, meta, _body in current}
            created_ids = [str(meta["id"]) for _path, meta, _body in created]
            collisions = sorted(current_ids.intersection(created_ids))
            if collisions:
                raise RuntimeError(
                    "issue-series identifiers already exist: " + ", ".join(collisions)
                )
            if len(created_ids) != len(set(created_ids)):
                raise RuntimeError("issue-series contains duplicate task identifiers")
            connection.execute(
                """INSERT INTO issue_series(
                       repository, issue_number, manifest_json, manifest_digest
                   )
                   VALUES (?, ?, ?, ?)""",
                (
                    repository,
                    issue_number,
                    json.dumps(manifest, sort_keys=True, separators=(",", ":")),
                    manifest_digest,
                ),
            )
            for filename, meta, body in created:
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
                connection.executemany(
                    "INSERT INTO dependencies(task_id, dependency_id) VALUES (?, ?)",
                    [(meta["id"], value) for value in meta.get("depends_on", [])],
                )
                connection.execute(
                    """INSERT INTO events(task_id, revision, kind, recorded_at, note)
                       VALUES (?, ?, 'issue-series-create', ?, ?)""",
                    (
                        meta["id"],
                        meta["task_revision"],
                        recorded_at,
                        "Created from a locally validated issue-series manifest.",
                    ),
                )
                linkage = cast(Meta, meta["issue_series"])
                connection.execute(
                    """INSERT INTO issue_series_members
                       (repository, issue_number, task_id, member_id) VALUES (?, ?, ?, ?)""",
                    (repository, issue_number, meta["id"], linkage["member_id"]),
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


ISSUE_SERIES_STATEMENTS = (
    """CREATE TABLE IF NOT EXISTS issue_series(
 repository TEXT NOT NULL,
 issue_number INTEGER NOT NULL CHECK(issue_number > 0),
 manifest_json TEXT NOT NULL CHECK(json_valid(manifest_json)),
 manifest_digest TEXT NOT NULL CHECK(length(manifest_digest)=71),
 PRIMARY KEY(repository, issue_number)
) STRICT""",
    """CREATE TABLE IF NOT EXISTS issue_series_members(
 repository TEXT NOT NULL,
 issue_number INTEGER NOT NULL,
 task_id TEXT NOT NULL REFERENCES tasks(id) ON DELETE CASCADE,
 member_id TEXT NOT NULL,
 PRIMARY KEY(repository, issue_number, task_id),
 UNIQUE(repository, issue_number, member_id),
 FOREIGN KEY(repository, issue_number)
   REFERENCES issue_series(repository, issue_number) ON DELETE CASCADE
) STRICT""",
    """CREATE TABLE IF NOT EXISTS issue_series_publications(
 repository TEXT NOT NULL,
 issue_number INTEGER NOT NULL CHECK(issue_number > 0),
 manifest_digest TEXT NOT NULL CHECK(length(manifest_digest)=71),
 publication_key TEXT NOT NULL CHECK(length(publication_key)=64),
 status TEXT NOT NULL CHECK(status IN (
   'published','already_published','dry_run','deferred_unavailable',
   'deferred_unauthorized','deferred_timeout','deferred_conflict',
   'deferred_wrong_identity','deferred_closed','deferred_moved','ambiguous')),
 comment_id TEXT CHECK(comment_id IS NULL OR (length(comment_id) BETWEEN 1 AND 128)),
 recorded_at TEXT NOT NULL,
 PRIMARY KEY(repository, issue_number, manifest_digest),
 UNIQUE(publication_key),
 FOREIGN KEY(repository, issue_number)
   REFERENCES issue_series(repository, issue_number) ON DELETE CASCADE,
 CHECK((status IN ('published','already_published')) OR comment_id IS NULL)
) STRICT""",
)
ISSUE_SERIES_SCHEMA = "\n".join(f"{statement};" for statement in ISSUE_SERIES_STATEMENTS)


EXECUTION_ENVELOPE_STATEMENTS = (
    """CREATE TABLE IF NOT EXISTS execution_envelopes(
 execution_id TEXT PRIMARY KEY CHECK(length(execution_id)=36),
 task_id TEXT NOT NULL REFERENCES tasks(id) ON DELETE RESTRICT,
 task_revision INTEGER NOT NULL CHECK(task_revision >= 1),
 owner TEXT NOT NULL, claim_expires TEXT NOT NULL, worktree_key TEXT NOT NULL,
 branch TEXT NOT NULL, spec_ref TEXT, spec_revision INTEGER,
 policy_digest TEXT NOT NULL CHECK(length(policy_digest)=64),
 argv_sha256 TEXT NOT NULL CHECK(length(argv_sha256)=64),
 timeout_seconds REAL NOT NULL CHECK(timeout_seconds > 0), created_at TEXT NOT NULL,
 envelope_json TEXT NOT NULL CHECK(json_valid(envelope_json)),
 CHECK((spec_ref IS NULL) = (spec_revision IS NULL))
) STRICT""",
    """CREATE TABLE IF NOT EXISTS execution_results(
 execution_id TEXT PRIMARY KEY REFERENCES execution_envelopes(execution_id) ON DELETE RESTRICT,
 classification TEXT NOT NULL CHECK(classification IN ('EXIT','SUBPROCESS_TIMEOUT')),
 returncode INTEGER NOT NULL, recorded_at TEXT NOT NULL,
 result_json TEXT NOT NULL CHECK(json_valid(result_json))
) STRICT""",
)
EXECUTION_ENVELOPE_SCHEMA = "\n".join(
    f"{statement};" for statement in EXECUTION_ENVELOPE_STATEMENTS
)


SCHEMA = (
    """
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
    + ISSUE_SERIES_SCHEMA
    + EXECUTION_ENVELOPE_SCHEMA
)


def create_database(  # noqa: C901
    path: Path,
    binding: Meta,
    tasks: Sequence[Task],
    *,
    imported_at: str,
    source_backend: str,
    source_checkpoint: str,
    command_results: Sequence[Meta] = (),
    session_records: Sequence[Meta] = (),
    checkpoint_records: Sequence[Meta] = (),
    issue_series: Sequence[Meta] = (),
    issue_series_publications: Sequence[Meta] = (),
    execution_envelopes: Sequence[Meta] = (),
    execution_results: Sequence[Meta] = (),
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
            for receipt in issue_series:
                identity = cast(Meta, receipt["series_identity"])
                repository = str(identity["repository"])
                issue_number = int(identity["issue_number"])
                manifest = cast(Meta, receipt["manifest"])
                connection.execute(
                    """INSERT INTO issue_series(
                           repository, issue_number, manifest_json, manifest_digest
                       ) VALUES (?, ?, ?, ?)""",
                    (
                        repository,
                        issue_number,
                        json.dumps(manifest, sort_keys=True, separators=(",", ":")),
                        str(receipt["manifest_digest"]),
                    ),
                )
                connection.executemany(
                    """INSERT INTO issue_series_members(
                           repository, issue_number, task_id, member_id
                       ) VALUES (?, ?, ?, ?)""",
                    [
                        (repository, issue_number, str(member_id), str(member_id))
                        for member_id in receipt["task_ids"]
                    ],
                )
            for receipt in issue_series_publications:
                normalized = SQLiteBackend._normalize_issue_series_publication(receipt, imported_at)
                identity = cast(Meta, normalized["series_identity"])
                connection.execute(
                    """INSERT INTO issue_series_publications(
                           repository, issue_number, manifest_digest, publication_key,
                           status, comment_id, recorded_at
                       ) VALUES (?, ?, ?, ?, ?, ?, ?)""",
                    (
                        identity["repository"],
                        identity["issue_number"],
                        normalized["manifest_digest"],
                        normalized["publication_key"],
                        normalized["status"],
                        normalized["comment_id"],
                        normalized["recorded_at"],
                    ),
                )
            normalized_envelopes = [
                SQLiteBackend._normalize_execution_envelope(envelope)
                for envelope in execution_envelopes
            ]
            normalized_results = [
                SQLiteBackend._normalize_execution_result(result) for result in execution_results
            ]
            envelope_ids = {str(envelope["execution_id"]) for envelope in normalized_envelopes}
            if len(envelope_ids) != len(normalized_envelopes):
                raise ValueError("execution envelope import has duplicate identities")
            if any(
                str(result["execution_id"]) not in envelope_ids for result in normalized_results
            ):
                raise ValueError("execution result import lacks an execution intent")
            if len({str(result["execution_id"]) for result in normalized_results}) != len(
                normalized_results
            ):
                raise ValueError("execution result import has duplicate identities")
            for envelope in normalized_envelopes:
                connection.execute(
                    """INSERT INTO execution_envelopes(
                           execution_id, task_id, task_revision, owner, claim_expires,
                           worktree_key, branch, spec_ref, spec_revision, policy_digest,
                           argv_sha256, timeout_seconds, created_at, envelope_json
                       ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                    (
                        envelope["execution_id"],
                        envelope["task"],
                        envelope["task_revision"],
                        envelope["owner"],
                        envelope["claim_expires"],
                        envelope["worktree_key"],
                        envelope["branch"],
                        envelope["spec_ref"],
                        envelope["spec_revision"],
                        envelope["policy_digest"],
                        envelope["argv_sha256"],
                        envelope["timeout_seconds"],
                        envelope["created_at"],
                        json.dumps(envelope, sort_keys=True, separators=(",", ":")),
                    ),
                )
            for result in normalized_results:
                connection.execute(
                    """INSERT INTO execution_results(
                           execution_id, classification, returncode, recorded_at, result_json
                       ) VALUES (?, ?, ?, ?, ?)""",
                    (
                        result["execution_id"],
                        result["classification"],
                        result["returncode"],
                        result["recorded_at"],
                        json.dumps(result, sort_keys=True, separators=(",", ":")),
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
            if session_records:
                connection.execute(
                    """CREATE TABLE IF NOT EXISTS session_records(
                       sequence INTEGER PRIMARY KEY AUTOINCREMENT,
                       task_id TEXT NOT NULL REFERENCES tasks(id) ON DELETE CASCADE,
                       task_revision INTEGER NOT NULL,
                       record_json TEXT NOT NULL CHECK(json_valid(record_json)),
                       recorded_at TEXT NOT NULL,
                       UNIQUE(task_id, task_revision)) STRICT"""
                )
            if checkpoint_records:
                connection.execute(
                    """CREATE TABLE IF NOT EXISTS checkpoint_records(
                       sequence INTEGER PRIMARY KEY AUTOINCREMENT,
                       task_id TEXT NOT NULL REFERENCES tasks(id) ON DELETE CASCADE,
                       task_revision INTEGER NOT NULL,
                       record_json TEXT NOT NULL CHECK(json_valid(record_json)),
                       recorded_at TEXT NOT NULL,
                       UNIQUE(task_id, task_revision)) STRICT"""
                )
            if session_records:
                connection.executemany(
                    """INSERT INTO session_records
                       (task_id, task_revision, record_json, recorded_at)
                       VALUES (:task, :task_revision, :record_json, :recorded_at)""",
                    [
                        {
                            "task": record["task"],
                            "task_revision": record["task_revision"],
                            "record_json": json.dumps(
                                record, sort_keys=True, separators=(",", ":")
                            ),
                            "recorded_at": record["recorded_at"],
                        }
                        for record in session_records
                    ],
                )
            if checkpoint_records:
                connection.executemany(
                    """INSERT INTO checkpoint_records
                       (task_id, task_revision, record_json, recorded_at)
                       VALUES (:task, :task_revision, :record_json, :recorded_at)""",
                    [
                        {
                            "task": record["task"],
                            "task_revision": record["task_revision"],
                            "record_json": json.dumps(
                                record, sort_keys=True, separators=(",", ":")
                            ),
                            "recorded_at": record["recorded_at"],
                        }
                        for record in checkpoint_records
                    ],
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


def bind_sqlite_backend(
    path: Path,
    binding: Meta,
    tasks_root: Path,
    backend_binding: SQLiteBackendBinding | SQLiteAuthorityBinding | SQLiteMutationBinding,
    scope: object,
) -> SQLiteBackend:
    """Build a bound backend from the concrete ordered admission scope.

    This is the adapter-owned integration seam.  ``scope`` must be a real
    ``LockDomainScope``; arbitrary context managers are rejected.  The scope
    owns common -> control -> authority lock ordering and durable admission.
    The legacy constructor remains available for unbound/read-only callers.
    """
    from tools.lock_domain_scope import LockDomainScope

    if not isinstance(scope, LockDomainScope):
        raise TypeError("SQLite backend requires adapter-owned LockDomainScope")
    if not isinstance(backend_binding, SQLiteAuthorityBinding):
        raise TypeError("SQLite backend factory requires dual authority binding")
    session_store = getattr(scope, "_session_store", None)
    scope_control = getattr(session_store, "_control", None)
    fence = getattr(scope, "_authority_fence", None)
    control_binding = (
        backend_binding._control
        if isinstance(backend_binding, SQLiteAuthorityBinding)
        else backend_binding
    )
    if scope_control is not control_binding._control_store:
        raise ValueError("SQLite admission scope is bound to a foreign control store")
    if getattr(fence, "control_store", None) != control_binding.path:
        raise ValueError("SQLite admission scope is bound to a foreign authority fence")
    return SQLiteBackend(
        path,
        binding,
        tasks_root,
        mutation_scope=scope.hold,
        backend_binding=backend_binding,
        _admission_capability=_FACTORY_SENTINEL,
    )


class SQLiteAuthorityWriteAdapter:
    """Typed authority writer bound to one lock-domain scope.

    The raw backend is intentionally retained privately.  Each operation must
    enter the caller-owned common -> control -> authority scope first; the
    backend transaction then performs only the SQLite/descriptor checks while
    those locks remain held.  This adapter does not authorize upgrade phases
    and is not connected to the public upgrade dispatcher.
    """

    __slots__ = ("_backend",)

    def __init__(self, backend: SQLiteBackend, sentinel: object) -> None:
        if sentinel is not _FACTORY_SENTINEL:
            raise TypeError("SQLiteAuthorityWriteAdapter must be issued by its factory")
        self._backend = backend

    def mutate(
        self,
        task_id: str,
        expected_revision: int,
        kind: str,
        at: str,
        transition: Callable[[Meta, list[Task]], tuple[str, str]],
        session_record: Meta | None = None,
        session_factory: Callable[[Meta], Meta] | None = None,
        checkpoint_factory: Callable[[Meta], Meta] | None = None,
    ) -> None:
        """Apply one fenced task transition."""
        self._backend.mutate(
            task_id,
            expected_revision,
            kind,
            at,
            transition,
            session_record,
            session_factory,
            checkpoint_factory,
        )

    def update_observations(self, observations: dict[str, Meta], at: str) -> None:
        """Persist fenced live-worktree observations."""
        self._backend.update_observations(observations, at)

    def append_command_result(
        self,
        task_id: str,
        owner: str,
        command_hash: str,
        returncode: int,
        classification: str,
        recorded_at: str,
    ) -> None:
        """Persist fenced command evidence."""
        self._backend.append_command_result(
            task_id, owner, command_hash, returncode, classification, recorded_at
        )

    def retire(
        self,
        project: Callable[[list[Task]], None],
        switch_selector: Callable[[], None],
    ) -> None:
        """Retire authority through the fenced route."""
        self._backend.retire(project, switch_selector)


def bind_sqlite_authority_writer(
    path: Path,
    binding: Meta,
    tasks_root: Path,
    authority_binding: SQLiteAuthorityBinding,
    scope: object,
) -> SQLiteAuthorityWriteAdapter:
    """Issue typed scope-bound writes without exposing a raw backend."""
    from tools.lock_domain_scope import LockDomainScope

    if not isinstance(scope, LockDomainScope):
        raise TypeError("authority writer requires adapter-owned LockDomainScope")
    if not isinstance(authority_binding, SQLiteAuthorityBinding):
        raise TypeError("authority writer requires SQLiteAuthorityBinding")
    if authority_binding.path != path.absolute():
        raise ValueError("authority writer path does not match its binding")
    backend = bind_sqlite_backend(path, binding, tasks_root, authority_binding, scope)
    return SQLiteAuthorityWriteAdapter(backend, _FACTORY_SENTINEL)


def bind_released_sqlite_backend(
    path: Path,
    binding: Meta,
    tasks_root: Path,
    fence: object,
    common_lock: Callable[[], AbstractContextManager[object]],
    session_identity: object | None = None,
) -> SQLiteBackend:
    """Build the public writer backend for a provisioned released barrier.

    This factory is intentionally separate from the held upgrade scope: normal
    coordination must continue while no upgrade is active, while the fence
    still rejects held, releasing, ambiguous, missing, or replaced control
    state before SQLite opens a write transaction.
    """
    from tools.mutation_fence import MutationFence

    if not isinstance(fence, MutationFence):
        raise TypeError("released SQLite backend requires a concrete mutation fence")
    if session_identity is not None:
        fence.bind_session_identity(session_identity)
    authority_binding = SQLiteMutationBinding.bind(fence, path)
    return SQLiteBackend(
        path,
        binding,
        tasks_root,
        mutation_scope=lambda: fence.mutation_scope(common_lock),
        backend_binding=authority_binding,
        _admission_capability=_FACTORY_SENTINEL,
    )
