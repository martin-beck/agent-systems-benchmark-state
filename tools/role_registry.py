# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Fail-closed validation for the public Coordinator role registry."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, cast

from jsonschema import Draft202012Validator, RefResolver

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_SCHEMA = ROOT / "schema/role-registry.schema.json"
FORBIDDEN_ROLE_ALIASES = frozenset({"administrator", "admin-role", "root", "superuser"})


class RoleRegistryError(ValueError):
    """A role registry is malformed or violates a semantic safety rule."""


def _load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise RoleRegistryError(f"cannot read JSON registry: {path}") from error
    if not isinstance(value, dict):
        raise RoleRegistryError("role registry must be an object")
    return value


def _schema_errors(value: dict[str, Any]) -> list[str]:
    schema = _load_json(REGISTRY_SCHEMA)
    role_schema = _load_json(REGISTRY_SCHEMA.with_name("role.schema.json"))
    resolver = RefResolver(
        REGISTRY_SCHEMA.as_uri(),
        schema,
        store={role_schema["$id"]: role_schema},
    )
    validator = Draft202012Validator(schema, resolver=resolver)
    return [error.message for error in sorted(validator.iter_errors(value), key=str)]


def _semantic_errors(value: dict[str, Any]) -> list[str]:
    roles = cast(list[dict[str, Any]], value["roles"])
    role_ids = [role["role_id"] for role in roles]
    errors: list[str] = []
    if len(role_ids) != len(set(role_ids)):
        errors.append("semantic: role_id values must be unique")
    if value["default_role"] not in role_ids:
        errors.append("semantic: default_role must reference a declared role")
    for role in roles:
        role_id = role["role_id"]
        if role_id in FORBIDDEN_ROLE_ALIASES:
            errors.append(f"semantic: forbidden role alias: {role_id}")
        capability_ids = [item["capability_id"] for item in role["capabilities"]]
        if len(capability_ids) != len(set(capability_ids)):
            errors.append(f"semantic: duplicate capability_id in role: {role_id}")
        forbidden = set(role["forbidden_actions"])
        allowed = set(role["tool_policy"]["allow"])
        if forbidden & allowed:
            errors.append(f"semantic: tool action is both allowed and forbidden: {role_id}")
        capability_actions = {
            action for capability in role["capabilities"] for action in capability["actions"]
        }
        overlap = sorted(capability_actions & forbidden)
        if overlap:
            errors.append(f"semantic: capability action is forbidden ({role_id}): {overlap}")
    return errors


def registry_errors(value: object) -> list[str]:
    """Return all validation errors without accepting partial or unknown data."""
    if not isinstance(value, dict):
        return ["role registry must be an object"]
    errors = _schema_errors(value)
    if errors:
        return [f"schema: {error}" for error in errors]
    return _semantic_errors(value)


def validate_registry(value: object) -> dict[str, Any]:
    """Validate and return a detached registry value, or fail closed."""
    errors = registry_errors(value)
    if errors:
        raise RoleRegistryError("; ".join(errors))
    if not isinstance(value, dict):
        raise RoleRegistryError("role registry must be an object")
    return cast(dict[str, Any], json.loads(json.dumps(value)))


def check_registry(path: Path) -> None:
    """Validate one registry file for CI and command-line use."""
    validate_registry(_load_json(path))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("registry", type=Path)
    args = parser.parse_args()
    try:
        check_registry(args.registry)
    except RoleRegistryError as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
