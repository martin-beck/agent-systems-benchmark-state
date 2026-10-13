# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Bounded, explicit freshness revalidation for task assumptions.

An assumption is deliberately opt-in.  A task author chooses whether a base,
dependency, or local observation is material; only a declared material
assumption can delay the task's acceptance or ``done`` release.  Freshness is
always derived from a new observation, rather than being an untrusted mutable
``stale`` flag in task metadata.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import stat
import subprocess
from pathlib import Path
from typing import Any

if __package__:
    from .change_drift import safe_path
else:  # pragma: no cover - direct handoffctl execution
    from change_drift import safe_path  # type: ignore[import-not-found,no-redef]

type Meta = dict[str, Any]

SCHEMA_VERSION = 1
MAX_RECORDS = 64
TASK = re.compile(r"^AR-[0-9]{4}$")
ASSUMPTION_ID = re.compile(r"^[a-z][a-z0-9-]{0,63}$")
KINDS = frozenset({"base", "dependency", "observation"})
ACTIONS = frozenset({"declare", "revalidate", "dispose"})
DIGEST = re.compile(r"^sha256:[0-9a-f]{64}$")
RECORD_FIELDS = frozenset(
    {
        "schema_version",
        "action",
        "id",
        "kind",
        "material",
        "binding",
        "task_revision",
        "previous_digest",
        "reason",
        "digest",
    }
)


