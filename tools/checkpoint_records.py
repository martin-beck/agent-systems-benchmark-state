# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Bounded, privacy-safe task checkpoint records."""

from __future__ import annotations

import hashlib
import json
import os
import re
from pathlib import Path
from typing import Any

Meta = dict[str, Any]
CHECKPOINT_SCHEMA_VERSION = 1
MAX_CHECKPOINTS = 16
TASK_RE = re.compile(r"AR-[0-9]{4}\Z")
COMMIT_RE = re.compile(r"[0-9a-f]{40}\Z")
REQUIRED = {
    "schema_version",
    "name",
    "task",
    "task_revision",
    "recorded_at",
    "source_commit",
    "state",
    "body_digest",
    "artifact_refs",
}


def checkpoint_path(root: Path, task_id: str) -> Path:
    if not TASK_RE.fullmatch(task_id):
        raise ValueError("invalid checkpoint task")
    return root / "checkpoints" / f"{task_id}.jsonl"


def _canonical(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def _artifact_refs(meta: Meta) -> list[str]:
    refs: list[str] = []
    spec = meta.get("spec_ref")
    if isinstance(spec, str) and spec:
        refs.append(f"spec:{spec}")
    acceptance = meta.get("spec_acceptance")
    if isinstance(acceptance, dict):
        evidence = acceptance.get("evidence_ref")
        if isinstance(evidence, str) and evidence:
            refs.append(f"evidence:{evidence}")
    return refs[:8]


def build_checkpoint(
    meta: Meta,
    body: str,
    source_commit: str,
    recorded_at: str,
) -> Meta:
    if not COMMIT_RE.fullmatch(source_commit):
        raise ValueError("checkpoint source commit must be a 40-character hexadecimal commit")
    task_id = str(meta.get("id", ""))
    if not TASK_RE.fullmatch(task_id):
        raise ValueError("invalid checkpoint task")
    state = dict(meta)
    return {
        "schema_version": CHECKPOINT_SCHEMA_VERSION,
        "name": f"{task_id}-r{int(meta['task_revision']):04d}",
        "task": task_id,
        "task_revision": int(meta["task_revision"]),
        "recorded_at": recorded_at,
        "source_commit": source_commit,
        "state": state,
        "body_digest": hashlib.sha256(body.encode()).hexdigest(),
        "artifact_refs": _artifact_refs(meta),
    }


def _validate_checkpoint_identity(record: Meta) -> None:
    if set(record) != REQUIRED:
        raise ValueError("invalid checkpoint fields")
    if record["schema_version"] != CHECKPOINT_SCHEMA_VERSION:
        raise ValueError("unsupported checkpoint schema")
    task = record["task"]
    if not isinstance(task, str) or not TASK_RE.fullmatch(task):
        raise ValueError("invalid checkpoint task")
    if (
        not isinstance(record["name"], str)
        or record["name"] != f"{task}-r{record['task_revision']:04d}"
    ):
        raise ValueError("invalid checkpoint name")
    if type(record["task_revision"]) is not int or record["task_revision"] < 1:
        raise ValueError("invalid checkpoint revision")
    if not isinstance(record["source_commit"], str) or not COMMIT_RE.fullmatch(
        record["source_commit"]
    ):
        raise ValueError("invalid checkpoint source commit")
    state = record["state"]
    if not isinstance(state, dict) or state.get("id") != task:
        raise ValueError("invalid checkpoint state")


def _validate_checkpoint_content(record: Meta) -> None:
    if not isinstance(record["recorded_at"], str) or not record["recorded_at"]:
        raise ValueError("invalid checkpoint timestamp")
    if not isinstance(record["body_digest"], str) or not re.fullmatch(
        r"[0-9a-f]{64}", record["body_digest"]
    ):
        raise ValueError("invalid checkpoint body digest")
    refs = record["artifact_refs"]
    if (
        not isinstance(refs, list)
        or len(refs) > 8
        or any(not isinstance(item, str) or not item for item in refs)
    ):
        raise ValueError("invalid checkpoint artifact refs")


def validate_checkpoint(record: Meta) -> None:
    _validate_checkpoint_identity(record)
    _validate_checkpoint_content(record)


def decode_checkpoints(lines: list[str]) -> list[Meta]:
    records: list[Meta] = []
    for number, line in enumerate(lines, 1):
        try:
            value = json.loads(line)
        except json.JSONDecodeError as error:
            raise ValueError(f"invalid checkpoint line {number}") from error
        if not isinstance(value, dict):
            raise ValueError(f"invalid checkpoint line {number}")
        validate_checkpoint(value)
        records.append(value)
    if len(records) > MAX_CHECKPOINTS:
        raise ValueError("checkpoint history exceeds bound")
    return records


def append_checkpoint(root: Path, record: Meta) -> None:
    validate_checkpoint(record)
    path = checkpoint_path(root, str(record["task"]))
    existing = decode_checkpoints(path.read_text().splitlines()) if path.exists() else []
    existing.append(record)
    encoded = "".join(_canonical(item) + "\n" for item in existing[-MAX_CHECKPOINTS:])
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


def load_checkpoints(root: Path, task_id: str | None = None) -> list[Meta]:
    paths = (
        [checkpoint_path(root, task_id)]
        if task_id
        else sorted((root / "checkpoints").glob("AR-*.jsonl"))
    )
    records: list[Meta] = []
    for path in paths:
        if path.exists():
            records.extend(decode_checkpoints(path.read_text().splitlines()))
    return records
