# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Provisioned authority-lock and mutation-fence foundation.

This module is an optional seam: ordinary coordination does not construct it.
The SQLite backend accepts it only when an explicitly provisioned caller binds
the route; ``storage_backend`` remains unbound. Upgrade admission and
apply/rollback remain rejection-only.

This slice does not claim WAL/SHM crash consistency, process-death recovery,
or refinement of the durable barrier protocol; those require a separate
formal and multiprocess evidence slice.
"""

from __future__ import annotations

import errno
import fcntl
import hashlib
import json
import os
import re
import secrets
import sqlite3
import stat
import threading
import time
from collections.abc import Callable, Iterator
from contextlib import AbstractContextManager, contextmanager, suppress
from dataclasses import asdict, dataclass
from pathlib import Path


class MutationFenceError(RuntimeError):
    """A provisioned authority fence is missing or no longer trustworthy."""


SCHEMA_VERSION = 1
LIFECYCLE_STATES = {"absent", "active", "clean_checkpointed"}
LOCK_TIMEOUT_SECONDS = 10.0
LOCK_POLL_SECONDS = 0.01
_PROJECT_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,127}")


def _acquire_file_lock(descriptor: int, label: str, timeout: float | None = None) -> None:
    """Acquire a fence lock with a bounded deadline and fail closed."""
    if timeout is None:
        timeout = LOCK_TIMEOUT_SECONDS
    if type(timeout) is not float or timeout <= 0:
        raise MutationFenceError("fence lock timeout is invalid")
    deadline = time.monotonic() + timeout
    while True:
        try:
            fcntl.flock(descriptor, fcntl.LOCK_EX | fcntl.LOCK_NB)
            return
        except BlockingIOError as error:
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise MutationFenceError(
                    f"{label} acquisition timed out after {timeout:.1f}s"
                ) from error
            time.sleep(min(LOCK_POLL_SECONDS, remaining))


@dataclass(frozen=True, slots=True)
class DescriptorIdentity:
    """Stable identity of one retained project-bound filesystem object."""

    device: int
    inode: int
    parent_device: int
    parent_inode: int
    mode: int
    owner: int
    links: int


def _identity(status: os.stat_result, parent: os.stat_result) -> DescriptorIdentity:
    return DescriptorIdentity(
        status.st_dev,
        status.st_ino,
        parent.st_dev,
        parent.st_ino,
        stat.S_IMODE(status.st_mode),
        status.st_uid,
        status.st_nlink,
    )


def _canonical(value: dict[str, object]) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")


def _digest(value: dict[str, object]) -> str:
    return "sha256:" + hashlib.sha256(_canonical(value)).hexdigest()


def _read_json(path: Path, label: str) -> dict[str, object]:
    parent_fd = -1
    descriptor = -1
    try:
        parent_fd, parent = _parent(path)
        descriptor = os.open(path.name, os.O_RDONLY | os.O_NOFOLLOW, dir_fd=parent_fd)
        before = os.fstat(descriptor)
        if (
            not stat.S_ISREG(before.st_mode)
            or before.st_uid != os.geteuid()
            or before.st_nlink != 1
            or stat.S_IMODE(before.st_mode) != 0o600
        ):
            raise MutationFenceError(f"{label} is not an owner-only regular file")
        chunks: list[bytes] = []
        while chunk := os.read(descriptor, 8192):
            chunks.append(chunk)
        after = os.fstat(descriptor)
        if before.st_dev != after.st_dev or before.st_ino != after.st_ino:
            raise MutationFenceError(f"{label} identity changed")
        if (
            os.fstat(parent_fd).st_dev != parent.st_dev
            or os.fstat(parent_fd).st_ino != parent.st_ino
        ):
            raise MutationFenceError(f"{label} parent identity changed")
        value = json.loads(b"".join(chunks).decode("utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        raise MutationFenceError(f"{label} is unreadable") from error
    finally:
        if descriptor >= 0:
            os.close(descriptor)
        if parent_fd >= 0:
            os.close(parent_fd)
    if not isinstance(value, dict):
        raise MutationFenceError(f"{label} schema is invalid")
    return value


def _validate_binding(binding: object, project_id: str) -> dict[str, object]:
    if not isinstance(binding, dict):
        raise MutationFenceError("control binding schema is invalid")
    if binding.get("identity_digest") != _digest(
        {key: value for key, value in binding.items() if key != "identity_digest"}
    ):
        raise MutationFenceError("control binding digest is invalid")
    if binding.get("project_id") != project_id:
        raise MutationFenceError("control binding project identity changed")
    return binding


def _open_binding_descriptor(
    path: Path, project_id: str
) -> tuple[int, int, os.stat_result, os.stat_result, dict[str, object], bytes]:
    parent_fd, parent = _parent(path)
    descriptor = -1
    try:
        descriptor = os.open(path.name, os.O_RDONLY | os.O_NOFOLLOW, dir_fd=parent_fd)
        before = os.fstat(descriptor)
        if (
            not stat.S_ISREG(before.st_mode)
            or before.st_uid != os.geteuid()
            or before.st_nlink != 1
            or stat.S_IMODE(before.st_mode) != 0o600
        ):
            raise MutationFenceError("control binding is not an owner-only regular file")
        binding_bytes = os.read(descriptor, 1 << 20)
        if os.read(descriptor, 1):
            raise MutationFenceError("control binding is too large")
        if (
            before.st_dev != os.fstat(descriptor).st_dev
            or before.st_ino != os.fstat(descriptor).st_ino
        ):
            raise MutationFenceError("control binding identity changed")
        binding = _validate_binding(json.loads(binding_bytes.decode("utf-8")), project_id)
        return parent_fd, descriptor, parent, before, binding, binding_bytes
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        if descriptor >= 0:
            os.close(descriptor)
        os.close(parent_fd)
        raise MutationFenceError("control binding is unreadable") from error
    except MutationFenceError:
        if descriptor >= 0:
            os.close(descriptor)
        os.close(parent_fd)
        raise


def _verify_binding_unchanged(
    path: Path,
    parent_fd: int,
    parent: os.stat_result,
    descriptor: int,
    before: os.stat_result,
    original: bytes,
) -> None:
    if _identity(os.fstat(descriptor), os.fstat(parent_fd)) != _identity(before, parent):
        raise MutationFenceError("control binding identity changed")
    os.lseek(descriptor, 0, os.SEEK_SET)
    if os.read(descriptor, 1 << 20) != original:
        raise MutationFenceError("control binding contents changed")
    path_descriptor = os.open(path.name, os.O_RDONLY | os.O_NOFOLLOW, dir_fd=parent_fd)
    try:
        if _identity(os.fstat(path_descriptor), os.fstat(parent_fd)) != _identity(before, parent):
            raise MutationFenceError("control binding identity changed")
    finally:
        os.close(path_descriptor)


def _parent_after_binding(
    path: Path, binding_descriptor: int, binding_parent_fd: int
) -> tuple[int, os.stat_result]:
    try:
        return _parent(path)
    except (MutationFenceError, OSError):
        os.close(binding_descriptor)
        os.close(binding_parent_fd)
        raise


def _parent(path: Path) -> tuple[int, os.stat_result]:
    if not path.is_absolute() or ".." in path.parts or path.name in {"", ".", ".."}:
        raise MutationFenceError("fence path is not canonical and absolute")
    descriptor = os.open("/", os.O_RDONLY | os.O_DIRECTORY)
    try:
        for part in path.parent.parts[1:]:
            child = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=descriptor)
            os.close(descriptor)
            descriptor = child
        status = os.fstat(descriptor)
        if status.st_uid != os.geteuid() or stat.S_IMODE(status.st_mode) != 0o700:
            raise MutationFenceError("fence parent requires an owner-only provisioned directory")
        return descriptor, status
    except Exception:
        os.close(descriptor)
        raise


def _existing(path: Path, label: str) -> DescriptorIdentity:
    parent_fd, parent = _parent(path)
    descriptor = -1
    try:
        descriptor = os.open(path.name, os.O_RDWR | os.O_NOFOLLOW, dir_fd=parent_fd)
        status = os.fstat(descriptor)
        if (
            not stat.S_ISREG(status.st_mode)
            or status.st_uid != os.geteuid()
            or status.st_nlink != 1
            or stat.S_IMODE(status.st_mode) != 0o600
        ):
            raise MutationFenceError(f"{label} is not an owner-only regular file")
        return _identity(status, parent)
    except FileNotFoundError as error:
        raise MutationFenceError(f"{label} is missing") from error
    except OSError as error:
        raise MutationFenceError(f"{label} descriptor is unsafe") from error
    finally:
        if descriptor >= 0:
            os.close(descriptor)
        os.close(parent_fd)


def _create_lock(path: Path) -> DescriptorIdentity:
    parent_fd, parent = _parent(path)
    descriptor = -1
    try:
        try:
            descriptor = os.open(
                path.name,
                os.O_CREAT | os.O_EXCL | os.O_RDWR | os.O_NOFOLLOW,
                0o600,
                dir_fd=parent_fd,
            )
            os.fsync(descriptor)
            os.fsync(parent_fd)
        except FileExistsError:
            descriptor = os.open(path.name, os.O_RDWR | os.O_NOFOLLOW, dir_fd=parent_fd)
        status = os.fstat(descriptor)
        if not stat.S_ISREG(status.st_mode) or status.st_uid != os.geteuid():
            raise MutationFenceError("authority.lock is not an owner-only regular file")
        if stat.S_IMODE(status.st_mode) != 0o600 or status.st_nlink != 1:
            raise MutationFenceError("authority.lock permissions or links are unsafe")
        return _identity(status, parent)
    except OSError as error:
        raise MutationFenceError("authority.lock cannot be provisioned safely") from error
    finally:
        if descriptor >= 0:
            os.close(descriptor)
        os.close(parent_fd)


def _atomic_json(path: Path, value: dict[str, object]) -> None:
    parent_fd, _ = _parent(path)
    temporary = path.parent / f".{path.name}.{secrets.token_hex(8)}.tmp"
    descriptor = -1
    try:
        descriptor = os.open(
            temporary.name,
            os.O_CREAT | os.O_EXCL | os.O_WRONLY | os.O_NOFOLLOW,
            0o600,
            dir_fd=parent_fd,
        )
        payload = _canonical(value) + b"\n"
        os.write(descriptor, payload)
        os.fsync(descriptor)
        os.close(descriptor)
        descriptor = -1
        os.rename(temporary.name, path.name, src_dir_fd=parent_fd, dst_dir_fd=parent_fd)
        os.fsync(parent_fd)
    except OSError as error:
        raise MutationFenceError("fence record publication is ambiguous") from error
    finally:
        if descriptor >= 0:
            os.close(descriptor)
        with suppress(FileNotFoundError):
            os.unlink(temporary.name, dir_fd=parent_fd)
        os.close(parent_fd)


def provision_control_binding(
    control_store: Path, descriptor: Path, control_lock: Path, project_id: str
) -> dict[str, object]:
    """Bind an existing control store and publish its separate descriptor."""
    if _PROJECT_ID.fullmatch(project_id) is None:
        raise MutationFenceError("project identifier is not canonical and opaque")
    store_identity = _existing(control_store, "control store")
    lock_identity = _create_lock(control_lock)
    record: dict[str, object] = {
        "schema_version": SCHEMA_VERSION,
        "project_id": project_id,
        "control_store": asdict(store_identity),
        "control_lock": asdict(lock_identity),
    }
    record["identity_digest"] = _digest(record)
    if descriptor.exists():
        if _read_json(descriptor, "control binding") != record:
            raise MutationFenceError("control binding is already provisioned with another identity")
        return record
    _atomic_json(descriptor, record)
    return record


def provision(
    authority: Path,
    marker: Path,
    lifecycle: Path,
    authority_lock: Path,
    project_id: str,
) -> dict[str, object]:
    """Bind an existing authority and publish its fence records atomically."""
    if _PROJECT_ID.fullmatch(project_id) is None:
        raise MutationFenceError("project identifier is not canonical and opaque")
    authority_identity = _existing(authority, "authority database")
    lock_identity = _create_lock(authority_lock)
    record: dict[str, object] = {
        "schema_version": SCHEMA_VERSION,
        "project_id": project_id,
        "authority": asdict(authority_identity),
        "authority_lock": asdict(lock_identity),
        "lifecycle": str(lifecycle.name),
    }
    record["identity_digest"] = _digest(record)
    lifecycle_record = {
        "schema_version": SCHEMA_VERSION,
        "authority_digest": record["identity_digest"],
        "state": "clean_checkpointed",
        "generation": 0,
    }
    lifecycle_record["record_digest"] = _digest(lifecycle_record)
    if marker.exists():
        existing = _read_json(marker, "authority fence marker")
        if existing != record:
            raise MutationFenceError("authority fence is already provisioned with another identity")
        if _read_json(lifecycle, "authority lifecycle") != lifecycle_record:
            raise MutationFenceError(
                "authority lifecycle is already provisioned with another state"
            )
        return record
    if lifecycle.exists():
        if _read_json(lifecycle, "authority lifecycle") != lifecycle_record:
            raise MutationFenceError("authority lifecycle already exists with another identity")
    else:
        _atomic_json(lifecycle, lifecycle_record)
    _atomic_json(marker, record)
    return record


class MutationFence:
    """Concrete authority.lock seam for a future barrier-aware writer."""

    def __init__(
        self,
        authority: Path,
        marker: Path,
        lifecycle: Path,
        authority_lock: Path,
        control_store: Path | None = None,
        control_binding: Path | None = None,
        control_lock: Path | None = None,
    ):
        self.authority = authority
        self.marker = marker
        self.lifecycle = lifecycle
        self.authority_lock = authority_lock
        self.control_store = control_store
        self.control_binding = control_binding
        self.control_lock = control_lock
        self._scope_owner: int | None = None
        self._process_lock = threading.Lock()
        self._bound_session_identity: tuple[object, ...] | None = None

    def _verify(self) -> dict[str, object]:
        record = _read_json(self.marker, "authority fence marker")
        project_id = self._verify_marker(record)
        if asdict(_existing(self.authority, "authority database")) != record.get("authority"):
            raise MutationFenceError("authority database identity changed")
        if asdict(_existing(self.authority_lock, "authority.lock")) != record.get("authority_lock"):
            raise MutationFenceError("authority.lock identity changed")
        life = _read_json(self.lifecycle, "authority lifecycle")
        if life.get("record_digest") != _digest(
            {key: value for key, value in life.items() if key != "record_digest"}
        ):
            raise MutationFenceError("authority lifecycle digest is invalid")
        if life.get("authority_digest") != record["identity_digest"]:
            raise MutationFenceError("authority lifecycle binding is invalid")
        if life.get("state") not in LIFECYCLE_STATES:
            raise MutationFenceError("authority lifecycle state is invalid")
        if any((self.control_store, self.control_binding, self.control_lock)):
            self._verify_control_binding(project_id)
        return record

    def verify_binding(self) -> None:
        """Public read-only binding check for future caller-owned adapters."""
        self._verify()

    def bind_session_identity(self, identity: object) -> None:
        """Bind this long-lived fence to one trusted admitted session."""
        from tools.upgrade_identity import BarrierSessionIdentity

        if not isinstance(identity, BarrierSessionIdentity):
            raise MutationFenceError("barrier session identity is required")
        bound = (
            identity.project_id,
            identity.attempt_id,
            identity.state_revision,
            identity.authority_revision_at_acquire,
            identity.durable_barrier_id,
            identity.fencing_token,
            identity.fencing_owner,
            identity.identity_digest,
        )
        if self._bound_session_identity is not None and self._bound_session_identity != bound:
            raise MutationFenceError("barrier session identity already bound")
        self._bound_session_identity = bound

    def _verify_marker(self, record: dict[str, object]) -> str:
        if record.get("identity_digest") != _digest(
            {key: value for key, value in record.items() if key != "identity_digest"}
        ):
            raise MutationFenceError("authority fence marker digest is invalid")
        if record.get("schema_version") != SCHEMA_VERSION:
            raise MutationFenceError("authority fence schema is unsupported")
        project_id = record.get("project_id")
        if not isinstance(project_id, str) or _PROJECT_ID.fullmatch(project_id) is None:
            raise MutationFenceError("project identifier is not canonical and opaque")
        return project_id

    def _verify_control_binding(self, project_id: str) -> None:
        store = self.control_store
        binding_path = self.control_binding
        lock = self.control_lock
        if not all((store, binding_path, lock)):
            raise MutationFenceError("control binding prerequisites are incomplete")
        if store is None or binding_path is None or lock is None:
            raise MutationFenceError("control binding prerequisites are incomplete")
        binding = _read_json(binding_path, "control binding")
        if binding.get("identity_digest") != _digest(
            {key: value for key, value in binding.items() if key != "identity_digest"}
        ):
            raise MutationFenceError("control binding digest is invalid")
        if binding.get("project_id") != project_id:
            raise MutationFenceError("control binding project identity changed")
        if asdict(_existing(store, "control store")) != binding.get("control_store"):
            raise MutationFenceError("control store identity changed")
        if asdict(_existing(lock, "control.lock")) != binding.get("control_lock"):
            raise MutationFenceError("control.lock identity changed")

    @contextmanager
    def control_locked(self) -> Iterator[None]:
        """Hold the separately provisioned control lock."""
        self._verify()
        lock = self.control_lock
        binding_path = self.control_binding
        if lock is None or binding_path is None:
            raise MutationFenceError("control binding prerequisites are incomplete")
        binding = _read_json(binding_path, "control binding")
        parent_fd, _ = _parent(lock)
        descriptor = -1
        try:
            descriptor = os.open(lock.name, os.O_RDWR | os.O_NOFOLLOW, dir_fd=parent_fd)
            if asdict(_identity(os.fstat(descriptor), os.fstat(parent_fd))) != binding.get(
                "control_lock"
            ):
                raise MutationFenceError("control.lock identity changed")
            _acquire_file_lock(descriptor, "control.lock")
            self._verify()
            yield
        finally:
            if descriptor >= 0:
                fcntl.flock(descriptor, fcntl.LOCK_UN)
                os.close(descriptor)
            os.close(parent_fd)

    @contextmanager
    def mutation_scope(
        self,
        common_lock: Callable[[], AbstractContextManager[object]],
    ) -> Iterator[None]:
        """Acquire common -> control -> authority and admit only released."""
        if self._scope_owner == threading.get_ident():
            raise MutationFenceError("mutation fence scope is non-reentrant")
        if not self._process_lock.acquire(blocking=False):
            raise MutationFenceError("mutation fence scope is busy")
        self._scope_owner = threading.get_ident()
        try:
            with common_lock(), self.control_locked(), self.locked():
                status = self._read_barrier_status()
                if status != "released":
                    raise MutationFenceError(
                        f"authority mutation rejected while barrier is {status}"
                    )
                yield
        finally:
            self._scope_owner = None
            self._process_lock.release()

    def _read_barrier_status(self) -> str:  # noqa: C901
        if self.control_store is None or self.control_binding is None:
            raise MutationFenceError("control binding prerequisites are incomplete")
        project_id = self._verify_marker(_read_json(self.marker, "authority fence marker"))
        (
            binding_parent_fd,
            binding_descriptor,
            binding_parent,
            binding_before,
            binding,
            binding_bytes,
        ) = _open_binding_descriptor(self.control_binding, project_id)
        expected_identity = binding.get("control_store")
        parent_fd, parent = _parent_after_binding(
            self.control_store, binding_descriptor, binding_parent_fd
        )
        descriptor = -1
        connection: sqlite3.Connection | None = None
        try:
            descriptor = os.open(
                self.control_store.name, os.O_RDONLY | os.O_NOFOLLOW, dir_fd=parent_fd
            )
            status = os.fstat(descriptor)
            if asdict(_identity(status, parent)) != expected_identity:
                raise MutationFenceError("control store identity changed")
            # The /proc descriptor URI contains no caller-controlled pathname,
            # so URI metacharacters cannot redirect the SQLite open.
            connection = sqlite3.connect(
                f"file:/proc/self/fd/{descriptor}?mode=ro", uri=True, timeout=10
            )
            from tools.rollback_control_store import (
                ControlStoreError,
                SQLiteBarrierSessionStore,
            )

            try:
                observed = SQLiteBarrierSessionStore.observe_connection(connection, project_id)
            except ControlStoreError as error:
                raise MutationFenceError("durable control barrier state is invalid") from error
            identity = observed.identity if observed is not None else None
            if identity is not None:
                current_identity = (
                    identity.project_id,
                    identity.attempt_id,
                    identity.state_revision,
                    identity.authority_revision_at_acquire,
                    identity.durable_barrier_id,
                    identity.fencing_token,
                    identity.fencing_owner,
                    identity.identity_digest,
                )
                if self._bound_session_identity is None:
                    self._bound_session_identity = current_identity
                elif self._bound_session_identity != current_identity:
                    raise MutationFenceError("barrier session identity changed")
            current = os.fstat(descriptor)
            if _identity(current, os.fstat(parent_fd)) != _identity(status, parent):
                raise MutationFenceError("control store identity changed")
            _verify_binding_unchanged(
                self.control_binding,
                binding_parent_fd,
                binding_parent,
                binding_descriptor,
                binding_before,
                binding_bytes,
            )
        except (sqlite3.Error, OSError) as error:
            raise MutationFenceError("durable control barrier is unreadable") from error
        finally:
            if connection is not None:
                connection.close()
            if descriptor >= 0:
                os.close(descriptor)
            os.close(parent_fd)
            os.close(binding_descriptor)
            os.close(binding_parent_fd)
        if observed is None:
            raise MutationFenceError("durable control barrier is missing or ambiguous")
        return observed.status

    @contextmanager
    def locked(self) -> Iterator[None]:
        """Hold authority.lock after a complete identity/lifecycle reread."""
        self._verify()
        parent_fd, _ = _parent(self.authority_lock)
        descriptor = -1
        try:
            descriptor = os.open(
                self.authority_lock.name, os.O_RDWR | os.O_NOFOLLOW, dir_fd=parent_fd
            )
            status = os.fstat(descriptor)
            parent_status = os.fstat(parent_fd)
            actual = _identity(status, parent_status)
            marker = _read_json(self.marker, "authority fence marker")
            if asdict(actual) != marker.get("authority_lock"):
                raise MutationFenceError("authority.lock identity changed")
            _acquire_file_lock(descriptor, "authority.lock")
            self._verify()
            yield
        except OSError as error:
            if error.errno in {errno.EACCES, errno.EAGAIN}:
                raise MutationFenceError("authority.lock acquisition failed") from error
            raise
        finally:
            try:
                if descriptor >= 0:
                    fcntl.flock(descriptor, fcntl.LOCK_UN)
            finally:
                if descriptor >= 0:
                    os.close(descriptor)
                os.close(parent_fd)
