# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Hostile tests for the isolated generated commit-phase adapter."""

from __future__ import annotations

import unittest
from typing import cast

from tools.authority_mutation import DurableBoundBackendMutation, MutationReceipt
from tools.authority_neutral_commit_dispatch import (
    BoundCommitPhaseAdapter,
    CommitDispatchError,
    DurableCommitExecutor,
)

OPERATION = {
    "operation_id": "upgrade-1:commit",
    "opcode": "authority.atomic_replace",
    "inputs": {
        "backend": "git",
        "selector_ref": ".runtime/runtime-selector.json",
        "expected_state_revision": 7,
        "barrier_id": "barrier-7",
        "fencing_token": "fence-7",
        "backup_operation_id": "upgrade-1:backup",
    },
    "timeout_seconds": 300,
    "resources": ["maintenance-barrier", "durable-operation-record"],
    "preconditions": ["previous-phase-complete"],
    "postconditions": ["commit-contract-satisfied"],
    "evidence": ["durable-operation-record"],
    "durable_record": "operation-id-and-outcome",
}
CONTEXT = {
    "backend": "git",
    "target": "new",
    "operation_id": "upgrade-1:commit",
    "state_revision": 7,
    "durable_barrier_id": "barrier-7",
    "fencing_token": "fence-7",
}


class FakeExecutor(DurableBoundBackendMutation):
    def __init__(self, receipt: MutationReceipt) -> None:
        self.receipt = receipt
        self.arguments: list[object] = []

    def execute(self, argument: object) -> MutationReceipt:
        self.arguments.append(argument)
        return self.receipt


class WrongResultExecutor(DurableBoundBackendMutation):
    def __init__(self) -> None:
        pass

    def execute(self, argument: object) -> object:  # type: ignore[override]
        return argument


class NonCallableExecutor(DurableBoundBackendMutation):
    def __init__(self) -> None:
        pass

    execute = None  # type: ignore[assignment]


def receipt(
    *, operation_id: str = "upgrade-1:commit", mutates_authority: bool = True
) -> MutationReceipt:
    return MutationReceipt(
        backend="git",
        target="new",
        operation_id=operation_id,
        state_revision=7,
        barrier_id="barrier-7",
        artifact_identity="artifact",
        manifest_identity="manifest",
        selector_identity="selector",
        runtime_identity="runtime",
        fencing_token="fence-7",  # noqa: S106
        mutates_authority=mutates_authority,
    )


