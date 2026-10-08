#!/usr/bin/env python3
# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Transactional, project-configurable coordination state."""

import argparse
import contextlib
import datetime as dt
import fcntl
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import textwrap
import threading
import time
import uuid
from collections import Counter
from collections.abc import Iterator
from pathlib import Path
from typing import Any, cast

if not __package__:
    _SCRIPT_ROOT = str(Path(__file__).resolve().parent.parent)
    if _SCRIPT_ROOT not in sys.path:
        sys.path.insert(0, _SCRIPT_ROOT)

if __package__:
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
    from .task_spec import done_admission_error, task_spec_errors
else:  # pragma: no cover - direct script execution
    try:
        from board_metrics import build_metrics  # type: ignore[import-not-found,no-redef]  # noqa: I001
        from board_metrics import encode as encode_metrics  # type: ignore[no-redef]
    except ModuleNotFoundError:  # pragma: no cover - standalone vendored bootstrap

        def build_metrics(tasks: list[tuple[Any, dict[str, Any], str]]) -> dict[str, Any]:
            del tasks
            raise RuntimeError("board metrics module is unavailable in this vendored bootstrap")

        def encode_metrics(metrics: dict[str, Any]) -> str:
            del metrics
            raise RuntimeError("board metrics module is unavailable in this vendored bootstrap")

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
        done_admission_error,
        task_spec_errors,
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
    "release",
    "promote",
    "pause",
    "resume",
    "unblock",
    "recover-expired",
    "update",
)
# CURRENT.md is the compact actionable queue; terminal history remains in the
# full STATUS.md projection and authoritative task records.
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
    "owner",
    "role",
    "team",
    "claim_expires",
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
    "parent_task_ref",
    "children",
}
type Meta = dict[str, Any]
type Task = tuple[Path, Meta, str]
type State = dict[str, Any]

COORDINATOR_VERSION = "0.3.57"
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
    """Load and strictly validate the tracked, non-secret project profile."""
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
    """Normalize a GitHub repository URL or OWNER/REPOSITORY value."""
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
    """Load the project-bound backend; missing legacy selection means Git."""
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
    """Adapter preserving the existing file/Git authority contract."""

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
    """Return the barrier-aware writer, or an explicit legacy compatibility route.

    Pre-marker installations remain usable as required by the compatibility
    contract. They cannot start an upgrade; once provisioning exists, every
    write goes through the durable fence factory below.
    """
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
    """Provision the authority fence and one released baseline session."""
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
    """Read and normalize one checkout's origin identity."""
    result = run(["git", "-C", str(root), "remote", "get-url", "origin"])
    return repository_slug(result.stdout.strip())


def inside(candidate: Path, root: Path) -> bool:
    """Return whether candidate is root or one of its descendants."""
    candidate = candidate.resolve()
    root = root.resolve()
    return candidate == root or root in candidate.parents


def _assert_storage_binding(binding: Meta) -> None:
    """Check the tracked selector and SQLite-internal identity."""
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


def assert_project_binding() -> None:
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
    current = Path.cwd().resolve()
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


class LockTimeoutError(RuntimeError):
    """The coordinator lock could not be acquired within its bounded deadline."""


class LockOwnershipError(RuntimeError):
    """A coordinator lock capability is missing, stale, or used incorrectly."""


class CoordinatorLockGuard:
    """Capability proving that this process and thread hold one lock inode."""

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
        """Fail closed unless the original owner still holds the same inode."""
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
    """A Git/GitHub or coordinator command exceeded its bounded deadline."""


class ReplicaDivergedError(RuntimeError):
    """The state replica cannot be advanced without reconciling Git history."""


class ExternalObservationError(RuntimeError):
    """A bounded read-only external observation failed after retries."""


class PostCommandReconcileError(RuntimeError):
    """A command result is durable, but its subsequent live reconciliation failed."""


class StorageCommittedError(RuntimeError):
    """A SQLite transaction committed but its disposable projection failed."""


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

