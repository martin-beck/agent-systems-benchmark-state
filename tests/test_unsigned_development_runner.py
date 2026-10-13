# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Tests for the provider-free unsigned-development path."""

from __future__ import annotations

import importlib.util
import json
import runpy
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock, patch

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

    def test_rejects_receipt_path_without_a_filename(self) -> None:
        with self.assertRaisesRegex(RUNNER.DevelopmentRunnerError, "must name a file"):
            RUNNER._write_receipt(Path(), {})

    def test_creates_missing_output_parent_atomically(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "new" / "nested" / "receipt.json"

            receipt = RUNNER.create_receipt(output=output)

            self.assertEqual(receipt, json.loads(output.read_text(encoding="utf-8")))
            self.assertEqual([], list(output.parent.glob(".*.tmp")))

    def test_main_returns_success_for_parsed_arguments(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "receipt.json"
            argument_parser = Mock(
                parse_args=Mock(return_value=SimpleNamespace(output=output, workload="cli"))
            )

            with patch.object(RUNNER, "parser", return_value=argument_parser):
                self.assertEqual(0, RUNNER.main())

            self.assertTrue(output.is_file())
            argument_parser.error.assert_not_called()

    def test_main_reports_runner_and_filesystem_errors(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            blocked_parent = Path(directory) / "not-a-directory"
            blocked_parent.write_text("file", encoding="utf-8")
            argument_parser = Mock(
                parse_args=Mock(
                    return_value=SimpleNamespace(
                        output=blocked_parent / "receipt.json", workload="development"
                    )
                )
            )
            argument_parser.error.side_effect = SystemExit(2)

            with (
                patch.object(RUNNER, "parser", return_value=argument_parser),
                self.assertRaisesRegex(SystemExit, "2"),
            ):
                RUNNER.main()

            argument_parser.error.assert_called_once()
            self.assertIn("File exists", argument_parser.error.call_args.args[0])

    def test_script_entrypoint_handles_success_and_invalid_input(self) -> None:
        script = ROOT / "tools" / "unsigned_development_runner.py"
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "receipt.json"
            with (
                patch.object(sys, "argv", [str(script), "--output", str(output)]),
                self.assertRaisesRegex(SystemExit, "0"),
            ):
                runpy.run_path(str(script), run_name="__main__")
            self.assertTrue(output.is_file())

            with (
                patch.object(
                    sys,
                    "argv",
                    [str(script), "--output", str(output), "--workload", "invalid workload"],
                ),
                self.assertRaisesRegex(SystemExit, "2"),
            ):
                runpy.run_path(str(script), run_name="__main__")


if __name__ == "__main__":
    unittest.main()
