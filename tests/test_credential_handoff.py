# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Offline tests for the bounded credential descriptor handoff."""

from __future__ import annotations

import argparse
import subprocess
import unittest
from unittest.mock import MagicMock, patch

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

        args = argparse.Namespace(_envelope_worktree_fd=-1, credential_fd=93)
        with self.assertRaisesRegex(RuntimeError, "worktree descriptor"):
            credential_handoff.run_envelope_subprocess(["true"], 1.0, args)

    def test_runs_without_a_worktree_descriptor_when_credential_is_admitted(self) -> None:
        args = argparse.Namespace(credential_fd=93)
        completed: subprocess.CompletedProcess[bytes] = subprocess.CompletedProcess(["gh"], 0)
        with patch.object(credential_handoff.subprocess, "run", return_value=completed):  # type: ignore[attr-defined]
            self.assertIs(
                completed,
                credential_handoff.run_envelope_subprocess(["gh", "status"], 2.0, args),
            )

    def test_handoffctl_delegates_admitted_credential_runs(self) -> None:
        args = argparse.Namespace(credential_fd=93)
        completed: subprocess.CompletedProcess[bytes] = subprocess.CompletedProcess(["gh"], 0)
        with patch.object(
            handoffctl._credential_handoff_runtime,  # type: ignore[attr-defined]
            "run_envelope_subprocess",
            return_value=completed,
        ) as launch:
            self.assertIs(
                completed,
                handoffctl._run_envelope_subprocess(["gh", "status"], 2.0, args),
            )
        launch.assert_called_once_with(["gh", "status"], 2.0, args)

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

    def test_handoffctl_accepts_authorized_publication_descriptor(self) -> None:
        handoffctl._validate_credential_fd(
            argparse.Namespace(
                credential_fd=93,
                command_class="git-publication",
                authorize_external_side_effects=True,
            )
        )

    def test_cmd_run_fenced_rejects_invalid_descriptor_before_launch(self) -> None:
        args = argparse.Namespace(
            task="AR-1936",
            owner="worker",
            command=["true"],
            command_class="git-publication",
            authorize_external_side_effects=True,
            credential_fd=2,
        )
        with (
            patch.object(handoffctl, "backend_selection", return_value={"backend": "git"}),
            patch.object(handoffctl, "config", return_value={}),
            patch.object(handoffctl, "require_active_owner", return_value=MagicMock()),
            patch.object(handoffctl, "_run_envelope_subprocess") as launch,
            self.assertRaisesRegex(RuntimeError, "open fd >= 3"),
        ):
            handoffctl._cmd_run_fenced(args)
        launch.assert_not_called()

    def test_cmd_run_fenced_admits_authorized_descriptor_to_launch(self) -> None:
        args = argparse.Namespace(
            task="AR-1936",
            owner="worker",
            command=["true"],
            command_class="git-publication",
            authorize_external_side_effects=True,
            credential_fd=93,
            _envelope_worktree="bound",
            _envelope_worktree_fd=71,
            scope_path=[],
            retry_window=3,
        )
        with (
            patch.object(handoffctl, "backend_selection", return_value={"backend": "git"}),
            patch.object(handoffctl, "config", return_value={}),
            patch.object(handoffctl, "require_active_owner", return_value=MagicMock()),
            patch.object(handoffctl, "run_envelope_timeout", return_value=None),
            patch.object(handoffctl, "require_policy_unchanged"),
            patch.object(handoffctl.al, "prepare"),  # type: ignore[attr-defined]
            patch.object(handoffctl, "sandboxed_envelope_command", return_value=["true"]),
            patch.object(handoffctl, "locate", return_value=(None, {"task_revision": 4}, None)),
            patch.object(handoffctl, "mutate"),
            patch.object(handoffctl, "task_execution_locked", return_value=MagicMock()),
            patch.object(
                handoffctl,
                "_run_envelope_subprocess",
                side_effect=RuntimeError("launch boundary"),
            ) as launch,
            self.assertRaisesRegex(RuntimeError, "launch boundary"),
        ):
            handoffctl._cmd_run_fenced(args)
        launch.assert_called_once()
        self.assertEqual(93, launch.call_args.args[2].credential_fd)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
