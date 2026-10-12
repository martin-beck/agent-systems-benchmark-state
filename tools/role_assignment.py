# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Fail-closed validation for Coordinator role assignments."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
from pathlib import Path
from typing import Any, cast

from tools.role_registry import RoleRegistryError, _load_json

ROOT = Path(__file__).resolve().parents[1]
ASSIGNMENT_ID = re.compile(r"^[a-zA-Z0-9][a-zA-Z0-9._-]{2,63}$")
OWNER_ID = re.compile(r"^[a-zA-Z0-9][a-zA-Z0-9._:@/-]{2,127}$")
ROLE_ID = re.compile(r"^[a-z][a-z0-9-]{2,63}$")
PUBLIC_REF = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._/-]{0,127}$")
DIGEST = re.compile(r"^sha256:[0-9a-f]{64}$")
RFC3339_TIMESTAMP = re.compile(
    r"^\d{4}-\d{2}-\d{2}[Tt]\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:[Zz]|[+-]\d{2}:\d{2})$"
)


class RoleAssignmentError(ValueError):
    """A role assignment is malformed, stale, unauthorized, or unsafe."""


def _assignment_role_errors(value: object) -> list[str]:
    errors: list[str] = []
    if not isinstance(value, list) or not value:
        errors.append("assignment roles must be a non-empty array")
        return errors
    for role in value:
        if not isinstance(role, dict) or set(role) != {"role_id", "expires_at"}:
            errors.append("assignment role fields are malformed")
            continue
        if not isinstance(role["role_id"], str) or not ROLE_ID.fullmatch(role["role_id"]):
            errors.append("assignment role_id has an invalid format")
        try:
            if not isinstance(role["expires_at"], str) or not RFC3339_TIMESTAMP.fullmatch(
                role["expires_at"]
            ):
                raise ValueError
            expires = dt.datetime.fromisoformat(
                role["expires_at"].replace("Z", "+00:00").replace("z", "+00:00")
            )
            if expires.tzinfo is None:
                raise ValueError
        except ValueError:
            errors.append("assignment expires_at must be a timezone-aware date-time")
    return errors


def _evidence_errors(value: object) -> list[str]:
    errors: list[str] = []
    if not isinstance(value, list) or not value:
        errors.append("authorization_evidence must be a non-empty array")
        return errors
    for item in value:
        if not isinstance(item, dict) or set(item) != {"kind", "ref", "digest"}:
            errors.append("authorization evidence fields are malformed")
            continue
        if not isinstance(item["kind"], str) or item["kind"] not in {"review", "policy", "ticket"}:
            errors.append("authorization evidence kind is invalid")
        if not isinstance(item["ref"], str) or not PUBLIC_REF.fullmatch(item["ref"]):
            errors.append("authorization evidence ref has an invalid format")
        if not isinstance(item["digest"], str) or not DIGEST.fullmatch(item["digest"]):
            errors.append("authorization evidence digest has an invalid format")
    return errors


def _schema_errors(value: dict[str, Any]) -> list[str]:
    required = {"schema_version", "assignment_id", "owner_id", "roles", "authorization_evidence"}
    if set(value) != required:
        return ["role assignment fields are malformed"]
    errors: list[str] = []
    if (
        not isinstance(value["schema_version"], int)
        or isinstance(value["schema_version"], bool)
        or value["schema_version"] != 1
    ):
        errors.append("assignment schema_version must be 1")
    for field, pattern in (("assignment_id", ASSIGNMENT_ID), ("owner_id", OWNER_ID)):
        item = value[field]
        if not isinstance(item, str) or not pattern.fullmatch(item):
            errors.append(f"{field} has an invalid format")
    errors.extend(_assignment_role_errors(value["roles"]))
    errors.extend(_evidence_errors(value["authorization_evidence"]))
    return errors


def _semantic_errors(
    value: dict[str, Any],
    registry: dict[str, Any],
    now: dt.datetime | None,
    *,
    check_expiry: bool = True,
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
    if check_expiry:
        current = now or dt.datetime.now(dt.UTC)
        if current.tzinfo is None:
            errors.append("semantic: validation time must be timezone-aware")
        else:
            for item in assignments:
                expires = dt.datetime.fromisoformat(
                    item["expires_at"].replace("Z", "+00:00").replace("z", "+00:00")
                )
                if expires <= current:
                    errors.append(f"semantic: expired role assignment: {item['role_id']}")
    return errors


def assignment_errors(
    value: object,
    registry: object,
    *,
    now: dt.datetime | None = None,
    check_expiry: bool = True,
) -> list[str]:
    """Return schema, registry-reference, expiry, and evidence errors."""
    if not isinstance(value, dict):
        return ["role assignment must be an object"]
    errors = _schema_errors(value)
    if errors:
        return [f"schema: {error}" for error in errors]
    if not isinstance(registry, dict):
        return ["registry: role registry must be an object"]
    return errors + _semantic_errors(value, registry, now, check_expiry=check_expiry)


def validate_assignment(
    value: object,
    registry: object,
    *,
    now: dt.datetime | None = None,
    check_expiry: bool = True,
) -> dict[str, Any]:
    """Validate and return a detached assignment, or fail closed."""
    errors = assignment_errors(value, registry, now=now, check_expiry=check_expiry)
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
