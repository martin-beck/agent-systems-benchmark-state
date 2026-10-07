# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Hostile and positive contract tests for mandatory interaction gates."""

import unittest
from pathlib import Path
from typing import Any

from tools.oracle_lifecycle import (
    ArtifactRef,
    GateError,
    GateStage,
    InteractionEvent,
    StageGate,
    apply_event,
    gate_errors,
    transition_allowed,
)
from tools.oracle_lifecycle_model import State, check_bounded_model, step


def event(task_revision: int, stage: GateStage, action: str, disposition: str) -> InteractionEvent:
    return InteractionEvent(
        task_id="AR-0022",
        task_revision=task_revision,
        stage=stage,
        action=action,
        disposition=disposition,
        before=(ArtifactRef("plan/before", "sha256:" + "a" * 64),),
        after=(ArtifactRef("plan/after", "sha256:" + "b" * 64),),
        public_ref="oracle/decision-1",
        recorded_at="2026-09-17T00:00:00+00:00",
    )


def stage_event(
    task_revision: int, stage: StageGate, action: str, disposition: str
) -> InteractionEvent:
    return InteractionEvent(
        task_id="AR-0022",
        task_revision=task_revision,
        stage=stage,
        action=action,
        disposition=disposition,
        before=(ArtifactRef("plan/before", "sha256:" + "a" * 64),),
        after=(ArtifactRef("plan/after", "sha256:" + "b" * 64),),
        public_ref="oracle/decision-1",
        recorded_at="2026-09-17T00:00:00+00:00",
    )


