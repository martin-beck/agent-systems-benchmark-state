# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Issue-series command service, installed into handoffctl at runtime.

The core CLI owns process setup; this companion owns the bounded issue-series
service and is vendored alongside the CLI.
"""

from __future__ import annotations

import argparse
import contextlib
import fcntl
import hashlib
import json
import os
import re
import shutil
import stat
import subprocess
import time
from collections.abc import Iterator
from contextvars import ContextVar
from functools import wraps
from pathlib import Path
from typing import TYPE_CHECKING, Any, cast

if __package__:
    from .issue_series import parse_manifest
    from .issue_series_plan import IssueSeriesPlanError, plan_issue_series
    from .issue_series_publish import (
        DryRunTransport,
        MockTransport,
        PublicationOutcome,
        publication_key,
        render_publication,
    )
else:  # pragma: no cover - direct vendored execution
    from issue_series import parse_manifest  # type: ignore[import-not-found,no-redef]
    from issue_series_plan import (  # type: ignore[import-not-found,no-redef]
        IssueSeriesPlanError,
        plan_issue_series,
    )
    from issue_series_publish import (  # type: ignore[import-not-found,no-redef]
        DryRunTransport,
        MockTransport,
        PublicationOutcome,
        publication_key,
        render_publication,
    )


if TYPE_CHECKING:
    # The service is installed after handoffctl has finished initializing.  Keep
    # that runtime dependency injection explicit to static analyzers without
    # importing handoffctl during its own module initialization.
    from .handoffctl import (
        CONFIG,
        LOCK_POLL_SECONDS,
        LOCK_TIMEOUT_SECONDS,
        ROOT,
        TASKS,
        LockTimeoutError,
        Meta,
        StorageCommittedError,
        Task,
        all_tasks,
        atomic,
        backend_selection,
        basic_task_errors,
        changed_paths,
        commit,
        config,
        coordinator_lock_path,
        generated_paths,
        generated_view_errors,
        introduced_content_errors,
        locked,
        mutating_sqlite_backend,
        mutation_global_errors,
        now,
        policy_snapshot,
        project_binding,
        project_settings,
        push_replica,
        rendered_task_views,
        repository_slug,
        require_project_settings_unchanged,
        restore_paths,
        storage_backend,
        sync_replica_before_write,
        write_rendered_task_views,
        write_sqlite_projections,
        write_task,
    )
    from .sqlite_storage import SQLiteBackend
    from .task_spec import EvidencePolicy, require_policy_unchanged


@contextlib.contextmanager
def issue_series_publication_locked(key: str) -> Iterator[None]:
    """Serialize one optional remote publication without occupying the state lock."""
    path = coordinator_lock_path().parent / "issue-series-publications" / f"{key}.lock"
    path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    fd = os.open(path, os.O_CREAT | os.O_RDWR, 0o600)
    try:
        deadline = time.monotonic() + LOCK_TIMEOUT_SECONDS
        while True:
            try:
                fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
                break
            except BlockingIOError as error:
                if time.monotonic() >= deadline:
                    raise LockTimeoutError(
                        "LOCK_TIMEOUT acquiring issue-series publication lock"
                    ) from error
                time.sleep(LOCK_POLL_SECONDS)
        yield
    finally:
        fcntl.flock(fd, fcntl.LOCK_UN)
        os.close(fd)


def write_sqlite_issue_series_projections(backend: SQLiteBackend) -> list[Path]:
    """Export authoritative SQLite issue-series manifests as Git projections."""
    issue_series_root = ROOT / "issue-series"
    issue_series_root.mkdir(mode=0o700, parents=True, exist_ok=True)
    expected_series: set[Path] = set()
    paths: list[Path] = []
    for receipt in backend.load_issue_series():
        path = issue_series_manifest_path(receipt)
        expected_series.add(path.resolve())
        atomic(path, json.dumps(receipt["manifest"], indent=2, sort_keys=True) + "\n")
        paths.append(path)
    for path in issue_series_root.glob("*.json"):
        if path.resolve() not in expected_series:
            path.unlink()
    return paths


def write_sqlite_issue_series_publication_projections(backend: SQLiteBackend) -> list[Path]:
    """Export normalized optional publication receipts without making them authority."""
    root = ROOT / "issue-series-publications"
    root.mkdir(mode=0o700, parents=True, exist_ok=True)
    expected: set[Path] = set()
    paths: list[Path] = []
    for record in backend.load_issue_series_publications():
        key = str(record["publication_key"])
        path = issue_series_publication_path(key)
        expected.add(path.resolve())
        atomic(path, json.dumps(record, sort_keys=True, separators=(",", ":")) + "\n")
        paths.append(path)
    for path in root.glob("*.json"):
        if path.resolve() not in expected:
            path.unlink()
    return paths


def issue_series_state_digest(tasks: list[Task]) -> str:
    """Bind a plan receipt to the stable, local task graph it inspected."""
    snapshot = [
        {
            "depends_on": meta.get("depends_on", []),
            "id": meta["id"],
            "parent_task_ref": meta.get("parent_task_ref", ""),
            "status": meta["status"],
            "task_revision": meta["task_revision"],
        }
        for _path, meta, _body in sorted(tasks, key=lambda task: str(task[1]["id"]))
    ]
    encoded = json.dumps(snapshot, separators=(",", ":"), sort_keys=True).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def load_issue_series_plan(path: Path, tasks: list[Task]) -> str:
    """Validate one offline issue-series plan without changing local authority."""
    try:
        info = path.lstat()
        if stat.S_ISLNK(info.st_mode) or not stat.S_ISREG(info.st_mode) or info.st_size > 200_000:
            raise RuntimeError("issue-series manifest must be a bounded regular file")
        return plan_issue_series(
            path,
            expected_product_slug=str(project_binding()["product_repository"]),
            existing_task_ids=(str(meta["id"]) for _path, meta, _body in tasks),
            existing_issue_series_identities=(
                meta.get("issue_series") for _path, meta, _body in tasks
            ),
            current_state_digest=issue_series_state_digest(tasks),
        )
    except (OSError, IssueSeriesPlanError) as error:
        raise RuntimeError(f"invalid issue-series manifest: {error}") from error


def _load_git_issue_series_receipt(manifest_ref: str, members: list[Meta]) -> Meta:
    """Load one bounded projection and prove its task linkage before authority migration."""
    path = (ROOT / manifest_ref).resolve()
    issue_root = (ROOT / "issue-series").resolve()
    if path.parent != issue_root or path.suffix != ".json":
        raise RuntimeError("issue-series manifest reference is outside the local series directory")
    try:
        info = path.lstat()
        if stat.S_ISLNK(info.st_mode) or not stat.S_ISREG(info.st_mode) or info.st_size > 200_000:
            raise RuntimeError("issue-series manifest must be a bounded regular file")
        receipt = cast(
            Meta,
            json.loads(
                plan_issue_series(
                    path,
                    expected_product_slug=str(project_binding()["product_repository"]),
                    existing_task_ids=(),
                    existing_issue_series_identities=(),
                    current_state_digest="sha256:" + "0" * 64,
                )
            ),
        )
    except (OSError, IssueSeriesPlanError) as error:
        raise RuntimeError(f"invalid issue-series manifest {manifest_ref}: {error}") from error
    expected_ids = sorted(str(item) for item in receipt["task_ids"])
    linked_ids = sorted(str(meta["id"]) for meta in members)
    if linked_ids != expected_ids:
        raise RuntimeError(f"issue-series membership does not match manifest {manifest_ref}")
    digest = str(receipt["manifest_digest"])
    if any(cast(Meta, item["issue_series"]).get("manifest_digest") != digest for item in members):
        raise RuntimeError(f"issue-series digest does not match manifest {manifest_ref}")
    return receipt


def git_issue_series_receipts(tasks: list[Task]) -> list[Meta]:
    """Reconstruct and validate authoritative local series records for SQLite import."""
    linked: dict[str, list[Meta]] = {}
    for _path, meta, _body in tasks:
        linkage = meta.get("issue_series")
        if linkage is None:
            continue
        if not isinstance(linkage, dict) or not isinstance(linkage.get("manifest_ref"), str):
            raise RuntimeError(f"invalid issue-series linkage in {meta['id']}")
        linked.setdefault(str(linkage["manifest_ref"]), []).append(meta)
    return [
        _load_git_issue_series_receipt(manifest_ref, members)
        for manifest_ref, members in sorted(linked.items())
    ]


def git_issue_series_publication_receipts(tasks: list[Task]) -> list[Meta]:
    """Reconstruct bounded Git publication receipts for SQLite authority migration."""
    identities = {
        publication_key(
            str(cast(Meta, receipt["series_identity"])["repository"]),
            int(cast(Meta, receipt["series_identity"])["issue_number"]),
            str(receipt["manifest_digest"]),
        ): cast(Meta, receipt["series_identity"])
        for receipt in git_issue_series_receipts(tasks)
    }
    directory = ROOT / "issue-series-publications"
    if not directory.exists():
        return []
    receipts: list[Meta] = []
    for path in sorted(directory.glob("*.json")):
        if path.parent != directory or path.is_symlink() or path.stat().st_size > 10_000:
            raise RuntimeError("issue-series publication receipt is not a bounded regular file")
        raw = cast(Meta, json.loads(path.read_text(encoding="utf-8")))
        key = raw.get("publication_key")
        identity = identities.get(key) if isinstance(key, str) else None
        if identity is None or raw.get("manifest_digest") is None:
            raise RuntimeError("issue-series publication receipt does not match a local series")
        receipts.append(
            {
                "series_identity": identity,
                "manifest_digest": raw["manifest_digest"],
                "publication_key": key,
                "status": raw.get("status"),
                "comment_id": raw.get("comment_id") or None,
            }
        )
    return receipts


def cmd_issue_series_plan(args: argparse.Namespace) -> None:
    """Print a deterministic local planning receipt; never publish or mutate."""
    receipt = load_issue_series_plan(Path(args.manifest), all_tasks())
    print(receipt)


def create_sqlite_issue_series(receipt: Meta, created: list[Task], policy: EvidencePolicy) -> None:
    """Commit one preflighted series in SQLite before exporting disposable projections."""
    backend = mutating_sqlite_backend()
    backend.create_issue_series(
        receipt,
        created,
        expected_state_digest=str(receipt["current_state_digest"]),
        recorded_at=now(),
    )
    try:
        write_sqlite_projections(backend.load_tasks(), already_locked=True, policy=policy)
    except Exception as error:
        identity = cast(Meta, receipt["series_identity"])
        raise StorageCommittedError(
            "SQLITE_COMMITTED_EXPORT_FAILED: issue-series="
            f"{identity['repository']}#{identity['issue_number']}; {error}"
        ) from error


def create_git_issue_series(receipt: Meta, created: list[Task], policy: EvidencePolicy) -> None:
    """Write, validate, and commit one preflighted Git-authoritative issue series."""
    manifest_path = issue_series_manifest_path(receipt)
    before: dict[Path, str | None] = {
        path: path.read_text() if path.exists() else None for path, _meta, _body in created
    }
    before[manifest_path] = None
    before.update({path: path.read_text() if path.exists() else None for path in generated_paths()})
    committed = False
    try:
        atomic(manifest_path, json.dumps(receipt["manifest"], indent=2, sort_keys=True) + "\n")
        for path, meta, body in created:
            write_task(path, meta, body)
        view_tasks = all_tasks()
        settings = project_settings()
        views = rendered_task_views(view_tasks)
        before.update(
            {
                path: path.read_text() if path.exists() else None
                for path in views
                if path not in before
            }
        )
        write_rendered_task_views(views)
        require_project_settings_unchanged(settings)
        require_policy_unchanged(ROOT, policy)
        errors = mutation_global_errors(view_tasks)
        errors.extend(
            generated_view_errors(view_tasks, rendered_snapshot=(view_tasks, views, settings))
        )
        errors.extend(introduced_content_errors(before))
        if errors:
            raise RuntimeError(
                "issue-series mutation validation failed:\n" + "\n".join(sorted(set(errors)))
            )
        identity = cast(Meta, receipt["series_identity"])
        committed = commit(
            f"chore(state): create issue series {identity['repository']}"
            f"#{identity['issue_number']}",
            changed_paths(before, include_deleted=True),
        )
        if not committed:
            raise RuntimeError("issue-series create produced no commit")
        push_replica()
    except Exception:
        if not committed:
            restore_paths(before)
        raise


def cmd_issue_series_create(args: argparse.Namespace) -> None:
    """Atomically create one locally validated series through selected local authority."""
    with locked(phase="issue_series_create"):
        selected_backend = str(backend_selection()["backend"])
        if selected_backend not in {"git", "sqlite"}:
            raise RuntimeError("BACKEND_CHANGED: retry issue-series create")
        if selected_backend == "git":
            sync_replica_before_write()
        tasks = all_tasks()
        receipt = cast(Meta, json.loads(load_issue_series_plan(Path(args.manifest), tasks)))
        if args.expected_state_digest != receipt["current_state_digest"]:
            raise RuntimeError("STALE_STATE: re-run issue-series plan before create")
        manifest_path = issue_series_manifest_path(receipt)
        if manifest_path.exists():
            raise RuntimeError("issue-series manifest identity already exists")
        created = issue_series_tasks(receipt, manifest_path)
        policy = policy_snapshot(None)
        errors = [
            error
            for path, meta, _body in created
            for error in basic_task_errors(path, meta, policy)
        ]
        errors.extend(mutation_global_errors([*tasks, *created]))
        if errors:
            raise RuntimeError("issue-series preflight failed:\n" + "\n".join(sorted(set(errors))))
        if selected_backend == "sqlite":
            create_sqlite_issue_series(receipt, created, policy)
        else:
            create_git_issue_series(receipt, created, policy)


def issue_series_publication_path(key: str) -> Path:
    """Return the separate bounded Git projection for one local publication receipt."""
    if not re.fullmatch(r"[0-9a-f]{64}", key):
        raise RuntimeError("invalid issue-series publication key")
    return ROOT / "issue-series-publications" / f"{key}.json"


def _issue_series_receipt(repository: str, issue_number: int, digest: str) -> Meta:
    """Locate exactly the immutable local series selected for optional projection."""
    backend = storage_backend()
    records = (
        backend.load_issue_series()
        if isinstance(backend, SQLiteBackend)
        else git_issue_series_receipts(all_tasks())
    )
    for receipt in records:
        identity = cast(Meta, receipt["series_identity"])
        if (
            identity.get("repository") == repository
            and identity.get("issue_number") == issue_number
            and receipt.get("manifest_digest") == digest
        ):
            return receipt
    raise RuntimeError("issue-series publication does not match a local authoritative manifest")


def _publication_record(outcome: PublicationOutcome, markdown: str) -> Meta:
    """Make a bounded receipt without retaining arbitrary hosted material or Markdown."""
    return {
        "schema_version": 1,
        "publication_key": outcome.publication_key,
        "manifest_digest": outcome.manifest_digest,
        "status": outcome.status,
        "comment_id": outcome.comment_id or "",
        "rendered_sha256": "sha256:" + hashlib.sha256(markdown.encode("utf-8")).hexdigest(),
    }


def _git_record_issue_series_publication(record: Meta) -> None:
    """Commit one local-only projection; no network call occurs under the Coordinator lock."""
    key = str(record["publication_key"])
    path = issue_series_publication_path(key)
    path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    encoded = json.dumps(record, sort_keys=True, separators=(",", ":")) + "\n"
    if path.exists():
        if path.read_text(encoding="utf-8") != encoded:
            raise RuntimeError(
                "issue-series publication receipt conflicts with existing local receipt"
            )
        return
    atomic(path, encoded)
    if not commit("chore(state): record issue-series publication", [path]):
        raise RuntimeError("issue-series publication receipt produced no commit")
    push_replica()


def _git_resolve_issue_series_publication(record: Meta) -> None:
    """Replace a non-final Git receipt with one locally durable outcome."""
    path = issue_series_publication_path(str(record["publication_key"]))
    if not path.exists():
        raise RuntimeError("issue-series publication reservation is missing")
    current = cast(Meta, json.loads(path.read_text(encoding="utf-8")))
    if current.get("status") in {"published", "already_published"}:
        if current != record:
            raise RuntimeError("issue-series publication receipt is already final")
        push_replica()
        return
    if current.get("manifest_digest") != record.get("manifest_digest"):
        raise RuntimeError("issue-series publication reservation identity changed")
    atomic(path, json.dumps(record, sort_keys=True, separators=(",", ":")) + "\n")
    if not commit("chore(state): resolve issue-series publication", [path]):
        raise RuntimeError("issue-series publication resolution produced no commit")
    push_replica()


def _record_issue_series_publication(
    repository: str, issue_number: int, record: Meta, *, resolve: bool = False
) -> None:
    """Persist one optional projection with Git/SQLite parity."""
    if isinstance(storage_backend(), SQLiteBackend):
        backend = mutating_sqlite_backend()
        if resolve:
            backend.resolve_issue_series_publication(repository, issue_number, record)
        else:
            backend.record_issue_series_publication(repository, issue_number, record)
        write_sqlite_projections(backend.load_tasks(), already_locked=True)
    elif resolve:
        _git_resolve_issue_series_publication(record)
    else:
        _git_record_issue_series_publication(record)


def _existing_issue_series_publication(
    repository: str, issue_number: int, digest: str
) -> Meta | None:
    """Load the one local receipt for this immutable publication intent."""
    key = publication_key(repository, issue_number, digest)
    backend = storage_backend()
    if isinstance(backend, SQLiteBackend):
        for receipt in backend.load_issue_series_publications():
            if receipt.get("publication_key") == key:
                return receipt
        return None
    path = issue_series_publication_path(key)
    if not path.exists():
        return None
    record = cast(Meta, json.loads(path.read_text(encoding="utf-8")))
    if record.get("manifest_digest") != digest:
        raise RuntimeError("issue-series publication receipt identity changed")
    return record


def _live_publication_failure(diagnostic: str, key: str, digest: str) -> PublicationOutcome:
    """Classify a bounded live transport failure without retaining its response."""
    normalized = diagnostic.lower()
    if "401" in normalized or "403" in normalized:
        return PublicationOutcome("deferred_unauthorized", key, digest)
    if "410" in normalized or "closed" in normalized:
        return PublicationOutcome("deferred_closed", key, digest)
    if "404" in normalized or "moved" in normalized:
        return PublicationOutcome("deferred_moved", key, digest)
    if "409" in normalized or "conflict" in normalized:
        return PublicationOutcome("deferred_conflict", key, digest)
    return PublicationOutcome("deferred_unavailable", key, digest)


def _live_existing_issue_series_comment(
    slug: str, issue_number: int, key: str, digest: str
) -> PublicationOutcome | None:
    """Find the sole prior marker comment, without retaining its hosted body."""
    marker = f"agent-workflow-issue-series:v1 digest={digest} key={key}"
    gh_executable = shutil.which("gh")
    if gh_executable is None:
        return PublicationOutcome("deferred_unavailable", key, digest)
    try:
        found = subprocess.run(  # noqa: S603 - resolved local executable
            [
                gh_executable,
                "api",
                "--paginate",
                f"repos/{slug}/issues/{issue_number}/comments?per_page=100",
                "--jq",
                f'.[] | select(.body | contains("{marker}")) | .id',
            ],
            text=True,
            capture_output=True,
            check=False,
            timeout=15,
        )
    except (OSError, subprocess.TimeoutExpired):
        return PublicationOutcome("deferred_timeout", key, digest)
    if found.returncode:
        return _live_publication_failure(found.stderr, key, digest)
    existing_ids = [line for line in found.stdout.splitlines() if line]
    if len(existing_ids) == 1 and re.fullmatch(r"[1-9][0-9]{0,18}", existing_ids[0]):
        return PublicationOutcome("already_published", key, digest, existing_ids[0])
    if len(existing_ids) > 1 or any(
        not re.fullmatch(r"[1-9][0-9]{0,18}", item) for item in existing_ids
    ):
        return PublicationOutcome("ambiguous", key, digest)
    return None


def _live_issue_series_publication(
    repository: str, issue_number: int, digest: str, markdown: str
) -> PublicationOutcome:
    """Use configured ``gh`` credentials without storing a response or credential."""
    key = publication_key(repository, issue_number, digest)
    if not CONFIG.exists():
        return PublicationOutcome("deferred_unavailable", key, digest)
    configured = config().get("github_repository")
    slug = repository.removeprefix("github.com/")
    if not isinstance(configured, str) or repository_slug(configured) != repository_slug(slug):
        return PublicationOutcome("deferred_wrong_identity", key, digest)
    existing = _live_existing_issue_series_comment(slug, issue_number, key, digest)
    if existing is not None:
        return existing
    gh_executable = shutil.which("gh")
    if gh_executable is None:
        return PublicationOutcome("deferred_unavailable", key, digest)
    try:
        result = subprocess.run(  # noqa: S603 - resolved local executable
            [
                gh_executable,
                "api",
                "--method",
                "POST",
                f"repos/{slug}/issues/{issue_number}/comments",
                "-f",
                f"body={markdown}",
                "--jq",
                ".id",
            ],
            text=True,
            capture_output=True,
            check=False,
            timeout=15,
        )
    except (OSError, subprocess.TimeoutExpired):
        return PublicationOutcome("deferred_timeout", key, digest)
    if result.returncode:
        return _live_publication_failure(result.stderr, key, digest)
    comment_id = result.stdout.strip()
    if not re.fullmatch(r"[1-9][0-9]{0,18}", comment_id):
        return PublicationOutcome("ambiguous", key, digest)
    return PublicationOutcome("published", key, digest, comment_id)


def cmd_issue_series_publish(args: argparse.Namespace) -> None:  # noqa: C901
    """Record an optional local-first series projection outcome without changing task lifecycle."""
    with locked(phase="issue_series_publish"):
        repository = str(args.repository)
        issue_number = int(args.issue_number)
        digest = str(args.expected_manifest_digest)
        receipt = _issue_series_receipt(repository, issue_number, digest)
        manifest = parse_manifest(cast(Meta, receipt["manifest"]))
        markdown = render_publication(manifest, digest)
        key = publication_key(repository, issue_number, digest)
        if args.transport == "dry-run":
            outcome = DryRunTransport().publish(repository, issue_number, digest, markdown)
        elif args.transport == "mock":
            raw: Meta = {"status": str(args.mock_status)}
            if args.mock_status in {"published", "already_published"}:
                raw.update(
                    {
                        "repository": repository,
                        "issue_number": issue_number,
                        "manifest_digest": digest,
                        "publication_key": key,
                        "comment_id": str(args.mock_comment_id),
                    }
                )
            outcome = MockTransport(raw).publish(repository, issue_number, digest, markdown)
        if args.transport in {"dry-run", "mock"}:
            record = _publication_record(outcome, markdown)
            _record_issue_series_publication(repository, issue_number, record)
            print(json.dumps(record, sort_keys=True))
            return
        existing = _existing_issue_series_publication(repository, issue_number, digest)
        if existing is None:
            reservation = _publication_record(
                PublicationOutcome("ambiguous", key, digest), markdown
            )
            _record_issue_series_publication(repository, issue_number, reservation)
        elif existing.get("status") in {"published", "already_published"}:
            print(json.dumps(existing, sort_keys=True))
            return
    live_record: Meta | None = None
    with issue_series_publication_locked(key):
        with locked(phase="issue_series_publish_prepare"):
            _issue_series_receipt(repository, issue_number, digest)
            existing = _existing_issue_series_publication(repository, issue_number, digest)
            if existing is not None and existing.get("status") in {
                "published",
                "already_published",
            }:
                live_record = existing
            else:
                if existing is not None and existing.get("status") != "ambiguous":
                    reservation = _publication_record(
                        PublicationOutcome("ambiguous", key, digest), markdown
                    )
                    _record_issue_series_publication(
                        repository, issue_number, reservation, resolve=True
                    )
        if live_record is None:
            outcome = _core_value("_live_issue_series_publication")(
                repository, issue_number, digest, markdown
            )
            live_record = _publication_record(outcome, markdown)
            with locked(phase="issue_series_publish_resolve"):
                _issue_series_receipt(repository, issue_number, digest)
                _record_issue_series_publication(
                    repository, issue_number, live_record, resolve=True
                )
    print(json.dumps(live_record, sort_keys=True))


def issue_series_manifest_path(receipt: Meta) -> Path:
    """Return one bounded deterministic local manifest name for a validated receipt."""
    identity = cast(Meta, receipt["series_identity"])
    repository = str(identity["repository"])
    number = int(identity["issue_number"])
    stem = hashlib.sha256(f"{repository}#{number}".encode()).hexdigest()[:24]
    return ROOT / "issue-series" / f"{stem}.json"


def issue_series_tasks(receipt: Meta, manifest_path: Path) -> list[Task]:
    """Derive every planned task and hierarchy edge before any Git write occurs."""
    manifest = cast(Meta, receipt["manifest"])
    finalizer = str(manifest["finalizer"])
    manifest_digest = str(receipt["manifest_digest"])
    members = cast(list[Meta], manifest["members"])
    child_ids = [str(member["id"]) for member in members if str(member["id"]) != finalizer]
    generated: list[Task] = []
    created_at = now()
    for member in members:
        task_id = str(member["id"])
        dependencies = [str(edge["id"]) for edge in cast(list[Meta], member["depends_on"])]
        meta: Meta = {
            "schema_version": 1,
            "id": task_id,
            "title": str(member["short_title"]),
            "short_title": str(member["short_title"]),
            "status": "planned",
            "priority": "P1",
            "summary": str(member["scope"]),
            "next_action": "Implement the bounded scope and record local acceptance evidence.",
            "task_revision": 1,
            "updated_at": created_at,
            "owner": "",
            "claim_expires": "",
            "checkpoint_commit": "",
            "depends_on": dependencies,
            "parent_task_ref": "" if task_id == finalizer else finalizer,
            "children": child_ids if task_id == finalizer else [],
            "issue_series": {
                "manifest_ref": str(manifest_path.relative_to(ROOT)),
                "manifest_digest": manifest_digest,
                "member_id": task_id,
            },
        }
        body = (
            "\n\n".join(
                (
                    "Issue-series member created from a locally validated manifest.",
                    f"Scope: {member['scope']}",
                    f"Acceptance: {member['acceptance']}",
                    f"Ownership hint: {member['ownership']}",
                )
            )
            + "\n"
        )
        generated.append((TASKS / f"{task_id}.md", meta, body))
    return generated


_CORE: dict[str, Any] | None = None
_ACTIVE_CORE: ContextVar[dict[str, Any] | None] = ContextVar(
    "issue_series_active_core", default=None
)
_LOCAL_FUNCTIONS = {
    name
    for name, value in tuple(globals().items())
    if callable(value) and getattr(value, "__module__", None) == __name__
}
_PROTECTED = _LOCAL_FUNCTIONS | {"_ACTIVE_CORE", "_CORE", "_LOCAL_FUNCTIONS", "_PROTECTED"}


def _refresh() -> None:
    """Expose current handoffctl dependencies, including test-time replacements."""
    core = _ACTIVE_CORE.get() or _CORE
    if core is None:
        raise RuntimeError("issue-series service is not installed")
    for name, value in core.items():
        if not name.startswith("__") and name not in _PROTECTED:
            globals()[name] = value


def _delegate(implementation: Any, core: dict[str, Any]) -> Any:
    @wraps(implementation)
    def call(*args: Any, **kwargs: Any) -> Any:
        context_marker = _ACTIVE_CORE.set(core)
        try:
            _refresh()
            return implementation(*args, **kwargs)
        finally:
            _ACTIVE_CORE.reset(context_marker)

    return call


def _core_value(name: str) -> Any:
    core = _ACTIVE_CORE.get() or _CORE
    if core is None:
        raise RuntimeError("issue-series service is not installed")
    return core[name]


def install(core: dict[str, Any]) -> dict[str, Any]:
    """Return compatibility delegates for the handoffctl issue-series API."""
    global _CORE
    _CORE = core
    _refresh()
    exported = {name: _delegate(globals()[name], core) for name in sorted(_LOCAL_FUNCTIONS)}
    exported.update(
        {
            "DryRunTransport": DryRunTransport,
            "IssueSeriesPlanError": IssueSeriesPlanError,
            "MockTransport": MockTransport,
            "PublicationOutcome": PublicationOutcome,
            "parse_manifest": parse_manifest,
            "plan_issue_series": plan_issue_series,
            "publication_key": publication_key,
            "render_publication": render_publication,
        }
    )
    return exported


def add_cli_parser(commands: Any) -> None:
    """Add the bounded issue-series command grammar to handoffctl."""
    item = commands.add_parser("issue-series")
    actions = item.add_subparsers(dest="issue_series_action", required=True)
    actions.add_parser("plan").add_argument("--manifest", type=Path, required=True)
    create = actions.add_parser("create")
    create.add_argument("--manifest", type=Path, required=True)
    create.add_argument("--expected-state-digest", required=True)
    publish = actions.add_parser("publish")
    publish.add_argument("--repository", required=True)
    publish.add_argument("--issue-number", required=True, type=int)
    publish.add_argument("--expected-manifest-digest", required=True)
    publish.add_argument("--transport", choices=("dry-run", "mock", "live"), required=True)
    publish.add_argument(
        "--mock-status",
        choices=(
            "published",
            "already_published",
            "unavailable",
            "unauthorized",
            "timeout",
            "conflict",
            "wrong_identity",
            "closed",
            "moved",
            "ambiguous",
        ),
        default="published",
    )
    publish.add_argument("--mock-comment-id", default="mock-comment")


def dispatch_cli(args: Any, core: dict[str, Any] | None = None) -> bool:
    """Dispatch an issue-series command and report whether it was selected."""
    if args.cmd != "issue-series":
        return False
    marker = _ACTIVE_CORE.set(core) if core is not None else None
    try:
        _refresh()
        actions = {
            "plan": _core_value("cmd_issue_series_plan"),
            "create": _core_value("cmd_issue_series_create"),
            "publish": _core_value("cmd_issue_series_publish"),
        }
        try:
            actions[args.issue_series_action](args)
        except KeyError as error:
            raise RuntimeError("unsupported issue-series action") from error
    finally:
        if marker is not None:
            _ACTIVE_CORE.reset(marker)
    return True


def sqlite_projection_paths(backend: Any) -> list[Any]:
    """Return disposable issue-series projections for a SQLite authority."""
    if not isinstance(backend, SQLiteBackend):
        return []
    return [
        *write_sqlite_issue_series_projections(backend),
        *write_sqlite_issue_series_publication_projections(backend),
    ]
