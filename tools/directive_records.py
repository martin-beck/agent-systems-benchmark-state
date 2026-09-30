# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Bounded, revision-fenced user directive records."""

from __future__ import annotations

import json
import os
import re
from pathlib import Path
from typing import Any

Meta = dict[str, Any]
SCHEMA_VERSION = 1
MAX_DIRECTIVES = 64
DIRECTIVE_RE = re.compile(r"UD-[0-9]{4}\Z")
TASK_RE = re.compile(r"AR-[0-9]{4}\Z")
REF_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9._/-]{2,127}\Z")
GUIDANCE_RE = re.compile(r"AR-0053\Z")
LIFECYCLES = {"proposed", "active", "superseded", "revoked", "escalated"}
REQUIRED = {
    "schema_version",
    "directive_id",
    "authority",
    "precedence",
    "scope",
    "statement",
    "lifecycle",
    "revision",
    "owner",
    "claim_expires",
    "guidance_ref",
    "created_at",
    "updated_at",
}


def directive_path(root: Path) -> Path:
    """Return the tracked bounded directive journal."""
    return root / "directives" / "records.jsonl"


def _scope(value: object) -> Meta:
    if not isinstance(value, dict) or set(value) != {"roles", "tasks"}:
        raise ValueError("directive scope must contain roles and tasks")
    roles = value["roles"]
    tasks = value["tasks"]
    if not isinstance(roles, list) or not isinstance(tasks, list):
        raise ValueError("directive scope values must be lists")
    if not roles and not tasks:
        raise ValueError("directive scope must target a role or task")
    _scope_list(roles, REF_RE, "role")
    _scope_list(tasks, TASK_RE, "task")
    return {"roles": sorted(roles), "tasks": sorted(tasks)}


def _scope_list(values: list[object], pattern: re.Pattern[str], label: str) -> None:
    if any(not isinstance(item, str) for item in values):
        raise ValueError(f"invalid directive {label} scope")
    strings = [str(item) for item in values]
    if len(strings) != len(set(strings)):
        raise ValueError("directive scope contains duplicates")
    if any(not pattern.fullmatch(item) for item in strings):
        raise ValueError(f"invalid directive {label} scope")


def build_directive(
    directive_id: str,
    *,
    authority: str,
    precedence: int,
    scope: Meta,
    statement: str,
    recorded_at: str,
    owner: str,
    claim_expires: str,
    lifecycle: str = "proposed",
    revision: int = 1,
    guidance_ref: str = "",
) -> Meta:
    """Build one exact-shape directive record."""
    if not DIRECTIVE_RE.fullmatch(directive_id):
        raise ValueError("invalid directive id")
    record = {
        "schema_version": SCHEMA_VERSION,
        "directive_id": directive_id,
        "authority": authority,
        "precedence": precedence,
        "scope": _scope(scope),
        "statement": statement.strip() if isinstance(statement, str) else statement,
        "lifecycle": lifecycle,
        "revision": revision,
        "owner": owner,
        "claim_expires": claim_expires,
        "guidance_ref": guidance_ref,
        "created_at": recorded_at,
        "updated_at": recorded_at,
    }
    validate_directive(record)
    return record


def _validate_identity(record: Meta) -> None:
    if set(record) != REQUIRED or record["schema_version"] != SCHEMA_VERSION:
        raise ValueError("invalid directive fields")
    if not isinstance(record["directive_id"], str) or not DIRECTIVE_RE.fullmatch(
        record["directive_id"]
    ):
        raise ValueError("invalid directive id")
    if not isinstance(record["authority"], str) or not REF_RE.fullmatch(record["authority"]):
        raise ValueError("invalid directive authority")
    if type(record["precedence"]) is not int or record["precedence"] < 1:
        raise ValueError("invalid directive precedence")
    _scope(record["scope"])


def _validate_content(record: Meta) -> None:
    _validate_statement(record["statement"])
    if record["lifecycle"] not in LIFECYCLES:
        raise ValueError("invalid directive lifecycle")
    if type(record["revision"]) is not int or record["revision"] < 1:
        raise ValueError("invalid directive revision")
    _validate_owner(record["owner"])
    _validate_lease(record["claim_expires"])
    _validate_guidance(record["guidance_ref"])
    _validate_timestamps(record)


def _validate_statement(value: object) -> None:
    if not isinstance(value, str) or not value.strip() or "\n" in value or len(value) > 4096:
        raise ValueError("invalid directive statement")


