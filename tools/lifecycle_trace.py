# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Immutable lifecycle observations for bounded formal correspondence."""

from __future__ import annotations

from dataclasses import dataclass, field
from itertools import pairwise
from pathlib import Path
from typing import Protocol

MODEL_ACTIONS = {
    "acquire": "Preflight",
    "quiesce": "Quiesce",
    "backup": "Backup",
    "stage": "Stage",
    "commit": "Commit",
    "validate": "Validate",
    "reopen": "Reopen",
    "rollback_started": "StartRollback",
    "rollback_verified": "VerifyRollback",
    "rollback_released": "ReleaseRollback",
}
MODEL_TRANSITIONS = {
    "acquire": frozenset({"quiesce", "rollback_started"}),
    "quiesce": frozenset({"backup", "rollback_started"}),
    "backup": frozenset({"stage", "rollback_started"}),
    "stage": frozenset({"commit", "rollback_started"}),
    "commit": frozenset({"validate", "rollback_started"}),
    "validate": frozenset({"reopen", "rollback_started"}),
    "reopen": frozenset({"rollback_started"}),
    "rollback_started": frozenset({"rollback_verified"}),
    "rollback_verified": frozenset({"rollback_released"}),
    "rollback_released": frozenset(),
}
MODEL_ACTION_TRANSITIONS = {
    "Preflight": (
        'phase[op] = "discover"',
        'phase\' = [phase EXCEPT ![op] = "preflight"]',
        "fence' = [fence EXCEPT ![op] = @ + 1]",
    ),
    "Quiesce": (
        'phase[op] = "preflight"',
        'barrier\' = [barrier EXCEPT ![op] = "held"]',
        'phase\' = [phase EXCEPT ![op] = "quiesce"]',
    ),
    "Backup": (
        'phase[op] = "quiesce" /\\ barrier[op] = "held"',
        "backup' = [backup EXCEPT ![op] = TRUE]",
        'phase\' = [phase EXCEPT ![op] = "backup"]',
    ),
    "Stage": (
        'phase[op] = "backup" /\\ backup[op]',
        'phase\' = [phase EXCEPT ![op] = "stage"]',
    ),
    "Commit": (
        'phase[op] = "stage" /\\ backup[op] /\\ barrier[op] = "held"',
        'phase\' = [phase EXCEPT ![op] = "commit"]',
        'runtime\' = [runtime EXCEPT ![op] = "new"]',
    ),
    "Validate": (
        'phase[op] = "commit" /\\ runtime[op] = "new"',
        'phase\' = [phase EXCEPT ![op] = "validate"]',
    ),
    "Reopen": (
        'phase[op] = "validate" /\\ barrier[op] = "held"',
        'phase\' = [phase EXCEPT ![op] = "reopen"]',
        'barrier\' = [barrier EXCEPT ![op] = "released"]',
        'journal\' = [journal EXCEPT ![op] = "completed"]',
    ),
    "StartRollback": (
        'journal[op] \\in {"running", "safe_mode"}',
        'backup[op] /\\ barrier[op] = "held"',
        'target\' = [target EXCEPT ![op] = "rollback"]',
        'journal\' = [journal EXCEPT ![op] = "rollback_started"]',
    ),
    "VerifyRollback": (
        'journal[op] = "rollback_started" /\\ target[op] = "rollback"',
        'journal\' = [journal EXCEPT ![op] = "rollback_verified"]',
    ),
    "ReleaseRollback": (
        'journal[op] = "rollback_verified" /\\ barrier[op] = "held"',
        'barrier\' = [barrier EXCEPT ![op] = "released"]',
        'journal\' = [journal EXCEPT ![op] = "rolled_back"]',
        'runtime\' = [runtime EXCEPT ![op] = "old"]',
    ),
}
MODEL_RECOVERY_TRANSITIONS = {
    "Crash": (
        'barrier[op] = "held"',
        'journal[op] \\in {"running", "rollback_verified"}',
        'barrier\' = [barrier EXCEPT ![op] = "ambiguous"]',
        'IF journal[op] = "running"',
        'journal\' = [journal EXCEPT ![op] = "safe_mode"]',
    ),
    "Recover": (
        'journal[op] = "rollback_verified" /\\ barrier[op] = "released"',
        'journal\' = [journal EXCEPT ![op] = "rolled_back"]',
        'runtime\' = [runtime EXCEPT ![op] = "old"]',
        'journal[op] = "safe_mode" /\\ barrier[op] = "ambiguous" /\\ backup[op]',
        'target\' = [target EXCEPT ![op] = "rollback"]',
        'barrier\' = [barrier EXCEPT ![op] = "held"]',
        'journal\' = [journal EXCEPT ![op] = "rollback_started"]',
    ),
}
MODEL_INVARIANTS = {
    "FunctionalAvailability": r"\A op \in Operations: available[op]",
    "NoReplacementBeforeBackup": 'runtime[op] = "new" => backup[op]',
    "ReleaseOrder": r'barrier[op] = "released" => journal[op] \in {"completed", "rolled_back"}',
    "RollbackProof": (
        'journal[op] = "rolled_back" => target[op] = "rollback" /\\ runtime[op] = "old"'
    ),
    "RollbackRequiresBackup": 'journal[op] = "rolled_back" => backup[op]',
}
MODEL_TYPE_FIELDS = (
    "phase \\in [Operations -> Phases]",
    "target \\in [Operations -> Targets]",
    "backend \\in [Operations -> Backends]",
    "barrier \\in [Operations -> Barriers]",
    "journal \\in [Operations -> Journals]",
    "runtime \\in [Operations -> Releases]",
    "backup \\in [Operations -> BOOLEAN]",
    "fence \\in [Operations -> Nat]",
    "available \\in [Operations -> BOOLEAN]",
)


