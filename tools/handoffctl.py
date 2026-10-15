#!/usr/bin/env python3
# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""State."""

import sys

if __name__ == "__main__" and len(sys.argv) > 2 and sys.argv[1] == "fast":
    from fast_receipt_socket import try_socket_fast  # type: ignore[import-not-found]

    _FAST_EXIT = try_socket_fast(sys.argv[1:])
    if _FAST_EXIT is not None:
        raise SystemExit(_FAST_EXIT)

import argparse
import contextlib
import datetime as dt
import fcntl
import hashlib
import json
import os
import re
import stat
import subprocess
import tempfile
import textwrap
import threading
import time
import uuid
from collections import Counter
from collections.abc import Callable, Iterator
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import TYPE_CHECKING, Any, cast

if not __package__:
    _SCRIPT_ROOT = str(Path(__file__).resolve().parent.parent)
    if _SCRIPT_ROOT not in sys.path:
        sys.path.insert(0, _SCRIPT_ROOT)

if __package__:
    from . import (
        assumption_revalidation,
        change_drift,
        command_results,
        execution_abandonment,
        execution_envelope,
        execution_lifecycle,
        execution_receipt,
        resume_card,
        resume_card_runtime,
        retry_circuit,
        run_command,
    )
    from . import autonomy_limits as al
    from . import predicate_ledger_repair as plr
    from . import roles as role_module
    from .board_metrics import build_metrics
    from .board_metrics import encode as encode_metrics
    from .checkpoint_records import (
        append_checkpoint,
        build_checkpoint,
        checkpoint_path,
        load_checkpoints,
        validate_checkpoint,
    )
    from .directive_records import (
        append_directive,
        build_directive,
        conflicting_directives,
        directive_path,
        latest_directives,
        validate_directive,
    )
    from .hierarchy import hierarchy_errors, open_child_error
    from .oracle_lifecycle import (
        ArtifactRef,
        GateError,
        GateStage,
        InteractionEvent,
        StageGate,
        apply_event,
        gate_errors,
        transition_allowed,
    )
    from .predicate_ledger import apply_acceptance
    from .rollback_records import (
        append_record,
        build_record,
        latest_for_checkpoint,
        load_records,
        rollback_path,
        validate_record,
    )
    from .session_records import (
        append_session_record,
        build_session_record,
        decode_session_lines,
        latest_session,
        session_path,
        validate_session_record,
    )
    from .sqlite_storage import (
        Backend,
        SQLiteBackend,
        bind_released_sqlite_backend,
        create_database,
    )
    from .status_renderer import (
        StatusRenderError,
        graph_errors,
        render_status,
        render_status_pages_from_text,
    )
    from .task_spec import (
        DEFAULT_EVIDENCE_POLICY,
        EvidencePolicy,
        done_admission_error,
        evidence_policy,
        next_unmet_predicate,
        require_policy_unchanged,
        task_spec_errors,
        task_spec_policy_errors,
    )
else:
    import assumption_revalidation  # type: ignore[import-not-found,no-redef]
    import autonomy_limits as al  # type: ignore[import-not-found,no-redef]
    import change_drift  # type: ignore[import-not-found,no-redef]
    import command_results  # type: ignore[import-not-found,no-redef]

    try:
        from board_metrics import build_metrics  # type: ignore[import-not-found,no-redef]  # noqa: I001
        from board_metrics import encode as encode_metrics  # type: ignore[no-redef]
    except ModuleNotFoundError:

        def build_metrics(tasks: list[tuple[Any, dict[str, Any], str]]) -> dict[str, Any]:
            del tasks
            raise RuntimeError("board metrics module is unavailable in this vendored bootstrap")

        def encode_metrics(metrics: dict[str, Any]) -> str:
            del metrics
            raise RuntimeError("board metrics module is unavailable in this vendored bootstrap")

    import execution_abandonment  # type: ignore[import-not-found,no-redef]
    import execution_envelope  # type: ignore[import-not-found,no-redef]
    import execution_lifecycle  # type: ignore[import-not-found,no-redef]
    import execution_receipt  # type: ignore[import-not-found,no-redef]
    import predicate_ledger_repair as plr  # type: ignore[import-not-found,no-redef]
    import resume_card  # type: ignore[import-not-found,no-redef]
    import resume_card_runtime  # type: ignore[import-not-found,no-redef]
    import retry_circuit  # type: ignore[import-not-found,no-redef]
    import roles as role_module  # type: ignore[import-not-found,no-redef]
    import run_command  # type: ignore[import-not-found,no-redef]
    from checkpoint_records import (  # type: ignore[import-not-found,no-redef]
        append_checkpoint,
        build_checkpoint,
        checkpoint_path,
        load_checkpoints,
        validate_checkpoint,
    )
    from directive_records import (  # type: ignore[import-not-found,no-redef]
        append_directive,
        build_directive,
        conflicting_directives,
        directive_path,
        latest_directives,
        validate_directive,
    )
    from hierarchy import (  # type: ignore[import-not-found,no-redef]
        hierarchy_errors,
        open_child_error,
    )
    from oracle_lifecycle import (  # type: ignore[import-not-found,no-redef]
        ArtifactRef,
        GateError,
        GateStage,
        InteractionEvent,
        StageGate,
        apply_event,
        gate_errors,
        transition_allowed,
    )
    from predicate_ledger import apply_acceptance  # type: ignore[import-not-found,no-redef]
    from rollback_records import (  # type: ignore[import-not-found,no-redef]
        append_record,
        build_record,
        latest_for_checkpoint,
        load_records,
        rollback_path,
        validate_record,
    )
    from session_records import (  # type: ignore[import-not-found,no-redef]
        append_session_record,
        build_session_record,
        decode_session_lines,
        latest_session,
        session_path,
        validate_session_record,
    )
    from sqlite_storage import (  # type: ignore[import-not-found,no-redef]
        Backend,
        SQLiteBackend,
        bind_released_sqlite_backend,
        create_database,
    )
    from status_renderer import (  # type: ignore[import-not-found,no-redef]
        StatusRenderError,
        graph_errors,
        render_status,
        render_status_pages_from_text,
    )
    from task_spec import (  # type: ignore[import-not-found,no-redef]
        DEFAULT_EVIDENCE_POLICY,
        EvidencePolicy,
        done_admission_error,
        evidence_policy,
        next_unmet_predicate,
        require_policy_unchanged,
        task_spec_errors,
        task_spec_policy_errors,
    )

if TYPE_CHECKING:
    __all__ = (
        "DEFAULT_EVIDENCE_POLICY",
        "graph_errors",
        "hierarchy_errors",
    )

ROOT = Path(__file__).resolve().parent.parent
TASKS = ROOT / "tasks"
RUNTIME = ROOT / ".runtime"
LOCK = RUNTIME / "state.lock"
CONFIG = RUNTIME / "config.json"
REPLICA_BLOCKED = RUNTIME / "replica-blocked.json"
PROJECT_CONFIG = ROOT / ".handoffctl.json"
BINDING = ROOT / "coordinator.binding.json"
BACKEND_CONFIG = ROOT / "coordinator.backend.json"
DATABASE = RUNTIME / "coordinator.sqlite3"
CONTROL_DATABASE = RUNTIME / "coordinator.control.sqlite3"
AUTHORITY_MARKER = RUNTIME / "coordinator.authority-marker.json"
AUTHORITY_LIFECYCLE = RUNTIME / "coordinator.authority-lifecycle.json"
AUTHORITY_LOCK = RUNTIME / "coordinator.authority.lock"
CONTROL_BINDING = RUNTIME / "coordinator.control-binding.json"
CONTROL_LOCK = RUNTIME / ".coordinator.control.sqlite3.lock"
BACKENDS = ("sqlite", "git")
LOCK_TIMEOUT_SECONDS = 10.0
LOCK_POLL_SECONDS = 0.05
_GUARD_CREATION_TOKEN = object()
SUBPROCESS_TIMEOUT_SECONDS = 30.0
COMMAND_TIMEOUT_SECONDS = 1800.0
OBSERVATION_ATTEMPTS = 3
OBSERVATION_RETRY_SECONDS = 0.25
SESSION_REFERENCE = re.compile(r"^(AR-[0-9]{4})@([1-9][0-9]*)$")
STATUSES = (
    "in_progress",
    "open",
    "blocked",
    "planned",
    "future",
    "done",
    "cancelled",
    "superseded",
)
LIFECYCLE_MUTATION_COMMANDS = (
    "claim",
    "heartbeat",
    "accept",
    "bind-spec",
    "bind-worktree",
    "bind-envelope",
    "replace-envelope",
    "release",
    "promote",
    "pause",
    "resume",
    "unblock",
    "recover-expired",
    "recover-execution",
    "abandon-execution",
    "update",
    "change-drift",
    "assumption",
)


class IdempotentMutationError(RuntimeError):
    """Signal an admitted no-op replay."""


CURRENT_STATUSES = ("in_progress", "open", "blocked", "planned", "future")
PRIORITIES = ("P0", "P1", "P2", "P3", "P4")
REQ = (
    "schema_version",
    "id",
    "title",
    "status",
    "priority",
    "summary",
    "next_action",
    "task_revision",
    "updated_at",
)
FIELDS = set(REQ) | {
    "short_title",
    "owner",
    "role",
    "team",
    "claim_expires",
    "claim_process",
    "worktree_key",
    "branch",
    "checkpoint_commit",
    "plan",
    "depends_on",
    "observed_branch",
    "observed_head",
    "observed_dirty",
    "superseded_by",
    "oracle_gate",
    "spec_ref",
    "spec_revision",
    "spec_acceptance",
    "evidence_ledger",
    "execution_envelope_ref",
    "execution_envelope_revision",
    "execution_envelope_task_revision",
    "execution_envelope_digest",
    "execution_envelope",
    "execution_reservation",
    "execution_result",
    "execution_abandonments",
    "parent_task_ref",
    "children",
    "issue_series",
    "change_drift",
    "assumption_revalidation",
    "retry_circuit",
    "autonomy_limits",
}
type Meta = dict[str, Any]
type Task = tuple[Path, Meta, str]
type State = dict[str, Any]


def task_label(meta: Meta) -> str:
    return f"{meta['id']} — {meta.get('short_title') or meta['title']}"


def short_title_errors(path: Path, task_id: str, value: object) -> list[str]:
    if value is None:
        return []
    if (
        not isinstance(value, str)
        or not value.strip()
        or any(ord(char) < 32 or ord(char) == 127 for char in value)
    ):
        return [f"{task_id}: invalid short_title"]
    if len(value) > 120:
        return [f"{task_id}: short_title exceeds 120 characters"]
    if len(value.split()) > 4:
        return [f"{task_id}: short_title exceeds four words"]
    if private_text_errors(path, value):
        return [f"{task_id}: privacy-unsafe short_title"]
    return []


COORDINATOR_VERSION = "0.7.14"
DEFAULT_PROJECT_SETTINGS: Meta = {
    "schema_version": 1,
    "project_id": "00000000-0000-4000-8000-000000000000",
    "project_name": "agent-workflow",
    "project_title": "Agent Workflow",
    "status_view": False,
    "commit_signoff": False,
}
PROJECT_SETTING_KEYS = frozenset(DEFAULT_PROJECT_SETTINGS)


def project_settings() -> Meta:
    if not PROJECT_CONFIG.exists():
        return dict(DEFAULT_PROJECT_SETTINGS)
    value = json.loads(PROJECT_CONFIG.read_text())
    if not isinstance(value, dict) or set(value) != PROJECT_SETTING_KEYS:
        raise RuntimeError(".handoffctl.json must contain exactly the documented project keys")
    if value.get("schema_version") != 1:
        raise RuntimeError("unsupported .handoffctl.json schema_version")
    try:
        project_id = uuid.UUID(str(value.get("project_id")))
    except ValueError as error:
        raise RuntimeError("invalid project_id in .handoffctl.json") from error
    if project_id.version != 4:
        raise RuntimeError("project_id must be a UUIDv4")
    if not isinstance(value.get("project_name"), str) or not re.fullmatch(
        r"[a-z0-9]+(?:-[a-z0-9]+)*", value["project_name"]
    ):
        raise RuntimeError("invalid project_name in .handoffctl.json")
    if not isinstance(value.get("project_title"), str) or not value["project_title"].strip():
        raise RuntimeError("invalid project_title in .handoffctl.json")
    if not isinstance(value.get("status_view"), bool) or not isinstance(
        value.get("commit_signoff"), bool
    ):
        raise RuntimeError("status_view and commit_signoff must be booleans")
    return value


def repository_slug(value: object) -> str:
    text = str(value or "").strip().removesuffix(".git")
    if "://" in text:
        text = text.split("://", 1)[1].split("/", 1)[-1]
    elif text.startswith("git@") and ":" in text:
        text = text.split(":", 1)[1]
    text = text.strip("/")
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", text):
        raise RuntimeError(f"invalid GitHub repository identity: {value}")
    return text.lower()


def backend_selection() -> Meta:
    if not BACKEND_CONFIG.exists():
        return {"schema_version": 1, "backend": "git", "legacy": True}
    try:
        value = json.loads(BACKEND_CONFIG.read_text())
    except (OSError, json.JSONDecodeError) as error:
        raise RuntimeError("invalid coordinator.backend.json") from error
    required = {"schema_version", "project_id", "backend"}
    if not isinstance(value, dict) or set(value) != required or value.get("schema_version") != 1:
        raise RuntimeError("invalid coordinator.backend.json")
    if value.get("backend") not in BACKENDS:
        raise RuntimeError("unsupported coordinator backend")
    return cast(Meta, value)


class GitBackend:
    name = "git"

    def load_tasks(self) -> list[Task]:
        return git_tasks()

    def load_session_records(self, _task_id: str | None = None) -> list[Meta]:
        task_id = _task_id
        paths = (
            [session_path(ROOT, task_id)]
            if task_id is not None
            else sorted((ROOT / "sessions").glob("AR-*.jsonl"))
        )
        records: list[Meta] = []
        for path in paths:
            try:
                records.extend(decode_session_lines(path, path.stem))
            except ValueError as error:
                raise RuntimeError("session history is invalid") from error
        return records

    def load_checkpoint_records(self, task_id: str | None = None) -> list[Meta]:
        return load_checkpoints(ROOT, task_id)

    def has_command_result(self, task_id: str, owner: str, argv_sha256: str) -> bool:
        return any(
            record["task"] == task_id
            and record["owner"] == owner
            and record["argv_sha256"] == argv_sha256
            for record in legacy_command_results()
        )

    def append_command_result(
        self,
        task_id: str,
        owner: str,
        command_hash: str,
        returncode: int,
        classification: str,
        recorded_at: str,
    ) -> None:
        append_file_command_result(
            task_id, owner, command_hash, returncode, classification, recorded_at
        )


def storage_backend() -> Backend:
    selection = backend_selection()
    if selection["backend"] == "git":
        return GitBackend()
    return SQLiteBackend(DATABASE, project_binding(), TASKS)


def mutating_sqlite_backend() -> SQLiteBackend:
    if not all(
        path.exists()
        for path in (
            CONTROL_DATABASE,
            AUTHORITY_MARKER,
            AUTHORITY_LIFECYCLE,
            AUTHORITY_LOCK,
            CONTROL_BINDING,
        )
    ):
        return SQLiteBackend(DATABASE, project_binding(), TASKS)
    from tools.mutation_fence import MutationFence
    from tools.rollback_control_store import SQLiteBarrierSessionStore, SQLiteRollbackControlStore

    binding = project_binding()
    project_id = str(binding["project_id"])
    control = SQLiteRollbackControlStore(CONTROL_DATABASE, project_id, DATABASE)
    session = SQLiteBarrierSessionStore(control)
    admitted = session.snapshot()
    if admitted is None:
        raise RuntimeError("durable barrier session is missing")
    fence = MutationFence(
        DATABASE,
        AUTHORITY_MARKER,
        AUTHORITY_LIFECYCLE,
        AUTHORITY_LOCK,
        CONTROL_DATABASE,
        CONTROL_BINDING,
        CONTROL_LOCK,
    )
    return bind_released_sqlite_backend(
        DATABASE,
        binding,
        TASKS,
        fence,
        locked,
        admitted.identity,
    )


def provision_sqlite_barrier() -> None:
    """Provision the authority fence and baseline session."""
    from tools.mutation_fence import provision, provision_control_binding
    from tools.rollback_control_store import SQLiteBarrierSessionStore, SQLiteRollbackControlStore
    from tools.upgrade_identity import BarrierSessionIdentity, canonical_barrier_session_digest

    binding = project_binding()
    project_id = str(binding["project_id"])
    RUNTIME.mkdir(mode=0o700, parents=True, exist_ok=True)
    runtime_status = RUNTIME.stat()
    if runtime_status.st_uid != os.geteuid() or not RUNTIME.is_dir():
        raise RuntimeError("SQLite barrier runtime directory is not owner-controlled")
    if (runtime_status.st_mode & 0o777) != 0o700:
        RUNTIME.chmod(0o700)
    if (RUNTIME.stat().st_mode & 0o777) != 0o700:
        raise RuntimeError("SQLite barrier runtime directory must be owner-only")
    provision(DATABASE, AUTHORITY_MARKER, AUTHORITY_LIFECYCLE, AUTHORITY_LOCK, project_id)
    control = SQLiteRollbackControlStore(CONTROL_DATABASE, project_id, DATABASE)
    provision_control_binding(CONTROL_DATABASE, CONTROL_BINDING, CONTROL_LOCK, project_id)
    authority = DATABASE.stat()
    authority_revision = (
        "authority-"
        + hashlib.sha256(
            f"{authority.st_dev}:{authority.st_ino}:{authority.st_size}:{authority.st_mtime_ns}".encode()
        ).hexdigest()
    )
    attempt = "baseline-" + uuid.uuid4().hex
    identity_values: dict[str, object] = {
        "schema_version": 1,
        "project_id": project_id,
        "attempt_id": attempt,
        "state_revision": 1,
        "authority_revision_at_acquire": authority_revision,
        "durable_barrier_id": "baseline-barrier-" + uuid.uuid4().hex,
        "fencing_token": "baseline-fence-" + uuid.uuid4().hex,
        "fencing_owner": "coordinator-bootstrap",
    }
    identity_values["identity_digest"] = canonical_barrier_session_digest(identity_values)
    SQLiteBarrierSessionStore(control, lambda: authority_revision).provision_released(
        BarrierSessionIdentity.from_record(identity_values)
    )


def project_binding() -> Meta:
    """Load the immutable project binding created by `handoffctl init`."""
    try:
        value = json.loads(BINDING.read_text())
    except (OSError, json.JSONDecodeError) as error:
        raise RuntimeError("coordinator is not initialized for this project") from error
    required = {"schema_version", "project_id", "state_repository", "product_repository"}
    if not isinstance(value, dict) or set(value) != required or value.get("schema_version") != 1:
        raise RuntimeError("invalid coordinator.binding.json")
    try:
        project_id = uuid.UUID(str(value.get("project_id")))
    except ValueError as error:
        raise RuntimeError("invalid project_id in coordinator binding") from error
    if project_id.version != 4:
        raise RuntimeError("binding project_id must be a UUIDv4")
    repository_slug(value["state_repository"])
    repository_slug(value["product_repository"])
    return value


def git_repository_slug(root: Path) -> str:
    """Normalize a checkout origin."""
    result = run(["git", "-C", str(root), "remote", "get-url", "origin"])
    return repository_slug(result.stdout.strip())


def inside(candidate: Path, root: Path) -> bool:
    """Inside."""
    candidate = candidate.resolve()
    root = root.resolve()
    return candidate == root or root in candidate.parents


def _assert_storage_binding(binding: Meta) -> None:
    """Check stored identity."""
    selection = backend_selection()
    if not selection.get("legacy") and selection.get("project_id") != binding["project_id"]:
        raise RuntimeError("storage backend does not match coordinator binding")
    if selection["backend"] == "sqlite":
        SQLiteBackend(DATABASE, binding, TASKS).load_tasks()


def configured_product_checkout(binding: Meta) -> tuple[Path, Path]:
    """Validate runtime product identity and return its root and projects directory."""
    runtime = config()
    configured_github = runtime.get("github_repository")
    if configured_github and repository_slug(configured_github) != repository_slug(
        binding["product_repository"]
    ):
        raise RuntimeError("runtime product repository does not match coordinator binding")
    projects_root = Path(str(runtime["projects_root"])).resolve()
    product = projects_root / str(runtime["product_worktree"])
    if git_repository_slug(product) != repository_slug(binding["product_repository"]):
        raise RuntimeError("product checkout does not match coordinator binding")
    return projects_root, product.resolve()


def assert_project_binding(caller_cwd: Path | None = None) -> None:
    """Fail closed when this initialized coordinator is called from another project."""
    settings = project_settings()
    binding = project_binding()
    if settings["project_id"] != binding["project_id"]:
        raise RuntimeError("project profile does not match coordinator binding")
    _assert_storage_binding(binding)
    top = Path(run(["git", "-C", str(ROOT), "rev-parse", "--show-toplevel"]).stdout.strip())
    if top.resolve() != ROOT.resolve():
        raise RuntimeError("handoffctl is not installed at its bound state repository root")
    if git_repository_slug(ROOT) != repository_slug(binding["state_repository"]):
        raise RuntimeError("state repository does not match coordinator binding")
    allowed = [ROOT.resolve()]
    projects_root: Path | None = None
    if CONFIG.exists():
        projects_root, product = configured_product_checkout(binding)
        allowed.append(product)
    current = (Path.cwd() if caller_cwd is None else caller_cwd).resolve()
    if projects_root is not None and inside(current, projects_root):
        candidate = run(
            ["git", "-C", str(current), "rev-parse", "--show-toplevel"], check=False
        ).stdout.strip()
        if candidate:
            candidate_root = Path(candidate).resolve()
            if (
                candidate_root != ROOT.resolve()
                and inside(candidate_root, projects_root)
                and git_repository_slug(candidate_root)
                == repository_slug(binding["product_repository"])
            ):
                allowed.append(candidate_root)
    if not any(inside(current, root) for root in allowed):
        raise RuntimeError("handoffctl must be called from its bound state or product project")


class RetryableCoordinatorError(RuntimeError):
    pass


class LockTimeoutError(RetryableCoordinatorError):
    pass


class LockOwnershipError(RuntimeError):
    pass


