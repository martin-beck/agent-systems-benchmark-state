# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Positive and negative tests for the AR-1308 capacity contract."""

from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path


def load_module():
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

    def test_wrong_commit_fails_closed(self) -> None:
        candidate = copy.deepcopy(RECEIPT)
        candidate["pinned_inputs"]["ar1307_commit"] = "deadbeef0"
        self.assertIn("exact signed AR-1307 head", " ".join(validator.validate_receipt(candidate)))

    def test_network_and_mounts_fail_closed(self) -> None:
        candidate = copy.deepcopy(RECEIPT)
        candidate["network"] = "user"
        candidate["host_mounts"] = True
        issues = " ".join(validator.validate_receipt(candidate))
        self.assertIn("network must be none", issues)
        self.assertIn("host_mounts=false", issues)

    def test_insufficient_host_capacity_fails_closed(self) -> None:
        issues = validator.validate_host(
            {"architecture": "x86_64", "available_memory_bytes": 1, "available_disk_bytes": 1}
        )
        self.assertEqual(len(issues), 2)

    def test_wrong_architecture_fails_closed(self) -> None:
        issues = validator.validate_host(
            {
                "architecture": "aarch64",
                "available_memory_bytes": 64 * validator.GIB,
                "available_disk_bytes": 64 * validator.GIB,
            }
        )
        self.assertEqual(issues, ["host architecture must be x86_64"])
