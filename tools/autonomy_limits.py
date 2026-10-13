# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Tracked autonomy budgets with diagnostic, revision-fenced local holds."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import stat
import subprocess
from pathlib import Path
from typing import Any, cast

type Meta = dict[str, Any]

POLICY_NAME = "autonomy-limits-policy.json"
MAX_BYTES = 4096
LIMITS = frozenset(
    {
        "max_elapsed_seconds",
        "max_retries",
        "max_commands",
        "max_diff_bytes",
        "max_cost_units",
        "max_external_side_effects",
    }
)
TRIGGERS = frozenset(
    {"elapsed-time", "retry", "command", "diff-size", "cost", "external-side-effect"}
)


class PolicyError(RuntimeError):
    """The optional project policy is unsafe, malformed, or changed."""


def _canonical(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def _timestamp(value: object) -> dt.datetime:
    if not isinstance(value, str):
        raise ValueError("autonomy limit timestamp is invalid")
    try:
        parsed = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as error:
        raise ValueError("autonomy limit timestamp is invalid") from error
    if parsed.tzinfo is None:
        raise ValueError("autonomy limit timestamp is invalid")
    return parsed.astimezone(dt.UTC)


def _tracked(root: Path, payload: bytes) -> bool:
    """Require one ordinary policy file to equal a clean HEAD blob."""
    try:
        commands = (
            ["/usr/bin/git", "-C", str(root), "show", f"HEAD:{POLICY_NAME}"],
            ["/usr/bin/git", "-C", str(root), "diff", "--quiet", "--", POLICY_NAME],
            ["/usr/bin/git", "-C", str(root), "diff", "--cached", "--quiet", "--", POLICY_NAME],
        )
        shown = subprocess.run(  # noqa: S603 - fixed Git executable and bounded policy name
            commands[0],
            check=False,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            timeout=10,
        )
        return (
            shown.returncode == 0
            and shown.stdout == payload
            and all(
                subprocess.run(  # noqa: S603 - fixed Git executable and bounded policy name
                    command,
                    check=False,
                    stdin=subprocess.DEVNULL,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    timeout=10,
                ).returncode
                == 0
                for command in commands[1:]
            )
        )
    except (OSError, subprocess.SubprocessError):
        return False


def _head_tracks(root: Path) -> bool:
    try:
        return (
            subprocess.run(  # noqa: S603 - fixed Git executable and bounded policy name
                ["/usr/bin/git", "-C", str(root), "cat-file", "-e", f"HEAD:{POLICY_NAME}"],
                check=False,
                stdin=subprocess.DEVNULL,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                timeout=10,
            ).returncode
            == 0
        )
    except (OSError, subprocess.SubprocessError):
        return False


def policy(root: Path) -> Meta | None:
    """Load the bounded opt-in policy, refusing mutable or non-regular input."""
    path = root / POLICY_NAME
    if not path.exists():
        if _head_tracks(root):
            raise PolicyError("autonomy limits policy must be tracked and unchanged")
        return None
    try:
        found = path.lstat()
        if (
            not stat.S_ISREG(found.st_mode)
            or found.st_nlink != 1
            or found.st_uid != os.geteuid()
            or stat.S_IMODE(found.st_mode) & 0o002
            or not 2 <= found.st_size <= MAX_BYTES
        ):
            raise PolicyError("autonomy limits policy has unsafe identity or size")
        payload = path.read_bytes()
    except OSError as error:
        raise PolicyError("autonomy limits policy is unreadable") from error
    if len(payload) != found.st_size or not _tracked(root, payload):
        raise PolicyError("autonomy limits policy must be tracked and unchanged")
    try:
        value = json.loads(payload.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise PolicyError("autonomy limits policy is not valid UTF-8 JSON") from error
    if not isinstance(value, dict) or value.get("schema_version") != 1:
        raise PolicyError("autonomy limits policy shape or version is invalid")
    values = set(value) - {"schema_version"}
    if (
        not values
        or not values <= LIMITS
        or any(
            type(value[name]) is not int or value[name] < 0 or value[name] > 1_000_000_000
            for name in values
        )
    ):
        raise PolicyError("autonomy limits policy budgets are invalid")
    value["digest"] = "sha256:" + hashlib.sha256(payload).hexdigest()
    return value


def require_unchanged(root: Path, expected: Meta | None) -> None:
    if policy(root) != expected:
        raise PolicyError("autonomy limits policy changed during operation")


def diff_bytes(root: Path) -> int:
    """Measure local diff bytes without retaining source text or paths."""
    process = subprocess.Popen(  # noqa: S603 - fixed Git executable and bound repository root
        ["/usr/bin/git", "-C", str(root), "diff", "--no-ext-diff", "--binary"],
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
    )
    if process.stdout is None:  # pragma: no cover - PIPE is supplied above.
        process.kill()
        raise RuntimeError("cannot measure autonomy diff budget")
    total = 0
    with process.stdout:
        while chunk := process.stdout.read(65536):
            total += len(chunk)
    if process.wait(timeout=10) != 0:
        raise RuntimeError("cannot measure autonomy diff budget")
    return total


def prepare(runtime: Any, args: argparse.Namespace, evidence_policy: object) -> None:
    """Fence one opt-in policy and persist any pre-effect budget hold."""
    try:
        selected = policy(runtime.ROOT)
    except PolicyError as error:
        raise RuntimeError(f"run preflight failed: {error}") from error
    if selected is None:
        return
    _, current, _ = runtime.locate(args.task)
    args.expected_revision = int(current["task_revision"])
    args.autonomy_limits_policy = selected
    args.autonomy_diff_bytes = diff_bytes(runtime.ROOT)
    args._autonomy_limits_phase = "preflight"
    runtime.mutate(args, "autonomy-limits-preflight", evidence_policy)
    require_unchanged(runtime.ROOT, selected)
    if getattr(args, "autonomy_limit_held", False):
        raise RuntimeError("AUTONOMY_LIMIT_HOLD: explicit autonomy-limits dispose is required")


def metadata_error(meta: Meta) -> str | None:
    value = meta.get("autonomy_limits")
    if value is None:
        return None
    if not isinstance(value, dict) or set(value) != {
        "schema_version",
        "policy_digest",
        "started_at",
        "commands",
        "retries",
        "cost_units",
        "external_side_effects",
        "hold",
        "dispositions",
    }:
        return "autonomy limits fields are invalid"
    if value.get("schema_version") != 1 or not re.fullmatch(
        r"sha256:[0-9a-f]{64}", str(value.get("policy_digest", ""))
    ):
        return "autonomy limits identity is invalid"
    try:
        _timestamp(value.get("started_at"))
    except ValueError:
        return "autonomy limits start is invalid"
    if (
        any(
            type(value.get(name)) is not int or value[name] < 0
            for name in ("commands", "retries", "cost_units", "external_side_effects")
        )
        or not isinstance(value.get("dispositions"), list)
        or len(value["dispositions"]) > 32
    ):
        return "autonomy limits counters are invalid"
    hold = value.get("hold")
    if hold is not None and (
        not isinstance(hold, dict)
        or set(hold) != {"trigger", "observed", "limit", "held_at", "task_revision"}
        or hold.get("trigger") not in TRIGGERS
        or type(hold.get("observed")) is not int
        or type(hold.get("limit")) is not int
        or type(hold.get("task_revision")) is not int
        or hold["task_revision"] != meta.get("task_revision")
    ):
        return "autonomy limits hold is invalid"
    if any(
        not isinstance(item, dict)
        or set(item) != {"held_revision", "task_revision", "reason", "recorded_at"}
        or type(item.get("held_revision")) is not int
        or type(item.get("task_revision")) is not int
        or not isinstance(item.get("reason"), str)
        or not item["reason"].strip()
        or len(item["reason"]) > 500
        or "\n" in item["reason"]
        for item in value["dispositions"]
    ):
        return "autonomy limits disposition is invalid"
    return None


def _state(meta: Meta, selected: Meta, at: str) -> Meta:
    value = meta.get("autonomy_limits")
    if value is None:
        value = {
            "schema_version": 1,
            "policy_digest": selected["digest"],
            "started_at": at,
            "commands": 0,
            "retries": 0,
            "cost_units": 0,
            "external_side_effects": 0,
            "hold": None,
            "dispositions": [],
        }
        meta["autonomy_limits"] = value
    if metadata_error(meta) or value["policy_digest"] != selected["digest"]:
        raise RuntimeError("AUTONOMY_LIMIT_POLICY_MISMATCH: durable policy identity is invalid")
    return value


def _breach(state: Meta, selected: Meta, at: str, diff_bytes: int) -> tuple[str, int, int] | None:
    elapsed = int((_timestamp(at) - _timestamp(state["started_at"])).total_seconds())
    observed = {
        "elapsed-time": elapsed,
        "retry": state["retries"],
        "command": state["commands"],
        "diff-size": diff_bytes,
        "cost": state["cost_units"],
        "external-side-effect": state["external_side_effects"],
    }
    names = {
        "elapsed-time": "max_elapsed_seconds",
        "retry": "max_retries",
        "command": "max_commands",
        "diff-size": "max_diff_bytes",
        "cost": "max_cost_units",
        "external-side-effect": "max_external_side_effects",
    }
    return next(
        (
            (trigger, observed[trigger], selected[name])
            for trigger, name in names.items()
            if name in selected and observed[trigger] >= selected[name]
        ),
        None,
    )


def apply_preflight(args: argparse.Namespace, meta: Meta, selected: Meta | None, at: str) -> str:
    """Start a ledger or persist a no-effect hold before command execution."""
    if selected is None:
        return ""
    state = _state(meta, selected, at)
    if state["hold"] is not None:
        raise RuntimeError("AUTONOMY_LIMIT_HOLD: explicit autonomy-limits dispose is required")
    diff_bytes = int(getattr(args, "autonomy_diff_bytes", 0))
    breach = _breach(state, selected, at, diff_bytes)
    if breach is None:
        return "Autonomy limits admitted."
    trigger, observed, limit = breach
    state["hold"] = {
        "trigger": trigger,
        "observed": observed,
        "limit": limit,
        "held_at": at,
        "task_revision": int(meta["task_revision"]) + 1,
    }
    args.autonomy_limit_held = True
    return f"Autonomy limit hold recorded: {trigger} observed={observed} limit={limit}."


def apply_record(args: argparse.Namespace, meta: Meta, selected: Meta | None, at: str) -> str:
    """Record one completed command and convert any overrun into a diagnostic hold."""
    if selected is None:
        return ""
    state = _state(meta, selected, at)
    if type(getattr(args, "cost_units", 0)) is not int or getattr(args, "cost_units", 0) < 0:
        raise RuntimeError("autonomy limits cost units are invalid")
    state["commands"] += 1
    state["retries"] += int(getattr(args, "autonomy_returncode", 0) != 0)
    state["cost_units"] += int(getattr(args, "cost_units", 0))
    state["external_side_effects"] += int(
        bool(getattr(args, "external_side_effect", False))
        or getattr(args, "command_class", None) == "git-publication"
    )
    breach = _breach(state, selected, at, int(getattr(args, "autonomy_diff_bytes", 0)))
    if breach is not None and state["hold"] is None:
        trigger, observed, limit = breach
        state["hold"] = {
            "trigger": trigger,
            "observed": observed,
            "limit": limit,
            "held_at": at,
            "task_revision": int(meta["task_revision"]) + 1,
        }
        return f"Autonomy limit hold recorded: {trigger} observed={observed} limit={limit}."
    return "Autonomy limits recorded."


def apply_dispose(args: argparse.Namespace, meta: Meta, at: str) -> str:
    if meta.get("owner") != args.owner or meta.get("status") != "in_progress":
        raise RuntimeError("autonomy limits disposition requires the active task owner")
    if args.expected_revision != meta.get("task_revision"):
        raise RuntimeError(
            f"stale revision: expected {args.expected_revision}, current {meta['task_revision']}"
        )
    state = meta.get("autonomy_limits")
    if (
        metadata_error(meta)
        or not isinstance(state, dict)
        or not isinstance(state.get("hold"), dict)
    ):
        raise RuntimeError("autonomy limits disposition requires a current diagnostic hold")
    hold = state["hold"]
    if hold["task_revision"] != meta["task_revision"]:
        raise RuntimeError("autonomy limits hold is not fenced to the current revision")
    reason = str(args.reason).strip()
    if not reason or len(reason) > 500 or "\n" in reason:
        raise RuntimeError("autonomy limits disposition reason is invalid")
    state["dispositions"] = [
        *state["dispositions"],
        {
            "held_revision": hold["task_revision"],
            "task_revision": int(meta["task_revision"]) + 1,
            "reason": reason,
            "recorded_at": at,
        },
    ][-32:]
    state["hold"] = None
    return "Recorded local autonomy-limit disposition."


def next_revision_projection(meta: Meta) -> Meta:
    """Return the task shape after SQLite atomically advances its revision."""
    projected = cast(Meta, json.loads(json.dumps(meta)))
    projected["task_revision"] = int(meta["task_revision"]) + 1
    return projected


def carry_run_hold(args: argparse.Namespace, kind: str, meta: Meta) -> None:
    """Fence a run-created hold to its final durable receipt revision."""
    state = meta.get("autonomy_limits")
    if (
        kind == "update"
        and getattr(args, "_session_trigger", None) == "run"
        and isinstance(state, dict)
        and isinstance(state.get("hold"), dict)
    ):
        state["hold"]["task_revision"] = int(meta["task_revision"]) + 1


def preflight(admit: Any, args: argparse.Namespace, meta: Meta, at: str) -> str:
    admit(args, meta)
    return apply_preflight(args, meta, args.autonomy_limits_policy, at)


def record(admit: Any, args: argparse.Namespace, meta: Meta, at: str) -> str:
    admit(args, meta)
    return apply_record(args, meta, args.autonomy_limits_policy, at)


def transition(admit: Any, args: argparse.Namespace, meta: Meta, at: str) -> str:
    if args.cmd == "autonomy-limits":
        return apply_dispose(args, meta, at)
    return (
        preflight(admit, args, meta, at)
        if args._autonomy_limits_phase == "preflight"
        else record(admit, args, meta, at)
    )


def dispatch(runtime: Any, args: argparse.Namespace) -> int:
    if args.autonomy_limits_action == "status":
        _, meta, _ = runtime.locate(args.task)
        print(json.dumps(meta.get("autonomy_limits") or {}, sort_keys=True, separators=(",", ":")))
        return 0
    runtime.dispatch_lifecycle_mutation(args)
    return 0


def add_command_parser(commands: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    item = commands.add_parser("autonomy-limits")
    nested = item.add_subparsers(dest="autonomy_limits_action", required=True)
    status = nested.add_parser("status")
    status.add_argument("task")
    dispose = nested.add_parser("dispose")
    dispose.add_argument("task")
    dispose.add_argument("--owner", required=True)
    dispose.add_argument("--expected-revision", type=int, required=True)
    dispose.add_argument("--reason", required=True)


def add_run_arguments(item: argparse.ArgumentParser) -> None:
    item.add_argument("--cost-units", type=int, default=0)
    item.add_argument("--external-side-effect", action="store_true")
