# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Explicit binding between a portable upgrade contract and runtime identity."""

from __future__ import annotations

import hashlib
import json
import re
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import Any, cast

if __package__:
    from .upgrade_contract_runtime import RuntimeContractError, validate_runtime_contract
    from .upgrade_identity import ENVELOPE_FIELDS, UpgradeIdentityError, validate_envelope
else:  # pragma: no cover - direct vendored script imports
    from upgrade_contract_runtime import (  # type: ignore[import-not-found,no-redef]
        RuntimeContractError,
        validate_runtime_contract,
    )
    from upgrade_identity import (  # type: ignore[import-not-found,no-redef]
        ENVELOPE_FIELDS,
        UpgradeIdentityError,
        validate_envelope,
    )

BINDING_SCHEMA_VERSION = 1
BINDING_FIELDS = (
    "schema_version",
    "contract_digest",
    "session_identity_digest",
    "contract_operation_id",
    "contract_backend",
    "contract_selector_ref",
    "contract_expected_state_revision",
    "contract_barrier_id",
    "contract_fencing_token",
    "contract_backup_operation_id",
    "runtime_envelope",
)
_DIGEST = re.compile(r"[0-9a-f]{64}")
_LIVE_BINDING_TOKEN = object()
_LIVE_BINDING_REGISTRY: dict[int, tuple[object, tuple[object, ...]]] = {}


def _live_binding_fingerprint(value: object) -> tuple[object, ...]:
    return (
        id(getattr(value, "runtime", None)),
        id(getattr(value, "session", None)),
        id(getattr(value, "scope", None)),
        id(getattr(value, "lease", None)),
        id(getattr(value, "admission_recheck", None)),
        id(getattr(value, "adapter", None)),
        getattr(value, "expected_branch", None),
        getattr(value, "expected_head", None),
        getattr(value, "expected_git_repository", None),
        id(getattr(value, "_token", None)),
    )


class UpgradeBindingError(ValueError):
    """A portable contract and host-bound runtime identity do not match."""


