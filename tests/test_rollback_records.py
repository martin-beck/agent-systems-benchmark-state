# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Tests for the durable fail-closed rollback journal."""

import json
import tempfile
import unittest
from pathlib import Path
from typing import Any
from unittest.mock import patch

from tools.rollback_records import (
    append_record,
    build_record,
    decode_records,
    latest_for_checkpoint,
    load_records,
    validate_record,
)


def checkpoint() -> dict[str, object]:
    return {
        "name": "AR-0079-r0003",
        "task": "AR-0079",
        "source_commit": "a" * 40,
    }


class RollbackRecordTests(unittest.TestCase):
    def test_state_transitions_are_valid_and_lookup_is_latest(self) -> None:
        record = build_record(checkpoint(), "b" * 40, "2026-09-24T00:00:00+00:00")
        validate_record(record)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            append_record(root, record)
            started = build_record(
                checkpoint(),
                "b" * 40,
                "2026-09-24T00:00:01+00:00",
                status="restore_started",
                operation_id=str(record["operation_id"]),
                revision=2,
            )
            append_record(root, started)
            latest = latest_for_checkpoint(root, str(record["checkpoint"]))
            self.assertIsNotNone(latest)
            assert latest is not None
            self.assertEqual("restore_started", latest["status"])
            self.assertEqual(2, len(load_records(root)))

    def test_decode_rejects_invalid_status_and_duplicate_shape(self) -> None:
        record = build_record(checkpoint(), "b" * 40, "now")
        record["status"] = "released"
        with self.assertRaisesRegex(ValueError, "invalid rollback status"):
            validate_record(record)
        with self.assertRaisesRegex(ValueError, "invalid rollback line"):
            decode_records(["[]"])
        with self.assertRaisesRegex(ValueError, "invalid rollback line"):
            decode_records(["not-json"])

    def test_builder_and_validator_reject_each_identity_boundary(self) -> None:
        valid = build_record(checkpoint(), "b" * 40, "now")
        cases: list[tuple[dict[str, Any], str]] = [
            ({"checkpoint": "bad"}, "invalid rollback checkpoint"),
            ({"task": "bad"}, "invalid rollback task"),
            ({"source_commit": "bad"}, "invalid rollback commit"),
            ({"current_commit": "bad"}, "invalid rollback commit"),
            ({"rollback_commit": "bad"}, "invalid rollback result commit"),
            ({"status": "bad"}, "invalid rollback status"),
            ({"revision": 0}, "invalid rollback revision"),
        ]
        for changes, message in cases:
            candidate = dict(valid)
            candidate.update(changes)
            with self.subTest(changes=changes), self.assertRaisesRegex(ValueError, message):
                validate_record(candidate)
        candidate = dict(valid)
        candidate.pop("task")
        with self.assertRaisesRegex(ValueError, "invalid rollback fields"):
            validate_record(candidate)
        with self.assertRaisesRegex(ValueError, "invalid rollback operation"):
            build_record(checkpoint(), "b" * 40, "now", operation_id="bad")
        invalid_builds = [
            (dict(checkpoint(), name="bad"), "invalid rollback checkpoint"),
            (dict(checkpoint(), task="bad"), "invalid rollback task"),
            (dict(checkpoint(), source_commit="bad"), "invalid rollback commit"),
        ]
        for invalid, message in invalid_builds:
            with self.subTest(invalid=invalid), self.assertRaisesRegex(ValueError, message):
                build_record(invalid, "b" * 40, "now")
        invalid = build_record(checkpoint(), "b" * 40, "now")
        invalid["recorded_at"] = ""
        with self.assertRaisesRegex(ValueError, "invalid rollback timestamp"):
            validate_record(invalid)
        invalid["recorded_at"] = "now"
        invalid["operation_id"] = "bad"
        with self.assertRaisesRegex(ValueError, "invalid rollback operation"):
            validate_record(invalid)

    def test_decoder_bound_and_append_fsync_failure_are_fail_closed(self) -> None:
        record = build_record(checkpoint(), "b" * 40, "now")
        with self.assertRaisesRegex(ValueError, "rollback journal exceeds bound"):
            decode_records([json.dumps(record)] * 65)
        with (
            tempfile.TemporaryDirectory() as directory,
            patch("tools.rollback_records.os.fsync", side_effect=OSError("fsync")),
            self.assertRaisesRegex(OSError, "fsync"),
        ):
            append_record(Path(directory), record)

    def test_completed_and_ambiguous_require_result_or_recovery(self) -> None:
        record = build_record(
            checkpoint(),
            "b" * 40,
            "now",
            status="rollback_completed",
            rollback_commit="c" * 40,
        )
        validate_record(record)
        ambiguous = dict(record)
        ambiguous["status"] = "ambiguous"
        ambiguous["rollback_commit"] = ""
        validate_record(ambiguous)


if __name__ == "__main__":
    unittest.main()
