# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Tests for the bounded launcher around the immutable formal script."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from subprocess import DEVNULL, PIPE
from unittest import mock

from tools import run_formal_tier


class FormalLauncherTests(unittest.TestCase):
    def test_environment_selects_exact_profile_and_private_root(self) -> None:
        portable = run_formal_tier.environment("portable-smoke")
        required = run_formal_tier.environment("pr-publication")
        full = run_formal_tier.environment("full-exhaustive")
        self.assertEqual(portable["TLC_CGROUP_MODE"], "portable")
        self.assertEqual(required["TLC_CGROUP_MODE"], "required")
        self.assertEqual(full["TLC_TIMEOUT_SECONDS"], "7200")
        self.assertTrue(Path(full["TMPDIR"]).is_relative_to(Path("/srv/data/projects")))
        self.assertTrue(full["TLC_LAUNCHER_SHA256"])

    def test_environment_rejects_runtime_root_outside_approved_disk(self) -> None:
        with self.assertRaisesRegex(ValueError, "under /srv/data/projects"):
            run_formal_tier.environment("portable-smoke", runtime_root=Path("/etc/asb-runtime"))

    def test_unknown_tier_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "unknown formal tier"):
            run_formal_tier.environment("diagnostic")

    def test_run_uses_argv_without_retaining_output(self) -> None:
        process = mock.Mock(pid=1234)
        process.wait.return_value = 0
        with (
            mock.patch.object(run_formal_tier, "_private_directory"),
            mock.patch("subprocess.Popen", return_value=process) as popen,
        ):
            self.assertEqual(run_formal_tier.run("portable-smoke"), 0)
        command = popen.call_args.args[0]
        self.assertEqual(command[-2:], ["--tier", "portable-smoke"])
        self.assertNotIn("shell", popen.call_args.kwargs)
        self.assertIs(popen.call_args.kwargs["stdout"], DEVNULL)
        self.assertIs(popen.call_args.kwargs["stderr"], PIPE)

    def test_interruption_receipt_is_bounded_and_non_success(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with mock.patch.object(run_formal_tier, "RUNTIME_ROOT", root):
                run_formal_tier._write_interruption_receipt(
                    "full-exhaustive",
                    state="interrupted",
                    reason="launcher interruption",
                    timeout=7800,
                )
            receipt = root / "receipts" / "full-exhaustive-interruption.json"
            payload = receipt.read_text(encoding="utf-8")
        self.assertIn('"state": "interrupted"', payload)
        self.assertIn('"timeout_seconds": 7800', payload)
        self.assertNotIn("attestation", payload)


if __name__ == "__main__":
    unittest.main()
