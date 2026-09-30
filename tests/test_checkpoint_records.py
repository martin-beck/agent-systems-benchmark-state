# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Tests for bounded task checkpoint records."""

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools.checkpoint_records import (
    MAX_CHECKPOINTS,
    append_checkpoint,
    build_checkpoint,
    decode_checkpoints,
    load_checkpoints,
    validate_checkpoint,
)


def task(revision: int = 2) -> dict[str, object]:
    return {
        "id": "AR-0079",
        "task_revision": revision,
        "status": "in_progress",
        "owner": "worker",
        "checkpoint_commit": "",
        "spec_ref": "plans/AR-0079.md",
        "spec_acceptance": {"evidence_ref": "PR-1"},
    }


class CheckpointRecordsTests(unittest.TestCase):
    def test_shape_contains_state_artifacts_and_digests(self) -> None:
        record = build_checkpoint(task(), "# task\n", "a" * 40, "2026-09-24T00:00:00+00:00")
        validate_checkpoint(record)
        self.assertEqual("AR-0079-r0002", record["name"])
        self.assertEqual(["spec:plans/AR-0079.md", "evidence:PR-1"], record["artifact_refs"])
        self.assertNotIn("# task", json.dumps(record))

    def test_append_is_bounded_and_loads_latest_history(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for revision in range(1, MAX_CHECKPOINTS + 4):
                append_checkpoint(
                    root,
                    build_checkpoint(
                        task(revision), "body", "b" * 40, f"2026-09-24T00:00:{revision:02d}+00:00"
                    ),
                )
            records = load_checkpoints(root, "AR-0079")
            self.assertEqual(MAX_CHECKPOINTS, len(records))
            self.assertEqual(4, records[0]["task_revision"])

    def test_decoder_rejects_corruption_and_bad_commit(self) -> None:
        with self.assertRaisesRegex(ValueError, "invalid checkpoint line"):
            decode_checkpoints(["not-json"])
        with self.assertRaisesRegex(ValueError, "source commit"):
            build_checkpoint(task(), "body", "bad", "now")

    def test_rejects_each_invalid_record_boundary(self) -> None:
        valid = build_checkpoint(task(), "body", "a" * 40, "now")
        cases = [
            ("schema_version", 2, "unsupported checkpoint schema"),
            ("task", "bad", "invalid checkpoint task"),
            ("name", "bad", "invalid checkpoint name"),
            ("task_revision", 0, "invalid checkpoint revision"),
            ("recorded_at", "", "invalid checkpoint timestamp"),
            ("source_commit", "bad", "invalid checkpoint source commit"),
            ("state", [], "invalid checkpoint state"),
            ("body_digest", "bad", "invalid checkpoint body digest"),
            ("artifact_refs", [""], "invalid checkpoint artifact refs"),
        ]
        for field, value, message in cases:
            candidate = dict(valid)
            candidate[field] = value
            if field == "task_revision":
                candidate["name"] = "AR-0079-r0000"
            with self.subTest(field=field), self.assertRaisesRegex(ValueError, message):
                validate_checkpoint(candidate)
        candidate = dict(valid)
        del candidate["state"]
        with self.assertRaisesRegex(ValueError, "invalid checkpoint fields"):
            validate_checkpoint(candidate)

    def test_decoder_rejects_non_object_and_overlong_history(self) -> None:
        record = build_checkpoint(task(), "body", "a" * 40, "now")
        with self.assertRaisesRegex(ValueError, "invalid checkpoint line"):
            decode_checkpoints(["[]"])
        with self.assertRaisesRegex(ValueError, "checkpoint history exceeds bound"):
            decode_checkpoints([json.dumps(record)] * (MAX_CHECKPOINTS + 1))

    def test_paths_and_all_task_loading_are_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            append_checkpoint(root, build_checkpoint(task(), "body", "a" * 40, "now"))
            other = dict(task())
            other["id"] = "AR-0002"
            append_checkpoint(root, build_checkpoint(other, "body", "b" * 40, "now"))
            self.assertEqual(2, len(load_checkpoints(root)))
            with self.assertRaisesRegex(ValueError, "invalid checkpoint task"):
                load_checkpoints(root, "bad")
            with (
                patch("tools.checkpoint_records.os.fsync", side_effect=OSError("fsync")),
                self.assertRaisesRegex(OSError, "fsync"),
            ):
                append_checkpoint(root, build_checkpoint(task(3), "body", "c" * 40, "now"))


if __name__ == "__main__":
    unittest.main()
