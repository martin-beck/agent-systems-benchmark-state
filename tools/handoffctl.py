#!/usr/bin/env python3
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
import time
import uuid
from collections.abc import Iterator
from pathlib import Path
from typing import Any, cast

from status_renderer import StatusRenderError, graph_errors, render_status

ROOT = Path(__file__).resolve().parent.parent
TASKS = ROOT / "tasks"
RUNTIME = ROOT / ".runtime"
LOCK = RUNTIME / "state.lock"
CONFIG = RUNTIME / "config.json"
PROJECT_CONFIG = ROOT / ".handoffctl.json"
BINDING = ROOT / "coordinator.binding.json"
LOCK_TIMEOUT_SECONDS = 10.0
LOCK_POLL_SECONDS = 0.05
SUBPROCESS_TIMEOUT_SECONDS = 30.0
COMMAND_TIMEOUT_SECONDS = 1800.0
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
    "claim_expires",
    "worktree_key",
    "branch",
    "checkpoint_commit",
    "plan",
    "depends_on",
    "observed_branch",
    "observed_head",
    "observed_dirty",
}
type Meta = dict[str, Any]
type Task = tuple[Path, Meta, str]
type State = dict[str, Any]

COORDINATOR_VERSION = "0.1.3"
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


def assert_project_binding() -> None:
    """Fail closed when this initialized coordinator is called from another project."""
    settings = project_settings()
    binding = project_binding()
    if settings["project_id"] != binding["project_id"]:
        raise RuntimeError("project profile does not match coordinator binding")
    top = Path(run(["git", "-C", str(ROOT), "rev-parse", "--show-toplevel"]).stdout.strip())
    if top.resolve() != ROOT.resolve():
        raise RuntimeError("handoffctl is not installed at its bound state repository root")
    if git_repository_slug(ROOT) != repository_slug(binding["state_repository"]):
        raise RuntimeError("state repository does not match coordinator binding")
    allowed = [ROOT.resolve()]
    if CONFIG.exists():
        runtime = config()
        if repository_slug(runtime.get("github_repository")) != repository_slug(
            binding["product_repository"]
        ):
            raise RuntimeError("runtime product repository does not match coordinator binding")
        product = Path(str(runtime["projects_root"])) / str(runtime["product_worktree"])
        if git_repository_slug(product) != repository_slug(binding["product_repository"]):
            raise RuntimeError("product checkout does not match coordinator binding")
        allowed.append(product.resolve())
    current = Path.cwd().resolve()
    if not any(inside(current, root) for root in allowed):
        raise RuntimeError("handoffctl must be called from its bound state or product project")


class LockTimeoutError(RuntimeError):
    """The coordinator lock could not be acquired within its bounded deadline."""


class SubprocessTimeoutError(RuntimeError):
    """A Git/GitHub or coordinator command exceeded its bounded deadline."""


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
        Path("tests/test_handoffctl.py"),
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


@contextlib.contextmanager
def locked(*, exclusive: bool = True, timeout: float = LOCK_TIMEOUT_SECONDS) -> Iterator[None]:
    RUNTIME.mkdir(mode=0o700, exist_ok=True)
    fd = os.open(LOCK, os.O_CREAT | os.O_RDWR, 0o600)
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
        yield
    finally:
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


