# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Tests for revision-bound append-only claim identity records."""

import contextlib
import copy
import json
import tempfile
import unittest
from argparse import Namespace
from pathlib import Path
from typing import cast
from unittest.mock import patch

from tools import handoffctl
from tools.claim_records import (
    append_record,
    build_record,
    fingerprint,
    latest_for_task,
    load_records,
    mismatch,
)


def task() -> dict[str, object]:
    return {
        "id": "AR-1720",
        "title": "Integrity",
        "summary": "Protect claims",
        "depends_on": [],
        "plan": "../plans/AR-1720-coordinator-claim-integrity.md",
        "spec_ref": "specs/AR-1720.json",
        "owner": "worker",
        "claim_expires": "2099-01-01T00:00:00+00:00",
        "task_revision": 4,
    }


class ClaimRecordTests(unittest.TestCase):
    def test_record_round_trip_and_fingerprint(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            value = task()
            record = build_record(value, "claim", "2026-01-01T00:00:00+00:00")
            append_record(root, record)
            loaded = load_records(root)
            self.assertEqual(record, latest_for_task(loaded, "AR-1720"))
            self.assertEqual(record["fingerprint"], fingerprint(value))
            self.assertIsNone(mismatch(record, value))

    def test_identity_change_and_stale_revision_are_rejected(self) -> None:
        value = task()
        record = build_record(value, "claim", "2026-01-01T00:00:00+00:00")
        changed = dict(value, summary="changed")
        self.assertIn("differs", mismatch(record, changed) or "")
        revised = dict(value, task_revision=5)
        self.assertIn("differs", mismatch(record, revised) or "")
        stale_record = dict(record, task_revision=3)
        self.assertIn("stale", mismatch(stale_record, value) or "")

    def test_record_validation_rejects_each_malformed_field(self) -> None:
        value = task()
        record = build_record(value, "claim", "2026-01-01T00:00:00+00:00")
        cases = [
            ({"extra": True}, "fields"),
            ({"schema_version": 2}, "schema"),
            ({"task": "bad"}, "task"),
            ({"task_revision": 0}, "revision"),
            ({"recorded_at": ""}, "timestamp"),
            ({"operation": ""}, "operation"),
            ({"identity": []}, "identity"),
            ({"identity": dict(record["identity"], id="AR-0001")}, "does not match"),
            ({"fingerprint": "bad"}, "fingerprint"),
            ({"fingerprint": "0" * 64}, "fingerprint mismatch"),
        ]
        for changes, expected in cases:
            with self.subTest(expected=expected):
                malformed = copy.deepcopy(record)
                malformed.update(cast(dict[str, object], changes))
                with self.assertRaisesRegex(ValueError, expected):
                    from tools.claim_records import validate_record

                    validate_record(malformed)

        with self.assertRaises(ValueError):
            build_record(dict(value, id="bad"), "claim", "now")
        with self.assertRaises(ValueError):
            build_record(value, "", "now")

    def test_loading_rejects_bad_lines_and_preserves_history(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "integrity/claim-ledger.jsonl"
            path.parent.mkdir()
            path.write_text("not-json\n")
            with self.assertRaisesRegex(ValueError, "line 1"):
                load_records(root)
            path.write_text("[]\n")
            with self.assertRaisesRegex(ValueError, "line 1"):
                load_records(root)
            value = task()
            record = build_record(value, "claim", "2026-01-01T00:00:00+00:00")
            path.write_text("".join(json.dumps(record) + "\n" for _ in range(2049)))
            self.assertEqual(2049, len(load_records(root)))
            append_record(root, build_record(dict(value, task_revision=5), "heartbeat", "now"))
            self.assertEqual(2050, len(load_records(root)))

    def test_append_cleans_temporary_file_when_replace_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            record = build_record(task(), "claim", "2026-01-01T00:00:00+00:00")
            with (
                patch.object(Path, "replace", side_effect=OSError("injected")),
                self.assertRaises(OSError),
            ):
                append_record(root, record)

    def test_coordinator_validation_detects_claimed_scope_swap(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            value = task()
            value["status"] = "in_progress"
            value["updated_at"] = "2026-01-01T00:00:00+00:00"
            append_record(root, build_record(value, "enroll", "2026-01-01T00:00:00+00:00"))
            task_tuple = (root / "tasks/AR-1720.md", value, "")
            with patch.object(handoffctl, "ROOT", root):
                self.assertEqual([], handoffctl.claim_integrity_errors([task_tuple]))
                changed = dict(value, summary="scope replaced")
                changed_tuple = (task_tuple[0], changed, "")
                self.assertIn("differs", handoffctl.claim_integrity_errors([changed_tuple])[0])

    def test_integrity_enrollment_is_one_signed_coordinator_transaction(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            value = task()
            value["status"] = "in_progress"
            value["updated_at"] = "2026-01-01T00:00:00+00:00"
            task_tuple = (root / "tasks/AR-1720.md", value, "")
            with (
                patch.object(handoffctl, "ROOT", root),
                patch.object(handoffctl, "locked", return_value=contextlib.nullcontext()),
                patch.object(handoffctl, "backend_selection", return_value={"backend": "git"}),
                patch.object(handoffctl, "sync_replica_before_write"),
                patch.object(handoffctl, "all_tasks", return_value=[task_tuple]),
                patch.object(handoffctl, "commit", return_value=True) as commit,
                patch.object(handoffctl, "push_replica"),
                patch.object(handoffctl, "now", return_value="2026-01-01T00:00:00+00:00"),
            ):
                handoffctl.cmd_integrity(Namespace(integrity_action="enroll"))
                commit.assert_called_once()
                with self.assertRaisesRegex(RuntimeError, "already enabled"):
                    handoffctl.cmd_integrity(Namespace(integrity_action="enroll"))

    def test_integrity_enrollment_rejects_unsupported_or_empty_actions(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with patch.object(handoffctl, "ROOT", root):
                with self.assertRaisesRegex(RuntimeError, "unsupported"):
                    handoffctl.cmd_integrity(Namespace(integrity_action="list"))
                with (
                    patch.object(handoffctl, "locked", return_value=contextlib.nullcontext()),
                    patch.object(handoffctl, "backend_selection", return_value={"backend": "git"}),
                    patch.object(handoffctl, "sync_replica_before_write"),
                    patch.object(handoffctl, "all_tasks", return_value=[]),
                    self.assertRaisesRegex(RuntimeError, "empty claim"),
                ):
                    handoffctl.cmd_integrity(Namespace(integrity_action="enroll"))

    def test_enrollment_preserves_committed_ledger_when_replication_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            value = task()
            value["status"] = "in_progress"
            value["updated_at"] = "2026-01-01T00:00:00+00:00"
            task_tuple = (root / "tasks/AR-1720.md", value, "")
            with (
                patch.object(handoffctl, "ROOT", root),
                patch.object(handoffctl, "locked", return_value=contextlib.nullcontext()),
                patch.object(handoffctl, "backend_selection", return_value={"backend": "git"}),
                patch.object(handoffctl, "sync_replica_before_write"),
                patch.object(handoffctl, "all_tasks", return_value=[task_tuple]),
                patch.object(handoffctl, "commit", return_value=True),
                patch.object(handoffctl, "push_replica", side_effect=RuntimeError("offline")),
                patch.object(handoffctl, "now", return_value="2026-01-01T00:00:00+00:00"),
                self.assertRaisesRegex(RuntimeError, "offline"),
            ):
                handoffctl.cmd_integrity(Namespace(integrity_action="enroll"))
            self.assertTrue((root / "integrity/claim-ledger.jsonl").exists())

    def test_reconcile_and_mutation_fail_before_re_recording_a_scope_swap(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            original = task()
            original["status"] = "in_progress"
            original["updated_at"] = "2026-01-01T00:00:00+00:00"
            changed = dict(original, summary="unapproved replacement")
            task_tuple = (root / "tasks/AR-1720.md", changed, "")
            append_record(root, build_record(original, "enroll", "2026-01-01T00:00:00+00:00"))
            state = {"remote_main": "a" * 40, "worktrees": []}
            common = (
                patch.object(handoffctl, "ROOT", root),
                patch.object(handoffctl, "locked", return_value=contextlib.nullcontext()),
                patch.object(handoffctl, "backend_selection", return_value={"backend": "git"}),
                patch.object(handoffctl, "sync_replica_before_write"),
                patch.object(handoffctl, "project_scan", return_value=state),
                patch.object(handoffctl, "all_tasks", return_value=[task_tuple]),
            )
            with (
                common[0],
                common[1],
                common[2],
                common[3],
                common[4],
                common[5],
                self.assertRaisesRegex(RuntimeError, "claim integrity"),
            ):
                handoffctl.reconcile(do_commit=False)
            args = Namespace(task="AR-1720")
            with (
                common[0],
                common[1],
                common[2],
                common[3],
                common[5],
                patch.object(handoffctl, "locate", return_value=task_tuple),
                self.assertRaisesRegex(RuntimeError, "claim integrity"),
            ):
                handoffctl.mutate(args, "heartbeat")


if __name__ == "__main__":
    unittest.main()
