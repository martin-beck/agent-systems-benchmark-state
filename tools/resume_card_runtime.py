# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Read-only snapshot and routing support for resume-card observations."""

from __future__ import annotations

import fcntl
import os
import time
from collections.abc import Callable
from pathlib import Path
from typing import Any, cast

type Meta = dict[str, Any]
type Task = tuple[Path, Meta, str]


def read_only_snapshot(
    callback: Callable[[], str],
    coordinator_lock_path: Callable[[], Path],
    timeout_seconds: float,
    poll_seconds: float,
    timeout_error: type[Exception],
) -> str:
    """Read a linearizable snapshot without creating lock or trace artifacts."""
    lock_path = coordinator_lock_path()
    for _ in range(2):
        try:
            descriptor = os.open(lock_path, os.O_RDONLY)
        except FileNotFoundError:
            result = callback()
            if not lock_path.exists():
                return result
            continue
        try:
            deadline = time.monotonic() + timeout_seconds
            while True:
                try:
                    fcntl.flock(descriptor, fcntl.LOCK_SH | fcntl.LOCK_NB)
                    break
                except BlockingIOError as error:
                    remaining = deadline - time.monotonic()
                    if remaining <= 0:
                        raise timeout_error(
                            f"LOCK_TIMEOUT after {timeout_seconds:.1f}s acquiring "
                            "shared resume-card snapshot lock"
                        ) from error
                    time.sleep(min(poll_seconds, remaining))
            return callback()
        finally:
            fcntl.flock(descriptor, fcntl.LOCK_UN)
            os.close(descriptor)
    raise RuntimeError("resume-card authority snapshot changed while being read")


def snapshot_errors(
    tasks: list[Task],
    policy: Any,
    *,
    basic_task_errors: Callable[[Path, Meta, Any], list[str]],
    projection_errors: Callable[[Path, Meta, str, Callable[[Path, str], list[str]]], list[str]],
    private_text_errors: Callable[[Path, str], list[str]],
    evidence_errors: Callable[[Meta, frozenset[str]], object],
    graph_errors: Callable[[list[Task]], list[str]],
    hierarchy_errors: Callable[[list[Task]], list[str]],
    supersession_errors: Callable[[list[Task]], list[str]],
) -> list[str]:
    """Validate every authority value that a resume card could project."""
    errors: list[str] = []
    ids: set[str] = set()
    for path, meta, body in tasks:
        task_id = str(meta.get("id", ""))
        if task_id in ids:
            errors.append(f"duplicate {task_id}")
        ids.add(task_id)
        errors.extend(basic_task_errors(path, meta, policy))
        errors.extend(projection_errors(path, meta, body, private_text_errors))
        try:
            evidence_errors(meta, policy.classes)
        except ValueError as error:
            errors.append(f"{task_id}: {error}")
    errors.extend(graph_errors(tasks))
    errors.extend(hierarchy_errors(tasks))
    errors.extend(supersession_errors(tasks))
    return sorted(set(errors))


def dispatch(args: Any, coordinator: Any) -> int:
    """Render a validated card from one artifact-free read-only snapshot."""

    def render() -> str:
        policy = coordinator.evidence_policy(coordinator.ROOT)
        tasks = coordinator.all_tasks()
        errors = snapshot_errors(
            tasks,
            policy,
            basic_task_errors=coordinator.basic_task_errors,
            projection_errors=coordinator.resume_card.projection_errors,
            private_text_errors=coordinator.private_text_errors,
            evidence_errors=coordinator.resume_card._evidence,
            graph_errors=coordinator.graph_errors,
            hierarchy_errors=coordinator.hierarchy_errors,
            supersession_errors=coordinator.supersession_errors,
        )
        if errors:
            raise RuntimeError("resume-card snapshot validation failed:\n" + "\n".join(errors))
        observed_at = (
            getattr(args, "observed_at", None) or coordinator.resume_card.current_observed_at()
        )
        return cast(
            str,
            coordinator.resume_card.command(
                coordinator.ROOT,
                Path(str(coordinator.config().get("projects_root", ""))),
                args.task,
                tasks,
                args.json,
                observed_at,
                policy.classes,
            ),
        )

    print(
        read_only_snapshot(
            render,
            coordinator.coordinator_lock_path,
            coordinator.LOCK_TIMEOUT_SECONDS,
            coordinator.LOCK_POLL_SECONDS,
            coordinator.LockTimeoutError,
        ),
        end="",
    )
    return 0