def validate_model_action_contract(root: Path) -> None:
    """Require every trace action to remain defined by the authoritative TLA+ model."""
    model = root / "formal/upgrade/UpgradeRecovery.tla"
    try:
        text = model.read_text(encoding="utf-8")
    except OSError as error:
        raise ValueError("authoritative upgrade model is unavailable") from error
    definitions = {
        "Preflight": ("Preflight(op) ==",),
        "Quiesce": ("Quiesce(op) ==",),
        "Backup": ("BackupGit(op) ==", "BackupSQLite(op) =="),
        "Stage": ("Stage(op) ==",),
        "Commit": ("Commit(op) ==",),
        "Validate": ("Validate(op) ==",),
        "Reopen": ("Reopen(op) ==",),
        "StartRollback": ("StartRollback(op) ==",),
        "VerifyRollback": ("VerifyRollback(op) ==",),
        "ReleaseRollback": ("ReleaseRollback(op) ==",),
    }
    missing = [
        action
        for action, names in definitions.items()
        if (action == "Backup" and not all(name in text for name in names))
        or (action != "Backup" and not any(name in text for name in names))
    ]
    required_invariants = tuple(f"{name} ==" for name in MODEL_INVARIANTS)
    missing.extend(
        f"invariant {name.split()[0]}" for name in required_invariants if name not in text
    )
    missing.extend(
        f"invariant {name} semantics"
        for name, fragment in MODEL_INVARIANTS.items()
        if fragment not in text
    )
    missing.extend(
        f"TypeInvariant field {fragment}" for fragment in MODEL_TYPE_FIELDS if fragment not in text
    )
    if "THEOREM Spec => []TypeInvariant" not in text:
        missing.append("theorem TypeInvariant")
    if "THEOREM Spec => []FunctionalAvailability" not in text:
        missing.append("theorem FunctionalAvailability")
    if "THEOREM Spec => []NoReplacementBeforeBackup" not in text:
        missing.append("theorem NoReplacementBeforeBackup")
    missing.extend(
        f"{action} transition {fragment}"
        for action, fragments in MODEL_ACTION_TRANSITIONS.items()
        for fragment in fragments
        if fragment not in text
    )
    missing.extend(
        f"{action} transition {fragment}"
        for action, fragments in MODEL_RECOVERY_TRANSITIONS.items()
        for fragment in fragments
        if fragment not in text
    )
    if missing:
        raise ValueError(f"model actions or transitions are missing: {', '.join(missing)}")


