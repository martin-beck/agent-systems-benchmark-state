# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Narrow admission policy for lifecycle mutation validation."""

from __future__ import annotations

from pathlib import Path
from typing import Any

try:
    from .task_spec import EvidencePolicy, task_spec_errors
except ImportError:  # pragma: no cover - direct vendored execution
    from task_spec import (  # type: ignore[import-not-found,no-redef]
        EvidencePolicy,
        task_spec_errors,
    )


def task_errors(
    root: Path,
    meta: dict[str, Any],
    policy: EvidencePolicy | None,
    *,
    include_ledger: bool = True,
) -> list[str]:
    """Validate task-spec metadata, optionally omitting historical ledger replay."""
    return task_spec_errors(root, meta, policy, include_ledger=include_ledger)
