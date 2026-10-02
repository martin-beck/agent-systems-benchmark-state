# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Durable fail-closed phase journal for the upgrade engine."""

from __future__ import annotations

import hashlib
import json
import os
import tempfile
import time
from collections.abc import Callable, Iterator, Mapping
from contextlib import AbstractContextManager, contextmanager, nullcontext
from copy import deepcopy
from dataclasses import asdict, dataclass
from dataclasses import field as dataclass_field
from pathlib import Path
from types import MappingProxyType
from typing import Any, Protocol, cast, runtime_checkable

from tools.authority_mutation import (
    AuthorityMutationAmbiguousError,
    AuthorityMutationRejectedError,
)
from tools.authority_neutral_backup import BoundBackupPhaseAdapter
from tools.authority_neutral_commit_dispatch import BoundCommitPhaseAdapter, CommitDispatchError
from tools.authority_neutral_rollback_dispatch import (
    BoundRollbackPhaseAdapter,
    RollbackDispatchError,
)
from tools.authority_neutral_stage import BoundStagePhaseAdapter
from tools.authority_neutral_validation import BoundValidationPhaseAdapter
from tools.rollback_control_store import ControlStoreError
from tools.rollback_evidence import BackupObservation
from tools.runtime_bootstrap import DispatchAdmission
from tools.upgrade_admission import (
    admit_preflight,
    admit_quiesced,
    admit_reopen,
    recheck_before_replacement,
)
from tools.upgrade_identity import (
    ENVELOPE_FIELDS,
    UpgradeIdentityError,
    canonical_barrier_digest,
    canonical_envelope_digest,
    validate_envelope,
)

try:
    import fcntl
except ImportError:  # pragma: no cover - the coordinator is POSIX-only
    fcntl = None  # type: ignore[assignment]

PHASES = ("discover", "preflight", "quiesce", "backup", "stage", "commit", "validate", "reopen")
JOURNAL_SCHEMA_VERSION = 3
MAX_OPERATION_ID_LENGTH = 128 - max(len(f".{phase}") for phase in (*PHASES, "rollback"))


@dataclass(frozen=True)
class JournalSnapshot:
    """Immutable validated journal envelope for diagnostics and recovery tests."""

    status: str
    phase: str | None
    records: tuple[Mapping[str, object], ...]

    @classmethod
    def from_mapping(cls, value: Mapping[str, object]) -> JournalSnapshot:
        if not isinstance(value, Mapping):
            raise ValueError("journal snapshot must be a mapping")
        if set(value) != {"status", "phase", "records"}:
            raise ValueError("journal snapshot fields are invalid")
        status, phase, records = value["status"], value["phase"], value["records"]
        if not isinstance(status, str) or (phase is not None and not isinstance(phase, str)):
            raise ValueError("journal snapshot identity is invalid")
        if not isinstance(records, list) or not all(
            isinstance(record, Mapping) for record in records
        ):
            raise ValueError("journal snapshot records are invalid")
        immutable_records = tuple(cast(Mapping[str, object], _freeze(record)) for record in records)
        return cls(status, phase, immutable_records)

    def as_mapping(self) -> dict[str, object]:
        return {
            "status": self.status,
            "phase": self.phase,
            "records": [_thaw(record) for record in self.records],
        }


class UpgradeError(RuntimeError):
    """An upgrade cannot safely advance."""


Handler = Callable[[str, Mapping[str, Any]], Mapping[str, Any] | None]


@runtime_checkable
class BackendAdapter(Protocol):
    """Concrete authority adapter for Git or SQLite upgrade operations."""

    def snapshot(self, phase: str, context: Mapping[str, object]) -> Mapping[str, object]: ...

    def verify_rollback_context(
        self, context: Mapping[str, object]
    ) -> Mapping[str, object] | None: ...

    def execute(self, phase: str, context: Mapping[str, object]) -> Mapping[str, object]: ...


@runtime_checkable
class RollbackObservationProvider(Protocol):
    """Adapter-owned, lock-scoped source of typed rollback observations."""

    @property
    def observation_provider_token(self) -> object: ...

    def observe_backup_identity(
        self, backup: Path, manifest: Path, context: Mapping[str, object]
    ) -> BackupObservation: ...


@dataclass(frozen=True, init=False)
class SQLiteRollbackObservationCapability:
    """Instance-bound SQLite observation authority; never authorizes rollback."""

    adapter: object
    identity: tuple[object, ...]

    def __init__(self) -> None:
        raise TypeError("SQLite rollback observation capability must be bound")

    @classmethod
    def bind(
        cls, context: PhaseContext, adapter: RollbackObservationProvider
    ) -> SQLiteRollbackObservationCapability:
        from tools.rollback_control_store import SQLiteControlStoreAdapter

        if not isinstance(adapter, SQLiteControlStoreAdapter):
            raise UpgradeError("SQLite rollback observation requires a concrete adapter")
        fields = tuple(field for field in CONTEXT_FIELDS if field != "target")
        capability = object.__new__(cls)
        object.__setattr__(capability, "adapter", adapter)
        object.__setattr__(
            capability, "identity", tuple(asdict(context)[field] for field in fields)
        )
        return capability

    def observe(self, context: Mapping[str, object]) -> BackupObservation:
        fields = tuple(field for field in CONTEXT_FIELDS if field != "target")
        if self.identity != tuple(context.get(field) for field in fields):
            raise UpgradeError("SQLite rollback observation context identity mismatch")
        backup = context.get("destination")
        manifest = context.get("manifest")
        if not isinstance(backup, str) or not isinstance(manifest, str):
            raise UpgradeError("rollback preflight artifact paths are invalid")
        return cast(RollbackObservationProvider, self.adapter).observe_backup_identity(
            Path(backup), Path(manifest), context
        )


@dataclass(frozen=True, init=False)
class GitRollbackObservationCapability:
    """Instance-bound Git observation authority; never authorizes rollback."""

    adapter: object
    identity: tuple[object, ...]
    scope: object
    lease: object
    admission_recheck: object
    expected_branch: str
    expected_head: str

    def __init__(self) -> None:
        raise TypeError("Git rollback observation capability must be bound")

    @classmethod
    def bind(
        cls,
        context: PhaseContext,
        adapter: object,
        scope: object,
        *,
        lease: object,
        admission_recheck: object,
        expected_branch: str,
        expected_head: str,
    ) -> GitRollbackObservationCapability:
        from tools.git_authority_adapter import GitAuthorityAdapter

        if not isinstance(adapter, GitAuthorityAdapter):
            raise UpgradeError("Git rollback observation requires a concrete adapter")
        if not isinstance(expected_branch, str) or not expected_branch:
            raise UpgradeError("Git rollback branch binding is invalid")
        if not isinstance(expected_head, str) or not expected_head:
            raise UpgradeError("Git rollback head binding is invalid")
        fields = tuple(field for field in CONTEXT_FIELDS if field != "target")
        capability = object.__new__(cls)
        object.__setattr__(capability, "adapter", adapter)
        object.__setattr__(
            capability, "identity", tuple(asdict(context)[field] for field in fields)
        )
        object.__setattr__(capability, "scope", scope)
        object.__setattr__(capability, "lease", lease)
        object.__setattr__(capability, "admission_recheck", admission_recheck)
        object.__setattr__(capability, "expected_branch", expected_branch)
        object.__setattr__(capability, "expected_head", expected_head)
        return capability

    def observe(self, context: Mapping[str, object]) -> BackupObservation:
        from tools.admission_lease import AdmissionLease, AdmissionRecheck
        from tools.git_authority_adapter import GitAuthorityAdapter, GitBackupObservation
        from tools.lock_domain_scope import LockDomainScope

        fields = tuple(field for field in CONTEXT_FIELDS if field != "target")
        if self.identity != tuple(context.get(field) for field in fields):
            raise UpgradeError("Git rollback observation context identity mismatch")
        result = cast(GitAuthorityAdapter, self.adapter).preflight_git(
            context,
            cast(LockDomainScope, self.scope),
            lease=cast(AdmissionLease, self.lease),
            admission_recheck=cast(AdmissionRecheck, self.admission_recheck),
            expected_branch=self.expected_branch,
            expected_head=self.expected_head,
        )
        if not isinstance(result, GitBackupObservation):
            raise UpgradeError("Git rollback observation result is invalid")
        return cast(BackupObservation, result)


