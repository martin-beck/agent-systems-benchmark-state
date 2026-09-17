"""Bounded, fail-closed tests for the state TLC admission runner."""

from __future__ import annotations

import importlib.util
import json
import os
import tempfile
import unittest
from argparse import Namespace
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "tools" / "tlc_runner.py"
SPEC = importlib.util.spec_from_file_location("tlc_runner", SOURCE)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load TLC runner")
RUNNER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(RUNNER)


class TlcRunnerTests(unittest.TestCase):
    def test_command_has_bounded_jvm_and_process_group(self) -> None:
        command = RUNNER.build_command(
            jar=Path("tla.jar"),
            model=Path("Handoffctl.tla"),
            config=Path("Handoffctl.cfg"),
            metadir=Path("states"),
            cgroup_mode="required",
        )
        self.assertTrue(command[0].endswith("/systemd-run"))
        self.assertIn("--property=MemoryMax=3G", command)
        self.assertIn("--property=MemorySwapMax=3G", command)
        self.assertIn("--property=TasksMax=64", command)
        self.assertIn("--property=KillMode=control-group", command)
        self.assertIn("-Xmx2048m", command)

    def test_invalid_bounds_fail_closed(self) -> None:
        with self.assertRaises(RUNNER.AdmissionError):
            RUNNER.build_command(
                jar=Path("jar"),
                model=Path("model"),
                config=Path("config"),
                metadir=Path("meta"),
                heap="3G",
                memory_max="3G",
                cgroup_mode="off",
            )
        with self.assertRaises(RUNNER.AdmissionError):
            RUNNER.build_command(
                jar=Path("jar"),
                model=Path("model"),
                config=Path("config"),
                metadir=Path("meta"),
                workers=0,
                cgroup_mode="off",
            )

    def test_portable_mode_requires_bounded_host_tools(self) -> None:
        with (
            mock.patch.object(RUNNER.shutil, "which", return_value=None),
            self.assertRaisesRegex(RUNNER.AdmissionError, "timeout and prlimit"),
        ):
            RUNNER.build_command(
                jar=Path("jar"),
                model=Path("model"),
                config=Path("config"),
                metadir=Path("meta"),
                cgroup_mode="portable",
            )

    def test_stale_queued_record_is_reconciled(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            queue = Path(directory)
            job = queue / "old.job.json"
            job.write_text(json.dumps({"state": "queued"}) + "\n", encoding="utf-8")
            old = job.stat().st_mtime - 90_000
            os.utime(job, (old, old))
            RUNNER._prune_stale(queue)
            self.assertFalse(job.exists())
            outcome = queue / "old.outcome.json"
            self.assertEqual(json.loads(outcome.read_text(encoding="utf-8"))["state"], "orphaned")

    def test_live_running_record_is_not_reclaimed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            queue = Path(directory)
            job = queue / "live.job.json"
            job.write_text(
                json.dumps({"state": "running", "pid": os.getpid()}) + "\n", encoding="utf-8"
            )
            old = job.stat().st_mtime - 90_000
            os.utime(job, (old, old))
            RUNNER._prune_stale(queue)
            self.assertTrue(job.exists())
            self.assertFalse((queue / "live.outcome.json").exists())

    def test_run_records_cancellation_and_removes_queue_entry(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            queue = Path(directory) / "queue"
            args = Namespace(
                queue=str(queue),
                jar="jar",
                model="model",
                config="config",
                metadir=str(Path(directory) / "meta"),
                workers=2,
                heap="2048m",
                memory_max="3G",
                swap_max="3G",
                cpu_quota="200%",
                tasks_max=64,
                timeout_seconds=10,
                cgroup_mode="off",
                admission_lock=str(Path(directory) / "admission.lock"),
            )
            with (
                mock.patch.object(RUNNER, "build_command", return_value=["java"]),
                mock.patch.object(RUNNER.subprocess, "run", side_effect=KeyboardInterrupt),
                self.assertRaises(KeyboardInterrupt),
            ):
                RUNNER.run(args)
            self.assertEqual(list(queue.glob("*.job.json")), [])
            outcomes = list(queue.glob("*.outcome.json"))
            self.assertEqual(len(outcomes), 1)
            self.assertEqual(json.loads(outcomes[0].read_text())["state"], "canceled")


if __name__ == "__main__":
    unittest.main()
