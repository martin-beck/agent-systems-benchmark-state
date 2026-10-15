"""Positive and hostile coverage for the exact AR-1937 binding repair."""

import argparse
import unittest
from typing import cast

from tools.legacy_binding_repair import repair


def request(task: str, key: str, note: str = "doctor evidence") -> argparse.Namespace:
    return argparse.Namespace(
        task=task,
        expected_revision=8,
        worktree_key=key,
        note=note,
    )


class LegacyBindingRepairTests(unittest.TestCase):
    def test_repairs_each_approved_blocked_binding_and_preserves_history(self) -> None:
        cases = (
            ("AR-1891", "asb-ar1891-recovery-20261014"),
            ("AR-1935", "agent-workflow-coordinator-ar1933-credential-handoff"),
        )
        for task, key in cases:
            with self.subTest(task=task):
                meta = {
                    "id": task,
                    "task_revision": 8,
                    "status": "open",
                    "owner": "",
                    "claim_expires": "",
                    "branch": "",
                    "worktree_key": key,
                    "summary": "preserve this history",
                }
                self.assertEqual("doctor evidence", repair(request(task, key), meta))
                self.assertEqual("", meta["worktree_key"])
                self.assertEqual("open", meta["status"])
                self.assertEqual("preserve this history", meta["summary"])

    def test_rejects_target_identity_branch_key_and_unbounded_evidence(self) -> None:
        base = {
            "id": "AR-1891",
            "task_revision": 8,
            "status": "open",
            "owner": "",
            "claim_expires": "",
            "branch": "",
            "worktree_key": "asb-ar1891-recovery-20261014",
        }
        cases = (
            argparse.Namespace(
                task="AR-1891", expected_revision=7, worktree_key=base["worktree_key"], note="x"
            ),
            argparse.Namespace(
                task="AR-1891", expected_revision=8, worktree_key=base["worktree_key"], note="x"
            ),
            request("AR-1891", "wrong"),
            request("AR-1891", cast(str, base["worktree_key"]), ""),
        )
        for candidate in cases:
            with self.subTest(candidate=candidate):
                meta = dict(base)
                if (
                    candidate.expected_revision == 8
                    and candidate.worktree_key == base["worktree_key"]
                    and candidate.note == "x"
                ):
                    meta["status"] = "blocked"
                before = dict(meta)
                with self.assertRaises(RuntimeError):
                    repair(candidate, meta)
                self.assertEqual(before, meta)


if __name__ == "__main__":
    unittest.main()
