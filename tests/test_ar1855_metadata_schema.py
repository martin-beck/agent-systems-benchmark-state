# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Positive and hostile coverage for the AR-1850 metadata repair."""

from __future__ import annotations

import json
import unittest
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parent.parent


def _schema() -> dict[str, object]:
    return json.loads((ROOT / "schema/task-schema.json").read_text(encoding="utf-8"))


def _task() -> dict[str, object]:
    text = (ROOT / "tasks/AR-1850-development-tui-interactive-lifetime.md").read_text(
        encoding="utf-8"
    )
    end = text.index("\n---\n", 4)
    return json.loads(text[4:end])


class Ar1855MetadataSchemaTests(unittest.TestCase):
    def test_repaired_dirty_count_is_an_integer_zero(self) -> None:
        record = _task()
        self.assertEqual(record["observed_dirty"], 0)
        self.assertIs(type(record["observed_dirty"]), int)
        jsonschema.Draft202012Validator(_schema()).validate(record)


    def test_boolean_dirty_observation_is_rejected(self) -> None:
        record = _task()
        record["observed_dirty"] = False
        errors = list(jsonschema.Draft202012Validator(_schema()).iter_errors(record))
        self.assertTrue(any(error.path and error.path[-1] == "observed_dirty" for error in errors))


if __name__ == "__main__":
    unittest.main()