def validate_terminal_recovery_contract(root: Path) -> None:
    """Require terminal success state to be explicit in the barrier model."""
    model = root / "formal/upgrade/HandoffctlUpgradeBarrier.tla"
    try:
        text = model.read_text(encoding="utf-8")
    except OSError as error:
        raise ValueError("terminal recovery model is unavailable") from error
    required = (
        'Targets == {"new", "rollback"}',
        'TerminalResults == {"none", "new", "rollback"}',
        "VerifyTerminal(p, target) ==",
        "ControlHeld(p)",
        "AuthorityHeld(p)",
        "activeAttempt = p",
        "terminalTarget = NoTarget",
        "terminalTarget",
        "terminalVerified",
        "freshRuntimeVerified",
        'IF target = "new"',
        "rollbackChild # NoChild",
        "ELSE rollbackChild # NoChild",
        "~terminalVerified",
        "terminalTarget' = target",
        "terminalVerified' = TRUE",
        "freshRuntimeVerified' = TRUE",
        "BeginReopen(p) ==",
        "authorityRechecked",
        "controlRevision < MaxRevision",
        "CompleteReopen(p) ==",
        'sessionStatus = "releasing"',
        'sessionStatus\' = "released"',
        "controlRevision' = controlRevision + 1",
        "FreshRuntimeRead(p) ==",
        "NoUnheldRollbackGap",
        "terminalTarget \\in Targets",
        "THEOREM Spec => []TypeOK",
        "THEOREM Spec => []NoUnheldRollbackGap",
        "THEOREM Spec => []ReleaseEvidence",
        "THEOREM Spec => []WriterDrainOnAcquire",
        "THEOREM Spec => []StaleCASRejected",
        "THEOREM Spec => []RecheckEvidence",
        "THEOREM Spec => []AmbiguousIsWriteClosed",
        "THEOREM Spec => []LockOwnership",
        "THEOREM Spec => []LockOrder",
        "THEOREM Spec => []CasBounded",
        "THEOREM Spec => []WriteFence",
        "THEOREM Spec => []IdentityStable",
        "THEOREM Spec => []ChildIdentityStable",
        "THEOREM Spec => []OneActiveSession",
    )
    missing = [name for name in required if name not in text]
    if missing:
        raise ValueError(f"terminal recovery model fields are missing: {', '.join(missing)}")


@dataclass(frozen=True, slots=True, init=False)
class LifecycleEvent:
    phase: str
    revision: int
    owner: str
    lock: str
    project_id: str
    session_digest: str
    fencing_token: str
    terminal_target: str | None
    _scope_proof: object = field(repr=False, compare=False)

    def __init__(self, *_args: object, **_kwargs: object) -> None:
        raise TypeError("lifecycle events are scope-issued")


def _issue_event(
    scope_proof: object,
    phase: str,
    revision: int,
    owner: str,
    lock: str,
    project_id: str,
    session_digest: str,
    fencing_token: str,
    *,
    terminal_target: str | None = None,
) -> LifecycleEvent:
    event = object.__new__(LifecycleEvent)
    object.__setattr__(event, "phase", phase)
    object.__setattr__(event, "revision", revision)
    object.__setattr__(event, "owner", owner)
    object.__setattr__(event, "lock", lock)
    object.__setattr__(event, "project_id", project_id)
    object.__setattr__(event, "session_digest", session_digest)
    object.__setattr__(event, "fencing_token", fencing_token)
    object.__setattr__(event, "terminal_target", terminal_target)
    object.__setattr__(event, "_scope_proof", scope_proof)
    return event


