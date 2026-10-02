# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Bound internal rollback-effect dispatch.

The capability is deliberately internal: public rollback dispatch remains
rejection-only until a later AR supplies the complete operational evidence.
"""

from __future__ import annotations

import posixpath
import re
from collections.abc import Mapping
from copy import deepcopy
from types import MappingProxyType
from typing import Protocol

from tools.authority_mutation import DurableBoundBackendMutation, MutationReceipt


class RollbackDispatchError(RuntimeError):
    """A generated rollback operation cannot be safely dispatched."""


class DurableRollbackExecutor(Protocol):
    def execute(self, argument: object) -> MutationReceipt: ...


_OPERATION_FIELDS = {
    "operation_id",
    "opcode",
    "inputs",
    "timeout_seconds",
    "resources",
    "preconditions",
    "postconditions",
    "evidence",
    "durable_record",
}
_INPUT_FIELDS = {
    "backend",
    "target",
    "selector_ref",
    "expected_state_revision",
    "barrier_id",
    "fencing_token",
    "backup_operation_id",
}
_SELECTOR_REF = re.compile(r"(?!/)(?!.*(?:^|/)\.\.(?:/|$))[A-Za-z0-9._/-]{1,255}")


def _validate_operation(operation: Mapping[str, object]) -> dict[str, object]:  # noqa: C901
    if not isinstance(operation, Mapping) or set(operation) != _OPERATION_FIELDS:
        raise RollbackDispatchError("rollback operation fields are incomplete or unknown")
    if operation.get("opcode") != "backend.restore":
        raise RollbackDispatchError("rollback operation opcode is unsupported")
    operation_id = operation.get("operation_id")
    if not isinstance(operation_id, str) or not operation_id:
        raise RollbackDispatchError("rollback operation identity is invalid")
    inputs = operation.get("inputs")
    if not isinstance(inputs, Mapping) or set(inputs) != _INPUT_FIELDS:
        raise RollbackDispatchError("rollback operation inputs are incomplete or unknown")
    if inputs.get("backend") not in {"git", "sqlite"} or inputs.get("target") != "rollback":
        raise RollbackDispatchError("rollback operation target or backend is invalid")
    selector_ref = inputs.get("selector_ref")
    if (
        not isinstance(selector_ref, str)
        or _SELECTOR_REF.fullmatch(selector_ref) is None
        or posixpath.normpath(selector_ref) != selector_ref
    ):
        raise RollbackDispatchError("rollback operation selector reference is invalid")
    if inputs.get("backup_operation_id") != f"{operation_id.rsplit(':', 1)[0]}:backup":
        raise RollbackDispatchError("rollback operation backup identity is invalid")
    if (
        type(inputs.get("expected_state_revision")) is not int
        or inputs["expected_state_revision"] < 1
    ):
        raise RollbackDispatchError("rollback operation state revision is invalid")
    for field in ("barrier_id", "fencing_token"):
        if not isinstance(inputs.get(field), str) or not inputs[field]:
            raise RollbackDispatchError(f"rollback operation {field} is invalid")
    return dict(operation)


class BoundRollbackPhaseAdapter:
    """Consume one exact, durable rollback capability once."""

    def __init__(
        self,
        operation: Mapping[str, object],
        context: Mapping[str, object],
        executor: DurableRollbackExecutor,
        argument: object,
    ) -> None:
        validated = _validate_operation(operation)
        if not isinstance(context, Mapping):
            raise RollbackDispatchError("rollback context is invalid")
        inputs = validated["inputs"]
        if not isinstance(inputs, Mapping):  # pragma: no cover - operation validation precedes this
            raise RollbackDispatchError("rollback operation inputs are invalid")
        expected = {
            "backend": inputs["backend"],
            "target": "rollback",
            "selector_ref": inputs["selector_ref"],
            "operation_id": validated["operation_id"],
            "state_revision": inputs["expected_state_revision"],
            "durable_barrier_id": inputs["barrier_id"],
            "fencing_token": inputs["fencing_token"],
        }
        for field, value in expected.items():
            if context.get(field) != value:
                raise RollbackDispatchError(f"rollback context identity mismatch: {field}")
        if not isinstance(executor, DurableBoundBackendMutation) or not callable(
            getattr(executor, "execute", None)
        ):
            raise RollbackDispatchError("rollback executor is not a durable capability")
        self._operation = MappingProxyType(deepcopy(dict(validated)))
        self._context = MappingProxyType(deepcopy(dict(context)))
        self._executor = executor
        self._argument = argument
        self._consumed = False

    def execute(self, context: Mapping[str, object]) -> dict[str, object]:
        if self._consumed:
            raise RollbackDispatchError("rollback adapter capability already consumed")
        for field in (
            "backend",
            "target",
            "selector_ref",
            "operation_id",
            "state_revision",
            "durable_barrier_id",
            "fencing_token",
        ):
            expected = self._context[field]
            if context.get(field) != expected or type(context.get(field)) is not type(expected):
                raise RollbackDispatchError(f"rollback context identity drifted: {field}")
        self._consumed = True
        receipt = self._executor.execute(self._argument)
        if not isinstance(receipt, MutationReceipt):
            raise RollbackDispatchError("rollback effect receipt is invalid")
        inputs = self._operation["inputs"]
        if not isinstance(
            inputs, Mapping
        ):  # pragma: no cover - constructor validation precedes this
            raise RollbackDispatchError("rollback operation inputs are invalid")
        expected_receipt = {
            "backend": inputs["backend"],
            "target": "rollback",
            "operation_id": self._operation["operation_id"],
            "state_revision": inputs["expected_state_revision"],
            "barrier_id": inputs["barrier_id"],
            "fencing_token": inputs["fencing_token"],
        }
        if (
            any(getattr(receipt, field, None) != value for field, value in expected_receipt.items())
            or receipt.mutates_authority is not True
        ):
            raise RollbackDispatchError("rollback effect receipt identity is invalid")
        return {
            **dict(context),
            "operation_id": self._operation["operation_id"],
            "phase": "rollback",
            "opcode": self._operation["opcode"],
            "outcome": "completed",
            "authority_effect_verified": True,
            "backend_identity_verified": True,
            "mutates_authority": True,
            "restored_verified": True,
            "runtime_validated": True,
            "backend_roundtrip_valid": True,
            "fencing_token": receipt.fencing_token,
        }
