# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Hostile tests for the read-only Git authority adapter slice."""

# Test setup invokes fixed Git commands against an isolated temporary repository.
# ruff: noqa: S603, S607

from __future__ import annotations

import multiprocessing
import os
import sqlite3
import subprocess
import tempfile
import unittest
from collections.abc import Mapping
from contextlib import AbstractContextManager, closing, nullcontext
from pathlib import Path
from typing import Any, cast
from unittest.mock import MagicMock, patch

import tools.sqlite_storage as sqlite_storage
from tools.admission_lease import AdmissionLease, validate_recheck
from tools.authority_neutral_commit import CommitAdmissionBundle
from tools.generate_upgrade_contract import generate
from tools.git_authority_adapter import (
    GitAuthorityAdapter,
    GitAuthorityError,
    GitBackupObservation,
    GitRollbackArtifactBinding,
    GitRollbackSessionState,
)
from tools.git_authority_mutation import GitCommitCapability
from tools.git_backup import BackupError, create_backup
from tools.handoffctl import locked
from tools.lock_domain import LockDomainContract
from tools.lock_domain_scope import LockDomainScope
from tools.mutation_fence import MutationFence, provision, provision_control_binding
from tools.rollback_control_store import (
    BarrierSessionState,
    ControlStoreError,
    SQLiteBarrierSessionStore,
    SQLiteRollbackControlStore,
)
from tools.scoped_backend_adapter import ScopedBackendAdapter
from tools.sqlite_storage import (
    SQLiteAuthorityBinding,
    SQLiteBackend,
    SQLiteBackendBinding,
    bind_sqlite_authority_writer,
    bind_sqlite_backend,
    create_database,
)
from tools.upgrade_binding import LiveUpgradeBinding, UpgradeBindingError, UpgradeRuntimeBinding
from tools.upgrade_engine import (
    BoundRollbackCapability,
    GitRollbackObservationCapability,
    PhaseContext,
    RollbackAuthorizationCapability,
    UpgradeEngine,
    UpgradeError,
)
from tools.upgrade_identity import (
    BarrierChildIdentity,
    BarrierSessionIdentity,
    canonical_barrier_digest,
    canonical_barrier_session_digest,
    canonical_envelope_digest,
)

PROJECT = "11111111-1111-4111-8111-111111111111"

CONTEXT = {
    "schema_version": 2,
    "backend": "git",
    "project_id": PROJECT,
    "operation_id": "op-1",
    "state_revision": 1,
    "authority_revision": "authority",
    "fencing_token": "fence",
    "fencing_owner": "owner",
    "durable_barrier_id": "barrier",
    "artifact_root": "/artifacts",
    "source": "/source",
    "destination": "/destination",
    "manifest": "/manifest",
    "selector_ref": ".runtime/runtime-selector.json",
    "barrier_identity_digest": "0" * 64,
    "target": "new",
    "envelope_digest": "0" * 64,
}


def _bound_snapshot_process(
    repository_text: str,
    coordination_text: str,
    expected_branch: str,
    expected_head: str,
    mode: str,
    result: Any,
    rollback: bool = False,
) -> None:
    """Run one real bound snapshot in a fresh process.

    ``crash`` aborts from the first Git observation, after ``snapshot_bound``
    has entered the concrete common/control/authority scope. ``stale`` keeps
    the backend observable so a call would be reported, but must reject from
    the durable reread first.
    """
    coordination = Path(coordination_text)
    authority = coordination / "authority.sqlite"
    control = coordination / "control.sqlite"
    store = SQLiteRollbackControlStore(control, PROJECT, authority)
    session = SQLiteBarrierSessionStore(store, lambda: "authority")
    fence = MutationFence(
        authority,
        coordination / "authority-marker.json",
        coordination / "authority-lifecycle.json",
        coordination / "authority.lock",
        control,
        coordination / "control-binding.json",
        store.control_lock_path,
    )
    with locked() as guard:
        domain = LockDomainContract.capture(guard, session, fence)
    replacement = mode == "replacement"
    authority_revision = "authority"
    fencing_token = "fence-replaced" if replacement else "fence"
    fencing_owner = "owner-replaced" if replacement else "owner"
    durable_barrier_id = "barrier-replaced" if replacement else "barrier"
    state_revision = 2 if replacement else 1
    lease = AdmissionLease(
        PROJECT,
        authority_revision,
        fencing_token,
        fencing_owner,
        durable_barrier_id,
        state_revision,
    )
    recheck = validate_recheck(
        lease,
        project_id=PROJECT,
        authority_revision=authority_revision,
        fencing_token=fencing_token,
        fencing_owner=fencing_owner,
        durable_barrier_id=durable_barrier_id,
        revision=state_revision,
    )
    adapter = GitAuthorityAdapter(Path(repository_text))
    adapter_any: Any = adapter

    if mode == "crash":

        def aborting_git(*_arguments: str) -> str:
            os._exit(17)

        adapter_any._git = aborting_git
    elif mode == "stale":
        calls = 0

        def unexpected_git(*_arguments: str) -> str:
            nonlocal calls
            calls += 1
            raise AssertionError("stale session reached Git backend")

        adapter_any._git = unexpected_git

    active_context = {
        **CONTEXT,
        "target": "rollback" if rollback else "new",
        "authority_revision": authority_revision,
        "fencing_token": fencing_token,
        "fencing_owner": fencing_owner,
        "durable_barrier_id": durable_barrier_id,
        "state_revision": state_revision,
    }
    try:
        scope = LockDomainScope.bind(session, fence, lease, recheck, locked)
        if rollback:
            value = adapter.verify_rollback_context_bound(
                active_context,
                scope,
                lease=lease,
                admission_recheck=recheck,
                expected_branch=expected_branch,
                expected_head=expected_head,
            )
        else:
            value = adapter.snapshot_bound(
                "discover",
                active_context,
                scope,
                lease=lease,
                admission_recheck=recheck,
                expected_branch=expected_branch,
                expected_head=expected_head,
            )
    except Exception as error:
        result.put(("rejected", type(error).__name__, str(error), locals().get("calls", 0)))
    else:
        result.put(("success", value["git_head"], value["git_branch"]))


