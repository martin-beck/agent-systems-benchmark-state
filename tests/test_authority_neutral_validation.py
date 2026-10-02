# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Hostile tests for selector/runtime readiness validation."""

from __future__ import annotations

import unittest
from typing import cast
from unittest.mock import patch

from tools.authority_neutral_validation import (
    BoundValidationPhaseAdapter,
    ValidationExecutionError,
    execute_verified_validation,
)
from tools.runtime_bootstrap import DispatchAdmission

OPERATION = {"operation_id": "op-1:validate", "opcode": "runtime.validate"}
CONTEXT = {
    "backend": "sqlite",
    "target": "new",
    "operation_id": "op-1",
    "fencing_token": "fence",
    "binding": {"project_id": "project"},
}


def _admission() -> DispatchAdmission:
    return object.__new__(DispatchAdmission)


class _Backend:
    def snapshot(self, phase: str, _context: object) -> dict[str, object]:
        return {"phase": phase}

    def verify_rollback_context(self, _context: object) -> None:
        return None

    def execute(self, phase: str, _context: object) -> dict[str, object]:
        return {"phase": phase, "mutates_authority": False}


class AuthorityNeutralValidationTests(unittest.TestCase):
    def test_revalidates_retained_admission_and_returns_read_only_evidence(self) -> None:
        admission = _admission()
        with patch.object(DispatchAdmission, "revalidate") as revalidate:
            result = execute_verified_validation(admission, OPERATION, CONTEXT)
        revalidate.assert_called_once_with()
        self.assertTrue(result["runtime_validated"])
        self.assertFalse(result["mutates_authority"])

    def test_rejects_forged_admission_operation_context_and_binding(self) -> None:
        with self.assertRaisesRegex(ValidationExecutionError, "not retained"):
            execute_verified_validation(object(), OPERATION, CONTEXT)
        admission = _admission()
        with self.assertRaisesRegex(ValidationExecutionError, "unsupported"):
            execute_verified_validation(admission, {"opcode": "selector.commit"}, CONTEXT)
        with self.assertRaisesRegex(ValidationExecutionError, "incomplete"):
            execute_verified_validation(admission, OPERATION, {})
        invalid = {**CONTEXT, "target": "rollback"}
        with self.assertRaisesRegex(ValidationExecutionError, "identity"):
            execute_verified_validation(admission, OPERATION, invalid)
        invalid = {**CONTEXT, "binding": []}
        with self.assertRaisesRegex(ValidationExecutionError, "binding"):
            execute_verified_validation(admission, OPERATION, invalid)

    def test_revalidation_failure_is_write_closed(self) -> None:
        admission = _admission()
        with (
            patch.object(DispatchAdmission, "revalidate", side_effect=RuntimeError("drift")),
            self.assertRaisesRegex(ValidationExecutionError, "revalidation failed"),
        ):
            execute_verified_validation(admission, OPERATION, CONTEXT)

    def test_bound_adapter_dispatches_validate_and_rejects_drift(self) -> None:
        admission = _admission()
        adapter = BoundValidationPhaseAdapter(_Backend(), admission, OPERATION, CONTEXT)
        with patch.object(DispatchAdmission, "revalidate"):
            result = adapter.execute("validate", CONTEXT)
        self.assertEqual("completed", result["outcome"])
        drifted = {**CONTEXT, "fencing_token": "foreign"}
        with self.assertRaisesRegex(ValidationExecutionError, "identity mismatch"):
            adapter.execute("validate", drifted)
        self.assertEqual({"phase": "stage"}, adapter.snapshot("stage", CONTEXT))
        self.assertIsNone(adapter.verify_rollback_context(CONTEXT))
        self.assertEqual(
            {"phase": "reopen", "mutates_authority": False},
            adapter.execute("reopen", CONTEXT),
        )

    def test_bound_adapter_rejects_bad_shapes(self) -> None:
        with self.assertRaisesRegex(ValidationExecutionError, "not retained"):
            BoundValidationPhaseAdapter(
                _Backend(), cast(DispatchAdmission, object()), OPERATION, CONTEXT
            )
        with self.assertRaisesRegex(ValidationExecutionError, "unsupported"):
            BoundValidationPhaseAdapter(_Backend(), _admission(), {"opcode": "commit"}, CONTEXT)
        with self.assertRaisesRegex(ValidationExecutionError, "incomplete"):
            BoundValidationPhaseAdapter(_Backend(), _admission(), OPERATION, {})

        with self.assertRaisesRegex(ValidationExecutionError, "incomplete"):
            BoundValidationPhaseAdapter(_Backend(), _admission(), OPERATION, None)  # type: ignore[arg-type]

        class BadBackend:
            def snapshot(self, _phase: str, _context: object) -> dict[str, object]:
                return cast(dict[str, object], [])

            def verify_rollback_context(self, _context: object) -> dict[str, object]:
                return cast(dict[str, object], [])

            def execute(self, _phase: str, _context: object) -> dict[str, object]:
                return cast(dict[str, object], [])

        adapter = BoundValidationPhaseAdapter(BadBackend(), _admission(), OPERATION, CONTEXT)
        with self.assertRaisesRegex(ValidationExecutionError, "snapshot"):
            adapter.snapshot("stage", CONTEXT)
        with self.assertRaisesRegex(ValidationExecutionError, "rollback"):
            adapter.verify_rollback_context(CONTEXT)
        with self.assertRaisesRegex(ValidationExecutionError, "execution"):
            adapter.execute("reopen", CONTEXT)


if __name__ == "__main__":
    unittest.main()
