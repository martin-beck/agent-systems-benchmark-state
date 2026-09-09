# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Fault, consistency, claim and generation tests for handoffctl."""

import argparse
import datetime as dt
import importlib.util
import json
import multiprocessing
import subprocess
import sys
import time
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Any, cast
from unittest.mock import patch

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
                    "project_id": "11111111-1111-4111-8111-111111111111",
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
                    "project_id": "11111111-1111-4111-8111-111111111111",
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
                return_value=CORE.uuid.UUID("33333333-3333-4333-8333-333333333333"),
            ),
            patch("builtins.print"),
        ):
            run.return_value = subprocess.CompletedProcess([], 0, str(self.root) + "\n", "")
            CORE.cmd_init(args)
        self.assertEqual(
            "33333333-3333-4333-8333-333333333333", CORE.project_settings()["project_id"]
        )
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
            {**valid_settings, "project_id": "11111111-1111-1111-8111-111111111111"},
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
            {**valid_binding, "project_id": "11111111-1111-1111-8111-111111111111"},
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

    def test_future_series_is_never_omitted_from_graph_or_text_fallback(self) -> None:
        self.make_task("AR-1101")
        status = CORE.render_status_view(CORE.all_tasks())
        self.assertEqual(1, status.count('AR_1101["AR-1101 - Open"]'))
        self.assertIn('subgraph series_11["11 - Additional work"]', status)
        self.assertIn("| [AR-1101](tasks/AR-1101-test.md) | None | None |", status)

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
            self.assertRaisesRegex(RuntimeError, "promotion preflight failed"),
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
        args = argparse.Namespace(task="AR-0001", expected_revision=0, note="blocker cleared")
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
                argparse.Namespace(task="AR-0001", expected_revision=2, note="again"),
                "resume",
            )

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
        sample_uuid = "33333333-3333-4333-8333-333333333333"
        for relative in (
            Path("tools/handoffctl.py"),
            Path("tests/test_handoffctl.py"),
            Path("tests/test_sqlite_storage.py"),
        ):
            fixture = self.root / relative
            fixture.parent.mkdir(exist_ok=True)
            fixture.write_text(sample_uuid)
        (self.root / "notes.md").write_text(sample_uuid)
        CORE.BINDING.write_text(CORE.BINDING.read_text() + "\ntoken=leak\n")
        errors = "\n".join(CORE.privacy_errors())
        self.assertIn("exceeds 200 KiB", errors)
        self.assertIn("notes.md: session-like UUID", errors)
        self.assertNotIn("tools/handoffctl.py: session-like UUID", errors)
        self.assertNotIn("tests/test_handoffctl.py: session-like UUID", errors)
        self.assertNotIn("tests/test_sqlite_storage.py: session-like UUID", errors)
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
        product.mkdir()
        second.mkdir()
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

        def fake_run(args: list[str], **_: object) -> object:  # noqa: C901
            joined = " ".join(args)
            stdout = ""
            returncode = 0
            if "worktree list" in joined:
                stdout = f"worktree {product}\n\nworktree {second}\n"
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

    def test_recover_expired_requires_exact_expired_revision(self) -> None:
        future = (
            (dt.datetime.now(dt.UTC) + dt.timedelta(minutes=10)).replace(microsecond=0).isoformat()
        )
        path = self.make_task(
            status="in_progress",
            owner="worker-a",
            claim_expires=future,
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
        self.assertIn("Recovered expired claim formerly owned by worker-a", body)
        with (
            patch.object(CORE, "commit", return_value=True),
            self.assertRaisesRegex(RuntimeError, "stale revision"),
        ):
            CORE.mutate(args, "recover-expired")

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
                    "--note",
                    "ready",
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
            patch.object(CORE, "assert_project_binding"),
            patch("builtins.print"),
        ):
            self.assertEqual(1, CORE.main())


if __name__ == "__main__":
    unittest.main()
