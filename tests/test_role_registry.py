# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Positive and hostile tests for the role registry contract."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from typing import Any

from tools.role_registry import (
    RoleRegistryError,
    _load_json,
    check_registry,
    registry_errors,
    validate_registry,
)

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "examples/roles"


def load_fixture(name: str) -> dict[str, Any]:
    value = json.loads((FIXTURES / name).read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise TypeError("fixture must be an object")
    return value


class RoleRegistryTests(unittest.TestCase):
    def test_positive_registry_fixture_is_valid(self) -> None:
        registry = validate_registry(load_fixture("role-registry.json"))
        self.assertEqual("implementer", registry["default_role"])

    def test_hostile_fixtures_fail_closed(self) -> None:
        for fixture, message in (
            ("hostile-unknown-field.json", "schema:"),
            ("hostile-malformed-capability.json", "schema:"),
            ("hostile-forbidden-alias.json", "forbidden role alias"),
        ):
            with self.subTest(fixture=fixture), self.assertRaisesRegex(RoleRegistryError, message):
                validate_registry(load_fixture(fixture))

    def test_unknown_and_duplicate_capability_actions_fail_closed(self) -> None:
        registry = load_fixture("role-registry.json")
        self.assertIsInstance(registry, dict)
        registry["roles"][0]["capabilities"][0]["actions"].append("unknown.action")
        registry["roles"][0]["forbidden_actions"].append("unknown.action")
        errors = registry_errors(registry)
        self.assertTrue(any("capability action is forbidden" in error for error in errors))

    def test_duplicate_role_and_capability_ids_are_rejected(self) -> None:
        registry = load_fixture("role-registry.json")
        self.assertIsInstance(registry, dict)
        registry["roles"].append(registry["roles"][0])
        errors = registry_errors(registry)
        self.assertIn("semantic: role_id values must be unique", errors)

    def test_semantic_conflicts_and_file_checker_fail_closed(self) -> None:
        registry = load_fixture("role-registry.json")
        role = registry["roles"][0]
        role["capabilities"].append(dict(role["capabilities"][0]))
        role["forbidden_actions"].append("source.read")
        role["tool_policy"]["allow"].append("authority.commit")
        role["tool_policy"]["deny"].append("authority.commit")
        errors = registry_errors(registry)
        self.assertTrue(any("duplicate capability_id" in error for error in errors))
        self.assertTrue(any("both allowed and forbidden" in error for error in errors))
        self.assertTrue(any("capability action is forbidden" in error for error in errors))
        registry["default_role"] = "missing"
        self.assertIn(
            "semantic: default_role must reference a declared role", registry_errors(registry)
        )
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "registry.json"
            path.write_text(json.dumps(load_fixture("role-registry.json")), encoding="utf-8")
            check_registry(path)
            with self.assertRaises(RoleRegistryError):
                _load_json(Path(directory) / "missing.json")


if __name__ == "__main__":
    unittest.main()
