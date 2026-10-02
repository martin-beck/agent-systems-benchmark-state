# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Synthetic cross-project trace and evidence-boundary tests."""

import unittest
from typing import Any

from tools.oracle_integration import (
    AWGDecision,
    AWQEvidence,
    IntegrationTraceError,
    _event,
    run_synthetic_trace,
)
from tools.oracle_lifecycle import GateError, GateStage, apply_event


def _digest(char: str) -> str:
    return "sha256:" + char * 64


class OracleIntegrationTests(unittest.TestCase):
    def _awg(self, decision: str = "accept") -> AWGDecision:
        return AWGDecision("awg/packet-1", decision, "awg/rationale-1", _digest("c"))

    def _awq(self, status: str = "passed") -> AWQEvidence:
        return AWQEvidence("awq/evidence-1", status, "implementation-test", _digest("d"))

    def test_projection_inputs_are_public_safe_and_typed(self) -> None:
        with self.assertRaisesRegex(IntegrationTraceError, "public-safe"):
            AWGDecision("../private", "accept", "awg/rationale-1", _digest("c"))
        with self.assertRaisesRegex(IntegrationTraceError, "digest"):
            AWGDecision("awg/packet-1", "accept", "awg/rationale-1", "bad")
        with self.assertRaisesRegex(IntegrationTraceError, "decision"):
            AWGDecision("awg/packet-1", "nope", "awg/rationale-1", _digest("c"))
        with self.assertRaisesRegex(IntegrationTraceError, "quality_status"):
            AWQEvidence("awq/evidence-1", "unknown", "implementation-test", _digest("d"))
        with self.assertRaisesRegex(IntegrationTraceError, "evidence_class"):
            AWQEvidence("awq/evidence-1", "passed", "unknown", _digest("d"))
        with self.assertRaisesRegex(IntegrationTraceError, "public-safe"):
            AWQEvidence("/private", "passed", "implementation-test", _digest("d"))

    def test_trace_identity_and_evidence_inputs_fail_closed(self) -> None:
        with self.assertRaisesRegex(IntegrationTraceError, "identity"):
            run_synthetic_trace(task_id="bad", start_revision=1, awg=self._awg(), awq=self._awq())
        with self.assertRaisesRegex(IntegrationTraceError, "identity"):
            run_synthetic_trace(
                task_id="AR-0025", start_revision=0, awg=self._awg(), awq=self._awq()
            )

    def test_complete_synthetic_trace_preserves_three_owners(self) -> None:
        result = run_synthetic_trace(
            task_id="AR-0025", start_revision=7, awg=self._awg(), awq=self._awq()
        )
        self.assertEqual(15, result.final_revision)
        self.assertEqual(8, len(result.event_digests))
        self.assertEqual("awg/packet-1", result.awg_decision_ref)
        self.assertEqual("awq/evidence-1", result.awq_evidence_ref)

    def test_quality_pass_does_not_become_user_intent(self) -> None:
        with self.assertRaisesRegex(IntegrationTraceError, "user decision"):
            run_synthetic_trace(
                task_id="AR-0025", start_revision=1, awg=self._awg("clarify"), awq=self._awq()
            )

    def test_failed_quality_does_not_authorize_workflow(self) -> None:
        with self.assertRaisesRegex(IntegrationTraceError, "quality evidence"):
            run_synthetic_trace(
                task_id="AR-0025", start_revision=1, awg=self._awg(), awq=self._awq("failed")
            )

    def test_skipped_formal_review_and_stale_event_are_rejected(self) -> None:
        meta: dict[str, Any] = {"id": "AR-0025", "task_revision": 1}
        with self.assertRaisesRegex(GateError, "skipped"):
            apply_event(meta, _event("AR-0025", 1, GateStage.RECONCILIATION, "open", "unresolved"))
        with self.assertRaisesRegex(GateError, "stale"):
            apply_event(meta, _event("AR-0025", 2, GateStage.INTAKE, "open", "unresolved"))

    def test_unresolved_guidance_cannot_complete_trace(self) -> None:
        meta: dict[str, Any] = {"id": "AR-0025", "task_revision": 1}
        apply_event(meta, _event("AR-0025", 1, GateStage.INTAKE, "open", "unresolved"))
        meta["task_revision"] = 2
        apply_event(meta, _event("AR-0025", 2, GateStage.INTAKE, "resolve", "unresolved"))
        self.assertFalse(meta["oracle_gate"]["authorized"])


if __name__ == "__main__":
    unittest.main()
