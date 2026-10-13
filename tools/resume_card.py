# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Deterministic, privacy-safe resume cards derived from durable task records."""

from __future__ import annotations

import argparse
import datetime as dt
import json
from collections.abc import Callable
from pathlib import Path
from typing import Any

if __package__:
    from . import (
        assumption_revalidation,
        change_drift,
        execution_envelope,
        retry_circuit,
        task_spec,
    )
else:  # pragma: no cover - direct handoffctl execution
    import assumption_revalidation  # type: ignore[import-not-found,no-redef]
    import change_drift  # type: ignore[import-not-found,no-redef]
    import execution_envelope  # type: ignore[import-not-found,no-redef]
    import retry_circuit  # type: ignore[import-not-found,no-redef]
    import task_spec  # type: ignore[import-not-found,no-redef]

type Meta = dict[str, Any]

SCHEMA_VERSION = 2
MAX_TITLE_BYTES = 512
MAX_SUMMARY_BYTES = 4000
MAX_NEXT_ACTION_BYTES = 1024


def parse_observed_at(value: str) -> dt.datetime:
    """Parse one explicit, timezone-aware observation instant for a card."""
    try:
        parsed = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as error:
        raise argparse.ArgumentTypeError("observed-at must be ISO-8601") from error
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise argparse.ArgumentTypeError("observed-at must include a timezone")
    return parsed.astimezone(dt.UTC).replace(microsecond=0)


def current_observed_at() -> dt.datetime:
    """Capture the one live instant used for an otherwise unpinned card."""
    return dt.datetime.now(dt.UTC).replace(microsecond=0)


def _observed_at_text(observed_at: dt.datetime) -> str:
    if observed_at.tzinfo is None or observed_at.utcoffset() is None:
        raise ValueError("observed_at is not timezone-aware")
    return observed_at.astimezone(dt.UTC).replace(microsecond=0).isoformat()


def projection_errors(
    path: Path,
    task: Meta,
    body: str,
    private_text_errors: Callable[[Path, str], list[str]],
) -> list[str]:
    """Reject unsafe or overlarge authority text before a card can expose it."""
    errors: list[str] = []
    limits = {
        "title": MAX_TITLE_BYTES,
        "summary": MAX_SUMMARY_BYTES,
        "next_action": MAX_NEXT_ACTION_BYTES,
    }
    for field, maximum in limits.items():
        value = task.get(field)
        if isinstance(value, str) and len(value.encode("utf-8")) > maximum:
            errors.append(f"{task.get('id', path.stem)}: {field} exceeds {maximum} bytes")
    authority_text = json.dumps(task, sort_keys=True, separators=(",", ":")) + "\n" + body
    if len(authority_text.encode("utf-8")) > 200000:
        errors.append(f"{path.name}: projected authority exceeds 200 KiB")
    errors.extend(private_text_errors(path, authority_text))
    try:
        updated_at = dt.datetime.fromisoformat(
            str(task.get("updated_at", "")).replace("Z", "+00:00")
        )
        if updated_at.tzinfo is None or updated_at.utcoffset() is None:
            raise ValueError
    except ValueError:
        errors.append(f"{task.get('id', path.stem)}: updated_at is not timezone-aware")
    return errors


def _source(task: Meta) -> Meta:
    return {
        "branch": str(task.get("observed_branch", "")),
        "checkpoint_commit": str(task.get("checkpoint_commit", "")),
        "head": str(task.get("observed_head", "")),
        "revision": int(task["task_revision"]),
    }


def _scope(task: Meta) -> tuple[Meta, list[Meta]]:
    history = change_drift.records(task)
    baseline = change_drift.latest(history, "baseline")
    declared = [] if baseline is None else change_drift.active_scope(history, baseline)
    outstanding = change_drift.unresolved(history)
    drift = [
        {
            "field": f"scope.{entry['path']}",
            "kind": "scope",
            "material": True,
            "status": "unacknowledged",
        }
        for entry in outstanding
    ]
    return {"declared": declared, "state": "absent" if baseline is None else "observed"}, drift


