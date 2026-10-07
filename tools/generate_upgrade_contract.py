# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Generate a deterministic, data-only release upgrade contract."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, cast

if __package__:
    from .validate_upgrade_contract import ContractError, validate_contract
else:  # pragma: no cover - direct script execution
    from validate_upgrade_contract import (  # type: ignore[import-not-found,no-redef]
        ContractError,
        validate_contract,
    )

PHASES = ("discover", "preflight", "quiesce", "backup", "stage", "commit", "validate", "reopen")
PHASE_OPCODES = {
    "discover": "release.inspect",
    "preflight": "admission.check",
    "quiesce": "barrier.acquire",
    "backup": "backend.backup",
    "stage": "runtime.stage",
    "commit": "authority.atomic_replace",
    "validate": "runtime.validate",
    "reopen": "barrier.reopen",
}
TRANSITION_FIELDS = {
    "operation_id",
    "backend",
    "selector_ref",
    "expected_state_revision",
    "barrier_id",
    "fencing_token",
    "from",
    "to",
}


def _validate_transition(value: Any) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ContractError("transition input must be an object")
    if set(value) != TRANSITION_FIELDS:
        raise ContractError("transition input fields are incomplete or unknown")
    if not isinstance(value["operation_id"], str):
        raise ContractError("operation_id must be a string")
    if not isinstance(value["from"], dict) or not isinstance(value["to"], dict):
        raise ContractError("from and to must be release objects")
    if value["backend"] not in {"git", "sqlite"}:
        raise ContractError("backend must be git or sqlite")
    if type(value["expected_state_revision"]) is not int or value["expected_state_revision"] < 1:
        raise ContractError("expected_state_revision must be a positive integer")
    for field in ("selector_ref", "barrier_id", "fencing_token"):
        if not isinstance(value[field], str) or not value[field]:
            raise ContractError(f"{field} must be a non-empty string")
    return value


def _load_transition(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ContractError(f"invalid transition input: {error}") from error
    return _validate_transition(value)


def _operation(
    transition: dict[str, Any], phase: str, opcode: str, *, target: str | None = None
) -> dict[str, Any]:
    operation_id = transition["operation_id"]
    operation = {
        "operation_id": f"{operation_id}:{phase}",
        "opcode": opcode,
        "inputs": {
            "backend": transition["backend"],
            "selector_ref": transition["selector_ref"],
            "expected_state_revision": transition["expected_state_revision"],
            "barrier_id": transition["barrier_id"],
            "fencing_token": transition["fencing_token"],
            "backup_operation_id": f"{operation_id}:backup",
        },
        "timeout_seconds": 300,
        "resources": ["maintenance-barrier", "durable-operation-record"],
        "preconditions": ["previous-phase-complete"],
        "postconditions": [f"{phase}-contract-satisfied"],
        "evidence": ["durable-operation-record"],
        "durable_record": "operation-id-and-outcome",
    }
    if target is not None:
        cast(dict[str, Any], operation["inputs"])["target"] = target
    return operation


def generate(transition: dict[str, Any]) -> dict[str, Any]:
    operation_id = transition["operation_id"]
    phases = []
    dependencies = {
        "discover": [],
        "preflight": ["discover"],
        "quiesce": ["preflight"],
        "backup": ["quiesce"],
        "stage": ["backup"],
        "commit": ["quiesce", "backup", "stage"],
        "validate": ["commit"],
        "reopen": ["validate"],
    }
    failure_modes = {
        "discover": "stop-before-mutation",
        "preflight": "stop-before-mutation",
        "quiesce": "stop-before-mutation",
        "backup": "stop-before-mutation",
        "stage": "restore-known-good",
        "commit": "restore-known-good",
        "validate": "restore-known-good",
        "reopen": "safe-mode",
    }
    for order, phase in enumerate(PHASES, 1):
        phases.append(
            {
                "id": phase,
                "order": order,
                "mutates_authority": phase == "commit",
                "requires": dependencies[phase],
                "on_failure": failure_modes[phase],
                "operation": _operation(transition, phase, PHASE_OPCODES[phase]),
            }
        )
    document = {
        "schema_version": 2,
        "operation_id": operation_id,
        "backend": transition["backend"],
        "from": transition["from"],
        "to": transition["to"],
        "preconditions": [
            {
                "id": "RELEASE.AUTHENTICITY",
                "effect": "read-only",
                "failure_mode": "stop-before-mutation",
                "preconditions": ["immutable-tag-and-commit"],
                "postconditions": ["release-identity-recorded"],
                "evidence": ["release-manifest", "tag-binding"],
            },
            {
                "id": "BACKEND.COMPATIBILITY",
                "effect": "validate",
                "failure_mode": "stop-before-mutation",
                "preconditions": ["backend-contracts-present", "schema-compatible"],
                "postconditions": ["backend-round-trip-plan-recorded"],
                "evidence": ["compatibility-matrix"],
            },
        ],
        "phases": phases,
        "backend_contracts": [
            {
                "backend": "git",
                "authority": ["reachable-objects", "refs", "index", "task-history"],
                "backup": ["object-and-ref-inventory", "binding", "projections"],
                "restore": ["verify-objects", "restore-refs", "verify-history"],
                "selector": ["coordinator.backend.json"],
                "projections": ["CURRENT.md", "STATUS.md"],
                "equivalence": "authority-compatible-round-trip",
            },
            {
                "backend": "sqlite",
                "authority": ["database", "wal", "shm"],
                "backup": ["online-backup-api", "binding", "projections"],
                "restore": ["integrity-check", "restore-selector", "verify-history"],
                "selector": ["coordinator.backend.json"],
                "projections": ["CURRENT.md", "STATUS.md"],
                "equivalence": "authority-compatible-round-trip",
                "wal": ["checkpoint-policy", "synchronous-full"],
            },
        ],
        "rollback": {
            "required": True,
            "backup_integrity": "backend-specific",
            "integrity_by_backend": {
                "git": "git-object-and-ref",
                "sqlite": "sqlite-integrity-and-backup-api",
            },
            "equivalence": "authority-compatible-round-trip",
            "reopen_gate": "validate-before-reopen",
            "ambiguous_external_result": "persist-operation-id-and-reconcile",
            "operation": _operation(transition, "rollback", "backend.restore", target="rollback"),
        },
    }
    validate_contract(document)
    return document


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args(argv)
    try:
        document = generate(_load_transition(args.input))
        args.output.write_text(
            json.dumps(document, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
    except (ContractError, OSError) as error:
        print(f"invalid upgrade transition: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
