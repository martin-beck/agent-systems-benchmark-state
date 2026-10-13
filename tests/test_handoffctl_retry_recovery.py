# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""End-to-end retry-slot fencing for expired-claim recovery."""

from __future__ import annotations

import argparse
from unittest.mock import patch

import test_handoffctl as _handoffctl


class RetryRecoveryTest(_handoffctl.HandoffTest):
    def test_recover_expired_fences_live_unbound_retry_and_cleans_expired_slots(self) -> None:
        path = self.make_task(
            status="in_progress", owner="worker-a", claim_expires="2000-01-01T00:00:00+00:00"
        )
        meta, body = _handoffctl.CORE.read_task(path)
        identity = _handoffctl.CORE.retry_circuit.normalized_identity("a" * 64, None, [])
        _handoffctl.CORE.retry_circuit.reserve(
            meta, identity, 3, "b" * 32, "2026-10-13T12:00:00+00:00", "2099-01-01T00:00:00+00:00"
        )
        _handoffctl.CORE.write_task(path, meta, body)
        self.refresh_views()
        args = argparse.Namespace(
            task="AR-0001",
            expected_revision=1,
            allow_legacy_without_identity=True,
            note="No live process remains.",
        )
        with (
            patch.object(_handoffctl.CORE, "commit", return_value=True) as commit,
            self.assertRaisesRegex(RuntimeError, "RETRY_CIRCUIT_IN_PROGRESS"),
        ):
            _handoffctl.CORE.mutate(args, "recover-expired")
        commit.assert_not_called()
        self.assertEqual("in_progress", _handoffctl.CORE.read_task(path)[0]["status"])
        meta, body = _handoffctl.CORE.read_task(path)
        meta["retry_circuit"]["reservations"][0].update(
            reserved_at="1999-12-31T23:59:00+00:00", expires_at="2000-01-01T00:00:00+00:00"
        )
        _handoffctl.CORE.write_task(path, meta, body)
        self.refresh_views()
        with patch.object(_handoffctl.CORE, "commit", return_value=True):
            _handoffctl.CORE.mutate(args, "recover-expired")
        recovered, _ = _handoffctl.CORE.read_task(path)
        self.assertEqual("open", recovered["status"])
        self.assertEqual([], recovered["retry_circuit"]["reservations"])
        self.assertEqual(1, len(recovered["retry_circuit"]["abandoned"]))
