# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Fail-closed primitive coverage for issue-series planning and publication."""

from __future__ import annotations

import copy
import unittest

from tools.issue_series import IssueSeriesValidationError, parse_manifest
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
        private["members"] = copy.deepcopy(private["members"])
        private["members"][0]["scope"] = "/tmp/private"  # noqa: S108 - hostile input
        cases.append(("private", private))
        title = manifest()
        title["members"] = copy.deepcopy(title["members"])
        title["members"][0]["short_title"] = "one two three four five"  # type: ignore[index]
        cases.append(("title", title))
        cycle = manifest()
        cycle["members"] = copy.deepcopy(cycle["members"])
        cycle["members"][0]["depends_on"] = [{"id": "AR-9001", "rationale": "cycle"}]  # type: ignore[index]
        cases.append(("cycle", cycle))
        duplicate = manifest()
        duplicate["members"] = copy.deepcopy(duplicate["members"])
        duplicate["members"][1]["depends_on"] *= 2  # type: ignore[index]
        cases.append(("duplicate", duplicate))
        unordered = manifest()
        unordered["finalizer"] = "AR-9000"
        cases.append(("finalizer", unordered))
        for label, value in cases:
            with self.subTest(label=label), self.assertRaises(IssueSeriesValidationError):
                parse_manifest(value)

    def test_publication_escapes_and_normalizes_transport_boundaries(self) -> None:
        value = manifest()
        value["members"] = copy.deepcopy(value["members"])
        value["members"][0]["short_title"] = "escape | [title]"  # type: ignore[index]
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
            (REPOSITORY, True, DIGEST),
            (REPOSITORY, 7, "bad"),
        ):
            with (
                self.subTest(repository=repository),
                self.assertRaises(IssueSeriesPublicationError),
            ):
                publication_key(repository, number, digest)  # type: ignore[arg-type]


if __name__ == "__main__":
    unittest.main()
