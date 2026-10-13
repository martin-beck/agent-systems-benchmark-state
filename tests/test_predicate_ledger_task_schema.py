# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Strict state-schema coverage for Coordinator predicate evidence ledgers."""

import copy
import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator, ValidationError

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / "schema/task-schema.json").read_text(encoding="utf-8"))
VALIDATOR = Draft202012Validator(SCHEMA)
DIGEST = "sha256:" + "a" * 64


def record() -> dict[str, object]:
    return {
        "schema_version": 1,
        "id": "AR-0001",
        "title": "Predicate ledger fixture",
        "status": "done",
        "priority": "P0",
        "summary": "Strict predicate ledger fixture",
        "next_action": "No further action.",
        "task_revision": 2,
        "updated_at": "2026-10-13T18:00:00+00:00",
        "owner": "",
        "claim_expires": "",
        "worktree_key": "",
        "branch": "",
        "checkpoint_commit": "",
        "plan": "",
        "depends_on": [],
        "evidence_ledger": {
            "candidate_ref": "coordinator.vendor.json",
            "candidate_digest": DIGEST,
            "steps": [
                {
                    "predicate_id": "vendor-parity",
                    "status": "pass",
                    "candidate_ref": "coordinator.vendor.json",
                    "candidate_digest": DIGEST,
                    "evidence_class": "mechanical",
                    "evidence_ref": "coordinator.vendor.json",
                    "evidence_digest": DIGEST,
                    "recorded_task_revision": 2,
                }
            ],
        },
    }


class PredicateLedgerTaskSchemaTests(unittest.TestCase):
    def test_current_ledger_is_admitted(self) -> None:
        VALIDATOR.validate(record())

    def test_unknown_or_malformed_ledger_data_is_rejected(self) -> None:
        value = record()
        value["evidence_ledger"]["unexpected"] = True  # type: ignore[index]
        with self.assertRaises(ValidationError):
            VALIDATOR.validate(value)

        value = record()
        step = value["evidence_ledger"]["steps"][0]  # type: ignore[index]
        step["evidence_digest"] = "invalid"
        with self.assertRaises(ValidationError):
            VALIDATOR.validate(value)

        value = record()
        step = copy.deepcopy(value["evidence_ledger"]["steps"][0])  # type: ignore[index]
        step["unexpected"] = True
        value["evidence_ledger"]["steps"] = [step]  # type: ignore[index]
        with self.assertRaises(ValidationError):
            VALIDATOR.validate(value)


if __name__ == "__main__":
    unittest.main()