def _validate_owner(value: object) -> None:
    if not isinstance(value, str) or (value and not REF_RE.fullmatch(value)):
        raise ValueError("invalid directive owner")


def _validate_lease(value: object) -> None:
    if not isinstance(value, str):
        raise ValueError("invalid directive lease")


def _validate_guidance(value: object) -> None:
    if not isinstance(value, str) or (value and not GUIDANCE_RE.fullmatch(value)):
        raise ValueError("invalid directive guidance reference")


def _validate_timestamps(record: Meta) -> None:
    for field in ("created_at", "updated_at"):
        if not isinstance(record[field], str) or not record[field]:
            raise ValueError(f"invalid directive {field}")


def validate_directive(record: Meta) -> None:
    """Validate exact fields and bounded content."""
    _validate_identity(record)
    _validate_content(record)


def decode_directives(lines: list[str]) -> list[Meta]:
    """Decode and validate the bounded directive journal."""
    records: list[Meta] = []
    for number, line in enumerate(lines, 1):
        try:
            value = json.loads(line)
        except json.JSONDecodeError as error:
            raise ValueError(f"invalid directive line {number}") from error
        if not isinstance(value, dict):
            raise ValueError(f"invalid directive line {number}")
        validate_directive(value)
        records.append(value)
    if len(records) > MAX_DIRECTIVES:
        raise ValueError("directive journal exceeds bound")
    return records


def load_directives(root: Path) -> list[Meta]:
    """Load all directive revisions in journal order."""
    path = directive_path(root)
    return decode_directives(path.read_text(encoding="utf-8").splitlines()) if path.exists() else []


def latest_directives(root: Path) -> list[Meta]:
    """Return one latest record per directive id."""
    latest: dict[str, Meta] = {}
    for record in load_directives(root):
        current = latest.get(str(record["directive_id"]))
        if current is not None and int(record["revision"]) <= int(current["revision"]):
            raise ValueError("directive revisions are not strictly increasing")
        latest[str(record["directive_id"])] = record
    return sorted(latest.values(), key=lambda item: str(item["directive_id"]))


def append_directive(root: Path, record: Meta) -> None:
    """Atomically append a directive revision with bounded retention."""
    validate_directive(record)
    existing = load_directives(root)
    same = [item for item in existing if item["directive_id"] == record["directive_id"]]
    if same and int(record["revision"]) != int(same[-1]["revision"]) + 1:
        raise ValueError("directive revision is not the next CAS revision")
    encoded = "".join(
        json.dumps(item, sort_keys=True, separators=(",", ":")) + "\n"
        for item in [*existing, record][-MAX_DIRECTIVES:]
    )
    path = directive_path(root)
    path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    descriptor = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
            stream.write(encoded)
            stream.flush()
            os.fsync(stream.fileno())
        temporary.replace(path)
        directory = os.open(path.parent, os.O_DIRECTORY)
        try:
            os.fsync(directory)
        finally:
            os.close(directory)
    except Exception:
        temporary.unlink(missing_ok=True)
        raise


def scopes_overlap(left: Meta, right: Meta) -> bool:
    """Return whether two directives address any common role or task."""
    first = _scope(left["scope"])
    second = _scope(right["scope"])
    return bool(
        set(first["roles"]) & set(second["roles"]) or set(first["tasks"]) & set(second["tasks"])
    )


def conflicting_directives(records: list[Meta], candidate: Meta) -> list[Meta]:
    """Find active same-precedence directives with overlapping scope."""
    return [
        record
        for record in records
        if record["lifecycle"] == "active"
        and int(record["precedence"]) == int(candidate["precedence"])
        and record["directive_id"] != candidate["directive_id"]
        and scopes_overlap(record, candidate)
        and record["statement"] != candidate["statement"]
    ]


def applicable_directives(records: list[Meta], *, role: str = "", task: str = "") -> list[Meta]:
    """Return active directives for one scope, highest precedence first."""
    if not role and not task:
        raise ValueError("directive applicability requires a role or task")
    if role and not REF_RE.fullmatch(role):
        raise ValueError("invalid directive role")
    if task and not TASK_RE.fullmatch(task):
        raise ValueError("invalid directive task")
    selected = []
    for record in records:
        if record["lifecycle"] != "active":
            continue
        scope = _scope(record["scope"])
        if (role and role in scope["roles"]) or (task and task in scope["tasks"]):
            selected.append(record)
    return sorted(selected, key=lambda item: (-int(item["precedence"]), str(item["directive_id"])))
