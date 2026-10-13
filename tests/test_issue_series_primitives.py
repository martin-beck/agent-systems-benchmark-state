# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Fail-closed primitive coverage for issue-series planning and publication."""

from __future__ import annotations

import copy
import json
import tempfile
import unittest
from pathlib import Path
from typing import cast

from tools.issue_series import IssueSeriesValidationError, parse_manifest
from tools.issue_series_plan import IssueSeriesPlanError, plan_issue_series
from tools.issue_series_publish import (
    IssueSeriesPublicationError,
    normalize_outcome,
    publication_key,
    render_publication,
)

DIGEST = "sha256:" + "a" * 64
REPOSITORY = "github.com/owner/project"


def manifest() -> dict[str, object]:
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
                "short_title": "Qualify records",
                "scope": "Qualify local records",
                "acceptance": "Tests pass",
                "ownership": "Coordinator core",
                "depends_on": [{"id": "AR-9000", "rationale": "needs records"}],
            },
        ],
        "finalizer": "AR-9001",
    }


class IssueSeriesPrimitiveTests(unittest.TestCase):
    def test_planning_is_canonical_and_rejects_untrusted_state(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "series.json"
            path.write_text(json.dumps(manifest()), encoding="utf-8")
            receipt = json.loads(
                plan_issue_series(
                    path,
                    expected_product_slug="https://github.com/owner/project",
                    existing_task_ids=[],
                    existing_issue_series_identities=[],
                    current_state_digest=DIGEST,
                )
            )
            self.assertEqual(REPOSITORY, receipt["series_identity"]["repository"])
            self.assertEqual(["AR-9000", "AR-9001"], receipt["task_ids"])
            cases: tuple[tuple[str, str, list[str], list[object], str], ...] = (
                ("slug", "not a slug", [], [], DIGEST),
                ("digest", "https://github.com/owner/project", [], [], "bad"),
                ("task", "https://github.com/owner/project", ["AR-9000"], [], DIGEST),
                (
                    "legacy-identity",
                    "https://github.com/owner/project",
                    [],
                    [{"repository": "owner/project", "issue_number": 7}],
                    DIGEST,
                ),
                (
                    "nested-identity",
                    "https://github.com/owner/project",
                    [],
                    [{"repository": REPOSITORY, "issue": {"number": 7}}],
                    DIGEST,
                ),
            )
            for label, slug, task_ids, identities, digest in cases:
                with self.subTest(label=label), self.assertRaises(IssueSeriesPlanError):
                    plan_issue_series(
                        path,
                        expected_product_slug=slug,
                        existing_task_ids=task_ids,
                        existing_issue_series_identities=identities,
                        current_state_digest=digest,
                    )
            with self.assertRaisesRegex(IssueSeriesPlanError, "does not exist"):
                plan_issue_series(
                    path.with_name("missing.json"),
                    expected_product_slug="https://github.com/owner/project",
                    existing_task_ids=[],
                    existing_issue_series_identities=[],
                    current_state_digest=DIGEST,
                )
            with self.assertRaisesRegex(IssueSeriesPlanError, "not a file"):
                plan_issue_series(
                    Path(directory),
                    expected_product_slug="https://github.com/owner/project",
                    existing_task_ids=[],
                    existing_issue_series_identities=[],
                    current_state_digest=DIGEST,
                )
            path.write_text("not json", encoding="utf-8")
            with self.assertRaisesRegex(IssueSeriesPlanError, "not valid JSON"):
                plan_issue_series(
                    path,
                    expected_product_slug="https://github.com/owner/project",
                    existing_task_ids=[],
                    existing_issue_series_identities=[],
                    current_state_digest=DIGEST,
                )

    def test_manifest_accepts_normalized_tree(self) -> None:
        value = parse_manifest(manifest())
        self.assertEqual(REPOSITORY, value.repository)
        self.assertEqual(("AR-9000", "AR-9001"), tuple(item.id for item in value.members))

    def test_manifest_rejects_hostile_shape_identity_and_graphs(self) -> None:
        cases: list[tuple[str, object]] = [("non-object", [])]
        unknown = manifest()
        unknown["unknown"] = True
        cases.append(("unknown", unknown))
        missing = manifest()
        del missing["issue"]
        cases.append(("missing", missing))
        upper = manifest()
        upper["repository"] = "github.com/Owner/project"
        cases.append(("upper", upper))
        bad_url = manifest()
        bad_url["issue"] = {"number": 7, "url": "https://github.com/owner/project/issues/8"}
        cases.append(("url", bad_url))
        private = manifest()
        private_members = cast(list[dict[str, object]], copy.deepcopy(private["members"]))
        private["members"] = private_members
        private_members[0]["scope"] = "/tmp/private"  # noqa: S108 - hostile input
        cases.append(("private", private))
        title = manifest()
        title_members = cast(list[dict[str, object]], copy.deepcopy(title["members"]))
        title["members"] = title_members
        title_members[0]["short_title"] = "one two three four five"
        cases.append(("title", title))
        cycle = manifest()
        cycle_members = cast(list[dict[str, object]], copy.deepcopy(cycle["members"]))
        cycle["members"] = cycle_members
        cycle_members[0]["depends_on"] = [{"id": "AR-9001", "rationale": "cycle"}]
        cases.append(("cycle", cycle))
        duplicate = manifest()
        duplicate_members = cast(list[dict[str, object]], copy.deepcopy(duplicate["members"]))
        duplicate["members"] = duplicate_members
        dependencies = cast(list[object], duplicate_members[1]["depends_on"])
        duplicate_members[1]["depends_on"] = dependencies * 2
        cases.append(("duplicate", duplicate))
        unordered = manifest()
        unordered["finalizer"] = "AR-9000"
        cases.append(("finalizer", unordered))
        for label, value in cases:
            with self.subTest(label=label), self.assertRaises(IssueSeriesValidationError):
                parse_manifest(value)

    def test_publication_escapes_and_normalizes_transport_boundaries(self) -> None:
        value = manifest()
        members = cast(list[dict[str, object]], copy.deepcopy(value["members"]))
        value["members"] = members
        members[0]["short_title"] = "escape | [title]"
        parsed = parse_manifest(value)
        key = publication_key(REPOSITORY, 7, DIGEST)
        rendered = render_publication(parsed, DIGEST)
        self.assertIn("escape \\| \\[title\\]", rendered)
        self.assertIn(key, rendered)
        self.assertEqual(
            "ambiguous",
            normalize_outcome(
                None, repository=REPOSITORY, issue_number=7, manifest_digest=DIGEST
            ).status,
        )
        self.assertEqual(
            "deferred_timeout",
            normalize_outcome(
                {"status": "timeout"}, repository=REPOSITORY, issue_number=7, manifest_digest=DIGEST
            ).status,
        )
        self.assertEqual(
            "deferred_wrong_identity",
            normalize_outcome(
                {
                    "status": "published",
                    "repository": REPOSITORY,
                    "issue_number": 7,
                    "manifest_digest": DIGEST,
                    "publication_key": "wrong",
                    "comment_id": "42",
                },
                repository=REPOSITORY,
                issue_number=7,
                manifest_digest=DIGEST,
            ).status,
        )
        published = normalize_outcome(
            {
                "status": "published",
                "repository": REPOSITORY,
                "issue_number": 7,
                "manifest_digest": DIGEST,
                "publication_key": key,
                "comment_id": "42",
            },
            repository=REPOSITORY,
            issue_number=7,
            manifest_digest=DIGEST,
        )
        self.assertEqual(("published", "42"), (published.status, published.comment_id))
        for repository, number, digest in (
            ("owner/project", 7, DIGEST),
            (REPOSITORY, cast(int, True), DIGEST),
            (REPOSITORY, 7, "bad"),
        ):
            with (
                self.subTest(repository=repository),
                self.assertRaises(IssueSeriesPublicationError),
            ):
                publication_key(repository, number, digest)


if __name__ == "__main__":
    unittest.main()
