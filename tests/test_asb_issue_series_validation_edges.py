# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Focused rejection coverage for issue-series manifest validation."""

from __future__ import annotations

import copy
import unittest
from typing import Any

from tools.issue_series import IssueSeriesValidationError, parse_manifest

REPOSITORY = "github.com/owner/project"
DIGEST = "sha256:" + "a" * 64


def manifest() -> dict[str, Any]:
    return {
        "schema_version": 1,
        "repository": REPOSITORY,
        "issue": {"number": 7, "url": f"https://{REPOSITORY}/issues/7"},
        "issue_digest": DIGEST,
        "members": [
            {
                "id": "AR-9000",
                "short_title": "Create records",
                "scope": "Create local records",
                "acceptance": "Tests pass",
                "ownership": "Coordinator core",
                "depends_on": [],
            },
            {
                "id": "AR-9001",
                "short_title": "Finalize records",
                "scope": "Finalize local records",
                "acceptance": "Tests pass",
                "ownership": "Coordinator core",
                "depends_on": [{"id": "AR-9000", "rationale": "needs records"}],
            },
        ],
        "finalizer": "AR-9001",
    }


class IssueSeriesValidationEdgeTests(unittest.TestCase):
    def assert_rejected(self, value: object, expression: str) -> None:
        with self.assertRaisesRegex(IssueSeriesValidationError, expression):
            parse_manifest(value)

    def test_rejects_member_and_dependency_shape_errors(self) -> None:
        cases: list[tuple[str, object, str]] = []
        unknown_member = manifest()
        unknown_member["members"][0]["extra"] = "not allowed"
        cases.append(("unknown member", unknown_member, "unknown fields: extra"))
        missing_member = manifest()
        del missing_member["members"][0]["scope"]
        cases.append(("missing member", missing_member, "missing fields: scope"))
        non_list_dependencies = manifest()
        non_list_dependencies["members"][1]["depends_on"] = "AR-9000"
        cases.append(("non-list dependencies", non_list_dependencies, "must be a list"))
        malformed_dependency = manifest()
        malformed_dependency["members"][1]["depends_on"] = [{"id": "AR-9000"}]
        cases.append(("missing rationale", malformed_dependency, "missing fields: rationale"))
        bad_dependency_id = manifest()
        bad_dependency_id["members"][1]["depends_on"] = [
            {"id": "not-an-ar", "rationale": "needs records"}
        ]
        cases.append(("invalid dependency id", bad_dependency_id, "must be an AR identifier"))
        for label, value, expression in cases:
            with self.subTest(label=label):
                self.assert_rejected(value, expression)

    def test_reports_missing_duplicate_self_and_cyclic_dependency_edges(self) -> None:
        missing = manifest()
        missing["members"][1]["depends_on"] = [{"id": "AR-9999", "rationale": "missing"}]
        self.assert_rejected(missing, "missing dependency AR-9999")

        duplicate = manifest()
        edge = {"id": "AR-9000", "rationale": "needs records"}
        duplicate["members"][1]["depends_on"] = [edge, copy.deepcopy(edge)]
        self.assert_rejected(duplicate, "duplicate dependencies")

        self_edge = manifest()
        self_edge["members"][1]["depends_on"] = [{"id": "AR-9001", "rationale": "self"}]
        self.assert_rejected(self_edge, "depends on itself")

        cycle = manifest()
        cycle["members"][0]["depends_on"] = [{"id": "AR-9001", "rationale": "cycle"}]
        self.assert_rejected(cycle, "dependency cycle includes AR-9000")

    def test_requires_finalizer_to_connect_every_member(self) -> None:
        value = manifest()
        value["members"].append(
            {
                "id": "AR-9002",
                "short_title": "Independent work",
                "scope": "Remain disconnected",
                "acceptance": "Tests pass",
                "ownership": "Coordinator core",
                "depends_on": [],
            }
        )
        value["finalizer"] = "AR-9002"
        self.assert_rejected(value, "finalizer AR-9002 must directly depend on AR-9000")


if __name__ == "__main__":
    unittest.main()
