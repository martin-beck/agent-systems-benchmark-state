# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Hostile tests for commit prerequisite authorization evidence."""

from __future__ import annotations

import unittest
from dataclasses import replace

from tools.authority_neutral_commit import (
    BoundCommitAuthorizationAdapter,
    CommitAdmissionBundle,
    CommitAuthorizationExecutionError,
    execute_verified_commit_authorization,
)

OPERATION = {"operation_id": "op-1:commit", "opcode": "authority.commit.admit"}
EVIDENCE = {
    "backend": "sqlite",
    "target": "new",
    "operation_id": "op-1",
    "fencing_token": "fence-1",
    "state_revision": 7,
    "barrier_id": "barrier-1",
    "backup_verified": True,
    "restore_roundtrip_verified": True,
    "staged_verified": True,
    "manifest_verified": True,
    "selector_admission_verified": True,
    "runtime_replacement_admission_verified": True,
    "backend_identity_verified": True,
    "mutates_authority": False,
    "artifact_identity": "artifact-1",
    "manifest_identity": "manifest-1",
    "selector_identity": "selector-1",
    "runtime_identity": "runtime-1",
}


class CommitAuthorizationTests(unittest.TestCase):
    def test_admission_bundle_binds_all_mutation_identities(self) -> None:
        bundle = CommitAdmissionBundle.from_evidence(EVIDENCE)
        self.assertTrue(bundle.matches(EVIDENCE))
        self.assertFalse(bundle.matches({**EVIDENCE, "runtime_identity": "foreign"}))
        with self.assertRaisesRegex(CommitAuthorizationExecutionError, "artifact_identity"):
            CommitAdmissionBundle.from_evidence({**EVIDENCE, "artifact_identity": ""})
        with self.assertRaisesRegex(CommitAuthorizationExecutionError, "artifact_identity"):
            replace(bundle, artifact_identity="")
        with self.assertRaisesRegex(CommitAuthorizationExecutionError, "identity"):
            replace(bundle, backend="rollback")

    def test_admission_rejects_unhashable_backend_and_target_values(self) -> None:
        for field in ("backend", "target"):
            with (
                self.subTest(field=field),
                self.assertRaisesRegex(CommitAuthorizationExecutionError, "identity is invalid"),
            ):
                CommitAdmissionBundle.from_evidence({**EVIDENCE, field: []})

    def test_admission_matches_non_mapping_as_false(self) -> None:
        bundle = CommitAdmissionBundle.from_evidence(EVIDENCE)
        self.assertFalse(bundle.matches([]))

    def test_prerequisites_are_verified_without_authorizing_commit(self) -> None:
        result = execute_verified_commit_authorization(OPERATION, EVIDENCE)
        self.assertTrue(result["commit_prerequisites_verified"])
        self.assertFalse(result["commit_authorized"])
        self.assertFalse(result["mutates_authority"])

    def test_rejects_forged_or_unverified_prerequisites(self) -> None:
        with self.assertRaisesRegex(CommitAuthorizationExecutionError, "unsupported"):
            execute_verified_commit_authorization({"opcode": "authority.atomic_replace"}, EVIDENCE)
        with self.assertRaisesRegex(CommitAuthorizationExecutionError, "identity"):
            execute_verified_commit_authorization(OPERATION, {**EVIDENCE, "target": "rollback"})
        for field, value, message in (
            ("backup_verified", False, "unverified"),
            ("selector_admission_verified", False, "unverified"),
            ("mutates_authority", True, "mutating"),
            ("state_revision", 0, "revision"),
            ("barrier_id", "", "barrier_id"),
        ):
            with (
                self.subTest(field=field),
                self.assertRaisesRegex(CommitAuthorizationExecutionError, message),
            ):
                execute_verified_commit_authorization(OPERATION, {**EVIDENCE, field: value})
        missing = dict(EVIDENCE)
        missing.pop("runtime_replacement_admission_verified")
        with self.assertRaisesRegex(CommitAuthorizationExecutionError, "incomplete"):
            execute_verified_commit_authorization(OPERATION, missing)

    def test_bound_adapter_rejects_phase_and_identity_drift(self) -> None:
        with self.assertRaisesRegex(CommitAuthorizationExecutionError, "unsupported"):
            BoundCommitAuthorizationAdapter({"opcode": "authority.atomic_replace"}, EVIDENCE)
        adapter = BoundCommitAuthorizationAdapter(OPERATION, EVIDENCE)
        result = adapter.execute("commit_admission", EVIDENCE)
        self.assertTrue(result["commit_prerequisites_verified"])
        with self.assertRaisesRegex(CommitAuthorizationExecutionError, "unsupported"):
            adapter.execute("commit", EVIDENCE)
        with self.assertRaisesRegex(CommitAuthorizationExecutionError, "identity mismatch"):
            adapter.execute("commit_admission", {**EVIDENCE, "fencing_token": "foreign"})


if __name__ == "__main__":
    unittest.main()
