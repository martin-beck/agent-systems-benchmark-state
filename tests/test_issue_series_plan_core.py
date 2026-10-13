# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Focused coverage for the pure issue-series planning adapter."""

from __future__ import annotations

import copy
import json
import tempfile
import unittest
from pathlib import Path
from typing import Any
from unittest.mock import patch

from tools.issue_series_plan import IssueSeriesPlanError, plan_issue_series


def manifest() -> dict[str, Any]:
    return {
        "schema_version": 1,
        "repository": "github.com/example/coordinator",
        "issue": {"number": 42, "url": "https://github.com/example/coordinator/issues/42"},
        "issue_digest": "sha256:" + "a" * 64,
        "members": [
            {
                "id": "AR-1000",
                "short_title": "Create plan",
                "scope": "Create a local plan",
                "acceptance": "Focused tests pass",
                "ownership": "Coordinator core",
                "depends_on": [],
            },
            {
                "id": "AR-1001",
                "short_title": "Complete plan",
                "scope": "Complete the local plan",
                "acceptance": "Receipt is canonical",
                "ownership": "Coordinator core",
                "depends_on": [{"id": "AR-1000", "rationale": "Requires the plan"}],
            },
        ],
        "finalizer": "AR-1001",
    }


class IssueSeriesPlanCoreTests(unittest.TestCase):
    def write_manifest(self, value: object) -> Path:
        path = Path(self.temporary.name) / "series.json"
        path.write_text(json.dumps(value, indent=2), encoding="utf-8")
        return path

    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)

    def plan(self, path: Path, **changes: object) -> str:
        arguments: dict[str, object] = {
            "expected_product_slug": "Example/Coordinator",
            "existing_task_ids": (),
            "existing_issue_series_identities": (),
            "current_state_digest": "sha256:" + "b" * 64,
        }
        arguments.update(changes)
        return plan_issue_series(path, **arguments)  # type: ignore[arg-type]

    def test_positive_plan_is_deterministic_and_canonical(self) -> None:
        path = self.write_manifest(manifest())
        first = self.plan(path)
        second = self.plan(path)
        self.assertEqual(first, second)
        receipt = json.loads(first)
        self.assertEqual(first, json.dumps(receipt, sort_keys=True, separators=(",", ":")))
        self.assertEqual("github.com/example/coordinator", receipt["series_identity"]["repository"])
        self.assertEqual(["AR-1000", "AR-1001"], receipt["task_ids"])
        self.assertEqual("sha256:" + "b" * 64, receipt["current_state_digest"])
        self.assertRegex(receipt["manifest_digest"], r"^sha256:[0-9a-f]{64}$")

    def test_missing_or_malformed_manifest_fails_closed(self) -> None:
        missing = Path(self.temporary.name) / "missing.json"
        with self.assertRaisesRegex(IssueSeriesPlanError, "does not exist"):
            self.plan(missing)
        malformed = self.write_manifest("not-json")
        malformed.write_text("{", encoding="utf-8")
        with self.assertRaisesRegex(IssueSeriesPlanError, "not valid JSON"):
            self.plan(malformed)

    def test_semantically_invalid_manifest_cannot_be_planned(self) -> None:
        value = manifest()
        value["schema_version"] = 2
        with self.assertRaisesRegex(IssueSeriesPlanError, "schema_version"):
            self.plan(self.write_manifest(value))

    def test_manifest_transport_and_receipt_inputs_are_bounded(self) -> None:
        directory = Path(self.temporary.name) / "directory"
        directory.mkdir()
        with self.assertRaisesRegex(IssueSeriesPlanError, "not a file"):
            self.plan(directory)
        invalid_utf8 = Path(self.temporary.name) / "invalid-utf8.json"
        invalid_utf8.write_bytes(b"\xff")
        with self.assertRaisesRegex(IssueSeriesPlanError, "not UTF-8"):
            self.plan(invalid_utf8)
        path = self.write_manifest(manifest())
        for digest in ("", "sha256:" + "A" * 64, "sha256:" + "a" * 63):
            with (
                self.subTest(digest=digest),
                self.assertRaisesRegex(IssueSeriesPlanError, "current state digest"),
            ):
                self.plan(path, current_state_digest=digest)
        receipt = json.loads(
            self.plan(path, expected_product_slug="https://github.com/Example/Coordinator")
        )
        self.assertEqual("github.com/example/coordinator", receipt["series_identity"]["repository"])

    def test_malformed_existing_identity_cannot_authorize_duplicate_detection(self) -> None:
        path = self.write_manifest(manifest())
        self.assertIsInstance(
            self.plan(
                path,
                existing_issue_series_identities=(
                    {"repository": 42, "issue": {"number": 42}},
                    {"repository": "github.com/example/coordinator", "issue": {"number": True}},
                ),
            ),
            str,
        )

    def test_unreadable_manifest_and_invalid_existing_identities_fail_closed(self) -> None:
        path = self.write_manifest(manifest())
        with (
            patch.object(Path, "read_text", side_effect=OSError("denied")),
            self.assertRaisesRegex(IssueSeriesPlanError, "cannot be read"),
        ):
            self.plan(path)
        receipt = self.plan(
            path,
            existing_issue_series_identities=(
                [],
                {"repository": "not a repository", "issue_number": 42},
                {"repository": "example/coordinator", "issue_number": True},
                {"repository": "example/coordinator", "issue_number": "42"},
            ),
        )
        self.assertIn("series_identity", receipt)

    def test_wrong_product_repository_is_rejected(self) -> None:
        value = manifest()
        value["repository"] = "github.com/example/other"
        value["issue"]["url"] = "https://github.com/example/other/issues/42"
        with self.assertRaisesRegex(IssueSeriesPlanError, "expected product slug"):
            self.plan(self.write_manifest(value))

    def test_existing_task_identifier_is_rejected(self) -> None:
        with self.assertRaisesRegex(IssueSeriesPlanError, "identifiers already exist"):
            self.plan(self.write_manifest(manifest()), existing_task_ids=("AR-1000", "AR-9999"))

    def test_existing_issue_identity_is_rejected(self) -> None:
        identity = {"repository": "Example/Coordinator", "issue": {"number": 42}}
        with self.assertRaisesRegex(IssueSeriesPlanError, "identity already has a series"):
            self.plan(
                self.write_manifest(copy.deepcopy(manifest())),
                existing_issue_series_identities=(identity,),
            )
