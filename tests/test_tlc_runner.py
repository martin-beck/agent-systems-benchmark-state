# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Bounded, fail-closed tests for the state TLC admission runner."""

from __future__ import annotations

import importlib.util
import json
import os
import sys
import tempfile
import subprocess
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
        self.assertIn("run: formal/handoffctl/verify.sh --tier full-exhaustive", workflow)
        verify = (ROOT / "formal" / "handoffctl" / "verify.sh").read_text(encoding="utf-8")
        self.assertIn("--timeout-seconds", verify)
        self.assertIn("timeout_for_tier", verify)

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
                address_space_max="8G",
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

    def test_guest_seed_contains_complete_bounded_bootstrap(self) -> None:
        seed = GUEST.build_user_data("full-exhaustive")
        for contract in (
            "mount, UUID=fecbb9dc-d835-4bd5-b8bc-a053d677bf21",
            "/usr/local/libexec/asb-offline/curl",
            "cp /mnt/asb-data/tla2tools.jar",
            "user-runtime-dir@1000.service",
            "user@1000.service",
            "DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus",
            "test, -S, /run/user/1000/bus",
            "GIT_DIR=/mnt/asb-data/git",
            "TMPDIR=/mnt/asb-data/tmp",
            "TLC_ATTESTATION_PATH=/mnt/asb-data/evidence/full-exhaustive-attestation.json",
            "/run/asb-validate.py",
            "systemctl, poweroff",
        ):
            self.assertIn(contract, seed)
        self.assertNotIn("network:", seed)
        self.assertNotIn("\\n  - [", seed)

    def test_guest_seed_rejects_unknown_tier(self) -> None:
        with self.assertRaisesRegex(ValueError, "unknown formal tier"):
            GUEST.build_user_data("unknown")

    def test_guest_seed_normal_import_renders(self) -> None:
        completed = subprocess.run(
            [sys.executable, "-c", "from tools.guest_seed import build_user_data; print(build_user_data('full-exhaustive'))"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("TLC_TIMEOUT_SECONDS=7200", completed.stdout)


if __name__ == "__main__":
    unittest.main()
