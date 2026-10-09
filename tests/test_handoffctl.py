# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Fault, consistency, claim and generation tests for handoffctl."""

import argparse
import datetime as dt
import importlib.util
import json
import multiprocessing
import os
import re
import subprocess
import sys
import threading
import time
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace
from typing import Any, cast
from unittest.mock import patch

from fixture_ids import project_uuid

SOURCE = Path(__file__).resolve().parent.parent / "tools/handoffctl.py"
sys.path.insert(0, str(SOURCE.parent))
SPEC = importlib.util.spec_from_file_location("handoffctl_core", SOURCE)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load handoffctl")
CORE: Any = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CORE)


def hold_lock(lock_path: str, ready: Any, release: Any) -> None:
    """Hold an exclusive lock in a separate process."""
    CORE.LOCK = Path(lock_path)
    CORE.RUNTIME = CORE.LOCK.parent
    CORE.ROOT = CORE.RUNTIME.parent
    with CORE.locked():
        ready.set()
        release.wait(5)


def hold_shared_lock(lock_path: str, ready: Any, release: Any) -> None:
    """Hold a shared lock in a separate process."""
    CORE.LOCK = Path(lock_path)
    CORE.RUNTIME = CORE.LOCK.parent
    CORE.ROOT = CORE.RUNTIME.parent
    with CORE.locked(exclusive=False):
        ready.set()
        release.wait(5)


def configure_child(root_value: str) -> None:
    """Point the imported coordinator module at a process-shared fixture."""
    root = Path(root_value)
    CORE.ROOT = root
    CORE.TASKS = root / "tasks"
    CORE.RUNTIME = root / ".runtime"
    CORE.LOCK = CORE.RUNTIME / "state.lock"
    CORE.CONFIG = CORE.RUNTIME / "config.json"
    CORE.REPLICA_BLOCKED = CORE.RUNTIME / "replica-blocked.json"
    CORE.PROJECT_CONFIG = root / ".handoffctl.json"
    CORE.BINDING = root / "coordinator.binding.json"
    CORE.BACKEND_CONFIG = root / "coordinator.backend.json"
    CORE.DATABASE = CORE.RUNTIME / "coordinator.sqlite3"


def racing_claim(root_value: str, start: Any, owner: str, outcomes: Any) -> None:
    """Race a claim and report whether the serialized transition won."""
    configure_child(root_value)
    start.wait(5)
    try:
        with patch.object(CORE, "commit", return_value=True):
            CORE.mutate(
                argparse.Namespace(task="AR-0001", owner=owner, lease_minutes=10),
                "claim",
            )
    except RuntimeError as error:
        outcomes.put(("rejected", str(error)))
    else:
        outcomes.put(("accepted", owner))


def concurrent_claim(root_value: str, start: Any) -> None:
    """Claim through the real locked mutation path in a child process."""
    configure_child(root_value)
    start.wait(5)
    with patch.object(CORE, "commit", return_value=True):
        CORE.mutate(argparse.Namespace(task="AR-0001", owner="worker-a", lease_minutes=10), "claim")


def concurrent_reconcile(root_value: str, start: Any) -> None:
    """Reconcile through the real locked generation path in a child process."""
    configure_child(root_value)
    start.wait(5)
    state = {
        "remote_main": "a" * 40,
        "origin_main": "a" * 40,
        "primary_head": "b" * 40,
        "worktrees": [],
        "prs": [],
        "runs": [],
    }
    completed = subprocess.CompletedProcess(["git"], 0, stdout="b" * 40 + "\n", stderr="")
    with (
        patch.object(CORE, "project_scan", return_value=state),
        patch.object(CORE, "run", return_value=completed),
    ):
        CORE.reconcile(do_commit=False)


def concurrent_observation_ticket(root_value: str, start: Any, outcomes: Any) -> None:
    """Reserve an advisory scan ticket from one shared fixture across processes."""
    configure_child(root_value)
    start.wait(5)
    outcomes.put(CORE.reserve_observation_ticket())


def concurrent_promote(root_value: str, start: Any) -> None:
    """Promote through the real locked mutation path in a child process."""
    configure_child(root_value)
    start.wait(5)
    args = argparse.Namespace(
        task="AR-0001",
        expected_revision=1,
        note="dependencies verified",
    )
    with (
        patch.object(CORE, "commit", return_value=True),
        patch.object(CORE, "dirty_state_paths", return_value=[]),
    ):
        CORE.mutate(args, "promote")


def racing_unblock(root_value: str, start: Any, outcomes: Any) -> None:
    """Race one exact-revision external unblock through the Git authority."""
    configure_child(root_value)
    start.wait(5)
    args = argparse.Namespace(task="AR-0001", expected_revision=1, note="external clear")
    try:
        with (
            patch.object(CORE, "commit", return_value=True),
            patch.object(CORE, "dirty_state_paths", return_value=[]),
        ):
            CORE.mutate(args, "unblock")
    except RuntimeError as error:
        outcomes.put(("rejected", str(error)))
    else:
        outcomes.put(("accepted", "open"))


def racing_resume(root_value: str, start: Any, outcomes: Any) -> None:
    """Race one exact paused-session resume through the Git authority."""
    configure_child(root_value)
    start.wait(5)
    args = argparse.Namespace(
        task="AR-0001", expected_revision=1, session="AR-0001@1", note="resume"
    )
    try:
        with (
            patch.object(CORE, "commit", return_value=True),
            patch.object(CORE, "dirty_state_paths", return_value=[]),
        ):
            CORE.mutate(args, "resume")
    except RuntimeError as error:
        outcomes.put(("rejected", str(error)))
    else:
        outcomes.put(("accepted", "open"))


def hold_repository_lock(root_value: str, ready: Any, release: Any) -> None:
    """Hold the repository-common lock from one linked worktree."""
    configure_child(root_value)
    with CORE.locked():
        ready.set()
        release.wait(5)


def run_git(args: list[str], *, check: bool = True, capture_output: bool = False) -> None:
    """Run Git for a real-filesystem integration fixture."""
    subprocess.run(  # noqa: S603
        ["/usr/bin/git", *args[1:]],
        check=check,
        capture_output=capture_output,
    )


