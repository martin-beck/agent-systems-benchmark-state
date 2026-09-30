# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Durable SQLite control-plane records for upgrade barriers.

The control store is deliberately separate from the coordinator authority.  It
is the source of truth for rollback-context rechecks; Git backends do not have
an implementation yet and must fail closed.
"""

from __future__ import annotations

import json
import os
import re
import sqlite3
import stat
import threading
import time
import uuid
from collections.abc import Callable, Iterator, Mapping
from contextlib import AbstractContextManager, contextmanager, nullcontext
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol, cast

from tools.handoffctl import (
    CoordinatorLockGuard,
    LockOwnershipError,
    coordinator_lock_path,
    locked,
)
from tools.rollback_evidence import _OBSERVATION_PROVIDER_TOKEN, BackupObservation
from tools.sqlite_wal_lifecycle import WALLifecycleError, WALLifecycleStore
from tools.upgrade_authority import inspect_sqlite_release_authority
from tools.upgrade_identity import (
    ENVELOPE_FIELDS,
    BarrierChildIdentity,
    BarrierSessionIdentity,
    UpgradeIdentityError,
    validate_envelope,
)

SCHEMA_VERSION = 3
SIDECAR_SUFFIXES = ("-wal", "-shm")
IDENTITY_FIELDS = ENVELOPE_FIELDS
STATUSES = {"held", "releasing", "released", "ambiguous"}
STATUS_TRANSITIONS = {
    "held": {"held", "releasing", "ambiguous"},
    "releasing": {"releasing", "released", "ambiguous"},
    "released": {"released"},
    "ambiguous": set(),
}
_COLUMNS = (*IDENTITY_FIELDS, "status", "revision")
_SELECT_COLUMNS = (
    "schema_version,backend,project_id,operation_id,state_revision,authority_revision,"
    "fencing_token,fencing_owner,durable_barrier_id,artifact_root,source,destination,manifest,selector_ref,"
    "barrier_identity_digest,target,envelope_digest,status,revision"
)
_SELECT_SQL = f"SELECT {_SELECT_COLUMNS} FROM barrier WHERE operation_id=?"  # noqa: S608
_INSERT_SQL = (
    "INSERT INTO barrier (schema_version,backend,project_id,operation_id,state_revision,"
    "authority_revision,fencing_token,fencing_owner,durable_barrier_id,artifact_root,source,"
    "destination,manifest,selector_ref,barrier_identity_digest,target,envelope_digest,status,"
    "revision) "
    "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
)
_UPDATE_FIELDS = tuple(field for field in _COLUMNS if field != "operation_id")
_UPDATE_SQL = (
    "UPDATE barrier SET schema_version=?,backend=?,project_id=?,state_revision=?,"
    "authority_revision=?,fencing_token=?,fencing_owner=?,durable_barrier_id=?,artifact_root=?,"
    "source=?,destination=?,manifest=?,selector_ref=?,barrier_identity_digest=?,target=?,envelope_digest=?,"
    "status=?,revision=? "
    "WHERE operation_id=? AND revision=?"
)
_RELEASE_EVIDENCE_FIELDS = {
    "restored_verified",
    "runtime_validated",
    "backend_roundtrip_valid",
    "backend",
    "fencing_token",
}
_REOPEN_EVIDENCE_FIELDS = {
    "operation_id",
    "target",
    "barrier_identity_digest",
    "validated",
}
_REOPEN_RUNTIME_EVIDENCE_FIELDS = {
    "authority_revision",
    "backend",
    "backend_roundtrip",
    "foreign_key_violations",
    "fencing_token",
    "integrity_check",
    "project_id",
    "target",
    "verified",
}
_CAUSE_CODE = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,127}")


@dataclass(frozen=True)
class _ReleaseAuthorization:
    operation_id: str
    envelope_digest: str
    fencing_token: str
    revision: int


class ControlStoreError(RuntimeError):
    """Control-store data is unavailable or failed validation."""


class ControlStoreAmbiguousError(ControlStoreError):
    """A durable control-store boundary may have committed before failing."""


class RecoveryRejectedError(ControlStoreError):
    """Recovery admission was rejected without changing durable state."""


class UpgradeAdapter(Protocol):
    """Minimal engine adapter surface wrapped by the control store."""

    def snapshot(self, phase: str, context: Mapping[str, object]) -> Mapping[str, object]: ...

    def execute(self, phase: str, context: Mapping[str, object]) -> Mapping[str, object]: ...


@dataclass(frozen=True, slots=True)
class SQLiteAuthorityRuntimeState:
    """Facts produced by a fresh authority and runtime reread."""

    backend: str
    project_id: str
    authority_revision: str
    fencing_token: str
    target: str
    integrity_check: str
    foreign_key_violations: int
    backend_roundtrip: str


@dataclass(frozen=True, slots=True)
class BarrierSessionState:
    """Typed, immutable view of a target-neutral barrier session.

    The existing SQLite rollback adapter remains v9 and fail-closed.  This
    value object is the v10 control-store seam: it makes the shared session
    identity and CAS state explicit without pretending that the durable
    adapter or SQLite mutation fencing is complete.
    """

    identity: BarrierSessionIdentity
    status: str
    revision: int
    forward_child: BarrierChildIdentity | None = None
    rollback_child: BarrierChildIdentity | None = None
    reopen_target: str | None = None

    def __post_init__(self) -> None:
        if self.status not in {"held", "releasing", "released", "ambiguous"}:
            raise ControlStoreError("barrier session status is invalid")
        if type(self.revision) is not int or self.revision < 1:
            raise ControlStoreError("barrier session revision is invalid")
        if self.reopen_target not in {None, "new", "rollback"}:
            raise ControlStoreError("barrier reopen target is invalid")
        if self.status == "held" and self.reopen_target is not None:
            raise ControlStoreError("held barrier session cannot have a reopen target")
        for child in (self.forward_child, self.rollback_child):
            if child is not None:
                child.validate_for(self.identity)
        if (
            self.forward_child is not None
            and self.rollback_child is not None
            and self.forward_child.operation_id == self.rollback_child.operation_id
        ):
            raise ControlStoreError("barrier child operation identities must be distinct")


@dataclass(frozen=True, slots=True)
class AuthorityEffectIntent:
    """Durable identity of an authority effect whose reply is not yet known."""

    intent_id: str
    operation_id: str
    backend: str
    target: str
    attempt_id: str
    identity_digest: str
    fencing_token: str
    session_revision: int
    artifact_identity: str | None = None
    manifest_identity: str | None = None
    selector_identity: str | None = None
    runtime_identity: str | None = None

    def __post_init__(self) -> None:
        if not all(
            isinstance(value, str) and value
            for value in (
                self.intent_id,
                self.operation_id,
                self.backend,
                self.target,
                self.attempt_id,
                self.identity_digest,
                self.fencing_token,
            )
        ):
            raise ControlStoreError("authority effect intent identity is invalid")
        if self.backend not in {"git", "sqlite"} or self.target not in {"new", "rollback"}:
            raise ControlStoreError("authority effect intent backend or target is invalid")
        if type(self.session_revision) is not int or self.session_revision < 1:
            raise ControlStoreError("authority effect intent session revision is invalid")
        admission_identities = (
            self.artifact_identity,
            self.manifest_identity,
            self.selector_identity,
            self.runtime_identity,
        )
        if any(
            value is not None and (not isinstance(value, str) or not value)
            for value in admission_identities
        ):
            raise ControlStoreError("authority effect admission identity is invalid")
        if any(value is None for value in admission_identities) and any(
            value is not None for value in admission_identities
        ):
            raise ControlStoreError("authority effect admission identity is incomplete")


def _validate_authority_effect_receipt(
    intent: AuthorityEffectIntent, receipt: object | None
) -> None:
    """Require a committed receipt to match every persisted admission field."""

    def receipt_field(name: str) -> object:
        if isinstance(receipt, Mapping):
            return receipt.get(name)
        return getattr(receipt, name, None)

    expected = {
        "backend": intent.backend,
        "target": intent.target,
        "operation_id": intent.operation_id,
        "state_revision": intent.session_revision,
        "artifact_identity": intent.artifact_identity,
        "manifest_identity": intent.manifest_identity,
        "selector_identity": intent.selector_identity,
        "runtime_identity": intent.runtime_identity,
        "fencing_token": intent.fencing_token,
        "mutates_authority": True,
    }
    if any(receipt_field(name) != value for name, value in expected.items()):
        raise ControlStoreError("authority effect receipt identity mismatch")


class BarrierSessionContract:
    """Small pure CAS contract used to gate a future durable adapter.

    This class intentionally has no filesystem or SQLite side effects.  It is
    suitable for exact transition tests while the production adapter remains
    disabled until AR-0012 supplies authority fencing and crash evidence.
    """

    def __init__(self, identity: BarrierSessionIdentity) -> None:
        self._state = BarrierSessionState(identity, "held", 1)

    @property
    def state(self) -> BarrierSessionState:
        return self._state

    def recheck_held(self, expected_revision: int) -> BarrierSessionState:
        self._expect(expected_revision, {"held"})
        return self._state

    def bind_child(
        self, expected_revision: int, child: BarrierChildIdentity
    ) -> BarrierSessionState:
        self._expect(expected_revision, {"held"})
        child.validate_for(self._state.identity)
        if child.target == "new":
            if self._state.forward_child is not None:
                raise ControlStoreError("forward barrier child is already bound")
            updated = BarrierSessionState(
                self._state.identity,
                self._state.status,
                self._state.revision + 1,
                child,
                self._state.rollback_child,
                self._state.reopen_target,
            )
        else:
            if self._state.forward_child is None:
                raise ControlStoreError("rollback child requires a bound forward child")
            if self._state.rollback_child is not None:
                raise ControlStoreError("rollback barrier child is already bound")
            updated = BarrierSessionState(
                self._state.identity,
                self._state.status,
                self._state.revision + 1,
                self._state.forward_child,
                child,
                self._state.reopen_target,
            )
        self._state = updated
        return updated

    def begin_reopen(
        self,
        expected_revision: int,
        child_target: str,
        verified_child_evidence: Mapping[str, object] | None = None,
    ) -> BarrierSessionState:
        self._expect(expected_revision, {"held"})
        if child_target not in {"new", "rollback"}:
            raise ControlStoreError("reopen child target is invalid")
        child = (
            self._state.rollback_child if child_target == "rollback" else self._state.forward_child
        )
        if child is None:
            raise ControlStoreError("reopen child is not bound")
        if verified_child_evidence is None:
            raise ControlStoreError("verified child evidence is required to begin reopen")
        if (
            set(verified_child_evidence) != _REOPEN_EVIDENCE_FIELDS
            or verified_child_evidence.get("operation_id") != child.operation_id
            or verified_child_evidence.get("target") != child.target
            or verified_child_evidence.get("barrier_identity_digest")
            != self._state.identity.identity_digest
            or verified_child_evidence.get("validated") is not True
        ):
            raise ControlStoreError("verified child evidence identity is invalid")
        self._state = BarrierSessionState(
            self._state.identity,
            "releasing",
            self._state.revision + 1,
            self._state.forward_child,
            self._state.rollback_child,
            child_target,
        )
        return self._state

    def complete_reopen(
        self,
        expected_revision: int,
        fresh_runtime_evidence: Mapping[str, object] | None = None,
    ) -> BarrierSessionState:
        self._expect(expected_revision, {"releasing"})
        if not isinstance(fresh_runtime_evidence, Mapping):
            raise ControlStoreError("fresh runtime evidence is required to release barrier")
        target = fresh_runtime_evidence.get("target")
        if target != self._state.reopen_target:
            raise ControlStoreError("fresh runtime evidence target does not match reopen target")
        child = self._state.rollback_child if target == "rollback" else self._state.forward_child
        if child is None or (
            set(fresh_runtime_evidence) != _REOPEN_RUNTIME_EVIDENCE_FIELDS
            or fresh_runtime_evidence.get("authority_revision")
            != self._state.identity.authority_revision_at_acquire
            or fresh_runtime_evidence.get("backend") != "sqlite"
            or fresh_runtime_evidence.get("backend_roundtrip") != "sqlite"
            or fresh_runtime_evidence.get("foreign_key_violations") != 0
            or fresh_runtime_evidence.get("fencing_token") != self._state.identity.fencing_token
            or fresh_runtime_evidence.get("integrity_check") != "ok"
            or fresh_runtime_evidence.get("project_id") != self._state.identity.project_id
            or fresh_runtime_evidence.get("target") != child.target
            or fresh_runtime_evidence.get("verified") is not True
        ):
            raise ControlStoreError("fresh runtime evidence identity is invalid")
        self._state = BarrierSessionState(
            self._state.identity,
            "released",
            self._state.revision + 1,
            self._state.forward_child,
            self._state.rollback_child,
            self._state.reopen_target,
        )
        return self._state

    def mark_ambiguous(self, expected_revision: int, cause_code: str) -> BarrierSessionState:
        self._expect(expected_revision, {"held", "releasing"})
        if _CAUSE_CODE.fullmatch(cause_code) is None:
            raise ControlStoreError("ambiguous barrier cause code is invalid")
        self._state = BarrierSessionState(
            self._state.identity,
            "ambiguous",
            self._state.revision + 1,
            self._state.forward_child,
            self._state.rollback_child,
            self._state.reopen_target,
        )
        return self._state

    def _expect(self, expected_revision: int, statuses: set[str]) -> None:
        if type(expected_revision) is not int or expected_revision != self._state.revision:
            raise ControlStoreError("barrier session revision conflict")
        if self._state.status not in statuses:
            raise ControlStoreError("barrier session transition is not permitted")


class AuthorityRuntimeRereader(Protocol):
    """Trusted boundary that rereads authority and runtime instead of echoing claims."""

    def reread_rollback(
        self, context: Mapping[str, object], result: Mapping[str, object]
    ) -> SQLiteAuthorityRuntimeState: ...


class SQLiteAuthorityRuntimeRereader:
    """Release-specific rereader backed by the restored authority and selectors."""

    def __init__(
        self,
        authority_path: Path,
        project_binding_path: Path,
        backend_selector_path: Path,
        runtime_selector_path: Path,
        *,
        active_release: str,
        previous_release: str,
    ) -> None:
        if not active_release or not previous_release:
            raise ControlStoreError("release-specific runtime selector identity is required")
        self._authority_path = authority_path
        self._project_binding_path = project_binding_path
        self._backend_selector_path = backend_selector_path
        self._runtime_selector_path = runtime_selector_path
        self._active_release = active_release
        self._previous_release = previous_release

    def reread_rollback(
        self, context: Mapping[str, object], result: Mapping[str, object]
    ) -> SQLiteAuthorityRuntimeState:
        project_id = context.get("project_id")
        fencing_token = context.get("fencing_token")
        if (
            context.get("backend") != "sqlite"
            or context.get("target") != "rollback"
            or not isinstance(project_id, str)
            or not isinstance(fencing_token, str)
            or set(result) != _RELEASE_EVIDENCE_FIELDS
            or any(
                result.get(field) is not True
                for field in (
                    "restored_verified",
                    "runtime_validated",
                    "backend_roundtrip_valid",
                )
            )
            or result.get("backend") != "sqlite"
            or result.get("fencing_token") != fencing_token
        ):
            raise ControlStoreError("rollback reread inputs are not release-specific")
        snapshot = inspect_sqlite_release_authority(
            self._authority_path,
            self._project_binding_path,
            self._backend_selector_path,
            self._runtime_selector_path,
            project_id,
            self._active_release,
            self._previous_release,
        )
        return SQLiteAuthorityRuntimeState(
            backend="sqlite",
            project_id=snapshot.project_id,
            authority_revision=snapshot.authority_revision,
            fencing_token=fencing_token,
            target="rollback",
            integrity_check=snapshot.integrity_check,
            foreign_key_violations=snapshot.foreign_key_violations,
            backend_roundtrip="sqlite",
        )


class SQLiteControlStoreAdapter:
    """Bind an engine adapter's rollback authority to a durable SQLite store."""

    def __init__(
        self,
        delegate: UpgradeAdapter,
        store: SQLiteRollbackControlStore,
        authority_runtime: AuthorityRuntimeRereader | None = None,
    ) -> None:
        if authority_runtime is None:
            raise ControlStoreError("concrete SQLite authority/runtime rereader is required")
        self._delegate = delegate
        self._store = store
        self._authority_runtime = authority_runtime
        self._release_authorization: _ReleaseAuthorization | None = None
        self._observation_provider_token = _OBSERVATION_PROVIDER_TOKEN

    @property
    def observation_provider_token(self) -> object:
        return self._observation_provider_token

    def snapshot(self, phase: str, context: Mapping[str, object]) -> Mapping[str, object]:
        return self._delegate.snapshot(phase, context)

    def execute(self, phase: str, context: Mapping[str, object]) -> Mapping[str, object]:
        return self._delegate.execute(phase, context)

    def verify_rollback_context(self, context: Mapping[str, object]) -> dict[str, object] | None:
        if self._store.operation_owned_by_current_thread:
            return self._store._verify_rollback_context_locked(context)
        return self._store.verify_rollback_context(context)

    def verify_rollback_context_bound(
        self,
        context: Mapping[str, object],
        scope: object,
        *,
        lease: object,
        admission_recheck: object,
    ) -> Mapping[str, object]:
        """Forward bound authority reread while retaining the control-store binding."""
        verifier = getattr(self._delegate, "verify_rollback_context_bound", None)
        if not callable(verifier):
            raise ControlStoreError("bound SQLite authority rereader is unavailable")
        return cast(
            Mapping[str, object],
            verifier(context, scope, lease=lease, admission_recheck=admission_recheck),
        )

    def observe_backup_identity(
        self, backup: Path, manifest: Path, context: Mapping[str, object]
    ) -> BackupObservation:
        """Bind artifact evidence to a fresh durable control-store reread."""
        with self._store.operation_lock():
            durable = self._store._verify_rollback_context_locked(context)
            if not isinstance(durable, Mapping):
                raise ControlStoreError("backup observation requires a valid control-store reread")
            try:
                control_stat = self._store.control_store_path.stat()
            except OSError as error:
                raise ControlStoreError("control-store identity reread failed") from error
            identity = f"{control_stat.st_dev}:{control_stat.st_ino}"
            revision = durable.get("revision")
            if type(revision) is not int:
                raise ControlStoreError("control-store reread identity is invalid")
            return BackupObservation.from_artifacts(
                backup,
                manifest,
                control_store_identity=identity,
                control_store_revision=revision,
            )

    def begin_release_rollback_context(self, context: Mapping[str, object]) -> Mapping[str, object]:
        operation_id = str(context["operation_id"])
        if not self._store.operation_owned_by_current_thread:
            raise ControlStoreError("rollback release requires the outer operation lock")
        self._release_authorization = None
        return self._store._begin_release_locked(operation_id)

    def complete_release_rollback_context(
        self, context: Mapping[str, object]
    ) -> Mapping[str, object]:
        operation_id = str(context["operation_id"])
        if not self._store.operation_owned_by_current_thread:
            raise ControlStoreError("rollback release requires the outer operation lock")
        authorization = self._release_authorization
        if authorization is None:
            raise ControlStoreError("rollback release lacks authority revalidation")
        try:
            return self._store._complete_release_locked(operation_id, authorization)
        finally:
            self._release_authorization = None

    def revalidate_rollback(
        self, context: Mapping[str, object], result: Mapping[str, object]
    ) -> Mapping[str, object]:
        durable = (
            self._store._verify_rollback_context_locked(context)
            if self._store.operation_owned_by_current_thread
            else self._store.verify_rollback_context(context)
        )
        if durable is None or durable["status"] not in {"releasing", "released"}:
            raise ControlStoreError("rollback control record is not ready for reopen validation")
        try:
            reread = self._authority_runtime.reread_rollback(context, result)
        except Exception as error:
            raise ControlStoreError("authority/runtime rollback reread failed") from error
        if not isinstance(reread, SQLiteAuthorityRuntimeState) or (
            reread.backend != "sqlite"
            or reread.backend != context.get("backend")
            or reread.project_id != context.get("project_id")
            or reread.authority_revision != context.get("authority_revision")
            or reread.fencing_token != context.get("fencing_token")
            or reread.target != context.get("target")
            or reread.integrity_check != "ok"
            or type(reread.foreign_key_violations) is not int
            or reread.foreign_key_violations != 0
            or reread.backend_roundtrip != "sqlite"
        ):
            raise ControlStoreError("authority/runtime rollback reread is invalid")
        evidence = {
            "restored_verified": True,
            "runtime_validated": True,
            "backend_roundtrip_valid": True,
            "backend": reread.backend,
            "fencing_token": reread.fencing_token,
        }
        if durable["status"] == "releasing":
            if not self._store.operation_owned_by_current_thread:
                raise ControlStoreError("rollback revalidation requires the outer operation lock")
            self._release_authorization = self._store._authorize_release_locked(context, evidence)
        return dict(evidence)

    def operation_lock(self) -> AbstractContextManager[None]:
        return self._store.operation_lock()


