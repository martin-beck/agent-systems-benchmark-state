# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
# mypy: disable-error-code=attr-defined
"""Downstream-only command-result and fast-dispatch coverage for handoffctl."""

from __future__ import annotations

import argparse
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

from tools import handoffctl


class HandoffctlReceiptDispatchEdgeTests(unittest.TestCase):
    """Exercise receipt seams without sharing the live coordinator lock."""

    def setUp(self) -> None:
        self.directory = tempfile.TemporaryDirectory()
        self.root = Path(self.directory.name)
        runtime = self.root / ".runtime"
        runtime.mkdir(mode=0o700)
        self.coordinator_globals = patch.multiple(
            handoffctl,
            ROOT=self.root,
            RUNTIME=runtime,
            LOCK=runtime / "state.lock",
        )
        self.coordinator_globals.start()

    def tearDown(self) -> None:
        self.coordinator_globals.stop()
        self.directory.cleanup()

    def test_command_result_selects_the_authoritative_backend(self) -> None:
        sqlite = MagicMock()
        git = MagicMock()
        with (
            patch.object(
                handoffctl,
                "backend_selection",
                side_effect=[{"backend": "sqlite"}, {"backend": "git"}],
            ),
            patch.object(handoffctl, "mutating_sqlite_backend", return_value=sqlite),
            patch.object(handoffctl, "storage_backend", return_value=git),
            patch.object(handoffctl.command_results, "append_backend") as append,
        ):
            handoffctl.append_command_result("AR-0042", "sqlite-worker", "a" * 64, 0, False)
            handoffctl.append_command_result("AR-0043", "git-worker", "b" * 64, 75, True)

        self.assertEqual(
            [
                ((sqlite, handoffctl.now, "AR-0042", "sqlite-worker", "a" * 64, 0, False), {}),
                ((git, handoffctl.now, "AR-0043", "git-worker", "b" * 64, 75, True), {}),
            ],
            append.call_args_list,
        )

    def test_legacy_file_receipts_use_the_private_runtime_directory(self) -> None:
        loaded = [{"task": "AR-0042"}]
        with (
            patch.object(handoffctl.command_results, "append_file") as append,
            patch.object(handoffctl.command_results, "load_file", return_value=loaded) as load,
        ):
            handoffctl.append_file_command_result(
                "AR-0042", "worker", "c" * 64, 1, "failed", "2026-10-13T00:00:00Z"
            )
            self.assertEqual(loaded, handoffctl.legacy_command_results())
        append.assert_called_once_with(
            handoffctl.RUNTIME,
            "AR-0042",
            "worker",
            "c" * 64,
            1,
            "failed",
            "2026-10-13T00:00:00Z",
        )
        load.assert_called_once_with(handoffctl.RUNTIME)

    def test_envelope_subprocess_preserves_or_omits_the_worktree_descriptor(self) -> None:
        completed = MagicMock()
        inherited = argparse.Namespace(_envelope_worktree_fd=71)
        plain = argparse.Namespace()
        with patch.object(handoffctl.subprocess, "run", return_value=completed) as run:
            self.assertIs(completed, handoffctl._run_envelope_subprocess(["true"], 3.5, inherited))
            self.assertIs(completed, handoffctl._run_envelope_subprocess(["false"], 2.0, plain))
        self.assertEqual(
            [
                (
                    (["true"],),
                    {
                        "check": False,
                        "stdin": handoffctl.subprocess.DEVNULL,
                        "timeout": 3.5,
                        "pass_fds": (71,),
                    },
                ),
                (
                    (["false"],),
                    {"check": False, "stdin": handoffctl.subprocess.DEVNULL, "timeout": 2.0},
                ),
            ],
            run.call_args_list,
        )

    def test_fast_dispatch_uses_the_fast_module_and_preserves_its_error(self) -> None:
        args = argparse.Namespace(cmd="fast", fast_action="receipt", receipt_id="missing")
        with patch("tools.fast_receipt_cli.dispatch_fast", return_value=17) as dispatch:
            self.assertEqual(17, handoffctl.dispatch_fast_command(args))
        dispatch.assert_called_once_with(handoffctl, args)

        with (
            patch(
                "tools.fast_receipt_cli.dispatch_fast",
                side_effect=RuntimeError("unknown fast receipt"),
            ),
            self.assertRaisesRegex(RuntimeError, "unknown fast receipt"),
        ):
            handoffctl.dispatch_fast_command(args)

    def test_main_parses_fast_observation_before_delegating(self) -> None:
        argv = ["handoffctl", "fast", "observe", "--max-age-seconds", "15"]
        with (
            patch("sys.argv", argv),
            patch.object(handoffctl, "assert_project_binding") as binding,
            patch.object(handoffctl, "dispatch_fast_command", return_value=23) as dispatch,
        ):
            self.assertEqual(23, handoffctl.main())
        binding.assert_called_once_with()
        parsed = dispatch.call_args.args[0]
        self.assertEqual(
            ("fast", "observe", 15), (parsed.cmd, parsed.fast_action, parsed.max_age_seconds)
        )


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
