# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Downstream coverage for strict command-result journal validation."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from tools import command_results


class CommandResultJournalValidationEdgeTests(unittest.TestCase):
    """Cover valid and rejected values at the journal's strict type boundary."""

    def setUp(self) -> None:
        self.directory = tempfile.TemporaryDirectory()
        self.runtime = Path(self.directory.name)

    def tearDown(self) -> None:
        self.directory.cleanup()

    def write_record(self, **overrides: object) -> None:
        record: dict[str, object] = {
            "at": "2026-10-13T00:00:00Z",
            "task": "AR-0042",
            "owner": "worker",
            "argv_sha256": "a" * 64,
            "returncode": 0,
            "classification": "EXIT",
        }
        record.update(overrides)
        (self.runtime / "command-results.jsonl").write_text(json.dumps(record) + "\n")

    def test_load_file_accepts_a_hex_digest_and_integer_return_code(self) -> None:
        self.write_record(argv_sha256="f" * 64, returncode=-1)

        self.assertEqual(
            [
                {
                    "at": "2026-10-13T00:00:00Z",
                    "task": "AR-0042",
                    "owner": "worker",
                    "argv_sha256": "f" * 64,
                    "returncode": -1,
                    "classification": "EXIT",
                }
            ],
            command_results.load_file(self.runtime),
        )

    def test_load_file_rejects_a_non_hex_digest(self) -> None:
        self.write_record(argv_sha256="g" * 64)

        with self.assertRaisesRegex(RuntimeError, "invalid command journal digest at line 1"):
            command_results.load_file(self.runtime)

    def test_load_file_rejects_a_non_integer_return_code(self) -> None:
        self.write_record(returncode="0")

        with self.assertRaisesRegex(RuntimeError, "invalid command journal return code at line 1"):
            command_results.load_file(self.runtime)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