class HandoffTest(unittest.TestCase):
    """Exercise transaction safety without accessing the live project."""

    def setUp(self) -> None:
        self.temp = TemporaryDirectory()
        root = Path(self.temp.name)
        CORE.ROOT = root
        CORE.TASKS = root / "tasks"
        CORE.RUNTIME = root / ".runtime"
        CORE.LOCK = CORE.RUNTIME / "state.lock"
        CORE.CONFIG = CORE.RUNTIME / "config.json"
        CORE.REPLICA_BLOCKED = CORE.RUNTIME / "replica-blocked.json"
        CORE.PROJECT_CONFIG = root / ".handoffctl.json"
        CORE.BINDING = root / "coordinator.binding.json"
        CORE.BACKEND_CONFIG = root / "coordinator.backend.json"
        CORE.DATABASE = CORE.RUNTIME / "coordinator.sqlite3"
        CORE.TASKS.mkdir()
        (root / "plans").mkdir()
        CORE.PROJECT_CONFIG.write_text(
            json.dumps(
                {
                    "schema_version": 1,
                    "project_id": project_uuid("1"),
                    "project_name": "test-project",
                    "project_title": "Test Project",
                    "status_view": True,
                    "commit_signoff": True,
                }
            )
        )
        CORE.BINDING.write_text(
            json.dumps(
                {
                    "schema_version": 1,
                    "project_id": project_uuid("1"),
                    "state_repository": "owner/state",
                    "product_repository": "owner/product",
                }
            )
        )
        self.root = root

    def tearDown(self) -> None:
        self.temp.cleanup()

    def make_task(self, task_id: str = "AR-0001", **changes: object) -> Path:
        """Create one valid task fixture."""
        meta = {
            "schema_version": 1,
            "id": task_id,
            "title": "Test task",
            "status": "open",
            "priority": "P1",
            "summary": "Ready for testing.",
            "next_action": "Run the test.",
            "task_revision": 1,
            "updated_at": "2026-09-03T20:00:00+00:00",
            "owner": "",
            "claim_expires": "",
            "worktree_key": "",
            "branch": "",
            "checkpoint_commit": "",
            "plan": "",
            "depends_on": [],
        }
        meta.update(changes)
        path = CORE.TASKS / f"{task_id}-test.md"
        CORE.write_task(path, meta, "# Test\n")
        self.refresh_views()
        return cast(Path, path)

    def enable_additive_policy(self) -> None:
        """Commit the supported downstream policy in the isolated state root."""
        (self.root / "task-spec-policy.json").write_text(
            json.dumps(
                {
                    "schema_version": 1,
                    "additional_evidence_classes": [
                        "hosted",
                        "offline",
                        "privacy",
                        "journey",
                        "quality",
                    ],
                }
            )
            + "\n",
            encoding="utf-8",
        )
        run_git(["git", "init", "-q", str(self.root)])
        run_git(["git", "-C", str(self.root), "add", "task-spec-policy.json"])
        run_git(
            [
                "git",
                "-C",
                str(self.root),
                "-c",
                "user.name=Policy Test",
                "-c",
                "user.email=policy@example.invalid",
                "commit",
                "-qm",
                "policy fixture",
            ],
        )

    def write_additive_spec(self) -> None:
        """Write one realistic project spec that uses every additive class."""
        value = json.loads(
            (
                Path(__file__).resolve().parents[1] / "examples/task-specs/downstream-additive.json"
            ).read_text(encoding="utf-8")
        )
        value["spec_ref"] = "spec.json"
        (self.root / "spec.json").write_text(json.dumps(value) + "\n", encoding="utf-8")

    def refresh_views(self) -> None:
        """Refresh both deterministic task views in a fixture repository."""
        tasks = CORE.all_tasks()
        CORE.atomic(self.root / "CURRENT.md", CORE.render_current(tasks))
        CORE.atomic(self.root / "STATUS.md", CORE.render_status_view(tasks))

    def test_project_profile_is_strict_and_controls_optional_status(self) -> None:
        settings = CORE.project_settings()
        self.assertEqual("Test Project", settings["project_title"])
        self.assertTrue(settings["status_view"])
        CORE.PROJECT_CONFIG.write_text(json.dumps({**settings, "status_view": False}))
        self.make_task()
        (self.root / "STATUS.md").unlink()
        self.assertNotIn(
            "STATUS.md differs from generated tasks", CORE.generated_view_errors(CORE.all_tasks())
        )
        with self.assertRaisesRegex(RuntimeError, "generation is disabled"):
            CORE.cmd_render_status(check=True)
        CORE.PROJECT_CONFIG.write_text(json.dumps({**settings, "unknown": True}))
        with self.assertRaisesRegex(RuntimeError, "exactly the documented"):
            CORE.project_settings()

    def test_binding_rejects_other_projects_and_init_is_one_time(self) -> None:
        self.assertEqual("owner/state", CORE.repository_slug("git@github.com:Owner/State.git"))
        with (
            patch.object(CORE, "run") as run,
            patch.object(CORE, "git_repository_slug", return_value="owner/state"),
            patch.object(CORE.Path, "cwd", return_value=self.root),
        ):
            run.return_value = subprocess.CompletedProcess([], 0, str(self.root) + "\n", "")
            CORE.assert_project_binding()
        settings = CORE.project_settings()
        CORE.PROJECT_CONFIG.write_text(
            json.dumps({**settings, "project_id": str("2" * 8 + "-2222-4222-8222-" + "2" * 12)})
        )
        with self.assertRaisesRegex(RuntimeError, "does not match"):
            CORE.assert_project_binding()
        CORE.PROJECT_CONFIG.unlink()
        CORE.BINDING.unlink()
        args = argparse.Namespace(
            state_repository="owner/state",
            product_repository="owner/product",
            project_name="test-project",
            project_title="Test Project",
            status_view=True,
            commit_signoff=True,
        )
        with (
            patch.object(CORE, "run") as run,
            patch.object(CORE, "git_repository_slug", return_value="owner/state"),
            patch.object(CORE.Path, "cwd", return_value=self.root),
            patch.object(
                CORE.uuid,
                "uuid4",
                return_value=CORE.uuid.UUID(project_uuid("3")),
            ),
            patch("builtins.print"),
        ):
            run.return_value = subprocess.CompletedProcess([], 0, str(self.root) + "\n", "")
            CORE.cmd_init(args)
        self.assertEqual(project_uuid("3"), CORE.project_settings()["project_id"])
        with self.assertRaisesRegex(RuntimeError, "already initialized"):
            CORE.cmd_init(args)

    def test_project_profile_and_binding_reject_malformed_identity(self) -> None:
        valid_settings = CORE.project_settings()
        CORE.PROJECT_CONFIG.unlink()
        self.assertEqual("Agent Workflow", CORE.project_settings()["project_title"])
        invalid_settings = [
            [],
            {**valid_settings, "schema_version": 2},
            {**valid_settings, "project_id": "bad"},
            {**valid_settings, "project_id": project_uuid("1").replace("-4111-", "-1111-")},
            {**valid_settings, "project_name": "Bad Name"},
            {**valid_settings, "project_title": ""},
            {**valid_settings, "status_view": "yes"},
        ]
        for value in invalid_settings:
            with self.subTest(value=value), self.assertRaises(RuntimeError):
                CORE.PROJECT_CONFIG.write_text(json.dumps(value))
                CORE.project_settings()
        CORE.PROJECT_CONFIG.write_text(json.dumps(valid_settings))
        valid_binding = CORE.project_binding()
        for value in (
            {},
            {**valid_binding, "schema_version": 2},
            {**valid_binding, "project_id": "bad"},
            {**valid_binding, "project_id": project_uuid("1").replace("-4111-", "-1111-")},
        ):
            with self.subTest(binding=value), self.assertRaises(RuntimeError):
                CORE.BINDING.write_text(json.dumps(value))
                CORE.project_binding()
        CORE.BINDING.write_text("bad-json")
        with self.assertRaisesRegex(RuntimeError, "not initialized"):
            CORE.project_binding()
        CORE.BINDING.write_text(json.dumps(valid_binding))
        self.assertEqual("owner/state", CORE.repository_slug("https://github.com/Owner/State.git"))
        with self.assertRaisesRegex(RuntimeError, "invalid GitHub"):
            CORE.repository_slug("not-a-repository")
        self.assertTrue(CORE.inside(self.root / "tasks", self.root))
        self.assertFalse(CORE.inside(self.root, self.root / "tasks"))
        with patch.object(CORE, "run") as run:
            run.return_value = subprocess.CompletedProcess(
                [], 0, "git@github.com:Owner/State.git\n", ""
            )
            self.assertEqual("owner/state", CORE.git_repository_slug(self.root))

    def test_binding_checks_root_origin_product_and_caller(self) -> None:
        completed = subprocess.CompletedProcess([], 0, str(self.root) + "\n", "")
        with (
            patch.object(CORE, "run", return_value=completed),
            patch.object(CORE, "git_repository_slug", return_value="other/state"),
            self.assertRaisesRegex(RuntimeError, "state repository"),
        ):
            CORE.assert_project_binding()

        other = self.root.parent / f"{self.root.name}-other"
        wrong_top = subprocess.CompletedProcess([], 0, str(other) + "\n", "")
        with (
            patch.object(CORE, "run", return_value=wrong_top),
            self.assertRaisesRegex(RuntimeError, "bound state repository root"),
        ):
            CORE.assert_project_binding()
        CORE.RUNTIME.mkdir()
        CORE.CONFIG.write_text(
            json.dumps(
                {
                    "projects_root": str(self.root),
                    "product_worktree": "product",
                    "github_repository": "owner/wrong",
                    "push_enabled": False,
                }
            )
        )
        with (
            patch.object(CORE, "run", return_value=completed),
            patch.object(CORE, "git_repository_slug", return_value="owner/state"),
            self.assertRaisesRegex(RuntimeError, "runtime product"),
        ):
            CORE.assert_project_binding()
        runtime = json.loads(CORE.CONFIG.read_text())
        runtime["github_repository"] = "owner/product"
        CORE.CONFIG.write_text(json.dumps(runtime))
        with (
            patch.object(CORE, "run", return_value=completed),
            patch.object(CORE, "git_repository_slug", side_effect=["owner/state", "owner/wrong"]),
            self.assertRaisesRegex(RuntimeError, "product checkout"),
        ):
            CORE.assert_project_binding()
        with (
            patch.object(CORE, "run", return_value=completed),
            patch.object(CORE, "git_repository_slug", side_effect=["owner/state", "owner/product"]),
            patch.object(CORE.Path, "cwd", return_value=other),
            self.assertRaisesRegex(RuntimeError, "must be called"),
        ):
            CORE.assert_project_binding()

    def test_binding_accepts_linked_product_worktree_with_matching_origin(self) -> None:
        projects_root = self.root.parent
        product = projects_root / f"{self.root.name}-product"
        linked = projects_root / f"{self.root.name}-product-worker"
        product.mkdir()
        linked.mkdir()
        CORE.CONFIG.parent.mkdir()
        CORE.CONFIG.write_text(
            json.dumps(
                {
                    "projects_root": str(projects_root),
                    "product_worktree": product.name,
                    "github_repository": "owner/product",
                    "push_enabled": False,
                }
            )
        )

        def git_query(args: list[str], **_: object) -> subprocess.CompletedProcess[str]:
            if args[-2:] == ["rev-parse", "--show-toplevel"]:
                checkout = Path(args[2])
                top = linked if checkout == linked else self.root
                return subprocess.CompletedProcess(args, 0, str(top) + "\n", "")
            if args[-3:] == ["remote", "get-url", "origin"]:
                remote = (
                    "git@github.com:owner/product.git"
                    if Path(args[2]) != CORE.ROOT
                    else "git@github.com:owner/state.git"
                )
                return subprocess.CompletedProcess(args, 0, remote + "\n", "")
            raise AssertionError(args)

        with (
            patch.object(CORE, "run", side_effect=git_query),
            patch.object(CORE.Path, "cwd", return_value=linked),
        ):
            CORE.assert_project_binding()

    def configure_product_invocation(self, product: Path) -> None:
        """Configure one product checkout for wrapped-command identity tests."""
        CORE.CONFIG.parent.mkdir(parents=True, exist_ok=True)
        CORE.CONFIG.write_text(
            json.dumps(
                {
                    "projects_root": str(product.parent),
                    "product_worktree": product.name,
                    "github_repository": "owner/product",
                    "push_enabled": False,
                }
            )
        )

    def product_git_query(self, product: Path, args: list[str], **_: object) -> Any:
        """Answer the bounded Git identity queries used by invocation preflight."""
        if args[-2:] == ["rev-parse", "--show-toplevel"]:
            return subprocess.CompletedProcess(args, 0, str(product) + "\n", "")
        if args[-4:] == ["symbolic-ref", "--short", "-q", "HEAD"]:
            return subprocess.CompletedProcess(args, 0, "feature/good\n", "")
        raise AssertionError(args)

    def test_wrapped_product_invocation_must_match_declared_worktree(self) -> None:
        product = self.root / "product"
        product.mkdir()
        self.configure_product_invocation(product)
        self.make_task(
            status="in_progress",
            owner="worker",
            claim_expires="2999-01-01T00:00:00+00:00",
            worktree_key="product",
            branch="feature/good",
        )
        with (
            patch.object(CORE.Path, "cwd", return_value=product),
            patch.object(
                CORE,
                "run",
                side_effect=lambda args, **kwargs: self.product_git_query(product, args, **kwargs),
            ),
        ):
            CORE.require_active_owner("AR-0001", "worker")

    def test_wrapped_product_invocation_rejects_wrong_worktree_or_branch(self) -> None:
        product = self.root / "product"
        product.mkdir()
        self.configure_product_invocation(product)
        self.make_task(
            status="in_progress",
            owner="worker",
            claim_expires="2999-01-01T00:00:00+00:00",
            worktree_key="other-worktree",
            branch="feature/good",
        )
        with (
            patch.object(CORE.Path, "cwd", return_value=product),
            patch.object(
                CORE,
                "run",
                side_effect=lambda args, **kwargs: self.product_git_query(product, args, **kwargs),
            ),
            self.assertRaisesRegex(RuntimeError, "does not match declared worktree"),
        ):
            CORE.require_active_owner("AR-0001", "worker")

        meta, body = CORE.read_task(CORE.locate("AR-0001")[0])
        meta["worktree_key"] = "product"
        meta["branch"] = "feature/expected"
        CORE.write_task(CORE.locate("AR-0001")[0], meta, body)
        with (
            patch.object(CORE.Path, "cwd", return_value=product),
            patch.object(
                CORE,
                "run",
                side_effect=lambda args, **kwargs: self.product_git_query(product, args, **kwargs),
            ),
            self.assertRaisesRegex(RuntimeError, "does not match declared branch"),
        ):
            CORE.require_active_owner("AR-0001", "worker")

    def test_wrapped_state_invocation_remains_valid_for_state_commands(self) -> None:
        self.make_task(
            status="in_progress",
            owner="worker",
            claim_expires="2999-01-01T00:00:00+00:00",
            worktree_key="product",
            branch="feature/good",
        )
        with patch.object(CORE.Path, "cwd", return_value=self.root):
            CORE.require_active_owner("AR-0001", "worker")

    def test_wrapped_product_invocation_requires_declared_identity(self) -> None:
        product = self.root / "product"
        product.mkdir()
        self.configure_product_invocation(product)
        self.make_task(
            status="in_progress",
            owner="worker",
            claim_expires="2999-01-01T00:00:00+00:00",
        )
        with (
            patch.object(CORE.Path, "cwd", return_value=product),
            patch.object(
                CORE,
                "run",
                side_effect=lambda args, **kwargs: self.product_git_query(product, args, **kwargs),
            ),
            self.assertRaisesRegex(RuntimeError, "lacks declared worktree"),
        ):
            CORE.require_active_owner("AR-0001", "worker")

    def test_atomic_task_round_trip_and_render(self) -> None:
        path = self.make_task()
        meta, body = CORE.read_task(path)
        self.assertEqual("AR-0001", meta["id"])
        self.assertEqual("# Test\n", body)
        current = CORE.render_current(CORE.all_tasks())
        self.assertIn("## Open", current)
        self.assertIn("[AR-0001]", current)
        status = CORE.render_status_view(CORE.all_tasks())
        self.assertIn("flowchart LR", status)
        self.assertIn("**1 ARs tracked**", status)

    def test_current_projection_is_actionable_and_keeps_terminal_history_out(self) -> None:
        self.make_task("AR-0001", status="open", priority="P0")
        self.make_task("AR-0002", status="in_progress", priority="P1")
        self.make_task("AR-0003", status="blocked", priority="P2")
        self.make_task("AR-0004", status="planned", priority="P3")
        self.make_task("AR-0005", status="future", priority="P4")
        for index, status in enumerate(("done", "cancelled", "superseded"), start=6):
            self.make_task(f"AR-000{index}", status=status, priority="P0")

        current = CORE.render_current(CORE.all_tasks())

        for task_id in ("AR-0001", "AR-0002", "AR-0003", "AR-0004", "AR-0005"):
            self.assertIn(f"[{task_id}]", current)
        for task_id in ("AR-0006", "AR-0007", "AR-0008"):
            self.assertNotIn(f"[{task_id}]", current)
        for label in ("Done", "Cancelled", "Superseded"):
            self.assertNotIn(f"## {label}", current)

    def test_status_is_deterministic_complete_accessible_and_injection_safe(self) -> None:
        self.make_task(
            "AR-0001",
            title="Hostile ](https://example.invalid) | `code`\n%%{init: bad}%%",
            summary="<script>alert(1)</script>",
        )
        self.make_task("AR-0002", status="done", priority="P0", depends_on=["AR-0001"])
        tasks = CORE.all_tasks()
        status = CORE.render_status_view(tasks)
        self.assertEqual(status, CORE.render_status_view(list(reversed(tasks))))
        self.assertEqual(2, status.count(":::status_"))
        self.assertIn('subgraph series_00["00 - Coordination foundation"]', status)
        self.assertEqual(1, status.count("AR_0001 --> AR_0002"))
        self.assertIn("Accessible dependency index", status)
        self.assertIn("&#93;(https://example.invalid)", status)
        self.assertIn("&lt;script&gt;alert(1)&lt;/script&gt;", status)
        self.assertNotIn("%%{init: bad}%%", status)

    def test_status_contains_company_role_and_task_rollups_without_private_body_data(self) -> None:
        self.make_task(
            "AR-0001",
            title="Company parent",
            role="implementer",
            team="platform",
            children=["AR-0002"],
            summary="Public parent summary",
        )
        self.make_task(
            "AR-0002",
            role="reviewer",
            team="platform",
            parent_task_ref="AR-0001",
            status="done",
            summary="Public child summary",
        )
        tasks = CORE.all_tasks()
        status = CORE.render_status_view(tasks)
        self.assertEqual(status, CORE.render_status_view(list(reversed(tasks))))
        self.assertIn("## Company hierarchy rollup", status)
        self.assertIn("## Role and team rollup", status)
        self.assertIn("## Task drill-down", status)
        self.assertIn("| implementer | platform | 1 | 1 | 0 | 0 |", status)
        self.assertIn("| Parent | AR-0001 |", status)
        self.assertNotIn("\n# Test\n", status)

    def test_future_series_is_never_omitted_from_graph_or_text_fallback(self) -> None:
        self.make_task("AR-1101")
        status = CORE.render_status_view(CORE.all_tasks())
        self.assertEqual(1, status.count('AR_1101["AR-1101 - Open"]'))
        self.assertIn('subgraph series_11["11 - Additional work"]', status)
        self.assertIn("| [AR-1101](tasks/AR-1101-test.md) | None | None |", status)

    def test_large_status_is_deterministically_sharded_below_limit(self) -> None:
        payload = "meaningful status context " * 18
        for number in range(1, 301):
            self.make_task(
                f"AR-{number:04d}",
                summary=payload,
                next_action=payload,
            )
        views = CORE.render_status_views(CORE.all_tasks())
        self.assertGreater(len(views), 2)
        self.assertIn("status/STATUS-0001.md", views["STATUS.md"])
        self.assertNotIn("flowchart LR", views["STATUS.md"])
        for relative in re.findall(r"\]\((status/STATUS-\d{4}\.md)\)", views["STATUS.md"]):
            self.assertIn(relative, views)
        for relative, content in views.items():
            self.assertLessEqual(len(content.encode()), 200_000, relative)
        pages = [content for path, content in views.items() if path != "STATUS.md"]
        combined = "\n".join(pages)
        self.assertTrue(all("](tasks/" not in page for page in pages))
        self.assertTrue(any("](../tasks/" in page for page in pages))
        prefix = (
            "<!-- This page is generated; the root STATUS.md index links the complete view. -->\n\n"
        )
        full = CORE.render_status_view(CORE.all_tasks())
        self.assertEqual(
            full,
            "".join(page.removeprefix(prefix) for page in pages).replace("](../tasks/", "](tasks/"),
        )
        for number in range(1, 301):
            self.assertIn(f"AR-{number:04d}", combined)
        self.assertEqual(views, CORE.render_status_views(list(reversed(CORE.all_tasks()))))

    def test_status_shards_are_checked_and_stale_pages_are_rejected(self) -> None:
        payload = "status detail " * 18
        for number in range(1, 301):
            self.make_task(f"AR-{number:04d}", summary=payload, next_action=payload)
        views = CORE.render_status_views(CORE.all_tasks())
        for relative, content in views.items():
            CORE.atomic(self.root / relative, content)
        stale = self.root / "status" / "STATUS-9999.md"
        stale.write_text("stale")
        errors = CORE.generated_view_errors(CORE.all_tasks())
        self.assertIn("status/STATUS-9999.md is stale", errors)
        stale.unlink()
        self.assertEqual([], CORE.generated_view_errors(CORE.all_tasks()))

    def test_status_rejects_malformed_duplicate_self_missing_and_cycles(self) -> None:
        first = self.make_task("AR-0001")
        second = self.make_task("AR-0002")
        meta, body = CORE.read_task(first)
        meta["depends_on"] = ["AR-0001", "AR-9999"]
        CORE.write_task(first, meta, body)
        other, other_body = CORE.read_task(second)
        other["depends_on"] = ["AR-0001", "AR-0001"]
        CORE.write_task(second, other, other_body)
        errors = "\n".join(CORE.graph_errors(CORE.all_tasks()))
        self.assertIn("duplicate dependency AR-0001", errors)
        self.assertIn("self dependency", errors)
        self.assertIn("missing dependency AR-9999", errors)
        self.assertIn("dependency cycle", errors)
        other["depends_on"] = "AR-0001"
        CORE.write_task(second, other, other_body)
        self.assertIn("must be a list", "\n".join(CORE.graph_errors(CORE.all_tasks())))
        duplicate = self.root / "tasks" / "AR-0001-copy.md"
        CORE.write_task(duplicate, meta, body)
        self.assertIn("duplicate graph node", "\n".join(CORE.graph_errors(CORE.all_tasks())))

    def test_status_rejects_unsafe_filename_and_unknown_presentation(self) -> None:
        path = self.make_task()
        task = CORE.all_tasks()[0]
        with self.assertRaisesRegex(CORE.StatusRenderError, "unsafe"):
            CORE.render_status_view([(path.with_name("AR-0001-BAD.md"), task[1], task[2])])
        task[1]["priority"] = "PX"
        with self.assertRaisesRegex(CORE.StatusRenderError, "unknown status or priority"):
            CORE.render_status_view([task])

    def test_rejects_bad_front_matter(self) -> None:
        path = CORE.TASKS / "AR-0001-bad.md"
        path.write_text("bad")
        with self.assertRaisesRegex(ValueError, "no front matter"):
            CORE.read_task(path)
        path.write_text("---\n{}")
        with self.assertRaisesRegex(ValueError, "unterminated"):
            CORE.read_task(path)

    def test_validation_finds_schema_graph_claim_and_privacy_errors(self) -> None:
        first = self.make_task("AR-0001", extra="bad")
        second = self.make_task(
            "AR-0002",
            status="in_progress",
            owner="worker-a",
            claim_expires="",
        )
        first_meta, first_body = CORE.read_task(first)
        second_meta, second_body = CORE.read_task(second)
        first_meta["depends_on"] = ["AR-0002"]
        second_meta["depends_on"] = ["AR-0001"]
        CORE.write_task(first, first_meta, first_body)
        CORE.write_task(second, second_meta, second_body)
        (self.root / "leak.md").write_text("/" + "home/example")
        errors = CORE.validate()
        joined = "\n".join(errors)
        self.assertIn("unknown field extra", joined)
        self.assertIn("active without claim", joined)
        self.assertIn("dependency cycle", joined)
        self.assertIn("absolute Linux home path", joined)

    def test_claim_update_release_and_stale_revision(self) -> None:
        path = self.make_task()
        (self.root / "spec.json").write_text(
            json.dumps(
                {
                    "schema_version": 1,
                    "spec_ref": "spec.json",
                    "spec_revision": 1,
                    "acceptance_predicates": [{"id": "predicate", "description": "pass"}],
                    "definition_of_done": ["pass"],
                    "inputs": [{"id": "input", "description": "input"}],
                    "outputs": [{"id": "output", "description": "output"}],
                    "allowed_tools": ["source.read"],
                    "forbidden_tools": [],
                    "required_evidence_classes": ["contract-test"],
                    "gates": [{"id": "gate", "description": "pass"}],
                }
            )
        )
        with patch.object(CORE, "commit", return_value=True):
            CORE.mutate(
                argparse.Namespace(task="AR-0001", owner="worker-a", lease_minutes=10),
                "claim",
            )
            meta, _ = CORE.read_task(path)
            self.assertEqual("in_progress", meta["status"])
            revision = meta["task_revision"]
            with self.assertRaisesRegex(RuntimeError, "stale revision"):
                CORE.mutate(
                    argparse.Namespace(
                        task="AR-0001",
                        owner="worker-a",
                        expected_revision=revision - 1,
                        status=None,
                        priority=None,
                        summary=None,
                        next_action=None,
                        note="stale",
                    ),
                    "update",
                )
            CORE.mutate(
                argparse.Namespace(
                    task="AR-0001",
                    owner="worker-a",
                    expected_revision=revision,
                    status=None,
                    priority="P0",
                    summary="Updated.",
                    next_action="Continue.",
                    note="verified",
                ),
                "update",
            )
            meta, body = CORE.read_task(path)
            meta["spec_ref"] = "spec.json"
            meta["spec_revision"] = 1
            meta["spec_acceptance"] = {
                "spec_ref": "spec.json",
                "spec_revision": 1,
                "status": "pass",
                "evidence_class": "contract-test",
                "evidence_ref": "awq/evidence/AR-0001",
                "evidence_digest": "sha256:" + "a" * 64,
            }
            CORE.write_task(path, meta, body)
            CORE.mutate(
                argparse.Namespace(
                    task="AR-0001",
                    owner="worker-a",
                    status="done",
                    note="verified completion evidence " * 8,
                ),
                "release",
            )
        meta, _ = CORE.read_task(path)
        self.assertEqual("done", meta["status"])
        self.assertEqual("", meta["owner"])
        self.assertTrue(all(len(line) <= 100 for line in path.read_text().splitlines()))

    def test_claim_enforces_dependencies_owner_and_positive_lease(self) -> None:
        self.make_task("AR-0001")
        self.make_task("AR-0002", depends_on=["AR-0001"])
        with patch.object(CORE, "commit", return_value=True):
            with self.assertRaisesRegex(RuntimeError, "unfinished dependencies"):
                CORE.mutate(
                    argparse.Namespace(task="AR-0002", owner="worker-a", lease_minutes=10),
                    "claim",
                )
            with self.assertRaisesRegex(RuntimeError, "positive"):
                CORE.mutate(
                    argparse.Namespace(task="AR-0001", owner="worker-a", lease_minutes=0),
                    "claim",
                )
            CORE.mutate(
                argparse.Namespace(task="AR-0001", owner="worker-a", lease_minutes=10),
                "claim",
            )
            with self.assertRaisesRegex(RuntimeError, "not open"):
                CORE.mutate(
                    argparse.Namespace(task="AR-0001", owner="worker-b", lease_minutes=10),
                    "claim",
                )

    def test_superseded_dependency_requires_done_successor_chain(self) -> None:
        self.make_task("AR-0003", status="done")
        self.make_task("AR-0002", status="superseded", superseded_by="AR-0003")
        self.make_task("AR-0001", status="superseded", superseded_by="AR-0002")
        self.make_task("AR-0004", depends_on=["AR-0001"])
        with patch.object(CORE, "commit", return_value=True):
            CORE.mutate(
                argparse.Namespace(task="AR-0004", owner="worker-a", lease_minutes=10),
                "claim",
            )
        self.assertEqual("in_progress", CORE.read_task(CORE.TASKS / "AR-0004-test.md")[0]["status"])

    def test_superseded_dependency_fails_closed_for_missing_or_unfinished_successor(self) -> None:
        self.make_task("AR-0003", status="open")
        self.make_task("AR-0002", status="superseded", superseded_by="AR-0003")
        self.make_task("AR-0001", depends_on=["AR-0002"])
        with self.assertRaisesRegex(RuntimeError, "unfinished dependencies"):
            CORE.mutate(
                argparse.Namespace(task="AR-0001", owner="worker-a", lease_minutes=10),
                "claim",
            )

        dependency, body = CORE.read_task(CORE.TASKS / "AR-0002-test.md")
        dependency["superseded_by"] = "AR-9999"
        CORE.write_task(CORE.TASKS / "AR-0002-test.md", dependency, body)
        self.refresh_views()
        self.assertIn("missing superseded_by task", "\n".join(CORE.validate()))

    def test_supersession_validation_rejects_invalid_status_self_and_cycle(self) -> None:
        self.make_task("AR-0001", status="open", superseded_by="AR-0002")
        self.make_task("AR-0002", status="superseded", superseded_by="bad")
        self.make_task("AR-0003", status="superseded", superseded_by="AR-0003")
        self.make_task("AR-0004", status="superseded", superseded_by="AR-0005")
        self.make_task("AR-0005", status="superseded", superseded_by="AR-0004")

        errors = "\n".join(CORE.validate())
        self.assertIn("AR-0001: superseded_by requires superseded status", errors)
        self.assertIn("AR-0002: invalid superseded_by", errors)
        self.assertIn("AR-0003: superseded_by self reference", errors)
        self.assertIn("AR-0004: superseded_by chain does not end in done task", errors)
        self.assertIn("AR-0005: superseded_by chain does not end in done task", errors)

    def test_promote_is_dependency_revision_and_state_aware(self) -> None:
        dependency = self.make_task("AR-0001", status="done")
        target = self.make_task(
            "AR-0002",
            status="planned",
            depends_on=["AR-0001"],
        )
        before = target.read_text()
        args = argparse.Namespace(
            task="AR-0002",
            expected_revision=0,
            note="dependencies verified",
        )
        with (
            patch.object(CORE, "dirty_state_paths", return_value=[]),
            self.assertRaisesRegex(RuntimeError, "stale revision"),
        ):
            CORE.mutate(args, "promote")
        self.assertEqual(before, target.read_text())

        dependency_meta, dependency_body = CORE.read_task(dependency)
        dependency_meta["status"] = "open"
        CORE.write_task(dependency, dependency_meta, dependency_body)
        self.refresh_views()
        args.expected_revision = 1
        with (
            patch.object(CORE, "dirty_state_paths", return_value=[]),
            self.assertRaisesRegex(RuntimeError, "unfinished dependencies"),
        ):
            CORE.mutate(args, "promote")
        dependency_meta["status"] = "done"
        CORE.write_task(dependency, dependency_meta, dependency_body)
        self.refresh_views()

        args.note = ""
        with (
            patch.object(CORE, "dirty_state_paths", return_value=[]),
            self.assertRaisesRegex(RuntimeError, "must not be empty"),
        ):
            CORE.mutate(args, "promote")
        args.note = "dependencies verified"

        with (
            patch.object(CORE, "dirty_state_paths", return_value=[]),
            patch.object(CORE, "commit", return_value=True),
        ):
            CORE.mutate(args, "promote")
        meta, body = CORE.read_task(target)
        self.assertEqual("open", meta["status"])
        self.assertEqual(2, meta["task_revision"])
        self.assertIn("dependencies verified", body)
        self.assertIn("AR_0001 --> AR_0002", (self.root / "STATUS.md").read_text())
        self.assertIn("## Open", (self.root / "CURRENT.md").read_text())

    def test_promote_rejects_dirty_invalid_claimed_and_nonplanned_state(self) -> None:
        path = self.make_task(status="planned")
        args = argparse.Namespace(task="AR-0001", expected_revision=1, note="ready")
        with (
            patch.object(CORE, "dirty_state_paths", return_value=[" M tasks/other.md"]),
            self.assertRaisesRegex(RuntimeError, "clean state repository"),
        ):
            CORE.mutate(args, "promote")
        self.assertEqual("planned", CORE.read_task(path)[0]["status"])

        (self.root / "STATUS.md").write_text("stale")
        with (
            patch.object(CORE, "dirty_state_paths", return_value=[]),
            self.assertRaisesRegex(RuntimeError, "promotion preflight failed"),
        ):
            CORE.mutate(args, "promote")
        self.refresh_views()

        meta, body = CORE.read_task(path)
        meta["owner"] = "worker-a"
        meta["claim_expires"] = "2099-01-01T00:00:00+00:00"
        CORE.write_task(path, meta, body)
        self.refresh_views()
        with (
            patch.object(CORE, "dirty_state_paths", return_value=[]),
            self.assertRaisesRegex(RuntimeError, "active claim metadata"),
        ):
            CORE.mutate(args, "promote")
        meta["owner"] = ""
        meta["claim_expires"] = ""
        meta["status"] = "future"
        CORE.write_task(path, meta, body)
        self.refresh_views()
        with (
            patch.object(CORE, "dirty_state_paths", return_value=[]),
            self.assertRaisesRegex(RuntimeError, "not planned"),
        ):
            CORE.mutate(args, "promote")

    def test_resume_reopens_only_exact_blocked_revision(self) -> None:
        target = self.make_task("AR-0001", status="blocked")
        CORE.append_session_record(
            CORE.ROOT,
            CORE.build_session_record(
                CORE.read_task(target)[0], "pause", "2026-09-24T12:00:00+00:00"
            ),
        )
        args = argparse.Namespace(
            task="AR-0001", expected_revision=0, session="AR-0001@1", note="blocker cleared"
        )
        with (
            patch.object(CORE, "dirty_state_paths", return_value=[]),
            self.assertRaisesRegex(RuntimeError, "stale revision"),
        ):
            CORE.mutate(args, "resume")

        args.expected_revision = 1
        args.note = ""
        with (
            patch.object(CORE, "dirty_state_paths", return_value=[]),
            self.assertRaisesRegex(RuntimeError, "must not be empty"),
        ):
            CORE.mutate(args, "resume")

        args.note = "blocker cleared"
        with (
            patch.object(CORE, "dirty_state_paths", return_value=[]),
            patch.object(CORE, "commit", return_value=True),
        ):
            CORE.mutate(args, "resume")
        meta, body = CORE.read_task(target)
        self.assertEqual("open", meta["status"])
        self.assertEqual("", meta["owner"])
        self.assertEqual(2, meta["task_revision"])
        self.assertIn("blocker cleared", body)

        with (
            patch.object(CORE, "dirty_state_paths", return_value=[]),
            self.assertRaisesRegex(RuntimeError, "not blocked"),
        ):
            CORE.mutate(
                argparse.Namespace(
                    task="AR-0001", expected_revision=2, session="AR-0001@1", note="again"
                ),
                "resume",
            )

    def test_external_unblock_release_reopen_and_claim_preserves_state(self) -> None:
        target = self.make_task(
            status="in_progress",
            owner="worker-a",
            claim_expires="2099-01-01T00:00:00+00:00",
            next_action="Wait for external AR-9999.",
        )
        with patch.object(CORE, "commit", return_value=True):
            CORE.mutate(
                argparse.Namespace(
                    task="AR-0001", owner="worker-a", status="blocked", note="external wait"
                ),
                "release",
            )
        blocked, _ = CORE.read_task(target)
        self.assertEqual(("blocked", 2), (blocked["status"], blocked["task_revision"]))
        self.assertEqual([], CORE.storage_backend().load_session_records("AR-0001"))

        with (
            patch.object(CORE, "dirty_state_paths", return_value=[]),
            patch.object(CORE, "commit", return_value=True),
        ):
            CORE.mutate(
                argparse.Namespace(
                    task="AR-0001", expected_revision=2, note="external dependency verified"
                ),
                "unblock",
            )
            CORE.mutate(
                argparse.Namespace(task="AR-0001", owner="worker-b", lease_minutes=10),
                "claim",
            )
        reopened, body = CORE.read_task(target)
        self.assertEqual(("in_progress", 4), (reopened["status"], reopened["task_revision"]))
        self.assertEqual("Wait for external AR-9999.", reopened["next_action"])
        self.assertEqual([], CORE.storage_backend().load_session_records("AR-0001"))
        self.assertIn("external dependency verified", body)

    def test_unblock_and_resume_reject_cross_mode_and_hostile_provenance(self) -> None:
        target = self.make_task(status="blocked", task_revision=2)
        blocked, _ = CORE.read_task(target)
        stale = argparse.Namespace(task="AR-0001", expected_revision=1, note="clear")
        with self.assertRaisesRegex(RuntimeError, "stale revision"):
            CORE.apply_unblock(stale, dict(blocked), [])

        active = dict(blocked, owner="worker-a", claim_expires="later")
        current = argparse.Namespace(task="AR-0001", expected_revision=2, note="clear")
        with self.assertRaisesRegex(RuntimeError, "active claim metadata"):
            CORE.apply_unblock(current, active, [])
        with self.assertRaisesRegex(RuntimeError, "must not be empty"):
            CORE.apply_unblock(
                argparse.Namespace(task="AR-0001", expected_revision=2, note=""),
                dict(blocked),
                [],
            )

        old = dict(blocked, task_revision=1)
        CORE.append_session_record(
            CORE.ROOT,
            CORE.build_session_record(old, "pause", "2026-09-24T12:00:00+00:00"),
        )
        preserved = dict(blocked)
        self.assertEqual("clear", CORE.apply_unblock(current, preserved, []))
        self.assertEqual("open", preserved["status"])

        pause = CORE.build_session_record(blocked, "pause", "2026-09-24T12:01:00+00:00")
        CORE.append_session_record(CORE.ROOT, pause)
        with self.assertRaisesRegex(RuntimeError, "task is paused"):
            CORE.apply_unblock(current, dict(blocked), [])

        external = self.make_task("AR-0002", status="blocked")
        external_meta, _ = CORE.read_task(external)
        with self.assertRaisesRegex(RuntimeError, "no session snapshot"):
            CORE.apply_resume(
                argparse.Namespace(
                    task="AR-0002", expected_revision=1, session="AR-0002@1", note="wrong mode"
                ),
                external_meta,
                [],
            )

        malformed = dict(pause, step_state={"status": "open", "task_revision": 2})
        backend = SimpleNamespace(load_session_records=lambda _task: [malformed])
        with (
            patch.object(CORE, "storage_backend", return_value=backend),
            self.assertRaisesRegex(RuntimeError, "provenance is malformed"),
        ):
            CORE.apply_unblock(current, dict(blocked), [])
        duplicate = SimpleNamespace(load_session_records=lambda _task: [pause, dict(pause)])
        with (
            patch.object(CORE, "storage_backend", return_value=duplicate),
            self.assertRaisesRegex(RuntimeError, "provenance is ambiguous"),
        ):
            CORE.apply_unblock(current, dict(blocked), [])

    def test_resume_rejects_hostile_pause_provenance_without_mutation(self) -> None:
        target = self.make_task(status="blocked", task_revision=7)
        blocked, _ = CORE.read_task(target)
        pause = CORE.build_session_record(blocked, "pause", "2026-10-08T00:00:00+00:00")
        args = argparse.Namespace(
            task="AR-0001", expected_revision=7, session="AR-0001@7", note="resume"
        )
        hostile = (
            ([pause, dict(pause)], "ambiguous"),
            (
                [dict(pause, step_state={"status": "open", "task_revision": 7})],
                "malformed",
            ),
            (
                [dict(pause, step_state={"status": "blocked", "task_revision": 6})],
                "malformed",
            ),
            ([dict(pause, task="AR-0002")], "coherent paused"),
            ([dict(pause, trigger="update")], "coherent paused"),
            (
                [dict(pause, status="open", step_state={"status": "open", "task_revision": 7})],
                "coherent paused",
            ),
        )
        for records, message in hostile:
            candidate = dict(blocked)
            with (
                self.subTest(message=message),
                patch.object(
                    CORE,
                    "storage_backend",
                    return_value=SimpleNamespace(
                        load_session_records=lambda _task, value=records: value
                    ),
                ),
                self.assertRaisesRegex(RuntimeError, message),
            ):
                CORE.apply_resume(args, candidate, [])
            self.assertEqual(blocked, candidate)

    def test_git_resume_hostile_histories_stutter_before_publication(self) -> None:
        target = self.make_task(status="blocked", task_revision=7)
        blocked, _ = CORE.read_task(target)
        pause = CORE.build_session_record(blocked, "pause", "2026-10-08T00:00:00+00:00")
        histories = (
            [pause, dict(pause)],
            [
                dict(
                    pause,
                    task_revision=True,
                    step_state={"status": "blocked", "task_revision": True},
                )
            ],
            [dict(pause, step_state={"status": "open", "task_revision": 7})],
            [dict(pause, step_state={"status": "blocked", "task_revision": 6})],
            [dict(pause, task="AR-0002")],
            [dict(pause, trigger="update")],
        )
        session = self.root / "sessions/AR-0001.jsonl"
        session.parent.mkdir()
        args = argparse.Namespace(
            task="AR-0001", expected_revision=7, session="AR-0001@7", note="resume"
        )
        for records in histories:
            session.write_text(
                "".join(json.dumps(record, sort_keys=True) + "\n" for record in records)
            )
            before = {
                path: path.read_bytes()
                for path in (target, self.root / "CURRENT.md", self.root / "STATUS.md", session)
            }
            with (
                self.subTest(records=records),
                patch.object(CORE, "dirty_state_paths", return_value=[]),
                patch.object(CORE, "commit") as commit,
                patch.object(CORE, "push_replica") as push,
                self.assertRaises(RuntimeError),
            ):
                CORE.mutate(args, "resume")
            self.assertTrue(all(path.read_bytes() == content for path, content in before.items()))
            commit.assert_not_called()
            push.assert_not_called()

    def test_unblock_failure_restores_task_views_and_session_history(self) -> None:
        target = self.make_task(status="blocked")
        before = {
            path: path.read_text()
            for path in (target, self.root / "CURRENT.md", self.root / "STATUS.md")
        }
        real_atomic = CORE.atomic

        def fail_task(path: Path, content: str) -> None:
            if path == target:
                raise OSError("injected unblock failure")
            real_atomic(path, content)

        with (
            patch.object(CORE, "dirty_state_paths", return_value=[]),
            patch.object(CORE, "atomic", side_effect=fail_task),
            self.assertRaisesRegex(OSError, "injected unblock failure"),
        ):
            CORE.mutate(
                argparse.Namespace(task="AR-0001", expected_revision=1, note="external clear"),
                "unblock",
            )
        self.assertTrue(all(path.read_text() == content for path, content in before.items()))
        self.assertEqual([], CORE.storage_backend().load_session_records("AR-0001"))

    def test_resume_failure_restores_task_views_and_preserves_pause_history(self) -> None:
        target = self.make_task(status="blocked")
        blocked, _ = CORE.read_task(target)
        CORE.append_session_record(
            CORE.ROOT,
            CORE.build_session_record(blocked, "pause", "2026-10-08T00:00:00+00:00"),
        )
        session = self.root / "sessions/AR-0001.jsonl"
        before = {
            path: path.read_text()
            for path in (target, self.root / "CURRENT.md", self.root / "STATUS.md", session)
        }
        real_atomic = CORE.atomic

        def fail_task(path: Path, content: str) -> None:
            if path == target:
                raise OSError("injected resume failure")
            real_atomic(path, content)

        with (
            patch.object(CORE, "dirty_state_paths", return_value=[]),
            patch.object(CORE, "atomic", side_effect=fail_task),
            self.assertRaisesRegex(OSError, "injected resume failure"),
        ):
            CORE.mutate(
                argparse.Namespace(
                    task="AR-0001",
                    expected_revision=1,
                    session="AR-0001@1",
                    note="resume",
                ),
                "resume",
            )
        self.assertTrue(all(path.read_text() == content for path, content in before.items()))

    def test_pause_freezes_lease_and_resume_reloads_exact_snapshot(self) -> None:
        target = self.make_task(
            status="in_progress",
            owner="worker-a",
            claim_expires="2099-01-01T00:00:00+00:00",
            next_action="Continue the verified step.",
        )
        pause = argparse.Namespace(
            task="AR-0001",
            owner="worker-a",
            expected_revision=1,
            note="operator pause",
        )
        with patch.object(CORE, "commit", return_value=True):
            CORE.mutate(pause, "pause")
        paused, _ = CORE.read_task(target)
        self.assertEqual(
            ("blocked", "", ""), (paused["status"], paused["owner"], paused["claim_expires"])
        )
        self.assertEqual(2, paused["task_revision"])
        snapshot = CORE.latest_session(CORE.ROOT, "AR-0001")
        self.assertIsNotNone(snapshot)
        assert snapshot is not None
        self.assertEqual(
            ("pause", "blocked", 2),
            (snapshot["trigger"], snapshot["status"], snapshot["task_revision"]),
        )

        resume = argparse.Namespace(
            task="AR-0001", expected_revision=2, session="AR-0001@2", note="continue"
        )
        with (
            patch.object(CORE, "commit", return_value=True),
            patch.object(CORE, "dirty_state_paths", return_value=[]),
        ):
            CORE.mutate(resume, "resume")
        resumed, _ = CORE.read_task(target)
        self.assertEqual("open", resumed["status"])
        self.assertEqual("Continue the verified step.", resumed["next_action"])

    def test_pause_failure_restores_authority_and_session(self) -> None:
        target = self.make_task(
            status="in_progress",
            owner="worker-a",
            claim_expires="2099-01-01T00:00:00+00:00",
        )
        before = target.read_text()
        pause = argparse.Namespace(
            task="AR-0001", owner="worker-a", expected_revision=1, note="pause"
        )
        real_atomic = CORE.atomic

        failed = False

        def fail_task_once(path: Path, text: str) -> None:
            nonlocal failed
            if path == target and not failed:
                failed = True
                raise OSError("injected pause failure")
            real_atomic(path, text)

        with (
            patch.object(CORE, "atomic", side_effect=fail_task_once),
            self.assertRaisesRegex(OSError, "injected pause failure"),
        ):
            CORE.mutate(pause, "pause")
        self.assertEqual(before, target.read_text())
        self.assertIsNone(CORE.latest_session(CORE.ROOT, "AR-0001"))

    def test_pause_and_resume_reject_invalid_authority_and_references(self) -> None:
        target = self.make_task(
            status="in_progress",
            owner="worker-a",
            claim_expires="2099-01-01T00:00:00+00:00",
        )
        meta, _ = CORE.read_task(target)
        args = argparse.Namespace(
            task="AR-0001", owner="worker-b", expected_revision=1, note="pause"
        )
        with self.assertRaisesRegex(RuntimeError, "owned by worker-a"):
            CORE.apply_pause(args, meta)
        args.owner = "worker-a"
        args.expected_revision = 0
        with self.assertRaisesRegex(RuntimeError, "stale revision"):
            CORE.apply_pause(args, meta)
        args.expected_revision = 1
        meta["status"] = "open"
        with self.assertRaisesRegex(RuntimeError, "not in progress"):
            CORE.apply_pause(args, meta)
        meta["status"] = "in_progress"
        args.note = ""
        with self.assertRaisesRegex(RuntimeError, "must not be empty"):
            CORE.apply_pause(args, meta)

        with self.assertRaisesRegex(RuntimeError, "TASK@REVISION"):
            CORE._session_for_reference("AR-0001", "AR-0002@1")
        with self.assertRaisesRegex(RuntimeError, "no session snapshot"):
            CORE._session_for_reference("AR-0001", "AR-0001@9")
        with self.assertRaisesRegex(RuntimeError, "^no session snapshot at requested revision$"):
            CORE._session_for_reference("AR-0001", "AR-0001@" + "9" * 4000)

        CORE.append_session_record(
            CORE.ROOT,
            CORE.build_session_record(meta, "update", "2026-09-24T12:00:00+00:00"),
        )
        with self.assertRaisesRegex(RuntimeError, "not a coherent paused snapshot"):
            CORE._session_for_reference("AR-0001", "AR-0001@1")

        resume_meta = dict(meta, status="blocked", owner="worker-a", claim_expires="later")
        resume = argparse.Namespace(
            task="AR-0001", expected_revision=1, session="AR-0001@1", note="resume"
        )
        with self.assertRaisesRegex(RuntimeError, "active claim metadata"):
            CORE.apply_resume(resume, resume_meta, [])

    def test_promote_failure_restores_task_and_generated_views(self) -> None:
        path = self.make_task(status="planned")
        before = {
            item: item.read_text()
            for item in (path, self.root / "CURRENT.md", self.root / "STATUS.md")
        }
        args = argparse.Namespace(task="AR-0001", expected_revision=1, note="ready")
        real_atomic = CORE.atomic
        failed = False

        def fail_status_once(target: Path, text: str) -> None:
            nonlocal failed
            if target.name == "STATUS.md" and not failed:
                failed = True
                raise OSError("injected status failure")
            real_atomic(target, text)

        with (
            patch.object(CORE, "dirty_state_paths", return_value=[]),
            patch.object(CORE, "atomic", side_effect=fail_status_once),
            self.assertRaisesRegex(OSError, "injected status failure"),
        ):
            CORE.mutate(args, "promote")
        self.assertTrue(all(item.read_text() == text for item, text in before.items()))

        with (
            patch.object(CORE, "dirty_state_paths", return_value=[]),
            patch.object(CORE, "commit", side_effect=RuntimeError("injected commit failure")),
            self.assertRaisesRegex(RuntimeError, "injected commit failure"),
        ):
            CORE.mutate(args, "promote")
        self.assertTrue(all(item.read_text() == text for item, text in before.items()))

    def test_promote_push_failure_preserves_durable_state(self) -> None:
        path = self.make_task(status="planned")
        args = argparse.Namespace(task="AR-0001", expected_revision=1, note="ready")
        with (
            patch.object(CORE, "dirty_state_paths", return_value=[]),
            patch.object(CORE, "commit", return_value=True),
            patch.object(CORE, "push_replica", side_effect=RuntimeError("push failed")),
            self.assertRaisesRegex(RuntimeError, "push failed"),
        ):
            CORE.mutate(args, "promote")
        self.assertEqual("open", CORE.read_task(path)[0]["status"])
        self.assertEqual(
            CORE.render_status_view(CORE.all_tasks()), (self.root / "STATUS.md").read_text()
        )

    def test_dirty_state_paths_uses_complete_porcelain(self) -> None:
        completed = subprocess.CompletedProcess(
            ["git"],
            0,
            stdout=" M tasks/one.md\n?? tasks/two.md\n",
            stderr="",
        )
        with patch.object(CORE, "run", return_value=completed) as invoked:
            self.assertEqual(
                [" M tasks/one.md", "?? tasks/two.md"],
                CORE.dirty_state_paths(),
            )
        command = invoked.call_args.args[0]
        self.assertIn("--porcelain=v1", command)
        self.assertIn("--untracked-files=all", command)

    def test_concurrent_promote_and_reconcile_keep_source_and_views_atomic(self) -> None:
        self.make_task(status="planned")
        start = multiprocessing.Event()
        promote = multiprocessing.Process(target=concurrent_promote, args=(str(self.root), start))
        reconcile = multiprocessing.Process(
            target=concurrent_reconcile, args=(str(self.root), start)
        )
        promote.start()
        reconcile.start()
        start.set()
        promote.join(10)
        reconcile.join(10)
        self.assertEqual(0, promote.exitcode)
        self.assertEqual(0, reconcile.exitcode)
        meta, _ = CORE.read_task(CORE.locate("AR-0001")[0])
        self.assertEqual("open", meta["status"])
        self.assertEqual(
            CORE.render_current(CORE.all_tasks()), (self.root / "CURRENT.md").read_text()
        )
        self.assertEqual(
            CORE.render_status_view(CORE.all_tasks()), (self.root / "STATUS.md").read_text()
        )

    def test_invalid_update_rolls_back_both_files(self) -> None:
        path = self.make_task()
        with patch.object(CORE, "commit", return_value=True):
            CORE.mutate(
                argparse.Namespace(task="AR-0001", owner="worker-a", lease_minutes=10),
                "claim",
            )
            before_task = path.read_text()
            before_current = (self.root / "CURRENT.md").read_text()
            before_status = (self.root / "STATUS.md").read_text()
            revision = CORE.read_task(path)[0]["task_revision"]
            with self.assertRaisesRegex(RuntimeError, "invalid summary"):
                CORE.mutate(
                    argparse.Namespace(
                        task="AR-0001",
                        owner="worker-a",
                        expected_revision=revision,
                        status=None,
                        priority=None,
                        summary="",
                        next_action=None,
                        note="invalid",
                    ),
                    "update",
                )
        self.assertEqual(before_task, path.read_text())
        self.assertEqual(before_current, (self.root / "CURRENT.md").read_text())
        self.assertEqual(before_status, (self.root / "STATUS.md").read_text())

    def test_failed_push_preserves_durable_commit_state(self) -> None:
        path = self.make_task()
        with (
            patch.object(CORE, "commit", return_value=True),
            patch.object(CORE, "push_replica", side_effect=RuntimeError("push failed")),
            self.assertRaisesRegex(RuntimeError, "push failed"),
        ):
            CORE.mutate(
                argparse.Namespace(task="AR-0001", owner="worker-a", lease_minutes=10),
                "claim",
            )
        meta, _ = CORE.read_task(path)
        self.assertEqual("in_progress", meta["status"])
        self.assertEqual("worker-a", meta["owner"])
        self.assertEqual(
            CORE.render_current(CORE.all_tasks()), (self.root / "CURRENT.md").read_text()
        )
        self.assertEqual(
            CORE.render_status_view(CORE.all_tasks()), (self.root / "STATUS.md").read_text()
        )

    def test_lock_excludes_a_second_process(self) -> None:
        ready = multiprocessing.Event()
        release = multiprocessing.Event()
        process = multiprocessing.Process(
            target=hold_lock,
            args=(str(CORE.LOCK), ready, release),
        )
        process.start()
        self.assertTrue(ready.wait(5))
        start = time.monotonic()
        release.set()
        with CORE.locked():
            elapsed = time.monotonic() - start
        process.join(5)
        self.assertEqual(0, process.exitcode)
        self.assertGreaterEqual(elapsed, 0)

    def test_shared_readers_coexist_and_exclude_a_writer(self) -> None:
        ready = multiprocessing.Event()
        release = multiprocessing.Event()
        reader = multiprocessing.Process(
            target=hold_shared_lock,
            args=(str(CORE.LOCK), ready, release),
        )
        reader.start()
        self.assertTrue(ready.wait(5))
        try:
            with CORE.locked(exclusive=False, timeout=0.1):
                pass
            with (
                self.assertRaisesRegex(CORE.LockTimeoutError, "LOCK_TIMEOUT"),
                CORE.locked(timeout=0.1),
            ):
                pass
        finally:
            release.set()
            reader.join(5)
        self.assertEqual(0, reader.exitcode)

    def test_lock_timeout_is_bounded_and_does_not_wait_for_convoy(self) -> None:
        ready = multiprocessing.Event()
        release = multiprocessing.Event()
        process = multiprocessing.Process(
            target=hold_lock,
            args=(str(CORE.LOCK), ready, release),
        )
        process.start()
        self.assertTrue(ready.wait(5))
        started = time.monotonic()
        try:
            with (
                self.assertRaisesRegex(CORE.LockTimeoutError, "LOCK_TIMEOUT"),
                CORE.locked(timeout=0.1),
            ):
                pass
        finally:
            release.set()
            process.join(5)
        self.assertLess(time.monotonic() - started, 1)
        self.assertEqual(0, process.exitcode)

    def test_lock_is_released_after_body_error(self) -> None:
        with self.assertRaisesRegex(RuntimeError, "body failure"), CORE.locked(timeout=0.1):
            raise RuntimeError("body failure")
        with CORE.locked(timeout=0.1):
            pass

    def test_private_lock_trace_records_wait_hold_and_timeout(self) -> None:
        trace = self.root / "lock-trace.jsonl"
        with (
            patch.dict(os.environ, {"HANDOFFCTL_LOCK_TRACE": str(trace)}),
            CORE.locked(phase="fixture_hold"),
            self.assertRaisesRegex(CORE.LockTimeoutError, "LOCK_TIMEOUT"),
            CORE.locked(timeout=0, phase="fixture_wait"),
        ):
            pass
        records = [json.loads(line) for line in trace.read_text().splitlines()]
        self.assertEqual({"fixture_hold", "fixture_wait"}, {item["phase"] for item in records})
        self.assertTrue(
            next(item for item in records if item["phase"] == "fixture_wait")["timeout"]
        )
        self.assertIsInstance(records[0]["ended_ns"], int)
        with patch.dict(os.environ, {"HANDOFFCTL_LOCK_TRACE": str(self.root)}):
            CORE.trace_lock_metric("fixture", "shared", 0, 0)

    def test_lock_yields_capability_and_invalidates_after_scope(self) -> None:
        with CORE.locked(timeout=0.1) as guard:
            self.assertEqual(CORE.coordinator_lock_path().resolve(), guard.path)
            guard.assert_owned()
        with self.assertRaisesRegex(CORE.LockOwnershipError, "inactive"):
            guard.assert_owned()

    def test_lock_guard_constructor_is_not_public(self) -> None:
        with TemporaryDirectory() as directory:
            path = Path(directory) / "state.lock"
            fd = path.open("w+")
            try:
                with self.assertRaises(TypeError):
                    CORE.CoordinatorLockGuard(path, fd.fileno(), exclusive=True)
                with self.assertRaisesRegex(TypeError, "construction is private"):
                    CORE.CoordinatorLockGuard(
                        path, fd.fileno(), exclusive=True, _creation_token=object()
                    )
            finally:
                fd.close()

    def test_lock_guard_rejects_use_from_another_thread(self) -> None:
        errors: list[BaseException] = []
        with CORE.locked(timeout=0.1) as guard:
            thread = threading.Thread(
                target=lambda: self._assert_guard_rejected(guard, errors), daemon=True
            )
            thread.start()
            thread.join(5)
        self.assertEqual(1, len(errors))
        self.assertIsInstance(errors[0], CORE.LockOwnershipError)

    def test_shared_lock_guard_cannot_authorize_exclusive_operation(self) -> None:
        with (
            CORE.locked(exclusive=False, timeout=0.1) as guard,
            self.assertRaisesRegex(CORE.LockOwnershipError, "not exclusive"),
        ):
            guard.assert_owned()

    def test_lock_guard_rejects_replaced_path_inode(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            with (
                patch.object(CORE, "ROOT", root),
                patch.object(CORE, "RUNTIME", root / ".runtime"),
                patch.object(CORE, "LOCK", root / ".runtime" / "state.lock"),
                CORE.locked(timeout=0.1) as guard,
            ):
                guard.path.replace(guard.path.with_name("state.lock.old"))
                guard.path.touch()
                with self.assertRaisesRegex(CORE.LockOwnershipError, "path identity"):
                    guard.assert_owned()

    def test_lock_guard_rejects_descriptor_and_path_failures(self) -> None:
        with CORE.locked(timeout=0.1) as guard:
            with (
                patch.object(CORE.os, "fstat", side_effect=OSError("closed")),
                self.assertRaisesRegex(CORE.LockOwnershipError, "descriptor is unavailable"),
            ):
                guard.assert_owned()
            with (
                patch.object(
                    CORE.os,
                    "fstat",
                    return_value=SimpleNamespace(st_dev=-1, st_ino=-1),
                ),
                self.assertRaisesRegex(CORE.LockOwnershipError, "descriptor identity"),
            ):
                guard.assert_owned()
            with (
                patch.object(
                    CORE, "coordinator_lock_path", return_value=guard.path.parent / "other"
                ),
                self.assertRaisesRegex(CORE.LockOwnershipError, "path changed"),
            ):
                guard.assert_owned()

    @staticmethod
    def _assert_guard_rejected(guard: Any, errors: list[BaseException]) -> None:
        try:
            guard.assert_owned()
        except BaseException as error:
            errors.append(error)

    def test_subprocess_timeout_is_classified(self) -> None:
        with (
            patch.object(
                CORE.subprocess,
                "run",
                side_effect=subprocess.TimeoutExpired(["git", "scan"], 0.1),
            ),
            self.assertRaisesRegex(CORE.SubprocessTimeoutError, "SUBPROCESS_TIMEOUT"),
        ):
            CORE.run(["git", "scan"], timeout=0.1)

    def test_parallel_claims_have_one_linearization_winner(self) -> None:
        self.make_task()
        start = multiprocessing.Event()
        outcomes: Any = multiprocessing.Queue()
        claimants = [
            multiprocessing.Process(
                target=racing_claim,
                args=(str(self.root), start, owner, outcomes),
            )
            for owner in ("worker-a", "worker-b")
        ]
        for process in claimants:
            process.start()
        start.set()
        for process in claimants:
            process.join(10)
            self.assertEqual(0, process.exitcode)

        results = sorted(outcomes.get(timeout=2)[0] for _ in claimants)
        self.assertEqual(["accepted", "rejected"], results)
        meta, _ = CORE.read_task(CORE.locate("AR-0001")[0])
        self.assertEqual("in_progress", meta["status"])
        self.assertIn(meta["owner"], {"worker-a", "worker-b"})
        self.assertEqual(2, meta["task_revision"])
        self.assertEqual(
            CORE.render_status_view(CORE.all_tasks()), (self.root / "STATUS.md").read_text()
        )

    def test_parallel_external_unblocks_have_one_linearization_winner(self) -> None:
        self.make_task(status="blocked")
        start = multiprocessing.Event()
        outcomes: Any = multiprocessing.Queue()
        workers = [
            multiprocessing.Process(target=racing_unblock, args=(str(self.root), start, outcomes))
            for _ in range(2)
        ]
        for process in workers:
            process.start()
        start.set()
        for process in workers:
            process.join(10)
            self.assertEqual(0, process.exitcode)
        self.assertEqual(
            ["accepted", "rejected"], sorted(outcomes.get(timeout=2)[0] for _ in workers)
        )
        meta, _ = CORE.read_task(CORE.locate("AR-0001")[0])
        self.assertEqual(("open", 2), (meta["status"], meta["task_revision"]))
        self.assertEqual([], CORE.storage_backend().load_session_records("AR-0001"))

    def test_parallel_paused_resumes_have_one_linearization_winner(self) -> None:
        target = self.make_task(status="blocked")
        blocked, _ = CORE.read_task(target)
        CORE.append_session_record(
            CORE.ROOT,
            CORE.build_session_record(blocked, "pause", "2026-10-08T00:00:00+00:00"),
        )
        start = multiprocessing.Event()
        outcomes: Any = multiprocessing.Queue()
        workers = [
            multiprocessing.Process(target=racing_resume, args=(str(self.root), start, outcomes))
            for _ in range(2)
        ]
        for process in workers:
            process.start()
        start.set()
        for process in workers:
            process.join(10)
            self.assertEqual(0, process.exitcode)
        self.assertEqual(
            ["accepted", "rejected"], sorted(outcomes.get(timeout=2)[0] for _ in workers)
        )
        final, _ = CORE.read_task(target)
        self.assertEqual(("open", 2), (final["status"], final["task_revision"]))

    def test_concurrent_claim_and_reconcile_keep_status_current(self) -> None:
        self.make_task()
        start = multiprocessing.Event()
        claim = multiprocessing.Process(target=concurrent_claim, args=(str(self.root), start))
        reconcile = multiprocessing.Process(
            target=concurrent_reconcile, args=(str(self.root), start)
        )
        claim.start()
        reconcile.start()
        start.set()
        claim.join(10)
        reconcile.join(10)
        self.assertEqual(0, claim.exitcode)
        self.assertEqual(0, reconcile.exitcode)
        meta, _ = CORE.read_task(CORE.locate("AR-0001")[0])
        self.assertEqual("in_progress", meta["status"])
        self.assertEqual(
            CORE.render_status_view(CORE.all_tasks()), (self.root / "STATUS.md").read_text()
        )

    def test_live_document_generation_and_observation_sync(self) -> None:
        path = self.make_task(worktree_key="agent-systems-benchmark-test")
        state = {
            "remote_main": "a" * 40,
            "origin_main": "a" * 40,
            "primary_head": "b" * 40,
            "worktrees": [
                {
                    "key": "agent-systems-benchmark-test",
                    "branch": "feature/test",
                    "head": "c" * 40,
                    "dirty": 2,
                    "paths": ["one", "two"],
                    "behind": 1,
                    "ahead": 2,
                }
            ],
            "prs": [
                {
                    "number": 1,
                    "title": "Test",
                    "headRefName": "feature/test",
                    "headRefOid": "c" * 40,
                    "baseRefName": "main",
                    "mergeStateStatus": "CLEAN",
                    "statusCheckRollup": [{"status": "COMPLETED", "conclusion": "SUCCESS"}],
                }
            ],
            "runs": [
                {
                    "databaseId": 1,
                    "headSha": "c" * 40,
                    "event": "push",
                    "workflowName": "Verify",
                    "status": "completed",
                    "conclusion": "success",
                }
            ],
        }
        project, worktrees = CORE.live_docs(state)
        self.assertIn("Product remote main", project)
        self.assertIn("#1", project)
        self.assertIn("dirty", worktrees.lower())
        self.assertIn("| changed files | - | - | - | `one`, `two` |", worktrees)
        CORE.sync_task_observations(CORE.all_tasks(), state)
        meta, _ = CORE.read_task(path)
        self.assertEqual(2, meta["observed_dirty"])

    def test_run_config_privacy_and_locate_failures(self) -> None:
        with self.assertRaisesRegex(RuntimeError, "command failed"):
            CORE.run(["false"])
        with self.assertRaisesRegex(RuntimeError, "missing private runtime"):
            CORE.config()
        CORE.CONFIG.parent.mkdir()
        CORE.CONFIG.write_text(
            json.dumps(
                {
                    "projects_root": "root",
                    "product_worktree": "repo",
                    "github_repository": "owner/repo",
                }
            )
        )
        self.assertEqual("repo", CORE.config()["product_worktree"])
        with self.assertRaisesRegex(RuntimeError, "unknown task"):
            CORE.locate("AR-9999")
        binary = self.root / "binary"
        binary.write_bytes(b"\\xff")
        large = self.root / "large.md"
        large.write_text("x" * 200001)
        sample_uuid = project_uuid("3")
        for relative in (Path("tools/handoffctl.py"),):
            fixture = self.root / relative
            fixture.parent.mkdir(exist_ok=True)
            fixture.write_text(sample_uuid)
        (self.root / "notes.md").write_text(sample_uuid)
        CORE.BINDING.write_text(CORE.BINDING.read_text() + "\ntoken=leak\n")
        errors = "\n".join(CORE.privacy_errors())
        self.assertIn("exceeds 200 KiB", errors)
        self.assertIn("notes.md: session-like UUID", errors)
        self.assertNotIn("tools/handoffctl.py: session-like UUID", errors)
        self.assertNotIn("coordinator.binding.json: session-like UUID", errors)
        self.assertIn("coordinator.binding.json: possible credential", errors)

    def test_validation_reports_all_basic_reference_and_claim_errors(self) -> None:
        path = self.make_task("AR-0001")
        meta, body = CORE.read_task(path)
        meta.update(
            {
                "id": "bad",
                "status": "wrong",
                "priority": "PX",
                "task_revision": 0,
                "title": "",
                "summary": "",
                "next_action": "",
                "updated_at": "bad",
                "checkpoint_commit": "no",
                "plan": "../plans/AR-0001.md",
                "owner": "orphan",
                "claim_expires": "later",
            }
        )
        CORE.write_task(path, meta, body)
        errors = "\n".join(CORE.validate())
        for phrase in (
            "invalid id",
            "invalid status",
            "invalid priority",
            "invalid revision",
            "invalid title",
            "invalid summary",
            "invalid next_action",
            "invalid updated_at",
            "invalid checkpoint",
            "missing plan",
            "inactive task retains claim",
        ):
            self.assertIn(phrase, errors)

    def test_claim_expiry_is_timezone_aware_and_live(self) -> None:
        path = self.make_task(
            status="in_progress",
            owner="worker-a",
            claim_expires="2000-01-01T00:00:00+00:00",
        )
        self.assertIn("expired claim", "\n".join(CORE.validate()))
        meta, body = CORE.read_task(path)
        meta["claim_expires"] = "2099-01-01T00:00:00"
        CORE.write_task(path, meta, body)
        CORE.atomic(self.root / "CURRENT.md", CORE.render_current(CORE.all_tasks()))
        self.assertIn("invalid claim expiry", "\n".join(CORE.validate()))
        meta["claim_expires"] = 123
        CORE.write_task(path, meta, body)
        CORE.atomic(self.root / "CURRENT.md", CORE.render_current(CORE.all_tasks()))
        self.assertIn("invalid claim expiry", "\n".join(CORE.validate()))

    def test_push_replica_disabled_without_private_config(self) -> None:
        with patch.object(CORE, "run") as run_mock:
            CORE.push_replica()
            run_mock.assert_not_called()

    def test_claim_owner_collision_heartbeat_and_release_failures(self) -> None:
        first = self.make_task("AR-0001")
        self.make_task("AR-0002")
        with patch.object(CORE, "commit", return_value=True):
            CORE.mutate(
                argparse.Namespace(task="AR-0001", owner="worker-a", lease_minutes=10), "claim"
            )
            with self.assertRaisesRegex(RuntimeError, "already holds"):
                CORE.mutate(
                    argparse.Namespace(task="AR-0002", owner="worker-a", lease_minutes=10), "claim"
                )
            with self.assertRaisesRegex(RuntimeError, "owned by"):
                CORE.mutate(
                    argparse.Namespace(task="AR-0001", owner="worker-b", lease_minutes=10),
                    "heartbeat",
                )
            with self.assertRaisesRegex(RuntimeError, "positive lease"):
                CORE.mutate(
                    argparse.Namespace(task="AR-0001", owner="worker-a", lease_minutes=0),
                    "heartbeat",
                )
            CORE.mutate(
                argparse.Namespace(task="AR-0001", owner="worker-a", lease_minutes=20),
                "heartbeat",
            )
            revision = CORE.read_task(first)[0]["task_revision"]
            with self.assertRaisesRegex(RuntimeError, "use release"):
                CORE.mutate(
                    argparse.Namespace(
                        task="AR-0001",
                        owner="worker-a",
                        expected_revision=revision,
                        status="done",
                        priority=None,
                        summary=None,
                        next_action=None,
                        note="bad",
                    ),
                    "update",
                )

    def fake_scan(self) -> dict[str, object]:
        return {
            "remote_main": "a" * 40,
            "origin_main": "a" * 40,
            "primary_head": "b" * 40,
            "worktrees": [],
            "prs": [],
            "runs": [],
        }

    def test_project_scan_covers_dirty_and_detached_worktrees(self) -> None:  # noqa: C901
        product = self.root / "agent-systems-benchmark"
        second = self.root / "agent-systems-benchmark-two"
        state_task = self.root / "state-task"
        product.mkdir()
        second.mkdir()
        state_task.mkdir()
        CORE.CONFIG.parent.mkdir()
        CORE.CONFIG.write_text(
            json.dumps(
                {
                    "projects_root": str(self.root),
                    "product_worktree": product.name,
                    "github_repository": "owner/repo",
                }
            )
        )

        calls: list[list[str]] = []

        def fake_run(args: list[str], **_: object) -> object:  # noqa: C901
            calls.append(args)
            joined = " ".join(args)
            stdout = ""
            returncode = 0
            if "worktree list" in joined:
                checkout = args[args.index("-C") + 1]
                if checkout == str(CORE.ROOT):
                    stdout = f"worktree {CORE.ROOT}\n\nworktree {state_task}\n"
                else:
                    stdout = (
                        f"worktree {product}\nHEAD {'b' * 40}\nbranch refs/heads/main\n\n"
                        f"worktree {second}\nHEAD {'c' * 40}\ndetached\n"
                    )
            elif "symbolic-ref" in joined and str(second) in joined:
                returncode = 1
            elif "symbolic-ref" in joined:
                stdout = "main\n"
            elif "status --porcelain" in joined and str(product) in joined:
                stdout = " M file\n"
            elif "rev-list" in joined and str(product) in joined:
                stdout = "1 2\n"
            elif "rev-list" in joined:
                returncode = 1
            elif "ls-remote" in joined:
                stdout = ("a" * 40) + "\trefs/heads/main\n"
            elif "rev-parse origin/main" in joined:
                stdout = ("a" * 40) + "\n"
            elif "rev-parse HEAD" in joined and str(product) in joined:
                stdout = ("b" * 40) + "\n"
            elif "rev-parse HEAD" in joined:
                stdout = ("c" * 40) + "\n"
            elif args[:3] == ["gh", "pr", "list"] or args[:3] == ["gh", "run", "list"]:
                stdout = "[]"
            return subprocess.CompletedProcess(args, returncode, stdout=stdout, stderr="")

        with patch.object(CORE, "run", side_effect=fake_run):
            state = CORE.project_scan()
        self.assertEqual("a" * 40, state["remote_main"])
        self.assertEqual(2, len(state["worktrees"]))
        self.assertEqual(1, state["worktrees"][0]["dirty"])
        self.assertEqual("DETACHED", state["worktrees"][1]["branch"])
        self.assertFalse(any("symbolic-ref" in args for args in calls))
        self.assertFalse(any("rev-parse" in args and str(second) in args for args in calls))

    def test_project_scan_excludes_all_coordinator_worktrees(self) -> None:
        product = self.root / "product"
        state_task = self.root / "state-task"
        product.mkdir()
        state_task.mkdir()
        CORE.CONFIG.parent.mkdir()
        CORE.CONFIG.write_text(
            json.dumps(
                {
                    "projects_root": str(self.root),
                    "product_worktree": product.name,
                    "github_repository": "owner/repo",
                }
            )
        )

        def fake_run(args: list[str], **_: object) -> object:
            joined = " ".join(args)
            if "worktree list" in joined:
                checkout = args[args.index("-C") + 1]
                if checkout == str(CORE.ROOT):
                    stdout = f"worktree {CORE.ROOT}\n\nworktree {state_task}\n"
                else:
                    stdout = f"worktree {product}\n"
                return subprocess.CompletedProcess(args, 0, stdout=stdout, stderr="")
            if args[:3] in (["gh", "pr", "list"], ["gh", "run", "list"]):
                return subprocess.CompletedProcess(args, 0, stdout="[]", stderr="")
            if "ls-remote" in joined:
                return subprocess.CompletedProcess(args, 0, stdout=("a" * 40) + "\n", stderr="")
            if "symbolic-ref" in joined:
                return subprocess.CompletedProcess(args, 0, stdout="main\n", stderr="")
            if "status --porcelain" in joined:
                return subprocess.CompletedProcess(args, 0, stdout="", stderr="")
            if "rev-list" in joined:
                return subprocess.CompletedProcess(args, 0, stdout="0 0\n", stderr="")
            return subprocess.CompletedProcess(args, 0, stdout=("b" * 40) + "\n", stderr="")

        with patch.object(CORE, "run", side_effect=fake_run):
            state = CORE.project_scan()
        self.assertEqual(
            {product.name},
            {item["key"] for item in state["worktrees"]},
        )

    def test_changed_paths_preserves_existing_and_deleted_semantics(self) -> None:
        changed = self.root / "changed.md"
        changed.write_text("after")
        deleted = self.root / "deleted.md"
        unchanged = self.root / "unchanged.md"
        unchanged.write_text("same")
        before = {changed: "before", deleted: "before", unchanged: "same"}
        self.assertEqual([changed], CORE.changed_paths(before))
        self.assertEqual([changed, deleted], CORE.changed_paths(before, include_deleted=True))

    def test_reconcile_and_live_staleness(self) -> None:
        self.make_task()
        with (
            patch.object(CORE, "project_scan", return_value=self.fake_scan()),
            patch.object(CORE, "commit", return_value=True) as commit,
        ):
            self.assertTrue(CORE.reconcile(do_commit=True))
            commit.assert_called_once()
            self.assertEqual([], CORE.validate(live=True))
            (self.root / "PROJECT_STATE.md").write_text("stale")
            errors = CORE.validate(live=True)
            self.assertIn("PROJECT_STATE.md is stale", errors)

    def test_git_reconcile_observes_product_without_authority_lock(self) -> None:
        self.make_task()
        observed = False

        def scan_without_lock() -> Any:
            nonlocal observed
            # A second descriptor must be able to acquire the same lock while
            # the slow external observation phase is in progress.
            with CORE.locked(timeout=0):
                observed = True
            return self.fake_scan()

        with patch.object(CORE, "project_scan", side_effect=scan_without_lock):
            self.assertTrue(CORE.reconcile(do_commit=False))
        self.assertTrue(observed)

    def test_git_snapshot_observes_product_without_shared_lock(self) -> None:
        self.make_task()

        def scan_without_lock() -> Any:
            with CORE.locked(timeout=0):
                pass
            return self.fake_scan()

        with patch.object(CORE, "project_scan", side_effect=scan_without_lock):
            CORE.reconcile(do_commit=False)
            with patch.object(CORE, "run", return_value=SimpleNamespace(stdout="state\n")):
                CORE.cmd_snapshot()

    def test_git_doctor_scans_unlocked_but_validates_under_shared_lock(self) -> None:
        self.make_task()
        with patch.object(CORE, "project_scan", return_value=self.fake_scan()):
            CORE.reconcile(do_commit=False)
        actual_validate = CORE.validate

        def unlocked_scan() -> Any:
            with CORE.locked(timeout=0):
                pass
            return self.fake_scan()

        def locked_validation(*, live: bool, live_state: Any) -> list[str]:
            with (
                self.assertRaises(CORE.LockTimeoutError),
                CORE.locked(timeout=0),
            ):
                pass
            return cast(list[str], actual_validate(live=live, live_state=live_state))

        with (
            patch.object(CORE, "project_scan", side_effect=unlocked_scan),
            patch.object(CORE, "validate", side_effect=locked_validation),
        ):
            self.assertEqual(0, CORE.cmd_doctor(live=True))

    def test_git_doctor_accepts_equivalent_publication_during_scan(self) -> None:
        self.make_task()
        with patch.object(CORE, "project_scan", return_value=self.fake_scan()):
            CORE.reconcile(do_commit=False)
        scans = 0

        def interleaved_scan() -> Any:
            nonlocal scans
            scans += 1
            if scans == 1:
                with patch.object(CORE, "project_scan", return_value=self.fake_scan()):
                    CORE.reconcile(do_commit=False)
            return self.fake_scan()

        with patch.object(CORE, "project_scan", side_effect=interleaved_scan):
            self.assertEqual(0, CORE.cmd_doctor(live=True))
        self.assertEqual(1, scans)

    def test_git_doctor_retries_changed_publication_during_scan(self) -> None:
        self.make_task()
        older = self.fake_scan()
        newer = self.fake_scan()
        newer["remote_main"] = "c" * 40
        with patch.object(CORE, "project_scan", return_value=older):
            CORE.reconcile(do_commit=False)
        scans = 0

        def interleaved_scan() -> Any:
            nonlocal scans
            scans += 1
            if scans == 1:
                with patch.object(CORE, "project_scan", return_value=newer):
                    CORE.reconcile(do_commit=False)
                return older
            return newer

        with patch.object(CORE, "project_scan", side_effect=interleaved_scan):
            self.assertEqual(0, CORE.cmd_doctor(live=True))
        self.assertEqual(2, scans)

    def test_git_doctor_fails_boundedly_if_every_scan_is_overtaken(self) -> None:
        self.make_task()
        with patch.object(CORE, "project_scan", return_value=self.fake_scan()):
            CORE.reconcile(do_commit=False)
        scans = 0

        def overtaken_scan() -> Any:
            nonlocal scans
            scans += 1
            newer = self.fake_scan()
            newer["remote_main"] = "c" * 40
            with patch.object(CORE, "project_scan", return_value=newer):
                CORE.reconcile(do_commit=False)
            return self.fake_scan()

        with (
            patch.object(CORE, "project_scan", side_effect=overtaken_scan),
            patch("builtins.print") as printed,
        ):
            self.assertEqual(1, CORE.cmd_doctor(live=True))
        self.assertEqual(3, scans)
        printed.assert_called_once_with("ERROR: OBSERVATION_CHANGED: retry doctor")

    def test_git_doctor_does_not_hide_structural_error_behind_overtaken_scan(self) -> None:
        self.make_task()
        with patch.object(CORE, "project_scan", return_value=self.fake_scan()):
            CORE.reconcile(do_commit=False)
        scans = 0

        def overtaken_scan() -> Any:
            nonlocal scans
            scans += 1
            with patch.object(CORE, "project_scan", return_value=self.fake_scan()):
                CORE.reconcile(do_commit=False)
            return self.fake_scan()

        with (
            patch.object(CORE, "project_scan", side_effect=overtaken_scan),
            patch.object(
                CORE,
                "doctor_checks",
                return_value=["PROJECT_STATE.md is stale", "structural error"],
            ),
            patch("builtins.print") as printed,
        ):
            self.assertEqual(1, CORE.cmd_doctor(live=True))
        self.assertEqual(1, scans)
        printed.assert_called_once_with("ERROR: PROJECT_STATE.md is stale\nERROR: structural error")

    def test_git_doctor_rejects_changed_binding_after_scan(self) -> None:
        self.make_task()

        def changed_binding_scan() -> Any:
            binding = json.loads(CORE.BINDING.read_text())
            binding["product_repository"] = "owner/other"
            CORE.BINDING.write_text(json.dumps(binding))
            return self.fake_scan()

        with (
            patch.object(CORE, "project_scan", side_effect=changed_binding_scan),
            self.assertRaisesRegex(RuntimeError, "OBSERVATION_INPUT_CHANGED"),
        ):
            CORE.cmd_doctor(live=True)

    def test_git_reconcile_does_not_publish_an_overtaken_scan(self) -> None:
        self.make_task(worktree_key="worker-one")
        older = self.fake_scan()
        newer = self.fake_scan()
        for state, head in ((older, "a" * 40), (newer, "b" * 40)):
            state["worktrees"] = [
                {
                    "key": "worker-one",
                    "branch": "feature/one",
                    "head": head,
                    "dirty": 0,
                    "paths": [],
                    "behind": 0,
                    "ahead": 1,
                }
            ]
        scans = 0

        def out_of_order_scan() -> Any:
            nonlocal scans
            scans += 1
            if scans == 1:
                self.assertTrue(CORE.reconcile(do_commit=False))
                return older
            return newer

        with patch.object(CORE, "project_scan", side_effect=out_of_order_scan):
            self.assertTrue(CORE.reconcile(do_commit=False))
        self.assertEqual(3, scans)
        self.assertEqual("b" * 40, CORE.locate("AR-0001")[1]["observed_head"])
        self.assertEqual(CORE.live_docs(newer)[1], (self.root / "WORKTREES.md").read_text())
        self.assertEqual("3\n", CORE.observation_marker("observation-published").read_text())

    def test_overtaken_commit_and_push_honor_durability_request(self) -> None:
        task_path = self.make_task()
        scans = 0

        def publish_newer_plain_reconcile() -> Any:
            nonlocal scans
            scans += 1
            if scans == 1:
                self.assertTrue(CORE.reconcile(do_commit=False))
                task_path.write_text(task_path.read_text() + "\nUnrelated draft note.\n")
            return self.fake_scan()

        with (
            patch.object(CORE, "project_scan", side_effect=publish_newer_plain_reconcile),
            patch.object(CORE, "commit", return_value=True) as commit,
            patch.object(CORE, "push_replica") as push,
        ):
            self.assertTrue(CORE.reconcile(do_commit=True, push=True))
        commit.assert_called_once()
        self.assertNotIn(task_path, commit.call_args.args[1])
        push.assert_called_once()
        self.assertEqual("3\n", CORE.observation_marker("observation-published").read_text())

    def test_commit_collects_pending_paths_from_earlier_plain_reconcile(self) -> None:
        self.make_task()
        with patch.object(CORE, "project_scan", return_value=self.fake_scan()):
            CORE.reconcile(do_commit=False)
            pending = json.loads((CORE.RUNTIME / "last-reconcile.json").read_text())[
                "pending_paths"
            ]
            self.assertTrue(pending)
            with patch.object(CORE, "commit", return_value=True) as commit:
                self.assertTrue(CORE.reconcile(do_commit=True))
        self.assertTrue(
            {CORE.ROOT / value for value in pending}.issubset(set(commit.call_args.args[1]))
        )
        self.assertEqual(
            [], json.loads((CORE.RUNTIME / "last-reconcile.json").read_text())["pending_paths"]
        )

    def test_pending_task_content_change_refuses_later_commit(self) -> None:
        task_path = self.make_task(worktree_key="worker-one")
        state = self.fake_scan()
        state["worktrees"] = [
            {
                "key": "worker-one",
                "branch": "feature/one",
                "head": "b" * 40,
                "dirty": 0,
                "paths": [],
                "behind": 0,
                "ahead": 1,
            }
        ]
        with patch.object(CORE, "project_scan", return_value=state):
            CORE.reconcile(do_commit=False)
            task_path.write_text(task_path.read_text() + "\nUnrelated draft note.\n")
            with self.assertRaisesRegex(RuntimeError, "PENDING_OBSERVATION_CHANGED"):
                CORE.reconcile(do_commit=True)

    def test_committed_task_transition_clears_stale_pending_hash(self) -> None:
        task_path = self.make_task(worktree_key="worker-one")
        CORE.run(["git", "init", "-b", "main", str(self.root)])
        for key, value in (
            ("user.name", "Fixture"),
            ("user.email", "fixture@example.invalid"),
            ("commit.gpgsign", "false"),
        ):
            CORE.run(["git", "-C", str(self.root), "config", key, value])
        CORE.run(["git", "-C", str(self.root), "add", "--all"])
        CORE.run(["git", "-C", str(self.root), "commit", "-m", "fixture baseline"])
        state = self.fake_scan()
        state["worktrees"] = [
            {
                "key": "worker-one",
                "branch": "feature/one",
                "head": "b" * 40,
                "dirty": 0,
                "paths": [],
                "behind": 0,
                "ahead": 1,
            }
        ]
        with patch.object(CORE, "project_scan", return_value=state):
            self.assertTrue(CORE.reconcile(do_commit=False))
            self.assertIn(
                str(task_path.relative_to(self.root)),
                json.loads((CORE.RUNTIME / "last-reconcile.json").read_text())["pending_paths"],
            )
            meta, body = CORE.read_task(task_path)
            meta["status"] = "in_progress"
            meta["owner"] = "worker-one"
            meta["claim_expires"] = "2030-01-01T00:00:00+00:00"
            meta["task_revision"] = 2
            CORE.write_task(task_path, meta, body)
            self.refresh_views()
            CORE.run(["git", "-C", str(self.root), "add", "--all"])
            CORE.run(["git", "-C", str(self.root), "commit", "-m", "fixture claim"])
            self.assertTrue(CORE.reconcile(do_commit=False))

    def test_observation_tickets_are_checkout_local(self) -> None:
        first = CORE.reserve_observation_ticket()
        other_runtime = self.root / "other-checkout" / ".runtime"
        with patch.object(CORE, "RUNTIME", other_runtime):
            self.assertEqual(1, CORE.reserve_observation_ticket())
            self.assertEqual(0, CORE.published_observation_ticket())
        self.assertEqual(1, first)
        self.assertEqual(2, CORE.reserve_observation_ticket())

    def test_failed_push_keeps_locally_published_observation_ticket(self) -> None:
        self.make_task()
        with (
            patch.object(CORE, "project_scan", return_value=self.fake_scan()),
            patch.object(CORE, "commit", return_value=True),
            patch.object(CORE, "push_replica", side_effect=OSError("push failed")),
            self.assertRaisesRegex(OSError, "push failed"),
        ):
            CORE.reconcile(do_commit=True, push=True)
        self.assertEqual("1\n", CORE.observation_marker("observation-published").read_text())

    def test_failed_publication_marker_recovers_on_later_scan(self) -> None:
        self.make_task()
        real_atomic = CORE.atomic

        def fail_marker(path: Path, value: str) -> None:
            if path.name == "last-reconcile.json":
                raise OSError("marker write failed")
            real_atomic(path, value)

        with (
            patch.object(CORE, "project_scan", return_value=self.fake_scan()),
            patch.object(CORE, "commit", return_value=True),
            patch.object(CORE, "atomic", side_effect=fail_marker),
            self.assertRaisesRegex(OSError, "marker write failed"),
        ):
            CORE.reconcile(do_commit=True)
        self.assertEqual("1\n", CORE.observation_marker("observation-published").read_text())
        with patch.object(CORE, "project_scan", return_value=self.fake_scan()):
            self.assertTrue(CORE.reconcile(do_commit=False))
        self.assertEqual("2\n", CORE.observation_marker("observation-published").read_text())

    def test_snapshot_retries_when_reconcile_publishes_during_scan(self) -> None:
        self.make_task()
        with patch.object(CORE, "project_scan", return_value=self.fake_scan()):
            CORE.reconcile(do_commit=False)
        scans = 0

        def scan_with_interleaved_publication() -> Any:
            nonlocal scans
            scans += 1
            if scans == 1:
                with patch.object(CORE, "project_scan", return_value=self.fake_scan()):
                    CORE.reconcile(do_commit=False)
            return self.fake_scan()

        with (
            patch.object(CORE, "project_scan", side_effect=scan_with_interleaved_publication),
            patch.object(CORE, "run", return_value=SimpleNamespace(stdout="state\n")),
        ):
            CORE.cmd_snapshot()
        self.assertEqual(2, scans)

    def test_observation_tickets_are_unique_across_workers(self) -> None:
        start = multiprocessing.Event()
        outcomes: Any = multiprocessing.Queue()
        processes = [
            multiprocessing.Process(
                target=concurrent_observation_ticket,
                args=(str(self.root), start, outcomes),
            )
            for _ in range(8)
        ]
        for process in processes:
            process.start()
        start.set()
        values = [outcomes.get(timeout=5) for _ in processes]
        for process in processes:
            process.join(5)
            self.assertEqual(0, process.exitcode)
        self.assertEqual(list(range(1, 9)), sorted(values))

    def test_git_reconcile_rejects_changed_scan_binding(self) -> None:
        self.make_task()

        def change_binding() -> Any:
            binding = json.loads(CORE.BINDING.read_text())
            binding["product_repository"] = "owner/other"
            CORE.BINDING.write_text(json.dumps(binding))
            return self.fake_scan()

        with (
            patch.object(CORE, "project_scan", side_effect=change_binding),
            self.assertRaisesRegex(RuntimeError, "OBSERVATION_INPUT_CHANGED"),
        ):
            CORE.reconcile(do_commit=False)
        self.assertFalse((self.root / "PROJECT_STATE.md").exists())

    def test_generated_view_validation_reports_stale_and_renderer_errors(self) -> None:
        self.make_task()
        (self.root / "CURRENT.md").write_text("stale")
        (self.root / "STATUS.md").unlink()
        errors = CORE.generated_view_errors(CORE.all_tasks())
        self.assertIn("CURRENT.md differs from generated tasks", errors)
        self.assertIn("STATUS.md differs from generated tasks", errors)
        with patch.object(
            CORE,
            "render_status_view",
            side_effect=CORE.StatusRenderError("hostile graph"),
        ):
            self.assertIn("hostile graph", CORE.generated_view_errors(CORE.all_tasks()))
        path = CORE.locate("AR-0001")[0]
        meta, body = CORE.read_task(path)
        meta["status"] = "invalid"
        CORE.write_task(path, meta, body)
        self.assertEqual([], CORE.generated_view_errors(CORE.all_tasks()))

    def test_reconcile_generation_failure_rolls_back_every_view(self) -> None:
        path = self.make_task(worktree_key="agent-systems-benchmark-test")
        before_task = path.read_text()
        before_current = (self.root / "CURRENT.md").read_text()
        before_status = (self.root / "STATUS.md").read_text()
        state = self.fake_scan()
        state["worktrees"] = [
            {
                "key": "agent-systems-benchmark-test",
                "branch": "feature/test",
                "head": "c" * 40,
                "dirty": 1,
                "paths": ["changed"],
                "behind": 0,
                "ahead": 1,
            }
        ]
        real_atomic = CORE.atomic
        failed = False

        def fail_status_once(target: Path, text: str) -> None:
            nonlocal failed
            if target.name == "STATUS.md" and not failed:
                failed = True
                raise OSError("injected status write failure")
            real_atomic(target, text)

        with (
            patch.object(CORE, "project_scan", return_value=state),
            patch.object(CORE, "atomic", side_effect=fail_status_once),
            self.assertRaisesRegex(OSError, "injected status write failure"),
        ):
            CORE.reconcile(do_commit=False)
        self.assertEqual(before_task, path.read_text())
        self.assertEqual(before_current, (self.root / "CURRENT.md").read_text())
        self.assertEqual(before_status, (self.root / "STATUS.md").read_text())
        self.assertFalse((self.root / "PROJECT_STATE.md").exists())
        self.assertFalse((self.root / "WORKTREES.md").exists())

    def test_reconcile_commit_failure_rolls_back_and_push_failure_preserves(self) -> None:
        path = self.make_task(worktree_key="agent-systems-benchmark-test")
        before = {
            item: item.read_text()
            for item in (path, self.root / "CURRENT.md", self.root / "STATUS.md")
        }
        with (
            patch.object(CORE, "project_scan", return_value=self.fake_scan()),
            patch.object(CORE, "commit", side_effect=RuntimeError("commit failed")),
            self.assertRaisesRegex(RuntimeError, "commit failed"),
        ):
            CORE.reconcile(do_commit=True)
        self.assertTrue(all(item.read_text() == text for item, text in before.items()))
        with (
            patch.object(CORE, "project_scan", return_value=self.fake_scan()),
            patch.object(CORE, "commit", return_value=True),
            patch.object(CORE, "push_replica", side_effect=RuntimeError("push failed")),
            self.assertRaisesRegex(RuntimeError, "push failed"),
        ):
            CORE.reconcile(do_commit=True, push=True)
        self.assertEqual(
            CORE.render_status_view(CORE.all_tasks()), (self.root / "STATUS.md").read_text()
        )

    def test_mutation_render_and_commit_failures_restore_three_files(self) -> None:
        path = self.make_task()
        before = {
            item: item.read_text()
            for item in (path, self.root / "CURRENT.md", self.root / "STATUS.md")
        }
        args = argparse.Namespace(task="AR-0001", owner="worker-a", lease_minutes=10)
        with (
            patch.object(CORE, "render_status_view", side_effect=RuntimeError("render failed")),
            self.assertRaisesRegex(RuntimeError, "render failed"),
        ):
            CORE.mutate(args, "claim")
        self.assertTrue(all(item.read_text() == text for item, text in before.items()))
        (self.root / "STATUS.md").unlink()
        with (
            patch.object(CORE, "render_status_view", side_effect=RuntimeError("render failed")),
            self.assertRaisesRegex(RuntimeError, "render failed"),
        ):
            CORE.mutate(args, "claim")
        self.assertFalse((self.root / "STATUS.md").exists())
        CORE.atomic(self.root / "STATUS.md", before[self.root / "STATUS.md"])
        with (
            patch.object(CORE, "commit", side_effect=RuntimeError("commit failed")),
            self.assertRaisesRegex(RuntimeError, "commit failed"),
        ):
            CORE.mutate(args, "claim")
        self.assertTrue(all(item.read_text() == text for item, text in before.items()))

    def test_commit_no_change_and_change_paths(self) -> None:
        target = self.root / "CURRENT.md"
        target.write_text("x")
        calls = []

        self.assertFalse(CORE.commit("empty", []))

        def fake_run(args: list[str], **_: object) -> object:
            calls.append(args)
            return subprocess.CompletedProcess(args, 0, stdout="", stderr="")

        with patch.object(CORE, "run", side_effect=fake_run):
            self.assertFalse(CORE.commit("test", [target]))
        self.assertFalse(any("commit" in args for args in calls))

        def changed_run(args: list[str], **_: object) -> object:
            calls.append(args)
            code = 1 if "diff" in args else 0
            return subprocess.CompletedProcess(args, code, stdout="", stderr="")

        with patch.object(CORE, "run", side_effect=changed_run):
            self.assertTrue(CORE.commit("test", [target]))
        commit_call = next(args for args in calls if "commit" in args)
        self.assertIn("-S", commit_call)
        self.assertIn("-s", commit_call)

        self.assertIn("--only", commit_call)
        self.assertEqual(str(target.relative_to(self.root)), commit_call[-1])
        self.assertTrue(any("diff" in args and args[-1] == "CURRENT.md" for args in calls))

        def failing_run(args: list[str], **_: object) -> object:
            calls.append(args)
            if "diff" in args:
                return subprocess.CompletedProcess(args, 1, stdout="", stderr="")
            if "commit" in args:
                raise RuntimeError("signing failed")
            return subprocess.CompletedProcess(args, 0, stdout="", stderr="")

        with (
            patch.object(CORE, "run", side_effect=failing_run),
            self.assertRaisesRegex(RuntimeError, "signing failed"),
        ):
            CORE.commit("test", [target])
        self.assertTrue(any("reset" in args for args in calls))

    def test_push_replica_fast_forward_noop_and_divergence(self) -> None:
        CORE.CONFIG.parent.mkdir()
        CORE.CONFIG.write_text('{"push_enabled": true}')
        local = "a" * 40
        remote = "b" * 40
        calls: list[list[str]] = []

        def fake_run(args: list[str], **_: object) -> object:
            calls.append(args)
            joined = " ".join(args)
            stdout = ""
            returncode = 0
            if "remote get-url" in joined:
                stdout = "git@example.invalid:owner/state.git\n"
            elif "symbolic-ref" in joined:
                stdout = "main\n"
            elif "rev-parse HEAD" in joined:
                stdout = local + "\n"
            elif "rev-parse FETCH_HEAD" in joined:
                stdout = remote + "\n"
            return subprocess.CompletedProcess(args, returncode, stdout=stdout, stderr="")

        with patch.object(CORE, "run", side_effect=fake_run):
            CORE.push_replica()
        self.assertTrue(any("push" in args for args in calls))

        calls.clear()
        local = remote
        with patch.object(CORE, "run", side_effect=fake_run):
            CORE.push_replica()
        self.assertFalse(any("push" in args for args in calls))

        local = "c" * 40

        def divergent_run(args: list[str], **kwargs: object) -> object:
            result = fake_run(args, **kwargs)
            if "merge-base" in args:
                return subprocess.CompletedProcess(args, 1, stdout="", stderr="")
            return result

        with (
            patch.object(CORE, "run", side_effect=divergent_run),
            self.assertRaisesRegex(RuntimeError, "REPLICA_DIVERGED"),
        ):
            CORE.push_replica()

    def test_push_replica_requires_origin_when_enabled(self) -> None:
        CORE.CONFIG.parent.mkdir()
        CORE.CONFIG.write_text('{"push_enabled": true}')
        failed = subprocess.CompletedProcess(["git"], 2, stdout="", stderr="")
        with (
            patch.object(CORE, "run", return_value=failed),
            self.assertRaisesRegex(RuntimeError, "origin is missing"),
        ):
            CORE.push_replica()

    def test_snapshot_and_run_command_paths(self) -> None:
        self.make_task(
            status="in_progress",
            owner="worker-a",
            claim_expires=(
                (dt.datetime.now(dt.UTC) + dt.timedelta(minutes=5))
                .replace(microsecond=0)
                .isoformat()
            ),
        )
        CORE.atomic(self.root / "PROJECT_STATE.md", CORE.live_docs(self.fake_scan())[0])
        CORE.atomic(self.root / "WORKTREES.md", CORE.live_docs(self.fake_scan())[1])
        completed = subprocess.CompletedProcess(["true"], 0, stdout="", stderr="")
        with (
            patch.object(CORE, "project_scan", return_value=self.fake_scan()),
            patch.object(CORE, "run", return_value=completed),
            patch("builtins.print"),
        ):
            CORE.cmd_snapshot()
        args = argparse.Namespace(task="AR-0001", owner="worker-a", command=["true"])
        CORE.CONFIG.write_text("{}")
        with (
            patch.object(CORE.subprocess, "run", return_value=completed) as subprocess_run,
            patch.object(CORE, "reconcile"),
            patch.object(CORE, "mutate") as mutate,
        ):
            self.assertEqual(0, CORE.cmd_run(args))
            self.assertIn("command argv SHA-256", mutate.call_args.args[0].note)
            self.assertIsNone(mutate.call_args.args[0].expected_revision)
            subprocess_run.assert_called_once_with(
                ["true"], check=False, stdin=subprocess.DEVNULL, timeout=1800.0
            )
        timeout_args = argparse.Namespace(
            task="AR-0001",
            owner="worker-a",
            command=["slow"],
            timeout_seconds=0.1,
        )
        with (
            patch.object(
                CORE.subprocess,
                "run",
                side_effect=subprocess.TimeoutExpired(["slow"], 0.1),
            ),
            patch.object(CORE, "reconcile"),
            patch.object(CORE, "mutate") as mutate,
        ):
            self.assertEqual(124, CORE.cmd_run(timeout_args))
            self.assertIn("classification=SUBPROCESS_TIMEOUT", mutate.call_args.args[0].note)
        with (
            patch.object(CORE.subprocess, "run", return_value=completed),
            patch.object(
                CORE,
                "reconcile",
                side_effect=CORE.SubprocessTimeoutError("SUBPROCESS_TIMEOUT after 0.1s"),
            ),
            patch.object(CORE, "mutate") as mutate,
        ):
            with self.assertRaisesRegex(
                CORE.PostCommandReconcileError,
                "COMMAND_RECORDED_POST_RECONCILE_FAILED",
            ):
                CORE.cmd_run(args)
            self.assertIn("command argv SHA-256", mutate.call_args.args[0].note)
        with (
            patch.object(CORE.subprocess, "run") as command,
            self.assertRaisesRegex(RuntimeError, "timeout must be positive"),
        ):
            CORE.cmd_run(
                argparse.Namespace(
                    task="AR-0001",
                    owner="worker-a",
                    command=["true"],
                    timeout_seconds=0,
                )
            )
        command.assert_not_called()
        with self.assertRaisesRegex(RuntimeError, "claim"):
            CORE.cmd_run(argparse.Namespace(task="AR-0001", owner="wrong", command=["true"]))
        with self.assertRaisesRegex(RuntimeError, "missing command"):
            CORE.cmd_run(argparse.Namespace(task="AR-0001", owner="worker-a", command=[]))
        path = CORE.locate("AR-0001")[0]
        meta, body = CORE.read_task(path)
        meta["claim_expires"] = "2000-01-01T00:00:00+00:00"
        CORE.write_task(path, meta, body)
        with (
            patch.object(CORE.subprocess, "run") as command,
            self.assertRaisesRegex(RuntimeError, "expired claim"),
        ):
            CORE.cmd_run(argparse.Namespace(task="AR-0001", owner="worker-a", command=["true"]))
        command.assert_not_called()

    def test_run_a_b_a_policy_swap_has_no_command_or_journal_effect(self) -> None:
        self.enable_additive_policy()
        self.make_task(
            status="in_progress",
            owner="worker-a",
            claim_expires="2099-01-01T00:00:00+00:00",
        )
        CORE.CONFIG.parent.mkdir(exist_ok=True)
        CORE.CONFIG.write_text("{}")
        policy_path = self.root / "task-spec-policy.json"
        original_payload = policy_path.read_bytes()
        original_check = CORE.require_policy_unchanged
        checks = 0

        def a_b_a_check(root: Path, expected: Any) -> None:
            nonlocal checks
            checks += 1
            if checks == 1:
                original_check(root, expected)
                return
            saved = self.root / "task-spec-policy.saved"
            policy_path.replace(saved)
            policy_path.write_bytes(original_payload.replace(b'"hosted"', b'"remote"', 1))
            try:
                original_check(root, expected)
            finally:
                policy_path.unlink()
                saved.replace(policy_path)

        real_subprocess_run = CORE.subprocess.run
        commands: list[object] = []

        def observe_run(command: object, *args: object, **kwargs: object) -> object:
            commands.append(command)
            return real_subprocess_run(command, *args, **kwargs)

        with (
            patch.object(CORE, "assert_invocation_worktree"),
            patch.object(CORE, "require_policy_unchanged", side_effect=a_b_a_check),
            patch.object(CORE.subprocess, "run", side_effect=observe_run),
            self.assertRaisesRegex(RuntimeError, "changed during operation"),
        ):
            CORE.cmd_run(argparse.Namespace(task="AR-0001", owner="worker-a", command=["true"]))
        self.assertNotIn(["true"], commands)
        self.assertEqual(original_payload, policy_path.read_bytes())
        self.assertFalse((self.root / "sessions/AR-0001.jsonl").exists())

    def test_replica_prewrite_fast_forward_and_dirty_refusal(self) -> None:
        CORE.CONFIG.parent.mkdir()
        CORE.CONFIG.write_text('{"push_enabled": true}')
        local = "a" * 40
        remote = "b" * 40
        calls: list[list[str]] = []
        dirty = ""

        def fake_run(args: list[str], **_: object) -> object:
            calls.append(args)
            joined = " ".join(args)
            stdout = ""
            returncode = 0
            if "remote get-url" in joined:
                stdout = "git@example.invalid:owner/state.git\n"
            elif "symbolic-ref" in joined:
                stdout = "main\n"
            elif "rev-parse HEAD" in joined:
                stdout = local + "\n"
            elif "rev-parse FETCH_HEAD" in joined:
                stdout = remote + "\n"
            elif "merge-base" in joined:
                returncode = 0 if args[-2:] == [local, remote] else 1
            elif "status --porcelain" in joined:
                stdout = dirty
            return subprocess.CompletedProcess(args, returncode, stdout=stdout, stderr="")

        CORE.REPLICA_BLOCKED.write_text("{}")
        with patch.object(CORE, "run", side_effect=fake_run):
            CORE.sync_replica_before_write()
        self.assertFalse(CORE.REPLICA_BLOCKED.exists())
        self.assertTrue(any("merge" in args and "--ff-only" in args for args in calls))

        calls.clear()
        dirty = " M task.md\n"
        with (
            patch.object(CORE, "run", side_effect=fake_run),
            self.assertRaisesRegex(CORE.ReplicaDivergedError, "REPLICA_BEHIND_DIRTY"),
        ):
            CORE.sync_replica_before_write()
        self.assertFalse(any("merge" in args and "--ff-only" in args for args in calls))
        blocked = json.loads(CORE.REPLICA_BLOCKED.read_text())
        self.assertEqual("REPLICA_BEHIND_DIRTY", blocked["code"])

    def test_repository_common_lock_is_shared_across_worktrees(self) -> None:
        with TemporaryDirectory() as temporary:
            base = Path(temporary)
            primary = base / "state"
            secondary = base / "state-worktree"
            run_git(["git", "init", "-b", "main", str(primary)], check=True, capture_output=True)
            run_git(
                ["git", "-C", str(primary), "config", "user.email", "test@example.invalid"],
                check=True,
            )
            run_git(
                ["git", "-C", str(primary), "config", "user.name", "Test"],
                check=True,
            )
            (primary / "seed").write_text("seed\n")
            run_git(["git", "-C", str(primary), "add", "seed"], check=True)
            run_git(
                ["git", "-C", str(primary), "commit", "-m", "seed"],
                check=True,
                capture_output=True,
            )
            run_git(
                ["git", "-C", str(primary), "worktree", "add", "-b", "second", str(secondary)],
                check=True,
                capture_output=True,
            )
            CORE.ROOT = primary
            CORE.RUNTIME = primary / ".runtime"
            CORE.LOCK = CORE.RUNTIME / "state.lock"
            first = CORE.coordinator_lock_path()
            CORE.ROOT = secondary
            CORE.RUNTIME = secondary / ".runtime"
            CORE.LOCK = CORE.RUNTIME / "state.lock"
            second = CORE.coordinator_lock_path()
            self.assertEqual(first, second)
            self.assertEqual(primary / ".git" / "handoffctl" / "state.lock", first)
            ready = multiprocessing.Event()
            release = multiprocessing.Event()
            process = multiprocessing.Process(
                target=hold_repository_lock,
                args=(str(primary), ready, release),
            )
            process.start()
            self.assertTrue(ready.wait(5))
            try:
                with (
                    self.assertRaisesRegex(CORE.LockTimeoutError, "LOCK_TIMEOUT"),
                    CORE.locked(timeout=0.1),
                ):
                    pass
            finally:
                release.set()
                process.join(5)
            self.assertEqual(0, process.exitcode)

    def test_github_observation_retries_and_classifies(self) -> None:
        completed = subprocess.CompletedProcess(["gh"], 0, stdout="[]", stderr="")
        with (
            patch.object(CORE, "run", side_effect=[RuntimeError("HTTP 502"), completed]) as run,
            patch.object(CORE.time, "sleep") as sleep,
        ):
            self.assertIs(completed, CORE.run_github_observation(["gh", "run", "list"]))
        self.assertEqual(2, run.call_count)
        sleep.assert_called_once()
        with (
            patch.object(CORE, "run", side_effect=RuntimeError("HTTP 502")),
            patch.object(CORE.time, "sleep"),
            self.assertRaisesRegex(CORE.ExternalObservationError, "EXTERNAL_API_ERROR"),
        ):
            CORE.run_github_observation(["gh", "run", "list"])

    def test_multiple_expired_claims_recover_sequentially(self) -> None:
        expired = "2000-01-01T00:00:00+00:00"
        first = self.make_task(
            "AR-0001",
            status="in_progress",
            owner="worker-a",
            claim_expires=expired,
            worktree_key="worktree-a",
            branch="feature/a",
        )
        second = self.make_task(
            "AR-0002",
            status="in_progress",
            owner="worker-b",
            claim_expires=expired,
            worktree_key="worktree-b",
            branch="feature/b",
        )
        for task_id in ("AR-0001", "AR-0002"):
            CORE.append_session_record(
                CORE.ROOT,
                CORE.build_session_record(
                    CORE.read_task(CORE.locate(task_id)[0])[0],
                    "update",
                    "2026-09-24T12:00:00+00:00",
                ),
            )
        with patch.object(CORE, "commit", return_value=True):
            for task_id in ("AR-0001", "AR-0002"):
                CORE.mutate(
                    argparse.Namespace(
                        task=task_id,
                        expected_revision=1,
                        note="No live process remains.",
                    ),
                    "recover-expired",
                )
        for path in (first, second):
            meta, _ = CORE.read_task(path)
            self.assertEqual("open", meta["status"])
            self.assertEqual("", meta["owner"])
            self.assertEqual(2, meta["task_revision"])
        self.assertEqual([], CORE.validate())

    def test_unrelated_expiry_does_not_block_healthy_lifecycle(self) -> None:
        expired = "2000-01-01T00:00:00+00:00"
        self.make_task(
            "AR-0001",
            status="in_progress",
            owner="stale-worker",
            claim_expires=expired,
        )
        claimed = self.make_task("AR-0002")
        healthy = self.make_task(
            "AR-0003",
            status="in_progress",
            owner="healthy-worker",
            claim_expires="2099-01-01T00:00:00+00:00",
        )
        healthy_meta, healthy_body = CORE.read_task(healthy)
        healthy_meta.update(
            {
                "spec_ref": "spec.json",
                "spec_revision": 1,
                "spec_acceptance": {
                    "spec_ref": "spec.json",
                    "spec_revision": 1,
                    "status": "pass",
                    "evidence_class": "contract-test",
                    "evidence_ref": "awq/evidence/AR-0003",
                    "evidence_digest": "sha256:" + "b" * 64,
                },
            }
        )
        (self.root / "spec.json").write_text(
            json.dumps(
                {
                    "schema_version": 1,
                    "spec_ref": "spec.json",
                    "spec_revision": 1,
                    "acceptance_predicates": [{"id": "predicate", "description": "pass"}],
                    "definition_of_done": ["pass"],
                    "inputs": [{"id": "input", "description": "input"}],
                    "outputs": [{"id": "output", "description": "output"}],
                    "allowed_tools": ["source.read"],
                    "forbidden_tools": [],
                    "required_evidence_classes": ["contract-test"],
                    "gates": [{"id": "gate", "description": "pass"}],
                }
            )
        )
        CORE.write_task(healthy, healthy_meta, healthy_body)
        promoted = self.make_task("AR-0004", status="planned")
        with patch.object(CORE, "commit", return_value=True):
            CORE.mutate(
                argparse.Namespace(task="AR-0002", owner="new-worker", lease_minutes=10),
                "claim",
            )
            CORE.mutate(
                argparse.Namespace(task="AR-0003", owner="healthy-worker", lease_minutes=20),
                "heartbeat",
            )
            CORE.mutate(
                argparse.Namespace(
                    task="AR-0003",
                    owner="healthy-worker",
                    status="done",
                    note="Healthy work completed.",
                ),
                "release",
            )
            with patch.object(CORE, "dirty_state_paths", return_value=[]):
                CORE.mutate(
                    argparse.Namespace(
                        task="AR-0004",
                        expected_revision=1,
                        note="Dependencies verified.",
                    ),
                    "promote",
                )
        self.assertEqual("in_progress", CORE.read_task(claimed)[0]["status"])
        self.assertEqual("done", CORE.read_task(healthy)[0]["status"])
        self.assertEqual("open", CORE.read_task(promoted)[0]["status"])
        self.assertIn("AR-0001: expired claim", CORE.validate())

    def test_preexisting_privacy_and_size_findings_do_not_block_mutations(self) -> None:
        expired = self.make_task(
            "AR-0001",
            status="in_progress",
            owner="stale-worker",
            claim_expires="2000-01-01T00:00:00+00:00",
        )
        CORE.append_session_record(
            CORE.ROOT,
            CORE.build_session_record(
                CORE.read_task(expired)[0], "update", "2026-09-24T12:00:00+00:00"
            ),
        )
        claimed = self.make_task("AR-0002")
        (self.root / "NOTES.md").write_text("Investigate " + "127." + "0.0.1.")
        (self.root / "archive.txt").write_text("x" * 200001)
        with patch.object(CORE, "commit", return_value=True):
            CORE.mutate(
                argparse.Namespace(
                    task="AR-0001",
                    expected_revision=1,
                    note="No live process remains.",
                ),
                "recover-expired",
            )
            CORE.mutate(
                argparse.Namespace(task="AR-0002", owner="new-worker", lease_minutes=10),
                "claim",
            )
        self.assertEqual("open", CORE.read_task(expired)[0]["status"])
        self.assertEqual("in_progress", CORE.read_task(claimed)[0]["status"])
        errors = CORE.validate()
        self.assertIn("NOTES.md: private or loopback IP", errors)
        self.assertIn("archive.txt: state file exceeds 200 KiB", errors)

    def test_new_privacy_and_size_findings_roll_back_exactly(self) -> None:
        path = self.make_task(
            status="in_progress",
            owner="worker-a",
            claim_expires="2099-01-01T00:00:00+00:00",
        )
        CORE.append_session_record(
            CORE.ROOT,
            CORE.build_session_record(
                CORE.read_task(path)[0], "update", "2026-09-24T12:00:00+00:00"
            ),
        )
        owned = (path, self.root / "CURRENT.md", self.root / "STATUS.md")
        before = {candidate: candidate.read_text() for candidate in owned}
        private_args = argparse.Namespace(
            task="AR-0001",
            owner="worker-a",
            expected_revision=1,
            status=None,
            priority=None,
            summary="Connect to " + "127." + "0.0.1.",
            next_action=None,
            note="Unsafe update.",
        )
        with (
            patch.object(CORE, "commit", return_value=True) as commit,
            self.assertRaisesRegex(RuntimeError, "newly introduced private or loopback IP"),
        ):
            CORE.mutate(private_args, "update")
        commit.assert_not_called()
        self.assertTrue(all(candidate.read_text() == before[candidate] for candidate in owned))

        oversized_args = argparse.Namespace(
            task="AR-0001",
            owner="worker-a",
            expected_revision=1,
            status=None,
            priority=None,
            summary=None,
            next_action="x" * 200001,
            note="Oversized update.",
        )
        with (
            patch.object(CORE, "commit", return_value=True) as commit,
            self.assertRaisesRegex(RuntimeError, "state file exceeds 200 KiB"),
        ):
            CORE.mutate(oversized_args, "update")
        commit.assert_not_called()
        self.assertTrue(all(candidate.read_text() == before[candidate] for candidate in owned))
        self.assertEqual(1, CORE.read_task(path)[0]["task_revision"])

    def test_mutation_keeps_global_active_key_uniqueness(self) -> None:
        self.make_task(
            "AR-0001",
            status="in_progress",
            owner="worker-a",
            claim_expires="2099-01-01T00:00:00+00:00",
            worktree_key="shared-worktree",
            branch="feature/shared",
        )
        target = self.make_task(
            "AR-0002",
            worktree_key="shared-worktree",
            branch="feature/shared",
        )
        before = {
            candidate: candidate.read_text()
            for candidate in (target, self.root / "CURRENT.md", self.root / "STATUS.md")
        }
        with (
            patch.object(CORE, "commit", return_value=True) as commit,
            self.assertRaises(RuntimeError) as raised,
        ):
            CORE.mutate(
                argparse.Namespace(task="AR-0002", owner="worker-b", lease_minutes=10), "claim"
            )
        commit.assert_not_called()
        self.assertIn("active worktree_key also used", str(raised.exception))
        self.assertIn("active branch also used", str(raised.exception))
        self.assertTrue(all(candidate.read_text() == before[candidate] for candidate in before))

    def test_mutation_requires_valid_target_even_with_unrelated_findings(self) -> None:
        target = self.make_task("AR-0001", extra="unsupported")
        before = {
            candidate: candidate.read_text()
            for candidate in (target, self.root / "CURRENT.md", self.root / "STATUS.md")
        }
        with (
            patch.object(CORE, "commit", return_value=True) as commit,
            self.assertRaisesRegex(RuntimeError, "unknown field extra"),
        ):
            CORE.mutate(
                argparse.Namespace(task="AR-0001", owner="worker-a", lease_minutes=10),
                "claim",
            )
        commit.assert_not_called()
        self.assertTrue(all(candidate.read_text() == before[candidate] for candidate in before))

    def test_recover_expired_requires_exact_expired_revision(self) -> None:
        future = (
            (dt.datetime.now(dt.UTC) + dt.timedelta(minutes=10)).replace(microsecond=0).isoformat()
        )
        path = self.make_task(
            status="in_progress",
            owner="worker-a",
            claim_expires=future,
            next_action="Resume the verified step.",
        )
        CORE.append_session_record(
            CORE.ROOT,
            CORE.build_session_record(
                CORE.read_task(path)[0], "update", "2026-09-24T12:00:00+00:00"
            ),
        )
        args = argparse.Namespace(
            task="AR-0001",
            expected_revision=1,
            note="No live process remains.",
        )
        with (
            patch.object(CORE, "commit", return_value=True),
            self.assertRaisesRegex(RuntimeError, "has not expired"),
        ):
            CORE.mutate(args, "recover-expired")
        meta, body = CORE.read_task(path)
        meta["claim_expires"] = "2000-01-01T00:00:00+00:00"
        CORE.write_task(path, meta, body)
        self.refresh_views()
        with patch.object(CORE, "commit", return_value=True):
            CORE.mutate(args, "recover-expired")
        recovered, body = CORE.read_task(path)
        self.assertEqual("open", recovered["status"])
        self.assertEqual("", recovered["owner"])
        self.assertEqual("Resume the verified step.", recovered["next_action"])
        self.assertIn("Recovered expired claim formerly owned by worker-a", body)
        with (
            patch.object(CORE, "commit", return_value=True),
            self.assertRaisesRegex(RuntimeError, "stale revision"),
        ):
            CORE.mutate(args, "recover-expired")

    def test_recover_expired_rejects_missing_session(self) -> None:
        self.make_task(
            status="in_progress",
            owner="worker-a",
            claim_expires="2000-01-01T00:00:00+00:00",
        )
        with (
            patch.object(CORE, "commit", return_value=True),
            self.assertRaisesRegex(RuntimeError, "no session snapshot"),
        ):
            CORE.mutate(
                argparse.Namespace(
                    task="AR-0001", expected_revision=1, note="No live process remains."
                ),
                "recover-expired",
            )

    def test_run_preflight_and_durable_journal_precede_reconcile(self) -> None:
        self.make_task(
            status="in_progress",
            owner="worker-a",
            claim_expires="2099-01-01T00:00:00+00:00",
        )
        args = argparse.Namespace(task="AR-0001", owner="worker-a", command=["true"])
        with (
            patch.object(CORE.subprocess, "run") as command,
            self.assertRaisesRegex(RuntimeError, "missing private runtime config"),
        ):
            CORE.cmd_run(args)
        command.assert_not_called()

        CORE.CONFIG.parent.mkdir(exist_ok=True)
        CORE.CONFIG.write_text("{}")
        completed = subprocess.CompletedProcess(["true"], 0, stdout="", stderr="")
        with (
            patch.object(CORE.subprocess, "run", return_value=completed),
            patch.object(CORE, "mutate"),
            patch.object(CORE, "reconcile", side_effect=RuntimeError("HTTP 502")),
            self.assertRaisesRegex(
                CORE.PostCommandReconcileError,
                "COMMAND_RECORDED_POST_RECONCILE_FAILED",
            ),
        ):
            CORE.cmd_run(args)
        journal = [
            json.loads(line)
            for line in (CORE.RUNTIME / "command-results.jsonl").read_text().splitlines()
        ]
        self.assertEqual(0, journal[-1]["returncode"])
        self.assertEqual("AR-0001", journal[-1]["task"])
        self.assertEqual("EXIT", journal[-1]["classification"])

    def test_update_and_run_append_replayable_session_snapshots(self) -> None:
        self.make_task(
            status="in_progress",
            owner="worker-a",
            claim_expires="2099-01-01T00:00:00+00:00",
        )
        update_args = argparse.Namespace(
            task="AR-0001",
            owner="worker-a",
            expected_revision=1,
            status=None,
            priority=None,
            summary=None,
            next_action="Run the verified command.",
            note="updated session state",
        )
        with patch.object(CORE, "commit", return_value=True):
            CORE.mutate(update_args, "update")
        first = CORE.latest_session(CORE.ROOT, "AR-0001")
        self.assertIsNotNone(first)
        self.assertEqual("update", first["trigger"])
        self.assertEqual(2, first["task_revision"])

        CORE.CONFIG.parent.mkdir(exist_ok=True)
        CORE.CONFIG.write_text("{}")
        with (
            patch.object(
                CORE.subprocess, "run", return_value=subprocess.CompletedProcess(["true"], 0)
            ),
            patch.object(CORE, "commit", return_value=True),
            patch.object(CORE, "reconcile", return_value=True),
        ):
            self.assertEqual(
                0,
                CORE.cmd_run(
                    argparse.Namespace(task="AR-0001", owner="worker-a", command=["true"])
                ),
            )
        latest = CORE.latest_session(CORE.ROOT, "AR-0001")
        self.assertEqual("run", latest["trigger"])
        self.assertEqual(3, latest["task_revision"])
        with (
            patch("builtins.print") as output,
            patch.object(CORE, "validate", return_value=[]),
            patch.object(CORE, "run", return_value=SimpleNamespace(stdout="state\n")),
            patch.object(CORE, "project_scan", return_value=self.fake_scan()),
        ):
            CORE.cmd_snapshot("AR-0001")
        self.assertTrue(any("SESSION_SNAPSHOT=" in str(call) for call in output.call_args_list))
        self.assertNotIn(
            "updated session state", (self.root / "sessions/AR-0001.jsonl").read_text()
        )

        empty_note = argparse.Namespace(
            task="AR-0001",
            owner="worker-a",
            expected_revision=3,
            status=None,
            priority=None,
            summary=None,
            next_action=None,
            note="",
        )
        with patch.object(CORE, "commit", return_value=True):
            CORE.mutate(empty_note, "update")
        with (
            patch("builtins.print"),
            patch.object(CORE, "validate", return_value=[]),
            patch.object(CORE, "run", return_value=SimpleNamespace(stdout="state\n")),
            patch.object(CORE, "project_scan", return_value=self.fake_scan()),
            self.assertRaisesRegex(RuntimeError, "no session snapshot"),
        ):
            CORE.cmd_snapshot("AR-9999")

    def test_doctor_rejects_corrupt_session_record(self) -> None:
        self.make_task()
        sessions = self.root / "sessions"
        sessions.mkdir()
        (sessions / "AR-0001.jsonl").write_text("{}\n")
        errors = CORE.validate()
        self.assertTrue(any("session validation failed" in error for error in errors))

    def test_doctor_rejects_wrong_task_and_duplicate_session_history(self) -> None:
        self.make_task()
        sessions = self.root / "sessions"
        sessions.mkdir()
        record = CORE.build_session_record(
            CORE.read_task(self.root / "tasks/AR-0001-test.md")[0],
            "update",
            "2026-10-08T00:00:00+00:00",
        )
        path = sessions / "AR-0001.jsonl"
        path.write_text(json.dumps(dict(record, task="AR-0002")) + "\n")
        self.assertTrue(any("session history is invalid" in error for error in CORE.validate()))
        path.write_text(json.dumps(record) + "\n" + json.dumps(record) + "\n")
        self.assertTrue(any("session history is invalid" in error for error in CORE.validate()))

    def test_git_to_sqlite_migration_rejects_hostile_session_history(self) -> None:
        self.make_task()
        sessions = self.root / "sessions"
        sessions.mkdir()
        record = CORE.build_session_record(
            CORE.read_task(self.root / "tasks/AR-0001-test.md")[0],
            "update",
            "2026-10-08T00:00:00+00:00",
        )
        histories = (
            [record, dict(record)],
            [dict(record, task="AR-0002")],
        )
        for history in histories:
            (sessions / "AR-0001.jsonl").write_text(
                "".join(json.dumps(item) + "\n" for item in history)
            )
            with (
                self.subTest(history=history),
                patch.object(CORE, "sync_replica_before_write"),
                self.assertRaisesRegex(RuntimeError, "session history is invalid"),
            ):
                CORE.cmd_migrate(argparse.Namespace(to="sqlite"))
            self.assertEqual("git", CORE.backend_selection()["backend"])
            self.assertFalse(CORE.DATABASE.exists())

    def test_checkpoint_captures_source_state_before_task_mutation(self) -> None:
        self.make_task(
            status="in_progress",
            owner="worker-a",
            claim_expires="2099-01-01T00:00:00+00:00",
        )
        args = argparse.Namespace(
            task="AR-0001",
            owner="worker-a",
            expected_revision=1,
            source_commit="c" * 40,
        )
        with patch.object(CORE, "commit", return_value=True):
            CORE.mutate(args, "checkpoint")
        record = CORE.load_checkpoints(CORE.ROOT, "AR-0001")
        self.assertEqual(1, len(record))
        self.assertEqual("c" * 40, record[0]["source_commit"])
        self.assertEqual(2, record[0]["task_revision"])
        _, meta, _ = CORE.locate("AR-0001")
        self.assertEqual("c" * 40, meta["checkpoint_commit"])

    def test_checkpoint_command_uses_product_head_when_called_from_worktree(self) -> None:
        args = argparse.Namespace(task="AR-0001", owner="worker-a", expected_revision=1)
        with (
            patch.object(CORE, "invocation_worktree", return_value=("worktree", "branch")),
            patch.object(
                CORE,
                "run",
                return_value=subprocess.CompletedProcess(["git"], 0, stdout="e" * 40 + "\n"),
            ),
            patch.object(CORE, "mutate") as mutate,
        ):
            CORE.cmd_checkpoint(args)
        self.assertEqual("e" * 40, args.source_commit)
        mutate.assert_called_once_with(args, "checkpoint")

    def test_explicit_status_render_and_stale_check(self) -> None:
        self.make_task()
        CORE.cmd_render_status(check=True)
        (self.root / "STATUS.md").write_text("stale")
        with self.assertRaisesRegex(RuntimeError, "STATUS.md differs"):
            CORE.cmd_render_status(check=True)
        CORE.cmd_render_status(check=False)
        self.assertEqual(
            CORE.render_status_view(CORE.all_tasks()), (self.root / "STATUS.md").read_text()
        )

    def test_additive_policy_is_shared_by_doctor_render_run_and_done_lifecycle(self) -> None:
        self.enable_additive_policy()
        self.write_additive_spec()
        acceptance = {
            "spec_ref": "spec.json",
            "spec_revision": 1,
            "status": "pass",
            "evidence_class": "hosted",
            "evidence_ref": "quality/AR-0001",
            "evidence_digest": "sha256:" + "a" * 64,
        }
        self.make_task(
            status="in_progress",
            owner="worker-a",
            claim_expires="2099-01-01T00:00:00+00:00",
            spec_ref="spec.json",
            spec_revision=1,
            spec_acceptance=acceptance,
        )
        self.assertEqual([], CORE.validate())
        CORE.cmd_render_status(check=True)
        with patch.object(CORE, "assert_invocation_worktree"):
            CORE.require_active_owner("AR-0001", "worker-a")
        args = argparse.Namespace(
            task="AR-0001",
            owner="worker-a",
            expected_revision=1,
            status="done",
            note="accepted",
        )
        with (
            patch.object(CORE, "sync_replica_before_write"),
            patch.object(CORE, "commit", return_value=True),
            patch.object(CORE, "push_replica"),
        ):
            CORE.mutate(args, "release")
        self.assertEqual("done", CORE.locate("AR-0001")[1]["status"])

    def test_policy_and_spec_failures_cover_every_read_only_preflight(self) -> None:
        self.make_task(
            status="in_progress",
            owner="worker-a",
            claim_expires="2099-01-01T00:00:00+00:00",
        )
        with patch.object(
            CORE, "evidence_policy", side_effect=RuntimeError("invalid project policy")
        ):
            self.assertIn("invalid project policy", CORE.validate())
            with self.assertRaisesRegex(RuntimeError, "task-spec policy invalid"):
                CORE.cmd_render_status(check=True)
            with self.assertRaisesRegex(RuntimeError, "run preflight failed"):
                CORE.require_active_owner("AR-0001", "worker-a")

        path, meta, body = CORE.locate("AR-0001")
        meta.update(spec_ref="missing.json", spec_revision=1)
        CORE.write_task(path, meta, body)
        self.refresh_views()
        with self.assertRaisesRegex(RuntimeError, "task-spec validation failed"):
            CORE.cmd_render_status(check=True)
        with self.assertRaisesRegex(RuntimeError, "run preflight failed"):
            CORE.require_active_owner("AR-0001", "worker-a")

    def test_done_policy_snapshot_rejects_missing_evidence_and_open_child(self) -> None:
        meta = {"id": "AR-0001", "status": "in_progress"}
        with self.assertRaisesRegex(RuntimeError, "spec_acceptance is incomplete"):
            CORE.require_done_admission(meta, policy=CORE.DEFAULT_EVIDENCE_POLICY)
        accepted = {
            **meta,
            "spec_ref": "spec.json",
            "spec_revision": 1,
            "spec_acceptance": {
                "spec_ref": "spec.json",
                "spec_revision": 1,
                "status": "pass",
                "evidence_class": "contract-test",
                "evidence_ref": "quality/AR-0001",
                "evidence_digest": "sha256:" + "a" * 64,
            },
        }
        spec = json.loads(
            (Path(__file__).resolve().parents[1] / "examples/task-specs/AR-0070.json").read_text()
        )
        spec["spec_ref"] = "spec.json"
        (self.root / "spec.json").write_text(json.dumps(spec), encoding="utf-8")
        with (
            patch.object(CORE, "open_child_error", return_value="open child remains"),
            self.assertRaisesRegex(RuntimeError, "open child remains"),
        ):
            CORE.require_done_admission(
                accepted, [(self.root / "task", accepted, "body")], CORE.DEFAULT_EVIDENCE_POLICY
            )
        CORE.require_done_admission({"status": "open"}, policy=CORE.DEFAULT_EVIDENCE_POLICY)

    def test_policy_change_during_git_mutation_is_atomic(self) -> None:
        self.enable_additive_policy()
        self.make_task(
            status="in_progress",
            owner="worker-a",
            claim_expires="2099-01-01T00:00:00+00:00",
        )
        task_before = CORE.locate("AR-0001")[0].read_text(encoding="utf-8")
        current_before = (self.root / "CURRENT.md").read_text(encoding="utf-8")
        args = argparse.Namespace(
            task="AR-0001",
            owner="worker-a",
            expected_revision=1,
            status=None,
            priority=None,
            summary=None,
            next_action="changed",
            note="race",
        )
        with (
            patch.object(CORE, "sync_replica_before_write"),
            patch.object(
                CORE,
                "require_policy_unchanged",
                side_effect=RuntimeError("task-spec policy changed during operation"),
            ),
            self.assertRaisesRegex(RuntimeError, "policy changed during operation"),
        ):
            CORE.mutate(args, "update")
        self.assertEqual(task_before, CORE.locate("AR-0001")[0].read_text(encoding="utf-8"))
        self.assertEqual(current_before, (self.root / "CURRENT.md").read_text(encoding="utf-8"))
        self.assertFalse((self.root / "sessions/AR-0001.jsonl").exists())

    def test_policy_validation_and_reconcile_failures_leave_state_unchanged(self) -> None:
        path = self.make_task()
        before = path.read_text(encoding="utf-8")
        self.assertTrue(
            any(
                "mutation target is not unique" in error
                for error in CORE.mutation_errors(self.root / "tasks/missing.md", {})
            )
        )
        task = CORE.locate("AR-0001")
        with patch.object(CORE, "all_tasks", return_value=[task, task]):
            self.assertIn("duplicate AR-0001", CORE.validate())
        failing_backend = unittest.mock.Mock()
        failing_backend.load_tasks.return_value = [task]
        failing_backend.load_checkpoint_records.side_effect = RuntimeError("checkpoint fault")
        failing_backend.load_session_records.return_value = []
        with patch.object(CORE, "storage_backend", return_value=failing_backend):
            self.assertIn("checkpoint validation failed", "\n".join(CORE.validate()))

        with (
            patch.object(
                CORE, "backend_selection", side_effect=[{"backend": "git"}, {"backend": "sqlite"}]
            ),
            patch.object(CORE, "project_scan", return_value=self.fake_scan()),
            self.assertRaisesRegex(RuntimeError, "BACKEND_CHANGED"),
        ):
            CORE.reconcile(do_commit=False)
        with (
            patch.object(CORE, "backend_selection", return_value={"backend": "git"}),
            patch.object(CORE, "sync_replica_before_write"),
            patch.object(CORE, "project_scan", return_value=self.fake_scan()),
            patch.object(CORE, "write_generated_views"),
            patch.object(CORE, "validate", return_value=["injected policy validation"]),
            self.assertRaisesRegex(RuntimeError, "validation failed"),
        ):
            CORE.reconcile(do_commit=False)
        self.assertEqual(before, path.read_text(encoding="utf-8"))

    def test_policy_lifecycle_helpers_reject_inactive_gate_and_prune_stale_view(self) -> None:
        self.make_task(status="open", owner="worker-a")
        with self.assertRaisesRegex(RuntimeError, "claim is not active"):
            CORE.require_active_owner("AR-0001", "worker-a")
        path, meta, body = CORE.locate("AR-0001")
        meta.update(
            status="in_progress",
            owner="worker-a",
            claim_expires="2099-01-01T00:00:00+00:00",
        )
        CORE.write_task(path, meta, body)
        with (
            patch.object(CORE, "transition_allowed", side_effect=CORE.GateError("gate denied")),
            self.assertRaisesRegex(RuntimeError, "gate denied"),
        ):
            CORE.require_active_owner("AR-0001", "worker-a")
        self.assertEqual("body", CORE._transition_note("body", "", "now"))
        stale = self.root / "status/STATUS-9999.md"
        stale.parent.mkdir()
        stale.write_text("stale", encoding="utf-8")
        CORE.write_status_views({"STATUS.md": "current\n"})
        self.assertFalse(stale.exists())

    def test_doctor_reports_replica_circuit_breaker(self) -> None:
        CORE.REPLICA_BLOCKED.parent.mkdir(exist_ok=True)
        CORE.REPLICA_BLOCKED.write_text('{"code": "REPLICA_DIVERGED"}')
        with patch.object(CORE, "validate", return_value=[]), patch("builtins.print") as output:
            self.assertEqual(1, CORE.cmd_doctor(live=False))
        self.assertIn("REPLICA_DIVERGED", output.call_args.args[0])
        CORE.REPLICA_BLOCKED.write_text("bad")
        with patch.object(CORE, "validate", return_value=[]), patch("builtins.print") as output:
            self.assertEqual(1, CORE.cmd_doctor(live=False))
        self.assertIn("REPLICA_BLOCKED", output.call_args.args[0])

    def test_main_dispatches_every_command(self) -> None:
        cases = [
            (["handoffctl", "reconcile", "--commit"], "reconcile", None),
            (["handoffctl", "snapshot"], "cmd_snapshot", None),
            (["handoffctl", "render-status", "--check"], "cmd_render_status", None),
            (["handoffctl", "claim", "AR-0001", "--owner", "worker-a"], "mutate", None),
            (["handoffctl", "heartbeat", "AR-0001", "--owner", "worker-a"], "mutate", None),
            (
                [
                    "handoffctl",
                    "promote",
                    "AR-0001",
                    "--expected-revision",
                    "1",
                    "--note",
                    "ready",
                ],
                "mutate",
                None,
            ),
            (
                [
                    "handoffctl",
                    "resume",
                    "AR-0001",
                    "--expected-revision",
                    "1",
                    "--session",
                    "AR-0001@1",
                    "--note",
                    "ready",
                ],
                "mutate",
                None,
            ),
            (
                [
                    "handoffctl",
                    "unblock",
                    "AR-0001",
                    "--expected-revision",
                    "1",
                    "--note",
                    "external clear",
                ],
                "mutate",
                None,
            ),
            (
                [
                    "handoffctl",
                    "pause",
                    "AR-0001",
                    "--owner",
                    "worker-a",
                    "--expected-revision",
                    "1",
                    "--note",
                    "pause",
                ],
                "mutate",
                None,
            ),
            (
                [
                    "handoffctl",
                    "release",
                    "AR-0001",
                    "--owner",
                    "worker-a",
                    "--status",
                    "open",
                    "--note",
                    "pause",
                ],
                "mutate",
                None,
            ),
            (
                [
                    "handoffctl",
                    "recover-expired",
                    "AR-0001",
                    "--expected-revision",
                    "1",
                    "--note",
                    "expired",
                ],
                "mutate",
                None,
            ),
            (
                [
                    "handoffctl",
                    "update",
                    "AR-0001",
                    "--owner",
                    "worker-a",
                    "--expected-revision",
                    "1",
                    "--note",
                    "update",
                ],
                "mutate",
                None,
            ),
            (
                ["handoffctl", "run", "--owner", "worker-a", "AR-0001", "--", "true"],
                "cmd_run",
                7,
            ),
            (
                ["handoffctl", "upgrade", "check", "--contract", "contract.json"],
                "cmd_upgrade",
                0,
            ),
        ]
        for argv, target, result in cases:
            with (
                self.subTest(target=target),
                patch.object(sys, "argv", argv),
                patch.object(CORE, target, return_value=result) as called,
                patch.object(CORE, "assert_project_binding"),
            ):
                self.assertEqual(result or 0, CORE.main())
                called.assert_called_once()
        with (
            patch.object(sys, "argv", ["handoffctl", "doctor"]),
            patch.object(CORE, "validate", return_value=[]),
            patch.object(CORE, "assert_project_binding"),
            patch("builtins.print"),
        ):
            self.assertEqual(0, CORE.main())
        with (
            patch.object(sys, "argv", ["handoffctl", "doctor", "--live"]),
            patch.object(CORE, "validate", return_value=["bad"]),
            patch.object(CORE, "project_scan", return_value=self.fake_scan()),
            patch.object(CORE, "assert_project_binding"),
            patch("builtins.print"),
        ):
            self.assertEqual(1, CORE.main())

    def test_cmd_upgrade_dispatches_both_live_binding_resolvers(self) -> None:
        commands = importlib.import_module("upgrade_commands")
        production = importlib.import_module("production_upgrade_binding")
        args = argparse.Namespace(
            upgrade_action="apply",
            contract="contract.json",
            binding="binding.json",
        )
        for backend, resolver_name in (
            ("sqlite", "resolve_sqlite_live_binding"),
            ("git", "resolve_git_live_binding"),
        ):
            with (
                self.subTest(backend=backend),
                patch.object(CORE, "backend_selection", return_value={"backend": backend}),
                patch.object(commands, "_read_contract", return_value={"contract": True}),
                patch.object(commands, "_read_runtime_binding", return_value="runtime"),
                patch.object(production, resolver_name, return_value="live") as resolver,
                patch.object(commands, "execute_upgrade_command", return_value=0) as execute,
            ):
                self.assertEqual(0, CORE.cmd_upgrade(args))
            resolver.assert_called_once()
            execute.assert_called_once_with(
                "apply", Path("contract.json"), backend, Path("binding.json"), "live"
            )

    def test_oracle_gate_dispatch_and_transition_errors_are_normalized(self) -> None:
        digest = "sha256:" + "a" * 64
        values = CORE._artifact_values([f"plan/before={digest}"], "--before")
        self.assertEqual("plan/before", values[0].ref)
        with self.assertRaisesRegex(RuntimeError, "REF=DIGEST"):
            CORE._artifact_values(["malformed"], "--before")
        with self.assertRaisesRegex(RuntimeError, "sha256 digest"):
            CORE._artifact_values(["plan/before=bad"], "--before")

        meta: dict[str, Any] = {"id": "AR-0022", "task_revision": 1}
        args = argparse.Namespace(
            expected_revision=1,
            stage="intake",
            action="open",
            disposition="accepted",
            before=[f"plan/before={digest}"],
            after=[f"plan/after={'sha256:' + 'b' * 64}"],
            public_ref="oracle/decision-1",
        )
        self.assertIn("Recorded open", CORE.apply_gate(args, meta))
        with self.assertRaisesRegex(RuntimeError, "already open"):
            CORE.apply_gate(args, meta)
        args.stage = "not-a-stage"
        with self.assertRaisesRegex(RuntimeError, "unknown interaction gate stage"):
            CORE.apply_gate(args, {"id": "AR-0022", "task_revision": 1})

        held_gate = {"required": True, "open_stage": "intake"}
        release_args = argparse.Namespace(owner="worker", status="done", note="released")
        with self.assertRaisesRegex(RuntimeError, "unresolved"):
            CORE.apply_owned_change(
                release_args,
                "release",
                {"id": "AR-0022", "owner": "worker", "oracle_gate": held_gate},
            )
        released = {
            "id": "AR-0022",
            "owner": "worker",
            "oracle_gate": {"required": True, "open_stage": None},
        }
        self.assertEqual("released", CORE.apply_owned_change(release_args, "release", released))
        self.assertEqual("done", released["status"])

    def test_oracle_gate_blocks_claim_and_promote(self) -> None:
        gate = {"required": True, "open_stage": "intake"}
        claim_args = argparse.Namespace(task="AR-0022", owner="worker", lease_minutes=10)
        with self.assertRaisesRegex(RuntimeError, "unresolved"):
            CORE.apply_claim(
                claim_args,
                {"id": "AR-0022", "status": "open", "oracle_gate": gate},
                [],
            )
        promote_args = argparse.Namespace(task="AR-0022", expected_revision=1, note="promote")
        with self.assertRaisesRegex(RuntimeError, "unresolved"):
            CORE.apply_promote(
                promote_args,
                {"id": "AR-0022", "status": "planned", "task_revision": 1, "oracle_gate": gate},
                [],
            )


if __name__ == "__main__":
    unittest.main()
