# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Fail-closed repair for stale partial legacy task bindings."""

from typing import Any


def repair(args: Any, meta: dict[str, Any]) -> str:
    """Clear one exact stale branch/worktree pair without reopening history."""
    if args.expected_revision != meta["task_revision"]:
        raise RuntimeError(
            f"stale revision: expected {args.expected_revision}, current {meta['task_revision']}"
        )
    if meta.get("status") not in {"open", "done"} or meta.get("owner") or meta.get("claim_expires"):
        raise RuntimeError("repair-legacy-binding requires an inactive, unowned task")
    expected_branch = getattr(args, "expected_branch", "")
    if not isinstance(expected_branch, str) or not expected_branch.strip():
        raise RuntimeError("repair-legacy-binding requires --expected-branch")
    if meta.get("branch") != expected_branch:
        raise RuntimeError("repair-legacy-binding branch does not match retained metadata")
    if meta.get("worktree_key") != args.worktree_key:
        raise RuntimeError("repair-legacy-binding worktree key does not match retained metadata")
    if not args.note.strip():
        raise RuntimeError("repair-legacy-binding note must not be empty")
    meta["worktree_key"] = ""
    return str(args.note)
