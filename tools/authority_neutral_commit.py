# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Authority-neutral prerequisite evidence for a future authority commit."""

from __future__ import annotations

from collections.abc import Mapping
from copy import deepcopy
from dataclasses import dataclass
from types import MappingProxyType
from typing import Any, cast


class CommitAuthorizationExecutionError(RuntimeError):
    """Raised when commit prerequisites are absent, contradictory, or uncertain."""


_IDENTITY_FIELDS = frozenset(
    {"backend", "target", "operation_id", "fencing_token", "state_revision", "barrier_id"}
)
_REQUIRED_EVIDENCE = frozenset(
    {
        "backend",
        "target",
        "operation_id",
        "fencing_token",
        "state_revision",
        "barrier_id",
        "backup_verified",
        "restore_roundtrip_verified",
        "staged_verified",
        "manifest_verified",
        "selector_admission_verified",
        "runtime_replacement_admission_verified",
        "backend_identity_verified",
        "mutates_authority",
    }
)

_MUTATION_BINDING_FIELDS = (
    "backend",
    "target",
    "operation_id",
    "fencing_token",
    "state_revision",
    "barrier_id",
    "artifact_identity",
    "manifest_identity",
    "selector_identity",
    "runtime_identity",
)


@dataclass(frozen=True)
class CommitAdmissionBundle:
    """Immutable identity bundle for a future authority effect."""

    backend: str
    target: str
    operation_id: str
    fencing_token: str
    state_revision: int
    barrier_id: str
    artifact_identity: str
    manifest_identity: str
    selector_identity: str
    runtime_identity: str

    def __post_init__(self) -> None:
        if not isinstance(self.backend, str) or self.backend not in {"git", "sqlite"}:
            raise CommitAuthorizationExecutionError("commit authorization identity is invalid")
        if not isinstance(self.target, str) or self.target not in {"new", "rollback"}:
            raise CommitAuthorizationExecutionError("commit authorization identity is invalid")
        for field in ("operation_id", "fencing_token", "barrier_id"):
            value = getattr(self, field)
            if not isinstance(value, str) or not value:
                raise CommitAuthorizationExecutionError(f"commit authorization {field} is invalid")
        if type(self.state_revision) is not int or self.state_revision < 1:
            raise CommitAuthorizationExecutionError("commit authorization revision is invalid")
        for field in (
            "artifact_identity",
            "manifest_identity",
            "selector_identity",
            "runtime_identity",
        ):
            value = getattr(self, field)
            if not isinstance(value, str) or not value:
                raise CommitAuthorizationExecutionError(f"commit authorization {field} is invalid")

    @classmethod
    def from_evidence(cls, evidence: Mapping[str, object]) -> CommitAdmissionBundle:
        _validate_evidence(evidence)
        for field in _MUTATION_BINDING_FIELDS[6:]:
            value = evidence.get(field)
            if not isinstance(value, str) or not value:
                raise CommitAuthorizationExecutionError(f"commit authorization {field} is invalid")
        return cls(
            backend=cast(str, evidence["backend"]),
            target=cast(str, evidence["target"]),
            operation_id=cast(str, evidence["operation_id"]),
            fencing_token=cast(str, evidence["fencing_token"]),
            state_revision=cast(int, evidence["state_revision"]),
            barrier_id=cast(str, evidence["barrier_id"]),
            artifact_identity=cast(str, evidence["artifact_identity"]),
            manifest_identity=cast(str, evidence["manifest_identity"]),
            selector_identity=cast(str, evidence["selector_identity"]),
            runtime_identity=cast(str, evidence["runtime_identity"]),
        )

    def matches(self, evidence: object) -> bool:
        if not isinstance(evidence, Mapping):
            return False
        return all(
            evidence.get(field) == getattr(self, field) for field in _MUTATION_BINDING_FIELDS
        )


def _validate_evidence(evidence: Mapping[str, object]) -> None:
    if not isinstance(evidence, Mapping) or not set(evidence) >= _REQUIRED_EVIDENCE:
        raise CommitAuthorizationExecutionError("commit authorization evidence is incomplete")
    if not isinstance(evidence["backend"], str) or evidence["backend"] not in {"git", "sqlite"}:
        raise CommitAuthorizationExecutionError("commit authorization identity is invalid")
    if not isinstance(evidence["target"], str) or evidence["target"] != "new":
        raise CommitAuthorizationExecutionError("commit authorization identity is invalid")
    for field in ("operation_id", "fencing_token", "barrier_id"):
        if not isinstance(evidence[field], str) or not evidence[field]:
            raise CommitAuthorizationExecutionError(f"commit authorization {field} is invalid")
    if type(evidence["state_revision"]) is not int or evidence["state_revision"] < 1:
        raise CommitAuthorizationExecutionError("commit authorization revision is invalid")
    required_true = (
        "backup_verified",
        "restore_roundtrip_verified",
        "staged_verified",
        "manifest_verified",
        "selector_admission_verified",
        "runtime_replacement_admission_verified",
        "backend_identity_verified",
    )
    if any(evidence[field] is not True for field in required_true):
        raise CommitAuthorizationExecutionError("commit authorization prerequisite is unverified")
    if evidence["mutates_authority"] is not False:
        raise CommitAuthorizationExecutionError("commit authorization evidence is mutating")


def execute_verified_commit_authorization(
    operation: Mapping[str, object], evidence: Mapping[str, object]
) -> dict[str, object]:
    """Validate all prerequisites without authorizing or dispatching commit."""
    if not isinstance(operation, Mapping) or operation.get("opcode") != "authority.commit.admit":
        raise CommitAuthorizationExecutionError("commit authorization operation is unsupported")
    _validate_evidence(evidence)
    return {
        "outcome": "completed",
        "commit_prerequisites_verified": True,
        "commit_authorized": False,
        "mutates_authority": False,
        "backend_identity_verified": True,
        "fencing_token": evidence["fencing_token"],
    }


class BoundCommitAuthorizationAdapter:
    """Bind prerequisite evidence to one immutable operation identity."""

    def __init__(self, operation: Mapping[str, object], evidence: Mapping[str, object]) -> None:
        if (
            not isinstance(operation, Mapping)
            or operation.get("opcode") != "authority.commit.admit"
        ):
            raise CommitAuthorizationExecutionError("commit authorization operation is unsupported")
        _validate_evidence(evidence)
        self._bundle = CommitAdmissionBundle.from_evidence(evidence)
        self._operation = MappingProxyType(deepcopy(dict(operation)))
        self._evidence = MappingProxyType(deepcopy(dict(evidence)))
        self._identity = {field: self._evidence[field] for field in _IDENTITY_FIELDS}

    def execute(self, phase: str, evidence: Mapping[str, object]) -> dict[str, Any]:
        if phase != "commit_admission":
            raise CommitAuthorizationExecutionError("commit authorization phase is unsupported")
        if not self._bundle.matches(evidence):
            raise CommitAuthorizationExecutionError("commit authorization identity mismatch")
        return execute_verified_commit_authorization(self._operation, self._evidence)
