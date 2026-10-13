# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Internal Git fast-receipt executor; no queued intent is a completed task."""

from __future__ import annotations

import argparse
import datetime as dt
import fcntl
import hashlib
import json
import os
import re
import signal
import stat
import threading
import time
import uuid
from collections.abc import Iterator
from contextlib import contextmanager
from typing import Any

if __package__:
    from .fast_receipts import ReceiptStore, validate_update_changes
    from .session_records import MAX_SESSION_RECORDS, validate_session_record
else:  # pragma: no cover - direct vendored import
    from fast_receipts import (  # type: ignore[import-not-found,no-redef]
        ReceiptStore,
        validate_update_changes,
    )
    from session_records import (  # type: ignore[import-not-found,no-redef]
        MAX_SESSION_RECORDS,
        validate_session_record,
    )

_OID = re.compile(r"[0-9a-f]{40}\Z")
_REJECTABLE = (
    "stale revision",
    "is owned by",
    "heartbeat requires an active task",
    "is not planned",
    "is not open",
    "unfinished dependencies",
    "has active claim metadata",
    "owner already holds",
    "role admission denied",
    "claim worker identity is not a live matching process",
)
_HEARTBEAT_FIELDS = frozenset(("task_revision", "updated_at", "claim_expires"))
_CLAIM_FIELDS = frozenset(
    ("task_revision", "updated_at", "claim_expires", "owner", "status", "claim_process")
)
_PROMOTE_FIELDS = frozenset(("task_revision", "updated_at", "status"))
_UPDATE_FIELDS = frozenset(
    ("task_revision", "updated_at", "status", "priority", "summary", "next_action")
)


def _require_bound_store(core: Any, store: ReceiptStore) -> None:
    core.assert_project_binding()
    if core.backend_selection()["backend"] != "git":
        raise RuntimeError("fast receipts require Git authority")
    expected = core.coordinator_lock_path().parent / "fast-receipts.sqlite3"
    if (
        store.project_id != core.project_binding()["project_id"]
        or store.path.resolve() != expected.resolve()
    ):
        raise RuntimeError("fast receipt store does not match the bound project")


