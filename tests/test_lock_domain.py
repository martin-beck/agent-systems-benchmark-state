# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Hostile tests for the uncalled lock-domain identity contract."""

from __future__ import annotations

import json
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path
from typing import cast

from tools.admission_lease import AdmissionLease
from tools.handoffctl import CoordinatorLockGuard, locked
from tools.lock_domain import LockDomainContract, LockDomainError, _identity
from tools.mutation_fence import MutationFence, provision, provision_control_binding
from tools.rollback_control_store import (
    BarrierSessionState,
    SQLiteBarrierSessionStore,
    SQLiteRollbackControlStore,
)
from tools.upgrade_identity import BarrierSessionIdentity, canonical_barrier_session_digest

PROJECT = "11111111-1111-4111-8111-111111111111"


def session_identity() -> BarrierSessionIdentity:
    record: dict[str, object] = {
        "schema_version": 1,
        "project_id": PROJECT,
        "attempt_id": "attempt-1",
        "state_revision": 3,
        "authority_revision_at_acquire": "authority-1",
        "durable_barrier_id": "barrier-1",
        "fencing_token": "fence-1",
        "fencing_owner": "owner-1",
        "identity_digest": "0" * 64,
    }
    record["identity_digest"] = canonical_barrier_session_digest(record)
    return BarrierSessionIdentity.from_record(record)


