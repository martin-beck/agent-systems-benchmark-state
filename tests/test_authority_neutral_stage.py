# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Hostile tests for the authority-neutral staged-artifact capability."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools.authority_neutral_stage import (
    BoundStagePhaseAdapter,
    StageExecutionError,
    execute_verified_stage,
)

OPERATION = {"operation_id": "op-1:stage", "opcode": "backend.stage"}


def _context(backend: str = "git") -> dict[str, object]:
    root = Path(tempfile.gettempdir()).resolve() / "coordinator-artifacts"
    return {
        "schema_version": 2,
        "backend": backend,
        "project_id": "project",
        "operation_id": "op-1",
        "state_revision": 1,
        "authority_revision": "authority",
        "fencing_token": "fence",
        "fencing_owner": "owner",
        "durable_barrier_id": "barrier",
        "artifact_root": str(root),
        "source": "source",
        "destination": str(root / "backup"),
        "manifest": "manifest",
        "selector_ref": "selector",
        "barrier_identity_digest": "digest",
        "target": "new",
        "envelope_digest": "envelope",
        "runtime_root": str(root / "runtime"),
        "manifest_digest": "a" * 64,
        "binding": {"project_id": "project"},
    }


class _Backend:
    def snapshot(self, phase: str, _context: object) -> dict[str, object]:
        return {"phase": phase}

    def verify_rollback_context(self, _context: object) -> dict[str, object] | None:
        return None

    def execute(self, phase: str, _context: object) -> dict[str, object]:
        return {"phase": phase, "mutates_authority": False}


class AuthorityNeutralStageTests(unittest.TestCase):
    def test_verified_stage_returns_non_mutating_evidence(self) -> None:
        context = _context()
        with patch("tools.authority_neutral_stage.verify_runtime_manifest", return_value=True):
            result = execute_verified_stage(_Backend(), OPERATION, context)
        self.assertTrue(result["staged_verified"])
        self.assertFalse(result["mutates_authority"])

    def test_sqlite_uses_same_artifact_contract(self) -> None:
        context = _context("sqlite")
        with patch("tools.authority_neutral_stage.verify_runtime_manifest", return_value=True):
            result = execute_verified_stage(_Backend(), OPERATION, context)
        self.assertEqual("sqlite", result["backend"])

    def test_rejects_invalid_operation_and_context(self) -> None:
        with self.assertRaisesRegex(StageExecutionError, "unsupported"):
            execute_verified_stage(_Backend(), {"opcode": "backend.commit"}, _context())
        with self.assertRaisesRegex(StageExecutionError, "incomplete"):
            execute_verified_stage(_Backend(), OPERATION, {})
        context = _context()
        context["target"] = "rollback"
        with self.assertRaisesRegex(StageExecutionError, "identity"):
            execute_verified_stage(_Backend(), OPERATION, context)
        context = _context()
        context["binding"] = []
        with self.assertRaisesRegex(StageExecutionError, "binding"):
            execute_verified_stage(_Backend(), OPERATION, context)

    def test_rejects_artifact_escape_and_bad_digest(self) -> None:
        context = _context()
        context["runtime_root"] = str(Path(str(context["artifact_root"])).parent / "escape")
        with self.assertRaisesRegex(StageExecutionError, "escapes"):
            execute_verified_stage(_Backend(), OPERATION, context)
        context = _context()
        context["manifest_digest"] = object()
        with self.assertRaisesRegex(StageExecutionError, "binding"):
            execute_verified_stage(_Backend(), OPERATION, context)

    def test_wraps_runtime_verification_failure_and_incomplete_result(self) -> None:
        with (
            patch(
                "tools.authority_neutral_stage.verify_runtime_manifest",
                side_effect=RuntimeError("injected"),
            ),
            self.assertRaisesRegex(StageExecutionError, "verification failed"),
        ):
            execute_verified_stage(_Backend(), OPERATION, _context())
        with (
            patch("tools.authority_neutral_stage.verify_runtime_manifest", return_value=False),
            self.assertRaisesRegex(StageExecutionError, "incomplete"),
        ):
            execute_verified_stage(_Backend(), OPERATION, _context())

    def test_bound_adapter_dispatches_stage_and_rejects_drift(self) -> None:
        context = _context()
        adapter = BoundStagePhaseAdapter(_Backend(), OPERATION, context)
        with patch("tools.authority_neutral_stage.verify_runtime_manifest", return_value=True):
            result = adapter.execute("stage", context)
        self.assertEqual("completed", result["outcome"])
        drifted = {**context, "fencing_token": "foreign"}
        with self.assertRaisesRegex(StageExecutionError, "identity mismatch"):
            adapter.execute("stage", drifted)
        self.assertEqual({"phase": "discover"}, adapter.snapshot("discover", context))
        self.assertIsNone(adapter.verify_rollback_context(context))
        self.assertEqual(
            {"phase": "reopen", "mutates_authority": False},
            adapter.execute("reopen", context),
        )

    def test_bound_adapter_rejects_selector_drift_before_runtime_verification(self) -> None:
        context = _context()
        adapter = BoundStagePhaseAdapter(_Backend(), OPERATION, context)
        drifted = {**context, "selector_ref": "foreign-selector"}
        with (
            patch("tools.authority_neutral_stage.verify_runtime_manifest") as verifier,
            self.assertRaisesRegex(StageExecutionError, "identity mismatch"),
        ):
            adapter.execute("stage", drifted)
        verifier.assert_not_called()

    def test_bound_adapter_rejects_bad_constructor_and_backend_shapes(self) -> None:
        context = _context()
        with self.assertRaisesRegex(StageExecutionError, "unsupported"):
            BoundStagePhaseAdapter(_Backend(), {"opcode": "backend.commit"}, context)
        with self.assertRaisesRegex(StageExecutionError, "context is incomplete"):
            BoundStagePhaseAdapter(_Backend(), OPERATION, None)  # type: ignore[arg-type]
        with self.assertRaisesRegex(StageExecutionError, "omits engine identity"):
            BoundStagePhaseAdapter(_Backend(), OPERATION, {"backend": "git"})

        class Invalid:
            def snapshot(self, _phase: str, _context: object) -> str:
                return "bad"

            def verify_rollback_context(self, _context: object) -> str:
                return "bad"

            def execute(self, _phase: str, _context: object) -> str:
                return "bad"

        adapter = BoundStagePhaseAdapter(Invalid(), OPERATION, context)
        with self.assertRaisesRegex(StageExecutionError, "snapshot"):
            adapter.snapshot("discover", context)
        with self.assertRaisesRegex(StageExecutionError, "rollback verification"):
            adapter.verify_rollback_context(context)
        with self.assertRaisesRegex(StageExecutionError, "execution result"):
            adapter.execute("reopen", context)


if __name__ == "__main__":
    unittest.main()
