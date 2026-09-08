# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Verify exact headers on every tracked Agent Systems Benchmark State source."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

COPYRIGHT = "Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved."
SPDX = "SPDX-License-Identifier: MIT"
TLA_MODULE_DECLARATION = re.compile(r"^-{4,} MODULE ([A-Za-z_][A-Za-z0-9_]*) -{4,}$")
COMMENT_PREFIXES = {".py": "# ", ".sh": "# ", ".tla": r"\* "}
EXTENSIONLESS_SOURCES = {Path("tools/handoffctl"): "# ", Path("tools/awq"): "# "}


class HeaderCheckError(RuntimeError):
    """Report a repository or source-decoding error."""


def comment_prefix(path: Path) -> str | None:
    """Return the required line-comment prefix for a tracked source path."""
    return EXTENSIONLESS_SOURCES.get(path, COMMENT_PREFIXES.get(path.suffix))


def tracked_source_files(root: Path) -> tuple[Path, ...]:
    """Return NUL-safely selected source files from Git's tracked set."""
    result = subprocess.run(["git", "ls-files", "-z"], cwd=root, check=False, capture_output=True)
    if result.returncode != 0:
        detail = result.stderr.decode("utf-8", errors="replace").strip()
        raise HeaderCheckError(f"git ls-files failed: {detail}")
    paths: list[Path] = []
    for raw in result.stdout.split(b"\0"):
        if not raw:
            continue
        try:
            path = Path(raw.decode("utf-8"))
        except UnicodeDecodeError as error:
            raise HeaderCheckError(f"tracked path is not valid UTF-8: {error}") from error
        if comment_prefix(path) is not None:
            paths.append(path)
    return tuple(paths)


def check_file(root: Path, path: Path) -> list[str]:
    """Return exact-header violations for one selected source file."""
    prefix = comment_prefix(path)
    if prefix is None:
        raise HeaderCheckError(f"unsupported source path: {path}")
    try:
        lines = (root / path).read_text(encoding="utf-8").splitlines()
    except UnicodeDecodeError as error:
        return [f"{path}: source is not valid UTF-8: {error}"]
    except OSError as error:
        return [f"{path}: cannot read source: {error}"]
    is_tla = path.suffix == ".tla"
    start = 1 if is_tla or (lines and lines[0].startswith("#!")) else 0
    expected = [prefix + COPYRIGHT, prefix + SPDX]
    issues: list[str] = []
    if is_tla:
        declaration = TLA_MODULE_DECLARATION.fullmatch(lines[0]) if lines else None
        if declaration is None or declaration.group(1) != path.stem:
            issues.append(f"{path}: expected matching TLA+ MODULE declaration at line 1")
    if lines[start : start + 2] != expected:
        issues.append(f"{path}: expected exact Huawei/MIT header at line {start + 1}")
    pair_count = sum(lines[index : index + 2] == expected for index in range(len(lines) - 1))
    if pair_count != 1:
        issues.append(f"{path}: expected exactly one canonical Huawei/MIT header pair")
    return issues


def main(argv: list[str] | None = None) -> int:
    """Check the repository and print actionable violations."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    root = parser.parse_args(argv).root.resolve()
    try:
        sources = tracked_source_files(root)
        issues = [issue for path in sources for issue in check_file(root, path)]
    except HeaderCheckError as error:
        print(f"header check failed: {error}", file=sys.stderr)
        return 2
    if issues:
        print("\n".join(issues), file=sys.stderr)
        return 1
    print(f"Verified Huawei/MIT headers in {len(sources)} tracked source files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