REQUIRED_EVIDENCE = {
    "discover": ("release_authentic", "runtime_supported", "backend_identity_verified"),
    "preflight": ("preflight_admitted", "capacity_verified", "backend_identity_verified"),
    "quiesce": ("barrier_acquired", "workers_drained", "leases_fenced", "fencing_verified"),
    "backup": ("backup_verified", "restore_roundtrip_verified", "backend_identity_verified"),
    "stage": ("staged_verified", "manifest_verified", "backend_identity_verified"),
    "commit": (
        "quiesced",
        "backup_verified",
        "selector_verified",
        "selector_commit_atomic",
        "fencing_verified",
        "selector_before_verified",
        "selector_after_verified",
    ),
    "validate": (
        "runtime_validated",
        "backend_roundtrip_valid",
        "projections_valid",
        "binding_valid",
    ),
    "reopen": ("validated", "barrier_held"),
}
ROLLBACK_RESULT_FIELDS = {
    "restored_verified",
    "runtime_validated",
    "backend_roundtrip_valid",
    "backend",
    "fencing_token",
}
PHASE_MUTATION = {phase: phase == "commit" for phase in PHASES}
STATUSES = {"planned", "running", "failed", "completed", "rolled-back", "safe-mode"}
TOP_LEVEL_FIELDS = {
    "schema_version",
    "operation_id",
    "status",
    "phase",
    "context",
    "records",
}
RECORD_FIELDS = {"operation_id", "step_id", "phase", "outcome", "result", "error", "context"}
CONTEXT_FIELDS = ENVELOPE_FIELDS
_ROLLBACK_EVIDENCE_TOKEN = object()
_COMMIT_PHASE_EVIDENCE_FIELDS = frozenset(
    {
        "quiesced",
        "backup_verified",
        "selector_verified",
        "selector_commit_atomic",
        "fencing_verified",
        "selector_before_verified",
        "selector_after_verified",
        "admitted_snapshot",
        "current_snapshot",
    }
)
_BOUND_CAPABILITY_IDENTITY_FIELDS = tuple(
    field
    for field in CONTEXT_FIELDS
    if field not in {"target", "barrier_identity_digest", "envelope_digest"}
)


def backup_identity_digest(
    context: Mapping[str, object],
    *,
    backup_bytes_digest: str,
    manifest_digest: str,
    control_store_identity: str,
    control_store_revision: int,
) -> str:
    """Bind backup bytes, manifest, control state, and upgrade identity."""
    payload = {
        field: context[field]
        for field in (
            "backend",
            "project_id",
            "operation_id",
            "state_revision",
            "source",
            "destination",
            "manifest",
            "selector_ref",
            "barrier_identity_digest",
            "target",
        )
    }
    payload.update(
        backup_bytes_digest=backup_bytes_digest,
        manifest_digest=manifest_digest,
        control_store_identity=control_store_identity,
        control_store_revision=control_store_revision,
    )
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


@dataclass(frozen=True)
class PhaseContext:
    """Immutable identity and backend binding for one upgrade operation."""

    schema_version: int
    backend: str
    project_id: str
    operation_id: str
    state_revision: int
    authority_revision: str
    fencing_token: str
    fencing_owner: str
    durable_barrier_id: str
    artifact_root: str
    source: str
    destination: str
    manifest: str
    selector_ref: str
    barrier_identity_digest: str
    target: str
    envelope_digest: str


@dataclass(frozen=True)
class BoundRollbackCapability:
    """Typed, identity-bound evidence capability; never authorizes rollback."""

    identity: tuple[object, ...]
    verifier: Any
    scope: Any = None
    lease: Any = None
    admission_recheck: Any = None
    expected_branch: str | None = None
    expected_head: str | None = None
    backend_kind: str | None = None

    @classmethod
    def bind(
        cls,
        context: PhaseContext,
        verifier: Any,
        scope: Any = None,
        *,
        lease: Any = None,
        admission_recheck: Any = None,
        expected_branch: str | None = None,
        expected_head: str | None = None,
    ) -> BoundRollbackCapability:
        if not callable(getattr(verifier, "verify_rollback_context_bound", None)):
            raise UpgradeError("bound rollback verifier capability is incomplete")
        backend_kind = getattr(verifier, "bound_rollback_kind", None)
        concrete_backend = backend_kind in {"git", "sqlite"}
        if concrete_backend and (scope is None or lease is None or admission_recheck is None):
            raise UpgradeError("concrete rollback capability binding is incomplete")
        if expected_branch is not None and not isinstance(expected_branch, str):
            raise UpgradeError("Git rollback branch binding is invalid")
        if expected_head is not None and not isinstance(expected_head, str):
            raise UpgradeError("Git rollback head binding is invalid")
        return cls(
            tuple(asdict(context)[field] for field in _BOUND_CAPABILITY_IDENTITY_FIELDS),
            verifier,
            scope,
            lease,
            admission_recheck,
            expected_branch,
            expected_head,
            backend_kind,
        )

    def matches(self, context: PhaseContext) -> bool:
        values = asdict(context)
        return self.identity == tuple(values[field] for field in _BOUND_CAPABILITY_IDENTITY_FIELDS)

    def verify(self, context: Mapping[str, object]) -> Mapping[str, object]:
        """Invoke concrete bound verification, but never authorize rollback."""
        if set(context) != set(CONTEXT_FIELDS):
            raise UpgradeError("bound rollback capability context is incomplete")
        if self.backend_kind in {"git", "sqlite"}:
            try:
                validate_envelope(context)
            except UpgradeIdentityError as error:
                raise UpgradeError(
                    "bound rollback capability context identity is invalid"
                ) from error
        if self.identity != tuple(context[field] for field in _BOUND_CAPABILITY_IDENTITY_FIELDS):
            raise UpgradeError("bound rollback capability context identity mismatch")
        concrete_backend = self.backend_kind in {"git", "sqlite"}
        if concrete_backend:
            arguments: list[object] = [context, self.scope]
            keywords: dict[str, object] = {
                "lease": self.lease,
                "admission_recheck": self.admission_recheck,
            }
            if self.expected_branch is not None or self.expected_head is not None:
                if self.expected_branch is None or self.expected_head is None:
                    raise UpgradeError("Git rollback identity binding is incomplete")
                keywords.update(
                    expected_branch=self.expected_branch,
                    expected_head=self.expected_head,
                )
            result = self.verifier.verify_rollback_context_bound(*arguments, **keywords)
        else:
            result = self.verifier.verify_rollback_context_bound(context)
        if not isinstance(result, Mapping):
            raise UpgradeError("bound rollback verifier result is invalid")
        return {**dict(result), "rollback_context_verified": False}


@dataclass(frozen=True)
class RollbackAuthorizationRequest:
    """Immutable validated request; it carries no execution authority."""

    identity: tuple[object, ...]
    backup_identity_digest: str
    context: tuple[tuple[str, object], ...]
    evidence: tuple[tuple[str, object], ...]


