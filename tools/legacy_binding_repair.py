# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Fail-closed repair for stale partial legacy task bindings."""

from typing import Any


def repair(args: Any, meta: dict[str, Any]) -> str:
    """Clear one exact stale worktree key without reopening completed history."""
    if args.expected_revision != meta["task_revision"]:
        raise RuntimeError(
            f"stale revision: expected {args.expected_revision}, current {meta['task_revision']}"
        )
    if meta.get("status") not in {"open", "done"} or meta.get("owner") or meta.get("claim_expires"):
        raise RuntimeError("repair-legacy-binding requires an inactive, unowned task")
    if meta.get("status") == "open" and meta.get("branch"):
        raise RuntimeError("repair-legacy-binding requires an empty legacy branch")
    if meta.get("worktree_key") != args.worktree_key:
        raise RuntimeError("repair-legacy-binding worktree key does not match retained metadata")
    if not args.note.strip():
        raise RuntimeError("repair-legacy-binding note must not be empty")
    meta["worktree_key"] = ""
    return str(args.note)
