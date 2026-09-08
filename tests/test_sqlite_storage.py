# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""SQLite backend conformance, fault and real multiprocess tests."""

import argparse
import importlib.util
import json
import multiprocessing
import sqlite3
import subprocess
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Any
from unittest.mock import patch

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / "tools"
sys.path.insert(0, str(TOOLS))
from sqlite_storage import (  # noqa: E402
    SQLiteBackend,
    StorageContentionError,
    _translate,
    create_database,
    require_local_filesystem,
)

SPEC = importlib.util.spec_from_file_location("handoffctl_sqlite_test", TOOLS / "handoffctl.py")
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load handoffctl")
CORE: Any = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CORE)

BINDING = {
    "schema_version": 1,
    "project_id": "11111111-1111-4111-8111-111111111111",
    "state_repository": "owner/state",
    "product_repository": "owner/product",
}


def task(
    task_id: str, *, status: str = "open", revision: int = 1
) -> tuple[Path, dict[str, Any], str]:
    meta = {
        "schema_version": 1,
        "id": task_id,
        "title": "Test task",
        "status": status,
        "priority": "P1",
        "summary": "Ready.",
        "next_action": "Test.",
        "task_revision": revision,
        "updated_at": "2026-09-08T00:00:00+00:00",
        "owner": "",
        "claim_expires": "",
        "worktree_key": "",
        "branch": "",
        "checkpoint_commit": "",
        "plan": "",
        "depends_on": [],
    }
    return Path(f"{task_id}-test.md"), meta, "# Test\n"


def claim_worker(database: str, tasks_root: str, start: Any, owner: str, outcomes: Any) -> None:
    backend = SQLiteBackend(Path(database), BINDING, Path(tasks_root))
    start.wait(5)

    def claim(meta: dict[str, Any], _tasks: list[Any]) -> tuple[str, str]:
        if meta["status"] != "open":
            raise RuntimeError("not open")
        meta["status"] = "in_progress"
        meta["owner"] = owner
        meta["claim_expires"] = "2099-01-01T00:00:00+00:00"
        return "claimed", "# Test\n- claimed\n"

    try:
        backend.mutate("AR-0001", 1, "claim", "2026-09-08T00:01:00+00:00", claim)
    except RuntimeError as error:
        outcomes.put(("rejected", str(error)))
    else:
        outcomes.put(("accepted", owner))


def revision_stress_worker(
    database: str, tasks_root: str, start: Any, task_id: str, iterations: int, outcomes: Any
) -> None:
    """Commit many CAS-fenced updates with stale-revision retry in an independent process."""
    backend = SQLiteBackend(Path(database), BINDING, Path(tasks_root))
    start.wait(5)
    completed = 0
    while completed < iterations:
        tasks = backend.load_tasks()
        revision = int(next(item[1] for item in tasks if item[1]["id"] == task_id)["task_revision"])

        def update(meta: dict[str, Any], _tasks: list[Any]) -> tuple[str, str]:
            meta["summary"] = "stress update"
            return "stress", "# stress\n"

        try:
            backend.mutate(task_id, revision, "update", "2026-09-08T00:01:00+00:00", update)
        except RuntimeError as error:
            if "stale revision" not in str(error):
                outcomes.put(("error", str(error)))
                return
        else:
            completed += 1
    outcomes.put(("done", task_id, completed))


class SQLiteStorageTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.tasks = self.root / "tasks"
        self.tasks.mkdir()
        self.database = self.root / ".runtime/coordinator.sqlite3"

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def create(self, tasks: list[Any] | None = None) -> SQLiteBackend:
        create_database(
            self.database,
            BINDING,
            tasks or [task("AR-0001")],
            imported_at="2026-09-08T00:00:00+00:00",
            source_backend="git",
            source_checkpoint="a" * 40,
        )
        return SQLiteBackend(self.database, BINDING, self.tasks)

    def configure_core(self, *, backend: str = "git") -> None:
        """Point the CLI module at this isolated project fixture."""
        CORE.ROOT = self.root
        CORE.TASKS = self.tasks
        CORE.RUNTIME = self.root / ".runtime"
        CORE.LOCK = CORE.RUNTIME / "state.lock"
        CORE.CONFIG = CORE.RUNTIME / "config.json"
        CORE.REPLICA_BLOCKED = CORE.RUNTIME / "replica-blocked.json"
        CORE.PROJECT_CONFIG = self.root / ".handoffctl.json"
        CORE.BINDING = self.root / "coordinator.binding.json"
        CORE.BACKEND_CONFIG = self.root / "coordinator.backend.json"
        CORE.DATABASE = self.database
        CORE.PROJECT_CONFIG.write_text(
            json.dumps(
                {
                    "schema_version": 1,
                    "project_id": BINDING["project_id"],
                    "project_name": "test-project",
                    "project_title": "Test Project",
                    "status_view": False,
                    "commit_signoff": False,
                }
            )
        )
        CORE.BINDING.write_text(json.dumps(BINDING))
        CORE.BACKEND_CONFIG.write_text(
            json.dumps(
                {"schema_version": 1, "project_id": BINDING["project_id"], "backend": backend}
            )
        )

    def write_git_tasks(self, values: list[Any] | None = None) -> None:
        for path, meta, body in values or [task("AR-0001")]:
            CORE.write_task(self.tasks / path.name, meta, body)
        CORE.atomic(self.root / "CURRENT.md", CORE.render_current(CORE.git_tasks()))

    def test_database_is_wal_full_durable_bound_and_strict(self) -> None:
        backend = self.create()
        connection = sqlite3.connect(self.database)
        self.assertEqual("wal", connection.execute("PRAGMA journal_mode").fetchone()[0])
        self.assertEqual(2, connection.execute("PRAGMA synchronous").fetchone()[0])
        self.assertEqual(
            "strict",
            connection.execute(
                "SELECT strict FROM pragma_table_list WHERE name='tasks'"
            ).fetchone()[0]
            and "strict",
        )
        connection.close()
        self.assertEqual("AR-0001", backend.load_tasks()[0][1]["id"])
        copied = SQLiteBackend(self.database, {**BINDING, "project_id": "other"}, self.tasks)
        with self.assertRaisesRegex(RuntimeError, "BINDING_MISMATCH"):
            copied.load_tasks()

    def test_exact_revision_cas_events_and_aba_prevention(self) -> None:
        backend = self.create()

        def update(meta: dict[str, Any], _tasks: list[Any]) -> tuple[str, str]:
            meta["summary"] = "changed"
            return "changed", "body"

        backend.mutate("AR-0001", 1, "update", "2026-09-08T00:01:00+00:00", update)
        with self.assertRaisesRegex(RuntimeError, "stale revision"):
            backend.mutate("AR-0001", 1, "update", "2026-09-08T00:02:00+00:00", update)
        connection = sqlite3.connect(self.database)
        self.assertEqual(2, connection.execute("SELECT revision FROM tasks").fetchone()[0])
        self.assertEqual(2, connection.execute("SELECT count(*) FROM events").fetchone()[0])
        connection.close()

    def test_real_processes_cannot_double_claim(self) -> None:
        backend = self.create()
        context = multiprocessing.get_context("fork")
        start, outcomes = context.Event(), context.Queue()
        processes = [
            context.Process(
                target=claim_worker,
                args=(str(self.database), str(self.tasks), start, owner, outcomes),
            )
            for owner in ("worker-a", "worker-b")
        ]
        for process in processes:
            process.start()
        start.set()
        results = [outcomes.get(timeout=10) for _ in processes]
        for process in processes:
            process.join(10)
            self.assertEqual(0, process.exitcode)
        self.assertEqual(1, sum(result[0] == "accepted" for result in results))
        row = backend.load_tasks()[0][1]
        self.assertEqual("in_progress", row["status"])
        self.assertIn(row["owner"], ("worker-a", "worker-b"))

    def test_high_frequency_same_and_different_task_writers_have_no_lost_updates(self) -> None:
        backend = self.create([task("AR-0001"), task("AR-0002")])
        context = multiprocessing.get_context("fork")
        start, outcomes = context.Event(), context.Queue()
        task_ids = ("AR-0001", "AR-0001", "AR-0002", "AR-0002")
        processes = [
            context.Process(
                target=revision_stress_worker,
                args=(str(self.database), str(self.tasks), start, task_id, 20, outcomes),
            )
            for task_id in task_ids
        ]
        for process in processes:
            process.start()
        start.set()
        results = [outcomes.get(timeout=30) for _ in processes]
        for process in processes:
            process.join(30)
            self.assertEqual(0, process.exitcode)
        self.assertTrue(all(result[0] == "done" for result in results), results)
        tasks = backend.load_tasks()
        self.assertEqual([41, 41], [item[1]["task_revision"] for item in tasks])
        connection = sqlite3.connect(self.database)
        self.assertEqual(82, connection.execute("SELECT count(*) FROM events").fetchone()[0])
        connection.close()

    def test_database_constraints_reject_duplicate_active_owner(self) -> None:
        backend = self.create([task("AR-0001"), task("AR-0002")])

        def claim(meta: dict[str, Any], _tasks: list[Any]) -> tuple[str, str]:
            meta.update(
                status="in_progress", owner="one", claim_expires="2099-01-01T00:00:00+00:00"
            )
            return "claim", "body"

        backend.mutate("AR-0001", 1, "claim", "2026-09-08T00:01:00+00:00", claim)
        with self.assertRaisesRegex(RuntimeError, "UNIQUE constraint"):
            backend.mutate("AR-0002", 1, "claim", "2026-09-08T00:02:00+00:00", claim)
        self.assertEqual(1, backend.load_tasks()[1][1]["task_revision"])

    def test_command_result_is_an_independent_durable_transaction(self) -> None:
        backend = self.create()
        backend.append_command_result(
            "AR-0001", "worker", "a" * 64, 7, "EXIT", "2026-09-08T00:01:00+00:00"
        )
        connection = sqlite3.connect(self.database)
        self.assertEqual(
            (7, "EXIT"),
            connection.execute("SELECT returncode, classification FROM command_results").fetchone(),
        )
        connection.close()

    def test_busy_timeout_corruption_network_fs_and_read_only_fail_closed(self) -> None:
        backend = self.create()
        connection = sqlite3.connect(self.database, isolation_level=None)
        connection.execute("BEGIN IMMEDIATE")
        with (
            patch("sqlite_storage.BUSY_TIMEOUT_MS", 25),
            self.assertRaises(StorageContentionError),
            backend.transaction(),
        ):
            pass
        connection.rollback()
        connection.close()
        with self.assertRaisesRegex(RuntimeError, "UNSUPPORTED_FILESYSTEM"):
            require_local_filesystem(self.database, "1 1 0:1 / / rw - nfs server rw\n")
        corrupt = self.root / "corrupt.sqlite3"
        corrupt.write_bytes(b"not a database")
        with self.assertRaisesRegex(RuntimeError, "SQLITE_(?:CORRUPT|ERROR)"):
            SQLiteBackend(corrupt, BINDING, self.tasks).load_tasks()

    def test_failed_atomic_install_does_not_select_partial_database(self) -> None:
        with (
            patch.object(Path, "replace", side_effect=OSError(28, "disk full")),
            self.assertRaisesRegex(OSError, "disk full"),
        ):
            self.create()
        self.assertFalse(self.database.exists())

    def test_legacy_backend_selection_and_cli_default(self) -> None:
        old = (CORE.ROOT, CORE.BACKEND_CONFIG)
        CORE.ROOT = self.root
        CORE.BACKEND_CONFIG = self.root / "coordinator.backend.json"
        try:
            self.assertEqual("git", CORE.backend_selection()["backend"])
            CORE.BACKEND_CONFIG.write_text(
                json.dumps(
                    {"schema_version": 1, "project_id": BINDING["project_id"], "backend": "sqlite"}
                )
            )
            self.assertEqual("sqlite", CORE.backend_selection()["backend"])
            with (
                patch.object(
                    sys,
                    "argv",
                    [
                        "handoffctl",
                        "init",
                        "--state-repository",
                        "o/s",
                        "--product-repository",
                        "o/p",
                        "--project-name",
                        "p",
                        "--project-title",
                        "P",
                    ],
                ),
                patch.object(CORE, "cmd_init") as initialize,
            ):
                CORE.main()
            self.assertEqual("sqlite", initialize.call_args.args[0].backend)
        finally:
            CORE.ROOT, CORE.BACKEND_CONFIG = old

    def test_explicit_migration_round_trip_preserves_records_and_projections(self) -> None:
        self.configure_core()
        self.write_git_tasks([task("AR-0001"), task("AR-0002")])
        CORE.RUNTIME.mkdir(exist_ok=True)
        (CORE.RUNTIME / "command-results.jsonl").write_text(
            json.dumps(
                {
                    "at": "2026-09-08T00:00:00+00:00",
                    "task": "AR-0001",
                    "owner": "worker",
                    "argv_sha256": "a" * 64,
                    "returncode": 0,
                    "classification": "EXIT",
                }
            )
            + "\n"
        )
        completed = subprocess.CompletedProcess([], 0, "b" * 40 + "\n", "")
        with (
            patch.object(CORE, "sync_replica_before_write"),
            patch.object(CORE, "run", return_value=completed),
            patch("builtins.print"),
        ):
            CORE.cmd_migrate(argparse.Namespace(to="sqlite"))
        self.assertEqual("sqlite", CORE.backend_selection()["backend"])
        self.assertEqual(["AR-0001", "AR-0002"], [item[1]["id"] for item in CORE.all_tasks()])
        connection = sqlite3.connect(self.database)
        self.assertEqual(
            1, connection.execute("SELECT count(*) FROM command_results").fetchone()[0]
        )
        connection.close()
        self.assertEqual(
            CORE.render_current(CORE.all_tasks()), (self.root / "CURRENT.md").read_text()
        )
        with patch("builtins.print"):
            CORE.cmd_migrate(argparse.Namespace(to="git"))
        self.assertEqual("git", CORE.backend_selection()["backend"])
        self.assertEqual(2, len(CORE.git_tasks()))
        with self.assertRaisesRegex(RuntimeError, "already uses"):
            CORE.cmd_migrate(argparse.Namespace(to="git"))

    def test_sqlite_cli_lifecycle_uses_same_transition_contract(self) -> None:
        self.configure_core(backend="sqlite")
        self.create()
        CORE.export_sqlite_projections()
        with patch.object(CORE, "push_replica"):
            CORE.mutate(
                argparse.Namespace(task="AR-0001", owner="worker", lease_minutes=10), "claim"
            )
            claimed = CORE.all_tasks()[0][1]
            CORE.mutate(
                argparse.Namespace(
                    task="AR-0001",
                    owner="worker",
                    expected_revision=claimed["task_revision"],
                    status=None,
                    priority="P0",
                    summary=None,
                    next_action=None,
                    note="updated",
                ),
                "update",
            )
            CORE.mutate(
                argparse.Namespace(task="AR-0001", owner="worker", status="done", note="done"),
                "release",
            )
        final = CORE.all_tasks()[0][1]
        self.assertEqual(
            ("done", 4, "P0"), (final["status"], final["task_revision"], final["priority"])
        )
        self.assertIn("updated", (self.tasks / "AR-0001-test.md").read_text())

    def test_sqlite_projection_failure_does_not_rollback_committed_task(self) -> None:
        self.configure_core(backend="sqlite")
        self.create()
        with (
            patch.object(CORE, "export_sqlite_projections", side_effect=OSError(28, "disk full")),
            self.assertRaisesRegex(CORE.StorageCommittedError, "SQLITE_COMMITTED_EXPORT_FAILED"),
        ):
            CORE.mutate(
                argparse.Namespace(task="AR-0001", owner="worker", lease_minutes=10), "claim"
            )
        self.assertEqual(2, CORE.all_tasks()[0][1]["task_revision"])

    def test_sqlite_command_journal_snapshot_doctor_and_offline_reconcile(self) -> None:
        self.configure_core(backend="sqlite")
        self.create()
        CORE.export_sqlite_projections()
        CORE.append_command_result("AR-0001", "worker", "f" * 64, 0, False)
        with patch("builtins.print") as output:
            CORE.cmd_snapshot()
        self.assertTrue(
            any("STORAGE_BACKEND=sqlite" in str(call) for call in output.call_args_list)
        )
        with patch("builtins.print"):
            self.assertEqual(0, CORE.cmd_doctor(live=True))
        CORE.RUNTIME.mkdir(exist_ok=True)
        CORE.CONFIG.write_text("{}")
        with patch("builtins.print"):
            self.assertEqual(0, CORE.cmd_doctor(live=True))
        self.assertTrue(CORE.reconcile(do_commit=False))

    def test_sqlite_run_needs_no_runtime_or_network_publication(self) -> None:
        self.configure_core(backend="sqlite")
        self.create()
        CORE.export_sqlite_projections()
        CORE.mutate(argparse.Namespace(task="AR-0001", owner="worker", lease_minutes=10), "claim")
        args = argparse.Namespace(
            task="AR-0001", owner="worker", timeout_seconds=5.0, command=["/bin/true"]
        )
        with patch.object(CORE, "reconcile", return_value=True) as reconcile:
            self.assertEqual(0, CORE.cmd_run(args))
        reconcile.assert_called_once_with(do_commit=False, push=False)
        connection = sqlite3.connect(self.database)
        self.assertEqual(
            1, connection.execute("SELECT count(*) FROM command_results").fetchone()[0]
        )
        connection.close()

    def test_selector_rejects_malformed_unknown_and_mismatched_values(self) -> None:
        self.configure_core()
        for value in (
            "not-json",
            "{}",
            json.dumps(
                {"schema_version": 1, "project_id": BINDING["project_id"], "backend": "remote"}
            ),
        ):
            CORE.BACKEND_CONFIG.write_text(value)
            with self.assertRaises(RuntimeError):
                CORE.backend_selection()
        CORE.BACKEND_CONFIG.write_text(
            json.dumps({"schema_version": 1, "project_id": "foreign", "backend": "git"})
        )
        with self.assertRaisesRegex(RuntimeError, "storage backend"):
            CORE._assert_storage_binding(BINDING)

    def test_migration_rejects_malformed_legacy_command_journal(self) -> None:
        self.configure_core()
        CORE.RUNTIME.mkdir(exist_ok=True)
        journal = CORE.RUNTIME / "command-results.jsonl"
        for value, message in (
            ("not-json\n", "line 1"),
            (json.dumps({"task": "AR-0001"}) + "\n", "line 1"),
        ):
            journal.write_text(value)
            with self.assertRaisesRegex(RuntimeError, message):
                CORE.legacy_command_results()

    def test_storage_binding_opens_bound_sqlite_database(self) -> None:
        self.configure_core(backend="sqlite")
        self.create()
        CORE._assert_storage_binding(BINDING)

    def test_sqlite_init_is_default_atomic_and_git_remains_opt_in(self) -> None:
        self.configure_core()
        CORE.PROJECT_CONFIG.unlink()
        CORE.BINDING.unlink()
        CORE.BACKEND_CONFIG.unlink()
        self.write_git_tasks()
        args = argparse.Namespace(
            state_repository="owner/state",
            product_repository="owner/product",
            project_name="test-project",
            project_title="Test Project",
            status_view=False,
            commit_signoff=False,
            backend="sqlite",
        )
        top = subprocess.CompletedProcess([], 0, str(self.root) + "\n", "")
        with (
            patch.object(CORE, "run", return_value=top),
            patch.object(CORE, "git_repository_slug", return_value="owner/state"),
            patch.object(CORE.Path, "cwd", return_value=self.root),
            patch.object(CORE.uuid, "uuid4", return_value=CORE.uuid.UUID(BINDING["project_id"])),
            patch("builtins.print"),
        ):
            CORE.cmd_init(args)
        self.assertEqual("sqlite", CORE.backend_selection()["backend"])
        self.assertTrue(self.database.is_file())

    def test_sqlite_init_failure_restores_all_binding_files(self) -> None:
        self.configure_core()
        CORE.PROJECT_CONFIG.unlink()
        CORE.BINDING.unlink()
        CORE.BACKEND_CONFIG.unlink()
        bad = task("AR-0001")
        bad[1]["title"] = ""
        self.write_git_tasks([bad])
        args = argparse.Namespace(
            state_repository="owner/state",
            product_repository="owner/product",
            project_name="test-project",
            project_title="Test Project",
            status_view=False,
            commit_signoff=False,
            backend="sqlite",
        )
        top = subprocess.CompletedProcess([], 0, str(self.root) + "\n", "")
        with (
            patch.object(CORE, "run", return_value=top),
            patch.object(CORE, "git_repository_slug", return_value="owner/state"),
            patch.object(CORE.Path, "cwd", return_value=self.root),
            self.assertRaisesRegex(RuntimeError, "initial task import"),
        ):
            CORE.cmd_init(args)
        self.assertFalse(CORE.PROJECT_CONFIG.exists())
        self.assertFalse(CORE.BINDING.exists())
        self.assertFalse(CORE.BACKEND_CONFIG.exists())
        self.assertFalse(self.database.exists())

    def test_reconcile_publication_is_optional_bounded_and_ordered(self) -> None:
        self.configure_core(backend="sqlite")
        tracked = task("AR-0001")
        tracked[1]["worktree_key"] = "worker-1"
        backend = self.create([tracked])
        CORE.RUNTIME.mkdir(exist_ok=True)
        CORE.CONFIG.write_text('{"github_repository": "owner/product"}')
        state: dict[str, Any] = {
            "remote_main": "a" * 40,
            "origin_main": "a" * 40,
            "primary_head": "b" * 40,
            "worktrees": [
                {
                    "key": "worker-1",
                    "branch": "feature/test",
                    "head": "c" * 40,
                    "dirty": True,
                    "paths": ["safe/path.py"],
                    "behind": 0,
                    "ahead": 1,
                }
            ],
            "prs": [],
            "runs": [],
        }
        with (
            patch.object(CORE, "project_scan", return_value=state),
            patch.object(CORE, "commit", return_value=True) as commit,
            patch.object(CORE, "push_replica") as push,
        ):
            self.assertTrue(CORE.reconcile(do_commit=True, push=True))
        commit.assert_called_once()
        push.assert_called_once()
        observed = backend.load_tasks()[0][1]
        self.assertEqual(observed["observed_branch"], "feature/test")
        self.assertEqual(observed["observed_head"], "c" * 40)
        self.assertTrue(observed["observed_dirty"])
        self.assertEqual(observed["task_revision"], 2)
        self.assertIn("feature/test", (self.tasks / tracked[0]).read_text())
        backend.update_observations(
            {"worker-1": state["worktrees"][0]}, "2026-09-08T00:02:00+00:00"
        )
        self.assertEqual(
            backend.load_tasks()[0][1]["task_revision"], 2, "identical scans must be idempotent"
        )
        with self.assertRaisesRegex(RuntimeError, "requires --commit"):
            CORE.reconcile(do_commit=False, push=True)

    def test_projection_removes_non_authoritative_task_and_reports_invalid_view(self) -> None:
        self.configure_core(backend="sqlite")
        self.create()
        stale = self.tasks / "AR-9999-stale.md"
        stale.write_text("stale")
        CORE.export_sqlite_projections()
        self.assertFalse(stale.exists())
        with (
            patch.object(CORE, "validate", return_value=["injected"]),
            self.assertRaisesRegex(RuntimeError, "projection validation"),
        ):
            CORE.export_sqlite_projections()

    def test_sqlite_negative_open_and_mountinfo_paths(self) -> None:
        missing = SQLiteBackend(self.root / "missing.sqlite3", BINDING, self.tasks)
        with self.assertRaisesRegex(RuntimeError, "SQLITE_MISSING"):
            missing.load_tasks()
        link = self.root / "link.sqlite3"
        link.symlink_to(self.database)
        with self.assertRaisesRegex(RuntimeError, "symlink"):
            SQLiteBackend(link, BINDING, self.tasks).load_tasks()
        require_local_filesystem(self.database, "malformed line")

    def test_disk_full_read_only_and_io_errors_have_stable_classifications(self) -> None:
        cases = (
            (sqlite3.SQLITE_FULL, "SQLITE_STORAGE_FULL"),
            (sqlite3.SQLITE_READONLY, "SQLITE_READ_ONLY"),
            (sqlite3.SQLITE_IOERR, "SQLITE_IO_ERROR"),
        )
        for code, classification in cases:
            error = sqlite3.OperationalError("injected")
            error.sqlite_errorcode = code
            self.assertIn(classification, str(_translate(error)))

    def test_retired_backend_rejects_stale_process_connections(self) -> None:
        backend = self.create()
        projected: list[str] = []
        backend.retire(
            lambda tasks: projected.extend(item[1]["id"] for item in tasks), lambda: None
        )
        self.assertEqual(["AR-0001"], projected)
        with self.assertRaisesRegex(RuntimeError, "BACKEND_INACTIVE"):
            backend.load_tasks()

    def test_git_writer_waiting_across_backend_switch_is_fenced(self) -> None:
        self.configure_core(backend="git")
        self.write_git_tasks()
        with (
            patch.object(
                CORE, "backend_selection", side_effect=[{"backend": "git"}, {"backend": "sqlite"}]
            ),
            self.assertRaisesRegex(RuntimeError, "BACKEND_CHANGED"),
        ):
            CORE.mutate(
                argparse.Namespace(task="AR-0001", owner="worker", lease_minutes=10), "claim"
            )
        self.assertEqual("open", CORE.git_tasks()[0][1]["status"])


if __name__ == "__main__":
    unittest.main()
