# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Typed, public-safe interaction gates owned by Coordinator.

The module deliberately models only gate ordering and evidence binding.  It
does not interpret the user's decision or own AWG/AWQ decision semantics.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import re
from collections.abc import Mapping
from dataclasses import dataclass
from enum import StrEnum
from typing import Any

GATE_SEQUENCE = ("intake", "discussion", "formal_spec_review", "reconciliation")
SHA256 = re.compile(r"^sha256:[0-9a-f]{64}$")
PUBLIC_REF = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._/-]{0,127}$")
DISPOSITIONS = frozenset(
    {"accepted", "rejected", "clarify", "user-added-option", "contradiction", "unresolved"}
)
NON_AUTHORIZING_DISPOSITIONS = frozenset(
    {"rejected", "clarify", "user-added-option", "contradiction", "unresolved"}
)
ACTIONS = frozenset({"open", "resolve", "reopen"})
MAX_DISCUSSION_ROUNDS = 16


class GateStage(StrEnum):
    INTAKE = "intake"
    DISCUSSION = "discussion"
    FORMAL_SPEC_REVIEW = "formal_spec_review"
    RECONCILIATION = "reconciliation"


class GateError(ValueError):
    """A malformed, stale, skipped, or unresolved interaction transition."""


def _public_ref(value: str, label: str) -> str:
    if not isinstance(value, str) or not PUBLIC_REF.fullmatch(value):
        raise GateError(f"{label} must be a public-safe reference")
    if value.startswith("/") or ".." in value or "//" in value:
        raise GateError(f"{label} must be a public-safe reference")
    return value


def _digest(value: str, label: str) -> str:
    if not isinstance(value, str) or not SHA256.fullmatch(value):
        raise GateError(f"{label} must be a sha256 digest")
    return value


@dataclass(frozen=True, slots=True)
class ArtifactRef:
    """A named public artifact and its content digest."""

    ref: str
    digest: str

    def __post_init__(self) -> None:
        _public_ref(self.ref, "artifact ref")
        _digest(self.digest, "artifact digest")

    def as_record(self) -> dict[str, str]:
        return {"ref": self.ref, "digest": self.digest}


@dataclass(frozen=True, slots=True)
class InteractionEvent:
    """One revision-bound user interaction gate event."""

    task_id: str
    task_revision: int
    stage: GateStage
    action: str
    disposition: str
    before: tuple[ArtifactRef, ...]
    after: tuple[ArtifactRef, ...]
    public_ref: str
    recorded_at: str

    def __post_init__(self) -> None:
        if not re.fullmatch(r"AR-\d{4}", self.task_id):
            raise GateError("event task_id is invalid")
        if self.task_revision < 1:
            raise GateError("event task_revision must be positive")
        if self.action not in ACTIONS:
            raise GateError("unknown interaction event action")
        if self.disposition not in DISPOSITIONS:
            raise GateError("unknown interaction disposition")
        if not self.before or not self.after:
            raise GateError("interaction event requires before and after artifacts")
        _public_ref(self.public_ref, "event public_ref")
        try:
            parsed = dt.datetime.fromisoformat(self.recorded_at.replace("Z", "+00:00"))
        except ValueError as error:
            raise GateError("event recorded_at is invalid") from error
        if parsed.tzinfo is None:
            raise GateError("event recorded_at requires a timezone")

    @classmethod
    def from_record(cls, value: Mapping[str, Any]) -> InteractionEvent:
        required = {
            "task_id",
            "task_revision",
            "stage",
            "action",
            "disposition",
            "before",
            "after",
            "public_ref",
            "recorded_at",
        }
        if set(value) != required:
            raise GateError("interaction event fields are incomplete or unknown")

        def refs(name: str) -> tuple[ArtifactRef, ...]:
            raw = value[name]
            if not isinstance(raw, list):
                raise GateError(f"event {name} must be a list")
            try:
                return tuple(ArtifactRef(str(item["ref"]), str(item["digest"])) for item in raw)
            except (KeyError, TypeError) as error:
                raise GateError(f"event {name} contains an invalid artifact") from error

        try:
            stage = GateStage(str(value["stage"]))
        except ValueError as error:
            raise GateError("unknown interaction gate stage") from error
        return cls(
            task_id=str(value["task_id"]),
            task_revision=int(value["task_revision"]),
            stage=stage,
            action=str(value["action"]),
            disposition=str(value["disposition"]),
            before=refs("before"),
            after=refs("after"),
            public_ref=str(value["public_ref"]),
            recorded_at=str(value["recorded_at"]),
        )

    def as_record(self) -> dict[str, Any]:
        return {
            "task_id": self.task_id,
            "task_revision": self.task_revision,
            "stage": self.stage.value,
            "action": self.action,
            "disposition": self.disposition,
            "before": [item.as_record() for item in self.before],
            "after": [item.as_record() for item in self.after],
            "public_ref": self.public_ref,
            "recorded_at": self.recorded_at,
        }


