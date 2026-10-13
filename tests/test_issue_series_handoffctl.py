# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Issue-series integration and contention coverage for handoffctl."""

import argparse
import importlib.util
import json
import multiprocessing
import sqlite3
import subprocess
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Any, cast
from unittest.mock import patch

from fixture_ids import project_uuid
from test_handoffctl import CORE, SOURCE, HandoffTest, configure_child, run_git


def install_secondary_controller() -> None:
    """Install another controller as discovery can do before forked workers run."""
    spec = importlib.util.spec_from_file_location("handoffctl_issue_series_secondary", SOURCE)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load secondary handoffctl controller")
    secondary = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(secondary)


def racing_issue_series_create(
    root_value: str, manifest_value: str, expected_digest: str, start: Any, outcomes: Any
) -> None:
    """Race one issue identity through independent local coordinator processes."""
    configure_child(root_value)
    CORE.coordinator_lock_path = lambda: CORE.LOCK
    CORE.sync_replica_before_write = lambda: None
    CORE.push_replica = lambda: None
    CORE.commit = lambda *_args, **_kwargs: True
    start.wait(10)
    try:
        CORE.cmd_issue_series_create(
            argparse.Namespace(manifest=Path(manifest_value), expected_state_digest=expected_digest)
        )
    except RuntimeError as error:
        outcomes.put(("rejected", str(error)))
    else:
        outcomes.put(("accepted", "created"))


def racing_real_issue_series_create(
    root_value: str, manifest_value: str, expected_digest: str, start: Any, outcomes: Any
) -> None:
    """Race the production Git commit/push path against one local bare remote."""
    configure_child(root_value)
    start.wait(10)
    try:
        CORE.cmd_issue_series_create(
            argparse.Namespace(manifest=Path(manifest_value), expected_state_digest=expected_digest)
        )
    except RuntimeError as error:
        outcomes.put(("rejected", str(error)))
    else:
        outcomes.put(("accepted", "created"))


def racing_sqlite_issue_series_create(
    root_value: str, manifest_value: str, expected_digest: str, start: Any, outcomes: Any
) -> None:
    """Race SQLite's authoritative whole-series transaction from separate processes."""
    configure_child(root_value)
    start.wait(10)
    try:
        CORE.cmd_issue_series_create(
            argparse.Namespace(manifest=Path(manifest_value), expected_state_digest=expected_digest)
        )
    except RuntimeError as error:
        outcomes.put(("rejected", str(error)))
    else:
        outcomes.put(("accepted", "created"))


