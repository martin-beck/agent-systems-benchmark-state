# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Downstream durability coverage for retry-circuit state recovery boundaries."""

from __future__ import annotations

import argparse
import copy
import datetime as dt
import unittest

from tools import retry_circuit

NOW = "2026-10-13T12:00:00+00:00"
LATER = "2026-10-13T12:02:00+00:00"
COMMIT = "c" * 40


class RetryCircuitRecoveryStateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.meta: retry_circuit.Meta = {
            "id": "AR-0001",
            "owner": "worker",
            "status": "in_progress",
            "task_revision": 2,
        }
        self.identity = retry_circuit.normalized_identity("a" * 64, "test", ["tests"])

    def _reserve(self, reservation: str = "b" * 32) -> None:
        retry_circuit.reserve(
            self.meta,
            self.identity,
            3,
            reservation,
            NOW,
            "2026-10-13T12:01:00+00:00",
        )

    def _hold(self) -> None:
        for revision in range(2, 5):
            self.meta["task_revision"] = revision
            retry_circuit.record_failure(
                self.meta, self.identity, "EXIT", 3, f"2026-10-13T12:00:0{revision}+00:00"
            )
        self.meta["task_revision"] = 5

    def test_metadata_error_reports_corrupt_durable_state_without_raising(self) -> None:
        self.assertIsNone(retry_circuit.metadata_error(self.meta))
        self.meta["retry_circuit"] = {"schema_version": 999}
        self.assertIn("fields are not exact", retry_circuit.metadata_error(self.meta) or "")

    def test_validation_rejects_hold_without_active_attempt_series(self) -> None:
        self._hold()
        state = copy.deepcopy(self.meta["retry_circuit"])
        state["attempts"] = state["attempts"][:-1]
        with self.assertRaisesRegex(ValueError, "insufficient attempts"):
            retry_circuit.validate(state)

    def test_changed_progress_allows_a_new_window_but_preserves_the_old_hold(self) -> None:
        self._hold()
        self.meta["checkpoint_commit"] = COMMIT
        self.assertIn(
            "1/4",
            retry_circuit.record_failure(
                self.meta, self.identity, "SUBPROCESS_TIMEOUT", 4, "2026-10-13T12:01:00+00:00"
            ),
        )
        self.assertEqual(3, self.meta["retry_circuit"]["hold"]["attempts"])
        self.assertEqual(4, self.meta["retry_circuit"]["attempts"][-1]["window"])

    def test_checkpoint_recovery_requires_and_records_the_current_checkpoint(self) -> None:
        self._hold()
        self.meta["checkpoint_commit"] = COMMIT
        self.assertEqual(
            "Retry circuit recovered by checkpoint.",
            retry_circuit.recover(
                self.meta, self.identity, "checkpoint", "durable checkpoint", NOW
            ),
        )
        recovery = self.meta["retry_circuit"]["recoveries"][-1]
        self.assertEqual(COMMIT, recovery["checkpoint_commit"])
        self.assertIsNone(self.meta["retry_circuit"]["hold"])

    def test_live_reservation_cleanup_rejects_then_expiry_unblocks_recovery(self) -> None:
        self._reserve()
        with self.assertRaisesRegex(RuntimeError, "live unbound"):
            retry_circuit.require_no_live_reservation(self.meta, NOW)
        retry_circuit.require_no_live_reservation(self.meta, LATER)
        self.assertEqual([], self.meta["retry_circuit"]["reservations"])
        self.assertEqual(1, len(self.meta["retry_circuit"]["abandoned"]))

    def test_apply_resolve_requires_post_reservation_revision_before_releasing(self) -> None:
        self._reserve()
        args = argparse.Namespace(
            owner="worker",
            expected_revision=3,
            retry_circuit_identity=self.identity,
            retry_circuit_reservation="b" * 32,
            retry_circuit_failure=None,
        )
        with self.assertRaisesRegex(RuntimeError, "immediately after"):
            retry_circuit.apply_resolve(args, self.meta, NOW)
        self.meta["task_revision"] = 3
        self.assertIn("Released", retry_circuit.apply_resolve(args, self.meta, NOW))
        self.assertNotIn("retry_circuit", self.meta)

    def test_cleanup_retains_only_bounded_abandoned_audit_records(self) -> None:
        start = dt.datetime(2026, 10, 13, 13, tzinfo=dt.UTC)
        for index in range(retry_circuit.MAX_ABANDONED + 2):
            reservation = f"{index:032x}"
            at = (start + dt.timedelta(minutes=index * 3)).isoformat()
            expires = (start + dt.timedelta(minutes=index * 3 + 1)).isoformat()
            retry_circuit.reserve(self.meta, self.identity, 3, reservation, at, expires)
            retry_circuit.cleanup_expired(
                self.meta, (start + dt.timedelta(minutes=index * 3 + 2)).isoformat()
            )
            self.meta["task_revision"] += 1
        abandoned = self.meta["retry_circuit"]["abandoned"]
        self.assertEqual(retry_circuit.MAX_ABANDONED, len(abandoned))
        self.assertEqual(f"{2:032x}", abandoned[0]["id"])
