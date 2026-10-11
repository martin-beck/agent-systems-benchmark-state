# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Fail-closed validation for the public Coordinator role registry."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any, cast

ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN_ROLE_ALIASES = frozenset({"administrator", "admin-role", "root", "superuser"})
ROLE_ID = re.compile(r"^[a-z][a-z0-9-]{2,63}$")
ACTION = re.compile(r"^[a-z][a-z0-9_.:-]{1,63}$")
PUBLIC_REF = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._/-]{0,127}$")
PATH_PATTERN = re.compile(r"^[\s\S]{1,200}$")


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


def _exact_object(value: object, required: set[str], label: str) -> list[str]:
    if not isinstance(value, dict):
        return [f"{label} must be an object"]
    errors: list[str] = []
    missing = sorted(required - set(value))
    unknown = sorted(set(value) - required)
    if missing:
        errors.append(f"{label} is missing required fields: {missing}")
    if unknown:
        errors.append(f"{label} has unknown fields: {unknown}")
    return errors


def _string(
    value: object, label: str, pattern: re.Pattern[str], minimum: int, maximum: int
) -> list[str]:
    if not isinstance(value, str):
        return [f"{label} must be a string"]
    if not minimum <= len(value) <= maximum:
        return [f"{label} length must be between {minimum} and {maximum}"]
    if not pattern.fullmatch(value):
        return [f"{label} has an invalid format"]
    return []


def _unique_strings(
    value: object, label: str, *, minimum: int, pattern: re.Pattern[str]
) -> list[str]:
    if not isinstance(value, list) or any(not isinstance(item, str) for item in value):
        return [f"{label} must be an array of strings"]
    if len(value) < minimum:
        return [f"{label} must contain at least {minimum} items"]
    if len(value) != len(set(value)):
        return [f"{label} must not contain duplicates"]
    return [error for item in value for error in _string(item, label, pattern, 1, 200)]


def _capability_errors(value: object) -> list[str]:
    required = {"capability_id", "description", "actions", "scope"}
    errors = _exact_object(value, required, "capability")
    if errors or not isinstance(value, dict):
        return errors
    errors.extend(_string(value["capability_id"], "capability_id", ROLE_ID, 3, 64))
    description = value["description"]
    if not isinstance(description, str) or not 1 <= len(description) <= 500:
        errors.append("capability description must be a non-empty string of at most 500 characters")
    errors.extend(
        _unique_strings(value["actions"], "capability actions", minimum=1, pattern=ACTION)
    )
    if not isinstance(value["scope"], str) or value["scope"] not in {"read", "write", "admin"}:
        errors.append("capability scope is invalid")
    return errors


def _role_policy_errors(value: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    policy = value["tool_policy"]
    errors.extend(_exact_object(policy, {"allow", "deny"}, "tool_policy"))
    if isinstance(policy, dict) and set(policy) == {"allow", "deny"}:
        errors.extend(
            _unique_strings(policy["allow"], "tool_policy allow", minimum=0, pattern=ACTION)
        )
        errors.extend(
            _unique_strings(policy["deny"], "tool_policy deny", minimum=0, pattern=ACTION)
        )
    worktree = value["worktree_policy"]
    errors.extend(_exact_object(worktree, {"mode", "path_patterns"}, "worktree_policy"))
    if isinstance(worktree, dict) and set(worktree) == {"mode", "path_patterns"}:
        if worktree["mode"] not in {"shared", "isolated", "none"}:
            errors.append("worktree mode is invalid")
        errors.extend(
            _unique_strings(
                worktree["path_patterns"],
                "worktree path_patterns",
                minimum=1,
                pattern=PATH_PATTERN,
            )
        )
    return errors


def _role_errors(value: object) -> list[str]:
    required = {
        "schema_version",
        "role_id",
        "title",
        "summary",
        "capabilities",
        "forbidden_actions",
        "tool_policy",
        "worktree_policy",
        "awq_profile_refs",
    }
    errors = _exact_object(value, required, "role")
    if errors or not isinstance(value, dict):
        return errors
    if (
        not isinstance(value["schema_version"], int)
        or isinstance(value["schema_version"], bool)
        or value["schema_version"] != 1
    ):
        errors.append("role schema_version must be 1")
    errors.extend(_string(value["role_id"], "role_id", ROLE_ID, 3, 64))
    for field, maximum in (("title", 100), ("summary", 1000)):
        if not isinstance(value[field], str) or not 1 <= len(value[field]) <= maximum:
            errors.append(
                f"role {field} must be a non-empty string of at most {maximum} characters"
            )
    capabilities = value["capabilities"]
    if not isinstance(capabilities, list) or not capabilities:
        errors.append("role capabilities must be a non-empty array")
    elif all(isinstance(item, dict) for item in capabilities):
        errors.extend(error for item in capabilities for error in _capability_errors(item))
    else:
        errors.append("role capabilities must contain objects")
    errors.extend(
        _unique_strings(value["forbidden_actions"], "forbidden_actions", minimum=0, pattern=ACTION)
    )
    errors.extend(_role_policy_errors(value))
    errors.extend(
        _unique_strings(
            value["awq_profile_refs"], "awq_profile_refs", minimum=0, pattern=PUBLIC_REF
        )
    )
    return errors


def _schema_errors(value: dict[str, Any]) -> list[str]:
    required = {
        "schema_version",
        "registry_id",
        "roles",
        "default_role",
        "default_awq_profile_refs",
    }
    errors = _exact_object(value, required, "role registry")
    if errors:
        return errors
    if (
        not isinstance(value["schema_version"], int)
        or isinstance(value["schema_version"], bool)
        or value["schema_version"] != 1
    ):
        errors.append("registry schema_version must be 1")
    errors.extend(_string(value["registry_id"], "registry_id", ROLE_ID, 3, 64))
    roles = value["roles"]
    if not isinstance(roles, list) or not roles:
        errors.append("registry roles must be a non-empty array")
    elif all(isinstance(item, dict) for item in roles):
        errors.extend(error for item in roles for error in _role_errors(item))
    else:
        errors.append("registry roles must contain objects")
    errors.extend(_string(value["default_role"], "default_role", ROLE_ID, 3, 64))
    errors.extend(
        _unique_strings(
            value["default_awq_profile_refs"],
            "default_awq_profile_refs",
            minimum=1,
            pattern=PUBLIC_REF,
        )
    )
    return errors


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
