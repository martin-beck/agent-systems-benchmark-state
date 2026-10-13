# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Negative-path contracts for retry-circuit durable state validation."""

from __future__ import annotations

import argparse
import copy
import unittest

from tools import retry_circuit

NOW = "2026-10-13T12:00:00+00:00"
EXPIRES = "2026-10-13T12:01:00+00:00"


class RetryCircuitValidationEdgeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.meta: retry_circuit.Meta = {
            "id": "AR-0001",
            "owner": "worker",
            "status": "in_progress",
            "task_revision": 2,
        }
        self.identity = retry_circuit.normalized_identity("a" * 64, "test", ["tests"])

    def reserve(self) -> None:
        retry_circuit.reserve(self.meta, self.identity, 3, "b" * 32, NOW, EXPIRES)

    def failure(self) -> None:
        retry_circuit.record_failure(self.meta, self.identity, "EXIT", 3, NOW)

    def test_identity_rejects_malformed_digest_and_command_class(self) -> None:
        with self.assertRaisesRegex(ValueError, "command digest"):
            retry_circuit.normalized_identity("not-a-digest", "test", [])
        with self.assertRaisesRegex(ValueError, "command class"):
            retry_circuit.normalized_identity("a" * 64, "network", [])

    def test_progress_uses_only_the_latest_structured_drift_digest(self) -> None:
        baseline = retry_circuit.progress_digest(self.meta)
        self.meta["change_drift"] = [{"digest": "first"}, {"digest": "last"}]
        changed = retry_circuit.progress_digest(self.meta)
        self.assertNotEqual(baseline, changed)
        self.meta["change_drift"].append("unstructured")
        self.assertEqual(baseline, retry_circuit.progress_digest(self.meta))

    def test_input_validation_rejects_invalid_window_timestamps_and_failures(self) -> None:
        with self.assertRaisesRegex(ValueError, "window"):
            retry_circuit.reserve(self.meta, self.identity, True, "b" * 32, NOW, EXPIRES)
        with self.assertRaisesRegex(ValueError, "reservation timestamp"):
            retry_circuit.reserve(
                self.meta, self.identity, 3, "b" * 32, "2026-10-13T12:00:00", EXPIRES
            )
        with self.assertRaisesRegex(ValueError, "reservation expiry"):
            retry_circuit.reserve(self.meta, self.identity, 3, "b" * 32, NOW, NOW)
        with self.assertRaisesRegex(ValueError, "failure input"):
            retry_circuit.record_failure(self.meta, self.identity, "UNKNOWN", 3, NOW)

    def test_validation_rejects_corrupt_attempt_recovery_hold_and_reservation_fields(self) -> None:
        self.failure()
        state = copy.deepcopy(self.meta["retry_circuit"])
        state["attempts"][0].pop("window")
        with self.assertRaisesRegex(ValueError, "attempt fields"):
            retry_circuit.validate(state)

        self.meta["task_revision"] = 3
        retry_circuit.record_failure(self.meta, self.identity, "EXIT", 3, "2026-10-13T12:00:01+00:00")
        self.meta["task_revision"] = 4
        retry_circuit.record_failure(self.meta, self.identity, "EXIT", 3, "2026-10-13T12:00:02+00:00")
        self.meta["task_revision"] = 5
        retry_circuit.recover(self.meta, self.identity, "changed-approach", "new evidence", NOW)
        state = copy.deepcopy(self.meta["retry_circuit"])
        state["recoveries"][0]["checkpoint_commit"] = 42
        with self.assertRaisesRegex(ValueError, "recovery"):
            retry_circuit.validate(state)

        self.meta["retry_circuit"]["hold"] = {"identity": self.identity}
        with self.assertRaisesRegex(ValueError, "hold fields"):
            retry_circuit.validate(self.meta["retry_circuit"])

        self.meta.pop("retry_circuit")
        self.reserve()
        state = copy.deepcopy(self.meta["retry_circuit"])
        state["reservations"][0]["expires_at"] = NOW
        with self.assertRaisesRegex(ValueError, "reservation expiry"):
            retry_circuit.validate(state)

    def test_validation_rejects_schema_list_and_abandoned_record_corruption(self) -> None:
        self.reserve()
        state = copy.deepcopy(self.meta["retry_circuit"])
        state["schema_version"] = 2
        self.assertEqual("retry circuit schema is unsupported", retry_circuit.metadata_error({"retry_circuit": state}))

        state = copy.deepcopy(self.meta["retry_circuit"])
        state["reservations"] = "not-a-list"
        with self.assertRaisesRegex(ValueError, "reservations"):
            retry_circuit.validate(state)

        state = copy.deepcopy(self.meta["retry_circuit"])
        reservation = state["reservations"].pop()
        state["abandoned"] = [{**reservation, "cleaned_at": NOW, "cause": "expired", "extra": True}]
        with self.assertRaisesRegex(ValueError, "abandoned slot fields"):
            retry_circuit.validate(state)

    def test_successful_resolution_preserves_auditable_attempt_history(self) -> None:
        self.failure()
        self.meta["task_revision"] = 3
        self.reserve()
        self.assertEqual(
            "Released retry circuit launch slot.",
            retry_circuit.resolve(self.meta, self.identity, "b" * 32, None, NOW),
        )
        self.assertEqual(1, len(self.meta["retry_circuit"]["attempts"]))
        self.assertEqual([], self.meta["retry_circuit"]["reservations"])

    def test_apply_rejects_stale_revision_before_recovery(self) -> None:
        args = argparse.Namespace(
            owner="worker",
            expected_revision=1,
            attempt=self.identity,
            retry_circuit_action="changed-approach",
            reason="new evidence",
        )
        with self.assertRaisesRegex(RuntimeError, "current task revision"):
            retry_circuit.apply(args, self.meta, NOW)

