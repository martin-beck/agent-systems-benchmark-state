# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Strict task-schema coverage for the supported oracle_gate contract."""

import copy
import json
import unittest
from pathlib import Path
from typing import Any, cast

from jsonschema import Draft202012Validator, FormatChecker, ValidationError

ROOT = Path(__file__).parents[1]
SCHEMA = json.loads((ROOT / "schema/task-schema.json").read_text(encoding="utf-8"))
VALIDATOR = Draft202012Validator(SCHEMA, format_checker=FormatChecker())


def record(task_id: str) -> dict[str, Any]:
    path = next((ROOT / "tasks").glob(f"{task_id}-*.md"))
    return cast(
        dict[str, Any], json.loads(path.read_text(encoding="utf-8").split("\n---\n", 1)[0][4:])
    )


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

        value = record("AR-1811")
        event = copy.deepcopy(value["oracle_gate"]["events"][0])
        value["oracle_gate"]["events"] = [event] * 33
        with self.assertRaises(ValidationError):
            VALIDATOR.validate(value)