def _digest_record(value: Mapping[str, Any]) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def gate_errors(value: object) -> list[str]:  # noqa: C901
    """Validate an optional task ``oracle_gate`` record without changing it."""
    if value is None:
        return []
    if not isinstance(value, dict):
        return ["oracle_gate must be an object"]
    required = {"required", "open_stage", "completed", "events"}
    if not required.issubset(value) or set(value) - {
        *required,
        "authorized",
        "discussion_rounds",
        "reconciliation_required",
    }:
        return ["oracle_gate fields are incomplete or unknown"]
    if value["required"] is not True:
        return ["oracle_gate.required must be true"]
    open_stage = value["open_stage"]
    if open_stage is not None and open_stage not in GATE_SEQUENCE:
        return ["oracle_gate.open_stage is invalid"]
    completed = value["completed"]
    if not isinstance(completed, list) or any(item not in GATE_SEQUENCE for item in completed):
        return ["oracle_gate.completed is invalid"]
    rounds = value.get("discussion_rounds", 0)
    if not isinstance(rounds, int) or not 0 <= rounds <= MAX_DISCUSSION_ROUNDS:
        return ["oracle_gate.discussion_rounds is invalid"]
    if not isinstance(value.get("authorized", False), bool):
        return ["oracle_gate.authorized is invalid"]
    if not isinstance(value.get("reconciliation_required", False), bool):
        return ["oracle_gate.reconciliation_required is invalid"]
    events = value["events"]
    if not isinstance(events, list) or len(events) > 32:
        return ["oracle_gate.events is invalid or unbounded"]
    for item in events:
        try:
            InteractionEvent.from_record(item)
        except (GateError, KeyError, TypeError, ValueError) as error:
            return [f"oracle_gate event invalid: {error}"]
    return []


def transition_allowed(meta: Mapping[str, Any], operation: str) -> None:
    """Reject autonomous lifecycle operations while a required gate is open."""
    gate = meta.get("oracle_gate")
    legacy_authorized = (
        (
            ("completed" not in gate or gate.get("completed", []) == list(GATE_SEQUENCE))
            and not gate.get("open_stage")
            and not gate.get("reconciliation_required", False)
            and "authorized" not in gate
        )
        if isinstance(gate, dict)
        else False
    )
    if (
        isinstance(gate, dict)
        and gate.get("required") is True
        and (gate.get("open_stage") or gate.get("authorized", legacy_authorized) is not True)
        and operation in {"promote", "claim", "run", "release"}
    ):
        reason = gate.get("open_stage") or "reconciliation"
        raise GateError(f"interaction gate unresolved: {reason}")


def apply_event(meta: dict[str, Any], event: InteractionEvent) -> str:  # noqa: C901
    """Apply one event to task metadata and return a stable audit note."""
    if event.task_id != meta.get("id"):
        raise GateError("event task_id does not match task")
    if event.task_revision != meta.get("task_revision"):
        raise GateError("stale interaction event revision")
    current = meta.get("oracle_gate") or {
        "required": True,
        "open_stage": None,
        "completed": [],
        "events": [],
        "authorized": False,
        "discussion_rounds": 0,
        "reconciliation_required": False,
    }
    errors = gate_errors(current)
    if errors:
        raise GateError(errors[0])
    open_stage = current["open_stage"]
    completed = list(current["completed"])
    current.setdefault("authorized", False)
    current.setdefault("discussion_rounds", 0)
    current.setdefault("reconciliation_required", False)
    index = GATE_SEQUENCE.index(event.stage.value)
    if event.action == "open":
        if open_stage is not None:
            raise GateError("interaction gate already open")
        if event.stage.value in completed or index != len(completed):
            raise GateError("interaction gate skipped or already completed")
        current["open_stage"] = event.stage.value
    elif event.action == "resolve":
        if open_stage != event.stage.value:
            raise GateError("interaction event does not match open gate")
        if event.disposition == "accepted":
            current["open_stage"] = None
            completed.append(event.stage.value)
        else:
            current["open_stage"] = event.stage.value
            if current["discussion_rounds"] >= MAX_DISCUSSION_ROUNDS:
                raise GateError("repeated discussion limit exceeded")
            current["discussion_rounds"] += 1
            current["reconciliation_required"] = True
    else:  # reopen
        if event.stage.value not in completed or open_stage is not None:
            raise GateError("only a completed gate can be reopened")
        completed = completed[:index]
        current["open_stage"] = event.stage.value
        if current["discussion_rounds"] >= MAX_DISCUSSION_ROUNDS:
            raise GateError("repeated discussion limit exceeded")
        current["discussion_rounds"] += 1
        current["reconciliation_required"] = True
    if (
        event.action == "resolve"
        and event.disposition == "accepted"
        and event.stage is GateStage.RECONCILIATION
    ):
        current["reconciliation_required"] = False
    current["completed"] = completed
    current["authorized"] = (
        current["open_stage"] is None
        and completed == list(GATE_SEQUENCE)
        and not current["reconciliation_required"]
    )
    current["events"] = [*current["events"], event.as_record()]
    if len(current["events"]) > 32:
        raise GateError("interaction event history is bounded at 32 events")
    meta["oracle_gate"] = current
    digest = _digest_record(event.as_record())
    return f"Recorded {event.action} interaction gate {event.stage.value}; event={digest}."
