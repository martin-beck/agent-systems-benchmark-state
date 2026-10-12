# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Tests for the provider-free unsigned-development path."""

from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPEC = importlib.util.spec_from_file_location(
    "unsigned_development_runner", ROOT / "tools" / "unsigned_development_runner.py"
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load unsigned development runner")
RUNNER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(RUNNER)


class UnsignedDevelopmentRunnerTests(unittest.TestCase):
    def test_receipt_is_provider_free_and_non_authorizing(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "receipt.json"
            receipt = RUNNER.create_receipt(output=output, workload="fixture")
            self.assertEqual(receipt, json.loads(output.read_text(encoding="utf-8")))
            self.assertEqual("unsigned-development", receipt["profile"])
            self.assertFalse(receipt["provider_required"])
            self.assertFalse(receipt["formal_execution"])
            self.assertFalse(receipt["qualification_authorized"])
            self.assertFalse(receipt["seed_retained"])
            self.assertRegex(receipt["seed_sha256"], r"^[0-9a-f]{64}$")

    def test_rejects_unbounded_or_whitespace_workload(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "receipt.json"
            for workload in ("", "bad workload", "x" * 129):
                with self.assertRaisesRegex(RUNNER.DevelopmentRunnerError, "workload"):
                    RUNNER.create_receipt(output=output, workload=workload)


if __name__ == "__main__":
    unittest.main()
