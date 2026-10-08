# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Fresh Git/SQLite upgrade campaigns with failure-path recovery evidence.

These tests intentionally use real temporary authorities and the production
backup/restore helpers.  They are campaign fixtures, not an authorization for
the still fail-closed user-facing ``upgrade apply`` command.
"""

from __future__ import annotations

import json
import multiprocessing
import os
import shutil
import signal
import sqlite3
import subprocess
import tempfile
import unittest
from pathlib import Path
from typing import Any

from tools.generate_upgrade_contract import generate
from tools.git_backup import create_backup as create_git_backup
from tools.git_backup import restore_backup
from tools.git_backup import verify_backup as verify_git_backup
from tools.sqlite_backup import BackupError as SQLiteBackupError
from tools.sqlite_backup import backup_database, restore_database, verify_backup
from tools.sqlite_storage import create_database
from tools.upgrade_authority import commit_runtime_selector, read_runtime_selector
from tools.upgrade_commands import UpgradeCommandError, execute_upgrade_command

FAILURE_POINTS = (
    "discover",
    "preflight",
    "quiesce",
    "backup",
    "stage",
    "commit",
    "validate",
    "reopen",
    None,
)


class InjectedCampaignFailureError(RuntimeError):
    """A deterministic fault at one generated phase boundary."""


def _execute_generated_operations(
    document: dict[str, Any], failure: str | None = None
) -> list[dict[str, str]]:
    """Consume generated operations and persist deterministic outcome records.

    This is deliberately a campaign executor, not production authorization:
    it validates the generated dependency/order contract and records the
    rollback operation when a post-backup fixture fault is injected.
    """
    handlers = {
        "release.inspect": "discover",
        "admission.check": "preflight",
        "barrier.acquire": "quiesce",
        "backend.backup": "backup",
        "runtime.stage": "stage",
        "authority.atomic_replace": "commit",
        "runtime.validate": "validate",
        "barrier.reopen": "reopen",
    }
    completed: set[str] = set()
    records: list[dict[str, str]] = []
    for phase in document["phases"]:
        phase_id = str(phase["id"])
        if set(phase["requires"]) != {
            str(previous["id"])
            for previous in document["phases"]
            if str(previous["id"]) in set(phase["requires"])
        }:
            raise AssertionError("generated dependency record is inconsistent")
        if not set(phase["requires"]).issubset(completed):
            raise AssertionError("generated phase dependency was not completed")
        operation = phase["operation"]
        if handlers.get(str(operation["opcode"])) != phase_id:
            raise AssertionError("generated opcode has no phase dispatcher")
        records.append(
            {
                "operation_id": str(operation["operation_id"]),
                "opcode": str(operation["opcode"]),
                "outcome": "failed" if failure == phase_id else "completed",
            }
        )
        if failure == phase_id:
            if phase_id not in {"stage", "commit", "validate", "reopen"}:
                break
            rollback = document["rollback"]["operation"]
            records.append(
                {
                    "operation_id": str(rollback["operation_id"]),
                    "opcode": str(rollback["opcode"]),
                    "outcome": "completed",
                }
            )
            break
        completed.add(phase_id)
    if failure in {"stage", "commit", "validate", "reopen"} and records[-1]["operation_id"] != (
        f"{document['operation_id']}:rollback"
    ):
        raise AssertionError("failed generated operation did not link rollback record")
    return records


def _crash_after_uncommitted_coordinator_write(database: str, ready: str) -> None:
    """Crash a real coordinator SQLite writer before commit, leaving WAL residue."""
    connection = sqlite3.connect(database)
    try:
        connection.execute("PRAGMA journal_mode=WAL")
        connection.execute("BEGIN IMMEDIATE")
        connection.execute("UPDATE tasks SET body=? WHERE id='AR-0001'", ("# partial write\n",))
        Path(ready).write_text("writer-ready\n", encoding="utf-8")
        os.kill(os.getpid(), signal.SIGKILL)
    finally:  # pragma: no cover - process is deliberately killed
        connection.close()


def _run(args: list[str], cwd: Path) -> str:
    return subprocess.check_output(  # noqa: S603
        args, cwd=cwd, text=True, stderr=subprocess.STDOUT
    )


def _contract(backend: str) -> dict[str, Any]:
    def release(version: str, seed: str) -> dict[str, str]:
        return {
            "version": version,
            "source_commit": seed * 40,
            "tag_ref": f"refs/tags/{version}",
            "tag_object": chr(ord(seed) + 1) * 40,
            "signature_sha256": chr(ord(seed) + 2) * 64,
            "trust_policy_sha256": chr(ord(seed) + 3) * 64,
            "vendor_manifest_sha256": chr(ord(seed) + 4) * 64,
        }

    return generate(
        {
            "operation_id": f"campaign:v0.3.5-to-v0.3.6:{backend}",
            "backend": backend,
            "selector_ref": ".runtime/runtime-selector.json",
            "expected_state_revision": 7,
            "barrier_id": "barrier-7",
            "fencing_token": "fence-7",
            "from": release("v0.3.5", "a"),
            "to": release("v0.3.6", "b"),
        }
    )


class UpgradeCampaignTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(prefix="upgrade-campaign-")
        self.root = Path(self.temporary.name)

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def test_generated_contract_is_the_executed_ordered_campaign(self) -> None:
        for backend in ("git", "sqlite"):
            document = _contract(backend)
            phase_ids = tuple(phase["id"] for phase in document["phases"])
            self.assertEqual(
                (
                    "discover",
                    "preflight",
                    "quiesce",
                    "backup",
                    "stage",
                    "commit",
                    "validate",
                    "reopen",
                ),
                phase_ids,
            )
            self.assertEqual(list(range(1, 9)), [phase["order"] for phase in document["phases"]])
            self.assertEqual(
                [phase["operation"]["operation_id"] for phase in document["phases"]],
                [f"{document['operation_id']}:{phase}" for phase in phase_ids],
            )
            self.assertEqual(
                f"{document['operation_id']}:backup",
                document["rollback"]["operation"]["inputs"]["backup_operation_id"],
            )
            records = _execute_generated_operations(document, "validate")
            self.assertEqual("failed", records[-2]["outcome"])
            self.assertEqual("backend.restore", records[-1]["opcode"])
            self.assertEqual(f"{document['operation_id']}:rollback", records[-1]["operation_id"])

    def test_production_apply_is_explicitly_rejected_without_authority_mutation(self) -> None:
        document = _contract("sqlite")
        contract_path = self.root / "generated-contract.json"
        contract_path.write_text(json.dumps(document, sort_keys=True), encoding="utf-8")
        before = contract_path.read_bytes()
        with self.assertRaisesRegex(UpgradeCommandError, "no coordinator state was mutated"):
            execute_upgrade_command("apply", contract_path, "sqlite")
        self.assertEqual(before, contract_path.read_bytes())

    def _git_authority(self, path: Path, version: str) -> None:
        path.mkdir()
        _run(["git", "init", "-q", "-b", "main", str(path)], self.root)
        _run(["git", "config", "user.email", "campaign@example.invalid"], path)
        _run(["git", "config", "user.name", "Upgrade Campaign"], path)
        (path / "runtime-selector.json").write_text(
            json.dumps(
                {"schema_version": 1, "active_release": version, "previous_release": "v0.3.4"}
            )
            + "\n",
            encoding="utf-8",
        )
        (path / "runtime.version").write_text(version + "\n", encoding="utf-8")
        (path / "state.json").write_text('{"state":"active"}\n', encoding="utf-8")
        (path / "coordinator.binding.json").write_text(
            '{"schema_version":1,"project_id":"11111111-1111-4111-8111-111111111111",'
            '"state_repository":"campaign/state","product_repository":"campaign/product"}\n',
            encoding="utf-8",
        )
        (path / "coordinator.backend.json").write_text(
            '{"schema_version":1,"project_id":"11111111-1111-4111-8111-111111111111",'
            '"backend":"git"}\n',
            encoding="utf-8",
        )
        (path / "AR-0001.md").write_text(
            '{"id":"AR-0001","status":"open","task_revision":1}\n\n# Task\n',
            encoding="utf-8",
        )
        (path / "CURRENT.md").write_text("AR-0001: open\n", encoding="utf-8")
        (path / "STATUS.md").write_text("campaign state active\n", encoding="utf-8")
        (path / "events.json").write_text('[{"kind":"import","revision":1}]\n', encoding="utf-8")
        (path / "history.json").write_text(
            '[{"task_id":"AR-0001","revision":1}]\n', encoding="utf-8"
        )
        _run(
            [
                "git",
                "add",
                "runtime.version",
                "state.json",
                "runtime-selector.json",
                "coordinator.binding.json",
                "coordinator.backend.json",
                "AR-0001.md",
                "CURRENT.md",
                "STATUS.md",
                "events.json",
                "history.json",
            ],
            path,
        )
        _run(["git", "commit", "-q", "-m", f"runtime {version}"], path)

    @staticmethod
    def _git_functional(path: Path, expected: str) -> None:
        assert _run(["git", "status", "--porcelain"], path) == ""
        assert _run(["git", "symbolic-ref", "--short", "HEAD"], path).strip() == "main"
        assert (path / "runtime.version").read_text(encoding="utf-8") == expected + "\n"
        assert json.loads((path / "state.json").read_text(encoding="utf-8"))["state"] == "active"
        binding = json.loads((path / "coordinator.binding.json").read_text(encoding="utf-8"))
        assert binding["project_id"] == "11111111-1111-4111-8111-111111111111"
        assert (
            json.loads((path / "coordinator.backend.json").read_text(encoding="utf-8"))["backend"]
            == "git"
        )
        assert (
            json.loads((path / "runtime-selector.json").read_text(encoding="utf-8"))[
                "active_release"
            ]
            == expected
        )
        task_header = (path / "AR-0001.md").read_text(encoding="utf-8").split("\n", 1)[0]
        assert json.loads(task_header)["status"] == "open"
        assert json.loads((path / "events.json").read_text(encoding="utf-8"))[0]["kind"] == "import"
        assert (
            json.loads((path / "history.json").read_text(encoding="utf-8"))[0]["task_id"]
            == "AR-0001"
        )

    def _replace_git(self, authority: Path, backup: Path) -> None:
        displaced = authority.with_name("authority-displaced")
        if displaced.exists():
            shutil.rmtree(displaced)
        authority.rename(displaced)
        restore_backup(backup, authority)

    def _run_git_campaign(self, failure: str | None) -> str:  # noqa: C901
        phases = _contract("git")["phases"]
        campaign_root = self.root / ("git-" + (failure or "success"))
        campaign_root.mkdir(mode=0o700)
        authority = campaign_root / "git-authority"
        target = campaign_root / "git-target"
        self._git_authority(authority, "v0.3.5")
        self._git_authority(target, "v0.3.6")
        old_head = _run(["git", "rev-parse", "HEAD"], authority).strip()
        old_backup = campaign_root / "git-backup"
        target_backup = campaign_root / "git-target-backup"
        executed: list[str] = []
        try:
            for phase_record in phases:
                phase = phase_record["id"]
                executed.append(phase)
                self.assertEqual(
                    phase_record["operation"]["operation_id"],
                    f"campaign:v0.3.5-to-v0.3.6:git:{phase}",
                )
                if phase == "backup":
                    create_git_backup(authority, old_backup, quiesced=True)
                    verify_git_backup(old_backup)
                if phase == "stage":
                    create_git_backup(target, target_backup, quiesced=True)
                    verify_git_backup(target_backup)
                if phase == "commit":
                    self._replace_git(authority, target_backup)
                if failure == phase:
                    raise InjectedCampaignFailureError(phase)
                if phase in {"validate", "reopen"}:
                    self._git_functional(authority, "v0.3.6")
        except InjectedCampaignFailureError:
            pass
        if failure is not None and failure in {"commit", "validate", "reopen"}:
            self._replace_git(authority, old_backup)
        expected = "v0.3.5" if failure is not None else "v0.3.6"
        self._git_functional(authority, expected)
        if failure is not None and failure in {"commit", "validate", "reopen"}:
            self.assertEqual(old_head, _run(["git", "rev-parse", "HEAD"], authority).strip())
        return executed[-1]

    def test_git_campaign_reopens_functional_old_or_new_runtime_after_each_failure(self) -> None:
        for failure in FAILURE_POINTS:
            with self.subTest(failure=failure):
                self.assertEqual(failure or "reopen", self._run_git_campaign(failure))

    @staticmethod
    def _sqlite_authority(path: Path, version: str) -> dict[str, str]:
        binding = {
            "project_id": "11111111-1111-4111-8111-111111111111",
            "state_repository": "campaign/state",
            "product_repository": "campaign/product",
        }
        metadata = {
            "schema_version": 1,
            "id": "AR-0001",
            "title": "Campaign task",
            "status": "open",
            "priority": "P1",
            "summary": f"Runtime {version}.",
            "next_action": "Continue.",
            "task_revision": 1,
            "updated_at": "2026-09-16T00:00:00+00:00",
            "owner": "",
            "claim_expires": "",
            "worktree_key": "",
            "branch": "",
            "checkpoint_commit": "",
            "plan": "",
            "depends_on": [],
        }
        create_database(
            path,
            binding,
            [(Path("AR-0001.md"), metadata, f"# Campaign {version}\n")],
            imported_at="2026-09-16T00:00:00+00:00",
            source_backend="git",
            source_checkpoint="a" * 40,
        )
        # Exercise the real WAL path and durable event/history tables.  The
        # schema itself has no runtime-release column; release identity is
        # deliberately held by the separate selector below.
        connection = sqlite3.connect(path)
        try:
            connection.execute("PRAGMA journal_mode=WAL")
            connection.execute(
                "INSERT INTO events(task_id, revision, kind, recorded_at, note) "
                "VALUES ('AR-0001', 2, 'campaign', ?, ?)",
                ("2026-09-16T00:00:01+00:00", version),
            )
            connection.commit()
        finally:
            connection.close()
        return binding

    @staticmethod
    def _sqlite_functional(path: Path, expected: str, binding: dict[str, str]) -> None:
        connection = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
        try:
            assert connection.execute("PRAGMA integrity_check").fetchone()[0] == "ok"
            metadata = dict(connection.execute("SELECT key, value FROM metadata"))
            assert metadata["state"] == "active"
            assert metadata["project_id"] == binding["project_id"]
            assert (
                connection.execute("SELECT status FROM tasks WHERE id='AR-0001'").fetchone()[0]
                == "open"
            )
            assert connection.execute("SELECT COUNT(*) FROM events").fetchone()[0] >= 2
        finally:
            connection.close()
        selector = path.with_name("runtime-selector.json")
        assert read_runtime_selector(selector)["active_release"] == expected

    @staticmethod
    def _checkpoint(path: Path) -> None:
        connection = sqlite3.connect(path)
        try:
            connection.execute("PRAGMA wal_checkpoint(TRUNCATE)")
        finally:
            connection.close()

    def _run_sqlite_campaign(self, failure: str | None) -> str:
        phases = _contract("sqlite")["phases"]
        campaign_root = self.root / ("sqlite-" + (failure or "success"))
        campaign_root.mkdir(mode=0o700)
        authority = campaign_root / "sqlite-authority.db"
        target = campaign_root / "sqlite-target.db"
        binding = self._sqlite_authority(authority, "v0.3.5")
        self._sqlite_authority(target, "v0.3.6")
        old_selector = campaign_root / "runtime-selector.json"
        commit_runtime_selector(old_selector, "v0.3.5", "v0.3.4")
        old_backup = campaign_root / "sqlite-old.db"
        target_backup = campaign_root / "sqlite-target-backup.db"
        old_manifest: dict[str, Any] | None = None
        target_manifest: dict[str, Any] | None = None
        executed: list[str] = []
        try:
            for phase_record in phases:
                phase = phase_record["id"]
                executed.append(phase)
                self.assertEqual(
                    phase_record["operation"]["operation_id"],
                    f"campaign:v0.3.5-to-v0.3.6:sqlite:{phase}",
                )
                if phase == "backup":
                    old_manifest = backup_database(authority, old_backup, binding)
                    verify_backup(old_backup, old_manifest, binding)
                if phase == "stage":
                    target_manifest = backup_database(target, target_backup, binding)
                    verify_backup(target_backup, target_manifest, binding)
                if phase == "commit":
                    assert old_manifest is not None and target_manifest is not None
                    self._checkpoint(authority)
                    restore_database(
                        target_backup, authority, target_manifest, binding, quiesced=True
                    )
                    commit_runtime_selector(old_selector, "v0.3.6", "v0.3.5")
                if failure == phase:
                    raise InjectedCampaignFailureError(phase)
                if phase in {"validate", "reopen"}:
                    self._sqlite_functional(authority, "v0.3.6", binding)
        except InjectedCampaignFailureError:
            pass
        if failure is not None and failure in {"commit", "validate", "reopen"}:
            assert old_manifest is not None
            self._checkpoint(authority)
            restore_database(old_backup, authority, old_manifest, binding, quiesced=True)
            commit_runtime_selector(old_selector, "v0.3.5", "v0.3.4")
        self._sqlite_functional(authority, "v0.3.5" if failure is not None else "v0.3.6", binding)
        return executed[-1]

    def test_sqlite_campaign_reopens_functional_old_or_new_runtime_after_each_failure(self) -> None:
        for failure in FAILURE_POINTS:
            with self.subTest(failure=failure):
                self.assertEqual(failure or "reopen", self._run_sqlite_campaign(failure))

    def test_sqlite_process_death_reopens_last_committed_coordinator_state(self) -> None:
        root = self.root / "sqlite-crash"
        root.mkdir(mode=0o700)
        database = root / "authority.db"
        binding = self._sqlite_authority(database, "v0.3.5")
        selector = root / "runtime-selector.json"
        commit_runtime_selector(selector, "v0.3.5", "v0.3.4")
        ready = root / "writer.ready"
        process = multiprocessing.get_context("fork").Process(
            target=_crash_after_uncommitted_coordinator_write,
            args=(str(database), str(ready)),
        )
        process.start()
        process.join(timeout=10)
        self.assertEqual(-signal.SIGKILL, process.exitcode)
        self.assertFalse(process.is_alive())
        selected = read_runtime_selector(selector)
        self.assertEqual(
            {"schema_version": 1, "active_release": "v0.3.5", "previous_release": "v0.3.4"},
            selected,
        )
        self._sqlite_functional(database, "v0.3.5", binding)
        connection = sqlite3.connect(f"file:{database}?mode=ro", uri=True)
        try:
            self.assertEqual(
                "# Campaign v0.3.5\n",
                connection.execute("SELECT body FROM tasks WHERE id='AR-0001'").fetchone()[0],
            )
        finally:
            connection.close()

    def test_sqlite_rollback_failure_is_fail_closed_until_sidecar_is_checkpointed(self) -> None:
        root = self.root / "sqlite-rollback-error"
        root.mkdir(mode=0o700)
        authority = root / "authority.db"
        backup = root / "backup.db"
        binding = self._sqlite_authority(authority, "v0.3.5")
        manifest = backup_database(authority, backup, binding)
        selector = root / "runtime-selector.json"
        commit_runtime_selector(selector, "v0.3.6", "v0.3.5")
        # A live sidecar is an unresolved quiescence failure, not permission
        # to risk a partial rollback.
        sidecar = Path(str(authority) + "-wal")
        sidecar.write_bytes(b"live-wal")
        with self.assertRaisesRegex(SQLiteBackupError, "without live WAL sidecars"):
            restore_database(backup, authority, manifest, binding, quiesced=True)
        self._sqlite_functional(authority, "v0.3.6", binding)
        sidecar.unlink()
        self._checkpoint(authority)
        restore_database(backup, authority, manifest, binding, quiesced=True)
        commit_runtime_selector(selector, "v0.3.5", "v0.3.4")
        self._sqlite_functional(authority, "v0.3.5", binding)


if __name__ == "__main__":
    unittest.main()
