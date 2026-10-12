# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Downstream tests for the ASB coordinator projection launcher."""

from __future__ import annotations

import importlib.util
import os
import subprocess
import sys
import tempfile
import types
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LAUNCHER = ROOT / "tools" / "awq-handoffctl.py"


def load_launcher() -> types.ModuleType:
    spec = importlib.util.spec_from_file_location("asb_projection_launcher", LAUNCHER)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ProjectionLauncherTest(unittest.TestCase):
    def test_launcher_disables_bytecode_before_loading_vendor(self) -> None:
        result = subprocess.run(
            [str(ROOT / "tools" / "awq-handoffctl"), "--help"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            env={**os.environ, "PYTHONDONTWRITEBYTECODE": ""},
        )
        self.assertIn("reconcile", result.stdout)
        self.assertFalse(list((ROOT / "tools").rglob("*.pyc")))

    def test_transaction_restores_previous_matched_set_after_interruption(self) -> None:
        launcher = load_launcher()
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            runtime = root / ".runtime"
            runtime.mkdir()
            target = root / "PROJECT_STATE.md"
            target.write_text("old\n", encoding="utf-8")
            core = types.SimpleNamespace(
                ROOT=root,
                RUNTIME=runtime,
                atomic=lambda path, text: Path(path).write_text(text, encoding="utf-8"),
            )
            original_replace = Path.replace

            def fail_replace(self: Path, destination: Path) -> Path:
                if destination == target:
                    raise OSError("injected publication interruption")
                return original_replace(self, destination)

            Path.replace = fail_replace  # type: ignore[method-assign]
            try:
                with self.assertRaisesRegex(OSError, "injected publication interruption"):
                    launcher._publish_transaction(core, {target: "new\n"})
            finally:
                Path.replace = original_replace  # type: ignore[method-assign]
            self.assertEqual(target.read_text(encoding="utf-8"), "old\n")
            self.assertFalse((runtime / "asb-projection-transaction.json").exists())


if __name__ == "__main__":
    unittest.main()
