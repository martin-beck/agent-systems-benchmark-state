# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Tests for the repository-owned generated-view consistency gate."""

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools import check_generated_views


class GeneratedViewsTests(unittest.TestCase):
    def test_main_accepts_one_consistent_snapshot(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "CURRENT.md").write_text("current")
            with (
                patch.object(check_generated_views.handoffctl, "ROOT", root),
                patch.object(check_generated_views.handoffctl, "all_tasks", return_value=[]),
                patch.object(
                    check_generated_views.handoffctl, "render_current", return_value="current"
                ),
                patch.object(
                    check_generated_views.handoffctl,
                    "project_settings",
                    return_value={"status_view": False},
                ),
            ):
                self.assertEqual(0, check_generated_views.main())

    def test_main_reports_stale_current_and_status_views(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "CURRENT.md").write_text("stale")
            with (
                patch.object(check_generated_views.handoffctl, "ROOT", root),
                patch.object(check_generated_views.handoffctl, "all_tasks", return_value=[]),
                patch.object(
                    check_generated_views.handoffctl, "render_current", return_value="current"
                ),
                patch.object(
                    check_generated_views.handoffctl,
                    "project_settings",
                    return_value={"status_view": True},
                ),
                patch.object(
                    check_generated_views.handoffctl,
                    "render_status_views",
                    return_value={"STATUS.md": "expected"},
                ),
                patch.object(
                    check_generated_views.handoffctl,
                    "status_projection_errors",
                    return_value=["STATUS.md differs from generated tasks"],
                ),
            ):
                self.assertEqual(1, check_generated_views.main())


if __name__ == "__main__":
    unittest.main()
