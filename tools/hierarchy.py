# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Validation and rollup admission for hierarchical task edges."""

from __future__ import annotations

import re
from collections.abc import Sequence
from pathlib import Path
from typing import Any

Meta = dict[str, Any]
Task = tuple[Path, Meta, str]
TASK_RE = re.compile(r"AR-[0-9]{4}\Z")
TERMINAL_CHILD_STATUSES = frozenset({"done", "cancelled", "superseded"})


def _task_id(value: object) -> bool:
    return isinstance(value, str) and bool(TASK_RE.fullmatch(value))


def _children(meta: Meta) -> tuple[list[str], list[str]]:
    value = meta.get("children", [])
    if not isinstance(value, list):
        return [], ["children must be a list of AR identifiers"]
    if any(not _task_id(item) for item in value):
        return [], ["children must be a list of AR identifiers"]
    children = [str(item) for item in value]
    duplicates = sorted({item for item in children if children.count(item) > 1})
    if duplicates:
        return children, [f"duplicate child {item}" for item in duplicates]
    if str(meta.get("id", "")) in children:
        return children, ["task cannot be its own child"]
    return children, []


def hierarchy_errors(tasks: Sequence[Task]) -> list[str]:  # noqa: C901
    """Return deterministic errors for parent/children edges and cycles."""
    by_id = {str(meta.get("id", "")): meta for _, meta, _ in tasks}
    errors: list[str] = []
    parents: dict[str, str] = {}
    children_by_parent: dict[str, list[str]] = {}
    for _, meta, _ in tasks:
        task_id = str(meta.get("id", ""))
        parent = meta.get("parent_task_ref", "")
        if parent and not _task_id(parent):
            errors.append(f"{task_id}: invalid parent_task_ref")
        elif parent:
            parents[task_id] = str(parent)
            if str(parent) == task_id:
                errors.append(f"{task_id}: parent_task_ref self reference")
            elif str(parent) not in by_id:
                errors.append(f"{task_id}: missing parent task {parent}")
        children, child_errors = _children(meta)
        errors.extend(f"{task_id}: {error}" for error in child_errors)
        children_by_parent[task_id] = children
        for child in children:
            if child not in by_id:
                errors.append(f"{task_id}: missing child task {child}")
            elif str(by_id[child].get("parent_task_ref", "")) != task_id:
                errors.append(f"{task_id}: child {child} does not point back to parent")
    for child, parent in parents.items():
        if child not in children_by_parent.get(parent, []):
            errors.append(f"{child}: parent {parent} does not list child")
    for task_id in sorted(by_id):
        seen: set[str] = set()
        current = task_id
        while current in parents:
            if current in seen:
                errors.append(f"hierarchy cycle involving {task_id}")
                break
            seen.add(current)
            current = parents[current]
    return sorted(set(errors))


def open_child_error(meta: Meta, tasks: Sequence[Task]) -> str | None:
    """Return the rollup admission error for a parent becoming done."""
    if meta.get("status") != "in_progress":
        return None
    children = [
        str(candidate.get("id", ""))
        for _, candidate, _ in tasks
        if str(candidate.get("parent_task_ref", "")) == str(meta.get("id", ""))
        and candidate.get("status") not in TERMINAL_CHILD_STATUSES
    ]
    if children:
        return f"{meta['id']}: cannot complete with open children: {', '.join(sorted(children))}"
    return None
