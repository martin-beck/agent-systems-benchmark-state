# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Fail-closed semantic validation for generated upgrade contracts."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, ValidationError

if __package__:
    from .upgrade_contract_runtime import (
        INPUT_FIELDS,
        PHASE_OPCODES,
        PHASES,
        ROLLBACK_INPUT_FIELDS,
        RuntimeContractError,
        validate_runtime_contract,
    )
else:  # pragma: no cover - direct script execution
    try:
        from upgrade_contract_runtime import (  # type: ignore[import-not-found,no-redef]
            INPUT_FIELDS,
            PHASE_OPCODES,
            PHASES,
            ROLLBACK_INPUT_FIELDS,
            RuntimeContractError,
            validate_runtime_contract,
        )
    except ModuleNotFoundError:
        from tools.upgrade_contract_runtime import (
            INPUT_FIELDS,
            PHASE_OPCODES,
            PHASES,
            ROLLBACK_INPUT_FIELDS,
            RuntimeContractError,
            validate_runtime_contract,
        )

ROOT = Path(__file__).resolve().parents[1]


class ContractError(ValueError):
    """Raised when a contract is structurally or semantically unsafe."""


def validate_contract(document: dict[str, Any]) -> None:
    """Validate a complete generated contract before any upgrade mutation."""
    try:
        validate_runtime_contract(document)
    except RuntimeContractError as error:
        raise ContractError(str(error)) from error
    schema = json.loads((ROOT / "schema/handoffctl-upgrade-contract.schema.json").read_text())
    try:
        Draft202012Validator(schema).validate(document)
    except ValidationError as error:
        raise ContractError(str(error)) from error
    if document["from"] == document["to"]:
        raise ContractError("from and to release identities must differ")
    if document["from"]["version"] == document["to"]["version"]:
        raise ContractError("from and to versions must differ")
    for release in (document["from"], document["to"]):
        if release["tag_ref"] != "refs/tags/" + release["version"]:
            raise ContractError("tag reference must match release version")
    _validate_phases(document)
    _validate_backends(document)


def _validate_phases(document: dict[str, Any]) -> None:  # noqa: C901
    """Validate ordering, dependencies, operation identity, and gates."""
    phases = document["phases"]
    if [phase["id"] for phase in phases] != list(PHASES):
        raise ContractError("phase IDs must be unique and in canonical order")
    if [phase["order"] for phase in phases] != list(range(1, len(PHASES) + 1)):
        raise ContractError("phase orders must be contiguous from one")
    operation_ids: set[str] = set()
    top_operation_id = document["operation_id"]
    selected_backend = document["backend"]
    canonical_inputs: dict[str, object] | None = None
    expected_dependencies = {
        "discover": set(),
        "preflight": {"discover"},
        "quiesce": {"preflight"},
        "backup": {"quiesce"},
        "stage": {"backup"},
        "commit": {"stage", "quiesce", "backup"},
        "validate": {"commit"},
        "reopen": {"validate"},
    }
    for phase in phases:
        phase_id = phase["id"]
        if phase["mutates_authority"] != (phase_id == "commit"):
            raise ContractError("only commit may mutate authority")
        if set(phase["requires"]) != expected_dependencies[phase_id]:
            raise ContractError(f"incorrect dependencies for {phase_id}")
        operation_id = phase["operation"]["operation_id"]
        expected = f"{top_operation_id}:{phase_id}"
        if operation_id != expected or operation_id in operation_ids:
            raise ContractError(f"operation ID is not bound to {phase_id}")
        operation_ids.add(operation_id)
        operation = phase["operation"]
        if operation["opcode"] != PHASE_OPCODES[phase_id]:
            raise ContractError(f"opcode is not bound to {phase_id}")
        inputs = operation["inputs"]
        _validate_inputs(inputs, selected_backend, top_operation_id)
        if canonical_inputs is None:
            canonical_inputs = inputs
        elif inputs != canonical_inputs:
            raise ContractError("operation inputs change between phases")

    rollback = document["rollback"]["operation"]
    if rollback["operation_id"] != f"{top_operation_id}:rollback":
        raise ContractError("rollback operation ID is not bound")
    if rollback["opcode"] != "backend.restore":
        raise ContractError("rollback must use backend.restore")
    _validate_inputs(rollback["inputs"], selected_backend, top_operation_id, rollback=True)
    if {
        key: value for key, value in rollback["inputs"].items() if key != "target"
    } != canonical_inputs:
        raise ContractError("rollback inputs do not match forward operation")


def _validate_inputs(
    inputs: dict[str, object],
    backend: str,
    operation_id: str,
    *,
    rollback: bool = False,
) -> None:
    """Require one exact identity/fencing input tuple for every typed opcode."""
    expected_fields = ROLLBACK_INPUT_FIELDS if rollback else INPUT_FIELDS
    if set(inputs) != expected_fields:
        raise ContractError("operation input fields are incomplete or unknown")
    if rollback and inputs["target"] != "rollback":
        raise ContractError("rollback target is invalid")
    if inputs["backend"] != backend:
        raise ContractError("operation backend does not match selected backend")
    revision = inputs["expected_state_revision"]
    if type(revision) is not int or revision < 1:
        raise ContractError("operation state revision is invalid")
    if inputs["backup_operation_id"] != f"{operation_id}:backup":
        raise ContractError("backup operation identity is not bound")


def _validate_backends(document: dict[str, Any]) -> None:
    """Validate backend coverage and backend-specific rollback integrity."""
    if {backend["backend"] for backend in document["backend_contracts"]} != {"git", "sqlite"}:
        raise ContractError("both Git and SQLite backend contracts are required")
    integrity = document["rollback"]["integrity_by_backend"]
    if document["rollback"]["backup_integrity"] != "backend-specific":
        raise ContractError("generic rollback integrity must be backend-specific")
    if integrity != {"git": "git-object-and-ref", "sqlite": "sqlite-integrity-and-backup-api"}:
        raise ContractError("rollback integrity must match each backend")


def main(argv: list[str] | None = None) -> int:
    """Validate one contract file and return a stable CLI status."""
    args = sys.argv[1:] if argv is None else argv
    if len(args) != 1:
        print("usage: validate_upgrade_contract.py CONTRACT.json", file=sys.stderr)
        return 2
    try:
        validate_contract(json.loads(Path(args[0]).read_text()))
    except (ContractError, json.JSONDecodeError, OSError) as error:
        print(f"invalid upgrade contract: {error}", file=sys.stderr)
        return 1
    print("upgrade contract: valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
