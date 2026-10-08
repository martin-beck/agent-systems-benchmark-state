# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""SQLite backend conformance, fault and real multiprocess tests."""

import argparse
import importlib.util
import json
import multiprocessing
import os
import signal
import sqlite3
import subprocess
import sys
import time
import unittest
from collections.abc import Callable
from contextlib import closing
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Any, Literal
from unittest.mock import patch

from fixture_ids import project_uuid

from tools.sqlite_storage import (
    SQLiteAuthorityBinding,
    SQLiteBackend,
    StorageContentionError,
    _translate,
    create_database,
    require_local_filesystem,
)

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / "tools"
sys.path.insert(0, str(TOOLS))

SPEC = importlib.util.spec_from_file_location("handoffctl_sqlite_test", TOOLS / "handoffctl.py")
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load handoffctl")
CORE: Any = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CORE)

BINDING = {
    "schema_version": 1,
    "project_id": project_uuid("1"),
    "state_repository": "owner/state",
    "product_repository": "owner/product",
}


# Diagnostic only: terminate an authority writer after an uncommitted WAL
# update and verify that SQLite reopens the prior durable state. This does not
# claim barrier admission, authority-route fencing, or formal refinement.
_CRASHING_AUTHORITY_SCRIPT = r"""
import os
import signal
import sqlite3
import sys
from pathlib import Path

database = Path(sys.argv[1])
ready = database.with_name(database.name + ".ready")
connection = sqlite3.connect(database)
connection.execute("PRAGMA journal_mode=WAL")
connection.execute("BEGIN IMMEDIATE")
connection.execute(
    "UPDATE tasks SET body=?, revision=revision+1 WHERE id=?",
    ("# crashed before commit\n", "AR-0001"),
)
ready.write_text("uncommitted-wal\n", encoding="utf-8")
with ready.open("rb") as stream:
    os.fsync(stream.fileno())
os.kill(os.getpid(), signal.SIGKILL)
"""


def _commit_then_crash_before_projection(database: str, tasks_root: str) -> None:
    """Commit the SQLite CAS, then die before disposable projections are written."""
    CORE.DATABASE = Path(database)
    CORE.TASKS = Path(tasks_root)
    arguments = argparse.Namespace(task="AR-0001", owner="worker", lease_minutes=10)

    def crash(*_args: object, **_kwargs: object) -> None:
        os.kill(os.getpid(), signal.SIGKILL)

    with patch.object(CORE, "export_sqlite_projections", side_effect=crash):
        CORE.mutate(arguments, "claim")


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


def sqlite_unblock_worker(start: Any, outcomes: Any) -> None:
    """Race the supported external unblock against one SQLite authority."""
    start.wait(5)
    try:
        CORE.mutate(
            argparse.Namespace(task="AR-0001", expected_revision=1, note="external clear"),
            "unblock",
        )
    except RuntimeError as error:
        outcomes.put(("rejected", str(error)))
    else:
        outcomes.put(("accepted", "open"))


def sqlite_resume_worker(start: Any, outcomes: Any) -> None:
    """Race the supported paused resume against one SQLite authority."""
    start.wait(5)
    try:
        CORE.mutate(
            argparse.Namespace(
                task="AR-0001",
                expected_revision=1,
                session="AR-0001@1",
                note="resume",
            ),
            "resume",
        )
    except RuntimeError as error:
        outcomes.put(("rejected", str(error)))
    else:
        outcomes.put(("accepted", "open"))


