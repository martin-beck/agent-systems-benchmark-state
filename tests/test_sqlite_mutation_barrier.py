# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Independent-process tests for normal SQLite writers at the upgrade barrier."""

# The executable and arguments are fixed test fixtures.
# ruff: noqa: S603, S607

from __future__ import annotations

import multiprocessing
import os
import signal
import sqlite3
import subprocess
import tempfile
import unittest
from contextlib import closing
from multiprocessing.process import BaseProcess
from pathlib import Path
from typing import Any, NoReturn, cast
from unittest.mock import patch

import tools.handoffctl as handoffctl
import tools.mutation_fence as mutation_fence
from tools.admission_lease import AdmissionLease, validate_recheck
from tools.authority_mutation import DurableBoundAuthorityMutation
from tools.authority_neutral_commit import CommitAdmissionBundle
from tools.git_authority_adapter import GitAuthorityAdapter
from tools.git_authority_mutation import GitCommitCapability
from tools.handoffctl import locked
from tools.lock_domain_scope import LockDomainScope
from tools.mutation_fence import (
    MutationFence,
    MutationFenceError,
    provision,
    provision_control_binding,
)
from tools.rollback_control_store import (
    AuthorityEffectIntent,
    BarrierSessionState,
    ControlStoreError,
    SQLiteBarrierSessionStore,
    SQLiteRollbackControlStore,
)
from tools.sqlite_authority_adapter import SQLiteAuthorityAdapter
from tools.sqlite_authority_mutation import (
    SQLiteCommitCapability,
    SQLiteMutationRejectedError,
)
from tools.sqlite_storage import SQLiteBackend, bind_released_sqlite_backend, create_database
from tools.upgrade_identity import (
    BarrierChildIdentity,
    BarrierSessionIdentity,
    canonical_barrier_session_digest,
)

PROJECT = "11111111-1111-4111-8111-111111111111"
BINDING = {
    "project_id": PROJECT,
    "state_repository": "owner/state",
    "product_repository": "owner/product",
}


def _runtime_evidence(state: BarrierSessionState, target: str) -> dict[str, object]:
    return {
        "authority_revision": state.identity.authority_revision_at_acquire,
        "backend": "sqlite",
        "backend_roundtrip": "sqlite",
        "foreign_key_violations": 0,
        "fencing_token": state.identity.fencing_token,
        "integrity_check": "ok",
        "project_id": state.identity.project_id,
        "target": target,
        "verified": True,
    }


def _identity(
    *,
    attempt: str = "attempt-1",
    state_revision: int = 1,
    barrier: str = "barrier-1",
    fence: str = "fence-1",
    owner: str = "owner-1",
) -> BarrierSessionIdentity:
    record: dict[str, object] = {
        "schema_version": 1,
        "project_id": PROJECT,
        "attempt_id": attempt,
        "state_revision": state_revision,
        "authority_revision_at_acquire": "authority-1",
        "durable_barrier_id": barrier,
        "fencing_token": fence,
        "fencing_owner": owner,
        "identity_digest": "0" * 64,
    }
    record["identity_digest"] = canonical_barrier_session_digest(record)
    return BarrierSessionIdentity.from_record(record)


def _control(root: Path) -> SQLiteRollbackControlStore:
    return SQLiteRollbackControlStore(root / "control.sqlite", PROJECT, root / "authority.sqlite")


def _fence(root: Path, control: SQLiteRollbackControlStore) -> MutationFence:
    return MutationFence(
        root / "authority.sqlite",
        root / "authority-marker.json",
        root / "authority-lifecycle.json",
        root / "authority.lock",
        control.control_store_path,
        root / "control-binding.json",
        control.control_lock_path,
    )


def _git(root: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(root), *args], check=True, capture_output=True, text=True
    )
    return result.stdout.rstrip("\n")


def _backend(root: Path, fence: MutationFence) -> SQLiteBackend:
    return SQLiteBackend(
        root / "authority.sqlite",
        BINDING,
        root / "tasks",
        mutation_scope=lambda: fence.mutation_scope(locked),
    )


def _normal_writer(root_text: str, result: Any, start: Any | None = None) -> None:
    """Run one public mutation route from a freshly constructed process."""
    root = Path(root_text)
    control = _control(root)
    backend = _backend(root, _fence(root, control))
    if start is not None:
        start.wait()

    def update_summary(
        meta: dict[str, Any], _tasks: list[tuple[Path, dict[str, Any], str]]
    ) -> tuple[str, str]:
        meta["summary"] = "mutated after verified release"
        return "released writer", "# Authority fixture\n\nWriter committed.\n"

    try:
        backend.mutate(
            "AR-0001",
            1,
            "update",
            "2026-09-16T15:10:00+00:00",
            update_summary,
        )
    except Exception as error:
        result.put(("rejected", type(error).__name__, str(error)))
    else:
        result.put(("committed",))


def _bound_writer_after_replacement(
    root_text: str,
    identity: BarrierSessionIdentity,
    ready: Any,
    proceed: Any,
    result: Any,
) -> None:
    """Use a previously admitted identity after the durable session changes."""
    root = Path(root_text)
    control = _control(root)
    fence = _fence(root, control)
    backend = bind_released_sqlite_backend(
        root / "authority.sqlite",
        BINDING,
        root / "tasks",
        fence,
        locked,
        identity,
    )
    ready.set()
    if not proceed.wait(5):
        result.put(("rejected", "RuntimeError", "replacement synchronization timed out"))
        return

    def update_summary(
        meta: dict[str, Any], _tasks: list[tuple[Path, dict[str, Any], str]]
    ) -> tuple[str, str]:
        meta["summary"] = "stale writer must not commit"
        return "stale writer", "# Must not persist\n"

    try:
        backend.mutate(
            "AR-0001",
            1,
            "update",
            "2026-09-21T00:16:00+00:00",
            update_summary,
        )
    except Exception as error:
        result.put(("rejected", type(error).__name__, str(error)))
    else:
        result.put(("committed",))


def _route_writer(root_text: str, route: str, result: Any) -> None:
    """Exercise one inventoried public write route in a fresh process."""
    root = Path(root_text)
    control = _control(root)
    backend = _backend(root, _fence(root, control))
    try:
        _perform_route(backend, route)
    except Exception as error:
        result.put(("rejected", type(error).__name__, str(error)))
    else:
        result.put(("committed",))


def _perform_route(backend: SQLiteBackend, route: str) -> None:
    if route == "mutate":

        def update_summary(
            meta: dict[str, Any], _tasks: list[tuple[Path, dict[str, Any], str]]
        ) -> tuple[str, str]:
            meta["summary"] = "route mutation"
            return "route mutation", "# Route mutation\n"

        backend.mutate(
            "AR-0001",
            1,
            "update",
            "2026-09-16T15:13:00+00:00",
            update_summary,
        )
    elif route == "update_observations":
        backend.update_observations(
            {"worker-1": {"branch": "route", "head": "b" * 40, "dirty": 0}},
            "2026-09-16T15:13:00+00:00",
        )
    elif route == "append_command_result":
        backend.append_command_result(
            "AR-0001",
            "route-worker",
            "a" * 64,
            0,
            "success",
            "2026-09-16T15:13:00+00:00",
        )
    elif route == "retire":
        backend.retire(lambda _tasks: None, lambda: None)
    else:
        raise AssertionError(f"unknown route {route}")


def _route_effect_waiting_for_sidecar_fault_all_routes(
    root_text: str, route: str, ready: Any, resume: Any, result: Any
) -> None:
    """Pause each public route while its authority sidecars are retained."""
    root = Path(root_text)
    backend = _backend(root, _fence(root, _control(root)))
    original_assert = backend._assert_mutation_binding
    paused = False

    def wait_after_binding_check() -> None:
        nonlocal paused
        original_assert()
        if not paused:
            paused = True
            ready.set()
            if not resume.wait(5):
                raise RuntimeError("authority sidecar fault injection timed out")

    backend_any: Any = backend
    backend_any._assert_mutation_binding = wait_after_binding_check
    try:
        _perform_route(backend, route)
    except Exception as error:
        result.put(("rejected", type(error).__name__, str(error)))
    else:
        result.put(("committed",))


def _held_scope_owner(root_text: str, ready: Any) -> None:
    """Hold the real common/control/authority scope until externally killed."""
    root = Path(root_text)
    control = _control(root)
    session = SQLiteBarrierSessionStore(control, lambda: "authority-1")
    state = session.snapshot()
    assert state is not None
    identity = state.identity
    lease = AdmissionLease(
        PROJECT,
        identity.authority_revision_at_acquire,
        identity.fencing_token,
        identity.fencing_owner,
        identity.durable_barrier_id,
        identity.state_revision,
    )
    recheck = validate_recheck(
        lease,
        project_id=PROJECT,
        authority_revision=identity.authority_revision_at_acquire,
        fencing_token=identity.fencing_token,
        fencing_owner=identity.fencing_owner,
        durable_barrier_id=identity.durable_barrier_id,
        revision=identity.state_revision,
    )
    scope = LockDomainScope.bind(session, _fence(root, control), lease, recheck, locked)
    with scope.hold():
        ready.set()
        multiprocessing.Event().wait()


def _held_control_owner(root_text: str, ready: Any) -> None:
    """Hold only the control lock so a writer exercises its bounded wait."""
    root = Path(root_text)
    fence = _fence(root, _control(root))
    with fence.control_locked():
        ready.set()
        multiprocessing.Event().wait()


