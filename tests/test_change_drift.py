# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""End-to-end coverage for bounded change-drift records."""

from __future__ import annotations

import subprocess
import tempfile
import unittest
from pathlib import Path

from tools import change_drift


def git(root: Path, *arguments: str) -> None:
    subprocess.run(  # noqa: S603 - fixed Git test fixture commands
        ["git", "-C", str(root), *arguments],  # noqa: S607
        check=True,
        capture_output=True,
        text=True,
    )


class ChangeDriftTests(unittest.TestCase):
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
