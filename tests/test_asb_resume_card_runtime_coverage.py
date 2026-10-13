# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
# mypy: disable-error-code=attr-defined

"""ASB-owned liveness coverage for read-only resume-card snapshots."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools import resume_card_runtime


class SnapshotTimeoutError(RuntimeError):
    """Private test boundary for snapshot lock timeouts."""


class ResumeCardRuntimeCoverageTests(unittest.TestCase):
    def test_unstable_absent_lock_retries_then_fails_closed(self) -> None:
        lock = Path("/does/not/matter")
        with (
            patch.object(resume_card_runtime.os, "open", side_effect=FileNotFoundError),
            patch.object(Path, "exists", return_value=True),
            self.assertRaisesRegex(RuntimeError, "snapshot changed"),
        ):
            resume_card_runtime.read_only_snapshot(
                lambda: "card", lambda: lock, 1.0, 0.01, SnapshotTimeoutError
            )

    def test_existing_locked_snapshot_times_out_without_mutating_lock(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            lock = Path(directory) / "state.lock"
            lock.write_text("existing", encoding="utf-8")

            def flock(_descriptor: int, operation: int) -> None:
                if operation & resume_card_runtime.fcntl.LOCK_NB:
                    raise BlockingIOError

            with (
                patch.object(resume_card_runtime.fcntl, "flock", side_effect=flock),
                patch.object(resume_card_runtime.time, "monotonic", side_effect=(0.0, 1.0)),
                self.assertRaisesRegex(SnapshotTimeoutError, "LOCK_TIMEOUT"),
            ):
                resume_card_runtime.read_only_snapshot(
                    lambda: "card", lambda: lock, 1.0, 0.01, SnapshotTimeoutError
                )
            self.assertEqual("existing", lock.read_text(encoding="utf-8"))

    def test_snapshot_errors_deduplicates_duplicate_ids_and_evidence_errors(self) -> None:
        tasks = [
            (Path("one.md"), {"id": "AR-0001"}, ""),
            (Path("two.md"), {"id": "AR-0001"}, ""),
        ]
        errors = resume_card_runtime.snapshot_errors(
            tasks,
            type("Policy", (), {"classes": frozenset()})(),
            basic_task_errors=lambda *_: [],
            projection_errors=lambda *_: [],
            private_text_errors=lambda *_: [],
            evidence_errors=lambda *_: (_ for _ in ()).throw(ValueError("bad evidence")),
            graph_errors=lambda _: [],
            hierarchy_errors=lambda _: [],
            supersession_errors=lambda _: [],
        )
        self.assertEqual(["AR-0001: bad evidence", "duplicate AR-0001"], errors)
