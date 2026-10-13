# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Downstream validation and ownership coverage for mutation-fence seams."""

from __future__ import annotations

import os
import sqlite3
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools import mutation_fence
from tools.mutation_fence import (
    MutationFence,
    MutationFenceError,
    provision,
    provision_control_binding,
)
from tools.upgrade_identity import BarrierSessionIdentity


class MutationFenceValidationEdgeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.root.chmod(0o700)
        self.authority = self.root / "authority.sqlite3"
        self.authority.write_bytes(b"authority")
        self.authority.chmod(0o600)
        self.marker = self.root / "marker.json"
        self.lifecycle = self.root / "lifecycle.json"
        self.authority_lock = self.root / "authority.lock"
        self.project_id = "project-fence-edges"

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def _fence(self) -> MutationFence:
        provision(
            self.authority,
            self.marker,
            self.lifecycle,
            self.authority_lock,
            self.project_id,
        )
        return MutationFence(self.authority, self.marker, self.lifecycle, self.authority_lock)

    def test_file_lock_rejects_non_float_and_times_out_or_retries(self) -> None:
        for timeout in (0.0, -0.1, 1, True):
            with (
                self.subTest(timeout=timeout),
                self.assertRaisesRegex(MutationFenceError, "timeout"),
            ):
                mutation_fence._acquire_file_lock(7, "test.lock", timeout)  # type: ignore[arg-type]

        with (
            patch.object(mutation_fence.time, "monotonic", side_effect=(1.0, 1.2)),
            patch.object(mutation_fence.fcntl, "flock", side_effect=BlockingIOError()),
            self.assertRaisesRegex(
                MutationFenceError, "test.lock acquisition timed out after 0.1s"
            ),
        ):
            mutation_fence._acquire_file_lock(7, "test.lock", 0.1)

        with (
            patch.object(mutation_fence.time, "monotonic", side_effect=(1.0, 1.0)),
            patch.object(
                mutation_fence.fcntl, "flock", side_effect=(BlockingIOError(), None)
            ) as flock,
            patch.object(mutation_fence.time, "sleep") as sleep,
        ):
            mutation_fence._acquire_file_lock(7, "test.lock", 0.1)
        self.assertEqual(2, flock.call_count)
        sleep.assert_called_once_with(mutation_fence.LOCK_POLL_SECONDS)

    def test_binding_provisioning_rejects_bad_identifier_and_reuses_complete_lifecycle(
        self,
    ) -> None:
        control = self.root / "control.sqlite3"
        control.write_bytes(b"control")
        control.chmod(0o600)
        with self.assertRaisesRegex(MutationFenceError, "canonical"):
            provision_control_binding(
                control, self.root / "binding.json", self.root / "control.lock", "bad/project"
            )

        provision(
            self.authority,
            self.marker,
            self.lifecycle,
            self.authority_lock,
            self.project_id,
        )
        self.marker.unlink()
        record = provision(
            self.authority,
            self.marker,
            self.lifecycle,
            self.authority_lock,
            self.project_id,
        )
        self.assertEqual(self.project_id, record["project_id"])
        self.assertTrue(self.marker.exists())

    def test_session_identity_and_control_prerequisite_fail_closed(self) -> None:
        fence = self._fence()
        fence.verify_binding()
        with self.assertRaisesRegex(MutationFenceError, "identity is required"):
            fence.bind_session_identity(object())

        identity = BarrierSessionIdentity(
            1,
            self.project_id,
            "attempt-1",
            1,
            "authority-1",
            "barrier-1",
            "token-1",
            "owner-1",
            "a" * 64,
        )
        fence.bind_session_identity(identity)
        fence.bind_session_identity(identity)
        with self.assertRaisesRegex(MutationFenceError, "already bound"):
            fence.bind_session_identity(
                BarrierSessionIdentity(
                    1,
                    self.project_id,
                    "attempt-2",
                    1,
                    "authority-1",
                    "barrier-1",
                    "token-1",
                    "owner-1",
                    "b" * 64,
                )
            )
        with self.assertRaisesRegex(MutationFenceError, "prerequisites"), fence.control_locked():
            pass

    def test_control_binding_digest_project_and_owned_object_changes_fail_closed(self) -> None:
        control = self.root / "control.sqlite3"
        control.write_bytes(b"control")
        control.chmod(0o600)
        control_lock = self.root / "control.lock"
        binding = self.root / "control-binding.json"
        provision_control_binding(control, binding, control_lock, self.project_id)
        provision(
            self.authority,
            self.marker,
            self.lifecycle,
            self.authority_lock,
            self.project_id,
        )
        fence = MutationFence(
            self.authority,
            self.marker,
            self.lifecycle,
            self.authority_lock,
            control,
            binding,
            control_lock,
        )

        original = binding.read_text()
        tampered = original
        binding.write_text(tampered.replace("sha256:", "sha257:", 1))
        binding.chmod(0o600)
        with self.assertRaisesRegex(MutationFenceError, "control binding digest"):
            fence.verify_binding()

        binding.write_text(original)
        binding.chmod(0o600)
        changed = control_lock.with_name("replacement-control.lock")
        changed.write_bytes(b"")
        changed.chmod(0o600)
        control_lock.unlink()
        changed.rename(control_lock)
        with self.assertRaisesRegex(MutationFenceError, "control.lock identity changed"):
            fence.verify_binding()

    def test_control_locked_releases_descriptor_when_post_lock_verify_fails(self) -> None:
        control = self.root / "control.sqlite3"
        sqlite3.connect(control).close()
        control.chmod(0o600)
        control_lock = self.root / "control.lock"
        binding = self.root / "control-binding.json"
        provision_control_binding(control, binding, control_lock, self.project_id)
        provision(
            self.authority,
            self.marker,
            self.lifecycle,
            self.authority_lock,
            self.project_id,
        )
        fence = MutationFence(
            self.authority,
            self.marker,
            self.lifecycle,
            self.authority_lock,
            control,
            binding,
            control_lock,
        )
        with (
            patch.object(fence, "_verify", side_effect=(None, MutationFenceError("reread"))),
            self.assertRaisesRegex(MutationFenceError, "reread"),
            fence.control_locked(),
        ):
            pass
        descriptor = os.open(control_lock, os.O_RDWR | os.O_NOFOLLOW)
        try:
            mutation_fence._acquire_file_lock(descriptor, "control.lock", 0.1)
        finally:
            os.close(descriptor)


if __name__ == "__main__":
    unittest.main()
