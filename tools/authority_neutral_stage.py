# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Authority-neutral, read-only staged-runtime verification."""

from __future__ import annotations

from collections.abc import Mapping
from copy import deepcopy
from pathlib import Path
from types import MappingProxyType
from typing import Any, cast

from tools.runtime_bootstrap import verify_runtime_manifest
from tools.upgrade_authority import AuthorityError


class StageExecutionError(RuntimeError):
    """A staged artifact cannot be proven immutable and identity-bound."""


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
_REQUIRED_CONTEXT = {
    "backend",
    "target",
    "artifact_root",
    "runtime_root",
    "manifest_digest",
    "binding",
}
_REQUIRED_RESULT = {"outcome", "staged_verified", "manifest_verified", "backend_identity_verified"}


def _validate_context(context: Mapping[str, object]) -> tuple[Path, str]:
    if not isinstance(context, Mapping) or not set(context) >= _REQUIRED_CONTEXT:
        raise StageExecutionError("stage execution context is incomplete")
    if context.get("backend") not in {"git", "sqlite"} or context.get("target") != "new":
        raise StageExecutionError("stage execution identity is invalid")
    if not isinstance(context.get("binding"), dict):
        raise StageExecutionError("stage authority binding is invalid")
    root = context.get("artifact_root")
    runtime = context.get("runtime_root")
    digest = context.get("manifest_digest")
    if not isinstance(root, str) or not isinstance(runtime, str) or not isinstance(digest, str):
        raise StageExecutionError("stage artifact binding is invalid")
    runtime_path = Path(runtime).resolve()
    try:
        runtime_path.relative_to(Path(root).resolve())
    except ValueError as error:
        raise StageExecutionError("stage runtime escapes artifact root") from error
    return runtime_path, digest


def execute_verified_stage(
    _adapter: object, operation: Mapping[str, object], context: Mapping[str, object]
) -> dict[str, object]:
    """Verify one generated stage operation without changing authority."""
    if not isinstance(operation, Mapping) or operation.get("opcode") not in {
        "backend.stage",
        "runtime.stage",
    }:
        raise StageExecutionError("stage operation is unsupported")
    runtime_root, digest = _validate_context(context)
    try:
        verified = verify_runtime_manifest(runtime_root, digest)
    except (AuthorityError, OSError, RuntimeError) as error:
        raise StageExecutionError("staged runtime verification failed") from error
    if verified is not True:
        raise StageExecutionError("staged runtime verification is incomplete")
    return {
        "operation_id": operation.get("operation_id"),
        "opcode": operation["opcode"],
        "outcome": "completed",
        "backend": context["backend"],
        "staged_verified": True,
        "manifest_verified": True,
        "backend_identity_verified": True,
        "mutates_authority": False,
        "fencing_token": context["fencing_token"],
    }


class BoundStagePhaseAdapter:
    """Bind stage verification to one immutable engine session."""

    def __init__(
        self, backend: object, operation: Mapping[str, object], stage_context: Mapping[str, object]
    ) -> None:
        if not isinstance(operation, Mapping) or operation.get("opcode") not in {
            "backend.stage",
            "runtime.stage",
        }:
            raise StageExecutionError("stage operation is unsupported")
        if not isinstance(stage_context, Mapping):
            raise StageExecutionError("stage execution context is incomplete")
        if not set(stage_context) >= _ENGINE_IDENTITY_FIELDS:
            raise StageExecutionError("stage execution context omits engine identity")
        _validate_context(stage_context)
        self._backend = backend
        self._operation = MappingProxyType(deepcopy(dict(operation)))
        self._stage_context = MappingProxyType(deepcopy(dict(stage_context)))
        self._identity = {field: self._stage_context[field] for field in _ENGINE_IDENTITY_FIELDS}

    def snapshot(self, phase: str, context: Mapping[str, object]) -> dict[str, Any]:
        result = self._backend.snapshot(phase, context)  # type: ignore[attr-defined]
        if not isinstance(result, dict):
            raise StageExecutionError("backend snapshot must be an object")
        return result

    def verify_rollback_context(self, context: Mapping[str, object]) -> dict[str, Any] | None:
        result = self._backend.verify_rollback_context(context)  # type: ignore[attr-defined]
        if result is not None and not isinstance(result, dict):
            raise StageExecutionError("rollback verification result must be an object or null")
        return result

    def execute(self, phase: str, context: Mapping[str, object]) -> dict[str, Any]:
        if phase == "stage":
            if any(context.get(field) != value for field, value in self._identity.items()):
                raise StageExecutionError("stage engine context identity mismatch")
            return cast(
                dict[str, Any],
                execute_verified_stage(self._backend, self._operation, self._stage_context),
            )
        result = self._backend.execute(phase, context)  # type: ignore[attr-defined]
        if not isinstance(result, dict):
            raise StageExecutionError("backend execution result must be an object")
        return result
