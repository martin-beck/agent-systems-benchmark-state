# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Focused tests for bounded TLC admission and resource containment."""

from __future__ import annotations

import importlib.util
import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import ANY, Mock, patch

ROOT = Path(__file__).resolve().parents[1]
_runner_spec = importlib.util.spec_from_file_location("tlc_runner", ROOT / "tools/tlc_runner.py")
assert _runner_spec and _runner_spec.loader
_runner = importlib.util.module_from_spec(_runner_spec)
_runner_spec.loader.exec_module(_runner)
AdmissionError = _runner.AdmissionError
_prune_stale = _runner._prune_stale
build_command = _runner.build_command
verify_effective_cgroup = _runner.verify_effective_cgroup
verify_effective_cgroup_main = _runner.verify_effective_cgroup_main
run = _runner.run
parser = _runner.parser
positive_int = _runner._positive_int
heap_bytes = _runner._heap_bytes
memory_bytes = _runner._memory_bytes


class TLCAdmissionTests(unittest.TestCase):
    @staticmethod
    def _args(queue: Path, **overrides: object) -> SimpleNamespace:
        values: dict[str, object] = {
            "queue": str(queue),
            "model": "Model.tla",
            "jar": "tla.jar",
            "config": "Model.cfg",
            "metadir": str(queue / "workspace" / "states"),
            "workspace": str(queue / "workspace"),
            "workers": 2,
            "heap": "64m",
            "memory_max": "1G",
            "swap_max": "1G",
            "storage_max": "1M",
            "storage_reserve": "1M",
            "cgroup_mode": "portable",
            "cpu_quota": "200%",
            "tasks_max": 64,
            "timeout_seconds": 1800,
            "admission_lock": str(queue / "admission.lock"),
        }
        values.update(overrides)
        return SimpleNamespace(**values)

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
        self.assertIn("-Djava.io.tmpdir=" + str(Path("states").parent.resolve()), command)
        self.assertIn("-Duser.dir=" + str(Path("states").parent.resolve()), command)
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

    def test_required_command_verifies_then_execs_inside_the_child_unit(self) -> None:
        with patch("tools.tlc_runner.shutil.which", return_value="/usr/bin/systemd-run"):
            command = build_command(
                jar=Path("tla.jar"),
                model=Path("Model.tla"),
                config=Path("Model.cfg"),
                metadir=Path("states"),
                memory_max="64G",
                swap_max="64G",
            )
        self.assertEqual(command[0], "/usr/bin/systemd-run")
        self.assertIn("--property=MemoryMax=64G", command)
        self.assertIn("--property=MemorySwapMax=64G", command)
        marker = command.index("--verify-effective-cgroup")
        self.assertEqual("--memory-max", command[marker + 1])
        self.assertEqual("64G", command[marker + 2])
        self.assertEqual("--swap-max", command[marker + 3])
        self.assertEqual("64G", command[marker + 4])
        self.assertIn("java", command[marker + 6 :])

    def test_effective_cgroup_rejects_lower_ancestor_and_wrong_leaf(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            mount = root / "cgroup"
            leaf = mount / "worker" / "unit"
            leaf.mkdir(parents=True)
            (root / "self").mkdir()
            (root / "self/cgroup").write_text("0::/worker/unit\n")
            (root / "self/mountinfo").write_text(f"1 0 0:1 / {mount} rw - cgroup2 cgroup rw\n")
            for directory in (mount, mount / "worker", leaf):
                for name in ("memory.max", "memory.high", "memory.swap.max"):
                    (directory / name).write_text("max\n")
            for name, value in (("memory.max", "3221225472"), ("memory.swap.max", "3221225472")):
                (leaf / name).write_text(value + "\n")
            verify_effective_cgroup(memory_max="3G", swap_max="3G", proc_root=root)
            (mount / "worker" / "memory.high").write_text("1\n")
            with self.assertRaisesRegex(AdmissionError, "effective memory.high"):
                verify_effective_cgroup(memory_max="3G", swap_max="3G", proc_root=root)
            (mount / "worker" / "memory.high").write_text("max\n")
            (leaf / "memory.max").write_text("1\n")
            with self.assertRaisesRegex(AdmissionError, "leaf memory.max"):
                verify_effective_cgroup(memory_max="3G", swap_max="3G", proc_root=root)

    def test_effective_cgroup_skips_an_undelegated_ancestor_control(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            mount = root / "cgroup"
            leaf = mount / "delegated" / "unit"
            leaf.mkdir(parents=True)
            (root / "self").mkdir()
            (root / "self/cgroup").write_text("0::/delegated/unit\n")
            (root / "self/mountinfo").write_text(f"1 0 0:1 / {mount} rw - cgroup2 cgroup rw\n")
            for directory in (mount, leaf):
                for name in ("memory.max", "memory.high", "memory.swap.max"):
                    (directory / name).write_text("max\n")
            for name in ("memory.max", "memory.swap.max"):
                (leaf / name).write_text("3221225472\n")
            verify_effective_cgroup(memory_max="3G", swap_max="3G", proc_root=root)
            (mount / "memory.max").write_text("1\n")
            with self.assertRaisesRegex(AdmissionError, "effective memory.max"):
                verify_effective_cgroup(memory_max="3G", swap_max="3G", proc_root=root)

    def test_effective_cgroup_resolves_a_non_root_cgroup_mount(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            mount = root / "cgroup"
            leaf = mount / "unit"
            leaf.mkdir(parents=True)
            (root / "self").mkdir()
            (root / "self/cgroup").write_text("0::/user.slice/user-985.slice/unit\n")
            (root / "self/mountinfo").write_text(
                f"1 0 0:1 /user.slice/user-985.slice {mount} rw - cgroup2 cgroup rw\n"
            )
            for directory in (mount, leaf):
                for name in ("memory.max", "memory.high", "memory.swap.max"):
                    (directory / name).write_text("max\n")
            for name in ("memory.max", "memory.swap.max"):
                (leaf / name).write_text("3221225472\n")
            verify_effective_cgroup(memory_max="3G", swap_max="3G", proc_root=root)

    def test_effective_cgroup_wrapper_strips_separator_before_exec(self) -> None:
        with (
            patch.object(_runner, "verify_effective_cgroup") as verify,
            patch.object(_runner.os, "execvp", side_effect=OSError("fixture")) as execute,
        ):
            result = verify_effective_cgroup_main(
                ["--memory-max", "3G", "--swap-max", "3G", "--", "java", "-version"]
            )
        self.assertEqual(2, result)
        verify.assert_called_once_with(memory_max="3G", swap_max="3G")
        execute.assert_called_once_with("java", ["java", "-version"])

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
        self.assertEqual(args.storage_max, "2G")
        self.assertEqual(args.storage_reserve, "256M")

    def test_private_workspace_rejects_metadir_outside_its_boundary(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with self.assertRaisesRegex(AdmissionError, "inside the private TLC workspace"):
                _runner._prepare_workspace(root / "workspace", root / "foreign", 1)

    def test_preflight_rejects_insufficient_workspace_capacity(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            workspace = Path(directory) / "workspace"
            with (
                patch.object(_runner, "_available_bytes", return_value=0),
                self.assertRaisesRegex(AdmissionError, "insufficient workspace capacity"),
            ):
                _runner._prepare_workspace(workspace, workspace / "states", 1)

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
                patch("tools.tlc_runner.subprocess.Popen") as execute,
            ):
                execute.return_value.poll.side_effect = [None, 0]
                execute.return_value.returncode = 0
                self.assertEqual(run(args), 0)
                execute.assert_called_once()
            self.assertEqual(list(queue.glob("*.job.json")), [])
            outcomes = list(queue.glob("*.outcome.json"))
            self.assertEqual(len(outcomes), 1)
            self.assertEqual(json.loads(outcomes[0].read_text())["state"], "completed")

    def test_run_marks_a_running_storage_breach_and_stops_portable_process(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            queue = Path(directory)
            args = self._args(queue)
            with (
                patch.object(_runner, "build_command", return_value=["tlc"]),
                patch.object(_runner, "_available_bytes", return_value=2 * 1024**2),
                patch.object(_runner, "_directory_bytes", side_effect=[2 * 1024**2] * 2),
                patch.object(_runner, "_stop_over_budget") as stop,
                patch.object(_runner.subprocess, "Popen") as execute,
            ):
                execute.return_value.poll.return_value = None
                execute.return_value.returncode = 9
                self.assertEqual(run(args), 75)
            stop.assert_called_once_with(execute.return_value, "portable", ANY)
            outcome = next(queue.glob("*.outcome.json"))
            record = json.loads(outcome.read_text())
            self.assertEqual(record["state"], "storage-exhausted")
            self.assertEqual(record["workspace_bytes"], 2 * 1024**2)

    def test_run_catches_a_fast_exit_that_exceeds_storage_after_poll(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            queue = Path(directory)
            args = self._args(queue)
            with (
                patch.object(_runner, "build_command", return_value=["tlc"]),
                patch.object(_runner, "_available_bytes", return_value=2 * 1024**2),
                patch.object(_runner, "_directory_bytes", return_value=2 * 1024**2),
                patch.object(_runner.subprocess, "Popen") as execute,
            ):
                execute.return_value.poll.return_value = 0
                execute.return_value.returncode = 0
                self.assertEqual(run(args), 75)
            record = json.loads(next(queue.glob("*.outcome.json")).read_text())
            self.assertEqual(record["state"], "storage-exhausted")

    def test_run_preserves_a_failed_admission_as_a_durable_outcome(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            queue = Path(directory)
            args = self._args(queue)
            with (
                patch.object(_runner, "_available_bytes", return_value=2 * 1024**2),
                patch.object(_runner, "build_command", side_effect=AdmissionError("no sandbox")),
                patch.object(_runner.sys, "stderr"),
            ):
                # stderr is intentionally not part of the durable proof; the outcome is.
                self.assertEqual(run(args), 2)
            record = json.loads(next(queue.glob("*.outcome.json")).read_text())
            self.assertEqual(record["state"], "failed")
            self.assertEqual(record["error"], "no sandbox")
            self.assertEqual(list(queue.glob("*.job.json")), [])

    def test_stop_over_budget_fails_closed_without_systemctl_for_required_unit(self) -> None:
        process = Mock()
        with (
            patch.object(_runner.shutil, "which", return_value=None),
            self.assertRaisesRegex(AdmissionError, "systemctl is required"),
        ):
            _runner._stop_over_budget(process, "required", "handoffctl-tlc-test")
        process.terminate.assert_not_called()

    def test_stop_over_budget_kills_a_portable_process_that_ignores_term(self) -> None:
        process = Mock()
        process.wait.side_effect = [subprocess.TimeoutExpired(["tlc"], 5), None]
        _runner._stop_over_budget(process, "portable", "unused")
        process.terminate.assert_called_once_with()
        process.kill.assert_called_once_with()
        self.assertEqual(process.wait.call_count, 2)

    def test_stale_pruning_preserves_existing_outcome_and_tolerates_disappearance(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            queue = Path(directory)
            record = queue / "stale.job.json"
            outcome = queue / "stale.outcome.json"
            record.write_text(json.dumps({"state": "queued"}))
            outcome.write_text('{"state":"completed"}\n')
            original_stat = Path.stat
            with patch.object(
                _runner.Path,
                "stat",
                autospec=True,
                side_effect=lambda path, *args, **kwargs: (
                    (_ for _ in ()).throw(FileNotFoundError)
                    if path == record
                    else original_stat(path, *args, **kwargs)
                ),
            ):
                _prune_stale(queue)
            self.assertEqual(outcome.read_text(), '{"state":"completed"}\n')

    def test_stale_pruning_marks_an_unreadable_queue_record_orphaned(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            queue = Path(directory)
            record = queue / "stale.job.json"
            record.write_text("not json")
            with patch("tools.tlc_runner.time.time", return_value=record.stat().st_mtime + 90000):
                _prune_stale(queue)
            outcome = json.loads((queue / "stale.outcome.json").read_text())
            self.assertEqual(outcome["state"], "orphaned")
            self.assertEqual(outcome["error"], "stale queue record was unreadable")

    def test_cgroup_discovery_and_required_leaf_controls_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "self").mkdir()
            (root / "self/cgroup").write_text("0::/unit\n")
            (root / "self/mountinfo").write_text("")
            with self.assertRaisesRegex(AdmissionError, "membership is unavailable"):
                _runner._cgroup_v2_directory(root)

            mount = root / "cgroup"
            leaf = mount / "unit"
            leaf.mkdir(parents=True)
            (root / "self/mountinfo").write_text(f"1 0 0:1 / {mount} rw - cgroup2 cgroup rw\n")
            for name in ("memory.high", "memory.swap.max"):
                (leaf / name).write_text("max\n")
            with self.assertRaisesRegex(AdmissionError, "required cgroup control"):
                verify_effective_cgroup(memory_max="3G", swap_max="3G", proc_root=root)

    def test_parser_keeps_canonical_lock_default_and_accepts_explicit_isolated_lock(self) -> None:
        isolated_lock = "isolated-admission.lock"
        with patch.dict(os.environ):
            os.environ.pop("TLC_ADMISSION_LOCK", None)
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
                patch("tools.tlc_runner.subprocess.Popen", side_effect=KeyboardInterrupt),
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

    def test_fast_exit_over_storage_budget_is_not_reported_as_completed(self) -> None:
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
                    "metadir": str(queue / "workspace" / "states"),
                    "workspace": str(queue / "workspace"),
                    "workers": 2,
                    "heap": "64m",
                    "memory_max": "1G",
                    "swap_max": "1G",
                    "storage_max": "1M",
                    "storage_reserve": "1M",
                    "admission_lock": str(queue / "admission.lock"),
                    "cpu_quota": "200%",
                    "tasks_max": 64,
                    "timeout_seconds": 1800,
                    "cgroup_mode": "off",
                },
            )()
            with (
                patch.object(_runner, "_available_bytes", return_value=2 * 1024**2),
                patch.object(_runner, "_directory_bytes", return_value=2 * 1024**2),
                patch("tools.tlc_runner.subprocess.Popen") as execute,
            ):
                execute.return_value.poll.return_value = 0
                execute.return_value.returncode = 0
                self.assertEqual(run(args), 75)
            outcome = next(queue.glob("*.outcome.json"))
            self.assertEqual("storage-exhausted", json.loads(outcome.read_text())["state"])

    def test_required_storage_stop_targets_the_transient_unit(self) -> None:
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
                    "metadir": str(queue / "workspace" / "states"),
                    "workspace": str(queue / "workspace"),
                    "workers": 2,
                    "heap": "64m",
                    "memory_max": "1G",
                    "swap_max": "1G",
                    "storage_max": "1M",
                    "storage_reserve": "1M",
                    "admission_lock": str(queue / "admission.lock"),
                    "cpu_quota": "200%",
                    "tasks_max": 64,
                    "timeout_seconds": 1800,
                    "cgroup_mode": "required",
                },
            )()
            with (
                patch.object(_runner, "_available_bytes", return_value=2 * 1024**2),
                patch.object(_runner, "_directory_bytes", return_value=2 * 1024**2),
                patch("tools.tlc_runner.shutil.which", side_effect=lambda name: f"/usr/bin/{name}"),
                patch("tools.tlc_runner.subprocess.Popen") as execute,
                patch("tools.tlc_runner.subprocess.run") as stop,
            ):
                execute.return_value.poll.side_effect = [None, 0]
                execute.return_value.returncode = 0
                self.assertEqual(run(args), 75)
            self.assertEqual(["/usr/bin/systemctl", "--user", "stop"], stop.call_args.args[0][:3])


if __name__ == "__main__":
    unittest.main()
