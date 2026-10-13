# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Downstream rollback-control coverage for recovery and terminal edge cases."""

from __future__ import annotations

import json
import sqlite3
import tempfile
import unittest
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path
from unittest.mock import patch

from fixture_ids import project_uuid

from tools.rollback_control_store import (
    ControlStoreError,
    SQLiteBarrierSessionStore,
    SQLiteRollbackControlStore,
)
from tools.upgrade_identity import (
    BarrierChildIdentity,
    BarrierSessionIdentity,
    canonical_barrier_session_digest,
)

PROJECT = project_uuid("3")


@contextmanager
def _local_lock() -> Iterator[None]:
    """Avoid the process-wide coordinator lock for isolated SQLite fixtures."""
    yield


class RollbackControlStoreRecoveryEdgeTests(unittest.TestCase):
    def _identity(
        self,
        *,
        attempt: str = "attempt-1",
        revision: int = 3,
        authority: str = "authority-3",
        barrier: str = "barrier-1",
        fencing_token: str = "fence-1",  # noqa: S107 - opaque fencing fixture
    ) -> BarrierSessionIdentity:
        record: dict[str, object] = {
            "schema_version": 1,
            "project_id": PROJECT,
            "attempt_id": attempt,
            "state_revision": revision,
            "authority_revision_at_acquire": authority,
            "durable_barrier_id": barrier,
            "fencing_token": fencing_token,
            "fencing_owner": "owner-1",
            "identity_digest": "0" * 64,
        }
        record["identity_digest"] = canonical_barrier_session_digest(record)
        return BarrierSessionIdentity.from_record(record)

    @staticmethod
    def _child_evidence(
        identity: BarrierSessionIdentity, child: BarrierChildIdentity
    ) -> dict[str, object]:
        return {
            "operation_id": child.operation_id,
            "target": child.target,
            "barrier_identity_digest": identity.identity_digest,
            "validated": True,
        }

    @staticmethod
    def _runtime_evidence(identity: BarrierSessionIdentity, target: str) -> dict[str, object]:
        return {
            "authority_revision": identity.authority_revision_at_acquire,
            "backend": "sqlite",
            "backend_roundtrip": "sqlite",
            "foreign_key_violations": 0,
            "fencing_token": identity.fencing_token,
            "integrity_check": "ok",
            "project_id": PROJECT,
            "target": target,
            "verified": True,
        }

    def _store(self, root: Path, authority: list[str]) -> SQLiteBarrierSessionStore:
        return SQLiteBarrierSessionStore(
            SQLiteRollbackControlStore(root / "control.sqlite", PROJECT), lambda: authority[0]
        )

    def test_rollback_child_reopen_requires_the_registered_rollback_identity(self) -> None:
        authority = ["authority-3"]
        with (
            tempfile.TemporaryDirectory() as directory,
            patch("tools.rollback_control_store.locked", side_effect=_local_lock),
        ):
            store = self._store(Path(directory), authority)
            identity = self._identity()
            held = store.create(identity)
            forward = BarrierChildIdentity.bind(identity, "forward-1", "new")
            bound_forward = store.bind_child(held.revision, forward)
            rollback = BarrierChildIdentity.bind(identity, "rollback-1", "rollback")
            bound = store.bind_child(bound_forward.revision, rollback)

            forged = self._child_evidence(identity, rollback)
            forged["operation_id"] = forward.operation_id
            with self.assertRaisesRegex(ControlStoreError, "evidence identity"):
                store.begin_reopen(bound.revision, "rollback", forged)

            reopening = store.begin_reopen(
                bound.revision, "rollback", self._child_evidence(identity, rollback)
            )
            self.assertEqual(("releasing", "rollback"), (reopening.status, reopening.reopen_target))
            released = store.complete_reopen(
                reopening.revision, self._runtime_evidence(identity, "rollback")
            )
            self.assertEqual("released", released.status)
            with self.assertRaisesRegex(ControlStoreError, "transition is not permitted"):
                store.begin_reopen(
                    released.revision, "rollback", self._child_evidence(identity, rollback)
                )

    def test_released_session_preserves_history_and_rejects_non_new_replacement(self) -> None:
        authority = ["authority-3"]
        with (
            tempfile.TemporaryDirectory() as directory,
            patch("tools.rollback_control_store.locked", side_effect=_local_lock),
        ):
            root = Path(directory)
            store = self._store(root, authority)
            original = self._identity()
            held = store.create(original)
            child = BarrierChildIdentity.bind(original, "forward-1", "new")
            bound = store.bind_child(held.revision, child)
            releasing = store.begin_reopen(
                bound.revision, "new", self._child_evidence(original, child)
            )
            released = store.complete_reopen(
                releasing.revision, self._runtime_evidence(original, "new")
            )

            with self.assertRaisesRegex(ControlStoreError, "distinct newer project fence"):
                store.create(self._identity(attempt="attempt-2", authority="authority-3"))

            authority[0] = "authority-4"
            replacement = self._identity(
                attempt="attempt-2",
                revision=4,
                authority="authority-4",
                barrier="barrier-2",
                fencing_token="fence-2",  # noqa: S106 - opaque fencing fixture
            )
            new_held = store.create(replacement)
            self.assertEqual(
                ("attempt-2", "held", 1),
                (new_held.identity.attempt_id, new_held.status, new_held.revision),
            )
            with sqlite3.connect(root / "control.sqlite") as connection:
                row = connection.execute(
                    "SELECT revision,record_json FROM barrier_session_history "
                    "WHERE project_id=? AND attempt_id=?",
                    (PROJECT, original.attempt_id),
                ).fetchone()
            self.assertIsNotNone(row)
            assert row is not None
            self.assertEqual(released.revision, row[0])
            self.assertEqual("released", json.loads(row[1])["status"])

    def test_recovery_fences_prepared_authority_effect_as_terminal_ambiguity(self) -> None:
        authority = ["authority-3"]
        with (
            tempfile.TemporaryDirectory() as directory,
            patch("tools.rollback_control_store.locked", side_effect=_local_lock),
        ):
            root = Path(directory)
            store = self._store(root, authority)
            held = store.create(self._identity())
            intent = store.prepare_authority_effect(held.revision, "effect-1", "sqlite")

            recovered = store.recover_unknown()
            self.assertIsNotNone(recovered)
            assert recovered is not None
            self.assertEqual(
                ("ambiguous", held.revision + 1), (recovered.status, recovered.revision)
            )
            with sqlite3.connect(root / "control.sqlite") as connection:
                outcome = connection.execute(
                    "SELECT outcome,cause_code FROM authority_effect_intent WHERE intent_id=?",
                    (intent.intent_id,),
                ).fetchone()
            self.assertEqual(("ambiguous", "process-death"), outcome)
            with self.assertRaisesRegex(ControlStoreError, "session identity changed"):
                store.finish_authority_effect(intent, "committed")

    def test_malformed_persisted_child_encoding_fails_closed_on_reopen(self) -> None:
        authority = ["authority-3"]
        with (
            tempfile.TemporaryDirectory() as directory,
            patch("tools.rollback_control_store.locked", side_effect=_local_lock),
        ):
            root = Path(directory)
            store = self._store(root, authority)
            identity = self._identity()
            held = store.create(identity)
            child = BarrierChildIdentity.bind(identity, "forward-1", "new")
            store.bind_child(held.revision, child)
            with sqlite3.connect(root / "control.sqlite") as connection:
                connection.execute(
                    "UPDATE barrier_session SET forward_child=? WHERE project_id=?",
                    ('{"operation_id":"forged"}', PROJECT),
                )
                connection.commit()
            with self.assertRaisesRegex(ControlStoreError, "session state is invalid"):
                store.begin_reopen(2, "new", self._child_evidence(identity, child))
