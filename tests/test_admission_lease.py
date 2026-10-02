# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Tests for the non-wired typed admission-lease contract."""

from __future__ import annotations

import dataclasses
import unittest

from tools.admission_lease import (
    LOCK_ORDER,
    AdmissionLeaseError,
    LockOrder,
    lease_from_record,
    validate_recheck,
)


class AdmissionLeaseTests(unittest.TestCase):
    def setUp(self) -> None:
        self.record = {
            "project_id": "project",
            "authority_revision": "authority-3",
            "fencing_token": "fence-1",
            "fencing_owner": "owner-1",
            "durable_barrier_id": "barrier-1",
            "revision": 4,
        }

    def test_lease_is_immutable_and_has_fixed_order(self) -> None:
        lease = lease_from_record(self.record)
        self.assertEqual(LOCK_ORDER, lease.order.names)
        with self.assertRaises(dataclasses.FrozenInstanceError):
            lease.revision = 5  # type: ignore[misc]
        with self.assertRaisesRegex(AdmissionLeaseError, "lock order"):
            LockOrder(("control", "common", "authority"))

    def test_recheck_requires_exact_identity_and_revision(self) -> None:
        lease = lease_from_record(self.record)
        checked = validate_recheck(lease, **self.record)
        self.assertEqual(lease, checked.lease)
        for field, value in (
            ("fencing_token", "other"),
            ("authority_revision", "authority-4"),
            ("revision", 5),
        ):
            changed = dict(self.record)
            changed[field] = value
            with self.subTest(field=field), self.assertRaisesRegex(AdmissionLeaseError, "changed"):
                validate_recheck(lease, **changed)

    def test_malformed_records_fail_closed(self) -> None:
        for field, value in (("project_id", ""), ("revision", True), ("fencing_token", 1)):
            malformed = dict(self.record)
            malformed[field] = value
            with self.subTest(field=field), self.assertRaises(AdmissionLeaseError):
                lease_from_record(malformed)
        with self.assertRaisesRegex(AdmissionLeaseError, "fields"):
            lease_from_record({**self.record, "status": "held"})