def all_tasks() -> list[Task]:
    result: list[Task] = []
    for path in sorted(TASKS.glob("AR-*.md")):
        meta, body = read_task(path)
        result.append((path, meta, body))
    return result


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

    for status in STATUSES:
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
    raw = run(["git", "-C", str(repo), "worktree", "list", "--porcelain"]).stdout
    paths = [Path(line[9:]) for line in raw.splitlines() if line.startswith("worktree ")]
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
        run(
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
        run(
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


def basic_task_errors(path: Path, meta: Meta) -> list[str]:
    return [*field_errors(path, meta), *value_errors(path, meta), *reference_errors(path, meta)]


def active_expiry_errors(task_id: str, expiry: object) -> list[str]:
    if not expiry:
        return [f"{task_id}: active without claim"]
    if not isinstance(expiry, str):
        return [f"{task_id}: invalid claim expiry"]
    try:
        parsed_expiry = dt.datetime.fromisoformat(expiry.replace("Z", "+00:00"))
        if parsed_expiry.tzinfo is None:
            raise ValueError
    except ValueError:
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


def render_status_view(tasks: list[Task]) -> str:
    """Render the public task dashboard with coordinator presentation constants."""
    return render_status(tasks, STATUSES, PRIORITIES, str(project_settings()["project_title"]))


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
        expected_status = render_status_view(tasks)
    except StatusRenderError as error:
        errors.extend(str(error).splitlines())
    else:
        status = ROOT / "STATUS.md"
        if not status.exists() or status.read_text() != expected_status:
            errors.append("STATUS.md differs from generated tasks")
    return errors


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
    errors.extend(generated_view_errors(tasks))
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
    run(["git", "-C", str(ROOT), "add", "--", *relative])
    try:
        if (
            run(["git", "-C", str(ROOT), "diff", "--cached", "--quiet"], check=False).returncode
            == 0
        ):
            return False
        command = ["git", "-C", str(ROOT), "commit", "-S"]
        if project_settings()["commit_signoff"]:
            command.append("-s")
        run([*command, "-m", message], capture=False)
        return True
    except Exception:
        run(["git", "-C", str(ROOT), "reset", "--", *relative], check=False)
        raise


def push_replica() -> None:
    if not CONFIG.exists():
        return
    if not config().get("push_enabled", False):
        return
    remote = run(["git", "-C", str(ROOT), "remote", "get-url", "origin"], check=False)
    if remote.returncode:
        raise RuntimeError("state replication is enabled but origin is missing")
    run(["git", "-C", str(ROOT), "fetch", "--no-tags", "origin", "main"])
    local_head = run(["git", "-C", str(ROOT), "rev-parse", "HEAD"]).stdout.strip()
    remote_head = run(["git", "-C", str(ROOT), "rev-parse", "FETCH_HEAD"]).stdout.strip()
    if local_head == remote_head:
        return
    ancestry = run(
        ["git", "-C", str(ROOT), "merge-base", "--is-ancestor", remote_head, local_head],
        check=False,
    )
    if ancestry.returncode:
        raise RuntimeError("state replica diverged; refusing non-fast-forward push")
    run(["git", "-C", str(ROOT), "push", "origin", f"{local_head}:refs/heads/main"])


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
    return [ROOT / name for name in names]


def write_generated_views(tasks: list[Task], state: Meta) -> None:
    """Atomically refresh every configured generated projection."""
    atomic(ROOT / "CURRENT.md", render_current(tasks))
    if project_settings()["status_view"]:
        atomic(ROOT / "STATUS.md", render_status_view(tasks))
    project, worktrees = live_docs(state)
    atomic(ROOT / "PROJECT_STATE.md", project)
    atomic(ROOT / "WORKTREES.md", worktrees)


def reconcile(*, do_commit: bool, push: bool = False) -> bool:

    with locked():
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
            touched = [
                path for path, old in before.items() if path.exists() and path.read_text() != old
            ]
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


def locate(task_id: str) -> Task:
    for path, meta, body in all_tasks():
        if meta["id"] == task_id:
            return path, meta, body
    raise RuntimeError(f"unknown task {task_id}")


def apply_claim(args: argparse.Namespace, meta: Meta, tasks: list[Task]) -> str:
    if args.lease_minutes <= 0:
        raise RuntimeError("lease must be positive")
    if meta.get("status") != "open":
        raise RuntimeError(f"{args.task} is not open")
    states = {item["id"]: item["status"] for _, item, _ in tasks}
    pending = [item for item in meta.get("depends_on", []) if states.get(item) != "done"]
    if pending:
        raise RuntimeError("unfinished dependencies: " + ", ".join(pending))
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
    states = {item["id"]: item["status"] for _, item, _ in tasks}
    pending = [item for item in meta.get("depends_on", []) if states.get(item) != "done"]
    if pending:
        raise RuntimeError("unfinished dependencies: " + ", ".join(pending))
    if not args.note.strip():
        raise RuntimeError("promotion note must not be empty")
    meta["status"] = "open"
    return str(args.note)


def apply_resume(args: argparse.Namespace, meta: Meta, _tasks: list[Task]) -> str:
    """Reopen a blocked task after an explicit coordinator review."""
    if args.expected_revision != meta["task_revision"]:
        raise RuntimeError(
            f"stale revision: expected {args.expected_revision}, current {meta['task_revision']}"
        )
    if meta.get("status") != "blocked":
        raise RuntimeError(f"{args.task} is not blocked")
    if meta.get("owner") or meta.get("claim_expires"):
        raise RuntimeError(f"{args.task} has active claim metadata")
    if not args.note.strip():
        raise RuntimeError("resume note must not be empty")
    meta["status"] = "open"
    return str(args.note)


def require_promotion_preflight(kind: str) -> None:
    """Reject a promotion before writes when its source checkout is ambiguous."""
    if kind not in ("promote", "resume"):
        return
    errors = validate(live=False)
    if errors:
        raise RuntimeError("promotion preflight failed:\n" + "\n".join(errors))
    if dirty_state_paths():
        raise RuntimeError("promotion requires a clean state repository")


def apply_owned_change(args: argparse.Namespace, kind: str, meta: Meta) -> str:
    if meta.get("owner") != args.owner:
        raise RuntimeError(f"{args.task} is owned by {meta.get('owner') or 'nobody'}")
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


def rendered_task_views(tasks: list[Task]) -> dict[Path, str]:
    """Return every enabled task-derived projection for one consistent task snapshot."""
    views = {ROOT / "CURRENT.md": render_current(tasks)}
    if project_settings()["status_view"]:
        views[ROOT / "STATUS.md"] = render_status_view(tasks)
    return views


def mutate(args: argparse.Namespace, kind: str) -> None:
    with locked():
        path, meta, body = locate(args.task)
        require_promotion_preflight(kind)
        view_paths = rendered_task_views(all_tasks())
        before: dict[Path, str | None] = {path: path.read_text()}
        before.update(
            {target: target.read_text() if target.exists() else None for target in view_paths}
        )
        committed = False
        note = (
            apply_claim(args, meta, all_tasks())
            if kind == "claim"
            else (
                apply_promote(args, meta, all_tasks())
                if kind == "promote"
                else apply_resume(args, meta, all_tasks())
                if kind == "resume"
                else apply_owned_change(args, kind, meta)
            )
        )
        meta["task_revision"] += 1
        meta["updated_at"] = now()
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
            write_task(path, meta, body)
            views = rendered_task_views(all_tasks())
            for target, content in views.items():
                atomic(target, content)
            errors = validate(live=False)
            if errors:
                raise RuntimeError("\n".join(errors))
            committed = commit(f"chore(state): {kind} {args.task}", [path, *views])
            push_replica()
        except Exception:
            # A signed local commit is already durable even when replication fails.
            # Keep its worktree representation intact so a later reconcile can safely
            # inspect and retry the push instead of silently rolling state backward.
            if not committed:
                restore_paths(before)
            raise


def cmd_render_status(*, check: bool) -> None:
    """Render STATUS.md or fail if its checked-in form is stale."""
    if not project_settings()["status_view"]:
        raise RuntimeError("STATUS.md generation is disabled by .handoffctl.json")
    with locked(exclusive=not check):
        expected = render_status_view(all_tasks())
        path = ROOT / "STATUS.md"
        if check:
            if not path.exists() or path.read_text() != expected:
                raise RuntimeError("STATUS.md differs from generated tasks")
            return
        atomic(path, expected)


def cmd_doctor(*, live: bool) -> int:
    """Validate static state and optionally compare the live generated views."""
    errors = validate(live=live)
    if errors:
        print("\n".join("ERROR: " + value for value in errors))
        return 1
    print(
        "OK: structure, references, privacy, generated views"
        + (" and live state" if live else "")
        + " are consistent"
    )
    return 0


def cmd_snapshot() -> None:
    with locked(exclusive=False):
        errors = validate(live=True)
        if errors:
            raise RuntimeError("snapshot refused:\n" + "\n".join(errors))
        print("STATE_COMMIT=" + run(["git", "-C", str(ROOT), "rev-parse", "HEAD"]).stdout.strip())
        print((ROOT / "CURRENT.md").read_text(), end="")


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


def cmd_run(args: argparse.Namespace) -> int:
    if not args.command:
        raise RuntimeError("missing command")
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
    note = (
        f"Recorded command timeout; classification=SUBPROCESS_TIMEOUT; "
        f"deadline={timeout:.1f}s; command argv SHA-256 {command_hash}."
        if timed_out
        else f"Recorded command exit {returncode}; command argv SHA-256 {command_hash}."
    )
    try:
        reconcile(do_commit=True, push=True)
    except (LockTimeoutError, SubprocessTimeoutError) as error:
        note += f" Reconciliation classification preserved: {error}."
    update = argparse.Namespace(
        task=args.task,
        owner=args.owner,
        expected_revision=None,
        status=None,
        priority=None,
        summary=None,
        next_action=None,
        note=note,
    )
    mutate(update, "update")
    return returncode


def cmd_init(args: argparse.Namespace) -> None:
    """Bind a fresh vendored coordinator permanently to one state/product pair."""
    if PROJECT_CONFIG.exists() or BINDING.exists():
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
    before: dict[Path, str | None] = {PROJECT_CONFIG: None, BINDING: None}
    try:
        atomic(PROJECT_CONFIG, json.dumps(settings, indent=2, sort_keys=True) + "\n")
        project_settings()
        atomic(BINDING, json.dumps(binding, indent=2, sort_keys=True) + "\n")
        project_binding()
    except Exception:
        restore_paths(before)
        raise
    print(f"Initialized project binding {project_id}")


def dispatch_bound_command(args: argparse.Namespace) -> int:
    """Dispatch a command only after the permanent project binding has passed."""
    if args.cmd == "reconcile":
        reconcile(do_commit=args.commit, push=args.push)
    elif args.cmd == "snapshot":
        cmd_snapshot()
    elif args.cmd == "doctor":
        return cmd_doctor(live=args.live)
    elif args.cmd == "render-status":
        cmd_render_status(check=args.check)
    elif args.cmd in ("claim", "heartbeat", "release", "promote", "resume", "update"):
        mutate(args, args.cmd)
    elif args.cmd == "run":
        if args.command and args.command[0] == "--":
            args.command = args.command[1:]
        return cmd_run(args)
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
    item = commands.add_parser("reconcile")
    item.add_argument("--commit", action="store_true")
    item.add_argument("--push", action="store_true")
    commands.add_parser("snapshot")
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
    return dispatch_bound_command(args)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        print(f"ERROR: {error}", file=sys.stderr)
        raise SystemExit(1) from error
