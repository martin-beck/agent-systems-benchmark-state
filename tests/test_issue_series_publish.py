# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Focused evidence for pure, local-first issue-series publication helpers."""

from __future__ import annotations

import copy
import unittest
from typing import Any

from tools.issue_series import parse_manifest
from tools.issue_series_publish import (
    DryRunTransport,
    IssueSeriesPublicationError,
    MockTransport,
    normalize_outcome,
    publication_key,
    render_publication,
)


def source_manifest() -> dict[str, Any]:
    return {
        "schema_version": 1,
        "repository": "github.com/example/coordinator",
        "issue": {"number": 42, "url": "https://github.com/example/coordinator/issues/42"},
        "issue_digest": "sha256:" + "a" * 64,
        "members": [
            {
                "id": "AR-1000",
                "short_title": "Parse [safe] *input*",
                "scope": "Parse a bounded manifest",
                "acceptance": "Focused validator tests pass",
                "ownership": "Coordinator core",
                "depends_on": [],
            },
            {
                "id": "AR-1001",
                "short_title": "Publish series",
                "scope": "Publish only after preflight",
                "acceptance": "Atomic publisher test passes",
                "ownership": "Coordinator core",
                "depends_on": [{"id": "AR-1000", "rationale": "Needs validated input"}],
            },
        ],
        "finalizer": "AR-1001",
    }


class IssueSeriesPublishTests(unittest.TestCase):
    def setUp(self) -> None:
        self.manifest = parse_manifest(source_manifest())
        self.digest = "sha256:" + "b" * 64
        self.key = publication_key(
            self.manifest.repository, self.manifest.issue_number, self.digest
        )

    def test_key_and_render_are_deterministic_public_safe_and_marked(self) -> None:
        rendered = render_publication(self.manifest, self.digest)
        self.assertEqual(rendered, render_publication(copy.deepcopy(self.manifest), self.digest))
        self.assertEqual(64, len(self.key))
        self.assertIn("Parse \\[safe\\] \\*input\\*", rendered)
        self.assertIn(f"digest={self.digest} key={self.key}", rendered)
        self.assertLessEqual(len(rendered), 8192)

    def test_key_rejects_unsafe_identity_and_digest(self) -> None:
        for repository, number, digest in (
            ("github.com/Example/coordinator", 42, self.digest),
            ("example/coordinator", 42, self.digest),
            (self.manifest.repository, True, self.digest),
            (self.manifest.repository, 0, self.digest),
            (self.manifest.repository, 42, "sha256:" + "B" * 64),
        ):
            with (
                self.subTest(repository=repository, number=number, digest=digest),
                self.assertRaises(IssueSeriesPublicationError),
            ):
                publication_key(repository, number, digest)

    def test_dry_run_is_typed_and_has_no_success_receipt(self) -> None:
        result = DryRunTransport().publish(
            self.manifest.repository, self.manifest.issue_number, self.digest, "untrusted markdown"
        )
        self.assertEqual("dry_run", result.status)
        self.assertEqual(self.key, result.publication_key)
        self.assertIsNone(result.comment_id)

    def test_mock_accepts_only_full_exact_identity(self) -> None:
        raw = {
            "status": "published",
            "repository": self.manifest.repository,
            "issue_number": self.manifest.issue_number,
            "manifest_digest": self.digest,
            "publication_key": self.key,
            "comment_id": "1234",
        }
        result = MockTransport(raw).publish(
            self.manifest.repository, self.manifest.issue_number, self.digest, "ignored"
        )
        self.assertEqual(("published", "1234"), (result.status, result.comment_id))
        raw["status"] = "already_published"
        self.assertEqual(
            "already_published",
            MockTransport(raw)
            .publish(self.manifest.repository, self.manifest.issue_number, self.digest, "ignored")
            .status,
        )
        raw["repository"] = "github.com/other/project"
        self.assertEqual(
            "deferred_wrong_identity",
            MockTransport(raw)
            .publish(self.manifest.repository, self.manifest.issue_number, self.digest, "ignored")
            .status,
        )

    def test_normalizes_every_deferred_and_hostile_outcome_fail_closed(self) -> None:
        expected = {
            "unavailable": "deferred_unavailable",
            "unauthorized": "deferred_unauthorized",
            "timeout": "deferred_timeout",
            "conflict": "deferred_conflict",
            "wrong_identity": "deferred_wrong_identity",
            "closed": "deferred_closed",
            "moved": "deferred_moved",
            "ambiguous": "ambiguous",
        }
        for raw, status in expected.items():
            with self.subTest(raw=raw):
                result = normalize_outcome(
                    {"status": raw},
                    repository=self.manifest.repository,
                    issue_number=self.manifest.issue_number,
                    manifest_digest=self.digest,
                )
                self.assertEqual(status, result.status)
                self.assertIsNone(result.comment_id)
        hostile_values: tuple[object, ...] = (None, [], {"status": "success"})
        for hostile in hostile_values:
            with self.subTest(hostile=hostile):
                self.assertEqual(
                    "ambiguous",
                    normalize_outcome(
                        hostile,
                        repository=self.manifest.repository,
                        issue_number=self.manifest.issue_number,
                        manifest_digest=self.digest,
                    ).status,
                )
        self.assertEqual(
            "deferred_wrong_identity",
            normalize_outcome(
                {"status": "published"},
                repository=self.manifest.repository,
                issue_number=self.manifest.issue_number,
                manifest_digest=self.digest,
            ).status,
        )