def _acknowledgements(task: Meta) -> list[Meta]:
    history = change_drift.records(task)
    delta = change_drift.latest(history, "delta")
    material = (
        {}
        if delta is None
        else {entry["path"] for entry in delta["payload"]["entries"] if entry["material"]}
    )
    scope = [
        {"field": f"scope.{path}", "kind": "scope", "record": "explain"}
        for record in history
        if record["kind"] == "explain"
        and record["payload"]["delta_digest"] == (delta or {}).get("digest")
        for path in record["payload"]["paths"]
        if path in material
    ]
    assumptions = [
        {"field": f"assumptions.{record['id']}", "kind": record["kind"], "record": record["action"]}
        for record in assumption_revalidation.records(task)
        if record["material"] and record["action"] in {"revalidate", "dispose"}
    ]
    return sorted(
        [*scope, *assumptions], key=lambda item: (str(item["field"]), str(item["record"]))
    )


def _assumptions(
    root: Path, projects_root: Path, task: Meta, tasks: list[Meta]
) -> tuple[list[Meta], list[Meta]]:
    cards: list[Meta] = []
    drift: list[Meta] = []
    for assumption_id, record in sorted(
        assumption_revalidation.active(assumption_revalidation.records(task)).items()
    ):
        item: Meta = {
            "id": assumption_id,
            "kind": record["kind"],
            "material": record["material"],
            "recorded_binding": record["binding"],
        }
        if record["action"] == "dispose":
            item["status"] = "disposed"
        else:
            try:
                current = assumption_revalidation.current_binding(
                    root, projects_root, task, tasks, record
                )
            except RuntimeError:
                item["status"] = "unavailable"
            else:
                item["status"] = "fresh" if current == record["binding"] else "stale"
                item["current_binding"] = current
        cards.append(item)
        if item["status"] in {"stale", "unavailable"}:
            drift.append(
                {
                    "field": f"assumptions.{assumption_id}",
                    "kind": str(record["kind"]),
                    "material": bool(record["material"]),
                    "status": item["status"],
                }
            )
    return cards, drift


def _acceptance(task: Meta, evidence_classes: frozenset[str]) -> Meta | None:
    """Return only a closed, validated legacy acceptance record."""
    acceptance = task.get("spec_acceptance")
    if acceptance is None:
        return None
    has_spec = "spec_ref" in task or "spec_revision" in task
    required = {"status", "evidence_class", "evidence_ref", "evidence_digest"}
    required |= {"spec_ref", "spec_revision"} if has_spec else {"match"}
    if not isinstance(acceptance, dict) or set(acceptance) != required:
        raise ValueError("spec acceptance is incomplete or unknown")
    if (
        acceptance.get("status") != "pass"
        or acceptance.get("evidence_class") not in evidence_classes
        or not isinstance(acceptance.get("evidence_ref"), str)
        or task_spec.EVIDENCE_REF.fullmatch(acceptance["evidence_ref"]) is None
        or not isinstance(acceptance.get("evidence_digest"), str)
        or task_spec.DIGEST.fullmatch(acceptance["evidence_digest"]) is None
    ):
        raise ValueError("spec acceptance is invalid")
    if has_spec and (
        acceptance.get("spec_ref") != task.get("spec_ref")
        or acceptance.get("spec_revision") != task.get("spec_revision")
    ):
        raise ValueError("spec acceptance does not match task specification")
    if not has_spec and acceptance.get("match") != "best_effort":
        raise ValueError("spec acceptance match is invalid")
    return {key: acceptance[key] for key in sorted(required)}


