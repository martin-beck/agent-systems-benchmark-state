# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""ASB-owned edge coverage for SQLite execution and publication receipts."""

from __future__ import annotations

import hashlib
import json
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
EXECUTION_ID = project_uuid("1")


def task() -> tuple[Path, dict[str, object], str]:
    return (
        Path("AR-1729.md"),
        {
            "schema_version": 1,
            "id": "AR-1729",
            "title": "Receipt coverage",
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
        "# Receipt coverage\n",
    )


def publication_key(repository: str, issue_number: int, digest: str) -> str:
    return hashlib.sha256(
        f"issue-series-publication-v1\0{repository}\0{issue_number}\0{digest}".encode()
    ).hexdigest()


class AsbSQLiteReceiptEdgeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.tasks = self.root / "tasks"
        self.tasks.mkdir()
        self.database = self.root / ".runtime" / "coordinator.sqlite3"
        self.series = {
            "series_identity": {"repository": REPOSITORY, "issue_number": 1729},
            "manifest": {"schema_version": 1, "title": "Receipt coverage"},
            "manifest_digest": DIGEST,
            "task_ids": ["AR-1729"],
        }
        create_database(
            self.database,
            BINDING,
            [task()],
            imported_at="2026-10-13T00:00:00+00:00",
            source_backend="git",
            source_checkpoint="a" * 40,
            issue_series=[self.series],
        )
        self.backend = SQLiteBackend(self.database, BINDING, self.tasks)

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def envelope(self, **changes: object) -> dict[str, object]:
        value: dict[str, object] = {
            "schema_version": 1,
            "execution_id": EXECUTION_ID,
            "task": "AR-1729",
            "task_revision": 1,
            "owner": "worker",
            "claim_expires": "2026-10-14T00:00:00+00:00",
            "worktree_key": "receipt-worktree",
            "branch": "codex/receipt-coverage",
            "spec_ref": None,
            "spec_revision": None,
            "policy_digest": "b" * 64,
            "argv_sha256": "c" * 64,
            "timeout_seconds": 30,
            "created_at": "2026-10-13T00:01:00+00:00",
        }
        value.update(changes)
        return value

    def result(self, **changes: object) -> dict[str, object]:
        value: dict[str, object] = {
            "schema_version": 1,
            "execution_id": EXECUTION_ID,
            "classification": "EXIT",
            "returncode": 0,
            "recorded_at": "2026-10-13T00:02:00+00:00",
        }
        value.update(changes)
        return value

    def publication(self, **changes: object) -> dict[str, object]:
        value: dict[str, object] = {
            "manifest_digest": DIGEST,
            "publication_key": publication_key(REPOSITORY, 1729, DIGEST),
            "status": "ambiguous",
            "comment_id": None,
        }
        value.update(changes)
        return value

    def test_execution_receipts_round_trip_filter_and_exact_replay(self) -> None:
        envelope = self.envelope()
        self.assertEqual((True, None), self.backend.begin_execution_envelope(envelope))
        self.assertEqual((False, None), self.backend.begin_execution_envelope(envelope))
        self.assertEqual(
            [envelope | {"timeout_seconds": 30.0}], self.backend.load_execution_envelopes()
        )
        self.assertEqual([], self.backend.load_execution_envelopes("AR-9999"))
        result = self.result()
        self.assertEqual(result, self.backend.record_execution_result(result))
        self.assertEqual(result, self.backend.record_execution_result(result))
        self.assertEqual([result], self.backend.load_execution_results("AR-1729"))
        self.assertEqual((False, result), self.backend.begin_execution_envelope(envelope))

    def test_execution_receipts_reject_conflicts_missing_intent_and_invalid_shapes(self) -> None:
        with self.assertRaisesRegex(RuntimeError, "lacks a durable intent"):
            self.backend.record_execution_result(self.result())
        for invalid, message in (
            (self.envelope(timeout_seconds=True), "invalid timeout"),
            (self.envelope(spec_ref="specs/a", spec_revision=None), "incomplete spec"),
            (self.envelope(owner="bad\nowner"), "unsafe text"),
            (self.result(classification="UNKNOWN"), "invalid fields"),
            (self.result(returncode=True), "invalid fields"),
        ):
            with self.subTest(invalid=invalid):
                method = (
                    self.backend.record_execution_result
                    if "classification" in invalid and "task" not in invalid
                    else self.backend.record_execution_envelope
                )
                with self.assertRaisesRegex(ValueError, message):
                    method(invalid)
        self.backend.record_execution_envelope(self.envelope())
        with self.assertRaisesRegex(RuntimeError, "envelope conflicts"):
            self.backend.record_execution_envelope(self.envelope(owner="other"))
        self.backend.record_execution_result(self.result())
        with self.assertRaisesRegex(RuntimeError, "result conflicts"):
            self.backend.record_execution_result(self.result(returncode=1))

    def test_execution_receipt_loads_are_legacy_safe_and_corruption_fails_closed(self) -> None:
        connection = sqlite3.connect(self.database)
        try:
            connection.execute("DROP TABLE execution_results")
            connection.execute("DROP TABLE execution_envelopes")
            connection.commit()
        finally:
            connection.close()
        self.assertEqual([], self.backend.load_execution_envelopes())
        self.assertEqual([], self.backend.load_execution_results())
        self.backend.record_execution_envelope(self.envelope())
        connection = sqlite3.connect(self.database)
        try:
            connection.execute("UPDATE execution_envelopes SET envelope_json='[]'")
            connection.commit()
        finally:
            connection.close()
        with self.assertRaisesRegex(StorageCorruptionError, "invalid execution envelope"):
            self.backend.load_execution_envelopes()

    def test_execution_result_corruption_is_rejected_when_reserving_or_loading(self) -> None:
        self.backend.record_execution_envelope(self.envelope())
        self.backend.record_execution_result(self.result())
        connection = sqlite3.connect(self.database)
        try:
            connection.execute("UPDATE execution_results SET result_json=?", (json.dumps([]),))
            connection.commit()
        finally:
            connection.close()
        with self.assertRaisesRegex(StorageCorruptionError, "invalid execution result"):
            self.backend.begin_execution_envelope(self.envelope())
        with self.assertRaisesRegex(StorageCorruptionError, "invalid execution result"):
            self.backend.load_execution_results()

    def test_publication_adapter_and_ambiguous_resolution_are_bounded(self) -> None:
        record = self.publication()
        pending = self.backend.record_issue_series_publication(REPOSITORY, 1729, record)
        self.assertEqual("ambiguous", pending["status"])
        final_record = self.publication(status="published", comment_id="42")
        final = self.backend.resolve_issue_series_publication(REPOSITORY, 1729, final_record)
        self.assertEqual("published", final["status"])
        with self.assertRaisesRegex(RuntimeError, "reservation is missing"):
            self.backend.resolve_issue_series_publication(
                REPOSITORY,
                1730,
                self.publication(
                    status="published",
                    comment_id="42",
                    publication_key=publication_key(REPOSITORY, 1730, DIGEST),
                ),
            )

    def test_publication_inputs_fail_closed_before_durable_write(self) -> None:
        invalid = (
            ({"manifest_digest": DIGEST}, "lacks series identity"),
            (
                {"series_identity": {"repository": REPOSITORY, "issue_number": True}},
                "invalid issue",
            ),
            (
                {
                    "series_identity": {
                        "repository": "github.com/Acme/Product",
                        "issue_number": 1729,
                    }
                },
                "unsafe repository",
            ),
            (
                {"series_identity": self.series["series_identity"]}
                | self.publication(publication_key="0" * 64),
                "key disagrees",
            ),
            (
                {"series_identity": self.series["series_identity"]}
                | self.publication(status="published", comment_id="0"),
                "invalid comment",
            ),
        )
        for record, message in invalid:
            with self.subTest(record=record), self.assertRaisesRegex(ValueError, message):
                self.backend.record_issue_series_publication(
                    record, recorded_at="2026-10-13T00:03:00+00:00"
                )
        with self.assertRaisesRegex(ValueError, "adapter arguments are incomplete"):
            self.backend.record_issue_series_publication(REPOSITORY, 1729)
        self.assertEqual([], self.backend.load_issue_series_publications())


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