@contextmanager
def _private_lock(core: Any, filename: str) -> Iterator[None]:
    path = core.coordinator_lock_path().parent / filename
    path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    parent = path.parent.lstat()
    if (
        not stat.S_ISDIR(parent.st_mode)
        or parent.st_uid != os.geteuid()
        or stat.S_IMODE(parent.st_mode) & 0o077
    ):
        raise RuntimeError("fast receipt service directory is not private")
    descriptor = os.open(path, os.O_CREAT | os.O_RDWR | os.O_NOFOLLOW, 0o600)
    try:
        info = os.fstat(descriptor)
        current = path.lstat()
        if (
            not stat.S_ISREG(info.st_mode)
            or info.st_uid != os.geteuid()
            or info.st_nlink != 1
            or stat.S_IMODE(info.st_mode) != 0o600
            or (info.st_dev, info.st_ino) != (current.st_dev, current.st_ino)
        ):
            raise RuntimeError("fast receipt service lock is unsafe")
        try:
            fcntl.flock(descriptor, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as error:
            raise RuntimeError("fast receipt service is already active") from error
        yield
    finally:
        fcntl.flock(descriptor, fcntl.LOCK_UN)
        os.close(descriptor)


@contextmanager
def service_lock(core: Any) -> Iterator[None]:
    """Fence recovery and execution to one process per Git common directory."""
    with _private_lock(core, "fast-receipts.service.lock"):
        yield


@contextmanager
def publication_lock(core: Any) -> Iterator[None]:
    """Fence remote observation/push without blocking local intent execution."""
    with _private_lock(core, "fast-receipts.publication.lock"):
        yield


def _git(core: Any, *args: str, check: bool = True) -> str:
    command = ["git", "-C", str(core.ROOT), *args]
    result = core.run(command, check=check)
    return str(result.stdout)


def _task_record(core: Any, oid: str, path: str) -> tuple[dict[str, Any], str]:
    source = _git(core, "show", f"{oid}:{path}")
    if not source.startswith("---\n"):
        raise RuntimeError("receipt task has no front matter")
    end = source.find("\n---\n", 4)
    if end < 0:
        raise RuntimeError("receipt task front matter is incomplete")
    value = json.loads(source[4:end])
    if not isinstance(value, dict):
        raise RuntimeError("receipt task front matter is invalid")
    return value, source[end + 5 :]


def _task_views(core: Any, oid: str) -> dict[str, str]:
    """Render task-derived projections from the exact committed task snapshot."""
    tasks = []
    for name in _git(core, "ls-tree", "-r", "--name-only", oid, "tasks").splitlines():
        if name.startswith("tasks/") and name.endswith(".md"):
            meta, body = _task_record(core, oid, name)
            tasks.append((core.ROOT / name, meta, body))
    views = {"CURRENT.md": core.render_current(tasks)}
    if core.project_settings()["status_view"]:
        views.update(core.render_status_views(tasks))
    return views


def _task_change(
    core: Any, oid: str, task: str, *, sidecars: frozenset[str] = frozenset()
) -> tuple[dict[str, Any], str, dict[str, Any], str]:
    paths = _git(core, "diff-tree", "--no-commit-id", "--name-only", "-r", oid).splitlines()
    matches = [
        path
        for path in paths
        if path == f"tasks/{task}.md"
        or (path.startswith(f"tasks/{task}-") and path.endswith(".md"))
    ]
    if len(matches) != 1:
        raise RuntimeError("receipt commit does not change exactly one target task")
    projections = set(paths) - set(matches)
    if any(
        projection not in sidecars
        and projection not in {"CURRENT.md", "STATUS.md"}
        and not projection.startswith("status/STATUS-")
        for projection in projections
    ):
        raise RuntimeError("receipt commit changes paths outside target task")
    parent = _git(core, "rev-parse", f"{oid}^").strip()
    if not _OID.fullmatch(parent):
        raise RuntimeError("receipt commit has no valid parent")
    before_meta, before_body = _task_record(core, parent, matches[0])
    after_meta, after_body = _task_record(core, oid, matches[0])
    before_views = _task_views(core, parent)
    views = _task_views(core, oid)
    if not projections <= set(before_views) | set(views) | sidecars:
        raise RuntimeError("receipt commit changes paths outside target task")
    for projection, expected in views.items():
        found = _git(core, "show", f"{oid}:{projection}", check=False)
        if found != expected:
            raise RuntimeError("receipt commit task projection does not match committed tasks")
    for projection in set(before_views) - set(views):
        if _git(core, "ls-tree", "--name-only", oid, "--", projection).strip():
            raise RuntimeError("receipt commit retains an obsolete task projection")
    return before_meta, before_body, after_meta, after_body


def _verify_heartbeat_delta(
    core: Any, intent: dict[str, Any], payload: dict[str, Any], oid: str
) -> int:
    before, before_body, after, after_body = _task_change(core, oid, str(intent["task_id"]))
    expected_before = int(intent["expected_revision"])
    owner = payload.get("owner")
    if (
        before.get("id") != intent["task_id"]
        or before.get("owner") != owner
        or before.get("status") != "in_progress"
        or before.get("task_revision") != expected_before
        or after.get("id") != intent["task_id"]
        or after.get("owner") != owner
        or after.get("status") != "in_progress"
        or after.get("task_revision") != expected_before + 1
    ):
        raise RuntimeError("receipt commit task state does not match intent")
    before_stable = {key: value for key, value in before.items() if key not in _HEARTBEAT_FIELDS}
    after_stable = {key: value for key, value in after.items() if key not in _HEARTBEAT_FIELDS}
    if before_stable != after_stable:
        raise RuntimeError("receipt commit changes non-heartbeat task fields")
    updated = dt.datetime.fromisoformat(str(after["updated_at"]))
    expiry = dt.datetime.fromisoformat(str(after["claim_expires"]))
    if updated.tzinfo is None or expiry.tzinfo is None:
        raise RuntimeError("receipt commit heartbeat timestamps are naive")
    seconds = (expiry - updated).total_seconds()
    requested = int(payload["lease_minutes"]) * 60
    if abs(seconds - requested) > 2:
        raise RuntimeError("receipt commit lease does not match queued heartbeat")
    expected_body = core._transition_note(
        before_body, f"Heartbeat by {owner}.", str(after["updated_at"])
    )
    if after_body != expected_body:
        raise RuntimeError("receipt commit body does not match heartbeat")
    return expected_before + 1


def _verify_promote_delta(
    core: Any, intent: dict[str, Any], payload: dict[str, Any], oid: str
) -> int:
    before, before_body, after, after_body = _task_change(core, oid, str(intent["task_id"]))
    expected_before = int(intent["expected_revision"])
    if (
        before.get("id") != intent["task_id"]
        or before.get("status") != "planned"
        or before.get("owner")
        or before.get("claim_expires")
        or before.get("task_revision") != expected_before
        or after.get("id") != intent["task_id"]
        or after.get("status") != "open"
        or after.get("owner")
        or after.get("claim_expires")
        or after.get("task_revision") != expected_before + 1
    ):
        raise RuntimeError("receipt commit task state does not match promote intent")
    before_stable = {key: value for key, value in before.items() if key not in _PROMOTE_FIELDS}
    after_stable = {key: value for key, value in after.items() if key not in _PROMOTE_FIELDS}
    if before_stable != after_stable:
        raise RuntimeError("receipt commit changes non-promote task fields")
    expected_body = core._transition_note(
        before_body, str(payload["note"]), str(after["updated_at"])
    )
    if after_body != expected_body:
        raise RuntimeError("receipt commit body does not match promote")
    return expected_before + 1


def _verify_claim_delta(
    core: Any, intent: dict[str, Any], payload: dict[str, Any], oid: str
) -> int:
    before, before_body, after, after_body = _task_change(core, oid, str(intent["task_id"]))
    expected_before = int(intent["expected_revision"])
    owner = payload.get("owner")
    identity = after.get("claim_process")
    identity_matches = (
        identity is None
        if "worker_pid" not in payload
        else isinstance(identity, dict)
        and identity.get("pid") == payload["worker_pid"]
        and identity.get("start_time") == payload["worker_start_time"]
        and core.scoped_claim_process(identity)
    )
    if (
        before.get("id") != intent["task_id"]
        or before.get("status") != "open"
        or before.get("owner")
        or before.get("claim_expires")
        or before.get("task_revision") != expected_before
        or after.get("id") != intent["task_id"]
        or after.get("status") != "in_progress"
        or after.get("owner") != owner
        or after.get("task_revision") != expected_before + 1
        or not identity_matches
    ):
        raise RuntimeError("receipt commit task state does not match claim intent")
    before_stable = {key: value for key, value in before.items() if key not in _CLAIM_FIELDS}
    after_stable = {key: value for key, value in after.items() if key not in _CLAIM_FIELDS}
    if before_stable != after_stable:
        raise RuntimeError("receipt commit changes non-claim task fields")
    updated = dt.datetime.fromisoformat(str(after["updated_at"]))
    expiry = dt.datetime.fromisoformat(str(after["claim_expires"]))
    if updated.tzinfo is None or expiry.tzinfo is None:
        raise RuntimeError("receipt commit claim timestamps are naive")
    requested = int(payload["lease_minutes"]) * 60
    if abs((expiry - updated).total_seconds() - requested) > 2:
        raise RuntimeError("receipt commit lease does not match queued claim")
    expected_body = core._transition_note(
        before_body, f"Claimed by {owner}.", str(after["updated_at"])
    )
    if after_body != expected_body:
        raise RuntimeError("receipt commit body does not match claim")
    return expected_before + 1


def _verify_update_delta(
    core: Any, intent: dict[str, Any], payload: dict[str, Any], oid: str
) -> int:
    """Require a receipt update to change exactly its closed metadata descriptor."""
    task = str(intent["task_id"])
    session = f"sessions/{task}.jsonl"
    before, before_body, after, after_body = _task_change(
        core, oid, task, sidecars=frozenset((session,))
    )
    expected_before = int(intent["expected_revision"])
    owner = payload.get("owner")
    changes = payload.get("changes")
    if not isinstance(changes, dict):
        raise RuntimeError("receipt update changes are invalid")
    if (
        before.get("id") != intent["task_id"]
        or before.get("owner") != owner
        or before.get("status") != "in_progress"
        or before.get("task_revision") != expected_before
        or after.get("id") != intent["task_id"]
        or after.get("owner") != owner
        or after.get("status") != "in_progress"
        or after.get("task_revision") != expected_before + 1
    ):
        raise RuntimeError("receipt commit task state does not match update intent")
    before_stable = {key: value for key, value in before.items() if key not in _UPDATE_FIELDS}
    after_stable = {key: value for key, value in after.items() if key not in _UPDATE_FIELDS}
    if before_stable != after_stable:
        raise RuntimeError("receipt commit changes non-update task fields")
    for name in ("status", "priority", "summary", "next_action"):
        expected = changes.get(name, before.get(name))
        if after.get(name) != expected:
            raise RuntimeError("receipt commit changes fields outside update intent")
    expected_body = core._transition_note(
        before_body, str(payload["note"]), str(after["updated_at"])
    )
    if after_body != expected_body:
        raise RuntimeError("receipt commit body does not match update")
    _verify_update_session(core, oid, session, task, after)
    return expected_before + 1


def _session_rows(source: str, task: str) -> list[dict[str, Any]]:
    """Decode the bounded canonical session projection from one Git tree."""
    rows: list[dict[str, Any]] = []
    revisions: set[int] = set()
    for number, line in enumerate(source.splitlines(), 1):
        try:
            row = json.loads(line)
        except json.JSONDecodeError as error:
            raise RuntimeError(f"receipt session line {number} is invalid") from error
        if not isinstance(row, dict):
            raise RuntimeError(f"receipt session line {number} is invalid")
        try:
            validate_session_record(row)
        except ValueError as error:
            raise RuntimeError(f"receipt session line {number} is invalid") from error
        if row["task"] != task or row["task_revision"] in revisions:
            raise RuntimeError("receipt session does not match target task")
        revisions.add(row["task_revision"])
        rows.append(row)
    if len(rows) > MAX_SESSION_RECORDS:
        raise RuntimeError("receipt session exceeds bounded retention")
    return rows


def _verify_update_session(
    core: Any, oid: str, path: str, task: str, after: dict[str, Any]
) -> None:
    """Require the normal update session sidecar to be the exact canonical append."""
    parent = _git(core, "rev-parse", f"{oid}^").strip()
    before = _session_rows(_git(core, "show", f"{parent}:{path}", check=False), task)
    found = _session_rows(_git(core, "show", f"{oid}:{path}", check=False), task)
    expected = core.build_session_record(after, "update", str(after["updated_at"]))
    expected_rows = [*before, expected][-MAX_SESSION_RECORDS:]
    if found != expected_rows:
        raise RuntimeError("receipt session does not match update")


def _require_active_branch_commit(core: Any, oid: str) -> None:
    """Require a well-formed commit reachable from the active state branch."""
    if not _OID.fullmatch(oid):
        raise RuntimeError("invalid receipt commit oid")
    ancestor = core.run(
        ["git", "-C", str(core.ROOT), "merge-base", "--is-ancestor", oid, "HEAD"],
        check=False,
    )
    if ancestor.returncode:
        raise RuntimeError("receipt commit is not on the active state branch")


def _verify_operation_delta(
    core: Any, operation: str, intent: dict[str, Any], payload: dict[str, Any], oid: str
) -> int:
    if operation == "heartbeat":
        return _verify_heartbeat_delta(core, intent, payload, oid)
    if operation == "claim":
        return _verify_claim_delta(core, intent, payload, oid)
    if operation == "update":
        return _verify_update_delta(core, intent, payload, oid)
    return _verify_promote_delta(core, intent, payload, oid)


def verify_local_commit(core: Any, intent: dict[str, Any], oid: str) -> int:
    """Verify exact marker, active-branch commit, and task revision before receipt."""
    _require_active_branch_commit(core, oid)
    message = _git(core, "log", "-1", "--format=%B", oid)
    marker = f"Handoffctl-Receipt: {intent['receipt_id']}"
    lines = message.splitlines()
    if lines.count(marker) != 1:
        raise RuntimeError("receipt commit marker is missing or duplicated")
    operation = str(intent["operation"])
    if operation not in {"claim", "heartbeat", "promote", "update"}:
        raise RuntimeError("receipt operation is unsupported")
    if not lines or lines[0] != f"chore(state): {operation} {intent['task_id']}":
        raise RuntimeError("receipt commit operation does not match intent")
    payload = json.loads(str(intent["payload_json"]))
    if not isinstance(payload, dict):
        raise RuntimeError("receipt intent payload is invalid")
    expected = _verify_operation_delta(core, operation, intent, payload, oid)
    if core.project_settings()["commit_signoff"]:
        committer = _git(core, "show", "-s", "--format=%cn <%ce>", oid).strip()
        if lines.count(f"Signed-off-by: {committer}") != 1:
            raise RuntimeError("receipt commit DCO does not match committer")
    return expected


def find_receipt_commit(core: Any, receipt_id: str) -> str | None:
    marker = f"Handoffctl-Receipt: {receipt_id}"
    candidates = _git(core, "log", "--all", "--format=%H", "--grep", marker).splitlines()
    exact = [
        oid
        for oid in candidates
        if _OID.fullmatch(oid)
        and _git(core, "log", "-1", "--format=%B", oid).splitlines().count(marker) == 1
    ]
    if len(exact) > 1:
        raise RuntimeError("multiple commits carry one receipt marker")
    return exact[0] if exact else None


def _validated_intent(intent: dict[str, Any]) -> dict[str, Any]:
    payload_text = str(intent["payload_json"])
    payload = json.loads(payload_text)
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    if (
        not isinstance(payload, dict)
        or payload_text != canonical
        or hashlib.sha256(canonical.encode()).hexdigest() != intent["input_digest"]
        or payload.get("project_id") != intent["project_id"]
        or payload.get("task") != intent["task_id"]
        or payload.get("expected_revision") != intent["expected_revision"]
    ):
        raise RuntimeError("receipt intent does not match canonical typed fields")
    if payload.get("operation") == "heartbeat" and (
        set(payload)
        != {"expected_revision", "lease_minutes", "operation", "owner", "project_id", "task"}
        or not isinstance(payload.get("owner"), str)
        or not isinstance(payload.get("lease_minutes"), int)
        or isinstance(payload.get("lease_minutes"), bool)
        or not 1 <= payload["lease_minutes"] <= 1440
        or not isinstance(payload.get("expected_revision"), int)
        or isinstance(payload.get("expected_revision"), bool)
        or payload["expected_revision"] < 1
    ):
        raise RuntimeError(f"receipt {payload.get('operation')} intent fields are invalid")
    if payload.get("operation") == "claim" and (
        set(payload)
        not in (
            {"expected_revision", "lease_minutes", "operation", "owner", "project_id", "task"},
            {
                "expected_revision",
                "lease_minutes",
                "operation",
                "owner",
                "project_id",
                "task",
                "worker_pid",
                "worker_start_time",
            },
        )
        or not isinstance(payload.get("owner"), str)
        or not isinstance(payload.get("lease_minutes"), int)
        or isinstance(payload.get("lease_minutes"), bool)
        or not 1 <= payload["lease_minutes"] <= 1440
        or not isinstance(payload.get("expected_revision"), int)
        or isinstance(payload.get("expected_revision"), bool)
        or payload["expected_revision"] < 1
        or (
            "worker_pid" in payload
            and (
                type(payload["worker_pid"]) is not int
                or payload["worker_pid"] <= 0
                or type(payload["worker_start_time"]) is not int
                or payload["worker_start_time"] < 0
            )
        )
    ):
        raise RuntimeError("receipt claim intent fields are invalid")
    if payload.get("operation") == "promote" and (
        set(payload) != {"expected_revision", "note", "operation", "project_id", "task"}
        or not isinstance(payload.get("note"), str)
        or not 1 <= len(payload["note"]) <= 4096
        or "\x00" in payload["note"]
        or not isinstance(payload.get("expected_revision"), int)
        or isinstance(payload.get("expected_revision"), bool)
        or payload["expected_revision"] < 1
    ):
        raise RuntimeError("receipt promote intent fields are invalid")
    if payload.get("operation") == "update" and (
        set(payload)
        != {"changes", "expected_revision", "note", "operation", "owner", "project_id", "task"}
        or not isinstance(payload.get("owner"), str)
        or not isinstance(payload.get("note"), str)
        or not 1 <= len(payload["note"]) <= 4096
        or "\x00" in payload["note"]
        or not isinstance(payload.get("expected_revision"), int)
        or isinstance(payload.get("expected_revision"), bool)
        or payload["expected_revision"] < 1
    ):
        raise RuntimeError("receipt update intent fields are invalid")
    if payload.get("operation") == "update":
        try:
            validate_update_changes(payload.get("changes"))
        except ValueError as error:
            raise RuntimeError("receipt update intent fields are invalid") from error
    if payload.get("operation") not in {"claim", "heartbeat", "promote", "update"}:
        raise RuntimeError("receipt operation is unsupported")
    return payload


def process_one(core: Any, store: ReceiptStore) -> dict[str, Any] | None:
    """Execute one intent; unknown post-commit state remains explicitly ambiguous."""
    _require_bound_store(core, store)
    intent = store.claim_next()
    if intent is None:
        return None
    receipt_id = str(intent["receipt_id"])
    try:
        payload = _validated_intent(intent)
        operation = str(payload["operation"])
        if operation in {"heartbeat", "claim"}:
            args = argparse.Namespace(
                task=intent["task_id"],
                owner=payload["owner"],
                lease_minutes=payload["lease_minutes"],
                expected_revision=intent["expected_revision"],
                _receipt_id=receipt_id,
                worker_pid=payload.get("worker_pid"),
                worker_start_time=payload.get("worker_start_time"),
            )
        elif operation == "promote":
            args = argparse.Namespace(
                task=intent["task_id"],
                expected_revision=intent["expected_revision"],
                note=payload["note"],
                _receipt_id=receipt_id,
            )
        else:
            changes = payload["changes"]
            args = argparse.Namespace(
                task=intent["task_id"],
                owner=payload["owner"],
                expected_revision=intent["expected_revision"],
                status=changes.get("status"),
                priority=changes.get("priority"),
                summary=changes.get("summary"),
                next_action=changes.get("next_action"),
                note=payload["note"],
                _receipt_id=receipt_id,
            )
        core.mutate(args, operation)
        oid = str(args._committed_oid)
        revision = verify_local_commit(core, intent, oid)
        return store.record_local_commit(receipt_id, oid, revision)
    except Exception as error:
        try:
            recovered = find_receipt_commit(core, receipt_id)
            if recovered is not None:
                revision = verify_local_commit(core, intent, recovered)
                return store.record_local_commit(receipt_id, recovered, revision)
        except Exception:
            return store.record_ambiguity(receipt_id, "COMMIT_EVIDENCE_UNKNOWN")
        if any(text in str(error) for text in _REJECTABLE):
            return store.record_rejection(receipt_id, "ADMISSION_REJECTED")
        return store.record_ambiguity(receipt_id, "MUTATION_OUTCOME_UNKNOWN")


def recover_running(core: Any, store: ReceiptStore) -> list[dict[str, Any]]:
    """Resolve interrupted reservations without re-executing an external effect."""
    _require_bound_store(core, store)
    outcomes: list[dict[str, Any]] = []
    for intent in store.running():
        receipt_id = str(intent["receipt_id"])
        try:
            oid = find_receipt_commit(core, receipt_id)
            if oid is not None:
                revision = verify_local_commit(core, intent, oid)
                outcomes.append(store.record_local_commit(receipt_id, oid, revision))
                continue
        except Exception:
            outcomes.append(store.record_ambiguity(receipt_id, "COMMIT_EVIDENCE_UNKNOWN"))
            continue
        outcomes.append(store.record_ambiguity(receipt_id, "INTERRUPTED_BEFORE_COMMIT"))
    return outcomes


def process_pending(core: Any, store: ReceiptStore, *, limit: int = 16) -> list[dict[str, Any]]:
    """Recover first, then execute bounded queued work under one service lease."""
    if not 1 <= limit <= 1024:
        raise ValueError("invalid fast receipt batch limit")
    with service_lock(core):
        outcomes = recover_running(core, store)
        for _ in range(limit):
            result = process_one(core, store)
            if result is None:
                break
            outcomes.append(result)
        return outcomes


def serve_local(
    core: Any, store: ReceiptStore, *, limit: int = 16, poll_seconds: float = 0.05
) -> None:
    """Run one resident local executor; a restart never blindly replays running work."""
    if not 1 <= limit <= 1024 or not 0.01 <= poll_seconds <= 60:
        raise ValueError("invalid local receipt service limits")
    from .fast_receipt_socket import socket_service

    stopping = threading.Event()
    on_main_thread = threading.current_thread() is threading.main_thread()
    previous_term = signal.getsignal(signal.SIGTERM) if on_main_thread else None
    if on_main_thread:
        signal.signal(signal.SIGTERM, lambda _signum, _frame: stopping.set())
    try:
        with service_lock(core):
            recover_running(core, store)
            with socket_service(core):
                while not stopping.is_set():
                    count = 0
                    for _ in range(limit):
                        if stopping.is_set() or process_one(core, store) is None:
                            break
                        count += 1
                    if count == 0 and not stopping.is_set():
                        time.sleep(poll_seconds)
    finally:
        if previous_term is not None:
            signal.signal(signal.SIGTERM, previous_term)


def _is_ancestor(core: Any, older: str, newer: str) -> bool:
    result = core.run(
        ["git", "-C", str(core.ROOT), "merge-base", "--is-ancestor", older, newer],
        check=False,
    )
    return bool(result.returncode == 0)


def _observe_remote_main(core: Any) -> str | None:
    observed = core.run(
        ["git", "-C", str(core.ROOT), "ls-remote", "--exit-code", "origin", "refs/heads/main"],
        check=False,
    )
    if observed.returncode:
        return None
    lines = str(observed.stdout).splitlines()
    if len(lines) != 1:
        return None
    fields = lines[0].split()
    if len(fields) != 2 or fields[1] != "refs/heads/main" or not _OID.fullmatch(fields[0]):
        return None
    oid = fields[0]
    present = core.run(
        ["git", "-C", str(core.ROOT), "cat-file", "-e", f"{oid}^{{commit}}"],
        check=False,
    )
    if present.returncode:
        core.run(
            ["git", "-C", str(core.ROOT), "fetch", "--no-tags", "origin", oid],
            check=False,
        )
        present = core.run(
            ["git", "-C", str(core.ROOT), "cat-file", "-e", f"{oid}^{{commit}}"],
            check=False,
        )
    return oid if present.returncode == 0 else None


def _publish_if_needed(
    core: Any,
    store: ReceiptStore,
    pending: list[dict[str, Any]],
    local_head: str,
    remote_head: str,
) -> str | None:
    needs_push = any(
        not _is_ancestor(core, str(item["commit_oid"]), remote_head)
        for item in pending
        if _is_ancestor(core, str(item["commit_oid"]), local_head)
    )
    if not needs_push or not _is_ancestor(core, remote_head, local_head):
        return remote_head
    core.assert_project_binding()
    job = store.admit_publication(
        key=f"fast-publisher:{local_head}",
        candidate_oid=local_head,
        expected_remote_oid=remote_head,
    )
    job_id = str(job["job_id"])
    if job["phase"] in {"ambiguous", "publishing"}:
        try:
            job = store.recover_publication(job_id, observed_remote_oid=remote_head)
        except RuntimeError as error:
            if "still active" not in str(error):
                raise
    if job["phase"] == "published":
        return remote_head
    if job["phase"] != "queued":
        return remote_head
    lease = uuid.uuid4().hex
    claimed = store.claim_publication(job_id, lease=lease)
    if claimed is None:
        return remote_head
    try:
        core.run(
            [
                "git",
                "-C",
                str(core.ROOT),
                "push",
                f"--force-with-lease=refs/heads/main:{remote_head}",
                "origin",
                f"{local_head}:refs/heads/main",
            ],
            check=False,
        )
    except Exception:
        _record_admitted_push_observation(core, store, job_id, lease, local_head, "PUSH_UNKNOWN")
        raise

    return _record_admitted_push_observation(
        core, store, job_id, lease, local_head, "REMOTE_UNKNOWN"
    )


def _recover_outstanding_publications(
    store: ReceiptStore, local_head: str, remote_head: str
) -> None:
    """Resolve every nonterminal job; only the current local head may remain queued."""
    for existing in store.recoverable_publications():
        try:
            job_id = str(existing["job_id"])
            if existing["phase"] == "queued":
                if existing["candidate_oid"] == local_head:
                    continue
                store.resolve_superseded_publication(job_id, observed_remote_oid=remote_head)
            else:
                store.recover_publication(job_id, observed_remote_oid=remote_head)
        except RuntimeError as error:
            if not (
                "still active" in str(error)
                or "changed while recovering" in str(error)
                or "changed while resolving" in str(error)
            ):
                raise


def _record_admitted_push_observation(
    core: Any,
    store: ReceiptStore,
    job_id: str,
    lease: str,
    candidate: str,
    unknown_code: str,
) -> str | None:
    """Persist only an exact remote observation for the admitted candidate."""
    observed = _observe_remote_main(core)
    if observed == candidate:
        store.finish_publication(
            job_id,
            lease=lease,
            phase="published",
            observed_remote_oid=observed,
        )
    elif observed is not None and _is_ancestor(core, candidate, observed):
        store.finish_publication(
            job_id,
            lease=lease,
            phase="rejected",
            observed_remote_oid=observed,
            error_code="REMOTE_ADVANCED",
        )
    elif observed is None:
        store.finish_publication(job_id, lease=lease, phase="ambiguous", error_code=unknown_code)
    else:
        store.finish_publication(
            job_id,
            lease=lease,
            phase="rejected",
            observed_remote_oid=observed,
            error_code="REMOTE_CHANGED",
        )
    return observed


def _finish_publications(
    core: Any,
    store: ReceiptStore,
    pending: list[dict[str, Any]],
    local_head: str,
    remote_head: str,
) -> list[dict[str, Any]]:
    outcomes = []
    for item in pending:
        receipt_id = str(item["receipt_id"])
        commit_oid = str(item["commit_oid"])
        if not _is_ancestor(core, commit_oid, local_head):
            outcomes.append(store.record_publication_failure(receipt_id, "LOCAL_BRANCH_MOVED"))
        elif _is_ancestor(core, commit_oid, remote_head):
            outcomes.append(store.record_remote_observation(receipt_id, remote_head))
        else:
            outcomes.append(
                store.record_publication_failure(receipt_id, "REMOTE_NOT_CONTAINING_COMMIT")
            )
    return outcomes


def _publish_selected(
    core: Any, store: ReceiptStore, pending: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    if not core.replication_enabled():
        return [
            store.record_publication_failure(str(item["receipt_id"]), "REPLICATION_DISABLED")
            for item in pending
        ]
    branch = _git(core, "symbolic-ref", "--short", "-q", "HEAD").strip()
    if branch != "main":
        return [
            store.record_publication_failure(str(item["receipt_id"]), "STATE_BRANCH_NOT_MAIN")
            for item in pending
        ]
    local_head = _git(core, "rev-parse", "HEAD").strip()
    if not _OID.fullmatch(local_head):
        raise RuntimeError("cannot identify local publication head")
    remote_head = _observe_remote_main(core)
    if remote_head is None:
        return [
            store.record_publication_failure(str(item["receipt_id"]), "REMOTE_UNKNOWN")
            for item in pending
        ]
    _recover_outstanding_publications(store, local_head, remote_head)
    remote_head = _publish_if_needed(core, store, pending, local_head, remote_head)
    if remote_head is None:
        return [
            store.record_publication_failure(str(item["receipt_id"]), "REMOTE_UNKNOWN")
            for item in pending
        ]
    return _finish_publications(core, store, pending, local_head, remote_head)


def publish_pending(core: Any, store: ReceiptStore) -> list[dict[str, Any]]:
    """Observe exact remote ancestry; a bounded timeout remains a local receipt."""
    _require_bound_store(core, store)
    pending = store.pending_publication()
    try:
        return _publish_selected(core, store, pending)
    except Exception as error:
        timeout_type = getattr(core, "SubprocessTimeoutError", None)
        if not isinstance(timeout_type, type) or not isinstance(error, timeout_type):
            raise
        outcomes: list[dict[str, Any]] = []
        for item in pending:
            receipt_id = str(item["receipt_id"])
            current = store.read(receipt_id)
            if current is None:
                raise RuntimeError("pending receipt disappeared during publication") from error
            if current["phase"] == "published-remote":
                outcomes.append(current)
            elif current["phase"] == "completed-local":
                outcomes.append(store.record_publication_failure(receipt_id, "PUBLICATION_TIMEOUT"))
            else:
                raise RuntimeError("pending receipt entered an invalid phase") from error
        return outcomes


def serve_publication(core: Any, store: ReceiptStore, *, poll_seconds: float = 5.0) -> None:
    """Observe remote completion in a separate fenced process from local writes."""
    if not 0.1 <= poll_seconds <= 60:
        raise ValueError("invalid publication polling interval")
    with publication_lock(core):
        while True:
            publish_pending(core, store)
            time.sleep(poll_seconds)
