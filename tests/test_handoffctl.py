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
SPEC = importlib.util.spec_from_file_location("handoffctl_core", SOURCE)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load handoffctl")
CORE: Any = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CORE)


def hold_lock(lock_path: str, ready: Any, release: Any) -> None:
    """Hold an exclusive lock in a separate process."""
    CORE.LOCK = Path(lock_path)
    CORE.RUNTIME = CORE.LOCK.parent
    with CORE.locked():
        ready.set()
        release.wait(5)


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
        CORE.TASKS.mkdir()
        (root / "plans").mkdir()
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
        CORE.atomic(self.root / "CURRENT.md", CORE.render_current(CORE.all_tasks()))
        return cast(Path, path)

    def test_atomic_task_round_trip_and_render(self) -> None:
        path = self.make_task()
        meta, body = CORE.read_task(path)
        self.assertEqual("AR-0001", meta["id"])
        self.assertEqual("# Test\n", body)
        current = CORE.render_current(CORE.all_tasks())
        self.assertIn("## Open", current)
        self.assertIn("[AR-0001]", current)

    def test_rejects_bad_front_matter(self) -> None:
        path = CORE.TASKS / "AR-0001-bad.md"
        path.write_text("bad")
        with self.assertRaisesRegex(ValueError, "no front matter"):
            CORE.read_task(path)
        path.write_text("---\n{}")
        with self.assertRaisesRegex(ValueError, "unterminated"):
            CORE.read_task(path)

    def test_validation_finds_schema_graph_claim_and_privacy_errors(self) -> None:
        self.make_task("AR-0001", depends_on=["AR-0002"], extra="bad")
        self.make_task(
            "AR-0002",
            status="in_progress",
            owner="worker-a",
            claim_expires="",
            depends_on=["AR-0001"],
        )
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

    def test_invalid_update_rolls_back_both_files(self) -> None:
        path = self.make_task()
        with patch.object(CORE, "commit", return_value=True):
            CORE.mutate(
                argparse.Namespace(task="AR-0001", owner="worker-a", lease_minutes=10),
                "claim",
            )
            before_task = path.read_text()
            before_current = (self.root / "CURRENT.md").read_text()
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
        errors = "\n".join(CORE.privacy_errors())
        self.assertIn("exceeds 200 KiB", errors)

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

    def test_commit_no_change_and_change_paths(self) -> None:
        target = self.root / "CURRENT.md"
        target.write_text("x")
        calls = []

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
            self.assertRaisesRegex(RuntimeError, "diverged"),
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
        with (
            patch.object(CORE.subprocess, "run", return_value=completed) as subprocess_run,
            patch.object(CORE, "reconcile"),
            patch.object(CORE, "mutate") as mutate,
        ):
            self.assertEqual(0, CORE.cmd_run(args))
            self.assertIn("command argv SHA-256", mutate.call_args.args[0].note)
            self.assertIsNone(mutate.call_args.args[0].expected_revision)
            subprocess_run.assert_called_once_with(["true"], check=False, stdin=subprocess.DEVNULL)
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

    def test_main_dispatches_every_command(self) -> None:
        cases = [
            (["handoffctl", "reconcile", "--commit"], "reconcile", None),
            (["handoffctl", "snapshot"], "cmd_snapshot", None),
            (["handoffctl", "claim", "AR-0001", "--owner", "worker-a"], "mutate", None),
            (["handoffctl", "heartbeat", "AR-0001", "--owner", "worker-a"], "mutate", None),
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
            ):
                self.assertEqual(result or 0, CORE.main())
                called.assert_called_once()
        with (
            patch.object(sys, "argv", ["handoffctl", "doctor"]),
            patch.object(CORE, "validate", return_value=[]),
            patch("builtins.print"),
        ):
            self.assertEqual(0, CORE.main())
        with (
            patch.object(sys, "argv", ["handoffctl", "doctor", "--live"]),
            patch.object(CORE, "validate", return_value=["bad"]),
            patch("builtins.print"),
        ):
            self.assertEqual(1, CORE.main())


if __name__ == "__main__":
    unittest.main()
