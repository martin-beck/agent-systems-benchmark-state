# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Focused positive and hostile checks for the task-record vocabulary."""

import copy
import json
import unittest
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker, ValidationError

ROOT = Path(__file__).resolve().parents[1]


def record() -> dict[str, Any]:
    return {
        "schema_version": 1,
        "id": "AR-1864",
        "title": "Align task-record schema vocabulary",
        "status": "in_progress",
        "priority": "P1",
        "summary": "Align execution and retry metadata.",
        "next_action": "Run schema checks.",
        "task_revision": 2,
        "updated_at": "2026-10-13T20:00:00+00:00",
        "owner": "schema-worker",
        "claim_expires": "2026-10-13T22:00:00+00:00",
        "worktree_key": "agent-systems-benchmark-state-ar-1864-schema-vocabulary",
        "branch": "codex/ar1864-schema-vocabulary",
        "checkpoint_commit": "",
        "plan": "../plans/AR-1864-task-record-schema-vocabulary.md",
        "depends_on": [],
        "observed_branch": "main",
        "observed_head": "0123456789abcdef0123456789abcdef01234567",
        "observed_dirty": 0,
        "execution_reservation": {
            "execution_id": "0123456789abcdef0123456789abcdef",
            "owner": "schema-worker",
            "task_revision": 2,
            "envelope_digest": "sha256:" + "a" * 64,
            "command_class": "test",
            "scope_digest": "sha256:" + "b" * 64,
            "argv_digest": "c" * 64,
            "expires_at": "2026-10-13T22:00:00+00:00",
        },
        "retry_circuit": {
            "schema_version": 1,
            "attempts": [],
            "recoveries": [],
            "hold": None,
            "reservations": [],
            "abandoned": [],
        },
    }


class TaskRecordSchemaTests(unittest.TestCase):
    def setUp(self) -> None:
        schema = json.loads((ROOT / "schema/task-record.schema.json").read_text())
        Draft202012Validator.check_schema(schema)
        self.validator = Draft202012Validator(schema, format_checker=FormatChecker())
        state_schema = json.loads((ROOT / "schema/task-schema.json").read_text())
        Draft202012Validator.check_schema(state_schema)
        self.state_validator = Draft202012Validator(state_schema, format_checker=FormatChecker())

    def test_execution_retry_and_standard_metadata_are_accepted(self) -> None:
        coordinator_record = copy.deepcopy(record())
        coordinator_record["observed_dirty"] = False
        self.validator.validate(coordinator_record)
        self.state_validator.validate(record())

    def test_execution_result_and_retry_records_are_accepted(self) -> None:
        value = record()
        value["execution_result"] = {
            "execution_id": "0123456789abcdef0123456789abcdef",
            "owner": "schema-worker",
            "envelope_digest": "sha256:" + "a" * 64,
            "argv_digest": "c" * 64,
            "classification": "EXIT",
            "returncode": 0,
            "recorded_at": "2026-10-13T22:00:00+00:00",
        }
        value["retry_circuit"]["attempts"] = [
            {
                "identity": "sha256:" + "d" * 64,
                "failure": "RETRYABLE",
                "progress_digest": "sha256:" + "e" * 64,
                "task_revision": 2,
                "recorded_at": "2026-10-13T22:00:00+00:00",
                "window": 3,
            }
        ]
        value["retry_circuit"]["recoveries"] = [
            {
                "identity": "sha256:" + "d" * 64,
                "progress_digest": "sha256:" + "e" * 64,
                "kind": "checkpoint",
                "reason": "Saved checkpoint.",
                "task_revision": 2,
                "recorded_at": "2026-10-13T22:01:00+00:00",
                "checkpoint_commit": "0123456789abcdef0123456789abcdef01234567",
            }
        ]
        coordinator_value = copy.deepcopy(value)
        coordinator_value["observed_dirty"] = False
        self.validator.validate(coordinator_value)
        self.state_validator.validate(value)

    def test_unknown_execution_field_is_rejected(self) -> None:
        invalid = record()
        invalid["execution_reservation"]["unexpected"] = True
        with self.assertRaises(ValidationError):
            self.validator.validate(invalid)
        with self.assertRaises(ValidationError):
            self.state_validator.validate(invalid)

        invalid = record()
        invalid["execution_result"] = {
            "execution_id": "0123456789abcdef0123456789abcdef",
            "owner": "schema-worker",
            "envelope_digest": "sha256:" + "a" * 64,
            "argv_digest": "c" * 64,
            "classification": "EXIT",
            "returncode": 0,
            "recorded_at": "2026-10-13T22:00:00+00:00",
            "unexpected": True,
        }
        with self.assertRaises(ValidationError):
            self.validator.validate(invalid)
        with self.assertRaises(ValidationError):
            self.state_validator.validate(invalid)

    def test_unknown_retry_field_is_rejected(self) -> None:
        invalid = record()
        invalid["retry_circuit"]["attempts"] = [
            {
                "identity": "sha256:" + "d" * 64,
                "failure": "RETRYABLE",
                "progress_digest": "sha256:" + "e" * 64,
                "task_revision": 2,
                "recorded_at": "2026-10-13T22:00:00+00:00",
                "window": 3,
                "unexpected": True,
            }
        ]
        with self.assertRaises(ValidationError):
            self.validator.validate(invalid)
        with self.assertRaises(ValidationError):
            self.state_validator.validate(invalid)

    def test_invalid_standard_metadata_is_rejected(self) -> None:
        invalid = record()
        invalid["observed_dirty"] = -1
        with self.assertRaises(ValidationError):
            self.validator.validate(invalid)
        invalid = copy.deepcopy(record())
        invalid["checkpoint_commit"] = "not-a-commit"
        with self.assertRaises(ValidationError):
            self.validator.validate(invalid)

        invalid = copy.deepcopy(record())
        invalid["role"] = "bad role"
        with self.assertRaises(ValidationError):
            self.validator.validate(invalid)

        invalid = copy.deepcopy(record())
        invalid["claim_expires"] = "x" * 41
        with self.assertRaises(ValidationError):
            self.validator.validate(invalid)

    def test_unknown_standard_metadata_is_rejected(self) -> None:
        invalid = record()
        invalid["unrecognized_metadata"] = True
        with self.assertRaises(ValidationError):
            self.validator.validate(invalid)


if __name__ == "__main__":
    unittest.main()
