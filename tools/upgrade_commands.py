# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Fail-closed user-facing commands for typed coordinator upgrade contracts."""

from __future__ import annotations

import json
import os
import stat
from pathlib import Path
from typing import Any, NoReturn, cast

if __package__:
    from .upgrade_contract_runtime import RuntimeContractError, validate_runtime_contract
else:  # pragma: no cover - direct script execution
    from upgrade_contract_runtime import (  # type: ignore[import-not-found,no-redef]
        RuntimeContractError,
        validate_runtime_contract,
    )

MAX_CONTRACT_BYTES = 1024 * 1024
READ_ONLY_ACTIONS = {"check", "plan"}
MUTATING_ACTIONS = {"apply", "rollback"}


class UpgradeCommandError(RuntimeError):
    """A requested upgrade command is invalid or not safely executable."""


def _strict_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    if len(pairs) != len({key for key, _ in pairs}):
        raise ValueError("duplicate JSON object key")
    return dict(pairs)


def _reject_constant(value: str) -> NoReturn:
    raise ValueError(f"non-finite JSON constant: {value}")


def _read_contract(path: Path) -> dict[str, Any]:  # noqa: C901
    """Read one bounded regular contract without following its leaf symlink."""
    descriptor = -1
    try:
        descriptor = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK | os.O_CLOEXEC)
        status = os.fstat(descriptor)
        if not stat.S_ISREG(status.st_mode) or status.st_nlink != 1:
            raise UpgradeCommandError("upgrade contract must be a single-link regular file")
        if status.st_size > MAX_CONTRACT_BYTES:
            raise UpgradeCommandError("upgrade contract exceeds the size limit")
        chunks: list[bytes] = []
        remaining = MAX_CONTRACT_BYTES + 1
        while remaining:
            chunk = os.read(descriptor, min(65536, remaining))
            if not chunk:
                break
            chunks.append(chunk)
            remaining -= len(chunk)
        if remaining == 0:
            raise UpgradeCommandError("upgrade contract exceeds the size limit")
    except OSError as error:
        raise UpgradeCommandError("upgrade contract is unavailable or unsafe") from error
    finally:
        if descriptor >= 0:
            os.close(descriptor)
    try:
        value = json.loads(
            b"".join(chunks).decode("utf-8"),
            object_pairs_hook=_strict_object,
            parse_constant=_reject_constant,
        )
    except (UnicodeDecodeError, ValueError) as error:
        raise UpgradeCommandError("upgrade contract is not canonical JSON data") from error
    if not isinstance(value, dict):
        raise UpgradeCommandError("upgrade contract must be an object")
    document = cast(dict[str, Any], value)
    try:
        validate_runtime_contract(document)
    except RuntimeContractError as error:
        raise UpgradeCommandError("upgrade contract validation failed") from error
    return document


def _validate_selected_backend(document: dict[str, Any], selected_backend: str) -> None:
    if selected_backend not in {"git", "sqlite"}:
        raise UpgradeCommandError("selected coordinator backend is unsupported")
    if document["backend"] != selected_backend:
        raise UpgradeCommandError("upgrade contract backend does not match coordinator backend")


def _summary(document: dict[str, Any], *, include_plan: bool) -> dict[str, object]:
    """Return a path-, fence-, and host-free deterministic contract projection."""
    result: dict[str, object] = {
        "schema_version": 1,
        "kind": "agent-workflow-coordinator-upgrade-contract-check",
        "contract_schema_version": document["schema_version"],
        "operation_id": document["operation_id"],
        "backend": document["backend"],
        "from_version": document["from"]["version"],
        "to_version": document["to"]["version"],
        "valid": True,
        "executable": False,
    }
    if include_plan:
        result["kind"] = "agent-workflow-coordinator-upgrade-contract-plan"
        result["phases"] = [
            {
                "id": phase["id"],
                "operation_id": phase["operation"]["operation_id"],
                "opcode": phase["operation"]["opcode"],
                "mutates_authority": phase["mutates_authority"],
            }
            for phase in document["phases"]
        ]
        result["rollback"] = {
            "operation_id": document["rollback"]["operation"]["operation_id"],
            "opcode": document["rollback"]["operation"]["opcode"],
        }
    return result


def execute_upgrade_command(action: str, contract_path: Path, selected_backend: str) -> int:
    """Validate and report, while rejecting every unimplemented mutation path."""
    if action not in READ_ONLY_ACTIONS | MUTATING_ACTIONS:
        raise UpgradeCommandError("unknown upgrade action")
    document = _read_contract(contract_path)
    _validate_selected_backend(document, selected_backend)
    if action in MUTATING_ACTIONS:
        raise UpgradeCommandError(
            "upgrade execution protocol is incomplete; no coordinator state was mutated"
        )
    print(
        json.dumps(
            _summary(document, include_plan=action == "plan"),
            ensure_ascii=True,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        )
    )
    return 0
