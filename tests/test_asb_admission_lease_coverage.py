# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""ASB-owned fail-closed coverage for the read-only admission lease contract."""

from __future__ import annotations

import unittest

from tools.admission_lease import (
    AdmissionLease,
    AdmissionLeaseError,
    AdmissionRecheck,
    LockOrder,
    lease_from_record,
    validate_recheck,
)


class ASBAdmissionLeaseCoverageTests(unittest.TestCase):
    def setUp(self) -> None:
        self.record: dict[str, object] = {
            "project_id": "asb-state",
            "authority_revision": "main:0123456789abcdef",
            "fencing_token": "fence-42",
            "fencing_owner": "worker-asb",
            "durable_barrier_id": "barrier-42",
            "revision": 42,
        }

    def test_validation_rejects_direct_corrupt_lease_shapes(self) -> None:
        fields = {
            "project_id": "",
            "authority_revision": b"revision",
            "fencing_token": True,
            "fencing_owner": None,
            "durable_barrier_id": 0,
            "revision": 0,
        }
        for field, value in fields.items():
            with self.subTest(field=field), self.assertRaises(AdmissionLeaseError):
                AdmissionLease(**{**self.record, field: value})  # type: ignore[arg-type]
        with self.assertRaisesRegex(AdmissionLeaseError, "order"):
            AdmissionLease(**self.record, order=object())  # type: ignore[arg-type]

    def test_recheck_rejects_each_corrupted_identity_observation(self) -> None:
        lease = lease_from_record(self.record)
        corruptions = {
            "project_id": "other-project",
            "authority_revision": "main:replaced",
            "fencing_token": "fence-replaced",
            "fencing_owner": "other-worker",
            "durable_barrier_id": "barrier-replaced",
            "revision": 43,
        }
        for field, value in corruptions.items():
            with self.subTest(field=field), self.assertRaisesRegex(AdmissionLeaseError, "changed"):
                validate_recheck(lease, **{**self.record, field: value})
        with self.assertRaisesRegex(AdmissionLeaseError, "lease"):
            validate_recheck(object(), **self.record)  # type: ignore[arg-type]

    def test_corrupt_durable_snapshot_fails_closed_then_exact_restore_rechecks(self) -> None:
        original = dict(self.record)
        lease = lease_from_record(original)
        corrupt = {**original, "durable_barrier_id": ""}
        with self.assertRaisesRegex(AdmissionLeaseError, "identity"):
            lease_from_record(corrupt)

        restored = lease_from_record(original)
        recheck = validate_recheck(restored, **original)
        self.assertEqual(lease, restored)
        self.assertEqual(restored, recheck.lease)
        self.assertEqual(42, recheck.revision)

    def test_record_schema_and_recheck_constructor_are_strict(self) -> None:
        for corrupt in (
            {key: value for key, value in self.record.items() if key != "revision"},
            {**self.record, "unexpected": "forged"},
            {**self.record, "revision": False},
        ):
            with self.subTest(corrupt=corrupt), self.assertRaises(AdmissionLeaseError):
                lease_from_record(corrupt)

        lease = lease_from_record(self.record)
        with self.assertRaisesRegex(AdmissionLeaseError, "lease"):
            AdmissionRecheck(
                lease=object(),  # type: ignore[arg-type]
                **self.record,
            )
        with self.assertRaisesRegex(AdmissionLeaseError, "changed"):
            AdmissionRecheck(lease=lease, **{**self.record, "revision": 41})
        with self.assertRaisesRegex(AdmissionLeaseError, "lock order"):
            LockOrder(names=("authority", "control", "common"))
