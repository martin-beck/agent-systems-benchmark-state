#!/usr/bin/env python3
"""Transactional coordination state for Agent Systems Benchmark."""

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
from collections.abc import Iterator
from pathlib import Path
from typing import Any, cast

ROOT = Path(__file__).resolve().parent.parent
TASKS = ROOT / "tasks"
RUNTIME = ROOT / ".runtime"
LOCK = RUNTIME / "state.lock"
CONFIG = RUNTIME / "config.json"
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


def now() -> str:
    return dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat()


def run(
    args: list[str],
    *,
    cwd: Path | None = None,
    check: bool = True,
    capture: bool = True,
) -> subprocess.CompletedProcess[str]:
    proc = subprocess.run(args, cwd=cwd, text=True, capture_output=capture, check=False)
    if check and proc.returncode:
        raise RuntimeError(f"command failed ({proc.returncode}): {' '.join(args)}\n{proc.stderr}")
    return proc


def config() -> Meta:
    if not CONFIG.exists():
        raise RuntimeError(f"missing private runtime config: {CONFIG}")
    return cast(Meta, json.loads(CONFIG.read_text()))


@contextlib.contextmanager
def locked(*, exclusive: bool = True) -> Iterator[None]:
    RUNTIME.mkdir(mode=0o700, exist_ok=True)
    fd = os.open(LOCK, os.O_CREAT | os.O_RDWR, 0o600)
    try:
        fcntl.flock(fd, fcntl.LOCK_EX if exclusive else fcntl.LOCK_SH)
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
        "# Agent Systems Benchmark current coordination state",
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
        "# Agent Systems Benchmark live project state",
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
        "# Agent Systems Benchmark worktree inventory",
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


def dependency_errors(tasks: list[Task], ids: set[str]) -> list[str]:
    errors: list[str] = []
    graph = {meta["id"]: meta.get("depends_on", []) for _, meta, _ in tasks}
    errors.extend(
        f"{task_id}: missing dependency {dependency}"
        for task_id, dependencies in graph.items()
        for dependency in dependencies
        if dependency not in ids
    )

    def visit(task_id: str, trail: list[str]) -> None:
        if task_id in trail:
            errors.append("dependency cycle: " + " -> ".join([*trail, task_id]))
            return
        for dependency in graph.get(task_id, []):
            visit(dependency, [*trail, task_id])

    for task_id in ids:
        visit(task_id, [])
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
    errors.extend(dependency_errors(tasks, set(ids)))
    current = ROOT / "CURRENT.md"
    if all(meta.get("status") in STATUSES for _, meta, _ in tasks):
        expected = render_current(tasks)
        if current.exists() and current.read_text() != expected:
            errors.append("CURRENT.md differs from generated tasks")
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
    if run(["git", "-C", str(ROOT), "diff", "--cached", "--quiet"], check=False).returncode == 0:
        return False
    run(["git", "-C", str(ROOT), "commit", "-S", "-s", "-m", message], capture=False)
    return True


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


def reconcile(*, do_commit: bool, push: bool = False) -> bool:
    with locked():
        state = project_scan()
        before = {path: path.read_text() for path, _, _ in all_tasks()}
        sync_task_observations(all_tasks(), state)
        atomic(ROOT / "CURRENT.md", render_current(all_tasks()))
        project, worktrees = live_docs(state)
        atomic(ROOT / "PROJECT_STATE.md", project)
        atomic(ROOT / "WORKTREES.md", worktrees)
        errors = validate(live=False)
        if errors:
            raise RuntimeError("validation failed:\n" + "\n".join(errors))
        touched = [path for path, old in before.items() if path.read_text() != old]
        touched += [ROOT / name for name in ("CURRENT.md", "PROJECT_STATE.md", "WORKTREES.md")]
        changed = (
            commit("chore(state): reconcile Agent Systems Benchmark", touched)
            if do_commit
            else True
        )
        head = run(["git", "-C", str(ROOT), "rev-parse", "HEAD"], check=False).stdout.strip()
        if push:
            push_replica()
        atomic(
            RUNTIME / "last-reconcile.json",
            json.dumps(
                {"at": now(), "state_commit": head, "project_main": state["remote_main"]}, indent=2
            )
            + "\n",
        )
        return changed


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
    if args.expected_revision != meta["task_revision"]:
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


def mutate(args: argparse.Namespace, kind: str) -> None:
    with locked():
        path, meta, body = locate(args.task)
        old_task = path.read_text()
        current_path = ROOT / "CURRENT.md"
        old_current = current_path.read_text() if current_path.exists() else ""
        note = (
            apply_claim(args, meta, all_tasks())
            if kind == "claim"
            else apply_owned_change(args, kind, meta)
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
            atomic(current_path, render_current(all_tasks()))
            errors = validate(live=False)
            if errors:
                raise RuntimeError("\n".join(errors))
            commit(f"chore(state): {kind} {args.task}", [path, current_path])
            push_replica()
        except Exception:
            atomic(path, old_task)
            if old_current:
                atomic(current_path, old_current)
            raise


def cmd_snapshot() -> None:
    with locked(exclusive=False):
        errors = validate(live=True)
        if errors:
            raise RuntimeError("snapshot refused:\n" + "\n".join(errors))
        print("STATE_COMMIT=" + run(["git", "-C", str(ROOT), "rev-parse", "HEAD"]).stdout.strip())
        print((ROOT / "CURRENT.md").read_text(), end="")


def cmd_run(args: argparse.Namespace) -> int:
    _, meta, _ = locate(args.task)
    if meta.get("owner") != args.owner:
        raise RuntimeError("task claim does not match owner")
    if not args.command:
        raise RuntimeError("missing command")
    proc = subprocess.run(args.command, check=False)
    reconcile(do_commit=True, push=True)

    command_hash = hashlib.sha256("\0".join(args.command).encode()).hexdigest()
    update = argparse.Namespace(
        task=args.task,
        owner=args.owner,
        expected_revision=locate(args.task)[1]["task_revision"],
        status=None,
        priority=None,
        summary=None,
        next_action=None,
        note=f"Recorded command exit {proc.returncode}; command SHA-256 {command_hash}.",
    )
    mutate(update, "update")
    return proc.returncode


def main() -> int:
    parser = argparse.ArgumentParser()
    commands = parser.add_subparsers(dest="cmd", required=True)
    item = commands.add_parser("reconcile")
    item.add_argument("--commit", action="store_true")
    item.add_argument("--push", action="store_true")
    commands.add_parser("snapshot")
    item = commands.add_parser("doctor")
    item.add_argument("--live", action="store_true")
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
    item.add_argument("command", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    if args.cmd == "reconcile":
        reconcile(do_commit=args.commit, push=args.push)
    elif args.cmd == "snapshot":
        cmd_snapshot()
    elif args.cmd == "doctor":
        errors = validate(live=args.live)
        if errors:
            print("\n".join("ERROR: " + value for value in errors))
            return 1
        print(
            "OK: structure, references, privacy, generated views"
            + (" and live state" if args.live else "")
            + " are consistent"
        )
    elif args.cmd in ("claim", "heartbeat", "release", "update"):
        mutate(args, args.cmd)
    elif args.cmd == "run":
        if args.command and args.command[0] == "--":
            args.command = args.command[1:]
        return cmd_run(args)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        print(f"ERROR: {error}", file=sys.stderr)
        raise SystemExit(1) from error
