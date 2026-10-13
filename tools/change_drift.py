# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Deterministic, non-destructive Git worktree change-drift records."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path
from typing import Any

type Meta = dict[str, Any]

SCHEMA_VERSION = 2
MAX_RECORDS = 32
TASK = re.compile(r"^AR-[0-9]{4}$")
DIGEST = re.compile(r"^sha256:[0-9a-f]{64}$")
KINDS = frozenset({"baseline", "delta", "explain", "rescope"})
CLASSIFICATIONS = frozenset({"in_scope", "out_of_scope"})


def canonical(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def digest(value: object) -> str:
    return "sha256:" + hashlib.sha256(canonical(value)).hexdigest()


def safe_path(value: object) -> bool:
    return (
        isinstance(value, str)
        and bool(value)
        and len(value) <= 1024
        and "\x00" not in value
        and not Path(value).is_absolute()
        and all(part not in {"", ".", ".."} for part in Path(value).parts)
    )


def normalize_scope(values: list[str]) -> list[str]:
    if not values or len(values) > 64 or not all(safe_path(value) for value in values):
        raise ValueError("change-drift scope must be a bounded list of safe paths")
    normalized = sorted(set(values))
    if len(normalized) != len(values):
        raise ValueError("change-drift scope contains duplicates")
    return normalized


def _inside(path: str, scope: list[str]) -> bool:
    return any(path == item or path.startswith(item + "/") for item in scope)


def _generated(path: str) -> bool:
    parts = Path(path).parts
    name = Path(path).name.lower()
    return any(
        part.lower() in {"build", "dist", "generated", "__generated__"} for part in parts
    ) or name.endswith((".generated", ".gen.py", ".pb.go", ".min.js"))


def _content_digest(worktree: Path, path: str) -> str:
    """Hash a present worktree path without retaining its contents."""
    target = worktree / path
    if not target.exists() and not target.is_symlink():
        return ""
    result = subprocess.run(  # noqa: S603
        ["git", "-C", str(worktree), "hash-object", "--no-filters", "--", path],  # noqa: S607
        check=False,
        capture_output=True,
        text=True,
    )
    value = result.stdout.strip()
    if result.returncode or not re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", value):
        raise RuntimeError("change-drift could not fingerprint a changed path")
    return value


def _status_entries(raw: bytes, worktree: Path | None = None) -> list[Meta]:
    """Parse porcelain v1 -z without interpreting hostile filenames as text lines."""
    fields = raw.split(b"\0")
    entries: list[Meta] = []
    index = 0
    while index < len(fields) - 1:
        field = fields[index]
        index += 1
        if len(field) < 4 or field[2:3] != b" ":
            raise ValueError("Git returned malformed porcelain status")
        status = field[:2].decode("ascii", "strict")
        path = field[3:].decode("utf-8", "surrogateescape")
        previous_path = ""
        if status[:1] in {"R", "C"} or status[1:2] in {"R", "C"}:
            if index >= len(fields) - 1:
                raise ValueError("Git returned truncated rename status")
            previous_path = fields[index].decode("utf-8", "surrogateescape")
            index += 1
        if not safe_path(path) or (previous_path and not safe_path(previous_path)):
            raise ValueError("Git returned an unsafe changed path")
        entries.append(
            {
                "path": path,
                "previous_path": previous_path,
                "status": status,
                "generated": _generated(path),
                "content_digest": _content_digest(worktree, path) if worktree else "",
            }
        )
    return sorted(
        entries,
        key=lambda item: (str(item["path"]), str(item["previous_path"]), str(item["status"])),
    )


def observe(worktree: Path) -> Meta:
    """Take a stable, path-safe worktree observation without changing it."""
    root = worktree.resolve()
    head = subprocess.run(  # noqa: S603
        ["git", "-C", str(root), "rev-parse", "--verify", "HEAD"],  # noqa: S607
        check=False,
        capture_output=True,
        text=True,
    )
    status = subprocess.run(  # noqa: S603
        ["git", "-C", str(root), "status", "--porcelain=v1", "-z", "--untracked-files=all"],  # noqa: S607
        check=False,
        capture_output=True,
    )
    if status.returncode:
        raise RuntimeError("change-drift observation requires a Git worktree")
    return {
        "head": head.stdout.strip() if head.returncode == 0 else "",
        "entries": _status_entries(status.stdout, root),
    }


def _record(
    kind: str,
    task: str,
    revision: int,
    recorded_at: str,
    payload: Meta,
    previous_digest: str = "",
) -> Meta:
    if kind not in KINDS or not TASK.fullmatch(task) or revision < 1 or not recorded_at:
        raise ValueError("invalid change-drift record identity")
    if previous_digest and not DIGEST.fullmatch(previous_digest):
        raise ValueError("invalid change-drift predecessor")
    identity = {
        "schema_version": SCHEMA_VERSION,
        "kind": kind,
        "task": task,
        "task_revision": revision,
        "payload": payload,
        "previous_digest": previous_digest,
    }
    return {**identity, "recorded_at": recorded_at, "digest": digest(identity)}


def baseline(
    task: str,
    revision: int,
    recorded_at: str,
    worktree: Path,
    scope: list[str],
    previous_digest: str = "",
) -> Meta:
    return _record(
        "baseline",
        task,
        revision,
        recorded_at,
        {**observe(worktree), "scope": normalize_scope(scope)},
        previous_digest,
    )


def _entry_key(entry: Meta) -> tuple[str, str]:
    return str(entry["path"]), str(entry["previous_path"])


def _head_entries(worktree: Path, before: str, after: str) -> list[Meta]:
    """Return committed tree changes, retaining Git's rename pairing."""
    if before == after:
        return []
    result = subprocess.run(  # noqa: S603
        ["git", "-C", str(worktree), "diff", "--name-status", "-z", "-M", before, after],  # noqa: S607
        check=False,
        capture_output=True,
    )
    if result.returncode:
        raise RuntimeError("change-drift could not compare committed work")
    fields = result.stdout.split(b"\0")
    entries: list[Meta] = []
    index = 0
    while index < len(fields) - 1:
        status_field = fields[index]
        index += 1
        if not status_field:
            break
        status = status_field.decode("ascii", "strict")
        if not status or index >= len(fields) - 1:
            raise ValueError("Git returned malformed committed change status")
        previous_path = ""
        if status[:1] in {"R", "C"}:
            previous_path = fields[index].decode("utf-8", "surrogateescape")
            index += 1
        path = fields[index].decode("utf-8", "surrogateescape")
        index += 1
        if not safe_path(path) or (previous_path and not safe_path(previous_path)):
            raise ValueError("Git returned an unsafe committed changed path")
        entries.append(
            {
                "path": path,
                "previous_path": previous_path,
                "status": status[:1] + " ",
                "generated": _generated(path),
                "content_digest": _content_digest(worktree, path),
            }
        )
    return sorted(entries, key=lambda item: (*_entry_key(item), str(item["status"])))


def delta(
    task: str,
    revision: int,
    recorded_at: str,
    worktree: Path,
    baseline_record: Meta,
    scope: list[str],
    previous_digest: str | None = None,
) -> Meta:
    current = observe(worktree)
    before = {_entry_key(entry): entry for entry in baseline_record["payload"]["entries"]}
    changed: list[Meta] = []
    for entry in current["entries"]:
        previous = before.get(_entry_key(entry))
        if previous == entry:
            continue
        paths = [str(entry["path"])] + (
            [str(entry["previous_path"])] if entry["previous_path"] else []
        )
        classification = (
            "in_scope" if all(_inside(path, scope) for path in paths) else "out_of_scope"
        )
        changed.append({**entry, "classification": classification, "material": True})
    baseline_paths = {
        str(entry["path"]): str(entry["content_digest"])
        for entry in baseline_record["payload"]["entries"]
    }
    for entry in _head_entries(
        worktree, str(baseline_record["payload"]["head"]), str(current["head"])
    ):
        if baseline_paths.get(str(entry["path"])) == entry["content_digest"]:
            continue
        if _entry_key(entry) in {_entry_key(item) for item in changed}:
            continue
        paths = [str(entry["path"])] + (
            [str(entry["previous_path"])] if entry["previous_path"] else []
        )
        classification = (
            "in_scope" if all(_inside(path, scope) for path in paths) else "out_of_scope"
        )
        changed.append({**entry, "classification": classification, "material": True})
    changed.sort(key=lambda item: (*_entry_key(item), str(item["status"])))
    payload = {"baseline_digest": baseline_record["digest"], **current, "entries": changed}
    return _record(
        "delta",
        task,
        revision,
        recorded_at,
        payload,
        baseline_record["digest"] if previous_digest is None else previous_digest,
    )


def explain(
    task: str,
    revision: int,
    recorded_at: str,
    delta_digest: str,
    paths: list[str],
    reason: str,
    generated: bool,
    previous_digest: str | None = None,
) -> Meta:
    if (
        not DIGEST.fullmatch(delta_digest)
        or not paths
        or len(paths) > 64
        or not all(safe_path(path) for path in paths)
    ):
        raise ValueError("invalid change-drift explanation paths")
    if not reason.strip() or len(reason) > 1000 or "\n" in reason:
        raise ValueError("change-drift explanation reason is invalid")
    return _record(
        "explain",
        task,
        revision,
        recorded_at,
        {
            "delta_digest": delta_digest,
            "paths": sorted(set(paths)),
            "reason": reason,
            "generated": generated,
        },
        delta_digest if previous_digest is None else previous_digest,
    )


def rescope(
    task: str,
    revision: int,
    recorded_at: str,
    baseline_digest: str,
    scope: list[str],
    previous_digest: str | None = None,
) -> Meta:
    if not DIGEST.fullmatch(baseline_digest):
        raise ValueError("invalid change-drift baseline digest")
    return _record(
        "rescope",
        task,
        revision,
        recorded_at,
        {"baseline_digest": baseline_digest, "scope": normalize_scope(scope)},
        baseline_digest if previous_digest is None else previous_digest,
    )


def validate(record: object) -> None:  # noqa: C901
    if not isinstance(record, dict) or set(record) != {
        "schema_version",
        "kind",
        "task",
        "task_revision",
        "recorded_at",
        "payload",
        "previous_digest",
        "digest",
    }:
        raise ValueError("change-drift record fields are not exact")
    identity = {
        key: record[key]
        for key in ("schema_version", "kind", "task", "task_revision", "payload", "previous_digest")
    }
    if (
        record.get("schema_version") != SCHEMA_VERSION
        or record.get("kind") not in KINDS
        or not TASK.fullmatch(str(record.get("task", "")))
        or type(record.get("task_revision")) is not int
        or int(record["task_revision"]) < 1
        or not isinstance(record.get("recorded_at"), str)
        or not record["recorded_at"]
        or not isinstance(record.get("previous_digest"), str)
        or (record["previous_digest"] and not DIGEST.fullmatch(record["previous_digest"]))
        or record.get("digest") != digest(identity)
    ):
        raise ValueError("invalid change-drift record identity")
    payload = record["payload"]
    if not isinstance(payload, dict):
        raise ValueError("invalid change-drift record payload")
    kind = str(record["kind"])
    if kind == "baseline":
        _validate_observation(payload, with_scope=True)
    elif kind == "delta":
        if set(payload) != {"baseline_digest", "head", "entries"} or not DIGEST.fullmatch(
            str(payload.get("baseline_digest", ""))
        ):
            raise ValueError("invalid change-drift delta payload")
        _validate_observation(payload, with_scope=False, classified=True)
    elif kind == "explain":
        paths = payload.get("paths")
        if (
            set(payload) != {"delta_digest", "paths", "reason", "generated"}
            or not DIGEST.fullmatch(str(payload.get("delta_digest", "")))
            or not isinstance(paths, list)
            or not paths
            or len(paths) > 64
            or not all(safe_path(path) for path in paths)
            or len(set(paths)) != len(paths)
            or not isinstance(payload.get("reason"), str)
            or not str(payload["reason"]).strip()
            or len(str(payload["reason"])) > 1000
            or "\n" in str(payload["reason"])
            or type(payload.get("generated")) is not bool
        ):
            raise ValueError("invalid change-drift explanation payload")
    else:
        if set(payload) != {"baseline_digest", "scope"} or not DIGEST.fullmatch(
            str(payload.get("baseline_digest", ""))
        ):
            raise ValueError("invalid change-drift re-scope payload")
        try:
            if payload["scope"] != normalize_scope(payload["scope"]):
                raise ValueError("scope is not canonical")
        except (KeyError, TypeError, ValueError) as error:
            raise ValueError("invalid change-drift re-scope payload") from error


def _validate_observation(  # noqa: C901
    payload: Meta, *, with_scope: bool, classified: bool = False
) -> None:
    expected = {"head", "entries"} | ({"scope"} if with_scope else {"baseline_digest"})
    if set(payload) != expected or not isinstance(payload.get("head"), str):
        raise ValueError("invalid change-drift observation payload")
    entries = payload.get("entries")
    if not isinstance(entries, list) or len(entries) > 4096:
        raise ValueError("invalid change-drift observation entries")
    expected_entry = {"path", "previous_path", "status", "generated", "content_digest"}
    if classified:
        expected_entry |= {"classification", "material"}
    for entry in entries:
        if (
            not isinstance(entry, dict)
            or set(entry) != expected_entry
            or not safe_path(entry.get("path"))
            or (entry.get("previous_path") and not safe_path(entry.get("previous_path")))
            or not isinstance(entry.get("previous_path"), str)
            or not isinstance(entry.get("status"), str)
            or len(str(entry["status"])) != 2
            or type(entry.get("generated")) is not bool
            or not isinstance(entry.get("content_digest"), str)
            or (
                entry["content_digest"]
                and not re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", entry["content_digest"])
            )
            or (classified and entry.get("classification") not in CLASSIFICATIONS)
            or (classified and type(entry.get("material")) is not bool)
        ):
            raise ValueError("invalid change-drift observation entry")
    if entries != sorted(entries, key=lambda item: (*_entry_key(item), str(item["status"]))):
        raise ValueError("change-drift observation entries are not canonical")
    if with_scope:
        try:
            if payload["scope"] != normalize_scope(payload["scope"]):
                raise ValueError("scope is not canonical")
        except (KeyError, TypeError, ValueError) as error:
            raise ValueError("invalid change-drift baseline payload") from error


def records(meta: Meta) -> list[Meta]:  # noqa: C901
    value = meta.get("change_drift", [])
    if not isinstance(value, list) or len(value) > MAX_RECORDS:
        raise ValueError("invalid change-drift history")
    previous_digest = ""
    previous_revision = 0
    active_baseline: Meta | None = None
    active_delta: Meta | None = None
    for record in value:
        validate(record)
        if record["task"] != meta.get("id"):
            raise ValueError("change-drift record task differs from task")
        if record["previous_digest"] != previous_digest:
            raise ValueError("change-drift history is not linked")
        if record["task_revision"] <= previous_revision:
            raise ValueError("change-drift history revisions are not increasing")
        kind = record["kind"]
        payload = record["payload"]
        if kind == "baseline":
            if active_delta is not None and unresolved(value[: value.index(record)]):
                raise ValueError("change-drift baseline bypasses unresolved work")
            active_baseline, active_delta = record, None
        elif kind == "rescope":
            if (
                active_baseline is None
                or active_delta is not None
                or payload["baseline_digest"] != active_baseline["digest"]
            ):
                raise ValueError("change-drift re-scope is not linked to the active baseline")
        elif kind == "delta":
            if (
                active_baseline is None
                or active_delta is not None
                or payload["baseline_digest"] != active_baseline["digest"]
            ):
                raise ValueError("change-drift delta is not linked to the active baseline")
            active_delta = record
        else:
            if active_delta is None or payload["delta_digest"] != active_delta["digest"]:
                raise ValueError("change-drift explanation is not linked to the active delta")
            material = {entry["path"]: entry for entry in active_delta["payload"]["entries"]}
            if not set(payload["paths"]).issubset(material):
                raise ValueError("change-drift explanation names unrelated paths")
        previous_digest = record["digest"]
        previous_revision = record["task_revision"]
    return value


def latest(records_value: list[Meta], kind: str) -> Meta | None:
    return next((record for record in reversed(records_value) if record["kind"] == kind), None)


def active_scope(records_value: list[Meta], baseline_record: Meta) -> list[str]:
    scope = list(baseline_record["payload"]["scope"])
    for record in records_value:
        if (
            record["kind"] == "rescope"
            and record["payload"]["baseline_digest"] == baseline_record["digest"]
        ):
            scope = list(record["payload"]["scope"])
    return scope


def unresolved(records_value: list[Meta]) -> list[Meta]:
    current = latest(records_value, "delta")
    if current is None:
        return []
    explained = {
        path
        for record in records_value
        if record["kind"] == "explain" and record["payload"]["delta_digest"] == current["digest"]
        for path in record["payload"]["paths"]
    }
    return [
        entry
        for entry in current["payload"]["entries"]
        if entry["material"] and entry["path"] not in explained
    ]


def completion_error(records_value: list[Meta]) -> str | None:
    """Return the fail-closed reason when a recorded cycle cannot complete."""
    if not records_value:
        return None
    records({"id": records_value[0]["task"], "change_drift": records_value})
    current = records_value[-1]
    if current["kind"] != "delta" and current["kind"] != "explain":
        return "CHANGE_DRIFT_DELTA_REQUIRED: active baseline requires a post-work delta"
    if unresolved(records_value):
        return "CHANGE_DRIFT_UNEXPLAINED"
    return None


def metadata_error(meta: Meta) -> str | None:
    """Return malformed change-drift history as task metadata validation error."""
    try:
        records(meta)
    except ValueError as error:
        return str(error)
    return None


def done_admission_error(meta: Meta) -> str | None:
    """Return the fail-closed change-drift condition for terminal admission."""
    try:
        history = records(meta)
        error = completion_error(history)
        if error and error != "CHANGE_DRIFT_UNEXPLAINED":
            return error
        outstanding = unresolved(history)
    except ValueError as error:
        return f"change-drift record is invalid: {error}"
    if outstanding:
        paths = ", ".join(str(entry["path"]) for entry in outstanding)
        return f"CHANGE_DRIFT_UNEXPLAINED: material changed paths require explanation: {paths}"
    return None


def next_record(
    task: str,
    revision: int,
    timestamp: str,
    worktree: Path,
    history: list[Meta],
    action: str,
    *,
    scope_paths: list[str] | None = None,
    paths: list[str] | None = None,
    reason: str | None = None,
    generated: bool = False,
) -> tuple[Meta, list[Meta]]:
    """Build one ordered, revision-fenced change-drift record."""
    if action == "baseline":
        if history and completion_error(history) is not None:
            raise RuntimeError("change-drift baseline requires completion of the active cycle")
        return baseline(task, revision, timestamp, worktree, scope_paths or []), []
    if action == "delta":
        base = latest(history, "baseline")
        if base is None or history[-1]["kind"] not in {"baseline", "rescope"}:
            raise RuntimeError("change-drift delta requires a baseline")
        return (
            delta(
                task,
                revision,
                timestamp,
                worktree,
                base,
                active_scope(history, base),
                history[-1]["digest"],
            ),
            history,
        )
    if action == "explain":
        current = latest(history, "delta")
        if current is None:
            raise RuntimeError("change-drift explanation requires a delta")
        return (
            explain(
                task,
                revision,
                timestamp,
                current["digest"],
                paths or [],
                reason or "",
                generated,
                history[-1]["digest"],
            ),
            history,
        )
    if action == "rescope":
        base = latest(history, "baseline")
        if base is None or history[-1]["kind"] not in {"baseline", "rescope"}:
            raise RuntimeError("change-drift re-scope requires a baseline")
        return (
            rescope(
                task,
                revision,
                timestamp,
                base["digest"],
                scope_paths or [],
                history[-1]["digest"],
            ),
            history,
        )
    raise ValueError("unknown change-drift action")


def bound_worktree(meta: Meta, projects_root: Path) -> Path:
    """Resolve the task's declared worktree without accepting arbitrary paths."""
    key = meta.get("worktree_key")
    if not isinstance(key, str) or not key:
        raise RuntimeError("change-drift requires a bound worktree")
    return projects_root.resolve() / key


def apply(args: argparse.Namespace, meta: Meta, projects_root: Path, timestamp: str) -> str:
    """Apply the command boundary's owner/revision-fenced drift mutation."""
    if meta.get("owner") != args.owner or meta.get("status") != "in_progress":
        raise RuntimeError("change-drift requires the active task owner")
    if args.expected_revision != meta["task_revision"]:
        raise RuntimeError(
            f"stale revision: expected {args.expected_revision}, current {meta['task_revision']}"
        )
    history = records(meta)
    revision = int(meta["task_revision"]) + 1
    record, history = next_record(
        args.task,
        revision,
        timestamp,
        bound_worktree(meta, projects_root),
        history,
        args.change_drift_action,
        scope_paths=getattr(args, "scope_path", None),
        paths=getattr(args, "path", None),
        reason=getattr(args, "reason", None),
        generated=getattr(args, "generated", False),
    )
    if len(history) >= MAX_RECORDS:
        raise RuntimeError("change-drift active cycle reached its bounded record limit")
    meta["change_drift"] = [*history, record]
    return f"Recorded change-drift {args.change_drift_action} {record['digest']}."


def add_command_parser(commands: Any) -> None:
    """Register the complete bounded change-drift CLI grammar."""
    item = commands.add_parser("change-drift")
    drift_commands = item.add_subparsers(dest="change_drift_action", required=True)
    for action in ("baseline", "delta", "rescope"):
        drift = drift_commands.add_parser(action)
        drift.add_argument("task")
        drift.add_argument("--owner", required=True)
        drift.add_argument("--expected-revision", type=int, required=True)
        if action in {"baseline", "rescope"}:
            drift.add_argument("--scope-path", action="append", required=True)
    drift = drift_commands.add_parser("explain")
    drift.add_argument("task")
    drift.add_argument("--owner", required=True)
    drift.add_argument("--expected-revision", type=int, required=True)
    drift.add_argument("--path", action="append", required=True)
    drift.add_argument("--reason", required=True)
    drift.add_argument("--generated", action="store_true")
