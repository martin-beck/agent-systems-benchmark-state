# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Strict, non-authorizing execution-envelope validation and preflight."""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import re
import shutil
import stat
import sys
from contextlib import suppress
from dataclasses import dataclass
from pathlib import Path
from typing import Any

TASK = re.compile(r"^AR-[0-9]{4}$")
REF = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._/-]{2,255}$")
ENVELOPE_ID = re.compile(r"^AR-[0-9]{4}-e[1-9][0-9]*$")
DIGEST = re.compile(r"^sha256:[0-9a-f]{64}$")
COMMAND_CLASSES = frozenset({"read", "test", "source-write", "git-publication"})


@dataclass(frozen=True)
class Preflight:
    """One deterministic, non-mutating command admission result."""

    allowed: bool
    code: str
    detail: str
    envelope_id: str = ""
    envelope_digest: str = ""

    def as_json(self) -> dict[str, object]:
        return {
            "allowed": self.allowed,
            "code": self.code,
            "detail": self.detail,
            "envelope_id": self.envelope_id,
            "envelope_digest": self.envelope_digest,
        }


def digest(payload: bytes) -> str:
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def canonical_digest(value: dict[str, Any]) -> str:
    """Return the stable digest used for an envelope copied into task authority."""
    return digest(json.dumps(value, sort_keys=True, separators=(",", ":")).encode())


def _paths(value: object, field: str, errors: list[str]) -> None:
    if not isinstance(value, list) or not value or len(value) > 64:
        errors.append(f"{field} must be a bounded nonempty list")
        return
    if len(set(value)) != len(value):
        errors.append(f"{field} contains duplicates")
    for item in value:
        path = str(item)
        if not isinstance(item, str) or not REF.fullmatch(path) or path.startswith("."):
            errors.append(f"{field} contains an unsafe path")
            break


def _identity_errors(value: dict[str, Any]) -> list[str]:
    """Validate the stable envelope/task/spec identity fields."""
    result: list[str] = []
    if type(value.get("schema_version")) is not int or value.get("schema_version") != 1:
        result.append("envelope schema_version must be 1")
    envelope_id = value.get("envelope_id")
    task = value.get("task")
    if not isinstance(envelope_id, str) or not ENVELOPE_ID.fullmatch(envelope_id):
        result.append("envelope_id is invalid")
    if not isinstance(task, str) or not TASK.fullmatch(task):
        result.append("task is invalid")
    if (
        isinstance(envelope_id, str)
        and isinstance(task, str)
        and not envelope_id.startswith(task + "-")
    ):
        result.append("envelope_id does not match task")
    result.extend(
        f"{name} is invalid"
        for name in ("envelope_revision", "task_revision", "spec_revision")
        if type(value.get(name)) is not int or value[name] < 1
    )
    if not isinstance(value.get("spec_ref"), str) or not REF.fullmatch(value["spec_ref"]):
        result.append("spec_ref is invalid")
    return result


def _collection_errors(value: dict[str, Any]) -> list[str]:
    """Validate bounded descriptive collections without interpreting their text."""
    result: list[str] = []
    for name in ("outputs", "evidence", "stop_conditions"):
        items = value.get(name)
        if not isinstance(items, list) or not items or len(items) > 32:
            result.append(f"{name} must be a bounded nonempty list")
            continue
        ids = [item.get("id") for item in items if isinstance(item, dict)]
        if (
            len(ids) != len(items)
            or not all(
                isinstance(item, str) and re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{2,63}", item)
                for item in ids
            )
            or len(set(ids)) != len(ids)
        ):
            result.append(f"{name} identifiers are invalid")
    result.extend(_item_shape_errors(value))
    non_goals = value.get("non_goals")
    valid_non_goals = (
        isinstance(non_goals, list)
        and bool(non_goals)
        and len(non_goals) <= 32
        and all(isinstance(item, str) and item.strip() and len(item) <= 240 for item in non_goals)
    )
    if not valid_non_goals:
        result.append("non_goals must be a bounded nonempty string list")
    return result


def _item_shape_errors(value: dict[str, Any]) -> list[str]:
    """Apply the schema's exact output, evidence, and stop-condition item shapes."""
    result: list[str] = []
    for item in value.get("outputs", []):
        if (
            not isinstance(item, dict)
            or set(item) != {"id", "description"}
            or not isinstance(item.get("description"), str)
            or not item["description"].strip()
            or len(item["description"]) > 1000
        ):
            result.append("outputs contain an invalid item")
            break
    for item in value.get("evidence", []):
        if (
            not isinstance(item, dict)
            or set(item) != {"id", "class", "required"}
            or not isinstance(item.get("class"), str)
            or not re.fullmatch(r"[a-z]+(?:-[a-z]+)*", item["class"])
            or type(item.get("required")) is not bool
        ):
            result.append("evidence contain an invalid item")
            break
    return result