def _predicates(task: Meta, evidence_classes: frozenset[str]) -> list[Meta]:
    ledger = task.get("evidence_ledger")
    if ledger is None:
        return []
    if not isinstance(ledger, dict) or set(ledger) != task_spec.LEDGER_FIELDS:
        raise ValueError("evidence ledger is incomplete or unknown")
    candidate_ref = ledger.get("candidate_ref")
    candidate_digest = ledger.get("candidate_digest")
    steps = ledger.get("steps")
    if (
        not isinstance(candidate_ref, str)
        or task_spec.EVIDENCE_REF.fullmatch(candidate_ref) is None
        or not isinstance(candidate_digest, str)
        or task_spec.DIGEST.fullmatch(candidate_digest) is None
        or not isinstance(steps, list)
    ):
        raise ValueError("evidence ledger is invalid")
    predicates: list[Meta] = []
    for step in steps:
        if not isinstance(step, dict) or set(step) != task_spec.LEDGER_STEP_FIELDS:
            raise ValueError("evidence ledger step is incomplete or unknown")
        if (
            not isinstance(step.get("predicate_id"), str)
            or task_spec.ID_REF.fullmatch(step["predicate_id"]) is None
            or step.get("status") not in {"pass", "stale"}
            or not isinstance(step.get("candidate_ref"), str)
            or task_spec.EVIDENCE_REF.fullmatch(step["candidate_ref"]) is None
            or not isinstance(step.get("candidate_digest"), str)
            or task_spec.DIGEST.fullmatch(step["candidate_digest"]) is None
            or step.get("evidence_class") not in evidence_classes
            or not isinstance(step.get("evidence_ref"), str)
            or task_spec.EVIDENCE_REF.fullmatch(step["evidence_ref"]) is None
            or not isinstance(step.get("evidence_digest"), str)
            or task_spec.DIGEST.fullmatch(step["evidence_digest"]) is None
            or type(step.get("recorded_task_revision")) is not int
            or step["recorded_task_revision"] < 1
        ):
            raise ValueError("evidence ledger step is invalid")
        predicates.append(
            {
                key: step[key]
                for key in (
                    "predicate_id",
                    "status",
                    "candidate_ref",
                    "candidate_digest",
                    "evidence_class",
                    "evidence_ref",
                    "evidence_digest",
                    "recorded_task_revision",
                )
            }
        )
    return sorted(predicates, key=lambda value: str(value["predicate_id"]))


def _evidence(task: Meta, evidence_classes: frozenset[str]) -> Meta:
    return {
        "acceptance": _acceptance(task, evidence_classes),
        "predicates": _predicates(task, evidence_classes),
    }


def _execution_recovery(task: Meta, observed_at: dt.datetime) -> tuple[Meta, Meta | None]:
    """Describe a valid execution fence before less-specific recovery paths."""
    reservation = task.get("execution_reservation")
    if reservation is None:
        return {"state": "clear"}, None
    if not execution_envelope.valid_reservation(reservation):
        raise ValueError("execution reservation is invalid")
    expires_at = dt.datetime.fromisoformat(str(reservation["expires_at"]).replace("Z", "+00:00"))
    observed_at_text = _observed_at_text(observed_at)
    details: Meta = {
        "execution_id": reservation["execution_id"],
        "expires_at": reservation["expires_at"],
        "observed_at": observed_at_text,
    }
    if expires_at > observed_at:
        return {"state": "live", **details}, {
            "kind": "wait-for-execution-reservation",
            "instruction": "Wait for the live bound execution reservation to finish or expire.",
        }
    return {"state": "expired", **details}, {
        "kind": "recover-execution-reservation",
        "instruction": "Recover expired reservation with verified exit and result evidence.",
    }


def _retry(task: Meta) -> tuple[Meta, Meta | None]:
    state = task.get("retry_circuit")
    if state is None:
        return {"state": "clear"}, None
    checked = retry_circuit.validate(state)
    if checked["reservations"]:
        return {"state": "recovery_required", "reservations": len(checked["reservations"])}, {
            "kind": "recover-retry-reservation",
            "instruction": "Recover the live retry reservation before resuming work.",
        }
    if checked["hold"] is not None:
        return {"state": "held", "attempts": checked["hold"]["attempts"]}, {
            "kind": "recover-retry-circuit",
            "instruction": "Record one retry-circuit recovery before repeating the held command.",
        }
    return {"state": "clear", "attempts": len(checked["attempts"])}, None


