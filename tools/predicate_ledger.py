# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Fail-closed predicate-evidence ledger transitions for ``handoffctl accept``."""

from __future__ import annotations

import argparse
import json
from collections.abc import Callable
from pathlib import Path
from typing import Any, cast

if __package__:
    from .task_spec import (
        EvidencePolicy,
        done_admission_error,
        evidence_ledger_errors,
        task_spec_errors,
    )
else:  # pragma: no cover - direct handoffctl execution
    from task_spec import (  # type: ignore[import-not-found,no-redef]
        EvidencePolicy,
        done_admission_error,
        evidence_ledger_errors,
        task_spec_errors,
    )

type Meta = dict[str, Any]
type PredicateInputs = tuple[str, str, str, bool]


def predicate_acceptance_inputs(args: argparse.Namespace) -> PredicateInputs | None:
    """Return a complete predicate request, rejecting partial predicate arguments."""
    predicate = getattr(args, "predicate", None)
    candidate_ref = getattr(args, "candidate_ref", None)
    candidate_digest = getattr(args, "candidate_digest", None)
    reopen = bool(getattr(args, "reopen", False))
    if predicate is None and candidate_ref is None and candidate_digest is None and not reopen:
        return None
    if not all(
        isinstance(value, str) and value for value in (predicate, candidate_ref, candidate_digest)
    ):
        raise RuntimeError(
            "predicate acceptance requires predicate, candidate ref, and candidate digest"
        )
    return cast(PredicateInputs, (predicate, candidate_ref, candidate_digest, reopen))


def _validate_spec(root: Path, meta: Meta, policy: EvidencePolicy | None, predicate: str) -> None:
    """Require a valid bound spec and a predicate declared by that exact spec."""
    if "spec_ref" not in meta or "spec_revision" not in meta:
        raise RuntimeError("predicate acceptance requires a bound task spec")
    preflight_meta = dict(meta)
    preflight_meta.pop("evidence_ledger", None)
    if task_spec_errors(root, preflight_meta, policy):
        raise RuntimeError("predicate acceptance task spec is unavailable")
    spec = json.loads((root / str(meta["spec_ref"])).read_text(encoding="utf-8"))
    predicates = {item["id"] for item in spec["acceptance_predicates"]}
    if predicate not in predicates:
        raise RuntimeError("predicate acceptance names an unknown predicate")


def _ledger(meta: Meta, candidate_ref: str, candidate_digest: str) -> Meta:
    """Load or initialize the ledger without accepting an unstructured value."""
    ledger = meta.get("evidence_ledger")
    if ledger is None:
        return {"candidate_ref": candidate_ref, "candidate_digest": candidate_digest, "steps": []}
    if not isinstance(ledger, dict):
        raise RuntimeError("predicate evidence ledger is malformed")
    return ledger


def _candidate_changed(ledger: Meta, candidate_ref: str, candidate_digest: str) -> bool:
    """Determine whether the recorded candidate binding is being replaced."""
    return (
        ledger.get("candidate_ref") != candidate_ref
        or ledger.get("candidate_digest") != candidate_digest
    )


def _historical_steps(existing_steps: object) -> object:
    """Retain every historical row while marking passing rows stale."""
    if not isinstance(existing_steps, list):
        return existing_steps
    history: list[object] = []
    for existing_step in existing_steps:
        if not isinstance(existing_step, dict):
            history.append(existing_step)
            continue
        historical = dict(existing_step)
        if historical.get("status") == "pass":
            historical["status"] = "stale"
        history.append(historical)
    return history


def _validate_ledger(
    root: Path,
    meta: Meta,
    ledger: Meta,
    policy: EvidencePolicy | None,
    candidate_ref: str,
    candidate_digest: str,
    changed_candidate: bool,
) -> None:
    """Validate current evidence, or its complete prospective historical form."""
    if not changed_candidate:
        errors = evidence_ledger_errors(root, meta, policy)
    else:
        prospective_ledger = dict(ledger)
        prospective_ledger.update(
            candidate_ref=candidate_ref,
            candidate_digest=candidate_digest,
            steps=_historical_steps(ledger.get("steps")),
        )
        errors = evidence_ledger_errors(
            root, dict(meta, evidence_ledger=prospective_ledger), policy
        )
    if errors:
        raise RuntimeError("predicate evidence is invalid: " + "; ".join(errors))