def _rule_errors(value: dict[str, Any]) -> list[str]:
    """Validate path, command, and stop-condition rules."""
    result: list[str] = []
    scope = value.get("path_scope")
    if not isinstance(scope, dict) or set(scope) != {"read", "write"}:
        result.append("path_scope must contain exactly read and write")
    else:
        _paths(scope["read"], "path_scope.read", result)
        _paths(scope["write"], "path_scope.write", result)
    classes = value.get("command_classes")
    if not isinstance(classes, dict) or not classes or set(classes) - COMMAND_CLASSES:
        result.append("command_classes are invalid")
    elif any(not _valid_command_rule(rule) for rule in classes.values()):
        result.append("command_classes contain an invalid rule")
    stops = value.get("stop_conditions")
    if not isinstance(stops, list) or not stops or len(stops) > 32:
        result.append("stop_conditions must be a bounded nonempty list")
    elif any(not _valid_stop_condition(item) for item in stops):
        result.append("stop_conditions contain an invalid rule")
    return result


def _valid_command_rule(rule: object) -> bool:
    return (
        isinstance(rule, dict)
        and set(rule) <= {"allowed", "timeout_seconds"}
        and type(rule.get("allowed")) is bool
        and (
            "timeout_seconds" not in rule
            or (type(rule["timeout_seconds"]) is int and 1 <= rule["timeout_seconds"] <= 3600)
        )
    )