class SQLiteStorageTest(unittest.TestCase):
    def test_authority_sidecar_descriptor_failures_are_fail_closed(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            root.chmod(0o700)
            authority = root / "authority.sqlite"
            authority.write_bytes(b"authority")
            parent = os.open(root, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
            try:
                with self.assertRaisesRegex(RuntimeError, "sidecar is unavailable"):
                    SQLiteAuthorityBinding._open_retained(parent, "missing-wal", "sidecar")

                hardlink_source = root / "hardlink-source"
                hardlink_source.write_bytes(b"unsafe")
                os.link(hardlink_source, root / "unsafe-wal")
                with self.assertRaisesRegex(RuntimeError, "sidecar is unsafe"):
                    SQLiteAuthorityBinding._open_retained(parent, "unsafe-wal", "sidecar")

                retained = root / "retained-wal"
                retained.write_bytes(b"retained")
                retained.chmod(0o600)
                descriptor, identity = SQLiteAuthorityBinding._open_retained(
                    parent, retained.name, "sidecar"
                )
                try:
                    retained.unlink()
                    with self.assertRaisesRegex(RuntimeError, "sidecar is unavailable"):
                        SQLiteAuthorityBinding._assert_retained(
                            parent, retained.name, descriptor, identity, "sidecar"
                        )
                    retained.write_bytes(b"replacement")
                    retained.chmod(0o600)
                    with self.assertRaisesRegex(RuntimeError, "sidecar identity changed"):
                        SQLiteAuthorityBinding._assert_retained(
                            parent, retained.name, descriptor, identity, "sidecar"
                        )
                    retained.chmod(0o644)
                    with self.assertRaisesRegex(RuntimeError, "sidecar identity changed"):
                        SQLiteAuthorityBinding._assert_retained(
                            parent, retained.name, descriptor, identity, "sidecar"
                        )
                finally:
                    os.close(descriptor)

                with self.assertRaisesRegex(RuntimeError, "sidecar is unavailable"):
                    SQLiteAuthorityBinding._open_sidecar_set(parent, authority)
            finally:
                os.close(parent)

    def test_retained_authority_parent_identity_rejects_ancestor_replacement(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            authority = root / "authority.sqlite"
            authority.write_bytes(b"authority")
            parent = root.stat()
            with self.assertRaisesRegex(RuntimeError, "parent identity changed"):
                SQLiteAuthorityBinding._assert_parent_identity(
                    authority, (parent.st_dev, parent.st_ino), (parent.st_dev, parent.st_ino + 1)
                )

    def setUp(self) -> None:
        self.temporary = TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.tasks = self.root / "tasks"
        self.tasks.mkdir()
        self.database = self.root / ".runtime/coordinator.sqlite3"

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def create(
        self,
        tasks: list[Any] | None = None,
        *,
        session_records: list[dict[str, Any]] | None = None,
    ) -> SQLiteBackend:
        create_database(
            self.database,
            BINDING,
            tasks or [task("AR-0001")],
            imported_at="2026-09-08T00:00:00+00:00",
            source_backend="git",
            source_checkpoint="a" * 40,
            session_records=session_records or (),
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
        CORE.CONTROL_DATABASE = CORE.RUNTIME / "coordinator.control.sqlite3"
        CORE.AUTHORITY_MARKER = CORE.RUNTIME / "coordinator.authority-marker.json"
        CORE.AUTHORITY_LIFECYCLE = CORE.RUNTIME / "coordinator.authority-lifecycle.json"
        CORE.AUTHORITY_LOCK = CORE.RUNTIME / "coordinator.authority.lock"
        CORE.CONTROL_BINDING = CORE.RUNTIME / "coordinator.control-binding.json"
        CORE.CONTROL_LOCK = CORE.RUNTIME / ".coordinator.control.sqlite3.lock"
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

    def enable_additive_policy(self) -> bytes:
        """Commit the supported project policy in this backend fixture."""
        payload = (
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
            + "\n"
        ).encode()
        (self.root / "task-spec-policy.json").write_bytes(payload)
        subprocess.run(  # noqa: S603
            ["/usr/bin/git", "init", "-q", str(self.root)], check=True
        )
        subprocess.run(  # noqa: S603
            ["/usr/bin/git", "-C", str(self.root), "add", "task-spec-policy.json"],
            check=True,
        )
        subprocess.run(  # noqa: S603
            [
                "/usr/bin/git",
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
            check=True,
        )
        return payload

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

    def test_authority_writer_death_rolls_back_uncommitted_wal_update(self) -> None:
        """Diagnostic SQLite WAL rollback only; no fencing or refinement claim."""
        backend = self.create()
        ready = self.database.with_name(self.database.name + ".ready")
        process = subprocess.Popen(  # noqa: S603 - fixed interpreter and test script
            [sys.executable, "-c", _CRASHING_AUTHORITY_SCRIPT, str(self.database)],
            cwd=ROOT,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        try:
            deadline = time.monotonic() + 10
            while not ready.exists() and time.monotonic() < deadline:
                if process.poll() is not None:
                    stdout, stderr = process.communicate()
                    self.fail(
                        f"authority crash fixture exited early: {process.returncode}; "
                        f"stdout={stdout!r}; stderr={stderr!r}"
                    )
                time.sleep(0.01)
            self.assertTrue(ready.exists(), "authority crash fixture did not reach WAL checkpoint")
            self.assertEqual("uncommitted-wal", ready.read_text(encoding="utf-8").strip())
            self.assertEqual(-signal.SIGKILL, process.wait(timeout=10))
            stdout, stderr = process.communicate()
            self.assertEqual("", stdout)
            self.assertEqual("", stderr)
        finally:
            if process.poll() is None:
                process.kill()
            process.communicate(timeout=5)

        task_row = next(item for item in backend.load_tasks() if item[1]["id"] == "AR-0001")
        self.assertEqual(1, task_row[1]["task_revision"])
        self.assertEqual("# Test\n", task_row[2])
        self.assertEqual([], backend.integrity_errors())

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

    def test_every_write_route_enters_fence_before_sqlite_mutation(self) -> None:
        ordinary = self.create()

        class RejectScope:
            def __enter__(self) -> None:
                raise RuntimeError("mutation fence rejected")

            def __exit__(self, *_args: object) -> Literal[False]:
                return False

        def reject_scope() -> RejectScope:
            return RejectScope()

        fenced = SQLiteBackend(
            self.database,
            BINDING,
            self.tasks,
            mutation_scope=reject_scope,
        )

        def transition(meta: dict[str, Any], _tasks: list[Any]) -> tuple[str, str]:
            meta["summary"] = "must not commit"
            return "update", "must not commit"

        routes: tuple[Callable[[], None], ...] = (
            lambda: fenced.mutate("AR-0001", 1, "update", "2026-09-08T00:01:00+00:00", transition),
            lambda: fenced.update_observations(
                {"": {"branch": "main", "head": "a" * 40, "dirty": False}},
                "2026-09-08T00:01:00+00:00",
            ),
            lambda: fenced.append_command_result(
                "AR-0001", "worker", "a" * 64, 0, "EXIT", "2026-09-08T00:01:00+00:00"
            ),
            lambda: fenced.retire(lambda _tasks: None, lambda: None),
        )
        for route in routes:
            with self.assertRaisesRegex(RuntimeError, "mutation fence rejected"):
                route()
        self.assertEqual(1, ordinary.load_tasks()[0][1]["task_revision"])
        connection = sqlite3.connect(self.database)
        self.assertEqual(
            0, connection.execute("SELECT count(*) FROM command_results").fetchone()[0]
        )
        self.assertEqual(
            "active",
            connection.execute("SELECT value FROM metadata WHERE key='state'").fetchone()[0],
        )
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

    def test_additive_policy_migrates_and_policy_removal_or_race_is_atomic(self) -> None:
        self.configure_core()
        payload = self.enable_additive_policy()
        path, meta, body = task("AR-0001")
        spec = json.loads(
            (
                Path(__file__).resolve().parents[1] / "examples/task-specs/downstream-additive.json"
            ).read_text(encoding="utf-8")
        )
        spec["spec_ref"] = "spec.json"
        (self.root / "spec.json").write_text(json.dumps(spec) + "\n", encoding="utf-8")
        meta.update(spec_ref="spec.json", spec_revision=1)
        self.write_git_tasks([(path, meta, body)])
        completed = subprocess.CompletedProcess([], 0, "b" * 40 + "\n", "")
        with (
            patch.object(CORE, "sync_replica_before_write"),
            patch.object(CORE, "run", return_value=completed),
            patch("builtins.print"),
        ):
            CORE.cmd_migrate(argparse.Namespace(to="sqlite"))
        self.assertEqual("sqlite", CORE.backend_selection()["backend"])
        self.assertEqual([], CORE.validate())

        (self.root / "task-spec-policy.json").unlink()
        with self.assertRaisesRegex(RuntimeError, "tracked and unchanged"):
            CORE.cmd_migrate(argparse.Namespace(to="git"))
        self.assertEqual("sqlite", CORE.backend_selection()["backend"])
        (self.root / "task-spec-policy.json").write_bytes(payload)
        with patch("builtins.print"):
            CORE.cmd_migrate(argparse.Namespace(to="git"))
        self.assertEqual("git", CORE.backend_selection()["backend"])

        with (
            patch.object(CORE, "sync_replica_before_write"),
            patch.object(CORE, "run", return_value=completed),
            patch.object(
                CORE,
                "require_policy_unchanged",
                side_effect=[None, RuntimeError("task-spec policy changed during operation")],
            ),
            self.assertRaisesRegex(RuntimeError, "policy changed during operation"),
        ):
            CORE.cmd_migrate(argparse.Namespace(to="sqlite"))
        self.assertEqual("git", CORE.backend_selection()["backend"])
        self.assertFalse(CORE.DATABASE.exists())

    def test_git_to_sqlite_a_b_a_policy_swap_has_no_backend_effect(self) -> None:
        self.configure_core()
        original_payload = self.enable_additive_policy()
        self.write_git_tasks()
        policy_path = self.root / "task-spec-policy.json"
        original_check = CORE.require_policy_unchanged
        checks = 0

        def a_b_a_check(root: Path, expected: Any) -> None:
            nonlocal checks
            checks += 1
            if checks > 1:
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

        with (
            patch.object(CORE, "sync_replica_before_write"),
            patch.object(CORE, "require_policy_unchanged", side_effect=a_b_a_check),
            self.assertRaisesRegex(RuntimeError, "changed during operation"),
        ):
            CORE.cmd_migrate(argparse.Namespace(to="sqlite"))
        self.assertEqual("git", CORE.backend_selection()["backend"])
        self.assertFalse(CORE.DATABASE.exists())
        self.assertEqual(original_payload, policy_path.read_bytes())

    def test_policy_migration_preflight_and_equivalence_failures_are_atomic(self) -> None:
        self.configure_core()
        self.enable_additive_policy()
        self.write_git_tasks()
        completed = subprocess.CompletedProcess([], 0, "b" * 40 + "\n", "")
        with (
            patch.object(CORE, "sync_replica_before_write"),
            patch.object(CORE, "validate", return_value=["injected invalid policy state"]),
            self.assertRaisesRegex(RuntimeError, "migration preflight failed"),
        ):
            CORE.cmd_migrate(argparse.Namespace(to="sqlite"))
        self.assertEqual("git", CORE.backend_selection()["backend"])
        self.assertFalse(CORE.DATABASE.exists())

        with (
            patch.object(CORE, "sync_replica_before_write"),
            patch.object(CORE, "run", return_value=completed),
            patch.object(CORE.SQLiteBackend, "load_tasks", return_value=[]),
            self.assertRaisesRegex(RuntimeError, "migration equivalence check failed"),
        ):
            CORE.cmd_migrate(argparse.Namespace(to="sqlite"))
        self.assertEqual("git", CORE.backend_selection()["backend"])
        self.assertFalse(CORE.DATABASE.exists())

        with (
            patch.object(CORE, "sync_replica_before_write"),
            patch.object(CORE, "run", return_value=completed),
            patch.object(CORE.SQLiteBackend, "load_session_records", return_value=[{}]),
            self.assertRaisesRegex(RuntimeError, "record migration equivalence check failed"),
        ):
            CORE.cmd_migrate(argparse.Namespace(to="sqlite"))
        self.assertEqual("git", CORE.backend_selection()["backend"])
        self.assertFalse(CORE.DATABASE.exists())

        with (
            patch.object(CORE, "sync_replica_before_write"),
            patch.object(CORE, "run", return_value=completed),
            patch("builtins.print"),
        ):
            CORE.cmd_migrate(argparse.Namespace(to="sqlite"))
        with (
            patch.object(CORE, "write_sqlite_projections"),
            patch.object(CORE, "validate", return_value=["injected rollback validation"]),
            self.assertRaisesRegex(RuntimeError, "rollback export failed"),
        ):
            CORE.cmd_migrate(argparse.Namespace(to="git"))
        self.assertEqual("sqlite", CORE.backend_selection()["backend"])

    def test_policy_sqlite_mutation_validation_and_unknown_task_are_atomic(self) -> None:
        self.configure_core(backend="sqlite")
        self.enable_additive_policy()
        active = task("AR-0001", status="in_progress")
        active[1].update(owner="worker-a", claim_expires="2099-01-01T00:00:00+00:00")
        self.create([active])
        with self.assertRaisesRegex(RuntimeError, "unknown task"):
            CORE.mutate_sqlite(argparse.Namespace(task="AR-9999", expected_revision=1), "update")
        before = SQLiteBackend(self.database, BINDING, self.tasks).load_tasks()[0][1]
        args = argparse.Namespace(
            task="AR-0001",
            owner="worker-a",
            expected_revision=1,
            status=None,
            priority=None,
            summary=None,
            next_action="changed",
            note="validation fault",
        )
        with (
            patch.object(CORE, "basic_task_errors", return_value=["injected spec error"]),
            self.assertRaisesRegex(RuntimeError, "transition validation failed"),
        ):
            CORE.mutate_sqlite(args, "update")
        self.assertEqual(
            before, SQLiteBackend(self.database, BINDING, self.tasks).load_tasks()[0][1]
        )

    def test_migration_preserves_hierarchy_session_and_checkpoint_records(self) -> None:
        self.configure_core()
        parent = task("AR-0001")
        child = task("AR-0002")
        parent[1]["children"] = ["AR-0002"]
        child[1]["parent_task_ref"] = "AR-0001"
        self.write_git_tasks([parent, child])
        CORE.append_session_record(
            self.root,
            CORE.build_session_record(parent[1], "update", "2026-09-08T00:02:00+00:00"),
        )
        CORE.append_checkpoint(
            self.root,
            CORE.build_checkpoint(parent[1], parent[2], "a" * 40, "2026-09-08T00:03:00+00:00"),
        )
        with (
            patch.object(CORE, "sync_replica_before_write"),
            patch.object(
                CORE,
                "run",
                return_value=subprocess.CompletedProcess([], 0, "b" * 40 + "\n", ""),
            ),
            patch("builtins.print"),
        ):
            CORE.cmd_migrate(argparse.Namespace(to="sqlite"))
        backend = SQLiteBackend(self.database, BINDING, self.tasks)
        self.assertEqual(["AR-0002"], backend.load_tasks()[0][1]["children"])
        self.assertEqual(1, len(backend.load_session_records()))
        self.assertEqual(1, len(backend.load_checkpoint_records()))
        with patch("builtins.print"):
            CORE.cmd_migrate(argparse.Namespace(to="git"))
        self.assertEqual(1, len(CORE.storage_backend().load_session_records()))
        self.assertEqual(1, len(CORE.storage_backend().load_checkpoint_records()))

    def test_external_blocked_provenance_survives_migration_round_trip(self) -> None:
        self.configure_core()
        external = task("AR-0001", status="in_progress")
        external[1].update(
            owner="worker-a",
            claim_expires="2099-01-01T00:00:00+00:00",
            next_action="Wait for external dependency.",
        )
        self.write_git_tasks([external])
        with (
            patch.object(CORE, "sync_replica_before_write"),
            patch.object(CORE, "commit", return_value=True),
        ):
            CORE.mutate(
                argparse.Namespace(
                    task="AR-0001", owner="worker-a", status="blocked", note="external wait"
                ),
                "release",
            )
        completed = subprocess.CompletedProcess([], 0, "b" * 40 + "\n", "")
        with (
            patch.object(CORE, "sync_replica_before_write"),
            patch.object(CORE, "run", return_value=completed),
            patch("builtins.print"),
        ):
            CORE.cmd_migrate(argparse.Namespace(to="sqlite"))
        CORE.mutate(
            argparse.Namespace(task="AR-0001", expected_revision=2, note="external clear"),
            "unblock",
        )
        with patch("builtins.print"):
            CORE.cmd_migrate(argparse.Namespace(to="git"))
        restored = CORE.git_tasks()[0][1]
        self.assertEqual(("open", 3), (restored["status"], restored["task_revision"]))
        self.assertEqual("Wait for external dependency.", restored["next_action"])
        self.assertEqual([], CORE.storage_backend().load_session_records("AR-0001"))

    def test_sqlite_cli_lifecycle_uses_same_transition_contract(self) -> None:
        self.configure_core(backend="sqlite")
        task_path, task_meta, task_body = task("AR-0001")
        task_meta.update(
            {
                "spec_ref": "spec.json",
                "spec_revision": 1,
                "spec_acceptance": {
                    "spec_ref": "spec.json",
                    "spec_revision": 1,
                    "status": "pass",
                    "evidence_class": "contract-test",
                    "evidence_ref": "awq/evidence/AR-0001",
                    "evidence_digest": "sha256:" + "c" * 64,
                },
            }
        )
        self.create([(task_path, task_meta, task_body)])
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

    def test_sqlite_release_blocked_unblock_and_claim_is_session_free(self) -> None:
        self.configure_core(backend="sqlite")
        task_path, task_meta, task_body = task("AR-0001", status="in_progress")
        task_meta.update(
            owner="worker-a",
            claim_expires="2099-01-01T00:00:00+00:00",
            next_action="Wait for external dependency.",
        )
        backend = self.create([(task_path, task_meta, task_body)])
        CORE.export_sqlite_projections()
        with patch.object(CORE, "push_replica"):
            CORE.mutate(
                argparse.Namespace(
                    task="AR-0001", owner="worker-a", status="blocked", note="external wait"
                ),
                "release",
            )
            CORE.mutate(
                argparse.Namespace(task="AR-0001", expected_revision=2, note="external clear"),
                "unblock",
            )
            CORE.mutate(
                argparse.Namespace(task="AR-0001", owner="worker-b", lease_minutes=10),
                "claim",
            )
        final = backend.load_tasks()[0][1]
        self.assertEqual(("in_progress", 4), (final["status"], final["task_revision"]))
        self.assertEqual("Wait for external dependency.", final["next_action"])
        self.assertEqual([], backend.load_session_records("AR-0001"))
        with closing(sqlite3.connect(self.database)) as connection:
            self.assertEqual(
                ["import", "release", "unblock", "claim"],
                [row[0] for row in connection.execute("SELECT kind FROM events ORDER BY revision")],
            )

    def test_sqlite_unique_pause_resume_restores_next_action(self) -> None:
        self.configure_core(backend="sqlite")
        task_path, task_meta, task_body = task("AR-0001", status="in_progress")
        task_meta.update(
            owner="worker-a",
            claim_expires="2099-01-01T00:00:00+00:00",
            next_action="Resume this exact step.",
        )
        backend = self.create([(task_path, task_meta, task_body)])
        CORE.export_sqlite_projections()
        with patch.object(CORE, "push_replica"):
            CORE.mutate(
                argparse.Namespace(
                    task="AR-0001", owner="worker-a", expected_revision=1, note="pause"
                ),
                "pause",
            )
            CORE.mutate(
                argparse.Namespace(
                    task="AR-0001",
                    expected_revision=2,
                    session="AR-0001@2",
                    note="resume",
                ),
                "resume",
            )
        final = backend.load_tasks()[0][1]
        self.assertEqual(("open", 3), (final["status"], final["task_revision"]))
        self.assertEqual("Resume this exact step.", final["next_action"])

    def test_sqlite_resume_projection_failure_keeps_committed_authority(self) -> None:
        self.configure_core(backend="sqlite")
        blocked = task("AR-0001", status="blocked")
        backend = self.create(
            [blocked],
            session_records=[
                CORE.build_session_record(blocked[1], "pause", "2026-10-08T00:00:00+00:00")
            ],
        )
        CORE.export_sqlite_projections()
        with (
            patch.object(CORE, "export_sqlite_projections", side_effect=OSError(28, "disk full")),
            self.assertRaisesRegex(CORE.StorageCommittedError, "SQLITE_COMMITTED_EXPORT_FAILED"),
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
        committed = backend.load_tasks()[0][1]
        self.assertEqual(("open", 2), (committed["status"], committed["task_revision"]))
        self.assertIn('"status": "blocked"', (self.tasks / "AR-0001-test.md").read_text())

    def test_sqlite_unblock_projection_failure_keeps_committed_authority(self) -> None:
        self.configure_core(backend="sqlite")
        backend = self.create([task("AR-0001", status="blocked")])
        CORE.export_sqlite_projections()
        with (
            patch.object(CORE, "export_sqlite_projections", side_effect=OSError(28, "disk full")),
            self.assertRaisesRegex(CORE.StorageCommittedError, "SQLITE_COMMITTED_EXPORT_FAILED"),
        ):
            CORE.mutate(
                argparse.Namespace(task="AR-0001", expected_revision=1, note="external clear"),
                "unblock",
            )
        committed = backend.load_tasks()[0][1]
        self.assertEqual(("open", 2), (committed["status"], committed["task_revision"]))
        self.assertIn('"status": "blocked"', (self.tasks / "AR-0001-test.md").read_text())
        CORE.export_sqlite_projections()
        self.assertIn('"status": "open"', (self.tasks / "AR-0001-test.md").read_text())

    def test_parallel_sqlite_unblocks_have_one_exact_revision_winner(self) -> None:
        self.configure_core(backend="sqlite")
        backend = self.create([task("AR-0001", status="blocked")])
        CORE.export_sqlite_projections()
        context = multiprocessing.get_context("fork")
        start = context.Event()
        outcomes: Any = context.Queue()
        workers = [
            context.Process(target=sqlite_unblock_worker, args=(start, outcomes)) for _ in range(2)
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
        final = backend.load_tasks()[0][1]
        self.assertEqual(("open", 2), (final["status"], final["task_revision"]))
        self.assertEqual([], backend.load_session_records("AR-0001"))

    def test_parallel_sqlite_resumes_have_one_exact_revision_winner(self) -> None:
        self.configure_core(backend="sqlite")
        blocked = task("AR-0001", status="blocked")
        backend = self.create(
            [blocked],
            session_records=[
                CORE.build_session_record(blocked[1], "pause", "2026-10-08T00:00:00+00:00")
            ],
        )
        CORE.export_sqlite_projections()
        context = multiprocessing.get_context("fork")
        start = context.Event()
        outcomes: Any = context.Queue()
        workers = [
            context.Process(target=sqlite_resume_worker, args=(start, outcomes)) for _ in range(2)
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
        final = backend.load_tasks()[0][1]
        self.assertEqual(("open", 2), (final["status"], final["task_revision"]))

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

    def test_process_death_after_commit_before_projection_reconciles_from_authority(self) -> None:
        self.configure_core(backend="sqlite")
        backend = self.create()
        CORE.export_sqlite_projections()
        process = multiprocessing.get_context("fork").Process(
            target=_commit_then_crash_before_projection,
            args=(str(self.database), str(self.tasks)),
        )
        process.start()
        process.join(timeout=10)
        self.assertEqual(-signal.SIGKILL, process.exitcode)
        self.assertFalse(process.is_alive())

        committed = next(item for item in backend.load_tasks() if item[1]["id"] == "AR-0001")
        self.assertEqual(
            ("in_progress", 2), (committed[1]["status"], committed[1]["task_revision"])
        )
        stale_projection = (self.tasks / "AR-0001-test.md").read_text()
        self.assertIn('"status": "open"', stale_projection)
        CORE.export_sqlite_projections()
        reconciled = (self.tasks / "AR-0001-test.md").read_text()
        self.assertIn('"status": "in_progress"', reconciled)

    def test_sqlite_command_journal_snapshot_doctor_and_offline_reconcile(self) -> None:
        self.configure_core(backend="sqlite")
        self.create()
        self.assertEqual([], CORE.storage_backend().load_session_records())
        tasks = CORE.all_tasks()
        with patch.object(CORE, "storage_backend", return_value=CORE.GitBackend()):
            CORE.write_sqlite_projections(tasks)
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
        stale = self.root / "sessions/AR-9999.jsonl"
        stale.parent.mkdir()
        stale.write_text("stale\n")
        CORE.export_sqlite_projections()
        CORE.mutate(argparse.Namespace(task="AR-0001", owner="worker", lease_minutes=10), "claim")
        CORE.mutate(
            argparse.Namespace(
                task="AR-0001",
                owner="worker",
                expected_revision=2,
                source_commit="d" * 40,
            ),
            "checkpoint",
        )
        args = argparse.Namespace(
            task="AR-0001", owner="worker", timeout_seconds=5.0, command=["/bin/true"]
        )
        with patch.object(CORE, "reconcile", return_value=True) as reconcile:
            self.assertEqual(0, CORE.cmd_run(args))
        reconcile.assert_called_once_with(
            do_commit=False,
            push=False,
            policy=CORE.DEFAULT_EVIDENCE_POLICY,
        )
        connection = sqlite3.connect(self.database)
        self.assertEqual(
            1, connection.execute("SELECT count(*) FROM command_results").fetchone()[0]
        )
        self.assertEqual(
            (1, "run"),
            connection.execute(
                "SELECT count(*), json_extract(record_json, '$.trigger') FROM session_records"
            ).fetchone(),
        )
        self.assertEqual(
            (1, "d" * 40),
            connection.execute(
                "SELECT count(*), json_extract(record_json, '$.source_commit') "
                "FROM checkpoint_records"
            ).fetchone(),
        )
        self.assertTrue((self.root / "checkpoints/AR-0001.jsonl").exists())
        self.assertFalse(stale.exists())
        with patch("builtins.print"):
            CORE.cmd_snapshot("AR-0001")
        connection.close()

    def test_sqlite_session_record_reader_rejects_corrupt_rows(self) -> None:
        self.configure_core(backend="sqlite")
        self.create()
        connection = sqlite3.connect(self.database)
        connection.execute(
            "CREATE TABLE session_records(sequence INTEGER PRIMARY KEY, task_id TEXT, "
            "task_revision INTEGER, record_json TEXT, recorded_at TEXT)"
        )
        connection.execute("INSERT INTO session_records VALUES (1, 'AR-0001', 2, '[]', 'now')")
        connection.commit()
        connection.close()
        with self.assertRaisesRegex(RuntimeError, "invalid session record"):
            CORE.storage_backend().load_session_records()
        connection = sqlite3.connect(self.database)
        connection.execute("UPDATE session_records SET record_json='not-json'")
        connection.commit()
        connection.close()
        with self.assertRaisesRegex(RuntimeError, "invalid session JSON"):
            CORE.storage_backend().load_session_records()

    def test_sqlite_session_reader_rejects_semantic_identity_corruption(self) -> None:
        self.configure_core(backend="sqlite")
        backend = self.create()
        blocked = task("AR-0001", status="blocked")[1]
        record = CORE.build_session_record(blocked, "pause", "2026-10-08T00:00:00+00:00")
        connection = sqlite3.connect(self.database)
        connection.execute(
            """CREATE TABLE session_records(
               sequence INTEGER PRIMARY KEY, task_id TEXT, task_revision INTEGER,
               record_json TEXT, recorded_at TEXT)"""
        )
        connection.execute(
            "INSERT INTO session_records VALUES (1, 'AR-0001', 1, ?, 'now')",
            (json.dumps(dict(record, task="AR-0002")),),
        )
        connection.commit()
        with self.assertRaisesRegex(RuntimeError, "identity mismatch"):
            backend.load_session_records()
        incoherent = dict(record, step_state={"status": "open", "task_revision": 1})
        connection.execute(
            "UPDATE session_records SET record_json=?",
            (json.dumps(incoherent),),
        )
        connection.commit()
        connection.close()
        with self.assertRaisesRegex(RuntimeError, "invalid session record"):
            backend.load_session_records()

    def test_sqlite_duplicate_pause_resume_stutters_before_projection(self) -> None:
        self.configure_core(backend="sqlite")
        blocked = task("AR-0001", status="blocked")
        backend = self.create([blocked])
        CORE.export_sqlite_projections()
        record = CORE.build_session_record(blocked[1], "pause", "2026-10-08T00:00:00+00:00")
        connection = sqlite3.connect(self.database)
        connection.execute(
            """CREATE TABLE session_records(
               sequence INTEGER PRIMARY KEY, task_id TEXT, task_revision INTEGER,
               record_json TEXT, recorded_at TEXT)"""
        )
        payload = json.dumps(record, sort_keys=True, separators=(",", ":"))
        connection.executemany(
            "INSERT INTO session_records VALUES (?, 'AR-0001', 1, ?, 'now')",
            [(1, payload), (2, payload)],
        )
        connection.commit()
        connection.close()
        task_before = backend.load_tasks()[0][1]
        projection_before = (self.tasks / "AR-0001-test.md").read_bytes()
        with (
            patch.object(CORE, "export_sqlite_projections") as export,
            self.assertRaisesRegex(RuntimeError, "ambiguous"),
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
        self.assertEqual(task_before, backend.load_tasks()[0][1])
        self.assertEqual(projection_before, (self.tasks / "AR-0001-test.md").read_bytes())
        export.assert_not_called()

    def test_sqlite_boolean_pause_revision_stutters_before_projection(self) -> None:
        self.configure_core(backend="sqlite")
        blocked = task("AR-0001", status="blocked")
        backend = self.create([blocked])
        CORE.export_sqlite_projections()
        record = CORE.build_session_record(blocked[1], "pause", "2026-10-08T00:00:00+00:00")
        record.update(
            task_revision=True,
            step_state={"status": "blocked", "task_revision": True},
        )
        connection = sqlite3.connect(self.database)
        connection.execute(
            """CREATE TABLE session_records(
               sequence INTEGER PRIMARY KEY, task_id TEXT, task_revision INTEGER,
               record_json TEXT, recorded_at TEXT)"""
        )
        connection.execute(
            "INSERT INTO session_records VALUES (?, ?, ?, ?, ?)",
            (
                1,
                "AR-0001",
                1,
                json.dumps(record, sort_keys=True, separators=(",", ":")),
                "now",
            ),
        )
        connection.commit()
        connection.close()
        task_before = backend.load_tasks()[0][1]
        projection = self.tasks / "AR-0001-test.md"
        projection_before = projection.read_bytes()
        with (
            patch.object(CORE, "export_sqlite_projections") as export,
            self.assertRaisesRegex(RuntimeError, "invalid session record"),
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
        self.assertEqual(task_before, backend.load_tasks()[0][1])
        self.assertEqual(projection_before, projection.read_bytes())
        export.assert_not_called()

    def test_sqlite_session_reader_translates_unexpected_database_errors(self) -> None:
        self.configure_core(backend="sqlite")
        self.create()

        class BrokenConnection:
            def execute(self, _query: str, _parameters: tuple[object, ...] = ()) -> Any:
                raise sqlite3.OperationalError("database unavailable")

            def close(self) -> None:
                return None

        backend = CORE.storage_backend()
        with (
            patch.object(backend, "_connect", return_value=BrokenConnection()),
            self.assertRaisesRegex(RuntimeError, "database unavailable"),
        ):
            backend.load_session_records()

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

    def test_retire_selector_failure_rolls_back_database_state(self) -> None:
        backend = self.create()

        def fail_selector() -> None:
            raise RuntimeError("selector switch failed")

        with self.assertRaisesRegex(RuntimeError, "selector switch failed"):
            backend.retire(lambda _tasks: None, fail_selector)

        self.assertEqual("open", backend.load_tasks()[0][1]["status"])
        with closing(sqlite3.connect(self.database)) as connection, connection:
            self.assertEqual(
                "active",
                connection.execute("SELECT value FROM metadata WHERE key='state'").fetchone()[0],
            )

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
