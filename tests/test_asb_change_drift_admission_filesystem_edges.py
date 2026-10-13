# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Downstream coverage for change-drift admission and filesystem failures."""

from __future__ import annotations

import argparse
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools import change_drift


class ChangeDriftAdmissionFilesystemEdgesTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name)
        self.worktree = self.root / "worker"
        self.worktree.mkdir()

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def _args(self) -> argparse.Namespace:
        return argparse.Namespace(
            task="AR-9000",
            owner="worker",
            expected_revision=7,
            change_drift_action="baseline",
            scope_path=["src"],
            path=None,
            reason=None,
            generated=False,
        )

    def _meta(self, *, status: str = "in_progress") -> change_drift.Meta:
        return {
            "id": "AR-9000",
            "owner": "worker",
            "status": status,
            "task_revision": 7,
            "worktree_key": self.worktree.name,
            "change_drift": [],
        }

    def test_apply_rejects_non_admitted_status_before_opening_worktree(self) -> None:
        for status in ("planned", "done"):
            with self.subTest(status=status), patch("tools.change_drift.bound_worktree") as bound:
                with self.assertRaisesRegex(RuntimeError, "active task owner"):
                    change_drift.apply(self._args(), self._meta(status=status), self.root, "now")
                bound.assert_not_called()

    def test_bound_worktree_rejects_regular_file_and_projects_open_failure(self) -> None:
        (self.root / "not-a-directory").write_text("x", encoding="utf-8")
        with (
            self.assertRaisesRegex(RuntimeError, "direct directory"),
            change_drift.bound_worktree({"worktree_key": "not-a-directory"}, self.root),
        ):
            pass

        with (
            patch("tools.change_drift.os.open", side_effect=OSError("permission denied")),
            self.assertRaisesRegex(RuntimeError, "direct directory"),
            change_drift.bound_worktree({"worktree_key": self.worktree.name}, self.root),
        ):
            pass

    def test_git_parsers_reject_unsafe_paths_and_malformed_committed_status(self) -> None:
        with self.assertRaisesRegex(ValueError, "unsafe changed path"):
            change_drift._status_entries(b"M  ../escape.py\0")

        malformed = subprocess.CompletedProcess(["git"], 0, stdout=b"M\0")
        with (
            patch("tools.change_drift.subprocess.run", return_value=malformed),
            self.assertRaisesRegex(ValueError, "malformed committed change status"),
        ):
            change_drift._head_entries(self.worktree, "before", "after")

        unsafe = subprocess.CompletedProcess(["git"], 0, stdout=b"M\0../escape.py\0")
        with (
            patch("tools.change_drift.subprocess.run", return_value=unsafe),
            self.assertRaisesRegex(ValueError, "unsafe committed changed path"),
        ):
            change_drift._head_entries(self.worktree, "before", "after")


if __name__ == "__main__":
    unittest.main()
