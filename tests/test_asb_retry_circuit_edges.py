# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Downstream edge coverage for retry-circuit recovery and reservation fencing."""

from __future__ import annotations

import argparse
import copy
import unittest

from tools import retry_circuit

NOW = "2026-10-13T12:00:00+00:00"
EXPIRES = "2026-10-13T12:01:00+00:00"
LATER = "2026-10-13T12:02:00+00:00"


class RetryCircuitEdgeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.meta: retry_circuit.Meta = {
            "id": "AR-0001",
            "owner": "worker",
            "status": "in_progress",
            "task_revision": 2,
        }
        self.identity = retry_circuit.normalized_identity("a" * 64, "test", ["tests"])
        self.other = retry_circuit.normalized_identity("b" * 64, "read", ["docs"])

    def reserve(self, reservation_id: str = "b" * 32) -> None:
        retry_circuit.reserve(self.meta, self.identity, 3, reservation_id, NOW, EXPIRES)

    def hold(self) -> None:
        for revision in range(2, 5):
            self.meta["task_revision"] = revision
            retry_circuit.record_failure(
                self.meta, self.identity, "EXIT", 3, f"2026-10-13T12:00:0{revision}+00:00"
            )
        self.meta["task_revision"] = 5

    def test_expiry_is_retired_and_audited_before_a_new_reservation(self) -> None:
        self.reserve()
        self.assertEqual(1, retry_circuit.cleanup_expired(self.meta, LATER))
        state = self.meta["retry_circuit"]
        self.assertEqual([], state["reservations"])
        self.assertEqual("expired", state["abandoned"][-1]["cause"])
        self.assertEqual(LATER, state["abandoned"][-1]["cleaned_at"])
        self.assertIn(
            "expired_slots_cleaned=0",
            retry_circuit.reserve(
                self.meta, self.identity, 3, "c" * 32, LATER, "2026-10-13T12:03:00+00:00"
            ),
        )

    def test_expiry_cleanup_is_idempotent_and_rejects_invalid_timestamp(self) -> None:
        self.reserve()
        self.assertEqual(0, retry_circuit.cleanup_expired(self.meta, NOW))
        with self.assertRaisesRegex(ValueError, "cleanup timestamp"):
            retry_circuit.cleanup_expired(self.meta, "not-a-time")

    def test_successful_resolution_removes_an_empty_circuit_state(self) -> None:
        self.reserve()
        self.assertEqual(
            "Released retry circuit launch slot.",
            retry_circuit.resolve(self.meta, self.identity, "b" * 32, None, NOW),
        )
        self.assertNotIn("retry_circuit", self.meta)

    def test_failed_resolution_becomes_an_attempt_and_fences_wrong_slot(self) -> None:
        self.reserve()
        with self.assertRaisesRegex(RuntimeError, "not current"):
            retry_circuit.resolve(self.meta, self.other, "b" * 32, "EXIT", NOW)
        self.assertIn(
            "1/3", retry_circuit.resolve(self.meta, self.identity, "b" * 32, "RETRYABLE", NOW)
        )
        self.assertEqual("RETRYABLE", self.meta["retry_circuit"]["attempts"][-1]["failure"])
        with self.assertRaisesRegex(RuntimeError, "not current"):
            retry_circuit.resolution_revision(self.meta, self.identity, "b" * 32)

    def test_recovery_requires_the_held_identity_and_valid_reason(self) -> None:
        self.hold()
        with self.assertRaisesRegex(RuntimeError, "exact held"):
            retry_circuit.recover(self.meta, self.other, "retry-exception", "transient", NOW)
        with self.assertRaisesRegex(ValueError, "reason"):
            retry_circuit.recover(self.meta, self.identity, "retry-exception", "\n", NOW)
        with self.assertRaisesRegex(ValueError, "recovery input"):
            retry_circuit.recover(self.meta, self.identity, "unknown", "transient", NOW)
        self.assertIn(
            "retry-exception",
            retry_circuit.recover(self.meta, self.identity, "retry-exception", "transient", NOW),
        )

    def test_recovery_apply_cleans_elapsed_slot_but_rejects_live_slot(self) -> None:
        self.hold()
        retry_circuit.reserve(self.meta, self.other, 3, "c" * 32, NOW, EXPIRES)
        args = argparse.Namespace(
            owner="worker",
            expected_revision=5,
            attempt=self.identity,
            retry_circuit_action="changed-approach",
            reason="fresh controlled approach",
        )
        self.assertIn("recovered", retry_circuit.apply(args, self.meta, LATER))
        self.assertEqual([], self.meta["retry_circuit"]["reservations"])

    def test_apply_reserve_and_resolve_enforce_owner_and_exact_revision(self) -> None:
        reserve_args = argparse.Namespace(
            owner="other",
            expected_revision=2,
            retry_circuit_identity=self.identity,
            retry_window=3,
            retry_circuit_reservation="b" * 32,
            retry_circuit_expires_at=EXPIRES,
        )
        with self.assertRaisesRegex(RuntimeError, "active task owner"):
            retry_circuit.apply_reserve(reserve_args, self.meta, NOW)
        reserve_args.owner = "worker"
        reserve_args.expected_revision = 1
        with self.assertRaisesRegex(RuntimeError, "current task revision"):
            retry_circuit.apply_reserve(reserve_args, self.meta, NOW)
        reserve_args.expected_revision = 2
        retry_circuit.apply_reserve(reserve_args, self.meta, NOW)
        resolve_args = argparse.Namespace(
            owner="other",
            expected_revision=3,
            retry_circuit_identity=self.identity,
            retry_circuit_reservation="b" * 32,
            retry_circuit_failure=None,
        )
        self.meta["task_revision"] = 3
        with self.assertRaisesRegex(RuntimeError, "active task owner"):
            retry_circuit.apply_resolve(resolve_args, self.meta, NOW)
        resolve_args.owner = "worker"
        resolve_args.expected_revision = 4
        with self.assertRaisesRegex(RuntimeError, "immediately after"):
            retry_circuit.apply_resolve(resolve_args, self.meta, NOW)
        resolve_args.expected_revision = 3
        self.assertIn("Released", retry_circuit.apply_resolve(resolve_args, self.meta, NOW))

    def test_validation_rejects_duplicate_reservations_and_bad_abandoned_record(self) -> None:
        self.reserve()
        state = copy.deepcopy(self.meta["retry_circuit"])
        state["reservations"].append(copy.deepcopy(state["reservations"][0]))
        with self.assertRaisesRegex(ValueError, "duplicated"):
            retry_circuit.validate(state)
        state = copy.deepcopy(self.meta["retry_circuit"])
        reservation = state["reservations"].pop()
        state["abandoned"] = [{**reservation, "cleaned_at": NOW, "cause": "expired"}]
        with self.assertRaisesRegex(ValueError, "abandoned slot"):
            retry_circuit.validate(state)