def bind_control_store(
    backend: str,
    delegate: UpgradeAdapter,
    store: SQLiteRollbackControlStore | None,
    authority_runtime: AuthorityRuntimeRereader | None = None,
) -> SQLiteControlStoreAdapter:
    """Construct only a proven SQLite adapter; Git is explicitly fail-closed."""
    if backend != "sqlite" or store is None or store.authority_path is None:
        raise ControlStoreError(
            "durable rollback control store or authority binding is unavailable"
        )
    if authority_runtime is None:
        raise ControlStoreError("concrete SQLite authority/runtime rereader is required")
    return SQLiteControlStoreAdapter(delegate, store, authority_runtime)


def _validate(record: Mapping[str, object]) -> dict[str, object]:
    if set(record) != set(IDENTITY_FIELDS) | {"status", "revision"}:
        raise ControlStoreError("control record fields are invalid")
    if not isinstance(record["state_revision"], int) or isinstance(record["state_revision"], bool):
        raise ControlStoreError("control state revision is invalid")
    if (
        record["state_revision"] < 1
        or not isinstance(record["revision"], int)
        or isinstance(record["revision"], bool)
        or record["revision"] < 1
    ):
        raise ControlStoreError("control revision is invalid")
    try:
        validate_envelope({field: record[field] for field in IDENTITY_FIELDS})
    except UpgradeIdentityError as error:
        raise ControlStoreError("control envelope identity is invalid") from error
    if record["backend"] != "sqlite":
        raise ControlStoreError("control backend is invalid")
    if record["status"] not in STATUSES:
        raise ControlStoreError("control status is invalid")
    return dict(record)


def _validate_expected_revision(expected_revision: object) -> int:
    if type(expected_revision) is not int or expected_revision < 0:
        raise ControlStoreError("control expected revision is invalid")
    return expected_revision


