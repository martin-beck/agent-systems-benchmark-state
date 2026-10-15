# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Offline tests for the bounded credential descriptor handoff."""

from __future__ import annotations

import argparse
import subprocess
import unittest
from unittest.mock import patch

from tools import credential_handoff, handoffctl


class CredentialHandoffTests(unittest.TestCase):
    def test_passes_only_worktree_and_credential_descriptors(self) -> None:
        args = argparse.Namespace(
            _envelope_worktree="bound-worktree",
            _envelope_worktree_fd=71,
            credential_fd=93,
        )
        completed: subprocess.CompletedProcess[bytes] = subprocess.CompletedProcess(["gh"], 0)
        with patch.object(credential_handoff.subprocess, "run", return_value=completed) as run:  # type: ignore[attr-defined]
            self.assertIs(
                completed,
                credential_handoff.run_envelope_subprocess(["gh", "pr", "merge"], 15.0, args),
            )
        run.assert_called_once_with(
            ["gh", "pr", "merge"],
            check=False,
            stdin=subprocess.DEVNULL,
            timeout=15.0,
            pass_fds=(71, 93),
            cwd="bound-worktree",
        )

    def test_rejects_invalid_credential_descriptor(self) -> None:
        args = argparse.Namespace(credential_fd=2)
        with self.assertRaisesRegex(RuntimeError, "open fd >= 3"):
            credential_handoff.run_envelope_subprocess(["true"], 1.0, args)

    def test_rejects_missing_credential_descriptor(self) -> None:
        with self.assertRaisesRegex(RuntimeError, "credential descriptor is required"):
            credential_handoff.run_envelope_subprocess(["true"], 1.0, argparse.Namespace())

    def test_handoffctl_rejects_credential_fd_without_publication_authority(self) -> None:
        args = argparse.Namespace(
            credential_fd=93,
            command_class="read",
            authorize_external_side_effects=True,
        )
        with self.assertRaisesRegex(RuntimeError, "git-publication"):
            handoffctl._validate_credential_fd(args)

        args.command_class = "git-publication"
        args.authorize_external_side_effects = False
        with self.assertRaisesRegex(RuntimeError, "authorized external side effects"):
            handoffctl._validate_credential_fd(args)

    def test_handoffctl_rejects_missing_credential_helper(self) -> None:
        args = argparse.Namespace(
            credential_fd=93,
            _envelope_worktree_fd=71,
            _envelope_worktree="bound-worktree",
        )
        with (
            patch.object(handoffctl, "_credential_handoff_runtime", None),
            self.assertRaisesRegex(RuntimeError, "credential helper unavailable"),
        ):
            handoffctl._run_envelope_subprocess(["gh", "pr", "merge"], 15.0, args)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
