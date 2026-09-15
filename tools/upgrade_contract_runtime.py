# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Stdlib-only strict validation for runtime upgrade contract inspection."""

from __future__ import annotations

import json
import re
from typing import Any

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
PHASES = tuple(PHASE_OPCODES)
INPUT_FIELDS = {
    "backend",
    "selector_ref",
    "expected_state_revision",
    "barrier_id",
    "fencing_token",
    "backup_operation_id",
}
_TOP_FIELDS = {
    "schema_version",
    "operation_id",
    "backend",
    "from",
    "to",
    "preconditions",
    "phases",
    "backend_contracts",
    "rollback",
}
_RELEASE_FIELDS = {
    "version",
    "source_commit",
    "tag_ref",
    "tag_object",
    "signature_sha256",
    "trust_policy_sha256",
    "vendor_manifest_sha256",
}
_OPERATION_FIELDS = {
    "operation_id",
    "opcode",
    "inputs",
    "timeout_seconds",
    "resources",
    "preconditions",
    "postconditions",
    "evidence",
    "durable_record",
}
_OPERATION_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9._:-]{0,127}")
_TOKEN = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,127}")
_SELECTOR = re.compile(r"(?!/)(?!.*(?:^|/)\.\.(?:/|$))[A-Za-z0-9._/-]{1,255}")
_VERSION = re.compile(r"v[0-9]+\.[0-9]+\.[0-9]+")
_COMMIT = re.compile(r"[0-9a-f]{40}")
_DIGEST = re.compile(r"[0-9a-f]{64}")


class RuntimeContractError(ValueError):
    """A contract is unsafe to inspect in the dependency-free runtime."""


def _mapping(value: object, fields: set[str], label: str) -> dict[str, Any]:
    if not isinstance(value, dict) or set(value) != fields:
        raise RuntimeContractError(f"{label} fields are invalid")
    return value


def _matches(value: object, pattern: re.Pattern[str], label: str) -> str:
    if not isinstance(value, str) or pattern.fullmatch(value) is None:
        raise RuntimeContractError(f"{label} is invalid")
    return value


def _choice(value: object, choices: set[str], label: str) -> str:
    if not isinstance(value, str) or value not in choices:
        raise RuntimeContractError(f"{label} is invalid")
    return value


def _string_list(value: object, label: str, *, allow_empty: bool = False) -> list[str]:
    if (
        not isinstance(value, list)
        or (not value and not allow_empty)
        or any(not isinstance(item, str) for item in value)
        or len(value) != len(set(value))
    ):
        raise RuntimeContractError(f"{label} is invalid")
    return value


def _unique_objects(value: list[object], label: str) -> None:
    encoded = [json.dumps(item, sort_keys=True, separators=(",", ":")) for item in value]
    if len(encoded) != len(set(encoded)):
        raise RuntimeContractError(f"{label} contains duplicates")


def _release(value: object, label: str) -> dict[str, Any]:
    release = _mapping(value, _RELEASE_FIELDS, label)
    version = _matches(release["version"], _VERSION, f"{label} version")
    _matches(release["source_commit"], _COMMIT, f"{label} source commit")
    _matches(release["tag_object"], _COMMIT, f"{label} tag object")
    if release["tag_ref"] != f"refs/tags/{version}":
        raise RuntimeContractError(f"{label} tag reference is invalid")
    for field in ("signature_sha256", "trust_policy_sha256", "vendor_manifest_sha256"):
        _matches(release[field], _DIGEST, f"{label} {field}")
    return release


def _check(value: object) -> None:
    fields = {"id", "effect", "failure_mode", "preconditions", "postconditions", "evidence"}
    check = _mapping(value, fields, "contract precondition")
    _matches(check["id"], re.compile(r"[A-Z0-9][A-Z0-9._:-]{1,127}"), "precondition ID")
    _choice(
        check["effect"],
        {"read-only", "quiesce", "backup", "replace", "validate", "reopen"},
        "precondition effect",
    )
    _choice(
        check["failure_mode"],
        {"stop-before-mutation", "restore-known-good", "safe-mode"},
        "precondition failure mode",
    )
    for field in ("preconditions", "postconditions", "evidence"):
        _string_list(check[field], f"precondition {field}")


def _inputs(value: object, backend: str, operation_id: str) -> dict[str, Any]:
    inputs = _mapping(value, INPUT_FIELDS, "operation inputs")
    if inputs["backend"] != backend:
        raise RuntimeContractError("operation backend identity changed")
    _matches(inputs["selector_ref"], _SELECTOR, "runtime selector reference")
    for field in ("barrier_id", "fencing_token"):
        _matches(inputs[field], _TOKEN, field)
    revision = inputs["expected_state_revision"]
    if type(revision) is not int or revision < 1:
        raise RuntimeContractError("expected state revision is invalid")
    if inputs["backup_operation_id"] != f"{operation_id}:backup":
        raise RuntimeContractError("backup operation identity is not bound")
    return inputs


def _operation(value: object, backend: str, operation_id: str) -> dict[str, Any]:
    operation = _mapping(value, _OPERATION_FIELDS, "operation")
    _matches(operation["operation_id"], _OPERATION_ID, "operation ID")
    _choice(
        operation["opcode"],
        {*PHASE_OPCODES.values(), "backend.restore"},
        "operation opcode",
    )
    _inputs(operation["inputs"], backend, operation_id)
    timeout = operation["timeout_seconds"]
    if type(timeout) is not int or not 1 <= timeout <= 86400:
        raise RuntimeContractError("operation timeout is invalid")
    for field in ("resources", "preconditions", "postconditions", "evidence"):
        _string_list(operation[field], f"operation {field}")
    _choice(
        operation["durable_record"],
        {"operation-id-and-outcome", "safe-mode-record"},
        "operation durable record",
    )
    return operation