UUID_PRIVACY_EXEMPT = frozenset(
    {
        Path(".handoffctl.json"),
        Path("coordinator.binding.json"),
        Path("coordinator.backend.json"),
        Path("tests/test_handoffctl.py"),
        Path("tests/test_sqlite_storage.py"),
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
    """Resolve one lock shared by every worktree of the same local Git repository."""
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


@contextlib.contextmanager
def locked(
    *, exclusive: bool = True, timeout: float = LOCK_TIMEOUT_SECONDS
) -> Iterator[CoordinatorLockGuard]:
    lock_path = coordinator_lock_path()
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
                        f"LOCK_TIMEOUT after {timeout:.1f}s acquiring {mode} coordinator lock"
                    ) from error
                time.sleep(min(LOCK_POLL_SECONDS, remaining))
        guard = CoordinatorLockGuard._create(lock_path, fd, exclusive=exclusive)
        yield guard
    finally:
        if "guard" in locals():
            guard._invalidate()
        fcntl.flock(fd, fcntl.LOCK_UN)
        os.close(fd)


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
        return str(value or "-").replace("|", "\\|").replace("\n", " ")

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
            link = f"[{meta['id']}](tasks/{by_id[meta['id']]})"
            row = (
                f"| {meta['priority']} | {link}: {clean(meta['title'])} | "
                f"{clean(meta['summary'])} | {clean(meta['next_action'])} | "
                f"{clean(meta.get('owner'))} |"
            )
            lines.append(row)
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def project_scan() -> State:
    settings = config()
    base = Path(settings["projects_root"])
    repo = base / settings["product_worktree"]

    def listed_worktrees(checkout: Path) -> list[Path]:
        raw = run(["git", "-C", str(checkout), "worktree", "list", "--porcelain"]).stdout
        return [Path(line[9:]) for line in raw.splitlines() if line.startswith("worktree ")]

    # The coordinator repository may have many linked worker checkouts. Their
    # relationship to the coordinator's origin/main changes whenever state is
    # committed, so including them makes the generated live projections stale
    # after every coordinator update. Keep all product-repository worktrees,
    # but exclude every checkout owned by the coordinator repository.
    coordinator_paths = {path.resolve() for path in listed_worktrees(ROOT)}
    paths: list[Path] = []
    for path in listed_worktrees(repo):
        if path.resolve() not in coordinator_paths and path not in paths:
            paths.append(path)
    worktrees = []
    for path in paths:
        head = run(["git", "-C", str(path), "rev-parse", "HEAD"]).stdout.strip()
        branch = (
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
        worktrees.append(
            {
                "key": path.name,
                "branch": branch,
                "head": head,
                "dirty": len(changed),
                "paths": [line[3:] for line in changed[:50]],
                "behind": int(counts[0]) if len(counts) == 2 else None,
                "ahead": int(counts[1]) if len(counts) == 2 else None,
            }
        )
    github = settings["github_repository"]
    prs = json.loads(
        run_github_observation(
            [
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
        ).stdout
    )
    runs = json.loads(
        run_github_observation(
            [
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
        ).stdout
    )
    remote_line = run(
        ["git", "-C", str(repo), "ls-remote", "origin", "refs/heads/main"]
    ).stdout.strip()
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
        for regex, label in PRIVATE:
            if not privacy_pattern_applies(relative, label):
                continue
            if regex.search(text):
                errors.append(f"{relative}: {label}")
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
    errors.extend(f"{task_id}: {error}" for error in gate_errors(meta.get("oracle_gate")))
    return errors


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


def basic_task_errors(path: Path, meta: Meta) -> list[str]:
    return [
        *field_errors(path, meta),
        *value_errors(path, meta),
        *reference_errors(path, meta),
        *task_spec_errors(ROOT, meta),
    ]


def parse_claim_expiry(expiry: object) -> dt.datetime:
    """Parse one timezone-aware lease deadline."""
    if not isinstance(expiry, str) or not expiry:
        raise ValueError("missing or non-string claim expiry")
    parsed = dt.datetime.fromisoformat(expiry.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("claim expiry lacks timezone")
    return parsed.astimezone(dt.UTC)


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


def mutation_errors(path: Path, before: dict[Path, str | None]) -> list[str]:
    """Validate a Git mutation without gating on unrelated repository findings."""
    tasks = all_tasks()
    selected = [meta for candidate, meta, _ in tasks if candidate == path]
    if len(selected) != 1:
        return [f"{path.name}: mutation target is not unique"]
    errors = basic_task_errors(path, selected[0])
    errors.extend(claim_errors(selected[0], {}, {}, {}))
    errors.extend(mutation_global_errors(tasks))
    errors.extend(generated_view_errors(tasks))
    errors.extend(introduced_content_errors(before))
    return errors


def render_status_view(tasks: list[Task]) -> str:
    """Render the public task dashboard with coordinator presentation constants."""
    return render_status(tasks, STATUSES, PRIORITIES, str(project_settings()["project_title"]))


def render_status_views(tasks: list[Task]) -> dict[str, str]:
    """Render the complete status view through the compatibility render hook."""
    return render_status_pages_from_text(render_status_view(tasks))


def status_projection_errors(expected: dict[str, str]) -> list[str]:
    """Compare status pages and report missing, changed, or orphaned files."""
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


def generated_view_errors(tasks: list[Task]) -> list[str]:
    """Check both task-derived views without allowing renderer errors to escape."""
    errors: list[str] = []
    if not all(meta.get("status") in STATUSES for _, meta, _ in tasks):
        return errors
    current = ROOT / "CURRENT.md"
    if current.exists() and current.read_text() != render_current(tasks):
        errors.append("CURRENT.md differs from generated tasks")
    if not project_settings()["status_view"]:
        return errors
    try:
        expected_status = render_status_views(tasks)
    except StatusRenderError as error:
        errors.extend(str(error).splitlines())
    else:
        errors.extend(status_projection_errors(expected_status))
    return errors


def rollback_validation_errors() -> list[str]:
    """Validate the durable rollback journal independently from task views."""
    try:
        for record in load_records(ROOT):
            validate_record(record)
    except (OSError, ValueError, RuntimeError) as error:
        return [f"rollback validation failed: {error}"]
    return []


def session_validation_errors() -> list[str]:
    """Validate every authoritative session record on the selected backend."""
    try:
        for record in storage_backend().load_session_records():
            validate_session_record(record)
    except (OSError, ValueError, RuntimeError) as error:
        return [f"session validation failed: {error}"]
    return []


def directive_validation_errors() -> list[str]:
    """Validate the bounded directive journal and its active precedence rules."""
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


def validate(*, live: bool = False) -> list[str]:
    errors: list[str] = []
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
        errors.extend(basic_task_errors(path, meta))
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
        state = project_scan()
        project, worktrees = live_docs(state)
        if (
            not (ROOT / "PROJECT_STATE.md").exists()
            or (ROOT / "PROJECT_STATE.md").read_text() != project
        ):
            errors.append("PROJECT_STATE.md is stale")
        if not (ROOT / "WORKTREES.md").exists() or (ROOT / "WORKTREES.md").read_text() != worktrees:
            errors.append("WORKTREES.md is stale")
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
        command = ["git", "-C", str(ROOT), "commit", "-S"]
        if project_settings()["commit_signoff"]:
            command.append("-s")
        run([*command, "-m", message, "--only", "--", *relative], capture=False)
        return True
    except Exception:
        run(["git", "-C", str(ROOT), "reset", "--", *relative], check=False)
        raise


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
    """Persist a privacy-safe circuit-breaker marker for reconciliation services."""
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
    """Clear a replica circuit breaker after verified ancestry recovery."""
    REPLICA_BLOCKED.unlink(missing_ok=True)


def sync_replica_before_write() -> None:
    """Fast-forward a clean behind replica before creating coordinator state."""
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
    """Restore a pre-transaction snapshot after a detected failure."""
    for path, old in before.items():
        if old is None:
            path.unlink(missing_ok=True)
        else:
            atomic(path, old)


def generated_paths() -> list[Path]:
    """Return every configured generated projection path."""
    names = ["CURRENT.md", "PROJECT_STATE.md", "WORKTREES.md"]
    if project_settings()["status_view"]:
        names.append("STATUS.md")
        names.extend(
            str(path.relative_to(ROOT)) for path in sorted((ROOT / "status").glob("STATUS-*.md"))
        )
    return [ROOT / name for name in names]


def changed_paths(before: dict[Path, str | None], *, include_deleted: bool = False) -> list[Path]:
    """Return paths whose current text differs from the captured snapshot."""
    return [
        path
        for path, old in before.items()
        if (include_deleted or path.exists())
        and (path.read_text() if path.exists() else None) != old
    ]


def write_generated_views(tasks: list[Task], state: Meta) -> None:
    """Atomically refresh every configured generated projection."""
    atomic(ROOT / "CURRENT.md", render_current(tasks))
    if project_settings()["status_view"]:
        expected = render_status_views(tasks)
        write_status_views(expected)
    project, worktrees = live_docs(state)
    atomic(ROOT / "PROJECT_STATE.md", project)
    atomic(ROOT / "WORKTREES.md", worktrees)


def reconcile(*, do_commit: bool, push: bool = False) -> bool:
    if backend_selection()["backend"] == "sqlite":
        return reconcile_sqlite(do_commit=do_commit, push=push)

    with locked():
        if backend_selection()["backend"] != "git":
            raise RuntimeError("BACKEND_CHANGED: retry using the selected backend")
        sync_replica_before_write()
        state = project_scan()
        generated = generated_paths()
        before: dict[Path, str | None] = {path: path.read_text() for path, _, _ in all_tasks()}
        before.update({path: path.read_text() if path.exists() else None for path in generated})
        committed = False
        try:
            sync_task_observations(all_tasks(), state)
            tasks = all_tasks()
            write_generated_views(tasks, state)
            errors = validate(live=False)
            if errors:
                raise RuntimeError("validation failed:\n" + "\n".join(errors))
            for path in generated_paths():
                before.setdefault(path, None)
            touched = changed_paths(before, include_deleted=True)
            title = project_settings()["project_title"]
            committed = commit(f"chore(state): reconcile {title}", touched) if do_commit else False
            head = run(["git", "-C", str(ROOT), "rev-parse", "HEAD"], check=False).stdout.strip()
            if push:
                push_replica()
            atomic(
                RUNTIME / "last-reconcile.json",
                json.dumps(
                    {"at": now(), "state_commit": head, "project_main": state["remote_main"]},
                    indent=2,
                )
                + "\n",
            )
            return committed if do_commit else True
        except Exception:
            if not committed:
                restore_paths(before)
            raise


def write_session_projections(session_records: list[Meta]) -> list[Path]:
    """Render bounded session histories from authoritative records."""
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
    """Render bounded checkpoint histories from authoritative SQLite records."""
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


def write_sqlite_projections(tasks: list[Task], *, already_locked: bool = False) -> list[Path]:
    """Regenerate byte-stable Markdown projections from one database snapshot."""
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
        errors = validate(live=False)
        if errors:
            raise RuntimeError("projection validation failed:\n" + "\n".join(errors))
        backend = storage_backend()
        session_records = backend.load_session_records()
        session_paths = write_session_projections(session_records)
        checkpoint_records = backend.load_checkpoint_records()
        checkpoint_paths = write_checkpoint_projections(checkpoint_records)
        return [
            *[path for path, _, _ in tasks],
            *views,
            *session_paths,
            *checkpoint_paths,
        ]


def export_sqlite_projections() -> list[Path]:
    """Regenerate projections from the currently selected SQLite authority."""
    return write_sqlite_projections(all_tasks())


def refresh_sqlite_live_state() -> State | None:
    """Refresh live observations when the private runtime is configured."""
    if not (CONFIG.exists() and config().get("github_repository")):
        return None
    state = project_scan()
    backend = mutating_sqlite_backend()
    backend.update_observations({item["key"]: item for item in state["worktrees"]}, now())
    return state


def reconcile_sqlite(*, do_commit: bool, push: bool) -> bool:
    """Export local authority; optional Git/GitHub publication is a replica only."""
    if push and not do_commit:
        raise RuntimeError("SQLite publication requires --commit with --push")
    before: dict[Path, str | None] = {path: path.read_text() for path in TASKS.glob("AR-*.md")}
    before.update({path: path.read_text() for path in (ROOT / "sessions").glob("AR-*.jsonl")})
    before.update({path: path.read_text() for path in (ROOT / "checkpoints").glob("AR-*.jsonl")})
    before.update({path: path.read_text() if path.exists() else None for path in generated_paths()})
    state = refresh_sqlite_live_state()
    paths = export_sqlite_projections()
    if state is not None:
        project, worktrees = live_docs(state)
        atomic(ROOT / "PROJECT_STATE.md", project)
        atomic(ROOT / "WORKTREES.md", worktrees)
        paths.extend((ROOT / "PROJECT_STATE.md", ROOT / "WORKTREES.md"))
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
    """Return whether one dependency is complete or explicitly superseded.

    A superseded task is not completion by itself. It satisfies a dependency
    only when its ``superseded_by`` field names an existing task that is done,
    or a finite chain of explicitly superseding tasks ending in one that is
    done. Malformed, missing, self-referential, cyclic, or unfinished
    successors therefore remain fail-closed and block the transition.
    """
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
    """Require a durable capability when the role workstream is initialized."""
    state_path = RUNTIME / "roles.json"
    if not state_path.exists():
        return
    try:
        if __package__:
            from .roles import role_admission_error as _role_admission_error
        else:  # pragma: no cover - direct script execution
            from roles import (  # type: ignore[import-not-found,no-redef]
                role_admission_error as _role_admission_error,
            )
        admission_error = _role_admission_error(
            state_path,
            ROOT / "examples/roles/role-registry.json",
            owner_id=owner_id,
            required_role=required_role,
        )
    except Exception as import_error:  # fail closed if the admission module is unavailable
        raise RuntimeError(f"role admission unavailable: {import_error}") from import_error
    if admission_error:
        raise RuntimeError(admission_error)


def require_update_role_admission(kind: str, owner_id: str) -> None:
    if kind in {"update", "pause"}:
        require_role_admission(owner_id)


def require_done_admission(meta: Meta, tasks: list[Task] | None = None) -> None:
    if meta.get("status") != "in_progress":
        return
    error = done_admission_error(ROOT, meta)
    if error:
        raise RuntimeError(error)
    if tasks is not None:
        hierarchy_error = open_child_error(meta, tasks)
        if hierarchy_error:
            raise RuntimeError(hierarchy_error)


def require_release_admission(
    kind: str, status: str | None, meta: Meta, tasks: list[Task] | None = None
) -> None:
    if kind == "release" and status == "done":
        require_done_admission(meta, tasks)


def apply_claim(args: argparse.Namespace, meta: Meta, tasks: list[Task]) -> str:
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
    meta["claim_expires"] = (
        (dt.datetime.now(dt.UTC) + dt.timedelta(minutes=args.lease_minutes))
        .replace(microsecond=0)
        .isoformat()
    )
    return f"Claimed by {args.owner}."


def dirty_state_paths() -> list[str]:
    """Return public state-repository changes that would make promotion ambiguous."""
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


def apply_recover_expired(args: argparse.Namespace, meta: Meta, _tasks: list[Task]) -> str:
    """Reopen an expired claim after restoring its latest bounded session."""
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
    records = storage_backend().load_session_records(args.task)
    if not records:
        raise RuntimeError(f"no session snapshot for {args.task}")
    session = records[-1]
    validate_session_record(session)
    if session["task_revision"] > meta["task_revision"]:
        raise RuntimeError("session snapshot revision is newer than the task")
    previous_owner = str(meta["owner"])
    meta["next_action"] = str(session["next_action"])
    meta["status"] = "open"
    meta["owner"] = ""
    meta["claim_expires"] = ""
    return f"Recovered expired claim formerly owned by {previous_owner}. {args.note}"


def require_promotion_preflight(kind: str) -> None:
    """Reject a promotion before writes when its source checkout is ambiguous."""
    if kind not in ("promote", "resume", "unblock"):
        return
    errors = generated_view_errors(all_tasks())
    if errors:
        raise RuntimeError("promotion preflight failed:\n" + "\n".join(errors))
    if dirty_state_paths():
        raise RuntimeError("promotion requires a clean state repository")


def apply_owned_change(  # noqa: C901
    args: argparse.Namespace, kind: str, meta: Meta, tasks: list[Task] | None = None
) -> str:
    if meta.get("owner") != args.owner:
        raise RuntimeError(f"{args.task} is owned by {meta.get('owner') or 'nobody'}")
    require_update_role_admission(kind, str(args.owner))
    require_release_admission(kind, getattr(args, "status", None), meta, tasks)
    if kind == "heartbeat":
        if args.lease_minutes <= 0 or meta.get("status") != "in_progress":
            raise RuntimeError("heartbeat requires an active task and positive lease")
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
    return str(args.note)


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


def apply_gate(args: argparse.Namespace, meta: Meta) -> str:
    """Record one typed interaction event as the task's next revision."""
    try:
        try:
            stage = GateStage(str(args.stage))
        except ValueError as error:
            raise GateError("unknown interaction gate stage") from error
        event = InteractionEvent(
            task_id=str(meta["id"]),
            task_revision=int(args.expected_revision),
            stage=stage,
            action=str(args.action),
            disposition=str(args.disposition),
            before=_artifact_values(args.before, "--before"),
            after=_artifact_values(args.after, "--after"),
            public_ref=str(args.public_ref),
            recorded_at=now(),
        )
        return apply_event(meta, event)
    except (GateError, ValueError) as error:
        raise RuntimeError(str(error)) from error


def apply_transition(args: argparse.Namespace, kind: str, meta: Meta, tasks: list[Task]) -> str:
    """Dispatch one typed lifecycle transition for both storage backends."""
    if kind == "claim":
        return apply_claim(args, meta, tasks)
    if kind == "promote":
        return apply_promote(args, meta, tasks)
    if kind == "pause":
        return apply_pause(args, meta)
    reopen = {"resume": apply_resume, "unblock": apply_unblock}.get(kind)
    if reopen is not None:
        return reopen(args, meta, tasks)
    if kind == "recover-expired":
        return apply_recover_expired(args, meta, tasks)
    if kind == "gate":
        return apply_gate(args, meta)
    if kind == "checkpoint":
        return apply_checkpoint(args, meta)
    if kind == "rollback":
        return apply_rollback(args, meta)
    return apply_owned_change(args, kind, meta, tasks)


def rendered_task_views(tasks: list[Task]) -> dict[Path, str]:
    """Return every enabled task-derived projection for one consistent task snapshot."""
    views = {ROOT / "CURRENT.md": render_current(tasks)}
    if project_settings()["status_view"]:
        views.update(
            {ROOT / relative: content for relative, content in render_status_views(tasks).items()}
        )
    return views


def write_status_views(views: dict[str, str]) -> None:
    """Atomically replace the root status index and remove obsolete shards."""
    expected_paths = {ROOT / relative for relative in views}
    for path in generated_paths():
        if path not in expected_paths and (
            path.name == "STATUS.md" or path.parent.name == "status"
        ):
            path.unlink(missing_ok=True)
    for relative, content in views.items():
        atomic(ROOT / relative, content)


def write_rendered_task_views(views: dict[Path, str]) -> None:
    """Write all task views while pruning obsolete status shards."""
    status_views = {
        str(target.relative_to(ROOT)): content
        for target, content in views.items()
        if target.name == "STATUS.md" or target.parent.name == "status"
    }
    write_status_views(status_views)
    for target, content in views.items():
        if target.name != "STATUS.md" and target.parent.name != "status":
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


def mutate(args: argparse.Namespace, kind: str) -> None:  # noqa: C901
    if backend_selection()["backend"] == "sqlite":
        mutate_sqlite(args, kind)
        return
    with locked():
        if backend_selection()["backend"] != "git":
            raise RuntimeError("BACKEND_CHANGED: retry using the selected backend")
        sync_replica_before_write()
        path, meta, body = locate(args.task)
        require_promotion_preflight(kind)
        before: dict[Path, str | None] = {path: path.read_text()}
        before.update(
            {
                target: target.read_text() if target.exists() else None
                for target in generated_paths()
            }
        )
        committed = False
        note = apply_transition(args, kind, meta, all_tasks())
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
        try:
            if session_record is not None:
                append_session_record(ROOT, session_record)
            if checkpoint_record is not None:
                append_checkpoint(ROOT, checkpoint_record)
            write_task(path, meta, body)
            views = rendered_task_views(all_tasks())
            write_rendered_task_views(views)
            errors = mutation_errors(path, before)
            if errors:
                raise RuntimeError("\n".join(errors))
            for target in generated_paths():
                before.setdefault(target, None)
            touched = changed_paths(before, include_deleted=True)
            committed = commit(f"chore(state): {kind} {args.task}", touched)
            push_replica()
        except Exception:
            # A signed local commit is already durable even when replication fails.
            # Keep its worktree representation intact so a later reconcile can safely
            # inspect and retry the push instead of silently rolling state backward.
            if not committed:
                restore_paths(before)
            raise


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


def mutate_sqlite(args: argparse.Namespace, kind: str) -> None:
    """Linearize a lifecycle mutation at SQLite's committed CAS update."""
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
        note = apply_transition(args, kind, meta, tasks)
        candidate = [
            (path, meta if item["id"] == args.task else item, text) for path, item, text in tasks
        ]
        errors = (
            basic_task_errors(selected[0], meta)
            + graph_errors(candidate)
            + hierarchy_errors(candidate)
            + supersession_errors(candidate)
        )
        if errors:
            raise RuntimeError("transition validation failed:\n" + "\n".join(errors))
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
        export_sqlite_projections()
    except Exception as error:
        raise StorageCommittedError(
            f"SQLITE_COMMITTED_EXPORT_FAILED: task={args.task}; revision={expected + 1}; {error}"
        ) from error


def cmd_render_status(*, check: bool) -> None:
    """Render STATUS.md or fail if its checked-in form is stale."""
    if not project_settings()["status_view"]:
        raise RuntimeError("STATUS.md generation is disabled by .handoffctl.json")
    with locked(exclusive=not check):
        expected = render_status_views(all_tasks())
        if check:
            if status_projection_errors(expected):
                raise RuntimeError("STATUS.md differs from generated tasks")
            return
        write_status_views(expected)


def role_doctor_errors() -> list[str]:
    if not (RUNTIME / "roles.json").exists():
        return []
    try:
        if __package__:
            from .roles import role_admission_errors as _role_admission_errors
        else:  # pragma: no cover - direct script execution
            from roles import (  # type: ignore[no-redef]
                role_admission_errors as _role_admission_errors,
            )
        active_roles = [
            (str(meta.get("owner")), "implementer")
            for _, meta, _ in all_tasks()
            if meta.get("status") == "in_progress" and meta.get("owner")
        ]
        return _role_admission_errors(
            RUNTIME / "roles.json",
            ROOT / "examples/roles/role-registry.json",
            active_roles,
        )
    except Exception as error:
        return [f"role admission unavailable: {error}"]


def cmd_doctor(*, live: bool) -> int:
    """Validate static state and optionally compare the live generated views."""
    sqlite = backend_selection()["backend"] == "sqlite"
    sqlite_live = CONFIG.exists() and bool(config().get("github_repository"))
    errors = validate(live=live and (not sqlite or sqlite_live))
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
    with locked(exclusive=False):
        sqlite = backend_selection()["backend"] == "sqlite"
        sqlite_live = CONFIG.exists() and bool(config().get("github_repository"))
        errors = validate(live=not sqlite or sqlite_live)
        if errors:
            raise RuntimeError("snapshot refused:\n" + "\n".join(errors))
        if sqlite:
            print("STORAGE_BACKEND=sqlite")
        else:
            print(
                "STATE_COMMIT=" + run(["git", "-C", str(ROOT), "rev-parse", "HEAD"]).stdout.strip()
            )
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
            print("SESSION_SNAPSHOT=" + json.dumps(record, sort_keys=True, separators=(",", ":")))


def cmd_board() -> None:
    """Print the privacy-safe company board from the SQLite authority."""
    if backend_selection()["backend"] != "sqlite":
        raise RuntimeError("board requires the SQLite authority")
    with locked(exclusive=False):
        print(encode_metrics(build_metrics(all_tasks())), end="")


def cmd_metrics() -> None:
    """Print the deterministic metrics projection from the SQLite authority."""
    if backend_selection()["backend"] != "sqlite":
        raise RuntimeError("metrics requires the SQLite authority")
    with locked(exclusive=False):
        print(encode_metrics(build_metrics(all_tasks())), end="")


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
            "-S",
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
    checkpoint, product, current_commit, previous = _rollback_target(args)
    started, skip_product = _start_rollback(args, checkpoint, product, current_commit, previous)
    try:
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
        mutate(args, "rollback")
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
    reconcile(do_commit=True, push=True)


def require_active_owner(task_id: str, owner: str) -> None:
    """Fence wrapped commands with a live claim before external effects."""
    with locked(exclusive=False):
        _, meta, _ = locate(task_id)
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


def invocation_worktree() -> tuple[str, str] | None:
    """Return the product worktree identity when called from a product checkout.

    The coordinator itself is normally invoked from the bound state repository, so
    that location remains valid for state-only commands.  When a caller starts in
    the configured product checkout, identify the actual Git root and branch so an
    active task can be fenced to its declared worktree.
    """
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
    """Reject product-checkout calls that do not match the active task claim."""
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
    """Fsync a privacy-safe local result before any fallible post-command work."""
    RUNTIME.mkdir(mode=0o700, parents=True, exist_ok=True)
    record = {
        "at": recorded_at,
        "task": task_id,
        "owner": owner,
        "argv_sha256": command_hash,
        "returncode": returncode,
        "classification": classification,
    }
    path = RUNTIME / "command-results.jsonl"
    descriptor = os.open(path, os.O_APPEND | os.O_CREAT | os.O_WRONLY, 0o600)
    with os.fdopen(descriptor, "ab") as stream:
        stream.write((json.dumps(record, sort_keys=True) + "\n").encode())
        stream.flush()
        os.fsync(stream.fileno())


def legacy_command_results() -> list[Meta]:
    """Strictly load the privacy-safe Git-backend journal for migration."""
    path = RUNTIME / "command-results.jsonl"
    if not path.exists():
        return []
    required = {"at", "task", "owner", "argv_sha256", "returncode", "classification"}
    records: list[Meta] = []
    for number, line in enumerate(path.read_text().splitlines(), 1):
        try:
            record = json.loads(line)
        except json.JSONDecodeError as error:
            raise RuntimeError(f"invalid command journal line {number}") from error
        if not isinstance(record, dict) or set(record) != required:
            raise RuntimeError(f"invalid command journal line {number}")
        if not re.fullmatch(r"[0-9a-f]{64}", str(record["argv_sha256"])):
            raise RuntimeError(f"invalid command journal digest at line {number}")
        if not isinstance(record["returncode"], int):
            raise RuntimeError(f"invalid command journal return code at line {number}")
        records.append(cast(Meta, record))
    return records


def append_command_result(
    task_id: str,
    owner: str,
    command_hash: str,
    returncode: int,
    timed_out: bool,
) -> None:
    """Record through the selected backend before any fallible follow-up."""
    selected_backend = (
        mutating_sqlite_backend()
        if backend_selection()["backend"] == "sqlite"
        else storage_backend()
    )
    selected_backend.append_command_result(
        task_id,
        owner,
        command_hash,
        returncode,
        "SUBPROCESS_TIMEOUT" if timed_out else "EXIT",
        now(),
    )


def cmd_run(args: argparse.Namespace) -> int:
    if not args.command:
        raise RuntimeError("missing command")
    if backend_selection()["backend"] == "git":
        config()
    require_active_owner(args.task, args.owner)
    # Never execute or consume untracked caller input. Scripts and data must be
    # named by argv or a stable file, whose content digest can be recorded too.
    command_hash = hashlib.sha256("\0".join(args.command).encode()).hexdigest()
    timeout = float(getattr(args, "timeout_seconds", COMMAND_TIMEOUT_SECONDS))
    if timeout <= 0:
        raise RuntimeError("command timeout must be positive")
    timed_out = False
    try:
        proc = subprocess.run(args.command, check=False, stdin=subprocess.DEVNULL, timeout=timeout)
    except subprocess.TimeoutExpired:
        timed_out = True
        returncode = 124
    else:
        returncode = proc.returncode
    append_command_result(
        args.task,
        args.owner,
        command_hash,
        returncode,
        timed_out,
    )
    note = (
        f"Recorded command timeout; classification=SUBPROCESS_TIMEOUT; "
        f"deadline={timeout:.1f}s; command argv SHA-256 {command_hash}."
        if timed_out
        else f"Recorded command exit {returncode}; command argv SHA-256 {command_hash}."
    )
    update = argparse.Namespace(
        task=args.task,
        owner=args.owner,
        expected_revision=None,
        status=None,
        priority=None,
        summary=None,
        next_action=None,
        note=note,
        _session_trigger="run",
    )
    mutate(update, "update")
    sqlite = backend_selection()["backend"] == "sqlite"
    try:
        reconcile(do_commit=not sqlite, push=not sqlite)
    except Exception as error:
        raise PostCommandReconcileError(
            "COMMAND_RECORDED_POST_RECONCILE_FAILED: "
            f"task={args.task}; argv_sha256={command_hash}; {error}"
        ) from error
    return returncode


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
        export_sqlite_projections()
    print(f"Initialized project binding {project_id} with {selected_backend} backend")


def cmd_migrate(args: argparse.Namespace) -> None:  # noqa: C901
    """Explicitly and restart-safely switch authority between supported backends."""
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
            errors = validate(live=False)
            if errors:
                raise RuntimeError("migration preflight failed:\n" + "\n".join(errors))
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
                provision_sqlite_barrier()
                atomic(BACKEND_CONFIG, json.dumps(selection, indent=2, sort_keys=True) + "\n")
            except Exception:
                DATABASE.unlink(missing_ok=True)
                raise
        export_sqlite_projections()
    else:
        backend = mutating_sqlite_backend()

        def project(tasks: list[Task]) -> None:
            write_sqlite_projections(tasks, already_locked=True)

        def switch() -> None:
            errors = validate(live=False)
            if errors:
                raise RuntimeError("rollback export failed:\n" + "\n".join(errors))
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
        else:  # pragma: no cover - direct script execution
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
        else:  # pragma: no cover - direct script execution
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
    if __package__:
        from .roles import RolesError
        from .roles import assign as assign_role
        from .roles import check as check_roles
        from .roles import list_assignments as list_roles
        from .roles import remove as remove_role
    else:  # pragma: no cover - direct script execution
        from roles import RolesError  # type: ignore[no-redef]
        from roles import assign as assign_role  # type: ignore[no-redef]
        from roles import check as check_roles  # type: ignore[no-redef]
        from roles import list_assignments as list_roles  # type: ignore[no-redef]
        from roles import remove as remove_role  # type: ignore[no-redef]
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
    except RolesError as error:
        raise RuntimeError(str(error)) from error
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))
    return 0


def dispatch_read_only_command(args: argparse.Namespace) -> None:
    """Dispatch read-only projections without inflating the mutation dispatcher."""
    if args.cmd == "snapshot":
        cmd_snapshot(args.task)
    elif args.cmd == "board":
        cmd_board()
    else:
        cmd_metrics()


def dispatch_bound_command(args: argparse.Namespace) -> int:  # noqa: C901
    """Dispatch a command only after the permanent project binding has passed."""
    if args.cmd == "reconcile":
        reconcile(do_commit=args.commit, push=args.push)
    elif args.cmd == "roles":
        return dispatch_roles_command(args)
    elif args.cmd in ("snapshot", "board", "metrics"):
        dispatch_read_only_command(args)
    elif args.cmd == "checkpoint":
        cmd_checkpoint(args)
    elif args.cmd == "rollback":
        cmd_rollback(args)
    elif args.cmd == "doctor":
        return cmd_doctor(live=args.live)
    elif args.cmd == "render-status":
        cmd_render_status(check=args.check)
    elif args.cmd in (
        *LIFECYCLE_MUTATION_COMMANDS,
        "gate",
    ):
        mutate(args, args.cmd)
    elif args.cmd == "run":
        if args.command and args.command[0] == "--":
            args.command = args.command[1:]
        return cmd_run(args)
    elif args.cmd == "migrate":
        cmd_migrate(args)
    elif args.cmd == "upgrade":
        return cmd_upgrade(args)
    return 0


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
    commands.add_parser("board")
    commands.add_parser("metrics")
    item = commands.add_parser("checkpoint")
    item.add_argument("task")
    item.add_argument("--owner", required=True)
    item.add_argument("--expected-revision", type=int, required=True)
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
    item = commands.add_parser("release")
    item.add_argument("task")
    item.add_argument("--owner", required=True)
    item.add_argument(
        "--status", required=True, choices=[value for value in STATUSES if value != "in_progress"]
    )
    item.add_argument("--note", required=True)
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
    item = commands.add_parser("run")
    item.add_argument("task")
    item.add_argument("--owner", required=True)
    item.add_argument("--timeout-seconds", type=float, default=COMMAND_TIMEOUT_SECONDS)
    item.add_argument("command", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    if args.cmd == "init":
        cmd_init(args)
        return 0
    assert_project_binding()
    if args.cmd == "directive":
        cmd_directive(args)
        return 0
    return dispatch_bound_command(args)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        print(f"ERROR: {error}", file=sys.stderr)
        raise SystemExit(1) from error
