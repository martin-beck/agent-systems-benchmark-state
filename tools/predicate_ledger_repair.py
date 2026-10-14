# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Audited repair of one predicate-evidence row after task inactivity."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any

try:
    from .task_spec import DEFAULT_EVIDENCE_POLICY, EVIDENCE_REF, EvidencePolicy, task_spec_errors
except ImportError:  # pragma: no cover - direct handoffctl execution
    from task_spec import (  # type: ignore[import-not-found,no-redef]
        DEFAULT_EVIDENCE_POLICY,
        EVIDENCE_REF,
        EvidencePolicy,
        task_spec_errors,
    )

_DIGEST = re.compile(r"^sha256:[0-9a-f]{64}$")
_MAX_REASON = 512


def add_parser(commands: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    item = commands.add_parser("repair-predicate-ledger")
    item.add_argument("task")
    item.add_argument("--expected-revision", type=int, required=True)
    for option in ("predicate", "evidence-class", "evidence-ref", "evidence-digest", "reason"):
        item.add_argument("--" + option, required=True)
    item.add_argument("--candidate-ref", required=True)
    item.add_argument("--candidate-digest", required=True)


def _digest(root: Path, reference: str) -> str | None:
    """Hash one bounded, relative regular file without following symlinks."""
    path = Path(reference)
    if path.is_absolute() or ".." in path.parts:
        return None
    target = root / path
    try:
        if target.is_symlink() or not target.is_file() or target.stat().st_size > 4 * 1024 * 1024:
            return None
        return "sha256:" + hashlib.sha256(target.read_bytes()).hexdigest()
    except OSError:
        return None


def repair(  # noqa: C901
    root: Path, args: Any, meta: dict[str, Any], policy: EvidencePolicy | None
) -> str:
    """Append a fresh pass while retaining every previous ledger row."""
    if args.expected_revision != meta.get("task_revision"):
        raise RuntimeError(
            "stale revision: expected "
            f"{args.expected_revision}, current {meta.get('task_revision')}"
        )
    if meta.get("status") != "done" or meta.get("owner") or meta.get("claim_expires"):
        raise RuntimeError("predicate-ledger repair requires a done, inactive, unowned task")
    reason = str(args.reason)
    if not reason.strip() or len(reason) > _MAX_REASON or any(ord(c) < 32 for c in reason):
        raise RuntimeError("predicate-ledger repair reason is empty or unbounded")
    predicate = str(args.predicate)
    evidence_ref = str(args.evidence_ref)
    evidence_digest = str(args.evidence_digest)
    if (
        not EVIDENCE_REF.fullmatch(evidence_ref)
        or evidence_ref.startswith("/")
        or ".." in Path(evidence_ref).parts
    ):
        raise RuntimeError("predicate-ledger repair evidence ref is unsafe")
    if not _DIGEST.fullmatch(evidence_digest) or _digest(root, evidence_ref) != evidence_digest:
        raise RuntimeError("predicate-ledger repair evidence digest is not fresh")
    ledger = meta.get("evidence_ledger")
    if not isinstance(ledger, dict) or set(ledger) != {
        "candidate_ref",
        "candidate_digest",
        "steps",
    }:
        raise RuntimeError("predicate-ledger repair requires a canonical evidence ledger")
    steps = ledger.get("steps")
    if not isinstance(steps, list):
        raise RuntimeError("predicate-ledger repair requires a canonical evidence ledger")
    # Validate task/spec identity without asking malformed historical rows to pass again.
    spec_meta = dict(meta)
    spec_meta.pop("evidence_ledger", None)
    selected_policy = policy or DEFAULT_EVIDENCE_POLICY
    if task_spec_errors(root, spec_meta, selected_policy):
        raise RuntimeError("predicate-ledger repair task spec is unavailable")
    spec = json.loads((root / str(meta["spec_ref"])).read_text(encoding="utf-8"))
    predicates = {item["id"] for item in spec["acceptance_predicates"] if isinstance(item, dict)}
    if predicate not in predicates:
        raise RuntimeError("predicate-ledger repair names an unknown predicate")
    candidate_ref = args.candidate_ref
    candidate_digest = args.candidate_digest
    if (
        not isinstance(candidate_ref, str)
        or not _DIGEST.fullmatch(candidate_digest)
        or _digest(root, candidate_ref) != candidate_digest
    ):
        raise RuntimeError("predicate-ledger repair candidate is stale")
    if (candidate_ref, candidate_digest) == (
        ledger.get("candidate_ref"),
        ledger.get("candidate_digest"),
    ):
        raise RuntimeError("predicate-ledger repair candidate is not new")
    if args.evidence_class not in selected_policy.classes:
        raise RuntimeError("predicate-ledger repair evidence class is unknown")
    fresh = {
        "predicate_id": predicate,
        "status": "pass",
        "candidate_ref": candidate_ref,
        "candidate_digest": candidate_digest,
        "evidence_class": args.evidence_class,
        "evidence_ref": evidence_ref,
        "evidence_digest": evidence_digest,
        "recorded_task_revision": int(meta["task_revision"]) + 1,
    }
    prospective = dict(ledger, candidate_ref=candidate_ref, candidate_digest=candidate_digest)
    historical = []
    for row in steps:
        if not isinstance(row, dict):
            raise RuntimeError("predicate-ledger repair found a malformed historical row")
        retained = dict(row)
        if retained.get("predicate_id") == predicate and retained.get("status") == "pass":
            retained["status"] = "stale"
        historical.append(retained)
    prospective["steps"] = [*historical, fresh]
    if not _DIGEST.fullmatch(evidence_digest):
        raise RuntimeError("predicate-ledger repair evidence digest is invalid")
    meta["evidence_ledger"] = prospective
    return reason
