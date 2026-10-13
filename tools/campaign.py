# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Portable, read-only campaign views over durable task and session authority."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

if __package__:
    from . import execution_envelope, retry_circuit
else:  # pragma: no cover - direct handoffctl execution
    import execution_envelope  # type: ignore[import-not-found,no-redef]
    import retry_circuit  # type: ignore[import-not-found,no-redef]

type Meta = dict[str, Any]
type Task = tuple[Path, Meta, str]

SCHEMA_VERSION = 1
TERMINAL = frozenset({"done", "cancelled", "superseded"})
MAX_PROJECTED_BYTES = 200_000
ISO_8601_TIMESTAMP = re.compile(
    r"^[0-9]{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12][0-9]|3[01])"
    r"T(?:[01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]"
    r"(?:\.[0-9]{1,9})?(?:Z|[+-](?:0[0-9]|1[0-4]):[0-5][0-9])$"
)


def parse_observed_at(value: str) -> dt.datetime:
    """Parse a reproducible, timezone-aware campaign observation instant."""
    try:
        return _timestamp(value, "observed-at").replace(microsecond=0)
    except ValueError as error:
        raise argparse.ArgumentTypeError("observed-at must be ISO-8601") from error


def current_observed_at() -> dt.datetime:
    """Capture one instant for the complete live campaign observation."""
    return dt.datetime.now(dt.UTC).replace(microsecond=0)


def _timestamp(value: object, field: str) -> dt.datetime:
    if not isinstance(value, str) or not ISO_8601_TIMESTAMP.fullmatch(value):
        raise ValueError(f"{field} is not a timestamp")
    try:
        parsed = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as error:
        raise ValueError(f"{field} is not a timestamp") from error
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ValueError(f"{field} lacks timezone")
    return parsed.astimezone(dt.UTC)


def projection_contract_errors(campaign: Meta) -> list[str]:
    """Check output-only terminal and timestamp invariants before rendering."""
    errors: list[str] = []
    try:
        _timestamp(campaign.get("observed_at"), "observed_at")
    except ValueError as error:
        errors.append(str(error))
    for card in campaign.get("tasks", []):
        errors.extend(_card_contract_errors(card))
    return errors


def _card_contract_errors(card: object) -> list[str]:
    if not isinstance(card, dict):
        return ["campaign card is invalid"]
    task_id = str(card.get("id", "unknown"))
    errors = _terminal_contract_errors(task_id, card)
    errors.extend(_card_timestamp_errors(task_id, card))
    return errors


def _terminal_contract_errors(task_id: str, card: Meta) -> list[str]:
    status, outcome, recovery = card.get("status"), card.get("outcome"), card.get("recovery")
    if status in TERMINAL:
        errors = []
        if not isinstance(outcome, dict) or outcome.get("status") != status:
            errors.append(f"{task_id}: terminal outcome does not match status")
        if recovery != {"kind": "none"}:
            errors.append(f"{task_id}: terminal task has recovery advice")
        return errors
    return [f"{task_id}: nonterminal task has outcome"] if outcome is not None else []


def _card_timestamp_errors(task_id: str, card: Meta) -> list[str]:
    errors: list[str] = []
    values: list[tuple[object, str]] = [(card.get("worker"), "worker")]
    values.extend((attempt, "attempt") for attempt in card.get("attempts", []))
    for value, name in values:
        if isinstance(value, dict):
            errors.extend(_value_timestamp_errors(task_id, name, value))
    return errors


def _value_timestamp_errors(task_id: str, name: str, value: Meta) -> list[str]:
    errors: list[str] = []
    for field in ("claim_expires", "recorded_at"):
        if field in value:
            try:
                _timestamp(value[field], f"{task_id} {name} {field}")
            except ValueError as error:
                errors.append(str(error))
    return errors


