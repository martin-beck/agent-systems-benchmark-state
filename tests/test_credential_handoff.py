# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Offline tests for the bounded credential descriptor handoff."""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
import unittest
from unittest.mock import MagicMock, patch

from tools import credential_handoff, handoffctl


class CredentialHandoffTests(unittest.TestCase):
    def test_handoffctl_runs_real_credential_descriptor_path(self) -> None:
        read_fd, write_fd = os.pipe()
        try:
            os.write(write_fd, b"x")
            os.close(write_fd)
            args = argparse.Namespace(credential_fd=read_fd)
            command = [
                sys.executable,
                "-c",
                "import os,sys; raise SystemExit(os.read(int(sys.argv[1]), 1) != b'x')",
                str(read_fd),
            ]
            completed = handoffctl._run_envelope_subprocess(command, 5.0, args)
            self.assertEqual(0, completed.returncode)
        finally:
            os.close(read_fd)

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

    def test_handoffctl_fallback_preserves_bound_worktree_cwd_without_credentials(self) -> None:
        args = argparse.Namespace(_envelope_worktree_fd=71, _envelope_worktree="bound")
        completed: subprocess.CompletedProcess[bytes] = subprocess.CompletedProcess(["true"], 0)
        with patch.object(handoffctl.subprocess, "run", return_value=completed) as run:  # type: ignore[attr-defined]
            self.assertIs(completed, handoffctl._run_envelope_subprocess(["true"], 2.0, args))
        run.assert_called_once_with(
            ["true"],
            cwd="bound",
            check=False,
            stdin=subprocess.DEVNULL,
            timeout=2.0,
            pass_fds=(71,),
        )

    def test_handoffctl_fallback_without_worktree_descriptor(self) -> None:
        args = argparse.Namespace()
        completed: subprocess.CompletedProcess[bytes] = subprocess.CompletedProcess(["true"], 0)
        with patch.object(handoffctl.subprocess, "run", return_value=completed) as run:  # type: ignore[attr-defined]
            self.assertIs(completed, handoffctl._run_envelope_subprocess(["true"], 2.0, args))
        run.assert_called_once_with(["true"], check=False, stdin=subprocess.DEVNULL, timeout=2.0)

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
            timeout_seconds=10.0,
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

    def test_cmd_run_fenced_records_bound_execution_reservation(self) -> None:
        args = argparse.Namespace(
            task="AR-1936",
            owner="worker",
            command=["gh", "status"],
            command_class="git-publication",
            authorize_external_side_effects=True,
            credential_fd=93,
            _envelope_worktree="bound",
            _envelope_worktree_fd=71,
            scope_path=["tools/credential_handoff.py"],
            retry_window=3,
            timeout_seconds=10.0,
        )
        policy = MagicMock()
        with (
            patch.object(handoffctl, "backend_selection", return_value={"backend": "git"}),
            patch.object(handoffctl, "config", return_value={}),
            patch.object(handoffctl, "require_active_owner", return_value=policy),
            patch.object(handoffctl, "run_envelope_timeout", return_value=15.0),
            patch.object(handoffctl, "require_policy_unchanged"),
            patch.object(handoffctl.al, "prepare"),  # type: ignore[attr-defined]
            patch.object(handoffctl, "sandboxed_envelope_command", return_value=["gh", "status"]),
            patch.object(
                handoffctl,
                "locate",
                side_effect=[
                    (None, {"task_revision": 4}, None),
                    (None, {"task_revision": 5}, None),
                ],
            ),
            patch.object(handoffctl, "mutate") as mutate,
            patch.object(
                handoffctl,
                "_run_envelope_subprocess",
                return_value=subprocess.CompletedProcess(["gh", "status"], 0),
            ) as launch,
        ):
            result = handoffctl._cmd_run_fenced(args)
        self.assertEqual((policy, result[1], 10.0, False, 0), result[:5])
        launch.assert_called_once()
        reservation = mutate.call_args.args[0]
        self.assertEqual("execution-start", mutate.call_args.args[1])
        self.assertEqual("AR-1936", reservation.task)
        self.assertEqual(93, args.credential_fd)

    def test_cmd_run_fenced_rejects_invalid_retry_window_before_launch(self) -> None:
        args = argparse.Namespace(
            task="AR-1936",
            owner="worker",
            command=["true"],
            command_class="git-publication",
            authorize_external_side_effects=True,
            credential_fd=93,
            retry_window=2,
        )
        with (
            patch.object(handoffctl, "backend_selection", return_value={"backend": "git"}),
            patch.object(handoffctl, "config", return_value={}),
            patch.object(handoffctl, "require_active_owner", return_value=MagicMock()),
            patch.object(handoffctl, "_run_envelope_subprocess") as launch,
            self.assertRaisesRegex(RuntimeError, "retry circuit window"),
        ):
            handoffctl._cmd_run_fenced(args)
        launch.assert_not_called()

    def test_cmd_run_fenced_rejects_nonpositive_timeout_before_launch(self) -> None:
        args = argparse.Namespace(
            task="AR-1936",
            owner="worker",
            command=["true"],
            command_class="read",
            authorize_external_side_effects=False,
            timeout_seconds=0,
        )
        with (
            patch.object(handoffctl, "backend_selection", return_value={"backend": "git"}),
            patch.object(handoffctl, "config", return_value={}),
            patch.object(handoffctl, "require_active_owner", return_value=MagicMock()),
            patch.object(handoffctl, "_run_envelope_subprocess") as launch,
            self.assertRaisesRegex(RuntimeError, "timeout must be positive"),
        ):
            handoffctl._cmd_run_fenced(args)
        launch.assert_not_called()

    def test_cmd_run_fenced_rejects_timeout_above_envelope_cap(self) -> None:
        args = argparse.Namespace(
            task="AR-1936",
            owner="worker",
            command=["true"],
            command_class="git-publication",
            authorize_external_side_effects=True,
            credential_fd=93,
            retry_window=3,
            timeout_seconds=11.0,
        )
        with (
            patch.object(handoffctl, "backend_selection", return_value={"backend": "git"}),
            patch.object(handoffctl, "config", return_value={}),
            patch.object(handoffctl, "require_active_owner", return_value=MagicMock()),
            patch.object(handoffctl, "run_envelope_timeout", return_value=10.0),
            patch.object(handoffctl, "_run_envelope_subprocess") as launch,
            self.assertRaisesRegex(RuntimeError, "exceeds envelope limit"),
        ):
            handoffctl._cmd_run_fenced(args)
        launch.assert_not_called()

    def test_cmd_run_fenced_reserves_retry_circuit_without_bound_worktree(self) -> None:
        args = argparse.Namespace(
            task="AR-1936",
            owner="worker",
            command=["true"],
            command_class="read",
            authorize_external_side_effects=False,
            retry_window=3,
            timeout_seconds=5.0,
            scope_path=[],
        )
        policy = MagicMock()
        lock = MagicMock()
        with (
            patch.object(handoffctl, "backend_selection", return_value={"backend": "git"}),
            patch.object(handoffctl, "config", return_value={}),
            patch.object(handoffctl, "require_active_owner", return_value=policy),
            patch.object(handoffctl, "run_envelope_timeout", return_value=None),
            patch.object(handoffctl, "require_policy_unchanged"),
            patch.object(handoffctl.al, "prepare"),  # type: ignore[attr-defined]
            patch.object(handoffctl, "sandboxed_envelope_command", return_value=["true"]),
            patch.object(handoffctl, "locate", return_value=(None, {"task_revision": 4}, None)),
            patch.object(handoffctl, "mutate"),
            patch.object(handoffctl, "task_execution_locked", return_value=lock),
            patch.object(
                handoffctl,
                "_run_envelope_subprocess",
                return_value=subprocess.CompletedProcess(["true"], 0),
            ) as launch,
        ):
            result = handoffctl._cmd_run_fenced(args)
        self.assertEqual((policy, result[1], 5.0, False, 0, None, None), result)
        launch.assert_called_once()

    def test_dispatch_retry_circuit_status_routes_to_renderer(self) -> None:
        args = argparse.Namespace(
            retry_circuit_action="status",
            task="AR-1936",
        )
        with patch.object(handoffctl, "cmd_retry_circuit_status", return_value=7) as status:
            self.assertEqual(7, handoffctl.dispatch_retry_circuit(args))
        status.assert_called_once_with("AR-1936")

    def test_main_parses_credential_fd_and_dispatches_run(self) -> None:
        with (
            patch.object(
                sys,
                "argv",
                [
                    "handoffctl",
                    "run",
                    "--owner",
                    "worker",
                    "--command-class",
                    "git-publication",
                    "--authorize-external-side-effects",
                    "--credential-fd",
                    "93",
                    "AR-1936",
                    "--",
                    "true",
                ],
            ),
            patch.object(handoffctl, "assert_project_binding"),
            patch.object(handoffctl, "dispatch_bound_command", return_value=0) as dispatch,
        ):
            self.assertEqual(0, handoffctl.main())
        parsed = dispatch.call_args.args[0]
        self.assertEqual("run", parsed.cmd)
        self.assertEqual(93, parsed.credential_fd)
        self.assertEqual(["true"], parsed.command)

    def test_dispatch_side_effect_command_routes_supported_and_unknown_commands(self) -> None:
        args = argparse.Namespace(cmd="reconcile", commit=False, push=False)
        with patch.object(handoffctl, "reconcile") as reconcile:
            self.assertTrue(handoffctl.dispatch_side_effect_command(args))
        reconcile.assert_called_once_with(do_commit=False, push=False)

        args.cmd = "not-a-side-effect"
        self.assertFalse(handoffctl.dispatch_side_effect_command(args))


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