def _session_commit_waiting_for_sigkill(root_text: str, ready: Any) -> None:
    """Pause after durable CAS commit but before intent outcome publication."""
    root = Path(root_text)
    session = SQLiteBarrierSessionStore(_control(root), lambda: "authority-1")

    def wait_after_commit(*_args: object, **_kwargs: object) -> None:
        ready.set()
        multiprocessing.Event().wait()

    session_any: Any = session
    session_any._mark_intent_locked = wait_after_commit
    session.create(_identity())


def _authority_effect_waiting_for_sigkill(root_text: str, ready: Any) -> None:
    """Commit a real SQLite effect, then die before durable outcome publication."""
    root = Path(root_text)
    control = _control(root)
    session = SQLiteBarrierSessionStore(control, lambda: "authority-1")
    session.create(_identity())
    admission = CommitAdmissionBundle(
        backend="sqlite",
        target="new",
        operation_id="op-1:commit",
        fencing_token="fence-1",  # noqa: S106
        state_revision=1,
        barrier_id="barrier-1",
        artifact_identity="artifact-1",
        manifest_identity="manifest-1",
        selector_identity="selector-1",
        runtime_identity="runtime-1",
    )
    keepalive = sqlite3.connect(root / "authority.sqlite")
    keepalive.execute("PRAGMA wal_autocheckpoint=0")
    keepalive.execute("PRAGMA user_version=1")
    keepalive.commit()

    capability = SQLiteAuthorityAdapter(root / "authority.sqlite").bind_durable_commit_capability(
        admission,
        session,
        session_revision=1,
        admission_reread=lambda: admission.__dict__,
    )

    def effect(connection: sqlite3.Connection) -> None:
        connection.execute(
            "UPDATE tasks SET body='effect committed before worker death' WHERE id='AR-0001'"
        )
        connection.commit()
        connection.close()
        keepalive.close()
        ready.set()
        os._exit(17)

    capability.execute(effect)


def _git_authority_effect_waiting_for_sigkill(root_text: str, ready: Any) -> None:
    """Commit a real Git effect, then die before durable outcome publication."""
    root = Path(root_text)
    control = _control(root)
    session = SQLiteBarrierSessionStore(control, lambda: "authority-1")
    session.create(_identity())
    admission = CommitAdmissionBundle(
        backend="git",
        target="new",
        operation_id="op-git-1:commit",
        fencing_token="fence-1",  # noqa: S106
        state_revision=1,
        barrier_id="barrier-1",
        artifact_identity="artifact-1",
        manifest_identity="manifest-1",
        selector_identity="selector-1",
        runtime_identity="runtime-1",
    )
    git_root = root / "git-authority"
    (git_root / "state").write_text("effect committed before worker death\n", encoding="utf-8")
    _git(git_root, "add", "state")
    capability = GitAuthorityAdapter(git_root).bind_durable_commit_capability(
        admission,
        session,
        session_revision=1,
        admission_reread=lambda: admission.__dict__,
        expected_branch="main",
        expected_head=_git(git_root, "rev-parse", "HEAD"),
    )

    def kill_before_finish(
        _intent: object, _outcome: str, _receipt: object | None = None
    ) -> NoReturn:
        ready.set()
        os._exit(17)

    session_any: Any = session
    session_any.finish_authority_effect = kill_before_finish
    capability.execute("op-git-1 authority commit")


def _session_recovery_waiting_for_sigkill(root_text: str, ready: Any) -> None:
    """Pause after durable ambiguity but before intent outcome publication."""
    root = Path(root_text)
    session = SQLiteBarrierSessionStore(_control(root), lambda: "authority-1")

    def wait_after_ambiguity(*_args: object, **_kwargs: object) -> None:
        ready.set()
        multiprocessing.Event().wait()

    session_any: Any = session
    session_any._mark_intent_locked = wait_after_ambiguity
    session.recover_unknown()


def _reconcile_waiting_for_sigkill(root_text: str, ready: Any) -> None:
    """Lose the reply after reconciliation commits before outcome publication."""
    root = Path(root_text)
    session = SQLiteBarrierSessionStore(_control(root), lambda: "authority-1")
    ambiguous = session.snapshot()
    assert ambiguous is not None
    replacement = BarrierSessionState(
        _identity(
            attempt="attempt-reconciled",
            state_revision=2,
            barrier="barrier-reconciled",
            fence="fence-reconciled",
            owner="owner-reconciled",
        ),
        "held",
        1,
    )

    def wait_before_outcome(*_args: object, **_kwargs: object) -> None:
        ready.set()
        multiprocessing.Event().wait()

    session_any: Any = session
    session_any._mark_intent_locked = wait_before_outcome
    session.reconcile_ambiguous(ambiguous.revision, replacement)


def _route_effect_waiting_for_sigkill(root_text: str, ready: Any) -> None:
    """Pause after a public route's SQL effects and before transaction commit."""
    root = Path(root_text)
    backend = _backend(root, _fence(root, _control(root)))
    checks = 0

    def wait_before_commit() -> None:
        nonlocal checks
        checks += 1
        if checks == 2:
            ready.set()
            multiprocessing.Event().wait()

    backend_any: Any = backend
    backend_any._assert_mutation_binding = wait_before_commit

    def update_summary(
        meta: dict[str, Any], _tasks: list[tuple[Path, dict[str, Any], str]]
    ) -> tuple[str, str]:
        meta["summary"] = "must roll back after SIGKILL"
        return "killed before commit", "# Must not persist\n"

    backend.mutate("AR-0001", 1, "update", "2026-09-16T15:11:00+00:00", update_summary)


def _route_effect_waiting_for_sigkill_all_routes(root_text: str, route: str, ready: Any) -> None:
    """Pause every public route after effects and before transaction commit."""
    root = Path(root_text)
    backend = _backend(root, _fence(root, _control(root)))
    original_assert = backend._assert_mutation_binding
    checks = 0

    def wait_before_commit() -> None:
        nonlocal checks
        checks += 1
        original_assert()
        if checks == 2:
            ready.set()
            multiprocessing.Event().wait()

    backend_any: Any = backend
    backend_any._assert_mutation_binding = wait_before_commit
    _perform_route(backend, route)


def _route_effect_waiting_for_sidecar_fault(
    root_text: str, ready: Any, resume: Any, result: Any
) -> None:
    """Pause a real mutation after WAL effects so its sidecars can be replaced."""
    root = Path(root_text)
    backend = _backend(root, _fence(root, _control(root)))
    original_assert = backend._assert_mutation_binding
    checks = 0

    def wait_before_commit() -> None:
        nonlocal checks
        checks += 1
        original_assert()
        if checks == 2:
            ready.set()
            if not resume.wait(5):
                raise RuntimeError("authority sidecar fault injection timed out")

    backend_any: Any = backend
    backend_any._assert_mutation_binding = wait_before_commit

    def update_summary(
        meta: dict[str, Any], _tasks: list[tuple[Path, dict[str, Any], str]]
    ) -> tuple[str, str]:
        meta["summary"] = "must roll back after WAL replacement"
        return "replace active WAL", "# Must not persist\n"

    try:
        backend.mutate(
            "AR-0001",
            1,
            "update",
            "2026-09-16T15:12:00+00:00",
            update_summary,
        )
    except Exception as error:
        result.put(("rejected", type(error).__name__, str(error)))
    else:
        result.put(("committed",))