@dataclass(frozen=True)
class RollbackBackupEvidence:
    """Typed evidence snapshot derived from observed backup/control inputs."""

    context: tuple[tuple[str, object], ...]
    backup_bytes_digest: str
    manifest_digest: str
    control_store_identity: str
    control_store_revision: int
    _token: object = dataclass_field(default=None, repr=False, compare=False)

    def __post_init__(self) -> None:
        if self._token is not _ROLLBACK_EVIDENCE_TOKEN:
            raise UpgradeError("rollback backup evidence requires trusted provenance")

    @classmethod
    def from_observations(
        cls,
        context: Mapping[str, object],
        backup_bytes: bytes,
        manifest: Mapping[str, object],
        control_store_identity: str,
        control_store_revision: int,
    ) -> RollbackBackupEvidence:
        if (
            not isinstance(context, Mapping)
            or set(context) != set(CONTEXT_FIELDS)
            or context.get("target") != "rollback"
        ):
            raise UpgradeError("rollback backup context is invalid")
        if not isinstance(backup_bytes, bytes) or not isinstance(manifest, Mapping):
            raise UpgradeError("rollback backup observations are invalid")
        if not isinstance(control_store_identity, str) or not control_store_identity:
            raise UpgradeError("rollback control-store identity is invalid")
        if type(control_store_revision) is not int or control_store_revision < 1:
            raise UpgradeError("rollback control-store revision is invalid")
        try:
            backup_digest = hashlib.sha256(backup_bytes).hexdigest()
            manifest_digest = hashlib.sha256(
                json.dumps(manifest, sort_keys=True, separators=(",", ":")).encode()
            ).hexdigest()
        except (TypeError, ValueError) as error:
            raise UpgradeError("rollback backup observations are not serializable") from error
        return cls(
            tuple((field, context[field]) for field in CONTEXT_FIELDS),
            backup_digest,
            manifest_digest,
            control_store_identity,
            control_store_revision,
            _ROLLBACK_EVIDENCE_TOKEN,
        )

    def as_mapping(self) -> dict[str, object]:
        context = dict(self.context)
        return context | {
            "phase": "rollback",
            "backend_identity_verified": True,
            "mutates_authority": False,
            "backup_verified": True,
            "restore_roundtrip_verified": True,
            "rollback_context_verified": False,
            "backup_bytes_digest": self.backup_bytes_digest,
            "manifest_digest": self.manifest_digest,
            "control_store_identity": self.control_store_identity,
            "control_store_revision": self.control_store_revision,
            "backup_identity_digest": backup_identity_digest(
                context,
                backup_bytes_digest=self.backup_bytes_digest,
                manifest_digest=self.manifest_digest,
                control_store_identity=self.control_store_identity,
                control_store_revision=self.control_store_revision,
            ),
        }


@dataclass(frozen=True)
class RollbackAuthorizationCapability:
    """Typed placeholder for future rollback authorization.

    This contract validates that an authorization request is tied to the same
    bound evidence identity, but deliberately never authorizes or dispatches a
    rollback.  A future implementation must replace the explicit refusal only
    after the execution and formal contracts are independently complete.
    """

    identity: tuple[object, ...]
    evidence_capability: BoundRollbackCapability

    @classmethod
    def bind(
        cls, context: PhaseContext, evidence_capability: BoundRollbackCapability
    ) -> RollbackAuthorizationCapability:
        if not isinstance(evidence_capability, BoundRollbackCapability):
            raise UpgradeError("rollback authorization requires bound evidence")
        if not evidence_capability.matches(context):
            raise UpgradeError("rollback authorization identity mismatch")
        fields = tuple(field for field in CONTEXT_FIELDS if field != "target")
        return cls(tuple(asdict(context)[field] for field in fields), evidence_capability)

    def validate(  # noqa: C901
        self, context: Mapping[str, object], evidence: Mapping[str, object] | RollbackBackupEvidence
    ) -> RollbackAuthorizationRequest:
        if isinstance(evidence, RollbackBackupEvidence):
            evidence = evidence.as_mapping()
        if not isinstance(context, Mapping) or not isinstance(evidence, Mapping):
            raise UpgradeError("rollback authorization context or evidence is invalid")
        if set(context) != set(CONTEXT_FIELDS) or context.get("target") != "rollback":
            raise UpgradeError("rollback authorization context is invalid")
        fields = tuple(field for field in CONTEXT_FIELDS if field != "target")
        if self.identity != tuple(context[field] for field in fields):
            raise UpgradeError("rollback authorization identity mismatch")
        allowed = set(CONTEXT_FIELDS) | {
            "phase",
            "backend_identity_verified",
            "mutates_authority",
            "rollback_context_verified",
            "backup_verified",
            "restore_roundtrip_verified",
            "git_head",
            "git_branch",
            "git_clean",
            "sqlite_integrity_verified",
            "sqlite_foreign_keys_verified",
            "backup_identity_digest",
            "backup_bytes_digest",
            "manifest_digest",
            "control_store_identity",
            "control_store_revision",
        }
        required = set(CONTEXT_FIELDS) | {
            "phase",
            "backend_identity_verified",
            "mutates_authority",
            "rollback_context_verified",
            "backup_verified",
            "restore_roundtrip_verified",
            "backup_identity_digest",
            "backup_bytes_digest",
            "manifest_digest",
            "control_store_identity",
            "control_store_revision",
        }
        if set(evidence) - allowed or not required.issubset(evidence):
            raise UpgradeError("rollback authorization evidence schema is invalid")
        if any(
            evidence.get(field) != context[field]
            or type(evidence.get(field)) is not type(context[field])
            for field in CONTEXT_FIELDS
        ):
            raise UpgradeError("rollback authorization evidence identity mismatch")
        if evidence.get("phase") != "rollback" or evidence.get("backend") != context["backend"]:
            raise UpgradeError("rollback authorization evidence phase or backend is invalid")
        if evidence.get("backend_identity_verified") is not True:
            raise UpgradeError("rollback authorization evidence identity is unverified")
        if evidence.get("mutates_authority") is not False:
            raise UpgradeError("rollback authorization evidence is mutating")
        if (
            type(evidence.get("backup_identity_digest")) is not str
            or type(evidence.get("backup_bytes_digest")) is not str
            or type(evidence.get("manifest_digest")) is not str
            or type(evidence.get("control_store_identity")) is not str
            or type(evidence.get("control_store_revision")) is not int
            or evidence.get("control_store_revision") != context["state_revision"]
            or evidence.get("backup_identity_digest")
            != backup_identity_digest(
                context,
                backup_bytes_digest=cast(str, evidence["backup_bytes_digest"]),
                manifest_digest=cast(str, evidence["manifest_digest"]),
                control_store_identity=cast(str, evidence["control_store_identity"]),
                control_store_revision=cast(int, evidence["control_store_revision"]),
            )
        ):
            raise UpgradeError("rollback authorization backup identity is invalid")
        if (
            evidence.get("backup_verified") is not True
            or evidence.get("restore_roundtrip_verified") is not True
        ):
            raise UpgradeError("rollback authorization evidence lacks backup or restore proof")
        if evidence.get("rollback_context_verified") is not False:
            raise UpgradeError("rollback authorization evidence is not diagnostic-only")
        return RollbackAuthorizationRequest(
            self.identity,
            cast(str, evidence["backup_identity_digest"]),
            tuple((field, context[field]) for field in CONTEXT_FIELDS),
            tuple((field, evidence[field]) for field in sorted(evidence)),
        )

    def authorize(self, context: Mapping[str, object], evidence: object) -> None:
        """Validate trusted typed evidence, then refuse until rollback is enabled."""
        if not isinstance(evidence, RollbackBackupEvidence):
            raise UpgradeError("rollback authorization requires typed evidence")
        self.validate(context, evidence)
        raise UpgradeError("rollback authorization is not enabled")

    def preflight(
        self,
        context: Mapping[str, object],
        provider: object,
    ) -> None:
        """Validate adapter-owned backup/CAS evidence without authorizing rollback."""
        if not isinstance(
            provider, (SQLiteRollbackObservationCapability, GitRollbackObservationCapability)
        ):
            raise UpgradeError("rollback preflight requires a bound observation provider")
        if provider.adapter is not self.evidence_capability.verifier:
            raise UpgradeError("rollback preflight provider is bound to a foreign adapter")
        if not isinstance(context, Mapping) or context.get("target") != "rollback":
            raise UpgradeError("rollback preflight context is invalid")
        identity_fields = tuple(field for field in CONTEXT_FIELDS if field != "target")
        if self.identity != tuple(context.get(field) for field in identity_fields):
            raise UpgradeError("rollback preflight context identity mismatch")
        try:
            observation = provider.observe(context)
        except Exception as error:
            raise UpgradeError("rollback preflight observation failed") from error
        if not observation.has_provenance:
            raise UpgradeError("rollback preflight observation provenance is invalid")
        raise UpgradeError("rollback authorization is not enabled")


