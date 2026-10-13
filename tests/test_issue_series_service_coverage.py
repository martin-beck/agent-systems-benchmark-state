# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""ASB-owned invariant and error coverage for issue-series service helpers."""

from __future__ import annotations

import json
import subprocess
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Any, cast
from unittest.mock import Mock, patch

from tools import issue_series_service as service
from tools.issue_series_publish import publication_key
from tools.sqlite_storage import SQLiteBackend


def write_atomic(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


class ReceiptBackend:
    def __init__(
        self, series: list[dict[str, object]], publications: list[dict[str, object]]
    ) -> None:
        self.series = series
        self.publications = publications

    def load_issue_series(self) -> list[dict[str, object]]:
        return self.series

    def load_issue_series_publications(self) -> list[dict[str, object]]:
        return self.publications


class IssueSeriesServiceCoverageTests(unittest.TestCase):
    def setUp(self) -> None:
        self.directory = TemporaryDirectory()
        self.root = Path(self.directory.name)
        self.root_patch = patch.object(service, "ROOT", self.root, create=True)
        self.root_patch.start()
        self.addCleanup(self.root_patch.stop)
        self.meta_patch = patch.object(service, "Meta", dict, create=True)
        self.meta_patch.start()
        self.addCleanup(self.meta_patch.stop)
        self.addCleanup(self.directory.cleanup)

    def test_sqlite_projection_export_removes_stale_files_and_preserves_receipts(self) -> None:
        series: dict[str, Any] = {
            "series_identity": {"repository": "github.com/acme/product", "issue_number": 7},
            "manifest": {"schema_version": 1, "members": []},
        }
        key = "a" * 64
        publication: dict[str, object] = {
            "publication_key": key,
            "status": "published",
            "comment_id": "19",
        }
        backend = ReceiptBackend([series], [publication])
        (self.root / "issue-series").mkdir()
        (self.root / "issue-series" / "stale.json").write_text("stale", encoding="utf-8")
        (self.root / "issue-series-publications").mkdir()
        (self.root / "issue-series-publications" / "stale.json").write_text(
            "stale", encoding="utf-8"
        )

        with patch.object(service, "atomic", side_effect=write_atomic, create=True):
            series_paths = service.write_sqlite_issue_series_projections(
                cast(SQLiteBackend, backend)
            )
            publication_paths = service.write_sqlite_issue_series_publication_projections(
                cast(SQLiteBackend, backend)
            )

        self.assertEqual(1, len(series_paths))
        self.assertEqual(
            {"schema_version": 1, "members": []}, json.loads(series_paths[0].read_text())
        )
        self.assertFalse((self.root / "issue-series" / "stale.json").exists())
        self.assertEqual(
            [self.root / "issue-series-publications" / f"{key}.json"], publication_paths
        )
        self.assertEqual(publication, json.loads(publication_paths[0].read_text()))
        self.assertFalse((self.root / "issue-series-publications" / "stale.json").exists())

    def test_git_publication_receipt_rejects_unlinked_or_oversized_projection(self) -> None:
        digest = "sha256:" + "d" * 64
        identity = {"repository": "github.com/acme/product", "issue_number": 7}
        key = publication_key(
            cast(str, identity["repository"]), cast(int, identity["issue_number"]), digest
        )
        directory = self.root / "issue-series-publications"
        directory.mkdir()
        receipt = {"publication_key": key, "manifest_digest": digest, "status": "published"}
        (directory / f"{key}.json").write_text(json.dumps(receipt), encoding="utf-8")
        series = [{"series_identity": identity, "manifest_digest": digest}]

        with patch.object(service, "git_issue_series_receipts", return_value=series):
            reconstructed = service.git_issue_series_publication_receipts([])
        self.assertEqual(
            [
                {
                    "series_identity": identity,
                    "manifest_digest": digest,
                    "publication_key": key,
                    "status": "published",
                    "comment_id": None,
                }
            ],
            reconstructed,
        )

        (directory / "foreign.json").write_text(
            json.dumps({"publication_key": "b" * 64, "manifest_digest": digest}), encoding="utf-8"
        )
        with (
            patch.object(service, "git_issue_series_receipts", return_value=series),
            self.assertRaisesRegex(RuntimeError, "does not match a local series"),
        ):
            service.git_issue_series_publication_receipts([])
        (directory / "foreign.json").unlink()
        oversized = directory / "oversized.json"
        oversized.write_text("x" * 10_001, encoding="utf-8")
        with (
            patch.object(service, "git_issue_series_receipts", return_value=series),
            self.assertRaisesRegex(RuntimeError, "bounded regular file"),
        ):
            service.git_issue_series_publication_receipts([])

    def test_git_publication_record_and_resolution_are_idempotent_but_fail_closed(self) -> None:
        key = "c" * 64
        pending = {
            "publication_key": key,
            "manifest_digest": "sha256:" + "e" * 64,
            "status": "ambiguous",
        }
        final = {**pending, "status": "published", "comment_id": "23"}
        with (
            patch.object(service, "atomic", side_effect=write_atomic, create=True),
            patch.object(service, "commit", return_value=True, create=True) as commit,
            patch.object(service, "push_replica", create=True) as push,
        ):
            service._git_record_issue_series_publication(pending)
            service._git_record_issue_series_publication(pending)
            service._git_resolve_issue_series_publication(final)
            service._git_resolve_issue_series_publication(final)
        path = service.issue_series_publication_path(key)
        self.assertEqual(final, json.loads(path.read_text()))
        self.assertEqual(2, commit.call_count)
        self.assertEqual(3, push.call_count)
        with self.assertRaisesRegex(RuntimeError, "already final"):
            service._git_resolve_issue_series_publication({**final, "comment_id": "24"})
        with self.assertRaisesRegex(RuntimeError, "conflicts"):
            service._git_record_issue_series_publication({**final, "status": "ambiguous"})

    def test_live_failure_and_existing_comment_outcomes_are_bounded(self) -> None:
        key = "f" * 64
        digest = "sha256:" + "a" * 64
        expected = {
            "401 denied": "deferred_unauthorized",
            "closed by maintainer": "deferred_closed",
            "repository moved": "deferred_moved",
            "409 conflict": "deferred_conflict",
            "socket broke": "deferred_unavailable",
        }
        for diagnostic, status in expected.items():
            with self.subTest(diagnostic=diagnostic):
                self.assertEqual(
                    status, service._live_publication_failure(diagnostic, key, digest).status
                )
        with patch("tools.issue_series_service.shutil.which", return_value=None):
            self.assertEqual(
                "deferred_unavailable",
                service._live_existing_issue_series_comment("acme/product", 7, key, digest).status,  # type: ignore[union-attr]
            )
        command = Mock(returncode=0, stdout="9\n11\n", stderr="")
        with (
            patch("tools.issue_series_service.shutil.which", return_value="gh"),
            patch("tools.issue_series_service.subprocess.run", return_value=command),
        ):
            self.assertEqual(
                "ambiguous",
                service._live_existing_issue_series_comment("acme/product", 7, key, digest).status,  # type: ignore[union-attr]
            )
        with (
            patch("tools.issue_series_service.shutil.which", return_value="gh"),
            patch(
                "tools.issue_series_service.subprocess.run",
                side_effect=subprocess.TimeoutExpired("gh", 15),
            ),
        ):
            self.assertEqual(
                "deferred_timeout",
                service._live_existing_issue_series_comment("acme/product", 7, key, digest).status,  # type: ignore[union-attr]
            )


if __name__ == "__main__":
    unittest.main()
