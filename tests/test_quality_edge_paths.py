# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Public edge-path tests for non-upgrade-engine quality gates."""

from __future__ import annotations

import math
import unittest

from tools.upgrade_admission import (
    AdmissionError,
    admit_preflight,
    admit_quiesced,
    admit_reopen,
    admit_safe_mode,
    recheck_before_replacement,
)
from tools.upgrade_identity import (
    UpgradeIdentityError,
    canonical_barrier_digest,
    canonical_envelope_digest,
    validate_envelope,
)

PROJECT = "11111111-1111-4111-8111-111111111111"
ADMISSION_TRUE_FIELDS = (
    "release_authentic",
    "runtime_supported",
    "state_clean",
    "state_synchronized",
    "no_divergence",
    "no_active_leases",
    "no_wrapped_commands",
    "no_reconciliation",
    "no_publication",
    "binding_valid",
    "backend_valid",
    "vendor_valid",
    "disk_capacity_ok",
    "scratch_capacity_ok",
    "backup_destination_restorable",
    "maintenance_barrier",
    "barrier_acquired_before_quiescence",
    "barrier_reopen_verified",
    "functional_available",
    "workers_drained",
    "leases_fenced",
    "wrapped_commands_drained",
    "reconciliation_stopped",
    "publication_stopped",
    "runtime_validated",
    "backend_roundtrip_valid",
    "projections_valid",
    "lease_fence_valid",
)


def envelope(**changes: object) -> dict[str, object]:
    value: dict[str, object] = {
        "schema_version": 2,
        "backend": "sqlite",
        "project_id": PROJECT,
        "operation_id": "op-quality",
        "state_revision": 1,
        "authority_revision": "authority-1",
        "fencing_token": "fence-1",
        "fencing_owner": "owner-1",
        "durable_barrier_id": "barrier-1",
        "artifact_root": "/artifacts",
        "source": "/authority.sqlite",
        "destination": "/artifacts/backup.sqlite",
        "manifest": "/artifacts/manifest.json",
        "selector_ref": ".runtime/runtime-selector.json",
        "barrier_identity_digest": "0" * 64,
        "target": "new",
        "envelope_digest": "0" * 64,
    }
    value.update(changes)
    value["barrier_identity_digest"] = canonical_barrier_digest(value)
    value["envelope_digest"] = canonical_envelope_digest(value)
    return value


def admission_snapshot(**changes: object) -> dict[str, object]:
    value = envelope(
        **dict.fromkeys(
            ADMISSION_TRUE_FIELDS,
            True,
        ),
        durable_barrier_id="barrier-1",
        barrier_status="held",
        reopen_barrier_status="released",
        safe_mode_ready=True,
    )
    value.update(changes)
    value["barrier_identity_digest"] = canonical_barrier_digest(value)
    value["envelope_digest"] = canonical_envelope_digest(value)
    return value


class QualityEdgePathTests(unittest.TestCase):
    def test_identity_rejects_noncanonical_json_and_missing_fields(self) -> None:
        noncanonical = envelope()
        noncanonical["state_revision"] = math.nan
        with self.assertRaises(UpgradeIdentityError):
            canonical_envelope_digest(noncanonical)
        with self.assertRaises(UpgradeIdentityError):
            canonical_envelope_digest({"schema_version": 2})

    def test_identity_rejects_invalid_project_and_aliasing(self) -> None:
        for mutation in (
            {"project_id": 7},
            {"artifact_root": "/"},
            {"destination": "/artifacts"},
            {"source": "/authority.sqlite", "manifest": "/authority.sqlite"},
        ):
            with self.subTest(mutation=mutation), self.assertRaises(UpgradeIdentityError):
                validate_envelope(envelope(**mutation))

    def test_identity_rejects_digest_tampering(self) -> None:
        value = envelope()
        value["envelope_digest"] = "f" * 64
        with self.assertRaises(UpgradeIdentityError):
            validate_envelope(value)

    def test_admission_requires_durable_barrier_proof(self) -> None:
        value = admission_snapshot(durable_barrier_id="")
        with self.assertRaisesRegex(AdmissionError, "invalid identity envelope"):
            admit_quiesced(value)
        with self.assertRaisesRegex(AdmissionError, "invalid identity envelope"):
            admit_reopen(value)
        with self.assertRaisesRegex(AdmissionError, "invalid identity envelope"):
            admit_safe_mode(value)

    def test_admission_rejects_invalid_reopen_and_safe_mode_states(self) -> None:
        with self.assertRaisesRegex(AdmissionError, "invalid identity envelope"):
            admit_reopen(admission_snapshot(target="sideways"))
        with self.assertRaisesRegex(AdmissionError, "validation_failed must be boolean"):
            admit_reopen(admission_snapshot(validation_failed="false"))
        with self.assertRaisesRegex(AdmissionError, "failed validation"):
            admit_reopen(admission_snapshot(validation_failed=True))
        with self.assertRaisesRegex(AdmissionError, "safe_mode_ready must be boolean"):
            admit_safe_mode(admission_snapshot(safe_mode_ready="yes"))
        with self.assertRaisesRegex(AdmissionError, "safe-mode record"):
            admit_safe_mode(admission_snapshot(safe_mode_ready=False))

    def test_replacement_rechecks_all_identity_fields(self) -> None:
        admitted = admission_snapshot()
        current = dict(admitted)
        current["operation_id"] = "op-other"
        current["barrier_identity_digest"] = canonical_barrier_digest(current)
        current["envelope_digest"] = canonical_envelope_digest(current)
        with self.assertRaisesRegex(AdmissionError, "stale operation_id"):
            recheck_before_replacement(admitted, current)

    def test_preflight_rejects_unknown_and_missing_predicates(self) -> None:
        with self.assertRaisesRegex(AdmissionError, "unknown fields"):
            admit_preflight(admission_snapshot(unexpected=True))
        with self.assertRaisesRegex(AdmissionError, "unmet predicates"):
            admit_preflight(admission_snapshot(release_authentic=False))


if __name__ == "__main__":
    unittest.main()
