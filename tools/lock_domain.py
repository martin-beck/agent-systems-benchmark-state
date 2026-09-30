# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Pure lock-domain identity contract for the future v10 caller seam."""

from __future__ import annotations

import os
import stat
from dataclasses import dataclass
from pathlib import Path

from tools.admission_lease import AdmissionLease
from tools.handoffctl import CoordinatorLockGuard
from tools.mutation_fence import MutationFence, MutationFenceError
from tools.rollback_control_store import (
    BarrierSessionState,
    SQLiteBarrierSessionStore,
)
from tools.upgrade_identity import (
    BarrierSessionIdentity,
    UpgradeIdentityError,
    validate_barrier_session_identity,
)


class LockDomainError(RuntimeError):
    """The common/control/authority lock domain is not proven stable."""


@dataclass(frozen=True, slots=True)
class DescriptorIdentity:
    """The descriptor and parent identity needed for replacement detection."""

    device: int
    inode: int
    parent_device: int
    parent_inode: int
    mode: int
    owner: int
    links: int


def _identity(path: Path) -> DescriptorIdentity:
    if not path.is_absolute() or path.absolute() != path.resolve():
        raise LockDomainError(f"lock-domain path is not canonical: {path}")
    parent_fd = -1
    descriptor = -1
    try:
        parent_fd = os.open(path.parent, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
        parent_status = os.fstat(parent_fd)
        if parent_status.st_uid != os.geteuid() or stat.S_IMODE(parent_status.st_mode) != 0o700:
            raise LockDomainError(f"lock-domain parent is not owner-only: {path.parent}")
        descriptor = os.open(path.name, os.O_RDONLY | os.O_NOFOLLOW, dir_fd=parent_fd)
        status = os.fstat(descriptor)
        if (
            not stat.S_ISREG(status.st_mode)
            or status.st_uid != os.geteuid()
            or status.st_nlink != 1
            or stat.S_IMODE(status.st_mode) != 0o600
        ):
            raise LockDomainError(f"lock-domain descriptor is unsafe: {path}")
        return DescriptorIdentity(
            status.st_dev,
            status.st_ino,
            parent_status.st_dev,
            parent_status.st_ino,
            stat.S_IMODE(status.st_mode),
            status.st_uid,
            status.st_nlink,
        )
    except LockDomainError:
        raise
    except OSError as error:
        raise LockDomainError(f"lock-domain descriptor is unavailable: {path}") from error
    finally:
        if descriptor >= 0:
            os.close(descriptor)
        if parent_fd >= 0:
            os.close(parent_fd)


@dataclass(frozen=True, slots=True)
class LockDomainIdentity:
    """Immutable identity snapshot; capturing it acquires no locks."""

    project_id: str
    common_lock: Path
    control_store: Path
    control_lock: Path
    authority: Path
    authority_lock: Path
    common_identity: DescriptorIdentity
    control_store_identity: DescriptorIdentity
    control_lock_identity: DescriptorIdentity
    authority_identity: DescriptorIdentity
    authority_lock_identity: DescriptorIdentity

    def assert_current(
        self,
        common_guard: CoordinatorLockGuard,
        session_store: SQLiteBarrierSessionStore,
        authority_fence: MutationFence,
    ) -> None:
        """Reject any path or descriptor replacement since capture."""
        current = LockDomainContract.capture(common_guard, session_store, authority_fence)
        self.assert_descriptor_binding(current)

    def assert_descriptor_binding(self, current: object) -> None:
        """Require a freshly captured, typed identity to match exactly."""
        if not isinstance(current, LockDomainIdentity):
            raise LockDomainError("lock-domain identity is required")
        if current != self:
            raise LockDomainError("lock-domain identity changed")

    def assert_session_binding(
        self,
        session_state: BarrierSessionState,
        lease: AdmissionLease,
        *,
        session_revision: int | None = None,
        allowed_statuses: tuple[str, ...] = ("held",),
    ) -> None:
        """Require durable session identity to match caller lease evidence."""
        if not isinstance(session_state, BarrierSessionState):
            raise LockDomainError("durable barrier session is required")
        if not isinstance(lease, AdmissionLease):
            raise LockDomainError("admission lease is required")
        if session_state.status not in allowed_statuses:
            message = (
                "durable barrier session is not held"
                if allowed_statuses == ("held",)
                else "durable barrier session is not in an admissible status"
            )
            raise LockDomainError(message)
        identity = session_state.identity
        if not isinstance(identity, BarrierSessionIdentity):
            raise LockDomainError("durable barrier session identity is required")
        try:
            validate_barrier_session_identity(identity.as_record())
        except UpgradeIdentityError as error:
            raise LockDomainError("durable barrier session identity is invalid") from error
        fields = (
            (identity.project_id, lease.project_id),
            (identity.authority_revision_at_acquire, lease.authority_revision),
            (identity.fencing_token, lease.fencing_token),
            (identity.fencing_owner, lease.fencing_owner),
            (identity.durable_barrier_id, lease.durable_barrier_id),
            (identity.project_id, self.project_id),
        )
        if any(left != right for left, right in fields):
            raise LockDomainError("durable session and lease identity do not match")
        if identity.state_revision != lease.revision:
            raise LockDomainError("identity revision and lease do not match")
        expected_session_revision = lease.revision if session_revision is None else session_revision
        if session_state.revision != expected_session_revision:
            raise LockDomainError("durable session and lease revision do not match")


class LockDomainContract:
    """Capture a matched, descriptor-safe lock domain without mutating state."""

    @staticmethod
    def _validate_paths(
        common_guard: CoordinatorLockGuard,
        session_store: SQLiteBarrierSessionStore,
        authority_fence: MutationFence,
    ) -> tuple[Path, Path, Path, Path, Path]:
        control_store = session_store.control_store_path
        control_lock = session_store.control_lock_path
        fence_control = authority_fence.control_store
        fence_lock = authority_fence.control_lock
        authority = session_store.authority_path
        if fence_control is None or fence_lock is None or authority is None:
            raise LockDomainError("authority fence binding is incomplete")
        paths = (
            common_guard.path,
            control_store,
            control_lock,
            authority,
            authority_fence.authority_lock,
        )
        resolved = tuple(path.resolve() for path in paths)
        if any(path.absolute() != path.resolve() for path in paths):
            raise LockDomainError("lock-domain paths must be canonical")
        if len(set(resolved)) != len(resolved):
            raise LockDomainError("lock-domain paths are duplicated")
        if fence_control.resolve() != control_store.resolve():
            raise LockDomainError("control-store path identity is split")
        if fence_lock.resolve() != control_lock.resolve():
            raise LockDomainError("control-lock path identity is split")
        if authority_fence.authority.resolve() != authority.resolve():
            raise LockDomainError("authority path identity is split")
        return paths

    @staticmethod
    def capture(
        common_guard: CoordinatorLockGuard,
        session_store: SQLiteBarrierSessionStore,
        authority_fence: MutationFence,
    ) -> LockDomainIdentity:
        if not isinstance(common_guard, CoordinatorLockGuard):
            raise LockDomainError("common lock guard is required")
        if not isinstance(session_store, SQLiteBarrierSessionStore):
            raise LockDomainError("v10 session store is required")
        if not isinstance(authority_fence, MutationFence):
            raise LockDomainError("authority fence is required")
        try:
            common_guard.assert_owned()
        except Exception as error:
            raise LockDomainError("common lock ownership is not proven") from error
        paths = LockDomainContract._validate_paths(common_guard, session_store, authority_fence)
        _, control_store, control_lock, authority, authority_lock = paths
        try:
            authority_fence.verify_binding()
        except MutationFenceError as error:
            raise LockDomainError("authority fence binding is invalid") from error
        return LockDomainIdentity(
            project_id=session_store.project_id,
            common_lock=common_guard.path,
            control_store=control_store,
            control_lock=control_lock,
            authority=authority,
            authority_lock=authority_lock,
            common_identity=_identity(common_guard.path),
            control_store_identity=_identity(control_store),
            control_lock_identity=_identity(control_lock),
            authority_identity=_identity(authority),
            authority_lock_identity=_identity(authority_fence.authority_lock),
        )