class CoordinatorLockGuard:
    __slots__ = (
        "_active",
        "_exclusive",
        "_fd",
        "_identity",
        "_owner_pid",
        "_owner_thread",
        "_path",
        "_path_identity",
    )

    def __init__(self, path: Path, fd: int, *, exclusive: bool, _creation_token: object) -> None:
        if _creation_token is not _GUARD_CREATION_TOKEN:
            raise TypeError("CoordinatorLockGuard construction is private")
        status = path.stat()
        self._fd = fd
        self._identity = (status.st_dev, status.st_ino)
        self._path_identity = (status.st_dev, status.st_ino)
        self._exclusive = exclusive
        self._owner_pid = os.getpid()
        self._owner_thread = threading.get_ident()
        self._path = path.resolve()
        self._active = True

    @classmethod
    def _create(cls, path: Path, fd: int, *, exclusive: bool) -> "CoordinatorLockGuard":
        return cls(path, fd, exclusive=exclusive, _creation_token=_GUARD_CREATION_TOKEN)

    @property
    def path(self) -> Path:
        return self._path

    def assert_owned(self) -> None:
        if not self._active:
            raise LockOwnershipError("coordinator lock guard is inactive")
        if not self._exclusive:
            raise LockOwnershipError("coordinator lock guard is not exclusive")
        if self._owner_pid != os.getpid() or self._owner_thread != threading.get_ident():
            raise LockOwnershipError("coordinator lock guard has a different owner")
        try:
            status = os.fstat(self._fd)
        except OSError as error:
            raise LockOwnershipError("coordinator lock guard descriptor is unavailable") from error
        if (status.st_dev, status.st_ino) != self._identity:
            raise LockOwnershipError("coordinator lock guard descriptor identity changed")
        current_path = coordinator_lock_path().resolve()
        if self._path != current_path:
            raise LockOwnershipError("coordinator lock guard path changed")
        try:
            path_status = current_path.stat()
        except OSError as error:
            raise LockOwnershipError("coordinator lock guard path is unavailable") from error
        if (path_status.st_dev, path_status.st_ino) != self._path_identity:
            raise LockOwnershipError("coordinator lock guard path identity changed")

    def _invalidate(self) -> None:
        self._active = False


class SubprocessTimeoutError(RuntimeError):
    pass


class RepairRequiredCoordinatorError(RuntimeError):
    pass


class ReplicaDivergedError(RepairRequiredCoordinatorError):
    pass


class ExternalObservationError(RuntimeError):
    pass


class PostCommandReconcileError(RuntimeError):
    pass


class StorageCommittedError(RuntimeError):
    pass


PRIVATE = (
    (re.compile("/" + "home/"), "absolute Linux home path"),
    (re.compile(r"[A-Za-z]:\\Users\\", re.I), "absolute Windows user path"),
    (re.compile(r"\bai" + r"-ws\b", re.I), "private host alias"),
    (re.compile(r"\b(?:10|127)\.(?:\d{1,3}\.){2}\d{1,3}\b"), "private or loopback IP"),
    (
        re.compile(
            r"\b(?:password|passwd|token|secret|api[_-]?key)\s*[:=]\s*[^\s<]+",
            re.I,
        ),
        "possible credential",
    ),
    (re.compile(r"-----BEGIN (?:OPENSSH|RSA|EC|DSA) PRIVATE KEY-----"), "private key"),
    (
        re.compile(
            r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b",
            re.I,
        ),
        "session-like UUID",
    ),
)
PRIVATE_HEX_DIGITS = frozenset("0123456789abcdefABCDEF")

UUID_PRIVACY_EXEMPT = frozenset(
    {
        Path(".handoffctl.json"),
        Path("coordinator.binding.json"),
        Path("coordinator.backend.json"),
        Path("tools/handoffctl.py"),
    }
)


def now() -> str:
    return dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat()


def run(
    args: list[str],
    *,
    cwd: Path | None = None,
    check: bool = True,
    capture: bool = True,
    timeout: float = SUBPROCESS_TIMEOUT_SECONDS,
) -> subprocess.CompletedProcess[str]:
    try:
        proc = subprocess.run(
            args,
            cwd=cwd,
            text=True,
            capture_output=capture,
            check=False,
            timeout=timeout,
        )
    except subprocess.TimeoutExpired as error:
        command = " ".join(args)
        raise SubprocessTimeoutError(
            f"SUBPROCESS_TIMEOUT after {timeout:.1f}s: {command}"
        ) from error
    if check and proc.returncode:
        raise RuntimeError(f"command failed ({proc.returncode}): {' '.join(args)}\n{proc.stderr}")
    return proc


def config() -> Meta:
    if not CONFIG.exists():
        raise RuntimeError(f"missing private runtime config: {CONFIG}")
    return cast(Meta, json.loads(CONFIG.read_text()))


def run_github_observation(args: list[str]) -> subprocess.CompletedProcess[str]:
    """Retry a bounded read-only GitHub query and classify exhausted failures."""
    failure: RuntimeError | None = None
    for attempt in range(OBSERVATION_ATTEMPTS):
        try:
            return run(args)
        except (RuntimeError, SubprocessTimeoutError) as error:
            failure = error
            if attempt + 1 < OBSERVATION_ATTEMPTS:
                time.sleep(OBSERVATION_RETRY_SECONDS * (attempt + 1))
    command = " ".join(args)
    raise ExternalObservationError(
        f"EXTERNAL_API_ERROR after {OBSERVATION_ATTEMPTS} attempts: {command}"
    ) from failure


def coordinator_lock_path() -> Path:
    """Resolve the lock shared by local Git worktrees."""
    configured = RUNTIME / "state.lock"
    if configured != LOCK or not (ROOT / ".git").exists():
        return LOCK
    result = run(
        ["git", "-C", str(ROOT), "rev-parse", "--git-common-dir"],
        check=False,
    )
    if result.returncode or not result.stdout.strip():
        raise RuntimeError("cannot resolve repository-common coordinator lock")
    common = Path(result.stdout.strip())
    if not common.is_absolute():
        common = ROOT / common
    return common.resolve() / "handoffctl" / "state.lock"


def task_execution_lock_path(task_id: str) -> Path:
    if not execution_envelope.TASK.fullmatch(task_id):
        raise RuntimeError("invalid task execution fence identifier")
    return coordinator_lock_path().parent / "task-executions" / f"{task_id}.lock"


@contextlib.contextmanager
def task_execution_locked(
    task_id: str,
    *,
    exclusive: bool,
    timeout: float = LOCK_TIMEOUT_SECONDS,
    phase: str = "task_execution",
) -> Iterator[None]:
    lock_path = task_execution_lock_path(task_id)
    lock_path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    fd = os.open(lock_path, os.O_CREAT | os.O_RDWR, 0o600)
    try:
        operation = fcntl.LOCK_EX if exclusive else fcntl.LOCK_SH
        deadline = time.monotonic() + timeout
        while True:
            try:
                fcntl.flock(fd, operation | fcntl.LOCK_NB)
                break
            except BlockingIOError as error:
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    mode = "exclusive" if exclusive else "shared"
                    raise LockTimeoutError(
                        f"LOCK_TIMEOUT after {timeout:.1f}s acquiring {mode} {phase} fence"
                    ) from error
                time.sleep(min(LOCK_POLL_SECONDS, remaining))
        yield
    finally:
        fcntl.flock(fd, fcntl.LOCK_UN)
        os.close(fd)


@contextlib.contextmanager
def locked(
    *, exclusive: bool = True, timeout: float = LOCK_TIMEOUT_SECONDS, phase: str = "other"
) -> Iterator[CoordinatorLockGuard]:
    lock_path = coordinator_lock_path()
    lock_path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    fd = os.open(lock_path, os.O_CREAT | os.O_RDWR, 0o600)
    try:
        operation = fcntl.LOCK_EX if exclusive else fcntl.LOCK_SH
        tracing = bool(os.environ.get("HANDOFFCTL_LOCK_TRACE"))
        started = time.monotonic()
        deadline = started + timeout
        while True:
            try:
                fcntl.flock(fd, operation | fcntl.LOCK_NB)
                break
            except BlockingIOError as error:
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    mode = "exclusive" if exclusive else "shared"
                    if tracing:
                        trace_lock_metric(phase, mode, time.monotonic() - started, None)
                    raise LockTimeoutError(
                        f"LOCK_TIMEOUT after {timeout:.1f}s acquiring {mode} coordinator lock"
                    ) from error
                time.sleep(min(LOCK_POLL_SECONDS, remaining))
        acquired = time.monotonic() if tracing else started
        guard = CoordinatorLockGuard._create(lock_path, fd, exclusive=exclusive)
        yield guard
    finally:
        metric: tuple[str, str, float, float] | None = None
        if "guard" in locals():
            if tracing:
                metric = (
                    phase,
                    "exclusive" if exclusive else "shared",
                    acquired - started,
                    time.monotonic() - acquired,
                )
            guard._invalidate()
        fcntl.flock(fd, fcntl.LOCK_UN)
        os.close(fd)
        if metric is not None:
            trace_lock_metric(*metric)


def trace_lock_metric(phase: str, mode: str, wait: float, hold: float | None) -> None:
    """Emit bounded private lock timing."""
    destination = os.environ.get("HANDOFFCTL_LOCK_TRACE")
    if not destination:
        return
    record = {
        "phase": phase,
        "mode": mode,
        "wait_ms": round(wait * 1000, 3),
        "hold_ms": None if hold is None else round(hold * 1000, 3),
        "timeout": hold is None,
        "ended_ns": time.monotonic_ns(),
    }
    try:
        descriptor = os.open(destination, os.O_APPEND | os.O_CREAT | os.O_WRONLY, 0o600)
        with os.fdopen(descriptor, "ab") as stream:
            stream.write((json.dumps(record, sort_keys=True) + "\n").encode())
    except (OSError, ValueError):
        pass


def observation_marker(name: str) -> Path:
    """Order per-checkout task and projection scans."""
    return RUNTIME / name


def reserve_observation_ticket() -> int:
    """Order slow scans outside the authority lock."""
    path = observation_marker("observation-sequence")
    path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    descriptor = os.open(path.with_suffix(".lock"), os.O_CREAT | os.O_RDWR, 0o600)
    try:
        fcntl.flock(descriptor, fcntl.LOCK_EX)
        previous = int(path.read_text()) if path.exists() else 0
        if previous < 0:
            raise RuntimeError("invalid observation sequence")
        ticket = previous + 1
        atomic(path, f"{ticket}\n")
        return ticket
    finally:
        fcntl.flock(descriptor, fcntl.LOCK_UN)
        os.close(descriptor)


def published_observation_ticket() -> int:
    path = observation_marker("observation-published")
    value = int(path.read_text()) if path.exists() else 0
    if value < 0:
        raise RuntimeError("invalid published observation ticket")
    return value


def atomic(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix="." + path.name + ".", dir=path.parent)
    try:
        with os.fdopen(fd, "w") as stream:
            stream.write(text)
            stream.flush()
            os.fsync(stream.fileno())
        temp_path = Path(tmp)
        temp_path.chmod(0o600)
        temp_path.replace(path)
        directory = os.open(path.parent, os.O_DIRECTORY)
        try:
            os.fsync(directory)
        finally:
            os.close(directory)
    finally:
        temp_path = Path(tmp)
        if temp_path.exists():
            temp_path.unlink()


def read_task(path: Path) -> tuple[Meta, str]:
    text = path.read_text()
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: no front matter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError(f"{path}: unterminated front matter")
    return cast(Meta, json.loads(text[4:end])), text[end + 5 :]


def write_task(path: Path, meta: Meta, body: str) -> None:
    atomic(path, "---\n" + json.dumps(meta, indent=2, sort_keys=True) + "\n---\n" + body)


def git_tasks() -> list[Task]:
    result: list[Task] = []
    for path in sorted(TASKS.glob("AR-*.md")):
        meta, body = read_task(path)
        result.append((path, meta, body))
    return result


def all_tasks() -> list[Task]:
    """Load one authoritative snapshot through the selected backend."""
    return storage_backend().load_tasks()


def render_current(tasks: list[Task]) -> str:
    groups: dict[str, list[Meta]] = {status: [] for status in STATUSES}
    for _, meta, _ in tasks:
        groups[meta["status"]].append(meta)
    labels = {x: x.replace("_", " ").title() for x in STATUSES}
    lines = [
        f"# {project_settings()['project_title']} current coordination state",
        "",
        "This file is generated. Read `README.md`, then use `tools/handoffctl snapshot`.",
        "Never edit this file directly.",
        "",
    ]
    by_id = {meta["id"]: path.name for path, meta, _ in tasks}

    def clean(value: object) -> str:
        return (
            str(value or "-")
            .replace("\\", "\\\\")
            .replace("|", "\\|")
            .replace("\n", " ")
            .replace("[", "\\[")
            .replace("]", "\\]")
            .replace("(", "\\(")
            .replace(")", "\\)")
        )

    for status in CURRENT_STATUSES:
        rows = sorted(
            groups[status], key=lambda meta: (PRIORITIES.index(meta["priority"]), meta["id"])
        )
        if not rows:
            continue
        lines += [
            f"## {labels[status]}",
            "",
            "| Priority | Task | Summary | Next action | Owner |",
            "| --- | --- | --- | --- | --- |",
        ]
        for meta in rows:
            link = f"[{clean(task_label(meta))}](tasks/{by_id[meta['id']]})"
            row = (
                f"| {meta['priority']} | {link} | "
                f"{clean(meta['summary'])} | {clean(meta['next_action'])} | "
                f"{clean(meta.get('owner'))} |"
            )
            lines.append(row)
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def parse_worktree_listing(raw: str) -> list[tuple[Path, str, str]]:
    """Reuse Git's listed head and branch when available."""
    records: list[tuple[Path, str, str]] = []
    for block in raw.split("\n\n"):
        lines = block.splitlines()
        if not lines or not lines[0].startswith("worktree "):
            continue
        head = next((line[5:] for line in lines[1:] if line.startswith("HEAD ")), "")
        if re.fullmatch(r"[0-9a-f]{40,64}", head) is None:
            head = ""
        branch = next((line[7:] for line in lines[1:] if line.startswith("branch ")), "")
        branch = branch.removeprefix("refs/heads/")
        if not branch and "detached" in lines:
            branch = "DETACHED"
        records.append((Path(lines[0][9:]), head, branch))
    return records


def scan_worktree(item: tuple[Path, str, str]) -> dict[str, Any]:
    """Observe one product checkout without Git mutation."""
    path, listed_head, listed_branch = item
    head = listed_head or run(["git", "-C", str(path), "rev-parse", "HEAD"]).stdout.strip()
    branch = listed_branch or (
        run(
            ["git", "-C", str(path), "symbolic-ref", "--short", "-q", "HEAD"], check=False
        ).stdout.strip()
        or "DETACHED"
    )
    changed = run(["git", "-C", str(path), "status", "--porcelain=v1"]).stdout.splitlines()
    counts = run(
        ["git", "-C", str(path), "rev-list", "--left-right", "--count", "origin/main...HEAD"],
        check=False,
    ).stdout.split()
    return {
        "key": path.name,
        "branch": branch,
        "head": head,
        "dirty": len(changed),
        "paths": [line[3:] for line in changed[:50]],
        "behind": int(counts[0]) if len(counts) == 2 else None,
        "ahead": int(counts[1]) if len(counts) == 2 else None,
    }


def project_scan() -> State:
    settings = config()
    base = Path(settings["projects_root"])
    repo = base / settings["product_worktree"]

    def listed_worktrees(checkout: Path) -> list[tuple[Path, str, str]]:
        raw = run(["git", "-C", str(checkout), "worktree", "list", "--porcelain"]).stdout
        return parse_worktree_listing(raw)

    # Exclude coordinator-owned checkouts from product worktree projections.
    coordinator_paths = {path.resolve() for path, _, _ in listed_worktrees(ROOT)}
    paths: list[tuple[Path, str, str]] = []
    seen_paths: set[Path] = set()
    for path, head, branch in listed_worktrees(repo):
        if path.resolve() not in coordinator_paths and path not in seen_paths:
            paths.append((path, head, branch))
            seen_paths.add(path)
    github = settings["github_repository"]
    pr_args = [
        "gh",
        "pr",
        "list",
        "-R",
        github,
        "--state",
        "open",
        "--limit",
        "100",
        "--json",
        "number,title,headRefName,headRefOid,baseRefName,isDraft,mergeStateStatus,statusCheckRollup",
    ]
    run_args = [
        "gh",
        "run",
        "list",
        "-R",
        github,
        "--limit",
        "12",
        "--json",
        "databaseId,headSha,status,conclusion,workflowName,event",
    ]
    with ThreadPoolExecutor(max_workers=min(32, max(1, len(paths))) + 3) as workers:
        prs_result = workers.submit(run_github_observation, pr_args)
        runs_result = workers.submit(run_github_observation, run_args)
        remote_result = workers.submit(
            run, ["git", "-C", str(repo), "ls-remote", "origin", "refs/heads/main"]
        )
        worktrees = list(workers.map(scan_worktree, paths))
        prs = json.loads(prs_result.result().stdout)
        runs = json.loads(runs_result.result().stdout)
        remote_line = remote_result.result().stdout.strip()
    if not remote_line:
        raise RuntimeError("remote main is missing")
    return {
        "remote_main": remote_line.split()[0],
        "origin_main": run(["git", "-C", str(repo), "rev-parse", "origin/main"]).stdout.strip(),
        "primary_head": run(["git", "-C", str(repo), "rev-parse", "HEAD"]).stdout.strip(),
        "worktrees": worktrees,
        "prs": prs,
        "runs": runs,
    }


