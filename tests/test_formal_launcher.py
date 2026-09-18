# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Tests for the bounded launcher around the immutable formal script."""

from __future__ import annotations

import importlib
import os
import subprocess
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
        self.assertEqual(full["TMPDIR"], "/srv/data/projects/.asb-tlc")
        self.assertTrue(full["TLC_LAUNCHER_SHA256"])

    def test_environment_rejects_runtime_root_outside_approved_disk(self) -> None:
        with self.assertRaisesRegex(ValueError, "under /srv/data/projects"):
            run_formal_tier.environment("portable-smoke", runtime_root=Path("/etc/asb-runtime"))

    def test_environment_accepts_approved_runtime_subdirectory(self) -> None:
        root = Path("/srv/data/projects/.asb-tlc/test-runtime")
        environment = run_formal_tier.environment("portable-smoke", runtime_root=root)
        self.assertEqual(environment["TMPDIR"], str(root))

    def test_validate_runtime_environment_accepts_approved_paths(self) -> None:
        environment = run_formal_tier.environment("portable-smoke")
        with mock.patch.object(run_formal_tier, "_private_directory"):
            self.assertEqual(
                run_formal_tier._validate_runtime_environment(environment),
                Path("/srv/data/projects/.asb-tlc"),
            )

    def test_validate_runtime_environment_rejects_unapproved_runtime(self) -> None:
        environment = run_formal_tier.environment("portable-smoke")
        environment["TLC_RUNTIME_ROOT"] = "/etc/asb-runtime"
        environment["TMPDIR"] = "/etc/asb-runtime"
        with self.assertRaisesRegex(ValueError, "under /srv/data/projects"):
            run_formal_tier._validate_runtime_environment(environment)

    def test_validate_runtime_environment_rejects_mismatched_tmpdir(self) -> None:
        environment = run_formal_tier.environment("portable-smoke")
        environment["TMPDIR"] = "/srv/data/projects/.asb-tlc/other"
        with self.assertRaisesRegex(ValueError, "TMPDIR must match"):
            run_formal_tier._validate_runtime_environment(environment)

    def test_validate_runtime_environment_rejects_unapproved_attestation(self) -> None:
        environment = run_formal_tier.environment("portable-smoke")
        environment["TLC_ATTESTATION_PATH"] = "/etc/asb-attestation.json"
        with self.assertRaisesRegex(ValueError, "attestation path must remain"):
            run_formal_tier._validate_runtime_environment(environment)

    def test_unknown_tier_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "unknown formal tier"):
            run_formal_tier.environment("diagnostic")

    def test_run_uses_argv_without_retaining_output(self) -> None:
        process = mock.Mock(pid=1234)
        process.wait.return_value = 0
        process.poll.return_value = None
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

    def test_run_accepts_explicit_approved_environment(self) -> None:
        process = mock.Mock(pid=1234)
        process.wait.return_value = 0
        process.poll.return_value = 0
        root = Path("/srv/data/projects/.asb-tlc")
        with (
            mock.patch.object(run_formal_tier, "_private_directory"),
            mock.patch("subprocess.Popen", return_value=process),
        ):
            self.assertEqual(
                run_formal_tier.run(
                    "portable-smoke",
                    environ={
                        "TMPDIR": str(root),
                        "TLC_RUNTIME_ROOT": str(root),
                        "TLC_ATTESTATION_PATH": str(root / "attestations" / "portable.json"),
                    },
                ),
                0,
            )

    def test_timeout_profile_fallback_loads_reviewed_sibling(self) -> None:
        with mock.patch.object(
            importlib,
            "import_module",
            side_effect=ModuleNotFoundError("formal"),
        ):
            self.assertEqual(run_formal_tier._timeout_for_tier("portable-smoke"), 1800)

    def test_timeout_profile_fallback_rejects_missing_loader(self) -> None:
        spec = mock.Mock(loader=None)
        with (
            mock.patch.object(
                importlib,
                "import_module",
                side_effect=ModuleNotFoundError("formal"),
            ),
            mock.patch.object(importlib.util, "spec_from_file_location", return_value=spec),
            self.assertRaisesRegex(RuntimeError, "profile module is unavailable"),
        ):
            run_formal_tier._timeout_for_tier("portable-smoke")

    def test_private_directory_rejects_wrong_owner(self) -> None:
        with (
            tempfile.TemporaryDirectory() as directory,
            mock.patch.object(os, "getuid", return_value=-1),
            self.assertRaisesRegex(RuntimeError, "owner-private"),
        ):
            run_formal_tier._private_directory(Path(directory) / "runtime")

    def test_digest_reads_bounded_chunks(self) -> None:
        with tempfile.NamedTemporaryFile() as fixture:
            fixture.write(b"x" * (1024 * 1024 + 1))
            fixture.flush()
            self.assertTrue(run_formal_tier._digest(Path(fixture.name)))

    def test_terminate_handles_dead_process(self) -> None:
        process = mock.Mock(pid=1234)
        with mock.patch.object(os, "killpg", side_effect=ProcessLookupError):
            run_formal_tier._terminate(process)
        process.wait.assert_not_called()

    def test_terminate_retries_after_bounded_wait(self) -> None:
        process = mock.Mock(pid=1234)
        process.wait.side_effect = [subprocess.TimeoutExpired(["x"], 5), None]
        with mock.patch.object(os, "killpg") as killpg:
            run_formal_tier._terminate(process)
        self.assertEqual(killpg.call_count, 2)

    def test_failure_detail_sanitizes_and_bounds_output(self) -> None:
        process = mock.Mock()
        process.stderr.read.return_value = b"prefix /srv/data/projects/private " + b"x" * 1200
        detail = run_formal_tier._failure_detail(process)
        self.assertNotIn("/srv/data/projects/private", detail)
        self.assertLessEqual(len(detail), 1000)

    def test_failure_detail_handles_missing_stderr(self) -> None:
        process = mock.Mock(stderr=None)
        self.assertEqual(run_formal_tier._failure_detail(process), "no diagnostic was emitted")

    def test_wait_for_process_reports_nonzero_exit(self) -> None:
        process = mock.Mock(pid=1234)
        process.wait.return_value = 7
        process.poll.return_value = 0
        process.stderr.read.return_value = b"bounded failure"
        self.assertEqual(run_formal_tier._wait_for_process("portable-smoke", process, 5), 7)

    def test_wait_for_process_writes_timeout_receipt(self) -> None:
        process = mock.Mock(pid=1234)
        process.wait.side_effect = subprocess.TimeoutExpired(["x"], 5)
        process.poll.return_value = 0
        with (
            mock.patch.object(run_formal_tier, "_terminate"),
            mock.patch.object(run_formal_tier, "_write_interruption_receipt") as receipt,
        ):
            self.assertEqual(run_formal_tier._wait_for_process("portable-smoke", process, 5), 124)
        receipt.assert_called_once_with(
            "portable-smoke", state="timed_out", reason="bounded launcher timeout", timeout=5
        )

    def test_wait_for_process_writes_interruption_receipt(self) -> None:
        process = mock.Mock(pid=1234)
        process.wait.side_effect = KeyboardInterrupt
        process.poll.return_value = 0
        with (
            mock.patch.object(run_formal_tier, "_terminate"),
            mock.patch.object(run_formal_tier, "_write_interruption_receipt") as receipt,
            self.assertRaises(KeyboardInterrupt),
        ):
            run_formal_tier._wait_for_process("portable-smoke", process, 5)
        receipt.assert_called_once_with(
            "portable-smoke", state="interrupted", reason="launcher interruption", timeout=5
        )

    def test_main_dispatches_selected_tier(self) -> None:
        with (
            mock.patch.object(run_formal_tier, "run", return_value=0) as run,
            mock.patch("sys.argv", ["run_formal_tier.py", "--tier", "portable-smoke"]),
        ):
            self.assertEqual(run_formal_tier.main(), 0)
        run.assert_called_once_with("portable-smoke")

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