def _valid_stop_condition(item: object) -> bool:
    return (
        isinstance(item, dict)
        and set(item) == {"id", "kind"}
        and isinstance(item.get("id"), str)
        and bool(re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{2,63}", item["id"]))
        and item.get("kind") in {"deny", "pause"}
    )


def errors(value: object) -> list[str]:
    """Validate a closed version-one envelope without inferring authorization."""
    if not isinstance(value, dict):
        return ["envelope must be an object"]
    required = {
        "schema_version",
        "envelope_id",
        "envelope_revision",
        "task",
        "task_revision",
        "spec_ref",
        "spec_revision",
        "outputs",
        "non_goals",
        "path_scope",
        "command_classes",
        "evidence",
        "stop_conditions",
    }
    result = [f"envelope missing field: {name}" for name in sorted(required - set(value))]
    result.extend(f"envelope unknown field: {name}" for name in sorted(set(value) - required))
    result.extend(_identity_errors(value))
    result.extend(_collection_errors(value))
    result.extend(_rule_errors(value))
    return result


def valid_binding(meta: dict[str, Any]) -> bool:
    """Accept no envelope binding fields or one complete, correctly typed binding."""
    envelope = (
        meta.get("execution_envelope_ref"),
        meta.get("execution_envelope_revision"),
        meta.get("execution_envelope_task_revision"),
        meta.get("execution_envelope_digest"),
        meta.get("execution_envelope"),
    )
    return not any(value is not None for value in envelope) or (
        isinstance(envelope[0], str)
        and REF.fullmatch(envelope[0]) is not None
        and type(envelope[1]) is int
        and envelope[1] >= 1
        and type(envelope[2]) is int
        and envelope[2] >= 1
        and isinstance(envelope[3], str)
        and DIGEST.fullmatch(envelope[3]) is not None
        and isinstance(envelope[4], dict)
    )


def load(root: Path, reference: str) -> tuple[dict[str, Any] | None, str, list[str]]:
    """Load one root-bound immutable envelope and return its exact digest."""
    if not REF.fullmatch(reference) or reference.startswith(".") or ".." in Path(reference).parts:
        return None, "", ["envelope reference is unsafe"]
    base = root.resolve()
    candidate = base / reference
    try:
        current = base
        for part in Path(reference).parts:
            current /= part
            if stat.S_ISLNK(current.lstat().st_mode):
                return None, "", ["envelope reference contains a symlink"]
        descriptor = os.open(candidate, os.O_RDONLY | os.O_NOFOLLOW)
        with os.fdopen(descriptor, "rb") as stream:
            payload = stream.read()
        value = json.loads(payload)
    except (OSError, json.JSONDecodeError) as error:
        return None, "", [f"cannot read envelope: {error}"]
    found = errors(value)
    return value if isinstance(value, dict) else None, digest(payload), found


def _bound_envelope(meta: dict[str, Any]) -> tuple[dict[str, Any] | None, Preflight | None]:
    """Load and verify the immutable envelope bound in task metadata."""
    reference = meta.get("execution_envelope_ref")
    embedded = meta.get("execution_envelope")
    if not isinstance(reference, str) or not isinstance(embedded, dict):
        return None, Preflight(False, "ENVELOPE_MISSING", "task has no bound execution envelope")
    found = errors(embedded)
    if found:
        return None, Preflight(False, "ENVELOPE_INVALID", "; ".join(found))
    envelope = embedded
    actual_digest = canonical_digest(envelope)
    if meta.get("execution_envelope_digest") != actual_digest:
        return None, Preflight(False, "ENVELOPE_DIGEST_MISMATCH", "bound envelope data changed")
    if (
        envelope["task"] != meta.get("id")
        or envelope["envelope_revision"] != meta.get("execution_envelope_revision")
        or envelope["task_revision"] != meta.get("execution_envelope_task_revision")
        or envelope["spec_ref"] != meta.get("spec_ref")
        or envelope["spec_revision"] != meta.get("spec_revision")
    ):
        return None, Preflight(
            False,
            "ENVELOPE_REVISION_MISMATCH",
            "envelope does not match durable task specification",
        )
    return envelope, None


def _scope_error(
    envelope: dict[str, Any], command_class: str, paths: list[str], worktree: Path
) -> Preflight | None:
    """Return a denial if declared paths leave their class-specific scope."""
    if command_class in {"source-write", "git-publication"} and not paths:
        return Preflight(
            False, "SCOPE_DECLARATION_REQUIRED", "mutating command classes require --scope-path"
        )
    allowed = envelope["path_scope"][
        "write" if command_class in {"source-write", "git-publication"} else "read"
    ]
    root = worktree.resolve()
    for declared in paths:
        candidate = (root / declared).resolve()
        try:
            relative = candidate.relative_to(root).as_posix()
        except ValueError:
            return Preflight(
                False, "PATH_OUTSIDE_SCOPE", "declared path escapes the bound worktree"
            )
        if not any(
            relative == scope.rstrip("/") or relative.startswith(scope.rstrip("/") + "/")
            for scope in allowed
        ):
            return Preflight(
                False, "PATH_OUTSIDE_SCOPE", "declared path is outside the command-class scope"
            )
    return None


def preflight(
    meta: dict[str, Any],
    owner: str,
    command_class: str,
    paths: list[str],
    worktree: Path,
) -> Preflight:
    """Evaluate only durable task/envelope facts; this function has no side effects."""
    envelope, denial = _bound_envelope(meta)
    if denial is not None or envelope is None:
        return denial or Preflight(False, "ENVELOPE_INVALID", "envelope could not be loaded")
    if meta.get("owner") != owner or meta.get("status") != "in_progress":
        return Preflight(False, "OWNER_CLAIM_REQUIRED", "active durable owner claim is required")
    claim_expires = meta.get("claim_expires")
    if not isinstance(claim_expires, str) or not claim_expires:
        return Preflight(False, "OWNER_CLAIM_REQUIRED", "active durable owner lease is required")
    try:
        if dt.datetime.fromisoformat(claim_expires.replace("Z", "+00:00")) <= dt.datetime.now(
            dt.UTC
        ):
            return Preflight(False, "OWNER_CLAIM_REQUIRED", "active durable owner lease is expired")
    except ValueError:
        return Preflight(False, "OWNER_CLAIM_REQUIRED", "active durable owner lease is invalid")
    if (
        command_class not in COMMAND_CLASSES
        or command_class not in envelope["command_classes"]
        or not envelope["command_classes"][command_class]["allowed"]
    ):
        return Preflight(
            False, "COMMAND_CLASS_DENIED", "command class is not allowed by the envelope"
        )
    scope_denial = _scope_error(envelope, command_class, paths, worktree)
    if scope_denial is not None:
        return scope_denial
    return Preflight(
        True,
        "ALLOWED",
        "durable envelope admission passed",
        envelope["envelope_id"],
        str(meta["execution_envelope_digest"]),
    )


def sandboxed_envelope_command(args: Any) -> list[str]:
    """Confine a bound command to its declared writable worktree paths."""
    worktree = getattr(args, "_envelope_worktree", None)
    write_scope = getattr(args, "_envelope_write_scope", None)
    read_scope = getattr(args, "_envelope_read_scope", None)
    if (
        not isinstance(worktree, str)
        or not isinstance(write_scope, list)
        or not isinstance(read_scope, list)
    ):
        return list(args.command)
    if shutil.which("bwrap") is None:
        raise RuntimeError("execution envelope sandbox requires bubblewrap (bwrap)")
    root = Path(worktree).absolute()
    root_fd = getattr(args, "_envelope_worktree_fd", None)
    if type(root_fd) is int and root_fd >= 0:
        mounts = [(str(relative), Path(), "--ro-bind") for relative in read_scope] + [
            (str(relative), Path(), "--bind") for relative in write_scope
        ]
    else:
        mounts = envelope_sandbox_mounts(root, read_scope, write_scope)
    targets = {Path("/worktree")}
    for relative, _candidate, _flag in mounts:
        targets.update((Path("/worktree") / relative).parents)
    command = sandbox_base_command()
    for directory in sorted(
        (path for path in targets if path != Path("/")), key=lambda path: len(path.parts)
    ):
        command.extend(["--dir", str(directory)])
    specification = {
        "root": str(root),
        "root_fd": root_fd,
        "mounts": [
            {"relative": relative, "destination": f"/worktree/{relative}", "mode": flag}
            for relative, _candidate, flag in mounts
        ],
    }
    launcher = (
        "import sys; sys.path.insert(0, sys.argv[1]); "
        "from tools.execution_envelope import _run_sandbox_helper; _run_sandbox_helper()"
    )
    return [
        sys.executable,
        "-c",
        launcher,
        str(Path(__file__).resolve().parent.parent),
        json.dumps({"command": command, "specification": specification}),
        "--",
        *args.command,
    ]


def envelope_sandbox_mounts(
    root: Path, read_scope: list[object], write_scope: list[object]
) -> list[tuple[str, Path, str]]:
    """Return read-only and writable project mounts for one envelope execution."""
    read_mounts = [
        (str(relative), envelope_scope_path(root, str(relative)), "--ro-bind")
        for relative in read_scope
    ]
    write_mounts = [
        (str(relative), envelope_scope_path(root, str(relative)), "--bind")
        for relative in write_scope
    ]
    return [*read_mounts, *write_mounts]


def valid_reservation(value: object) -> bool:  # noqa: C901
    """Validate a durable execution fence without interpreting its command."""
    required = {
        "execution_id",
        "owner",
        "task_revision",
        "envelope_digest",
        "command_class",
        "scope_digest",
        "argv_digest",
        "expires_at",
    }
    if not isinstance(value, dict) or set(value) != required:
        return False
    if not re.fullmatch(r"[0-9a-f]{32}", str(value.get("execution_id", ""))):
        return False
    if not isinstance(value.get("owner"), str) or not value["owner"] or len(value["owner"]) > 128:
        return False
    if type(value.get("task_revision")) is not int or value["task_revision"] < 1:
        return False
    if not DIGEST.fullmatch(str(value.get("envelope_digest", ""))):
        return False
    if value.get("command_class") not in COMMAND_CLASSES:
        return False
    if not DIGEST.fullmatch(str(value.get("scope_digest", ""))):
        return False
    if not re.fullmatch(r"[0-9a-f]{64}", str(value.get("argv_digest", ""))):
        return False
    try:
        expires_at = dt.datetime.fromisoformat(
            str(value.get("expires_at", "")).replace("Z", "+00:00")
        )
    except ValueError:
        return False
    return expires_at.tzinfo is not None and expires_at.utcoffset() is not None


def sandbox_base_command() -> list[str]:
    """Build a private Bubblewrap root with no inherited host state."""
    return [
        "bwrap",
        "--die-with-parent",
        "--unshare-user",
        "--unshare-net",
        "--uid",
        "0",
        "--gid",
        "0",
        "--tmpfs",
        "/",
        "--clearenv",
        "--setenv",
        "PATH",
        "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
        "--setenv",
        "HOME",
        "/tmp",  # noqa: S108
        "--setenv",
        "TMPDIR",
        "/tmp",  # noqa: S108
        "--setenv",
        "LANG",
        "C.UTF-8",
        "--proc",
        "/proc",
        "--dev",
        "/dev",
        "--tmpfs",
        "/tmp",  # noqa: S108
    ]


def _open_path(path: Path, *, directory: bool = False) -> int:
    """Open an absolute path one component at a time without following links."""
    parts = path.parts
    if not parts or parts[0] != "/":
        raise RuntimeError("sandbox source must be absolute")
    flags = os.O_PATH | os.O_NOFOLLOW
    current = os.open("/", os.O_PATH | os.O_DIRECTORY | os.O_NOFOLLOW)
    try:
        for index, part in enumerate(parts[1:], 1):
            next_fd = os.open(part, flags, dir_fd=current)
            if index < len(parts) - 1 and not stat.S_ISDIR(os.fstat(next_fd).st_mode):
                os.close(next_fd)
                raise RuntimeError("sandbox source contains a non-directory component")
            os.close(current)
            current = next_fd
        if directory and not stat.S_ISDIR(os.fstat(current).st_mode):
            raise RuntimeError("sandbox source is not a directory")
        os.set_inheritable(current, True)
        return current
    except BaseException:
        os.close(current)
        raise


def _open_scope_path(root: Path, relative: str) -> int:
    """Open a declared source beneath a stable, link-free directory descriptor."""
    parts = Path(relative).parts
    if not parts or any(part in {"", ".", ".."} for part in parts):
        raise RuntimeError("sandbox source path is unsafe")
    root_fd = _open_path(root, directory=True)
    current = root_fd
    try:
        for index, part in enumerate(parts):
            next_fd = os.open(part, os.O_PATH | os.O_NOFOLLOW, dir_fd=current)
            if index < len(parts) - 1 and not stat.S_ISDIR(os.fstat(next_fd).st_mode):
                os.close(next_fd)
                raise RuntimeError("sandbox source contains a non-directory component")
            os.close(current)
            current = next_fd
        os.set_inheritable(current, True)
        return current
    except BaseException:
        os.close(current)
        raise


def _open_scope_fd(root_fd: int, relative: str) -> int:
    """Open a declared source beneath an inherited no-follow root descriptor."""
    parts = Path(relative).parts
    if not parts or any(part in {"", ".", ".."} for part in parts):
        raise RuntimeError("sandbox source path is unsafe")
    current = os.dup(root_fd)
    try:
        for index, part in enumerate(parts):
            next_fd = os.open(part, os.O_PATH | os.O_NOFOLLOW, dir_fd=current)
            if index < len(parts) - 1 and not stat.S_ISDIR(os.fstat(next_fd).st_mode):
                os.close(next_fd)
                raise RuntimeError("sandbox source contains a non-directory component")
            os.close(current)
            current = next_fd
        os.set_inheritable(current, True)
        return current
    except BaseException:
        os.close(current)
        raise


def _run_sandbox_helper() -> None:
    """Open sources by descriptor, then exec Bubblewrap with descriptor mounts."""
    if len(sys.argv) < 4 or sys.argv[3] != "--":
        raise RuntimeError("sandbox helper arguments are invalid")
    sys.path.insert(0, sys.argv[1])
    payload = json.loads(sys.argv[2])
    command = [str(item) for item in payload["command"]]
    specification = payload["specification"]
    root = Path(specification["root"])
    root_fd = specification.get("root_fd")
    opened: list[int] = []
    try:
        for runtime_source, runtime_destination in (
            ("/usr", "/usr"),
            ("/usr/lib", "/lib"),
            ("/usr/lib64", "/lib64"),
        ):
            try:
                fd = _open_path(Path(runtime_source), directory=True)
            except FileNotFoundError:
                continue
            opened.append(fd)
            command.extend(["--ro-bind-fd", str(fd), runtime_destination])
        for mount in specification["mounts"]:
            fd = (
                _open_scope_fd(root_fd, str(mount["relative"]))
                if type(root_fd) is int and root_fd >= 0
                else _open_scope_path(root, str(mount["relative"]))
            )
            opened.append(fd)
            command.extend(
                [
                    "--ro-bind-fd" if mount["mode"] == "--ro-bind" else "--bind-fd",
                    str(fd),
                    str(mount["destination"]),
                ]
            )
        command.extend(["--chdir", "/worktree", "--", *sys.argv[4:]])
        bwrap = shutil.which("bwrap")
        if bwrap is None:
            raise RuntimeError("execution envelope sandbox requires bubblewrap (bwrap)")
        os.execvpe(bwrap, command, os.environ)  # noqa: S606
    finally:
        for fd in opened:
            with suppress(OSError):
                os.close(fd)


def envelope_scope_path(root: Path, relative: str) -> Path:
    """Resolve one mount source without accepting aliases outside its declared path."""
    parts = Path(relative).parts
    if not parts or any(part in {"", ".", ".."} for part in parts):
        raise RuntimeError("execution envelope path scope is unsafe")
    candidate = root
    for part in parts:
        candidate /= part
        try:
            mode = candidate.lstat().st_mode
        except OSError as error:
            raise RuntimeError("execution envelope path scope is unavailable") from error
        if stat.S_ISLNK(mode):
            raise RuntimeError("execution envelope path scope contains a symlink")
    return candidate
