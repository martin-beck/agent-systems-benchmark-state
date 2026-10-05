# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Append-only claim identity records for the Git coordinator backend."""

from __future__ import annotations

import hashlib
import json
import os
import re
from pathlib import Path
from typing import Any

Meta = dict[str, Any]
SCHEMA_VERSION = 1
TASK_RE = re.compile(r"AR-[0-9]{4}\Z")
SHA256_RE = re.compile(r"[0-9a-f]{64}\Z")
REQUIRED = {
    "schema_version",
    "task",
    "task_revision",
    "recorded_at",
    "operation",
    "identity",
    "fingerprint",
}
IDENTITY_FIELDS = (
    "id",
    "title",
    "summary",
    "depends_on",
    "plan",
    "spec_ref",
    "owner",
    "claim_expires",
    "task_revision",
)


def ledger_path(root: Path) -> Path:
    return root / "integrity" / "claim-ledger.jsonl"


def _canonical(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def identity(meta: Meta) -> Meta:
    """Return the immutable identity snapshot for one claimed task."""
    return {field: meta.get(field) for field in IDENTITY_FIELDS}


def fingerprint(meta: Meta) -> str:
    return hashlib.sha256(_canonical(identity(meta)).encode()).hexdigest()


def build_record(meta: Meta, operation: str, recorded_at: str) -> Meta:
    task = str(meta.get("id", ""))
    if not TASK_RE.fullmatch(task):
        raise ValueError("invalid claim record task")
    if not isinstance(operation, str) or not operation:
        raise ValueError("invalid claim record operation")
    snapshot = identity(meta)
    return {
        "schema_version": SCHEMA_VERSION,
        "task": task,
        "task_revision": int(meta["task_revision"]),
        "recorded_at": recorded_at,
        "operation": operation,
        "identity": snapshot,
        "fingerprint": hashlib.sha256(_canonical(snapshot).encode()).hexdigest(),
    }


def validate_record(record: Meta) -> None:  # noqa: C901
    if set(record) != REQUIRED:
        raise ValueError("invalid claim record fields")
    if record["schema_version"] != SCHEMA_VERSION:
        raise ValueError("unsupported claim record schema")
    task = record["task"]
    if not isinstance(task, str) or not TASK_RE.fullmatch(task):
        raise ValueError("invalid claim record task")
    if type(record["task_revision"]) is not int or record["task_revision"] < 1:
        raise ValueError("invalid claim record revision")
    if not isinstance(record["recorded_at"], str) or not record["recorded_at"]:
        raise ValueError("invalid claim record timestamp")
    if not isinstance(record["operation"], str) or not record["operation"]:
        raise ValueError("invalid claim record operation")
    snapshot = record["identity"]
    if not isinstance(snapshot, dict) or set(snapshot) != set(IDENTITY_FIELDS):
        raise ValueError("invalid claim record identity")
    if snapshot.get("id") != task or snapshot.get("task_revision") != record["task_revision"]:
        raise ValueError("claim record identity does not match task")
    digest = record["fingerprint"]
    if not isinstance(digest, str) or not SHA256_RE.fullmatch(digest):
        raise ValueError("invalid claim record fingerprint")
    if digest != hashlib.sha256(_canonical(snapshot).encode()).hexdigest():
        raise ValueError("claim record fingerprint mismatch")


def load_records(root: Path) -> list[Meta]:
    path = ledger_path(root)
    if not path.exists():
        return []
    records: list[Meta] = []
    for number, line in enumerate(path.read_text().splitlines(), 1):
        try:
            value = json.loads(line)
        except json.JSONDecodeError as error:
            raise ValueError(f"invalid claim record line {number}") from error
        if not isinstance(value, dict):
            raise ValueError(f"invalid claim record line {number}")
        validate_record(value)
        records.append(value)
    return records


def append_record(root: Path, record: Meta) -> None:
    validate_record(record)
    records = load_records(root)
    records.append(record)
    encoded = "".join(_canonical(item) + "\n" for item in records)
    path = ledger_path(root)
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


def latest_for_task(records: list[Meta], task: str) -> Meta | None:
    matches = [record for record in records if record.get("task") == task]
    return matches[-1] if matches else None


def mismatch(record: Meta, meta: Meta) -> str | None:
    """Return a stable error when a claimed task differs from its ledger record."""
    expected = record.get("fingerprint")
    actual = fingerprint(meta)
    if expected != actual:
        return f"{meta.get('id')}: claimed identity differs from append-only ledger"
    if record.get("task_revision") != meta.get("task_revision"):
        return f"{meta.get('id')}: claim ledger revision is stale"
    return None
