# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Downstream coverage for public rollback-session failure contracts."""

from __future__ import annotations

import tempfile
import unittest
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path
from unittest.mock import patch

from fixture_ids import project_uuid

from tools.rollback_control_store import (
    BarrierSessionState,
    ControlStoreError,
    RecoveryRejectedError,
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
    """Keep real SQLite transitions isolated from the process-wide coordinator lock."""
    yield


class RollbackControlStoreEdgeTests(unittest.TestCase):
    def _identity(
        self,
        *,
        attempt: str = "attempt-1",
        revision: int = 3,
        authority: str = "authority-3",
        barrier: str = "barrier-1",
        fencing_value: str = "fence-1",
    ) -> BarrierSessionIdentity:
        record: dict[str, object] = {
            "schema_version": 1,
            "project_id": PROJECT,
            "attempt_id": attempt,
            "state_revision": revision,
            "authority_revision_at_acquire": authority,
            "durable_barrier_id": barrier,
            "fencing_token": fencing_value,
            "fencing_owner": "owner-1",
            "identity_digest": "0" * 64,
        }
        record["identity_digest"] = canonical_barrier_session_digest(record)
        return BarrierSessionIdentity.from_record(record)

    def _store(self, root: Path, authority: list[str]) -> SQLiteBarrierSessionStore:
        return SQLiteBarrierSessionStore(
            SQLiteRollbackControlStore(root / "control.sqlite", PROJECT), lambda: authority[0]
        )

    @staticmethod
    def _reopen_evidence(
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
            "project_id": identity.project_id,
            "target": target,
            "verified": True,
        }

    def test_cas_rejects_absent_stale_and_identity_changed_writes(self) -> None:
        authority = ["authority-3"]
        with (
            tempfile.TemporaryDirectory() as directory,
            patch("tools.rollback_control_store.locked", side_effect=_local_lock),
        ):
            store = self._store(Path(directory), authority)
            identity = self._identity()
            held = BarrierSessionState(identity, "held", 1)

            with self.assertRaisesRegex(ControlStoreError, "does not exist"):
                store.cas(1, held)
            self.assertEqual(held, store.create(identity))
            with self.assertRaisesRegex(ControlStoreError, "CAS conflict"):
                store.cas(0, held)
            changed = BarrierSessionState(
                self._identity(attempt="attempt-2", revision=4),
                "held",
                2,
            )
            with self.assertRaisesRegex(ControlStoreError, "identity changed"):
                store.cas(1, changed)

    def test_reopen_requires_matched_evidence_before_terminal_release(self) -> None:
        authority = ["authority-3"]
        with (
            tempfile.TemporaryDirectory() as directory,
            patch("tools.rollback_control_store.locked", side_effect=_local_lock),
        ):
            store = self._store(Path(directory), authority)
            identity = self._identity()
            store.create(identity)
            child = BarrierChildIdentity.bind(identity, "forward-1", "new")
            bound = store.bind_child(1, child)
            self.assertEqual(2, bound.revision)

            invalid_evidence = self._reopen_evidence(identity, child)
            invalid_evidence["target"] = "rollback"
            with self.assertRaisesRegex(ControlStoreError, "evidence identity"):
                store.begin_reopen(2, "new", invalid_evidence)
            reopening = store.begin_reopen(2, "new", self._reopen_evidence(identity, child))
            self.assertEqual(("releasing", 3), (reopening.status, reopening.revision))

            with self.assertRaisesRegex(ControlStoreError, "does not match reopen target"):
                store.complete_reopen(3, self._runtime_evidence(identity, "rollback"))
            invalid_runtime = self._runtime_evidence(identity, "new")
            invalid_runtime["foreign_key_violations"] = 1
            with self.assertRaisesRegex(ControlStoreError, "runtime evidence identity"):
                store.complete_reopen(3, invalid_runtime)
            released = store.complete_reopen(3, self._runtime_evidence(identity, "new"))
            self.assertEqual(("released", 4), (released.status, released.revision))
            with self.assertRaisesRegex(ControlStoreError, "transition is not permitted"):
                store.mark_ambiguous(4, "after-release")

    def test_ambiguous_recovery_requires_distinct_newer_fence_and_fresh_authority(self) -> None:
        authority = ["authority-3"]
        with (
            tempfile.TemporaryDirectory() as directory,
            patch("tools.rollback_control_store.locked", side_effect=_local_lock),
        ):
            store = self._store(Path(directory), authority)
            original = self._identity()
            store.create(original)
            ambiguous = store.mark_ambiguous(1, "commit-uncertain")
            self.assertEqual(("ambiguous", 2), (ambiguous.status, ambiguous.revision))

            with self.assertRaisesRegex(RecoveryRejectedError, "distinct newer fence"):
                store.reconcile_ambiguous(2, BarrierSessionState(original, "held", 1))
            replacement = self._identity(
                attempt="attempt-2",
                revision=4,
                authority="authority-4",
                barrier="barrier-2",
                fencing_value="fence-2",
            )
            with self.assertRaisesRegex(RecoveryRejectedError, "authority revision changed"):
                store.reconcile_ambiguous(2, BarrierSessionState(replacement, "held", 1))
            authority[0] = "authority-4"
            recovered = store.reconcile_ambiguous(2, BarrierSessionState(replacement, "held", 1))
            self.assertEqual(
                ("attempt-2", "held", 1),
                (
                    recovered.identity.attempt_id,
                    recovered.status,
                    recovered.revision,
                ),
            )
