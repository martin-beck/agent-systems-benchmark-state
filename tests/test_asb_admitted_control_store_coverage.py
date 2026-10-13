# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""ASB-owned durability coverage for admitted control-store writes."""

from __future__ import annotations

import json
import sqlite3
import tempfile
import unittest
from collections.abc import Iterator, Mapping
from contextlib import contextmanager
from pathlib import Path
from typing import Any

from tools.admission_lease import AdmissionLease, AdmissionLeaseError, validate_recheck
from tools.admitted_control_store import AdmittedControlBinding, admitted_cas


class _PrivateScope:
    def assert_ordered(self) -> None:
        return None

    @contextmanager
    def hold(self) -> Iterator[None]:
        yield None


class _PrivateDurableStore:
    """Tiny private SQLite CAS fixture; it never reaches coordinator locks."""

    def __init__(self, path: Path) -> None:
        self.path = path
        with sqlite3.connect(path) as connection:
            connection.execute(
                "CREATE TABLE admitted (id INTEGER PRIMARY KEY CHECK (id = 1), revision INTEGER, payload TEXT)"
            )
            connection.execute("INSERT INTO admitted VALUES (1, 1, ?)", (json.dumps({}),))

    def cas(self, expected_revision: int, record: Mapping[str, object]) -> dict[str, object]:
        with sqlite3.connect(self.path) as connection:
            revision, payload = connection.execute(
                "SELECT revision, payload FROM admitted WHERE id = 1"
            ).fetchone()
            if revision != expected_revision:
                raise RuntimeError("durable revision conflict")
            next_record = dict(record, revision=expected_revision + 1)
            connection.execute(
                "UPDATE admitted SET revision = ?, payload = ? WHERE id = 1",
                (expected_revision + 1, json.dumps(next_record)),
            )
            return json.loads(connection.execute("SELECT payload FROM admitted WHERE id = 1").fetchone()[0])


class ASBAdmittedControlStoreCoverageTests(unittest.TestCase):
    def setUp(self) -> None:
        self.lease = AdmissionLease("project", "authority", "fence", "owner", "barrier", 1)
        self.recheck = validate_recheck(
            self.lease,
            project_id="project",
            authority_revision="authority",
            fencing_token="fence",  # noqa: S106
            fencing_owner="owner",
            durable_barrier_id="barrier",
            revision=1,
        )
        self.record: dict[str, object] = {
            "project_id": "project",
            "authority_revision": "authority",
            "fencing_token": "fence",
            "fencing_owner": "owner",
            "durable_barrier_id": "barrier",
            "status": "held",
        }

    def test_durable_corruption_is_rejected_then_repaired_record_can_commit(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            store = _PrivateDurableStore(Path(temporary) / "admitted.sqlite")
            with sqlite3.connect(store.path) as connection:
                connection.execute(
                    "CREATE TRIGGER corrupt_owner AFTER UPDATE ON admitted "
                    "BEGIN UPDATE admitted SET payload = json_set(payload, '$.fencing_owner', 'foreign') "
                    "WHERE id = 1; END"
                )
            with self.assertRaisesRegex(AdmissionLeaseError, "identity is invalid"):
                admitted_cas(store, 1, self.record, self.lease, self.recheck, _PrivateScope())
            with sqlite3.connect(store.path) as connection:
                connection.execute("DROP TRIGGER corrupt_owner")
                connection.execute("UPDATE admitted SET revision = 1, payload = ? WHERE id = 1", (json.dumps({}),))
            result = admitted_cas(store, 1, self.record, self.lease, self.recheck, _PrivateScope())
        self.assertEqual(2, result["revision"])
        self.assertEqual("owner", result["fencing_owner"])

    def test_binding_and_scope_fail_closed_without_durable_write(self) -> None:
        class BrokenScope:
            def assert_ordered(self) -> None:
                return None

            def hold(self) -> Any:
                return None

        with tempfile.TemporaryDirectory() as temporary:
            store = _PrivateDurableStore(Path(temporary) / "admitted.sqlite")
            binding = AdmittedControlBinding.bind(store, self.lease, self.recheck, BrokenScope())
            with self.assertRaisesRegex(AdmissionLeaseError, "scope is invalid"):
                binding.validated_scope().__enter__()
            with sqlite3.connect(store.path) as connection:
                self.assertEqual(1, connection.execute("SELECT revision FROM admitted").fetchone()[0])

    def test_invalid_scope_and_record_are_rejected_before_private_store(self) -> None:
        class InvalidRecord(Mapping[str, object]):
            def __getitem__(self, key: str) -> object:
                raise KeyError(key)

            def __iter__(self) -> Iterator[str]:
                raise ValueError("corrupt durable payload")

            def __len__(self) -> int:
                return 1

        with tempfile.TemporaryDirectory() as temporary:
            store = _PrivateDurableStore(Path(temporary) / "admitted.sqlite")
            with self.assertRaisesRegex(AdmissionLeaseError, "scope is required"):
                admitted_cas(store, 1, self.record, self.lease, self.recheck, object())  # type: ignore[arg-type]
            with self.assertRaisesRegex(AdmissionLeaseError, "record is invalid"):
                admitted_cas(store, 1, InvalidRecord(), self.lease, self.recheck, _PrivateScope())
            with sqlite3.connect(store.path) as connection:
                self.assertEqual(1, connection.execute("SELECT revision FROM admitted").fetchone()[0])