@dataclass(frozen=True, slots=True, init=False)
class LiveUpgradeBinding:
    """One immutable binding of contract, durable session, and backend scope.

    This is an admission identity only.  It deliberately exposes no mutation
    callback or phase executor; the production phase engine must consume this
    proof before it can construct any effect capability.
    """

    runtime: UpgradeRuntimeBinding
    session: object
    scope: object
    lease: object
    admission_recheck: object
    adapter: object
    _token: object
    expected_branch: str | None
    expected_head: str | None
    expected_git_repository: Path | None

    def __init__(self) -> None:
        raise TypeError("LiveUpgradeBinding must be issued by bind()")

    @classmethod
    def bind(  # noqa: C901
        cls,
        runtime: UpgradeRuntimeBinding,
        session: object,
        scope: object,
        lease: object,
        admission_recheck: object,
        adapter: object,
        *,
        expected_git_repository: Path | None = None,
    ) -> LiveUpgradeBinding:
        from tools.admission_lease import AdmissionLease, AdmissionRecheck
        from tools.git_authority_adapter import GitAuthorityAdapter
        from tools.lock_domain_scope import LockDomainScope
        from tools.rollback_control_store import BarrierSessionState, SQLiteBarrierSessionStore
        from tools.sqlite_authority_adapter import SQLiteAuthorityAdapter

        if type(runtime) is not UpgradeRuntimeBinding:
            raise UpgradeBindingError("runtime upgrade binding is required")
        if type(session) is not BarrierSessionState:
            raise UpgradeBindingError("live barrier session is invalid")
        if type(scope) is not LockDomainScope:
            raise UpgradeBindingError("live lock-domain scope is invalid")
        if type(lease) is not AdmissionLease:
            raise UpgradeBindingError("live admission lease is invalid")
        if type(admission_recheck) is not AdmissionRecheck:
            raise UpgradeBindingError("live admission recheck is invalid")
        if admission_recheck.lease != lease:
            raise UpgradeBindingError("live admission recheck does not match lease")
        envelope = runtime.runtime_envelope
        expected = {
            "project_id": envelope["project_id"],
            "authority_revision": envelope["authority_revision"],
            "fencing_token": envelope["fencing_token"],
            "fencing_owner": envelope["fencing_owner"],
            "durable_barrier_id": envelope["durable_barrier_id"],
            "state_revision": envelope["state_revision"],
        }
        if any(
            getattr(lease, "revision" if field == "state_revision" else field) != value
            for field, value in expected.items()
        ):
            raise UpgradeBindingError("live admission lease identity does not match runtime")
        try:
            scope.assert_context(expected)
        except Exception as error:
            raise UpgradeBindingError(
                "live lock-domain scope identity does not match runtime"
            ) from error
        session_store = getattr(scope, "_session_store", None)
        if type(session_store) is not SQLiteBarrierSessionStore:
            raise UpgradeBindingError("live scope does not carry a concrete session store")
        if getattr(scope, "_session_identity", None) != session.identity:
            raise UpgradeBindingError("live scope session identity does not match durable session")
        if getattr(scope, "_session_revision", None) != session.revision:
            raise UpgradeBindingError("live scope session revision does not match durable session")
        if getattr(scope, "_lease", None) != lease:
            raise UpgradeBindingError("live scope lease does not match admission lease")
        try:
            with scope.hold():
                observed = session_store.snapshot_owned_by_caller()
        except Exception as error:
            raise UpgradeBindingError("live durable session reread was rejected") from error
        if observed != session:
            raise UpgradeBindingError("live durable session changed during binding")
        runtime.validate_live_session(observed)
        backend = envelope["backend"]
        expected_branch: str | None = None
        expected_head: str | None = None
        if backend == "git" and type(adapter) is not GitAuthorityAdapter:
            raise UpgradeBindingError("Git live backend adapter is not concrete")
        if backend == "git":
            if not isinstance(expected_git_repository, Path):
                raise UpgradeBindingError("expected Git repository identity is required")
            git_adapter = cast(GitAuthorityAdapter, adapter)
            if git_adapter._repository != expected_git_repository.resolve():
                raise UpgradeBindingError("Git live backend is bound to a foreign repository")
        elif expected_git_repository is not None:
            raise UpgradeBindingError("Git repository identity is invalid for SQLite")
        if backend == "sqlite":
            if type(adapter) is not SQLiteAuthorityAdapter:
                raise UpgradeBindingError("SQLite live backend adapter is not concrete")
            if getattr(session_store, "authority_path", None) != getattr(
                adapter, "_authority", None
            ):
                raise UpgradeBindingError("SQLite live backend is bound to a foreign authority")
        if backend == "git":
            try:
                git_adapter = cast(GitAuthorityAdapter, adapter)
                expected_branch = git_adapter._git("symbolic-ref", "--short", "-q", "HEAD")
                expected_head = git_adapter._git("rev-parse", "--verify", "HEAD")
            except Exception as error:
                raise UpgradeBindingError("Git live backend reread was rejected") from error
        try:
            runtime.reread_backend_bound(
                adapter,
                scope,
                lease,
                admission_recheck,
                expected_branch=expected_branch,
                expected_head=expected_head,
            )
        except Exception as error:
            raise UpgradeBindingError("live backend reread was rejected") from error
        issued = object.__new__(cls)
        object.__setattr__(issued, "runtime", runtime)
        object.__setattr__(issued, "session", session)
        object.__setattr__(issued, "scope", scope)
        object.__setattr__(issued, "lease", lease)
        object.__setattr__(issued, "admission_recheck", admission_recheck)
        object.__setattr__(issued, "adapter", adapter)
        object.__setattr__(issued, "_token", _LIVE_BINDING_TOKEN)
        object.__setattr__(issued, "expected_branch", expected_branch)
        object.__setattr__(issued, "expected_head", expected_head)
        object.__setattr__(issued, "expected_git_repository", expected_git_repository)
        _LIVE_BINDING_REGISTRY[id(issued)] = (issued, _live_binding_fingerprint(issued))
        return issued

    def reread_backend(
        self, *, expected_branch: str | None = None, expected_head: str | None = None
    ) -> dict[str, object]:
        """Obtain fresh read-only backend evidence through this binding."""
        if expected_branch is None:
            expected_branch = self.expected_branch
        if expected_head is None:
            expected_head = self.expected_head
        return self.runtime.reread_backend_bound(
            self.adapter,
            self.scope,
            self.lease,
            self.admission_recheck,
            expected_branch=expected_branch,
            expected_head=expected_head,
        )

    def matches_runtime(self, runtime: UpgradeRuntimeBinding) -> bool:
        """Return whether this live binding is for the exact runtime binding."""
        return (
            self.is_admitted()
            and isinstance(runtime, UpgradeRuntimeBinding)
            and self.runtime == runtime
        )

    def matches_contract(self, contract: Mapping[str, object], backend: str) -> bool:
        """Return whether this binding is admitted for one exact contract."""
        return (
            self.is_admitted()
            and self.runtime.contract_digest == canonical_contract_digest(contract)
            and self.runtime.contract_backend == backend
        )

    def is_admitted(self) -> bool:
        """Revalidate the sealed binding before a production boundary consumes it."""
        if type(self) is not LiveUpgradeBinding:
            return False
        if getattr(self, "_token", None) is not _LIVE_BINDING_TOKEN:
            return False
        issued = _LIVE_BINDING_REGISTRY.get(id(self))
        if issued is None or issued[0] is not self or issued[1] != _live_binding_fingerprint(self):
            return False
        try:
            refreshed = LiveUpgradeBinding.bind(
                self.runtime,
                self.session,
                self.scope,
                self.lease,
                self.admission_recheck,
                self.adapter,
                expected_git_repository=self.expected_git_repository,
            )
        except Exception:
            return False
        return (
            refreshed.expected_branch == self.expected_branch
            and refreshed.expected_head == self.expected_head
        )


