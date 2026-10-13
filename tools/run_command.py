# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Wrapped command completion and durable retry-circuit recording."""

from __future__ import annotations

import argparse
from typing import Any


def cmd_run(runtime: Any, args: argparse.Namespace) -> int:  # noqa: C901
    """Execute one fenced command, then durably record its result and retry state."""
    if not args.command:
        raise RuntimeError("missing command")
    (
        policy,
        command_hash,
        timeout,
        timed_out,
        returncode,
        execution_id,
        execution_revision,
    ) = runtime._cmd_run_fenced(args)
    if execution_id is not None:
        result = argparse.Namespace(
            task=args.task,
            owner=args.owner,
            expected_revision=execution_revision,
            execution_id=execution_id,
            classification="SUBPROCESS_TIMEOUT" if timed_out else "EXIT",
            returncode=returncode,
            recorded_at=runtime.now(),
        )
        runtime.mutate(result, "execution-result", policy)
        _, recorded, _ = runtime.locate(args.task)
        execution_revision = int(recorded["task_revision"])
    if hasattr(args, "retry_circuit_reservation"):
        resolution_revision = getattr(args, "retry_circuit_resolution_revision", None)
        if type(resolution_revision) is not int:
            raise RuntimeError("retry circuit reservation is missing its resolution revision")
        args.expected_revision = resolution_revision
        args.retry_circuit_failure = (
            ("SUBPROCESS_TIMEOUT" if timed_out else "RETRYABLE" if returncode == 75 else "EXIT")
            if returncode
            else None
        )
        runtime.mutate(args, "retry-circuit-resolve", policy)
        _, current, _ = runtime.locate(args.task)
        execution_revision = int(current["task_revision"])
    if hasattr(args, "autonomy_limits_policy"):
        _, current, _ = runtime.locate(args.task)
        args.expected_revision = int(current["task_revision"])
        args.autonomy_returncode = returncode
        args.autonomy_diff_bytes = runtime.al.diff_bytes(runtime.ROOT)
        args._autonomy_limits_phase = "record"
        runtime.mutate(args, "autonomy-limits-record", policy)
        _, current, _ = runtime.locate(args.task)
        execution_revision = int(current["task_revision"])
    try:
        runtime.append_command_result(args.task, args.owner, command_hash, returncode, timed_out)
    except Exception as error:
        # Unbound runs resolve their slot first, so an append failure cannot
        # strand capacity after a command has already exited. Bound runs retain
        # their established execution-result/journal/finish sequence.
        if execution_id is not None:
            raise RuntimeError(
                "EXECUTION_RESULT_UNKNOWN: command result could not be journaled"
            ) from error
        raise
    note = (
        f"Recorded command timeout; classification=SUBPROCESS_TIMEOUT; "
        f"deadline={timeout:.1f}s; command argv SHA-256 {command_hash}."
        if timed_out
        else f"Recorded command exit {returncode}; command argv SHA-256 {command_hash}."
    )
    update = argparse.Namespace(
        task=args.task,
        owner=args.owner,
        expected_revision=execution_revision,
        status=None,
        priority=None,
        summary=None,
        next_action=None,
        note=note,
        _session_trigger="run",
    )
    if execution_id is not None:
        update.execution_id = execution_id
        runtime.mutate(update, "execution-finish", policy)
    else:
        runtime.mutate(update, "update", policy)
    sqlite = runtime.backend_selection()["backend"] == "sqlite"
    try:
        runtime.require_policy_unchanged(runtime.ROOT, policy)
        runtime.reconcile(do_commit=not sqlite, push=not sqlite, policy=policy)
    except Exception as error:
        raise runtime.PostCommandReconcileError(
            "COMMAND_RECORDED_POST_RECONCILE_FAILED: "
            f"task={args.task}; argv_sha256={command_hash}; {error}"
        ) from error
    return int(returncode)