class IssueSeriesHandoffTest(unittest.TestCase):
    """Reuse the shared handoff fixture without inheriting its test inventory."""

    def setUp(self) -> None:
        self.fixture = HandoffTest(methodName="run")
        self.fixture.setUp()

    def tearDown(self) -> None:
        self.fixture.tearDown()

    def __getattr__(self, name: str) -> Any:
        fixture = self.__dict__.get("fixture")
        if fixture is None:
            raise AttributeError(name)
        return getattr(fixture, name)

    def issue_series_manifest(self) -> Path:
        path = self.root / "series.json"
        path.write_text(
            json.dumps(
                {
                    "schema_version": 1,
                    "repository": "github.com/owner/product",
                    "issue": {
                        "number": 42,
                        "url": "https://github.com/owner/product/issues/42",
                    },
                    "issue_digest": "sha256:" + "a" * 64,
                    "members": [
                        {
                            "id": "AR-9000",
                            "short_title": "Create records",
                            "scope": "Create local series records",
                            "acceptance": "Focused local tests pass",
                            "ownership": "Coordinator core",
                            "depends_on": [],
                        },
                        {
                            "id": "AR-9001",
                            "short_title": "Qualify records",
                            "scope": "Qualify local series records",
                            "acceptance": "Local graph checks pass",
                            "ownership": "Coordinator core",
                            "depends_on": [{"id": "AR-9000", "rationale": "needs records"}],
                        },
                    ],
                    "finalizer": "AR-9001",
                }
            )
        )
        return cast(Path, path)

    def test_issue_series_create_is_atomic_and_stale_fenced(self) -> None:
        self.make_task()
        manifest = self.issue_series_manifest()
        digest = CORE.issue_series_state_digest(CORE.all_tasks())
        args = argparse.Namespace(manifest=manifest, expected_state_digest=digest)
        stale = argparse.Namespace(manifest=manifest, expected_state_digest="sha256:" + "b" * 64)
        with self.assertRaisesRegex(RuntimeError, "STALE_STATE"):
            CORE.cmd_issue_series_create(stale)
        self.assertEqual({"AR-0001"}, {meta["id"] for _path, meta, _body in CORE.all_tasks()})
        with patch.object(CORE, "commit", return_value=True) as commit:
            CORE.cmd_issue_series_create(args)
        created = {meta["id"]: meta for _path, meta, _body in CORE.all_tasks()}
        self.assertEqual({"AR-0001", "AR-9000", "AR-9001"}, set(created))
        self.assertEqual("AR-9001", created["AR-9000"]["parent_task_ref"])
        self.assertEqual(["AR-9000"], created["AR-9001"]["children"])
        self.assertEqual("Create records", created["AR-9000"]["short_title"])
        self.assertEqual(1, len(list((self.root / "issue-series").glob("*.json"))))
        commit.assert_called_once()
        before = (self.root / "CURRENT.md").read_text()
        with self.assertRaisesRegex(RuntimeError, "identifiers already exist"):
            CORE.cmd_issue_series_create(args)
        self.assertEqual(before, (self.root / "CURRENT.md").read_text())

    def test_optional_publication_is_local_idempotent_and_never_changes_tasks(self) -> None:
        self.make_task()
        manifest = self.issue_series_manifest()
        digest = CORE.issue_series_state_digest(CORE.all_tasks())
        with patch.object(CORE, "commit", return_value=True):
            CORE.cmd_issue_series_create(
                argparse.Namespace(manifest=manifest, expected_state_digest=digest)
            )
        series = CORE.git_issue_series_receipts(CORE.all_tasks())
        self.assertEqual(1, len(series))
        before = [
            (meta["id"], meta["status"], meta["task_revision"]) for _, meta, _ in CORE.all_tasks()
        ]
        args = argparse.Namespace(
            repository="github.com/owner/product",
            issue_number=42,
            expected_manifest_digest=series[0]["manifest_digest"],
            transport="mock",
            mock_status="published",
            mock_comment_id="42",
        )
        with patch.object(CORE, "commit", return_value=True) as commit:
            CORE.cmd_issue_series_publish(args)
        records = list((self.root / "issue-series-publications").glob("*.json"))
        self.assertEqual(1, len(records))
        recorded = json.loads(records[0].read_text())
        self.assertEqual("published", recorded["status"])
        self.assertEqual("42", recorded["comment_id"])
        self.assertEqual(
            before,
            [
                (meta["id"], meta["status"], meta["task_revision"])
                for _, meta, _ in CORE.all_tasks()
            ],
        )
        with patch.object(CORE, "commit", return_value=True) as replay:
            CORE.cmd_issue_series_publish(args)
        commit.assert_called_once()
        replay.assert_not_called()
        args.repository = "github.com/other/project"
        with self.assertRaisesRegex(RuntimeError, "authoritative manifest"):
            CORE.cmd_issue_series_publish(args)
        self.assertEqual(1, len(list((self.root / "issue-series-publications").glob("*.json"))))

    def test_live_publication_reserves_then_resolves_outside_the_lock(self) -> None:
        self.make_task()
        manifest = self.issue_series_manifest()
        with patch.object(CORE, "commit", return_value=True):
            CORE.cmd_issue_series_create(
                argparse.Namespace(
                    manifest=manifest,
                    expected_state_digest=CORE.issue_series_state_digest(CORE.all_tasks()),
                )
            )
        digest = CORE.git_issue_series_receipts(CORE.all_tasks())[0]["manifest_digest"]
        args = argparse.Namespace(
            repository="github.com/owner/product",
            issue_number=42,
            expected_manifest_digest=digest,
            transport="live",
            mock_status="published",
            mock_comment_id="unused",
        )
        outcome = CORE.PublicationOutcome(
            "published",
            CORE.publication_key(args.repository, args.issue_number, digest),
            digest,
            "42",
        )
        with (
            patch.object(CORE, "commit", return_value=True) as commit,
            patch.object(CORE, "_live_issue_series_publication", return_value=outcome) as live,
        ):
            CORE.cmd_issue_series_publish(args)
        live.assert_called_once()
        self.assertEqual(2, commit.call_count)
        record = json.loads(
            next((self.root / "issue-series-publications").glob("*.json")).read_text()
        )
        self.assertEqual("published", record["status"])
        self.assertEqual("42", record["comment_id"])

    def test_live_publication_classifies_failures_without_retaining_diagnostics(self) -> None:
        digest = "sha256:" + "a" * 64
        key = CORE.publication_key("github.com/owner/product", 42, digest)
        cases = {
            "HTTP 401": "deferred_unauthorized",
            "HTTP 410": "deferred_closed",
            "HTTP 404": "deferred_moved",
            "HTTP 409": "deferred_conflict",
            "temporary outage": "deferred_unavailable",
        }
        for diagnostic, expected in cases.items():
            with self.subTest(diagnostic=diagnostic):
                outcome = CORE._live_publication_failure(diagnostic, key, digest)
                self.assertEqual(expected, outcome.status)
                self.assertNotIn(diagnostic, repr(outcome))

    def test_live_publication_replays_final_receipt_without_another_post(self) -> None:
        self.make_task()
        manifest = self.issue_series_manifest()
        with patch.object(CORE, "commit", return_value=True):
            CORE.cmd_issue_series_create(
                argparse.Namespace(
                    manifest=manifest,
                    expected_state_digest=CORE.issue_series_state_digest(CORE.all_tasks()),
                )
            )
        digest = CORE.git_issue_series_receipts(CORE.all_tasks())[0]["manifest_digest"]
        args = argparse.Namespace(
            repository="github.com/owner/product",
            issue_number=42,
            expected_manifest_digest=digest,
            transport="live",
            mock_status="published",
            mock_comment_id="unused",
        )
        outcome = CORE.PublicationOutcome(
            "published",
            CORE.publication_key(args.repository, args.issue_number, digest),
            digest,
            "42",
        )
        with (
            patch.object(CORE, "commit", return_value=True),
            patch.object(CORE, "_live_issue_series_publication", return_value=outcome),
        ):
            CORE.cmd_issue_series_publish(args)
        with patch.object(CORE, "_live_issue_series_publication") as live:
            CORE.cmd_issue_series_publish(args)
        live.assert_not_called()

    def test_live_publication_rejects_non_numeric_remote_comment_id(self) -> None:
        digest = "sha256:" + "a" * 64
        with patch.object(CORE, "CONFIG", self.root / "config.json"):
            CORE.CONFIG.write_text(json.dumps({"github_repository": "owner/product"}))
            responses = [
                subprocess.CompletedProcess([], 0, "", ""),
                subprocess.CompletedProcess([], 0, "sensitive-output", ""),
            ]
            with patch.object(CORE.subprocess, "run", side_effect=responses):
                outcome = CORE._live_issue_series_publication(
                    "github.com/owner/product", 42, digest, "body"
                )
        self.assertEqual("ambiguous", outcome.status)
        self.assertIsNone(outcome.comment_id)

    def test_live_publication_defers_when_gh_is_unavailable(self) -> None:
        digest = "sha256:" + "c" * 64
        with patch.object(CORE, "CONFIG", self.root / "config.json"):
            CORE.CONFIG.write_text(json.dumps({"github_repository": "owner/product"}))
            with (
                patch.object(CORE.issue_series_service.shutil, "which", return_value=None),
                patch.object(CORE.subprocess, "run") as run,
            ):
                outcome = CORE._live_issue_series_publication(
                    "github.com/owner/product", 42, digest, "body"
                )
        self.assertEqual("deferred_unavailable", outcome.status)
        run.assert_not_called()

    def test_sqlite_issue_series_projections_replace_stale_files(self) -> None:
        key = "a" * 64
        receipt = {
            "series_identity": {"repository": "github.com/owner/product", "issue_number": 42},
            "manifest": {"schema_version": 1, "members": []},
        }
        publication = {
            "publication_key": key,
            "manifest_digest": "sha256:" + "b" * 64,
            "status": "deferred_unavailable",
            "comment_id": "",
        }

        class Backend:
            def load_issue_series(self) -> list[dict[str, object]]:
                return cast(list[dict[str, object]], [receipt])

            def load_issue_series_publications(self) -> list[dict[str, object]]:
                return cast(list[dict[str, object]], [publication])

        stale_manifest = self.root / "issue-series" / "stale.json"
        stale_manifest.parent.mkdir()
        stale_manifest.write_text("stale")
        stale_publication = self.root / "issue-series-publications" / ("c" * 64 + ".json")
        stale_publication.parent.mkdir()
        stale_publication.write_text("stale")

        self.assertEqual(1, len(CORE.write_sqlite_issue_series_projections(Backend())))
        self.assertEqual(1, len(CORE.write_sqlite_issue_series_publication_projections(Backend())))
        self.assertFalse(stale_manifest.exists())
        self.assertFalse(stale_publication.exists())
        self.assertEqual(
            {key + ".json"}, {path.name for path in stale_publication.parent.glob("*.json")}
        )

    def test_publication_lock_releases_after_scope(self) -> None:
        key = "d" * 64
        with patch.object(CORE, "coordinator_lock_path", return_value=self.root / "state.lock"):
            with CORE.issue_series_publication_locked(key):
                self.assertTrue((self.root / "issue-series-publications" / f"{key}.lock").exists())
            with CORE.issue_series_publication_locked(key):
                pass

    def test_live_publication_recovers_marker_before_posting(self) -> None:
        digest = "sha256:" + "b" * 64
        with patch.object(CORE, "CONFIG", self.root / "config.json"):
            CORE.CONFIG.write_text(json.dumps({"github_repository": "owner/product"}))
            found = subprocess.CompletedProcess([], 0, "77\n", "")
            with patch.object(CORE.subprocess, "run", return_value=found) as run:
                outcome = CORE._live_issue_series_publication(
                    "github.com/owner/product", 42, digest, "body"
                )
        self.assertEqual("already_published", outcome.status)
        self.assertEqual("77", outcome.comment_id)
        run.assert_called_once()

    def test_issue_series_create_restores_every_precommit_write(self) -> None:
        self.make_task()
        manifest = self.issue_series_manifest()
        args = argparse.Namespace(
            manifest=manifest,
            expected_state_digest=CORE.issue_series_state_digest(CORE.all_tasks()),
        )
        before = {path: path.read_text() for path in (self.root / "tasks").glob("*.md")}
        before[self.root / "CURRENT.md"] = (self.root / "CURRENT.md").read_text()
        before[self.root / "STATUS.md"] = (self.root / "STATUS.md").read_text()
        original = CORE.write_task
        writes = 0

        def fail_second_task(path: Path, meta: dict[str, object], body: str) -> None:
            nonlocal writes
            writes += 1
            if writes == 2:
                raise RuntimeError("injected task write failure")
            original(path, meta, body)

        with (
            patch.object(CORE, "write_task", side_effect=fail_second_task),
            self.assertRaisesRegex(RuntimeError, "injected task write failure"),
        ):
            CORE.cmd_issue_series_create(args)
        self.assertEqual({"AR-0001"}, {meta["id"] for _path, meta, _body in CORE.all_tasks()})
        self.assertFalse(list((self.root / "issue-series").glob("*.json")))
        self.assertEqual(before, {path: path.read_text() for path in before})

    def test_git_series_records_survive_sqlite_authority_import(self) -> None:
        self.make_task()
        manifest = self.issue_series_manifest()
        args = argparse.Namespace(
            manifest=manifest,
            expected_state_digest=CORE.issue_series_state_digest(CORE.all_tasks()),
        )
        with patch.object(CORE, "commit", return_value=True):
            CORE.cmd_issue_series_create(args)
        tasks = CORE.git_tasks()
        records = CORE.git_issue_series_receipts(tasks)
        self.assertEqual(1, len(records))
        CORE.DATABASE.parent.mkdir(exist_ok=True)
        CORE.create_database(
            CORE.DATABASE,
            CORE.project_binding(),
            tasks,
            imported_at="2026-10-12T00:00:00+00:00",
            source_backend="git",
            source_checkpoint="a" * 40,
            issue_series=records,
        )
        self.assertEqual(
            records[0]["manifest"],
            CORE.SQLiteBackend(
                CORE.DATABASE, CORE.project_binding(), CORE.TASKS
            ).load_issue_series()[0]["manifest"],
        )

    def test_issue_series_create_restores_every_write_when_commit_fails(self) -> None:
        self.make_task()
        manifest = self.issue_series_manifest()
        args = argparse.Namespace(
            manifest=manifest,
            expected_state_digest=CORE.issue_series_state_digest(CORE.all_tasks()),
        )
        before = {path: path.read_text() for path in (self.root / "tasks").glob("*.md")}
        before[self.root / "CURRENT.md"] = (self.root / "CURRENT.md").read_text()
        before[self.root / "STATUS.md"] = (self.root / "STATUS.md").read_text()
        with (
            patch.object(CORE, "commit", side_effect=RuntimeError("injected commit failure")),
            self.assertRaisesRegex(RuntimeError, "injected commit failure"),
        ):
            CORE.cmd_issue_series_create(args)
        self.assertEqual({"AR-0001"}, {meta["id"] for _path, meta, _body in CORE.all_tasks()})
        self.assertFalse(list((self.root / "issue-series").glob("*.json")))
        self.assertEqual(before, {path: path.read_text() for path in before})

    def test_issue_series_create_has_sqlite_authority_parity(self) -> None:
        self.make_task()
        CORE.DATABASE.parent.mkdir()
        CORE.create_database(
            CORE.DATABASE,
            CORE.project_binding(),
            CORE.git_tasks(),
            imported_at="2026-10-12T00:00:00+00:00",
            source_backend="git",
            source_checkpoint="a" * 40,
        )
        CORE.BACKEND_CONFIG.write_text(
            json.dumps(
                {
                    "schema_version": 1,
                    "project_id": project_uuid("1"),
                    "backend": "sqlite",
                }
            )
        )
        manifest = self.issue_series_manifest()
        args = argparse.Namespace(
            manifest=manifest,
            expected_state_digest=CORE.issue_series_state_digest(CORE.all_tasks()),
        )
        CORE.cmd_issue_series_create(args)
        created = {meta["id"]: meta for _path, meta, _body in CORE.all_tasks()}
        self.assertEqual({"AR-0001", "AR-9000", "AR-9001"}, set(created))
        backend = CORE.storage_backend()
        self.assertEqual(1, len(backend.load_issue_series()))
        connection = sqlite3.connect(CORE.DATABASE)
        try:
            self.assertEqual(
                ["AR-9000", "AR-9001"],
                [
                    row[0]
                    for row in connection.execute(
                        "SELECT task_id FROM issue_series_members ORDER BY task_id"
                    )
                ],
            )
        finally:
            connection.close()
        self.assertTrue(list((self.root / "issue-series").glob("*.json")))

    def test_sqlite_publication_exports_the_same_local_receipt_projection(self) -> None:
        self.make_task()
        CORE.DATABASE.parent.mkdir()
        CORE.create_database(
            CORE.DATABASE,
            CORE.project_binding(),
            CORE.git_tasks(),
            imported_at="2026-10-12T00:00:00+00:00",
            source_backend="git",
            source_checkpoint="a" * 40,
        )
        CORE.BACKEND_CONFIG.write_text(
            json.dumps({"schema_version": 1, "project_id": project_uuid("1"), "backend": "sqlite"})
        )
        manifest = self.issue_series_manifest()
        CORE.cmd_issue_series_create(
            argparse.Namespace(
                manifest=manifest,
                expected_state_digest=CORE.issue_series_state_digest(CORE.all_tasks()),
            )
        )
        series = CORE.storage_backend().load_issue_series()
        args = argparse.Namespace(
            repository="github.com/owner/product",
            issue_number=42,
            expected_manifest_digest=series[0]["manifest_digest"],
            transport="dry-run",
            mock_status="published",
            mock_comment_id="unused",
        )
        CORE.cmd_issue_series_publish(args)
        backend = CORE.storage_backend()
        published = backend.load_issue_series_publications()
        self.assertEqual(1, len(published))
        self.assertEqual("dry_run", published[0]["status"])
        projection = CORE.issue_series_publication_path(str(published[0]["publication_key"]))
        self.assertEqual(published[0], json.loads(projection.read_text()))

    def test_sixteen_processes_serialize_one_issue_series_create(self) -> None:
        self.make_task()
        manifest = self.issue_series_manifest()
        install_secondary_controller()
        digest = CORE.issue_series_state_digest(CORE.all_tasks())
        context = multiprocessing.get_context("fork")
        start, outcomes = context.Event(), context.Queue()
        workers = [
            context.Process(
                target=racing_issue_series_create,
                args=(str(self.root), str(manifest), digest, start, outcomes),
            )
            for _ in range(16)
        ]
        for worker in workers:
            worker.start()
        start.set()
        results = [outcomes.get(timeout=20) for _ in workers]
        for worker in workers:
            worker.join(20)
            self.assertEqual(0, worker.exitcode)
        self.assertEqual(1, sum(result[0] == "accepted" for result in results), results)
        self.assertTrue(all(result[0] in {"accepted", "rejected"} for result in results))
        created = {meta["id"] for _path, meta, _body in CORE.all_tasks()}
        self.assertEqual({"AR-0001", "AR-9000", "AR-9001"}, created)
        self.assertEqual(1, len(list((self.root / "issue-series").glob("*.json"))))

    def test_cli_dispatch_keeps_the_calling_controller_after_another_import(self) -> None:
        """The shared service must not route the first CLI through a later controller."""
        install_secondary_controller()
        args = argparse.Namespace(
            cmd="issue-series", issue_series_action="plan", manifest=self.root / "plan.json"
        )
        with patch.object(CORE, "cmd_issue_series_plan") as primary:
            self.assertTrue(CORE.issue_series_service.dispatch_cli(args, vars(CORE)))
        primary.assert_called_once_with(args)

    def test_sixteen_processes_commit_one_issue_series_to_a_real_remote(self) -> None:
        self.make_task()
        manifest = self.issue_series_manifest()
        CORE.RUNTIME.mkdir(exist_ok=True)
        CORE.CONFIG.write_text(json.dumps({"push_enabled": True}))
        run_git(["git", "init", "-q", "--initial-branch=main", str(self.root)])
        run_git(["git", "-C", str(self.root), "config", "user.name", "Series Fixture"])
        run_git(["git", "-C", str(self.root), "config", "user.email", "series@example.invalid"])
        run_git(["git", "-C", str(self.root), "add", "."])
        run_git(["git", "-C", str(self.root), "commit", "-qm", "series baseline"])
        remote_directory = TemporaryDirectory()
        self.addCleanup(remote_directory.cleanup)
        remote = Path(remote_directory.name) / "state.git"
        run_git(["git", "init", "--bare", "-q", "--initial-branch=main", str(remote)])
        run_git(["git", "-C", str(self.root), "remote", "add", "origin", str(remote)])
        run_git(["git", "-C", str(self.root), "push", "origin", "HEAD:refs/heads/main"])
        digest = CORE.issue_series_state_digest(CORE.all_tasks())
        context = multiprocessing.get_context("fork")
        start, outcomes = context.Event(), context.Queue()
        workers = [
            context.Process(
                target=racing_real_issue_series_create,
                args=(str(self.root), str(manifest), digest, start, outcomes),
            )
            for _ in range(16)
        ]
        for worker in workers:
            worker.start()
        start.set()
        results = [outcomes.get(timeout=30) for _ in workers]
        for worker in workers:
            worker.join(30)
            self.assertEqual(0, worker.exitcode)
        self.assertEqual(1, sum(result[0] == "accepted" for result in results), results)
        self.assertEqual(
            {"AR-0001", "AR-9000", "AR-9001"}, {item[1]["id"] for item in CORE.all_tasks()}
        )
        self.assertEqual(
            "", CORE.run(["git", "-C", str(self.root), "status", "--porcelain"]).stdout
        )
        self.assertEqual(
            CORE.run(["git", "-C", str(self.root), "rev-parse", "HEAD"]).stdout,
            CORE.run(["git", "-C", str(self.root), "rev-parse", "origin/main"]).stdout,
        )

    def test_sixteen_processes_commit_one_issue_series_to_sqlite(self) -> None:
        self.make_task()
        CORE.DATABASE.parent.mkdir()
        CORE.create_database(
            CORE.DATABASE,
            CORE.project_binding(),
            CORE.git_tasks(),
            imported_at="2026-10-12T00:00:00+00:00",
            source_backend="git",
            source_checkpoint="a" * 40,
        )
        CORE.BACKEND_CONFIG.write_text(
            json.dumps(
                {
                    "schema_version": 1,
                    "project_id": project_uuid("1"),
                    "backend": "sqlite",
                }
            )
        )
        manifest = self.issue_series_manifest()
        install_secondary_controller()
        digest = CORE.issue_series_state_digest(CORE.all_tasks())
        context = multiprocessing.get_context("fork")
        start, outcomes = context.Event(), context.Queue()
        workers = [
            context.Process(
                target=racing_sqlite_issue_series_create,
                args=(str(self.root), str(manifest), digest, start, outcomes),
            )
            for _ in range(16)
        ]
        for worker in workers:
            worker.start()
        start.set()
        results = [outcomes.get(timeout=30) for _ in workers]
        for worker in workers:
            worker.join(30)
            self.assertEqual(0, worker.exitcode)
        self.assertEqual(1, sum(result[0] == "accepted" for result in results), results)
        connection = sqlite3.connect(CORE.DATABASE)
        try:
            self.assertEqual(
                1, connection.execute("SELECT count(*) FROM issue_series").fetchone()[0]
            )
            self.assertEqual(
                2, connection.execute("SELECT count(*) FROM issue_series_members").fetchone()[0]
            )
        finally:
            connection.close()
        self.assertEqual(
            {"AR-0001", "AR-9000", "AR-9001"}, {item[1]["id"] for item in CORE.all_tasks()}
        )