def canonical_contract_digest(contract: Mapping[str, object]) -> str:
    """Return the digest of the exact validated portable contract."""
    try:
        encoded = json.dumps(
            contract, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",", ":")
        ).encode("utf-8")
    except (TypeError, ValueError) as error:
        raise UpgradeBindingError("upgrade contract is not canonical JSON") from error
    return hashlib.sha256(encoded).hexdigest()


def _contract_inputs(contract: Mapping[str, Any]) -> dict[str, Any]:
    rollback = contract["rollback"]
    operation = rollback["operation"]
    inputs = operation["inputs"]
    if not isinstance(inputs, dict):
        raise UpgradeBindingError("upgrade rollback operation inputs are invalid")
    return inputs


def _validate_contract_identity(contract: Mapping[str, Any]) -> dict[str, Any]:
    try:
        value = validate_runtime_contract(contract)
    except RuntimeContractError as error:
        raise UpgradeBindingError("upgrade contract is invalid") from error
    inputs = _contract_inputs(value)
    required = {
        "backend",
        "selector_ref",
        "expected_state_revision",
        "barrier_id",
        "fencing_token",
        "backup_operation_id",
        "target",
    }
    if set(inputs) != required:
        raise UpgradeBindingError("upgrade contract binding inputs are invalid")
    for phase in value["phases"]:
        if phase["operation"]["inputs"] != {
            key: value for key, value in inputs.items() if key != "target"
        }:
            raise UpgradeBindingError("upgrade phase inputs do not match rollback inputs")
    if value["backend"] != inputs["backend"]:
        raise UpgradeBindingError("upgrade contract backend binding is inconsistent")
    if inputs["backup_operation_id"] != f"{value['operation_id']}:backup":
        raise UpgradeBindingError("upgrade backup operation identity is invalid")
    if inputs["target"] != "rollback":
        raise UpgradeBindingError("upgrade rollback target is invalid")
    if value["rollback"]["operation"]["operation_id"] != f"{value['operation_id']}:rollback":
        raise UpgradeBindingError("upgrade rollback operation identity is invalid")
    return value


