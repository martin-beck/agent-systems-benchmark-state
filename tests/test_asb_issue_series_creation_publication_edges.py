# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""ASB-owned creation and live-publication coverage for issue-series service."""

from __future__ import annotations

import subprocess
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import Mock, patch

from tools import issue_series_service as service


class CommitThenExportError(RuntimeError):
    """Represent a projection failure after authoritative SQLite mutation."""


class IssueSeriesCreationPublicationEdgesTests(unittest.TestCase):
    def setUp(self) -> None:
        self.directory = TemporaryDirectory()
        self.root = Path(self.directory.name)
        self.addCleanup(self.directory.cleanup)

    def test_plan_loader_passes_stable_local_state_to_planner(self) -> None:
        manifest = self.root / "plan.json"
        manifest.write_text("{}", encoding="utf-8")
        tasks = [
            (
                self.root / "AR-1.md",
                {
                    "id": "AR-1",
                    "status": "planned",
                    "task_revision": 2,
                    "depends_on": [],
                },
                "",
            )
        ]
        planner = Mock(return_value='{"manifest_digest":"sha256:ok"}')
        with (
            patch.object(
                service,
                "project_binding",
                return_value={"product_repository": "github.com/acme/product"},
                create=True,
            ),
            patch.object(service, "plan_issue_series", planner),
        ):
            result = service.load_issue_series_plan(manifest, tasks)  # type: ignore[arg-type]

        self.assertEqual('{"manifest_digest":"sha256:ok"}', result)
        self.assertEqual(manifest, planner.call_args.args[0])
        self.assertEqual(
            "github.com/acme/product", planner.call_args.kwargs["expected_product_slug"]
        )
        self.assertEqual(["AR-1"], list(planner.call_args.kwargs["existing_task_ids"]))
        self.assertEqual(
            service.issue_series_state_digest(tasks),
            planner.call_args.kwargs["current_state_digest"],
        )

    def test_sqlite_create_reports_committed_export_failure_with_identity(self) -> None:
        receipt = {
            "series_identity": {"repository": "github.com/acme/product", "issue_number": 17},
            "current_state_digest": "sha256:" + "a" * 64,
        }
        backend = Mock()
        created = [(self.root / "AR-1.md", {"id": "AR-1"}, "")]
        with (
            patch.object(service, "mutating_sqlite_backend", return_value=backend, create=True),
            patch.object(service, "now", return_value="2026-10-13T00:00:00Z", create=True),
            patch.object(
                service,
                "write_sqlite_projections",
                side_effect=CommitThenExportError("disk full"),
                create=True,
            ),
            patch.object(service, "StorageCommittedError", RuntimeError, create=True),
            patch.object(service, "Meta", dict, create=True),
            self.assertRaisesRegex(
                RuntimeError,
                r"SQLITE_COMMITTED_EXPORT_FAILED: issue-series="
                r"github\.com/acme/product#17; disk full",
            ),
        ):
            service.create_sqlite_issue_series(receipt, created, object())  # type: ignore[arg-type]

        backend.create_issue_series.assert_called_once_with(
            receipt,
            created,
            expected_state_digest=receipt["current_state_digest"],
            recorded_at="2026-10-13T00:00:00Z",
        )

    def test_live_publication_posts_once_after_identity_and_marker_checks(self) -> None:
        digest = "sha256:" + "b" * 64
        config_path = self.root / "config.json"
        config_path.write_text("{}", encoding="utf-8")
        response = Mock(returncode=0, stdout="912\n", stderr="")
        with (
            patch.object(service, "CONFIG", config_path, create=True),
            patch.object(
                service, "config", return_value={"github_repository": "acme/product"}, create=True
            ),
            patch.object(service, "repository_slug", side_effect=lambda value: value, create=True),
            patch.object(service, "_live_existing_issue_series_comment", return_value=None),
            patch.object(service.shutil, "which", return_value="/usr/bin/gh"),
            patch.object(service.subprocess, "run", return_value=response) as run,
        ):
            outcome = service._live_issue_series_publication(
                "github.com/acme/product", 17, digest, "bounded publication"
            )

        self.assertEqual("published", outcome.status)
        self.assertEqual("912", outcome.comment_id)
        self.assertEqual("POST", run.call_args.args[0][3])
        self.assertIn("body=bounded publication", run.call_args.args[0])
        self.assertEqual(15, run.call_args.kwargs["timeout"])

    def test_live_publication_preserves_timeout_as_bounded_outcome(self) -> None:
        digest = "sha256:" + "c" * 64
        config_path = self.root / "config.json"
        config_path.write_text("{}", encoding="utf-8")
        with (
            patch.object(service, "CONFIG", config_path, create=True),
            patch.object(
                service, "config", return_value={"github_repository": "acme/product"}, create=True
            ),
            patch.object(service, "repository_slug", side_effect=lambda value: value, create=True),
            patch.object(service, "_live_existing_issue_series_comment", return_value=None),
            patch.object(service.shutil, "which", return_value="/usr/bin/gh"),
            patch.object(
                service.subprocess,
                "run",
                side_effect=subprocess.TimeoutExpired("gh", 15),
            ),
        ):
            outcome = service._live_issue_series_publication(
                "github.com/acme/product", 17, digest, "bounded publication"
            )

        self.assertEqual("deferred_timeout", outcome.status)
        self.assertEqual(None, outcome.comment_id)


if __name__ == "__main__":
    unittest.main()