def _canonical(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def _task_projection_errors(
    tasks: list[Task], basic_task_errors: Any, private_text_errors: Any, policy: Any
) -> tuple[list[str], dict[str, int]]:
    errors: list[str] = []
    revisions: dict[str, int] = {}
    for path, task, body in tasks:
        task_id = str(task.get("id", path.stem))
        errors.extend(basic_task_errors(path, task, policy))
        text = _canonical(task) + "\n" + body
        if len(text.encode("utf-8")) > MAX_PROJECTED_BYTES:
            errors.append(f"{task_id}: projected authority exceeds 200 KiB")
        errors.extend(private_text_errors(path, text))
        revision = task.get("task_revision")
        if isinstance(revision, int) and not isinstance(revision, bool):
            if task_id in revisions:
                errors.append(f"duplicate task {task_id}")
            revisions[task_id] = revision
    return errors, revisions


def _session_projection_errors(
    tasks: list[Task],
    sessions: list[Meta],
    revisions: dict[str, int],
    validate_session_record: Any,
    private_text_errors: Any,
) -> list[str]:
    errors: list[str] = []
    seen: set[tuple[str, int]] = set()
    for session in sessions:
        try:
            validate_session_record(session)
        except ValueError as error:
            errors.append(f"session: {error}")
            continue
        task_id = str(session["task"])
        revision = int(session["task_revision"])
        key = (task_id, revision)
        if key in seen:
            errors.append(f"duplicate session observation {task_id}@{revision}")
        seen.add(key)
        current = revisions.get(task_id)
        if current is None:
            errors.append(f"session observation has unknown task {task_id}")
        elif revision > current:
            errors.append(f"session observation is ahead of {task_id} authority")
        elif revision == current:
            task = next(meta for _, meta, _ in tasks if str(meta.get("id")) == task_id)
            if session["status"] != task.get("status"):
                errors.append(f"session observation status differs from {task_id} authority")
        text = _canonical(session)
        if len(text.encode("utf-8")) > MAX_PROJECTED_BYTES:
            errors.append(f"session observation {task_id}@{revision} exceeds 200 KiB")
        errors.extend(private_text_errors(Path(f"sessions/{task_id}.jsonl"), text))
    return errors


def projection_errors(
    tasks: list[Task],
    sessions: list[Meta],
    *,
    basic_task_errors: Any,
    validate_session_record: Any,
    private_text_errors: Any,
    graph_errors: Any,
    hierarchy_errors: Any,
    supersession_errors: Any,
    policy: Any,
) -> list[str]:
    """Reject invalid authority before exposing any campaign projection."""
    errors, revisions = _task_projection_errors(
        tasks, basic_task_errors, private_text_errors, policy
    )
    errors.extend(
        _session_projection_errors(
            tasks, sessions, revisions, validate_session_record, private_text_errors
        )
    )
    # Campaign is a read-only authority view, not an alternative graph model.
    # Reuse durable graph checks so incomplete or cyclic authority cannot be
    # rendered as actionable worker information.
    errors.extend(graph_errors(tasks))
    errors.extend(hierarchy_errors(tasks))
    errors.extend(supersession_errors(tasks))
    return sorted(set(errors))


def _worker(task: Meta, observed_at: dt.datetime) -> Meta:
    owner = task.get("owner")
    if not isinstance(owner, str) or not owner:
        return {"state": "unassigned"}
    expiry = task.get("claim_expires")
    if not isinstance(expiry, str) or not expiry:
        return {"owner": owner, "state": "unfenced"}
    deadline = _timestamp(expiry, "claim_expires")
    return {
        "owner": owner,
        "claim_expires": expiry,
        "state": "expired" if deadline <= observed_at else "active",
    }


def _dependencies(task: Meta, by_id: dict[str, Meta]) -> list[Meta]:
    values = task.get("depends_on", [])
    if not isinstance(values, list):
        raise ValueError("depends_on is invalid")
    return [
        {"task": dependency, "status": str(by_id.get(dependency, {}).get("status", "missing"))}
        for dependency in sorted(values)
    ]


def _reservation(task: Meta, observed_at: dt.datetime) -> tuple[str, Meta | None]:
    reservation = task.get("execution_reservation")
    if reservation is None:
        return "clear", None
    if not execution_envelope.valid_reservation(reservation):
        raise ValueError("execution reservation is invalid")
    expiry = _timestamp(reservation["expires_at"], "execution reservation expiry")
    return ("expired" if expiry <= observed_at else "live"), {
        "execution_id": reservation["execution_id"],
        "expires_at": reservation["expires_at"],
    }


def _blockers(task: Meta, dependencies: list[Meta], observed_at: dt.datetime) -> list[Meta]:
    blockers = [
        {"kind": "dependency", "task": item["task"], "status": item["status"]}
        for item in dependencies
        if item["status"] not in TERMINAL
    ]
    if task.get("status") == "blocked":
        blockers.append({"kind": "task-status"})
    state, _ = _reservation(task, observed_at)
    if state != "clear":
        blockers.append({"kind": "execution-claim", "state": state})
    circuit = task.get("retry_circuit")
    if circuit is not None:
        checked = retry_circuit.validate(circuit)
        if checked["hold"] is not None:
            blockers.append({"kind": "retry-circuit", "state": "held"})
        if checked["reservations"]:
            blockers.append({"kind": "retry-claim", "state": "live"})
    return blockers


def _outcome(task: Meta) -> Meta | None:
    status = str(task["status"])
    if status not in TERMINAL:
        return None
    acceptance = task.get("spec_acceptance")
    return {
        "status": status,
        "acceptance": "pass"
        if isinstance(acceptance, dict) and acceptance.get("status") == "pass"
        else "absent",
    }


def _attempts(task: Meta, sessions: list[Meta]) -> tuple[list[Meta], Meta]:
    current = int(task["task_revision"])
    attempts = [
        {
            "revision": int(session["task_revision"]),
            "recorded_at": session["recorded_at"],
            "status": session["status"],
            "trigger": session["trigger"],
            "state": "current" if int(session["task_revision"]) == current else "stale",
        }
        for session in sorted(sessions, key=lambda item: int(item["task_revision"]))
    ]
    stale = [item for item in attempts if item["state"] == "stale"]
    return attempts, {
        "current_session": bool(attempts and attempts[-1]["state"] == "current"),
        "stale_sessions": len(stale),
    }


def _recovery(task: Meta, worker: Meta, sessions: Meta, observed_at: dt.datetime) -> Meta:
    if task.get("status") in TERMINAL:
        return {"kind": "none"}
    state, _ = _reservation(task, observed_at)
    if state == "expired":
        return {"kind": "recover-execution-claim"}
    if state == "live":
        return {"kind": "wait-for-execution-claim"}
    if worker["state"] == "expired":
        return {"kind": "recover-expired-claim"}
    if task.get("status") == "blocked":
        return {"kind": "resume-or-unblock"}
    if sessions["stale_sessions"] and task.get("status") not in TERMINAL:
        return {"kind": "record-current-session"}
    return {"kind": "none"}


def build(tasks: list[Task], sessions: list[Meta], observed_at: dt.datetime) -> Meta:
    """Build a backend-neutral campaign graph from one authoritative snapshot."""
    by_id = {str(task["id"]): task for _, task, _ in tasks}
    sessions_by_task: dict[str, list[Meta]] = defaultdict(list)
    for session in sessions:
        sessions_by_task[str(session["task"])].append(session)
    cards: list[Meta] = []
    for task_id, task in sorted(by_id.items()):
        dependencies = _dependencies(task, by_id)
        worker = _worker(task, observed_at)
        attempts, session_state = _attempts(task, sessions_by_task[task_id])
        cards.append(
            {
                "id": task_id,
                "title": task["title"],
                "priority": task["priority"],
                "status": task["status"],
                "revision": task["task_revision"],
                "worker": worker,
                "dependencies": dependencies,
                "blockers": _blockers(task, dependencies, observed_at),
                "attempts": attempts,
                "session": session_state,
                "recovery": _recovery(task, worker, session_state, observed_at),
                "outcome": _outcome(task),
            }
        )
    counts = Counter(str(card["status"]) for card in cards)
    return {
        "schema_version": SCHEMA_VERSION,
        "observed_at": observed_at.isoformat(),
        "tasks": cards,
        "summary": {
            "tasks": len(cards),
            "sessions": len(sessions),
            "by_status": {status: counts[status] for status in sorted(counts)},
            "recovery_required": sum(card["recovery"]["kind"] != "none" for card in cards),
        },
    }


def render_text(campaign: Meta) -> str:
    """Render every JSON field in a compact human-readable, stable form."""
    lines = ["CAMPAIGN"]
    lines.extend(
        name.upper() + "=" + _canonical(campaign[name])
        for name in ("schema_version", "observed_at", "tasks", "summary")
    )
    return "\n".join(lines) + "\n"


def add_command_parser(commands: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    """Register the projection command; it has no lifecycle mutation arguments."""
    item = commands.add_parser("campaign")
    item.add_argument("--json", action="store_true")
    item.add_argument("--observed-at", type=parse_observed_at, metavar="ISO_8601")


def command(
    tasks: list[Task], sessions: list[Meta], as_json: bool, observed_at: dt.datetime
) -> str:
    """Return one text-first or canonical JSON campaign projection."""
    campaign = build(tasks, sessions, observed_at)
    if errors := projection_contract_errors(campaign):
        raise ValueError("campaign projection contract failed:\n" + "\n".join(errors))
    return _canonical(campaign) + "\n" if as_json else render_text(campaign)
