# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Additional admission and descriptor-boundary coverage for execution envelopes."""

from __future__ import annotations

import argparse
import os
import stat
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import cast
from unittest.mock import patch

from tools import execution_envelope


class ExecutionEnvelopeAdmissionCoverageTests(unittest.TestCase):
    def test_capability_matrix_and_publication_metadata_are_fail_closed(self) -> None:
        base = {"capabilities": {"git_metadata": {"allowed": True}, "network": {"allowed": True}}}
        self.assertIsNone(execution_envelope._capability_denial(base, "read", False))
        denied = cast(
            execution_envelope.Preflight,
            execution_envelope._capability_denial({}, "git-publication", False),
        )
        self.assertEqual("GIT_METADATA_CAPABILITY_DENIED", denied.code)
        denied = cast(
            execution_envelope.Preflight,
            execution_envelope._capability_denial(base, "read", True),
        )
        self.assertEqual("EXTERNAL_SIDE_EFFECTS_DENIED", denied.code)
        denied = cast(
            execution_envelope.Preflight,
            execution_envelope._capability_denial(
                {
                    "capabilities": {
                        "git_metadata": {"allowed": True},
                        "network": {"allowed": False},
                    }
                },
                "git-publication",
                True,
            ),
        )
        self.assertEqual("NETWORK_CAPABILITY_DENIED", denied.code)
        denied = cast(
            execution_envelope.Preflight,
            execution_envelope._capability_denial(
                {"capabilities": {"git_metadata": {"allowed": True}, "network": {"allowed": True}}},
                "git-publication",
                False,
            ),
        )
        self.assertEqual("EXTERNAL_SIDE_EFFECT_AUTHORIZATION_REQUIRED", denied.code)
        self.assertTrue(execution_envelope.publication_metadata_allowed(base))
        self.assertFalse(execution_envelope.publication_metadata_allowed({}))

    def test_valid_reservation_rejects_each_malformed_field(self) -> None:
        valid = {
            "execution_id": "a" * 32,
            "owner": "worker",
            "task_revision": 3,
            "envelope_digest": "sha256:" + "a" * 64,
            "command_class": "read",
            "scope_digest": "sha256:" + "b" * 64,
            "argv_digest": "c" * 64,
            "expires_at": "2099-01-01T00:00:00+00:00",
        }
        self.assertTrue(execution_envelope.valid_reservation(valid))
        for key, value in (
            ("execution_id", "bad"),
            ("owner", ""),
            ("task_revision", 0),
            ("envelope_digest", "bad"),
            ("command_class", "unknown"),
            ("scope_digest", "bad"),
            ("argv_digest", "bad"),
            ("expires_at", "invalid"),
        ):
            candidate = dict(valid)
            candidate[key] = value
            with self.subTest(key=key):
                self.assertFalse(execution_envelope.valid_reservation(candidate))

    def test_scope_openers_reject_aliases_and_accept_real_files(self) -> None:
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "src").mkdir()
            (root / "src" / "module.py").write_text("pass\n", encoding="utf-8")
            with self.assertRaisesRegex(RuntimeError, "unsafe"):
                execution_envelope.envelope_scope_path(root, "../outside")
            resolved = execution_envelope.envelope_scope_path(root, "src/module.py")
            self.assertEqual(root / "src/module.py", resolved)
            fd = execution_envelope._open_scope_path(root, "src/module.py")
            try:
                self.assertTrue(stat.S_ISREG(os.fstat(fd).st_mode))
            finally:
                os.close(fd)
            root_fd = execution_envelope._open_path(root, directory=True)
            try:
                nested_fd = execution_envelope._open_scope_fd(root_fd, "src/module.py")
                os.close(nested_fd)
            finally:
                os.close(root_fd)

    def test_sandbox_command_preserves_fallback_and_builds_descriptor_spec(self) -> None:
        fallback = argparse.Namespace(command=["true"])
        self.assertEqual(["true"], execution_envelope.sandboxed_envelope_command(fallback))
        args = argparse.Namespace(
            command=["true"],
            _envelope_worktree=str(Path.cwd()),
            _envelope_read_scope=["src"],
            _envelope_write_scope=["out"],
            _envelope_worktree_fd=71,
            _envelope_git_metadata=True,
            _envelope_network=False,
        )
        with (
            patch.object(execution_envelope.shutil, "which", return_value=None),  # type: ignore[attr-defined]
            self.assertRaisesRegex(RuntimeError, "bubblewrap"),
        ):
            execution_envelope.sandboxed_envelope_command(args)
        with (
            patch.object(execution_envelope.shutil, "which", return_value="/usr/bin/bwrap"),  # type: ignore[attr-defined]
            patch.object(execution_envelope, "sandbox_base_command", return_value=["bwrap"]),
        ):
            command = execution_envelope.sandboxed_envelope_command(args)
        self.assertIn("--", command)
        self.assertEqual("true", command[-1])


if __name__ == "__main__":
    unittest.main()
