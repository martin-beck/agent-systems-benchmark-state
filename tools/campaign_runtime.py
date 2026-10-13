# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Artifact-free runtime routing for campaign projections."""

from __future__ import annotations

from typing import Any

if __package__:
    from . import campaign, resume_card_runtime
else:  # pragma: no cover - direct handoffctl execution
    import campaign  # type: ignore[import-not-found,no-redef]
    import resume_card_runtime  # type: ignore[import-not-found,no-redef]


def dispatch(args: Any, coordinator: Any) -> int:
    """Validate and render a portable campaign from one read-only snapshot."""

    def render() -> str:
        policy = coordinator.evidence_policy(coordinator.ROOT)
        tasks = coordinator.all_tasks()
        sessions = coordinator.storage_backend().load_session_records()
        errors = campaign.projection_errors(
            tasks,
            sessions,
            basic_task_errors=coordinator.basic_task_errors,
            validate_session_record=coordinator.validate_session_record,
            private_text_errors=coordinator.private_text_errors,
            graph_errors=coordinator.graph_errors,
            hierarchy_errors=coordinator.hierarchy_errors,
            supersession_errors=coordinator.supersession_errors,
            policy=policy,
        )
        if errors:
            raise RuntimeError("campaign snapshot validation failed:\n" + "\n".join(errors))
        observed_at = getattr(args, "observed_at", None) or campaign.current_observed_at()
        return campaign.command(tasks, sessions, args.json, observed_at)

    print(
        resume_card_runtime.read_only_snapshot(
            render,
            coordinator.coordinator_lock_path,
            coordinator.LOCK_TIMEOUT_SECONDS,
            coordinator.LOCK_POLL_SECONDS,
            coordinator.LockTimeoutError,
        ),
        end="",
    )
    return 0
