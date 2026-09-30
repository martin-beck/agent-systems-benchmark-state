# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Durable, fail-closed rollback operation records."""

from __future__ import annotations

import json
import os
import re
import uuid
from pathlib import Path
from typing import Any

Meta = dict[str, Any]
SCHEMA_VERSION = 1
MAX_ROLLBACK_RECORDS = 64
COMMIT_RE = re.compile(r"[0-9a-f]{40}\Z")
CHECKPOINT_RE = re.compile(r"AR-[0-9]{4}-r[0-9]{4}\Z")
STATUS = {"planned", "restore_started", "rollback_completed", "ambiguous"}
REQUIRED = {
    "schema_version",
    "operation_id",
    "checkpoint",
    "task",
    "source_commit",
    "current_commit",
    "rollback_commit",
    "recorded_at",
    "status",
    "revision",
}


def rollback_path(root: Path) -> Path:
    """Return the tracked journal path for rollback operations."""
    return root / "rollbacks" / "operations.jsonl"


def build_record(
    checkpoint: Meta,
    current_commit: str,
    recorded_at: str,
    *,
    status: str = "planned",
    operation_id: str | None = None,
    rollback_commit: str = "",
    revision: int = 1,
) -> Meta:
    """Build one immutable operation-state record."""
    checkpoint_name = str(checkpoint.get("name", ""))
    source_commit = str(checkpoint.get("source_commit", ""))
    task = str(checkpoint.get("task", ""))
    if not CHECKPOINT_RE.fullmatch(checkpoint_name):
        raise ValueError("invalid rollback checkpoint")
    if not re.fullmatch(r"AR-[0-9]{4}\Z", task):
        raise ValueError("invalid rollback task")
    if not COMMIT_RE.fullmatch(source_commit) or not COMMIT_RE.fullmatch(current_commit):
        raise ValueError("invalid rollback commit")
    if rollback_commit and not COMMIT_RE.fullmatch(rollback_commit):
        raise ValueError("invalid rollback result commit")
    if status not in STATUS:
        raise ValueError("invalid rollback status")
    if type(revision) is not int or revision < 1:
        raise ValueError("invalid rollback revision")
    try:
        operation = str(uuid.UUID(operation_id)) if operation_id else str(uuid.uuid4())
    except ValueError as error:
        raise ValueError("invalid rollback operation") from error
    return {
        "schema_version": SCHEMA_VERSION,
        "operation_id": operation,
        "checkpoint": checkpoint_name,
        "task": task,
        "source_commit": source_commit,
        "current_commit": current_commit,
        "rollback_commit": rollback_commit,
        "recorded_at": recorded_at,
        "status": status,
        "revision": revision,
    }


def _validate_identity(record: Meta) -> None:
    if set(record) != REQUIRED or record["schema_version"] != SCHEMA_VERSION:
        raise ValueError("invalid rollback fields")
    try:
        uuid.UUID(str(record["operation_id"]))
    except ValueError as error:
        raise ValueError("invalid rollback operation") from error
    if not CHECKPOINT_RE.fullmatch(str(record["checkpoint"])):
        raise ValueError("invalid rollback checkpoint")
    if not re.fullmatch(r"AR-[0-9]{4}\Z", str(record["task"])):
        raise ValueError("invalid rollback task")
    for field in ("source_commit", "current_commit"):
        if not isinstance(record[field], str) or not COMMIT_RE.fullmatch(record[field]):
            raise ValueError("invalid rollback commit")


def _validate_content(record: Meta) -> None:
    if not isinstance(record["rollback_commit"], str) or (
        record["rollback_commit"] and not COMMIT_RE.fullmatch(record["rollback_commit"])
    ):
        raise ValueError("invalid rollback result commit")
    if not isinstance(record["recorded_at"], str) or not record["recorded_at"]:
        raise ValueError("invalid rollback timestamp")
    if record["status"] not in STATUS:
        raise ValueError("invalid rollback status")
    if type(record["revision"]) is not int or record["revision"] < 1:
        raise ValueError("invalid rollback revision")


def validate_record(record: Meta) -> None:
    """Validate exact fields and all identity boundaries."""
    _validate_identity(record)
    _validate_content(record)


def decode_records(lines: list[str]) -> list[Meta]:
    """Decode and validate the bounded journal."""
    records: list[Meta] = []
    for number, line in enumerate(lines, 1):
        try:
            value = json.loads(line)
        except json.JSONDecodeError as error:
            raise ValueError(f"invalid rollback line {number}") from error
        if not isinstance(value, dict):
            raise ValueError(f"invalid rollback line {number}")
        validate_record(value)
        records.append(value)
    if len(records) > MAX_ROLLBACK_RECORDS:
        raise ValueError("rollback journal exceeds bound")
    return records


def append_record(root: Path, record: Meta) -> None:
    """Atomically append a journal state before or after an external effect."""
    validate_record(record)
    path = rollback_path(root)
    existing = decode_records(path.read_text().splitlines()) if path.exists() else []
    existing.append(record)
    encoded = "".join(
        json.dumps(item, sort_keys=True, separators=(",", ":")) + "\n"
        for item in existing[-MAX_ROLLBACK_RECORDS:]
    )
    path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    descriptor = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        with os.fdopen(descriptor, "w") as stream:
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


def load_records(root: Path) -> list[Meta]:
    """Load the complete bounded rollback journal."""
    path = rollback_path(root)
    return decode_records(path.read_text().splitlines()) if path.exists() else []


def latest_for_checkpoint(root: Path, checkpoint: str) -> Meta | None:
    """Return the newest operation for one checkpoint reference."""
    matches = [record for record in load_records(root) if record["checkpoint"] == checkpoint]
    return matches[-1] if matches else None
