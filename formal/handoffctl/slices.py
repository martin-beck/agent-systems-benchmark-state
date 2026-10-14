# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Canonical source generation for full TLC operation slices."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

OPERATIONS = (
    "promote",
    "resume",
    "unblock",
    "pause",
    "claim",
    "heartbeat",
    "update",
    "accept",
    "bind-spec",
    "bind-worktree",
    "bind-envelope",
    "recover_expired",
    "recover-execution",
    "abandon-execution",
    "change-drift",
    "assumption",
    "release_planned",
    "release_open",
    "release_blocked",
    "release_done",
)


INIT_OPERATION_DOMAIN = "    /\\ operation \\in [Processes -> Operations]"


def module_name(operation: str) -> str:
    """Return a TLA+-legal, collision-free module name for an operation slice."""
    if operation not in OPERATIONS:
        raise ValueError(f"unknown operation slice: {operation}")
    return "HandoffctlSlice" + "".join(part.capitalize() for part in operation.split("-"))


def render_source(base: str, operation: str) -> str:
    """Render a source-literal p1 constraint that TLC can enumerate."""
    if operation not in OPERATIONS:
        raise ValueError(f"unknown operation slice: {operation}")
    if base.count(INIT_OPERATION_DOMAIN) != 2:
        raise ValueError("base source must contain Init and TypeOK operation domains")
    result = base.replace(
        INIT_OPERATION_DOMAIN,
        f'{INIT_OPERATION_DOMAIN}\n    /\\ operation["p1"] \\in {{"{operation}"}}',
        1,
    )
    result, count = re.subn(
        r"^-+ MODULE Handoffctl -+$",
        lambda _match: f"{'-' * 28} MODULE {module_name(operation)} {'-' * 28}",
        result,
        flags=re.MULTILINE,
    )
    if count != 1:
        raise ValueError("base source must contain exactly one Handoffctl module header")
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-source", type=Path, required=True)
    parser.add_argument("--operation", choices=OPERATIONS, required=True)
    parser.add_argument("--output-source", type=Path, required=True)
    args = parser.parse_args()
    base = args.base_source.read_text(encoding="utf-8")
    args.output_source.write_text(render_source(base, args.operation), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
