# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Authority-neutral, backup-only upgrade execution seam.

This module deliberately stops after an independently verified backup.  It does
not publish a selector, stage a runtime, commit authority state, or restore a
backup.  Those operations remain separately gated by the upgrade contract.
"""

from __future__ import annotations

from collections.abc import Mapping
from contextlib import nullcontext
from copy import deepcopy
from pathlib import Path
from types import MappingProxyType
from typing import Any, Protocol, cast


class BackupExecutionError(RuntimeError):
    """A backup-only operation cannot be proven safe."""


class BackupExecutor(Protocol):
    """Minimal generated-backup surface implemented by concrete adapters."""

    def execute_generated_backup(
        self, operation: Mapping[str, object], context: Mapping[str, object]
    ) -> Mapping[str, object]: ...

    def execute_generated_operation(
        self,
        operation: Mapping[str, object],
        destination: Path,
        binding: dict[str, Any],
    ) -> Mapping[str, object]: ...


_REQUIRED_CONTEXT = {
    "backend",
    "target",
    "destination",
    "artifact_root",
    "binding",
}
_REQUIRED_RESULT = {
    "outcome",
    "backup_verified",
    "restore_roundtrip_verified",
    "backend_identity_verified",
}

# These fields are the immutable identity envelope written by UpgradeEngine.
# A backup capability may carry additional backend binding data, but it may not
# be reused for a different engine operation or authority session.
_ENGINE_IDENTITY_FIELDS = frozenset(
    {
        "schema_version",
        "backend",
        "project_id",
        "operation_id",
        "state_revision",
        "authority_revision",
        "fencing_token",
        "fencing_owner",
        "durable_barrier_id",
        "artifact_root",
        "source",
        "destination",
        "manifest",
        "selector_ref",
        "barrier_identity_digest",
        "target",
        "envelope_digest",
    }
)


def _validated_artifacts(context: Mapping[str, object]) -> tuple[str, Path, dict[str, Any]]:
    if not isinstance(context, Mapping) or set(context) < _REQUIRED_CONTEXT:
        raise BackupExecutionError("backup execution context is incomplete")
    backend = context.get("backend")
    target = context.get("target")
    destination = context.get("destination")
    artifact_root = context.get("artifact_root")
    binding = context.get("binding")
    if not isinstance(backend, str) or backend not in {"git", "sqlite"} or target != "new":
        raise BackupExecutionError("backup execution identity is invalid")
    if not isinstance(destination, str) or not isinstance(artifact_root, str):
        raise BackupExecutionError("backup artifact binding is invalid")
    if not isinstance(binding, dict):
        raise BackupExecutionError("backup authority binding is invalid")
    destination_path = Path(destination).resolve()
    try:
        destination_path.relative_to(Path(artifact_root).resolve())
    except ValueError as error:
        raise BackupExecutionError("backup destination escapes artifact root") from error
    return backend, destination_path, binding


def _dispatch_backup(
    adapter: object,
    backend: str,
    operation: Mapping[str, object],
    context: Mapping[str, object],
    destination: Path,
    binding: dict[str, Any],
) -> Mapping[str, object]:
    concrete = cast(BackupExecutor, adapter)
    if backend == "git":
        return concrete.execute_generated_backup(operation, context)
    return concrete.execute_generated_operation(operation, destination, binding)


def _validated_result(result: Mapping[str, object]) -> dict[str, object]:
    if set(result) < _REQUIRED_RESULT:
        raise BackupExecutionError("generated backup result is incomplete")
    if (
        result.get("outcome") != "completed"
        or result.get("backup_verified") is not True
        or result.get("restore_roundtrip_verified") is not True
        or result.get("backend_identity_verified") is not True
        or result.get("mutates_authority") is True
    ):
        raise BackupExecutionError("generated backup postconditions are not proven")
    return dict(result)


def execute_verified_backup(
    adapter: object,
    operation: Mapping[str, object],
    context: Mapping[str, object],
) -> dict[str, object]:
    """Execute only a generated backup operation through the selected backend.

    The concrete Git/SQLite generated executors own their barrier, journal,
    identity, and durability checks.  This wrapper prevents the upgrade engine
    from selecting a backend-specific mutation path and validates the common
    postcondition before returning evidence to the phase journal.
    """
    if not isinstance(operation, Mapping) or operation.get("opcode") != "backend.backup":
        raise BackupExecutionError("backup operation is unsupported")
    backend, destination_path, binding = _validated_artifacts(context)
    try:
        result = _dispatch_backup(adapter, backend, operation, context, destination_path, binding)
    except BackupExecutionError:
        raise
    except Exception as error:
        raise BackupExecutionError("generated backup execution failed") from error
    if not isinstance(result, Mapping):
        raise BackupExecutionError("generated backup result is invalid")
    return _validated_result(result)


class BoundBackupPhaseAdapter:
    """Bind the generated backup capability to one immutable engine session.

    ``UpgradeEngine`` already invokes ``backend_adapter.execute`` for every
    phase.  This adapter is the deliberately narrow production binding for the
    backup phase: only that phase can reach the generated backup executor, and
    its context is checked against the exact immutable engine identity before
    dispatch.  All other phases retain the wrapped adapter's existing
    fail-closed behavior; in particular this class does not enable commit,
    apply, selector publication, or rollback.
    """

    def __init__(
        self,
        backend: object,
        operation: Mapping[str, object],
        backup_context: Mapping[str, object],
    ) -> None:
        if not isinstance(operation, Mapping) or operation.get("opcode") != "backend.backup":
            raise BackupExecutionError("backup operation is unsupported")
        if not isinstance(backup_context, Mapping):
            raise BackupExecutionError("backup execution context is incomplete")
        if not set(backup_context) >= _ENGINE_IDENTITY_FIELDS:
            raise BackupExecutionError("backup execution context omits engine identity")
        # Validate all artifact fields before exposing the capability.  Copies
        # prevent later caller mutation from changing the session binding.
        _validated_artifacts(backup_context)
        self._backend = backend
        self._operation = MappingProxyType(deepcopy(dict(operation)))
        self._backup_context = MappingProxyType(deepcopy(dict(backup_context)))
        self._identity = {field: self._backup_context[field] for field in _ENGINE_IDENTITY_FIELDS}

    @property
    def requires_bound_rollback(self) -> bool:
        return bool(getattr(self._backend, "requires_bound_rollback", False))

    def operation_lock(self) -> object:
        lock = getattr(self._backend, "operation_lock", None)
        return lock() if callable(lock) else nullcontext()

    def snapshot(self, phase: str, context: Mapping[str, object]) -> dict[str, Any]:
        result = self._backend.snapshot(phase, context)  # type: ignore[attr-defined]
        if not isinstance(result, dict):
            raise BackupExecutionError("backend snapshot must be an object")
        return result

    def verify_rollback_context(self, context: Mapping[str, object]) -> dict[str, Any] | None:
        result = self._backend.verify_rollback_context(context)  # type: ignore[attr-defined]
        if result is not None and not isinstance(result, dict):
            raise BackupExecutionError("rollback verification result must be an object or null")
        return result

    def execute(self, phase: str, context: Mapping[str, object]) -> dict[str, Any]:
        if phase == "backup":
            if any(context.get(field) != value for field, value in self._identity.items()):
                raise BackupExecutionError("backup engine context identity mismatch")
            return cast(
                dict[str, Any],
                execute_verified_backup(self._backend, self._operation, self._backup_context),
            )
        result = self._backend.execute(phase, context)  # type: ignore[attr-defined]
        if not isinstance(result, dict):
            raise BackupExecutionError("backend execution result must be an object")
        return result
