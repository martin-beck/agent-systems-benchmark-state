# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Strict task-schema coverage for the supported oracle_gate contract."""

import copy
import json
import unittest
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker, ValidationError

ROOT = Path(__file__).parents[1]
SCHEMA = json.loads((ROOT / "schema/task-schema.json").read_text(encoding="utf-8"))
VALIDATOR = Draft202012Validator(SCHEMA, format_checker=FormatChecker())


def record(task_id: str) -> dict[str, Any]:
    """Return a bounded fixture for an archived task record.

    AR-1811 and AR-1813 are intentionally no longer in the generated queue
    after completion. Keep their supported oracle-gate shape as a checked-in
    contract fixture instead of coupling schema tests to generated task
    retention.
    """
    digest = "sha256:" + ("0" if task_id == "AR-1811" else "1") * 64
    event = {
        "task_id": task_id,
        "task_revision": 1,
        "stage": "role",
        "action": "open",
        "disposition": "unresolved",
        "before": [{"ref": "review/base", "digest": digest}],
        "after": [{"ref": "review/candidate", "digest": digest}],
        "public_ref": f"PR-{task_id[3:]}/candidate",
        "recorded_at": "2026-10-12T10:16:21+00:00",
    }
    return {
        "schema_version": 1,
        "id": task_id,
        "title": "Archived oracle gate fixture",
        "status": "done",
        "priority": "P0",
        "summary": "Bounded oracle gate fixture",
        "next_action": "No further action.",
        "task_revision": 1,
        "updated_at": "2026-10-12T10:16:21+00:00",
        "owner": "",
        "claim_expires": "",
        "worktree_key": "",
        "branch": "",
        "checkpoint_commit": "",
        "plan": "",
        "depends_on": [],
        "oracle_gate": {
            "required": True,
            "open_stage": None,
            "completed": ["role", "spec", "decision"],
            "events": [event],
        },
    }


class TaskSchemaOracleGateTests(unittest.TestCase):
    def test_existing_oracle_gate_records_validate_strictly(self) -> None:
        VALIDATOR.validate(record("AR-1811"))
        VALIDATOR.validate(record("AR-1813"))

    def test_unknown_gate_and_event_fields_are_rejected(self) -> None:
        value = record("AR-1811")
        value["oracle_gate"]["unexpected"] = True
        with self.assertRaises(ValidationError):
            VALIDATOR.validate(value)

        value = record("AR-1813")
        value["oracle_gate"]["events"][0]["unexpected"] = True
        with self.assertRaises(ValidationError):
            VALIDATOR.validate(value)

    def test_malformed_event_and_unbounded_events_are_rejected(self) -> None:
        value = record("AR-1813")
        value["oracle_gate"]["events"][0]["before"][0]["digest"] = "not-a-digest"
        with self.assertRaises(ValidationError):
            VALIDATOR.validate(value)

    def test_state_coordinator_worktree_family_is_narrowly_admitted(self) -> None:
        value = record("AR-1811")
        value["worktree_key"] = "asb-state-coordinator-v070-ar1858-coverage-v070"
        VALIDATOR.validate(value)

        value["worktree_key"] = "unrelated-worker"
        with self.assertRaises(ValidationError):
            VALIDATOR.validate(value)

        value = record("AR-1811")
        event = copy.deepcopy(value["oracle_gate"]["events"][0])
        value["oracle_gate"]["events"] = [event] * 33
        with self.assertRaises(ValidationError):
            VALIDATOR.validate(value)
