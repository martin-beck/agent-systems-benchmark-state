# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Bounded, privacy-safe work-session snapshots."""

from __future__ import annotations

import hashlib
import json
import os
import re
import tempfile
from pathlib import Path
from typing import Any

type Meta = dict[str, Any]

SESSION_SCHEMA_VERSION = 1
MAX_SESSION_RECORDS = 32
MAX_SESSION_BYTES = 4096
SESSION_TASK = "AR-"
SESSION_FIELDS = frozenset(
    {
        "schema_version",
        "task",
        "task_revision",
        "recorded_at",
        "trigger",
        "status",
        "context_digest",
        "step_state",
        "artifact_refs",
        "next_action",
    }
)
TRIGGERS = frozenset({"update", "run", "pause"})
TASK_ID = re.compile(r"^AR-[0-9]{4}$")
DIGEST = re.compile(r"^sha256:[0-9a-f]{64}$")


def session_path(root: Path, task_id: str) -> Path:
    """Return the tracked projection path for one task's session history."""
    if not task_id.startswith(SESSION_TASK) or not task_id[3:].isdigit():
        raise ValueError("invalid session task id")
    return root / "sessions" / f"{task_id}.jsonl"


def _canonical(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def _artifact_refs(meta: Meta) -> list[str]:
    refs: list[str] = []
    spec_ref = meta.get("spec_ref")
    if isinstance(spec_ref, str) and spec_ref:
        refs.append(f"spec:{spec_ref}")
    acceptance = meta.get("spec_acceptance")
    if isinstance(acceptance, dict):
        evidence_ref = acceptance.get("evidence_ref")
        if isinstance(evidence_ref, str) and evidence_ref:
            refs.append(f"evidence:{evidence_ref}")
    checkpoint = meta.get("checkpoint_commit")
    if (
        isinstance(checkpoint, str)
        and len(checkpoint) == 40
        and all(character in "0123456789abcdef" for character in checkpoint)
    ):
        refs.append(f"git:{checkpoint}")
    return refs


def build_session_record(meta: Meta, trigger: str, recorded_at: str) -> Meta:
    """Build an exact-shape snapshot without copying notes, prompts, or logs."""
    if trigger not in TRIGGERS:
        raise ValueError("unknown session trigger")
    context = {
        "task": meta.get("id"),
        "branch": meta.get("branch", ""),
        "worktree_key": meta.get("worktree_key", ""),
        "spec_ref": meta.get("spec_ref", ""),
        "spec_revision": meta.get("spec_revision", 0),
    }
    record: Meta = {
        "schema_version": SESSION_SCHEMA_VERSION,
        "task": str(meta["id"]),
        "task_revision": int(meta["task_revision"]),
        "recorded_at": recorded_at,
        "trigger": trigger,
        "status": str(meta["status"]),
        "context_digest": "sha256:" + hashlib.sha256(_canonical(context)).hexdigest(),
        "step_state": {
            "status": str(meta["status"]),
            "task_revision": int(meta["task_revision"]),
        },
        "artifact_refs": _artifact_refs(meta),
        "next_action": str(meta.get("next_action", "")),
    }
    validate_session_record(record)
    return record


def _validate_header(record: Meta) -> None:
    if set(record) != SESSION_FIELDS:
        raise ValueError("session record fields are not exact")
    if record["schema_version"] != SESSION_SCHEMA_VERSION:
        raise ValueError("unsupported session record schema")
    if not isinstance(record["task"], str) or not TASK_ID.fullmatch(record["task"]):
        raise ValueError("invalid session record task")
    if not isinstance(record["task_revision"], int) or record["task_revision"] < 1:
        raise ValueError("invalid session record revision")
    if record["trigger"] not in TRIGGERS:
        raise ValueError("invalid session record trigger")
    if not isinstance(record["status"], str) or not record["status"]:
        raise ValueError("invalid session record status")
    if not isinstance(record["context_digest"], str) or not DIGEST.fullmatch(
        record["context_digest"]
    ):
        raise ValueError("invalid session context digest")


def _validate_state(record: Meta) -> None:
    state = record["step_state"]
    if not isinstance(state, dict) or set(state) != {"status", "task_revision"}:
        raise ValueError("invalid session step state")


def _validate_payload(record: Meta) -> None:
    refs = record["artifact_refs"]
    if not isinstance(refs, list) or not all(isinstance(value, str) and value for value in refs):
        raise ValueError("invalid session artifact refs")
    if not isinstance(record["next_action"], str) or "\n" in record["next_action"]:
        raise ValueError("invalid session next action")
    if len(_canonical(record)) > MAX_SESSION_BYTES:
        raise ValueError("session record exceeds bounded size")


def validate_session_record(record: Meta) -> None:
    """Reject malformed, overlarge, or privacy-unsafe session records."""
    _validate_header(record)
    _validate_state(record)
    _validate_payload(record)


def decode_session_lines(path: Path) -> list[Meta]:
    """Read and validate a bounded session history."""
    if not path.exists():
        return []
    records: list[Meta] = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        try:
            value = json.loads(line)
        except json.JSONDecodeError as error:
            raise ValueError(f"invalid session record line {number}") from error
        if not isinstance(value, dict):
            raise ValueError(f"invalid session record line {number}")
        validate_session_record(value)
        records.append(value)
    if len(records) > MAX_SESSION_RECORDS:
        raise ValueError("session history exceeds bounded retention")
    return records


def append_session_record(root: Path, record: Meta) -> Path:
    """Atomically append one record while retaining only the newest records."""
    validate_session_record(record)
    path = session_path(root, str(record["task"]))
    records = decode_session_lines(path)
    records.append(record)
    records = records[-MAX_SESSION_RECORDS:]
    path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(prefix=".session-", dir=path.parent)
    temporary_path = Path(temporary)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
            for item in records:
                stream.write(json.dumps(item, sort_keys=True, separators=(",", ":")) + "\n")
            stream.flush()
            os.fsync(stream.fileno())
        temporary_path.chmod(0o600)
        temporary_path.replace(path)
        directory = os.open(path.parent, os.O_DIRECTORY)
        try:
            os.fsync(directory)
        finally:
            os.close(directory)
    finally:
        temporary_path.unlink(missing_ok=True)
    return path


def latest_session(root: Path, task_id: str) -> Meta | None:
    records = decode_session_lines(session_path(root, task_id))
    return records[-1] if records else None
