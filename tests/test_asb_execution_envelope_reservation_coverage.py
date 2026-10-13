# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Downstream validation coverage for durable execution reservations."""

from __future__ import annotations

import unittest

from tools.execution_envelope import valid_reservation


def reservation(**changes: object) -> dict[str, object]:
    value: dict[str, object] = {
        "execution_id": "a" * 32,
        "owner": "worker",
        "task_revision": 1,
        "envelope_digest": "sha256:" + "b" * 64,
        "command_class": "read",
        "scope_digest": "sha256:" + "c" * 64,
        "argv_digest": "d" * 64,
        "expires_at": "2026-10-13T12:00:00+00:00",
    }
    value.update(changes)
    return value


class ExecutionEnvelopeReservationCoverageTests(unittest.TestCase):
    def test_valid_reservation_accepts_only_the_complete_canonical_shape(self) -> None:
        self.assertTrue(valid_reservation(reservation()))
        self.assertFalse(valid_reservation([]))
        self.assertFalse(valid_reservation(reservation(extra=True)))
        incomplete = reservation()
        incomplete.pop("owner")
        self.assertFalse(valid_reservation(incomplete))

    def test_valid_reservation_rejects_each_identity_and_digest_boundary(self) -> None:
        invalid = (
            {"execution_id": "not-an-id"},
            {"owner": ""},
            {"owner": "x" * 129},
            {"owner": 1},
            {"task_revision": 0},
            {"task_revision": True},
            {"envelope_digest": "sha256:bad"},
            {"command_class": "shell"},
            {"scope_digest": "bad"},
            {"argv_digest": "bad"},
            {"expires_at": "not-a-time"},
            {"expires_at": "2026-10-13T12:00:00"},
        )
        for changes in invalid:
            with self.subTest(changes=changes):
                self.assertFalse(valid_reservation(reservation(**changes)))
