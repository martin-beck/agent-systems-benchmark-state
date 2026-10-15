# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Fail-closed repair for stale partial legacy task bindings."""

from typing import Any


_EXPECTED = {
    "AR-1891": ("codex/ar-1891-recovery", "asb-ar1891-recovery-20261014"),
    "AR-1935": (
        "codex/ar1933-credential-handoff",
        "agent-workflow-coordinator-ar1933-credential-handoff",
    ),
}


def repair(args: Any, meta: dict[str, Any]) -> str:
    """Clear one of the two explicitly retained stale bindings."""
    expected = _EXPECTED.get(meta.get("id"))
    if expected is None or args.task != meta.get("id"):
        raise RuntimeError("repair-legacy-binding target is outside the approved stale bindings")
    if args.expected_revision != meta["task_revision"]:
        raise RuntimeError(
            f"stale revision: expected {args.expected_revision}, current {meta['task_revision']}"
        )
    if meta.get("status") != "blocked" or meta.get("owner") or meta.get("claim_expires"):
        raise RuntimeError("repair-legacy-binding requires an inactive, unowned task")
    if (args.branch, args.worktree_key) != expected:
        raise RuntimeError("repair-legacy-binding request is not the approved retained binding")
    if (meta.get("branch"), meta.get("worktree_key")) != expected:
        raise RuntimeError("repair-legacy-binding worktree key does not match retained metadata")
    note = args.note.strip()
    if not note or len(note) > 512 or any(ord(char) < 32 for char in note):
        raise RuntimeError("repair-legacy-binding evidence must be nonempty and at most 512 characters")
    meta["branch"] = ""
    meta["worktree_key"] = ""
    return note
