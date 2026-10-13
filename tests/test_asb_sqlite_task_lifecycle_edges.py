# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""ASB-owned core task lifecycle coverage for SQLite storage."""

from __future__ import annotations

import sqlite3
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from fixture_ids import project_uuid

from tools.checkpoint_records import build_checkpoint
from tools.session_records import build_session_record
from tools.sqlite_storage import SQLiteBackend, create_database

BINDING = {
    "schema_version": 1,
    "project_id": project_uuid("c"),
    "state_repository": "martin-beck/agent-systems-benchmark-state",
    "product_repository": "martin-beck/agent-systems-benchmark",
}


def task(task_id: str, **changes: object) -> tuple[Path, dict[str, object], str]:
    meta: dict[str, object] = {
        "schema_version": 1,
        "id": task_id,
        "title": "SQLite lifecycle coverage",
        "status": "open",
        "priority": "P1",
        "summary": "Ready.",
        "next_action": "Test.",
        "task_revision": 1,
        "updated_at": "2026-10-13T00:00:00+00:00",
        "owner": "",
        "claim_expires": "",
        "worktree_key": "",
        "branch": "",
        "checkpoint_commit": "",
        "plan": "",
        "depends_on": [],
    }
    meta.update(changes)
    return Path(f"{task_id}.md"), meta, f"# {task_id}\n"


class AsbSQLiteTaskLifecycleEdgeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.tasks = self.root / "tasks"
        self.tasks.mkdir()
        self.database = self.root / ".runtime" / "coordinator.sqlite3"
        create_database(
            self.database,
            BINDING,
            [
                task("AR-1729", worktree_key="worker-a", branch="codex/worker-a"),
                task("AR-1730", depends_on=["AR-1729"]),
            ],
            imported_at="2026-10-13T00:00:00+00:00",
            source_backend="git",
            source_checkpoint="a" * 40,
        )
        self.backend = SQLiteBackend(self.database, BINDING, self.tasks)

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def test_mutation_persists_task_session_checkpoint_and_dependency_lifecycle(self) -> None:
        def transition(meta: dict[str, object], _tasks: list[object]) -> tuple[str, str]:
            meta.update(
                {
                    "status": "in_progress",
                    "owner": "worker-a",
                    "claim_expires": "2026-10-14T00:00:00+00:00",
                    "next_action": "Complete lifecycle coverage.",
                    "depends_on": ["AR-1730"],
                }
            )
            return "claimed", "# AR-1729\n- claimed\n"

        self.backend.mutate(
            "AR-1729",
            1,
            "claim",
            "2026-10-13T00:01:00+00:00",
            transition,
            session_factory=lambda meta: build_session_record(
                meta, "update", "2026-10-13T00:01:00+00:00"
            ),
            checkpoint_factory=lambda meta: build_checkpoint(
                meta,
                "# AR-1729\n- claimed\n",
                "b" * 40,
                "2026-10-13T00:01:00+00:00",
            ),
        )

        loaded = {str(meta["id"]): (meta, body) for _, meta, body in self.backend.load_tasks()}
        changed, body = loaded["AR-1729"]
        self.assertEqual(
            ("in_progress", 2, ["AR-1730"]),
            (
                changed["status"],
                changed["task_revision"],
                changed["depends_on"],
            ),
        )
        self.assertEqual("# AR-1729\n- claimed\n", body)
        self.assertEqual(["AR-1729"], [row["task"] for row in self.backend.load_session_records()])
        self.assertEqual(
            [2], [row["task_revision"] for row in self.backend.load_checkpoint_records("AR-1729")]
        )
        self.assertEqual([], self.backend.load_session_records("AR-1730"))

        with self.assertRaisesRegex(RuntimeError, "stale revision"):
            self.backend.mutate("AR-1729", 1, "claim", "2026-10-13T00:02:00+00:00", transition)

    def test_observations_and_command_evidence_are_scoped_and_idempotent(self) -> None:
        self.backend.update_observations(
            {
                "worker-a": {
                    "branch": "codex/observed",
                    "head": "c" * 40,
                    "dirty": True,
                },
                "unused": {"branch": "ignored", "head": "d" * 40, "dirty": False},
            },
            "2026-10-13T00:03:00+00:00",
        )
        observed = next(meta for _, meta, _ in self.backend.load_tasks() if meta["id"] == "AR-1729")
        self.assertEqual(
            (2, "codex/observed", "c" * 40, True),
            (
                observed["task_revision"],
                observed["observed_branch"],
                observed["observed_head"],
                observed["observed_dirty"],
            ),
        )
        self.backend.update_observations(
            {"worker-a": {"branch": "codex/observed", "head": "c" * 40, "dirty": True}},
            "2026-10-13T00:04:00+00:00",
        )
        self.assertEqual(
            2,
            next(meta for _, meta, _ in self.backend.load_tasks() if meta["id"] == "AR-1729")[
                "task_revision"
            ],
        )

        digest = "e" * 64
        self.assertFalse(self.backend.has_command_result("AR-1729", "worker-a", digest))
        self.backend.append_command_result(
            "AR-1729", "worker-a", digest, 0, "EXIT", "2026-10-13T00:05:00+00:00"
        )
        self.assertTrue(self.backend.has_command_result("AR-1729", "worker-a", digest))
        self.assertFalse(self.backend.has_command_result("AR-1729", "worker-b", digest))

    def test_integrity_report_detects_corrupt_foreign_key_without_mutating_tasks(self) -> None:
        connection = sqlite3.connect(self.database)
        try:
            connection.execute("PRAGMA foreign_keys=OFF")
            connection.execute("INSERT INTO dependencies VALUES ('AR-1729', 'AR-9999')")
            connection.commit()
        finally:
            connection.close()

        self.assertIn("SQLITE_CORRUPT: foreign-key violations", self.backend.integrity_errors())
        self.assertEqual(
            ["AR-1729", "AR-1730"], [meta["id"] for _, meta, _ in self.backend.load_tasks()]
        )


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
