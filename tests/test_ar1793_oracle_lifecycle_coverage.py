# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Additional transition and failure coverage for AR-1793 oracle gates."""

from __future__ import annotations

import copy
import unittest
from typing import Any
from unittest.mock import patch

from tools.oracle_lifecycle import (
    MAX_DISCUSSION_ROUNDS,
    ArtifactRef,
    GateError,
    GateStage,
    InteractionEvent,
    apply_event,
    gate_errors,
    human_session_errors,
    transition_allowed,
)


def _event(
    revision: int, action: str, disposition: str, stage: GateStage = GateStage.INTAKE
) -> InteractionEvent:
    artifact = ArtifactRef("evidence/oracle.json", "sha256:" + "a" * 64)
    return InteractionEvent(
        task_id="AR-1793",
        task_revision=revision,
        stage=stage,
        action=action,
        disposition=disposition,
        before=(artifact,),
        after=(artifact,),
        public_ref="oracle/decision-1793",
        recorded_at="2026-10-11T12:00:00Z",
    )


def _session(
    *, status: str = "presenting", revision: int = 1, closed_at: str | None = None
) -> dict[str, object]:
    value: dict[str, object] = {
        "schema_version": "1.0",
        "session_id": "AWTUI-1793",
        "request_ref": "AWG-1793",
        "activation": "user-decision",
        "status": status,
        "task_revision": revision,
        "tui_contract_version": "1.0",
        "opened_at": "2026-10-11T11:00:00+00:00",
    }
    if closed_at is not None:
        value["closed_at"] = closed_at
    return value


class OracleLifecycleCoverageTests(unittest.TestCase):
    def test_presenting_session_blocks_then_resolve_closes_it(self) -> None:
        meta: dict[str, Any] = {"id": "AR-1793", "task_revision": 1}
        apply_event(meta, _event(1, "open", "unresolved"), _session())

        with self.assertRaisesRegex(GateError, "intake"):
            transition_allowed(meta, "release")

        meta["task_revision"] = 2
        apply_event(meta, _event(2, "resolve", "accepted"))
        session = meta["oracle_gate"]["human_session"]
        self.assertEqual("resolved", session["status"])
        self.assertEqual("2026-10-11T12:00:00Z", session["closed_at"])

    def test_transition_blocks_presenting_and_reconciliation_without_open_stage(self) -> None:
        presenting = {
            "oracle_gate": {
                "required": True,
                "open_stage": None,
                "completed": [item.value for item in GateStage],
                "events": [],
                "human_session": _session(),
            }
        }
        with self.assertRaisesRegex(GateError, "presenting"):
            transition_allowed(presenting, "promote")

        reconciliation = {
            "oracle_gate": {
                "required": True,
                "open_stage": None,
                "completed": [item.value for item in GateStage],
                "events": [],
                "reconciliation_required": True,
            }
        }
        with self.assertRaisesRegex(GateError, "reconciliation"):
            transition_allowed(reconciliation, "claim")

    def test_human_session_validation_rejects_closure_and_identity_errors(self) -> None:
        cases: tuple[tuple[str, dict[str, object], str], ...] = (
            ("closed-presenting", _session(closed_at="2026-10-11T12:00:00Z"), "cannot be closed"),
            ("open-resolved", _session(status="resolved"), "lacks closed_at"),
            (
                "bad-revision",
                {**_session(), "task_revision": True},
                "task_revision is invalid",
            ),
            ("bad-time", {**_session(), "opened_at": "not-a-time"}, "opened_at is invalid"),
        )
        for name, value, message in cases:
            with self.subTest(name=name):
                self.assertIn(message, human_session_errors(value)[0])

    def test_human_session_requires_matching_open_event_and_valid_opening(self) -> None:
        gate: dict[str, Any] = {
            "required": True,
            "open_stage": None,
            "completed": [],
            "events": [],
            "human_session": _session(),
        }
        self.assertIn("lacks its opening event", gate_errors(gate)[0])

        meta: dict[str, Any] = {"id": "AR-1793", "task_revision": 1}
        with self.assertRaisesRegex(GateError, "only when opening"):
            apply_event(meta, _event(1, "resolve", "accepted"), _session())
        with self.assertRaisesRegex(GateError, "does not match gate event"):
            apply_event(meta, _event(1, "open", "accepted"), _session(revision=2))

    def test_second_presenting_session_is_rejected(self) -> None:
        meta: dict[str, Any] = {"id": "AR-1793", "task_revision": 1}
        apply_event(meta, _event(1, "open", "unresolved"), _session())
        meta["task_revision"] = 2

        with self.assertRaisesRegex(GateError, "already presenting"):
            apply_event(meta, _event(2, "open", "accepted"), _session(revision=2))

    def test_accepted_reconciliation_clears_pending_reconciliation_requirement(self) -> None:
        meta: dict[str, Any] = {
            "id": "AR-1793",
            "task_revision": 1,
            "oracle_gate": {
                "required": True,
                "open_stage": "reconciliation",
                "completed": ["intake", "discussion", "formal_spec_review"],
                "events": [],
                "reconciliation_required": True,
            },
        }
        apply_event(meta, _event(1, "resolve", "accepted", GateStage.RECONCILIATION))
        self.assertFalse(meta["oracle_gate"]["reconciliation_required"])
        transition_allowed(meta, "run")

    def test_repeated_discussion_limit_rejects_resolve_and_reopen(self) -> None:
        unresolved: dict[str, Any] = {
            "id": "AR-1793",
            "task_revision": 1,
            "oracle_gate": {
                "required": True,
                "open_stage": "intake",
                "completed": [],
                "events": [],
                "discussion_rounds": MAX_DISCUSSION_ROUNDS,
            },
        }
        with self.assertRaisesRegex(GateError, "discussion limit"):
            apply_event(unresolved, _event(1, "resolve", "clarify"))

        reopened: dict[str, Any] = {
            "id": "AR-1793",
            "task_revision": 1,
            "oracle_gate": {
                "required": True,
                "open_stage": None,
                "completed": ["intake"],
                "events": [],
                "discussion_rounds": MAX_DISCUSSION_ROUNDS,
            },
        }
        with self.assertRaisesRegex(GateError, "discussion limit"):
            apply_event(reopened, _event(1, "reopen", "contradiction"))

    def test_event_history_limit_does_not_mutate_metadata_or_write_audit(self) -> None:
        event = _event(1, "open", "unresolved")
        meta: dict[str, Any] = {
            "id": "AR-1793",
            "task_revision": 1,
            "oracle_gate": {
                "required": True,
                "open_stage": None,
                "completed": [],
                "events": [event.as_record()] * 32,
            },
        }
        original = copy.deepcopy(meta)

        with (
            patch("tools.oracle_lifecycle._digest_record") as digest_record,
            self.assertRaisesRegex(GateError, "history is bounded"),
        ):
            apply_event(meta, event)

        self.assertEqual(original, meta)
        digest_record.assert_not_called()


if __name__ == "__main__":
    unittest.main()