def live_docs(state: State) -> tuple[str, str]:
    project = [
        f"# {project_settings()['project_title']} live project state",
        "",
        "Generated from local Git and GitHub. Do not edit.",
        "",
        f"- Product remote main: `{state['remote_main']}`",
        f"- Local origin/main: `{state['origin_main']}`",
        f"- Primary worktree head: `{state['primary_head']}`",
        "",
        "## Open pull requests",
        "",
        "| PR | Head | Base | Merge | Checks | Title |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for pr in sorted(state["prs"], key=lambda item: item["number"]):
        checks = [
            (item.get("status") or "") + ":" + (item.get("conclusion") or "")
            for item in pr.get("statusCheckRollup") or []
        ]
        title = pr["title"].replace("|", "/")
        project.append(
            f"| #{pr['number']} | `{pr['headRefName']}@{pr['headRefOid'][:12]}` | "
            f"`{pr['baseRefName']}` | {pr['mergeStateStatus']} | "
            f"{', '.join(checks) or '-'} | {title} |"
        )
    project += [
        "",
        "## Recent workflows",
        "",
        "| Run | SHA | Event | Workflow | State |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in state["runs"]:
        project.append(
            f"| {item['databaseId']} | `{item['headSha'][:12]}` | "
            f"{item['event']} | {item['workflowName']} | "
            f"{item['status']}:{item.get('conclusion') or '-'} |"
        )
    worktrees = [
        f"# {project_settings()['project_title']} worktree inventory",
        "",
        "Generated from live Git. Paths are privacy-safe worktree keys.",
        "",
        "| Worktree | Branch | Head | Dirty | vs origin/main |",
        "| --- | --- | --- | ---: | --- |",
    ]
    for item in state["worktrees"]:
        worktrees.append(
            f"| `{item['key']}` | `{item['branch']}` | "
            f"`{item['head'][:12]}` | {item['dirty']} | "
            f"behind {item['behind']}, ahead {item['ahead']} |"
        )
        if item["dirty"]:
            paths = ", ".join("`" + value + "`" for value in item["paths"])
            worktrees.append(f"| changed files | - | - | - | {paths} |")
    return "\n".join(project) + "\n", "\n".join(worktrees) + "\n"


def sync_task_observations(tasks: list[Task], state: State) -> None:
    observed = {item["key"]: item for item in state["worktrees"]}
    for path, meta, body in tasks:
        key = meta.get("worktree_key")
        if not key or key not in observed:
            continue
        item = observed[key]
        values = {
            "observed_branch": item["branch"],
            "observed_head": item["head"],
            "observed_dirty": item["dirty"],
        }
        if any(meta.get(name) != value for name, value in values.items()):
            meta.update(values)
            meta["updated_at"] = now()
            meta["task_revision"] += 1
            write_task(path, meta, body)


def privacy_pattern_applies(relative: Path, label: str) -> bool:
    """Allow UUID syntax only in exact coordinator identity and contract files."""
    return label != "session-like UUID" or relative not in UUID_PRIVACY_EXEMPT


def possible_uuid_pattern(text: str) -> bool:
    """Reject text without the fixed ASCII shape of any UUID regex match."""
    if len(text) < 36:
        return False
    hyphen = text.find("-", 8)
    while hyphen >= 0:
        if (
            hyphen + 28 <= len(text)
            and text[hyphen + 5] == "-"
            and text[hyphen + 10] == "-"
            and text[hyphen + 15] == "-"
            and all(char in PRIVATE_HEX_DIGITS for char in text[hyphen - 8 : hyphen])
        ):
            return True
        hyphen = text.find("-", hyphen + 1)
    return False


def possible_privacy_pattern(text: str, lowered: str, label: str) -> bool:
    """Use literals before the privacy regex."""
    if not text.isascii():
        return True
    if label == "absolute Linux home path":
        return "/" + "home/" in text
    if label == "absolute Windows user path":
        return ":\\users\\" in lowered
    if label == "private host alias":
        return "ai" + "-ws" in lowered
    if label == "private or loopback IP":
        return "10." in text or "127." in text
    if label == "possible credential":
        return any(
            word in lowered
            for word in ("password", "passwd", "token", "secret", "api_key", "api-key", "apikey")
        )
    if label == "private key":
        return "-----BEGIN " in text
    if label == "session-like UUID":
        return possible_uuid_pattern(text)
    return True


def private_text_errors(relative: Path, text: str) -> list[str]:
    """Keep the original privacy ordering after prefilters."""
    lowered = text.lower()
    return [
        f"{relative}: {label}"
        for regex, label in PRIVATE
        if privacy_pattern_applies(relative, label)
        and possible_privacy_pattern(text, lowered, label)
        and regex.search(text)
    ]


def privacy_errors() -> list[str]:
    errors: list[str] = []
    for path in sorted(ROOT.rglob("*")):
        if (
            not path.is_file()
            or ".git" in path.parts
            or ".runtime" in path.parts
            or ".venv" in path.parts
            or ".mypy_cache" in path.parts
            or ".ruff_cache" in path.parts
            or "__pycache__" in path.parts
            or path.suffix in {".pyc", ".pyo"}
            or "private-archive" in path.parts
        ):
            continue
        relative = path.relative_to(ROOT)
        if path.stat().st_size > 200000:
            errors.append(f"{relative}: state file exceeds 200 KiB")
        try:
            text = path.read_text()
        except UnicodeDecodeError:
            continue
        errors.extend(private_text_errors(relative, text))
    return errors


def introduced_content_errors(before: dict[Path, str | None]) -> list[str]:
    """Reject newly introduced privacy or size findings in mutation-owned files."""
    errors: list[str] = []
    for path, previous in before.items():
        if not path.exists():
            continue
        relative = path.relative_to(ROOT)
        current = path.read_text()
        previous_text = previous or ""
        previous_size = len(previous_text.encode()) if previous is not None else 0
        if path.stat().st_size > 200000 and previous_size <= 200000:
            errors.append(f"{relative}: state file exceeds 200 KiB")
        if current == previous_text:
            continue
        for regex, label in PRIVATE:
            if not privacy_pattern_applies(relative, label):
                continue
            old_matches = Counter(match.group(0) for match in regex.finditer(previous_text))
            new_matches = Counter(match.group(0) for match in regex.finditer(current))
            if new_matches - old_matches:
                errors.append(f"{relative}: newly introduced {label}")
    return errors


def field_errors(path: Path, meta: Meta) -> list[str]:
    errors = [f"{path.name}: missing {name}" for name in REQ if name not in meta]
    errors.extend(f"{path.name}: unknown field {name}" for name in set(meta) - FIELDS)
    return errors


def valid_claim_process(value: object) -> bool:
    """Recognize a legacy or scope-bound optional claim-time process identity."""
    if not isinstance(value, dict) or set(value) not in (
        {"pid", "start_time"},
        {"pid", "start_time", "boot_digest", "pid_namespace"},
    ):
        return False
    if type(value.get("pid")) is not int or int(value["pid"]) <= 0:
        return False
    if type(value.get("start_time")) is not int or int(value["start_time"]) < 0:
        return False
    if set(value) == {"pid", "start_time"}:
        return True
    return (
        isinstance(value.get("boot_digest"), str)
        and bool(re.fullmatch(r"sha256:[0-9a-f]{64}", value["boot_digest"]))
        and isinstance(value.get("pid_namespace"), str)
        and bool(re.fullmatch(r"[0-9]+:[0-9]+", value["pid_namespace"]))
    )


def scoped_claim_process(value: object) -> bool:
    """Require the scope fields needed to safely inspect a former worker."""
    return (
        isinstance(value, dict)
        and set(value) == {"pid", "start_time", "boot_digest", "pid_namespace"}
        and valid_claim_process(value)
    )


def value_errors(path: Path, meta: Meta) -> list[str]:
    errors: list[str] = []
    task_id = meta.get("id", "")
    if not re.fullmatch(r"AR-\d{4}", task_id):
        errors.append(f"{path.name}: invalid id")
    if meta.get("status") not in STATUSES:
        errors.append(f"{task_id}: invalid status")
    if meta.get("priority") not in PRIORITIES:
        errors.append(f"{task_id}: invalid priority")
    revision = meta.get("task_revision")
    if not isinstance(revision, int) or revision < 1:
        errors.append(f"{task_id}: invalid revision")
    errors.extend(
        f"{task_id}: invalid {name}"
        for name in ("title", "summary", "next_action", "updated_at")
        if not isinstance(meta.get(name), str) or not meta.get(name)
    )
    errors.extend(short_title_errors(path, task_id, meta.get("short_title")))
    worktree_key = meta.get("worktree_key")
    if worktree_key not in (None, "") and not valid_binding_worktree(worktree_key):
        errors.append(f"{task_id}: invalid worktree_key")
    errors.extend(f"{task_id}: {error}" for error in gate_errors(meta.get("oracle_gate")))
    errors.extend(execution_metadata_errors(task_id, meta))
    return errors


def execution_metadata_errors(task_id: str, meta: Meta) -> list[str]:  # noqa: C901
    """Validate optional process and execution-fence metadata together."""
    errors: list[str] = []
    claim_process = meta.get("claim_process")
    if claim_process is not None and not valid_claim_process(claim_process):
        errors.append(f"{task_id}: invalid claim_process")
    reservation = meta.get("execution_reservation")
    if reservation is not None and not valid_execution_reservation(reservation):
        errors.append(f"{task_id}: invalid execution_reservation")
    result = meta.get("execution_result")
    if result is not None and not valid_execution_result(result):
        errors.append(f"{task_id}: invalid execution_result")
    errors.extend(execution_abandonment_errors(task_id, meta))
    if not valid_execution_envelope_binding(meta):
        errors.append(f"{task_id}: invalid execution envelope binding")
    if not execution_envelope.valid_replacements(meta.get("execution_envelope_replacements")):
        errors.append(f"{task_id}: invalid execution envelope replacements")
    if error := change_drift.metadata_error(meta):
        errors.append(f"{task_id}: {error}")
    if error := assumption_revalidation.metadata_error(meta):
        errors.append(f"{task_id}: {error}")
    if error := retry_circuit.metadata_error(meta):
        errors.append(f"{task_id}: {error}")
    if error := al.metadata_error(meta):
        errors.append(f"{task_id}: {error}")
    return errors


def execution_abandonment_errors(task_id: str, meta: Meta) -> list[str]:
    """Reject malformed bounded abandonment history before it reaches projections."""
    if execution_abandonment.valid_records(meta.get("execution_abandonments")):
        return []
    return [f"{task_id}: invalid execution_abandonments"]


valid_execution_reservation = execution_envelope.valid_reservation
valid_execution_envelope_binding = execution_envelope.valid_binding
valid_execution_result = execution_receipt.valid
execution_result_matches = execution_receipt.matches


def live_execution_reservation(meta: Meta) -> Meta | None:
    reservation = meta.get("execution_reservation")
    if not valid_execution_reservation(reservation):
        return None
    valid_reservation = cast(Meta, reservation)
    expires = dt.datetime.fromisoformat(str(valid_reservation["expires_at"]).replace("Z", "+00:00"))
    return valid_reservation if expires > dt.datetime.now(dt.UTC) else None


def require_no_execution_reservation(meta: Meta) -> None:
    if meta.get("execution_reservation") is not None:
        raise RuntimeError("EXECUTION_RECOVERY_REQUIRED: task has a bound execution reservation")


def reference_errors(path: Path, meta: Meta) -> list[str]:
    errors: list[str] = []
    task_id = str(meta.get("id", ""))
    try:
        dt.datetime.fromisoformat(str(meta.get("updated_at", "")).replace("Z", "+00:00"))
    except ValueError:
        errors.append(f"{task_id}: invalid updated_at")
    checkpoint = meta.get("checkpoint_commit")
    if checkpoint and not re.fullmatch(r"[0-9a-f]{40}", checkpoint):
        errors.append(f"{task_id}: invalid checkpoint commit")
    plan = meta.get("plan")
    if plan and not (path.parent / plan).resolve().is_file():
        errors.append(f"{task_id}: missing plan {plan}")
    reference = meta.get("execution_envelope_ref")
    if isinstance(reference, str):
        envelope = meta.get("execution_envelope")
        found = execution_envelope.errors(envelope)
        if not isinstance(envelope, dict) or found:
            errors.append(f"{task_id}: invalid execution envelope: {'; '.join(found)}")
        elif meta.get("execution_envelope_digest") != execution_envelope.canonical_digest(envelope):
            errors.append(f"{task_id}: execution envelope digest mismatch")
        elif meta.get("execution_envelope_revision") != envelope.get("envelope_revision"):
            errors.append(f"{task_id}: execution envelope revision mismatch")
        elif meta.get("execution_envelope_task_revision") != envelope.get("task_revision"):
            errors.append(f"{task_id}: execution envelope task revision mismatch")
    return errors


def supersession_errors(tasks: list[Task]) -> list[str]:
    """Validate explicitly recorded supersession pointers without weakening old data."""
    by_id = {meta.get("id"): meta for _, meta, _ in tasks}
    errors: list[str] = []
    for _, meta, _ in tasks:
        successor = meta.get("superseded_by")
        if successor is None:
            continue
        task_id = str(meta.get("id", ""))
        if meta.get("status") != "superseded":
            errors.append(f"{task_id}: superseded_by requires superseded status")
            continue
        if not isinstance(successor, str) or not re.fullmatch(r"AR-\d{4}", successor):
            errors.append(f"{task_id}: invalid superseded_by")
            continue
        if successor == task_id:
            errors.append(f"{task_id}: superseded_by self reference")
            continue
        if successor not in by_id:
            errors.append(f"{task_id}: missing superseded_by task {successor}")
            continue
        if not dependency_satisfied(successor, tasks):
            errors.append(f"{task_id}: superseded_by chain does not end in done task")
    return errors


def basic_task_errors(path: Path, meta: Meta, policy: EvidencePolicy | None = None) -> list[str]:
    return [
        *field_errors(path, meta),
        *value_errors(path, meta),
        *reference_errors(path, meta),
        *task_spec_errors(ROOT, meta, policy),
    ]


def parse_claim_expiry(expiry: object) -> dt.datetime:
    """Parse one timezone-aware lease deadline."""
    if not isinstance(expiry, str) or not expiry:
        raise ValueError("missing or non-string claim expiry")
    parsed = dt.datetime.fromisoformat(expiry.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("claim expiry lacks timezone")
    return parsed.astimezone(dt.UTC)


def process_start_time(pid: int) -> int | None:
    """Return a Linux process start time, or ``None`` after it has exited."""
    proc = Path("/proc") / str(pid)
    try:
        stat_fields = (proc / "stat").read_text(encoding="utf-8").rsplit(")", 1)[1].split()
        return int(stat_fields[19])
    except FileNotFoundError:
        return None
    except (OSError, IndexError, ValueError) as error:
        raise RuntimeError("cannot independently read worker process identity") from error


def worker_execution_scope() -> tuple[str, str]:
    """Return the local boot and PID-namespace identities for recovery fencing."""
    try:
        boot_id = (Path("/proc/sys/kernel/random/boot_id").read_text(encoding="utf-8")).strip()
        namespace = Path("/proc/self/ns/pid").stat()
    except OSError as error:
        raise RuntimeError("cannot independently read worker execution scope") from error
    pid_namespace = f"{namespace.st_dev}:{namespace.st_ino}"
    try:
        valid_boot_id = str(uuid.UUID(boot_id)) == boot_id
    except ValueError:
        valid_boot_id = False
    if not valid_boot_id:
        raise RuntimeError("worker execution scope has invalid boot identity")
    return f"sha256:{hashlib.sha256(boot_id.encode()).hexdigest()}", pid_namespace


def claimed_process_identity(args: argparse.Namespace) -> Meta | None:
    """Validate an optional live worker identity at the exact claim transition."""
    pid = getattr(args, "worker_pid", None)
    start_time = getattr(args, "worker_start_time", None)
    if pid is None and start_time is None:
        return None
    if type(pid) is not int or pid <= 0 or type(start_time) is not int or start_time < 0:
        raise RuntimeError(
            "claim worker identity requires positive --worker-pid and --worker-start-time"
        )
    if process_start_time(pid) != start_time:
        raise RuntimeError("claim worker identity is not a live matching process")
    boot_digest, pid_namespace = worker_execution_scope()
    return {
        "pid": pid,
        "start_time": start_time,
        "boot_digest": boot_digest,
        "pid_namespace": pid_namespace,
    }


def require_claimed_worker_absent(meta: Meta) -> None:
    """Require a claim-time identity and independently confirm it no longer runs."""
    identity = meta.get("claim_process")
    if not scoped_claim_process(identity):
        raise RuntimeError(
            "snapshot-less recovery requires a scope-bound claim-time worker identity"
        )
    identity = cast(Meta, identity)
    boot_digest, pid_namespace = worker_execution_scope()
    if identity["boot_digest"] != boot_digest or identity["pid_namespace"] != pid_namespace:
        raise RuntimeError("snapshot-less recovery cannot verify the claim execution scope")
    pid = identity["pid"]
    start_time = identity["start_time"]
    if process_start_time(pid) == start_time:
        raise RuntimeError("former worker process is still alive")


def legacy_recovery_admitted(args: argparse.Namespace, meta: Meta) -> bool:
    """Admit an explicitly acknowledged recovery of a pre-identity legacy claim."""
    if not getattr(args, "allow_legacy_without_identity", False):
        return False
    if "claim_process" in meta:
        return False
    expiry = parse_claim_expiry(meta.get("claim_expires"))
    return not expiry > dt.datetime.now(dt.UTC)


def attach_claim_process(args: argparse.Namespace, meta: Meta) -> None:
    """Replace optional claim-time process identity after strict live validation."""
    meta.pop("claim_process", None)
    process_identity = claimed_process_identity(args)
    if process_identity is not None:
        meta["claim_process"] = process_identity


def active_expiry_errors(task_id: str, expiry: object) -> list[str]:
    if not expiry:
        return [f"{task_id}: active without claim"]
    try:
        parsed_expiry = parse_claim_expiry(expiry)
    except (TypeError, ValueError):
        return [f"{task_id}: invalid claim expiry"]
    if parsed_expiry <= dt.datetime.now(dt.UTC):
        return [f"{task_id}: expired claim"]
    return []


def claim_errors(
    meta: Meta,
    active_owners: dict[str, str],
    active_worktrees: dict[str, str],
    active_branches: dict[str, str],
) -> list[str]:
    errors: list[str] = []
    task_id = str(meta.get("id", ""))
    if meta.get("status") != "in_progress":
        if meta.get("owner") or meta.get("claim_expires"):
            errors.append(f"{task_id}: inactive task retains claim")
        return errors
    if not meta.get("owner"):
        errors.append(f"{task_id}: active without claim")
    errors.extend(active_expiry_errors(task_id, meta.get("claim_expires")))
    for field, seen in (
        ("owner", active_owners),
        ("worktree_key", active_worktrees),
        ("branch", active_branches),
    ):
        value = meta.get(field)
        if value and value in seen:
            errors.append(f"{task_id}: active {field} also used by {seen[value]}")
        elif value:
            seen[value] = task_id
    return errors


def mutation_global_errors(tasks: list[Task]) -> list[str]:
    """Check global identities, dependency graph, and active-key uniqueness."""
    errors: list[str] = []
    ids: dict[str, Path] = {}
    active: dict[str, dict[str, str]] = {
        "owner": {},
        "worktree_key": {},
        "branch": {},
    }
    for path, meta, _ in tasks:
        task_id = str(meta.get("id", ""))
        if task_id in ids:
            errors.append(f"duplicate {task_id}")
        ids[task_id] = path
        if meta.get("status") != "in_progress":
            continue
        for field, seen in active.items():
            value = meta.get(field)
            if value and value in seen:
                errors.append(f"{task_id}: active {field} also used by {seen[value]}")
            elif value:
                seen[value] = task_id
    errors.extend(graph_errors(tasks))
    errors.extend(hierarchy_errors(tasks))
    errors.extend(supersession_errors(tasks))
    return errors


def mutation_errors(
    path: Path,
    before: dict[Path, str | None],
    policy: EvidencePolicy | None = None,
    *,
    rendered_snapshot: tuple[list[Task], dict[Path, str], Meta] | None = None,
) -> list[str]:
    """Validate a Git mutation."""
    tasks = all_tasks()
    selected = [meta for candidate, meta, _ in tasks if candidate == path]
    if len(selected) != 1:
        return [f"{path.name}: mutation target is not unique"]
    errors = [] if policy is not None else task_spec_policy_errors(ROOT)
    errors.extend(basic_task_errors(path, selected[0], policy))
    errors.extend(claim_errors(selected[0], {}, {}, {}))
    errors.extend(mutation_global_errors(tasks))
    errors.extend(generated_view_errors(tasks, rendered_snapshot=rendered_snapshot))
    errors.extend(introduced_content_errors(before))
    return errors


def render_status_view(tasks: list[Task]) -> str:
    """Render the public dashboard."""
    return render_status(tasks, STATUSES, PRIORITIES, str(project_settings()["project_title"]))


def render_status_views(tasks: list[Task]) -> dict[str, str]:
    """Render the complete status view."""
    return render_status_pages_from_text(render_status_view(tasks))


def status_projection_errors(expected: dict[str, str]) -> list[str]:
    """Compare status pages."""
    errors = [
        f"{relative} differs from generated tasks"
        for relative, content in expected.items()
        if not (ROOT / relative).exists() or (ROOT / relative).read_text() != content
    ]
    expected_paths = {ROOT / relative for relative in expected}
    errors.extend(
        f"{status.relative_to(ROOT)} is stale"
        for status in sorted((ROOT / "status").glob("STATUS-*.md"))
        if status not in expected_paths
    )
    return errors


def status_views_for_validation(
    tasks: list[Task], snapshot: tuple[list[Task], dict[Path, str], Meta] | None
) -> dict[str, str]:
    if snapshot is None:
        return render_status_views(tasks)
    return {
        str(target.relative_to(ROOT)): content
        for target, content in snapshot[1].items()
        if target.name == "STATUS.md" or target.parent.name == "status"
    }


def generated_view_errors(
    tasks: list[Task],
    *,
    rendered_snapshot: tuple[list[Task], dict[Path, str], Meta] | None = None,
) -> list[str]:
    """Check task-derived views."""
    errors: list[str] = []
    if not all(meta.get("status") in STATUSES for _, meta, _ in tasks):
        return errors
    reusable_snapshot = (
        rendered_snapshot
        if rendered_snapshot is not None
        and tasks == rendered_snapshot[0]
        and project_settings() == rendered_snapshot[2]
        else None
    )
    current = ROOT / "CURRENT.md"
    expected_current = (
        reusable_snapshot[1][current] if reusable_snapshot is not None else render_current(tasks)
    )
    if current.exists() and current.read_text() != expected_current:
        errors.append("CURRENT.md differs from generated tasks")
    if not project_settings()["status_view"]:
        return errors
    try:
        expected_status = status_views_for_validation(tasks, reusable_snapshot)
    except StatusRenderError as error:
        errors.extend(str(error).splitlines())
    else:
        errors.extend(status_projection_errors(expected_status))
    return errors


def rollback_validation_errors() -> list[str]:
    """Validate the rollback journal."""
    try:
        for record in load_records(ROOT):
            validate_record(record)
    except (OSError, ValueError, RuntimeError) as error:
        return [f"rollback validation failed: {error}"]
    return []


def session_validation_errors() -> list[str]:
    """Validate session records."""
    try:
        for record in storage_backend().load_session_records():
            validate_session_record(record)
    except (OSError, ValueError, RuntimeError) as error:
        return [f"session validation failed: {error}"]
    return []


def directive_validation_errors() -> list[str]:
    """Validate the directive journal."""
    try:
        records = latest_directives(ROOT)
        for record in records:
            validate_directive(record)
        active = [record for record in records if record["lifecycle"] == "active"]
        for index, record in enumerate(active):
            conflicts = conflicting_directives(active[index + 1 :], record)
            if conflicts:
                return [
                    "directive validation failed: active conflict requires guidance AR-0053: "
                    + ",".join(str(item["directive_id"]) for item in conflicts)
                ]
    except (OSError, ValueError, RuntimeError) as error:
        return [f"directive validation failed: {error}"]
    return []


def validate(
    *, live: bool = False, policy: EvidencePolicy | None = None, live_state: State | None = None
) -> list[str]:
    errors: list[str] = []
    selected_policy = policy
    if selected_policy is None:
        try:
            selected_policy = evidence_policy(ROOT)
        except RuntimeError as error:
            errors.append(str(error))
            selected_policy = DEFAULT_EVIDENCE_POLICY
    tasks = all_tasks()
    ids: dict[str, Path] = {}
    active_owners: dict[str, str] = {}
    active_worktrees: dict[str, str] = {}
    active_branches: dict[str, str] = {}
    for path, meta, _ in tasks:
        task_id = str(meta.get("id", ""))
        if task_id in ids:
            errors.append(f"duplicate {task_id}")
        ids[task_id] = path
        errors.extend(basic_task_errors(path, meta, selected_policy))
        errors.extend(claim_errors(meta, active_owners, active_worktrees, active_branches))
    errors.extend(graph_errors(tasks))
    errors.extend(hierarchy_errors(tasks))
    errors.extend(supersession_errors(tasks))
    errors.extend(generated_view_errors(tasks))
    try:
        for record in storage_backend().load_checkpoint_records():
            validate_checkpoint(record)
    except (OSError, ValueError, RuntimeError) as error:
        errors.append(f"checkpoint validation failed: {error}")
    errors.extend(rollback_validation_errors())
    errors.extend(session_validation_errors())
    errors.extend(directive_validation_errors())
    errors.extend(privacy_errors())
    if live:
        # Hosted run/worktree observations can change after reconciliation.
        # They are advisory, not immutable local integrity evidence.
        del live_state
    return errors


def commit(message: str, paths: list[Path]) -> bool:
    relative = [str(path.relative_to(ROOT)) for path in paths]
    if not relative:
        return False
    run(["git", "-C", str(ROOT), "add", "--", *relative])
    try:
        if (
            run(
                ["git", "-C", str(ROOT), "diff", "--cached", "--quiet", "--", *relative],
                check=False,
            ).returncode
            == 0
        ):
            return False
        command = ["git", "-C", str(ROOT), "commit"]
        if project_settings()["commit_signoff"]:
            command.append("-s")
        run([*command, "-m", message, "--only", "--", *relative], capture=False)
        return True
    except Exception:
        run(["git", "-C", str(ROOT), "reset", "--", *relative], check=False)
        raise


def current_commit_oid() -> str:
    oid = run(["git", "-C", str(ROOT), "rev-parse", "HEAD"]).stdout.strip()
    if not re.fullmatch(r"[0-9a-f]{40}", oid):
        raise RuntimeError("cannot identify signed receipt commit")
    return oid


def replication_enabled() -> bool:
    """Return whether this checkout is the configured writable replica."""
    return CONFIG.exists() and bool(config().get("push_enabled", False))


def replica_heads() -> tuple[str, str]:
    """Fetch and return local/remote main heads for a configured replica."""
    remote = run(["git", "-C", str(ROOT), "remote", "get-url", "origin"], check=False)
    if remote.returncode:
        raise RuntimeError("state replication is enabled but origin is missing")
    branch = run(
        ["git", "-C", str(ROOT), "symbolic-ref", "--short", "-q", "HEAD"],
        check=False,
    ).stdout.strip()
    if branch != "main":
        raise RuntimeError("state replication requires the main checkout")
    run(["git", "-C", str(ROOT), "fetch", "--no-tags", "origin", "main"])
    local_head = run(["git", "-C", str(ROOT), "rev-parse", "HEAD"]).stdout.strip()
    remote_head = run(["git", "-C", str(ROOT), "rev-parse", "FETCH_HEAD"]).stdout.strip()
    return local_head, remote_head


def is_ancestor(older: str, newer: str) -> bool:
    """Return whether one fetched state revision is an ancestor of another."""
    return (
        run(
            ["git", "-C", str(ROOT), "merge-base", "--is-ancestor", older, newer],
            check=False,
        ).returncode
        == 0
    )


def record_replica_block(code: str, local_head: str, remote_head: str) -> None:
    """Persist a reconciliation circuit-breaker marker."""
    atomic(
        REPLICA_BLOCKED,
        json.dumps(
            {
                "at": now(),
                "code": code,
                "local_head": local_head,
                "remote_head": remote_head,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
    )


def clear_replica_block() -> None:
    """Clear a recovered replica circuit breaker."""
    REPLICA_BLOCKED.unlink(missing_ok=True)


def sync_replica_before_write() -> None:
    """Fast-forward a clean replica."""
    if not replication_enabled():
        return
    local_head, remote_head = replica_heads()
    if local_head == remote_head or is_ancestor(remote_head, local_head):
        clear_replica_block()
        return
    if not is_ancestor(local_head, remote_head):
        record_replica_block("REPLICA_DIVERGED", local_head, remote_head)
        raise ReplicaDivergedError(
            "REPLICA_DIVERGED: state histories require explicit reconciliation"
        )
    dirty = run(
        ["git", "-C", str(ROOT), "status", "--porcelain=v1", "--untracked-files=all"]
    ).stdout
    if dirty:
        record_replica_block("REPLICA_BEHIND_DIRTY", local_head, remote_head)
        raise ReplicaDivergedError(
            "REPLICA_BEHIND_DIRTY: clean the state checkout before fast-forwarding"
        )
    run(["git", "-C", str(ROOT), "merge", "--ff-only", remote_head])
    clear_replica_block()


def push_replica() -> None:
    if not replication_enabled():
        return
    local_head, remote_head = replica_heads()
    if local_head == remote_head:
        clear_replica_block()
        return
    if not is_ancestor(remote_head, local_head):
        relation = "REPLICA_BEHIND" if is_ancestor(local_head, remote_head) else "REPLICA_DIVERGED"
        record_replica_block(relation, local_head, remote_head)
        raise ReplicaDivergedError(
            f"{relation}: refusing non-fast-forward state push; reconcile before retrying"
        )
    run(["git", "-C", str(ROOT), "push", "origin", f"{local_head}:refs/heads/main"])
    clear_replica_block()


def restore_paths(before: dict[Path, str | None]) -> None:
    """Restore a transaction snapshot."""
    for path, old in before.items():
        if old is None:
            path.unlink(missing_ok=True)
        else:
            atomic(path, old)


def generated_paths() -> list[Path]:
    """Return generated projection paths."""
    names = ["CURRENT.md", "PROJECT_STATE.md", "WORKTREES.md"]
    if project_settings()["status_view"]:
        names.append("STATUS.md")
        names.extend(
            str(path.relative_to(ROOT)) for path in sorted((ROOT / "status").glob("STATUS-*.md"))
        )
    return [ROOT / name for name in names]


def changed_paths(before: dict[Path, str | None], *, include_deleted: bool = False) -> list[Path]:
    """Return changed snapshot paths."""
    return [
        path
        for path, old in before.items()
        if (include_deleted or path.exists())
        and (path.read_text() if path.exists() else None) != old
    ]


def write_generated_views(tasks: list[Task], state: Meta) -> None:
    """Atomically refresh projections."""
    atomic(ROOT / "CURRENT.md", render_current(tasks))
    if project_settings()["status_view"]:
        expected = render_status_views(tasks)
        write_status_views(expected)
    project, worktrees = live_docs(state)
    atomic(ROOT / "PROJECT_STATE.md", project)
    atomic(ROOT / "WORKTREES.md", worktrees)


def policy_snapshot(policy: EvidencePolicy | None) -> EvidencePolicy:
    """Return one policy snapshot."""
    return evidence_policy(ROOT) if policy is None else policy


def reconcile(
    *,
    do_commit: bool,
    push: bool = False,
    policy: EvidencePolicy | None = None,
) -> bool:
    selected_policy = policy_snapshot(policy)
    if backend_selection()["backend"] == "sqlite":
        return reconcile_sqlite(do_commit=do_commit, push=push, policy=selected_policy)
    if push and not do_commit:
        raise RuntimeError("PUSH_REQUIRES_COMMIT: reconcile --push also requires --commit")

    # Keep external observations outside the authority lock.
    for _ in range(32):
        scan_config = config() if CONFIG.exists() else None
        scan_binding = project_binding()
        ticket = reserve_observation_ticket()
        state = project_scan()
        with locked(phase="git_reconcile"):
            result = apply_git_reconciliation(
                state, selected_policy, scan_config, scan_binding, ticket, do_commit, push
            )
        if result is not None:
            return result
    raise RuntimeError("OBSERVATION_SUPERSEDED: retry reconcile after concurrent publications")


def observation_is_superseded(scan_config: Meta | None, scan_binding: Meta, ticket: int) -> bool:
    """Fence an unlocked scan."""
    if backend_selection()["backend"] != "git":
        raise RuntimeError("BACKEND_CHANGED: retry using the selected backend")
    current_config = config() if CONFIG.exists() else None
    if current_config != scan_config or project_binding() != scan_binding:
        raise RuntimeError("OBSERVATION_INPUT_CHANGED: retry reconcile")
    sync_replica_before_write()
    return ticket < published_observation_ticket()


def pending_observation_paths() -> list[Path]:
    """Return pending coordinator paths."""
    marker = RUNTIME / "last-reconcile.json"
    if not marker.exists():
        return []
    record = json.loads(marker.read_text())
    raw = record.get("pending_paths", [])
    if not isinstance(raw, list) or not all(isinstance(value, str) for value in raw):
        raise RuntimeError("invalid pending reconciliation paths")
    paths = [ROOT / value for value in raw]
    validate_pending_path_scope(paths)
    hashes = record.get("pending_hashes", {})
    if not isinstance(hashes, dict) or set(hashes) != set(raw):
        raise RuntimeError("invalid pending reconciliation hashes")
    remaining: list[Path] = []
    for value, path in zip(raw, paths, strict=True):
        if hashes[value] == pending_path_digest(path):
            remaining.append(path)
        elif not pending_path_matches_head(path):
            raise RuntimeError(
                "PENDING_OBSERVATION_CHANGED: reconcile cannot commit edited content"
            )
    return remaining


def pending_path_matches_head(path: Path) -> bool:
    """Discard paths already committed."""
    relative = path.relative_to(ROOT).as_posix()
    committed = run(["git", "-C", str(ROOT), "show", f"HEAD:{relative}"], check=False)
    if committed.returncode:
        return not path.exists()
    return path.exists() and path.read_text(encoding="utf-8") == committed.stdout


def validate_pending_path_scope(paths: list[Path]) -> None:
    """Refuse unsafe marker paths."""
    allowed = {path.resolve() for path, _, _ in all_tasks()}
    allowed.update(path.resolve() for path in generated_paths())
    if any(
        path.resolve() not in allowed
        and not (
            path.parent.resolve() == (ROOT / "status").resolve()
            and re.fullmatch(r"STATUS-[A-Za-z0-9_-]+\.md", path.name)
        )
        for path in paths
    ):
        raise RuntimeError("pending reconciliation path is outside coordinator projections")


def pending_path_digest(path: Path) -> str | None:
    """Bind a pending path to contents."""
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else None


def remaining_pending_paths(paths: list[Path], do_commit: bool) -> list[str]:
    """Keep coordinator paths pending commit."""
    if do_commit:
        return []
    return [str(path.relative_to(ROOT)) for path in paths]


def apply_git_reconciliation(
    state: State,
    policy: EvidencePolicy,
    scan_config: Meta | None,
    scan_binding: Meta,
    ticket: int,
    do_commit: bool,
    push: bool,
) -> bool | None:
    """Apply an external observation."""
    if observation_is_superseded(scan_config, scan_binding, ticket):
        return None
    prior_pending = pending_observation_paths()
    generated = generated_paths()
    before: dict[Path, str | None] = {path: path.read_text() for path, _, _ in all_tasks()}
    before.update({path: path.read_text() if path.exists() else None for path in generated})
    committed = False
    try:
        sync_task_observations(all_tasks(), state)
        tasks = all_tasks()
        write_generated_views(tasks, state)
        errors = validate(live=False, policy=policy)
        if errors:
            raise RuntimeError("validation failed:\n" + "\n".join(errors))
        require_policy_unchanged(ROOT, policy)
        for path in generated_paths():
            before.setdefault(path, None)
        touched = changed_paths(before, include_deleted=True)
        pending = sorted(set(prior_pending + touched))
        title = project_settings()["project_title"]
        committed = commit(f"chore(state): reconcile {title}", pending) if do_commit else False
        head = run(["git", "-C", str(ROOT), "rev-parse", "HEAD"], check=False).stdout.strip()
        atomic(observation_marker("observation-published"), f"{ticket}\n")
        atomic(
            RUNTIME / "last-reconcile.json",
            json.dumps(
                {
                    "at": now(),
                    "ticket": ticket,
                    "state_commit": head,
                    "project_main": state["remote_main"],
                    "pending_paths": remaining_pending_paths(pending, do_commit),
                    "pending_hashes": {
                        str(path.relative_to(ROOT)): pending_path_digest(path) for path in pending
                    }
                    if not do_commit
                    else {},
                },
                indent=2,
            )
            + "\n",
        )
        if push:
            push_replica()
        return committed if do_commit else True
    except Exception:
        if not committed:
            restore_paths(before)
        raise


def write_session_projections(session_records: list[Meta]) -> list[Path]:
    """Render bounded session histories."""
    by_task: dict[str, list[Meta]] = {}
    for record in session_records:
        validate_session_record(record)
        by_task.setdefault(str(record["task"]), []).append(record)
    sessions_root = ROOT / "sessions"
    sessions_root.mkdir(mode=0o700, parents=True, exist_ok=True)
    for task_id, records in by_task.items():
        atomic(
            session_path(ROOT, task_id),
            "".join(
                json.dumps(item, sort_keys=True, separators=(",", ":")) + "\n" for item in records
            ),
        )
    for path in sessions_root.glob("AR-*.jsonl"):
        if path.stem not in by_task:
            path.unlink()
    return [session_path(ROOT, task_id) for task_id in by_task]


def write_checkpoint_projections(checkpoint_records: list[Meta]) -> list[Path]:
    """Render bounded checkpoint histories."""
    by_task: dict[str, list[Meta]] = {}
    for record in checkpoint_records:
        validate_checkpoint(record)
        by_task.setdefault(str(record["task"]), []).append(record)
    checkpoints_root = ROOT / "checkpoints"
    checkpoints_root.mkdir(mode=0o700, parents=True, exist_ok=True)
    for task_id, records in by_task.items():
        atomic(
            checkpoint_path(ROOT, task_id),
            "".join(
                json.dumps(item, sort_keys=True, separators=(",", ":")) + "\n" for item in records
            ),
        )
    for path in checkpoints_root.glob("AR-*.jsonl"):
        if path.stem not in by_task:
            path.unlink()
    return [checkpoint_path(ROOT, task_id) for task_id in by_task]


def write_sqlite_projections(
    tasks: list[Task],
    *,
    already_locked: bool = False,
    policy: EvidencePolicy | None = None,
) -> list[Path]:
    """Regenerate Markdown projections."""
    selected_policy = policy_snapshot(policy)
    with contextlib.nullcontext() if already_locked else locked():
        expected = {path.resolve() for path, _, _ in tasks}
        for path, meta, body in tasks:
            write_task(path, meta, body)
        for path in TASKS.glob("AR-*.md"):
            if path.resolve() not in expected:
                path.unlink()
        views = rendered_task_views(tasks)
        for target, content in views.items():
            atomic(target, content)
        backend = storage_backend()
        issue_series_paths = issue_series_service.sqlite_projection_paths(backend)
        require_policy_unchanged(ROOT, selected_policy)
        errors = validate(live=False, policy=selected_policy)
        if errors:
            raise RuntimeError("projection validation failed:\n" + "\n".join(errors))
        session_records = backend.load_session_records()
        session_paths = write_session_projections(session_records)
        checkpoint_records = backend.load_checkpoint_records()
        checkpoint_paths = write_checkpoint_projections(checkpoint_records)
        return [
            *[path for path, _, _ in tasks],
            *views,
            *issue_series_paths,
            *session_paths,
            *checkpoint_paths,
        ]


def export_sqlite_projections(policy: EvidencePolicy | None = None) -> list[Path]:
    """Regenerate SQLite projections."""
    selected_policy = policy_snapshot(policy)
    return write_sqlite_projections(all_tasks(), policy=selected_policy)


def refresh_sqlite_live_state() -> State | None:
    """Refresh configured live observations."""
    if not (CONFIG.exists() and config().get("github_repository")):
        return None
    state = project_scan()
    backend = mutating_sqlite_backend()
    backend.update_observations({item["key"]: item for item in state["worktrees"]}, now())
    return state


def reconcile_sqlite(*, do_commit: bool, push: bool, policy: EvidencePolicy | None = None) -> bool:
    """Export local authority."""
    if push and not do_commit:
        raise RuntimeError("SQLite publication requires --commit with --push")
    selected_policy = policy_snapshot(policy)
    before: dict[Path, str | None] = {path: path.read_text() for path in TASKS.glob("AR-*.md")}
    before.update({path: path.read_text() for path in (ROOT / "sessions").glob("AR-*.jsonl")})
    before.update({path: path.read_text() for path in (ROOT / "checkpoints").glob("AR-*.jsonl")})
    before.update({path: path.read_text() if path.exists() else None for path in generated_paths()})
    state = refresh_sqlite_live_state()
    paths = export_sqlite_projections(selected_policy)
    if state is not None:
        project, worktrees = live_docs(state)
        atomic(ROOT / "PROJECT_STATE.md", project)
        atomic(ROOT / "WORKTREES.md", worktrees)
        paths.extend((ROOT / "PROJECT_STATE.md", ROOT / "WORKTREES.md"))
    require_policy_unchanged(ROOT, selected_policy)
    candidates = set(paths) | set(before)
    touched = changed_paths({path: before.get(path) for path in candidates}, include_deleted=True)
    title = project_settings()["project_title"]
    committed = commit(f"chore(state): export {title}", touched) if do_commit else False
    if push:
        push_replica()
    return committed if do_commit else True


def locate(task_id: str) -> Task:
    for path, meta, body in all_tasks():
        if meta["id"] == task_id:
            return path, meta, body
    raise RuntimeError(f"unknown task {task_id}")


def dependency_satisfied(dependency_id: str, tasks: list[Task]) -> bool:
    """Return whether a dependency is terminal."""
    by_id = {meta.get("id"): meta for _, meta, _ in tasks}
    seen: set[str] = set()
    current = dependency_id
    while True:
        if current in seen:
            return False
        seen.add(current)
        dependency = by_id.get(current)
        if dependency is None:
            return False
        status = dependency.get("status")
        if status == "done":
            return True
        if status != "superseded":
            return False
        successor = dependency.get("superseded_by")
        if not isinstance(successor, str) or not re.fullmatch(r"AR-\d{4}", successor):
            return False
        current = successor


def require_role_admission(owner_id: str, required_role: str = "implementer") -> None:
    """Require a valid durable role assignment when role management is initialized."""
    if not (RUNTIME / "roles.json").exists():
        return
    role_module.require_admission(
        RUNTIME / "roles.json",
        ROOT / "examples/roles/role-registry.json",
        owner_id,
        required_role,
    )


def require_update_role_admission(kind: str, owner_id: str) -> None:
    if kind in {"update", "pause"}:
        require_role_admission(owner_id)


def require_done_admission(
    meta: Meta,
    tasks: list[Task] | None = None,
    policy: EvidencePolicy | None = None,
) -> None:
    if meta.get("status") != "in_progress":
        return
    error = done_admission_error(ROOT, meta, policy)
    if error:
        raise RuntimeError(error)
    if tasks is not None:
        hierarchy_error = open_child_error(meta, tasks)
        if hierarchy_error:
            raise RuntimeError(hierarchy_error)
    if error := change_drift.done_admission_error(meta):
        raise RuntimeError(error)
    task_metadata = [item for _, item, _ in tasks] if tasks is not None else []
    if error := (
        assumption_revalidation.admission_error(
            ROOT, Path(str(config()["projects_root"])), meta, task_metadata
        )
        if assumption_revalidation.needs_admission(meta)
        else None
    ):
        raise RuntimeError(error)


def require_release_admission(
    kind: str,
    status: str | None,
    meta: Meta,
    tasks: list[Task] | None = None,
    policy: EvidencePolicy | None = None,
) -> None:
    if kind == "release" and status == "done":
        require_done_admission(meta, tasks, policy)


def apply_claim(args: argparse.Namespace, meta: Meta, tasks: list[Task]) -> str:
    if (
        getattr(args, "_receipt_id", None) is not None
        and args.expected_revision != meta["task_revision"]
    ):
        raise RuntimeError(
            f"stale revision: expected {args.expected_revision}, current {meta['task_revision']}"
        )
    if args.lease_minutes <= 0:
        raise RuntimeError("lease must be positive")
    if meta.get("status") != "open":
        raise RuntimeError(f"{args.task} is not open")
    require_role_admission(str(args.owner))
    pending = [item for item in meta.get("depends_on", []) if not dependency_satisfied(item, tasks)]
    if pending:
        raise RuntimeError("unfinished dependencies: " + ", ".join(pending))
    try:
        transition_allowed(meta, "claim")
    except GateError as error:
        raise RuntimeError(str(error)) from error
    held = [
        item["id"]
        for _, item, _ in tasks
        if item.get("status") == "in_progress"
        and item.get("owner") == args.owner
        and item["id"] != args.task
    ]
    if held:
        raise RuntimeError(f"owner already holds {held[0]}")
    meta["owner"] = args.owner
    meta["status"] = "in_progress"
    attach_claim_process(args, meta)
    meta["claim_expires"] = (
        (dt.datetime.now(dt.UTC) + dt.timedelta(minutes=args.lease_minutes))
        .replace(microsecond=0)
        .isoformat()
    )
    return f"Claimed by {args.owner}."


def dirty_state_paths() -> list[str]:
    """Return ambiguous public changes."""
    result = run(
        [
            "git",
            "-C",
            str(ROOT),
            "status",
            "--porcelain=v1",
            "--untracked-files=all",
        ]
    )
    return result.stdout.splitlines()


def apply_promote(args: argparse.Namespace, meta: Meta, tasks: list[Task]) -> str:
    """Validate the sole planned-to-open transition before changing task state."""
    if args.expected_revision != meta["task_revision"]:
        raise RuntimeError(
            f"stale revision: expected {args.expected_revision}, current {meta['task_revision']}"
        )
    if meta.get("status") != "planned":
        raise RuntimeError(f"{args.task} is not planned")
    if meta.get("owner") or meta.get("claim_expires"):
        raise RuntimeError(f"{args.task} has active claim metadata")
    pending = [item for item in meta.get("depends_on", []) if not dependency_satisfied(item, tasks)]
    if pending:
        raise RuntimeError("unfinished dependencies: " + ", ".join(pending))
    try:
        transition_allowed(meta, "promote")
    except GateError as error:
        raise RuntimeError(str(error)) from error
    if not args.note.strip():
        raise RuntimeError("promotion note must not be empty")
    meta["status"] = "open"
    return str(args.note)


def _coherent_pause_session(record: Meta, task_id: str, revision: int) -> bool:
    step_state = record.get("step_state")
    return (
        record.get("task") == task_id
        and record.get("trigger") == "pause"
        and record.get("status") == "blocked"
        and isinstance(step_state, dict)
        and step_state.get("status") == "blocked"
        and step_state.get("task_revision") == revision
    )


def _session_for_reference(task_id: str, reference: str) -> Meta:
    match = SESSION_REFERENCE.fullmatch(reference)
    if match is None or match.group(1) != task_id:
        raise RuntimeError("session reference must use TASK@REVISION for the target task")
    revision = int(match.group(2))
    try:
        records = storage_backend().load_session_records(task_id)
        current = [item for item in records if item.get("task_revision") == revision]
        for item in current:
            validate_session_record(item)
    except ValueError as error:
        raise RuntimeError("session provenance is malformed") from error
    if not current:
        raise RuntimeError("no session snapshot at requested revision")
    if len(current) != 1:
        raise RuntimeError("session provenance is ambiguous")
    record = current[0]
    if not _coherent_pause_session(record, task_id, revision):
        raise RuntimeError("session reference is not a coherent paused snapshot")
    return record


def apply_pause(args: argparse.Namespace, meta: Meta) -> str:
    """Freeze an owned task and its lease at one exact revision."""
    if meta.get("owner") != args.owner:
        raise RuntimeError(f"{args.task} is owned by {meta.get('owner') or 'nobody'}")
    require_role_admission(str(args.owner))
    require_no_execution_reservation(meta)
    if args.expected_revision != meta["task_revision"]:
        raise RuntimeError(
            f"stale revision: expected {args.expected_revision}, current {meta['task_revision']}"
        )
    if meta.get("status") != "in_progress":
        raise RuntimeError(f"{args.task} is not in progress")
    if not args.note.strip():
        raise RuntimeError("pause note must not be empty")
    meta["status"] = "blocked"
    meta["owner"] = ""
    meta["claim_expires"] = ""
    meta.pop("claim_process", None)
    return str(args.note)


def apply_resume(args: argparse.Namespace, meta: Meta, _tasks: list[Task]) -> str:
    """Reopen one exact paused snapshot after an exact-revision CAS."""
    if args.expected_revision != meta["task_revision"]:
        raise RuntimeError(
            f"stale revision: expected {args.expected_revision}, current {meta['task_revision']}"
        )
    if meta.get("status") != "blocked":
        raise RuntimeError(f"{args.task} is not blocked")
    if meta.get("owner") or meta.get("claim_expires"):
        raise RuntimeError(f"{args.task} has active claim metadata")
    record = _session_for_reference(args.task, args.session)
    if record["task_revision"] != args.expected_revision:
        raise RuntimeError("session snapshot revision does not match expected revision")
    if not args.note.strip():
        raise RuntimeError("resume note must not be empty")
    meta["next_action"] = str(record["next_action"])
    meta["status"] = "open"
    return str(args.note)


def _blocked_provenance(task_id: str, revision: int) -> str:
    """Classify blocked state from its exact-revision session evidence."""
    try:
        records = storage_backend().load_session_records(task_id)
        current = [record for record in records if record.get("task_revision") == revision]
        for record in current:
            validate_session_record(record)
    except ValueError as error:
        raise RuntimeError("blocked provenance is malformed") from error
    if not current:
        return "external"
    if len(current) != 1:
        raise RuntimeError("blocked provenance is ambiguous")
    record = current[0]
    step_state = record.get("step_state")
    if (
        record.get("task") != task_id
        or record.get("trigger") != "pause"
        or record.get("status") != "blocked"
        or not isinstance(step_state, dict)
        or step_state.get("status") != "blocked"
        or step_state.get("task_revision") != revision
    ):
        raise RuntimeError("blocked provenance is ambiguous")
    return "pause"


def apply_unblock(args: argparse.Namespace, meta: Meta, _tasks: list[Task]) -> str:
    """Reopen one exact external-blocked revision without restoring a session."""
    if args.expected_revision != meta["task_revision"]:
        raise RuntimeError(
            f"stale revision: expected {args.expected_revision}, current {meta['task_revision']}"
        )
    if meta.get("status") != "blocked":
        raise RuntimeError(f"{args.task} is not blocked")
    if meta.get("owner") or meta.get("claim_expires"):
        raise RuntimeError(f"{args.task} has active claim metadata")
    if _blocked_provenance(args.task, int(meta["task_revision"])) != "external":
        raise RuntimeError("task is paused; use resume with its exact session reference")
    if not args.note.strip():
        raise RuntimeError("unblock note must not be empty")
    meta["status"] = "open"
    return str(args.note)


def current_recovery_session(records: list[Meta], revision: int) -> Meta | None:
    """Validate recovery snapshots and return only the exact-current record."""
    for session in records:
        validate_session_record(session)
        if session["task_revision"] > revision:
            raise RuntimeError("session snapshot revision is newer than the task")
    return next(
        (session for session in reversed(records) if session["task_revision"] == revision), None
    )


def apply_recover_expired(args: argparse.Namespace, meta: Meta, _tasks: list[Task]) -> str:
    if args.expected_revision != meta["task_revision"]:
        raise RuntimeError(
            f"stale revision: expected {args.expected_revision}, current {meta['task_revision']}"
        )
    if meta.get("status") != "in_progress" or not meta.get("owner"):
        raise RuntimeError(f"{args.task} does not have an active claim")
    try:
        expiry = parse_claim_expiry(meta.get("claim_expires"))
    except (TypeError, ValueError) as error:
        raise RuntimeError(f"{args.task} has invalid claim expiry") from error
    if expiry > dt.datetime.now(dt.UTC):
        raise RuntimeError(f"{args.task} claim has not expired")
    if not args.note.strip():
        raise RuntimeError("expired-claim recovery note must not be empty")
    retry_circuit.require_no_live_reservation(meta, now())
    records = storage_backend().load_session_records(args.task)
    previous_owner = str(meta["owner"])
    recovery_note = str(args.note)
    current_session = current_recovery_session(records, int(meta["task_revision"]))
    if current_session is not None:
        meta["next_action"] = str(current_session["next_action"])
    elif legacy_recovery_admitted(args, meta):
        recovery_note = "LEGACY_NO_IDENTITY_RECOVERY: " + recovery_note
    else:
        require_claimed_worker_absent(meta)
    meta["status"] = "open"
    meta["owner"] = ""
    meta["claim_expires"] = ""
    meta.pop("claim_process", None)
    return f"Recovered expired claim formerly owned by {previous_owner}. {recovery_note}"


def require_promotion_preflight(kind: str) -> None:
    """Reject a promotion before writes when its source checkout is ambiguous."""
    if kind not in ("promote", "resume", "unblock"):
        return
    errors = generated_view_errors(all_tasks())
    if errors:
        raise RuntimeError("promotion preflight failed:\n" + "\n".join(errors))
    if dirty_state_paths():
        raise RuntimeError("promotion requires a clean state repository")


def apply_accept(
    args: argparse.Namespace,
    meta: Meta,
    policy: EvidencePolicy | None,
    tasks: list[Task] | None = None,
) -> str:
    """Record acceptance with optional material-assumption freshness admission."""
    require_role_admission(str(args.owner))
    return apply_acceptance(
        ROOT,
        args,
        meta,
        policy,
        lambda: (
            assumption_revalidation.admission_error(
                ROOT,
                Path(str(config()["projects_root"])),
                meta,
                [item for _, item, _ in tasks] if tasks is not None else [],
            )
            if assumption_revalidation.needs_admission(meta)
            else None
        ),
    )


def apply_bind_spec(args: argparse.Namespace, meta: Meta, policy: EvidencePolicy | None) -> str:
    """Bind one validated immutable task spec to a previously unbound active task."""
    if meta.get("owner") != args.owner:
        raise RuntimeError(f"{args.task} is owned by {meta.get('owner') or 'nobody'}")
    require_role_admission(str(args.owner))
    if meta.get("status") != "in_progress":
        raise RuntimeError("bind-spec requires an active task")
    try:
        if parse_claim_expiry(meta.get("claim_expires")) <= dt.datetime.now(dt.UTC):
            raise RuntimeError("bind-spec requires an unexpired owner lease")
    except ValueError as error:
        raise RuntimeError("bind-spec requires an unexpired owner lease") from error
    if args.expected_revision != meta["task_revision"]:
        raise RuntimeError(
            f"stale revision: expected {args.expected_revision}, current {meta['task_revision']}"
        )
    if any(name in meta for name in ("spec_ref", "spec_revision", "spec_acceptance")):
        raise RuntimeError("bind-spec requires an unbound task spec")
    candidate = {**meta, "spec_ref": args.spec_ref, "spec_revision": args.spec_revision}
    errors = task_spec_errors(ROOT, candidate, policy)
    if errors:
        raise RuntimeError("bind-spec task spec is invalid: " + "; ".join(errors))
    meta["spec_ref"] = args.spec_ref
    meta["spec_revision"] = args.spec_revision
    return f"Bound task spec {args.spec_ref} revision {args.spec_revision}."


def valid_binding_branch(value: object) -> bool:
    """Validate a branch."""
    if not isinstance(value, str) or len(value) > 128 or value == "DETACHED":
        return False
    try:
        result = run(["git", "check-ref-format", "--branch", value], check=False)
        return result.returncode == 0 and result.stdout.strip() == value
    except SubprocessTimeoutError:
        return False


def valid_binding_worktree(value: object) -> bool:
    """Validate a direct worktree."""
    if not change_drift.valid_worktree_key(value):
        return False
    value = cast(str, value)
    try:
        settings = config()
        if value in {".", "..", str(settings.get("product_worktree", ""))}:
            return False
        if "projects_root" not in settings:
            return bool(settings)
        projects_root = settings["projects_root"]
        if not isinstance(projects_root, str) or not projects_root:
            return False
        root = Path(projects_root).resolve()
        candidate = root / value
        return not candidate.is_symlink() and inside(candidate, root)
    except KeyError:
        return False
    except RuntimeError:
        return not CONFIG.exists()


def binding_artifact_path(args: argparse.Namespace, kind: str) -> Path | None:
    name = "spec_ref" if kind == "bind-spec" else "envelope_ref"
    reference = getattr(args, name, None)
    if not isinstance(reference, str) or not reference or Path(reference).is_absolute():
        return None
    candidate = ROOT / reference
    if ".." in Path(reference).parts:
        return None
    try:
        info = candidate.lstat()
    except OSError:
        return None
    if candidate.is_symlink() or not stat.S_ISREG(info.st_mode):
        return None
    if info.st_size > 4194304:
        return None
    return candidate


def binding_identity_conflicts(args: argparse.Namespace, meta: Meta, tasks: list[Task]) -> bool:
    return any(
        other.get("id") != meta.get("id")
        and other.get("status") == "in_progress"
        and (other.get("branch") == args.branch or other.get("worktree_key") == args.worktree_key)
        for _, other, _ in tasks
    )


def require_active_binding_owner(args: argparse.Namespace, meta: Meta) -> None:
    if meta.get("owner") != args.owner:
        raise RuntimeError(f"{args.task} is owned by {meta.get('owner') or 'nobody'}")
    require_role_admission(str(args.owner))
    if meta.get("status") != "in_progress":
        raise RuntimeError("bind-worktree requires an active task")
    try:
        if parse_claim_expiry(meta.get("claim_expires")) <= dt.datetime.now(dt.UTC):
            raise RuntimeError("bind-worktree requires an unexpired owner lease")
    except ValueError as error:
        raise RuntimeError("bind-worktree requires an unexpired owner lease") from error
    if args.expected_revision != meta["task_revision"]:
        raise RuntimeError(
            f"stale revision: expected {args.expected_revision}, current {meta['task_revision']}"
        )


def require_bind_worktree_admission(
    args: argparse.Namespace, meta: Meta, tasks: list[Task]
) -> None:
    """Admit a first binding or a matching partial-legacy completion safely."""
    require_active_binding_owner(args, meta)
    if not valid_binding_branch(args.branch):
        raise RuntimeError("bind-worktree branch is invalid")
    if not valid_binding_worktree(args.worktree_key):
        raise RuntimeError("bind-worktree worktree key is invalid")
    if binding_identity_conflicts(args, meta, tasks):
        raise RuntimeError("bind-worktree identity conflicts with an active task")
    branch = meta.get("branch", "")
    worktree_key = meta.get("worktree_key", "")
    if branch and worktree_key:
        if branch == args.branch and worktree_key == args.worktree_key:
            raise IdempotentMutationError(
                f"Worktree {args.worktree_key} on branch {args.branch} is already bound."
            )
        raise RuntimeError("bind-worktree requires empty legacy worktree metadata")
    if branch:
        raise RuntimeError("bind-worktree requires an empty legacy branch")
    if worktree_key and worktree_key != args.worktree_key:
        raise RuntimeError("bind-worktree worktree key conflicts with declared legacy metadata")


def apply_bind_worktree(args: argparse.Namespace, meta: Meta, tasks: list[Task]) -> str:
    require_bind_worktree_admission(args, meta, tasks)
    require_no_execution_reservation(meta)
    meta.update(branch=args.branch, worktree_key=args.worktree_key)
    return f"Bound worktree {args.worktree_key} on branch {args.branch}."


def apply_repair_legacy_binding(args: argparse.Namespace, meta: Meta, _tasks: list[Task]) -> str:
    if __package__:
        from .legacy_binding_repair import repair
    else:
        from legacy_binding_repair import repair  # type: ignore[import-not-found,no-redef]

    return repair(args, meta)


def bind_envelope_candidate(args: argparse.Namespace, meta: Meta) -> tuple[Meta, str]:
    """Load an envelope and verify its identity against the exact task revision."""
    if not isinstance(meta.get("spec_ref"), str) or not isinstance(meta.get("spec_revision"), int):
        raise RuntimeError("bind-envelope requires a bound task spec")
    envelope, _actual_digest, found = execution_envelope.load(ROOT, args.envelope_ref)
    if found or envelope is None:
        raise RuntimeError("bind-envelope envelope is invalid: " + "; ".join(found))
    if execution_envelope.errors(envelope):  # defensive: loader already validates this.
        raise RuntimeError("bind-envelope envelope is invalid")
    if envelope["task"] != args.task or envelope["spec_ref"] != meta["spec_ref"]:
        raise RuntimeError("bind-envelope envelope task or spec does not match")
    if envelope["task_revision"] != meta["task_revision"]:
        raise RuntimeError("bind-envelope envelope task revision does not match")
    if envelope["spec_revision"] != meta["spec_revision"]:
        raise RuntimeError("bind-envelope envelope spec revision does not match")
    if args.envelope_revision != envelope["envelope_revision"]:
        raise RuntimeError("bind-envelope envelope revision does not match")
    return envelope, execution_envelope.canonical_digest(envelope)


def apply_bind_envelope(args: argparse.Namespace, meta: Meta) -> str:
    """Bind one immutable, validated execution envelope to an active task."""
    require_active_binding_owner(args, meta)
    require_no_execution_reservation(meta)
    envelope, actual_digest = bind_envelope_candidate(args, meta)
    existing = (
        meta.get("execution_envelope_ref"),
        meta.get("execution_envelope_revision"),
        meta.get("execution_envelope_task_revision"),
        meta.get("execution_envelope_digest"),
        meta.get("execution_envelope"),
    )
    requested = (
        args.envelope_ref,
        args.envelope_revision,
        meta["task_revision"],
        actual_digest,
        envelope,
    )
    if any(value is not None for value in existing):
        if existing == requested:
            raise IdempotentMutationError(
                f"Execution envelope {args.envelope_ref} is already bound."
            )
        raise RuntimeError("bind-envelope requires an unbound execution envelope")
    meta.update(
        execution_envelope_ref=args.envelope_ref,
        execution_envelope_revision=args.envelope_revision,
        execution_envelope_task_revision=meta["task_revision"],
        execution_envelope_digest=actual_digest,
        execution_envelope=envelope,
    )
    return f"Bound execution envelope {args.envelope_ref} revision {args.envelope_revision}."


def apply_replace_envelope(args: argparse.Namespace, meta: Meta) -> str:
    require_active_binding_owner(args, meta)
    require_no_execution_reservation(meta)
    return execution_envelope.replace_bound(meta, args, ROOT, now())


def apply_execution_start(args: argparse.Namespace, meta: Meta) -> str:
    return execution_lifecycle.start(_EXECUTION_RUNTIME, args, meta)


def apply_execution_finish(args: argparse.Namespace, meta: Meta) -> str:
    return execution_lifecycle.finish(_EXECUTION_RUNTIME, args, meta)


def apply_execution_result(args: argparse.Namespace, meta: Meta) -> str:
    return execution_lifecycle.result(_EXECUTION_RUNTIME, args, meta)


def apply_recover_execution(args: argparse.Namespace, meta: Meta) -> str:
    return execution_lifecycle.recover(_EXECUTION_RUNTIME, args, meta)


def apply_abandon_execution(args: argparse.Namespace, meta: Meta) -> str:
    return execution_lifecycle.abandon(_EXECUTION_RUNTIME, args, meta)


def require_owned_change_admission(
    args: argparse.Namespace,
    kind: str,
    meta: Meta,
    tasks: list[Task] | None,
    policy: EvidencePolicy | None,
) -> None:
    """Apply shared owner, role, fence, and release-admission checks."""
    if meta.get("owner") != args.owner:
        raise RuntimeError(f"{args.task} is owned by {meta.get('owner') or 'nobody'}")
    require_update_role_admission(kind, str(args.owner))
    if kind in {"release", "pause"}:
        require_no_execution_reservation(meta)
    if kind in {"heartbeat", "update"} and meta.get("execution_reservation") is not None:
        raise RuntimeError("EXECUTION_IN_PROGRESS: use the bound command completion path")
    require_release_admission(kind, getattr(args, "status", None), meta, tasks, policy)


def apply_owned_change(
    args: argparse.Namespace,
    kind: str,
    meta: Meta,
    tasks: list[Task] | None = None,
    policy: EvidencePolicy | None = None,
) -> str:
    require_owned_change_admission(args, kind, meta, tasks, policy)
    if kind == "heartbeat":
        if args.lease_minutes <= 0 or meta.get("status") != "in_progress":
            raise RuntimeError("heartbeat requires an active task and positive lease")
        require_optional_revision(args, meta)
        meta["claim_expires"] = (
            (dt.datetime.now(dt.UTC) + dt.timedelta(minutes=args.lease_minutes))
            .replace(microsecond=0)
            .isoformat()
        )
        return f"Heartbeat by {args.owner}."
    if kind == "release":
        try:
            transition_allowed(meta, "release")
        except GateError as error:
            raise RuntimeError(str(error)) from error
        meta["status"] = args.status
        meta["owner"] = ""
        meta["claim_expires"] = ""
        meta.pop("claim_process", None)
        return str(args.note)
    if args.expected_revision is not None and args.expected_revision != meta["task_revision"]:
        expected = args.expected_revision
        current = meta["task_revision"]
        raise RuntimeError(f"stale revision: expected {expected}, current {current}")
    if args.status is not None and args.status != "in_progress":
        raise RuntimeError("use release for a non-active status")
    for name in ("status", "priority", "summary", "next_action"):
        value = getattr(args, name, None)
        if value is not None:
            meta[name] = value
    al.carry_run_hold(args, kind, meta)
    return str(args.note)


def require_optional_revision(args: argparse.Namespace, meta: Meta) -> None:
    """Reject a supplied lifecycle fence without changing legacy owner-only calls."""
    requested = getattr(args, "expected_revision", None)
    if requested is not None and requested != meta["task_revision"]:
        raise RuntimeError(f"stale revision: expected {requested}, current {meta['task_revision']}")


def apply_checkpoint(args: argparse.Namespace, meta: Meta) -> str:
    """Attach the exact source commit to the task before recording its snapshot."""
    if meta.get("owner") != args.owner:
        raise RuntimeError(f"{args.task} is owned by {meta.get('owner') or 'nobody'}")
    if args.expected_revision != meta["task_revision"]:
        raise RuntimeError(
            f"stale revision: expected {args.expected_revision}, current {meta['task_revision']}"
        )
    require_role_admission(str(args.owner))
    meta["checkpoint_commit"] = str(args.source_commit)
    return f"Checkpointed source commit {args.source_commit}."


def apply_rollback(args: argparse.Namespace, meta: Meta) -> str:
    """Restore checkpoint metadata through one exact-revision task mutation."""
    checkpoint = cast(Meta, args.rollback_checkpoint)
    if meta.get("owner") or meta.get("claim_expires"):
        raise RuntimeError("rollback requires the target task to have no active claim")
    state = checkpoint["state"]
    if not isinstance(state, dict) or state.get("id") != meta.get("id"):
        raise RuntimeError("rollback checkpoint task does not match target task")
    if "short_title" in state:
        meta["short_title"] = state["short_title"]
    else:
        meta.pop("short_title", None)
    for field in (
        "priority",
        "summary",
        "next_action",
        "depends_on",
        "superseded_by",
        "spec_ref",
        "spec_revision",
        "spec_acceptance",
        "branch",
        "worktree_key",
        "checkpoint_commit",
    ):
        if field in state:
            meta[field] = state[field]
    meta["status"] = "open" if state.get("status") == "in_progress" else state.get("status")
    meta["owner"] = ""
    meta["claim_expires"] = ""
    meta.pop("claim_process", None)
    meta["checkpoint_commit"] = str(checkpoint["source_commit"])
    return (
        f"Restored checkpoint {checkpoint['name']} from source commit "
        f"{checkpoint['source_commit']}."
    )


def _artifact_values(values: list[str], label: str) -> tuple[ArtifactRef, ...]:
    result: list[ArtifactRef] = []
    for value in values:
        ref, separator, digest = value.partition("=")
        if not separator:
            raise RuntimeError(f"{label} must use REF=DIGEST")
        try:
            result.append(ArtifactRef(ref, digest))
        except GateError as error:
            raise RuntimeError(str(error)) from error
    return tuple(result)


def _human_session_values(args: argparse.Namespace, recorded_at: str) -> Meta | None:
    """Build one complete public-safe TUI session record or reject partial input."""
    session_id = getattr(args, "session_id", None)
    request_ref = getattr(args, "request_ref", None)
    activation = getattr(args, "activation", None)
    version = getattr(args, "tui_contract_version", None)
    if not any((session_id, request_ref, activation, version)):
        return None
    if getattr(args, "action", None) != "open":
        raise RuntimeError("human session metadata is valid only when opening a gate")
    if not all((session_id, request_ref, activation, version)):
        raise RuntimeError(
            "human session metadata requires --session-id, --request-ref, --activation, "
            "and --tui-contract-version"
        )
    return {
        "schema_version": "1.0",
        "session_id": session_id,
        "request_ref": request_ref,
        "activation": activation,
        "status": "presenting",
        "task_revision": int(args.expected_revision),
        "tui_contract_version": version,
        "opened_at": recorded_at,
    }


def apply_gate(args: argparse.Namespace, meta: Meta) -> str:
    """Record one typed interaction event as the task's next revision."""
    try:
        try:
            stage: GateStage | StageGate = GateStage(str(args.stage))
        except ValueError as error:
            try:
                stage = StageGate(str(args.stage))
            except ValueError:
                raise GateError("unknown interaction gate stage") from error
        recorded_at = now()
        event = InteractionEvent(
            task_id=str(meta["id"]),
            task_revision=int(args.expected_revision),
            stage=stage,
            action=str(args.action),
            disposition=str(args.disposition),
            before=_artifact_values(args.before, "--before"),
            after=_artifact_values(args.after, "--after"),
            public_ref=str(args.public_ref),
            recorded_at=recorded_at,
        )
        return apply_event(meta, event, _human_session_values(args, recorded_at))
    except (GateError, ValueError) as error:
        raise RuntimeError(str(error)) from error


def apply_recover_expired_transition(
    args: argparse.Namespace, meta: Meta, tasks: list[Task]
) -> str:
    require_no_execution_reservation(meta)
    return apply_recover_expired(args, meta, tasks)


def lifecycle_transition_handler(
    args: argparse.Namespace,
    kind: str,
    meta: Meta,
    tasks: list[Task],
    policy: EvidencePolicy | None,
) -> Callable[[], str] | None:
    handlers: dict[str, Callable[[], str]] = {
        "claim": lambda: apply_claim(args, meta, tasks),
        "promote": lambda: apply_promote(args, meta, tasks),
        "pause": lambda: apply_pause(args, meta),
        "resume": lambda: apply_resume(args, meta, tasks),
        "unblock": lambda: apply_unblock(args, meta, tasks),
        "recover-expired": lambda: apply_recover_expired_transition(args, meta, tasks),
        "recover-execution": lambda: apply_recover_execution(args, meta),
        "abandon-execution": lambda: apply_abandon_execution(args, meta),
        "gate": lambda: apply_gate(args, meta),
        "change-drift": lambda: change_drift.apply(
            args,
            meta,
            Path(str(config()["projects_root"])),
            now(),
            str(config().get("product_worktree", "")),
        ),
        "assumption": lambda: assumption_revalidation.apply(
            ROOT, Path(str(config()["projects_root"])), args, meta, [item for _, item, _ in tasks]
        ),
        "retry-circuit": lambda: retry_circuit.apply(args, meta, now()),
        "retry-circuit-reserve": lambda: retry_circuit.apply_reserve(args, meta, now()),
        "retry-circuit-resolve": lambda: retry_circuit.apply_resolve(args, meta, now()),
        "checkpoint": lambda: apply_checkpoint(args, meta),
        "rollback": lambda: apply_rollback(args, meta),
        "accept": lambda: apply_accept(args, meta, policy),
        "bind-spec": lambda: apply_bind_spec(args, meta, policy),
        "bind-worktree": lambda: apply_bind_worktree(args, meta, tasks),
        "repair-legacy-binding": lambda: apply_repair_legacy_binding(args, meta, tasks),
        "repair-predicate-ledger": lambda: plr.repair(ROOT, args, meta, policy),
        "bind-envelope": lambda: apply_bind_envelope(args, meta),
        "replace-envelope": lambda: apply_replace_envelope(args, meta),
        "execution-start": lambda: apply_execution_start(args, meta),
        "execution-result": lambda: apply_execution_result(args, meta),
        "execution-finish": lambda: apply_execution_finish(args, meta),
    }
    if kind.startswith("autonomy-limits"):
        return lambda: al.transition(require_active_binding_owner, args, meta, now())
    return handlers.get(kind)


def apply_transition(
    args: argparse.Namespace,
    kind: str,
    meta: Meta,
    tasks: list[Task],
    policy: EvidencePolicy | None = None,
) -> str:
    handler = lifecycle_transition_handler(args, kind, meta, tasks, policy)
    if handler is not None:
        return handler()
    return apply_owned_change(args, kind, meta, tasks, policy)


def rendered_task_views(tasks: list[Task]) -> dict[Path, str]:
    views = {ROOT / "CURRENT.md": render_current(tasks)}
    if project_settings()["status_view"]:
        views.update(
            {ROOT / relative: content for relative, content in render_status_views(tasks).items()}
        )
    return views


def safe_generated_view_inode(info: os.stat_result) -> bool:
    return (
        stat.S_ISREG(info.st_mode)
        and info.st_nlink == 1
        and info.st_uid == os.geteuid()
        and stat.S_IMODE(info.st_mode) == 0o600
    )


def unchanged_generated_view(path: Path, content: str) -> bool:
    """Avoid an fsync only for an ordinary, already-correct projection file."""
    try:
        parent = path.parent.lstat()
        if not stat.S_ISDIR(parent.st_mode):
            return False
        descriptor = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    except OSError:
        return False
    try:
        found = os.fstat(descriptor)
        if not safe_generated_view_inode(found):
            return False
        expected = content.encode("utf-8")
        with os.fdopen(descriptor, "rb", closefd=False) as stream:
            if stream.read(len(expected) + 1) != expected:
                return False
        # Replaced pathnames must be re-read from the current inode.
        try:
            current_parent = path.parent.lstat()
            current = path.lstat()
        except OSError:
            return False
        return (
            stat.S_ISDIR(current_parent.st_mode)
            and (current_parent.st_dev, current_parent.st_ino) == (parent.st_dev, parent.st_ino)
            and (current.st_dev, current.st_ino) == (found.st_dev, found.st_ino)
            and safe_generated_view_inode(current)
        )
    finally:
        os.close(descriptor)


def write_status_views(views: dict[str, str]) -> None:
    """Atomically replace the root status index and remove obsolete shards."""
    expected_paths = {ROOT / relative for relative in views}
    for path in generated_paths():
        if path not in expected_paths and (
            path.name == "STATUS.md" or path.parent.name == "status"
        ):
            path.unlink(missing_ok=True)
    for relative, content in views.items():
        target = ROOT / relative
        if not unchanged_generated_view(target, content):
            atomic(target, content)


def write_rendered_task_views(views: dict[Path, str]) -> None:
    """Write all task views while pruning obsolete status shards."""
    status_views = {
        str(target.relative_to(ROOT)): content
        for target, content in views.items()
        if target.name == "STATUS.md" or target.parent.name == "status"
    }
    write_status_views(status_views)
    for target, content in views.items():
        if (
            target.name != "STATUS.md"
            and target.parent.name != "status"
            and not unchanged_generated_view(target, content)
        ):
            atomic(target, content)


def git_session_record(
    args: argparse.Namespace,
    kind: str,
    meta: Meta,
    before: dict[Path, str | None],
) -> Meta | None:
    """Prepare a Git-backed session record and its rollback path."""
    trigger = str(getattr(args, "_session_trigger", kind))
    if not (
        (kind == "update" and trigger in {"update", "run"})
        or (kind == "pause" and trigger == "pause")
    ):
        return None
    try:
        record = build_session_record(meta, trigger, str(meta["updated_at"]))
    except ValueError as error:
        raise RuntimeError(f"state file exceeds 200 KiB: {error}") from error
    record_path = session_path(ROOT, str(meta["id"]))
    before[record_path] = record_path.read_text() if record_path.exists() else None
    return record


def require_project_settings_unchanged(settings: Meta) -> None:
    if project_settings() != settings:
        raise RuntimeError("PROJECT_CONFIG_CHANGED: retry after a stable project profile")


def fast_receipt_id(args: argparse.Namespace, kind: str) -> str | None:
    """Validate receipt-only mutation arguments before selecting an authority backend."""
    receipt_id = getattr(args, "_receipt_id", None)
    if receipt_id is None:
        return None
    if (
        kind not in {"claim", "heartbeat", "promote", "update"}
        or not isinstance(receipt_id, str)
        or not re.fullmatch(r"[0-9a-f]{32}", receipt_id)
        or getattr(args, "expected_revision", None) is None
    ):
        raise RuntimeError("invalid fast receipt mutation")
    return receipt_id


def persist_git_mutation(
    args: argparse.Namespace,
    kind: str,
    receipt_id: str | None,
    path: Path,
    meta: Meta,
    body: str,
    before: dict[Path, str | None],
    selected_policy: EvidencePolicy,
    session_record: Meta | None,
    checkpoint_record: Meta | None,
    retained_paths: tuple[Path, ...] = (),
) -> None:
    """Write, validate, commit, and retain one locked Git mutation transaction."""
    committed = False
    try:
        if session_record is not None:
            append_session_record(ROOT, session_record)
        if checkpoint_record is not None:
            append_checkpoint(ROOT, checkpoint_record)
        write_task(path, meta, body)
        view_tasks = all_tasks()
        view_settings = project_settings()
        views = rendered_task_views(view_tasks)
        require_project_settings_unchanged(view_settings)
        write_rendered_task_views(views)
        require_policy_unchanged(ROOT, selected_policy)
        errors = mutation_errors(
            path,
            before,
            selected_policy,
            rendered_snapshot=(view_tasks, views, view_settings),
        )
        if errors:
            raise RuntimeError("\n".join(errors))
        for target in generated_paths():
            before.setdefault(target, None)
        committed = commit_persisted_mutation(
            args, kind, receipt_id, before, meta, retained_paths=retained_paths
        )
        if receipt_id is None:
            push_replica()
    except Exception:
        if not committed:
            restore_paths(before)
        raise


def commit_persisted_mutation(
    args: argparse.Namespace,
    kind: str,
    receipt_id: str | None,
    before: dict[Path, str | None],
    meta: Meta,
    *,
    retained_paths: tuple[Path, ...] = (),
) -> bool:
    """Commit a validated mutation and expose receipt-only local evidence."""
    message = f"chore(state): {kind} {args.task}"
    if receipt_id is not None:
        message += f"\n\nHandoffctl-Receipt: {receipt_id}"
    paths = changed_paths(before, include_deleted=True)
    for path in retained_paths:
        if path.exists() and path not in paths:
            paths.append(path)
    committed = commit(message, paths)
    if receipt_id is not None and not committed:
        raise RuntimeError("fast receipt mutation produced no signed commit")
    if receipt_id is not None:
        args._committed_oid = current_commit_oid()
        args._committed_revision = meta["task_revision"]
    return committed


def mutate(args: argparse.Namespace, kind: str, policy: EvidencePolicy | None = None) -> str | None:
    if kind not in {
        "release",
        "pause",
        "recover-expired",
        "recover-execution",
        "abandon-execution",
    }:
        return _mutate_fenced(args, kind, policy)
    with task_execution_locked(args.task, exclusive=True, phase="task_lifecycle_mutation"):
        return _mutate_fenced(args, kind, policy)


def _mutate_fenced(
    args: argparse.Namespace, kind: str, policy: EvidencePolicy | None = None
) -> str | None:
    receipt_id = fast_receipt_id(args, kind)
    if backend_selection()["backend"] == "sqlite":
        if receipt_id is not None:
            raise RuntimeError("fast receipts require Git authority")
        try:
            return mutate_sqlite(args, kind, policy)
        except IdempotentMutationError as replay:
            return str(replay)
    with locked(phase="git_mutate"):
        if backend_selection()["backend"] != "git":
            raise RuntimeError("BACKEND_CHANGED: retry using the selected backend")
        sync_replica_before_write()
        selected_policy = policy_snapshot(policy)
        path, meta, body = locate(args.task)
        require_promotion_preflight(kind)
        before: dict[Path, str | None] = {path: path.read_text()}
        before.update(
            {
                target: target.read_text() if target.exists() else None
                for target in generated_paths()
            }
        )
        retained_paths = tuple(
            path for path in (binding_artifact_path(args, kind),) if path is not None
        )
        try:
            note = apply_transition(args, kind, meta, all_tasks(), selected_policy)
        except IdempotentMutationError as replay:
            return str(replay)
        meta["task_revision"] += 1
        meta["updated_at"] = now()
        session_record = git_session_record(args, kind, meta, before)
        checkpoint_record = None
        if kind == "checkpoint":
            checkpoint_record = build_checkpoint(
                meta, body, str(args.source_commit), str(meta["updated_at"])
            )
            record_path = checkpoint_path(ROOT, str(meta["id"]))
            before[record_path] = record_path.read_text() if record_path.exists() else None
        if note:
            body += (
                "\n"
                + textwrap.fill(
                    f"{meta['updated_at']}: {note}",
                    width=100,
                    initial_indent="- ",
                    subsequent_indent="  ",
                    break_long_words=False,
                    break_on_hyphens=False,
                )
                + "\n"
            )
        persist_git_mutation(
            args,
            kind,
            receipt_id,
            path,
            meta,
            body,
            before,
            selected_policy,
            session_record,
            checkpoint_record,
            retained_paths,
        )
    return None


def _transition_note(body: str, note: str, at: str) -> str:
    if not note:
        return body
    return (
        body
        + "\n"
        + textwrap.fill(
            f"{at}: {note}",
            width=100,
            initial_indent="- ",
            subsequent_indent="  ",
            break_long_words=False,
            break_on_hyphens=False,
        )
        + "\n"
    )


def mutate_sqlite(
    args: argparse.Namespace, kind: str, policy: EvidencePolicy | None = None
) -> str | None:
    """Linearize a lifecycle mutation at SQLite's committed CAS update."""
    selected_policy = policy_snapshot(policy)
    backend = mutating_sqlite_backend()
    initial = backend.load_tasks()
    selected = next((task for task in initial if task[1]["id"] == args.task), None)
    if selected is None:
        raise RuntimeError(f"unknown task {args.task}")
    current = int(selected[1]["task_revision"])
    requested = getattr(args, "expected_revision", None)
    expected = current if requested is None else int(requested)
    at = now()

    def transition(meta: Meta, tasks: list[Task]) -> tuple[str, str]:
        require_policy_unchanged(ROOT, selected_policy)
        note = apply_transition(args, kind, meta, tasks, selected_policy)
        validated = al.next_revision_projection(meta)
        candidate = [
            (path, validated if item["id"] == args.task else item, text)
            for path, item, text in tasks
        ]
        errors = (
            basic_task_errors(selected[0], validated, selected_policy)
            + graph_errors(candidate)
            + hierarchy_errors(candidate)
            + supersession_errors(candidate)
        )
        if errors:
            raise RuntimeError("transition validation failed:\n" + "\n".join(errors))
        require_policy_unchanged(ROOT, selected_policy)
        return note, _transition_note(selected[2], note, at)

    trigger = str(getattr(args, "_session_trigger", kind))
    session_factory = None
    if (kind == "update" and trigger in {"update", "run"}) or (
        kind == "pause" and trigger == "pause"
    ):

        def make_session_record(updated: Meta) -> Meta:
            return build_session_record(updated, trigger, at)

        session_factory = make_session_record
    checkpoint_factory = None
    if kind == "checkpoint":

        def make_checkpoint_record(updated: Meta) -> Meta:
            return build_checkpoint(updated, selected[2], str(args.source_commit), at)

        checkpoint_factory = make_checkpoint_record
    backend.mutate(
        args.task,
        expected,
        kind,
        at,
        transition,
        session_factory=session_factory,
        checkpoint_factory=checkpoint_factory,
    )
    try:
        export_sqlite_projections(selected_policy)
    except Exception as error:
        raise StorageCommittedError(
            f"SQLITE_COMMITTED_EXPORT_FAILED: task={args.task}; revision={expected + 1}; {error}"
        ) from error
    return None


def cmd_render_status(*, check: bool) -> None:
    """Render STATUS.md or fail if its checked-in form is stale."""
    if not project_settings()["status_view"]:
        raise RuntimeError("STATUS.md generation is disabled by .handoffctl.json")
    with locked(exclusive=not check):
        try:
            policy = evidence_policy(ROOT)
        except RuntimeError as error:
            raise RuntimeError(f"task-spec policy invalid: {error}") from error
        task_errors = [
            error
            for path, meta, _body in all_tasks()
            for error in basic_task_errors(path, meta, policy)
        ]
        if task_errors:
            raise RuntimeError("task-spec validation failed: " + "; ".join(task_errors))
        expected = render_status_views(all_tasks())
        if check:
            if status_projection_errors(expected):
                raise RuntimeError("STATUS.md differs from generated tasks")
            return
        write_status_views(expected)


def role_doctor_errors() -> list[str]:
    """Validate active task owners against the durable role store when initialized."""
    state = RUNTIME / "roles.json"
    if not state.exists():
        return []
    owners = [
        (str(meta["owner"]), "implementer")
        for _path, meta, _body in all_tasks()
        if meta.get("status") == "in_progress" and isinstance(meta.get("owner"), str)
    ]
    return role_module.doctor_errors(state, owners)


def doctor_checks(*, live: bool, sqlite: bool, live_state: State | None) -> list[str]:
    """Validate one authority view and its optional pre-scanned live input."""
    errors = validate(live=live, live_state=live_state)
    errors.extend(role_doctor_errors())
    if sqlite:
        errors.extend(SQLiteBackend(DATABASE, project_binding(), TASKS).integrity_errors())
    if REPLICA_BLOCKED.exists():
        try:
            blocked = json.loads(REPLICA_BLOCKED.read_text())
            code = str(blocked.get("code", "REPLICA_BLOCKED"))
        except (OSError, json.JSONDecodeError, AttributeError):
            code = "REPLICA_BLOCKED"
        errors.append(f"{code}: replica reconciliation requires operator review")
    return errors


def git_doctor_checks(*, live: bool) -> list[str]:
    """Read one Git authority view while observing live data outside the lock."""
    if not live:
        with locked(exclusive=False, phase="doctor"):
            return doctor_checks(live=False, sqlite=False, live_state=None)
    for _ in range(3):
        ticket = published_observation_ticket()
        scan_config = config() if CONFIG.exists() else None
        scan_binding = project_binding()
        live_state = project_scan() if live else None
        with locked(exclusive=False, phase="doctor"):
            if backend_selection()["backend"] != "git":
                raise RuntimeError("BACKEND_CHANGED: retry doctor")
            if (config() if CONFIG.exists() else None) != scan_config:
                raise RuntimeError("OBSERVATION_INPUT_CHANGED: retry doctor")
            if project_binding() != scan_binding:
                raise RuntimeError("OBSERVATION_INPUT_CHANGED: retry doctor")
            errors = doctor_checks(live=live, sqlite=False, live_state=live_state)
            # Retry only stale live comparisons.
            if (
                ticket != published_observation_ticket()
                and errors
                and all(
                    error in {"PROJECT_STATE.md is stale", "WORKTREES.md is stale"}
                    for error in errors
                )
            ):
                continue
            return errors
    return ["OBSERVATION_CHANGED: retry doctor"]


def cmd_doctor(*, live: bool) -> int:
    """Validate one consistent Git authority view without locking its live scan."""
    sqlite = backend_selection()["backend"] == "sqlite"
    sqlite_live = CONFIG.exists() and bool(config().get("github_repository"))
    check_live = live and (not sqlite or sqlite_live)
    if sqlite:
        errors = doctor_checks(live=check_live, sqlite=True, live_state=None)
    else:
        errors = git_doctor_checks(live=check_live)
    if errors:
        print("\n".join("ERROR: " + value for value in errors))
        return 1
    print(
        "OK: structure, references, privacy, generated views"
        + (" and live state" if live else "")
        + " are consistent"
    )
    return 0


def cmd_snapshot(task_id: str | None = None) -> None:
    sqlite = backend_selection()["backend"] == "sqlite"
    sqlite_live = CONFIG.exists() and bool(config().get("github_repository"))
    for _ in range(3):
        ticket = published_observation_ticket() if not sqlite else None
        live_state = project_scan() if not sqlite or sqlite_live else None
        with locked(exclusive=False, phase="snapshot"):
            if (backend_selection()["backend"] == "sqlite") != sqlite:
                raise RuntimeError("BACKEND_CHANGED: retry snapshot")
            if not sqlite and ticket != published_observation_ticket():
                continue
            errors = validate(live=not sqlite or sqlite_live, live_state=live_state)
            if errors:
                raise RuntimeError("snapshot refused:\n" + "\n".join(errors))
            print_snapshot_under_lock(task_id, sqlite)
            return
    raise RuntimeError("OBSERVATION_CHANGED: retry snapshot")


def print_snapshot_under_lock(task_id: str | None, sqlite: bool) -> None:
    """Emit one validated snapshot while the caller holds the shared lock."""
    if sqlite:
        print("STORAGE_BACKEND=sqlite")
    else:
        print("STATE_COMMIT=" + run(["git", "-C", str(ROOT), "rev-parse", "HEAD"]).stdout.strip())
    print((ROOT / "CURRENT.md").read_text(), end="")
    if task_id is not None:
        if sqlite:
            records = storage_backend().load_session_records(task_id)
            record = records[-1] if records else None
        else:
            record = latest_session(ROOT, task_id)
        if record is None:
            raise RuntimeError(f"no session snapshot for {task_id}")
        validate_session_record(record)
        task = next((meta for _, meta, _ in all_tasks() if meta.get("id") == task_id), None)
        if task is None:
            raise RuntimeError(f"unknown task {task_id}")
        next_step = next_unmet_predicate(ROOT, task)
        if next_step is not None:
            print("NEXT_UNMET_STEP=" + next_step)
        print("SESSION_SNAPSHOT=" + json.dumps(record, sort_keys=True, separators=(",", ":")))


def _cmd_analytics(label: str) -> None:
    """Print one SQLite-only deterministic analytics projection."""
    if backend_selection()["backend"] != "sqlite":
        raise RuntimeError(f"{label} requires the SQLite authority")
    with locked(exclusive=False):
        print(encode_metrics(build_metrics(all_tasks())), end="")


def cmd_board() -> None:
    _cmd_analytics("board")


def cmd_metrics() -> None:
    _cmd_analytics("metrics")


def cmd_checkpoint(args: argparse.Namespace) -> None:
    """Capture a bounded task checkpoint before mutating task authority."""
    if invocation_worktree() is not None:
        args.source_commit = run(["git", "rev-parse", "HEAD"]).stdout.strip()
    else:
        args.source_commit = run(["git", "-C", str(ROOT), "rev-parse", "HEAD"]).stdout.strip()
    mutate(args, "checkpoint")


def _directive_claim_expiry(minutes: int) -> str:
    if minutes <= 0:
        raise RuntimeError("directive lease must be positive")
    return (
        (dt.datetime.now(dt.UTC) + dt.timedelta(minutes=minutes)).replace(microsecond=0).isoformat()
    )


def _directive_claim_is_live(record: Meta, owner: str) -> None:
    if str(record.get("owner")) != owner:
        raise RuntimeError(f"directive is owned by {record.get('owner') or 'nobody'}")
    try:
        expires = dt.datetime.fromisoformat(str(record["claim_expires"]))
    except ValueError as error:
        raise RuntimeError("directive claim expiry is invalid") from error
    if expires.tzinfo is None or expires <= dt.datetime.now(dt.UTC):
        raise RuntimeError("directive claim has expired")


def _commit_directive(record: Meta) -> None:
    append_directive(ROOT, record)
    if not commit(f"chore(state): directive {record['directive_id']}", [directive_path(ROOT)]):
        raise RuntimeError("directive record was not committed")
    push_replica()


def _create_directive(args: argparse.Namespace, records: list[Meta]) -> Meta:
    if any(item["directive_id"] == args.directive_id for item in records):
        raise RuntimeError(f"directive already exists: {args.directive_id}")
    return build_directive(
        args.directive_id,
        authority=args.authority,
        precedence=args.precedence,
        scope={"roles": args.role_scope, "tasks": args.task_scope},
        statement=args.statement,
        recorded_at=now(),
        owner=args.owner,
        claim_expires=_directive_claim_expiry(args.lease_minutes),
        guidance_ref=args.guidance_ref,
    )


def _transition_directive(args: argparse.Namespace, records: list[Meta]) -> Meta:
    current = next((item for item in records if item["directive_id"] == args.directive_id), None)
    if current is None:
        raise RuntimeError(f"unknown directive: {args.directive_id}")
    if int(current["revision"]) != args.expected_revision:
        raise RuntimeError(
            f"stale directive revision: expected {args.expected_revision}, "
            f"current {current['revision']}"
        )
    _directive_claim_is_live(current, args.owner)
    candidate = dict(current)
    candidate["revision"] = int(current["revision"]) + 1
    candidate["updated_at"] = now()
    candidate["guidance_ref"] = args.guidance_ref or str(current["guidance_ref"])
    candidate["lifecycle"] = _directive_lifecycle(args.action, candidate, records)
    if candidate["lifecycle"] != "active":
        candidate["owner"] = ""
        candidate["claim_expires"] = ""
    return candidate


def _directive_lifecycle(action: str, candidate: Meta, records: list[Meta]) -> str:
    if action == "activate":
        candidate["lifecycle"] = "active"
        conflicts = conflicting_directives(records, candidate)
        if conflicts and candidate["guidance_ref"] != "AR-0053":
            raise RuntimeError("directive conflict requires guidance escalation AR-0053")
        return "escalated" if conflicts else "active"
    if action == "escalate":
        if candidate["guidance_ref"] != "AR-0053":
            raise RuntimeError("directive escalation requires guidance AR-0053")
        return "escalated"
    if action == "supersede":
        return "superseded"
    if action == "revoke":
        return "revoked"
    raise RuntimeError("unknown directive action")


def cmd_directive(args: argparse.Namespace) -> None:
    """Create, list and CAS-transition board-authorized directives."""
    if backend_selection()["backend"] != "git":
        raise RuntimeError("directive commands currently require the Git authority backend")
    with locked():
        sync_replica_before_write()
        records = latest_directives(ROOT)
        if args.directive_action == "list":
            selected = [
                item
                for item in records
                if not args.lifecycle or item["lifecycle"] == args.lifecycle
            ]
            print(json.dumps(selected, sort_keys=True, separators=(",", ":")))
            return
        record = (
            _create_directive(args, records)
            if args.directive_action == "create"
            else _transition_directive(args, records)
        )
        _commit_directive(record)
        print(json.dumps(record, sort_keys=True, separators=(",", ":")))


def _rollback_commit(root: Path, record: Meta, message: str) -> None:
    """Persist one rollback journal state before returning to the caller."""
    del message
    append_record(root, record)
    if not commit(f"chore(state): rollback {record['checkpoint']}", [rollback_path(root)]):
        raise RuntimeError("rollback journal state was not committed")
    push_replica()


def _product_commit_for_checkpoint(product: Path, source_commit: str) -> str:
    """Require a clean descendant product checkout and return its current head."""
    status = run(
        ["git", "-C", str(product), "status", "--porcelain=v1", "--untracked-files=all"]
    ).stdout
    if status:
        raise RuntimeError("rollback requires a clean product checkout")
    run(["git", "-C", str(product), "cat-file", "-e", f"{source_commit}^{{commit}}"])
    current = run(["git", "-C", str(product), "rev-parse", "HEAD"]).stdout.strip()
    if current != source_commit:
        ancestor = run(
            ["git", "-C", str(product), "merge-base", "--is-ancestor", source_commit, current],
            check=False,
        )
        if ancestor.returncode != 0:
            raise RuntimeError("rollback source commit is not an ancestor of product HEAD")
    return current


def _revert_product(product: Path, source_commit: str, current_commit: str) -> str:
    """Create one signed product revert, leaving conflicts fail-closed."""
    if current_commit != source_commit:
        run(
            [
                "git",
                "-C",
                str(product),
                "revert",
                "--no-commit",
                f"{source_commit}..{current_commit}",
            ],
            capture=False,
        )
    if current_commit == source_commit:
        return current_commit
    run(
        [
            "git",
            "-C",
            str(product),
            "commit",
            "-s",
            "-m",
            f"revert: restore coordinator checkpoint {source_commit[:12]}",
        ],
        capture=False,
    )
    return run(["git", "-C", str(product), "rev-parse", "HEAD"]).stdout.strip()


def _rollback_target(args: argparse.Namespace) -> tuple[Meta, Path, str, Meta | None]:
    """Validate the checkpoint, product ancestry and any prior operation."""
    if backend_selection()["backend"] != "git":
        raise RuntimeError("rollback currently requires the Git authority backend")
    with locked():
        if dirty_state_paths():
            raise RuntimeError("rollback requires a clean state repository")
        checkpoint = next(
            (item for item in load_checkpoints(ROOT) if item["name"] == args.checkpoint),
            None,
        )
        if checkpoint is None:
            raise RuntimeError(f"unknown checkpoint {args.checkpoint}")
        previous = latest_for_checkpoint(ROOT, args.checkpoint)
        if previous is not None and previous["status"] == "rollback_completed":
            raise RuntimeError("checkpoint rollback is already completed")
        reconcile_requested = bool(getattr(args, "reconcile", False))
        if (
            previous is not None
            and previous["status"] in {"restore_started", "ambiguous"}
            and not reconcile_requested
        ):
            raise RuntimeError("checkpoint rollback requires explicit ambiguous recovery")
        _, product = configured_product_checkout(project_binding())
        current_commit = _product_commit_for_checkpoint(product, str(checkpoint["source_commit"]))
    return checkpoint, product, current_commit, previous


def _start_rollback(
    args: argparse.Namespace,
    checkpoint: Meta,
    product: Path,
    current_commit: str,
    previous: Meta | None,
) -> tuple[Meta, bool]:
    """Durably authorize a fresh restore or an exact-head reconciliation."""
    del product
    reconcile_requested = bool(getattr(args, "reconcile", False))
    skip_product = False
    if previous is not None and reconcile_requested:
        if previous["rollback_commit"]:
            if current_commit != previous["rollback_commit"]:
                raise RuntimeError("reconcile product head does not match rollback commit")
            skip_product = True
        elif current_commit != previous["current_commit"]:
            raise RuntimeError("reconcile product head changed during ambiguous rollback")
        started = build_record(
            checkpoint,
            current_commit,
            now(),
            status="restore_started",
            operation_id=str(previous["operation_id"]),
            rollback_commit=str(previous["rollback_commit"]),
            revision=int(previous["revision"]) + 1,
        )
        with locked():
            _rollback_commit(ROOT, started, "restore_started")
        return started, skip_product
    with locked():
        skip_product = False
        record = build_record(checkpoint, current_commit, now())
        _rollback_commit(ROOT, record, "planned")
        started = build_record(
            checkpoint,
            current_commit,
            now(),
            status="restore_started",
            operation_id=str(record["operation_id"]),
            revision=2,
        )
        _rollback_commit(ROOT, started, "restore_started")
    return started, skip_product


def cmd_rollback(args: argparse.Namespace) -> None:
    """Restore one checkpoint with a durable journal and coordinated Git revert."""
    policy = evidence_policy(ROOT)
    checkpoint, product, current_commit, previous = _rollback_target(args)
    require_policy_unchanged(ROOT, policy)
    started, skip_product = _start_rollback(args, checkpoint, product, current_commit, previous)
    try:
        require_policy_unchanged(ROOT, policy)
        rollback_commit = (
            str(started["rollback_commit"])
            if skip_product
            else _revert_product(product, str(checkpoint["source_commit"]), current_commit)
        )
    except Exception as error:
        ambiguous = build_record(
            checkpoint,
            current_commit,
            now(),
            status="ambiguous",
            operation_id=str(started["operation_id"]),
            revision=int(started["revision"]) + 1,
        )
        with locked():
            _rollback_commit(ROOT, ambiguous, "ambiguous")
        raise RuntimeError("rollback product effect failed; recovery is required") from error
    args.task = str(checkpoint["task"])
    args.expected_revision = int(
        next(item[1] for item in all_tasks() if item[1]["id"] == args.task)["task_revision"]
    )
    args.rollback_checkpoint = checkpoint
    try:
        require_policy_unchanged(ROOT, policy)
        mutate(args, "rollback", policy)
    except Exception as error:
        ambiguous = build_record(
            checkpoint,
            current_commit,
            now(),
            status="ambiguous",
            operation_id=str(started["operation_id"]),
            rollback_commit=rollback_commit,
            revision=int(started["revision"]) + 1,
        )
        with locked():
            _rollback_commit(ROOT, ambiguous, "ambiguous")
        raise RuntimeError("rollback state publication failed; recovery is required") from error
    completed = build_record(
        checkpoint,
        current_commit,
        now(),
        status="rollback_completed",
        operation_id=str(started["operation_id"]),
        rollback_commit=rollback_commit,
        revision=int(started["revision"]) + 1,
    )
    with locked():
        _rollback_commit(ROOT, completed, "rollback_completed")
    reconcile(do_commit=True, push=True, policy=policy)


def require_active_owner(task_id: str, owner: str) -> EvidencePolicy:
    """Fence wrapped commands with a live claim before external effects."""
    with locked(exclusive=False, phase="run_preflight"):
        _, meta, _ = locate(task_id)
        try:
            policy = evidence_policy(ROOT)
        except RuntimeError as error:
            raise RuntimeError(f"run preflight failed: {error}") from error
        spec_errors = task_spec_errors(ROOT, meta, policy)
        if spec_errors:
            raise RuntimeError("run preflight failed: " + "; ".join(spec_errors))
        if meta.get("owner") != owner:
            raise RuntimeError("task claim does not match owner")
        if meta.get("status") != "in_progress":
            raise RuntimeError("task claim is not active")
        errors = active_expiry_errors(task_id, meta.get("claim_expires"))
        if errors:
            raise RuntimeError(errors[0])
        require_role_admission(owner)
        try:
            transition_allowed(meta, "run")
        except GateError as error:
            raise RuntimeError(str(error)) from error
        assert_invocation_worktree(meta)
        require_policy_unchanged(ROOT, policy)
        return policy


def execution_preflight(args: argparse.Namespace) -> tuple[bool, str, str, float | None]:
    """Evaluate envelope admission."""
    with locked(exclusive=False, phase="execution_envelope_preflight"):
        release_envelope_worktree(args)
        _, meta, _ = locate(args.task)
        if not meta.get("worktree_key"):
            return False, "WORKTREE_BINDING_REQUIRED", "bound execution requires a worktree", None
        try:
            worktree_context = change_drift.bound_worktree(
                meta,
                Path(str(config()["projects_root"])),
                str(config().get("product_worktree", "")),
            )
            worktree = worktree_context.__enter__()
            args._envelope_worktree_context = worktree_context
        except RuntimeError as error:
            return False, "WORKTREE_BINDING_INVALID", str(error), None
        try:
            result = execution_envelope.preflight(
                meta,
                args.owner,
                args.command_class,
                list(args.scope_path),
                worktree,
                bool(getattr(args, "authorize_external_side_effects", False)),
            )
            if not result.allowed:
                release_envelope_worktree(args)
                return False, result.code, result.detail, None
            envelope = meta.get("execution_envelope")
            if not isinstance(envelope, dict):
                release_envelope_worktree(args)
                return False, "ENVELOPE_INVALID", "durable execution envelope is missing", None
            if execution_envelope.canonical_digest(envelope) != meta.get(
                "execution_envelope_digest"
            ):
                release_envelope_worktree(args)
                return (
                    False,
                    "ENVELOPE_INVALID",
                    "durable execution envelope digest mismatches",
                    None,
                )
            rule = prepare_envelope_mounts(args, envelope, worktree, worktree_context)
            return True, result.code, result.detail, rule.get("timeout_seconds")
        except RuntimeError as error:
            release_envelope_worktree(args)
            return False, "PATH_SCOPE_UNAVAILABLE", str(error), None


def prepare_envelope_mounts(
    args: argparse.Namespace, envelope: dict[str, Any], worktree: Path, worktree_context: Any
) -> dict[str, Any]:
    """Validate and retain the exact publication metadata/network mounts."""
    mount_scope = list(envelope["path_scope"]["read"])
    git_metadata = (
        args.command_class == "git-publication"
        and execution_envelope.publication_metadata_allowed(envelope)
    )
    if args.command_class in {"source-write", "git-publication"}:
        mount_scope.extend(args.scope_path)
    if git_metadata:
        envelope_scope_path(worktree, ".git")
    for relative in mount_scope:
        envelope_scope_path(worktree, str(relative))
    rule = envelope["command_classes"][args.command_class]
    args._envelope_worktree = str(worktree)
    args._envelope_worktree_fd = int(worktree.name)
    args._envelope_worktree_context = worktree_context
    args._envelope_write_scope = (
        list(args.scope_path) if args.command_class in {"source-write", "git-publication"} else []
    )
    args._envelope_read_scope = list(envelope["path_scope"]["read"])
    args._envelope_git_metadata = git_metadata
    args._envelope_network = bool(getattr(args, "authorize_external_side_effects", False))
    return cast(dict[str, Any], rule)


def release_envelope_worktree(args: argparse.Namespace) -> None:
    """Close a descriptor retained from bound execution admission."""
    context = getattr(args, "_envelope_worktree_context", None)
    if context is not None:
        delattr(args, "_envelope_worktree_context")
        context.__exit__(None, None, None)
    for name in (
        "_envelope_worktree",
        "_envelope_worktree_fd",
        "_envelope_git_metadata",
        "_envelope_network",
    ):
        if hasattr(args, name):
            delattr(args, name)


def print_execution_preflight(args: argparse.Namespace) -> int:
    """Print an explainable, side-effect-free envelope admission decision."""
    try:
        allowed, code, detail, timeout = execution_preflight(args)
        result: dict[str, object] = {"allowed": allowed, "code": code, "detail": detail}
        if timeout is not None:
            result["timeout_seconds"] = timeout
        if args.json:
            print(json.dumps(result, sort_keys=True, separators=(",", ":")))
        else:
            print(f"{code}: {detail}")
        return 0 if allowed else 2
    finally:
        release_envelope_worktree(args)


def run_envelope_timeout(args: argparse.Namespace) -> float | None:
    """Require envelope admission for a bound task and return its timeout cap."""
    with locked(exclusive=False, phase="run_envelope_check"):
        _, meta, _ = locate(args.task)
        has_envelope = "execution_envelope_ref" in meta
    command_class = getattr(args, "command_class", None)
    if has_envelope and command_class is None:
        raise RuntimeError("bound execution envelope requires --command-class")
    if command_class is None:
        return None
    args.command_class = command_class
    if not hasattr(args, "scope_path"):
        args.scope_path = []
    allowed, code, detail, timeout_cap = execution_preflight(args)
    if not allowed:
        raise RuntimeError(f"execution preflight {code}: {detail}")
    return timeout_cap


sandboxed_envelope_command = execution_envelope.sandboxed_envelope_command
envelope_sandbox_mounts = execution_envelope.envelope_sandbox_mounts
sandbox_base_command = execution_envelope.sandbox_base_command
envelope_scope_path = execution_envelope.envelope_scope_path


def invocation_worktree() -> tuple[str, str] | None:
    """Return product worktree identity."""
    if not CONFIG.exists():
        return None
    settings = config()
    if not {"projects_root", "product_worktree"}.issubset(settings):
        return None
    projects_root = Path(str(settings["projects_root"])).resolve()
    current = Path.cwd().resolve()
    if not inside(current, projects_root):
        return None
    top = Path(
        run(["git", "-C", str(current), "rev-parse", "--show-toplevel"]).stdout.strip()
    ).resolve()
    if top == ROOT.resolve() or not inside(top, projects_root):
        return None
    branch = (
        run(
            ["git", "-C", str(current), "symbolic-ref", "--short", "-q", "HEAD"],
            check=False,
        ).stdout.strip()
        or "DETACHED"
    )
    return top.name, branch


def assert_invocation_worktree(meta: Meta) -> None:
    """Fence product-checkout calls."""
    observed = invocation_worktree()
    if observed is None:
        return
    expected_key = str(meta.get("worktree_key") or "")
    expected_branch = str(meta.get("branch") or "")
    if not expected_key or not expected_branch:
        raise RuntimeError(f"{meta['id']}: active task lacks declared worktree and branch")
    actual_key, actual_branch = observed
    if actual_key != expected_key:
        raise RuntimeError(
            f"{meta['id']}: invocation worktree {actual_key!r} does not match declared "
            f"worktree {expected_key!r}"
        )
    if actual_branch != expected_branch:
        raise RuntimeError(
            f"{meta['id']}: invocation branch {actual_branch!r} does not match declared "
            f"branch {expected_branch!r}"
        )


def append_file_command_result(
    task_id: str,
    owner: str,
    command_hash: str,
    returncode: int,
    classification: str,
    recorded_at: str,
) -> None:
    command_results.append_file(
        RUNTIME, task_id, owner, command_hash, returncode, classification, recorded_at
    )


def legacy_command_results() -> list[Meta]:
    """Strictly load the privacy-safe Git-backend journal for migration."""
    return command_results.load_file(RUNTIME)


def append_command_result(
    task_id: str,
    owner: str,
    command_hash: str,
    returncode: int,
    timed_out: bool,
) -> None:
    selected_backend = (
        mutating_sqlite_backend()
        if backend_selection()["backend"] == "sqlite"
        else storage_backend()
    )
    command_results.append_backend(
        selected_backend, now, task_id, owner, command_hash, returncode, timed_out
    )


class _RunRuntime:
    def __getattr__(self, name: str) -> Any:
        return globals()[name]


_RUN_RUNTIME = _RunRuntime()


class _ExecutionRuntime:
    """Expose execution lifecycle dependencies without circular imports."""

    def __getattr__(self, name: str) -> Any:
        return globals()[name]


_EXECUTION_RUNTIME = _ExecutionRuntime()


def cmd_run(args: argparse.Namespace) -> int:
    return run_command.cmd_run(_RUN_RUNTIME, args)


def _run_envelope_subprocess(
    command: list[str], timeout: float, args: argparse.Namespace
) -> subprocess.CompletedProcess[bytes]:
    if hasattr(args, "_envelope_worktree_fd"):
        return subprocess.run(
            command,
            cwd=str(args._envelope_worktree),
            check=False,
            stdin=subprocess.DEVNULL,
            timeout=timeout,
            pass_fds=(int(args._envelope_worktree_fd),),
        )
    return subprocess.run(command, check=False, stdin=subprocess.DEVNULL, timeout=timeout)


def _cmd_run_fenced(
    args: argparse.Namespace,
) -> tuple[EvidencePolicy, str, float, bool, int, str | None, int | None]:
    if backend_selection()["backend"] == "git":
        config()
    policy = require_active_owner(args.task, args.owner)
    timeout = float(getattr(args, "timeout_seconds", COMMAND_TIMEOUT_SECONDS))
    if timeout <= 0:
        raise RuntimeError("command timeout must be positive")
    try:
        retry_circuit._window(getattr(args, "retry_window", retry_circuit.DEFAULT_WINDOW))
    except ValueError as error:
        raise RuntimeError(str(error)) from error
    timeout_cap = run_envelope_timeout(args)
    command_hash = hashlib.sha256("\0".join(args.command).encode()).hexdigest()
    if timeout_cap is not None and timeout > timeout_cap:
        raise RuntimeError(f"command timeout exceeds envelope limit of {timeout_cap}s")
    require_policy_unchanged(ROOT, policy)
    al.prepare(_RUN_RUNTIME, args, policy)
    command = sandboxed_envelope_command(args)
    execution_id: str | None = None
    execution_revision: int | None = None
    if hasattr(args, "_envelope_worktree"):
        execution_id = uuid.uuid4().hex
        expires_at = (
            (dt.datetime.now(dt.UTC) + dt.timedelta(seconds=timeout + 60))
            .replace(microsecond=0)
            .isoformat()
        )
        _, current, _ = locate(args.task)
        reserve = argparse.Namespace(
            task=args.task,
            owner=args.owner,
            expected_revision=current["task_revision"],
            execution_id=execution_id,
            execution_expires_at=expires_at,
            command_class=args.command_class,
            scope_digest="sha256:"
            + hashlib.sha256(
                json.dumps(list(args.scope_path), separators=(",", ":")).encode()
            ).hexdigest(),
            argv_digest=command_hash,
        )
        mutate(reserve, "execution-start", policy)
        _, reserved, _ = locate(args.task)
        execution_revision = int(reserved["task_revision"])
    if execution_id is None:
        identity = retry_circuit.normalized_identity(
            command_hash,
            getattr(args, "command_class", None),
            list(getattr(args, "scope_path", [])),
        )
        with task_execution_locked(args.task, exclusive=True, phase="retry_circuit_launch"):
            _, current, _ = locate(args.task)
            args.expected_revision = int(current["task_revision"])
            args.retry_circuit_identity = identity
            args.retry_circuit_reservation = uuid.uuid4().hex
            args.retry_window = getattr(args, "retry_window", retry_circuit.DEFAULT_WINDOW)
            args.retry_circuit_expires_at = (
                (dt.datetime.now(dt.UTC) + dt.timedelta(seconds=timeout + 60))
                .replace(microsecond=0)
                .isoformat()
            )
            mutate(args, "retry-circuit-reserve", policy)
            args.retry_circuit_resolution_revision = int(args.expected_revision) + 1
    timed_out = False
    try:
        proc = _run_envelope_subprocess(command, timeout, args)
    except subprocess.TimeoutExpired:
        timed_out = True
        returncode = 124
    else:
        returncode = proc.returncode
    return policy, command_hash, timeout, timed_out, returncode, execution_id, execution_revision


def cmd_init(args: argparse.Namespace) -> None:
    """Bind a fresh vendored coordinator permanently to one state/product pair."""
    if PROJECT_CONFIG.exists() or BINDING.exists() or BACKEND_CONFIG.exists():
        raise RuntimeError("coordinator is already initialized")
    top = Path(run(["git", "-C", str(ROOT), "rev-parse", "--show-toplevel"]).stdout.strip())
    if Path.cwd().resolve() != ROOT.resolve() or top.resolve() != ROOT.resolve():
        raise RuntimeError("initialize from the state repository root")
    state_repository = repository_slug(args.state_repository)
    product_repository = repository_slug(args.product_repository)
    if git_repository_slug(ROOT) != state_repository:
        raise RuntimeError("current origin does not match --state-repository")
    project_id = str(uuid.uuid4())
    settings = {
        "schema_version": 1,
        "project_id": project_id,
        "project_name": args.project_name,
        "project_title": args.project_title,
        "status_view": args.status_view,
        "commit_signoff": args.commit_signoff,
    }
    binding = {
        "schema_version": 1,
        "project_id": project_id,
        "state_repository": state_repository,
        "product_repository": product_repository,
    }
    selected_backend = str(getattr(args, "backend", "git"))
    selection = {"schema_version": 1, "project_id": project_id, "backend": selected_backend}
    before: dict[Path, str | None] = {PROJECT_CONFIG: None, BINDING: None, BACKEND_CONFIG: None}
    try:
        atomic(PROJECT_CONFIG, json.dumps(settings, indent=2, sort_keys=True) + "\n")
        project_settings()
        atomic(BINDING, json.dumps(binding, indent=2, sort_keys=True) + "\n")
        project_binding()
        if selected_backend == "sqlite":
            initial_tasks = git_tasks()
            initial_errors = []
            for path, meta, _ in initial_tasks:
                initial_errors.extend(basic_task_errors(path, meta))
            initial_errors.extend(graph_errors(initial_tasks))
            initial_errors.extend(hierarchy_errors(initial_tasks))
            if initial_errors:
                raise RuntimeError("initial task import failed:\n" + "\n".join(initial_errors))
            create_database(
                DATABASE,
                binding,
                initial_tasks,
                imported_at=now(),
                source_backend="initial",
                source_checkpoint="uncommitted-init",
                command_results=legacy_command_results(),
            )
            provision_sqlite_barrier()
        atomic(BACKEND_CONFIG, json.dumps(selection, indent=2, sort_keys=True) + "\n")
        backend_selection()
    except Exception:
        restore_paths(before)
        DATABASE.unlink(missing_ok=True)
        raise
    if selected_backend == "sqlite":
        export_sqlite_projections(evidence_policy(ROOT))
    print(f"Initialized project binding {project_id} with {selected_backend} backend")


def cmd_migrate(args: argparse.Namespace) -> None:  # noqa: C901
    """Explicitly and restart-safely switch authority between supported backends."""
    policy = evidence_policy(ROOT)
    current = str(backend_selection()["backend"])
    if current == args.to:
        raise RuntimeError(f"coordinator already uses {current}")
    binding = project_binding()
    selection = {"schema_version": 1, "project_id": binding["project_id"], "backend": args.to}
    if args.to == "sqlite":
        with locked():
            sync_replica_before_write()
            tasks = git_tasks()
            command_results = legacy_command_results()
            session_records = storage_backend().load_session_records()
            checkpoint_records = storage_backend().load_checkpoint_records()
            errors = validate(live=False, policy=policy)
            if errors:
                raise RuntimeError("migration preflight failed:\n" + "\n".join(errors))
            require_policy_unchanged(ROOT, policy)
            checkpoint = run(["git", "-C", str(ROOT), "rev-parse", "HEAD"]).stdout.strip()
            DATABASE.unlink(missing_ok=True)
            try:
                create_database(
                    DATABASE,
                    binding,
                    tasks,
                    imported_at=now(),
                    source_backend="git",
                    source_checkpoint=checkpoint,
                    command_results=command_results,
                    session_records=session_records,
                    checkpoint_records=checkpoint_records,
                )
                imported = SQLiteBackend(DATABASE, binding, TASKS).load_tasks()
                if [(m, b) for _, m, b in tasks] != [(m, b) for _, m, b in imported]:
                    raise RuntimeError("migration equivalence check failed")
                imported_sessions = SQLiteBackend(DATABASE, binding, TASKS).load_session_records()
                imported_checkpoints = SQLiteBackend(
                    DATABASE, binding, TASKS
                ).load_checkpoint_records()
                if (
                    imported_sessions != session_records
                    or imported_checkpoints != checkpoint_records
                ):
                    raise RuntimeError("record migration equivalence check failed")
                require_policy_unchanged(ROOT, policy)
                provision_sqlite_barrier()
                atomic(BACKEND_CONFIG, json.dumps(selection, indent=2, sort_keys=True) + "\n")
            except Exception:
                DATABASE.unlink(missing_ok=True)
                raise
        export_sqlite_projections(policy)
    else:
        backend = mutating_sqlite_backend()

        def project(tasks: list[Task]) -> None:
            write_sqlite_projections(tasks, already_locked=True, policy=policy)

        def switch() -> None:
            errors = validate(live=False, policy=policy)
            if errors:
                raise RuntimeError("rollback export failed:\n" + "\n".join(errors))
            require_policy_unchanged(ROOT, policy)
            atomic(BACKEND_CONFIG, json.dumps(selection, indent=2, sort_keys=True) + "\n")

        backend.retire(project, switch)
    print(f"Migrated authoritative storage from {current} to {args.to}")


def cmd_upgrade(args: argparse.Namespace) -> int:
    """Dispatch only the reviewed, fail-closed upgrade command boundary."""
    if __package__:
        from .upgrade_commands import (
            _read_contract,
            _read_runtime_binding,
            consume_selected_runtime_command,
            execute_upgrade_command,
        )
    else:
        from upgrade_commands import (  # type: ignore[import-not-found,no-redef]
            _read_contract,
            _read_runtime_binding,
            consume_selected_runtime_command,
            execute_upgrade_command,
        )

    if args.upgrade_action == "consume":
        if __package__:
            from .runtime_bootstrap import ExpectedRuntimeIdentity
        else:
            from runtime_bootstrap import (  # type: ignore[import-not-found,no-redef]
                ExpectedRuntimeIdentity,
            )

        return consume_selected_runtime_command(
            Path(args.selector),
            Path(args.releases_root),
            ExpectedRuntimeIdentity(
                args.source_commit,
                args.tag_ref,
                args.tag_object,
                args.signature_sha256,
                args.trust_policy_sha256,
                args.vendor_manifest_sha256,
            ),
            args.manifest_digest,
            tuple(args.runtime_command),
        )

    live_binding = None
    binding_path = Path(args.binding) if args.binding is not None else None
    selected_backend = str(backend_selection()["backend"])
    if args.upgrade_action in {"apply", "rollback"}:
        if __package__:
            from .production_upgrade_binding import (
                resolve_git_live_binding,
                resolve_sqlite_live_binding,
            )
        else:
            from production_upgrade_binding import (  # type: ignore[import-not-found,no-redef]
                resolve_git_live_binding,
                resolve_sqlite_live_binding,
            )
        if binding_path is None:
            raise RuntimeError(
                "mutating upgrade actions require --binding; no coordinator state was mutated"
            )
        contract = _read_contract(Path(args.contract))
        runtime_binding = _read_runtime_binding(
            binding_path, contract, str(backend_selection()["backend"])
        )
        if selected_backend == "sqlite":
            live_binding = resolve_sqlite_live_binding(
                runtime_binding,
                database=DATABASE,
                control_database=CONTROL_DATABASE,
                authority_marker=AUTHORITY_MARKER,
                authority_lifecycle=AUTHORITY_LIFECYCLE,
                authority_lock=AUTHORITY_LOCK,
                control_binding=CONTROL_BINDING,
                control_lock=CONTROL_LOCK,
                project_binding=BINDING,
                backend_config=BACKEND_CONFIG,
                runtime_selector=RUNTIME / "runtime-selector.json",
                common_lock=locked,
            )
        else:
            live_binding = resolve_git_live_binding(
                runtime_binding,
                repository=ROOT,
                control_database=CONTROL_DATABASE,
                authority_marker=AUTHORITY_MARKER,
                authority_lifecycle=AUTHORITY_LIFECYCLE,
                authority_lock=AUTHORITY_LOCK,
                control_binding=CONTROL_BINDING,
                control_lock=CONTROL_LOCK,
                project_binding=BINDING,
                runtime_selector=RUNTIME / "runtime-selector.json",
                common_lock=locked,
            )

    return execute_upgrade_command(
        str(args.upgrade_action),
        Path(args.contract),
        selected_backend,
        binding_path,
        live_binding,
    )


def dispatch_roles_command(args: argparse.Namespace) -> int:
    """Dispatch a role command after the permanent project binding passed."""
    role_error = role_module.RolesError
    assign_role = role_module.assign
    check_roles = role_module.check
    list_roles = role_module.list_assignments
    remove_role = role_module.remove
    try:
        if args.roles_command == "assign":
            result = assign_role(
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
        elif args.roles_command == "list":
            result = list_roles(args.state, args.registry, args.owner_id)
        elif args.roles_command == "check":
            result = check_roles(args.state, args.registry, args.owner_id)
        else:
            result = remove_role(
                args.state,
                args.registry,
                expected_revision=args.expected_revision,
                assignment_id=args.assignment_id,
            )
    except role_error as error:
        raise RuntimeError(str(error)) from error
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))
    return 0


def dispatch_read_only_command(args: argparse.Namespace) -> int:
    if args.cmd == "snapshot":
        cmd_snapshot(args.task)
    elif args.cmd == "resume-card":
        return resume_card_runtime.dispatch(args, sys.modules[__name__])
    elif args.cmd == "campaign":
        return cast(
            int,
            __import__("tools.campaign_runtime", fromlist=["dispatch"]).dispatch(
                args, sys.modules[__name__]
            ),
        )
    elif args.cmd == "board":
        cmd_board()
    elif args.cmd == "metrics":
        cmd_metrics()
    else:
        return print_execution_preflight(args)
    return 0


def cmd_retry_circuit_status(task_id: str) -> int:
    """Render the durable retry state without exposing command input or output."""
    with locked(exclusive=False, phase="retry_circuit_status"):
        _, meta, _ = locate(task_id)
        state = meta.get("retry_circuit")
        if state is None:
            state = {
                "schema_version": retry_circuit.SCHEMA_VERSION,
                "attempts": [],
                "recoveries": [],
                "hold": None,
                "reservations": [],
                "abandoned": [],
            }
        else:
            retry_circuit.validate(state)
        print(json.dumps(state, sort_keys=True, separators=(",", ":")))
    return 0


def dispatch_fast_command(args: argparse.Namespace) -> int:
    from tools.fast_receipt_cli import dispatch_fast

    return dispatch_fast(sys.modules[__name__], args)


def dispatch_lifecycle_mutation(args: argparse.Namespace) -> None:
    note = mutate(args, args.cmd)
    if note is not None:
        print(note)


def dispatch_retry_circuit(args: argparse.Namespace) -> int:
    if args.retry_circuit_action == "status":
        return cmd_retry_circuit_status(args.task)
    dispatch_lifecycle_mutation(args)
    return 0


def dispatch_side_effect_command(args: argparse.Namespace) -> bool:
    handlers: dict[str, Callable[[], object]] = {
        "reconcile": lambda: reconcile(do_commit=args.commit, push=args.push),
        "checkpoint": lambda: cmd_checkpoint(args),
        "rollback": lambda: cmd_rollback(args),
        "render-status": lambda: cmd_render_status(check=args.check),
        "migrate": lambda: cmd_migrate(args),
    }
    handler = handlers.get(args.cmd)
    if handler is None:
        return False
    handler()
    return True


def dispatch_returning_command(args: argparse.Namespace) -> int | None:
    if args.cmd == "roles":
        return dispatch_roles_command(args)
    if args.cmd in ("snapshot", "resume-card", "campaign", "board", "metrics", "preflight"):
        return dispatch_read_only_command(args)
    if args.cmd == "retry-circuit":
        return dispatch_retry_circuit(args)
    if args.cmd == "autonomy-limits":
        return al.dispatch(_RUN_RUNTIME, args)
    if args.cmd == "doctor":
        return cmd_doctor(live=args.live)
    if args.cmd == "upgrade":
        return cmd_upgrade(args)
    return None


def dispatch_bound_standard_command(args: argparse.Namespace) -> int:
    result = dispatch_returning_command(args)
    if result is not None:
        return result
    if args.cmd in {"repair-legacy-binding", "repair-predicate-ledger"}:
        dispatch_lifecycle_mutation(args)
        return 0
    if args.cmd in (
        *LIFECYCLE_MUTATION_COMMANDS,
        "gate",
    ):
        dispatch_lifecycle_mutation(args)
        return 0
    if args.cmd == "run":
        if args.command and args.command[0] == "--":
            args.command = args.command[1:]
        return cmd_run(args)
    if dispatch_side_effect_command(args):
        return 0
    return 0


if __package__:
    from . import issue_series_service
else:  # pragma: no cover
    import issue_series_service  # type: ignore[import-not-found,no-redef]

globals().update(issue_series_service.install(globals()))


def dispatch_bound_command(args: argparse.Namespace) -> int:
    if args.cmd == "fast":
        return dispatch_fast_command(args)
    return dispatch_bound_standard_command(args)


def main() -> int:
    parser = argparse.ArgumentParser()
    commands = parser.add_subparsers(dest="cmd", required=True)
    item = commands.add_parser("init")
    item.add_argument("--state-repository", required=True)
    item.add_argument("--product-repository", required=True)
    item.add_argument("--project-name", required=True)
    item.add_argument("--project-title", required=True)
    item.add_argument("--status-view", action="store_true")
    item.add_argument("--commit-signoff", action="store_true")
    item.add_argument("--backend", choices=BACKENDS, default="sqlite")
    item = commands.add_parser("migrate")
    item.add_argument("--to", choices=BACKENDS, required=True)
    item = commands.add_parser("upgrade")
    upgrade_actions = item.add_subparsers(dest="upgrade_action", required=True)
    for action in ("check", "plan", "apply", "rollback"):
        upgrade_action = upgrade_actions.add_parser(action)
        upgrade_action.add_argument("--contract", type=Path, required=True)
        upgrade_action.add_argument("--binding", type=Path)
    consume = upgrade_actions.add_parser("consume")
    consume.add_argument("--selector", type=Path, required=True)
    consume.add_argument("--releases-root", type=Path, required=True)
    consume.add_argument("--source-commit", required=True)
    consume.add_argument("--tag-ref", required=True)
    consume.add_argument("--tag-object", required=True)
    consume.add_argument("--signature-sha256", required=True)
    consume.add_argument("--trust-policy-sha256", required=True)
    consume.add_argument("--vendor-manifest-sha256", required=True)
    consume.add_argument("--manifest-digest", required=True)
    consume.add_argument("runtime_command", nargs="*")
    item = commands.add_parser("reconcile")
    item.add_argument("--commit", action="store_true")
    item.add_argument("--push", action="store_true")
    item = commands.add_parser("roles")
    item.add_argument("--state", type=Path, default=ROOT / ".runtime/roles.json")
    item.add_argument("--registry", type=Path, default=ROOT / "examples/roles/role-registry.json")
    role_commands = item.add_subparsers(dest="roles_command", required=True)
    role = role_commands.add_parser("assign")
    role.add_argument("--expected-revision", type=int, required=True)
    role.add_argument("--assignment-id", required=True)
    role.add_argument("--owner-id", required=True)
    role.add_argument("--role-id", required=True)
    role.add_argument("--expires-at", required=True)
    role.add_argument("--evidence-kind", choices=("review", "policy", "ticket"), required=True)
    role.add_argument("--evidence-ref", required=True)
    role.add_argument("--evidence-digest", required=True)
    role = role_commands.add_parser("list")
    role.add_argument("--owner-id")
    role_commands.add_parser("check").add_argument("--owner-id", required=True)
    role = role_commands.add_parser("remove")
    role.add_argument("--expected-revision", type=int, required=True)
    role.add_argument("--assignment-id", required=True)
    item = commands.add_parser("snapshot")
    item.add_argument("--task")
    resume_card.add_command_parser(commands)
    __import__("tools.campaign", fromlist=["add_command_parser"]).add_command_parser(commands)
    issue_series_service.add_cli_parser(commands)
    commands.add_parser("board")
    commands.add_parser("metrics")
    item = commands.add_parser("checkpoint")
    item.add_argument("task")
    item.add_argument("--owner", required=True)
    item.add_argument("--expected-revision", type=int, required=True)
    item = commands.add_parser("fast")
    fast_actions = item.add_subparsers(dest="fast_action", required=True)
    fast_heartbeat = fast_actions.add_parser("heartbeat")
    fast_heartbeat.add_argument("task")
    fast_heartbeat.add_argument("--owner", required=True)
    fast_heartbeat.add_argument("--expected-revision", type=int, required=True)
    fast_heartbeat.add_argument("--lease-minutes", type=int, default=120)
    fast_heartbeat.add_argument("--key", required=True)
    fast_claim = fast_actions.add_parser("claim")
    fast_claim.add_argument("task")
    fast_claim.add_argument("--owner", required=True)
    fast_claim.add_argument("--expected-revision", type=int, required=True)
    fast_claim.add_argument("--lease-minutes", type=int, default=120)
    fast_claim.add_argument("--worker-pid", type=int)
    fast_claim.add_argument("--worker-start-time", type=int)
    fast_claim.add_argument("--key", required=True)
    fast_promote = fast_actions.add_parser("promote")
    fast_promote.add_argument("task")
    fast_promote.add_argument("--expected-revision", type=int, required=True)
    fast_promote.add_argument("--note", required=True)
    fast_promote.add_argument("--key", required=True)
    fast_update = fast_actions.add_parser("update")
    fast_update.add_argument("task")
    fast_update.add_argument("--owner", required=True)
    fast_update.add_argument("--expected-revision", type=int, required=True)
    fast_update.add_argument("--status", choices=STATUSES)
    fast_update.add_argument("--priority", choices=PRIORITIES)
    fast_update.add_argument("--summary")
    fast_update.add_argument("--next-action")
    fast_update.add_argument("--note", required=True)
    fast_update.add_argument("--key", required=True)
    fast_receipt = fast_actions.add_parser("receipt")
    fast_receipt.add_argument("receipt_id")
    fast_observe = fast_actions.add_parser("observe")
    fast_observe.add_argument("--max-age-seconds", type=int, required=True)
    fast_worker = fast_actions.add_parser("worker")
    fast_worker.add_argument("--limit", type=int, default=16)
    fast_worker.add_argument("--serve", action="store_true")
    fast_worker.add_argument("--poll-seconds", type=float, default=0.05)
    fast_publisher = fast_actions.add_parser("publisher")
    fast_publisher.add_argument("--serve", action="store_true")
    fast_publisher.add_argument("--poll-seconds", type=float, default=5.0)
    item = commands.add_parser("directive")
    directive_commands = item.add_subparsers(dest="directive_action", required=True)
    directive = directive_commands.add_parser("create")
    directive.add_argument("--directive-id", required=True)
    directive.add_argument("--authority", required=True)
    directive.add_argument("--precedence", type=int, required=True)
    directive.add_argument("--role-scope", action="append", default=[])
    directive.add_argument("--task-scope", action="append", default=[])
    directive.add_argument("--statement", required=True)
    directive.add_argument("--owner", required=True)
    directive.add_argument("--lease-minutes", type=int, default=120)
    directive.add_argument("--guidance-ref", default="")
    directive = directive_commands.add_parser("list")
    directive.add_argument(
        "--lifecycle", choices=["proposed", "active", "superseded", "revoked", "escalated"]
    )
    directive = directive_commands.add_parser("transition")
    directive.add_argument("directive_id")
    directive.add_argument("action", choices=["activate", "supersede", "revoke", "escalate"])
    directive.add_argument("--owner", required=True)
    directive.add_argument("--expected-revision", type=int, required=True)
    directive.add_argument("--guidance-ref", default="")
    item = commands.add_parser("rollback")
    item.add_argument("--checkpoint", required=True)
    item.add_argument("--reconcile", action="store_true")
    item = commands.add_parser("doctor")
    item.add_argument("--live", action="store_true")
    item = commands.add_parser("render-status")
    item.add_argument("--check", action="store_true")
    for name in ("claim", "heartbeat"):
        item = commands.add_parser(name)
        item.add_argument("task")
        item.add_argument("--owner", required=True)
        item.add_argument("--lease-minutes", type=int, default=120)
        if name == "claim":
            item.add_argument("--worker-pid", type=int)
            item.add_argument("--worker-start-time", type=int)
        if name == "heartbeat":
            item.add_argument("--expected-revision", type=int)
    item = commands.add_parser("release")
    item.add_argument("task")
    item.add_argument("--owner", required=True)
    item.add_argument(
        "--status", required=True, choices=[value for value in STATUSES if value != "in_progress"]
    )
    item.add_argument("--note", required=True)
    item = commands.add_parser("accept")
    item.add_argument("task")
    item.add_argument("--owner", required=True)
    item.add_argument("--expected-revision", type=int, required=True)
    item.add_argument("--evidence-class", required=True)
    item.add_argument("--evidence-ref", required=True)
    item.add_argument("--evidence-digest", required=True)
    item.add_argument("--predicate")
    item.add_argument("--candidate-ref")
    item.add_argument("--candidate-digest")
    item.add_argument("--reopen", action="store_true")
    item.add_argument("--note", required=True)
    item = commands.add_parser("bind-spec")
    item.add_argument("task")
    item.add_argument("--owner", required=True)
    item.add_argument("--expected-revision", type=int, required=True)
    item.add_argument("--spec-ref", required=True)
    item.add_argument("--spec-revision", type=int, required=True)
    item = commands.add_parser("bind-worktree")
    item.add_argument("task")
    item.add_argument("--owner", required=True)
    item.add_argument("--expected-revision", type=int, required=True)
    item.add_argument("--branch", required=True)
    item.add_argument("--worktree-key", required=True)
    item = commands.add_parser("repair-legacy-binding")
    item.add_argument("task")
    item.add_argument("--expected-revision", type=int, required=True)
    item.add_argument("--branch", required=True)
    item.add_argument("--worktree-key", required=True)
    item.add_argument("--note", required=True)
    plr.add_parser(commands)
    item = commands.add_parser("bind-envelope")
    item.add_argument("task")
    item.add_argument("--owner", required=True)
    item.add_argument("--expected-revision", type=int, required=True)
    item.add_argument("--envelope-ref", required=True)
    item.add_argument("--envelope-revision", type=int, required=True)
    item = commands.add_parser("replace-envelope")
    item.add_argument("task")
    item.add_argument("--owner", required=True)
    item.add_argument("--expected-revision", type=int, required=True)
    item.add_argument("--envelope-ref", required=True)
    item.add_argument("--envelope-revision", type=int, required=True)
    item = commands.add_parser("preflight")
    item.add_argument("task")
    item.add_argument("--owner", required=True)
    item.add_argument(
        "--command-class", choices=sorted(execution_envelope.COMMAND_CLASSES), required=True
    )
    item.add_argument("--scope-path", action="append", default=[])
    item.add_argument("--json", action="store_true")
    item = commands.add_parser("promote")
    item.add_argument("task")
    item.add_argument("--expected-revision", type=int, required=True)
    item.add_argument("--note", required=True)
    item = commands.add_parser("resume")
    item.add_argument("task")
    item.add_argument("--expected-revision", type=int, required=True)
    item.add_argument("--session", required=True)
    item.add_argument("--note", required=True)
    item = commands.add_parser("unblock")
    item.add_argument("task")
    item.add_argument("--expected-revision", type=int, required=True)
    item.add_argument("--note", required=True)
    item = commands.add_parser("pause")
    item.add_argument("task")
    item.add_argument("--owner", required=True)
    item.add_argument("--expected-revision", type=int, required=True)
    item.add_argument("--note", required=True)
    item = commands.add_parser("recover-expired")
    item.add_argument("task")
    item.add_argument("--expected-revision", type=int, required=True)
    item.add_argument("--allow-legacy-without-identity", action="store_true")
    item.add_argument("--note", required=True)
    item = commands.add_parser("recover-execution")
    item.add_argument("task")
    item.add_argument("--expected-revision", type=int, required=True)
    item.add_argument("--note", required=True)
    item = commands.add_parser("abandon-execution")
    item.add_argument("task")
    item.add_argument("--expected-revision", type=int, required=True)
    item.add_argument("--execution-id", required=True)
    item.add_argument("--allow-legacy-without-identity", action="store_true")
    item.add_argument("--evidence-ref", required=True)
    item.add_argument("--evidence-digest", required=True)
    item.add_argument("--note", required=True)
    item = commands.add_parser("update")
    item.add_argument("task")
    item.add_argument("--owner", required=True)
    item.add_argument("--expected-revision", type=int, required=True)
    item.add_argument("--status", choices=STATUSES)
    item.add_argument("--priority", choices=PRIORITIES)
    item.add_argument("--summary")
    item.add_argument("--next-action")
    item.add_argument("--note", required=True)
    change_drift.add_command_parser(commands)
    assumption_revalidation.add_command_parser(commands)
    retry_circuit.add_command_parser(commands)
    al.add_command_parser(commands)
    item = commands.add_parser("gate")
    item.add_argument("task")
    item.add_argument("--expected-revision", type=int, required=True)
    item.add_argument(
        "--stage",
        choices=[stage.value for stage in (*GateStage, *StageGate)],
        required=True,
    )
    item.add_argument("--action", choices=("open", "resolve", "reopen"), required=True)
    item.add_argument(
        "--disposition", choices=("accepted", "rejected", "unresolved"), required=True
    )
    item.add_argument("--before", action="append", default=[], required=True)
    item.add_argument("--after", action="append", default=[], required=True)
    item.add_argument("--public-ref", required=True)
    item.add_argument("--session-id")
    item.add_argument("--request-ref")
    item.add_argument(
        "--activation",
        choices=(
            "user-decision",
            "user-detail-request",
            "user-proposal-review",
            "agent-uncertainty",
            "policy-required-approval",
        ),
    )
    item.add_argument("--tui-contract-version")
    item = commands.add_parser("run")
    item.add_argument("task")
    item.add_argument("--owner", required=True)
    item.add_argument("--timeout-seconds", type=float, default=COMMAND_TIMEOUT_SECONDS)
    item.add_argument("--retry-window", type=int, default=retry_circuit.DEFAULT_WINDOW)
    al.add_run_arguments(item)
    item.add_argument("--command-class", choices=sorted(execution_envelope.COMMAND_CLASSES))
    item.add_argument("--scope-path", action="append", default=[])
    item.add_argument("--authorize-external-side-effects", action="store_true")
    item.add_argument("command", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    if args.cmd == "init":
        cmd_init(args)
        return 0
    assert_project_binding()
    if args.cmd == "directive":
        cmd_directive(args)
        return 0
    if issue_series_service.dispatch_cli(args, globals()):
        return 0
    return dispatch_bound_command(args)


def main_entrypoint() -> int:
    try:
        return main()
    except RetryableCoordinatorError as error:
        print(f"RETRYABLE: {error}", file=sys.stderr)
        return 75
    except RepairRequiredCoordinatorError as error:
        print(f"REPAIR_REQUIRED: {error}", file=sys.stderr)
        return 76
    except Exception as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main_entrypoint())