def _next_action(
    task: Meta, drift: list[Meta], execution_recovery: Meta | None, retry_recovery: Meta | None
) -> Meta:
    if execution_recovery is not None:
        return execution_recovery
    if retry_recovery is not None:
        return retry_recovery
    material = next((item for item in drift if item["material"]), None)
    if material is not None:
        if material["kind"] == "scope":
            return {
                "kind": "explain-material-drift",
                "instruction": "Explain the material scope drift.",
            }
        assumption_id = str(material["field"]).split(".", 1)[1]
        return {
            "kind": "revalidate-material-assumption",
            "instruction": f"Revalidate or explicitly dispose material assumption {assumption_id}.",
        }
    return {"kind": "task-next-action", "instruction": str(task["next_action"])}


def build(
    root: Path,
    projects_root: Path,
    task: Meta,
    tasks: list[Meta],
    observed_at: dt.datetime,
    evidence_classes: frozenset[str] = task_spec.EVIDENCE_CLASSES,
) -> Meta:
    """Compose one stable card for an explicit observation instant."""
    scope, scope_drift = _scope(task)
    assumptions, assumption_drift = _assumptions(root, projects_root, task, tasks)
    observed_at_text = _observed_at_text(observed_at)
    execution, execution_recovery = _execution_recovery(task, observed_at)
    retry, retry_recovery = _retry(task)
    drift = sorted([*scope_drift, *assumption_drift], key=lambda item: str(item["field"]))
    return {
        "schema_version": SCHEMA_VERSION,
        "observed_at": observed_at_text,
        "task": {
            "id": task["id"],
            "priority": task["priority"],
            "status": task["status"],
            "summary": task["summary"],
            "title": task["title"],
        },
        "source": _source(task),
        "scope": scope,
        "evidence": _evidence(task, evidence_classes),
        "retry": retry,
        "recovery": {"execution": execution, "retry": retry},
        "assumptions": assumptions,
        "drift": drift,
        "acknowledgements": _acknowledgements(task),
        "next_action": _next_action(task, drift, execution_recovery, retry_recovery),
    }


def render_text(card: Meta) -> str:
    """Render the same card as compact, deterministic text-first output."""
    task = card["task"]
    lines = [f"RESUME_CARD={task['id']}"]
    lines.extend(
        f"{name.upper()}=" + json.dumps(card[name], sort_keys=True, separators=(",", ":"))
        for name in (
            "schema_version",
            "observed_at",
            "task",
            "source",
            "scope",
            "assumptions",
            "evidence",
            "retry",
            "recovery",
            "acknowledgements",
            "drift",
            "next_action",
        )
    )
    return "\n".join(lines) + "\n"


def add_command_parser(commands: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    """Register the read-only resume-card command without lifecycle authority."""
    item = commands.add_parser("resume-card")
    item.add_argument("task")
    item.add_argument("--json", action="store_true")
    item.add_argument(
        "--observed-at",
        type=parse_observed_at,
        metavar="ISO_8601",
        help="pin the card observation time for reproducible output (default: current UTC time)",
    )


def command(
    root: Path,
    projects_root: Path,
    task_id: str,
    tasks: list[tuple[Path, Meta, str]],
    as_json: bool,
    observed_at: dt.datetime,
    evidence_classes: frozenset[str] = task_spec.EVIDENCE_CLASSES,
) -> str:
    """Return one rendered card from a caller-held, consistent authority snapshot."""
    task = next((meta for _, meta, _ in tasks if meta.get("id") == task_id), None)
    if task is None:
        raise RuntimeError(f"unknown task {task_id}")
    card = build(
        root,
        projects_root,
        task,
        [meta for _, meta, _ in tasks],
        observed_at,
        evidence_classes,
    )
    return (
        json.dumps(card, sort_keys=True, separators=(",", ":")) + "\n"
        if as_json
        else render_text(card)
    )
