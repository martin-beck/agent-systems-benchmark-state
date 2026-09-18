# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Bounded, fail-closed tests for the state TLC admission runner."""

from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import os
import subprocess
import sys
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
ATTEST_SPEC = importlib.util.spec_from_file_location(
    "attest", ROOT / "formal" / "handoffctl" / "attest.py"
)
if ATTEST_SPEC is None or ATTEST_SPEC.loader is None:
    raise RuntimeError("cannot load attestation helper")
ATTEST = importlib.util.module_from_spec(ATTEST_SPEC)
ATTEST_SPEC.loader.exec_module(ATTEST)
PROFILE_SPEC = importlib.util.spec_from_file_location(
    "tier_profiles", ROOT / "formal" / "handoffctl" / "tier_profiles.py"
)
if PROFILE_SPEC is None or PROFILE_SPEC.loader is None:
    raise RuntimeError("cannot load tier profiles")
PROFILES = importlib.util.module_from_spec(PROFILE_SPEC)
PROFILE_SPEC.loader.exec_module(PROFILES)
sys.modules["tier_profiles"] = PROFILES
SEED_SPEC = importlib.util.spec_from_file_location(
    "seed_profile", ROOT / "formal" / "handoffctl" / "seed_profile.py"
)
if SEED_SPEC is None or SEED_SPEC.loader is None:
    raise RuntimeError("cannot load seed profile")
SEED = importlib.util.module_from_spec(SEED_SPEC)
SEED_SPEC.loader.exec_module(SEED)
GUEST_SPEC = importlib.util.spec_from_file_location("guest_seed", ROOT / "tools" / "guest_seed.py")
if GUEST_SPEC is None or GUEST_SPEC.loader is None:
    raise RuntimeError("cannot load guest seed")
GUEST = importlib.util.module_from_spec(GUEST_SPEC)
GUEST_SPEC.loader.exec_module(GUEST)


