# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Hierarchy edge, schema, and rollup admission tests."""

from __future__ import annotations

import json
import unittest
from pathlib import Path
from typing import Any

import jsonschema

from tools.hierarchy import hierarchy_errors, open_child_error


def task(
    task_id: str,
    *,
    status: str = "open",
    parent: str = "",
    children: list[str] | None = None,
) -> tuple[Path, dict[str, Any], str]:
    return (
        Path(f"{task_id}.md"),
        {
            "schema_version": 1,
            "id": task_id,
            "title": task_id,
            "status": status,
            "priority": "P1",
            "summary": "summary",
            "next_action": "next",
            "task_revision": 1,
            "updated_at": "2026-09-24T00:00:00+00:00",
            "parent_task_ref": parent,
            "children": [] if children is None else children,
        },
        "# task\n",
    )


class HierarchyTests(unittest.TestCase):
    def test_reciprocal_edge_is_valid(self) -> None:
        self.assertEqual(
            [],
            hierarchy_errors(
                [task("AR-0001", children=["AR-0002"]), task("AR-0002", parent="AR-0001")]
            ),
        )

    def test_malformed_and_one_sided_edges_fail_closed(self) -> None:
        errors = hierarchy_errors([task("AR-0001", children=["bad"]), task("AR-0002")])
        self.assertIn("AR-0001: children must be a list of AR identifiers", errors)
        errors = hierarchy_errors([task("AR-0001", children=["AR-0002"]), task("AR-0002")])
        self.assertIn("AR-0001: child AR-0002 does not point back to parent", errors)

    def test_edge_shape_and_reference_errors_are_explicit(self) -> None:
        malformed = task("AR-0001")[1]
        malformed["children"] = "AR-0002"
        self.assertIn(
            "AR-0001: children must be a list of AR identifiers",
            hierarchy_errors([(Path("AR-0001.md"), malformed, "")]),
        )
        duplicate = task("AR-0001", children=["AR-0002", "AR-0002"])
        self.assertIn("AR-0001: duplicate child AR-0002", hierarchy_errors([duplicate]))
        self_child = task("AR-0001", children=["AR-0001"])
        self.assertIn("AR-0001: task cannot be its own child", hierarchy_errors([self_child]))
        missing_child = task("AR-0001", children=["AR-0002"])
        self.assertIn("AR-0001: missing child task AR-0002", hierarchy_errors([missing_child]))

    def test_parent_reference_errors_are_explicit(self) -> None:
        invalid = task("AR-0001", parent="not-an-ar")
        self.assertIn("AR-0001: invalid parent_task_ref", hierarchy_errors([invalid]))
        self_parent = task("AR-0001", parent="AR-0001")
        self.assertIn("AR-0001: parent_task_ref self reference", hierarchy_errors([self_parent]))
        missing_parent = task("AR-0001", parent="AR-0002")
        self.assertIn("AR-0001: missing parent task AR-0002", hierarchy_errors([missing_parent]))
        omitted_child = [task("AR-0001"), task("AR-0002", parent="AR-0001")]
        self.assertIn(
            "AR-0002: parent AR-0001 does not list child",
            hierarchy_errors(omitted_child),
        )

    def test_cycles_are_rejected(self) -> None:
        errors = hierarchy_errors(
            [
                task("AR-0001", parent="AR-0002", children=["AR-0002"]),
                task("AR-0002", parent="AR-0001", children=["AR-0001"]),
            ]
        )
        self.assertTrue(any(error.startswith("hierarchy cycle involving") for error in errors))

    def test_done_admission_rejects_open_child(self) -> None:
        parent = task("AR-0001", status="in_progress", children=["AR-0002"])
        child = task("AR-0002", status="open", parent="AR-0001")
        self.assertEqual(
            "AR-0001: cannot complete with open children: AR-0002",
            open_child_error(parent[1], [parent, child]),
        )
        done = task("AR-0002", status="done", parent="AR-0001")
        self.assertIsNone(open_child_error(parent[1], [parent, done]))
        self.assertIsNone(open_child_error(task("AR-0001")[1], [task("AR-0001")]))

    def test_task_schema_accepts_hierarchy(self) -> None:
        schema = json.loads(Path("schema/task-record.schema.json").read_text(encoding="utf-8"))
        record = task("AR-0001", children=["AR-0002"])[1]
        jsonschema.Draft202012Validator(schema).validate(record)


if __name__ == "__main__":
    unittest.main()