class LifecycleObserver(Protocol):
    def __call__(self, event: LifecycleEvent) -> None: ...


def _validate_event_schema(events: tuple[LifecycleEvent, ...]) -> None:
    for event in events:
        if type(event.revision) is not int or event.revision < 0:
            raise ValueError("lifecycle trace revision is invalid")
        if any(
            type(value) is not str or not value
            for value in (
                event.owner,
                event.lock,
                event.project_id,
                event.session_digest,
                event.fencing_token,
            )
        ):
            raise ValueError("lifecycle trace identity is invalid")
        if event.terminal_target not in (None, "new", "rollback"):
            raise ValueError("lifecycle trace terminal target is invalid")
        if event.phase not in ("reopen", "rollback_released") and event.terminal_target is not None:
            raise ValueError("lifecycle trace terminal target is premature")
    identity = (
        events[0].owner,
        events[0].lock,
        events[0].project_id,
        events[0].session_digest,
        events[0].fencing_token,
    )
    if any(
        (event.owner, event.lock, event.project_id, event.session_digest, event.fencing_token)
        != identity
        for event in events
    ):
        raise ValueError("lifecycle trace identity changed")
    if any(left.revision > right.revision for left, right in pairwise(events)):
        raise ValueError("lifecycle trace revision regressed")


def validate_model_trace(
    events: tuple[LifecycleEvent, ...], *, model_root: Path | None = None
) -> tuple[str, ...]:
    """Map one scope-issued lifecycle trace to UpgradeRecovery actions.

    The private issuance token binds every event to the same trusted scope;
    callers cannot construct events directly or mix observations from scopes.
    """
    if not events:
        raise ValueError("lifecycle trace must not be empty")
    if any(not isinstance(event, LifecycleEvent) for event in events):
        raise ValueError("lifecycle trace contains an invalid event")
    contract_root = model_root or Path(__file__).resolve().parents[1]
    validate_model_action_contract(contract_root)
    validate_terminal_recovery_contract(contract_root)
    scope_proof = events[0]._scope_proof
    if any(event._scope_proof is not scope_proof for event in events):
        raise ValueError("lifecycle trace mixes scope-issued events")
    _validate_event_schema(events)
    phases = tuple(event.phase for event in events)
    if any(phase not in MODEL_ACTIONS for phase in phases):
        raise ValueError("lifecycle trace phase is not mapped to the model")
    if any(
        next_phase not in MODEL_TRANSITIONS[current_phase]
        for current_phase, next_phase in pairwise(phases)
    ):
        raise ValueError("lifecycle trace transition is not allowed by the model")
    return tuple(MODEL_ACTIONS[phase] for phase in phases)


def validate_terminal_outcome(
    events: tuple[LifecycleEvent, ...], *, model_root: Path | None = None
) -> str:
    """Validate that a trusted lifecycle trace reaches one model terminal outcome.

    A trace is usable for release only after forward reopen of the new target or
    after rollback verification and release of the old target.  Incomplete
    traces and target mismatches are rejected so callers cannot treat a durable
    prefix as a healthy coordinator state.
    """
    validate_model_trace(events, model_root=model_root)
    phases = tuple(event.phase for event in events)
    terminal = events[-1]
    if phases == ("acquire", "quiesce", "backup", "stage", "commit", "validate", "reopen"):
        if terminal.terminal_target != "new":
            raise ValueError("forward terminal outcome has wrong target")
        return "new"
    if (
        len(phases) >= 6
        and phases[:3] == ("acquire", "quiesce", "backup")
        and phases[-3:] == ("rollback_started", "rollback_verified", "rollback_released")
    ):
        if terminal.terminal_target != "rollback":
            raise ValueError("rollback terminal outcome has wrong target")
        return "rollback"
    raise ValueError("lifecycle trace terminal outcome is incomplete")
