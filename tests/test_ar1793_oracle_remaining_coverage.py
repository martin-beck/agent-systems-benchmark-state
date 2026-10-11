# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Remaining hostile-input coverage for AR-1793 oracle lifecycle gates."""

from __future__ import annotations

import unittest
from typing import Any
from unittest.mock import patch

from tools.oracle_lifecycle import (
    ArtifactRef,
    GateError,
    GateStage,
    InteractionEvent,
    apply_event,
    gate_errors,
    human_session_errors,
)


def _event(
    *, stage: GateStage = GateStage.INTAKE, action: str = "open", disposition: str = "unresolved"
) -> InteractionEvent:
    artifact = ArtifactRef("evidence/ar1793.json", "sha256:" + "a" * 64)
    return InteractionEvent(
        task_id="AR-1793",
        task_revision=1,
        stage=stage,
        action=action,
        disposition=disposition,
        before=(artifact,),
        after=(artifact,),
        public_ref="oracle/ar1793",
        recorded_at="2026-10-11T12:00:00Z",
    )


def _session() -> dict[str, object]:
    return {
        "schema_version": "1.0",
        "session_id": "AWTUI-1793",
        "request_ref": "AWG-1793",
        "activation": "user-decision",
        "status": "presenting",
        "task_revision": 1,
        "tui_contract_version": "1.0",
        "opened_at": "2026-10-11T11:00:00Z",
    }


class OracleRemainingCoverageTests(unittest.TestCase):
    def test_human_session_rejects_each_remaining_shape_and_timestamp_error(self) -> None:
        cases: tuple[tuple[str, object, str], ...] = (
            ("not-object", [], "must be an object"),
            ("unknown-field", {**_session(), "extra": True}, "incomplete or unknown"),
            ("version", {**_session(), "schema_version": "2.0"}, "unsupported"),
            ("session-id", {**_session(), "session_id": "bad"}, "session_id is invalid"),
            ("request-ref", {**_session(), "request_ref": "bad"}, "request_ref is invalid"),
            ("activation", {**_session(), "activation": "automatic"}, "activation or status"),
            ("opened-type", {**_session(), "opened_at": 1}, "opened_at is invalid"),
            (
                "opened-naive",
                {**_session(), "opened_at": "2026-10-11T11:00:00"},
                "requires a timezone",
            ),
        )

        for name, session, expected in cases:
            with self.subTest(name=name):
                self.assertIn(expected, human_session_errors(session)[0])

    def test_event_record_rejects_boolean_revision(self) -> None:
        record = _event().as_record()
        record["task_revision"] = True

        with self.assertRaisesRegex(GateError, "task_revision is invalid"):
            InteractionEvent.from_record(record)

    def test_gate_and_apply_event_propagate_invalid_human_session_errors(self) -> None:
        gate: dict[str, Any] = {
            "required": True,
            "open_stage": None,
            "completed": [],
            "events": [],
            "human_session": "not-a-session",
        }
        self.assertEqual(["oracle_gate.human_session must be an object"], gate_errors(gate))

        meta: dict[str, Any] = {"id": "AR-1793", "task_revision": 1}
        invalid_session = {**_session(), "status": "automatic"}
        with self.assertRaisesRegex(GateError, "activation or status"):
            apply_event(meta, _event(), invalid_session)

    def test_defensive_sequence_mismatch_rejects_event_after_validation_fixture(self) -> None:
        meta: dict[str, Any] = {
            "id": "AR-1793",
            "task_revision": 1,
            "oracle_gate": {
                "required": True,
                "stage_sequence": ["role"],
                "open_stage": "intake",
                "completed": [],
                "events": [],
            },
        }
        with (
            patch("tools.oracle_lifecycle.gate_errors", return_value=[]),
            self.assertRaisesRegex(GateError, "unknown interaction gate stage"),
        ):
            apply_event(meta, _event())

    def test_resolved_session_is_not_closed_again_when_another_gate_resolves(self) -> None:
        session = {**_session(), "status": "resolved", "closed_at": "2026-10-11T11:30:00Z"}
        meta: dict[str, Any] = {
            "id": "AR-1793",
            "task_revision": 1,
            "oracle_gate": {
                "required": True,
                "open_stage": "intake",
                "completed": [],
                "events": [_event().as_record()],
                "human_session": session,
            },
        }

        apply_event(meta, _event(action="resolve", disposition="accepted"))

        self.assertEqual(session, meta["oracle_gate"]["human_session"])
        self.assertIsNone(meta["oracle_gate"]["open_stage"])


if __name__ == "__main__":
    unittest.main()