class GitAuthorityAdapterTests(unittest.TestCase):
    def test_adapter_durable_commit_factory_journals_real_git_receipt(self) -> None:
        admission = CommitAdmissionBundle(
            backend="git",
            target="new",
            operation_id="op-1:commit",
            fencing_token="fence",  # noqa: S106
            state_revision=1,
            barrier_id="barrier",
            artifact_identity="artifact",
            manifest_identity="manifest",
            selector_identity="selector",
            runtime_identity="runtime",
        )
        subprocess.run(["git", "-C", str(self.root), "config", "user.name", "test"], check=True)
        subprocess.run(
            ["git", "-C", str(self.root), "config", "user.email", "test@example"], check=True
        )
        (self.root / "state").write_text("durable\n")
        subprocess.run(["git", "-C", str(self.root), "add", "state"], check=True)
        expected_head = self.adapter._git("rev-parse", "HEAD")
        journal: list[tuple[str, object | None]] = []

        class Journal:
            def prepare_authority_effect(self, *_args: object, **_kwargs: object) -> str:
                journal.append(("prepared", None))
                return "intent"

            def finish_authority_effect(
                self, _intent: object, outcome: str, receipt: object | None = None
            ) -> None:
                journal.append((outcome, receipt))

        capability = self.adapter.bind_durable_commit_capability(
            admission,
            Journal(),
            session_revision=1,
            admission_reread=lambda: admission.__dict__,
            expected_branch=self.adapter._git("symbolic-ref", "--short", "-q", "HEAD"),
            expected_head=expected_head,
        )
        receipt = capability.execute("durable commit")

        self.assertEqual("git", receipt.backend)
        self.assertEqual("op-1:commit", receipt.operation_id)
        self.assertEqual(["prepared", "committed"], [item[0] for item in journal])
        self.assertEqual(receipt, journal[1][1])

    def test_durable_commit_factory_normalizes_invalid_session_revision(self) -> None:
        admission = CommitAdmissionBundle(
            backend="git",
            target="new",
            operation_id="op-1:commit",
            fencing_token="fence",  # noqa: S106
            state_revision=1,
            barrier_id="barrier",
            artifact_identity="artifact",
            manifest_identity="manifest",
            selector_identity="selector",
            runtime_identity="runtime",
        )
        with self.assertRaisesRegex(GitAuthorityError, "durable commit capability binding"):
            self.adapter.bind_durable_commit_capability(
                admission,
                object(),
                session_revision=2,
                admission_reread=lambda: admission.__dict__,
                expected_branch=self.adapter._git("symbolic-ref", "--short", "-q", "HEAD"),
                expected_head=self.adapter._git("rev-parse", "HEAD"),
            )

    def test_durable_commit_factory_classifies_termination_as_rejected(self) -> None:
        admission = CommitAdmissionBundle(
            backend="git",
            target="new",
            operation_id="op-1:commit",
            fencing_token="fence",  # noqa: S106
            state_revision=1,
            barrier_id="barrier",
            artifact_identity="artifact",
            manifest_identity="manifest",
            selector_identity="selector",
            runtime_identity="runtime",
        )
        with (
            patch.object(self.adapter, "bind_commit_capability", return_value=object()),
            patch(
                "tools.authority_mutation.DurableBoundBackendMutation",
                side_effect=KeyboardInterrupt("injected termination"),
            ),
            self.assertRaisesRegex(
                GitAuthorityError, "durable commit capability binding was rejected"
            ),
        ):
            self.adapter.bind_durable_commit_capability(
                admission,
                object(),
                session_revision=1,
                admission_reread=lambda: admission.__dict__,
                expected_branch="master",
                expected_head="a" * 40,
            )

    def test_adapter_binds_isolated_commit_capability_without_enabling_dispatch(self) -> None:
        admission = CommitAdmissionBundle(
            backend="git",
            target="new",
            operation_id="op-1:commit",
            fencing_token="fence",  # noqa: S106
            state_revision=1,
            barrier_id="barrier",
            artifact_identity="artifact",
            manifest_identity="manifest",
            selector_identity="selector",
            runtime_identity="runtime",
        )
        capability = self.adapter.bind_commit_capability(
            admission,
            admission_reread=lambda: admission.__dict__,
            expected_branch="master",
            expected_head=self.adapter._git("rev-parse", "HEAD"),
        )
        self.assertIsInstance(capability, GitCommitCapability)
        with self.assertRaisesRegex(GitAuthorityError, "not implemented"):
            self.adapter.execute("commit", CONTEXT)

    def test_commit_bound_executes_one_exact_head_effect_without_public_dispatch(self) -> None:
        admission = CommitAdmissionBundle(
            backend="git",
            target="new",
            operation_id="op-bound:commit",
            fencing_token="fence",  # noqa: S106
            state_revision=1,
            barrier_id="barrier",
            artifact_identity="artifact",
            manifest_identity="manifest",
            selector_identity="selector",
            runtime_identity="runtime",
        )
        (self.root / "state").write_text("bound\n")
        subprocess.run(["git", "-C", str(self.root), "config", "user.name", "test"], check=True)
        subprocess.run(
            ["git", "-C", str(self.root), "config", "user.email", "test@example"], check=True
        )
        subprocess.run(["git", "-C", str(self.root), "add", "state"], check=True)

        def outputless_commit_runner(
            *args: object, **kwargs: object
        ) -> subprocess.CompletedProcess[str]:
            command = cast(list[str], args[0])
            result = subprocess.run(command, **cast(Any, kwargs))
            if "commit" in command and result.returncode == 0:
                return subprocess.CompletedProcess(command, 0, stdout="", stderr="")
            return result

        before = self.adapter._git("rev-parse", "HEAD")
        result = self.adapter.commit_bound(
            admission,
            "bound Git effect",
            admission_reread=lambda: admission.__dict__,
            expected_branch=self.adapter._git("symbolic-ref", "--short", "-q", "HEAD"),
            expected_head=before,
            runner=outputless_commit_runner,
        )
        self.assertEqual("git", result.backend)
        self.assertEqual("op-bound:commit", result.operation_id)
        self.assertEqual(before, result.before_head)
        self.assertEqual(result.after_head, self.adapter._git("rev-parse", "HEAD"))
        self.assertTrue(result.mutates_authority)
        with self.assertRaisesRegex(GitAuthorityError, "not implemented"):
            self.adapter.execute("commit", CONTEXT)

    def test_adapter_classifies_termination_during_commit_binding_as_rejected(self) -> None:
        admission = CommitAdmissionBundle(
            backend="git",
            target="new",
            operation_id="op-1:commit",
            fencing_token="fence",  # noqa: S106
            state_revision=1,
            barrier_id="barrier",
            artifact_identity="artifact",
            manifest_identity="manifest",
            selector_identity="selector",
            runtime_identity="runtime",
        )
        with (
            patch(
                "tools.git_authority_mutation.GitCommitCapability",
                side_effect=KeyboardInterrupt("injected termination"),
            ),
            self.assertRaisesRegex(GitAuthorityError, "commit capability binding was rejected"),
        ):
            self.adapter.bind_commit_capability(
                admission,
                admission_reread=lambda: admission.__dict__,
                expected_branch=self.adapter._git("symbolic-ref", "--short", "-q", "HEAD"),
                expected_head=self.adapter._git("rev-parse", "HEAD"),
            )

    def test_git_backup_observation_rejects_foreign_adapter_and_path(self) -> None:
        session = GitRollbackSessionState(
            PROJECT, "authority", 1, "fence", "owner", "barrier", "a" * 40, "main"
        )
        with self.assertRaisesRegex(GitAuthorityError, "concrete adapter"):
            GitBackupObservation.from_adapter(cast(Any, object()), session, Path("backup"))
        with self.assertRaisesRegex(GitAuthorityError, "artifact path"):
            GitBackupObservation.from_adapter(self.adapter, session, cast(Any, "backup"))

    def test_adapter_owned_backup_wrappers_restore_valid_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            artifact_root = Path(directory)
            backup = self.adapter.create_backup_bound(artifact_root / "backup", quiesced=True)
            restored = artifact_root / "restored"
            self.adapter.restore_backup_bound(backup, restored)
            self.assertEqual((self.root / "state").read_text(), (restored / "state").read_text())

    def test_generated_backup_executor_verifies_roundtrip_and_preserves_head(self) -> None:
        artifact_root = Path(self.coordination.name) / "artifacts"
        artifact_root.mkdir()
        context = {
            **CONTEXT,
            "operation_id": "campaign",
            "artifact_root": str(artifact_root),
            "destination": str(artifact_root / "backup"),
        }
        operation = {
            "operation_id": "campaign:backup",
            "opcode": "backend.backup",
            "inputs": {
                "backend": "git",
                "selector_ref": context["selector_ref"],
                "expected_state_revision": 1,
                "barrier_id": "barrier",
                "fencing_token": "fence",
                "backup_operation_id": "campaign:backup",
            },
            "timeout_seconds": 300,
            "resources": ["maintenance-barrier", "durable-operation-record"],
            "preconditions": ["previous-phase-complete"],
            "postconditions": ["backup-contract-satisfied"],
            "evidence": ["durable-operation-record"],
            "durable_record": "operation-id-and-outcome",
        }
        before = self.adapter._git("rev-parse", "HEAD")
        result = self.adapter.execute_generated_backup(operation, context)
        self.assertEqual("completed", result["outcome"])
        self.assertTrue(result["backup_verified"])
        self.assertTrue(result["restore_roundtrip_verified"])
        self.assertEqual(before, self.adapter._git("rev-parse", "HEAD"))

    def test_generated_backup_executor_rejects_foreign_destination_and_opcode(self) -> None:
        artifact_root = Path(self.coordination.name) / "artifacts"
        artifact_root.mkdir()
        context = {
            **CONTEXT,
            "artifact_root": str(artifact_root),
            "destination": str(self.root.parent / "outside-backup"),
        }
        operation = {
            "operation_id": "op-1:backup",
            "opcode": "backend.backup",
            "inputs": {
                "backend": "git",
                "selector_ref": CONTEXT["selector_ref"],
                "expected_state_revision": 1,
                "barrier_id": "barrier",
                "fencing_token": "fence",
                "backup_operation_id": "op-1:backup",
            },
            "timeout_seconds": 300,
            "resources": ["maintenance-barrier", "durable-operation-record"],
            "preconditions": ["previous-phase-complete"],
            "postconditions": ["backup-contract-satisfied"],
            "evidence": ["durable-operation-record"],
            "durable_record": "operation-id-and-outcome",
        }
        with self.assertRaisesRegex(GitAuthorityError, "escapes"):
            self.adapter.execute_generated_backup(operation, context)
        operation["opcode"] = "authority.atomic_replace"
        with self.assertRaisesRegex(GitAuthorityError, "unsupported"):
            self.adapter.execute_generated_backup(
                operation, {**context, "destination": str(artifact_root / "backup")}
            )

    def test_generated_backup_executor_rejects_all_identity_and_effect_failures(self) -> None:
        artifact_root = Path(self.coordination.name) / "failure-artifacts"
        artifact_root.mkdir()
        context = {
            **CONTEXT,
            "operation_id": "campaign",
            "artifact_root": str(artifact_root),
            "destination": str(artifact_root / "backup"),
        }
        operation = {
            "operation_id": "campaign:backup",
            "opcode": "backend.backup",
            "inputs": {
                "backend": "git",
                "selector_ref": context["selector_ref"],
                "expected_state_revision": 1,
                "barrier_id": "barrier",
                "fencing_token": "fence",
                "backup_operation_id": "campaign:backup",
            },
            "timeout_seconds": 300,
            "resources": ["maintenance-barrier", "durable-operation-record"],
            "preconditions": ["previous-phase-complete"],
            "postconditions": ["backup-contract-satisfied"],
            "evidence": ["durable-operation-record"],
            "durable_record": "operation-id-and-outcome",
        }
        for field, value in (
            ("resources", ["wrong"]),
            ("preconditions", []),
            ("postconditions", ["wrong"]),
            ("evidence", ["wrong"]),
            ("durable_record", "wrong"),
            ("inputs", {}),
        ):
            candidate: dict[str, Any] = dict(operation)
            candidate[field] = value
            with self.subTest(field=field), self.assertRaises(GitAuthorityError):
                self.adapter.execute_generated_backup(candidate, context)
        for identity_field, identity_value in (
            ("selector_ref", "foreign"),
            ("expected_state_revision", 2),
            ("barrier_id", "foreign"),
            ("fencing_token", "foreign"),
        ):
            identity_candidate: dict[str, Any] = dict(operation)
            identity_candidate["inputs"] = dict(cast(dict[str, Any], operation["inputs"]))
            identity_candidate["inputs"][identity_field] = identity_value
            with (
                self.subTest(field=identity_field),
                self.assertRaisesRegex(GitAuthorityError, "stale"),
            ):
                self.adapter.execute_generated_backup(identity_candidate, context)
        with self.assertRaisesRegex(GitAuthorityError, "forward target"):
            self.adapter.execute_generated_backup(operation, {**context, "target": "rollback"})
        with (
            patch.object(
                self.adapter,
                "_context",
                return_value={**context, "destination": object()},
            ),
            self.assertRaisesRegex(GitAuthorityError, "artifact binding"),
        ):
            self.adapter.execute_generated_backup(operation, context)
        before = {
            **context,
            "phase": "backup",
            "backend_identity_verified": True,
            "git_head": "a" * 40,
            "git_branch": "main",
            "git_clean": True,
            "mutates_authority": False,
        }
        with (
            patch.object(self.adapter, "snapshot", return_value={**before, "git_clean": False}),
            self.assertRaisesRegex(GitAuthorityError, "not clean"),
        ):
            self.adapter.execute_generated_backup(operation, context)
        with (
            patch.object(self.adapter, "snapshot", return_value=before),
            patch.object(self.adapter, "create_backup_bound"),
            patch.object(self.adapter, "verify_backup_artifact", return_value={"verified": False}),
            self.assertRaisesRegex(GitAuthorityError, "verification"),
        ):
            self.adapter.execute_generated_backup(operation, context)
        with (
            patch.object(
                self.adapter, "create_backup_bound", side_effect=GitAuthorityError("injected")
            ),
            self.assertRaisesRegex(GitAuthorityError, "injected"),
        ):
            self.adapter.execute_generated_backup(operation, context)
        with (
            patch.object(self.adapter, "create_backup_bound"),
            patch.object(
                self.adapter,
                "verify_backup_artifact",
                return_value={"verified": True, "commit": "a" * 40},
            ),
            patch.object(self.adapter, "restore_backup_bound", side_effect=RuntimeError("restore")),
            patch.object(self.adapter, "snapshot", return_value=before),
            self.assertRaisesRegex(GitAuthorityError, "failed"),
        ):
            self.adapter.execute_generated_backup(operation, context)
        after = {**before, "git_head": "b" * 40}
        with (
            patch.object(self.adapter, "create_backup_bound"),
            patch.object(
                self.adapter,
                "verify_backup_artifact",
                return_value={"verified": True, "commit": "a" * 40},
            ),
            patch.object(self.adapter, "restore_backup_bound"),
            patch.object(self.adapter, "snapshot", side_effect=(before, after)),
            self.assertRaisesRegex(GitAuthorityError, "identity changed"),
        ):
            self.adapter.execute_generated_backup(operation, context)

    def test_adapter_owned_backup_failure_removes_partial_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            artifact_root = Path(directory)
            destination = artifact_root / "backup"
            with (
                patch(
                    "tools.git_backup._run",
                    side_effect=BackupError("injected Git backup failure"),
                ),
                self.assertRaisesRegex(BackupError, "injected Git backup failure"),
            ):
                self.adapter.create_backup_bound(destination, quiesced=True)
            self.assertFalse(destination.exists())
            self.assertEqual([], list(artifact_root.iterdir()))

    def test_git_backup_observation_requires_verified_typed_result(self) -> None:
        session = GitRollbackSessionState(
            PROJECT, "authority", 1, "fence", "owner", "barrier", "a" * 40, "main"
        )
        observation = GitBackupObservation._from_verified(
            session, {"commit": "a" * 40, "verified": True, "artifact_count": 5}
        )
        self.assertEqual(session, observation.session)
        with self.assertRaisesRegex(TypeError, "verifier"):
            GitBackupObservation()
        for result in (
            {"commit": "b" * 40, "verified": True, "artifact_count": 5},
            {"commit": "a" * 40, "verified": False, "artifact_count": 5},
            {"commit": "a" * 40, "verified": True, "artifact_count": 0},
            {"commit": "a" * 40, "verified": True},
        ):
            with self.subTest(result=result), self.assertRaisesRegex(GitAuthorityError, "invalid"):
                GitBackupObservation._from_verified(session, result)

    def test_git_artifact_binding_is_root_scoped_and_git_specific(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            context = {"artifact_root": str(root), "git_backup_root": str(root / "backup")}
            binding = GitRollbackArtifactBinding.bind(context)
            self.assertEqual(root.resolve(), binding.artifact_root)
            self.assertEqual((root / "backup").resolve(), binding.git_backup_root)
            with self.assertRaisesRegex(GitAuthorityError, "incomplete"):
                GitRollbackArtifactBinding.bind({"artifact_root": str(root)})
            with self.assertRaisesRegex(GitAuthorityError, "outside"):
                GitRollbackArtifactBinding.bind(
                    {"artifact_root": str(root), "git_backup_root": str(root.parent / "foreign")}
                )

    def test_bound_reread_returns_typed_session_without_cas_arguments(self) -> None:
        value = {
            **CONTEXT,
            "phase": "rollback",
            "backend_identity_verified": True,
            "git_head": "a" * 40,
            "git_branch": "main",
            "git_clean": True,
            "mutates_authority": False,
        }
        with patch.object(self.adapter, "snapshot_bound", return_value=value) as reread:
            result = self.adapter.snapshot_bound_reread(
                CONTEXT,
                cast(Any, object()),
                lease=cast(Any, object()),
                admission_recheck=cast(Any, object()),
                expected_branch="main",
                expected_head="a" * 40,
            )
        self.assertIsInstance(result, GitRollbackSessionState)
        self.assertEqual("main", result.git_branch)
        self.assertEqual("a" * 40, result.git_head)
        self.assertEqual("rollback", reread.call_args.args[0])

    @staticmethod
    def _lease() -> AdmissionLease:
        return AdmissionLease(PROJECT, "authority", "fence", "owner", "barrier", 1)

    @staticmethod
    def _session_identity() -> BarrierSessionIdentity:
        record: dict[str, object] = {
            "schema_version": 1,
            "project_id": PROJECT,
            "attempt_id": "attempt-1",
            "state_revision": 1,
            "authority_revision_at_acquire": "authority",
            "durable_barrier_id": "barrier",
            "fencing_token": "fence",
            "fencing_owner": "owner",
            "identity_digest": "0" * 64,
        }
        record["identity_digest"] = canonical_barrier_session_digest(record)
        return BarrierSessionIdentity.from_record(record)

    def setUp(self) -> None:
        self.directory = tempfile.TemporaryDirectory()
        self.root = Path(self.directory.name)
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)
        (self.root / "state").write_text("clean\n")
        subprocess.run(["git", "-C", str(self.root), "add", "state"], check=True)
        subprocess.run(
            [
                "git",
                "-C",
                str(self.root),
                "-c",
                "user.name=test",
                "-c",
                "user.email=test@example",
                "commit",
                "-qm",
                "init",
            ],
            check=True,
        )
        self.root.chmod(0o700)
        (self.root / ".git").chmod(0o700)
        self.adapter = GitAuthorityAdapter(self.root)
        self.coordination = tempfile.TemporaryDirectory()
        coord = Path(self.coordination.name)
        authority = coord / "authority.sqlite"
        self.authority_tasks = coord / "tasks"
        self.authority_tasks.mkdir()
        authority_meta = {
            "schema_version": 1,
            "id": "AR-0001",
            "title": "Authority fixture task",
            "status": "open",
            "priority": "P1",
            "summary": "Ready.",
            "next_action": "Exercise the bound mutation route.",
            "task_revision": 1,
            "updated_at": "2026-09-16T00:00:00+00:00",
            "owner": "",
            "claim_expires": "",
            "worktree_key": "worker-1",
            "branch": "",
            "checkpoint_commit": "",
            "plan": "",
            "depends_on": [],
        }
        self.authority_binding = {
            "project_id": PROJECT,
            "state_repository": "owner/state",
            "product_repository": "owner/product",
        }
        create_database(
            authority,
            self.authority_binding,
            [(Path("AR-0001-authority-fixture.md"), authority_meta, "# Authority fixture\n")],
            imported_at="2026-09-16T00:00:00+00:00",
            source_backend="git",
            source_checkpoint="a" * 40,
        )
        control = coord / "control.sqlite"
        store = SQLiteRollbackControlStore(control, PROJECT, authority)
        self.control_store = store
        marker = coord / "authority-marker.json"
        lifecycle = coord / "authority-lifecycle.json"
        authority_lock = coord / "authority.lock"
        binding = coord / "control-binding.json"
        provision(authority, marker, lifecycle, authority_lock, PROJECT)
        provision_control_binding(control, binding, store.control_lock_path, PROJECT)
        fence = MutationFence(
            authority,
            marker,
            lifecycle,
            authority_lock,
            control,
            binding,
            store.control_lock_path,
        )
        self.session = SQLiteBarrierSessionStore(store, lambda: "authority")
        self.session.create(self._session_identity())
        self.lease = self._lease()
        self.recheck = validate_recheck(
            self.lease,
            project_id=PROJECT,
            authority_revision="authority",
            fencing_token="fence",  # noqa: S106
            fencing_owner="owner",
            durable_barrier_id="barrier",
            revision=1,
        )
        self.scope = LockDomainScope.bind(self.session, fence, self.lease, self.recheck, locked)

    def tearDown(self) -> None:
        self.coordination.cleanup()
        self.directory.cleanup()

    def test_sqlite_backend_binding_captures_immutable_durable_identity(self) -> None:
        binding = SQLiteBackendBinding.bind(self.control_store, self.session)
        self.assertEqual(binding.project_id, PROJECT)
        self.assertEqual(binding.fencing_owner, "owner")
        self.assertEqual(binding.fence, "fence")
        self.assertEqual(binding.revision, 1)
        with self.assertRaises(TypeError):
            SQLiteBackendBinding(self.control_store, self.session, self.session.snapshot())
        with self.assertRaises(AttributeError):
            binding._owner = "forged"
        # Binding is deliberately not an authorization or mutation surface.
        self.assertFalse(hasattr(binding, "mutate"))
        self.assertFalse(hasattr(binding, "authorize"))
        binding.assert_current()

    def test_live_upgrade_binding_uses_real_git_adapter_and_durable_scope(self) -> None:
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

        contract = generate(
            {
                "operation_id": "op-1",
                "backend": "git",
                "selector_ref": ".runtime/runtime-selector.json",
                "expected_state_revision": 1,
                "barrier_id": "barrier",
                "fencing_token": "fence",
                "from": release("v0.3.5", "a"),
                "to": release("v0.3.6", "b"),
            }
        )
        runtime: dict[str, object] = {
            "schema_version": 2,
            "backend": "git",
            "project_id": PROJECT,
            "operation_id": "op-1",
            "state_revision": 1,
            "authority_revision": "authority",
            "fencing_token": "fence",
            "fencing_owner": "owner",
            "durable_barrier_id": "barrier",
            "artifact_root": str(Path(self.coordination.name) / "artifacts"),
            "source": str(Path(self.coordination.name) / "artifacts" / "source"),
            "destination": str(Path(self.coordination.name) / "artifacts" / "destination"),
            "manifest": str(Path(self.coordination.name) / "artifacts" / "manifest.json"),
            "selector_ref": ".runtime/runtime-selector.json",
            "target": "rollback",
        }
        runtime["barrier_identity_digest"] = canonical_barrier_digest(runtime)
        runtime["envelope_digest"] = canonical_envelope_digest(runtime)
        identity = self._session_identity()
        forward = BarrierChildIdentity.bind(identity, "op-1:forward", "new")
        rollback = BarrierChildIdentity.bind(identity, "op-1", "rollback")
        self.session.bind_child(1, forward)
        self.session.bind_child(2, rollback)
        scope = LockDomainScope.bind(
            self.session, self.scope._authority_fence, self.lease, self.recheck, locked
        )
        binding = UpgradeRuntimeBinding.bind(
            contract, runtime, session_identity_digest=identity.identity_digest
        )
        live = LiveUpgradeBinding.bind(
            binding,
            self.session.snapshot(),
            scope,
            self.lease,
            self.recheck,
            self.adapter,
            expected_git_repository=self.root,
        )
        evidence = live.reread_backend(
            expected_branch=self.adapter._git("symbolic-ref", "--short", "-q", "HEAD"),
            expected_head=self.adapter._git("rev-parse", "HEAD"),
        )
        self.assertEqual("git", evidence["backend"])
        self.assertTrue(evidence["git_clean"])
        self.assertFalse(evidence["mutates_authority"])
        with tempfile.TemporaryDirectory() as foreign_directory:
            foreign_root = Path(foreign_directory)
            subprocess.run(["git", "init", "-q", str(foreign_root)], check=True)
            (foreign_root / "foreign-state").write_text("foreign\n")
            subprocess.run(["git", "-C", str(foreign_root), "add", "foreign-state"], check=True)
            subprocess.run(
                [
                    "git",
                    "-C",
                    str(foreign_root),
                    "-c",
                    "user.name=test",
                    "-c",
                    "user.email=test@example",
                    "commit",
                    "-qm",
                    "foreign",
                ],
                check=True,
            )
            with self.assertRaisesRegex(UpgradeBindingError, "foreign repository"):
                LiveUpgradeBinding.bind(
                    binding,
                    self.session.snapshot(),
                    scope,
                    self.lease,
                    self.recheck,
                    GitAuthorityAdapter(foreign_root),
                    expected_git_repository=self.root,
                )

    def test_sqlite_backend_binding_rejects_foreign_session_and_descriptor_swap(self) -> None:
        other_path = Path(self.coordination.name) / "foreign-control.sqlite"
        other_store = SQLiteRollbackControlStore(
            other_path, PROJECT, self.control_store.authority_path
        )
        with self.assertRaises(ValueError):
            SQLiteBackendBinding.bind(self.control_store, SQLiteBarrierSessionStore(other_store))
        binding = SQLiteBackendBinding.bind(self.control_store, self.session)
        original_path = self.control_store.control_store_path
        displaced = original_path.with_name("displaced-control.sqlite")
        original_path.rename(displaced)
        original_path.write_bytes(b"foreign descriptor")
        try:
            with self.assertRaisesRegex(RuntimeError, "reread failed"):
                binding.assert_current()
        finally:
            original_path.unlink()
            displaced.rename(original_path)

    def test_sqlite_backend_binding_rejects_untrusted_inputs_and_backend_mismatch(self) -> None:
        with self.assertRaises(TypeError):
            SQLiteBackendBinding.bind(object(), object())
        inactive_path = Path(self.coordination.name) / "inactive-control.sqlite"
        inactive = SQLiteRollbackControlStore(
            inactive_path, PROJECT, self.control_store.authority_path
        )
        with self.assertRaises(ValueError):
            SQLiteBackendBinding.bind(inactive, SQLiteBarrierSessionStore(inactive))
        binding = SQLiteBackendBinding.bind(self.control_store, self.session)
        backend_meta = {
            "project_id": PROJECT,
            "state_repository": "owner/state",
            "product_repository": "owner/product",
        }
        with self.assertRaisesRegex(ValueError, "adapter factory"):
            SQLiteBackend(
                binding.path,
                backend_meta,
                Path(self.coordination.name),
                backend_binding=cast(Any, object()),
            )
        with self.assertRaises(ValueError):
            SQLiteBackend(
                binding.path.with_name("alias.sqlite"),
                backend_meta,
                Path(self.coordination.name),
                backend_binding=binding,
            )

    def _bound_authority_backend(self) -> SQLiteBackend:
        control = SQLiteBackendBinding.bind(self.control_store, self.session)
        authority_path = self.control_store.authority_path
        assert authority_path is not None
        authority = SQLiteAuthorityBinding.bind(control, authority_path, self.scope)
        return bind_sqlite_backend(
            authority_path,
            self.authority_binding,
            self.authority_tasks,
            authority,
            self.scope,
        )

    def test_scope_bound_authority_writer_hides_raw_backend_and_holds_locks(self) -> None:
        control = SQLiteBackendBinding.bind(self.control_store, self.session)
        authority_path = self.control_store.authority_path
        assert authority_path is not None
        authority = SQLiteAuthorityBinding.bind(control, authority_path, self.scope)
        writer = bind_sqlite_authority_writer(
            authority_path,
            self.authority_binding,
            self.authority_tasks,
            authority,
            self.scope,
        )
        self.assertTrue(hasattr(writer, "mutate"))
        self.assertFalse(hasattr(writer, "backend"))

        def transition(
            meta: dict[str, Any], _tasks: list[tuple[Path, dict[str, Any], str]]
        ) -> tuple[str, str]:
            meta["summary"] = "scope-bound"
            return "bound writer", "# Authority fixture\n"

        writer.mutate("AR-0001", 1, "update", "2026-09-16T00:00:00+00:00", transition)
        self.assertEqual(
            "scope-bound", self._bound_authority_backend().load_tasks()[0][1]["summary"]
        )

    def test_scope_bound_authority_writer_rejects_unbound_capabilities(self) -> None:
        control = SQLiteBackendBinding.bind(self.control_store, self.session)
        authority_path = self.control_store.authority_path
        assert authority_path is not None
        authority = SQLiteAuthorityBinding.bind(control, authority_path, self.scope)
        backend = self._bound_authority_backend()

        with self.assertRaisesRegex(TypeError, "issued by its factory"):
            sqlite_storage.SQLiteAuthorityWriteAdapter(backend, object())
        with self.assertRaisesRegex(TypeError, "LockDomainScope"):
            bind_sqlite_authority_writer(
                authority_path,
                self.authority_binding,
                self.authority_tasks,
                authority,
                object(),
            )
        with self.assertRaisesRegex(TypeError, "SQLiteAuthorityBinding"):
            bind_sqlite_authority_writer(
                authority_path,
                self.authority_binding,
                self.authority_tasks,
                cast(Any, object()),
                self.scope,
            )
        with self.assertRaisesRegex(ValueError, "path does not match"):
            bind_sqlite_authority_writer(
                authority_path.with_name("other.sqlite"),
                self.authority_binding,
                self.authority_tasks,
                authority,
                self.scope,
            )

    def test_bound_backend_routes_use_initialized_authority_schema(self) -> None:
        control = SQLiteBackendBinding.bind(self.control_store, self.session)
        authority_path = self.control_store.authority_path
        assert authority_path is not None
        authority = SQLiteAuthorityBinding.bind(control, authority_path, self.scope)
        writer = bind_sqlite_authority_writer(
            authority_path,
            self.authority_binding,
            self.authority_tasks,
            authority,
            self.scope,
        )
        session_before = self.session.snapshot()

        def update_summary(
            meta: dict[str, Any], _tasks: list[tuple[Path, dict[str, Any], str]]
        ) -> tuple[str, str]:
            meta["summary"] = "Mutated through the bound authority route."
            return "bound mutation", "# Authority fixture\n\nMutation committed.\n"

        writer.mutate(
            "AR-0001",
            1,
            "update",
            "2026-09-16T00:01:00+00:00",
            update_summary,
        )

        writer.update_observations(
            {"worker-1": {"branch": "feature/test", "head": "b" * 40, "dirty": False}},
            "2026-09-16T00:02:00+00:00",
        )
        writer.append_command_result(
            "AR-0001",
            "worker",
            "c" * 64,
            0,
            "EXIT",
            "2026-09-16T00:03:00+00:00",
        )

        backend = self._bound_authority_backend()
        tasks = backend.load_tasks()
        self.assertEqual(1, len(tasks))
        _, meta, body = tasks[0]
        self.assertEqual(3, meta["task_revision"])
        self.assertEqual("Mutated through the bound authority route.", meta["summary"])
        self.assertEqual("feature/test", meta["observed_branch"])
        self.assertEqual("b" * 40, meta["observed_head"])
        self.assertFalse(meta["observed_dirty"])
        self.assertEqual("# Authority fixture\n\nMutation committed.\n", body)
        projected: list[list[tuple[Path, dict[str, Any], str]]] = []
        selector_calls: list[str] = []
        writer.retire(projected.append, lambda: selector_calls.append("retired"))
        self.assertEqual("AR-0001", projected[0][0][1]["id"])
        self.assertEqual(["retired"], selector_calls)
        self.assertEqual(session_before, self.session.snapshot())
        self.assertFalse(self.session.operation_owned_by_current_thread)
        with closing(sqlite3.connect(backend.path)) as connection, connection:
            state = connection.execute("SELECT value FROM metadata WHERE key='state'").fetchone()
            events = connection.execute(
                "SELECT revision, kind, note FROM events WHERE task_id=? ORDER BY revision",
                ("AR-0001",),
            ).fetchall()
            result = connection.execute(
                "SELECT owner, argv_sha256, returncode, classification "
                "FROM command_results WHERE task_id=?",
                ("AR-0001",),
            ).fetchone()
        self.assertEqual(("retired",), state)
        self.assertEqual((2, "update", "bound mutation"), events[1])
        self.assertEqual((3, "reconcile", "Recorded live worktree state."), events[2])
        self.assertEqual(("worker", "c" * 64, 0, "EXIT"), result)

    def test_bound_backend_authority_replacement_rolls_back_without_publication(self) -> None:
        backend = self._bound_authority_backend()
        binding = cast(SQLiteAuthorityBinding, backend.backend_binding)
        authority_path = binding.path
        displaced = authority_path.with_name("displaced-authority.sqlite")
        original_assert = SQLiteAuthorityBinding.assert_current
        rereads = 0

        def replace_before_precommit(current: SQLiteAuthorityBinding) -> None:
            nonlocal rereads
            rereads += 1
            if rereads == 3:
                authority_path.rename(displaced)
                authority_path.write_bytes(b"foreign authority")
            original_assert(current)

        def update_summary(
            meta: dict[str, Any], _tasks: list[tuple[Path, dict[str, Any], str]]
        ) -> tuple[str, str]:
            meta["summary"] = "must roll back"
            return "must roll back", "# Must not publish\n"

        try:
            with (
                patch.object(
                    SQLiteAuthorityBinding,
                    "assert_current",
                    autospec=True,
                    side_effect=replace_before_precommit,
                ),
                self.assertRaisesRegex(
                    RuntimeError, "SQLite backend binding reread failed"
                ) as caught,
            ):
                backend.mutate(
                    "AR-0001",
                    1,
                    "update",
                    "2026-09-16T00:01:00+00:00",
                    update_summary,
                )
        finally:
            authority_path.unlink(missing_ok=True)
            if displaced.exists():
                displaced.rename(authority_path)

        self.assertEqual(3, rereads)
        self.assertIsInstance(caught.exception.__cause__, ControlStoreError)
        self.assertEqual("authority descriptor identity changed", str(caught.exception.__cause__))

        tasks = backend.load_tasks()
        self.assertEqual(1, tasks[0][1]["task_revision"])
        self.assertEqual("Ready.", tasks[0][1]["summary"])
        self.assertEqual("# Authority fixture\n", tasks[0][2])
        self.assertFalse(self.session.operation_owned_by_current_thread)
        with closing(sqlite3.connect(authority_path)) as connection, connection:
            events = connection.execute(
                "SELECT revision, kind FROM events WHERE task_id=? ORDER BY revision",
                ("AR-0001",),
            ).fetchall()
        self.assertEqual([(1, "import")], events)

    def test_sqlite_control_binding_rejects_stale_durable_variants(self) -> None:
        binding = SQLiteBackendBinding.bind(self.control_store, self.session)
        self.assertEqual("fence", binding.fencing_token)
        self.assertEqual(self.control_store._control_identity, binding.descriptor_identity)

        original_descriptor = self.control_store._control_identity
        self.control_store._control_identity = (original_descriptor[0], original_descriptor[1] + 1)
        try:
            with self.assertRaisesRegex(RuntimeError, "descriptor identity changed"):
                binding.assert_current()
        finally:
            self.control_store._control_identity = original_descriptor

        with (
            patch.object(self.session, "snapshot", return_value=None),
            self.assertRaisesRegex(RuntimeError, "session is no longer active"),
        ):
            binding.assert_current()

        object.__setattr__(binding, "_revision", 2)
        try:
            with self.assertRaisesRegex(RuntimeError, "session identity changed"):
                binding.assert_current()
        finally:
            object.__setattr__(binding, "_revision", 1)

    def test_sqlite_authority_binding_rejects_unsafe_rereads(self) -> None:
        control = SQLiteBackendBinding.bind(self.control_store, self.session)
        authority_path = self.control_store.authority_path
        assert authority_path is not None
        authority = SQLiteAuthorityBinding.bind(control, authority_path, self.scope)
        authority_status = authority_path.stat()
        self.assertEqual(
            (authority_status.st_dev, authority_status.st_ino), authority.descriptor_identity
        )
        with self.assertRaises(TypeError):
            SQLiteAuthorityBinding(
                control,
                authority_path,
                authority.descriptor_identity,
                (authority_path.parent.stat().st_dev, authority_path.parent.stat().st_ino),
                object(),
            )
        with self.assertRaises(AttributeError):
            authority._path = authority_path.with_name("forged.sqlite")

        displaced = authority_path.with_name("displaced-authority.sqlite")
        with patch.object(SQLiteBackendBinding, "assert_current", return_value=None):
            authority_path.rename(displaced)
            authority_path.symlink_to(displaced)
            try:
                with self.assertRaisesRegex(RuntimeError, "descriptor is a symlink"):
                    authority.assert_current()
            finally:
                authority_path.unlink()
                displaced.rename(authority_path)

            authority_path.rename(displaced)
            try:
                with self.assertRaisesRegex(RuntimeError, "descriptor reread failed"):
                    authority.assert_current()
            finally:
                displaced.rename(authority_path)

            authority_path.rename(displaced)
            authority_path.write_bytes(b"replacement")
            try:
                with self.assertRaisesRegex(RuntimeError, "descriptor identity changed"):
                    authority.assert_current()
            finally:
                authority_path.unlink()
                displaced.rename(authority_path)

    def test_sqlite_authority_binding_rejects_scope_authority_mismatch(self) -> None:
        control = SQLiteBackendBinding.bind(self.control_store, self.session)
        authority_path = self.control_store.authority_path
        assert authority_path is not None
        foreign_authority = authority_path.with_name("foreign-valid-authority.sqlite")
        with (
            closing(sqlite3.connect(authority_path)) as source,
            closing(sqlite3.connect(foreign_authority)) as destination,
            source,
            destination,
        ):
            source.backup(destination)

        with self.assertRaisesRegex(ValueError, "does not match the admission scope authority"):
            SQLiteAuthorityBinding.bind(control, foreign_authority, self.scope)

        self.assertEqual(authority_path, self.scope._authority_fence.authority)
        self.assertEqual(
            "AR-0001",
            SQLiteBackend(
                foreign_authority, self.authority_binding, self.authority_tasks
            ).load_tasks()[0][1]["id"],
        )

    def test_sqlite_backend_factory_rejects_foreign_pairings(self) -> None:
        control = SQLiteBackendBinding.bind(self.control_store, self.session)
        authority_path = self.control_store.authority_path
        assert authority_path is not None
        authority = SQLiteAuthorityBinding.bind(control, authority_path, self.scope)
        foreign_store = SQLiteRollbackControlStore(
            Path(self.coordination.name) / "foreign-factory-control.sqlite",
            PROJECT,
            authority_path,
        )

        original_control = self.scope._session_store._control
        self.scope._session_store._control = foreign_store
        try:
            with self.assertRaisesRegex(ValueError, "foreign control store"):
                SQLiteAuthorityBinding.bind(control, authority_path, self.scope)

            with self.assertRaisesRegex(ValueError, "foreign control store"):
                bind_sqlite_backend(
                    authority_path,
                    self.authority_binding,
                    self.authority_tasks,
                    authority,
                    self.scope,
                )
        finally:
            self.scope._session_store._control = original_control

        original_fence_control = self.scope._authority_fence.control_store
        self.scope._authority_fence.control_store = foreign_store.control_store_path
        try:
            with self.assertRaisesRegex(ValueError, "foreign authority fence"):
                bind_sqlite_backend(
                    authority_path,
                    self.authority_binding,
                    self.authority_tasks,
                    authority,
                    self.scope,
                )
        finally:
            self.scope._authority_fence.control_store = original_fence_control

    def test_sqlite_backend_private_capability_rejects_invalid_construction(self) -> None:
        control = SQLiteBackendBinding.bind(self.control_store, self.session)
        authority_path = self.control_store.authority_path
        assert authority_path is not None
        authority = SQLiteAuthorityBinding.bind(control, authority_path, self.scope)
        sentinel = sqlite_storage._FACTORY_SENTINEL

        with self.assertRaisesRegex(TypeError, "SQLite binding capability"):
            SQLiteBackend(
                authority_path,
                self.authority_binding,
                self.authority_tasks,
                mutation_scope=nullcontext,
                backend_binding=cast(Any, object()),
                _admission_capability=sentinel,
            )
        with self.assertRaisesRegex(ValueError, "different database"):
            SQLiteBackend(
                authority_path.with_name("alias.sqlite"),
                self.authority_binding,
                self.authority_tasks,
                mutation_scope=nullcontext,
                backend_binding=authority,
                _admission_capability=sentinel,
            )
        with self.assertRaisesRegex(ValueError, "provisioned mutation scope"):
            SQLiteBackend(
                authority_path,
                self.authority_binding,
                self.authority_tasks,
                backend_binding=authority,
                _admission_capability=sentinel,
            )
        control_only = SQLiteBackend(
            control.path,
            self.authority_binding,
            self.authority_tasks,
            mutation_scope=nullcontext,
            backend_binding=control,
            _admission_capability=sentinel,
        )
        with (
            self.assertRaisesRegex(RuntimeError, "dual authority binding"),
            control_only._transaction(),
        ):
            self.fail("control-only mutation must reject before opening SQLite")

    def test_bound_backend_rejects_corrupt_rows_and_missing_routes(self) -> None:
        backend = self._bound_authority_backend()
        with closing(sqlite3.connect(backend.path)) as connection, connection:
            original_json = connection.execute(
                "SELECT meta_json FROM tasks WHERE id=?", ("AR-0001",)
            ).fetchone()[0]
            connection.execute("PRAGMA ignore_check_constraints=ON")
            connection.execute("UPDATE tasks SET meta_json=? WHERE id=?", ("{", "AR-0001"))
        with self.assertRaisesRegex(sqlite_storage.StorageCorruptionError, "invalid task JSON"):
            backend.load_tasks()

        with closing(sqlite3.connect(backend.path)) as connection, connection:
            connection.execute(
                "UPDATE tasks SET meta_json=?, revision=? WHERE id=?",
                (original_json, 2, "AR-0001"),
            )
        with self.assertRaisesRegex(
            sqlite_storage.StorageCorruptionError, "revision columns disagree"
        ):
            backend.load_tasks()

        with closing(sqlite3.connect(backend.path)) as connection, connection:
            connection.execute("UPDATE tasks SET revision=? WHERE id=?", (1, "AR-0001"))
        with self.assertRaisesRegex(RuntimeError, "unknown task AR-9999"):
            backend.mutate(
                "AR-9999",
                1,
                "update",
                "2026-09-16T00:01:00+00:00",
                lambda _meta, _tasks: ("unused", "unused"),
            )
        backend.update_observations(
            {"different-worker": {"branch": "main", "head": "d" * 40, "dirty": False}},
            "2026-09-16T00:02:00+00:00",
        )
        self.assertEqual(1, backend.load_tasks()[0][1]["task_revision"])
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_sqlite_storage_prerequisite_and_connection_failures_are_bounded(self) -> None:
        authority_path = cast(Path, self.control_store.authority_path)
        with patch.object(Path, "read_text", side_effect=OSError("unavailable")):
            self.assertIsNone(sqlite_storage._mount_type(authority_path))
        self.assertIsNone(
            sqlite_storage._mount_type(
                authority_path,
                "short - ext4 /dev/test / rw",
            )
        )
        with (
            patch.object(sqlite3, "sqlite_version_info", (3, 36, 0)),
            self.assertRaisesRegex(RuntimeError, "SQLite 3.37 or newer"),
        ):
            sqlite_storage._require_database(authority_path)

        backend = SQLiteBackend(
            authority_path,
            self.authority_binding,
            self.authority_tasks,
        )
        non_wal = MagicMock()
        non_wal.execute.return_value.fetchone.return_value = ("delete",)
        with (
            patch.object(sqlite3, "connect", return_value=non_wal),
            self.assertRaisesRegex(RuntimeError, "journal mode is not WAL"),
        ):
            backend._connect()
        non_wal.close.assert_called_once()

        failed = MagicMock()
        failed.execute.side_effect = sqlite3.OperationalError("database is busy")
        with (
            patch.object(sqlite3, "connect", return_value=failed),
            self.assertRaises(sqlite_storage.StorageContentionError),
        ):
            backend._connect()
        failed.close.assert_called_once()

        failed_target = Path(self.coordination.name) / "failed-create.sqlite"
        with (
            patch.object(sqlite3, "connect", side_effect=sqlite3.OperationalError("open failed")),
            self.assertRaisesRegex(RuntimeError, "SQLITE_ERROR"),
        ):
            create_database(
                failed_target,
                self.authority_binding,
                [],
                imported_at="2026-09-16T00:00:00+00:00",
                source_backend="git",
                source_checkpoint="e" * 40,
            )
        self.assertFalse(failed_target.exists())

    def test_sqlite_bound_routes_reject_conflicts_inactive_and_corrupt_state(self) -> None:
        backend = self._bound_authority_backend()
        with closing(sqlite3.connect(backend.path)) as connection, connection:
            connection.execute(
                "CREATE TRIGGER suppress_task_update BEFORE UPDATE ON tasks "
                "BEGIN SELECT RAISE(IGNORE); END"
            )
        with self.assertRaisesRegex(RuntimeError, "exact-revision update lost its fence"):
            backend.mutate(
                "AR-0001",
                1,
                "update",
                "2026-09-16T00:01:00+00:00",
                lambda _meta, _tasks: ("suppressed", "# Suppressed\n"),
            )
        with self.assertRaisesRegex(RuntimeError, "observation update lost its fence"):
            backend.update_observations(
                {"worker-1": {"branch": "main", "head": "f" * 40, "dirty": False}},
                "2026-09-16T00:02:00+00:00",
            )

        with closing(sqlite3.connect(backend.path)) as connection, connection:
            connection.execute("DROP TRIGGER suppress_task_update")
            connection.execute("PRAGMA foreign_keys=OFF")
            connection.execute(
                "INSERT INTO dependencies(task_id, dependency_id) VALUES (?, ?)",
                ("AR-0001", "AR-9999"),
            )
        self.assertIn("SQLITE_CORRUPT: foreign-key violations", backend.integrity_errors())

        with closing(sqlite3.connect(backend.path)) as connection, connection:
            connection.execute(
                "DELETE FROM dependencies WHERE task_id=? AND dependency_id=?",
                ("AR-0001", "AR-9999"),
            )
        with (
            patch.object(backend, "_load", side_effect=sqlite3.OperationalError("malformed")),
            self.assertRaises(sqlite_storage.StorageCorruptionError),
        ):
            backend.load_tasks()

        with closing(sqlite3.connect(backend.path)) as connection, connection:
            connection.execute("UPDATE metadata SET value='retired' WHERE key='state'")
        with (
            patch.object(backend, "_verify_binding", return_value=None),
            self.assertRaisesRegex(RuntimeError, "SQLITE_BACKEND_INACTIVE"),
            backend._transaction(),
        ):
            self.fail("inactive authority must reject before yielding")
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_bound_backend_mutation_boundary_rereads_identity(self) -> None:
        control = SQLiteBackendBinding.bind(self.control_store, self.session)
        authority_path = self.control_store.authority_path
        assert authority_path is not None
        binding = SQLiteAuthorityBinding.bind(control, authority_path, self.scope)
        backend_meta = {
            "project_id": PROJECT,
            "state_repository": "owner/state",
            "product_repository": "owner/product",
        }
        with self.assertRaisesRegex(ValueError, "adapter factory"):
            SQLiteBackend(
                binding.path,
                backend_meta,
                Path(self.coordination.name),
                backend_binding=binding,
            )
        backend = bind_sqlite_backend(
            binding.path, backend_meta, Path(self.coordination.name), binding, self.scope
        )
        backend._assert_mutation_binding()
        with (
            patch.object(
                SQLiteBackendBinding, "assert_current", side_effect=RuntimeError("stale session")
            ),
            self.assertRaisesRegex(RuntimeError, "stale session"),
        ):
            backend._assert_mutation_binding()

    def test_sqlite_backend_factory_requires_ordered_adapter_scope(self) -> None:
        binding = SQLiteBackendBinding.bind(self.control_store, self.session)
        backend_meta = {
            "project_id": PROJECT,
            "state_repository": "owner/state",
            "product_repository": "owner/product",
        }
        with self.assertRaises(TypeError):
            bind_sqlite_backend(
                binding.path, backend_meta, Path(self.coordination.name), binding, nullcontext()
            )
        with self.assertRaises(TypeError):
            bind_sqlite_backend(
                binding.path, backend_meta, Path(self.coordination.name), binding, self.scope
            )

    def test_sqlite_authority_binding_captures_and_rechecks_dual_identity(self) -> None:
        control = SQLiteBackendBinding.bind(self.control_store, self.session)
        authority_path = self.control_store.authority_path
        assert authority_path is not None
        authority = SQLiteAuthorityBinding.bind(control, authority_path, self.scope)
        authority.assert_current()
        self.assertEqual(authority.path, authority_path.absolute())
        bound_backend = bind_sqlite_backend(
            authority.path,
            {
                "project_id": PROJECT,
                "state_repository": "owner/state",
                "product_repository": "owner/product",
            },
            Path(self.coordination.name),
            authority,
            self.scope,
        )
        bound_backend._assert_mutation_binding()
        with self.assertRaises(TypeError):
            SQLiteAuthorityBinding.bind(control, authority_path, nullcontext())
        with self.assertRaises(TypeError):
            SQLiteAuthorityBinding.bind(cast(Any, object()), authority_path, self.scope)
        missing = authority_path.with_name("missing-authority.sqlite")
        original_authority = self.scope._authority_fence.authority
        self.scope._authority_fence.authority = missing
        try:
            with self.assertRaisesRegex(ValueError, "regular non-symlink"):
                SQLiteAuthorityBinding.bind(control, missing, self.scope)
        finally:
            self.scope._authority_fence.authority = original_authority
        symlink = authority_path.with_name("authority-link.sqlite")
        symlink.symlink_to(authority_path)
        self.scope._authority_fence.authority = symlink
        try:
            with self.assertRaisesRegex(ValueError, "regular non-symlink"):
                SQLiteAuthorityBinding.bind(control, symlink, self.scope)
        finally:
            self.scope._authority_fence.authority = original_authority
            symlink.unlink()
        original_control = self.scope._authority_fence.control_store
        self.scope._authority_fence.control_store = Path(self.coordination.name) / "foreign.sqlite"
        try:
            with self.assertRaisesRegex(ValueError, "foreign control"):
                SQLiteAuthorityBinding.bind(control, authority_path, self.scope)
        finally:
            self.scope._authority_fence.control_store = original_control
        displaced = authority.path.with_name("displaced-authority.sqlite")
        authority.path.rename(displaced)
        authority.path.write_bytes(b"foreign")
        try:
            with self.assertRaisesRegex(RuntimeError, "reread failed"):
                authority.assert_current()
        finally:
            authority.path.unlink()
            displaced.rename(authority.path)

    def test_engine_bound_rollback_inspection_uses_real_scope_and_preserves_journal(self) -> None:
        context = {**CONTEXT, "operation_id": "op-real-git-inspection", "target": "new"}
        artifact_root = Path(self.coordination.name) / "artifacts"
        artifact_root.mkdir()
        context.update(
            {
                "artifact_root": str(artifact_root),
                "destination": str(artifact_root / "destination"),
            }
        )
        backup = create_backup(self.root, artifact_root / "git-backup", quiesced=True)
        context.update({"manifest": str(backup / "manifest.json")})
        context["barrier_identity_digest"] = canonical_barrier_digest(context)
        context["envelope_digest"] = canonical_envelope_digest(context)
        observed = self.adapter.snapshot("discover", context)
        context["target"] = "new"
        engine = UpgradeEngine(
            str(context["operation_id"]),
            Path(self.coordination.name) / "engine-journal.json",
            context,
            backend_adapter=self.adapter,
            rollback_bound_verifier=BoundRollbackCapability.bind(
                PhaseContext(**cast(dict[str, Any], context)),
                self.adapter,
                self.scope,
                lease=self.lease,
                admission_recheck=self.recheck,
                expected_branch=str(observed["git_branch"]),
                expected_head=str(observed["git_head"]),
            ),
        )
        engine.plan()
        before = (Path(self.coordination.name) / "engine-journal.json").read_bytes()
        result = engine.inspect_rollback_bound()
        self.assertFalse(result["rollback_context_verified"])
        self.assertEqual(
            before, (Path(self.coordination.name) / "engine-journal.json").read_bytes()
        )
        self.assertFalse(self.session.operation_owned_by_current_thread)
        with engine._exclusive():
            pass

    def test_runtime_binding_rereads_real_git_backend_inside_scope(self) -> None:
        context = {**CONTEXT, "operation_id": "op-real-git-binding", "target": "rollback"}
        artifact_root = Path(self.coordination.name) / "binding-artifacts"
        artifact_root.mkdir()
        context.update(
            {
                "artifact_root": str(artifact_root),
                "destination": str(artifact_root / "destination"),
                "manifest": str(artifact_root / "manifest.json"),
            }
        )
        context["barrier_identity_digest"] = canonical_barrier_digest(context)
        context["envelope_digest"] = canonical_envelope_digest(context)
        contract = generate(
            {
                "operation_id": context["operation_id"],
                "backend": "git",
                "selector_ref": context["selector_ref"],
                "expected_state_revision": context["state_revision"],
                "barrier_id": context["durable_barrier_id"],
                "fencing_token": context["fencing_token"],
                "from": {
                    "version": "v0.3.5",
                    "source_commit": "a" * 40,
                    "tag_ref": "refs/tags/v0.3.5",
                    "tag_object": "b" * 40,
                    "signature_sha256": "c" * 64,
                    "trust_policy_sha256": "d" * 64,
                    "vendor_manifest_sha256": "e" * 64,
                },
                "to": {
                    "version": "v0.3.6",
                    "source_commit": "f" * 40,
                    "tag_ref": "refs/tags/v0.3.6",
                    "tag_object": "0" * 40,
                    "signature_sha256": "1" * 64,
                    "trust_policy_sha256": "2" * 64,
                    "vendor_manifest_sha256": "3" * 64,
                },
            }
        )
        session_state = self.session.snapshot()
        assert session_state is not None
        binding = UpgradeRuntimeBinding.bind(
            contract,
            context,
            session_identity_digest=session_state.identity.identity_digest,
        )
        expected_branch = str(self.adapter._git("symbolic-ref", "--short", "-q", "HEAD"))
        expected_head = str(self.adapter._git("rev-parse", "HEAD"))
        evidence = binding.reread_backend_bound(
            self.adapter,
            self.scope,
            self.lease,
            self.recheck,
            expected_branch=expected_branch,
            expected_head=expected_head,
        )
        self.assertTrue(evidence["backend_identity_verified"])
        self.assertFalse(evidence["mutates_authority"])
        self.assertEqual(expected_head, evidence["git_head"])
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_clean_snapshot_is_identity_bound_and_nonmutating(self) -> None:
        result = self.adapter.snapshot("discover", CONTEXT)
        self.assertTrue(result["backend_identity_verified"])
        self.assertTrue(result["git_clean"])
        self.assertFalse(result["mutates_authority"])
        for phase in ("", "unknown", 1, True):
            with (
                self.subTest(phase=phase),
                self.assertRaisesRegex(GitAuthorityError, "phase is invalid"),
            ):
                self.adapter.snapshot(cast(Any, phase), CONTEXT)
        durable_before = self.session.snapshot()
        with (
            patch.object(self.adapter, "_git", side_effect=AssertionError("Git reached")) as git,
            patch.object(
                self.adapter, "execute", side_effect=AssertionError("execute reached")
            ) as execute,
            self.assertRaisesRegex(GitAuthorityError, "rollback context target"),
        ):
            self.adapter.verify_rollback_context(CONTEXT)
        git.assert_not_called()
        execute.assert_not_called()
        self.assertEqual(durable_before, self.session.snapshot())
        self.assertFalse(self.session.operation_owned_by_current_thread)
        rollback_context = {**CONTEXT, "target": "rollback"}
        self.assertFalse(
            self.adapter.verify_rollback_context(rollback_context)["rollback_context_verified"]
        )
        bound = self.adapter.verify_rollback_context_bound(
            rollback_context,
            self.scope,
            lease=self.lease,
            admission_recheck=self.recheck,
            expected_branch=str(result["git_branch"]),
            expected_head=str(result["git_head"]),
        )
        self.assertEqual("rollback", bound["phase"])
        self.assertFalse(bound["rollback_context_verified"])
        self.assertFalse(self.session.operation_owned_by_current_thread)
        durable_before_bound_reject = self.session.snapshot()
        with (
            patch.object(self.adapter, "_git", side_effect=AssertionError("Git reached")) as git,
            patch.object(
                self.adapter, "execute", side_effect=AssertionError("execute reached")
            ) as execute,
            self.assertRaisesRegex(GitAuthorityError, "rollback context target"),
        ):
            self.adapter.verify_rollback_context_bound(
                CONTEXT,
                self.scope,
                lease=self.lease,
                admission_recheck=self.recheck,
                expected_branch=str(result["git_branch"]),
                expected_head=str(result["git_head"]),
            )
        git.assert_not_called()
        execute.assert_not_called()
        self.assertEqual(durable_before_bound_reject, self.session.snapshot())
        self.assertFalse(self.session.operation_owned_by_current_thread)
        with self.assertRaisesRegex(GitAuthorityError, "not implemented"):
            self.adapter.execute("commit", CONTEXT)

    def test_preflight_git_verifies_initialized_backup_without_mutation(self) -> None:
        artifact_root = Path(self.coordination.name) / "artifacts"
        backup = create_backup(self.root, artifact_root / "git-backup", quiesced=True)
        observed = self.adapter.snapshot("discover", CONTEXT)
        context = {
            **CONTEXT,
            "target": "rollback",
            "artifact_root": str(artifact_root),
            "git_backup_root": str(backup),
            "manifest": str(backup / "manifest.json"),
            "selector_ref": ".runtime/runtime-selector.json",
        }
        before = (self.root / "state").read_bytes()
        durable_before = self.session.snapshot()
        result = self.adapter.preflight_git(
            context,
            self.scope,
            lease=self.lease,
            admission_recheck=self.recheck,
            expected_branch=str(observed["git_branch"]),
            expected_head=str(observed["git_head"]),
        )
        self.assertEqual(str(observed["git_head"]), result.commit)
        self.assertGreaterEqual(result.artifact_count, 1)
        self.assertEqual(before, (self.root / "state").read_bytes())
        self.assertEqual(durable_before, self.session.snapshot())
        self.assertFalse(self.session.operation_owned_by_current_thread)
        with self.assertRaisesRegex(GitAuthorityError, "not implemented"):
            self.adapter.execute("rollback", context)

    def test_preflight_git_rejects_target_artifact_and_session_drift(self) -> None:
        artifact_root = Path(self.coordination.name) / "artifacts"
        backup = create_backup(self.root, artifact_root / "git-backup", quiesced=True)
        observed = self.adapter.snapshot("discover", CONTEXT)
        base = {
            **CONTEXT,
            "target": "rollback",
            "artifact_root": str(artifact_root),
            "git_backup_root": str(backup),
            "manifest": str(backup / "manifest.json"),
            "selector_ref": ".runtime/runtime-selector.json",
        }
        cases = (
            ({"git_backup_root": str(artifact_root / "missing")}, "manifest is not bound"),
            ({"git_backup_root": str(self.root)}, "outside artifact root"),
            ({"target": "new"}, "rollback target"),
            ({"authority_revision": "foreign"}, "identity changed"),
        )
        for changes, message in cases:
            context = {**base, **changes}
            with self.subTest(changes=changes), self.assertRaisesRegex(GitAuthorityError, message):
                self.adapter.preflight_git(
                    context,
                    self.scope,
                    lease=self.lease,
                    admission_recheck=self.recheck,
                    expected_branch=str(observed["git_branch"]),
                    expected_head=str(observed["git_head"]),
                )
        second_backup = create_backup(self.root, artifact_root / "git-backup-2", quiesced=True)
        foreign_manifest = {**base, "git_backup_root": str(second_backup)}
        with self.assertRaisesRegex(GitAuthorityError, "manifest is not bound"):
            self.adapter.preflight_git(
                foreign_manifest,
                self.scope,
                lease=self.lease,
                admission_recheck=self.recheck,
                expected_branch=str(observed["git_branch"]),
                expected_head=str(observed["git_head"]),
            )
        (backup / "refs.txt").write_text("tampered\n", encoding="utf-8")
        with self.assertRaisesRegex(GitAuthorityError, "verification failed"):
            self.adapter.preflight_git(
                base,
                self.scope,
                lease=self.lease,
                admission_recheck=self.recheck,
                expected_branch=str(observed["git_branch"]),
                expected_head=str(observed["git_head"]),
            )

    def test_preflight_git_failure_releases_scope_and_preserves_session(self) -> None:
        """A verifier failure cannot strand locks or alter durable session state."""
        artifact_root = Path(self.coordination.name) / "failure-artifacts"
        backup = create_backup(self.root, artifact_root / "git-backup", quiesced=True)
        observed = self.adapter.snapshot("discover", CONTEXT)
        context = {
            **CONTEXT,
            "target": "rollback",
            "artifact_root": str(artifact_root),
            "manifest": str(backup / "manifest.json"),
            "selector_ref": ".runtime/runtime-selector.json",
        }
        (backup / "refs.txt").write_text("tampered\n", encoding="utf-8")
        before = self.session.snapshot()
        with self.assertRaisesRegex(GitAuthorityError, "verification failed"):
            self.adapter.preflight_git(
                context,
                self.scope,
                lease=self.lease,
                admission_recheck=self.recheck,
                expected_branch=str(observed["git_branch"]),
                expected_head=str(observed["git_head"]),
            )
        self.assertEqual(before, self.session.snapshot())
        self.assertFalse(self.session.operation_owned_by_current_thread)
        with self.scope.hold():
            pass

    def test_authorization_preflight_consumes_git_provenance_then_refuses(self) -> None:
        artifact_root = Path(self.coordination.name) / "artifacts"
        backup = create_backup(self.root, artifact_root / "git-backup", quiesced=True)
        observed = self.adapter.snapshot("discover", CONTEXT)
        context = {
            **CONTEXT,
            "target": "rollback",
            "artifact_root": str(artifact_root),
            "manifest": str(backup / "manifest.json"),
            "selector_ref": ".runtime/runtime-selector.json",
        }
        phase_context = PhaseContext(**cast(dict[str, Any], context))
        bound = BoundRollbackCapability.bind(
            phase_context,
            self.adapter,
            self.scope,
            lease=self.lease,
            admission_recheck=self.recheck,
            expected_branch=str(observed["git_branch"]),
            expected_head=str(observed["git_head"]),
        )
        authorization = RollbackAuthorizationCapability.bind(phase_context, bound)
        provider = GitRollbackObservationCapability.bind(
            phase_context,
            self.adapter,
            self.scope,
            lease=self.lease,
            admission_recheck=self.recheck,
            expected_branch=str(observed["git_branch"]),
            expected_head=str(observed["git_head"]),
        )
        before = self.session.snapshot()
        with self.assertRaisesRegex(UpgradeError, "authorization is not enabled"):
            authorization.preflight(context, provider)
        self.assertEqual(before, self.session.snapshot())
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_git_observation_failures_and_invalid_repository_fail_closed(self) -> None:
        with self.assertRaisesRegex(GitAuthorityError, "unavailable"):
            GitAuthorityAdapter(self.root / "missing")
        with (
            patch("tools.git_authority_adapter.subprocess.run", side_effect=OSError("git")),
            self.assertRaisesRegex(GitAuthorityError, "observation failed"),
        ):
            self.adapter._git("status")
        failed = subprocess.CompletedProcess([], 1, stdout="", stderr="rejected")
        with (
            patch("tools.git_authority_adapter.subprocess.run", return_value=failed),
            self.assertRaisesRegex(GitAuthorityError, "observation was rejected"),
        ):
            self.adapter._git("status")
        with (
            patch.object(self.adapter, "_git", side_effect=("", "", "")),
            self.assertRaisesRegex(GitAuthorityError, "not clean"),
        ):
            self.adapter.snapshot("discover", CONTEXT)

    def test_snapshot_bound_validates_concrete_scope_and_admission_inputs(self) -> None:
        observed = self.adapter.snapshot("discover", CONTEXT)
        common = {
            "phase": "discover",
            "context": CONTEXT,
            "scope": self.scope,
            "lease": self.lease,
            "admission_recheck": self.recheck,
            "expected_branch": str(observed["git_branch"]),
            "expected_head": str(observed["git_head"]),
        }
        bound = cast(Any, self.adapter.snapshot_bound)
        with self.assertRaisesRegex(GitAuthorityError, "branch identity"):
            bound(**{**common, "expected_branch": ""})
        with self.assertRaisesRegex(GitAuthorityError, "head identity"):
            bound(**{**common, "expected_head": ""})
        with self.assertRaisesRegex(GitAuthorityError, "lease"):
            bound(**{**common, "lease": cast(Any, object())})
        with self.assertRaisesRegex(GitAuthorityError, "recheck"):
            bound(**{**common, "admission_recheck": cast(Any, object())})
        with self.assertRaisesRegex(GitAuthorityError, "recheck"):
            bound(
                **{
                    **common,
                    "admission_recheck": validate_recheck(
                        AdmissionLease(PROJECT, "authority", "other", "owner", "barrier", 1),
                        project_id=PROJECT,
                        authority_revision="authority",
                        fencing_token="other",  # noqa: S106
                        fencing_owner="owner",
                        durable_barrier_id="barrier",
                        revision=1,
                    ),
                }
            )
        with self.assertRaisesRegex(GitAuthorityError, "concrete lock-domain"):
            bound(**{**common, "scope": cast(Any, object())})
        for phase in ("", "unknown", 1, True):
            with (
                self.subTest(bound_phase=phase),
                patch.object(self.adapter, "_git") as git,
                self.assertRaisesRegex(GitAuthorityError, "phase is invalid"),
            ):
                bound(**{**common, "phase": cast(Any, phase)})
            git.assert_not_called()
        self.assertFalse(self.session.operation_owned_by_current_thread)
        with (
            patch.object(self.adapter, "_git", wraps=self.adapter._git) as git,
            self.assertRaisesRegex(GitAuthorityError, "phase is invalid"),
        ):
            bound(**{**common, "phase": ""})
        git.assert_not_called()

    def test_snapshot_bound_keeps_full_backend_schema_after_scope_binding(self) -> None:
        observed = self.adapter.snapshot("discover", CONTEXT)
        invalid_contexts = [
            {key: value for key, value in CONTEXT.items() if key != "operation_id"},
            {**CONTEXT, "operation_id": 3},
            {**CONTEXT, "unexpected": "hostile"},
        ]
        for invalid in invalid_contexts:
            with patch.object(self.adapter, "_git", wraps=self.adapter._git) as git:
                with (
                    self.subTest(context=repr(invalid)),
                    self.assertRaisesRegex(
                        GitAuthorityError, "incomplete or mismatched|types are invalid"
                    ),
                ):
                    self.adapter.snapshot_bound(
                        "discover",
                        invalid,
                        self.scope,
                        lease=self.lease,
                        admission_recheck=self.recheck,
                        expected_branch=str(observed["git_branch"]),
                        expected_head=str(observed["git_head"]),
                    )
                git.assert_not_called()

    def test_scoped_wrapper_is_the_only_composed_mutation_boundary(self) -> None:
        class Scope:
            def assert_ordered(self) -> None:
                pass

            def assert_context(self, _context: Mapping[str, object]) -> None:
                pass

            def hold(self) -> AbstractContextManager[object]:
                return nullcontext()

        adapter = ScopedBackendAdapter(self.adapter, Scope())
        self.assertTrue(adapter.snapshot("discover", CONTEXT)["git_clean"])
        with self.assertRaisesRegex(TypeError, "disabled"):
            adapter.execute("commit", CONTEXT)

    def test_snapshot_bound_rechecks_session_and_binds_immutable_git_identity(self) -> None:
        observed = self.adapter.snapshot("discover", CONTEXT)
        bound = self.adapter.snapshot_bound(
            "discover",
            CONTEXT,
            self.scope,
            lease=self._lease(),
            admission_recheck=self.recheck,
            expected_branch=str(observed["git_branch"]),
            expected_head=str(observed["git_head"]),
        )
        self.assertEqual(observed["git_head"], bound["git_head"])
        self.assertFalse(bound["mutates_authority"])

    def test_snapshot_bound_reread_real_session_and_rejects_foreign_head(self) -> None:
        observed = self.adapter.snapshot("rollback", CONTEXT)
        result = self.adapter.snapshot_bound_reread(
            CONTEXT,
            self.scope,
            lease=self.lease,
            admission_recheck=self.recheck,
            expected_branch=str(observed["git_branch"]),
            expected_head=str(observed["git_head"]),
        )
        self.assertEqual(str(observed["git_head"]), result.git_head)
        self.assertEqual(str(observed["git_branch"]), result.git_branch)
        with self.assertRaisesRegex(GitAuthorityError, "identity changed"):
            self.adapter.snapshot_bound_reread(
                CONTEXT,
                self.scope,
                lease=self.lease,
                admission_recheck=self.recheck,
                expected_branch=str(observed["git_branch"]),
                expected_head="0" * 40,
            )

    def test_snapshot_bound_rejects_session_or_identity_drift_before_observation(self) -> None:
        observed = self.adapter.snapshot("discover", CONTEXT)
        with self.assertRaisesRegex(GitAuthorityError, "identity changed"):
            self.adapter.snapshot_bound(
                "discover",
                CONTEXT,
                self.scope,
                lease=self._lease(),
                admission_recheck=self.recheck,
                expected_branch=str(observed["git_branch"]),
                expected_head="0" * 40,
            )
        self.session.mark_ambiguous(1, "stale-session")
        with (
            patch.object(self.adapter, "_git", wraps=self.adapter._git) as git,
            self.assertRaisesRegex(GitAuthorityError, "trusted Git session"),
        ):
            self.adapter.snapshot_bound(
                "discover",
                CONTEXT,
                self.scope,
                lease=self._lease(),
                admission_recheck=self.recheck,
                expected_branch=str(observed["git_branch"]),
                expected_head=str(observed["git_head"]),
            )
        git.assert_not_called()

    def test_dirty_or_detached_or_mismatched_context_fails_closed(self) -> None:
        (self.root / "state").write_text("dirty\n")
        with self.assertRaisesRegex(GitAuthorityError, "not clean"):
            self.adapter.snapshot("discover", CONTEXT)
        (self.root / "state").write_text("clean\n")
        with self.assertRaisesRegex(GitAuthorityError, "mismatched"):
            self.adapter.snapshot("discover", {**CONTEXT, "backend": "sqlite"})

    def test_snapshot_bound_rejects_durable_identity_drift_before_scope(self) -> None:
        observed = self.adapter.snapshot("discover", CONTEXT)
        for field in (
            "project_id",
            "authority_revision",
            "fencing_token",
            "fencing_owner",
            "durable_barrier_id",
            "state_revision",
        ):
            drifted = dict(CONTEXT)
            drifted[field] = 2 if field == "state_revision" else f"changed-{field}"
            with (
                self.subTest(field=field),
                self.assertRaisesRegex(GitAuthorityError, "session identity"),
            ):
                self.adapter.snapshot_bound(
                    "discover",
                    drifted,
                    self.scope,
                    lease=self._lease(),
                    admission_recheck=self.recheck,
                    expected_branch=str(observed["git_branch"]),
                    expected_head=str(observed["git_head"]),
                )

    def test_snapshot_bound_rejects_replaced_lease_before_backend(self) -> None:
        observed = self.adapter.snapshot("discover", CONTEXT)
        replaced = AdmissionLease(PROJECT, "authority", "replacement", "owner", "barrier", 1)
        with patch.object(self.adapter, "_git", wraps=self.adapter._git) as git:
            with self.assertRaisesRegex(GitAuthorityError, "recheck|session identity"):
                self.adapter.snapshot_bound(
                    "discover",
                    CONTEXT,
                    self.scope,
                    lease=replaced,
                    admission_recheck=self.recheck,
                    expected_branch=str(observed["git_branch"]),
                    expected_head=str(observed["git_head"]),
                )
            git.assert_not_called()

    def test_snapshot_bound_rejects_full_context_schema_before_scope(self) -> None:
        class ScopeMustNotRun:
            def assert_ordered(self) -> None:
                raise AssertionError("scope must not run")

            def assert_context(self, _context: Mapping[str, object]) -> None:
                raise AssertionError("scope must not run")

            def hold(self) -> AbstractContextManager[object]:
                raise AssertionError("scope must not run")

        observed = self.adapter.snapshot("discover", CONTEXT)
        invalid_contexts = [
            {key: value for key, value in CONTEXT.items() if key != "operation_id"},
            {**CONTEXT, "unexpected": "hostile"},
            {**CONTEXT, "state_revision": True},
        ]
        for invalid in invalid_contexts:
            with (
                self.subTest(context=repr(invalid)),
                self.assertRaisesRegex(GitAuthorityError, "context"),
            ):
                self.adapter.snapshot_bound(
                    "discover",
                    invalid,
                    cast(Any, ScopeMustNotRun()),
                    lease=self._lease(),
                    admission_recheck=self.recheck,
                    expected_branch=str(observed["git_branch"]),
                    expected_head=str(observed["git_head"]),
                )

    def test_process_abort_releases_bound_scope_for_fresh_read_only_worker(self) -> None:
        """A child abort inside snapshot_bound leaves all locks reusable."""
        observed = self.adapter.snapshot("discover", CONTEXT)
        context = multiprocessing.get_context("fork")
        crashed_result = context.Queue()
        crashed = context.Process(
            target=_bound_snapshot_process,
            args=(
                str(self.root),
                self.coordination.name,
                str(observed["git_branch"]),
                str(observed["git_head"]),
                "crash",
                crashed_result,
                True,
            ),
        )
        crashed.start()
        crashed.join(5)
        self.assertEqual(17, crashed.exitcode)

        recovered_result = context.Queue()
        recovered = context.Process(
            target=_bound_snapshot_process,
            args=(
                str(self.root),
                self.coordination.name,
                str(observed["git_branch"]),
                str(observed["git_head"]),
                "success",
                recovered_result,
                True,
            ),
        )
        recovered.start()
        recovered.join(5)
        self.assertEqual(0, recovered.exitcode)
        self.assertEqual(
            ("success", observed["git_head"], observed["git_branch"]),
            recovered_result.get(timeout=1),
        )

    def test_typed_session_transition_rejects_then_reacquires_fresh_worker(self) -> None:
        """Typed ambiguous/replacement transitions gate fresh bound workers."""
        observed = self.adapter.snapshot("discover", CONTEXT)

        def fail_publication(*_args: Any, **_kwargs: Any) -> None:
            raise OSError("intent publication unavailable")

        with (
            patch.object(self.session, "_mark_intent_locked", side_effect=fail_publication),
            self.assertRaisesRegex(ControlStoreError, "outcome publication is ambiguous"),
        ):
            self.session.cas(1, BarrierSessionState(self._session_identity(), "held", 2))
        ambiguous = self.session.recover_unknown()
        self.assertIsNotNone(ambiguous)
        assert ambiguous is not None
        self.assertEqual("ambiguous", ambiguous.status)
        durable_before_failures = self.session.snapshot()

        context = multiprocessing.get_context("fork")
        result = context.Queue()
        fresh = context.Process(
            target=_bound_snapshot_process,
            args=(
                str(self.root),
                self.coordination.name,
                str(observed["git_branch"]),
                str(observed["git_head"]),
                "stale",
                result,
            ),
        )
        fresh.start()
        fresh.join(5)
        self.assertEqual(0, fresh.exitcode)
        outcome = result.get(timeout=1)
        self.assertEqual("rejected", outcome[0])
        self.assertIn(outcome[1], {"GitAuthorityError", "LockDomainError"})
        self.assertEqual(0, outcome[3])
        self.assertFalse(self.session.operation_owned_by_current_thread)
        self.assertEqual(durable_before_failures, self.session.snapshot())

        replacement_record = self._session_identity().as_record()
        replacement_record.update(
            {
                "attempt_id": "attempt-replacement",
                "state_revision": 2,
                "durable_barrier_id": "barrier-replaced",
                "fencing_token": "fence-replaced",
                "fencing_owner": "owner-replaced",
            }
        )
        replacement_record["identity_digest"] = canonical_barrier_session_digest(replacement_record)
        replacement = BarrierSessionState(
            BarrierSessionIdentity.from_record(replacement_record), "held", 1
        )
        with self.assertRaisesRegex(ControlStoreError, "CAS conflict"):
            self.session.reconcile_ambiguous(ambiguous.revision - 1, replacement)
        self.assertFalse(self.session.operation_owned_by_current_thread)
        self.assertEqual(durable_before_failures, self.session.snapshot())
        for field in ("attempt_id", "durable_barrier_id", "fencing_token"):
            reused_record = dict(replacement_record)
            reused_record[field] = self._session_identity().as_record()[field]
            reused_record["identity_digest"] = canonical_barrier_session_digest(reused_record)
            reused = BarrierSessionState(
                BarrierSessionIdentity.from_record(reused_record), "held", 1
            )

            with (
                self.subTest(reused_field=field),
                self.assertRaisesRegex(ControlStoreError, "distinct newer fence"),
            ):
                self.session.reconcile_ambiguous(ambiguous.revision, reused)
            self.assertFalse(self.session.operation_owned_by_current_thread)
            self.assertEqual(durable_before_failures, self.session.snapshot())
        mismatch_store = SQLiteBarrierSessionStore(
            SQLiteRollbackControlStore(
                self.session.control_store_path, PROJECT, self.session.authority_path
            ),
            lambda: "authority-mismatch",
        )
        with self.assertRaisesRegex(ControlStoreError, "replacement authority revision changed"):
            mismatch_store.reconcile_ambiguous(ambiguous.revision, replacement)
        self.assertFalse(mismatch_store.operation_owned_by_current_thread)
        self.assertEqual(durable_before_failures, self.session.snapshot())
        self.assertEqual(
            replacement, self.session.reconcile_ambiguous(ambiguous.revision, replacement)
        )

        recovered_result = context.Queue()
        recovered = context.Process(
            target=_bound_snapshot_process,
            args=(
                str(self.root),
                self.coordination.name,
                str(observed["git_branch"]),
                str(observed["git_head"]),
                "replacement",
                recovered_result,
            ),
        )
        recovered.start()
        recovered.join(5)
        self.assertEqual(0, recovered.exitcode)
        self.assertEqual(
            ("success", observed["git_head"], observed["git_branch"]),
            recovered_result.get(timeout=1),
        )

    def test_snapshot_bound_rejects_backend_equivalence_drift(self) -> None:
        class TamperedAdapter(GitAuthorityAdapter):
            def snapshot(self, phase: str, context: Mapping[str, object]) -> dict[str, Any]:
                value = super().snapshot(phase, context)
                value["project_id"] = "tampered"
                return value

        observed = self.adapter.snapshot("discover", CONTEXT)
        tampered = TamperedAdapter(self.root)
        with (
            patch.object(tampered, "execute", side_effect=AssertionError("execute reached")),
            self.assertRaisesRegex(GitAuthorityError, "backend context identity"),
        ):
            tampered.snapshot_bound(
                "discover",
                CONTEXT,
                self.scope,
                lease=self._lease(),
                admission_recheck=self.recheck,
                expected_branch=str(observed["git_branch"]),
                expected_head=str(observed["git_head"]),
            )
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_snapshot_bound_rejects_non_read_only_backend_result(self) -> None:
        class TamperedAdapter(GitAuthorityAdapter):
            def snapshot(self, phase: str, context: Mapping[str, object]) -> dict[str, Any]:
                value = super().snapshot(phase, context)
                value["mutates_authority"] = True
                return value

        observed = self.adapter.snapshot("discover", CONTEXT)
        tampered = TamperedAdapter(self.root)
        with (
            patch.object(tampered, "execute", side_effect=AssertionError("execute reached")),
            self.assertRaisesRegex(GitAuthorityError, "not read-only"),
        ):
            tampered.snapshot_bound(
                "discover",
                CONTEXT,
                self.scope,
                lease=self._lease(),
                admission_recheck=self.recheck,
                expected_branch=str(observed["git_branch"]),
                expected_head=str(observed["git_head"]),
            )
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_snapshot_bound_rejects_phase_or_cleanliness_drift(self) -> None:
        class TamperedAdapter(GitAuthorityAdapter):
            field = "phase"

            def snapshot(self, phase: str, context: Mapping[str, object]) -> dict[str, Any]:
                value = super().snapshot(phase, context)
                value[self.field] = "other" if self.field == "phase" else False
                return value

        observed = self.adapter.snapshot("discover", CONTEXT)
        for field, message in (
            ("phase", "backend phase changed"),
            ("git_clean", "cleanliness is unverified"),
        ):
            with self.subTest(field=field):
                tampered = type("FieldTamperedAdapter", (TamperedAdapter,), {"field": field})(
                    self.root
                )
                with (
                    patch.object(
                        tampered, "execute", side_effect=AssertionError("execute reached")
                    ),
                    self.assertRaisesRegex(GitAuthorityError, message),
                ):
                    tampered.snapshot_bound(
                        "discover",
                        CONTEXT,
                        self.scope,
                        lease=self._lease(),
                        admission_recheck=self.recheck,
                        expected_branch=str(observed["git_branch"]),
                        expected_head=str(observed["git_head"]),
                    )
                self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_snapshot_bound_requires_exact_result_schema_and_types(self) -> None:
        fields = {
            "phase": 1,
            "backend_identity_verified": 1,
            "git_head": 1,
            "git_branch": 1,
            "git_clean": 1,
            "mutates_authority": 0,
        }

        class TamperedAdapter(GitAuthorityAdapter):
            mode = "wrong"
            field = "phase"
            wrong: object = 1

            def snapshot(self, phase: str, context: Mapping[str, object]) -> dict[str, Any]:
                value = super().snapshot(phase, context)
                if self.mode == "missing":
                    value.pop(self.field)
                elif self.mode == "extra":
                    value["unexpected"] = True
                else:
                    value[self.field] = self.wrong
                return value

        observed = self.adapter.snapshot("discover", CONTEXT)
        for mode in ("missing", "extra", "wrong"):
            for field, wrong in fields.items():
                with self.subTest(mode=mode, field=field):
                    adapter = type(
                        "SchemaTamperedAdapter",
                        (TamperedAdapter,),
                        {"mode": mode, "field": field, "wrong": wrong},
                    )(self.root)
                    with (
                        patch.object(
                            adapter, "execute", side_effect=AssertionError("execute reached")
                        ),
                        self.assertRaises(GitAuthorityError),
                    ):
                        adapter.snapshot_bound(
                            "discover",
                            CONTEXT,
                            self.scope,
                            lease=self._lease(),
                            admission_recheck=self.recheck,
                            expected_branch=str(observed["git_branch"]),
                            expected_head=str(observed["git_head"]),
                        )
                    self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_snapshot_bound_rejects_boolean_integer_context_substitution(self) -> None:
        class TamperedAdapter(GitAuthorityAdapter):
            def snapshot(self, phase: str, context: Mapping[str, object]) -> dict[str, Any]:
                value = super().snapshot(phase, context)
                value["state_revision"] = True
                return value

        observed = self.adapter.snapshot("discover", CONTEXT)
        tampered = TamperedAdapter(self.root)
        with (
            patch.object(tampered, "execute", side_effect=AssertionError("execute reached")),
            patch.object(tampered, "_git", wraps=tampered._git) as git,
            self.assertRaisesRegex(GitAuthorityError, "backend context identity"),
        ):
            tampered.snapshot_bound(
                "discover",
                CONTEXT,
                self.scope,
                lease=self._lease(),
                admission_recheck=self.recheck,
                expected_branch=str(observed["git_branch"]),
                expected_head=str(observed["git_head"]),
            )
        self.assertEqual(3, git.call_count)
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_typed_reconcile_rejects_real_unresolved_intent(self) -> None:
        """A prepared intent left by publication failure blocks replacement."""

        def fail_publication(*_args: Any, **_kwargs: Any) -> None:
            raise OSError("intent publication unavailable")

        with (
            patch.object(self.session, "_mark_intent_locked", side_effect=fail_publication),
            self.assertRaisesRegex(ControlStoreError, "outcome publication is ambiguous"),
        ):
            self.session.cas(1, BarrierSessionState(self._session_identity(), "held", 2))
        with (
            patch.object(self.session, "_mark_intent_locked", side_effect=fail_publication),
            self.assertRaisesRegex(OSError, "intent publication unavailable"),
        ):
            self.session.recover_unknown()
        current = self.session.snapshot()
        self.assertIsNotNone(current)
        assert current is not None
        replacement_record = self._session_identity().as_record()
        replacement_record.update(
            {
                "attempt_id": "attempt-newer",
                "state_revision": 3,
                "durable_barrier_id": "barrier-newer",
                "fencing_token": "fence-newer",
            }
        )
        replacement_record["identity_digest"] = canonical_barrier_session_digest(replacement_record)
        replacement = BarrierSessionState(
            BarrierSessionIdentity.from_record(replacement_record), "held", 1
        )
        with self.assertRaisesRegex(ControlStoreError, "unresolved intent"):
            self.session.reconcile_ambiguous(current.revision, replacement)
        self.assertFalse(self.session.operation_owned_by_current_thread)
        self.assertEqual(current, self.session.snapshot())

    def test_rollback_recheck_never_authorizes_mutation(self) -> None:
        result = self.adapter.verify_rollback_context({**CONTEXT, "target": "rollback"})
        self.assertFalse(result["rollback_context_verified"])

    def test_bound_rollback_rejects_stale_and_replaced_sessions_before_git(self) -> None:
        observed = self.adapter.snapshot("discover", CONTEXT)
        rollback = {**CONTEXT, "target": "rollback"}
        ambiguous = self.session.mark_ambiguous(1, "rollback-stale")
        before_stale = self.session.snapshot()
        with (
            patch.object(self.adapter, "_git", side_effect=AssertionError("Git reached")) as git,
            patch.object(
                self.adapter, "execute", side_effect=AssertionError("execute reached")
            ) as execute,
            self.assertRaisesRegex(GitAuthorityError, "trusted Git session"),
        ):
            self.adapter.verify_rollback_context_bound(
                rollback,
                self.scope,
                lease=self.lease,
                admission_recheck=self.recheck,
                expected_branch=str(observed["git_branch"]),
                expected_head=str(observed["git_head"]),
            )
        git.assert_not_called()
        execute.assert_not_called()
        self.assertEqual(before_stale, self.session.snapshot())
        self.assertFalse(self.session.operation_owned_by_current_thread)

        replacement_record = self._session_identity().as_record()
        replacement_record.update(
            {
                "attempt_id": "rollback-replacement",
                "state_revision": 2,
                "durable_barrier_id": "barrier-replacement",
                "fencing_token": "fence-replacement",
                "fencing_owner": "owner-replacement",
            }
        )
        replacement_record["identity_digest"] = canonical_barrier_session_digest(replacement_record)
        replacement = BarrierSessionState(
            BarrierSessionIdentity.from_record(replacement_record), "held", 1
        )
        self.session.reconcile_ambiguous(ambiguous.revision, replacement)
        before_replaced = self.session.snapshot()
        with (
            patch.object(self.adapter, "_git", side_effect=AssertionError("Git reached")) as git,
            patch.object(
                self.adapter, "execute", side_effect=AssertionError("execute reached")
            ) as execute,
            self.assertRaisesRegex(GitAuthorityError, "trusted Git session"),
        ):
            self.adapter.verify_rollback_context_bound(
                rollback,
                self.scope,
                lease=self.lease,
                admission_recheck=self.recheck,
                expected_branch=str(observed["git_branch"]),
                expected_head=str(observed["git_head"]),
            )
        git.assert_not_called()
        execute.assert_not_called()
        self.assertEqual(before_replaced, self.session.snapshot())
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_bound_rollback_rejects_tampered_git_results_without_state_change(self) -> None:
        observed = self.adapter.snapshot("discover", CONTEXT)
        rollback = {**CONTEXT, "target": "rollback"}

        class TamperedAdapter(GitAuthorityAdapter):
            field = "phase"
            replacement: object = "discover"

            def snapshot(self, phase: str, context: Mapping[str, object]) -> dict[str, object]:
                value = super().snapshot(phase, context)
                value[self.field] = self.replacement
                return value

        fields = (
            ("phase", "discover", "backend phase changed"),
            ("project_id", "tampered", "backend context identity changed"),
            ("backend_identity_verified", False, "identity is unverified"),
            ("git_clean", False, "cleanliness is unverified"),
            ("mutates_authority", True, "not read-only"),
        )
        for field, replacement, message in fields:
            with self.subTest(field=field):
                adapter = type(
                    "RollbackTamperedGitAdapter",
                    (TamperedAdapter,),
                    {"field": field, "replacement": replacement},
                )(self.root)
                before = self.session.snapshot()
                with (
                    patch.object(
                        adapter, "execute", side_effect=AssertionError("execute reached")
                    ) as execute,
                    self.assertRaisesRegex(GitAuthorityError, message),
                ):
                    adapter.verify_rollback_context_bound(
                        rollback,
                        self.scope,
                        lease=self.lease,
                        admission_recheck=self.recheck,
                        expected_branch=str(observed["git_branch"]),
                        expected_head=str(observed["git_head"]),
                    )
                execute.assert_not_called()
                self.assertEqual(before, self.session.snapshot())
                self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_bound_rollback_rejects_authority_and_backend_drift_without_execute(self) -> None:
        observed = self.adapter.snapshot("discover", CONTEXT)
        rollback = {**CONTEXT, "target": "rollback"}
        drifted = AdmissionLease(PROJECT, "authority-drift", "fence", "owner", "barrier", 1)
        drifted_recheck = validate_recheck(
            drifted,
            project_id=PROJECT,
            authority_revision="authority-drift",
            fencing_token="fence",  # noqa: S106
            fencing_owner="owner",
            durable_barrier_id="barrier",
            revision=1,
        )
        before = self.session.snapshot()
        with (
            patch.object(self.adapter, "_git", side_effect=AssertionError("Git reached")) as git,
            patch.object(
                self.adapter, "execute", side_effect=AssertionError("execute reached")
            ) as execute,
            self.assertRaisesRegex(GitAuthorityError, "trusted Git session reread"),
        ):
            self.adapter.verify_rollback_context_bound(
                {**rollback, "authority_revision": "authority-drift"},
                self.scope,
                lease=drifted,
                admission_recheck=drifted_recheck,
                expected_branch=str(observed["git_branch"]),
                expected_head=str(observed["git_head"]),
            )
        git.assert_not_called()
        execute.assert_not_called()
        self.assertEqual(before, self.session.snapshot())
        self.assertFalse(self.session.operation_owned_by_current_thread)

        with (
            patch.object(
                self.adapter, "execute", side_effect=AssertionError("execute reached")
            ) as execute,
            self.assertRaisesRegex(GitAuthorityError, "Git authority identity changed"),
        ):
            self.adapter.verify_rollback_context_bound(
                rollback,
                self.scope,
                lease=self.lease,
                admission_recheck=self.recheck,
                expected_branch=str(observed["git_branch"]),
                expected_head="0" * 40,
            )
        execute.assert_not_called()
        self.assertEqual(before, self.session.snapshot())
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_bound_rollback_rejects_malformed_admission_before_git(self) -> None:
        observed = self.adapter.snapshot("discover", CONTEXT)
        common = {
            "context": {**CONTEXT, "target": "rollback"},
            "scope": self.scope,
            "lease": self.lease,
            "admission_recheck": self.recheck,
            "expected_branch": str(observed["git_branch"]),
            "expected_head": str(observed["git_head"]),
        }
        bound = cast(Any, self.adapter.verify_rollback_context_bound)
        cases = (
            ("lease", cast(Any, object()), "trusted admission lease"),
            ("admission_recheck", cast(Any, object()), "trusted admission recheck"),
            ("scope", cast(Any, object()), "concrete lock-domain scope"),
            ("context", {**CONTEXT, "target": "unexpected"}, "rollback context target"),
        )
        for field, value, message in cases:
            with self.subTest(field=field):
                before = self.session.snapshot()
                with (
                    patch.object(
                        self.adapter, "_git", side_effect=AssertionError("Git reached")
                    ) as git,
                    patch.object(
                        self.adapter, "execute", side_effect=AssertionError("execute reached")
                    ) as execute,
                    self.assertRaisesRegex(GitAuthorityError, message),
                ):
                    bound(**{**common, field: value})
                git.assert_not_called()
                execute.assert_not_called()
                self.assertEqual(before, self.session.snapshot())
                self.assertFalse(self.session.operation_owned_by_current_thread)


if __name__ == "__main__":
    unittest.main()
