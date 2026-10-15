# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Positive and hostile coverage for the exact AR-1937 binding repair."""

import argparse
import unittest

from tools.legacy_binding_repair import repair


def request(task: str, branch: str, key: str, note: str = "doctor evidence") -> argparse.Namespace:
    return argparse.Namespace(
        task=task,
        expected_revision=8,
        branch=branch,
        worktree_key=key,
        note=note,
    )


class LegacyBindingRepairTests(unittest.TestCase):
    def test_repairs_each_approved_blocked_binding_and_preserves_history(self) -> None:
        cases = (
            ("AR-1891", "codex/ar-1891-recovery", "asb-ar1891-recovery-20261014"),
            (
                "AR-1935",
                "codex/ar1933-credential-handoff",
                "agent-workflow-coordinator-ar1933-credential-handoff",
            ),
        )
        for task, branch, key in cases:
            with self.subTest(task=task):
                meta = {
                    "id": task,
                    "task_revision": 8,
                    "status": "blocked",
                    "owner": "",
                    "claim_expires": "",
                    "branch": branch,
                    "worktree_key": key,
                    "summary": "preserve this history",
                }
                self.assertEqual("doctor evidence", repair(request(task, branch, key), meta))
                self.assertEqual("", meta["branch"])
                self.assertEqual("", meta["worktree_key"])
                self.assertEqual("blocked", meta["status"])
                self.assertEqual("preserve this history", meta["summary"])

    def test_rejects_target_identity_branch_key_and_unbounded_evidence(self) -> None:
        base = {
            "id": "AR-1891",
            "task_revision": 8,
            "status": "blocked",
            "owner": "",
            "claim_expires": "",
            "branch": "codex/ar-1891-recovery",
            "worktree_key": "asb-ar1891-recovery-20261014",
        }
        cases = (
            request("AR-1793", base["branch"], base["worktree_key"]),
            request("AR-1891", "wrong", base["worktree_key"]),
            request("AR-1891", base["branch"], "wrong"),
            request("AR-1891", base["branch"], base["worktree_key"], "x" * 513),
        )
        for candidate in cases:
            with self.subTest(candidate=candidate):
                meta = dict(base)
                before = dict(meta)
                with self.assertRaises(RuntimeError):
                    repair(candidate, meta)
                self.assertEqual(before, meta)


if __name__ == "__main__":
    unittest.main()