def _freeze(value: object) -> object:
    """Create a recursively immutable view for untrusted phase handlers."""
    if isinstance(value, Mapping):
        return MappingProxyType({key: _freeze(item) for key, item in value.items()})
    if isinstance(value, (list, tuple)):
        return tuple(_freeze(item) for item in value)
    return value


def _thaw(value: object) -> object:
    """Return a detached JSON-compatible copy of an immutable snapshot value."""
    if isinstance(value, Mapping):
        return {key: _thaw(item) for key, item in value.items()}
    if isinstance(value, tuple):
        return [_thaw(item) for item in value]
    return value


def _write(path: Path, value: Mapping[str, Any]) -> None:
    path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temporary = Path(name)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            json.dump(value, stream, indent=2, sort_keys=True)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        temporary.replace(path)
        directory = os.open(path.parent, os.O_DIRECTORY)
        try:
            os.fsync(directory)
        finally:
            os.close(directory)
    except OSError as error:
        try:
            temporary.unlink(missing_ok=True)
        except OSError as cleanup_error:
            raise UpgradeError("durable upgrade journal cleanup failed") from cleanup_error
        raise UpgradeError("durable upgrade journal write failed") from error


def _validate_context_identities(supplied: dict[str, object]) -> None:
    try:
        validate_envelope(supplied)
    except UpgradeIdentityError as error:
        raise UpgradeError("invalid phase context identity envelope") from error
    operation_id = cast(str, supplied["operation_id"])
    if len(operation_id) > MAX_OPERATION_ID_LENGTH:
        raise UpgradeError("invalid operation_id")


def _validate_context(supplied: dict[str, object], operation_id: str) -> None:
    if set(supplied) != set(CONTEXT_FIELDS) or supplied.get("operation_id") != operation_id:
        raise UpgradeError("complete bound phase context is required")
    _validate_context_identities(supplied)


