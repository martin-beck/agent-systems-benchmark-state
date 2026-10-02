# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Hostile tests for the bounded internal rollback adapter."""

from __future__ import annotations

import unittest
from typing import Any, cast

from tools.authority_mutation import DurableBoundBackendMutation, MutationReceipt
from tools.authority_neutral_rollback_dispatch import (
    BoundRollbackPhaseAdapter,
    RollbackDispatchError,
)

OPERATION = {
    "operation_id": "upgrade-1:rollback",
    "opcode": "backend.restore",
    "inputs": {
        "backend": "git",
        "target": "rollback",
        "selector_ref": ".runtime/runtime-selector.json",
        "expected_state_revision": 7,
        "barrier_id": "barrier-7",
        "fencing_token": "fence-7",
        "backup_operation_id": "upgrade-1:backup",
    },
    "timeout_seconds": 300,
    "resources": ["maintenance-barrier", "durable-operation-record"],
    "preconditions": ["failed-upgrade", "verified-backup"],
    "postconditions": ["old-runtime-restored"],
    "evidence": ["durable-operation-record"],
    "durable_record": "operation-id-and-outcome",
}
CONTEXT = {
    "backend": "git",
    "target": "rollback",
    "selector_ref": ".runtime/runtime-selector.json",
    "operation_id": "upgrade-1:rollback",
    "state_revision": 7,
    "durable_barrier_id": "barrier-7",
    "fencing_token": "fence-7",
}


def receipt() -> MutationReceipt:
    return MutationReceipt(
        backend="git",
        target="rollback",
        operation_id="upgrade-1:rollback",
        state_revision=7,
        barrier_id="barrier-7",
        artifact_identity="artifact",
        manifest_identity="manifest",
        selector_identity="selector",
        runtime_identity="runtime",
        fencing_token="fence-7",  # noqa: S106
        mutates_authority=True,
    )


class Executor(DurableBoundBackendMutation):
    def __init__(self) -> None:
        self.calls = 0

    def execute(self, _argument: object) -> MutationReceipt:
        self.calls += 1
        return receipt()


class RollbackDispatchTests(unittest.TestCase):
    def test_consumes_exact_capability_once(self) -> None:
        executor = Executor()
        adapter = BoundRollbackPhaseAdapter(OPERATION, CONTEXT, executor, "effect")
        result = adapter.execute(CONTEXT)
        self.assertEqual(executor.calls, 1)
        self.assertTrue(result["restored_verified"])
        with self.assertRaisesRegex(RollbackDispatchError, "already consumed"):
            adapter.execute(CONTEXT)

    def test_rejects_context_drift_before_effect(self) -> None:
        executor = Executor()
        adapter = BoundRollbackPhaseAdapter(OPERATION, CONTEXT, executor, "effect")
        drifted = {**CONTEXT, "fencing_token": "foreign"}
        with self.assertRaisesRegex(RollbackDispatchError, "identity drifted"):
            adapter.execute(drifted)
        self.assertEqual(executor.calls, 0)

    def test_rejects_wrong_operation_or_receipt(self) -> None:
        with self.assertRaises(RollbackDispatchError):
            BoundRollbackPhaseAdapter(
                {**OPERATION, "opcode": "authority.atomic_replace"},
                CONTEXT,
                Executor(),
                "effect",
            )

        class WrongExecutor(DurableBoundBackendMutation):
            def __init__(self) -> None:
                pass

            def execute(self, argument: object) -> object:  # type: ignore[override]
                return argument

        adapter = BoundRollbackPhaseAdapter(
            OPERATION, CONTEXT, cast(Any, WrongExecutor()), "effect"
        )
        with self.assertRaisesRegex(RollbackDispatchError, "receipt"):
            adapter.execute(CONTEXT)

    def test_rejects_malformed_operation_inputs(self) -> None:
        operation = cast(dict[str, Any], OPERATION)
        cases = [
            ({"extra": True}, "fields"),
            ({**operation, "opcode": "wrong"}, "opcode"),
            ({**operation, "operation_id": ""}, "identity"),
            ({**operation, "inputs": {}}, "inputs"),
            ({**operation, "inputs": {**operation["inputs"], "backend": "other"}}, "target"),
            (
                {**operation, "inputs": {**operation["inputs"], "backup_operation_id": "bad"}},
                "backup",
            ),
            (
                {**operation, "inputs": {**operation["inputs"], "expected_state_revision": 0}},
                "state",
            ),
            ({**operation, "inputs": {**operation["inputs"], "barrier_id": ""}}, "barrier"),
        ]
        for operation, message in cases:
            with (
                self.subTest(message=message),
                self.assertRaisesRegex(RollbackDispatchError, message),
            ):
                BoundRollbackPhaseAdapter(operation, CONTEXT, Executor(), "effect")
        with self.assertRaisesRegex(RollbackDispatchError, "selector reference"):
            base = cast(dict[str, Any], OPERATION)
            invalid = {
                **base,
                "inputs": {**base["inputs"], "selector_ref": ""},
            }
            BoundRollbackPhaseAdapter(invalid, CONTEXT, Executor(), "effect")

    def test_rejects_invalid_context_or_executor(self) -> None:
        with self.assertRaisesRegex(RollbackDispatchError, "context"):
            BoundRollbackPhaseAdapter(OPERATION, None, Executor(), "effect")  # type: ignore[arg-type]
        with self.assertRaisesRegex(RollbackDispatchError, "identity mismatch"):
            BoundRollbackPhaseAdapter(OPERATION, {**CONTEXT, "target": "new"}, Executor(), "effect")
        with self.assertRaisesRegex(RollbackDispatchError, "durable capability"):
            BoundRollbackPhaseAdapter(OPERATION, CONTEXT, object(), "effect")  # type: ignore[arg-type]

    def test_rejects_receipt_identity_or_mutation_flag(self) -> None:
        class BadReceiptExecutor(DurableBoundBackendMutation):
            def __init__(self) -> None:
                pass

            def execute(self, _argument: object) -> MutationReceipt:
                value = receipt()
                return MutationReceipt(**{**value.__dict__, "mutates_authority": False})

        adapter = BoundRollbackPhaseAdapter(OPERATION, CONTEXT, BadReceiptExecutor(), "effect")
        with self.assertRaisesRegex(RollbackDispatchError, "receipt"):
            adapter.execute(CONTEXT)


if __name__ == "__main__":
    unittest.main()
