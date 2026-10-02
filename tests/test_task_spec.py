# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Positive and hostile task-spec contract tests."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from typing import Any

from tools import handoffctl
from tools.task_spec import done_admission_error, spec_errors, task_spec_errors

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "examples/task-specs"


def load(name: str) -> dict[str, Any]:
    value = json.loads((FIXTURES / name).read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise TypeError("fixture must be an object")
    return value


class TaskSpecTests(unittest.TestCase):
    def _acceptance(self) -> dict[str, Any]:
        return {
            "spec_ref": "examples/task-specs/AR-0070.json",
            "spec_revision": 1,
            "status": "pass",
            "evidence_class": "contract-test",
            "evidence_ref": "awq/evidence/AR-0070",
            "evidence_digest": "sha256:" + "a" * 64,
        }

    def test_valid_spec_and_optional_metadata_are_accepted(self) -> None:
        value = load("AR-0070.json")
        self.assertEqual([], spec_errors(value))
        self.assertEqual(
            [],
            task_spec_errors(
                ROOT,
                {"id": "AR-0070", "spec_ref": value["spec_ref"], "spec_revision": 1},
            ),
        )

    def test_handoffctl_core_validates_bound_metadata(self) -> None:
        meta: dict[str, Any] = {
            "schema_version": 1,
            "id": "AR-0070",
            "title": "Task spec",
            "status": "open",
            "priority": "P0",
            "summary": "summary",
            "next_action": "action",
            "task_revision": 1,
            "updated_at": "2026-01-01T00:00:00+00:00",
            "spec_ref": "examples/task-specs/AR-0070.json",
            "spec_revision": 1,
        }
        self.assertEqual([], handoffctl.basic_task_errors(ROOT / "task.md", meta))

    def test_hostile_specs_fail_closed(self) -> None:
        self.assertTrue(
            any("overlap" in error for error in spec_errors(load("hostile-overlap.json")))
        )

    def test_spec_shape_and_duplicate_collections_fail_closed(self) -> None:
        value = load("AR-0070.json")
        value["definition_of_done"].append(value["definition_of_done"][0])
        value["acceptance_predicates"] = [{"unexpected": "field"}]
        value["inputs"] = [{"id": "bad id", "description": ""}]
        value["outputs"] = [
            {"id": "duplicate", "description": "one"},
            {"id": "duplicate", "description": "two"},
        ]
        errors = spec_errors(value)
        self.assertIn("definition_of_done must not contain duplicates", errors)
        self.assertIn("acceptance_predicates items must contain only id and description", errors)
        self.assertIn("inputs has an invalid id", errors)
        self.assertIn("inputs has an invalid description", errors)
        self.assertIn("outputs ids must be unique", errors)
        self.assertEqual(["spec must be an object"], spec_errors([]))
        self.assertTrue(
            any(
                "unknown evidence class" in error
                for error in spec_errors(load("hostile-unknown-evidence.json"))
            )
        )

    def test_missing_and_partial_metadata_fail_closed(self) -> None:
        self.assertEqual([], task_spec_errors(ROOT, {"id": "AR-0001"}))
        self.assertEqual(
            ["AR-0001: spec_ref is required"],
            task_spec_errors(ROOT, {"id": "AR-0001", "spec_revision": 1}),
        )
        errors = task_spec_errors(
            ROOT,
            {"id": "AR-0001", "spec_ref": "examples/task-specs/AR-0070.json", "spec_revision": 2},
        )
        self.assertIn("AR-0001: spec_revision does not match referenced spec", errors)

    def test_unsafe_missing_and_malformed_references_fail_closed(self) -> None:
        for ref in ("../secret.json", "/absolute/spec.json", "bad ref"):
            with self.subTest(ref=ref):
                errors = task_spec_errors(
                    ROOT, {"id": "AR-0001", "spec_ref": ref, "spec_revision": 1}
                )
                self.assertTrue(any("spec_ref is unsafe" in error for error in errors))
        missing = task_spec_errors(
            ROOT,
            {"id": "AR-0001", "spec_ref": "examples/task-specs/missing.json", "spec_revision": 1},
        )
        self.assertTrue(any("cannot read spec_ref" in error for error in missing))
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "bad.json"
            path.write_text("{", encoding="utf-8")
            errors = task_spec_errors(
                root, {"id": "AR-0001", "spec_ref": "bad.json", "spec_revision": 1}
            )
            self.assertTrue(any("cannot read spec_ref" in error for error in errors))

    def test_spec_shape_errors_cover_unknown_and_missing_fields(self) -> None:
        errors = spec_errors({"schema_version": 2, "unexpected": True})
        self.assertIn("spec contains unknown field: unexpected", errors)
        self.assertIn("spec missing field: acceptance_predicates", errors)
        self.assertIn("spec schema_version must be 1", errors)

    def test_invalid_revision_and_bound_reference_are_rejected(self) -> None:
        for revision in (True, 0, "1"):
            with self.subTest(revision=revision):
                errors = task_spec_errors(
                    ROOT,
                    {
                        "id": "AR-0001",
                        "spec_ref": "examples/task-specs/AR-0070.json",
                        "spec_revision": revision,
                    },
                )
                self.assertIn("AR-0001: spec_revision must be a positive integer", errors)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            spec = load("AR-0070.json")
            spec["spec_ref"] = "other.json"
            (root / "spec.json").write_text(json.dumps(spec), encoding="utf-8")
            errors = task_spec_errors(
                root, {"id": "AR-0001", "spec_ref": "spec.json", "spec_revision": 1}
            )
            self.assertIn("AR-0001: spec_ref does not match referenced spec", errors)

    def test_done_admission_requires_matching_pass_evidence(self) -> None:
        acceptance = self._acceptance()
        meta: dict[str, Any] = {
            "id": "AR-0070",
            "spec_ref": "examples/task-specs/AR-0070.json",
            "spec_revision": 1,
            "spec_acceptance": acceptance,
        }
        self.assertIsNone(done_admission_error(ROOT, meta))
        for field, value in (("status", "fail"), ("evidence_class", "invented")):
            rejected = dict(acceptance)
            rejected[field] = value
            with self.subTest(field=field):
                self.assertIn(
                    "done admission denied",
                    done_admission_error(ROOT, {**meta, "spec_acceptance": rejected}) or "",
                )
        incomplete = dict(meta)
        incomplete.pop("spec_acceptance")
        self.assertIn("incomplete", done_admission_error(ROOT, incomplete) or "")


if __name__ == "__main__":
    unittest.main()
