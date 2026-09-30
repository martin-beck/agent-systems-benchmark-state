# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Contract and retention tests for durable work-session snapshots."""

import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from tools.session_records import (
    MAX_SESSION_BYTES,
    MAX_SESSION_RECORDS,
    append_session_record,
    build_session_record,
    decode_session_lines,
    latest_session,
)


def meta(revision: int = 1) -> dict[str, object]:
    return {
        "id": "AR-0001",
        "task_revision": revision,
        "status": "in_progress",
        "branch": "ar0001-example",
        "worktree_key": "example",
        "spec_ref": "spec.json",
        "spec_revision": 1,
        "next_action": "Continue the bounded task.",
    }


class SessionRecordTests(unittest.TestCase):
    def test_record_is_exact_and_content_minimized(self) -> None:
        record = build_session_record(meta(), "update", "2026-09-24T12:00:00+00:00")
        self.assertEqual(
            {
                "schema_version",
                "task",
                "task_revision",
                "recorded_at",
                "trigger",
                "status",
                "context_digest",
                "step_state",
                "artifact_refs",
                "next_action",
            },
            set(record),
        )
        self.assertNotIn("prompt", record)
        self.assertLessEqual(len(json.dumps(record, sort_keys=True).encode()), MAX_SESSION_BYTES)

    def test_append_retains_bounded_history_and_replays_latest(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            for revision in range(1, MAX_SESSION_RECORDS + 5):
                append_session_record(
                    root,
                    build_session_record(
                        meta(revision), "update", f"2026-09-24T12:00:{revision:02d}+00:00"
                    ),
                )
            records = decode_session_lines(root / "sessions/AR-0001.jsonl")
            self.assertEqual(MAX_SESSION_RECORDS, len(records))
            latest = latest_session(root, "AR-0001")
            self.assertIsNotNone(latest)
            assert latest is not None
            self.assertEqual(MAX_SESSION_RECORDS + 4, latest["task_revision"])

    def test_rejects_unsafe_or_oversized_next_action(self) -> None:
        with self.assertRaisesRegex(ValueError, "exceeds bounded size"):
            build_session_record(
                {**meta(), "next_action": "x" * MAX_SESSION_BYTES}, "update", "now"
            )
        with self.assertRaisesRegex(ValueError, "unknown session trigger"):
            build_session_record(meta(), "claim", "now")

    def test_rejects_each_malformed_record_boundary(self) -> None:
        valid = build_session_record(meta(), "update", "now")
        cases: tuple[tuple[dict[str, object], str], ...] = (
            ({"extra": True}, "fields are not exact"),
            ({"schema_version": 2}, "unsupported session"),
            ({"task": "bad"}, "invalid session record task"),
            ({"task_revision": 0}, "invalid session record revision"),
            ({"trigger": "claim"}, "invalid session record trigger"),
            ({"status": ""}, "invalid session record status"),
            ({"context_digest": "sha256:bad"}, "invalid session context digest"),
            ({"step_state": {}}, "invalid session step state"),
            ({"artifact_refs": [""]}, "invalid session artifact refs"),
            ({"next_action": "line\nbreak"}, "invalid session next action"),
        )
        for changes, message in cases:
            candidate = dict(valid)
            candidate.update(changes)
            with self.subTest(message=message), self.assertRaisesRegex(ValueError, message):
                from tools.session_records import validate_session_record

                validate_session_record(candidate)

    def test_artifact_refs_and_file_decoder_fail_closed(self) -> None:
        from tools.session_records import session_path

        record = build_session_record(
            {
                **meta(),
                "spec_acceptance": {"evidence_ref": "awq/evidence/AR-0001"},
                "checkpoint_commit": "a" * 40,
            },
            "update",
            "now",
        )
        self.assertEqual(3, len(record["artifact_refs"]))
        no_evidence = build_session_record(
            {**meta(), "spec_acceptance": {"evidence_ref": 1}}, "update", "now"
        )
        self.assertEqual(["spec:spec.json"], no_evidence["artifact_refs"])
        with self.assertRaisesRegex(ValueError, "invalid session task id"):
            session_path(Path("root"), "not-a-task")
        with TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "bad.jsonl"
            path.write_text("not-json\n")
            with self.assertRaisesRegex(ValueError, "line 1"):
                decode_session_lines(path)
            path.write_text("[]\n")
            with self.assertRaisesRegex(ValueError, "line 1"):
                decode_session_lines(path)
            path.write_text("\n".join(json.dumps(record) for _ in range(MAX_SESSION_RECORDS + 1)))
            with self.assertRaisesRegex(ValueError, "retention"):
                decode_session_lines(path)


if __name__ == "__main__":
    unittest.main()