class SQLiteMutationBarrierProcessTests(unittest.TestCase):
    def setUp(self) -> None:
        self.directory = tempfile.TemporaryDirectory()
        self.root = Path(self.directory.name)
        self.root.chmod(0o700)
        self.git_authority = self.root / "git-authority"
        self.git_authority.mkdir()
        _git(self.git_authority, "init", "-b", "main")
        _git(self.git_authority, "config", "user.name", "Test Runner")
        _git(self.git_authority, "config", "user.email", "test@example.invalid")
        (self.git_authority / "state").write_text("old\n", encoding="utf-8")
        _git(self.git_authority, "add", "state")
        _git(self.git_authority, "commit", "-m", "initial")
        self.authority = self.root / "authority.sqlite"
        self.tasks = self.root / "tasks"
        self.tasks.mkdir()
        task = {
            "schema_version": 1,
            "id": "AR-0001",
            "title": "Authority fixture task",
            "status": "open",
            "priority": "P1",
            "summary": "Ready.",
            "next_action": "Exercise the independent writer.",
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
        create_database(
            self.authority,
            BINDING,
            [(Path("AR-0001-authority-fixture.md"), task, "# Authority fixture\n")],
            imported_at="2026-09-16T00:00:00+00:00",
            source_backend="git",
            source_checkpoint="a" * 40,
        )
        self.control = SQLiteRollbackControlStore(
            self.root / "control.sqlite", PROJECT, self.authority
        )
        self.session = SQLiteBarrierSessionStore(self.control, lambda: "authority-1")
        self.assertIsNone(self.session.snapshot())
        provision(
            self.authority,
            self.root / "authority-marker.json",
            self.root / "authority-lifecycle.json",
            self.root / "authority.lock",
            PROJECT,
        )
        provision_control_binding(
            self.control.control_store_path,
            self.root / "control-binding.json",
            self.control.control_lock_path,
            PROJECT,
        )

    def tearDown(self) -> None:
        self.directory.cleanup()

    def _create_held(self) -> BarrierSessionState:
        return self.session.create(_identity())

    def _kill(self, process: BaseProcess) -> None:
        process.kill()
        process.join(5)
        self.assertEqual(-signal.SIGKILL, process.exitcode)

    def _run_writer(self) -> tuple[str, ...]:
        context = multiprocessing.get_context("fork")
        result = context.Queue()
        worker = context.Process(target=_normal_writer, args=(self.directory.name, result))
        worker.start()
        worker.join(5)
        self.assertEqual(0, worker.exitcode)
        return cast(tuple[str, ...], result.get(timeout=1))

    def _run_route(self, route: str) -> tuple[str, ...]:
        context = multiprocessing.get_context("fork")
        result = context.Queue()
        worker = context.Process(target=_route_writer, args=(self.directory.name, route, result))
        worker.start()
        worker.join(5)
        self.assertEqual(0, worker.exitcode)
        return cast(tuple[str, ...], result.get(timeout=1))

    def _authority_revision(self) -> tuple[int, str]:
        with closing(sqlite3.connect(self.authority)) as connection, connection:
            row = connection.execute(
                "SELECT revision, meta_json FROM tasks WHERE id='AR-0001'"
            ).fetchone()
        assert row is not None
        return int(row[0]), str(row[1])

    def _replace_with_copy(self, path: Path) -> None:
        replacement = path.with_name(f".{path.name}.replacement")
        replacement.write_bytes(path.read_bytes())
        replacement.chmod(0o600)
        replacement.replace(path)

    def _release(self, held: BarrierSessionState) -> BarrierSessionState:
        child = BarrierChildIdentity("forward-1", "new", held.identity.identity_digest)
        bound = self.session.bind_child(held.revision, child)
        releasing = self.session.begin_reopen(
            bound.revision,
            "new",
            {
                "operation_id": child.operation_id,
                "target": child.target,
                "barrier_identity_digest": bound.identity.identity_digest,
                "validated": True,
            },
        )
        return self.session.complete_reopen(releasing.revision, _runtime_evidence(releasing, "new"))

    def test_released_writer_factory_cannot_bypass_held_barrier(self) -> None:
        self._create_held()
        fence = _fence(self.root, self.control)
        backend = bind_released_sqlite_backend(
            self.authority,
            BINDING,
            self.tasks,
            fence,
            locked,
        )

        def update_summary(
            meta: dict[str, Any], _tasks: list[tuple[Path, dict[str, Any], str]]
        ) -> tuple[str, str]:
            meta["summary"] = "must not commit while held"
            return "rejected", "# Must not persist\n"

        with self.assertRaisesRegex(
            RuntimeError, "authority mutation rejected while barrier is held"
        ):
            backend.mutate(
                "AR-0001",
                1,
                "update",
                "2026-09-21T00:00:00+00:00",
                update_summary,
            )
        self.assertEqual(1, self._authority_revision()[0])

    def test_handoffctl_factory_uses_bound_route_when_provisioned(self) -> None:
        self._create_held()
        with (
            patch.object(handoffctl, "DATABASE", self.authority),
            patch.object(handoffctl, "CONTROL_DATABASE", self.control.control_store_path),
            patch.object(handoffctl, "AUTHORITY_MARKER", self.root / "authority-marker.json"),
            patch.object(handoffctl, "AUTHORITY_LIFECYCLE", self.root / "authority-lifecycle.json"),
            patch.object(handoffctl, "AUTHORITY_LOCK", self.root / "authority.lock"),
            patch.object(handoffctl, "CONTROL_BINDING", self.root / "control-binding.json"),
            patch.object(handoffctl, "CONTROL_LOCK", self.control.control_lock_path),
            patch.object(handoffctl, "project_binding", return_value=BINDING),
            patch.object(handoffctl, "TASKS", self.tasks),
        ):
            backend = handoffctl.mutating_sqlite_backend()
        self.assertEqual("sqlite", backend.name)
        self.assertIsNotNone(backend.backend_binding)

    def test_handoffctl_factory_binds_the_admitted_session_identity(self) -> None:
        self._release(self._create_held())
        with (
            patch.object(handoffctl, "DATABASE", self.authority),
            patch.object(handoffctl, "CONTROL_DATABASE", self.control.control_store_path),
            patch.object(handoffctl, "AUTHORITY_MARKER", self.root / "authority-marker.json"),
            patch.object(handoffctl, "AUTHORITY_LIFECYCLE", self.root / "authority-lifecycle.json"),
            patch.object(handoffctl, "AUTHORITY_LOCK", self.root / "authority.lock"),
            patch.object(handoffctl, "CONTROL_BINDING", self.root / "control-binding.json"),
            patch.object(handoffctl, "CONTROL_LOCK", self.control.control_lock_path),
            patch.object(handoffctl, "project_binding", return_value=BINDING),
            patch.object(handoffctl, "TASKS", self.tasks),
        ):
            backend = handoffctl.mutating_sqlite_backend()

        second = self.session.create(
            _identity(
                attempt="attempt-factory-next",
                state_revision=2,
                barrier="barrier-factory-next",
                fence="fence-factory-next",
                owner="owner-factory-next",
            )
        )
        second_released = self._release(second)
        with self.assertRaisesRegex(MutationFenceError, "barrier session identity changed"):
            backend.update_observations(
                {"worker-1": {"branch": "stale", "head": "d" * 40, "dirty": 0}},
                "2026-09-21T00:17:00+00:00",
            )
        self.assertEqual(second_released, self.session.snapshot())
        self.assertEqual(1, self._authority_revision()[0])

    def test_bound_route_commits_after_independently_verified_release(self) -> None:
        held = self._create_held()
        self._release(held)
        backend = bind_released_sqlite_backend(
            self.authority,
            BINDING,
            self.tasks,
            _fence(self.root, self.control),
            locked,
        )

        def update_summary(
            meta: dict[str, Any], _tasks: list[tuple[Path, dict[str, Any], str]]
        ) -> tuple[str, str]:
            meta["summary"] = "committed after verified release"
            return "released writer", "# Authority fixture\n\nWriter committed.\n"

        backend.mutate(
            "AR-0001",
            1,
            "update",
            "2026-09-21T00:01:00+00:00",
            update_summary,
        )
        self.assertEqual(2, self._authority_revision()[0])

    def test_trusted_provisioning_creates_released_baseline(self) -> None:
        with (
            patch.object(handoffctl, "DATABASE", self.authority),
            patch.object(handoffctl, "CONTROL_DATABASE", self.control.control_store_path),
            patch.object(handoffctl, "AUTHORITY_MARKER", self.root / "authority-marker.json"),
            patch.object(handoffctl, "AUTHORITY_LIFECYCLE", self.root / "authority-lifecycle.json"),
            patch.object(handoffctl, "AUTHORITY_LOCK", self.root / "authority.lock"),
            patch.object(handoffctl, "CONTROL_BINDING", self.root / "control-binding.json"),
            patch.object(handoffctl, "CONTROL_LOCK", self.control.control_lock_path),
            patch.object(handoffctl, "project_binding", return_value=BINDING),
        ):
            handoffctl.provision_sqlite_barrier()
        state = self.session.snapshot()
        self.assertIsNotNone(state)
        assert state is not None
        self.assertEqual("released", state.status)
        self.assertTrue(state.identity.attempt_id.startswith("baseline-"))

    def test_independent_writer_rejects_until_verified_release(self) -> None:
        self.assertEqual(
            (
                "rejected",
                "MutationFenceError",
                "durable control barrier is missing or ambiguous",
            ),
            self._run_writer(),
        )
        held = self._create_held()
        context = multiprocessing.get_context("fork")
        ready = context.Event()
        holder = context.Process(target=_held_scope_owner, args=(self.directory.name, ready))
        holder.start()
        self.assertTrue(ready.wait(5))
        self._kill(holder)
        self.assertEqual(held, self.session.snapshot())

        self.assertEqual(
            ("rejected", "MutationFenceError", "authority mutation rejected while barrier is held"),
            self._run_writer(),
        )
        self.assertEqual(1, self._authority_revision()[0])

        child = BarrierChildIdentity("forward-1", "new", held.identity.identity_digest)
        bound = self.session.bind_child(held.revision, child)
        releasing = self.session.begin_reopen(
            bound.revision,
            "new",
            {
                "operation_id": child.operation_id,
                "target": child.target,
                "barrier_identity_digest": bound.identity.identity_digest,
                "validated": True,
            },
        )
        self.assertEqual(
            (
                "rejected",
                "MutationFenceError",
                "authority mutation rejected while barrier is releasing",
            ),
            self._run_writer(),
        )
        self.assertEqual(1, self._authority_revision()[0])

        released = self.session.complete_reopen(
            releasing.revision, _runtime_evidence(releasing, "new")
        )
        self.assertEqual("released", released.status)
        self.assertEqual(("committed",), self._run_writer())
        revision, meta_json = self._authority_revision()
        self.assertEqual(2, revision)
        self.assertIn("mutated after verified release", meta_json)

    def test_writer_times_out_on_control_lock_without_mutating_authority(self) -> None:
        released = self._release(self._create_held())
        context = multiprocessing.get_context("fork")
        ready = context.Event()
        holder = context.Process(
            target=_held_control_owner,
            args=(self.directory.name, ready),
        )
        holder.start()
        self.assertTrue(ready.wait(5))

        result = context.Queue()
        with patch.object(mutation_fence, "LOCK_TIMEOUT_SECONDS", 0.2):
            writer = context.Process(
                target=_normal_writer,
                args=(self.directory.name, result),
            )
            writer.start()
            writer.join(3)
        self.assertEqual(0, writer.exitcode)
        self.assertEqual(
            (
                "rejected",
                "MutationFenceError",
                "control.lock acquisition timed out after 0.2s",
            ),
            result.get(timeout=1),
        )
        self._kill(holder)
        self.assertEqual(released, self.session.snapshot())
        self.assertEqual(("committed",), self._run_writer())
        self.assertEqual(2, self._authority_revision()[0])

    def test_bound_writer_rejects_released_session_replacement(self) -> None:
        first = self._release(self._create_held())
        context = multiprocessing.get_context("fork")
        ready = context.Event()
        proceed = context.Event()
        result = context.Queue()
        writer = context.Process(
            target=_bound_writer_after_replacement,
            args=(self.directory.name, first.identity, ready, proceed, result),
        )
        writer.start()
        self.assertTrue(ready.wait(5))

        second = self.session.create(
            _identity(
                attempt="attempt-next",
                state_revision=2,
                barrier="barrier-next",
                fence="fence-next",
                owner="owner-next",
            )
        )
        second_released = self._release(second)
        proceed.set()
        writer.join(5)
        self.assertEqual(0, writer.exitcode)
        self.assertEqual(
            ("rejected", "MutationFenceError", "barrier session identity changed"),
            result.get(timeout=1),
        )
        self.assertEqual(second_released, self.session.snapshot())
        self.assertEqual(1, self._authority_revision()[0])

    def test_every_inventoried_route_rejects_while_barrier_is_held(self) -> None:
        self._create_held()
        expected = (
            "rejected",
            "MutationFenceError",
            "authority mutation rejected while barrier is held",
        )
        for route in ("mutate", "update_observations", "append_command_result", "retire"):
            self.assertEqual(expected, self._run_route(route), route)
        self.assertEqual(1, self._authority_revision()[0])

    def test_every_inventoried_route_rejects_while_barrier_is_releasing(self) -> None:
        held = self._create_held()
        child = BarrierChildIdentity("forward-1", "new", held.identity.identity_digest)
        bound = self.session.bind_child(held.revision, child)
        self.session.begin_reopen(
            bound.revision,
            "new",
            {
                "operation_id": child.operation_id,
                "target": child.target,
                "barrier_identity_digest": bound.identity.identity_digest,
                "validated": True,
            },
        )
        expected = (
            "rejected",
            "MutationFenceError",
            "authority mutation rejected while barrier is releasing",
        )
        for route in ("mutate", "update_observations", "append_command_result", "retire"):
            self.assertEqual(expected, self._run_route(route), route)
        self.assertEqual(1, self._authority_revision()[0])

    def test_every_inventoried_route_rejects_while_barrier_is_ambiguous(self) -> None:
        held = self._create_held()
        self.session.mark_ambiguous(held.revision, "route-state-test")
        expected = (
            "rejected",
            "MutationFenceError",
            "authority mutation rejected while barrier is ambiguous",
        )
        for route in ("mutate", "update_observations", "append_command_result", "retire"):
            self.assertEqual(expected, self._run_route(route), route)
        self.assertEqual(1, self._authority_revision()[0])

    def test_sigkill_after_route_effects_rolls_back_and_releases_locks(self) -> None:
        released = self._release(self._create_held())
        context = multiprocessing.get_context("fork")
        ready = context.Event()
        crashed = context.Process(
            target=_route_effect_waiting_for_sigkill,
            args=(self.directory.name, ready),
        )
        crashed.start()
        self.assertTrue(ready.wait(5))
        self._kill(crashed)

        revision, meta_json = self._authority_revision()
        self.assertEqual(1, revision)
        self.assertIn('"summary": "Ready."', meta_json)
        self.assertNotIn("must roll back after SIGKILL", meta_json)
        with closing(sqlite3.connect(self.authority)) as connection, connection:
            events = connection.execute(
                "SELECT revision, kind FROM events WHERE task_id='AR-0001' ORDER BY revision"
            ).fetchall()
        self.assertEqual([(1, "import")], events)
        self.assertEqual(released, self.session.snapshot())
        self.assertEqual(("committed",), self._run_writer())
        self.assertEqual(2, self._authority_revision()[0])

    def _assert_route_sigkill_rolls_back(self, route: str) -> None:
        released = self._release(self._create_held())
        context = multiprocessing.get_context("fork")
        ready = context.Event()
        crashed = context.Process(
            target=_route_effect_waiting_for_sigkill_all_routes,
            args=(self.directory.name, route, ready),
        )
        crashed.start()
        self.assertTrue(ready.wait(5), route)
        self._kill(crashed)
        self.assertEqual(released, self.session.snapshot())
        self.assertEqual(1, self._authority_revision()[0])
        with closing(sqlite3.connect(self.authority)) as connection, connection:
            self.assertEqual(
                ("active",),
                connection.execute("SELECT value FROM metadata WHERE key='state'").fetchone(),
            )
            self.assertEqual(
                (0,), connection.execute("SELECT COUNT(*) FROM command_results").fetchone()
            )

    def test_sigkill_after_update_observations_effect_rolls_back(self) -> None:
        self._assert_route_sigkill_rolls_back("update_observations")

    def test_sigkill_after_append_command_result_effect_rolls_back(self) -> None:
        self._assert_route_sigkill_rolls_back("append_command_result")

    def test_sigkill_after_retire_effect_rolls_back(self) -> None:
        self._assert_route_sigkill_rolls_back("retire")

    def test_active_authority_wal_replacement_rejects_without_publication(self) -> None:
        released = self._release(self._create_held())
        context = multiprocessing.get_context("fork")
        ready = context.Event()
        resume = context.Event()
        result = context.Queue()
        writer = context.Process(
            target=_route_effect_waiting_for_sidecar_fault,
            args=(self.directory.name, ready, resume, result),
        )
        writer.start()
        self.assertTrue(ready.wait(5))

        for suffix in ("-wal", "-shm"):
            sidecar = Path(f"{self.authority}{suffix}")
            self.assertTrue(sidecar.is_file())
            sidecar.unlink()
            sidecar.write_bytes(b"hostile authority sidecar replacement")
            sidecar.chmod(0o600)
        resume.set()
        writer.join(5)
        self.assertEqual(0, writer.exitcode)
        outcome = cast(tuple[str, ...], result.get(timeout=1))
        self.assertEqual("rejected", outcome[0])
        self.assertNotEqual(("committed",), outcome)

        for suffix in ("-wal", "-shm"):
            Path(f"{self.authority}{suffix}").unlink(missing_ok=True)
        revision, meta_json = self._authority_revision()
        self.assertEqual(1, revision)
        self.assertIn('"summary": "Ready."', meta_json)
        self.assertNotIn("must roll back after WAL replacement", meta_json)
        with closing(sqlite3.connect(self.authority)) as connection, connection:
            self.assertEqual(
                [(1, "import")],
                connection.execute(
                    "SELECT revision, kind FROM events WHERE task_id='AR-0001' ORDER BY revision"
                ).fetchall(),
            )
            self.assertEqual(("ok",), connection.execute("PRAGMA integrity_check").fetchone())
        self.assertEqual(released, self.session.snapshot())
        self.assertEqual(("committed",), self._run_writer())

    def _assert_route_rejects_authority_sidecar_replacement(self, route: str) -> None:
        self._release(self._create_held())
        context = multiprocessing.get_context("fork")
        ready = context.Event()
        resume = context.Event()
        result = context.Queue()
        writer = context.Process(
            target=_route_effect_waiting_for_sidecar_fault_all_routes,
            args=(self.directory.name, route, ready, resume, result),
        )
        writer.start()
        self.assertTrue(ready.wait(5), route)
        for suffix in ("-wal", "-shm"):
            sidecar = Path(f"{self.authority}{suffix}")
            self.assertTrue(sidecar.is_file(), (route, suffix))
            sidecar.unlink()
            sidecar.write_bytes(b"hostile authority sidecar replacement")
            sidecar.chmod(0o600)
        resume.set()
        writer.join(5)
        self.assertEqual(0, writer.exitcode, route)
        outcome = cast(tuple[str, ...], result.get(timeout=1))
        self.assertEqual("rejected", outcome[0], (route, outcome))
        self.assertIn("sidecar identity changed", outcome[2], (route, outcome))
        self.assertEqual(1, self._authority_revision()[0])

    def test_mutate_rejects_authority_sidecar_replacement(self) -> None:
        self._assert_route_rejects_authority_sidecar_replacement("mutate")

    def test_update_observations_rejects_authority_sidecar_replacement(self) -> None:
        self._assert_route_rejects_authority_sidecar_replacement("update_observations")

    def test_append_command_result_rejects_authority_sidecar_replacement(self) -> None:
        self._assert_route_rejects_authority_sidecar_replacement("append_command_result")

    def test_retire_rejects_authority_sidecar_replacement(self) -> None:
        self._assert_route_rejects_authority_sidecar_replacement("retire")

    def test_forged_released_row_rejects_before_authority_mutation(self) -> None:
        held = self._create_held()
        with closing(sqlite3.connect(self.control.control_store_path)) as connection, connection:
            connection.execute(
                "UPDATE barrier_session SET status='released',revision=?,identity_digest=? "
                "WHERE project_id=?",
                (held.revision + 1, "0" * 64, PROJECT),
            )
            connection.commit()

        self.assertEqual(
            (
                "rejected",
                "MutationFenceError",
                "durable control barrier state is invalid",
            ),
            self._run_writer(),
        )
        revision, meta_json = self._authority_revision()
        self.assertEqual(1, revision)
        self.assertIn('"summary": "Ready."', meta_json)
        self.assertNotIn("mutated after verified release", meta_json)
        with closing(sqlite3.connect(self.authority)) as connection, connection:
            events = connection.execute(
                "SELECT revision, kind FROM events WHERE task_id='AR-0001' ORDER BY revision"
            ).fetchall()
            results = connection.execute("SELECT COUNT(*) FROM command_results").fetchone()
        self.assertEqual([(1, "import")], events)
        self.assertEqual((0,), results)

    def test_every_inventoried_route_rejects_forged_released_row(self) -> None:
        """A stale/forged release must fence every SQLite mutation route."""
        held = self._create_held()
        with closing(sqlite3.connect(self.control.control_store_path)) as connection, connection:
            connection.execute(
                "UPDATE barrier_session SET status='released',revision=?,identity_digest=? "
                "WHERE project_id=?",
                (held.revision + 1, "0" * 64, PROJECT),
            )
            connection.commit()

        expected = (
            "rejected",
            "MutationFenceError",
            "durable control barrier state is invalid",
        )
        for route in ("mutate", "update_observations", "append_command_result", "retire"):
            self.assertEqual(expected, self._run_route(route), route)

        revision, meta_json = self._authority_revision()
        self.assertEqual(1, revision)
        self.assertIn('"summary": "Ready."', meta_json)
        with closing(sqlite3.connect(self.authority)) as connection, connection:
            self.assertEqual(
                [(1, "import")],
                connection.execute(
                    "SELECT revision, kind FROM events WHERE task_id='AR-0001' ORDER BY revision"
                ).fetchall(),
            )
            self.assertEqual(
                (0,),
                connection.execute("SELECT COUNT(*) FROM command_results").fetchone(),
            )

    def test_every_inventoried_route_rejects_control_store_replacement(self) -> None:
        self._create_held()
        self._replace_with_copy(self.control.control_store_path)
        expected = (
            "rejected",
            "MutationFenceError",
            "control store identity changed",
        )
        for route in ("mutate", "update_observations", "append_command_result", "retire"):
            self.assertEqual(expected, self._run_route(route), route)
        self.assertEqual(1, self._authority_revision()[0])

    def test_every_inventoried_route_rejects_replaced_released_owner(self) -> None:
        self._release(self._create_held())
        replacement = _identity(
            attempt="attempt-replaced",
            state_revision=2,
            barrier="barrier-replaced",
            fence="fence-replaced",
            owner="owner-replaced",
        )
        with closing(sqlite3.connect(self.control.control_store_path)) as connection, connection:
            connection.execute(
                "UPDATE barrier_session SET attempt_id=?,state_revision=?,"
                "durable_barrier_id=?,fencing_token=?,fencing_owner=?,identity_digest=?,"
                "forward_child=NULL,rollback_child=NULL "
                "WHERE project_id=?",
                (
                    replacement.attempt_id,
                    replacement.state_revision,
                    replacement.durable_barrier_id,
                    replacement.fencing_token,
                    replacement.fencing_owner,
                    replacement.identity_digest,
                    PROJECT,
                ),
            )
            connection.commit()
        expected = (
            "rejected",
            "MutationFenceError",
            "durable control barrier state is invalid",
        )
        for route in ("mutate", "update_observations", "append_command_result", "retire"):
            self.assertEqual(expected, self._run_route(route), route)
        self.assertEqual(1, self._authority_revision()[0])

    def test_bound_fence_rejects_identity_change_after_admission(self) -> None:
        self._release(self._create_held())
        backend = _backend(self.root, _fence(self.root, self.control))

        def update_summary(
            meta: dict[str, Any], _tasks: list[tuple[Path, dict[str, Any], str]]
        ) -> tuple[str, str]:
            meta["summary"] = "first bound mutation"
            return "first bound mutation", "# First bound mutation\n"

        backend.mutate(
            "AR-0001",
            1,
            "update",
            "2026-09-21T00:14:00+00:00",
            update_summary,
        )
        replacement = _identity(
            attempt="attempt-bound-replaced",
            state_revision=2,
            barrier="barrier-bound-replaced",
            fence="fence-bound-replaced",
            owner="owner-bound-replaced",
        )
        with closing(sqlite3.connect(self.control.control_store_path)) as connection, connection:
            current_revision = int(
                connection.execute(
                    "SELECT revision FROM barrier_session WHERE project_id=?", (PROJECT,)
                ).fetchone()[0]
            )
            connection.execute(
                "UPDATE barrier_session SET attempt_id=?,state_revision=?,"
                "durable_barrier_id=?,fencing_token=?,fencing_owner=?,identity_digest=?,"
                "forward_child=NULL,rollback_child=NULL WHERE project_id=?",
                (
                    replacement.attempt_id,
                    replacement.state_revision,
                    replacement.durable_barrier_id,
                    replacement.fencing_token,
                    replacement.fencing_owner,
                    replacement.identity_digest,
                    PROJECT,
                ),
            )
            connection.execute(
                "INSERT INTO barrier_session_intent "
                "(project_id,intent_id,attempt_id,expected_revision,proposed_revision,"
                "proposed_status,identity_digest,outcome,cause_code) VALUES (?,?,?,?,?,?,?,?,?)",
                (
                    PROJECT,
                    "bound-replacement-intent",
                    replacement.attempt_id,
                    current_revision - 1,
                    current_revision,
                    "released",
                    replacement.identity_digest,
                    "committed",
                    None,
                ),
            )
            connection.commit()
        with self.assertRaisesRegex(MutationFenceError, "barrier session identity changed"):
            backend.update_observations(
                {"worker-1": {"branch": "stale", "head": "c" * 40, "dirty": 0}},
                "2026-09-21T00:14:01+00:00",
            )
        self.assertEqual(2, self._authority_revision()[0])

    def test_every_inventoried_route_rejects_authority_replacement(self) -> None:
        self._create_held()
        self._replace_with_copy(self.authority)
        expected = (
            "rejected",
            "MutationFenceError",
            "authority database identity changed",
        )
        for route in ("mutate", "update_observations", "append_command_result", "retire"):
            self.assertEqual(expected, self._run_route(route), route)
        self.assertEqual(1, self._authority_revision()[0])

    def test_sigkill_session_commit_recovers_ambiguous_then_verified_release(self) -> None:
        context = multiprocessing.get_context("fork")
        ready = context.Event()
        crashed = context.Process(
            target=_session_commit_waiting_for_sigkill,
            args=(self.directory.name, ready),
        )
        crashed.start()
        self.assertTrue(ready.wait(5))
        self._kill(crashed)

        committed = self.session.snapshot()
        assert committed is not None
        self.assertEqual(
            ("held", 1, _identity()),
            (
                committed.status,
                committed.revision,
                committed.identity,
            ),
        )
        ambiguous = self.session.recover_unknown()
        assert ambiguous is not None
        self.assertEqual(("ambiguous", 2), (ambiguous.status, ambiguous.revision))
        self.assertEqual(_identity(), ambiguous.identity)
        self.assertEqual(
            (
                "rejected",
                "MutationFenceError",
                "authority mutation rejected while barrier is ambiguous",
            ),
            self._run_writer(),
        )
        self.assertEqual(1, self._authority_revision()[0])

        replacement = BarrierSessionState(
            _identity(
                attempt="attempt-2",
                state_revision=2,
                barrier="barrier-2",
                fence="fence-2",
                owner="owner-2",
            ),
            "held",
            1,
        )
        reconciled = self.session.reconcile_ambiguous(ambiguous.revision, replacement)
        self.assertEqual(replacement, reconciled)
        self.assertEqual(
            ("rejected", "MutationFenceError", "authority mutation rejected while barrier is held"),
            self._run_writer(),
        )
        released = self._release(reconciled)
        self.assertEqual("released", released.status)
        self.assertEqual(("committed",), self._run_writer())
        self.assertEqual(2, self._authority_revision()[0])

    def test_sigkill_after_authority_effect_requires_recovery_and_new_fence(self) -> None:
        context = multiprocessing.get_context("fork")
        ready = context.Event()
        worker = context.Process(
            target=_authority_effect_waiting_for_sigkill,
            args=(self.directory.name, ready),
        )
        worker.start()
        self.assertTrue(ready.wait(5))
        worker.join(5)
        self.assertEqual(17, worker.exitcode)

        reopened = SQLiteBarrierSessionStore(_control(self.root), lambda: "authority-1")
        held = reopened.snapshot()
        assert held is not None
        self.assertEqual(("held", 1), (held.status, held.revision))
        with closing(sqlite3.connect(self.authority)) as connection, connection:
            self.assertEqual(
                "effect committed before worker death",
                connection.execute("SELECT body FROM tasks WHERE id='AR-0001'").fetchone()[0],
            )
        with closing(sqlite3.connect(self.control.control_store_path)) as connection, connection:
            self.assertEqual(
                [("prepared",)],
                connection.execute(
                    "SELECT outcome FROM authority_effect_intent WHERE project_id=?",
                    (PROJECT,),
                ).fetchall(),
            )
            self.assertEqual(
                (
                    "op-1:commit",
                    "sqlite",
                    "new",
                    "attempt-1",
                    _identity().identity_digest,
                    "fence-1",
                    1,
                    "artifact-1",
                    "manifest-1",
                    "selector-1",
                    "runtime-1",
                    "prepared",
                ),
                connection.execute(
                    "SELECT operation_id,backend,target,attempt_id,identity_digest,"
                    "fencing_token,session_revision,artifact_identity,manifest_identity,"
                    "selector_identity,runtime_identity,outcome "
                    "FROM authority_effect_intent WHERE project_id=?",
                    (PROJECT,),
                ).fetchone(),
            )
        self.assertEqual(
            (
                "rejected",
                "MutationFenceError",
                "durable control barrier state is invalid",
            ),
            self._run_writer(),
        )
        with self.assertRaisesRegex(ControlStoreError, "only ambiguous"):
            reopened.reconcile_ambiguous(held.revision, held)

        ambiguous = reopened.recover_unknown()
        assert ambiguous is not None
        self.assertEqual(("ambiguous", 2), (ambiguous.status, ambiguous.revision))
        with closing(sqlite3.connect(self.control.control_store_path)) as connection, connection:
            self.assertEqual(
                [("ambiguous", "process-death")],
                connection.execute(
                    "SELECT outcome,cause_code FROM authority_effect_intent WHERE project_id=?",
                    (PROJECT,),
                ).fetchall(),
            )
            self.assertEqual(
                (
                    "op-1:commit",
                    "sqlite",
                    "new",
                    "attempt-1",
                    _identity().identity_digest,
                    "fence-1",
                    1,
                    "artifact-1",
                    "manifest-1",
                    "selector-1",
                    "runtime-1",
                    "ambiguous",
                ),
                connection.execute(
                    "SELECT operation_id,backend,target,attempt_id,identity_digest,"
                    "fencing_token,session_revision,artifact_identity,manifest_identity,"
                    "selector_identity,runtime_identity,outcome "
                    "FROM authority_effect_intent WHERE project_id=?",
                    (PROJECT,),
                ).fetchone(),
            )
        with self.assertRaisesRegex(ControlStoreError, "distinct newer fence"):
            reopened.reconcile_ambiguous(ambiguous.revision, held)

        replacement = BarrierSessionState(
            _identity(
                attempt="attempt-effect-recovered",
                state_revision=2,
                barrier="barrier-effect-recovered",
                fence="fence-effect-recovered",
                owner="owner-effect-recovered",
            ),
            "held",
            1,
        )
        self.assertEqual(replacement, reopened.reconcile_ambiguous(2, replacement))
        with self.assertRaisesRegex(ControlStoreError, "ambiguous prior outcome"):
            reopened.prepare_authority_effect(1, "op-1:commit", "sqlite")

        stale_called = False

        def stale_effect() -> dict[str, object]:
            nonlocal stale_called
            stale_called = True
            return {
                "operation_id": "op-stale:commit",
                "fencing_token": "fence-effect-1",
                "mutates_authority": True,
            }

        stale_admission = CommitAdmissionBundle(
            backend="sqlite",
            target="new",
            operation_id="op-stale:commit",
            fencing_token="fence-effect-1",  # noqa: S106
            state_revision=1,
            barrier_id="barrier-1",
            artifact_identity="artifact-1",
            manifest_identity="manifest-1",
            selector_identity="selector-1",
            runtime_identity="runtime-1",
        )
        with self.assertRaisesRegex(ControlStoreError, "fencing token conflict"):
            DurableBoundAuthorityMutation(stale_admission, reopened, session_revision=1).execute(
                stale_effect
            )
        self.assertFalse(stale_called)

        new_admission = CommitAdmissionBundle(
            backend="sqlite",
            target="new",
            operation_id="op-2:commit",
            fencing_token="fence-effect-recovered",  # noqa: S106
            state_revision=1,
            barrier_id="barrier-effect-recovered",
            artifact_identity="artifact-1",
            manifest_identity="manifest-1",
            selector_identity="selector-1",
            runtime_identity="runtime-1",
        )
        keepalive = sqlite3.connect(self.authority)
        keepalive.execute("PRAGMA wal_autocheckpoint=0")
        keepalive.execute("PRAGMA user_version=1")
        keepalive.commit()

        def identity(path: Path) -> tuple[int, int] | None:
            try:
                status = path.lstat()
            except FileNotFoundError:
                return None
            return status.st_dev, status.st_ino

        sqlite_capability = SQLiteCommitCapability(
            self.authority,
            admission=new_admission,
            admission_reread=lambda: new_admission.__dict__,
            expected_db_identity=identity(self.authority),  # type: ignore[arg-type]
            expected_wal_identity=identity(self.authority.with_name("authority.sqlite-wal")),
            expected_shm_identity=identity(self.authority.with_name("authority.sqlite-shm")),
        )

        def reopened_effect(connection: sqlite3.Connection) -> None:
            connection.execute(
                "UPDATE tasks SET body='newer fence committed after recovery' WHERE id='AR-0001'"
            )

        DurableBoundAuthorityMutation(new_admission, reopened, session_revision=1).execute(
            lambda: sqlite_capability.commit(reopened_effect)
        )
        keepalive.close()
        with closing(sqlite3.connect(self.authority)) as connection, connection:
            self.assertEqual(
                "newer fence committed after recovery",
                connection.execute("SELECT body FROM tasks WHERE id='AR-0001'").fetchone()[0],
            )
        recovered_identity = _identity(
            attempt="attempt-effect-recovered",
            state_revision=2,
            barrier="barrier-effect-recovered",
            fence="fence-effect-recovered",
            owner="owner-effect-recovered",
        )
        with closing(sqlite3.connect(self.control.control_store_path)) as connection, connection:
            self.assertEqual(
                (
                    "op-2:commit",
                    "sqlite",
                    "new",
                    recovered_identity.attempt_id,
                    recovered_identity.identity_digest,
                    recovered_identity.fencing_token,
                    1,
                    "artifact-1",
                    "manifest-1",
                    "selector-1",
                    "runtime-1",
                    "committed",
                ),
                connection.execute(
                    "SELECT operation_id,backend,target,attempt_id,identity_digest,"
                    "fencing_token,session_revision,artifact_identity,manifest_identity,"
                    "selector_identity,runtime_identity,outcome "
                    "FROM authority_effect_intent WHERE project_id=? AND operation_id=?",
                    (PROJECT, "op-2:commit"),
                ).fetchone(),
            )

    def test_sigkill_after_git_authority_effect_requires_recovery_and_new_fence(self) -> None:
        context = multiprocessing.get_context("fork")
        ready = context.Event()
        worker = context.Process(
            target=_git_authority_effect_waiting_for_sigkill,
            args=(self.directory.name, ready),
        )
        worker.start()
        self.assertTrue(ready.wait(5))
        worker.join(5)
        self.assertEqual(17, worker.exitcode)
        self.assertEqual(
            "effect committed before worker death\n",
            (self.git_authority / "state").read_text(encoding="utf-8"),
        )

        reopened = SQLiteBarrierSessionStore(_control(self.root), lambda: "authority-1")
        held = reopened.snapshot()
        assert held is not None
        self.assertEqual(("held", 1), (held.status, held.revision))
        with closing(sqlite3.connect(self.control.control_store_path)) as connection, connection:
            self.assertEqual(
                [("prepared",)],
                connection.execute(
                    "SELECT outcome FROM authority_effect_intent WHERE project_id=?",
                    (PROJECT,),
                ).fetchall(),
            )

        ambiguous = reopened.recover_unknown()
        assert ambiguous is not None
        self.assertEqual(("ambiguous", 2), (ambiguous.status, ambiguous.revision))
        with self.assertRaisesRegex(ControlStoreError, "distinct newer fence"):
            reopened.reconcile_ambiguous(ambiguous.revision, held)

        replacement = BarrierSessionState(
            _identity(
                attempt="attempt-git-effect-recovered",
                state_revision=2,
                barrier="barrier-git-effect-recovered",
                fence="fence-git-effect-recovered",
                owner="owner-git-effect-recovered",
            ),
            "held",
            1,
        )
        self.assertEqual(replacement, reopened.reconcile_ambiguous(2, replacement))
        stale_admission = CommitAdmissionBundle(
            backend="git",
            target="new",
            operation_id="op-git-stale:commit",
            fencing_token="fence-1",  # noqa: S106
            state_revision=1,
            barrier_id="barrier-1",
            artifact_identity="artifact-1",
            manifest_identity="manifest-1",
            selector_identity="selector-1",
            runtime_identity="runtime-1",
        )
        with self.assertRaisesRegex(ControlStoreError, "fencing token conflict"):
            DurableBoundAuthorityMutation(stale_admission, reopened, session_revision=1).execute(
                lambda: self.fail("stale Git admission reached the effect")
            )

        (self.git_authority / "state").write_text(
            "newer fence committed after recovery\n", encoding="utf-8"
        )
        _git(self.git_authority, "add", "state")
        new_admission = CommitAdmissionBundle(
            backend="git",
            target="new",
            operation_id="op-git-2:commit",
            fencing_token="fence-git-effect-recovered",  # noqa: S106
            state_revision=1,
            barrier_id="barrier-git-effect-recovered",
            artifact_identity="artifact-1",
            manifest_identity="manifest-1",
            selector_identity="selector-1",
            runtime_identity="runtime-1",
        )
        git_capability = GitCommitCapability(
            self.git_authority,
            admission=new_admission,
            admission_reread=lambda: new_admission.__dict__,
            expected_branch="main",
            expected_head=_git(self.git_authority, "rev-parse", "HEAD"),
        )
        DurableBoundAuthorityMutation(new_admission, reopened, session_revision=1).execute(
            lambda: git_capability.commit("op-git-2 authority commit")
        )
        self.assertEqual(
            "newer fence committed after recovery\n",
            (self.git_authority / "state").read_text(encoding="utf-8"),
        )
        with closing(sqlite3.connect(self.control.control_store_path)) as connection, connection:
            effect_outcomes = connection.execute(
                "SELECT outcome FROM authority_effect_intent WHERE project_id=?",
                (PROJECT,),
            ).fetchall()
        self.assertEqual([("ambiguous",), ("committed",)], effect_outcomes)
        recovered_identity = _identity(
            attempt="attempt-git-effect-recovered",
            state_revision=2,
            barrier="barrier-git-effect-recovered",
            fence="fence-git-effect-recovered",
            owner="owner-git-effect-recovered",
        )
        with closing(sqlite3.connect(self.control.control_store_path)) as connection, connection:
            self.assertEqual(
                (
                    "op-git-2:commit",
                    "git",
                    "new",
                    recovered_identity.attempt_id,
                    recovered_identity.identity_digest,
                    recovered_identity.fencing_token,
                    1,
                    "artifact-1",
                    "manifest-1",
                    "selector-1",
                    "runtime-1",
                    "committed",
                ),
                connection.execute(
                    "SELECT operation_id,backend,target,attempt_id,identity_digest,"
                    "fencing_token,session_revision,artifact_identity,manifest_identity,"
                    "selector_identity,runtime_identity,outcome "
                    "FROM authority_effect_intent WHERE project_id=? AND operation_id=?",
                    (PROJECT, "op-git-2:commit"),
                ).fetchone(),
            )

    def test_authority_effect_journal_validates_identity_and_single_use(self) -> None:
        with self.assertRaisesRegex(ControlStoreError, "session revision is invalid"):
            self.session.prepare_authority_effect(0, "op-1", "sqlite")
        with self.assertRaisesRegex(ControlStoreError, "identity is invalid"):
            self.session.prepare_authority_effect(1, "", "sqlite")
        with self.assertRaisesRegex(ControlStoreError, "backend or target"):
            self.session.prepare_authority_effect(1, "op-1", "git", "sideways")
        for values in (
            ("", "op", "sqlite", "new", "attempt", "d" * 64, "fence", 1),
            ("intent", "op", "other", "new", "attempt", "d" * 64, "fence", 1),
            ("intent", "op", "sqlite", "new", "attempt", "d" * 64, "fence", 0),
        ):
            with self.assertRaisesRegex(ControlStoreError, "identity|backend|revision"):
                AuthorityEffectIntent(*values)
        with self.assertRaisesRegex(ControlStoreError, "admission identity is invalid"):
            AuthorityEffectIntent(
                "intent",
                "op",
                "sqlite",
                "new",
                "attempt",
                "d" * 64,
                "fence",
                1,
                "",
                "manifest",
                "selector",
                "runtime",
            )
        with self.assertRaisesRegex(ControlStoreError, "admission identity is incomplete"):
            AuthorityEffectIntent(
                "intent",
                "op",
                "sqlite",
                "new",
                "attempt",
                "d" * 64,
                "fence",
                1,
                "artifact",
            )
        with self.assertRaisesRegex(ControlStoreError, "admission identity is invalid"):
            self.session.prepare_authority_effect(
                1,
                "op-invalid-admission",
                "sqlite",
                expected_artifact_identity="",
            )
        with self.assertRaisesRegex(ControlStoreError, "admission identity is incomplete"):
            self.session.prepare_authority_effect(
                1,
                "op-incomplete-admission",
                "sqlite",
                expected_artifact_identity="artifact",
            )

        held = self._create_held()
        with self.assertRaisesRegex(ControlStoreError, "fencing token conflict"):
            self.session.prepare_authority_effect(
                held.revision,
                "op-fencing-mismatch",
                "sqlite",
                expected_fencing_token="foreign-fence",  # noqa: S106
            )
        with self.assertRaisesRegex(ControlStoreError, "barrier identity conflict"):
            self.session.prepare_authority_effect(
                held.revision,
                "op-barrier-mismatch",
                "sqlite",
                expected_barrier_id="foreign-barrier",
            )
        intent = self.session.prepare_authority_effect(
            held.revision,
            "op-1",
            "sqlite",
            expected_fencing_token=held.identity.fencing_token,
            expected_barrier_id=held.identity.durable_barrier_id,
            expected_artifact_identity="artifact-1",
            expected_manifest_identity="manifest-1",
            expected_selector_identity="selector-1",
            expected_runtime_identity="runtime-1",
        )
        with closing(sqlite3.connect(self.control.control_store_path)) as connection, connection:
            persisted = connection.execute(
                "SELECT operation_id,backend,target,attempt_id,identity_digest,"
                "fencing_token,session_revision,artifact_identity,manifest_identity,"
                "selector_identity,runtime_identity,outcome "
                "FROM authority_effect_intent WHERE project_id=? AND intent_id=?",
                (PROJECT, intent.intent_id),
            ).fetchone()
        self.assertEqual(
            (
                intent.operation_id,
                intent.backend,
                intent.target,
                held.identity.attempt_id,
                held.identity.identity_digest,
                held.identity.fencing_token,
                held.revision,
                "artifact-1",
                "manifest-1",
                "selector-1",
                "runtime-1",
                "prepared",
            ),
            persisted,
        )
        with self.assertRaisesRegex(ControlStoreError, "outcome is invalid"):
            self.session.finish_authority_effect(intent, "unknown")
        with self.assertRaisesRegex(ControlStoreError, "intent is required"):
            self.session.finish_authority_effect(object(), "committed")  # type: ignore[arg-type]
        with self.assertRaisesRegex(ControlStoreError, "receipt identity mismatch"):
            self.session.finish_authority_effect(intent, "committed")
        with closing(sqlite3.connect(self.control.control_store_path)) as connection, connection:
            self.assertEqual(
                ("prepared",),
                connection.execute(
                    "SELECT outcome FROM authority_effect_intent "
                    "WHERE project_id=? AND intent_id=?",
                    (PROJECT, intent.intent_id),
                ).fetchone(),
            )
        with self.assertRaisesRegex(ControlStoreError, "receipt identity mismatch"):
            self.session.finish_authority_effect(
                intent,
                "committed",
                {"backend": "git"},
            )
        with closing(sqlite3.connect(self.control.control_store_path)) as connection, connection:
            self.assertEqual(
                ("prepared",),
                connection.execute(
                    "SELECT outcome FROM authority_effect_intent "
                    "WHERE project_id=? AND intent_id=?",
                    (PROJECT, intent.intent_id),
                ).fetchone(),
            )
        completed = self.session.finish_authority_effect(
            intent,
            "committed",
            {
                "backend": "sqlite",
                "target": "new",
                "operation_id": "op-1",
                "state_revision": held.revision,
                "artifact_identity": "artifact-1",
                "manifest_identity": "manifest-1",
                "selector_identity": "selector-1",
                "runtime_identity": "runtime-1",
                "fencing_token": held.identity.fencing_token,
                "mutates_authority": True,
            },
        )
        self.assertEqual(held, completed)
        with self.assertRaisesRegex(ControlStoreError, "already recorded"):
            self.session.prepare_authority_effect(held.revision, "op-1", "sqlite")

        ambiguous_intent = self.session.prepare_authority_effect(held.revision, "op-2", "sqlite")
        ambiguous = self.session.finish_authority_effect(ambiguous_intent, "ambiguous")
        self.assertEqual("ambiguous", ambiguous.status)

    def test_generated_authority_effect_must_match_registered_child(self) -> None:
        held = self._create_held()
        bound = self.session.bind_child(
            held.revision,
            BarrierChildIdentity("upgrade-1.commit", "new", held.identity.identity_digest),
        )
        with self.assertRaisesRegex(ControlStoreError, "registered barrier child"):
            self.session.prepare_authority_effect(
                bound.revision, "upgrade-foreign.commit", "sqlite"
            )

    def test_integrated_pre_effect_rejection_is_journaled_without_fencing(self) -> None:
        held = self._create_held()
        admission = CommitAdmissionBundle(
            backend="sqlite",
            target="new",
            operation_id="op-integrated-rejected",
            fencing_token=held.identity.fencing_token,
            state_revision=held.revision,
            barrier_id=held.identity.durable_barrier_id,
            artifact_identity="artifact-1",
            manifest_identity="manifest-1",
            selector_identity="selector-1",
            runtime_identity="runtime-1",
        )

        def identity(path: Path) -> tuple[int, int] | None:
            try:
                status = path.lstat()
            except FileNotFoundError:
                return None
            return status.st_dev, status.st_ino

        stale = dict(admission.__dict__)
        stale["fencing_token"] = "foreign-fence"  # noqa: S105
        capability = SQLiteCommitCapability(
            self.authority,
            admission=admission,
            admission_reread=lambda: stale,
            expected_db_identity=identity(self.authority),  # type: ignore[arg-type]
            expected_wal_identity=identity(self.authority.with_name("authority.sqlite-wal")),
            expected_shm_identity=identity(self.authority.with_name("authority.sqlite-shm")),
        )
        called = False

        def effect(connection: sqlite3.Connection) -> None:
            nonlocal called
            called = True
            connection.execute("UPDATE tasks SET body='must not publish' WHERE id='AR-0001'")

        with self.assertRaisesRegex(SQLiteMutationRejectedError, "admission identity changed"):
            DurableBoundAuthorityMutation(
                admission, self.session, session_revision=held.revision
            ).execute(lambda: capability.commit(effect))
        self.assertFalse(called)
        current = self.session.snapshot()
        assert current is not None
        self.assertEqual(("held", held.revision), (current.status, current.revision))
        with closing(sqlite3.connect(self.authority)) as connection, connection:
            self.assertEqual(
                "# Authority fixture\n",
                connection.execute("SELECT body FROM tasks WHERE id='AR-0001'").fetchone()[0],
            )
        with closing(sqlite3.connect(self.control.control_store_path)) as connection, connection:
            self.assertEqual(
                [("rejected",)],
                connection.execute(
                    "SELECT outcome FROM authority_effect_intent "
                    "WHERE project_id=? AND operation_id=?",
                    (PROJECT, admission.operation_id),
                ).fetchall(),
            )

    def test_sigkill_during_unknown_recovery_preserves_ambiguity_until_new_fence(self) -> None:
        context = multiprocessing.get_context("fork")
        commit_ready = context.Event()
        committed_without_outcome = context.Process(
            target=_session_commit_waiting_for_sigkill,
            args=(self.directory.name, commit_ready),
        )
        committed_without_outcome.start()
        self.assertTrue(commit_ready.wait(5))
        self._kill(committed_without_outcome)

        committed = self.session.snapshot()
        assert committed is not None
        self.assertEqual(("held", 1), (committed.status, committed.revision))

        recovery_ready = context.Event()
        crashed_recovery = context.Process(
            target=_session_recovery_waiting_for_sigkill,
            args=(self.directory.name, recovery_ready),
        )
        crashed_recovery.start()
        self.assertTrue(recovery_ready.wait(5))
        self._kill(crashed_recovery)

        reopened = SQLiteBarrierSessionStore(_control(self.root), lambda: "authority-1")
        ambiguous = reopened.snapshot()
        assert ambiguous is not None
        self.assertEqual(("ambiguous", 2), (ambiguous.status, ambiguous.revision))
        with closing(sqlite3.connect(self.control.control_store_path)) as connection, connection:
            self.assertEqual(
                [("prepared",)],
                connection.execute(
                    "SELECT outcome FROM barrier_session_intent WHERE project_id=?",
                    (PROJECT,),
                ).fetchall(),
            )

        self.assertEqual(
            (
                "rejected",
                "MutationFenceError",
                "authority mutation rejected while barrier is ambiguous",
            ),
            self._run_writer(),
        )
        self.assertEqual(1, self._authority_revision()[0])

        self.assertEqual(ambiguous, reopened.recover_unknown())
        with closing(sqlite3.connect(self.control.control_store_path)) as connection, connection:
            self.assertEqual(
                [("ambiguous",)],
                connection.execute(
                    "SELECT outcome FROM barrier_session_intent WHERE project_id=?",
                    (PROJECT,),
                ).fetchall(),
            )

        replacement = BarrierSessionState(
            _identity(
                attempt="attempt-recovered",
                state_revision=2,
                barrier="barrier-recovered",
                fence="fence-recovered",
                owner="owner-recovered",
            ),
            "held",
            1,
        )
        reconciled = reopened.reconcile_ambiguous(ambiguous.revision, replacement)
        self.assertEqual(replacement, reconciled)
        self.assertEqual(
            ("rejected", "MutationFenceError", "authority mutation rejected while barrier is held"),
            self._run_writer(),
        )
        self.session = reopened
        released = self._release(reconciled)
        self.assertEqual("released", released.status)
        self.assertEqual(("committed",), self._run_writer())
        self.assertEqual(2, self._authority_revision()[0])

    def test_sigkill_after_reconciliation_commit_recovers_new_fence_from_history(self) -> None:
        held = self._create_held()
        ambiguous = self.session.mark_ambiguous(held.revision, "process-death")
        self.assertEqual(("ambiguous", 2), (ambiguous.status, ambiguous.revision))

        context = multiprocessing.get_context("fork")
        ready = context.Event()
        crashed = context.Process(
            target=_reconcile_waiting_for_sigkill,
            args=(self.directory.name, ready),
        )
        crashed.start()
        self.assertTrue(ready.wait(5))
        self._kill(crashed)

        reopened = SQLiteBarrierSessionStore(_control(self.root), lambda: "authority-1")
        recovered = reopened.snapshot()
        assert recovered is not None
        self.assertEqual(("held", 1), (recovered.status, recovered.revision))
        self.assertEqual("attempt-reconciled", recovered.identity.attempt_id)
        self.assertEqual(2, recovered.identity.state_revision)
        self.assertNotEqual(ambiguous.identity.fencing_token, recovered.identity.fencing_token)
        with closing(sqlite3.connect(self.control.control_store_path)) as connection, connection:
            history = connection.execute(
                "SELECT attempt_id,revision,record_json FROM barrier_session_history "
                "WHERE project_id=?",
                (PROJECT,),
            ).fetchall()
        self.assertEqual(1, len(history))
        self.assertEqual((ambiguous.identity.attempt_id, ambiguous.revision), history[0][:2])
        self.assertIn('"status":"ambiguous"', str(history[0][2]))

        with closing(sqlite3.connect(self.control.control_store_path)) as connection, connection:
            intent_before = connection.execute(
                "SELECT expected_revision,proposed_revision,outcome "
                "FROM barrier_session_intent WHERE project_id=?",
                (PROJECT,),
            ).fetchall()
            connection.execute(
                "UPDATE barrier_session_intent SET expected_revision=999 "
                "WHERE project_id=? AND outcome='prepared'",
                (PROJECT,),
            )
            connection.commit()
        with self.assertRaisesRegex(Exception, "prepared session intent identity is invalid"):
            reopened.recover_unknown()
        self.assertEqual(recovered, reopened.snapshot())
        with closing(sqlite3.connect(self.control.control_store_path)) as connection, connection:
            intent_after_rejected_recovery = connection.execute(
                "SELECT expected_revision,proposed_revision,outcome "
                "FROM barrier_session_intent WHERE project_id=?",
                (PROJECT,),
            ).fetchall()
        self.assertEqual(
            [(999 if row[2] == "prepared" else row[0], row[1], row[2]) for row in intent_before],
            intent_after_rejected_recovery,
        )

        # Restore the exact predecessor revision only to continue the valid
        # recovery path; the forged attempt above must not mutate any row.
        with closing(sqlite3.connect(self.control.control_store_path)) as connection, connection:
            connection.execute(
                "UPDATE barrier_session_intent SET expected_revision=? "
                "WHERE project_id=? AND outcome='prepared'",
                (ambiguous.revision, PROJECT),
            )
            connection.commit()
        self.assertEqual(recovered, reopened.recover_unknown())

        self.assertEqual(
            ("rejected", "MutationFenceError", "authority mutation rejected while barrier is held"),
            self._run_writer(),
        )
        self.assertEqual(1, self._authority_revision()[0])
        with self.assertRaisesRegex(Exception, "only ambiguous sessions require reconciliation"):
            reopened.reconcile_ambiguous(ambiguous.revision, recovered)
        self.assertEqual(recovered, reopened.snapshot())

        self.session = reopened
        released = self._release(recovered)
        self.assertEqual("released", released.status)
        self.assertEqual(("committed",), self._run_writer())
        self.assertEqual(2, self._authority_revision()[0])

    def test_concurrent_released_writers_serialize_one_exact_revision(self) -> None:
        released = self._release(self._create_held())
        context = multiprocessing.get_context("fork")
        start = context.Event()
        result = context.Queue()
        workers = [
            context.Process(
                target=_normal_writer,
                args=(self.directory.name, result, start),
            )
            for _ in range(2)
        ]
        for worker in workers:
            worker.start()
        start.set()
        for worker in workers:
            worker.join(5)
            self.assertEqual(0, worker.exitcode)

        outcomes = sorted([result.get(timeout=1), result.get(timeout=1)])
        self.assertEqual(("committed",), outcomes[0])
        self.assertEqual("rejected", outcomes[1][0])
        self.assertEqual("RuntimeError", outcomes[1][1])
        self.assertIn("stale revision: expected 1, current 2", outcomes[1][2])
        self.assertEqual(released, self.session.snapshot())
        revision, meta_json = self._authority_revision()
        self.assertEqual(2, revision)
        self.assertIn("mutated after verified release", meta_json)
        with closing(sqlite3.connect(self.authority)) as connection, connection:
            events = connection.execute(
                "SELECT revision, kind FROM events WHERE task_id='AR-0001' ORDER BY revision"
            ).fetchall()
            results = connection.execute("SELECT COUNT(*) FROM command_results").fetchone()
        self.assertEqual([(1, "import"), (2, "update")], events)
        self.assertEqual((0,), results)


if __name__ == "__main__":
    unittest.main()