class UpgradeEngine:
    """Execute exactly eight ordered phases with durable outcomes."""

    def __init__(  # noqa: C901
        self,
        operation_id: str,
        journal: Path,
        context: Mapping[str, object],
        lock_path: Path | None = None,
        backend_adapter: BackendAdapter | None = None,
        rollback_bound_verifier: BoundRollbackCapability | None = None,
        backup_operation: Mapping[str, object] | None = None,
        backup_context: Mapping[str, object] | None = None,
        stage_operation: Mapping[str, object] | None = None,
        stage_context: Mapping[str, object] | None = None,
        validation_admission: object | None = None,
        validation_operation: Mapping[str, object] | None = None,
        validation_context: Mapping[str, object] | None = None,
        commit_operation: Mapping[str, object] | None = None,
        commit_context: Mapping[str, object] | None = None,
        commit_executor: object | None = None,
        commit_argument: object | None = None,
        commit_evidence: Mapping[str, object] | None = None,
        rollback_operation: Mapping[str, object] | None = None,
        rollback_context: Mapping[str, object] | None = None,
        rollback_executor: object | None = None,
        rollback_argument: object | None = None,
        rollback_evidence: Mapping[str, object] | None = None,
    ) -> None:
        if not operation_id or ":" in operation_id:
            raise UpgradeError("invalid operation identity")
        self.operation_id = operation_id
        self.journal = journal
        self.lock_path = lock_path or journal.parent / ".upgrade-engine.lock"
        self.backend_adapter = backend_adapter
        self.rollback_bound_verifier = rollback_bound_verifier
        rollback_parts = (
            rollback_operation,
            rollback_context,
            rollback_executor,
            rollback_argument,
            rollback_evidence,
        )
        rollback_count = sum(value is not None for value in rollback_parts)
        if rollback_count not in (0, len(rollback_parts)):
            raise UpgradeError(
                "rollback operation, context, executor, argument, and "
                "evidence are required together"
            )
        self._rollback_phase_adapter: BoundRollbackPhaseAdapter | None = None
        if rollback_count == len(rollback_parts):  # pragma: no cover - isolated internal seam
            if (
                backend_adapter is None
                or rollback_context is None
                or rollback_operation is None
                or rollback_executor is None
            ):
                raise UpgradeError("rollback capability requires a backend adapter")
            try:
                self._rollback_phase_adapter = BoundRollbackPhaseAdapter(
                    rollback_operation,
                    rollback_context,
                    cast(Any, rollback_executor),
                    rollback_argument,
                )
            except Exception as error:
                raise UpgradeError("rollback capability binding is invalid") from error
        if (backup_operation is None) != (backup_context is None):
            raise UpgradeError("backup operation and context must be supplied together")
        self._backup_phase_adapter: BoundBackupPhaseAdapter | None = None
        if backup_operation is not None and backup_context is not None:
            if backend_adapter is None:
                raise UpgradeError("backup capability requires a backend adapter")
            try:
                self._backup_phase_adapter = BoundBackupPhaseAdapter(
                    backend_adapter, backup_operation, backup_context
                )
            except Exception as error:
                raise UpgradeError("backup capability binding is invalid") from error
        if (stage_operation is None) != (stage_context is None):
            raise UpgradeError("stage operation and context must be supplied together")
        self._stage_phase_adapter: BoundStagePhaseAdapter | None = None
        if stage_operation is not None and stage_context is not None:
            if backend_adapter is None:
                raise UpgradeError("stage capability requires a backend adapter")
            try:
                self._stage_phase_adapter = BoundStagePhaseAdapter(
                    backend_adapter, stage_operation, stage_context
                )
            except Exception as error:
                raise UpgradeError("stage capability binding is invalid") from error
        validation_parts = (validation_admission, validation_operation, validation_context)
        validation_count = sum(value is not None for value in validation_parts)
        if validation_count not in (0, 3):
            raise UpgradeError("validation admission, operation, and context are required together")
        self._validation_phase_adapter: BoundValidationPhaseAdapter | None = None
        if validation_count == 3:
            if backend_adapter is None:
                raise UpgradeError("validation capability requires a backend adapter")
            try:
                self._validation_phase_adapter = BoundValidationPhaseAdapter(
                    backend_adapter,
                    cast(DispatchAdmission, validation_admission),
                    cast(Mapping[str, object], validation_operation),
                    cast(Mapping[str, object], validation_context),
                )
            except Exception as error:
                raise UpgradeError("validation capability binding is invalid") from error
        commit_parts = (
            commit_operation,
            commit_context,
            commit_executor,
            commit_argument,
            commit_evidence,
        )
        commit_count = sum(value is not None for value in commit_parts)
        if commit_count not in (0, len(commit_parts)):
            raise UpgradeError(
                "commit operation, context, executor, argument, and evidence are required together"
            )
        self._commit_phase_adapter: BoundCommitPhaseAdapter | None = None
        self._commit_operation: Mapping[str, object] | None = None
        self._commit_phase_evidence: dict[str, object] = {}
        if commit_count == len(commit_parts):
            if backend_adapter is None:
                raise UpgradeError("commit capability requires a backend adapter")
            if (
                not isinstance(commit_operation, Mapping)
                or commit_operation.get("operation_id") != f"{operation_id}:commit"
            ):
                raise UpgradeError("commit capability operation identity mismatch")
            if (
                not isinstance(commit_evidence, Mapping)
                or set(commit_evidence) != _COMMIT_PHASE_EVIDENCE_FIELDS
            ):
                raise UpgradeError("commit capability evidence is incomplete or unknown")
            for field in _COMMIT_PHASE_EVIDENCE_FIELDS - {"admitted_snapshot", "current_snapshot"}:
                if commit_evidence.get(field) is not True:
                    raise UpgradeError("commit capability evidence is not verified")
            for field in ("admitted_snapshot", "current_snapshot"):
                if not isinstance(commit_evidence.get(field), Mapping):
                    raise UpgradeError("commit capability admission snapshots are invalid")
            try:
                self._commit_operation = dict(commit_operation)
                self._commit_phase_adapter = BoundCommitPhaseAdapter(
                    commit_operation,
                    cast(Mapping[str, object], commit_context),
                    cast(Any, commit_executor),
                    commit_argument,
                )
            except Exception as error:
                raise UpgradeError("commit capability binding is invalid") from error
            self._commit_phase_evidence = deepcopy(dict(commit_evidence))
        self._verified_rollback_context: dict[str, object] | None = None
        supplied = dict(context)
        _validate_context(supplied, operation_id)
        self.context = PhaseContext(**cast(dict[str, Any], supplied))
        if self._commit_phase_adapter is not None:
            for field in ("admitted_snapshot", "current_snapshot"):
                snapshot = self._commit_phase_evidence[field]
                self._bind_snapshot(cast(Mapping[str, object], snapshot))
            try:
                self._admit("commit", self._commit_phase_evidence)
            except Exception as error:
                raise UpgradeError("commit capability admission evidence is invalid") from error
        if rollback_bound_verifier is not None and not isinstance(
            rollback_bound_verifier, BoundRollbackCapability
        ):
            raise UpgradeError("trusted bound rollback capability is required")
        if isinstance(rollback_bound_verifier, BoundRollbackCapability):
            if not rollback_bound_verifier.matches(self.context):
                raise UpgradeError("trusted bound rollback capability identity mismatch")
            if rollback_bound_verifier.verifier is not self.backend_adapter:
                raise UpgradeError("trusted bound rollback capability backend mismatch")

    @contextmanager
    def _exclusive(self) -> Iterator[None]:
        """Serialize journal decisions and fail closed if locking is unavailable."""
        if fcntl is None:
            raise UpgradeError("upgrade lock is unavailable")
        lock = self.lock_path
        lock.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
        with lock.open("a+") as stream:
            try:
                deadline = time.monotonic() + 30
                while True:
                    try:
                        fcntl.flock(stream.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
                        break
                    except BlockingIOError:
                        if time.monotonic() >= deadline:
                            raise UpgradeError("upgrade lock acquisition timed out") from None
                        time.sleep(0.01)
            except OSError as error:
                raise UpgradeError("upgrade lock acquisition failed") from error
            try:
                yield
            finally:
                fcntl.flock(stream.fileno(), fcntl.LOCK_UN)

    def check(self) -> dict[str, object]:
        return {"operation_id": self.operation_id, "phases": list(PHASES), "checked": True}

    def plan(self) -> dict[str, Any]:
        with self._exclusive():
            if self.journal.exists():
                raise UpgradeError("operation already planned")
            value: dict[str, Any] = {
                "schema_version": JOURNAL_SCHEMA_VERSION,
                "operation_id": self.operation_id,
                "status": "planned",
                "phase": None,
                "context": asdict(self.context),
                "records": [],
            }
            _write(self.journal, value)
            return value

    def _load(self) -> dict[str, Any]:  # noqa: C901
        try:
            value = json.loads(self.journal.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error:
            raise UpgradeError("upgrade journal is unreadable") from error
        if isinstance(value, dict) and value.get("schema_version") == 2:
            raise UpgradeError(
                "upgrade journal schema v2 requires recovery with its originating runtime"
            )
        if (
            value.get("schema_version") != JOURNAL_SCHEMA_VERSION
            or set(value) != TOP_LEVEL_FIELDS
            or value.get("operation_id") != self.operation_id
            or value.get("status") not in STATUSES
        ):
            raise UpgradeError("upgrade journal identity or records are invalid")
        context = value.get("context")
        if not isinstance(context, dict) or context != asdict(self.context):
            raise UpgradeError("upgrade journal context is invalid or changed")
        records = value.get("records")
        if not isinstance(records, list):
            raise UpgradeError("upgrade journal records are invalid")
        expected = 0
        phase_outcomes: list[str] = []
        rollback_seen = False
        for record in records:
            if not isinstance(record, dict):
                raise UpgradeError("upgrade journal record is invalid")
            phase = record.get("phase")
            if phase == "rollback":
                if rollback_seen:
                    raise UpgradeError("duplicate rollback record")
                rollback_seen = True
                if (
                    record.get("operation_id") != self.operation_id
                    or record.get("step_id") != f"{self.operation_id}.rollback"
                ):
                    raise UpgradeError("upgrade journal rollback identity is invalid")
                if record.get("outcome") not in {
                    "started",
                    "rollback_verified",
                    "rollback_completed",
                    "ambiguous",
                }:
                    raise UpgradeError("upgrade journal rollback outcome is invalid")
                rollback_context = record.get("context")
                if not isinstance(rollback_context, dict):
                    raise UpgradeError("verified rollback context is required")
                rollback_context = dict(rollback_context)
                _validate_context(rollback_context, self.operation_id)
                if rollback_context["target"] != "rollback":
                    raise UpgradeError("rollback context target is invalid")
                for field in CONTEXT_FIELDS:
                    if field not in {"target", "barrier_identity_digest", "envelope_digest"} and (
                        rollback_context[field] != asdict(self.context)[field]
                    ):
                        raise UpgradeError(f"rollback context mismatch: {field}")
                verifier = getattr(self.backend_adapter, "verify_rollback_context", None)
                try:
                    durable = (
                        verifier(cast(Mapping[str, object], _freeze(rollback_context)))
                        if callable(verifier)
                        else None
                    )
                except Exception as error:
                    raise UpgradeError("rollback authority verification failed") from error
                if not isinstance(durable, Mapping) or any(
                    durable.get(field) != rollback_context[field] for field in CONTEXT_FIELDS
                ):
                    raise UpgradeError("rollback context is not verified by authority")
                if set(record) - RECORD_FIELDS:
                    raise UpgradeError("upgrade journal rollback context is invalid")
                outcome = record["outcome"]
                expected_fields = {
                    "started": {"operation_id", "step_id", "phase", "outcome", "context"},
                    "rollback_completed": {
                        "operation_id",
                        "step_id",
                        "phase",
                        "outcome",
                        "context",
                        "result",
                    },
                    "rollback_verified": {
                        "operation_id",
                        "step_id",
                        "phase",
                        "outcome",
                        "context",
                        "result",
                    },
                    "ambiguous": {
                        "operation_id",
                        "step_id",
                        "phase",
                        "outcome",
                        "context",
                        "error",
                    },
                }[outcome]
                if set(record) != expected_fields:
                    raise UpgradeError("rollback record fields are invalid")
                if outcome in {"rollback_verified", "rollback_completed"} and not isinstance(
                    record["result"], dict
                ):
                    raise UpgradeError("verified rollback lacks result evidence")
                if outcome == "ambiguous" and not isinstance(record["error"], str):
                    raise UpgradeError("ambiguous rollback lacks error evidence")
                continue
            if phase is not None:
                if rollback_seen:
                    raise UpgradeError("phase follows rollback record")
                if (
                    expected >= len(PHASES)
                    or phase != PHASES[expected]
                    or record.get("operation_id") != self.operation_id
                    or record.get("step_id") != f"{self.operation_id}.{phase}"
                ):
                    raise UpgradeError("upgrade journal phase identity is invalid")
                if (  # pragma: no cover - phase identity validation already fixes this value
                    not isinstance(record.get("step_id"), str) or len(record["step_id"]) > 128
                ):
                    raise UpgradeError("upgrade journal step identity is invalid")
                if record.get("outcome") not in {"started", "success", "failed", "ambiguous"}:
                    raise UpgradeError("upgrade journal outcome is invalid")
                if set(record) - RECORD_FIELDS or record.get("context") != asdict(self.context):
                    raise UpgradeError("upgrade journal record fields are invalid")
                outcome = record["outcome"]
                expected_fields = {
                    "started": {"operation_id", "step_id", "phase", "outcome", "context"},
                    "success": {"operation_id", "step_id", "phase", "outcome", "context", "result"},
                    "failed": {"operation_id", "step_id", "phase", "outcome", "context", "error"},
                    "ambiguous": {
                        "operation_id",
                        "step_id",
                        "phase",
                        "outcome",
                        "context",
                        "error",
                    },
                }[outcome]
                if set(record) != expected_fields:
                    raise UpgradeError("phase outcome fields are invalid")
                if outcome == "success" and not isinstance(record.get("result"), dict):
                    raise UpgradeError("successful phase lacks result evidence")
                if outcome in {"failed", "ambiguous"} and not isinstance(record.get("error"), str):
                    raise UpgradeError("failed phase lacks error evidence")
                if outcome == "started" and set(record) != {  # pragma: no cover
                    "operation_id",
                    "step_id",
                    "phase",
                    "outcome",
                    "context",
                }:
                    raise UpgradeError("started phase has terminal evidence")
                phase_outcomes.append(cast(str, record["outcome"]))
                expected += 1
            else:
                raise UpgradeError("upgrade journal record phase is missing")
        status = cast(str, value["status"])
        if status == "planned" and records:
            raise UpgradeError("planned journal contains records")
        if status == "planned" and value.get("phase") is not None:
            raise UpgradeError("planned journal has an active phase")
        if status == "running" and (
            not phase_outcomes or phase_outcomes[-1] not in {"started", "success"}
        ):
            raise UpgradeError("running journal is not recoverable")
        if status == "running" and value.get("phase") != PHASES[len(phase_outcomes) - 1]:
            raise UpgradeError("running journal phase is inconsistent")
        if status in {"failed", "safe-mode"} and not phase_outcomes:
            raise UpgradeError("failed journal has no failed phase")
        rollback_records = [record for record in records if record.get("phase") == "rollback"]
        rollback_completed = [
            record for record in rollback_records if record.get("outcome") == "rollback_completed"
        ]
        rollback_verified = [
            record for record in rollback_records if record.get("outcome") == "rollback_verified"
        ]
        for rollback_record in (*rollback_verified, *rollback_completed):
            result = rollback_record.get("result")
            if (
                not isinstance(result, dict)
                or set(result) != ROLLBACK_RESULT_FIELDS
                or any(
                    result.get(field) is not True
                    for field in (
                        "restored_verified",
                        "runtime_validated",
                        "backend_roundtrip_valid",
                    )
                )
                or result.get("backend") != self.context.backend
                or result.get("fencing_token") != rollback_record["context"]["fencing_token"]
            ):
                raise UpgradeError("rollback result schema is invalid")
        if status == "completed" and (
            phase_outcomes != ["success"] * len(PHASES) or rollback_records
        ):
            raise UpgradeError("completed journal is incomplete")
        if status in {"failed", "safe-mode"} and rollback_completed:
            raise UpgradeError("failed journal has rollback completion")
        if status == "safe-mode" and rollback_verified:
            raise UpgradeError("safe-mode journal cannot discard verified rollback recovery")
        if status == "rolled-back" and (
            len(rollback_completed) != 1
            or not isinstance(rollback_completed[0].get("result"), dict)
            or any(
                rollback_completed[0]["result"].get(field) is not True
                for field in ("restored_verified", "runtime_validated", "backend_roundtrip_valid")
            )
        ):
            raise UpgradeError("rolled-back journal lacks rollback completion")
        if status == "rolled-back":
            result = rollback_completed[0]["result"]
            revalidate = getattr(self.backend_adapter, "revalidate_rollback", None)
            if not callable(revalidate):
                raise UpgradeError("rollback revalidation is unavailable")
            try:
                evidence = revalidate(
                    cast(Mapping[str, object], _freeze(rollback_completed[0]["context"])),
                    cast(Mapping[str, object], _freeze(result)),
                )
            except Exception as error:
                raise UpgradeError("rollback revalidation failed") from error
            if not isinstance(evidence, Mapping) or any(
                evidence.get(field) is not True
                for field in (
                    "restored_verified",
                    "runtime_validated",
                    "backend_roundtrip_valid",
                )
            ):
                raise UpgradeError("rollback runtime is not revalidated")
        if status == "rolled-back" and value.get("phase") != "rollback":
            raise UpgradeError("rolled-back journal phase is inconsistent")
        return cast(dict[str, Any], value)

    @staticmethod
    def _admit(phase: str, result: Mapping[str, Any]) -> None:
        """Execute the coordinator-native admission contract, not just booleans."""
        if phase == "preflight":
            snapshot = result.get("preflight_snapshot", result)
            if not isinstance(snapshot, Mapping):
                raise UpgradeError("preflight admission snapshot is absent")
            admit_preflight(snapshot)
        elif phase == "quiesce":
            snapshot = result.get("quiescence_snapshot", result)
            if not isinstance(snapshot, Mapping):
                raise UpgradeError("quiescence admission snapshot is absent")
            admit_quiesced(snapshot)
        elif phase == "commit":
            admitted = result.get("admitted_snapshot", result)
            current = result.get("current_snapshot", result)
            if not isinstance(admitted, Mapping) or not isinstance(current, Mapping):
                raise UpgradeError("replacement admission snapshots are absent")
            recheck_before_replacement(admitted, current)
        elif phase == "reopen":
            snapshot = result.get("reopen_snapshot", result)
            if not isinstance(snapshot, Mapping):
                raise UpgradeError("reopen admission snapshot is absent")
            admit_reopen(snapshot)

    def _bind_snapshot(self, snapshot: Mapping[str, object]) -> None:
        expected = asdict(self.context)
        for field in CONTEXT_FIELDS:
            if snapshot.get(field) != expected[field]:
                raise UpgradeError(f"admission snapshot identity mismatch: {field}")

    def _rollback_context(self) -> dict[str, object]:
        """Derive the canonical rollback child from the current engine context."""
        context = {**asdict(self.context), "target": "rollback"}
        context["barrier_identity_digest"] = canonical_barrier_digest(context)
        context["envelope_digest"] = canonical_envelope_digest(context)
        return context

    def _operation_scope(self) -> AbstractContextManager[None]:
        operation_lock = getattr(self.backend_adapter, "operation_lock", None)
        if callable(operation_lock):
            return cast(AbstractContextManager[None], operation_lock())
        return nullcontext()

    def apply(self, handlers: Mapping[str, Handler]) -> dict[str, Any]:
        with self._operation_scope(), self._exclusive():
            return self._apply_locked(handlers)

    def _apply_locked(self, handlers: Mapping[str, Handler]) -> dict[str, Any]:  # noqa: C901
        value = self._load()
        if value["status"] == "completed":
            return value
        if value["status"] in {"failed", "safe-mode", "rolled-back"}:
            raise UpgradeError("journal requires explicit recovery before apply")
        if self.backend_adapter is None:
            raise UpgradeError("backend adapter is required for authoritative upgrade")
        records: list[dict[str, Any]] = value["records"]
        phase_records = [r.get("phase") for r in records if "phase" in r]
        if (  # pragma: no cover - journal loader enforces ordering
            phase_records != list(dict.fromkeys(phase_records))
            or phase_records != list(dict.fromkeys(PHASES[: len(phase_records)]))
        ):
            raise UpgradeError("upgrade journal phase ordering is invalid")
        completed = {r["phase"] for r in records if r.get("outcome") == "success" and "phase" in r}
        if value["status"] == "running" and records and records[-1].get("outcome") == "started":
            raise UpgradeError("started phase requires explicit recovery")
        for phase in PHASES:
            if phase in completed:
                continue
            if phase not in handlers:
                raise UpgradeError(f"missing phase handler: {phase}")
            operation = self.operation_id
            step_id = f"{self.operation_id}.{phase}"
            record: dict[str, Any] = {
                "operation_id": operation,
                "step_id": step_id,
                "phase": phase,
                "outcome": "started",
                "context": asdict(self.context),
            }
            records.append(record)
            value["status"] = "running"
            value["phase"] = phase
            _write(self.journal, value)
            try:
                frozen_context = cast(Mapping[str, object], _freeze(asdict(self.context)))
                snapshot = self.backend_adapter.snapshot(phase, frozen_context)
                self._bind_snapshot(snapshot)
                self._admit(phase, {**snapshot})
                phase_adapters = {
                    "backup": self._backup_phase_adapter,
                    "stage": self._stage_phase_adapter,
                    "commit": self._commit_phase_adapter,
                    "validate": self._validation_phase_adapter,
                }
                executor = phase_adapters.get(phase) or self.backend_adapter
                if executor is None:  # pragma: no cover - backend checked before dispatch
                    raise UpgradeError("backend adapter is required for authoritative upgrade")
                dispatch_context = frozen_context
                if phase == "commit" and self._commit_phase_adapter is not None:
                    # The generated effect is a phase step (``operation:commit``),
                    # while the durable journal context names the parent
                    # operation.  Keep the parent context immutable and project
                    # only the step identity to the already-bound capability.
                    commit_operation_id = (
                        self._commit_operation.get("operation_id")
                        if self._commit_operation is not None
                        else None
                    )
                    if not isinstance(commit_operation_id, str):  # pragma: no cover
                        raise UpgradeError("commit operation identity is unavailable")
                    dispatch_context = cast(
                        Mapping[str, object],
                        _freeze({**dict(frozen_context), "operation_id": commit_operation_id}),
                    )
                adapter_result = executor.execute(phase, dispatch_context)
                if phase == "commit":
                    refresh = getattr(self.backend_adapter, "refresh_after_commit", None)
                    if callable(refresh):
                        try:
                            refresh()
                        except Exception as error:
                            raise CommitDispatchError(
                                "post-commit identity refresh is ambiguous"
                            ) from error
                result = dict(adapter_result)
                if phase == "commit" and self._commit_phase_adapter is not None:
                    result.update(self._commit_phase_evidence)
                handler_result = (
                    handlers[phase](step_id, cast(Mapping[str, Any], _freeze(value))) or {}
                )
                for key in set(result).intersection(handler_result):
                    if result[key] != handler_result[key]:
                        raise UpgradeError("handler cannot override backend evidence")
                result.update(handler_result)
                self._load()
            except (AuthorityMutationAmbiguousError, CommitDispatchError) as error:
                record.update(outcome="ambiguous", error=type(error).__name__)
                value["status"] = "safe-mode"
                _write(self.journal, value)
                raise UpgradeError(f"phase outcome is ambiguous: {phase}") from error
            except Exception as error:
                record.update(outcome="failed", error=type(error).__name__)
                value["status"] = "failed"
                _write(self.journal, value)
                raise UpgradeError(f"phase failed: {phase}") from error
            required = REQUIRED_EVIDENCE.get(phase, ())
            if (
                any(
                    type(result.get(field)) is not bool or result.get(field) is not True
                    for field in required
                )
                or type(result.get("mutates_authority")) is not bool
                or result.get("mutates_authority") is not PHASE_MUTATION[phase]
            ):
                record["outcome"] = "failed"
                record["error"] = "required evidence missing"
                value["status"] = "failed"
                _write(self.journal, value)
                raise UpgradeError(f"phase evidence incomplete: {phase}")
            if result.get("backend") != self.context.backend:
                record.update(outcome="failed", error="backend identity mismatch")
                value["status"] = "failed"
                _write(self.journal, value)
                raise UpgradeError(f"phase backend mismatch: {phase}")
            try:
                self._admit(phase, result)
            except Exception as error:
                record.update(outcome="failed", error=type(error).__name__)
                value["status"] = "failed"
                _write(self.journal, value)
                raise UpgradeError(f"phase admission denied: {phase}") from error
            if (
                phase in {"quiesce", "backup", "stage", "commit", "validate", "reopen"}
                and result.get("fencing_token") != self.context.fencing_token
            ):
                record.update(outcome="failed", error="fencing token mismatch")
                value["status"] = "failed"
                _write(self.journal, value)
                raise UpgradeError(f"phase fencing mismatch: {phase}")
            if result.get("ambiguous") is True:
                record.update(outcome="ambiguous", error="external outcome is ambiguous")
                value["status"] = "safe-mode"
                _write(self.journal, value)
                raise UpgradeError(f"phase outcome is ambiguous: {phase}")
            record["outcome"] = "success"
            record["result"] = dict(result)
            _write(self.journal, value)
        value["status"] = "completed"
        _write(self.journal, value)
        return value

    def rollback(self, handler: Handler) -> dict[str, Any]:  # noqa: C901
        with self._operation_scope(), self._exclusive():
            if self._rollback_phase_adapter is not None:  # pragma: no cover - public guard
                raise UpgradeError("public rollback dispatch is disabled")
            if self.backend_adapter is None:
                raise UpgradeError("backend adapter is required for rollback")
            snapshot: Mapping[str, object]
            if getattr(self.backend_adapter, "requires_bound_rollback", False):
                # Concrete authority adapters must be supplied through a caller-owned
                # scope/lease binding.  Do not fall back to their unbound snapshot.
                if not isinstance(self.rollback_bound_verifier, BoundRollbackCapability):
                    raise UpgradeError("rollback requires a trusted bound backend capability")
                rollback_context = self._rollback_context()
                try:
                    snapshot = dict(
                        self.rollback_bound_verifier.verify(
                            cast(Mapping[str, object], _freeze(rollback_context))
                        )
                    )
                except Exception as error:
                    raise UpgradeError("trusted bound rollback verification failed") from error
            else:
                snapshot = self.backend_adapter.snapshot(
                    "rollback", cast(Mapping[str, object], _freeze(asdict(self.context)))
                )
            if snapshot.get("rollback_context_verified") is not True:
                raise UpgradeError("backend did not verify rollback context")
            supplied = {field: snapshot.get(field) for field in CONTEXT_FIELDS}
            _validate_context(supplied, self.operation_id)
            if supplied["target"] != "rollback":
                raise UpgradeError("rollback context target is invalid")
            for field in CONTEXT_FIELDS:
                if (
                    field not in {"target", "barrier_identity_digest", "envelope_digest"}
                    and supplied[field] != asdict(self.context)[field]
                ):
                    raise UpgradeError(f"rollback context mismatch: {field}")
            verifier = getattr(self.backend_adapter, "verify_rollback_context", None)
            try:
                durable = (
                    verifier(cast(Mapping[str, object], _freeze(supplied)))
                    if callable(verifier)
                    else None
                )
            except Exception as error:
                raise UpgradeError("rollback authority verification failed") from error
            if not isinstance(durable, Mapping) or any(
                durable.get(field) != supplied[field] for field in CONTEXT_FIELDS
            ):
                raise UpgradeError("rollback context is not verified by authority")
            self._verified_rollback_context = supplied
            return self._rollback_locked(handler)

    def inspect_rollback_bound(self) -> dict[str, object]:
        """Return bound rollback evidence without authorizing or journaling rollback.

        This is intentionally separate from :meth:`rollback`: it acquires the
        same coordination locks and invokes only the typed capability.  The
        capability's non-authorizing result is preserved, and no handler,
        journal transition, or backend mutation can be reached.
        """
        with self._operation_scope(), self._exclusive():
            if self.backend_adapter is None:
                raise UpgradeError("backend adapter is required for rollback inspection")
            if not getattr(self.backend_adapter, "requires_bound_rollback", False):
                raise UpgradeError("rollback inspection requires a bound backend capability")
            if not isinstance(self.rollback_bound_verifier, BoundRollbackCapability):
                raise UpgradeError("rollback inspection requires a trusted bound capability")
            context = cast(
                Mapping[str, object],
                _freeze(self._rollback_context()),
            )
            try:
                result: Mapping[str, object]
                if (
                    self.rollback_bound_verifier.backend_kind == "git"
                    and self.rollback_bound_verifier.verifier is self.backend_adapter
                    and callable(getattr(self.backend_adapter, "preflight_git", None))
                    and self.rollback_bound_verifier.expected_branch is not None
                    and self.rollback_bound_verifier.expected_head is not None
                ):
                    observation = self.backend_adapter.preflight_git(
                        context,
                        self.rollback_bound_verifier.scope,
                        lease=self.rollback_bound_verifier.lease,
                        admission_recheck=self.rollback_bound_verifier.admission_recheck,
                        expected_branch=self.rollback_bound_verifier.expected_branch,
                        expected_head=self.rollback_bound_verifier.expected_head,
                    )
                    session = observation.session
                    result = {
                        **dict(context),
                        "phase": "rollback",
                        "backend_identity_verified": True,
                        "git_head": session.git_head,
                        "git_branch": session.git_branch,
                        "git_clean": True,
                        "mutates_authority": False,
                        "rollback_context_verified": False,
                        "backup_observation": observation,
                    }
                else:
                    result = self.rollback_bound_verifier.verify(context)
            except Exception as error:
                raise UpgradeError("trusted bound rollback inspection failed") from error
            if result.get("rollback_context_verified") is not False:
                raise UpgradeError("rollback inspection capability is authorizing")
            if (
                any(
                    field not in result
                    or result.get(field) != context[field]
                    or type(result.get(field)) is not type(context[field])
                    for field in CONTEXT_FIELDS
                )
                or result.get("phase") != "rollback"
                or result.get("backend") != self.context.backend
                or result.get("backend_identity_verified") is not True
                or type(result.get("mutates_authority")) is not bool
                or result.get("mutates_authority") is not False
            ):
                raise UpgradeError("rollback inspection evidence is incomplete or authorizing")
            return dict(result)

    def _rollback_locked(self, handler: Handler) -> dict[str, Any]:  # noqa: C901
        value = self._load()
        if self.backend_adapter is None:  # pragma: no cover - public check precedes this path
            raise UpgradeError("backend adapter is required for rollback")
        if value["status"] not in {"failed", "running", "safe-mode"}:
            raise UpgradeError("rollback requires failed, running, or safe-mode operation")
        rollback_records = [
            record for record in value["records"] if record.get("phase") == "rollback"
        ]
        if rollback_records:
            verified_record = rollback_records[0]
            if verified_record.get("outcome") != "rollback_verified":
                raise UpgradeError("rollback outcome requires explicit reconciliation")
            return self._finish_verified_rollback(value, verified_record)
        operation = self.operation_id
        step_id = f"{self.operation_id}.rollback"
        record: dict[str, Any] = {
            "operation_id": operation,
            "step_id": step_id,
            "phase": "rollback",
            "outcome": "started",
            "context": self._verified_rollback_context,
        }
        value["records"].append(record)
        _write(self.journal, value)
        try:
            rollback_context = cast(Mapping[str, object], _freeze(self._verified_rollback_context))
            # The internal rollback capability is bound for a later, separately
            # authorized dispatcher.  Public rollback remains rejection-only.
            adapter_result = dict(self.backend_adapter.execute("rollback", rollback_context))
            required = ("restored_verified", "runtime_validated", "backend_roundtrip_valid")
            if any(
                type(adapter_result.get(field)) is not bool or adapter_result.get(field) is not True
                for field in required
            ):
                raise UpgradeError("backend did not verify known-good runtime")
            result = dict(adapter_result)
            handler_result = handler(step_id, cast(Mapping[str, Any], _freeze(value))) or {}
            for key in set(result).intersection(handler_result):
                if result[key] != handler_result[key]:
                    raise UpgradeError("handler cannot override backend evidence")
            if set(handler_result).intersection(required):
                raise UpgradeError("handler cannot provide backend rollback evidence")
            result.update(handler_result)
            result = {key: result[key] for key in ROLLBACK_RESULT_FIELDS if key in result}
            if set(result) != ROLLBACK_RESULT_FIELDS:
                raise UpgradeError("backend rollback result identity is incomplete")
            record["outcome"] = "rollback_verified"
            record["result"] = result
        except (  # pragma: no cover - internal dispatcher is not public
            AuthorityMutationRejectedError,
            ControlStoreError,
            RollbackDispatchError,
        ) as error:
            record.update(outcome="failed", error=type(error).__name__)
            value["status"] = "failed"
            _write(self.journal, value)
            raise UpgradeError("rollback phase rejected") from error
        except Exception as error:
            record.update(outcome="ambiguous", error=type(error).__name__)
            value["status"] = "safe-mode"
            _write(self.journal, value)
            raise UpgradeError("rollback ambiguous; safe mode required") from error
        _write(self.journal, value)
        return self._finish_verified_rollback(value, record)

    def _finish_verified_rollback(  # noqa: C901
        self, value: dict[str, Any], record: dict[str, Any]
    ) -> dict[str, Any]:
        if self.backend_adapter is None or self._verified_rollback_context is None:
            raise UpgradeError("verified rollback recovery context is unavailable")
        context = cast(Mapping[str, object], _freeze(self._verified_rollback_context))
        result = cast(Mapping[str, object], _freeze(record["result"]))
        verifier = getattr(self.backend_adapter, "verify_rollback_context", None)
        begin_release = getattr(self.backend_adapter, "begin_release_rollback_context", None)
        complete_release = getattr(self.backend_adapter, "complete_release_rollback_context", None)
        revalidate = getattr(self.backend_adapter, "revalidate_rollback", None)
        methods = (verifier, begin_release, complete_release, revalidate)
        if not all(callable(method) for method in methods):
            raise UpgradeError("rollback release recovery API is unavailable")
        verifier_call = cast(Callable[[Mapping[str, object]], object], verifier)
        begin_release_call = cast(Callable[[Mapping[str, object]], object], begin_release)
        complete_release_call = cast(Callable[[Mapping[str, object]], object], complete_release)
        revalidate_call = cast(
            Callable[[Mapping[str, object], Mapping[str, object]], object], revalidate
        )
        try:
            durable = verifier_call(context)
            if not isinstance(durable, Mapping) or any(
                durable.get(field) != self._verified_rollback_context[field]
                for field in CONTEXT_FIELDS
            ):
                raise UpgradeError("rollback release identity changed")
            status = durable.get("status")
            if status == "held":
                durable = begin_release_call(context)
                if not isinstance(durable, Mapping) or durable.get("status") != "releasing":
                    raise UpgradeError("rollback barrier did not enter releasing")
                status = "releasing"
            if status not in {"releasing", "released"}:
                raise UpgradeError("rollback barrier state is not recoverable")
            self._require_rollback_revalidation(revalidate_call(context, result), record)
            if status == "releasing":
                durable = complete_release_call(context)
                if not isinstance(durable, Mapping) or durable.get("status") != "released":
                    raise UpgradeError("rollback barrier was not durably released")
            self._require_rollback_revalidation(revalidate_call(context, result), record)
        except Exception as error:
            raise UpgradeError("verified rollback release requires reconciliation") from error
        record["outcome"] = "rollback_completed"
        value["status"] = "rolled-back"
        value["phase"] = "rollback"
        _write(self.journal, value)
        return value

    def _require_rollback_revalidation(
        self, evidence: object, record: Mapping[str, object]
    ) -> None:
        if not isinstance(evidence, Mapping):
            raise UpgradeError("rollback runtime revalidation is invalid")
        result = cast(Mapping[str, object], record["result"])
        if any(evidence.get(field) != result[field] for field in ROLLBACK_RESULT_FIELDS):
            raise UpgradeError("rollback runtime revalidation changed")
