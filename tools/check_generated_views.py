#!/usr/bin/env python3
# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Verify every checked-in task-derived projection from one task snapshot."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools import handoffctl  # noqa: E402


def main() -> int:
    tasks = handoffctl.all_tasks()
    errors: list[str] = []
    current = handoffctl.ROOT / "CURRENT.md"
    if not current.exists() or current.read_text() != handoffctl.render_current(tasks):
        errors.append("CURRENT.md differs from generated tasks")
    if handoffctl.project_settings()["status_view"]:
        errors.extend(handoffctl.status_projection_errors(handoffctl.render_status_views(tasks)))
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("generated task views are current")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