class TlcRunnerTests(unittest.TestCase):
    def test_formal_workflow_selects_explicit_supported_tier(self) -> None:
        workflow = (ROOT / ".github" / "workflows" / "handoffctl-formal.yml").read_text(
            encoding="utf-8"
        )
        self.assertIn("run: formal/handoffctl/verify.sh --tier pr-publication", workflow)
        verify = (ROOT / "formal" / "handoffctl" / "verify.sh").read_text(encoding="utf-8")
        self.assertIn("TLC_RUNTIME_ROOT", workflow)
        self.assertIn("TLC_ATTESTATION_PATH", workflow)
        self.assertIn("TLC_RUNTIME_ROOT", verify)

    def test_pr_tier_has_one_process_contract_fixture(self) -> None:
        config = (ROOT / "formal" / "handoffctl" / "HandoffctlPR.cfg").read_text(encoding="utf-8")
        self.assertIn("Processes = {p1}", config)
        self.assertIn("Tasks = {t1}", config)

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

    def test_private_paths_reject_links_and_wrong_owner(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / "target"
            target.mkdir()
            link = root / "link"
            link.symlink_to(target, target_is_directory=True)
            with self.assertRaisesRegex(RUNNER.AdmissionError, "symbolic link"):
                RUNNER._private_directory(link)
            with (
                mock.patch.object(RUNNER.os, "getuid", return_value=-1),
                self.assertRaisesRegex(RUNNER.AdmissionError, "owner-only"),
            ):
                RUNNER._private_directory(root / "private")

    def test_digest_and_input_paths_reject_missing_or_linked_inputs(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            file_path = root / "input"
            file_path.write_text("fixture\n", encoding="utf-8")
            link = root / "link"
            link.symlink_to(file_path)
            self.assertIsNone(RUNNER._digest(link))
            self.assertIsNone(RUNNER._digest(root / "missing"))
            with self.assertRaisesRegex(RUNNER.AdmissionError, "symbolic link"):
                RUNNER._input_path(str(link), "model")
            with self.assertRaisesRegex(RUNNER.AdmissionError, "missing"):
                RUNNER._input_path(str(root / "missing"), "model")

    def test_git_provenance_failures_are_bounded(self) -> None:
        with (
            mock.patch.object(RUNNER.subprocess, "run", side_effect=OSError("unavailable")),
            self.assertRaisesRegex(RUNNER.AdmissionError, "Git provenance unavailable"),
        ):
            RUNNER._git_value(Path(), "rev-parse", "HEAD")
        with (
            mock.patch.object(
                RUNNER.subprocess,
                "run",
                side_effect=subprocess.TimeoutExpired(["git"], 1),
            ),
            self.assertRaisesRegex(RUNNER.AdmissionError, "Git provenance unavailable"),
        ):
            RUNNER._git_value(Path(), "rev-parse", "HEAD")
        failed = mock.Mock(returncode=1, stdout="")
        with (
            mock.patch.object(RUNNER.subprocess, "run", return_value=failed),
            self.assertRaisesRegex(RUNNER.AdmissionError, "Git provenance command"),
        ):
            RUNNER._git_value(Path(), "rev-parse", "HEAD")
        oversized = mock.Mock(returncode=0, stdout="x" * 129)
        with (
            mock.patch.object(RUNNER.subprocess, "run", return_value=oversized),
            self.assertRaisesRegex(RUNNER.AdmissionError, "oversized output"),
        ):
            RUNNER._git_value(Path(), "rev-parse", "HEAD")

    def test_provenance_rejects_missing_digest(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            inputs = [root / name for name in ("model", "jar", "config")]
            for path in inputs:
                path.write_text("fixture\n", encoding="utf-8")
            with (
                mock.patch.object(RUNNER, "_digest", return_value=None),
                self.assertRaisesRegex(RUNNER.AdmissionError, "formal input"),
            ):
                RUNNER._provenance(inputs[0], inputs[1], inputs[2], root / "meta")

    def test_bounded_process_reports_bounded_failure_detail(self) -> None:
        process = mock.Mock(pid=1234)
        process.wait.return_value = 7
        process.stderr.read.return_value = b"failure /srv/data/projects/private"
        with (
            mock.patch.object(RUNNER.subprocess, "Popen", return_value=process),
            contextlib.redirect_stderr(io.StringIO()) as output,
        ):
            result = RUNNER._bounded_process(["fixture"], 5)
        self.assertEqual(result, (7, False))
        self.assertIn("TLC child diagnostic", output.getvalue())
        self.assertNotIn("/srv/data/projects/private", output.getvalue())

    def test_bounded_process_escalates_after_timeout(self) -> None:
        process = mock.Mock(pid=1234)
        process.wait.side_effect = [
            subprocess.TimeoutExpired(["fixture"], 1),
            subprocess.TimeoutExpired(["fixture"], 1),
            None,
        ]
        with (
            mock.patch.object(RUNNER.subprocess, "Popen", return_value=process),
            mock.patch.object(RUNNER.os, "killpg") as killpg,
        ):
            self.assertEqual(RUNNER._bounded_process(["fixture"], 1), (124, True))
        self.assertEqual(killpg.call_count, 2)

    def test_numeric_bound_parsers_reject_invalid_values(self) -> None:
        with self.assertRaisesRegex(RUNNER.AdmissionError, "must be an integer"):
            RUNNER._positive_int("bad", "workers")
        with self.assertRaisesRegex(RUNNER.AdmissionError, "must be positive"):
            RUNNER._positive_int("0", "workers")
        with self.assertRaisesRegex(RUNNER.AdmissionError, "m or g"):
            RUNNER._heap_bytes("2x")
        with self.assertRaisesRegex(RUNNER.AdmissionError, "M or G"):
            RUNNER._memory_bytes("2x")

    def test_pid_liveness_handles_all_os_outcomes(self) -> None:
        self.assertFalse(RUNNER._pid_is_alive("bad"))
        self.assertFalse(RUNNER._pid_is_alive(0))
        with mock.patch.object(RUNNER.os, "kill", side_effect=ProcessLookupError):
            self.assertFalse(RUNNER._pid_is_alive(123))
        with mock.patch.object(RUNNER.os, "kill", side_effect=PermissionError):
            self.assertTrue(RUNNER._pid_is_alive(123))
        with mock.patch.object(RUNNER.os, "kill", side_effect=OSError):
            self.assertFalse(RUNNER._pid_is_alive(123))

    def test_prune_stale_records_ignores_unknown_and_existing_outcome(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            queue = Path(directory)
            unknown = queue / "unknown.job.json"
            unknown.write_text(json.dumps({"state": "done"}), encoding="utf-8")
            os.utime(unknown, (0, 0))
            existing = queue / "existing.job.json"
            existing.write_text(json.dumps({"state": "queued"}), encoding="utf-8")
            os.utime(existing, (0, 0))
            existing.with_name("existing.outcome.json").write_text("{}", encoding="utf-8")
            RUNNER._prune_stale(queue)
            self.assertTrue(unknown.exists())
            self.assertFalse(existing.exists())
            self.assertTrue((queue / "existing.outcome.json").exists())

    def test_prune_stale_records_rejects_corrupt_entry_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            queue = Path(directory)
            corrupt = queue / "corrupt.job.json"
            corrupt.write_text("not-json", encoding="utf-8")
            os.utime(corrupt, (0, 0))
            RUNNER._prune_stale(queue)
            outcome = queue / "corrupt.outcome.json"
            self.assertFalse(corrupt.exists())
            self.assertEqual(json.loads(outcome.read_text())["state"], "orphaned")

    def test_build_command_rejects_missing_limits_and_tools(self) -> None:
        values = {
            "jar": Path("j"),
            "model": Path("m"),
            "config": Path("c"),
            "metadir": Path("d"),
        }
        with self.assertRaisesRegex(RUNNER.AdmissionError, "non-zero"):
            RUNNER.build_command(**values, memory_max="0", cgroup_mode="off")
        with (
            mock.patch.object(RUNNER.shutil, "which", return_value=None),
            self.assertRaisesRegex(RUNNER.AdmissionError, "systemd-run"),
        ):
            RUNNER.build_command(**values, cgroup_mode="required")
        with (
            mock.patch.object(RUNNER.shutil, "which", side_effect=lambda name: name),
            self.assertRaisesRegex(RUNNER.AdmissionError, "cpu_quota"),
        ):
            RUNNER.build_command(**values, cpu_quota="invalid", cgroup_mode="portable")
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

    def test_portable_mode_separates_virtual_address_space_from_attested_memory(self) -> None:
        command = RUNNER.build_command(
            jar=Path("jar"),
            model=Path("model"),
            config=Path("config"),
            metadir=Path("meta"),
            memory_max="3G",
            swap_max="3G",
            address_space_max="8G",
            cgroup_mode="portable",
        )
        self.assertIn(f"--as={8 * 1024**3}:{8 * 1024**3}", command)
        self.assertNotIn(f"--as={3 * 1024**3}:{3 * 1024**3}", command)

    def test_default_admission_paths_are_on_second_disk(self) -> None:
        self.assertTrue(Path(RUNNER.DEFAULT_QUEUE).is_relative_to(Path("/srv/data/projects")))
        self.assertTrue(Path(RUNNER.DEFAULT_QUEUE).is_relative_to(RUNNER.APPROVED_RUNTIME_ROOT))
        self.assertEqual(
            RUNNER.DEFAULT_ADMISSION_LOCK,
            str(Path("/srv/data/projects/.asb-tlc") / "admission.lock"),
        )

    def test_canonical_lock_is_shared_by_default(self) -> None:
        args = RUNNER.parser().parse_args(
            ["--jar", "j", "--model", "m", "--config", "c", "--metadir", "d"]
        )
        self.assertEqual(args.admission_lock, RUNNER.DEFAULT_ADMISSION_LOCK)

    def test_bounded_process_kills_the_process_group_after_deadline(self) -> None:
        process = mock.Mock(pid=1234)
        process.wait.side_effect = [subprocess.TimeoutExpired(["fixture"], 1), None]
        with (
            mock.patch.object(RUNNER.subprocess, "Popen", return_value=process),
            mock.patch.object(RUNNER.os, "killpg") as killpg,
        ):
            result = RUNNER._bounded_process(["fixture"], 1)
        self.assertEqual(result, (124, True))
        killpg.assert_called_once_with(1234, RUNNER.signal.SIGTERM)

    def test_run_outcome_binds_inputs_and_artifact_paths(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            queue = root / "queue"
            jar = root / "jar"
            model = root / "model"
            config = root / "config"
            for path in (jar, model, config):
                path.write_text("fixture\n", encoding="utf-8")
            args = Namespace(
                queue=str(queue),
                jar=str(jar),
                model=str(model),
                config=str(config),
                metadir=str(root / "meta"),
                workers=2,
                heap="2048m",
                memory_max="3G",
                swap_max="3G",
                address_space_max="8G",
                cpu_quota="200%",
                tasks_max=64,
                timeout_seconds=10,
                cgroup_mode="off",
                admission_lock=str(root / "admission.lock"),
            )
            with (
                mock.patch.object(RUNNER, "DEFAULT_TMPDIR", root / "tmp"),
                mock.patch.object(RUNNER, "build_command", return_value=["java"]),
                mock.patch.object(RUNNER, "_bounded_process", return_value=(0, False)),
            ):
                self.assertEqual(RUNNER.run(args), 0)
            self.assertTrue((root / "tmp").is_dir())
            outcomes = list(queue.glob("*.outcome.json"))
            self.assertEqual(len(outcomes), 1)
            record = json.loads(outcomes[0].read_text(encoding="utf-8"))
            self.assertEqual(record["schema_version"], 1)
            source_root = SOURCE.resolve().parents[1]
            self.assertEqual(
                record["provenance"]["source_commit"],
                RUNNER._git_value(source_root, "rev-parse", "HEAD"),
            )
            self.assertTrue(record["provenance"]["runner_sha256"])
            self.assertEqual(record["classification"], "exit")

    def test_address_space_cannot_be_smaller_than_heap(self) -> None:
        with self.assertRaisesRegex(RUNNER.AdmissionError, "address-space limit"):
            RUNNER.build_command(
                jar=Path("jar"),
                model=Path("model"),
                config=Path("config"),
                metadir=Path("meta"),
                heap="2G",
                address_space_max="2G",
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
            jar = Path(directory) / "jar"
            model = Path(directory) / "model"
            config = Path(directory) / "config"
            for path in (jar, model, config):
                path.write_text("fixture\n", encoding="utf-8")
            args = Namespace(
                queue=str(queue),
                jar=str(jar),
                model=str(model),
                config=str(config),
                metadir=str(Path(directory) / "meta"),
                workers=2,
                heap="2048m",
                memory_max="3G",
                swap_max="3G",
                address_space_max="8G",
                cpu_quota="200%",
                tasks_max=64,
                timeout_seconds=10,
                cgroup_mode="off",
                admission_lock=str(Path(directory) / "admission.lock"),
            )
            with (
                mock.patch.object(RUNNER, "DEFAULT_TMPDIR", Path(directory) / "tmp"),
                mock.patch.object(RUNNER, "build_command", return_value=["java"]),
                mock.patch.object(RUNNER, "_bounded_process", side_effect=KeyboardInterrupt),
                self.assertRaises(KeyboardInterrupt),
            ):
                RUNNER.run(args)
            self.assertEqual(list(queue.glob("*.job.json")), [])
            outcomes = list(queue.glob("*.outcome.json"))
            self.assertEqual(len(outcomes), 1)
            self.assertEqual(json.loads(outcomes[0].read_text())["state"], "canceled")

    def test_manifest_rejects_malformed_and_duplicate_entries(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            manifest = Path(directory) / "manifest"
            manifest.write_text("HandoffctlBinding\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "malformed"):
                ATTEST.read_manifest(manifest)
            manifest.write_text(
                "HandoffctlBinding success\nHandoffctlBinding success\n", encoding="utf-8"
            )
            with self.assertRaisesRegex(ValueError, "duplicate"):
                ATTEST.read_manifest(manifest)

    def test_tier_evidence_rejects_wrong_schema(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            evidence = Path(directory) / "tier.json"
            evidence.write_text(json.dumps({"schema_version": 1, "tiers": {}}), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "exactly the supported tiers"):
                ATTEST.read_tier_evidence(evidence)

    def test_tier_evidence_records_separate_address_space_bound(self) -> None:
        tiers = ATTEST.read_tier_evidence(ROOT / "formal" / "tier-evidence.json")
        for tier in tiers.values():
            self.assertEqual(tier["memory_max"], "3G")
            self.assertEqual(tier["swap_max"], "3G")
            self.assertEqual(tier["address_space_max"], "8G")

    def test_full_exhaustive_uses_distinct_timeout_profile(self) -> None:
        tiers = ATTEST.read_tier_evidence(ROOT / "formal" / "tier-evidence.json")
        self.assertEqual(tiers["pr-publication"]["timeout_seconds"], 1800)
        self.assertEqual(tiers["full-exhaustive"]["timeout_seconds"], 7200)

    def test_full_exhaustive_rejects_required_timeout(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            evidence = json.loads((ROOT / "formal" / "tier-evidence.json").read_text())
            evidence["tiers"]["full-exhaustive"]["timeout_seconds"] = 1800
            path = Path(directory) / "tier.json"
            path.write_text(json.dumps(evidence), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "unsupported timeout"):
                ATTEST.read_tier_evidence(path)

    def test_tier_profile_rejects_unknown_and_preserves_required_bound(self) -> None:
        self.assertEqual(PROFILES.timeout_for_tier("pr-publication"), 1800)
        self.assertEqual(PROFILES.timeout_for_tier("full-exhaustive"), 7200)
        with self.assertRaisesRegex(ValueError, "unknown formal tier"):
            PROFILES.timeout_for_tier("unknown")

    def test_guest_seed_exports_tier_timeout_and_bounds(self) -> None:
        required = SEED.environment_for_tier("pr-publication")
        full = SEED.environment_for_tier("full-exhaustive")
        self.assertEqual(required["TLC_TIMEOUT_SECONDS"], "1800")
        self.assertEqual(full["TLC_TIMEOUT_SECONDS"], "7200")
        self.assertEqual(full["TLC_MEMORY_MAX"], required["TLC_MEMORY_MAX"])
        with self.assertRaisesRegex(ValueError, "unknown formal tier"):
            SEED.environment_for_tier("unknown")

    def test_guest_seed_renders_execution_timeout(self) -> None:
        required = GUEST.build_user_data("pr-publication")
        full = GUEST.build_user_data("full-exhaustive")
        self.assertIn("TLC_TIMEOUT_SECONDS=1800", required)
        self.assertIn("RuntimeMaxSec=1800", required)
        self.assertIn("TLC_TIMEOUT_SECONDS=7200", full)
        self.assertIn("RuntimeMaxSec=7200", full)

    def test_guest_seed_validates_containment_for_each_profile(self) -> None:
        portable = GUEST.build_user_data("portable-smoke")
        required = GUEST.build_user_data("pr-publication")
        self.assertIn('evidence["containment_mode"] == "portable"', portable)
        self.assertNotIn('evidence["containment_mode"] == "required"', portable)
        self.assertIn('evidence["containment_mode"] == "required"', required)

    def test_guest_seed_contains_complete_bounded_bootstrap(self) -> None:
        seed = GUEST.build_user_data("full-exhaustive")
        for contract in (
            "mount, UUID=" + GUEST.DATA_UUID,
            "TLC_JAR_PATH=/mnt/asb-data/tla2tools.jar",
            "TLC_JAR_SHA256=936a262061c914694dfd669a543be24573c45d5aa0ff20a8b96b23d01e050e88",
            "user-runtime-dir@1000.service",
            "user@1000.service",
            "DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus",
            "test, -S, /run/user/1000/bus",
            "TMPDIR=/mnt/asb-data/state/tmp",
            "TLC_ATTESTATION_PATH=/mnt/asb-data/state/evidence/full-exhaustive-attestation.json",
            "/run/asb-validate.py",
            "systemctl, poweroff",
        ):
            self.assertIn(contract, seed)
        self.assertNotIn("network:", seed)
        self.assertNotIn("curl", seed)
        self.assertNotIn("\\n  - [", seed)

    def test_verify_requires_preloaded_digest_pinned_jar_without_network_fallback(self) -> None:
        verify = (ROOT / "formal/handoffctl/verify.sh").read_text(encoding="utf-8")
        self.assertIn("TLC_RUNTIME_ROOT:-/srv/data/projects/.asb-tlc", verify)
        self.assertIn("curl --fail", verify)
        self.assertIn("sha256sum --check --strict", verify)

    def test_guest_seed_rejects_unknown_tier(self) -> None:
        with self.assertRaisesRegex(ValueError, "unknown formal tier"):
            GUEST.build_user_data("unknown")

    def test_guest_seed_normal_import_renders(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                "-c",
                "from tools.guest_seed import build_user_data; "
                "print(build_user_data('full-exhaustive'))",
            ],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("TLC_TIMEOUT_SECONDS=7200", completed.stdout)

    def test_runner_handles_io_and_child_failure_paths(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "input"
            path.write_text("fixture", encoding="utf-8")
            with mock.patch.object(RUNNER.Path, "open", side_effect=OSError("read failure")):
                self.assertIsNone(RUNNER._digest(path))
            process = mock.Mock(pid=1234)
            process.wait.return_value = 3
            process.stderr.read.return_value = b"child failure"
            process.stdout.read.return_value = b"child output"
            with (
                mock.patch.object(RUNNER.tempfile, "TemporaryFile", side_effect=PermissionError),
                mock.patch.object(RUNNER.subprocess, "Popen", return_value=process),
                contextlib.redirect_stderr(io.StringIO()),
            ):
                self.assertEqual(RUNNER._bounded_process(["fixture"], 5), (3, False))

    def test_runner_handles_admission_failure_and_cgroup_off(self) -> None:
        command = RUNNER.build_command(
            jar=Path("jar"),
            model=Path("model"),
            config=Path("config"),
            metadir=Path("meta"),
            cgroup_mode="off",
        )
        self.assertIn("java", command)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            args = Namespace(
                queue=str(root / "queue"),
                jar=str(root / "missing-jar"),
                model=str(root / "missing-model"),
                config=str(root / "missing-config"),
                metadir=str(root / "meta"),
                workers=2,
                heap="2048m",
                memory_max="3G",
                swap_max="3G",
                address_space_max="8G",
                cpu_quota="200%",
                tasks_max=64,
                timeout_seconds=10,
                cgroup_mode="off",
                admission_lock=str(root / "admission.lock"),
            )
            with (
                mock.patch.object(RUNNER, "DEFAULT_TMPDIR", root / "tmp"),
                self.assertRaisesRegex(RUNNER.AdmissionError, "model is missing"),
            ):
                RUNNER.run(args)


if __name__ == "__main__":
    unittest.main()