class LockDomainTests(unittest.TestCase):
    def setUp(self) -> None:
        self.directory = tempfile.TemporaryDirectory()
        self.root = Path(self.directory.name)
        self.root.chmod(0o700)
        self.authority = self.root / "authority.sqlite"
        self.authority.write_bytes(b"authority")
        self.authority.chmod(0o600)
        self.control = self.root / "control.sqlite"
        self.store = SQLiteRollbackControlStore(self.control, PROJECT, self.authority)
        self.marker = self.root / "authority-marker.json"
        self.lifecycle = self.root / "authority-lifecycle.json"
        self.authority_lock = self.root / "authority.lock"
        self.control_binding = self.root / "control-binding.json"
        provision(self.authority, self.marker, self.lifecycle, self.authority_lock, PROJECT)
        provision_control_binding(
            self.control,
            self.control_binding,
            self.store.control_lock_path,
            PROJECT,
        )
        self.fence = MutationFence(
            self.authority,
            self.marker,
            self.lifecycle,
            self.authority_lock,
            self.control,
            self.control_binding,
            self.store.control_lock_path,
        )
        self.session = SQLiteBarrierSessionStore(self.store, lambda: "authority-1")

    def tearDown(self) -> None:
        self.directory.cleanup()

    def test_capture_and_revalidation_are_read_only_and_stable(self) -> None:
        with locked() as guard:
            captured = LockDomainContract.capture(guard, self.session, self.fence)
            captured.assert_current(guard, self.session, self.fence)
            self.assertEqual(captured, LockDomainContract.capture(guard, self.session, self.fence))
            captured.assert_descriptor_binding(captured)
            with self.assertRaisesRegex(LockDomainError, "identity is required"):
                captured.assert_descriptor_binding(None)

    def test_split_control_lock_is_rejected_before_opening_it(self) -> None:
        split = MutationFence(
            self.authority,
            self.marker,
            self.lifecycle,
            self.authority_lock,
            self.control,
            self.control_binding,
            self.root / "different-control.lock",
        )
        with locked() as guard, self.assertRaisesRegex(LockDomainError, "control-lock"):
            LockDomainContract.capture(guard, self.session, split)

    def test_mismatched_authority_and_duplicate_path_are_rejected(self) -> None:
        other = self.root / "other-authority.sqlite"
        other.write_bytes(b"other")
        other.chmod(0o600)
        mismatched = MutationFence(
            other,
            self.marker,
            self.lifecycle,
            self.authority_lock,
            self.control,
            self.control_binding,
            self.store.control_lock_path,
        )
        with locked() as guard, self.assertRaisesRegex(LockDomainError, "authority path"):
            LockDomainContract.capture(guard, self.session, mismatched)

        duplicate = MutationFence(
            self.control,
            self.marker,
            self.lifecycle,
            self.control,
            self.control,
            self.control_binding,
            self.store.control_lock_path,
        )
        with locked() as guard, self.assertRaisesRegex(LockDomainError, "duplicated"):
            LockDomainContract.capture(guard, self.session, duplicate)

    def test_replaced_descriptor_and_inactive_guard_fail_closed(self) -> None:
        with locked() as guard:
            captured = LockDomainContract.capture(guard, self.session, self.fence)
        with self.assertRaisesRegex(LockDomainError, "guard"):
            LockDomainContract.capture(cast(CoordinatorLockGuard, None), self.session, self.fence)

        replacement = self.root / "replacement.lock"
        replacement.write_bytes(b"")
        replacement.chmod(0o600)
        self.store.control_lock_path.unlink()
        replacement.replace(self.store.control_lock_path)
        with locked() as guard, self.assertRaisesRegex(LockDomainError, "binding|identity"):
            captured.assert_current(guard, self.session, self.fence)

    def test_invalid_binding_json_is_rejected_and_no_state_is_written(self) -> None:
        before = self.marker.read_bytes()
        value = json.loads(before)
        value["project_id"] = "other"
        self.marker.write_text(json.dumps(value) + "\n")
        with locked() as guard, self.assertRaisesRegex(LockDomainError, "binding"):
            LockDomainContract.capture(guard, self.session, self.fence)
        self.assertNotEqual(before, self.marker.read_bytes())

    def test_identity_rejects_noncanonical_unsafe_and_unavailable_descriptors(self) -> None:
        with self.assertRaisesRegex(LockDomainError, "not canonical"):
            _identity(Path("relative-lock"))

        unsafe_parent = self.root / "unsafe-parent"
        unsafe_parent.mkdir()
        unsafe_parent.chmod(0o755)
        unsafe_file = unsafe_parent / "lock"
        unsafe_file.write_bytes(b"")
        unsafe_file.chmod(0o600)
        with self.assertRaisesRegex(LockDomainError, "parent is not owner-only"):
            _identity(unsafe_file)
        unsafe_parent.chmod(0o700)

        unsafe_file.chmod(0o644)
        with self.assertRaisesRegex(LockDomainError, "descriptor is unsafe"):
            _identity(unsafe_file)
        with self.assertRaisesRegex(LockDomainError, "unavailable"):
            _identity(self.root / "missing-lock")

    def test_identity_rejects_nonregular_descriptor_and_symlink(self) -> None:
        directory = self.root / "directory-lock"
        directory.mkdir()
        with self.assertRaisesRegex(LockDomainError, "descriptor is unsafe"):
            _identity(directory)

        target = self.root / "target-lock"
        target.write_bytes(b"")
        target.chmod(0o600)
        link = self.root / "link-lock"
        link.symlink_to(target)
        with self.assertRaisesRegex(LockDomainError, "canonical|unavailable"):
            _identity(link)

    def test_capture_rejects_missing_types_and_unowned_guard(self) -> None:
        with locked() as guard:
            with self.assertRaisesRegex(LockDomainError, "common lock"):
                LockDomainContract.capture(
                    cast(CoordinatorLockGuard, None), self.session, self.fence
                )
            with self.assertRaisesRegex(LockDomainError, "session store"):
                LockDomainContract.capture(guard, cast(SQLiteBarrierSessionStore, None), self.fence)
            with self.assertRaisesRegex(LockDomainError, "authority fence"):
                LockDomainContract.capture(guard, self.session, cast(MutationFence, None))
            saved_guard = guard
        with self.assertRaisesRegex(LockDomainError, "ownership"):
            LockDomainContract.capture(saved_guard, self.session, self.fence)

    def test_capture_rejects_incomplete_and_noncanonical_bindings(self) -> None:
        incomplete = MutationFence(self.authority, self.marker, self.lifecycle, self.authority_lock)
        with locked() as guard, self.assertRaisesRegex(LockDomainError, "incomplete"):
            LockDomainContract.capture(guard, self.session, incomplete)

        symlink = self.root / "control-link.sqlite"
        symlink.symlink_to(self.control)
        self.store.path = symlink
        with locked() as guard, self.assertRaisesRegex(LockDomainError, "canonical"):
            LockDomainContract.capture(guard, self.session, self.fence)

        split_store = self.root / "split-control.sqlite"
        split_store.write_bytes(b"split")
        split_store.chmod(0o600)
        self.store.path = split_store
        with locked() as guard, self.assertRaisesRegex(LockDomainError, "control-store"):
            LockDomainContract.capture(guard, self.session, self.fence)

    def test_assert_current_rejects_changed_identity(self) -> None:
        with locked() as guard:
            captured = LockDomainContract.capture(guard, self.session, self.fence)
            altered = replace(captured, authority=self.root / "other.sqlite")
            with self.assertRaisesRegex(LockDomainError, "identity changed"):
                altered.assert_current(guard, self.session, self.fence)

    def test_session_binding_matches_durable_identity_and_lease(self) -> None:
        with locked() as guard:
            captured = LockDomainContract.capture(guard, self.session, self.fence)
        identity = session_identity()
        lease = AdmissionLease(PROJECT, "authority-1", "fence-1", "owner-1", "barrier-1", 3)
        captured.assert_session_binding(BarrierSessionState(identity, "held", 3), lease)
        with self.assertRaisesRegex(LockDomainError, "revision"):
            captured.assert_session_binding(BarrierSessionState(identity, "held", 2), lease)

        for changed in (
            replace(lease, fencing_token="other"),  # noqa: S106
            replace(lease, revision=4),
        ):
            with self.subTest(changed=changed), self.assertRaisesRegex(LockDomainError, "match"):
                captured.assert_session_binding(BarrierSessionState(identity, "held", 3), changed)

        with self.assertRaisesRegex(LockDomainError, "not held"):
            captured.assert_session_binding(BarrierSessionState(identity, "released", 3), lease)
        with self.assertRaisesRegex(LockDomainError, "admissible status"):
            captured.assert_session_binding(
                BarrierSessionState(identity, "released", 3),
                lease,
                allowed_statuses=("releasing",),
            )
        with self.assertRaisesRegex(LockDomainError, "identity is required"):
            captured.assert_session_binding(
                BarrierSessionState(cast(BarrierSessionIdentity, object()), "held", 3),
                lease,
            )
        tampered = replace(identity, identity_digest="tampered")
        with self.assertRaisesRegex(LockDomainError, "identity is invalid"):
            captured.assert_session_binding(BarrierSessionState(tampered, "held", 3), lease)
        revision_drift = replace(identity, state_revision=4)
        revision_drift = replace(
            revision_drift,
            identity_digest=canonical_barrier_session_digest(revision_drift.as_record()),
        )
        with self.assertRaisesRegex(LockDomainError, "identity revision"):
            captured.assert_session_binding(BarrierSessionState(revision_drift, "held", 3), lease)


if __name__ == "__main__":
    unittest.main()