class SQLiteRollbackControlStore:
    """WAL-backed control store with coordinator-common locking and CAS."""

    def __init__(self, path: Path, project_id: str, authority_path: Path | None = None) -> None:
        try:
            project = uuid.UUID(project_id)
        except ValueError as error:
            raise ControlStoreError("control project_id must be UUIDv4") from error
        if project.version != 4:
            raise ControlStoreError("control project_id must be UUIDv4")
        self.path = path.absolute()
        self.authority_path = authority_path.absolute() if authority_path is not None else None
        if self.authority_path == self.path:
            raise ControlStoreError("control store aliases authority")
        self._authority_identity = (
            self._existing_regular_identity(self.authority_path)
            if self.authority_path is not None
            else None
        )
        self._parent_identity, self._control_identity = self._prepare_regular_file(self.path)
        if self._authority_identity == self._control_identity:
            raise ControlStoreError("control store aliases authority")
        self._lock_path = self.path.parent / f".{self.path.name}.lock"
        lock_parent, self._lock_identity = self._prepare_regular_file(self._lock_path)
        if lock_parent != self._parent_identity:
            raise ControlStoreError("control store lock parent identity changed")
        self._lifecycle_path = self.path.parent / f".{self.path.name}.lifecycle.json"
        self._lifecycle = WALLifecycleStore(
            self._lifecycle_path,
            project_id,
            self._control_identity,
            self._authority_identity,
        )
        try:
            if not self._lifecycle_path.exists() and not self._lifecycle_path.is_symlink():
                sidecars_exist = any(
                    (self.path.parent / f"{self.path.name}{suffix}").exists()
                    or (self.path.parent / f"{self.path.name}{suffix}").is_symlink()
                    for suffix in SIDECAR_SUFFIXES
                )
                if self.path.stat().st_size == 0 and not sidecars_exist:
                    self._lifecycle.initialize()
            else:
                self._lifecycle.initialize()
        except WALLifecycleError as error:
            raise ControlStoreError(str(error)) from error
        self._lifecycle_observed = False
        self._operation_owner: int | None = None
        self.project_id = project_id

    @staticmethod
    def _file_identity(value: os.stat_result) -> tuple[int, int]:
        return value.st_dev, value.st_ino

    @classmethod
    def _open_parent(cls, path: Path) -> tuple[int, tuple[int, int]]:
        if not path.is_absolute() or path.name in {"", ".", ".."}:
            raise ControlStoreError("control store path is invalid")
        descriptor = -1
        try:
            descriptor = os.open("/", os.O_RDONLY | os.O_DIRECTORY)
            for component in path.parent.parts[1:]:
                child = os.open(
                    component,
                    os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW,
                    dir_fd=descriptor,
                )
                previous = descriptor
                descriptor = child
                os.close(previous)
            parent_status = os.fstat(descriptor)
            if parent_status.st_uid != os.geteuid() or stat.S_IMODE(parent_status.st_mode) != 0o700:
                os.close(descriptor)
                descriptor = -1
                raise ControlStoreError(
                    "control store requires an owner-only provisioned directory"
                )
        except OSError as error:
            if descriptor >= 0:
                os.close(descriptor)
            raise ControlStoreError("control store parent descriptor is unsafe") from error
        return descriptor, cls._file_identity(parent_status)

    @classmethod
    def _sidecar_identities(
        cls, parent: int, name: str, *, required: bool
    ) -> dict[str, tuple[int, int] | None]:
        identities: dict[str, tuple[int, int] | None] = {}
        for suffix in SIDECAR_SUFFIXES:
            descriptor = -1
            try:
                descriptor = os.open(name + suffix, os.O_RDWR | os.O_NOFOLLOW, dir_fd=parent)
                status = os.fstat(descriptor)
                if not stat.S_ISREG(status.st_mode) or status.st_nlink != 1:
                    raise ControlStoreError("control store sidecar is not private and regular")
                identities[suffix] = cls._file_identity(status)
            except FileNotFoundError:
                if required:
                    raise ControlStoreError("control store WAL sidecars are unavailable") from None
                identities[suffix] = None
            except OSError as error:
                raise ControlStoreError("control store sidecar descriptor is unsafe") from error
            finally:
                if descriptor >= 0:
                    os.close(descriptor)
        return identities

    @classmethod
    def _bind_sidecars(
        cls,
        parent: int,
        name: str,
        previous: Mapping[str, tuple[int, int] | None],
    ) -> dict[str, tuple[int, int] | None]:
        current = cls._sidecar_identities(parent, name, required=True)
        if any(previous[suffix] not in {None, current[suffix]} for suffix in SIDECAR_SUFFIXES):
            raise ControlStoreError("control store WAL sidecar identity changed")
        return current

    @classmethod
    def _prepare_regular_file(cls, path: Path) -> tuple[tuple[int, int], tuple[int, int]]:
        parent, parent_identity = cls._open_parent(path)
        created = False
        try:
            try:
                descriptor = os.open(path.name, os.O_RDWR | os.O_NOFOLLOW, dir_fd=parent)
            except FileNotFoundError:
                try:
                    descriptor = os.open(
                        path.name,
                        os.O_CREAT | os.O_EXCL | os.O_RDWR | os.O_NOFOLLOW,
                        0o600,
                        dir_fd=parent,
                    )
                    created = True
                except OSError as error:
                    raise ControlStoreError("control store creation is unsafe") from error
            except OSError as error:
                raise ControlStoreError("control store descriptor is unsafe") from error
            try:
                status = os.fstat(descriptor)
                if not stat.S_ISREG(status.st_mode):
                    raise ControlStoreError("control store is not a regular file")
                if created:
                    os.fsync(descriptor)
                    os.fsync(parent)
                return parent_identity, cls._file_identity(status)
            finally:
                os.close(descriptor)
        finally:
            os.close(parent)

    @classmethod
    def _existing_regular_identity(cls, path: Path) -> tuple[int, int]:
        parent, _ = cls._open_parent(path)
        try:
            try:
                descriptor = os.open(path.name, os.O_RDONLY | os.O_NOFOLLOW, dir_fd=parent)
            except OSError as error:
                raise ControlStoreError("authority descriptor is unsafe") from error
            try:
                status = os.fstat(descriptor)
                if not stat.S_ISREG(status.st_mode):
                    raise ControlStoreError("authority is not a regular file")
                return cls._file_identity(status)
            finally:
                os.close(descriptor)
        finally:
            os.close(parent)

    def _open_bound_file(
        self, path: Path, expected_parent: tuple[int, int], expected_file: tuple[int, int]
    ) -> tuple[int, int]:
        parent, parent_identity = self._open_parent(path)
        if parent_identity != expected_parent:
            os.close(parent)
            raise ControlStoreError("control store parent identity changed")
        try:
            descriptor = os.open(path.name, os.O_RDWR | os.O_NOFOLLOW, dir_fd=parent)
        except OSError as error:
            os.close(parent)
            raise ControlStoreError("control store descriptor is unsafe") from error
        try:
            status = os.fstat(descriptor)
        except OSError as error:
            os.close(descriptor)
            os.close(parent)
            raise ControlStoreError("control store descriptor is unreadable") from error
        if not stat.S_ISREG(status.st_mode) or self._file_identity(status) != expected_file:
            os.close(descriptor)
            os.close(parent)
            raise ControlStoreError("control store descriptor identity changed")
        return parent, descriptor

    def _recheck_authority(self) -> None:
        if self.authority_path is None or self._authority_identity is None:
            return
        current = self._existing_regular_identity(self.authority_path)
        if current != self._authority_identity or current == self._control_identity:
            raise ControlStoreError("authority descriptor identity changed")

    @contextmanager
    def _connection(self) -> Iterator[sqlite3.Connection]:  # noqa: C901
        self._recheck_authority()
        lifecycle_missing = not self._lifecycle_path.exists() or self._lifecycle_path.is_symlink()
        parent, descriptor = self._open_bound_file(
            self.path, self._parent_identity, self._control_identity
        )
        try:
            before_sidecars = self._sidecar_identities(parent, self.path.name, required=False)
        except Exception:
            os.close(descriptor)
            os.close(parent)
            raise
        bound_sidecars: dict[str, tuple[int, int] | None] | None = None
        try:
            if not lifecycle_missing and not self._lifecycle_observed:
                try:
                    self._lifecycle.validate()
                except WALLifecycleError as error:
                    message = str(error)
                    if message == "WAL lifecycle project binding changed":
                        message = "control store project binding mismatch"
                    raise ControlStoreError(message) from error
            connection = sqlite3.connect(
                f"file:/proc/self/fd/{descriptor}?mode=rw",
                isolation_level=None,
                timeout=10,
                uri=True,
            )
        except Exception:
            os.close(descriptor)
            os.close(parent)
            raise
        try:
            # Inspect legacy metadata before enabling WAL or issuing any DDL.
            # Historical rows cannot be assigned a selector identity safely.
            if type(connection) is sqlite3.Connection:
                existing_tables = {
                    row[0]
                    for row in connection.execute(
                        "SELECT name FROM sqlite_master WHERE type='table'"
                    ).fetchall()
                }
                if "control_meta" in existing_tables:
                    version_row = connection.execute(
                        "SELECT value FROM control_meta WHERE key='schema_version'"
                    ).fetchone()
                    if version_row is not None and version_row[0] != str(SCHEMA_VERSION):
                        raise ControlStoreError(
                            "control store schema version is legacy; explicit migration is required"
                        )
                if "barrier" in existing_tables:
                    existing_columns = {
                        row[1]
                        for row in connection.execute("PRAGMA table_info(barrier)").fetchall()
                    }
                    if "selector_ref" not in existing_columns:
                        raise ControlStoreError(
                            "control store schema is legacy; explicit selector "
                            "migration is required"
                        )
            if lifecycle_missing:
                raise ControlStoreError("control store WAL lifecycle record is unavailable")
            mode = str(connection.execute("PRAGMA journal_mode=WAL").fetchone()[0]).lower()
            if mode != "wal":
                raise ControlStoreError("control store WAL is unavailable")
            connection.execute("PRAGMA synchronous=FULL")
            if int(connection.execute("PRAGMA synchronous").fetchone()[0]) != 2:
                raise ControlStoreError("control store FULL durability is unavailable")
            connection.execute(
                "CREATE TABLE IF NOT EXISTS control_meta "
                "(key TEXT PRIMARY KEY, value TEXT NOT NULL)"
            )
            connection.execute(
                """CREATE TABLE IF NOT EXISTS barrier (
                    schema_version INTEGER NOT NULL,
                    backend TEXT NOT NULL,
                    project_id TEXT NOT NULL,
                    operation_id TEXT PRIMARY KEY,
                    state_revision INTEGER NOT NULL,
                    authority_revision TEXT NOT NULL,
                    fencing_token TEXT NOT NULL,
                    fencing_owner TEXT NOT NULL,
                    durable_barrier_id TEXT NOT NULL,
                    artifact_root TEXT NOT NULL,
                    source TEXT NOT NULL,
                    destination TEXT NOT NULL,
                    manifest TEXT NOT NULL,
                    selector_ref TEXT NOT NULL,
                    barrier_identity_digest TEXT NOT NULL,
                    target TEXT NOT NULL,
                    envelope_digest TEXT NOT NULL,
                    status TEXT NOT NULL,
                    revision INTEGER NOT NULL
                )"""
            )
            connection.execute(
                "CREATE UNIQUE INDEX IF NOT EXISTS one_active_barrier_per_project "
                "ON barrier(project_id) WHERE status IN ('held','releasing')"
            )
            connection.execute(
                "INSERT OR IGNORE INTO control_meta(key,value) VALUES ('schema_version',?)",
                (str(SCHEMA_VERSION),),
            )
            schema = connection.execute(
                "SELECT value FROM control_meta WHERE key='schema_version'"
            ).fetchone()
            if schema is None or schema[0] != str(SCHEMA_VERSION):
                raise ControlStoreError("control store schema version mismatch")
            value = connection.execute(
                "SELECT value FROM control_meta WHERE key='project_id'"
            ).fetchone()
            if value is None:
                connection.execute(
                    "INSERT INTO control_meta(key,value) VALUES ('project_id',?)",
                    (self.project_id,),
                )
            elif value[0] != self.project_id:
                raise ControlStoreError("control store project binding mismatch")
            bound_sidecars = self._bind_sidecars(parent, self.path.name, before_sidecars)
            if not self._lifecycle_observed:
                try:
                    self._lifecycle.mark_active(parent, self.path.name, allow_rebind=True)
                except WALLifecycleError as error:
                    raise ControlStoreError(str(error)) from error
                self._lifecycle_observed = True
            yield connection
        except Exception:
            raise
        finally:
            try:
                try:
                    if bound_sidecars is not None:
                        current_sidecars = self._sidecar_identities(
                            parent, self.path.name, required=True
                        )
                        if current_sidecars != bound_sidecars:
                            raise ControlStoreAmbiguousError(
                                "control store WAL sidecar identity changed"
                            )
                finally:
                    try:
                        connection.close()
                    except (OSError, sqlite3.Error) as error:
                        raise ControlStoreAmbiguousError(
                            "control store connection close outcome is ambiguous"
                        ) from error
                    except BaseException as error:
                        raise ControlStoreAmbiguousError(
                            "control store connection close outcome is ambiguous"
                        ) from error
                try:
                    reopened_parent, reopened = self._open_bound_file(
                        self.path, self._parent_identity, self._control_identity
                    )
                except ControlStoreError as error:
                    raise ControlStoreAmbiguousError(
                        "control store reopen identity became uncertain"
                    ) from error
                os.close(reopened)
                os.close(reopened_parent)
                try:
                    self._recheck_authority()
                except ControlStoreError as error:
                    raise ControlStoreAmbiguousError(
                        "control store authority identity became uncertain"
                    ) from error
            finally:
                os.close(descriptor)
                os.close(parent)

    @contextmanager
    def _control_lock(self) -> Iterator[None]:
        """Hold the store-specific lock after the coordinator-common lock."""
        parent, descriptor = self._open_bound_file(
            self._lock_path, self._parent_identity, self._lock_identity
        )
        try:
            import fcntl
        except ImportError as error:  # pragma: no cover - coordinator is POSIX-only
            os.close(descriptor)
            os.close(parent)
            raise ControlStoreError("control store locking is unavailable") from error
        try:
            deadline = time.monotonic() + 10.0
            while True:
                try:
                    fcntl.flock(descriptor, fcntl.LOCK_EX | fcntl.LOCK_NB)
                    break
                except BlockingIOError as error:
                    remaining = deadline - time.monotonic()
                    if remaining <= 0:
                        raise ControlStoreError(
                            "control store lock acquisition timed out"
                        ) from error
                    time.sleep(min(0.05, remaining))
            yield
        finally:
            try:
                fcntl.flock(descriptor, fcntl.LOCK_UN)
            finally:
                os.close(descriptor)
                os.close(parent)

    @contextmanager
    def operation_lock(self) -> Iterator[None]:
        """Hold common then control-store locks once for a complete operation."""
        if self._operation_owner == threading.get_ident():
            raise ControlStoreError("control store lock is non-reentrant")
        with locked(), self._control_lock():
            if self._operation_owner is not None:
                raise ControlStoreError("control store operation is already active")
            self._operation_owner = threading.get_ident()
            try:
                yield
            finally:
                self._operation_owner = None

    def checkpoint_wal(self) -> None:
        """Checkpoint and durably record the clean sidecar lifecycle state."""
        if self._operation_owner is not None:
            raise ControlStoreError("control store lock is non-reentrant")
        with self.operation_lock():
            try:
                self._lifecycle.validate()
            except WALLifecycleError as error:
                raise ControlStoreError(str(error)) from error
            with self._connection() as connection:
                result = connection.execute("PRAGMA wal_checkpoint(TRUNCATE)").fetchone()
                if result is None or tuple(result) != (0, 0, 0):
                    raise ControlStoreError("WAL checkpoint did not complete")
            parent, descriptor = self._open_bound_file(
                self.path, self._parent_identity, self._control_identity
            )
            try:
                lifecycle = self._lifecycle.validate()
                sidecars = self._sidecar_identities(parent, self.path.name, required=False)
                if all(identity is None for identity in sidecars.values()):
                    if lifecycle["state"] == "active":
                        self._lifecycle.mark_clean_checkpointed(parent, self.path.name)
                        self._lifecycle_observed = False
                    elif lifecycle["state"] == "absent":
                        self._lifecycle._publish(
                            self._lifecycle._record(
                                "clean_checkpointed",
                                1,
                                dict.fromkeys(SIDECAR_SUFFIXES),
                            )
                        )
                        self._lifecycle_observed = False
                else:
                    self._lifecycle.mark_active(parent, self.path.name, allow_rebind=True)
            except WALLifecycleError as error:
                raise ControlStoreError(str(error)) from error
            finally:
                os.close(descriptor)
                os.close(parent)

    def reconcile_wal_lifecycle(self) -> None:
        """Reconcile a durable lifecycle after an interrupted SQLite process."""
        if self._operation_owner is not None:
            raise ControlStoreError("control store lock is non-reentrant")
        with self.operation_lock():
            self._reconcile_wal_lifecycle_locked()

    def _reconcile_wal_lifecycle_locked(self) -> None:
        """Reconcile lifecycle evidence while the caller owns the operation lock."""
        self._recheck_authority()
        parent, descriptor = self._open_bound_file(
            self.path, self._parent_identity, self._control_identity
        )
        connection: sqlite3.Connection | None = None
        try:
            lifecycle = self._lifecycle.validate()
            sidecars = self._sidecar_identities(parent, self.path.name, required=False)
            if all(identity is None for identity in sidecars.values()) and lifecycle["state"] in {
                "absent",
                "clean_checkpointed",
            }:
                return
            connection = sqlite3.connect(
                f"file:/proc/self/fd/{descriptor}?mode=rw",
                isolation_level=None,
                timeout=10,
                uri=True,
            )
            mode = str(connection.execute("PRAGMA journal_mode").fetchone()[0]).lower()
            if mode != "wal":
                raise ControlStoreError("control store WAL is unavailable")
            integrity = connection.execute("PRAGMA integrity_check").fetchone()
            if integrity is None or integrity[0] != "ok":
                raise ControlStoreError("control store integrity check failed")
            connection.close()
            connection = None
            sidecars = self._sidecar_identities(parent, self.path.name, required=False)
            if all(identity is None for identity in sidecars.values()):
                if lifecycle["state"] == "active":
                    self._lifecycle.mark_clean_checkpointed(parent, self.path.name)
                    self._lifecycle_observed = False
            else:
                self._lifecycle.mark_active(parent, self.path.name, allow_rebind=True)
        except WALLifecycleError as error:
            raise ControlStoreError(str(error)) from error
        finally:
            if connection is not None:
                connection.close()
            os.close(descriptor)
            os.close(parent)

    @contextmanager
    def lock_owned_by_caller(self, common_guard: CoordinatorLockGuard) -> Iterator[None]:
        """Hold the control lock under a caller-owned common-lock capability."""
        if not isinstance(common_guard, CoordinatorLockGuard):
            raise LockOwnershipError("caller-owned coordinator lock guard is required")
        common_guard.assert_owned()
        if common_guard.path != coordinator_lock_path().resolve():
            raise ControlStoreError("coordinator lock guard path mismatch")
        if self._operation_owner == threading.get_ident():
            raise ControlStoreError("control store lock is non-reentrant")
        with self._control_lock():
            if self._operation_owner is not None:
                raise ControlStoreError("control store operation is already active")
            self._operation_owner = threading.get_ident()
            try:
                common_guard.assert_owned()
                yield
                common_guard.assert_owned()
            finally:
                self._operation_owner = None

    @property
    def operation_owned_by_current_thread(self) -> bool:
        return self._operation_owner == threading.get_ident()

    @property
    def control_store_path(self) -> Path:
        """Return the canonical control-store path for identity contracts."""
        return self.path

    @property
    def control_lock_path(self) -> Path:
        """Return the canonical control-lock path for identity contracts."""
        return self._lock_path

    def _require_operation_lock(self) -> None:
        if not self.operation_owned_by_current_thread:
            raise ControlStoreError("control store operation lock is required")

    def snapshot(self, operation_id: str) -> dict[str, object]:
        if self._operation_owner is not None:
            raise ControlStoreError("control store lock is non-reentrant")
        with self.operation_lock():
            return self._snapshot_locked(operation_id)

    def _snapshot_locked(self, operation_id: str) -> dict[str, object]:
        self._require_operation_lock()
        with self._connection() as connection:
            row = connection.execute(_SELECT_SQL, (operation_id,)).fetchone()
            if row is None:
                raise ControlStoreError("control barrier is missing")
            return _validate(dict(zip((*IDENTITY_FIELDS, "status", "revision"), row, strict=True)))

    def verify_rollback_context(self, context: Mapping[str, object]) -> dict[str, object] | None:
        """Re-read the durable control record and compare every bound identity."""
        if self._operation_owner is not None:
            raise ControlStoreError("control store lock is non-reentrant")
        with self.operation_lock():
            return self._verify_rollback_context_locked(context)

    def _verify_rollback_context_locked(
        self, context: Mapping[str, object]
    ) -> dict[str, object] | None:
        self._require_operation_lock()
        operation_id = context.get("operation_id")
        if not isinstance(operation_id, str):
            return None
        try:
            durable = self._snapshot_locked(operation_id)
            supplied = _validate(
                {
                    **{field: context.get(field) for field in IDENTITY_FIELDS},
                    "status": durable["status"],
                    "revision": durable["revision"],
                }
            )
        except (ControlStoreError, TypeError):
            return None
        return (
            durable
            if supplied == durable
            and supplied["target"] == "rollback"
            and durable["status"] in {"held", "releasing", "released"}
            else None
        )

    def cas(self, expected_revision: int, record: Mapping[str, object]) -> dict[str, object]:
        expected_revision = _validate_expected_revision(expected_revision)
        supplied = _validate(record)
        if supplied["status"] == "released":
            raise ControlStoreError("released status requires authority revalidation")
        if supplied["project_id"] != self.project_id:
            raise ControlStoreError("control project binding mismatch")
        if self._operation_owner is not None:
            raise ControlStoreError("control store lock is non-reentrant")
        with self.operation_lock():
            return self._cas_locked(expected_revision, supplied)

    def _cas_locked(self, expected_revision: int, supplied: dict[str, object]) -> dict[str, object]:
        expected_revision = _validate_expected_revision(expected_revision)
        self._require_operation_lock()
        with self._connection() as connection:
            return self._cas_connection(connection, expected_revision, supplied)

    def cas_locked(
        self,
        common_guard: CoordinatorLockGuard,
        expected_revision: int,
        record: Mapping[str, object],
    ) -> dict[str, object]:
        """CAS one barrier under a caller-owned common/control lock.

        The authority lock is supplied by the enclosing lock-domain adapter;
        this method only exposes the typed control-store operation.
        """
        if not isinstance(common_guard, CoordinatorLockGuard):
            raise LockOwnershipError("caller-owned coordinator lock guard is required")
        common_guard.assert_owned()
        if common_guard.path != coordinator_lock_path().resolve():
            raise ControlStoreError("coordinator lock guard path mismatch")
        supplied = _validate(record)
        if supplied["project_id"] != self.project_id:
            raise ControlStoreError("control project binding mismatch")
        self._require_operation_lock()
        result = self._cas_locked(expected_revision, supplied)
        common_guard.assert_owned()
        return result

    def begin_release(self, operation_id: str) -> dict[str, object]:
        """Commit the held-to-releasing transition without reopening authority."""
        if self._operation_owner is not None:
            raise ControlStoreError("control store lock is non-reentrant")
        with self.operation_lock():
            return self._begin_release_locked(operation_id)

    def _begin_release_locked(self, operation_id: str) -> dict[str, object]:
        self._require_operation_lock()
        current = self._snapshot_locked(operation_id)
        if current["status"] != "held":
            raise ControlStoreError("barrier is not held")
        return self._cas_locked(cast(int, current["revision"]), {**current, "status": "releasing"})

    def _authorize_release_locked(
        self, context: Mapping[str, object], evidence: Mapping[str, object]
    ) -> _ReleaseAuthorization:
        self._require_operation_lock()
        current = self._snapshot_locked(str(context.get("operation_id", "")))
        if current["status"] != "releasing" or any(
            current[field] != context.get(field) for field in IDENTITY_FIELDS
        ):
            raise ControlStoreError("release authorization identity changed")
        if (
            set(evidence) != _RELEASE_EVIDENCE_FIELDS
            or any(
                evidence.get(field) is not True
                for field in (
                    "restored_verified",
                    "runtime_validated",
                    "backend_roundtrip_valid",
                )
            )
            or evidence.get("backend") != current["backend"]
            or evidence.get("fencing_token") != current["fencing_token"]
        ):
            raise ControlStoreError("release authority evidence is invalid")
        return _ReleaseAuthorization(
            operation_id=str(current["operation_id"]),
            envelope_digest=str(current["envelope_digest"]),
            fencing_token=str(current["fencing_token"]),
            revision=cast(int, current["revision"]),
        )

    def _complete_release_locked(
        self, operation_id: str, authorization: _ReleaseAuthorization
    ) -> dict[str, object]:
        self._require_operation_lock()
        releasing = self._snapshot_locked(operation_id)
        if (
            releasing["status"] != "releasing"
            or authorization.operation_id != operation_id
            or authorization.envelope_digest != releasing["envelope_digest"]
            or authorization.fencing_token != releasing["fencing_token"]
            or authorization.revision != releasing["revision"]
        ):
            raise ControlStoreError("barrier release authorization is stale")
        return self._cas_locked(releasing["revision"], {**releasing, "status": "released"})

    def reconcile_release(self, operation_id: str) -> dict[str, object]:
        """Reject blind release; engine recovery must revalidate authority and journal."""
        raise ControlStoreError(
            f"release reconciliation for {operation_id!r} requires verified engine recovery"
        )

    def reconcile_ambiguous(
        self, operation_id: str, replacement: Mapping[str, object]
    ) -> dict[str, object]:
        """Start a new fenced operation only after explicit ambiguous recovery."""
        previous = self.snapshot(operation_id)
        candidate = self._validate_ambiguous_replacement(previous, operation_id, replacement)
        return self.cas(0, candidate)

    @staticmethod
    def _validate_ambiguous_replacement(
        previous: Mapping[str, object],
        operation_id: str,
        replacement: Mapping[str, object],
    ) -> dict[str, object]:
        if previous["status"] != "ambiguous":
            raise ControlStoreError("only ambiguous barriers require reconciliation")
        candidate = _validate(replacement)
        if candidate["operation_id"] == operation_id or candidate["status"] != "held":
            raise ControlStoreError("ambiguous reconciliation requires a new held operation")
        if candidate["project_id"] != previous["project_id"] or cast(
            int, candidate["state_revision"]
        ) <= cast(int, previous["state_revision"]):
            raise ControlStoreError("ambiguous reconciliation requires a newer project fence")
        if (
            candidate["durable_barrier_id"] == previous["durable_barrier_id"]
            or candidate["fencing_token"] == previous["fencing_token"]
        ):
            raise ControlStoreError("ambiguous reconciliation requires a distinct project fence")
        return candidate

    def reconcile_ambiguous_locked(
        self,
        _common_guard: CoordinatorLockGuard,
        operation_id: str,
        replacement: Mapping[str, object],
    ) -> dict[str, object]:
        """Reconcile one ambiguous barrier under caller-owned locks."""
        self._require_operation_lock()
        previous = self._snapshot_locked(operation_id)
        candidate = self._validate_ambiguous_replacement(previous, operation_id, replacement)
        return self.cas_locked(_common_guard, 0, candidate)

    def _cas_connection(  # noqa: C901
        self, connection: sqlite3.Connection, expected_revision: int, supplied: dict[str, object]
    ) -> dict[str, object]:
        expected_revision = _validate_expected_revision(expected_revision)
        connection.execute("BEGIN IMMEDIATE")
        current = connection.execute(_SELECT_SQL, (supplied["operation_id"],)).fetchone()
        if current is not None and current[-1] != expected_revision:
            connection.rollback()
            raise ControlStoreError("control barrier CAS conflict")
        if current is None and expected_revision != 0:
            connection.rollback()
            raise ControlStoreError("control barrier does not exist")
        supplied["revision"] = expected_revision + 1
        if current is None and supplied["status"] != "held":
            connection.rollback()
            raise ControlStoreError("new control barrier must start held")
        if current is None:
            latest = connection.execute(
                "SELECT MAX(state_revision) FROM barrier WHERE project_id=?",
                (supplied["project_id"],),
            ).fetchone()[0]
            if latest is not None and supplied["state_revision"] <= latest:
                connection.rollback()
                raise ControlStoreError("stale control state revision")
            active = connection.execute(
                "SELECT operation_id FROM barrier WHERE project_id=? "
                "AND status IN ('held','releasing') LIMIT 1",
                (supplied["project_id"],),
            ).fetchone()
            if active is not None:
                connection.rollback()
                raise ControlStoreError("project already has an active barrier")
        if current is not None:
            current_record = dict(
                zip((*IDENTITY_FIELDS, "status", "revision"), current, strict=True)
            )
            if any(current_record[field] != supplied[field] for field in IDENTITY_FIELDS):
                connection.rollback()
                raise ControlStoreError("control identity changed during CAS")
        if current is not None and supplied["status"] not in STATUS_TRANSITIONS[str(current[-2])]:
            connection.rollback()
            raise ControlStoreError("illegal control barrier transition")
        columns = (*IDENTITY_FIELDS, "status", "revision")
        values = tuple(supplied[field] for field in columns)
        if current is None:
            cursor = connection.execute(_INSERT_SQL, values)
            if cursor.rowcount != 1:
                connection.rollback()
                raise ControlStoreError("control barrier CAS insert lost its fence")
        else:
            cursor = connection.execute(
                _UPDATE_SQL,
                (
                    *(supplied[field] for field in columns if field != "operation_id"),
                    supplied["operation_id"],
                    expected_revision,
                ),
            )
            if cursor.rowcount != 1:
                connection.rollback()
                raise ControlStoreError("control barrier CAS update lost its fence")
        try:
            connection.commit()
        except Exception as error:
            # A commit exception does not establish whether SQLite reached the
            # durable boundary.  Never turn that uncertainty into a success or
            # blindly retry a transition.  Fence the record into the terminal
            # ambiguous state using a fresh transaction instead.
            raise ControlStoreError(
                "control barrier commit outcome is ambiguous; durable state must be rechecked"
            ) from self._mark_ambiguous_after_commit_failure(
                connection, supplied, expected_revision, error
            )
        return dict(supplied)

    @staticmethod
    def _mark_ambiguous_after_commit_failure(
        connection: sqlite3.Connection,
        supplied: Mapping[str, object],
        expected_revision: int,
        commit_error: Exception,
    ) -> Exception:
        """Attempt to durably fence an uncertain CAS outcome as ambiguous."""
        try:
            connection.rollback()
            connection.execute("BEGIN IMMEDIATE")
            current = connection.execute(_SELECT_SQL, (supplied["operation_id"],)).fetchone()
            if current is None:
                values = dict(supplied)
                values["status"] = "ambiguous"
                values["revision"] = expected_revision + 1
                connection.execute(
                    _INSERT_SQL,
                    tuple(values[field] for field in (*IDENTITY_FIELDS, "status", "revision")),
                )
            else:
                current_revision = int(current[-1])
                cursor = connection.execute(
                    "UPDATE barrier SET status='ambiguous',revision=? "
                    "WHERE operation_id=? AND revision=?",
                    (current_revision + 1, supplied["operation_id"], current_revision),
                )
                if cursor.rowcount != 1:
                    raise ControlStoreError("ambiguous barrier fencing lost its row fence")
            connection.commit()
        except Exception as recovery_error:
            raise ControlStoreError(
                "control barrier commit outcome is ambiguous and could not be durably fenced"
            ) from recovery_error
        return commit_error

    def with_barrier(
        self,
        expected_revision: int,
        record: Mapping[str, object],
        authority: Callable[[Mapping[str, object]], Mapping[str, object]],
    ) -> dict[str, object]:
        """Run one authority critical section while the coordinator lock is held.

        The initial ``held`` CAS is committed before the callback.  A callback
        failure therefore leaves a durable held barrier for explicit recovery.
        """
        supplied = _validate(record)
        if supplied["project_id"] != self.project_id:
            raise ControlStoreError("control project binding mismatch")
        if self._operation_owner is not None:
            raise ControlStoreError("control store lock is non-reentrant")
        with self.operation_lock(), self._connection() as connection:
            held = self._cas_connection(connection, expected_revision, supplied)
            result = dict(authority(dict(held)))
            return self._cas_connection(connection, cast(int, held["revision"]), _validate(result))

    def with_barrier_locked(
        self,
        common_guard: CoordinatorLockGuard,
        expected_revision: int,
        record: Mapping[str, object],
        authority: Callable[[Mapping[str, object]], Mapping[str, object]],
    ) -> dict[str, object]:
        """Run the barrier callback while caller-owned locks are held."""
        supplied = _validate(record)
        if supplied["project_id"] != self.project_id:
            raise ControlStoreError("control project binding mismatch")
        self._require_operation_lock()
        held = self.cas_locked(common_guard, expected_revision, supplied)
        result = dict(authority(dict(held)))
        return self.cas_locked(common_guard, cast(int, held["revision"]), _validate(result))


