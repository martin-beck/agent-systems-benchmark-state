# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Coverage for change-drift worktree binding and metadata admission."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from tools import change_drift


class ChangeDriftBindingCoverageTests(unittest.TestCase):
    def test_bound_worktree_yields_direct_child_and_rejects_invalid_bindings(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            projects_root = Path(directory)
            child = projects_root / "worker-1"
            child.mkdir()
            meta: change_drift.Meta = {"worktree_key": child.name}

            with change_drift.bound_worktree(meta, projects_root) as bound:
                self.assertTrue(bound.is_dir())
                self.assertEqual(child.resolve(), bound.resolve())

            for key, product_worktree in (("../escape", None), (child.name, child.name)):
                with (
                    self.subTest(key=key, product_worktree=product_worktree),
                    self.assertRaisesRegex(RuntimeError, "requires a bound worktree"),
                    change_drift.bound_worktree(
                        {"worktree_key": key}, projects_root, product_worktree
                    ),
                ):
                    pass

    def test_bound_worktree_rejects_missing_and_symlink_children(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            projects_root = Path(directory)
            outside = projects_root / "outside"
            outside.mkdir()
            link = projects_root / "linked"
            link.symlink_to(outside, target_is_directory=True)

            for key in ("missing", link.name):
                with (
                    self.subTest(key=key),
                    self.assertRaisesRegex(RuntimeError, "direct directory"),
                    change_drift.bound_worktree({"worktree_key": key}, projects_root),
                ):
                    pass

    def test_metadata_and_done_admission_wrap_invalid_history(self) -> None:
        malformed: change_drift.Meta = {"id": "AR-0001", "change_drift": "not-a-list"}

        self.assertEqual("invalid change-drift history", change_drift.metadata_error(malformed))
        self.assertEqual(
            "change-drift record is invalid: invalid change-drift history",
            change_drift.done_admission_error(malformed),
        )

    def test_validate_rejects_noncanonical_observation_entries(self) -> None:
        record = change_drift._record(
            "delta",
            "AR-0001",
            2,
            "now",
            {
                "baseline_digest": "sha256:" + "0" * 64,
                "head": "head",
                "entries": [
                    {
                        "path": "src/b.py",
                        "previous_path": "",
                        "status": "M ",
                        "generated": False,
                        "content_digest": "",
                        "classification": "in_scope",
                        "material": True,
                    },
                    {
                        "path": "src/a.py",
                        "previous_path": "",
                        "status": "M ",
                        "generated": False,
                        "content_digest": "",
                        "classification": "in_scope",
                        "material": True,
                    },
                ],
            },
            "sha256:" + "1" * 64,
        )

        with self.assertRaisesRegex(ValueError, "entries are not canonical"):
            change_drift.validate(record)


if __name__ == "__main__":
    unittest.main()