def _canonical(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")


def _digest(value: object) -> str:
    return "sha256:" + hashlib.sha256(_canonical(value)).hexdigest()


def _within(parent: Path, child: Path) -> bool:
    try:
        child.relative_to(parent)
    except ValueError:
        return False
    return True


def _worktree(projects_root: Path, meta: Meta) -> Path:
    key = meta.get("worktree_key")
    if not safe_path(key):
        raise RuntimeError("assumption base requires a safely bound worktree")
    root = projects_root.resolve()
    path = (root / str(key)).resolve()
    if not _within(root, path) or not path.is_dir():
        raise RuntimeError("assumption base worktree is unavailable")
    return path


def _git_head(worktree: Path) -> str:
    result = subprocess.run(  # noqa: S603 - fixed Git executable and bounded arguments
        ["git", "-C", str(worktree), "rev-parse", "--verify", "HEAD^{commit}"],  # noqa: S607
        check=False,
        stdin=subprocess.DEVNULL,
        capture_output=True,
        text=True,
        timeout=10,
    )
    head = result.stdout.strip()
    if result.returncode != 0 or re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", head) is None:
        raise RuntimeError("assumption base observation requires a Git HEAD")
    return head


def _file_digest(root: Path, ref: str) -> str:
    if not safe_path(ref):
        raise RuntimeError("assumption observation ref is unsafe")
    target = (root / ref).resolve()
    if not _within(root.resolve(), target):
        raise RuntimeError("assumption observation ref escapes the state root")
    try:
        mode = target.stat().st_mode
    except OSError as error:
        raise RuntimeError("assumption observation is unavailable") from error
    if not stat.S_ISREG(mode) or target.is_symlink() or target.stat().st_size > 1024 * 1024:
        raise RuntimeError("assumption observation must be a bounded regular file")
    return "sha256:" + hashlib.sha256(target.read_bytes()).hexdigest()


def _dependency(tasks: list[Meta], dependency_id: str) -> Meta:
    if not TASK.fullmatch(dependency_id):
        raise RuntimeError("assumption dependency is invalid")
    dependency = next((task for task in tasks if task.get("id") == dependency_id), None)
    if dependency is None or type(dependency.get("task_revision")) is not int:
        raise RuntimeError("assumption dependency is unavailable")
    return {"task": dependency_id, "task_revision": dependency["task_revision"]}


def _binding(
    root: Path, projects_root: Path, meta: Meta, tasks: list[Meta], kind: str, reference: str
) -> Meta:
    if kind == "base":
        if reference != "":
            raise RuntimeError("assumption base does not accept a reference")
        return {"head": _git_head(_worktree(projects_root, meta))}
    if kind == "dependency":
        return _dependency(tasks, reference)
    if kind == "observation":
        return {"ref": reference, "digest": _file_digest(root, reference)}
    raise RuntimeError("assumption kind is invalid")


def _record(
    action: str,
    assumption_id: str,
    kind: str,
    material: bool,
    binding: Meta,
    revision: int,
    previous_digest: str,
    reason: str = "",
) -> Meta:
    if (
        action not in ACTIONS
        or not ASSUMPTION_ID.fullmatch(assumption_id)
        or kind not in KINDS
        or type(material) is not bool
        or type(revision) is not int
        or revision < 1
        or (previous_digest and not DIGEST.fullmatch(previous_digest))
    ):
        raise ValueError("invalid assumption record identity")
    identity: Meta = {
        "schema_version": SCHEMA_VERSION,
        "action": action,
        "id": assumption_id,
        "kind": kind,
        "material": material,
        "binding": binding,
        "task_revision": revision,
        "previous_digest": previous_digest,
        "reason": reason,
    }
    return {**identity, "digest": _digest(identity)}


def _validate_binding(kind: str, binding: object) -> None:
    if not isinstance(binding, dict):
        raise ValueError("assumption binding is invalid")
    if kind == "base":
        if (
            set(binding) != {"head"}
            or re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", str(binding.get("head", ""))) is None
        ):
            raise ValueError("assumption base binding is invalid")
    elif kind == "dependency":
        if (
            set(binding) != {"task", "task_revision"}
            or not TASK.fullmatch(str(binding.get("task", "")))
            or type(binding.get("task_revision")) is not int
            or int(binding["task_revision"]) < 1
        ):
            raise ValueError("assumption dependency binding is invalid")
    elif kind == "observation":
        if (
            set(binding) != {"ref", "digest"}
            or not safe_path(binding.get("ref"))
            or not DIGEST.fullmatch(str(binding.get("digest", "")))
        ):
            raise ValueError("assumption observation binding is invalid")
    else:
        raise ValueError("assumption kind is invalid")


def _record_fields(record: object) -> Meta:
    if not isinstance(record, dict) or set(record) != RECORD_FIELDS:
        raise ValueError("assumption record fields are not exact")
    return record


def _validate_identity(record: Meta) -> None:
    identity = {key: record[key] for key in record if key != "digest"}
    predecessor = record["previous_digest"]
    valid = all(
        (
            record.get("schema_version") == SCHEMA_VERSION,
            record.get("action") in ACTIONS,
            ASSUMPTION_ID.fullmatch(str(record.get("id", ""))) is not None,
            record.get("kind") in KINDS,
            type(record.get("material")) is bool,
            type(record.get("task_revision")) is int and int(record["task_revision"]) >= 1,
            isinstance(predecessor, str),
            isinstance(record.get("reason"), str),
            len(str(record["reason"])) <= 512,
            "\n" not in str(record["reason"]),
            record.get("digest") == _digest(identity),
        )
    )
    if not valid or (predecessor and not DIGEST.fullmatch(str(predecessor))):
        raise ValueError("assumption record identity is invalid")


def _validate_disposition(record: Meta) -> None:
    if record["action"] == "dispose":
        if not record["reason"].strip():
            raise ValueError("assumption disposition reason is invalid")
    elif record["reason"]:
        raise ValueError("assumption non-disposition reason is invalid")


def _validate(record: object) -> Meta:
    record = _record_fields(record)
    _validate_identity(record)
    _validate_disposition(record)
    _validate_binding(str(record["kind"]), record["binding"])
    return record


def records(meta: Meta) -> list[Meta]:
    """Validate and return the bounded, append-only assumption history."""
    ledger = meta.get("assumption_revalidation", [])
    if not isinstance(ledger, list) or len(ledger) > MAX_RECORDS:
        raise ValueError("assumption history is invalid")
    previous_digest = ""
    previous_revision = 0
    active: dict[str, Meta] = {}
    for raw in ledger:
        record = _validate(raw)
        if (
            record["previous_digest"] != previous_digest
            or record["task_revision"] <= previous_revision
        ):
            raise ValueError("assumption history is not linked")
        old = active.get(record["id"])
        if record["action"] == "declare":
            if old is not None:
                raise ValueError("assumption is declared more than once")
        else:
            if (
                old is None
                or old["kind"] != record["kind"]
                or old["material"] != record["material"]
            ):
                raise ValueError("assumption follow-up is not linked to declaration")
            if old["action"] == "dispose":
                raise ValueError("disposed assumption cannot be changed")
            if record["action"] == "revalidate" and old["binding"] == record["binding"]:
                raise ValueError("assumption revalidation requires a changed binding")
        active[record["id"]] = record
        previous_digest = record["digest"]
        previous_revision = record["task_revision"]
    return ledger


def active(records_value: list[Meta]) -> dict[str, Meta]:
    return {record["id"]: record for record in records_value}


def metadata_error(meta: Meta) -> str | None:
    try:
        records(meta)
    except ValueError as error:
        return str(error)
    return None


def needs_admission(meta: Meta) -> bool:
    """Return whether an active material record needs a freshness lookup."""
    return any(
        record["material"] and record["action"] != "dispose"
        for record in active(records(meta)).values()
    )


def current_binding(
    root: Path, projects_root: Path, meta: Meta, tasks: list[Meta], record: Meta
) -> Meta:
    """Observe the binding for one validated active assumption record."""
    _validate(record)
    reference = ""
    if record["kind"] == "dependency":
        reference = str(record["binding"]["task"])
    elif record["kind"] == "observation":
        reference = str(record["binding"]["ref"])
    return _binding(root, projects_root, meta, tasks, str(record["kind"]), reference)


def admission_error(root: Path, projects_root: Path, meta: Meta, tasks: list[Meta]) -> str | None:
    """Return the explicit revalidation requirement for stale material inputs."""
    try:
        current = active(records(meta))
        for assumption_id, record in current.items():
            if not record["material"] or record["action"] == "dispose":
                continue
            if current_binding(root, projects_root, meta, tasks, record) != record["binding"]:
                return f"ASSUMPTION_REVALIDATION_REQUIRED: {assumption_id} ({record['kind']})"
    except (RuntimeError, ValueError) as error:
        return f"ASSUMPTION_REVALIDATION_REQUIRED: {error}"
    return None


def _require_fenced_owner(args: argparse.Namespace, meta: Meta) -> None:
    if args.task != meta.get("id"):
        raise RuntimeError("assumption task does not match selected task")
    if meta.get("owner") != args.owner:
        raise RuntimeError(f"{args.task} is owned by {meta.get('owner') or 'nobody'}")
    if meta.get("status") != "in_progress":
        raise RuntimeError("assumption changes require an active task")
    if args.expected_revision != meta.get("task_revision"):
        raise RuntimeError(
            f"stale revision: expected {args.expected_revision}, "
            f"current {meta.get('task_revision')}"
        )


def _request_identity(args: argparse.Namespace, existing: Meta | None) -> tuple[bool, str, str]:
    """Return declared materiality, kind, and fixed reference for one action."""
    action = args.assumption_action
    if action == "declare":
        if existing is not None:
            raise RuntimeError("assumption is already declared")
        if args.kind is None or args.material is None:
            raise RuntimeError("assumption declaration requires kind and material policy")
        return bool(args.material), str(args.kind), str(args.reference or "")
    return _followup_identity(args, existing)


def _followup_identity(args: argparse.Namespace, existing: Meta | None) -> tuple[bool, str, str]:
    """Keep follow-up assumptions pinned to their original declaration."""
    if existing is None:
        raise RuntimeError("assumption must be declared before follow-up")
    material, kind = bool(existing["material"]), str(existing["kind"])
    if existing["action"] == "dispose":
        raise RuntimeError("disposed assumption cannot be changed")
    if args.kind is not None and args.kind != kind:
        raise RuntimeError("assumption kind cannot change")
    if kind == "dependency":
        return material, kind, str(existing["binding"]["task"])
    if kind == "observation":
        return material, kind, str(existing["binding"]["ref"])
    if args.reference:
        raise RuntimeError("assumption base does not accept a reference")
    return material, kind, ""


def apply(
    root: Path, projects_root: Path, args: argparse.Namespace, meta: Meta, tasks: list[Meta]
) -> str:
    """Append a fenced declaration, changed-binding revalidation, or disposition."""
    _require_fenced_owner(args, meta)
    history = records(meta)
    if len(history) >= MAX_RECORDS:
        raise RuntimeError("assumption history reached its bounded record limit")
    existing = active(history).get(args.assumption_id)
    material, kind, reference = _request_identity(args, existing)
    action = args.assumption_action
    binding = _binding(root, projects_root, meta, tasks, kind, reference)
    if action == "revalidate" and (existing is None or binding == existing["binding"]):
        raise RuntimeError("assumption revalidation requires a changed binding")
    if action == "dispose" and not args.reason.strip():
        raise RuntimeError("assumption disposition requires a reason")
    record = _record(
        action,
        args.assumption_id,
        kind,
        material,
        binding,
        int(meta["task_revision"]) + 1,
        history[-1]["digest"] if history else "",
        args.reason if action == "dispose" else "",
    )
    meta["assumption_revalidation"] = [*history, record]
    return f"Recorded assumption {action} for {args.assumption_id}."


def add_command_parser(commands: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    item = commands.add_parser("assumption")
    actions = item.add_subparsers(dest="assumption_action", required=True)
    for action in ("declare", "revalidate", "dispose"):
        child = actions.add_parser(action)
        child.add_argument("task")
        child.add_argument("--owner", required=True)
        child.add_argument("--expected-revision", type=int, required=True)
        child.add_argument("--assumption-id", required=True)
        child.add_argument("--kind", choices=sorted(KINDS))
        child.add_argument("--reference")
        child.add_argument("--reason", default="")
        group = child.add_mutually_exclusive_group()
        group.add_argument("--material", action="store_true")
        group.add_argument("--non-material", dest="material", action="store_false")
        child.set_defaults(material=None)
