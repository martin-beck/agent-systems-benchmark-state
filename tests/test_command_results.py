# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Validation coverage for durable wrapped-command result journals."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from tools.command_results import load_file


class CommandResultsTests(unittest.TestCase):
    def _write_record(self, record: dict[str, object]) -> Path:
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        runtime = Path(directory.name)
        (runtime / "command-results.jsonl").write_text(json.dumps(record) + "\n")
        return runtime

    def test_load_file_rejects_invalid_digest(self) -> None:
        runtime = self._write_record(
            {
                "at": "2026-10-13T00:00:00+00:00",
                "task": "AR-0001",
                "owner": "worker",
                "argv_sha256": "not-a-digest",
                "returncode": 0,
                "classification": "EXIT",
            }
        )
        with self.assertRaisesRegex(RuntimeError, "invalid command journal digest"):
            load_file(runtime)

    def test_load_file_rejects_non_integer_return_code(self) -> None:
        runtime = self._write_record(
            {
                "at": "2026-10-13T00:00:00+00:00",
                "task": "AR-0001",
                "owner": "worker",
                "argv_sha256": "a" * 64,
                "returncode": "0",
                "classification": "EXIT",
            }
        )
        with self.assertRaisesRegex(RuntimeError, "invalid command journal return code"):
            load_file(runtime)