class CommitDispatchTests(unittest.TestCase):
    def assert_constructor_rejects(
        self, operation: object, context: object, executor: object = None
    ) -> None:
        with self.assertRaises(CommitDispatchError):
            BoundCommitPhaseAdapter(
                cast(dict[str, object], operation),
                cast(dict[str, object], context),
                cast(DurableCommitExecutor, executor or FakeExecutor(receipt())),
                object(),
            )

    def test_bound_adapter_dispatches_one_exact_generated_commit(self) -> None:
        executor = FakeExecutor(receipt())
        adapter = BoundCommitPhaseAdapter(OPERATION, CONTEXT, executor, "built-in-effect")
        result = adapter.execute("commit", dict(CONTEXT))
        self.assertTrue(result["authority_effect_verified"])
        self.assertTrue(result["mutates_authority"])
        self.assertEqual(["built-in-effect"], executor.arguments)
        with self.assertRaisesRegex(CommitDispatchError, "already consumed"):
            adapter.execute("commit", dict(CONTEXT))
        self.assertEqual(["built-in-effect"], executor.arguments)

    def test_rejects_phase_identity_and_receipt_drift(self) -> None:
        executor = FakeExecutor(receipt())
        adapter = BoundCommitPhaseAdapter(OPERATION, CONTEXT, executor, object())
        with self.assertRaisesRegex(CommitDispatchError, "phase"):
            adapter.execute("apply", CONTEXT)
        with self.assertRaisesRegex(CommitDispatchError, "identity drifted"):
            adapter.execute("commit", {**CONTEXT, "fencing_token": "foreign"})
        with self.assertRaisesRegex(CommitDispatchError, "receipt identity"):
            BoundCommitPhaseAdapter(
                OPERATION,
                CONTEXT,
                FakeExecutor(receipt(operation_id="foreign")),
                object(),
            ).execute("commit", CONTEXT)

    def test_rejects_non_atomic_or_malformed_operation(self) -> None:
        with self.assertRaisesRegex(CommitDispatchError, "opcode"):
            BoundCommitPhaseAdapter(
                {**OPERATION, "opcode": "backend.restore"},
                CONTEXT,
                FakeExecutor(receipt()),
                object(),
            )
        malformed = dict(OPERATION)
        malformed["inputs"] = dict(
            cast(dict[str, object], OPERATION["inputs"]), backup_operation_id="wrong"
        )
        with self.assertRaisesRegex(CommitDispatchError, "backup identity"):
            BoundCommitPhaseAdapter(malformed, CONTEXT, FakeExecutor(receipt()), object())

    def test_rejects_invalid_operation_shapes_and_inputs(self) -> None:
        self.assert_constructor_rejects({}, CONTEXT)
        self.assert_constructor_rejects({**OPERATION, "operation_id": ""}, CONTEXT)
        for field, value in (
            ("backend", "other"),
            ("expected_state_revision", 0),
            ("expected_state_revision", True),
            ("selector_ref", ""),
            ("barrier_id", None),
            ("fencing_token", 7),
        ):
            inputs = dict(cast(dict[str, object], OPERATION["inputs"]))
            inputs[field] = value
            self.assert_constructor_rejects({**OPERATION, "inputs": inputs}, CONTEXT)
        malformed = dict(OPERATION)
        malformed["inputs"] = "not-a-mapping"
        self.assert_constructor_rejects(malformed, CONTEXT)
        malformed = dict(OPERATION)
        malformed.pop("evidence")
        self.assert_constructor_rejects(malformed, CONTEXT)

    def test_rejects_context_and_executor_binding_errors(self) -> None:
        self.assert_constructor_rejects(OPERATION, "not-a-mapping")
        for field in CONTEXT:
            self.assert_constructor_rejects(
                OPERATION,
                {key: value for key, value in CONTEXT.items() if key != field},
            )
        self.assert_constructor_rejects(OPERATION, CONTEXT, NonCallableExecutor())

    def test_rejects_receipt_shape_and_each_identity_field(self) -> None:
        self.assertRaises(
            CommitDispatchError,
            BoundCommitPhaseAdapter(
                OPERATION,
                CONTEXT,
                cast(DurableCommitExecutor, WrongResultExecutor()),
                object(),
            ).execute,
            "commit",
            CONTEXT,
        )
        for field, value in (
            ("backend", "sqlite"),
            ("target", "rollback"),
            ("operation_id", "foreign"),
            ("state_revision", 8),
            ("barrier_id", "foreign"),
            ("fencing_token", "foreign"),
        ):
            values = {
                "backend": "git",
                "target": "new",
                "operation_id": "upgrade-1:commit",
                "state_revision": 7,
                "barrier_id": "barrier-7",
                "fencing_token": "fence-7",
            }
            values[field] = value
            bad = MutationReceipt(
                backend=cast(str, values["backend"]),
                target=cast(str, values["target"]),
                operation_id=cast(str, values["operation_id"]),
                state_revision=cast(int, values["state_revision"]),
                barrier_id=cast(str, values["barrier_id"]),
                artifact_identity="artifact",
                manifest_identity="manifest",
                selector_identity="selector",
                runtime_identity="runtime",
                fencing_token=cast(str, values["fencing_token"]),
                mutates_authority=True,
            )
            with self.assertRaisesRegex(CommitDispatchError, "receipt identity"):
                BoundCommitPhaseAdapter(OPERATION, CONTEXT, FakeExecutor(bad), object()).execute(
                    "commit", CONTEXT
                )
        with self.assertRaisesRegex(CommitDispatchError, "receipt identity"):
            BoundCommitPhaseAdapter(
                OPERATION, CONTEXT, FakeExecutor(receipt(mutates_authority=False)), object()
            ).execute("commit", CONTEXT)

    def test_executor_failure_consumes_capability(self) -> None:
        class FailingExecutor(DurableBoundBackendMutation):
            def __init__(self) -> None:
                pass

            def execute(self, _argument: object) -> MutationReceipt:
                raise RuntimeError("durable effect failed")

        adapter = BoundCommitPhaseAdapter(OPERATION, CONTEXT, FailingExecutor(), object())
        with self.assertRaisesRegex(RuntimeError, "durable effect failed"):
            adapter.execute("commit", CONTEXT)
        with self.assertRaisesRegex(CommitDispatchError, "already consumed"):
            adapter.execute("commit", CONTEXT)


if __name__ == "__main__":
    unittest.main()