class SQLiteBarrierSessionStore:
    """Durable CAS adapter for the target-neutral v10 barrier session.

    This is intentionally only the control-plane slice.  It persists the
    immutable session identity and its two child bindings, but it does not
    open or mutate the coordinator authority.  The enclosing
    ``SQLiteRollbackControlStore`` supplies the existing lock order (the
    repository lock followed by the control-store lock); authority fencing
    will be added by the later mutation adapter before upgrade execution is
    enabled.

    A missing row is the only ``absent`` state.  Once a row exists every
    transition is a compare-and-swap and identity fields are immutable.  A
    failed or uncertain observation must therefore be recorded as
    ``ambiguous``; there is no recovery shortcut that silently clears it.
    """

    _TABLE = "barrier_session"
    _SELECT = (
        "SELECT schema_version,project_id,attempt_id,state_revision,"
        "authority_revision_at_acquire,durable_barrier_id,fencing_token,fencing_owner,"
        "identity_digest,status,revision,forward_child,rollback_child,reopen_target "
        "FROM barrier_session WHERE project_id=?"
    )
    _SELECT_LEGACY = (
        "SELECT schema_version,project_id,attempt_id,state_revision,"
        "authority_revision_at_acquire,durable_barrier_id,fencing_token,fencing_owner,"
        "identity_digest,status,revision,forward_child,rollback_child "
        "FROM barrier_session WHERE project_id=?"
    )

    def __init__(
        self,
        control: SQLiteRollbackControlStore,
        authority_revision_reader: Callable[[], str] | None = None,
    ) -> None:
        self._control = control
        self.project_id = control.project_id
        self._authority_revision_reader = authority_revision_reader

    @property
    def operation_owned_by_current_thread(self) -> bool:
        return self._control.operation_owned_by_current_thread

    @property
    def control_store_path(self) -> Path:
        """Return the underlying control-store path for identity contracts."""
        return self._control.control_store_path

    def reconcile_wal_lifecycle(self) -> None:
        """Reconcile interrupted control-store WAL/SHM state before recovery."""
        self._control.reconcile_wal_lifecycle()

    @property
    def control_lock_path(self) -> Path:
        """Return the underlying control-lock path for identity contracts."""
        return self._control.control_lock_path

    @property
    def authority_path(self) -> Path | None:
        """Return the descriptor-bound authority path, when configured."""
        return self._control.authority_path

    def operation_lock(self) -> AbstractContextManager[None]:
        """Acquire the common lock, then this control store's lock."""
        return self._control.operation_lock()

    def lock_owned_by_caller(
        self, common_guard: CoordinatorLockGuard
    ) -> AbstractContextManager[None]:
        """Hold the control lock under a caller-owned common-lock capability."""
        return self._control.lock_owned_by_caller(common_guard)

    def snapshot_owned_by_caller(self) -> BarrierSessionState:
        """Read the typed durable session while the caller-owned lock is held.

        The method never acquires a lock itself, so callers cannot accidentally
        use an unlocked or independently supplied revision as lifecycle evidence.
        """
        if not self.operation_owned_by_current_thread:
            raise ControlStoreError("caller-owned control lock is required")
        state = self._snapshot_locked()
        if state is None:
            raise ControlStoreError("durable barrier session is missing")
        return state

    def snapshot(self) -> BarrierSessionState | None:
        if self.operation_owned_by_current_thread:
            raise ControlStoreError("control store lock is non-reentrant")
        with self.operation_lock():
            return self._snapshot_locked()

    def _ensure_table(self, connection: sqlite3.Connection) -> None:
        connection.execute(
            """CREATE TABLE IF NOT EXISTS barrier_session (
                schema_version INTEGER NOT NULL,
                project_id TEXT PRIMARY KEY,
                attempt_id TEXT NOT NULL,
                state_revision INTEGER NOT NULL,
                authority_revision_at_acquire TEXT NOT NULL,
                durable_barrier_id TEXT NOT NULL,
                fencing_token TEXT NOT NULL,
                fencing_owner TEXT NOT NULL,
                identity_digest TEXT NOT NULL,
                status TEXT NOT NULL,
                revision INTEGER NOT NULL,
                forward_child TEXT,
                rollback_child TEXT,
                reopen_target TEXT
                )"""
        )
        pragma_cursor = connection.execute("PRAGMA table_info(barrier_session)")
        pragma_rows = pragma_cursor.fetchall() if hasattr(pragma_cursor, "fetchall") else []
        columns = {str(row[1]) for row in pragma_rows}
        if "reopen_target" not in columns:
            connection.execute("ALTER TABLE barrier_session ADD COLUMN reopen_target TEXT")
        # Released sessions are immutable audit records.  The current-row
        # table remains one row per project for cheap admission checks, but
        # a subsequent attempt must not overwrite the released session.
        connection.execute(
            """CREATE TABLE IF NOT EXISTS barrier_session_history (
                    project_id TEXT NOT NULL,
                    attempt_id TEXT NOT NULL,
                    revision INTEGER NOT NULL,
                    record_json TEXT NOT NULL,
                    PRIMARY KEY(project_id, attempt_id)
                )"""
        )
        connection.execute(
            """CREATE TABLE IF NOT EXISTS barrier_session_intent (
                    project_id TEXT NOT NULL,
                    intent_id TEXT PRIMARY KEY,
                    attempt_id TEXT NOT NULL,
                    expected_revision INTEGER NOT NULL,
                    proposed_revision INTEGER NOT NULL,
                    proposed_status TEXT NOT NULL,
                    identity_digest TEXT NOT NULL,
                    outcome TEXT NOT NULL,
                    cause_code TEXT,
                FOREIGN KEY(project_id) REFERENCES barrier_session(project_id)
            )"""
        )
        connection.execute(
            """CREATE TABLE IF NOT EXISTS authority_effect_intent (
                    project_id TEXT NOT NULL,
                    intent_id TEXT PRIMARY KEY,
                    operation_id TEXT NOT NULL,
                    backend TEXT NOT NULL,
                    target TEXT NOT NULL,
                    attempt_id TEXT NOT NULL,
                    identity_digest TEXT NOT NULL,
                    fencing_token TEXT NOT NULL,
                    session_revision INTEGER NOT NULL,
                    artifact_identity TEXT,
                    manifest_identity TEXT,
                    selector_identity TEXT,
                    runtime_identity TEXT,
                    outcome TEXT NOT NULL,
                    cause_code TEXT,
                    FOREIGN KEY(project_id) REFERENCES barrier_session(project_id)
                )"""
        )
        pragma_result = connection.execute("PRAGMA table_info(authority_effect_intent)")
        pragma_rows = pragma_result.fetchall() if hasattr(pragma_result, "fetchall") else []
        columns = {str(row[1]) for row in pragma_rows}
        for name in (
            "artifact_identity",
            "manifest_identity",
            "selector_identity",
            "runtime_identity",
        ):
            if name not in columns:
                connection.execute(f"ALTER TABLE authority_effect_intent ADD COLUMN {name} TEXT")

    def _prepared_intents_locked(
        self, connection: sqlite3.Connection
    ) -> list[tuple[str, str, int, int, str, str]]:
        self._control._require_operation_lock()
        rows = connection.execute(
            "SELECT intent_id,attempt_id,expected_revision,proposed_revision,identity_digest,"
            "proposed_status "
            "FROM barrier_session_intent "
            "WHERE project_id=? AND outcome='prepared' ORDER BY proposed_revision",
            (self.project_id,),
        ).fetchall()
        return [
            (
                cast(str, row[0]),
                cast(str, row[1]),
                cast(int, row[2]),
                cast(int, row[3]),
                cast(str, row[4]),
                cast(str, row[5]),
            )
            for row in rows
        ]

    def _mark_intent_locked(
        self,
        connection: sqlite3.Connection,
        intent_id: str,
        outcome: str,
        cause_code: str | None = None,
    ) -> None:
        if outcome not in {"committed", "ambiguous", "reconciled"}:
            raise ControlStoreError("barrier session intent outcome is invalid")
        cursor = connection.execute(
            "UPDATE barrier_session_intent SET outcome=?,cause_code=? "
            "WHERE project_id=? AND intent_id=? AND outcome='prepared'",
            (outcome, cause_code, self.project_id, intent_id),
        )
        if cursor.rowcount != 1:
            raise ControlStoreError("barrier session intent outcome fence was lost")

    def _prepared_effect_intents_locked(
        self, connection: sqlite3.Connection
    ) -> list[AuthorityEffectIntent]:
        self._control._require_operation_lock()
        rows = connection.execute(
            "SELECT intent_id,operation_id,backend,target,attempt_id,identity_digest,"
            "fencing_token,session_revision,artifact_identity,manifest_identity,"
            "selector_identity,runtime_identity FROM authority_effect_intent "
            "WHERE project_id=? AND outcome='prepared' ORDER BY rowid",
            (self.project_id,),
        ).fetchall()
        try:
            return [AuthorityEffectIntent(*row) for row in rows]
        except (ControlStoreError, TypeError, ValueError) as error:
            raise ControlStoreError("authority effect intent identity is invalid") from error

    def _mark_effect_intent_locked(
        self,
        connection: sqlite3.Connection,
        intent_id: str,
        outcome: str,
        cause_code: str | None = None,
    ) -> None:
        if outcome not in {"committed", "rejected", "ambiguous"}:
            raise ControlStoreError("authority effect intent outcome is invalid")
        cursor = connection.execute(
            "UPDATE authority_effect_intent SET outcome=?,cause_code=? "
            "WHERE project_id=? AND intent_id=? AND outcome='prepared'",
            (outcome, cause_code, self.project_id, intent_id),
        )
        if cursor.rowcount != 1:
            raise ControlStoreError("authority effect intent outcome fence was lost")

    @staticmethod
    def _effect_intent_matches(current: BarrierSessionState, intent: AuthorityEffectIntent) -> bool:
        return (
            current.status == "held"
            and current.revision == intent.session_revision
            and current.identity.attempt_id == intent.attempt_id
            and current.identity.identity_digest == intent.identity_digest
            and current.identity.fencing_token == intent.fencing_token
        )

    @staticmethod
    def _child_json(child: BarrierChildIdentity | None) -> str | None:
        if child is None:
            return None
        return json.dumps(
            {
                "operation_id": child.operation_id,
                "target": child.target,
                "barrier_identity_digest": child.barrier_identity_digest,
            },
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=True,
        )

    @staticmethod
    def _child(value: object) -> BarrierChildIdentity | None:
        if value is None:
            return None
        if not isinstance(value, str):
            raise ControlStoreError("barrier child encoding is invalid")
        try:
            decoded = json.loads(value)
        except (TypeError, ValueError) as error:
            raise ControlStoreError("barrier child encoding is invalid") from error
        if not isinstance(decoded, dict) or set(decoded) != {
            "operation_id",
            "target",
            "barrier_identity_digest",
        }:
            raise ControlStoreError("barrier child encoding is invalid")
        if not all(isinstance(item, str) for item in decoded.values()):
            raise ControlStoreError("barrier child encoding is invalid")
        return BarrierChildIdentity(
            operation_id=decoded["operation_id"],
            target=decoded["target"],
            barrier_identity_digest=decoded["barrier_identity_digest"],
        )

    @classmethod
    def _decode_observation(cls, project_id: str, row: tuple[object, ...]) -> BarrierSessionState:
        if len(row) == 13:
            row = (*row, None)
        if len(row) != 14:
            raise ControlStoreError("barrier session row is invalid")
        identity_record = dict(
            zip(
                (
                    "schema_version",
                    "project_id",
                    "attempt_id",
                    "state_revision",
                    "authority_revision_at_acquire",
                    "durable_barrier_id",
                    "fencing_token",
                    "fencing_owner",
                    "identity_digest",
                ),
                row[:9],
                strict=True,
            )
        )
        try:
            identity = BarrierSessionIdentity.from_record(identity_record)
        except (UpgradeIdentityError, TypeError) as error:
            raise ControlStoreError("barrier session identity is invalid") from error
        try:
            state = BarrierSessionState(
                identity,
                cast(str, row[9]),
                cast(int, row[10]),
                cls._child(row[11]),
                cls._child(row[12]),
                cast(str, row[13]) if row[13] is not None else None,
            )
        except (ControlStoreError, TypeError, ValueError) as error:
            raise ControlStoreError("barrier session state is invalid") from error
        if identity.project_id != project_id:
            raise ControlStoreError("barrier session project binding mismatch")
        return state

    def _row_state(self, row: tuple[object, ...]) -> BarrierSessionState:
        return self._decode_observation(self.project_id, row)

    @staticmethod
    def _prepared_intent_matches(
        current: BarrierSessionState,
        intent: tuple[str, str, int, int, str, str],
    ) -> bool:
        """Check that one prepared intent belongs to the durable current row."""
        _, attempt_id, expected_revision, proposed_revision, identity_digest, proposed_status = (
            intent
        )
        matches_current = (
            proposed_revision == current.revision
            and expected_revision == current.revision - 1
            and proposed_status == current.status
        )
        matches_interrupted_recovery = (
            current.status == "ambiguous"
            and proposed_revision == current.revision - 1
            and expected_revision == proposed_revision - 1
            and proposed_status in {"held", "releasing"}
        )
        matches_interrupted_reconciliation = (
            current.status == "held"
            and proposed_status == "held"
            and proposed_revision == current.revision
            and expected_revision == current.revision + 1
            and attempt_id == current.identity.attempt_id
            and identity_digest == current.identity.identity_digest
        )
        return (
            attempt_id == current.identity.attempt_id
            and identity_digest == current.identity.identity_digest
            and proposed_status in STATUS_TRANSITIONS
            and (
                matches_current
                or matches_interrupted_recovery
                or matches_interrupted_reconciliation
            )
        )

    @staticmethod
    def _is_interrupted_reconciliation(
        current: BarrierSessionState,
        intent: tuple[str, str, int, int, str, str],
    ) -> bool:
        """Identify a committed fresh held row lacking outcome publication."""
        _, _, expected_revision, proposed_revision, _, proposed_status = intent
        return (
            current.status == "held"
            and proposed_status == "held"
            and proposed_revision == current.revision
            and expected_revision == current.revision + 1
        )

    def _reconciliation_history_matches(
        self,
        connection: sqlite3.Connection,
        current: BarrierSessionState,
        intent: tuple[str, str, int, int, str, str],
    ) -> bool:
        """Require the exact typed ambiguous predecessor for a fresh fence."""
        _, _, expected_revision, _, _, _ = intent
        row = connection.execute(
            "SELECT attempt_id,revision,record_json "
            "FROM barrier_session_history WHERE project_id=? AND revision=?",
            (self.project_id, expected_revision),
        ).fetchone()
        if row is None:
            return False
        try:
            record = json.loads(cast(str, row[2]))
            if not isinstance(record, dict):
                return False
            previous = self._decode_observation(
                self.project_id,
                tuple(
                    record.get(field)
                    for field in (
                        "schema_version",
                        "project_id",
                        "attempt_id",
                        "state_revision",
                        "authority_revision_at_acquire",
                        "durable_barrier_id",
                        "fencing_token",
                        "fencing_owner",
                        "identity_digest",
                        "status",
                        "revision",
                        "forward_child",
                        "rollback_child",
                        "reopen_target",
                    )
                ),
            )
        except (ControlStoreError, TypeError, ValueError, json.JSONDecodeError):
            return False
        return (
            row[0] == previous.identity.attempt_id
            and row[1] == previous.revision
            and previous.status == "ambiguous"
            and previous.revision == expected_revision
            and previous.identity != current.identity
            and previous.identity.state_revision < current.identity.state_revision
        )

    @classmethod
    def observe_connection(  # noqa: C901
        cls, connection: sqlite3.Connection, project_id: str
    ) -> BarrierSessionState | None:
        """Decode one descriptor-bound row without acquiring another lock."""
        try:
            rows = connection.execute(cls._SELECT, (project_id,)).fetchall()
        except sqlite3.OperationalError as error:
            if "no such column: reopen_target" not in str(error).lower():
                raise
            rows = connection.execute(cls._SELECT_LEGACY, (project_id,)).fetchall()
        if not rows:
            return None
        if len(rows) != 1:
            raise ControlStoreError("durable barrier session observation is ambiguous")
        current = cls._decode_observation(project_id, tuple(rows[0]))
        # Once a session has advanced beyond its initial row, its immutable
        # identity and revision must also be present in the intent journal.
        # This rejects a forged/replaced released row that has a
        # self-consistent digest but was never produced by the CAS path.
        if current.status == "released" and current.revision > 1:
            intent = connection.execute(
                "SELECT 1 FROM barrier_session_intent "
                "WHERE project_id=? AND attempt_id=? AND identity_digest=? "
                "AND proposed_revision=? LIMIT 1",
                (
                    project_id,
                    current.identity.attempt_id,
                    current.identity.identity_digest,
                    current.revision,
                ),
            ).fetchone()
            if intent is None:
                raise ControlStoreError("durable barrier session intent is missing")
        try:
            effect_intent = connection.execute(
                "SELECT 1 FROM authority_effect_intent "
                "WHERE project_id=? AND outcome='prepared' LIMIT 1",
                (project_id,),
            ).fetchone()
        except sqlite3.OperationalError as error:
            # Older provisioned control stores predate the isolated effect
            # journal.  Absence is compatible; a malformed or unreadable
            # journal remains fail-closed below.
            if "no such table" in str(error).lower():
                return current
            raise ControlStoreError("durable authority effect journal is unreadable") from error
        except sqlite3.Error as error:
            raise ControlStoreError("durable authority effect journal is unreadable") from error
        if effect_intent is not None:
            raise ControlStoreError("durable authority effect intent is unresolved")
        return current

    def _snapshot_locked(self) -> BarrierSessionState | None:
        self._control._require_operation_lock()
        with self._control._connection() as connection:
            self._ensure_table(connection)
            row = connection.execute(self._SELECT, (self.project_id,)).fetchone()
            return None if row is None else self._row_state(row)

    def create(self, identity: BarrierSessionIdentity) -> BarrierSessionState:
        """Persist the initial held state; a second attempt is rejected."""
        return self.cas(0, BarrierSessionState(identity, "held", 1))

    def create_locked(
        self, common_guard: CoordinatorLockGuard, identity: BarrierSessionIdentity
    ) -> BarrierSessionState:
        """Create the initial held session under caller-owned locks."""
        if not isinstance(common_guard, CoordinatorLockGuard):
            raise LockOwnershipError("caller-owned coordinator lock guard is required")
        common_guard.assert_owned()
        if common_guard.path != coordinator_lock_path().resolve():
            raise ControlStoreError("coordinator lock guard path mismatch")
        if not isinstance(identity, BarrierSessionIdentity):
            raise ControlStoreError("barrier session identity is required")
        if identity.project_id != self.project_id:
            raise ControlStoreError("barrier session project binding mismatch")
        self._control._require_operation_lock()
        if self._authority_revision_reader is None:
            raise ControlStoreError("fresh authority rereader is required")
        try:
            authority_revision = self._authority_revision_reader()
        except Exception as error:
            raise ControlStoreError("fresh authority reread failed") from error
        if authority_revision != identity.authority_revision_at_acquire:
            raise ControlStoreError("barrier session authority revision changed")
        result = self._cas_locked(0, BarrierSessionState(identity, "held", 1))
        common_guard.assert_owned()
        return result

    def recheck_held(  # noqa: C901
        self,
        expected_revision: int | BarrierSessionState,
        fresh_authority_revision: str | None = None,
    ) -> BarrierSessionState:
        """Durably reread a held session before each fenced operation.

        This is intentionally read-only: the project fence and session
        revision are not advanced by a recheck.  A caller may additionally
        provide the freshly observed authority revision; a mismatch rejects
        admission instead of treating stale evidence as a held barrier.
        """
        expected_identity: BarrierSessionIdentity | None = None
        if isinstance(expected_revision, BarrierSessionState):
            expected_identity = expected_revision.identity
            expected_revision = expected_revision.revision
        if type(expected_revision) is not int or expected_revision < 1:
            raise ControlStoreError("barrier session expected revision is invalid")
        if fresh_authority_revision is not None:
            raise ControlStoreError("fresh authority revision must come from the trusted rereader")
        if self._authority_revision_reader is None:
            raise ControlStoreError("fresh authority rereader is required")
        try:
            fresh_authority_revision = self._authority_revision_reader()
        except Exception as error:
            raise ControlStoreError("fresh authority reread failed") from error
        if not isinstance(fresh_authority_revision, str) or not fresh_authority_revision:
            raise ControlStoreError("fresh authority revision is invalid")
        if self.operation_owned_by_current_thread:
            raise ControlStoreError("control store lock is non-reentrant")
        with self.operation_lock():
            current = self._snapshot_locked()
            if current is None:
                raise ControlStoreError("barrier session is absent")
            if current.revision != expected_revision:
                raise ControlStoreError("barrier session CAS conflict")
            if expected_identity is not None and expected_identity != current.identity:
                raise ControlStoreError("barrier session identity changed")
            if current.status != "held":
                raise ControlStoreError("barrier session is not held")
            if (
                fresh_authority_revision is not None
                and current.identity.authority_revision_at_acquire != fresh_authority_revision
            ):
                raise ControlStoreError("barrier session authority revision changed")
            return current

    def recheck_held_locked(  # noqa: C901
        self,
        common_guard: CoordinatorLockGuard,
        expected_identity: BarrierSessionIdentity,
        expected_revision: int,
        allowed_statuses: tuple[str, ...] = ("held",),
    ) -> BarrierSessionState:
        """Read-only session recheck while the caller owns both locks."""
        if not isinstance(common_guard, CoordinatorLockGuard):
            raise LockOwnershipError("caller-owned coordinator lock guard is required")
        common_guard.assert_owned()
        if common_guard.path != coordinator_lock_path().resolve():
            raise ControlStoreError("coordinator lock guard path mismatch")
        if not isinstance(expected_identity, BarrierSessionIdentity):
            raise ControlStoreError("barrier session identity is required")
        if type(expected_revision) is not int or expected_revision < 1:
            raise ControlStoreError("barrier session expected revision is invalid")
        if not allowed_statuses or any(
            status not in {"held", "releasing"} for status in allowed_statuses
        ):
            raise ControlStoreError("barrier session allowed statuses are invalid")
        self._control._require_operation_lock()
        if self._authority_revision_reader is None:
            raise ControlStoreError("fresh authority rereader is required")
        try:
            fresh_authority_revision = self._authority_revision_reader()
        except Exception as error:
            raise ControlStoreError("fresh authority reread failed") from error
        if not isinstance(fresh_authority_revision, str) or not fresh_authority_revision:
            raise ControlStoreError("fresh authority revision is invalid")
        current = self._snapshot_locked()
        if current is None:
            raise ControlStoreError("barrier session is absent")
        if current.revision != expected_revision:
            raise ControlStoreError("barrier session CAS conflict")
        if current.identity != expected_identity:
            raise ControlStoreError("barrier session identity changed")
        if current.status not in allowed_statuses:
            message = (
                "barrier session is not held"
                if allowed_statuses == ("held",)
                else "barrier session is not in an admissible status"
            )
            raise ControlStoreError(message)
        if current.identity.authority_revision_at_acquire != fresh_authority_revision:
            raise ControlStoreError("barrier session authority revision changed")
        common_guard.assert_owned()
        return current

    def provision_released(self, identity: BarrierSessionIdentity) -> BarrierSessionState:
        """Create one immutable released baseline during trusted provisioning.

        This is deliberately not part of the general CAS API: only an empty
        control store may receive a baseline, and later attempts must use the
        normal held-session acquisition path.
        """
        if identity.project_id != self.project_id:
            raise ControlStoreError("barrier session project binding mismatch")
        if self.operation_owned_by_current_thread:
            raise ControlStoreError("control store lock is non-reentrant")
        with self.operation_lock():
            current = self._snapshot_locked()
            if current is not None:
                if current.status == "released" and current.identity == identity:
                    return current
                raise ControlStoreError("barrier baseline already exists")
            return self._cas_locked(
                0,
                BarrierSessionState(identity, "released", 1),
                allow_initial_released=True,
            )

    def cas(self, expected_revision: int, state: BarrierSessionState) -> BarrierSessionState:
        if type(expected_revision) is not int or expected_revision < 0:
            raise ControlStoreError("barrier session expected revision is invalid")
        if state.identity.project_id != self.project_id:
            raise ControlStoreError("barrier session project binding mismatch")
        if state.status == "released" and expected_revision == 0:
            raise ControlStoreError("new barrier session must start held")
        if self.operation_owned_by_current_thread:
            raise ControlStoreError("control store lock is non-reentrant")
        with self.operation_lock():
            # Recheck under the write lock: authority may rotate after the
            # caller's admission check but before this CAS is serialized.
            if self._authority_revision_reader is not None:
                try:
                    current_authority = self._authority_revision_reader()
                except Exception as error:
                    raise ControlStoreError("fresh authority reread failed") from error
                if not isinstance(current_authority, str) or not current_authority:
                    raise ControlStoreError("fresh authority revision is invalid")
                if current_authority != state.identity.authority_revision_at_acquire:
                    raise ControlStoreError("barrier session authority revision changed")
            return self._cas_locked(expected_revision, state)

    def cas_locked(
        self,
        common_guard: CoordinatorLockGuard,
        expected_identity: BarrierSessionIdentity,
        expected_revision: int,
        state: BarrierSessionState,
    ) -> BarrierSessionState:
        """CAS one held session under caller-owned common/control locks.

        This is an uncalled adapter seam: it never acquires a lock or enables
        an authority mutation route.  The caller remains responsible for
        holding the authority lock around the eventual mutation.
        """
        if not isinstance(common_guard, CoordinatorLockGuard):
            raise LockOwnershipError("caller-owned coordinator lock guard is required")
        common_guard.assert_owned()
        if common_guard.path != coordinator_lock_path().resolve():
            raise ControlStoreError("coordinator lock guard path mismatch")
        if not isinstance(expected_identity, BarrierSessionIdentity):
            raise ControlStoreError("barrier session identity is required")
        if type(expected_revision) is not int or expected_revision < 1:
            raise ControlStoreError("barrier session expected revision is invalid")
        if state.identity != expected_identity or state.status not in {"held", "releasing"}:
            raise ControlStoreError("barrier session write identity is invalid")
        self._control._require_operation_lock()
        current = self.recheck_held_locked(common_guard, expected_identity, expected_revision)
        if current.revision != expected_revision:
            raise ControlStoreError("barrier session CAS conflict")
        common_guard.assert_owned()
        return self._cas_locked(expected_revision, state)

    def _cas_locked(  # noqa: C901
        self,
        expected_revision: int,
        supplied: BarrierSessionState,
        *,
        allow_initial_released: bool = False,
    ) -> BarrierSessionState:
        self._control._require_operation_lock()
        with self._control._connection() as connection:
            self._ensure_table(connection)
            connection.execute("BEGIN IMMEDIATE")
            current_row = connection.execute(self._SELECT, (self.project_id,)).fetchone()
            replacing_released = False
            if current_row is None:
                if expected_revision != 0:
                    connection.rollback()
                    raise ControlStoreError("barrier session does not exist")
                next_revision = 1
                if supplied.status != "held" and not (
                    allow_initial_released and supplied.status == "released"
                ):
                    connection.rollback()
                    raise ControlStoreError("new barrier session must start held")
            else:
                current = self._row_state(current_row)
                # A released session is terminal, but a new attempt may be
                # admitted with CAS(0).  Preserve the old terminal record in
                # history before replacing the current-session pointer.
                replacing_released = (
                    expected_revision == 0
                    and current.status == "released"
                    and supplied.status == "held"
                    and supplied.identity != current.identity
                )
                if replacing_released and (
                    supplied.identity.attempt_id == current.identity.attempt_id
                    or supplied.identity.state_revision <= current.identity.state_revision
                ):
                    connection.rollback()
                    raise ControlStoreError(
                        "fresh barrier session requires a distinct newer project fence"
                    )
                if not replacing_released and current.revision != expected_revision:
                    connection.rollback()
                    raise ControlStoreError("barrier session CAS conflict")
                if not replacing_released and supplied.identity != current.identity:
                    connection.rollback()
                    raise ControlStoreError("barrier session identity changed")
                if (
                    not replacing_released
                    and supplied.status not in STATUS_TRANSITIONS[current.status]
                ):
                    connection.rollback()
                    raise ControlStoreError("illegal barrier session transition")
                if not replacing_released and supplied.revision != expected_revision + 1:
                    connection.rollback()
                    raise ControlStoreError("barrier session revision is not monotonic")
                next_revision = 1 if replacing_released else supplied.revision
                if replacing_released:
                    connection.execute(
                        "INSERT OR REPLACE INTO barrier_session_history "
                        "(project_id,attempt_id,revision,record_json) VALUES (?,?,?,?)",
                        (
                            self.project_id,
                            current.identity.attempt_id,
                            current.revision,
                            json.dumps(
                                {
                                    **current.identity.as_record(),
                                    "status": current.status,
                                    "revision": current.revision,
                                    "forward_child": self._child_json(current.forward_child),
                                    "rollback_child": self._child_json(current.rollback_child),
                                    "reopen_target": current.reopen_target,
                                },
                                sort_keys=True,
                                separators=(",", ":"),
                            ),
                        ),
                    )
                    connection.execute(
                        "DELETE FROM barrier_session WHERE project_id=?", (self.project_id,)
                    )
            if supplied.revision != next_revision:
                connection.rollback()
                raise ControlStoreError("barrier session revision is invalid")
            intent_id = uuid.uuid4().hex
            connection.execute(
                "INSERT INTO barrier_session_intent "
                "(project_id,intent_id,attempt_id,expected_revision,proposed_revision,"
                "proposed_status,identity_digest,outcome,cause_code) VALUES (?,?,?,?,?,?,?,?,?)",
                (
                    self.project_id,
                    intent_id,
                    supplied.identity.attempt_id,
                    expected_revision,
                    supplied.revision,
                    supplied.status,
                    supplied.identity.identity_digest,
                    "prepared",
                    None,
                ),
            )
            values = (
                *supplied.identity.as_record().values(),
                supplied.status,
                supplied.revision,
                self._child_json(supplied.forward_child),
                self._child_json(supplied.rollback_child),
                supplied.reopen_target,
            )
            if current_row is None:
                cursor = connection.execute(
                    "INSERT INTO barrier_session "
                    "(schema_version,project_id,attempt_id,state_revision,"
                    "authority_revision_at_acquire,durable_barrier_id,fencing_token,"
                    "fencing_owner,identity_digest,status,revision,forward_child,rollback_child,"
                    "reopen_target) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    values,
                )
            else:
                if replacing_released:
                    cursor = connection.execute(
                        "INSERT INTO barrier_session "
                        "(schema_version,project_id,attempt_id,state_revision,"
                        "authority_revision_at_acquire,durable_barrier_id,fencing_token,"
                        "fencing_owner,identity_digest,status,revision,forward_child,"
                        "rollback_child,reopen_target) "
                        "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                        values,
                    )
                else:
                    cursor = connection.execute(
                        "UPDATE barrier_session SET status=?,revision=?,forward_child=?,"
                        "rollback_child=?,reopen_target=? WHERE project_id=? AND revision=?",
                        (
                            supplied.status,
                            supplied.revision,
                            values[-3],
                            values[-2],
                            values[-1],
                            self.project_id,
                            expected_revision,
                        ),
                    )
            if cursor.rowcount != 1:
                connection.rollback()
                raise ControlStoreError("barrier session CAS update lost its fence")
            try:
                connection.commit()
            except Exception as error:
                raise ControlStoreError(
                    "barrier session commit outcome is ambiguous; durable state must be rechecked"
                ) from self._mark_ambiguous_after_commit_failure(
                    connection, supplied, expected_revision, error
                )
            try:
                connection.execute("BEGIN IMMEDIATE")
                self._mark_intent_locked(connection, intent_id, "committed")
            except Exception as error:
                raise ControlStoreError(
                    "barrier session outcome publication is ambiguous; recovery is required"
                ) from error
            try:
                connection.commit()
            except Exception as error:
                raise ControlStoreError(
                    "barrier session outcome publication is ambiguous; recovery is required"
                ) from self._mark_recovery_ambiguous_after_commit_failure(connection, error)
            return supplied

    def _recover_prepared_locked(  # noqa: C901
        self,
        connection: sqlite3.Connection,
        prepared: list[tuple[str, str, int, int, str, str]],
    ) -> BarrierSessionState:
        """Resolve prepared intents while the control-store lock is held."""
        current = self._snapshot_locked()
        if current is None:
            raise ControlStoreError("prepared session intent has no session")
        if not all(self._prepared_intent_matches(current, intent) for intent in prepared):
            raise ControlStoreError("prepared session intent identity is invalid")
        if all(self._is_interrupted_reconciliation(current, intent) for intent in prepared):
            if not all(
                self._reconciliation_history_matches(connection, current, intent)
                for intent in prepared
            ):
                raise ControlStoreError("prepared reconciliation history is invalid")
            connection.execute("BEGIN IMMEDIATE")
            for intent_id, *_ in prepared:
                self._mark_intent_locked(connection, intent_id, "reconciled")
            try:
                connection.commit()
            except Exception as error:
                raise ControlStoreError(
                    "recovery commit outcome is ambiguous; durable state must be rechecked"
                ) from self._mark_recovery_ambiguous_after_commit_failure(connection, error)
            return current
        if current.status != "ambiguous":
            connection.execute("BEGIN IMMEDIATE")
            connection.execute(
                "UPDATE barrier_session SET status='ambiguous',revision=? "
                "WHERE project_id=? AND revision=? AND status IN ('held','releasing')",
                (current.revision + 1, self.project_id, current.revision),
            )
            if connection.execute("SELECT changes()").fetchone()[0] != 1:
                connection.rollback()
                raise ControlStoreError("unknown session outcome lost its row fence")
            current = BarrierSessionState(
                current.identity,
                "ambiguous",
                current.revision + 1,
                current.forward_child,
                current.rollback_child,
                current.reopen_target,
            )
            try:
                connection.commit()
            except Exception as error:
                raise ControlStoreError(
                    "recovery commit outcome is ambiguous; durable state must be rechecked"
                ) from self._mark_recovery_ambiguous_after_commit_failure(connection, error)
        connection.execute("BEGIN IMMEDIATE")
        for intent_id, _attempt_id, _expected, _proposed, _digest, _status in prepared:
            self._mark_intent_locked(connection, intent_id, "ambiguous", "process-death")
        try:
            connection.commit()
        except Exception as error:
            raise ControlStoreError(
                "recovery commit outcome is ambiguous; durable state must be rechecked"
            ) from self._mark_recovery_ambiguous_after_commit_failure(connection, error)
        return current

    def _mark_recovery_ambiguous_after_commit_failure(
        self,
        connection: sqlite3.Connection,
        commit_error: Exception,
    ) -> Exception:
        """Fence uncertain recovery progress into a durable ambiguous session."""
        try:
            connection.rollback()
            connection.execute("BEGIN IMMEDIATE")
            latest_row = connection.execute(self._SELECT, (self.project_id,)).fetchone()
            if latest_row is None:
                raise ControlStoreError("recovery ambiguity fencing found no session")
            latest = self._row_state(latest_row)
            if latest.status in {"held", "releasing"}:
                cursor = connection.execute(
                    "UPDATE barrier_session SET status='ambiguous',revision=? "
                    "WHERE project_id=? AND revision=?",
                    (latest.revision + 1, self.project_id, latest.revision),
                )
                if cursor.rowcount != 1:
                    raise ControlStoreError("recovery ambiguity fencing lost its row fence")
            for intent_id, *_ in self._prepared_intents_locked(connection):
                cursor = connection.execute(
                    "UPDATE barrier_session_intent SET outcome='ambiguous',"
                    "cause_code='commit-uncertain' WHERE project_id=? AND intent_id=? "
                    "AND outcome='prepared'",
                    (self.project_id, intent_id),
                )
                if cursor.rowcount != 1:
                    raise ControlStoreError("recovery session intent fence was lost")
            for intent in self._prepared_effect_intents_locked(connection):
                cursor = connection.execute(
                    "UPDATE authority_effect_intent SET outcome='ambiguous',"
                    "cause_code='commit-uncertain' WHERE project_id=? AND intent_id=? "
                    "AND outcome='prepared'",
                    (self.project_id, intent.intent_id),
                )
                if cursor.rowcount != 1:
                    raise ControlStoreError("recovery effect intent fence was lost")
            connection.commit()
        except Exception as recovery_error:
            raise ControlStoreError(
                "recovery commit outcome is ambiguous and could not be durably fenced"
            ) from recovery_error
        return commit_error

    def prepare_authority_effect(  # noqa: C901
        self,
        expected_revision: int,
        operation_id: str,
        backend: str,
        target: str = "new",
        *,
        expected_fencing_token: str | None = None,
        expected_barrier_id: str | None = None,
        expected_artifact_identity: str | None = None,
        expected_manifest_identity: str | None = None,
        expected_selector_identity: str | None = None,
        expected_runtime_identity: str | None = None,
        _common_guard: CoordinatorLockGuard | None = None,
    ) -> AuthorityEffectIntent:
        """Durably fence one external authority effect before invoking it.

        This is an isolated adapter seam.  It records intent only; it does not
        dispatch, commit, apply, or publish any authority mutation.
        """
        if type(expected_revision) is not int or expected_revision < 1:
            raise ControlStoreError("authority effect session revision is invalid")
        intent_id = uuid.uuid4().hex
        if not all(isinstance(value, str) and value for value in (operation_id, backend, target)):
            raise ControlStoreError("authority effect identity is invalid")
        if backend not in {"git", "sqlite"} or target not in {"new", "rollback"}:
            raise ControlStoreError("authority effect backend or target is invalid")
        for value, label in (
            (expected_fencing_token, "fencing token"),
            (expected_barrier_id, "barrier identity"),
        ):
            if value is not None and (not isinstance(value, str) or not value):
                raise ControlStoreError(f"authority effect {label} is invalid")
        admission_identities = (
            expected_artifact_identity,
            expected_manifest_identity,
            expected_selector_identity,
            expected_runtime_identity,
        )
        if any(
            value is not None and (not isinstance(value, str) or not value)
            for value in admission_identities
        ):
            raise ControlStoreError("authority effect admission identity is invalid")
        if any(value is None for value in admission_identities) and any(
            value is not None for value in admission_identities
        ):
            raise ControlStoreError("authority effect admission identity is incomplete")
        if _common_guard is None and self.operation_owned_by_current_thread:
            raise ControlStoreError("control store lock is non-reentrant")
        with self._authority_effect_scope(_common_guard), self._control._connection() as connection:
            self._ensure_table(connection)
            current = self._snapshot_locked()
            if current is None or current.status != "held":
                raise ControlStoreError("authority effect requires a held barrier session")
            if "." in operation_id or ":" in operation_id:
                child = current.rollback_child if target == "rollback" else current.forward_child
                expected_child_ids = {operation_id, operation_id.rsplit(":", 1)[0]}
                if child is not None and (
                    child.operation_id not in expected_child_ids or child.target != target
                ):
                    raise ControlStoreError(
                        "authority effect operation is not the registered barrier child"
                    )
            if current.revision != expected_revision:
                raise ControlStoreError("authority effect session revision conflict")
            if (
                expected_fencing_token is not None
                and current.identity.fencing_token != expected_fencing_token
            ):
                raise ControlStoreError("authority effect fencing token conflict")
            if (
                expected_barrier_id is not None
                and current.identity.durable_barrier_id != expected_barrier_id
            ):
                raise ControlStoreError("authority effect barrier identity conflict")
            prepared = self._prepared_effect_intents_locked(connection)
            if prepared:
                raise ControlStoreError("authority effect has unresolved intent")
            prior = connection.execute(
                "SELECT outcome FROM authority_effect_intent "
                "WHERE project_id=? AND operation_id=? LIMIT 1",
                (self.project_id, operation_id),
            ).fetchone()
            if prior is not None:
                if prior[0] == "ambiguous":
                    raise ControlStoreError(
                        "authority effect operation has an ambiguous prior outcome"
                    )
                raise ControlStoreError("authority effect operation was already recorded")
            intent = AuthorityEffectIntent(
                intent_id,
                operation_id,
                backend,
                target,
                current.identity.attempt_id,
                current.identity.identity_digest,
                current.identity.fencing_token,
                current.revision,
                expected_artifact_identity,
                expected_manifest_identity,
                expected_selector_identity,
                expected_runtime_identity,
            )
            connection.execute("BEGIN IMMEDIATE")
            connection.execute(
                "INSERT INTO authority_effect_intent "
                "(project_id,intent_id,operation_id,backend,target,attempt_id,"
                "identity_digest,fencing_token,session_revision,artifact_identity,"
                "manifest_identity,selector_identity,runtime_identity,outcome,cause_code) "
                "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (
                    self.project_id,
                    intent.intent_id,
                    intent.operation_id,
                    intent.backend,
                    intent.target,
                    intent.attempt_id,
                    intent.identity_digest,
                    intent.fencing_token,
                    intent.session_revision,
                    intent.artifact_identity,
                    intent.manifest_identity,
                    intent.selector_identity,
                    intent.runtime_identity,
                    "prepared",
                    None,
                ),
            )
            connection.commit()
            return intent

    def prepare_authority_effect_locked(
        self,
        common_guard: CoordinatorLockGuard,
        expected_revision: int,
        operation_id: str,
        backend: str,
        target: str = "new",
        *,
        expected_fencing_token: str | None = None,
        expected_barrier_id: str | None = None,
        expected_artifact_identity: str | None = None,
        expected_manifest_identity: str | None = None,
        expected_selector_identity: str | None = None,
        expected_runtime_identity: str | None = None,
    ) -> AuthorityEffectIntent:
        """Prepare one authority effect under caller-owned full-scope locks."""
        return self.prepare_authority_effect(
            expected_revision,
            operation_id,
            backend,
            target,
            expected_fencing_token=expected_fencing_token,
            expected_barrier_id=expected_barrier_id,
            expected_artifact_identity=expected_artifact_identity,
            expected_manifest_identity=expected_manifest_identity,
            expected_selector_identity=expected_selector_identity,
            expected_runtime_identity=expected_runtime_identity,
            _common_guard=common_guard,
        )

    def finish_authority_effect(  # noqa: C901
        self,
        intent: AuthorityEffectIntent,
        outcome: str,
        receipt: object | None = None,
        *,
        _common_guard: CoordinatorLockGuard | None = None,
    ) -> BarrierSessionState:
        """Publish an effect result, fencing ambiguity instead of retrying it."""
        if not isinstance(intent, AuthorityEffectIntent):
            raise ControlStoreError("authority effect intent is required")
        if outcome not in {"committed", "rejected", "ambiguous"}:
            raise ControlStoreError("authority effect outcome is invalid")
        if outcome == "committed" and intent.artifact_identity is not None:
            _validate_authority_effect_receipt(intent, receipt)
        if _common_guard is None and self.operation_owned_by_current_thread:
            raise ControlStoreError("control store lock is non-reentrant")
        with self._authority_effect_scope(_common_guard), self._control._connection() as connection:
            self._ensure_table(connection)
            current = self._snapshot_locked()
            if current is None or not self._effect_intent_matches(current, intent):
                raise ControlStoreError("authority effect session identity changed")
            if current.status != "held" and outcome == "committed":
                raise ControlStoreError(
                    "authority effect cannot complete from an ambiguous barrier"
                )
            connection.execute("BEGIN IMMEDIATE")
            self._mark_effect_intent_locked(connection, intent.intent_id, outcome)
            if outcome == "ambiguous":
                cursor = connection.execute(
                    "UPDATE barrier_session SET status='ambiguous',revision=? "
                    "WHERE project_id=? AND revision=? AND status='held'",
                    (current.revision + 1, self.project_id, current.revision),
                )
                if cursor.rowcount != 1:
                    connection.rollback()
                    raise ControlStoreError("authority effect ambiguity lost its row fence")
                current = BarrierSessionState(
                    current.identity,
                    "ambiguous",
                    current.revision + 1,
                    current.forward_child,
                    current.rollback_child,
                    current.reopen_target,
                )
            try:
                connection.commit()
            except Exception as error:
                raise ControlStoreError(
                    "authority effect outcome publication is ambiguous; recovery is required"
                ) from self._mark_recovery_ambiguous_after_commit_failure(connection, error)
            return current

    def finish_authority_effect_locked(
        self,
        common_guard: CoordinatorLockGuard,
        intent: AuthorityEffectIntent,
        outcome: str,
        receipt: object | None = None,
    ) -> BarrierSessionState:
        """Publish one authority-effect outcome under caller-owned full-scope locks."""
        return self.finish_authority_effect(intent, outcome, receipt, _common_guard=common_guard)

    @contextmanager
    def _authority_effect_scope(self, common_guard: CoordinatorLockGuard | None) -> Iterator[None]:
        if common_guard is None:
            with self.operation_lock():
                yield
            return
        if not isinstance(common_guard, CoordinatorLockGuard):
            raise LockOwnershipError("caller-owned coordinator lock guard is required")
        common_guard.assert_owned()
        if common_guard.path != coordinator_lock_path().resolve():
            raise ControlStoreError("coordinator lock guard path mismatch")
        self._control._require_operation_lock()
        common_guard.assert_owned()
        yield
        common_guard.assert_owned()

    def _recover_prepared_effects_locked(
        self,
        connection: sqlite3.Connection,
        prepared: list[AuthorityEffectIntent],
    ) -> BarrierSessionState:
        current = self._snapshot_locked()
        if current is None:
            raise ControlStoreError("prepared authority effect has no session")
        if not all(
            intent.attempt_id == current.identity.attempt_id
            and intent.identity_digest == current.identity.identity_digest
            and intent.fencing_token == current.identity.fencing_token
            and intent.session_revision in {current.revision, current.revision - 1}
            for intent in prepared
        ):
            raise ControlStoreError("prepared authority effect identity is invalid")
        connection.execute("BEGIN IMMEDIATE")
        if current.status == "held":
            cursor = connection.execute(
                "UPDATE barrier_session SET status='ambiguous',revision=? "
                "WHERE project_id=? AND revision=? AND status='held'",
                (current.revision + 1, self.project_id, current.revision),
            )
            if cursor.rowcount != 1:
                connection.rollback()
                raise ControlStoreError("unknown authority effect lost its row fence")
            current = BarrierSessionState(
                current.identity,
                "ambiguous",
                current.revision + 1,
                current.forward_child,
                current.rollback_child,
                current.reopen_target,
            )
        for intent in prepared:
            self._mark_effect_intent_locked(
                connection, intent.intent_id, "ambiguous", "process-death"
            )
        try:
            connection.commit()
        except Exception as error:
            raise ControlStoreError(
                "recovery commit outcome is ambiguous; durable state must be rechecked"
            ) from self._mark_recovery_ambiguous_after_commit_failure(connection, error)
        return current

    def _recover_unknown_connection_locked(
        self, connection: sqlite3.Connection
    ) -> BarrierSessionState | None:
        """Recover prepared outcomes while the caller owns control storage."""
        self._ensure_table(connection)
        prepared_effects = self._prepared_effect_intents_locked(connection)
        if prepared_effects:
            return self._recover_prepared_effects_locked(connection, prepared_effects)
        prepared = self._prepared_intents_locked(connection)
        return (
            self._snapshot_locked()
            if not prepared
            else self._recover_prepared_locked(connection, prepared)
        )

    def recover_unknown(self) -> BarrierSessionState | None:
        """Fence every prepared outcome left by a process death or lost reply."""
        if self.operation_owned_by_current_thread:
            raise ControlStoreError("control store lock is non-reentrant")
        with self.operation_lock():
            self._control._reconcile_wal_lifecycle_locked()
            with self._control._connection() as connection:
                return self._recover_unknown_connection_locked(connection)

    def recover_unknown_locked(
        self, common_guard: CoordinatorLockGuard
    ) -> BarrierSessionState | None:
        """Recover prepared outcomes under a caller-owned common/control lock."""
        if not isinstance(common_guard, CoordinatorLockGuard):
            raise LockOwnershipError("caller-owned coordinator lock guard is required")
        common_guard.assert_owned()
        if common_guard.path != coordinator_lock_path().resolve():
            raise ControlStoreError("coordinator lock guard path mismatch")
        self._control._require_operation_lock()
        self._control._reconcile_wal_lifecycle_locked()
        with self._control._connection() as connection:
            result = self._recover_unknown_connection_locked(connection)
        common_guard.assert_owned()
        return result

    def reconcile_ambiguous(  # noqa: C901
        self,
        expected_revision: int,
        replacement: BarrierSessionState,
        *,
        common_guard: CoordinatorLockGuard | None = None,
    ) -> BarrierSessionState:
        """Replace an ambiguous session only with a distinct newer fence."""
        if type(expected_revision) is not int or expected_revision < 1:
            raise RecoveryRejectedError("barrier session expected revision is invalid")
        if (
            replacement.status != "held"
            or replacement.revision != 1
            or replacement.identity.project_id != self.project_id
        ):
            raise RecoveryRejectedError("ambiguous reconciliation requires a new held session")
        if common_guard is None:
            if self.operation_owned_by_current_thread:
                raise RecoveryRejectedError("control store lock is non-reentrant")
            lock_context: AbstractContextManager[object] = self.operation_lock()
        else:
            if not isinstance(common_guard, CoordinatorLockGuard):
                raise LockOwnershipError("caller-owned coordinator lock guard is required")
            common_guard.assert_owned()
            if common_guard.path != coordinator_lock_path().resolve():
                raise RecoveryRejectedError("coordinator lock guard path mismatch")
            self._control._require_operation_lock()
            lock_context = nullcontext()
        with lock_context, self._control._connection() as connection:
            self._ensure_table(connection)
            current = self._snapshot_locked()
            if current is None or current.status != "ambiguous":
                raise RecoveryRejectedError("only ambiguous sessions require reconciliation")
            if current.revision != expected_revision:
                raise RecoveryRejectedError("barrier session CAS conflict")
            if (
                replacement.identity.attempt_id == current.identity.attempt_id
                or replacement.identity.state_revision <= current.identity.state_revision
                or replacement.identity.durable_barrier_id == current.identity.durable_barrier_id
                or replacement.identity.fencing_token == current.identity.fencing_token
            ):
                raise RecoveryRejectedError(
                    "ambiguous reconciliation requires a distinct newer fence"
                )
            if self._prepared_intents_locked(connection) or self._prepared_effect_intents_locked(
                connection
            ):
                raise RecoveryRejectedError("ambiguous reconciliation has unresolved intent")
            if self._authority_revision_reader is None:
                raise RecoveryRejectedError("fresh authority rereader is required")
            try:
                fresh_authority_revision = self._authority_revision_reader()
            except Exception as error:
                raise RecoveryRejectedError("fresh authority reread failed") from error
            if not isinstance(fresh_authority_revision, str) or not fresh_authority_revision:
                raise RecoveryRejectedError("fresh authority revision is invalid")
            if fresh_authority_revision != replacement.identity.authority_revision_at_acquire:
                raise RecoveryRejectedError("replacement authority revision changed")
            intent_id = uuid.uuid4().hex
            connection.execute("BEGIN IMMEDIATE")
            connection.execute(
                "INSERT INTO barrier_session_intent "
                "(project_id,intent_id,attempt_id,expected_revision,proposed_revision,"
                "proposed_status,identity_digest,outcome,cause_code) VALUES (?,?,?,?,?,?,?,?,?)",
                (
                    self.project_id,
                    intent_id,
                    replacement.identity.attempt_id,
                    expected_revision,
                    replacement.revision,
                    replacement.status,
                    replacement.identity.identity_digest,
                    "prepared",
                    None,
                ),
            )
            connection.execute(
                "INSERT OR REPLACE INTO barrier_session_history "
                "(project_id,attempt_id,revision,record_json) VALUES (?,?,?,?)",
                (
                    self.project_id,
                    current.identity.attempt_id,
                    current.revision,
                    json.dumps(
                        {
                            **current.identity.as_record(),
                            "status": current.status,
                            "revision": current.revision,
                            "forward_child": self._child_json(current.forward_child),
                            "rollback_child": self._child_json(current.rollback_child),
                            "reopen_target": current.reopen_target,
                        },
                        sort_keys=True,
                        separators=(",", ":"),
                    ),
                ),
            )
            connection.execute("DELETE FROM barrier_session WHERE project_id=?", (self.project_id,))
            values = (
                *replacement.identity.as_record().values(),
                replacement.status,
                replacement.revision,
                self._child_json(replacement.forward_child),
                self._child_json(replacement.rollback_child),
                replacement.reopen_target,
            )
            connection.execute(
                "INSERT INTO barrier_session "
                "(schema_version,project_id,attempt_id,state_revision,authority_revision_at_acquire,"
                "durable_barrier_id,fencing_token,fencing_owner,identity_digest,status,revision,"
                "forward_child,rollback_child,reopen_target) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                values,
            )
            try:
                connection.commit()
            except Exception as error:
                raise ControlStoreError(
                    "barrier session reconciliation commit outcome is ambiguous; "
                    "recovery is required"
                ) from self._mark_ambiguous_after_commit_failure(
                    connection, replacement, expected_revision, error
                )
            try:
                connection.execute("BEGIN IMMEDIATE")
                self._mark_intent_locked(connection, intent_id, "reconciled")
                connection.commit()
            except Exception as error:
                raise ControlStoreError(
                    "barrier session reconciliation outcome is ambiguous; recovery is required"
                ) from error
            if common_guard is not None:
                common_guard.assert_owned()
            return replacement

    def reconcile_ambiguous_locked(
        self,
        common_guard: CoordinatorLockGuard,
        expected_revision: int,
        replacement: BarrierSessionState,
    ) -> BarrierSessionState:
        """Reconcile an ambiguous session under caller-owned locks."""
        return self.reconcile_ambiguous(expected_revision, replacement, common_guard=common_guard)

    def _mark_ambiguous_after_commit_failure(
        self,
        connection: sqlite3.Connection,
        supplied: BarrierSessionState,
        expected_revision: int,
        commit_error: Exception,
    ) -> Exception:
        """Fence an uncertain session CAS outcome into durable ambiguity."""
        try:
            connection.rollback()
            connection.execute("BEGIN IMMEDIATE")
            current_row = connection.execute(self._SELECT, (self.project_id,)).fetchone()
            if current_row is None:
                ambiguous = BarrierSessionState(
                    supplied.identity,
                    "ambiguous",
                    expected_revision + 1,
                    supplied.forward_child,
                    supplied.rollback_child,
                    supplied.reopen_target,
                )
                values = (
                    *ambiguous.identity.as_record().values(),
                    ambiguous.status,
                    ambiguous.revision,
                    self._child_json(ambiguous.forward_child),
                    self._child_json(ambiguous.rollback_child),
                    ambiguous.reopen_target,
                )
                cursor = connection.execute(
                    "INSERT INTO barrier_session "
                    "(schema_version,project_id,attempt_id,state_revision,"
                    "authority_revision_at_acquire,durable_barrier_id,fencing_token,"
                    "fencing_owner,identity_digest,status,revision,forward_child,rollback_child,"
                    "reopen_target) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    values,
                )
            else:
                current = self._row_state(current_row)
                cursor = connection.execute(
                    "UPDATE barrier_session SET status='ambiguous',revision=? "
                    "WHERE project_id=? AND revision=?",
                    (current.revision + 1, self.project_id, current.revision),
                )
            if cursor.rowcount != 1:
                raise ControlStoreError("ambiguous session fencing lost its row fence")
            connection.commit()
        except Exception as recovery_error:
            raise ControlStoreError(
                "barrier session commit outcome is ambiguous and could not be durably fenced"
            ) from recovery_error
        return commit_error

    def bind_child(
        self, expected_revision: int, child: BarrierChildIdentity
    ) -> BarrierSessionState:
        current = self.snapshot()
        if current is None:
            raise ControlStoreError("barrier session is absent")
        if expected_revision != current.revision:
            raise ControlStoreError("barrier session revision conflict")
        contract = BarrierSessionContract(current.identity)
        # Reconstruct only to reuse the already-tested transition rules.
        contract._state = current
        return self.cas(expected_revision, contract.bind_child(expected_revision, child))

    def begin_reopen(
        self,
        expected_revision: int,
        target: str,
        verified_child_evidence: Mapping[str, object] | None = None,
    ) -> BarrierSessionState:
        current = self.snapshot()
        if current is None:
            raise ControlStoreError("barrier session is absent")
        contract = BarrierSessionContract(current.identity)
        contract._state = current
        return self.cas(
            expected_revision,
            contract.begin_reopen(expected_revision, target, verified_child_evidence),
        )

    def complete_reopen(
        self,
        expected_revision: int,
        fresh_runtime_evidence: Mapping[str, object] | None = None,
    ) -> BarrierSessionState:
        current = self.snapshot()
        if current is None:
            raise ControlStoreError("barrier session is absent")
        contract = BarrierSessionContract(current.identity)
        contract._state = current
        return self.cas(
            expected_revision,
            contract.complete_reopen(expected_revision, fresh_runtime_evidence),
        )

    def mark_ambiguous(self, expected_revision: int, cause_code: str) -> BarrierSessionState:
        current = self.snapshot()
        if current is None:
            raise ControlStoreError("barrier session is absent")
        contract = BarrierSessionContract(current.identity)
        contract._state = current
        return self.cas(expected_revision, contract.mark_ambiguous(expected_revision, cause_code))
