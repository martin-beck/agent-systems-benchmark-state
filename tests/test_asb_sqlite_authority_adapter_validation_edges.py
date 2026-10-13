# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Downstream validation and corruption coverage for SQLite authority reads."""

from __future__ import annotations

import sqlite3
import tempfile
import unittest
from collections.abc import Iterator
from contextlib import closing
from pathlib import Path
from unittest.mock import patch

from tools.authority_neutral_commit import CommitAdmissionBundle
from tools.sqlite_authority_adapter import SQLiteAuthorityAdapter, SQLiteAuthorityError

CONTEXT = {
    "schema_version": 2,
    "backend": "sqlite",
    "project_id": "project",
    "operation_id": "operation",
    "state_revision": 1,
    "authority_revision": "revision",
    "fencing_token": "token",
    "fencing_owner": "owner",
    "durable_barrier_id": "barrier",
    "artifact_root": "/artifacts",
    "source": "/source",
    "destination": "/destination",
    "manifest": "/manifest",
    "selector_ref": ".runtime/selector.json",
    "barrier_identity_digest": "0" * 64,
    "target": "new",
    "envelope_digest": "1" * 64,
}


class SQLiteAuthorityAdapterValidationEdgesTests(unittest.TestCase):
    def setUp(self) -> None:
        self.directory = tempfile.TemporaryDirectory()
        self.root = Path(self.directory.name)
        self.root.chmod(0o700)
        self.authority = self.root / "authority.sqlite"
        with closing(sqlite3.connect(self.authority)) as connection, connection:
            connection.execute("CREATE TABLE entries (id INTEGER PRIMARY KEY, body TEXT)")
            connection.execute("INSERT INTO entries(body) VALUES ('clean')")
        self.authority.chmod(0o600)
        self.adapter = SQLiteAuthorityAdapter(self.authority)

    def tearDown(self) -> None:
        self.directory.cleanup()

    def test_context_rejects_extra_missing_and_wrongly_typed_fields(self) -> None:
        invalid = (
            ({key: value for key, value in CONTEXT.items() if key != "manifest"}, "incomplete"),
            ({**CONTEXT, "unexpected": "value"}, "incomplete"),
            ({**CONTEXT, "backend": "git"}, "incomplete"),
            ({**CONTEXT, "schema_version": True}, "types"),
            ({**CONTEXT, "state_revision": 0}, "types"),
            ({**CONTEXT, "operation_id": ""}, "types"),
            ({**CONTEXT, "target": "apply"}, "target"),
        )
        for context, message in invalid:
            with (
                self.subTest(context=context),
                self.assertRaisesRegex(SQLiteAuthorityError, message),
            ):
                SQLiteAuthorityAdapter._context(context)

    def test_snapshot_rejects_invalid_phase_before_opening_database(self) -> None:
        with (
            patch("tools.sqlite_authority_adapter.sqlite3.connect") as connect,
            self.assertRaisesRegex(SQLiteAuthorityError, "phase is invalid"),
        ):
            self.adapter.snapshot("unknown", CONTEXT)
        connect.assert_not_called()

    def test_snapshot_fails_closed_on_real_corrupt_database_bytes(self) -> None:
        self.authority.write_bytes(b"not a SQLite database\x00corrupt")
        self.authority.chmod(0o600)
        with self.assertRaisesRegex(SQLiteAuthorityError, "observation failed"):
            self.adapter.snapshot("discover", CONTEXT)

    def test_snapshot_rejects_malformed_integrity_result_and_closes_connection(self) -> None:
        closed: list[bool] = []

        class Cursor:
            def fetchone(self) -> tuple[()]:
                return ()

            def __iter__(self) -> Iterator[object]:
                return iter(())

        class Connection:
            def execute(self, _statement: str) -> Cursor:
                return Cursor()

            def close(self) -> None:
                closed.append(True)

        with (
            patch("tools.sqlite_authority_adapter.sqlite3.connect", return_value=Connection()),
            self.assertRaisesRegex(SQLiteAuthorityError, "observation failed"),
        ):
            self.adapter.snapshot("discover", CONTEXT)
        self.assertEqual([True], closed)

    def test_rollback_context_rejects_nonrollback_target_before_snapshot(self) -> None:
        with (
            patch.object(self.adapter, "snapshot") as snapshot,
            self.assertRaisesRegex(SQLiteAuthorityError, "target is invalid"),
        ):
            self.adapter.verify_rollback_context(CONTEXT)
        snapshot.assert_not_called()

    def test_durable_rollback_binding_rejects_wrong_target_and_noncallable_effect(self) -> None:
        new_admission = CommitAdmissionBundle(
            backend="sqlite",
            target="new",
            operation_id="operation",
            fencing_token="token",  # noqa: S106
            state_revision=1,
            barrier_id="barrier",
            artifact_identity="artifact",
            manifest_identity="manifest",
            selector_identity="selector",
            runtime_identity="runtime",
        )
        rollback_admission = CommitAdmissionBundle(
            **{**new_admission.__dict__, "target": "rollback"}
        )
        for admission, effect in ((new_admission, lambda: None), (rollback_admission, object())):
            with (
                self.subTest(target=admission.target, callable=callable(effect)),
                self.assertRaisesRegex(SQLiteAuthorityError, "rollback capability binding"),
            ):
                self.adapter.bind_durable_rollback_capability(
                    admission, object(), session_revision=1, rollback_effect=effect
                )
