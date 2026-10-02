# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Transactional role assignment management for the Coordinator CLI."""

from __future__ import annotations

import argparse
import contextlib
import datetime as dt
import fcntl
import json
import os
import tempfile
from collections.abc import Iterator
from pathlib import Path
from typing import Any

from tools.role_assignment import RoleAssignmentError, validate_assignment
from tools.role_registry import RoleRegistryError, _load_json, validate_registry

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_STATE = ROOT / ".runtime/roles.json"
DEFAULT_REGISTRY = ROOT / "examples/roles/role-registry.json"
STATE_SCHEMA_VERSION = 1


class RolesError(ValueError):
    """A role command failed closed."""


def _stable(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n"


def _read_state(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"schema_version": STATE_SCHEMA_VERSION, "revision": 0, "assignments": []}
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise RolesError(f"cannot read role state: {path}") from error
    if (
        not isinstance(value, dict)
        or value.get("schema_version") != STATE_SCHEMA_VERSION
        or not isinstance(value.get("revision"), int)
        or value["revision"] < 0
        or not isinstance(value.get("assignments"), list)
    ):
        raise RolesError("role state is malformed")
    return value


def _write_state(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
            stream.write(_stable(value))
            stream.flush()
            os.fsync(stream.fileno())
        Path(temporary).replace(path)
    except OSError as error:
        with contextlib.suppress(OSError):
            Path(temporary).unlink()
        raise RolesError(f"cannot write role state: {path}") from error


@contextlib.contextmanager
def _locked(state: Path) -> Iterator[None]:
    lock = state.with_name("roles.lock")
    lock.parent.mkdir(parents=True, exist_ok=True)
    with lock.open("a+") as stream:
        fcntl.flock(stream.fileno(), fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(stream.fileno(), fcntl.LOCK_UN)


def _registry(path: Path) -> dict[str, Any]:
    try:
        return validate_registry(_load_json(path))
    except RoleRegistryError as error:
        raise RolesError(str(error)) from error


def _assignments(state: dict[str, Any], registry: dict[str, Any]) -> list[dict[str, Any]]:
    assignments = []
    for value in state["assignments"]:
        try:
            assignments.append(validate_assignment(value, registry))
        except RoleAssignmentError as error:
            raise RolesError(str(error)) from error
    return sorted(assignments, key=lambda item: (item["owner_id"], item["assignment_id"]))


def assign(
    state_path: Path,
    registry_path: Path,
    *,
    expected_revision: int,
    assignment_id: str,
    owner_id: str,
    role_id: str,
    expires_at: str,
    evidence_kind: str,
    evidence_ref: str,
    evidence_digest: str,
) -> dict[str, Any]:
    """Add one assignment using exact-revision compare-and-swap."""
    with _locked(state_path):
        state = _read_state(state_path)
        if state["revision"] != expected_revision:
            raise RolesError(
                f"stale role revision: expected {expected_revision}, current {state['revision']}"
            )
        registry = _registry(registry_path)
        value = {
            "schema_version": STATE_SCHEMA_VERSION,
            "assignment_id": assignment_id,
            "owner_id": owner_id,
            "roles": [{"role_id": role_id, "expires_at": expires_at}],
            "authorization_evidence": [
                {"kind": evidence_kind, "ref": evidence_ref, "digest": evidence_digest}
            ],
        }
        try:
            assignment = validate_assignment(value, registry)
        except RoleAssignmentError as error:
            raise RolesError(str(error)) from error
        if any(item["assignment_id"] == assignment_id for item in state["assignments"]):
            raise RolesError(f"assignment already exists: {assignment_id}")
        state["assignments"].append(assignment)
        state["revision"] += 1
        _write_state(state_path, state)
        return {"revision": state["revision"], "assignment": assignment}


def remove(
    state_path: Path, registry_path: Path, *, expected_revision: int, assignment_id: str
) -> dict[str, Any]:
    """Remove one assignment using exact-revision compare-and-swap."""
    with _locked(state_path):
        state = _read_state(state_path)
        if state["revision"] != expected_revision:
            raise RolesError(
                f"stale role revision: expected {expected_revision}, current {state['revision']}"
            )
        registry = _registry(registry_path)
        _assignments(state, registry)
        before = len(state["assignments"])
        state["assignments"] = [
            item for item in state["assignments"] if item.get("assignment_id") != assignment_id
        ]
        if len(state["assignments"]) == before:
            raise RolesError(f"assignment not found: {assignment_id}")
        state["revision"] += 1
        _write_state(state_path, state)
        return {"revision": state["revision"], "removed": assignment_id}


def list_assignments(state_path: Path, registry_path: Path, owner_id: str | None) -> dict[str, Any]:
    state = _read_state(state_path)
    assignments = _assignments(state, _registry(registry_path))
    if owner_id is not None:
        assignments = [item for item in assignments if item["owner_id"] == owner_id]
    return {"revision": state["revision"], "assignments": assignments}


def check(state_path: Path, registry_path: Path, owner_id: str) -> dict[str, Any]:
    result = list_assignments(state_path, registry_path, owner_id)
    if not result["assignments"]:
        raise RolesError(f"no active role assignment for owner: {owner_id}")
    return {"owner_id": owner_id, "revision": result["revision"], "valid": True}


def role_admission_error(
    state_path: Path,
    registry_path: Path,
    *,
    owner_id: str,
    required_role: str,
    now: dt.datetime | None = None,
) -> str | None:
    """Return a fail-closed admission error for one owner, or ``None``.

    A missing role-state file means the role workstream has not been initialized;
    existing installations remain compatible until the durable role store exists.
    Once present, every malformed, unknown, expired, or missing capability fails.
    """
    if not state_path.exists():
        return None
    try:
        state = _read_state(state_path)
        registry = _registry(registry_path)
        assignments = _assignments(state, registry)
    except RolesError as error:
        return f"role admission unavailable: {error}"
    current = now or dt.datetime.now(dt.UTC)
    if current.tzinfo is None:
        return "role admission requires a timezone-aware validation time"
    owner_assignments = [item for item in assignments if item["owner_id"] == owner_id]
    if not owner_assignments:
        return f"role admission denied: owner has no active assignment: {owner_id}"
    role_ids = {role["role_id"] for item in owner_assignments for role in item["roles"]}
    if required_role not in role_ids:
        return f"role admission denied: {owner_id} lacks role: {required_role}"
    return None


def role_admission_errors(
    state_path: Path,
    registry_path: Path,
    owners_and_roles: list[tuple[str, str]],
) -> list[str]:
    """Return deterministic admission errors for doctor validation."""
    if not state_path.exists():
        return []
    errors = [
        error
        for owner_id, required_role in owners_and_roles
        if (
            error := role_admission_error(
                state_path,
                registry_path,
                owner_id=owner_id,
                required_role=required_role,
            )
        )
    ]
    return sorted(set(errors))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state", type=Path, default=DEFAULT_STATE)
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    commands = parser.add_subparsers(dest="command", required=True)
    item = commands.add_parser("assign")
    item.add_argument("--expected-revision", type=int, required=True)
    item.add_argument("--assignment-id", required=True)
    item.add_argument("--owner-id", required=True)
    item.add_argument("--role-id", required=True)
    item.add_argument("--expires-at", required=True)
    item.add_argument("--evidence-kind", choices=("review", "policy", "ticket"), required=True)
    item.add_argument("--evidence-ref", required=True)
    item.add_argument("--evidence-digest", required=True)
    item = commands.add_parser("list")
    item.add_argument("--owner-id")
    item = commands.add_parser("check")
    item.add_argument("--owner-id", required=True)
    item = commands.add_parser("remove")
    item.add_argument("--expected-revision", type=int, required=True)
    item.add_argument("--assignment-id", required=True)
    args = parser.parse_args(argv)
    try:
        if args.command == "assign":
            result = assign(
                args.state,
                args.registry,
                expected_revision=args.expected_revision,
                assignment_id=args.assignment_id,
                owner_id=args.owner_id,
                role_id=args.role_id,
                expires_at=args.expires_at,
                evidence_kind=args.evidence_kind,
                evidence_ref=args.evidence_ref,
                evidence_digest=args.evidence_digest,
            )
        elif args.command == "list":
            result = list_assignments(args.state, args.registry, args.owner_id)
        elif args.command == "check":
            result = check(args.state, args.registry, args.owner_id)
        else:
            result = remove(
                args.state,
                args.registry,
                expected_revision=args.expected_revision,
                assignment_id=args.assignment_id,
            )
    except RolesError as error:
        parser.error(str(error))
    print(_stable(result), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
