# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Bounded executable model for hostile oracle-gate traces.

This is a finite transition checker for the same ordering contract as
``oracle_lifecycle``.  It intentionally makes no claim about AWG/AWQ decision
semantics or a required Python implementation refinement proof; source and
executable tests are the operational authority.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product

STAGES = ("intake", "discussion", "formal_spec_review", "reconciliation")
OPS = ("open", "resolve", "claim", "run", "release")


@dataclass(frozen=True, slots=True)
class State:
    revision: int
    completed: tuple[str, ...]
    open_stage: str | None


def step(
    state: State, operation: str, stage: str, expected_revision: int, disposition: str
) -> State:
    """Return the state after one bounded action, or raise on rejection."""
    if expected_revision != state.revision:
        raise ValueError("stale event")
    if operation in {"claim", "run", "release"} and state.open_stage is not None:
        raise ValueError("interaction gate unresolved")
    if operation == "open":
        if state.open_stage is not None or stage != STAGES[len(state.completed)]:
            raise ValueError("skipped gate")
        return State(state.revision + 1, state.completed, stage)
    if operation == "resolve":
        if state.open_stage != stage:
            raise ValueError("resolve does not match gate")
        if disposition == "unresolved":
            return State(state.revision + 1, state.completed, stage)
        return State(state.revision + 1, (*state.completed, stage), None)
    if operation in {"claim", "run", "release"}:
        return State(state.revision + 1, state.completed, state.open_stage)
    raise ValueError("unknown operation")


def check_bounded_model() -> dict[str, int]:
    """Exhaustively explore short traces and assert safety properties."""
    states = {State(1, (), None)}
    accepted = rejected = hostile = 0
    for _ in range(len(STAGES) * 2):
        next_states: set[State] = set()
        for state, operation, stage, disposition in product(
            states, OPS, STAGES, ("accepted", "unresolved")
        ):
            try:
                candidate = step(state, operation, stage, state.revision, disposition)
            except ValueError as error:
                rejected += 1
                if str(error) in {"skipped gate", "stale event", "interaction gate unresolved"}:
                    hostile += 1
                continue
            accepted += 1
            if (
                candidate.open_stage is not None
                and candidate.open_stage != STAGES[len(candidate.completed)]
            ):  # pragma: no cover - defensive invariant
                raise AssertionError("open gate skipped the ordered lifecycle")
            if len(candidate.completed) > len(STAGES):
                raise AssertionError("completed gate sequence exceeded bound")  # pragma: no cover
            next_states.add(candidate)
        states = next_states
    if hostile == 0 or accepted == 0:
        raise AssertionError(
            "bounded model did not cover accepted and hostile traces"
        )  # pragma: no cover
    return {"states": len(states), "accepted": accepted, "rejected": rejected, "hostile": hostile}


if __name__ == "__main__":
    print(check_bounded_model())
