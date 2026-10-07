# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Executable correspondence checks for the common/control/authority lock domain."""

from __future__ import annotations

from collections.abc import Iterable
from pathlib import Path

_ACQUIRE = {
    "AcquireCommon": "ReleaseCommon",
    "AcquireControl": "ReleaseControl",
    "AcquireAuthority": "ReleaseAuthority",
}
_RELEASE = {release: acquire for acquire, release in _ACQUIRE.items()}
_MODEL_ACTION_SIGNATURES = {
    "AcquireCommon": "AcquireCommon(p) ==",
    "AcquireControl": "AcquireControl(p) ==",
    "AcquireAuthority": "AcquireAuthority(p) ==",
    "ReleaseAuthority": "ReleaseAuthority(p) ==",
    "ReleaseControl": "ReleaseControl(p) ==",
    "ReleaseCommon": "ReleaseCommon(p) ==",
}
_MODEL_LOCK_TRANSITIONS = {
    "AcquireCommon": ('lockStage = "free"', 'lockStage\' = "common"'),
    "AcquireControl": ('lockStage = "common"', 'lockStage\' = "control"'),
    "AcquireAuthority": ('lockStage = "control"', 'lockStage\' = "authority"'),
    "ReleaseAuthority": ('lockStage\' = "control"',),
    "ReleaseControl": ('lockStage\' = "common"',),
    "ReleaseCommon": ('lockStage\' = "free"',),
}


def validate_lock_domain_model_contract(root: Path) -> None:
    """Require every concrete lock event to exist in the TLA+ model."""
    model = root / "formal/upgrade/HandoffctlUpgradeBarrier.tla"
    try:
        text = model.read_text(encoding="utf-8")
    except OSError as error:
        raise ValueError("lock-domain model is unavailable") from error
    missing = [
        f"action {action}"
        for action, signature in _MODEL_ACTION_SIGNATURES.items()
        if signature not in text
    ]
    if missing:
        raise ValueError(f"lock-domain model contract is incomplete: {', '.join(missing)}")
    missing_transitions = [
        f"transition {action}"
        for action, fragments in _MODEL_LOCK_TRANSITIONS.items()
        if not all(fragment in text for fragment in fragments)
    ]
    if missing_transitions:
        raise ValueError(
            "lock-domain model contract is missing transitions: " + ", ".join(missing_transitions)
        )


def validate_lock_domain_trace(events: Iterable[str]) -> tuple[str, ...]:
    """Validate one fully-unwound trace against the TLA+ lock nesting.

    A trace may stop after any acquisition because a failure can unwind the
    scope, but it must always contain the matching reverse releases.  This
    checks ordering and ownership shape only; it does not claim Python/TLA+
    semantic equivalence.
    """

    trace = tuple(events)
    if not trace:
        raise ValueError("lock-domain trace is empty")
    stack: list[str] = []
    for event in trace:
        if event in _ACQUIRE:
            if event in stack:
                raise ValueError("lock-domain acquisition is not reentrant")
            if (
                len(stack)
                != {"AcquireCommon": 0, "AcquireControl": 1, "AcquireAuthority": 2}[event]
            ):
                raise ValueError("lock-domain acquisition order is invalid")
            stack.append(event)
            continue
        if event in _RELEASE:
            if not stack or stack[-1] != _RELEASE[event]:
                raise ValueError("lock-domain release order is invalid")
            stack.pop()
            continue
        raise ValueError(f"unknown lock-domain action: {event}")
    if stack:
        raise ValueError("lock-domain trace did not release every lock")
    return trace
