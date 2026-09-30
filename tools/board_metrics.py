# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Deterministic, privacy-safe company board projections."""

from __future__ import annotations

from collections import Counter
from typing import Any

Meta = dict[str, Any]
Task = tuple[Any, Meta, str]


def _group(meta: Meta) -> tuple[str, str]:
    return str(meta.get("role") or "unassigned"), str(meta.get("team") or "unassigned")


def _gate_failure(meta: Meta) -> str | None:
    gate = meta.get("oracle_gate")
    if not isinstance(gate, dict) or gate.get("required") is not True:
        return None
    if gate.get("open_stage"):
        return str(gate["open_stage"])
    if gate.get("reconciliation_required"):
        return "reconciliation"
    if gate.get("authorized") is not True:
        sequence = gate.get("stage_sequence") or (
            "intake",
            "discussion",
            "formal_spec_review",
            "reconciliation",
        )
        completed = gate.get("completed") or []
        for stage in sequence:
            if stage not in completed:
                return str(stage)
        return "authorization"
    return None


def _decision_pending(meta: Meta) -> bool:
    gate = meta.get("oracle_gate")
    if not isinstance(gate, dict) or gate.get("required") is not True:
        return False
    sequence = gate.get("stage_sequence") or ()
    if "decision" not in sequence:
        return False
    return gate.get("open_stage") == "decision" or "decision" not in (gate.get("completed") or [])


def _evidence(meta: Meta) -> bool:
    acceptance = meta.get("spec_acceptance")
    return (
        isinstance(acceptance, dict)
        and acceptance.get("status") == "pass"
        and bool(acceptance.get("evidence_ref"))
    )


def _role_progress(ordered: list[Meta]) -> list[dict[str, Any]]:
    groups: dict[tuple[str, str], list[Meta]] = {}
    for meta in ordered:
        groups.setdefault(_group(meta), []).append(meta)
    result = []
    for (role, team), members in sorted(groups.items()):
        counts = Counter(str(item.get("status", "")) for item in members)
        result.append(
            {
                "role": role,
                "team": team,
                "tasks": len(members),
                "by_status": {status: counts[status] for status in sorted(counts)},
            }
        )
    return result


def _gate_failures(ordered: list[Meta]) -> list[dict[str, str]]:
    return [
        {"task": str(meta["id"]), "stage": stage}
        for meta in ordered
        if (stage := _gate_failure(meta)) is not None
    ]


def _blocked_tasks(ordered: list[Meta]) -> list[dict[str, str]]:
    return [
        {
            "task": str(meta["id"]),
            "priority": str(meta.get("priority", "")),
            "role": _group(meta)[0],
        }
        for meta in ordered
        if meta.get("status") == "blocked"
    ]


def build_metrics(tasks: list[Task]) -> dict[str, Any]:
    """Build the complete board projection from one authoritative task snapshot."""
    ordered = sorted((meta for _, meta, _ in tasks), key=lambda item: str(item.get("id", "")))
    counts = Counter(str(meta.get("status", "")) for meta in ordered)
    role_progress = _role_progress(ordered)
    decisions = [str(meta["id"]) for meta in ordered if _decision_pending(meta)]
    failures = _gate_failures(ordered)
    blocked = _blocked_tasks(ordered)
    evidence_tasks = [str(meta["id"]) for meta in ordered if _evidence(meta)]
    return {
        "schema_version": 1,
        "tasks": len(ordered),
        "by_status": {status: counts[status] for status in sorted(counts)},
        "role_progress": role_progress,
        "decision_backlog": {"count": len(decisions), "tasks": decisions},
        "gate_failures": {"count": len(failures), "items": failures},
        "blocked_tasks": {"count": len(blocked), "items": blocked},
        "evidence_coverage": {
            "covered": len(evidence_tasks),
            "total": len(ordered),
            "tasks": evidence_tasks,
        },
    }


def encode(metrics: dict[str, Any]) -> str:
    """Return the canonical byte-stable JSON representation."""
    import json

    return json.dumps(metrics, sort_keys=True, separators=(",", ":")) + "\n"
