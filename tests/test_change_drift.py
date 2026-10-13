# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""End-to-end coverage for bounded change-drift records."""

from __future__ import annotations

import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools import change_drift


def git(root: Path, *arguments: str) -> None:
    subprocess.run(  # noqa: S603 - fixed Git test fixture commands
        ["git", "-C", str(root), *arguments],  # noqa: S607
        check=True,
        capture_output=True,
        text=True,
    )


class ChangeDriftTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "src").mkdir()
        (self.root / "src" / "old.py").write_text("old\n", encoding="utf-8")
        git(self.root, "init", "-q")
        git(self.root, "add", ".")
        git(
            self.root,
            "-c",
            "user.name=Test",
            "-c",
            "user.email=test@example.invalid",
            "commit",
            "-qm",
            "initial",
        )

    def tearDown(self) -> None:
        self.temp.cleanup()

    def test_baseline_delta_preserves_rename_and_is_deterministic(self) -> None:
        first = change_drift.baseline("AR-0001", 2, "2026-10-12T00:00:00Z", self.root, ["src"])
        second = change_drift.baseline("AR-0001", 2, "different", self.root, ["src"])
        self.assertEqual(first["digest"], second["digest"])
        git(self.root, "mv", "src/old.py", "src/new.py")
        record = change_drift.delta("AR-0001", 3, "now", self.root, first, ["src"])
        entry = record["payload"]["entries"][0]
        self.assertEqual("src/new.py", entry["path"])
        self.assertEqual("src/old.py", entry["previous_path"])
        self.assertEqual("in_scope", entry["classification"])

    def test_generated_and_outside_paths_need_explicit_explanations(self) -> None:
        baseline = change_drift.baseline("AR-0001", 2, "now", self.root, ["src"])
        (self.root / "build").mkdir()
        (self.root / "build" / "bundle.generated").write_text("x", encoding="utf-8")
        current = change_drift.delta("AR-0001", 3, "now", self.root, baseline, ["src"])
        entry = current["payload"]["entries"][0]
        self.assertTrue(entry["generated"])
        self.assertEqual([entry], change_drift.unresolved([baseline, current]))
        explanation = change_drift.explain(
            "AR-0001", 4, "now", current["digest"], ["build/bundle.generated"], "build output", True
        )
        self.assertEqual([], change_drift.unresolved([baseline, current, explanation]))

    def test_committed_rename_preserves_its_pair(self) -> None:
        baseline = change_drift.baseline("AR-0001", 2, "now", self.root, ["src"])
        git(self.root, "mv", "src/old.py", "src/new.py")
        git(
            self.root,
            "-c",
            "user.name=Test",
            "-c",
            "user.email=test@example.invalid",
            "commit",
            "-qm",
            "rename",
        )
        record = change_drift.delta("AR-0001", 3, "now", self.root, baseline, ["src"])
        entry = record["payload"]["entries"][0]
        self.assertEqual(("src/new.py", "src/old.py"), (entry["path"], entry["previous_path"]))

    def test_status_and_committed_parser_reject_hostile_or_truncated_git_output(self) -> None:
        with self.assertRaisesRegex(ValueError, "malformed porcelain"):
            change_drift._status_entries(b"M bad\0")
        with self.assertRaisesRegex(ValueError, "truncated rename"):
            change_drift._status_entries(b"R  src/new.py\0")
        completed = subprocess.CompletedProcess(
            ["git"], 0, stdout=b"R100\0src/old.py\0src/new.py\0"
        )
        with patch("tools.change_drift.subprocess.run", return_value=completed):
            entries = change_drift._head_entries(self.root, "one", "two")
        self.assertEqual(
            [("src/new.py", "src/old.py", "R ")],
            [(entry["path"], entry["previous_path"], entry["status"]) for entry in entries],
        )
        failed = subprocess.CompletedProcess(["git"], 1, stdout=b"")
        with (
            patch("tools.change_drift.subprocess.run", return_value=failed),
            self.assertRaisesRegex(RuntimeError, "could not compare"),
        ):
            change_drift._head_entries(self.root, "one", "two")

    def test_history_is_linked_completion_state_machine(self) -> None:
        baseline = change_drift.baseline("AR-0001", 2, "now", self.root, ["src"])
        (self.root / "src" / "old.py").write_text("changed\n", encoding="utf-8")
        delta = change_drift.delta("AR-0001", 3, "now", self.root, baseline, ["src"])
        bypass = change_drift.baseline("AR-0001", 4, "now", self.root, ["src"], delta["digest"])
        with self.assertRaisesRegex(ValueError, "bypasses unresolved"):
            change_drift.records({"id": "AR-0001", "change_drift": [baseline, delta, bypass]})
        explanation = change_drift.explain(
            "AR-0001", 4, "now", delta["digest"], ["src/old.py"], "reviewed", False
        )
        history = [baseline, delta, explanation]
        change_drift.records({"id": "AR-0001", "change_drift": history})
        self.assertIsNone(change_drift.completion_error(history))

    def test_lifecycle_rejects_unfinished_completion_and_bad_order(self) -> None:
        baseline = change_drift.baseline("AR-0001", 2, "now", self.root, ["src"])
        with self.assertRaisesRegex(RuntimeError, "requires a baseline"):
            change_drift.next_record("AR-0001", 3, "now", self.root, [], "delta")
        with self.assertRaisesRegex(RuntimeError, "requires a delta"):
            change_drift.next_record("AR-0001", 3, "now", self.root, [baseline], "explain")
        self.assertEqual(
            "CHANGE_DRIFT_DELTA_REQUIRED: active baseline requires a post-work delta",
            change_drift.completion_error([baseline]),
        )
        with self.assertRaisesRegex(RuntimeError, "requires completion"):
            change_drift.next_record(
                "AR-0001", 3, "now", self.root, [baseline], "baseline", scope_paths=["src"]
            )

    def test_baseline_delta_explain_tracks_committed_and_dirty_changes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "src").mkdir()
            (root / "docs").mkdir()
            (root / "src" / "tracked.py").write_text("first\n", encoding="utf-8")
            git(root, "init", "-q")
            git(root, "add", ".")
            git(
                root,
                "-c",
                "user.name=Test",
                "-c",
                "user.email=test@example.invalid",
                "commit",
                "-qm",
                "initial",
            )
            baseline = change_drift.baseline("AR-9000", 1, "2026-10-13T00:00:00Z", root, ["src"])
            (root / "src" / "tracked.py").write_text("second\n", encoding="utf-8")
            git(root, "add", "src/tracked.py")
            git(
                root,
                "-c",
                "user.name=Test",
                "-c",
                "user.email=test@example.invalid",
                "commit",
                "-qm",
                "source change",
            )
            (root / "docs" / "notes.txt").write_text("dirty\n", encoding="utf-8")
            delta = change_drift.delta(
                "AR-9000", 2, "2026-10-13T00:01:00Z", root, baseline, ["src"]
            )
            entries = {item["path"]: item for item in delta["payload"]["entries"]}
            self.assertEqual("in_scope", entries["src/tracked.py"]["classification"])
            self.assertEqual("out_of_scope", entries["docs/notes.txt"]["classification"])
            history = [baseline, delta]
            self.assertEqual("CHANGE_DRIFT_UNEXPLAINED", change_drift.completion_error(history))
            explanation = change_drift.explain(
                "AR-9000",
                3,
                "2026-10-13T00:02:00Z",
                delta["digest"],
                sorted(entries),
                "Reviewed committed and local changes.",
                False,
                delta["digest"],
            )
            history.append(explanation)
            self.assertEqual([], change_drift.unresolved(history))
            self.assertIsNone(
                change_drift.done_admission_error({"id": "AR-9000", "change_drift": history})
            )

    def test_state_machine_rejects_unlinked_and_unsafe_records(self) -> None:
        with self.assertRaisesRegex(ValueError, "safe paths"):
            change_drift.normalize_scope(["../escape"])
        with self.assertRaisesRegex(ValueError, "explanation paths"):
            change_drift.explain("AR-9000", 1, "now", "bad", ["src/a"], "reason", False)
        with self.assertRaisesRegex(RuntimeError, "requires a baseline"):
            change_drift.next_record("AR-9000", 1, "now", Path(), [], "delta")
        with self.assertRaisesRegex(ValueError, "unknown"):
            change_drift.next_record("AR-9000", 1, "now", Path(), [], "unknown")


if __name__ == "__main__":
    unittest.main()
