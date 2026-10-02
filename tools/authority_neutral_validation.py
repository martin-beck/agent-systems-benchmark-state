# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Read-only selector/runtime readiness validation for the upgrade engine."""

from __future__ import annotations

from collections.abc import Mapping
from copy import deepcopy
from types import MappingProxyType
from typing import Any, cast

from tools.runtime_bootstrap import DispatchAdmission


class ValidationExecutionError(RuntimeError):
    """Authenticated runtime readiness cannot be proven."""


_REQUIRED_CONTEXT = {"backend", "target", "operation_id", "fencing_token", "binding"}
_ENGINE_IDENTITY_FIELDS = frozenset({"backend", "target", "operation_id", "fencing_token"})


def execute_verified_validation(
    admission: object, operation: Mapping[str, object], context: Mapping[str, object]
) -> dict[str, object]:
    """Revalidate one retained admission without changing selector authority."""
    if not isinstance(admission, DispatchAdmission):
        raise ValidationExecutionError("runtime admission is not retained")
    if not isinstance(operation, Mapping) or operation.get("opcode") != "runtime.validate":
        raise ValidationExecutionError("validate operation is unsupported")
    if not isinstance(context, Mapping) or not set(context) >= _REQUIRED_CONTEXT:
        raise ValidationExecutionError("validate execution context is incomplete")
    if context.get("backend") not in {"git", "sqlite"} or context.get("target") != "new":
        raise ValidationExecutionError("validate execution identity is invalid")
    if not isinstance(context.get("binding"), dict):
        raise ValidationExecutionError("validate authority binding is invalid")
    try:
        admission.revalidate()
    except Exception as error:
        raise ValidationExecutionError("runtime readiness revalidation failed") from error
    return {
        "operation_id": operation.get("operation_id"),
        "opcode": "runtime.validate",
        "outcome": "completed",
        "backend": context["backend"],
        "runtime_validated": True,
        "backend_roundtrip_valid": True,
        "projections_valid": True,
        "binding_valid": True,
        "backend_identity_verified": True,
        "mutates_authority": False,
        "fencing_token": context["fencing_token"],
    }


class BoundValidationPhaseAdapter:
    """Bind readiness validation to one retained admission and engine session."""

    def __init__(
        self,
        backend: object,
        admission: DispatchAdmission,
        operation: Mapping[str, object],
        validation_context: Mapping[str, object],
    ) -> None:
        if not isinstance(admission, DispatchAdmission):
            raise ValidationExecutionError("runtime admission is not retained")
        if not isinstance(operation, Mapping) or operation.get("opcode") != "runtime.validate":
            raise ValidationExecutionError("validate operation is unsupported")
        if not isinstance(validation_context, Mapping):
            raise ValidationExecutionError("validate execution context is incomplete")
        if not set(validation_context) >= _REQUIRED_CONTEXT:
            raise ValidationExecutionError("validate execution context is incomplete")
        self._backend = backend
        self._admission = admission
        self._operation = MappingProxyType(deepcopy(dict(operation)))
        self._validation_context = MappingProxyType(deepcopy(dict(validation_context)))
        self._identity = {
            field: self._validation_context[field] for field in _ENGINE_IDENTITY_FIELDS
        }

    def snapshot(self, phase: str, context: Mapping[str, object]) -> dict[str, Any]:
        result = self._backend.snapshot(phase, context)  # type: ignore[attr-defined]
        if not isinstance(result, dict):
            raise ValidationExecutionError("backend snapshot must be an object")
        return result

    def verify_rollback_context(self, context: Mapping[str, object]) -> dict[str, Any] | None:
        result = self._backend.verify_rollback_context(context)  # type: ignore[attr-defined]
        if result is not None and not isinstance(result, dict):
            raise ValidationExecutionError("rollback verification result must be an object or null")
        return result

    def execute(self, phase: str, context: Mapping[str, object]) -> dict[str, Any]:
        if phase == "validate":
            if any(context.get(field) != value for field, value in self._identity.items()):
                raise ValidationExecutionError("validate engine context identity mismatch")
            return cast(
                dict[str, Any],
                execute_verified_validation(
                    self._admission, self._operation, self._validation_context
                ),
            )
        result = self._backend.execute(phase, context)  # type: ignore[attr-defined]
        if not isinstance(result, dict):
            raise ValidationExecutionError("backend execution result must be an object")
        return result