def _validated_envelope(value: Mapping[str, object]) -> dict[str, object]:
    try:
        return validate_envelope(value)
    except UpgradeIdentityError as error:
        raise UpgradeBindingError("runtime upgrade envelope is invalid") from error


@dataclass(frozen=True, slots=True)
class UpgradeRuntimeBinding:
    """Validated contract/runtime identity; this type performs no dispatch."""

    schema_version: int
    contract_digest: str
    session_identity_digest: str
    contract_operation_id: str
    contract_backend: str
    contract_selector_ref: str
    contract_expected_state_revision: int
    contract_barrier_id: str
    contract_fencing_token: str
    contract_backup_operation_id: str
    runtime_envelope: dict[str, object]

    @classmethod
    def bind(
        cls,
        contract: Mapping[str, object],
        runtime_envelope: Mapping[str, object],
        *,
        session_identity_digest: str,
    ) -> UpgradeRuntimeBinding:
        value = _validate_contract_identity(contract)
        envelope = _validated_envelope(runtime_envelope)
        inputs = _contract_inputs(value)
        if _DIGEST.fullmatch(session_identity_digest) is None:
            raise UpgradeBindingError("runtime barrier session identity digest is invalid")
        if envelope["target"] != "rollback":
            raise UpgradeBindingError("runtime binding target must be rollback")
        if envelope["operation_id"] != value["operation_id"]:
            raise UpgradeBindingError("runtime operation identity does not match contract")
        if envelope["backend"] != inputs["backend"]:
            raise UpgradeBindingError("runtime backend identity does not match contract")
        for envelope_field, input_field in (
            ("selector_ref", "selector_ref"),
            ("state_revision", "expected_state_revision"),
            ("durable_barrier_id", "barrier_id"),
            ("fencing_token", "fencing_token"),
        ):
            if envelope[envelope_field] != inputs[input_field]:
                raise UpgradeBindingError(f"runtime {envelope_field} does not match contract")
        return cls(
            BINDING_SCHEMA_VERSION,
            canonical_contract_digest(value),
            session_identity_digest,
            value["operation_id"],
            inputs["backend"],
            inputs["selector_ref"],
            inputs["expected_state_revision"],
            inputs["barrier_id"],
            inputs["fencing_token"],
            inputs["backup_operation_id"],
            envelope,
        )

    @classmethod
    def from_mapping(cls, value: Mapping[str, object]) -> UpgradeRuntimeBinding:  # noqa: C901
        if set(value) != set(BINDING_FIELDS):
            raise UpgradeBindingError("runtime binding fields are invalid")
        if value["schema_version"] != BINDING_SCHEMA_VERSION:
            raise UpgradeBindingError("runtime binding schema version is invalid")
        envelope = value["runtime_envelope"]
        if not isinstance(envelope, Mapping) or set(envelope) != set(ENVELOPE_FIELDS):
            raise UpgradeBindingError("runtime binding envelope is invalid")
        if value["contract_operation_id"] != envelope.get("operation_id"):
            raise UpgradeBindingError("runtime binding operation identity is inconsistent")
        if value["contract_backend"] != envelope.get("backend"):
            raise UpgradeBindingError("runtime binding backend identity is inconsistent")
        for binding_field, envelope_field in (
            ("contract_selector_ref", "selector_ref"),
            ("contract_expected_state_revision", "state_revision"),
            ("contract_barrier_id", "durable_barrier_id"),
            ("contract_fencing_token", "fencing_token"),
        ):
            if value[binding_field] != envelope.get(envelope_field):
                raise UpgradeBindingError(
                    f"runtime binding {binding_field} is inconsistent with envelope"
                )
        for field in (
            "contract_digest",
            "session_identity_digest",
            "contract_operation_id",
            "contract_backend",
            "contract_selector_ref",
            "contract_barrier_id",
            "contract_fencing_token",
            "contract_backup_operation_id",
        ):
            if not isinstance(value[field], str) or not value[field]:
                raise UpgradeBindingError(f"runtime binding {field} is invalid")
        if _DIGEST.fullmatch(cast(str, value["contract_digest"])) is None:
            raise UpgradeBindingError("runtime binding contract digest is invalid")
        if _DIGEST.fullmatch(cast(str, value["session_identity_digest"])) is None:
            raise UpgradeBindingError("runtime binding session identity digest is invalid")
        revision = value["contract_expected_state_revision"]
        if type(revision) is not int or revision < 1:
            raise UpgradeBindingError("runtime binding state revision is invalid")
        _validated_envelope(envelope)
        strings = {
            field: cast(str, value[field])
            for field in (
                "contract_digest",
                "session_identity_digest",
                "contract_operation_id",
                "contract_backend",
                "contract_selector_ref",
                "contract_barrier_id",
                "contract_fencing_token",
                "contract_backup_operation_id",
            )
        }
        return cls(
            value["schema_version"],
            strings["contract_digest"],
            strings["session_identity_digest"],
            strings["contract_operation_id"],
            strings["contract_backend"],
            strings["contract_selector_ref"],
            revision,
            strings["contract_barrier_id"],
            strings["contract_fencing_token"],
            strings["contract_backup_operation_id"],
            dict(envelope),
        )

    def as_mapping(self) -> dict[str, object]:
        return {field: getattr(self, field) for field in BINDING_FIELDS}

    def validate_live_session(self, session: object) -> None:
        """Validate the observed held durable session without changing it."""
        from tools.rollback_control_store import BarrierSessionState

        if not isinstance(session, BarrierSessionState):
            raise UpgradeBindingError("live rollback barrier session is invalid")
        identity = session.identity
        envelope = self.runtime_envelope
        if identity.identity_digest != self.session_identity_digest:
            raise UpgradeBindingError("live barrier session identity digest does not match")
        for session_field, envelope_field in (
            ("project_id", "project_id"),
            ("state_revision", "state_revision"),
            ("authority_revision_at_acquire", "authority_revision"),
            ("durable_barrier_id", "durable_barrier_id"),
            ("fencing_token", "fencing_token"),
        ):
            if getattr(identity, session_field) != envelope[envelope_field]:
                raise UpgradeBindingError(f"live barrier {session_field} does not match")
        child = session.rollback_child
        if session.status != "held" or child is None:
            raise UpgradeBindingError("live rollback barrier is not held with a rollback child")
        if (
            child.operation_id != envelope["operation_id"]
            or child.target != "rollback"
            or child.barrier_identity_digest != identity.identity_digest
        ):
            raise UpgradeBindingError("live rollback child identity does not match")

    def validate_backend_evidence(  # noqa: C901
        self, evidence: Mapping[str, object]
    ) -> dict[str, object]:
        """Validate one concrete adapter's read-only rollback observation."""
        if not isinstance(evidence, Mapping):
            raise UpgradeBindingError("rollback backend evidence is invalid")
        backend = self.runtime_envelope["backend"]
        backend_fields = (
            {"git_head", "git_branch", "git_clean"}
            if backend == "git"
            else {"sqlite_integrity_verified", "sqlite_foreign_keys_verified"}
        )
        required = set(self.runtime_envelope) | {
            "phase",
            "backend_identity_verified",
            "mutates_authority",
            *backend_fields,
        }
        if set(evidence) != required:
            raise UpgradeBindingError("rollback backend evidence schema is invalid")
        for field, expected in self.runtime_envelope.items():
            if evidence.get(field) != expected or type(evidence.get(field)) is not type(expected):
                raise UpgradeBindingError("rollback backend evidence identity does not match")
        if evidence.get("phase") != "rollback":
            raise UpgradeBindingError("rollback backend evidence phase is invalid")
        if evidence.get("backend_identity_verified") is not True:
            raise UpgradeBindingError("rollback backend evidence is not verified")
        if backend == "git":
            if (
                not isinstance(evidence.get("git_head"), str)
                or not evidence["git_head"]
                or not isinstance(evidence.get("git_branch"), str)
                or not evidence["git_branch"]
                or evidence.get("git_clean") is not True
            ):
                raise UpgradeBindingError("rollback Git evidence is not verified")
        elif any(evidence.get(field) is not True for field in backend_fields):
            raise UpgradeBindingError("rollback SQLite evidence is not verified")
        if evidence.get("mutates_authority") is not False:
            raise UpgradeBindingError("rollback backend evidence is not read-only")
        return dict(evidence)

    def reread_backend_bound(  # noqa: C901
        self,
        adapter: object,
        scope: object,
        lease: object,
        admission_recheck: object,
        *,
        expected_branch: str | None = None,
        expected_head: str | None = None,
    ) -> dict[str, object]:
        """Reread concrete Git/SQLite evidence through the live bound scope."""
        from tools.admission_lease import AdmissionLease, AdmissionRecheck

        if self.runtime_envelope["backend"] == "git":
            from tools.git_authority_adapter import GitAuthorityAdapter
            from tools.lock_domain_scope import LockDomainScope

            if not isinstance(adapter, GitAuthorityAdapter):
                raise UpgradeBindingError("Git rollback adapter is not concrete")
            if not isinstance(scope, LockDomainScope):
                raise UpgradeBindingError("Git rollback lock-domain scope is not concrete")
            if not isinstance(lease, AdmissionLease):
                raise UpgradeBindingError("Git rollback admission lease is not concrete")
            if not isinstance(admission_recheck, AdmissionRecheck):
                raise UpgradeBindingError("Git rollback admission recheck is not concrete")
            if admission_recheck.lease != lease:
                raise UpgradeBindingError("Git rollback admission recheck does not match lease")
            if not isinstance(expected_branch, str) or not expected_branch:
                raise UpgradeBindingError("Git rollback branch evidence is required")
            if not isinstance(expected_head, str) or not expected_head:
                raise UpgradeBindingError("Git rollback head evidence is required")
            adapter_any = cast(Any, adapter)
            try:
                evidence = adapter_any.snapshot_bound(
                    "rollback",
                    self.runtime_envelope,
                    scope,
                    lease=lease,
                    admission_recheck=admission_recheck,
                    expected_branch=expected_branch,
                    expected_head=expected_head,
                )
            except Exception as error:
                raise UpgradeBindingError("bound Git rollback reread was rejected") from error
        else:
            from tools.lock_domain_scope import LockDomainScope
            from tools.sqlite_authority_adapter import SQLiteAuthorityAdapter

            if not isinstance(adapter, SQLiteAuthorityAdapter):
                raise UpgradeBindingError("SQLite rollback adapter is not concrete")
            if not isinstance(scope, LockDomainScope):
                raise UpgradeBindingError("SQLite rollback lock-domain scope is not concrete")
            if not isinstance(lease, AdmissionLease):
                raise UpgradeBindingError("SQLite rollback admission lease is not concrete")
            if not isinstance(admission_recheck, AdmissionRecheck):
                raise UpgradeBindingError("SQLite rollback admission recheck is not concrete")
            if admission_recheck.lease != lease:
                raise UpgradeBindingError("SQLite rollback admission recheck does not match lease")
            adapter_any = cast(Any, adapter)
            try:
                evidence = adapter_any.snapshot_bound(
                    "rollback",
                    self.runtime_envelope,
                    scope,
                    lease=lease,
                    admission_recheck=admission_recheck,
                )
            except Exception as error:
                raise UpgradeBindingError("bound SQLite rollback reread was rejected") from error
        if not isinstance(evidence, Mapping):
            raise UpgradeBindingError("bound rollback reread returned invalid evidence")
        return self.validate_backend_evidence(evidence)
