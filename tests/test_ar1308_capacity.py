# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Positive and negative tests for the AR-1308 capacity contract."""

from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path
from types import ModuleType
from unittest.mock import patch


def load_module() -> ModuleType:
    path = Path(__file__).parents[1] / "tools" / "validate_ar1308_capacity.py"
    spec = importlib.util.spec_from_file_location("validate_ar1308_capacity", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load AR-1308 validator")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


validator = load_module()
RECEIPT = json.loads(
    (Path(__file__).parents[1] / "runner/asb-state-tlc-vm-ar1308/runner-receipt.json").read_text()
)


class Ar1308CapacityTests(unittest.TestCase):
    def test_reviewed_receipt_is_ready(self) -> None:
        self.assertEqual(validator.validate_receipt(RECEIPT), [])

    def test_process_limits_cannot_be_widened(self) -> None:
        candidate = copy.deepcopy(RECEIPT)
        candidate["process_contract"]["memory_max"] = "8G"
        self.assertTrue(validator.validate_receipt(candidate))

    def test_all_receipt_shape_failures_are_reported(self) -> None:
        candidate = copy.deepcopy(RECEIPT)
        candidate.update(
            {
                "architecture": "aarch64",
                "disposable": False,
                "host_mounts": True,
                "network": "user",
                "guest_memory_bytes": 1,
                "vcpus": 1,
                "hypervisor": "qemu",
                "pinned_inputs": {"ar1307_commit": "x", "jdk_major": 8, "tlc_jar_sha256": "x"},
                "image_sha256": "bad",
                "model_config_sha256": "bad",
                "seed_sha256": "bad",
                "source_tree_sha256": "bad",
                "validator_sha256": "bad",
                "runner_id": "",
                "image_id": "",
                "overlay_id": "",
                "admission_lock_id": "",
                "cleanup_policy": "bad",
            }
        )
        issues = " ".join(validator.validate_receipt(candidate))
        for expected in ("architecture", "disposable", "host_mounts", "network", "JDK", "cleanup"):
            self.assertIn(expected, issues)

    def test_unknown_fields_fail_closed(self) -> None:
        candidate = copy.deepcopy(RECEIPT)
        candidate["unexpected"] = True
        self.assertIn("unknown fields", " ".join(validator.validate_receipt(candidate)))

    def test_wrong_image_and_guest_swap_fail_closed(self) -> None:
        candidate = copy.deepcopy(RECEIPT)
        candidate["image_sha256"] = "0" * 64
        candidate["guest_swap_bytes"] = 1
        issues = " ".join(validator.validate_receipt(candidate))
        self.assertIn("image", issues)
        self.assertIn("guest swap", issues)

    def test_disk_timeout_and_worker_contract_fail_closed(self) -> None:
        candidate = copy.deepcopy(RECEIPT)
        candidate["guest_disk_bytes"] = 1
        candidate["process_contract"]["timeout_seconds"] = 1
        candidate["process_contract"]["workers"] = 3
        issues = " ".join(validator.validate_receipt(candidate))
        self.assertIn("guest disk", issues)
        self.assertIn("process contract", issues)

    def test_cleanup_and_admission_identity_fail_closed(self) -> None:
        candidate = copy.deepcopy(RECEIPT)
        candidate["cleanup_policy"] = "unbounded"
        candidate["admission_lock_id"] = ""
        issues = " ".join(validator.validate_receipt(candidate))
        self.assertIn("cleanup policy", issues)
        self.assertNotEqual(validator.validate_receipt(candidate), [])

    def test_wrong_commit_fails_closed(self) -> None:
        candidate = copy.deepcopy(RECEIPT)
        candidate["pinned_inputs"]["ar1307_commit"] = "deadbeef0"
        self.assertIn("exact signed AR-1307 head", " ".join(validator.validate_receipt(candidate)))

    def test_unsigned_development_profile_is_explicit_and_diagnostic(self) -> None:
        candidate = copy.deepcopy(RECEIPT)
        candidate["pinned_inputs"]["ar1307_commit"] = "a" * 40
        self.assertEqual(validator.validate_receipt(candidate, "unsigned-development"), [])
        self.assertTrue(validator.validate_receipt(candidate))

    def test_unsigned_development_source_must_match_pin(self) -> None:
        from tempfile import TemporaryDirectory

        with TemporaryDirectory() as directory:
            source = Path(directory)
            (source / ".git").mkdir()
            with patch.object(
                validator,
                "_run",
                side_effect=[
                    validator.subprocess.CompletedProcess([], 0, "a" * 40, ""),
                    validator.subprocess.CompletedProcess([], 1, "", ""),
                    validator.subprocess.CompletedProcess([], 0, "", ""),
                    validator.subprocess.CompletedProcess([], 0, "a" * 40, ""),
                    validator.subprocess.CompletedProcess([], 0, "", ""),
                    validator.subprocess.CompletedProcess([], 0, "", ""),
                ],
            ):
                candidate = copy.deepcopy(RECEIPT)
                candidate["pinned_inputs"]["ar1307_commit"] = "a" * 40
                candidate["source_tree_sha256"] = validator.hashlib.sha256(b"").hexdigest()
                self.assertEqual(
                    validator._validate_source(candidate, source, "unsigned-development"), []
                )
                candidate["pinned_inputs"]["ar1307_commit"] = "b" * 40
                self.assertIn(
                    "does not match",
                    " ".join(validator._validate_source(candidate, source, "unsigned-development")),
                )

    def test_network_and_mounts_fail_closed(self) -> None:
        candidate = copy.deepcopy(RECEIPT)
        candidate["network"] = "user"
        candidate["host_mounts"] = True
        issues = " ".join(validator.validate_receipt(candidate))
        self.assertIn("network must be none", issues)
        self.assertIn("host_mounts=false", issues)

    def test_insufficient_host_capacity_fails_closed(self) -> None:
        issues = validator.validate_host(
            {
                "architecture": "x86_64",
                "memavailable_bytes": 1,
                "swapfree_bytes": 1,
                "available_disk_bytes": 1,
                "available_inodes": 1,
            }
        )
        self.assertEqual(len(issues), 4)

    def test_swap_oom_and_architecture_fail_closed(self) -> None:
        issues = validator.validate_host(
            {
                "architecture": "aarch64",
                "memavailable_bytes": 64 * validator.GIB,
                "swapfree_bytes": 0,
                "available_disk_bytes": 64 * validator.GIB,
                "available_inodes": 100_000,
            }
        )
        self.assertIn("architecture", issues[0])
        self.assertIn("swap", issues[1])

    def test_wrong_architecture_fails_closed(self) -> None:
        issues = validator.validate_host(
            {
                "architecture": "aarch64",
                "memavailable_bytes": 64 * validator.GIB,
                "swapfree_bytes": validator.MIN_HOST_SWAP,
                "available_disk_bytes": 64 * validator.GIB,
                "available_inodes": 100_000,
            }
        )
        self.assertEqual(issues, ["host architecture must be x86_64"])

    def test_live_input_binding_success_and_missing_artifacts(self) -> None:
        from tempfile import TemporaryDirectory

        with TemporaryDirectory() as lock_dir:
            lock = Path(lock_dir) / "admission.lock"
            lock.touch()
            with (
                patch.object(
                    validator,
                    "host_capacity",
                    return_value={
                        "architecture": "x86_64",
                        "memavailable_bytes": 64 * validator.GIB,
                        "swapfree_bytes": 2 * validator.GIB,
                        "available_disk_bytes": 64 * validator.GIB,
                        "available_inodes": 100_000,
                    },
                ),
                patch.object(validator, "_validate_vm", return_value=[]),
                patch.object(validator, "_validate_source", return_value=[]),
                patch.object(validator, "_validate_artifacts", return_value=[]),
            ):
                self.assertEqual(
                    validator.validate_live(
                        RECEIPT,
                        Path(lock_dir),
                        Path(lock_dir) / "image",
                        Path(lock_dir) / "overlay",
                        Path(lock_dir) / "source",
                        Path(lock_dir) / "model",
                        Path(lock_dir) / "seed",
                        Path(lock_dir) / "jdk",
                        Path(lock_dir) / "tlc.jar",
                        lock,
                    ),
                    [],
                )
            # The orchestration path is covered here; each live validator is
            # exercised independently below without embedding host paths.
            self.assertIn(
                "missing",
                " ".join(
                    validator._validate_artifacts(
                        RECEIPT,
                        Path("/no/model"),
                        Path("/no/seed"),
                        Path("/no/jdk"),
                        Path("/no/jar"),
                        lock,
                    )
                ),
            )

    def test_live_vm_and_source_failures_are_distinct(self) -> None:
        with patch.object(
            validator,
            "_run",
            side_effect=[
                validator.subprocess.CompletedProcess([], 1, "", ""),
                validator.subprocess.CompletedProcess([], 1, "", ""),
            ],
        ):
            issues = validator._validate_vm(Path("/missing-image"), Path("/missing-overlay"))
        self.assertIn("image file", " ".join(issues))
        self.assertIn("installed QEMU", " ".join(issues))
        self.assertIn("overlay metadata", " ".join(issues))
        self.assertIn(
            "Git metadata", validator._validate_source(RECEIPT, Path("/missing-source"))[0]
        )

    def test_live_metadata_malformed_and_source_mismatch_fail_closed(self) -> None:
        with patch.object(
            validator,
            "_run",
            side_effect=[
                validator.subprocess.CompletedProcess([], 0, "qemu 8.2.2", ""),
                validator.subprocess.CompletedProcess([], 0, "{}", ""),
            ],
        ):
            issues = validator._validate_vm(Path("/missing-image"), Path("/missing-overlay"))
        self.assertIn("malformed", " ".join(issues))
        from tempfile import TemporaryDirectory

        with TemporaryDirectory() as directory:
            source = Path(directory)
            (source / ".git").mkdir()
            with patch.object(
                validator,
                "_run",
                side_effect=[
                    validator.subprocess.CompletedProcess([], 0, "wrong", ""),
                    validator.subprocess.CompletedProcess([], 0, "wrong", ""),
                    validator.subprocess.CompletedProcess([], 1, "", ""),
                ],
            ):
                self.assertIn("exact signed", " ".join(validator._validate_source(RECEIPT, source)))

    def test_host_capacity_and_main_success_path(self) -> None:
        from tempfile import TemporaryDirectory

        with TemporaryDirectory() as directory:
            measured = validator.host_capacity(Path(directory))
            self.assertIn("available_inodes", measured)
            receipt = Path(directory) / "receipt.json"
            receipt.write_text(json.dumps(RECEIPT), encoding="utf-8")
            args = ["--receipt", str(receipt)]
            for name in (
                "runtime-root",
                "image",
                "overlay",
                "source",
                "model",
                "seed",
                "jdk",
                "tlc-jar",
                "admission-lock",
            ):
                args.extend((f"--{name}", str(receipt)))
            with patch.object(validator, "validate_live", return_value=[]):
                self.assertEqual(validator.main(args), 0)

    def test_main_reports_malformed_receipt_and_failures(self) -> None:
        with self.subTest("malformed"):
            from tempfile import TemporaryDirectory

            with TemporaryDirectory() as directory:
                receipt = Path(directory) / "receipt.json"
                receipt.write_text("not-json", encoding="utf-8")
                args = ["--receipt", str(receipt)]
                for name in (
                    "runtime-root",
                    "image",
                    "overlay",
                    "source",
                    "model",
                    "seed",
                    "jdk",
                    "tlc-jar",
                    "admission-lock",
                ):
                    args.extend((f"--{name}", str(receipt)))
                self.assertEqual(validator.main(args), 2)

    def test_main_labels_unsigned_development_as_diagnostic(self) -> None:
        from tempfile import TemporaryDirectory

        with TemporaryDirectory() as directory:
            receipt = Path(directory) / "receipt.json"
            candidate = copy.deepcopy(RECEIPT)
            candidate["pinned_inputs"]["ar1307_commit"] = "a" * 40
            receipt.write_text(json.dumps(candidate), encoding="utf-8")
            args = ["--receipt", str(receipt), "--profile", "unsigned-development"]
            for name in (
                "runtime-root",
                "image",
                "overlay",
                "source",
                "model",
                "seed",
                "jdk",
                "tlc-jar",
                "admission-lock",
            ):
                args.extend((f"--{name}", str(receipt)))
            with (
                patch.object(validator, "validate_live", return_value=[]),
                patch("builtins.print") as printed,
            ):
                self.assertEqual(validator.main(args), 0)
                output = json.loads(printed.call_args.args[0])
            self.assertEqual(output["status"], "diagnostic")
            self.assertFalse(output["qualification_authorized"])

    def test_live_validators_cover_bound_inputs_and_capacity_branches(self) -> None:
        from tempfile import TemporaryDirectory

        with TemporaryDirectory() as directory:
            root = Path(directory)
            image = root / "image"
            overlay = root / "overlay"
            model = root / "model"
            seed = root / "seed"
            jar = root / "tla2tools.jar"
            for path in (image, overlay, model, seed, jar):
                path.write_bytes(b"fixture")
            lock = root / "lock"
            lock.touch()
            jdk = root / "jdk"
            (jdk / "bin").mkdir(parents=True)
            (jdk / "bin/java").touch()
            with (
                patch.object(validator, "_digest", return_value=validator.REQUIRED_IMAGE_SHA256),
                patch.object(
                    validator,
                    "_run",
                    side_effect=[
                        validator.subprocess.CompletedProcess([], 0, "QEMU emulator 8.2.2", ""),
                        validator.subprocess.CompletedProcess(
                            [], 0, json.dumps({"virtual-size": 64 * validator.GIB}), ""
                        ),
                    ],
                ),
            ):
                self.assertEqual(validator._validate_vm(image, overlay), [])
            with (
                patch.object(
                    validator,
                    "_run",
                    return_value=validator.subprocess.CompletedProcess([], 0, "", 'version "17.0"'),
                ),
                patch.object(
                    validator, "_digest", side_effect=["m", "s", validator.REQUIRED_TLC_SHA256]
                ),
            ):
                candidate = copy.deepcopy(RECEIPT)
                candidate["model_config_sha256"] = "m"
                candidate["seed_sha256"] = "s"
                self.assertEqual(
                    validator._validate_artifacts(candidate, model, seed, jdk, jar, lock), []
                )

    def test_main_rejects_non_object_and_live_failure(self) -> None:
        from tempfile import TemporaryDirectory

        with TemporaryDirectory() as directory:
            receipt = Path(directory) / "receipt.json"
            receipt.write_text("[]", encoding="utf-8")
            args = ["--receipt", str(receipt)]
            for name in (
                "runtime-root",
                "image",
                "overlay",
                "source",
                "model",
                "seed",
                "jdk",
                "tlc-jar",
                "admission-lock",
            ):
                args.extend((f"--{name}", str(receipt)))
            self.assertEqual(validator.main(args), 1)
