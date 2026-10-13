# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""ASB-owned legacy and corruption-path coverage for SQLite storage."""

from __future__ import annotations

import sqlite3
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from fixture_ids import project_uuid

from tools.sqlite_storage import SQLiteBackend, StorageCorruptionError, create_database

BINDING = {
    "schema_version": 1,
    "project_id": project_uuid("b"),
    "state_repository": "martin-beck/agent-systems-benchmark-state",
    "product_repository": "martin-beck/agent-systems-benchmark",
}


def task() -> tuple[Path, dict[str, object], str]:
    return (
        Path("AR-1729.md"),
        {
            "schema_version": 1,
            "id": "AR-1729",
            "title": "SQLite legacy edges",
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
        },
        "# SQLite legacy edges\n",
    )


class AsbSQLiteLegacyErrorEdgeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = TemporaryDirectory()
        root = Path(self.temporary.name)
        self.database = root / ".runtime" / "coordinator.sqlite3"
        self.tasks = root / "tasks"
        self.tasks.mkdir()
        create_database(
            self.database,
            BINDING,
            [task()],
            imported_at="2026-10-13T00:00:00+00:00",
            source_backend="git",
            source_checkpoint="a" * 40,
        )
        self.backend = SQLiteBackend(self.database, BINDING, self.tasks)

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def database_edit(self, statement: str, parameters: tuple[object, ...] = ()) -> None:
        connection = sqlite3.connect(self.database)
        try:
            connection.execute(statement, parameters)
            connection.commit()
        finally:
            connection.close()

    def test_legacy_optional_receipt_tables_are_empty(self) -> None:
        connection = sqlite3.connect(self.database)
        try:
            connection.execute("DROP TABLE IF EXISTS session_records")
            connection.execute("DROP TABLE IF EXISTS checkpoint_records")
            connection.execute("DROP TABLE issue_series_publications")
            connection.execute("DROP TABLE issue_series_members")
            connection.execute("DROP TABLE issue_series")
            connection.commit()
        finally:
            connection.close()
        self.assertEqual([], self.backend.load_session_records())
        self.assertEqual([], self.backend.load_checkpoint_records())
        self.assertEqual([], self.backend.load_issue_series())
        self.assertEqual([], self.backend.load_issue_series_publications())

    def test_invalid_task_json_fails_closed(self) -> None:
        connection = sqlite3.connect(self.database)
        try:
            connection.execute("PRAGMA ignore_check_constraints=ON")
            connection.execute("UPDATE tasks SET meta_json='{not-json' WHERE id='AR-1729'")
            connection.commit()
        finally:
            connection.close()
        with self.assertRaisesRegex(StorageCorruptionError, "invalid task JSON"):
            self.backend.load_tasks()

    def test_task_revision_disagreement_fails_closed(self) -> None:
        self.database_edit(
            "UPDATE tasks SET meta_json=json_set(meta_json, '$.task_revision', 2) "
            "WHERE id='AR-1729'"
        )
        with self.assertRaisesRegex(StorageCorruptionError, "revision columns disagree"):
            self.backend.load_tasks()

    def test_malformed_legacy_session_and_checkpoint_records_fail_closed(self) -> None:
        self.database_edit(
            "CREATE TABLE session_records(sequence INTEGER PRIMARY KEY, task_id TEXT, "
            "task_revision INTEGER, record_json TEXT, recorded_at TEXT)"
        )
        self.database_edit("INSERT INTO session_records VALUES (1, 'AR-1729', 1, '[]', 'now')")
        with self.assertRaisesRegex(StorageCorruptionError, "invalid session record"):
            self.backend.load_session_records()
        self.database_edit("DROP TABLE session_records")
        self.database_edit(
            "CREATE TABLE checkpoint_records(sequence INTEGER PRIMARY KEY, task_id TEXT, "
            "task_revision INTEGER, record_json TEXT, recorded_at TEXT)"
        )
        self.database_edit(
            "INSERT INTO checkpoint_records VALUES (1, 'AR-1729', 1, 'not-json', 'now')"
        )
        with self.assertRaisesRegex(StorageCorruptionError, "invalid checkpoint JSON"):
            self.backend.load_checkpoint_records()

    def test_wrong_binding_and_retired_backend_are_rejected(self) -> None:
        wrong = BINDING | {"product_repository": "martin-beck/other"}
        with self.assertRaisesRegex(RuntimeError, "SQLITE_BINDING_MISMATCH"):
            SQLiteBackend(self.database, wrong, self.tasks).load_tasks()
        self.database_edit("UPDATE metadata SET value='retired' WHERE key='state'")
        with self.assertRaisesRegex(RuntimeError, "SQLITE_BACKEND_INACTIVE"):
            self.backend.load_tasks()
