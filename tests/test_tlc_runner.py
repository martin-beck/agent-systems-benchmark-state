# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Focused tests for bounded TLC admission and resource containment."""

from __future__ import annotations

import importlib.util
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
_runner_spec = importlib.util.spec_from_file_location("tlc_runner", ROOT / "tools/tlc_runner.py")
assert _runner_spec and _runner_spec.loader
_runner = importlib.util.module_from_spec(_runner_spec)
_runner_spec.loader.exec_module(_runner)
AdmissionError = _runner.AdmissionError
_prune_stale = _runner._prune_stale
build_command = _runner.build_command
run = _runner.run
parser = _runner.parser
positive_int = _runner._positive_int
heap_bytes = _runner._heap_bytes
memory_bytes = _runner._memory_bytes


class TLCAdmissionTests(unittest.TestCase):
    def test_command_has_finite_workers_heap_and_cgroup_limits(self) -> None:
        command = build_command(
            jar=Path("tla.jar"),
            model=Path("Model.tla"),
            config=Path("Model.cfg"),
            metadir=Path("states"),
        )
        self.assertIn("-workers", command)
        self.assertIn("2", command)
        self.assertIn("-Xmx2048m", command)
        self.assertIn("-XX:+UseSerialGC", command)
        self.assertIn("-XX:MaxMetaspaceSize=256m", command)
        self.assertIn("-XX:CompressedClassSpaceSize=128m", command)
        self.assertIn("-Xss256k", command)
        self.assertIn("--property=MemoryMax=3G", command)
        self.assertIn("--property=MemorySwapMax=3G", command)
        self.assertIn("--property=CPUQuota=200%", command)
        self.assertIn("--property=TasksMax=64", command)
        self.assertIn("--property=KillMode=control-group", command)
        self.assertIn("--property=RuntimeMaxSec=1800", command)

    def test_uncontained_execution_is_explicit_only(self) -> None:
        command = build_command(
            jar=Path("tla.jar"),
            model=Path("Model.tla"),
            config=Path("Model.cfg"),
            metadir=Path("states"),
            cgroup_mode="off",
        )
        self.assertEqual(command[0], "java")
        self.assertNotIn("auto", command)

    def test_portable_execution_has_kernel_limits_and_timeout(self) -> None:
        with (
            patch("tools.tlc_runner.shutil.which", side_effect=lambda name: f"/usr/bin/{name}"),
        ):
            command = build_command(
                jar=Path("tla.jar"),
                model=Path("Model.tla"),
                config=Path("Model.cfg"),
                metadir=Path("states"),
                cgroup_mode="portable",
            )
        self.assertEqual(
            command[:5],
            ["/usr/bin/timeout", "--signal=TERM", "--kill-after=5s", "1800", "/usr/bin/prlimit"],
        )
        self.assertIn("--as=3221225472:3221225472", command)
        self.assertTrue(any(item.startswith("--nproc=") for item in command))
        self.assertIn("--cpu=3600:3600", command)

    def test_portable_containment_fails_closed_without_tools(self) -> None:
        with (
            patch("tools.tlc_runner.shutil.which", return_value=None),
            self.assertRaises(AdmissionError),
        ):
            build_command(
                jar=Path("tla.jar"),
                model=Path("Model.tla"),
                config=Path("Model.cfg"),
                metadir=Path("states"),
                cgroup_mode="portable",
            )

    def test_portable_containment_validates_each_tool_and_cpu_bound(self) -> None:
        for missing in ("timeout", "prlimit"):
            with (
                patch(
                    "tools.tlc_runner.shutil.which",
                    side_effect=lambda name, absent=missing: (
                        None if name == absent else "/usr/bin/tool"
                    ),
                ),
                self.assertRaises(AdmissionError),
            ):
                build_command(
                    jar=Path("tla.jar"),
                    model=Path("Model.tla"),
                    config=Path("Model.cfg"),
                    metadir=Path("states"),
                    cgroup_mode="portable",
                )
        with (
            patch("tools.tlc_runner.shutil.which", return_value="/usr/bin/tool"),
            self.assertRaises(AdmissionError),
        ):
            build_command(
                jar=Path("tla.jar"),
                model=Path("Model.tla"),
                config=Path("Model.cfg"),
                metadir=Path("states"),
                cpu_quota="bad",
                cgroup_mode="portable",
            )

    def test_required_containment_builds_when_systemd_exists(self) -> None:
        with patch("tools.tlc_runner.shutil.which", return_value="/usr/bin/systemd-run"):
            command = build_command(
                jar=Path("tla.jar"),
                model=Path("Model.tla"),
                config=Path("Model.cfg"),
                metadir=Path("states"),
            )
        self.assertEqual(command[0], "/usr/bin/systemd-run")

    def test_large_required_profile_has_cgroup_headroom(self) -> None:
        with patch("tools.tlc_runner.shutil.which", return_value="/usr/bin/systemd-run"):
            command = build_command(
                jar=Path("tla.jar"),
                model=Path("Model.tla"),
                config=Path("Model.cfg"),
                metadir=Path("states"),
                heap="4096m",
                memory_max="6G",
                swap_max="6G",
            )
        self.assertIn("-Xmx4096m", command)
        self.assertIn("--property=MemoryMax=6G", command)
        self.assertIn("--property=MemorySwapMax=6G", command)

    def test_rejects_heap_that_exceeds_memory(self) -> None:
        with self.assertRaises(AdmissionError):
            build_command(
                jar=Path("tla.jar"),
                model=Path("Model.tla"),
                config=Path("Model.cfg"),
                metadir=Path("states"),
                heap="3G",
                memory_max="3G",
                cgroup_mode="off",
            )

    def test_rejects_malformed_bounds_and_parses_explicit_limits(self) -> None:
        for function, value in ((positive_int, "0"), (positive_int, "bad")):
            with self.assertRaises(AdmissionError):
                function(value, "bound")
        for function in (heap_bytes, memory_bytes):
            with self.assertRaises(AdmissionError):
                function("bad")
        args = parser().parse_args(
            [
                "--jar",
                "j",
                "--model",
                "m",
                "--config",
                "c",
                "--metadir",
                "d",
                "--cgroup-mode",
                "off",
            ]
        )
        self.assertEqual(args.workers, 2)
        self.assertEqual(args.timeout_seconds, 1800)

    def test_rejects_zero_memory_or_process_limits(self) -> None:
        for kwargs in (
            {"memory_max": "0"},
            {"swap_max": "0"},
            {"tasks_max": 0},
            {"timeout_seconds": 0},
        ):
            with self.assertRaises(AdmissionError):
                build_command(
                    jar=Path("tla.jar"),
                    model=Path("Model.tla"),
                    config=Path("Model.cfg"),
                    metadir=Path("states"),
                    cgroup_mode="off",
                    **kwargs,
                )

    def test_required_cgroup_rejects_missing_systemd(self) -> None:
        with (
            patch("tools.tlc_runner.shutil.which", return_value=None),
            self.assertRaises(AdmissionError),
        ):
            build_command(
                jar=Path("tla.jar"),
                model=Path("Model.tla"),
                config=Path("Model.cfg"),
                metadir=Path("states"),
            )

    def test_queue_record_and_cleanup_survive_normal_completion(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            queue = Path(directory)
            args = type(
                "Args",
                (),
                {
                    "queue": str(queue),
                    "model": "Model.tla",
                    "jar": "tla.jar",
                    "config": "Model.cfg",
                    "metadir": str(queue / "states"),
                    "workers": 2,
                    "heap": "64m",
                    "memory_max": "1G",
                    "swap_max": "1G",
                    "cgroup_mode": "portable",
                    "cpu_quota": "200%",
                    "tasks_max": 64,
                    "timeout_seconds": 1800,
                },
            )()
            with (
                patch.object(_runner, "DEFAULT_ADMISSION_LOCK", queue / "admission.lock"),
                patch("tools.tlc_runner.shutil.which", return_value="/usr/bin/tool"),
                patch("tools.tlc_runner.subprocess.run") as execute,
            ):
                execute.return_value.returncode = 0
                self.assertEqual(run(args), 0)
                execute.assert_called_once()
            self.assertEqual(list(queue.glob("*.job.json")), [])
            outcomes = list(queue.glob("*.outcome.json"))
            self.assertEqual(len(outcomes), 1)
            self.assertEqual(json.loads(outcomes[0].read_text())["state"], "completed")

    def test_parser_keeps_canonical_lock_default_and_accepts_explicit_isolated_lock(self) -> None:
        isolated_lock = "isolated-admission.lock"
        args = parser().parse_args(
            [
                "--jar",
                "tla.jar",
                "--model",
                "Model.tla",
                "--config",
                "Model.cfg",
                "--metadir",
                "states",
            ]
        )
        self.assertEqual(args.admission_lock, _runner.DEFAULT_ADMISSION_LOCK)
        args = parser().parse_args(
            [
                "--jar",
                "tla.jar",
                "--model",
                "Model.tla",
                "--config",
                "Model.cfg",
                "--metadir",
                "states",
                "--admission-lock",
                isolated_lock,
            ]
        )
        self.assertEqual(args.admission_lock, isolated_lock)

    def test_parser_accepts_an_isolated_lock_from_environment(self) -> None:
        with patch.dict(os.environ, {"TLC_ADMISSION_LOCK": "environment.lock"}):
            args = parser().parse_args(
                [
                    "--jar",
                    "tla.jar",
                    "--model",
                    "Model.tla",
                    "--config",
                    "Model.cfg",
                    "--metadir",
                    "states",
                ]
            )
        self.assertEqual(args.admission_lock, "environment.lock")

    def test_stale_queue_records_are_pruned(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            record = Path(directory) / "stale.job.json"
            record.write_text(json.dumps({"state": "queued"}))
            record.touch()
            with patch("tools.tlc_runner.time.time", return_value=record.stat().st_mtime + 90000):
                _prune_stale(Path(directory))
            self.assertFalse(record.exists())
            outcome = next(Path(directory).glob("*.outcome.json"))
            self.assertEqual(json.loads(outcome.read_text())["state"], "orphaned")

    def test_corrupt_stale_queue_record_is_durable_orphan(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            queue = Path(directory)
            record = queue / "corrupt.job.json"
            record.write_text("not-json")
            record.touch()
            with patch("tools.tlc_runner.time.time", return_value=record.stat().st_mtime + 90000):
                _prune_stale(queue)
            self.assertFalse(record.exists())
            outcome = queue / "corrupt.outcome.json"
            self.assertEqual(json.loads(outcome.read_text())["state"], "orphaned")

    def test_stale_running_record_is_retained_for_reconciliation(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            queue = Path(directory)
            record = queue / "running.job.json"
            record.write_text(json.dumps({"state": "running", "pid": 1234}))
            record.touch()
            with patch("tools.tlc_runner.time.time", return_value=record.stat().st_mtime + 90000):
                _prune_stale(queue)
            self.assertTrue(record.exists())
            self.assertFalse((queue / "running.outcome.json").exists())

    def test_caller_cancel_persists_canceled_outcome(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            queue = Path(directory)
            args = type(
                "Args",
                (),
                {
                    "queue": str(queue),
                    "model": "Model.tla",
                    "jar": "tla.jar",
                    "config": "Model.cfg",
                    "metadir": str(queue / "states"),
                    "workers": 2,
                    "heap": "64m",
                    "memory_max": "1G",
                    "swap_max": "1G",
                    "cpu_quota": "200%",
                    "tasks_max": 64,
                    "timeout_seconds": 1800,
                    "cgroup_mode": "off",
                },
            )()
            with (
                patch.object(_runner, "DEFAULT_ADMISSION_LOCK", queue / "admission.lock"),
                patch("tools.tlc_runner.subprocess.run", side_effect=KeyboardInterrupt),
                self.assertRaises(KeyboardInterrupt),
            ):
                run(args)
            outcome = next(Path(directory).glob("*.outcome.json"))
            self.assertEqual(json.loads(outcome.read_text())["state"], "canceled")

    def test_cgroup_rejection_persists_failed_outcome(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            queue = Path(directory)
            args = type(
                "Args",
                (),
                {
                    "queue": str(queue),
                    "model": "Model.tla",
                    "jar": "tla.jar",
                    "config": "Model.cfg",
                    "metadir": str(queue / "states"),
                    "workers": 2,
                    "heap": "64m",
                    "memory_max": "1G",
                    "swap_max": "1G",
                    "cpu_quota": "200%",
                    "tasks_max": 64,
                    "timeout_seconds": 1800,
                    "cgroup_mode": "required",
                },
            )()
            with (
                patch.object(_runner, "DEFAULT_ADMISSION_LOCK", queue / "admission.lock"),
                patch("tools.tlc_runner.shutil.which", return_value=None),
            ):
                self.assertEqual(run(args), 2)
            outcome = next(Path(directory).glob("*.outcome.json"))
            self.assertEqual(json.loads(outcome.read_text())["state"], "failed")


if __name__ == "__main__":
    unittest.main()