def _record_step(
    args: argparse.Namespace,
    meta: Meta,
    ledger: Meta,
    predicate: str,
    candidate_ref: str,
    candidate_digest: str,
    changed_candidate: bool,
) -> None:
    """Replace one predicate row after preserving and validating its history."""
    existing_steps = ledger.get("steps")
    steps = [dict(row) for row in existing_steps] if isinstance(existing_steps, list) else []
    if changed_candidate:
        for row in steps:
            if row.get("status") == "pass":
                row["status"] = "stale"
        ledger["candidate_ref"] = candidate_ref
        ledger["candidate_digest"] = candidate_digest
    step: Meta = {
        "predicate_id": predicate,
        "status": "pass",
        "candidate_ref": candidate_ref,
        "candidate_digest": candidate_digest,
        "evidence_class": args.evidence_class,
        "evidence_ref": args.evidence_ref,
        "evidence_digest": args.evidence_digest,
        "recorded_task_revision": int(meta["task_revision"]) + 1,
    }
    ledger["steps"] = [row for row in steps if row.get("predicate_id") != predicate] + [step]
    meta["evidence_ledger"] = ledger


def apply_predicate_acceptance(
    root: Path,
    args: argparse.Namespace,
    meta: Meta,
    policy: EvidencePolicy | None,
    inputs: PredicateInputs,
) -> str:
    """Record one predicate result while enforcing immutable candidate binding."""
    predicate, candidate_ref, candidate_digest, reopen = inputs
    _validate_spec(root, meta, policy, predicate)
    ledger = _ledger(meta, candidate_ref, candidate_digest)
    changed_candidate = _candidate_changed(ledger, candidate_ref, candidate_digest)
    if changed_candidate and not reopen:
        raise RuntimeError("candidate changed; reopen predicate evidence before recording")
    if reopen and not changed_candidate:
        raise RuntimeError("reopen requires a different candidate")
    _validate_ledger(root, meta, ledger, policy, candidate_ref, candidate_digest, changed_candidate)
    _record_step(args, meta, ledger, predicate, candidate_ref, candidate_digest, changed_candidate)
    errors = evidence_ledger_errors(root, meta, policy)
    if errors:
        raise RuntimeError("predicate evidence is invalid: " + "; ".join(errors))
    return str(args.note)


def apply_acceptance(
    root: Path,
    args: argparse.Namespace,
    meta: Meta,
    policy: EvidencePolicy | None,
    freshness_error: str | Callable[[], str | None] | None = None,
) -> str:
    """Apply ordinary or predicate acceptance after optional freshness admission."""
    if meta.get("owner") != args.owner:
        raise RuntimeError(f"{args.task} is owned by {meta.get('owner') or 'nobody'}")
    if meta.get("status") != "in_progress":
        raise RuntimeError("accept requires an active task")
    if args.expected_revision != meta["task_revision"]:
        raise RuntimeError(
            f"stale revision: expected {args.expected_revision}, current {meta['task_revision']}"
        )
    error = freshness_error() if callable(freshness_error) else freshness_error
    if error:
        raise RuntimeError(error)
    if inputs := predicate_acceptance_inputs(args):
        return apply_predicate_acceptance(root, args, meta, policy, inputs)
    acceptance: Meta = {
        "status": "pass",
        "evidence_class": args.evidence_class,
        "evidence_ref": args.evidence_ref,
        "evidence_digest": args.evidence_digest,
    }
    if "spec_ref" in meta and "spec_revision" in meta:
        acceptance.update(spec_ref=meta["spec_ref"], spec_revision=meta["spec_revision"])
    else:
        acceptance["match"] = "best_effort"
    meta["spec_acceptance"] = acceptance
    if error := done_admission_error(root, meta, policy):
        raise RuntimeError(error)
    return str(args.note)
