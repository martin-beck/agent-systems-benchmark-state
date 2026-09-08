# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Tests for exact all-source state header verification."""

from __future__ import annotations

import contextlib
import importlib.util
import io
import subprocess
import tempfile
import unittest
from pathlib import Path
from types import ModuleType
from unittest.mock import patch


def load_checker() -> ModuleType:
    path = Path(__file__).resolve().parents[1] / "tools" / "check_source_headers.py"
    spec = importlib.util.spec_from_file_location("check_source_headers", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("unable to load source-header checker")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


checker = load_checker()


def init_repository(root: Path) -> None:
    subprocess.run(["git", "init", "-q"], cwd=root, check=True)


class SourceHeaderTests(unittest.TestCase):
    def test_comment_prefix_selects_all_reviewed_formats_and_launchers(self) -> None:
        self.assertEqual(checker.comment_prefix(Path("src/tool.py")), "# ")
        self.assertEqual(checker.comment_prefix(Path("scripts/check.sh")), "# ")
        self.assertEqual(checker.comment_prefix(Path("formal/Model.tla")), r"\* ")
        self.assertEqual(checker.comment_prefix(Path("tools/handoffctl")), "# ")
        self.assertEqual(checker.comment_prefix(Path("tools/awq")), "# ")
        self.assertIsNone(checker.comment_prefix(Path("nested/tools/awq")))
        self.assertIsNone(checker.comment_prefix(Path("schema.json")))

    def test_check_file_accepts_plain_shebang_and_tla_headers(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            plain = Path("plain.py")
            shell = Path("tool.sh")
            model = Path("Model.tla")
            (root / plain).write_text(
                f"# {checker.COPYRIGHT}\n# {checker.SPDX}\n\npass\n", encoding="utf-8"
            )
            (root / shell).write_text(
                f"#!/bin/sh\n# {checker.COPYRIGHT}\n# {checker.SPDX}\n\nexit 0\n",
                encoding="utf-8",
            )
            (root / model).write_text(
                f"---- MODULE Model ----\n\\* {checker.COPYRIGHT}\n\\* {checker.SPDX}\n",
                encoding="utf-8",
            )
            self.assertEqual(checker.check_file(root, plain), [])
            self.assertEqual(checker.check_file(root, shell), [])
            self.assertEqual(checker.check_file(root, model), [])

    def test_tla_prologue_requires_syntax_and_matching_file_stem(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = Path("Model.tla")
            for prologue in ("not a module", "---- MODULE Other ----"):
                with self.subTest(prologue=prologue):
                    (root / path).write_text(
                        f"{prologue}\n\\* {checker.COPYRIGHT}\n\\* {checker.SPDX}\n",
                        encoding="utf-8",
                    )
                    issues = checker.check_file(root, path)
                    self.assertEqual(len(issues), 1)
                    self.assertIn("matching TLA+ MODULE declaration", issues[0])

    def test_check_file_rejects_malformed_or_duplicate_pairs(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = Path("tool.py")
            cases = (
                f"# {checker.SPDX}\n# {checker.COPYRIGHT}\n",
                "# Copyright (C) Huawei Technologies Co., Ltd. 2025. All rights reserved.\n"
                f"# {checker.SPDX}\n",
                f"# {checker.COPYRIGHT} \n# {checker.SPDX}\n",
                f"# {checker.COPYRIGHT}\n# SPDX-License-Identifier: Apache-2.0\n",
            )
            for data in cases:
                with self.subTest(data=data):
                    (root / path).write_text(data, encoding="utf-8")
                    self.assertTrue(checker.check_file(root, path))
            pair = f"# {checker.COPYRIGHT}\n# {checker.SPDX}\n"
            (root / path).write_text(pair + "\npass\n" + pair, encoding="utf-8")
            self.assertIn("exactly one canonical", checker.check_file(root, path)[0])

    def test_check_file_allows_standalone_matching_test_data(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = Path("tool.py")
            (root / path).write_text(
                f'# {checker.COPYRIGHT}\n# {checker.SPDX}\n\ndata = """\n'
                f"# {checker.COPYRIGHT}\nvalue\n# {checker.SPDX}\n"
                '"""\n',
                encoding="utf-8",
            )
            self.assertEqual(checker.check_file(root, path), [])

    def test_check_file_reports_read_errors_and_unsupported_paths(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            binary = Path("tool.py")
            (root / binary).write_bytes(b"\xff")
            self.assertIn("not valid UTF-8", checker.check_file(root, binary)[0])
            self.assertIn("cannot read source", checker.check_file(root, Path("missing.py"))[0])
            with self.assertRaisesRegex(checker.HeaderCheckError, "unsupported source"):
                checker.check_file(root, Path("schema.json"))

    def test_tracked_selection_is_nul_safe_and_includes_vendored_sources(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            init_repository(root)
            header = f"# {checker.COPYRIGHT}\n# {checker.SPDX}\n"
            for name in ("source with space.py", "line\nbreak.sh", "vendor/tool.py"):
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(header, encoding="utf-8")
            subprocess.run(["git", "add", "."], cwd=root, check=True)
            self.assertEqual(
                set(checker.tracked_source_files(root)),
                {Path("source with space.py"), Path("line\nbreak.sh"), Path("vendor/tool.py")},
            )

    def test_both_exact_extensionless_launchers_are_selected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            init_repository(root)
            for name in ("handoffctl", "awq"):
                launcher = root / "tools" / name
                launcher.parent.mkdir(exist_ok=True)
                launcher.write_text(
                    f"#!/bin/sh\n# {checker.COPYRIGHT}\n# {checker.SPDX}\n", encoding="utf-8"
                )
            lookalike = root / "nested" / "tools" / "awq"
            lookalike.parent.mkdir(parents=True)
            lookalike.write_text("#!/bin/sh\n", encoding="utf-8")
            subprocess.run(["git", "add", "."], cwd=root, check=True)
            self.assertEqual(
                set(checker.tracked_source_files(root)),
                {Path("tools/handoffctl"), Path("tools/awq")},
            )

    def test_main_reports_success_violation_and_git_failure(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            init_repository(root)
            source = root / "ok.py"
            source.write_text(f"# {checker.COPYRIGHT}\n# {checker.SPDX}\n", encoding="utf-8")
            subprocess.run(["git", "add", "."], cwd=root, check=True)
            stdout = io.StringIO()
            with contextlib.redirect_stdout(stdout):
                self.assertEqual(checker.main(["--root", str(root)]), 0)
            self.assertIn("1 tracked source files", stdout.getvalue())
            source.write_text("pass\n", encoding="utf-8")
            stderr = io.StringIO()
            with contextlib.redirect_stderr(stderr):
                self.assertEqual(checker.main(["--root", str(root)]), 1)
            self.assertIn("expected exact Huawei/MIT header", stderr.getvalue())
        with tempfile.TemporaryDirectory() as directory:
            stderr = io.StringIO()
            with contextlib.redirect_stderr(stderr):
                self.assertEqual(checker.main(["--root", directory]), 2)
            self.assertIn("git ls-files failed", stderr.getvalue())

    def test_non_utf8_tracked_path_fails_closed(self) -> None:
        result = subprocess.CompletedProcess([], 0, b"\xff\0", b"")
        with (
            patch.object(checker.subprocess, "run", return_value=result),
            self.assertRaisesRegex(checker.HeaderCheckError, "tracked path is not valid UTF-8"),
        ):
            checker.tracked_source_files(Path())


if __name__ == "__main__":
    unittest.main()
