# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Fail-closed validation for Coordinator role assignments."""

from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path
from typing import Any, cast

from jsonschema import Draft202012Validator

from tools.role_registry import RoleRegistryError, _load_json

ROOT = Path(__file__).resolve().parents[1]
ASSIGNMENT_SCHEMA = ROOT / "schema/role-assignment.schema.json"


class RoleAssignmentError(ValueError):
    """A role assignment is malformed, stale, unauthorized, or unsafe."""


def _schema_errors(value: dict[str, Any]) -> list[str]:
    schema = _load_json(ASSIGNMENT_SCHEMA)
    validator = Draft202012Validator(schema, format_checker=Draft202012Validator.FORMAT_CHECKER)
    return [error.message for error in sorted(validator.iter_errors(value), key=str)]


def _semantic_errors(
    value: dict[str, Any], registry: dict[str, Any], now: dt.datetime | None
) -> list[str]:
    roles = registry.get("roles")
    if not isinstance(roles, list):
        return ["registry: roles are unavailable"]
    known_roles = {item.get("role_id") for item in roles if isinstance(item, dict)}
    assignments = cast(list[dict[str, Any]], value["roles"])
    role_ids = [item["role_id"] for item in assignments]
    errors: list[str] = []
    if len(role_ids) != len(set(role_ids)):
        errors.append("semantic: one owner cannot receive a role more than once")
    unknown = sorted(set(role_ids) - known_roles)
    if unknown:
        errors.append(f"semantic: unknown role: {unknown}")
    current = now or dt.datetime.now(dt.UTC)
    if current.tzinfo is None:
        errors.append("semantic: validation time must be timezone-aware")
    else:
        for item in assignments:
            expires = dt.datetime.fromisoformat(item["expires_at"].replace("Z", "+00:00"))
            if expires <= current:
                errors.append(f"semantic: expired role assignment: {item['role_id']}")
    return errors


def assignment_errors(
    value: object,
    registry: object,
    *,
    now: dt.datetime | None = None,
) -> list[str]:
    """Return schema, registry-reference, expiry, and evidence errors."""
    if not isinstance(value, dict):
        return ["role assignment must be an object"]
    errors = _schema_errors(value)
    if errors:
        return [f"schema: {error}" for error in errors]
    if not isinstance(registry, dict):
        return ["registry: role registry must be an object"]
    return errors + _semantic_errors(value, registry, now)


def validate_assignment(
    value: object,
    registry: object,
    *,
    now: dt.datetime | None = None,
) -> dict[str, Any]:
    """Validate and return a detached assignment, or fail closed."""
    errors = assignment_errors(value, registry, now=now)
    if errors:
        raise RoleAssignmentError("; ".join(errors))
    if not isinstance(value, dict):
        raise RoleAssignmentError("role assignment must be an object")
    return cast(dict[str, Any], json.loads(json.dumps(value)))


def check_assignment(path: Path, registry_path: Path, *, now: dt.datetime | None = None) -> None:
    """Validate one assignment against one role registry."""
    try:
        validate_assignment(_load_json(path), _load_json(registry_path), now=now)
    except RoleRegistryError as error:
        raise RoleAssignmentError(str(error)) from error


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("assignment", type=Path)
    parser.add_argument("registry", type=Path)
    args = parser.parse_args()
    try:
        check_assignment(args.assignment, args.registry)
    except RoleAssignmentError as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
