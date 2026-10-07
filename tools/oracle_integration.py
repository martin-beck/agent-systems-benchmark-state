# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Offline synthetic Coordinator/AWG/AWQ trace built on typed gate events."""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from typing import Any

from tools.oracle_lifecycle import ArtifactRef, GateStage, InteractionEvent, apply_event

PUBLIC_REF = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._/-]{0,127}$")
SHA256 = re.compile(r"^sha256:[0-9a-f]{64}$")


class IntegrationTraceError(ValueError):
    """A malformed synthetic trace or evidence-boundary violation."""


def _public_ref(value: str, label: str) -> None:
    if not isinstance(value, str) or not PUBLIC_REF.fullmatch(value):
        raise IntegrationTraceError(f"{label} must be public-safe")
    if value.startswith("/") or ".." in value or "//" in value:
        raise IntegrationTraceError(f"{label} must be public-safe")


def _digest(value: str, label: str) -> None:
    if not isinstance(value, str) or not SHA256.fullmatch(value):
        raise IntegrationTraceError(f"{label} must be a sha256 digest")


def _record_digest(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


@dataclass(frozen=True, slots=True)
class AWGDecision:
    """AWG-owned decision semantics; this is the only user-intent record."""

    packet_ref: str
    decision: str
    rationale_ref: str
    decision_digest: str

    def __post_init__(self) -> None:
        _public_ref(self.packet_ref, "AWG packet_ref")
        _public_ref(self.rationale_ref, "AWG rationale_ref")
        _digest(self.decision_digest, "AWG decision_digest")
        if self.decision not in {"accept", "reject", "clarify"}:
            raise IntegrationTraceError("AWG decision is invalid")


@dataclass(frozen=True, slots=True)
class AWQEvidence:
    """AWQ-owned evidence; a passing result is deliberately non-authorizing."""

    evidence_ref: str
    quality_status: str
    evidence_class: str
    requirement_digest: str

    def __post_init__(self) -> None:
        _public_ref(self.evidence_ref, "AWQ evidence_ref")
        _digest(self.requirement_digest, "AWQ requirement_digest")
        if self.quality_status not in {"passed", "failed"}:
            raise IntegrationTraceError("AWQ quality_status is invalid")
        if self.evidence_class not in {"implementation-test", "bounded-model"}:
            raise IntegrationTraceError("AWQ evidence_class is invalid")


@dataclass(frozen=True, slots=True)
class IntegrationResult:
    """Public-safe result with exact Coordinator revision and event digests."""

    task_id: str
    final_revision: int
    event_digests: tuple[str, ...]
    awg_decision_ref: str
    awq_evidence_ref: str


def run_synthetic_trace(
    *, task_id: str, start_revision: int, awg: AWGDecision, awq: AWQEvidence
) -> IntegrationResult:
    """Run all four Coordinator gates without provider or runtime integration."""
    if not re.fullmatch(r"AR-\d{4}", task_id) or start_revision < 1:
        raise IntegrationTraceError("Coordinator task identity is invalid")
    if awg.decision != "accept":
        raise IntegrationTraceError("AWG user decision is not accepting")
    if awq.quality_status != "passed":
        raise IntegrationTraceError("AWQ quality evidence did not pass")

    meta: dict[str, Any] = {"id": task_id, "task_revision": start_revision}
    digests: list[str] = []
    for stage in GateStage:
        revision = meta["task_revision"]
        opening = _event(task_id, revision, stage, "open", "unresolved")
        digests.append(_record_digest(opening.as_record()))
        apply_event(meta, opening)
        meta["task_revision"] += 1
        revision = meta["task_revision"]
        resolving = _event(task_id, revision, stage, "resolve", "accepted")
        digests.append(_record_digest(resolving.as_record()))
        apply_event(meta, resolving)
        meta["task_revision"] += 1

    gate = meta["oracle_gate"]
    expected = [stage.value for stage in GateStage]
    if gate["authorized"] is not True or gate["completed"] != expected:
        raise IntegrationTraceError("Coordinator did not authorize the complete gate sequence")
    return IntegrationResult(
        task_id=task_id,
        final_revision=meta["task_revision"],
        event_digests=tuple(digests),
        awg_decision_ref=awg.packet_ref,
        awq_evidence_ref=awq.evidence_ref,
    )


def _event(
    task_id: str, revision: int, stage: GateStage, action: str, disposition: str
) -> InteractionEvent:
    artifact_digest = "sha256:" + ("a" if action == "open" else "b") * 64
    return InteractionEvent(
        task_id=task_id,
        task_revision=revision,
        stage=stage,
        action=action,
        disposition=disposition,
        before=(ArtifactRef("trace/before", artifact_digest),),
        after=(ArtifactRef("trace/after", artifact_digest),),
        public_ref="trace/oracle-integration",
        recorded_at="2026-09-17T00:00:00+00:00",
    )
