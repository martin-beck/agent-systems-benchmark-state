# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Validation, retention and precedence tests for user directives."""

import json
import tempfile
import unittest
from pathlib import Path
from typing import Any
from unittest.mock import patch

import jsonschema

from tools.directive_records import (
    append_directive,
    applicable_directives,
    build_directive,
    conflicting_directives,
    decode_directives,
    latest_directives,
    scopes_overlap,
    validate_directive,
)


def directive(**changes: object) -> dict[str, Any]:
    values: dict[str, Any] = {
        "directive_id": "UD-0001",
        "authority": "BOARD-001",
        "precedence": 10,
        "scope": {"roles": ["implementer"], "tasks": []},
        "statement": "Preserve the verified release boundary.",
        "recorded_at": "2026-09-24T00:00:00+00:00",
        "owner": "board-chair",
        "claim_expires": "2026-09-24T01:00:00+00:00",
    }
    values.update(changes)
    return build_directive(**values)


class DirectiveRecordTests(unittest.TestCase):
    def test_builds_exact_record_and_normalizes_scope(self) -> None:
        record = directive(scope={"roles": ["z-role", "a-role"], "tasks": ["AR-0002"]})
        validate_directive(record)
        self.assertEqual(["a-role", "z-role"], record["scope"]["roles"])
        self.assertEqual(1, record["revision"])

    def test_rejects_invalid_identity_scope_and_content(self) -> None:
        cases: tuple[tuple[dict[str, object], str], ...] = (
            ({"directive_id": "bad"}, "directive id"),
            ({"authority": "x"}, "authority"),
            ({"scope": {"roles": [], "tasks": []}}, "scope"),
            ({"statement": "line\nline"}, "statement"),
            ({"guidance_ref": "AR-0001"}, "guidance"),
        )
        for change, message in cases:
            with self.subTest(message=message), self.assertRaisesRegex(ValueError, message):
                directive(**change)

    def test_rejects_all_structural_and_lifecycle_boundaries(self) -> None:
        cases: tuple[tuple[dict[str, object], str], ...] = (
            ({"scope": {"roles": ["implementer"]}}, "scope must contain"),
            ({"scope": {"roles": "implementer", "tasks": []}}, "scope values"),
            ({"scope": {"roles": ["implementer", "implementer"], "tasks": []}}, "duplicates"),
            ({"scope": {"roles": ["x"], "tasks": []}}, "role scope"),
            ({"scope": {"roles": [1], "tasks": []}}, "role scope"),
            ({"authority": "x"}, "authority"),
            ({"precedence": 0}, "precedence"),
            ({"lifecycle": "unknown"}, "lifecycle"),
            ({"revision": 0}, "revision"),
            ({"owner": "x"}, "owner"),
            ({"claim_expires": 7}, "lease"),
            ({"recorded_at": ""}, "created_at"),
        )
        for change, message in cases:
            with self.subTest(message=message), self.assertRaisesRegex(ValueError, message):
                directive(**change)
        for field, value, message in (
            ("directive_id", "bad", "directive id"),
            ("authority", "x", "authority"),
            ("precedence", 0, "precedence"),
        ):
            record = directive()
            record[field] = value
            with self.subTest(field=field), self.assertRaisesRegex(ValueError, message):
                validate_directive(record)

    def test_decode_and_latest_reject_malformed_or_nonmonotonic_journal(self) -> None:
        with self.assertRaisesRegex(ValueError, "line 1"):
            decode_directives(["not-json"])
        with self.assertRaisesRegex(ValueError, "line 1"):
            decode_directives(["[]"])
        with self.assertRaisesRegex(ValueError, "exceeds bound"):
            decode_directives([json.dumps(directive())] * 65)
        first = directive()
        second = dict(first, revision=1)
        with (
            tempfile.TemporaryDirectory() as temporary,
            self.assertRaisesRegex(ValueError, "strictly increasing"),
        ):
            root = Path(temporary)
            append_directive(root, first)
            path = root / "directives/records.jsonl"
            path.write_text(path.read_text() + json.dumps(second) + "\n")
            latest_directives(root)

    def test_append_fsync_failure_is_reported_and_temporary_removed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            with (
                patch("tools.directive_records.os.fsync", side_effect=OSError("fsync")),
                self.assertRaisesRegex(OSError, "fsync"),
            ):
                append_directive(root, directive())
            self.assertEqual([], list((root / "directives").glob("*.tmp")))

    def test_append_enforces_per_directive_cas_and_bounded_history(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            first = directive()
            append_directive(root, first)
            second = dict(first, revision=2, updated_at="2026-09-24T00:01:00+00:00")
            append_directive(root, second)
            with self.assertRaisesRegex(ValueError, "next CAS"):
                append_directive(root, dict(first, revision=4))
            self.assertEqual(1, len(latest_directives(root)))
            self.assertEqual(
                2,
                len(
                    decode_directives((root / "directives/records.jsonl").read_text().splitlines())
                ),
            )

    def test_scope_overlap_and_equal_precedence_conflict(self) -> None:
        active = directive(directive_id="UD-0001", lifecycle="active")
        same = directive(directive_id="UD-0002", lifecycle="active", statement="Stop the release.")
        lower = directive(
            directive_id="UD-0003", lifecycle="active", precedence=9, statement="Different."
        )
        self.assertTrue(scopes_overlap(active, same))
        self.assertEqual([active], conflicting_directives([active, lower], same))

    def test_different_scope_or_statement_is_not_a_conflict(self) -> None:
        active = directive(directive_id="UD-0001", lifecycle="active")
        other_role = directive(
            directive_id="UD-0002",
            lifecycle="active",
            scope={"roles": ["reviewer"], "tasks": []},
            statement="Different.",
        )
        same_statement = directive(directive_id="UD-0003", lifecycle="active")
        self.assertFalse(scopes_overlap(active, other_role))
        self.assertEqual([], conflicting_directives([active, other_role], same_statement))

    def test_applicable_directives_are_precedence_ordered(self) -> None:
        low = directive(directive_id="UD-0001", lifecycle="active", precedence=2)
        high = directive(directive_id="UD-0002", lifecycle="active", precedence=20)
        self.assertEqual(
            ["UD-0002", "UD-0001"],
            [
                item["directive_id"]
                for item in applicable_directives([low, high], role="implementer")
            ],
        )
        with self.assertRaisesRegex(ValueError, "requires a role"):
            applicable_directives([low], role="", task="")
        with self.assertRaisesRegex(ValueError, "invalid directive role"):
            applicable_directives([low], role="x")
        with self.assertRaisesRegex(ValueError, "invalid directive task"):
            applicable_directives([low], task="bad")
        self.assertEqual([], applicable_directives([low], task="AR-0001"))

    def test_json_schema_matches_terminal_empty_lease_and_owner(self) -> None:
        schema = json.loads(Path("schema/directive-record.schema.json").read_text())
        record = directive(lifecycle="revoked", owner="", claim_expires="", guidance_ref="")
        jsonschema.Draft202012Validator(schema).validate(record)


if __name__ == "__main__":
    unittest.main()
