# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Additional non-vendored coverage for AR-1954 root compatibility branches."""

import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from tools.execution_envelope import (
    canonical_digest,
    envelope_sandbox_mounts,
    envelope_scope_path,
    errors,
    preflight,
    sandbox_base_command,
    valid_binding,
    valid_reservation,
    validate_external_root,
)


class EnvelopeCompatibilityCoverageTests(unittest.TestCase):
    def test_roots_and_mounts(self) -> None:
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            product = root / "product"
            state = root / "state"
            source = root / "source"
            for path in (product, state / "tasks", source / "src"):
                path.mkdir(parents=True)
            self.assertEqual(state.resolve(), validate_external_root(state, "state"))
            mounts = envelope_sandbox_mounts(
                product,
                ["product-root", "state:tasks", "source-root"],
                ["state:tasks"],
                state_root=state,
                source_root=source,
            )
            self.assertEqual(
                ["product/.", "state/tasks", "source/.", "state/tasks"],
                [mount[0] for mount in mounts],
            )
            with self.assertRaisesRegex(RuntimeError, "unavailable root"):
                envelope_sandbox_mounts(product, ["source-root"], [], state_root=state)

    def test_invalid_roots_and_symlinks_fail_closed(self) -> None:
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            product = root / "product"
            product.mkdir()
            with self.assertRaisesRegex(RuntimeError, "root is unavailable"):
                validate_external_root(root / "missing", "state")
            outside = root / "outside"
            outside.mkdir()
            (product / "alias").symlink_to(outside, target_is_directory=True)
            with self.assertRaisesRegex(RuntimeError, "contains a symlink"):
                envelope_scope_path(product, "alias")

            regular = product / "file"
            regular.write_text("x")
            with self.assertRaisesRegex(RuntimeError, "not a real directory"):
                validate_external_root(regular, "state")
            with self.assertRaisesRegex(RuntimeError, "unsafe"):
                envelope_scope_path(product, "../outside")
            with self.assertRaisesRegex(RuntimeError, "unavailable"):
                envelope_scope_path(product, "missing/leaf")

    def test_validation_edges_and_runtime_command(self) -> None:
        self.assertEqual(["envelope must be an object"], errors(None))
        self.assertTrue(any("missing field" in item for item in errors({})))
        self.assertFalse(valid_binding({"execution_envelope_ref": "bad ref"}))
        self.assertTrue(valid_binding({}))
        self.assertFalse(valid_reservation(None))
        reservation = {
            "execution_id": "a" * 32,
            "owner": "worker",
            "task_revision": 1,
            "envelope_digest": "sha256:" + "a" * 64,
            "command_class": "read",
            "scope_digest": "sha256:" + "b" * 64,
            "argv_digest": "c" * 64,
            "expires_at": "2026-10-15T05:00:00+00:00",
        }
        self.assertTrue(valid_reservation(reservation))
        reservation["expires_at"] = "not-a-date"
        self.assertFalse(valid_reservation(reservation))
        isolated = sandbox_base_command()
        connected = sandbox_base_command(network=True)
        self.assertIn("--unshare-net", isolated)
        self.assertNotIn("--unshare-net", connected)

    def test_metadata_mount_and_root_selector(self) -> None:
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / ".git").mkdir()
            state = root / "state"
            state.mkdir()
            mounts = envelope_sandbox_mounts(
                root,
                ["product-root"],
                ["state-root"],
                git_metadata=True,
                state_root=state,
            )
            self.assertEqual(
                ["product/.", "product/.git", "state/."],
                [mount[0] for mount in mounts],
            )

    def test_preflight_fail_closed_and_root_qualified_success(self) -> None:
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            state = root / "state"
            (root / "tools").mkdir(parents=True)
            state.mkdir()
            envelope = {
                "schema_version": 2,
                "envelope_id": "AR-1954-e1",
                "envelope_revision": 1,
                "task": "AR-1954",
                "task_revision": 1,
                "spec_ref": "specs/AR-1954.json",
                "spec_revision": 1,
                "outputs": [{"id": "result", "description": "result"}],
                "non_goals": ["unrelated changes"],
                "command_classes": {"read": {"allowed": True}},
                "path_scope": {"read": ["product-root", "state-root"], "write": ["tools"]},
                "capabilities": {"git_metadata": {"allowed": False}, "network": {"allowed": False}},
                "evidence": [{"id": "test", "class": "unit-test", "required": True}],
                "stop_conditions": [{"id": "stop", "kind": "pause"}],
            }
            meta = {
                "owner": "worker",
                "status": "in_progress",
                "id": "AR-1954",
                "spec_ref": "specs/AR-1954.json",
                "spec_revision": 1,
                "task_revision": 1,
                "claim_expires": "2999-01-01T00:00:00+00:00",
                "execution_envelope_ref": "envelopes/AR-1954-e1.json",
                "execution_envelope_revision": 1,
                "execution_envelope_task_revision": 1,
                "execution_envelope": envelope,
                "execution_envelope_digest": canonical_digest(envelope),
            }
            denied = preflight(meta, "other", "read", ["tools"], root)
            self.assertEqual("OWNER_CLAIM_REQUIRED", denied.code)
            denied = preflight(meta, "worker", "source-write", [], root)
            self.assertEqual("COMMAND_CLASS_DENIED", denied.code)
            allowed = preflight(meta, "worker", "read", ["state-root"], root, state_root=state)
            self.assertTrue(allowed.allowed)
            outside = preflight(meta, "worker", "read", ["missing"], root, state_root=state)
            self.assertEqual("PATH_SCOPE_UNAVAILABLE", outside.code)


if __name__ == "__main__":
    unittest.main()