class OracleLifecycleTests(unittest.TestCase):
    def test_generic_role_spec_decision_gates_are_ordered_and_authorizing(self) -> None:
        meta: dict[str, Any] = {"id": "AR-0022", "task_revision": 1}
        for stage in StageGate:
            revision = meta["task_revision"]
            apply_event(meta, stage_event(revision, stage, "open", "unresolved"))
            meta["task_revision"] += 1
            apply_event(meta, stage_event(meta["task_revision"], stage, "resolve", "accepted"))
            meta["task_revision"] += 1
        self.assertEqual([item.value for item in StageGate], meta["oracle_gate"]["completed"])
        self.assertTrue(meta["oracle_gate"]["authorized"])

    def test_generic_gate_unknown_stage_and_invalid_sequence_fail_closed(self) -> None:
        valid = stage_event(1, StageGate.ROLE, "open", "accepted").as_record()
        valid["stage"] = "unknown"
        with self.assertRaisesRegex(GateError, "unknown interaction gate stage"):
            InteractionEvent.from_record(valid)
        self.assertTrue(
            gate_errors(
                {
                    "required": True,
                    "stage_sequence": ["role", "role"],
                    "open_stage": None,
                    "completed": [],
                    "events": [],
                }
            )
        )

    def test_formal_model_is_in_required_fast_tier(self) -> None:
        root = Path(__file__).parents[1]
        verify = (root / "formal/handoffctl/verify.sh").read_text(encoding="utf-8")
        attest = (root / "formal/handoffctl/attest.py").read_text(encoding="utf-8")
        # State's verifier dispatches the oracle model through the generic
        # run_model function, while retaining the model-specific name.
        self.assertIn('model}" == "OracleInteractionGates"', verify)
        self.assertIn('"OracleInteractionGates"', attest)

    def test_bounded_model_covers_hostile_and_accepted_traces(self) -> None:
        result = check_bounded_model()
        self.assertGreater(result["accepted"], 0)
        self.assertGreater(result["hostile"], 0)

    def test_complete_ordered_lifecycle_is_typed_and_revision_bound(self) -> None:
        meta: dict[str, Any] = {"id": "AR-0022", "task_revision": 1}
        for stage in GateStage:
            revision = meta["task_revision"]
            apply_event(meta, event(revision, stage, "open", "unresolved"))
            meta["task_revision"] += 1
            apply_event(meta, event(meta["task_revision"], stage, "resolve", "accepted"))
            meta["task_revision"] += 1
        self.assertEqual(
            list(GateStage), [GateStage(item) for item in meta["oracle_gate"]["completed"]]
        )
        self.assertIsNone(meta["oracle_gate"]["open_stage"])

    def test_skipped_gate_and_stale_event_are_rejected(self) -> None:
        meta: dict[str, Any] = {"id": "AR-0022", "task_revision": 3}
        with self.assertRaisesRegex(GateError, "skipped"):
            apply_event(meta, event(3, GateStage.DISCUSSION, "open", "unresolved"))
        with self.assertRaisesRegex(GateError, "stale"):
            apply_event(meta, event(2, GateStage.INTAKE, "open", "unresolved"))

    def test_unresolved_guidance_keeps_gate_open_and_blocks_autonomous_work(self) -> None:
        meta: dict[str, Any] = {"id": "AR-0022", "task_revision": 1}
        apply_event(meta, event(1, GateStage.INTAKE, "open", "unresolved"))
        meta["task_revision"] += 1
        apply_event(meta, event(2, GateStage.INTAKE, "resolve", "unresolved"))
        self.assertEqual("intake", meta["oracle_gate"]["open_stage"])
        with self.assertRaisesRegex(GateError, "unresolved"):
            transition_allowed(meta, "release")
        with self.assertRaisesRegex(GateError, "unresolved"):
            transition_allowed(meta, "run")

    def test_legacy_completed_gate_metadata_remains_compatible(self) -> None:
        legacy = {
            "id": "AR-0022",
            "oracle_gate": {"required": True, "open_stage": None},
        }
        transition_allowed(legacy, "release")

        incomplete = {
            "id": "AR-0022",
            "oracle_gate": {"required": True, "open_stage": None, "completed": []},
        }
        with self.assertRaisesRegex(GateError, "reconciliation"):
            transition_allowed(incomplete, "release")

    def test_public_safe_artifacts_and_event_shape_are_fail_closed(self) -> None:
        with self.assertRaisesRegex(GateError, "public-safe"):
            ArtifactRef("/private/plan", "sha256:" + "a" * 64)
        with self.assertRaisesRegex(GateError, "public-safe"):
            ArtifactRef("plan/../private", "sha256:" + "a" * 64)
        self.assertEqual([], gate_errors(None))
        malformed = {
            "required": True,
            "open_stage": "intake",
            "completed": [],
            "events": [{"secret": "not-an-event"}],
        }
        self.assertTrue(gate_errors(malformed))

    def test_artifact_and_event_validation_rejects_malformed_values(self) -> None:
        with self.assertRaisesRegex(GateError, "digest"):
            ArtifactRef("plan/x", "not-a-digest")
        valid = event(1, GateStage.INTAKE, "open", "accepted").as_record()
        for key in (
            "task_id",
            "task_revision",
            "stage",
            "action",
            "disposition",
            "before",
            "after",
            "public_ref",
            "recorded_at",
        ):
            malformed = dict(valid)
            malformed.pop(key)
            with self.subTest(key=key), self.assertRaises(GateError):
                InteractionEvent.from_record(malformed)
        malformed = dict(valid)
        malformed["stage"] = "unknown"
        with self.assertRaisesRegex(GateError, "stage"):
            InteractionEvent.from_record(malformed)
        malformed = dict(valid)
        malformed["before"] = "not-a-list"
        with self.assertRaisesRegex(GateError, "must be a list"):
            InteractionEvent.from_record(malformed)
        malformed = dict(valid)
        for field in ("before", "after"):
            malformed = dict(valid)
            malformed[field] = [{"ref": "plan/x"}]
            with self.subTest(field=field), self.assertRaisesRegex(GateError, "invalid artifact"):
                InteractionEvent.from_record(malformed)
        for field, value in (
            ("task_id", "bad"),
            ("task_revision", 0),
            ("action", "bad"),
            ("disposition", "bad"),
            ("public_ref", "../secret"),
            ("recorded_at", "2026-09-17T00:00:00"),
        ):
            malformed = dict(valid)
            malformed[field] = value
            with self.subTest(field=field), self.assertRaises(GateError):
                InteractionEvent.from_record(malformed)
        with self.assertRaisesRegex(GateError, "requires before and after"):
            InteractionEvent(
                task_id="AR-0022",
                task_revision=1,
                stage=GateStage.INTAKE,
                action="open",
                disposition="accepted",
                before=(),
                after=(ArtifactRef("plan/after", "sha256:" + "b" * 64),),
                public_ref="oracle/decision-1",
                recorded_at="2026-09-17T00:00:00+00:00",
            )
        with self.assertRaisesRegex(GateError, "recorded_at is invalid"):
            InteractionEvent(
                task_id="AR-0022",
                task_revision=1,
                stage=GateStage.INTAKE,
                action="open",
                disposition="accepted",
                before=(ArtifactRef("plan/before", "sha256:" + "a" * 64),),
                after=(ArtifactRef("plan/after", "sha256:" + "b" * 64),),
                public_ref="oracle/decision-1",
                recorded_at="not-a-timestamp",
            )

    def test_gate_validation_and_transition_reject_invalid_shapes(self) -> None:
        cases: list[Any] = [
            [],
            {"required": False},
            {"required": False, "open_stage": None, "completed": [], "events": []},
            {"required": True, "open_stage": "bad", "completed": [], "events": []},
            {"required": True, "open_stage": None, "completed": ["bad"], "events": []},
            {"required": True, "open_stage": None, "completed": [], "events": [object()]},
            {"required": True, "open_stage": None, "completed": [], "events": [None] * 33},
        ]
        self.assertEqual([], gate_errors(None))
        for value in cases:
            with self.subTest(value=value):
                self.assertTrue(gate_errors(value))
        meta: dict[str, Any] = {
            "id": "AR-0022",
            "task_revision": 1,
            "oracle_gate": {"required": True, "open_stage": None, "completed": [], "events": []},
        }
        transition_allowed(meta, "status")
        with self.assertRaisesRegex(GateError, "already open"):
            apply_event(
                {
                    "id": "AR-0022",
                    "task_revision": 1,
                    "oracle_gate": {
                        "required": True,
                        "open_stage": "intake",
                        "completed": [],
                        "events": [],
                    },
                },
                event(1, GateStage.INTAKE, "open", "accepted"),
            )
        with self.assertRaisesRegex(GateError, "does not match task"):
            apply_event(
                {"id": "AR-0099", "task_revision": 1},
                event(1, GateStage.INTAKE, "open", "accepted"),
            )
        with self.assertRaisesRegex(GateError, "invalid"):
            apply_event(
                {
                    "id": "AR-0022",
                    "task_revision": 1,
                    "oracle_gate": {
                        "required": True,
                        "open_stage": None,
                        "completed": [],
                        "events": [{"bad": True}],
                    },
                },
                event(1, GateStage.INTAKE, "open", "accepted"),
            )

    def test_event_reconciliation_rejects_invalid_order_and_supports_reopen(self) -> None:
        meta: dict[str, Any] = {"id": "AR-0022", "task_revision": 1}
        with self.assertRaisesRegex(GateError, "does not match"):
            apply_event(meta, event(1, GateStage.INTAKE, "resolve", "accepted"))
        apply_event(meta, event(1, GateStage.INTAKE, "open", "accepted"))
        meta["task_revision"] += 1
        apply_event(meta, event(2, GateStage.INTAKE, "resolve", "accepted"))
        meta["task_revision"] += 1
        apply_event(meta, event(3, GateStage.INTAKE, "reopen", "accepted"))
        self.assertEqual("intake", meta["oracle_gate"]["open_stage"])
        meta["task_revision"] += 1
        with self.assertRaisesRegex(GateError, "only a completed"):
            apply_event(meta, event(4, GateStage.DISCUSSION, "reopen", "accepted"))

    def test_event_history_is_bounded_and_model_rejects_hostile_inputs(self) -> None:
        meta: dict[str, Any] = {"id": "AR-0022", "task_revision": 1}
        for stage in GateStage:
            apply_event(meta, event(meta["task_revision"], stage, "open", "accepted"))
            meta["task_revision"] += 1
            apply_event(meta, event(meta["task_revision"], stage, "resolve", "accepted"))
            meta["task_revision"] += 1
        for _ in range(12):
            apply_event(meta, event(meta["task_revision"], GateStage.INTAKE, "reopen", "accepted"))
            meta["task_revision"] += 1
            apply_event(meta, event(meta["task_revision"], GateStage.INTAKE, "resolve", "accepted"))
            meta["task_revision"] += 1
        with self.assertRaisesRegex(GateError, "bounded"):
            apply_event(meta, event(meta["task_revision"], GateStage.INTAKE, "reopen", "accepted"))
        state = State(2, (), "intake")
        with self.assertRaisesRegex(ValueError, "stale"):
            step(state, "open", "intake", 1, "accepted")
        with self.assertRaisesRegex(ValueError, "unresolved"):
            step(state, "release", "intake", 2, "accepted")
        with self.assertRaisesRegex(ValueError, "unknown"):
            step(State(1, (), None), "unknown", "intake", 1, "accepted")

    def test_model_preserves_unresolved_gate_and_accepts_lifecycle_actions(self) -> None:
        state = step(State(1, (), None), "open", "intake", 1, "unresolved")
        unresolved = step(state, "resolve", "intake", 2, "unresolved")
        self.assertEqual(State(3, (), "intake"), unresolved)
        with self.assertRaisesRegex(ValueError, "unresolved"):
            step(unresolved, "claim", "intake", 3, "accepted")
        resolved = step(unresolved, "resolve", "intake", 3, "accepted")
        self.assertEqual(State(4, ("intake",), None), resolved)
        for expected_revision, operation in enumerate(("claim", "run", "release"), start=5):
            with self.subTest(operation=operation):
                resolved = step(resolved, operation, "intake", resolved.revision, "accepted")
                self.assertEqual(expected_revision, resolved.revision)

    def test_non_authorizing_user_dispositions_keep_pause_active(self) -> None:
        for disposition in ("rejected", "clarify", "user-added-option", "contradiction"):
            with self.subTest(disposition=disposition):
                meta: dict[str, Any] = {"id": "AR-0022", "task_revision": 1}
                apply_event(meta, event(1, GateStage.INTAKE, "open", "unresolved"))
                meta["task_revision"] += 1
                apply_event(meta, event(2, GateStage.INTAKE, "resolve", disposition))
                self.assertEqual("intake", meta["oracle_gate"]["open_stage"])
                with self.assertRaisesRegex(GateError, "unresolved"):
                    transition_allowed(meta, "run")

    def test_contradiction_reopens_completed_stage_and_requires_reconciliation(self) -> None:
        meta: dict[str, Any] = {"id": "AR-0022", "task_revision": 1}
        apply_event(meta, event(1, GateStage.INTAKE, "open", "unresolved"))
        meta["task_revision"] += 1
        apply_event(meta, event(2, GateStage.INTAKE, "resolve", "accepted"))
        meta["task_revision"] += 1
        apply_event(meta, event(3, GateStage.INTAKE, "reopen", "contradiction"))
        self.assertEqual([], meta["oracle_gate"]["completed"])
        self.assertFalse(meta["oracle_gate"]["authorized"])
        with self.assertRaisesRegex(GateError, "unresolved"):
            transition_allowed(meta, "release")

    def test_duplicate_and_stale_responses_cannot_advance_a_pause(self) -> None:
        meta: dict[str, Any] = {"id": "AR-0022", "task_revision": 1}
        apply_event(meta, event(1, GateStage.INTAKE, "open", "unresolved"))
        meta["task_revision"] += 1
        apply_event(meta, event(2, GateStage.INTAKE, "resolve", "clarify"))
        meta["task_revision"] += 1
        with self.assertRaisesRegex(GateError, "stale"):
            apply_event(meta, event(2, GateStage.INTAKE, "resolve", "accepted"))
        with self.assertRaisesRegex(GateError, "already open"):
            apply_event(meta, event(3, GateStage.INTAKE, "open", "unresolved"))

    def test_repeated_discussion_is_bounded_and_does_not_authorize_work(self) -> None:
        meta: dict[str, Any] = {"id": "AR-0022", "task_revision": 1}
        apply_event(meta, event(1, GateStage.INTAKE, "open", "unresolved"))
        for _ in range(16):
            meta["task_revision"] += 1
            apply_event(meta, event(meta["task_revision"], GateStage.INTAKE, "resolve", "clarify"))
        with self.assertRaisesRegex(GateError, "repeated discussion"):
            apply_event(meta, event(meta["task_revision"], GateStage.INTAKE, "resolve", "clarify"))


if __name__ == "__main__":
    unittest.main()
