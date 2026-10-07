# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Bound internal commit-phase dispatch for the upgrade effect boundary.

This module composes an already-bound durable backend effect with the generated
``authority.atomic_replace`` operation.  It is intentionally not connected to
the public upgrade CLI: callers must provide a capability created by the
concrete backend adapter, while the CLI accepts neither capabilities nor
handlers.
"""

from __future__ import annotations

from collections.abc import Mapping
from copy import deepcopy
from types import MappingProxyType
from typing import Protocol

from tools.authority_mutation import DurableBoundBackendMutation, MutationReceipt


class CommitDispatchError(RuntimeError):
    """A generated commit operation cannot be safely dispatched internally."""


class DurableCommitExecutor(Protocol):
    """Already-bound, single-use durable backend effect."""

    def execute(self, argument: object) -> MutationReceipt: ...


_IDENTITY_FIELDS = (
    "backend",
    "target",
    "operation_id",
    "state_revision",
    "barrier_id",
    "fencing_token",
)
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
    "selector_ref",
    "expected_state_revision",
    "barrier_id",
    "fencing_token",
    "backup_operation_id",
}


def _validate_inputs(operation_id: str, inputs: object) -> None:
    if not isinstance(inputs, Mapping) or set(inputs) != _INPUT_FIELDS:
        raise CommitDispatchError("commit operation inputs are incomplete or unknown")
    if inputs.get("backend") not in {"git", "sqlite"}:
        raise CommitDispatchError("commit operation backend is invalid")
    if inputs.get("backup_operation_id") != f"{operation_id.rsplit(':', 1)[0]}:backup":
        raise CommitDispatchError("commit operation backup identity is invalid")
    if (
        type(inputs.get("expected_state_revision")) is not int
        or inputs["expected_state_revision"] < 1
    ):
        raise CommitDispatchError("commit operation state revision is invalid")
    for field in ("selector_ref", "barrier_id", "fencing_token"):
        if not isinstance(inputs.get(field), str) or not inputs[field]:
            raise CommitDispatchError(f"commit operation {field} is invalid")


def _validate_operation(operation: Mapping[str, object]) -> dict[str, object]:
    if not isinstance(operation, Mapping) or set(operation) != _OPERATION_FIELDS:
        raise CommitDispatchError("commit operation fields are incomplete or unknown")
    if operation.get("opcode") != "authority.atomic_replace":
        raise CommitDispatchError("commit operation opcode is unsupported")
    operation_id = operation.get("operation_id")
    if not isinstance(operation_id, str) or not operation_id:
        raise CommitDispatchError("commit operation identity is invalid")
    _validate_inputs(operation_id, operation.get("inputs"))
    return dict(operation)


def _receipt_result(operation: Mapping[str, object], receipt: MutationReceipt) -> dict[str, object]:
    if not isinstance(receipt, MutationReceipt):
        raise CommitDispatchError("commit effect receipt is invalid")
    inputs = operation["inputs"]
    if not isinstance(inputs, Mapping):  # pragma: no cover - operation validation precedes this
        raise CommitDispatchError("commit operation inputs are invalid")
    expected = {
        "backend": inputs["backend"],
        "target": "new",
        "operation_id": operation["operation_id"],
        "state_revision": inputs["expected_state_revision"],
        "barrier_id": inputs["barrier_id"],
        "fencing_token": inputs["fencing_token"],
    }
    actual = {field: getattr(receipt, field, None) for field in expected}
    if actual != expected or receipt.mutates_authority is not True:
        raise CommitDispatchError("commit effect receipt identity is invalid")
    return {
        "operation_id": operation["operation_id"],
        "opcode": operation["opcode"],
        "outcome": "completed",
        "backend": receipt.backend,
        "authority_effect_verified": True,
        "backend_identity_verified": True,
        "mutates_authority": True,
        "fencing_token": receipt.fencing_token,
    }


class BoundCommitPhaseAdapter:
    """Bind one generated commit operation to one consumed durable capability."""

    def __init__(
        self,
        operation: Mapping[str, object],
        context: Mapping[str, object],
        executor: DurableCommitExecutor,
        argument: object,
    ) -> None:
        validated = _validate_operation(operation)
        if not isinstance(context, Mapping):
            raise CommitDispatchError("commit context is invalid")
        inputs = validated["inputs"]
        if not isinstance(inputs, Mapping):  # pragma: no cover - validated above
            raise CommitDispatchError("commit operation inputs are invalid")
        for field, expected in (
            ("backend", inputs["backend"]),
            ("target", "new"),
            ("operation_id", validated["operation_id"]),
            ("state_revision", inputs["expected_state_revision"]),
            ("durable_barrier_id", inputs["barrier_id"]),
            ("fencing_token", inputs["fencing_token"]),
        ):
            if context.get(field) != expected:
                raise CommitDispatchError(f"commit context identity mismatch: {field}")
        if not isinstance(executor, DurableBoundBackendMutation) or not callable(
            getattr(executor, "execute", None)
        ):
            raise CommitDispatchError("commit executor is not a durable capability")
        self._operation = MappingProxyType(deepcopy(dict(validated)))
        self._context = MappingProxyType(deepcopy(dict(context)))
        self._executor = executor
        self._argument = argument
        self._consumed = False

    def execute(self, phase: str, context: Mapping[str, object]) -> dict[str, object]:
        if self._consumed:
            raise CommitDispatchError("commit adapter capability already consumed")
        if phase != "commit":
            raise CommitDispatchError("commit adapter phase is unsupported")
        for field in (
            "backend",
            "target",
            "operation_id",
            "state_revision",
            "durable_barrier_id",
            "fencing_token",
        ):
            expected = self._context[field]
            if context.get(field) != expected or type(context.get(field)) is not type(expected):
                raise CommitDispatchError(f"commit context identity drifted: {field}")
        self._consumed = True
        receipt = self._executor.execute(self._argument)
        return _receipt_result(self._operation, receipt)