def _backend_contract(value: object) -> str:
    if not isinstance(value, dict):
        raise RuntimeContractError("backend contract is invalid")
    backend = value.get("backend")
    fields = {"backend", "authority", "backup", "restore", "selector", "projections", "equivalence"}
    if backend == "sqlite":
        fields.add("wal")
    contract = _mapping(value, fields, "backend contract")
    _choice(backend, {"git", "sqlite"}, "backend contract identity")
    for field in ("authority", "backup", "restore", "selector", "projections"):
        _string_list(contract[field], f"backend {field}")
    if backend == "sqlite":
        _string_list(contract["wal"], "backend WAL contract")
    if contract["equivalence"] != "authority-compatible-round-trip":
        raise RuntimeContractError("backend equivalence is invalid")
    return str(backend)


def validate_runtime_contract(document: object) -> dict[str, Any]:  # noqa: C901
    """Validate the exact schema-v2 contract using only the Python standard library."""
    contract = _mapping(document, _TOP_FIELDS, "upgrade contract")
    if type(contract["schema_version"]) is not int or contract["schema_version"] != 2:
        raise RuntimeContractError("upgrade contract schema version is invalid")
    operation_id = _matches(contract["operation_id"], _OPERATION_ID, "upgrade operation ID")
    backend = contract["backend"]
    backend = _choice(backend, {"git", "sqlite"}, "upgrade backend")
    source = _release(contract["from"], "source release")
    target = _release(contract["to"], "target release")
    if source == target or source["version"] == target["version"]:
        raise RuntimeContractError("source and target releases must differ")
    preconditions = contract["preconditions"]
    if not isinstance(preconditions, list) or not preconditions:
        raise RuntimeContractError("contract preconditions are invalid")
    for precondition in preconditions:
        _check(precondition)
    _unique_objects(preconditions, "contract preconditions")

    phases = contract["phases"]
    if not isinstance(phases, list) or len(phases) != len(PHASES):
        raise RuntimeContractError("upgrade phases are invalid")
    expected_dependencies = {
        "discover": [],
        "preflight": ["discover"],
        "quiesce": ["preflight"],
        "backup": ["quiesce"],
        "stage": ["backup"],
        "commit": ["quiesce", "backup", "stage"],
        "validate": ["commit"],
        "reopen": ["validate"],
    }
    canonical_inputs: dict[str, Any] | None = None
    for order, (phase_id, value) in enumerate(zip(PHASES, phases, strict=True), 1):
        phase = _mapping(
            value,
            {"id", "order", "mutates_authority", "requires", "on_failure", "operation"},
            "upgrade phase",
        )
        if phase["id"] != phase_id or type(phase["order"]) is not int or phase["order"] != order:
            raise RuntimeContractError("phase order or identity is invalid")
        if type(phase["mutates_authority"]) is not bool or phase["mutates_authority"] is not (
            phase_id == "commit"
        ):
            raise RuntimeContractError("only commit may mutate authority")
        requires = _string_list(phase["requires"], "phase dependencies", allow_empty=True)
        if set(requires) != set(expected_dependencies[phase_id]):
            raise RuntimeContractError("phase dependencies are invalid")
        _choice(
            phase["on_failure"],
            {"stop-before-mutation", "restore-known-good", "safe-mode"},
            "phase failure mode",
        )
        operation = _operation(phase["operation"], backend, operation_id)
        if operation["operation_id"] != f"{operation_id}:{phase_id}" or (
            operation["opcode"] != PHASE_OPCODES[phase_id]
        ):
            raise RuntimeContractError("phase operation is not bound")
        inputs = operation["inputs"]
        if canonical_inputs is None:
            canonical_inputs = inputs
        elif inputs != canonical_inputs:
            raise RuntimeContractError("operation inputs change between phases")

    backend_contracts = contract["backend_contracts"]
    if not isinstance(backend_contracts, list) or len(backend_contracts) != 2:
        raise RuntimeContractError("backend contracts are invalid")
    if {_backend_contract(item) for item in backend_contracts} != {"git", "sqlite"}:
        raise RuntimeContractError("both backend contracts are required")
    _unique_objects(backend_contracts, "backend contracts")

    rollback_fields = {
        "required",
        "backup_integrity",
        "integrity_by_backend",
        "equivalence",
        "reopen_gate",
        "ambiguous_external_result",
        "operation",
    }
    rollback = _mapping(contract["rollback"], rollback_fields, "rollback contract")
    if (
        rollback["required"] is not True
        or rollback["backup_integrity"] != "backend-specific"
        or rollback["integrity_by_backend"]
        != {"git": "git-object-and-ref", "sqlite": "sqlite-integrity-and-backup-api"}
        or rollback["equivalence"] != "authority-compatible-round-trip"
        or rollback["reopen_gate"] != "validate-before-reopen"
        or not isinstance(rollback["ambiguous_external_result"], str)
        or rollback["ambiguous_external_result"]
        not in {"persist-operation-id-and-reconcile", "safe-mode"}
    ):
        raise RuntimeContractError("rollback contract is invalid")
    rollback_operation = _operation(rollback["operation"], backend, operation_id)
    if (
        rollback_operation["operation_id"] != f"{operation_id}:rollback"
        or rollback_operation["opcode"] != "backend.restore"
        or rollback_operation["inputs"] != canonical_inputs
    ):
        raise RuntimeContractError("rollback operation is not bound")
    return contract
