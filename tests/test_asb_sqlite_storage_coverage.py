"""ASB-owned regression coverage for durable SQLite issue-series receipts."""

from __future__ import annotations

import hashlib
import sqlite3
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from fixture_ids import project_uuid

from tools.sqlite_storage import SQLiteBackend, StorageCorruptionError, create_database

BINDING = {
    "schema_version": 1,
    "project_id": project_uuid("a"),
    "state_repository": "martin-beck/agent-systems-benchmark-state",
    "product_repository": "martin-beck/agent-systems-benchmark",
}
REPOSITORY = "github.com/martin-beck/agent-systems-benchmark"
DIGEST = "sha256:" + "a" * 64


def task(task_id: str) -> tuple[Path, dict[str, object], str]:
    return (
        Path(f"{task_id}.md"),
        {
            "schema_version": 1,
            "id": task_id,
            "title": "ASB storage coverage",
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
        "# ASB storage coverage\n",
    )


def publication_key(repository: str, issue_number: int, digest: str) -> str:
    return hashlib.sha256(
        f"issue-series-publication-v1\0{repository}\0{issue_number}\0{digest}".encode()
    ).hexdigest()


class AsbSQLiteStorageCoverageTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.tasks = self.root / "tasks"
        self.tasks.mkdir()
        self.database = self.root / ".runtime" / "coordinator.sqlite3"
        self.manifest = {"schema_version": 1, "title": "ASB follow-up"}
        self.series = {
            "series_identity": {"repository": REPOSITORY, "issue_number": 1729},
            "manifest": self.manifest,
            "manifest_digest": DIGEST,
            "task_ids": ["AR-1729"],
        }
        create_database(
            self.database,
            BINDING,
            [task("AR-1729")],
            imported_at="2026-10-13T00:00:00+00:00",
            source_backend="git",
            source_checkpoint="a" * 40,
            issue_series=[self.series],
        )
        self.backend = SQLiteBackend(self.database, BINDING, self.tasks)

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def receipt(self, **changes: object) -> dict[str, object]:
        base: dict[str, object] = {
            "series_identity": {"repository": REPOSITORY, "issue_number": 1729},
            "manifest_digest": DIGEST,
            "publication_key": publication_key(REPOSITORY, 1729, DIGEST),
            "status": "published",
            "comment_id": "42",
        }
        base.update(changes)
        return base

    def test_publication_replay_is_exact_and_conflicts_fail_closed(self) -> None:
        first = self.backend.record_issue_series_publication(
            self.receipt(), recorded_at="2026-10-13T00:01:00+00:00"
        )
        replay = self.backend.record_issue_series_publication(
            self.receipt(status="published", comment_id="42"),
            recorded_at="2026-10-13T00:02:00+00:00",
        )
        self.assertEqual(first, replay)
        self.assertEqual([first], self.backend.load_issue_series_publications())
        with self.assertRaisesRegex(RuntimeError, "conflicts with durable record"):
            self.backend.record_issue_series_publication(
                self.receipt(status="already_published", comment_id="43"),
                recorded_at="2026-10-13T00:03:00+00:00",
            )

    def test_legacy_missing_publication_table_is_empty_but_malformed_series_is_corrupt(
        self,
    ) -> None:
        connection = sqlite3.connect(self.database)
        try:
            connection.execute("DROP TABLE issue_series_publications")
            connection.commit()
        finally:
            connection.close()
        self.assertEqual([], self.backend.load_issue_series_publications())

        connection = sqlite3.connect(self.database)
        try:
            connection.execute("PRAGMA ignore_check_constraints=ON")
            connection.execute("UPDATE issue_series SET manifest_json='not-json'")
            connection.commit()
        finally:
            connection.close()
        with self.assertRaisesRegex(StorageCorruptionError, "invalid issue-series JSON"):
            self.backend.load_issue_series()

    def test_deferred_receipts_cannot_smuggle_comment_identifiers(self) -> None:
        with self.assertRaisesRegex(ValueError, "deferred issue-series publication"):
            self.backend.record_issue_series_publication(
                self.receipt(status="deferred_timeout", comment_id="42"),
                recorded_at="2026-10-13T00:01:00+00:00",
            )
        self.assertEqual([], self.backend.load_issue_series_publications())
