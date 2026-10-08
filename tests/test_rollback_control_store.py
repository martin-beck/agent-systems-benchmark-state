# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Hostile and durability tests for the SQLite rollback control store."""

from __future__ import annotations

import inspect
import json
import multiprocessing
import os
import signal
import sqlite3
import subprocess
import sys
import tempfile
import threading
import time
import unittest
from collections.abc import Callable, Iterator, Mapping
from contextlib import closing, contextmanager
from pathlib import Path
from typing import Any, cast
from unittest.mock import MagicMock, patch

from _rollback_control_store_subprocess import (
    STALE_FENCE_SCRIPT,
    SUBPROCESS_SESSION_SCRIPT,
)

from tools import upgrade_authority
from tools.handoffctl import CoordinatorLockGuard, LockOwnershipError, locked
from tools.rollback_control_store import (
    IDENTITY_FIELDS,
    AuthorityRuntimeRereader,
    BarrierSessionContract,
    BarrierSessionState,
    ControlStoreAmbiguousError,
    ControlStoreError,
    RecoveryRejectedError,
    SQLiteAuthorityRuntimeRereader,
    SQLiteAuthorityRuntimeState,
    SQLiteBarrierSessionStore,
    SQLiteControlStoreAdapter,
    SQLiteRollbackControlStore,
    bind_control_store,
)
from tools.sqlite_storage import SQLiteBackend, create_database
from tools.upgrade_authority import (
    AuthorityError,
    commit_runtime_selector,
    inspect_sqlite_release_authority,
    read_runtime_selector,
)
from tools.upgrade_identity import (
    BarrierChildIdentity,
    BarrierSessionIdentity,
    canonical_barrier_digest,
    canonical_barrier_session_digest,
    canonical_envelope_digest,
)


def _reopen_evidence(state: BarrierSessionState | None, target: str) -> dict[str, object]:
    assert state is not None
    child = state.rollback_child if target == "rollback" else state.forward_child
    assert child is not None
    return {
        "operation_id": child.operation_id,
        "target": child.target,
        "barrier_identity_digest": state.identity.identity_digest,
        "validated": True,
    }


def _runtime_evidence(state: BarrierSessionState | None, target: str) -> dict[str, object]:
    assert state is not None
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


PROJECT = "-".join(("11111111", "1111", "4111", "8111", "111111111111"))
OTHER_PROJECT = "-".join(("22222222", "2222", "4222", "8222", "222222222222"))
INVALID_VARIANT_PROJECT = "-".join(("11111111", "1111", "1111", "8111", "111111111111"))
RECORD = {
    "schema_version": 2,
    "backend": "sqlite",
    "project_id": PROJECT,
    "operation_id": "op-1",
    "state_revision": 1,
    "authority_revision": "authority-1",
    "fencing_token": "fence-1",
    "fencing_owner": "owner-1",
    "durable_barrier_id": "barrier-1",
    "artifact_root": "/artifacts",
    "source": "/authority.sqlite",
    "destination": "/artifacts/backup.sqlite",
    "manifest": "/artifacts/manifest.json",
    "selector_ref": ".runtime/runtime-selector.json",
    "barrier_identity_digest": "0" * 64,
    "target": "rollback",
    "envelope_digest": "0" * 64,
    "status": "held",
    "revision": 1,
}
RECORD["barrier_identity_digest"] = canonical_barrier_digest(RECORD)
RECORD["envelope_digest"] = canonical_envelope_digest(RECORD)
RELEASE_EVIDENCE = {
    "restored_verified": True,
    "runtime_validated": True,
    "backend_roundtrip_valid": True,
    "backend": "sqlite",
    "fencing_token": "fence-1",
}

AUTHORITY_BINDING = {
    "schema_version": 1,
    "project_id": PROJECT,
    "state_repository": "owner/state",
    "product_repository": "owner/product",
}


def _reopen_ambiguous_child(control_text: str, authority_text: str, result_text: str) -> None:
    store = SQLiteBarrierSessionStore(
        SQLiteRollbackControlStore(Path(control_text), PROJECT, Path(authority_text)),
        lambda: "authority-3",
    )
    state = store.snapshot()
    if state is None:
        raise SystemExit("missing state")
    Path(result_text).write_text(f"{state.status}:{state.revision}\n", encoding="utf-8")


def _recover_ambiguous_child(control_text: str, authority_text: str, result_text: str) -> None:
    store = SQLiteBarrierSessionStore(
        SQLiteRollbackControlStore(Path(control_text), PROJECT, Path(authority_text)),
        lambda: "authority-3",
    )
    state = store.recover_unknown()
    if state is None:
        raise SystemExit("missing recovery state")
    if store.operation_owned_by_current_thread:
        raise SystemExit("recovery retained the operation lock")
    with store.operation_lock():
        pass
    Path(result_text).write_text(
        f"{state.status}:{state.revision}:lock-released\n", encoding="utf-8"
    )


def _recover_effect_child(
    control_text: str,
    authority_text: str,
    result_text: str,
    operation_id: str = "subprocess-effect",
) -> None:
    store = SQLiteBarrierSessionStore(
        SQLiteRollbackControlStore(Path(control_text), PROJECT, Path(authority_text)),
        lambda: "authority-3",
    )
    state = store.recover_unknown()
    if state is None:
        raise SystemExit("missing effect recovery state")
    with store.operation_lock():
        pass
    with closing(sqlite3.connect(control_text)) as connection, connection:
        outcome = connection.execute(
            "SELECT outcome FROM authority_effect_intent WHERE project_id=? AND operation_id=?",
            (PROJECT, operation_id),
        ).fetchone()
    if outcome is None:
        raise SystemExit("missing effect outcome")
    Path(result_text).write_text(
        f"{state.status}:{state.revision}:{outcome[0]}:lock-released\n",
        encoding="utf-8",
    )


def authority_task() -> tuple[Path, dict[str, object], str]:
    meta: dict[str, object] = {
        "schema_version": 1,
        "id": "AR-0001",
        "title": "Release authority test",
        "status": "open",
        "priority": "P1",
        "summary": "Ready.",
        "next_action": "Test.",
        "task_revision": 1,
        "updated_at": "2026-09-14T00:00:00+00:00",
        "owner": "",
        "claim_expires": "",
        "worktree_key": "",
        "branch": "",
        "checkpoint_commit": "",
        "plan": "",
        "depends_on": [],
    }
    return Path("AR-0001-release.md"), meta, "# Release authority test\n"


def create_release_authority(root: Path) -> tuple[Path, Path, Path, Path]:
    authority = root / ".runtime" / "coordinator.sqlite3"
    create_database(
        authority,
        AUTHORITY_BINDING,
        [authority_task()],
        imported_at="2026-09-14T00:00:00+00:00",
        source_backend="git",
        source_checkpoint="a" * 40,
    )
    project_binding = root / "coordinator.binding.json"
    project_binding.write_text(json.dumps(AUTHORITY_BINDING) + "\n")
    backend_selector = root / "coordinator.backend.json"
    backend_selector.write_text(
        json.dumps({"schema_version": 1, "project_id": PROJECT, "backend": "sqlite"}) + "\n"
    )
    runtime_selector = root / ".runtime" / "runtime-selector.json"
    commit_runtime_selector(runtime_selector, "release-old", "release-older")
    return authority, project_binding, backend_selector, runtime_selector


class StaticAuthorityRuntimeRereader:
    def __init__(self, **changes: object) -> None:
        self.changes = changes

    def reread_rollback(
        self, context: Mapping[str, object], _result: Mapping[str, object]
    ) -> SQLiteAuthorityRuntimeState:
        values: dict[str, object] = {
            "backend": context["backend"],
            "project_id": context["project_id"],
            "authority_revision": context["authority_revision"],
            "fencing_token": context["fencing_token"],
            "target": context["target"],
            "integrity_check": "ok",
            "foreign_key_violations": 0,
            "backend_roundtrip": "sqlite",
            **self.changes,
        }
        return SQLiteAuthorityRuntimeState(
            backend=cast(str, values["backend"]),
            project_id=cast(str, values["project_id"]),
            authority_revision=cast(str, values["authority_revision"]),
            fencing_token=cast(str, values["fencing_token"]),
            target=cast(str, values["target"]),
            integrity_check=cast(str, values["integrity_check"]),
            foreign_key_violations=cast(int, values["foreign_key_violations"]),
            backend_roundtrip=cast(str, values["backend_roundtrip"]),
        )


class RollbackControlStoreTests(unittest.TestCase):
    def test_session_recheck_and_provision_released_negative_paths(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            control = SQLiteRollbackControlStore(Path(directory) / "control.sqlite", PROJECT)
            store = SQLiteBarrierSessionStore(control, lambda: "authority-3")
            identity = self._session_identity()
            with self.assertRaisesRegex(ControlStoreError, "project binding"):
                store.provision_released(
                    BarrierSessionIdentity(
                        identity.schema_version,
                        OTHER_PROJECT,
                        identity.attempt_id,
                        identity.state_revision,
                        identity.authority_revision_at_acquire,
                        identity.durable_barrier_id,
                        identity.fencing_token,
                        identity.fencing_owner,
                        identity.identity_digest,
                    )
                )
            released = store.provision_released(identity)
            self.assertEqual("released", released.status)
            self.assertEqual(store.provision_released(identity), released)
            other_record = identity.as_record()
            other_record["attempt_id"] = "different-attempt"
            from tools.upgrade_identity import canonical_barrier_session_digest

            other_record["identity_digest"] = canonical_barrier_session_digest(other_record)
            with self.assertRaisesRegex(ControlStoreError, "already exists"):
                store.provision_released(BarrierSessionIdentity.from_record(other_record))
            with self.assertRaisesRegex(LockOwnershipError, "required"):
                store.recheck_held_locked(object(), identity, 1)  # type: ignore[arg-type]

    def test_recheck_held_rejects_absent_revision_identity_and_status(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            control = SQLiteRollbackControlStore(Path(directory) / "control.sqlite", PROJECT)
            store = SQLiteBarrierSessionStore(control, lambda: "authority-3")
            identity = self._session_identity()
            store.create(identity)
            with self.assertRaisesRegex(ControlStoreError, "trusted rereader"):
                no_reader = SQLiteBarrierSessionStore(control, None)
                no_reader.recheck_held(99, cast(Any, identity))
            with self.assertRaisesRegex(ControlStoreError, "CAS conflict"):
                store.recheck_held(99)

    def test_session_state_rejects_invalid_status_revision_reopen_and_duplicate_children(
        self,
    ) -> None:
        identity = self._session_identity()
        for kwargs, message in cast(
            tuple[tuple[dict[str, Any], str], ...],
            (
                ({"status": "unknown", "revision": 1}, "status"),
                ({"status": "held", "revision": 0}, "revision"),
                ({"status": "released", "revision": 1, "reopen_target": "bogus"}, "reopen"),
                ({"status": "held", "revision": 1, "reopen_target": "new"}, "held"),
            ),
        ):
            with self.subTest(message=message), self.assertRaisesRegex(ControlStoreError, message):
                BarrierSessionState(identity, **cast(Any, kwargs))
        child = BarrierChildIdentity.bind(identity, "same-child", "new")
        with self.assertRaisesRegex(ControlStoreError, "distinct"):
            BarrierSessionState(identity, "releasing", 1, child, child)

    def test_runtime_rereader_rejects_non_release_specific_inputs(self) -> None:
        rereader = SQLiteAuthorityRuntimeRereader(
            Path("/missing-authority"),
            Path("/missing-binding"),
            Path("/missing-backend"),
            Path("/missing-runtime"),
            active_release="new",
            previous_release="old",
        )
        context = {
            "backend": "sqlite",
            "target": "rollback",
            "project_id": PROJECT,
            "fencing_token": "fence",
        }
        valid = {
            "restored_verified": True,
            "runtime_validated": True,
            "backend_roundtrip_valid": True,
            "backend": "sqlite",
            "fencing_token": "fence",
        }
        cases = [
            ({**context, "backend": "git"}, valid),
            ({**context, "target": "new"}, valid),
            ({**context, "project_id": 3}, valid),
            (context, {**valid, "extra": True}),
            (context, {**valid, "runtime_validated": False}),
            (context, {**valid, "backend": "git"}),
            (context, {**valid, "fencing_token": "other"}),
        ]
        for bad_context, bad_result in cases:
            with (
                self.subTest(context=bad_context, result=bad_result),
                self.assertRaisesRegex(ControlStoreError, "release-specific"),
            ):
                rereader.reread_rollback(
                    cast(Mapping[str, object], bad_context),
                    cast(Mapping[str, object], bad_result),
                )

    def test_adapter_binding_and_bound_verifier_fail_closed(self) -> None:
        delegate: Any = object()
        with tempfile.TemporaryDirectory() as directory:
            store = SQLiteRollbackControlStore(Path(directory) / "control.sqlite", PROJECT)
            rereader = StaticAuthorityRuntimeRereader()
            with self.assertRaisesRegex(ControlStoreError, "rereader"):
                SQLiteControlStoreAdapter(delegate, store)
            with self.assertRaisesRegex(ControlStoreError, "unavailable"):
                SQLiteControlStoreAdapter(delegate, store, rereader).verify_rollback_context_bound(
                    {}, object(), lease=object(), admission_recheck=object()
                )
            with self.assertRaisesRegex(ControlStoreError, "unavailable"):
                bind_control_store("git", delegate, store, rereader)
            with self.assertRaisesRegex(ControlStoreError, "unavailable"):
                bind_control_store("sqlite", delegate, None, rereader)
            with self.assertRaisesRegex(ControlStoreError, "unavailable"):
                bind_control_store("sqlite", delegate, store)

    def test_authority_effect_prepare_reopen_uncertainty_is_ambiguous(self) -> None:
        class ReopenFailureStore(SQLiteRollbackControlStore):
            def __init__(self, path: Path) -> None:
                super().__init__(path, PROJECT)
                self.open_calls = 0
                self.fail_reopen = False

            def _open_bound_file(
                self,
                path: Path,
                expected_parent: tuple[int, int],
                expected_identity: tuple[int, int],
            ) -> tuple[int, int]:
                self.open_calls += 1
                if self.fail_reopen and self.open_calls == 5:
                    raise ControlStoreError("injected reopen identity failure")
                return super()._open_bound_file(path, expected_parent, expected_identity)

        with tempfile.TemporaryDirectory() as directory:
            control = ReopenFailureStore(Path(directory) / "control.sqlite")
            store = SQLiteBarrierSessionStore(control, lambda: "authority-3")
            store.create(self._session_identity())
            control.open_calls = 0
            control.fail_reopen = True

            with self.assertRaisesRegex(
                ControlStoreAmbiguousError, "reopen identity became uncertain"
            ):
                store.prepare_authority_effect(1, "effect-reopen-uncertain", "sqlite")

            with closing(sqlite3.connect(control.path)) as connection:
                self.assertEqual(
                    [("prepared",)],
                    connection.execute(
                        "SELECT outcome FROM authority_effect_intent "
                        "WHERE project_id=? AND operation_id=?",
                        (PROJECT, "effect-reopen-uncertain"),
                    ).fetchall(),
                )

    def test_rejected_authority_effect_is_write_closed_without_fencing_session(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            control = SQLiteRollbackControlStore(root / "control.sqlite", PROJECT)
            store = SQLiteBarrierSessionStore(control, lambda: "authority-3")
            store.create(self._session_identity())
            intent = store.prepare_authority_effect(1, "effect-rejected", "sqlite")

            state = store.finish_authority_effect(intent, "rejected")

            self.assertEqual(("held", 1), (state.status, state.revision))
            self.assertEqual(state, store.snapshot())
            with closing(sqlite3.connect(control.path)) as connection:
                self.assertEqual(
                    [("rejected",)],
                    connection.execute(
                        "SELECT outcome FROM authority_effect_intent "
                        "WHERE project_id=? AND operation_id=?",
                        (PROJECT, "effect-rejected"),
                    ).fetchall(),
                )

    def test_legacy_barrier_schema_is_rejected_without_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "control.sqlite"
            with closing(sqlite3.connect(path)) as connection:
                connection.execute(
                    "CREATE TABLE barrier (operation_id TEXT PRIMARY KEY, manifest TEXT NOT NULL)"
                )
                connection.commit()
            with self.assertRaisesRegex(ControlStoreError, "legacy"):
                SQLiteRollbackControlStore(path, PROJECT).snapshot("missing")
            with closing(sqlite3.connect(path)) as connection:
                columns = {row[1] for row in connection.execute("PRAGMA table_info(barrier)")}
            self.assertNotIn("selector_ref", columns)

    def test_snapshot_owned_by_caller_requires_and_reuses_operation_lock(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            control = SQLiteRollbackControlStore(root / "control.sqlite", PROJECT)
            store = SQLiteBarrierSessionStore(control, lambda: "authority-3")
            store.create(self._session_identity())

            with self.assertRaisesRegex(ControlStoreError, "caller-owned control lock"):
                store.snapshot_owned_by_caller()
            with store.operation_lock():
                snapshot = store.snapshot_owned_by_caller()
                self.assertEqual("held", snapshot.status)
                self.assertEqual(1, snapshot.revision)
                with self.assertRaisesRegex(ControlStoreError, "non-reentrant"):
                    store.snapshot()

    def test_authoritative_control_store_routes_have_operation_scope_contract(self) -> None:
        """Keep the documented rollback/session write surface behind admission."""
        routes = {
            SQLiteRollbackControlStore: (
                ("cas", "scoped"),
                ("begin_release", "scoped"),
                ("reconcile_release", "rejected"),
                ("reconcile_ambiguous", "scoped"),
                ("with_barrier", "scoped"),
            ),
            SQLiteBarrierSessionStore: (
                ("create", "scoped"),
                ("cas", "scoped"),
                ("bind_child", "scoped"),
                ("begin_reopen", "scoped"),
                ("complete_reopen", "scoped"),
                ("mark_ambiguous", "scoped"),
                ("recover_unknown", "scoped"),
                ("reconcile_ambiguous", "scoped"),
            ),
        }
        for store_type, route_contracts in routes.items():
            for name, contract in route_contracts:
                with self.subTest(store=store_type.__name__, route=name):
                    source = inspect.getsource(getattr(store_type, name))
                    if contract == "rejected":
                        self.assertIn("requires verified engine recovery", source)
                    else:
                        self.assertTrue(
                            "operation_lock" in source or "self.cas(" in source,
                            f"{store_type.__name__}.{name} lacks operation-scope admission",
                        )

    def _session_identity(self) -> BarrierSessionIdentity:
        from tools.upgrade_identity import BarrierSessionIdentity, canonical_barrier_session_digest

        record = {
            "schema_version": 1,
            "project_id": PROJECT,
            "attempt_id": "attempt-1",
            "state_revision": 3,
            "authority_revision_at_acquire": "authority-3",
            "durable_barrier_id": "barrier-1",
            "fencing_token": "fence-1",
            "fencing_owner": "owner-1",
            "identity_digest": "0" * 64,
        }
        record["identity_digest"] = canonical_barrier_session_digest(record)
        return BarrierSessionIdentity.from_record(record)

    def _run_session_process(
        self, control_path: Path, authority_path: Path, mode: str, ready_path: Path
    ) -> subprocess.Popen[str]:
        return subprocess.Popen(  # noqa: S603 - fixed interpreter and in-test script
            [
                sys.executable,
                "-c",
                SUBPROCESS_SESSION_SCRIPT,
                str(control_path),
                str(authority_path),
                PROJECT,
                mode,
                str(ready_path),
            ],
            cwd=Path(__file__).parents[1],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

    def _run_stale_fence_process(
        self, control_path: Path, authority_path: Path, ready_path: Path, role: str
    ) -> subprocess.Popen[str]:
        return subprocess.Popen(  # noqa: S603 - fixed interpreter and in-test script
            [
                sys.executable,
                "-c",
                STALE_FENCE_SCRIPT,
                str(control_path),
                str(authority_path),
                str(ready_path),
                role,
                PROJECT,
            ],
            cwd=Path(__file__).parents[1],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

    @staticmethod
    def _wait_for_file(path: Path, process: subprocess.Popen[str]) -> None:
        deadline = time.monotonic() + 10
        while time.monotonic() < deadline and not path.exists():
            if process.poll() is not None:
                stdout, stderr = process.communicate()
                raise AssertionError(
                    f"session subprocess exited early: {process.returncode}; "
                    f"stdout={stdout!r}; stderr={stderr!r}"
                )
            time.sleep(0.01)
        if not path.exists():
            process.kill()
            stdout, stderr = process.communicate(timeout=5)
            raise AssertionError(
                "session subprocess did not reach its checkpoint: "
                f"stdout={stdout!r}; stderr={stderr!r}"
            )

    def test_v10_subprocess_reopens_wal_session_without_authority_change(self) -> None:
        """Cover clean subprocess reopen only; no admission or fencing claim."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            control_path = root / "control.sqlite"
            authority_path = root / "authority.sqlite"
            authority_bytes = b"authority remains untouched\n"
            authority_path.write_bytes(authority_bytes)
            ready_path = root / "ready"
            process = self._run_session_process(control_path, authority_path, "clean", ready_path)
            stdout, stderr = process.communicate(timeout=10)
            self.assertEqual(0, process.returncode, msg=f"stdout={stdout}; stderr={stderr}")
            self.assertEqual("wal", ready_path.read_text(encoding="utf-8").strip())

            store = SQLiteBarrierSessionStore(
                SQLiteRollbackControlStore(control_path, PROJECT, authority_path),
                lambda: "authority-3",
            )
            state = store.snapshot()
            self.assertIsNotNone(state)
            assert state is not None
            self.assertEqual(("held", 2), (state.status, state.revision))
            self.assertIsNotNone(state.forward_child)
            child_result = root / "child-result"
            verifier = multiprocessing.get_context("fork").Process(
                target=_reopen_ambiguous_child,
                args=(str(control_path), str(authority_path), str(child_result)),
            )
            verifier.start()
            verifier.join(timeout=10)
            self.assertEqual(0, verifier.exitcode)
            self.assertEqual("held:2\n", child_result.read_text(encoding="utf-8"))
            self.assertEqual(authority_bytes, authority_path.read_bytes())

    def test_v10_multiprocess_stale_fence_writer_is_rejected(self) -> None:
        """A stale process cannot write after a newer fence replaces its session."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            control_path = root / "control.sqlite"
            authority_path = root / "authority.sqlite"
            authority_path.write_bytes(b"authority remains untouched\n")
            ready_path = root / "replaced"

            seed = SQLiteBarrierSessionStore(
                SQLiteRollbackControlStore(control_path, PROJECT, authority_path),
                lambda: "authority-3",
            )
            seed.create(self._session_identity())

            replace = self._run_stale_fence_process(
                control_path, authority_path, ready_path, "replace"
            )
            stale = self._run_stale_fence_process(control_path, authority_path, ready_path, "stale")
            try:
                replace_stdout, replace_stderr = replace.communicate(timeout=10)
                stale_stdout, stale_stderr = stale.communicate(timeout=10)
            finally:
                for process in (replace, stale):
                    if process.poll() is None:
                        process.kill()
                    process.communicate(timeout=5)
            self.assertEqual(
                0,
                replace.returncode,
                msg=f"replace stdout={replace_stdout}; stderr={replace_stderr}",
            )
            self.assertEqual(
                0,
                stale.returncode,
                msg=f"stale stdout={stale_stdout}; stderr={stale_stderr}",
            )
            restarted_stale = self._run_stale_fence_process(
                control_path, authority_path, ready_path, "stale"
            )
            restarted_stdout, restarted_stderr = restarted_stale.communicate(timeout=10)
            self.assertEqual(
                0,
                restarted_stale.returncode,
                msg=f"restarted stale stdout={restarted_stdout}; stderr={restarted_stderr}",
            )
            self.assertEqual(b"authority remains untouched\n", authority_path.read_bytes())
            child_result = root / "child-result"
            verifier = multiprocessing.get_context("fork").Process(
                target=_reopen_ambiguous_child,
                args=(str(control_path), str(authority_path), str(child_result)),
            )
            verifier.start()
            verifier.join(timeout=10)
            self.assertEqual(0, verifier.exitcode)
            self.assertEqual("held:1\n", child_result.read_text(encoding="utf-8"))
            with locked() as guard:
                self.assertIsNotNone(guard)
            final = seed.snapshot()
            self.assertIsNotNone(final)
            assert final is not None
            self.assertEqual(
                ("attempt-2", "fence-2", "held", 1),
                (
                    final.identity.attempt_id,
                    final.identity.fencing_token,
                    final.status,
                    final.revision,
                ),
            )
            reopened_final = SQLiteBarrierSessionStore(
                SQLiteRollbackControlStore(control_path, PROJECT, authority_path),
                lambda: "authority-3",
            ).snapshot()
            self.assertIsNotNone(reopened_final)
            assert reopened_final is not None
            self.assertEqual(final, reopened_final)
            self.assertGreater(len(set(reopened_final.identity.identity_digest)), 1)
            self.assertEqual(
                final.identity.identity_digest, reopened_final.identity.identity_digest
            )
            self.assertEqual(4, reopened_final.identity.state_revision)
            self.assertGreater(reopened_final.identity.state_revision, 1)
            self.assertEqual("fence-2", reopened_final.identity.fencing_token)
            self.assertEqual("owner-1", reopened_final.identity.fencing_owner)
            self.assertEqual("barrier-2", reopened_final.identity.durable_barrier_id)
            self.assertEqual(PROJECT, reopened_final.identity.project_id)
            self.assertEqual("attempt-2", reopened_final.identity.attempt_id)
            self.assertIsNone(reopened_final.forward_child)
            self.assertIsNone(reopened_final.rollback_child)
            self.assertEqual("held", reopened_final.status)
            self.assertEqual(1, reopened_final.revision)
            self.assertEqual("authority-3", reopened_final.identity.authority_revision_at_acquire)
            self.assertEqual(64, len(reopened_final.identity.identity_digest))
            self.assertNotEqual("0" * 64, reopened_final.identity.identity_digest)
            self.assertTrue(reopened_final.identity.identity_digest.isalnum())
            self.assertEqual(
                reopened_final.identity.identity_digest,
                reopened_final.identity.identity_digest.lower(),
            )
            self.assertTrue(
                all(
                    character in "0123456789abcdef"
                    for character in reopened_final.identity.identity_digest
                )
            )
            self.assertEqual(
                canonical_barrier_session_digest(reopened_final.identity.as_record()),
                reopened_final.identity.identity_digest,
            )
            self.assertEqual(final.identity.authority_revision_at_acquire, "authority-3")
            self.assertEqual(b"authority remains untouched\n", authority_path.read_bytes())
            for _ in range(2):
                reader = SQLiteBarrierSessionStore(
                    SQLiteRollbackControlStore(control_path, PROJECT, authority_path),
                    lambda: "authority-3",
                )
                snapshot = reader.snapshot()
                self.assertEqual(final, snapshot)
                assert snapshot is not None
                self.assertIsNone(snapshot.forward_child)
                self.assertEqual(b"authority remains untouched\n", authority_path.read_bytes())
            self.assertEqual(final, reader.snapshot())

    def test_v10_subprocess_death_rolls_back_uncommitted_wal_change(self) -> None:
        """Cover uncommitted WAL rollback only; no ambiguous-recovery claim."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            control_path = root / "control.sqlite"
            authority_path = root / "authority.sqlite"
            authority_bytes = b"authority remains untouched after crash\n"
            authority_path.write_bytes(authority_bytes)
            ready_path = root / "ready"
            process = self._run_session_process(
                control_path, authority_path, "kill-during-transaction", ready_path
            )
            self._wait_for_file(ready_path, process)
            self.assertEqual("wal", ready_path.read_text(encoding="utf-8").strip())
            self.assertTrue((root / "control.sqlite-wal").exists())
            self.assertTrue((root / "control.sqlite-shm").exists())
            returncode = process.wait(timeout=10)
            stdout, stderr = process.communicate()
            self.assertEqual(
                -signal.SIGKILL,
                returncode,
                msg=f"stdout={stdout}; stderr={stderr}",
            )

            store = SQLiteBarrierSessionStore(
                SQLiteRollbackControlStore(control_path, PROJECT, authority_path),
                lambda: "authority-3",
            )
            state = store.snapshot()
            self.assertIsNotNone(state)
            assert state is not None
            self.assertEqual(("held", 2), (state.status, state.revision))
            self.assertEqual(authority_bytes, authority_path.read_bytes())

    def test_v10_subprocess_caller_owned_wal_rollback_preserves_recheck(self) -> None:
        """Cover caller-owned WAL rollback and recheck only; no ambiguity claim."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            control_path = root / "control.sqlite"
            authority_path = root / "authority.sqlite"
            authority_bytes = b"authority remains untouched after caller-owned crash\n"
            authority_path.write_bytes(authority_bytes)
            ready_path = root / "ready"
            process = self._run_session_process(
                control_path,
                authority_path,
                "kill-during-caller-owned-recheck",
                ready_path,
            )
            self._wait_for_file(ready_path, process)
            self.assertEqual("wal", ready_path.read_text(encoding="utf-8").strip())
            self.assertTrue((root / "control.sqlite-wal").exists())
            self.assertTrue((root / "control.sqlite-shm").exists())
            returncode = process.wait(timeout=10)
            stdout, stderr = process.communicate()
            self.assertEqual(
                -signal.SIGKILL,
                returncode,
                msg=f"stdout={stdout}; stderr={stderr}",
            )

            store = SQLiteBarrierSessionStore(
                SQLiteRollbackControlStore(control_path, PROJECT, authority_path),
                lambda: "authority-3",
            )
            state = store.snapshot()
            self.assertIsNotNone(state)
            assert state is not None
            self.assertEqual(("held", 2), (state.status, state.revision))
            with locked() as guard, store.lock_owned_by_caller(guard):
                self.assertEqual(
                    state,
                    store.recheck_held_locked(guard, state.identity, state.revision),
                )
            child_result = root / "child-result"
            verifier = multiprocessing.get_context("fork").Process(
                target=_reopen_ambiguous_child,
                args=(str(control_path), str(authority_path), str(child_result)),
            )
            verifier.start()
            verifier.join(timeout=10)
            self.assertEqual(0, verifier.exitcode)
            self.assertEqual("held:2\n", child_result.read_text(encoding="utf-8"))
            self.assertEqual(authority_bytes, authority_path.read_bytes())

    def test_v10_active_wal_sidecar_replacement_fails_closed_before_recheck(self) -> None:
        """Replacing active WAL/SHM sidecars is rejected before the scope can proceed."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            control_path = root / "control.sqlite"
            authority_path = root / "authority.sqlite"
            authority_bytes = b"authority remains untouched after sidecar replacement\n"
            authority_path.write_bytes(authority_bytes)
            ready_path = root / "ready"
            process = self._run_session_process(
                control_path, authority_path, "replace-active-wal-sidecars", ready_path
            )
            self._wait_for_file(ready_path, process)
            self.assertEqual("wal", ready_path.read_text(encoding="utf-8").strip())
            self.assertTrue((root / "control.sqlite-wal").exists())
            self.assertTrue((root / "control.sqlite-shm").exists())
            ready_path.with_suffix(".replace").touch()
            stdout, stderr = process.communicate(timeout=10)
            self.assertNotEqual(0, process.returncode, msg=f"stdout={stdout}; stderr={stderr}")
            self.assertIn("WAL sidecar identity changed", stderr)
            self.assertEqual(authority_bytes, authority_path.read_bytes())

            # The failed connection must have released both locks before a
            # clean worker can remove the damaged sidecars and reacquire.
            for suffix in ("-wal", "-shm"):
                (root / f"control.sqlite{suffix}").unlink(missing_ok=True)
            fresh_ready = root / "fresh-ready"
            fresh = self._run_session_process(
                control_path, authority_path, "probe-after-sidecar", fresh_ready
            )
            fresh_stdout, fresh_stderr = fresh.communicate(timeout=10)
            self.assertEqual(
                0,
                fresh.returncode,
                msg=f"stdout={fresh_stdout}; stderr={fresh_stderr}",
            )
            self.assertEqual("wal", fresh_ready.read_text(encoding="utf-8").strip())
            child_result = root / "child-result"
            verifier = multiprocessing.get_context("fork").Process(
                target=_reopen_ambiguous_child,
                args=(str(control_path), str(authority_path), str(child_result)),
            )
            verifier.start()
            verifier.join(timeout=10)
            self.assertEqual(0, verifier.exitcode)
            self.assertEqual("held:2\n", child_result.read_text(encoding="utf-8"))

    def test_v10_subprocess_commit_before_outcome_recovers_ambiguously(self) -> None:
        """Cover post-CAS/pre-outcome death; no authority-fencing claim."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            control_path = root / "control.sqlite"
            authority_path = root / "authority.sqlite"
            authority_bytes = b"authority remains untouched after outcome loss\n"
            authority_path.write_bytes(authority_bytes)
            ready_path = root / "ready"
            process = self._run_session_process(
                control_path, authority_path, "kill-after-session-commit", ready_path
            )
            self._wait_for_file(ready_path, process)
            self.assertEqual(
                "committed-before-outcome", ready_path.read_text(encoding="utf-8").strip()
            )
            returncode = process.wait(timeout=10)
            stdout, stderr = process.communicate()
            self.assertEqual(
                -signal.SIGKILL,
                returncode,
                msg=f"stdout={stdout}; stderr={stderr}",
            )
            store = SQLiteBarrierSessionStore(
                SQLiteRollbackControlStore(control_path, PROJECT, authority_path),
                lambda: "authority-3",
            )
            state = store.snapshot()
            self.assertIsNotNone(state)
            assert state is not None
            self.assertEqual(("releasing", 3), (state.status, state.revision))
            child_result = root / "recovered-child-result"
            verifier = multiprocessing.get_context("fork").Process(
                target=_recover_ambiguous_child,
                args=(str(control_path), str(authority_path), str(child_result)),
            )
            verifier.start()
            verifier.join(timeout=10)
            self.assertEqual(0, verifier.exitcode)
            self.assertEqual(
                "ambiguous:4:lock-released\n", child_result.read_text(encoding="utf-8")
            )
            recovered = store.snapshot()
            self.assertIsNotNone(recovered)
            assert recovered is not None
            self.assertEqual(("ambiguous", 4), (recovered.status, recovered.revision))
            child_result = root / "child-result"
            verifier = multiprocessing.get_context("fork").Process(
                target=_reopen_ambiguous_child,
                args=(str(control_path), str(authority_path), str(child_result)),
            )
            verifier.start()
            verifier.join(timeout=10)
            self.assertEqual(0, verifier.exitcode)
            self.assertEqual("ambiguous:4\n", child_result.read_text(encoding="utf-8"))
            self.assertEqual(authority_bytes, authority_path.read_bytes())

    def test_v10_subprocess_after_outcome_publication_reopens_releasing(self) -> None:
        """A death after durable intent publication leaves an inspectable release barrier."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            control_path = root / "control.sqlite"
            authority_path = root / "authority.sqlite"
            authority_path.write_bytes(b"authority remains untouched after outcome publication\n")
            ready_path = root / "ready"
            process = self._run_session_process(
                control_path, authority_path, "kill-after-outcome-publication", ready_path
            )
            self._wait_for_file(ready_path, process)
            self.assertEqual(
                "committed-after-outcome", ready_path.read_text(encoding="utf-8").strip()
            )
            self.assertEqual(-signal.SIGKILL, process.wait(timeout=10))
            stdout, stderr = process.communicate()
            self.assertEqual("", stderr, msg=stdout)
            store = SQLiteBarrierSessionStore(
                SQLiteRollbackControlStore(control_path, PROJECT, authority_path),
                lambda: "authority-3",
            )
            state = store.snapshot()
            self.assertIsNotNone(state)
            assert state is not None
            self.assertEqual(("releasing", 3), (state.status, state.revision))
            child_result = root / "child-result"
            verifier = multiprocessing.get_context("fork").Process(
                target=_reopen_ambiguous_child,
                args=(str(control_path), str(authority_path), str(child_result)),
            )
            verifier.start()
            verifier.join(timeout=10)
            self.assertEqual(0, verifier.exitcode)
            self.assertEqual("releasing:3\n", child_result.read_text(encoding="utf-8"))
            with closing(sqlite3.connect(control_path)) as connection:
                outcomes = connection.execute(
                    "SELECT outcome FROM barrier_session_intent WHERE project_id=?",
                    (PROJECT,),
                ).fetchall()
            self.assertEqual([("committed",), ("committed",), ("committed",)], outcomes)
            self.assertEqual(state, store.recover_unknown())
            self.assertEqual(state, store.snapshot())
            self.assertEqual(
                b"authority remains untouched after outcome publication\n",
                authority_path.read_bytes(),
            )

    def test_v10_subprocess_death_after_committed_effect_publication_is_reopenable(
        self,
    ) -> None:
        """A death after a committed effect outcome leaves a durable lock-safe journal."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            control_path = root / "control.sqlite"
            authority_path = root / "authority.sqlite"
            authority_bytes = b"authority remains untouched after committed effect\n"
            authority_path.write_bytes(authority_bytes)
            ready_path = root / "ready"
            process = self._run_session_process(
                control_path,
                authority_path,
                "kill-after-effect-committed-publication",
                ready_path,
            )
            self._wait_for_file(ready_path, process)
            self.assertEqual(
                "effect-committed-after-outcome",
                ready_path.read_text(encoding="utf-8").strip(),
            )
            self.assertEqual(-signal.SIGKILL, process.wait(timeout=10))
            stdout, stderr = process.communicate()
            self.assertEqual("", stderr, msg=stdout)

            child_result = root / "child-result"
            verifier = multiprocessing.get_context("fork").Process(
                target=_recover_effect_child,
                args=(str(control_path), str(authority_path), str(child_result)),
            )
            verifier.start()
            verifier.join(timeout=10)
            self.assertEqual(0, verifier.exitcode)
            self.assertEqual(
                "held:2:committed:lock-released\n",
                child_result.read_text(encoding="utf-8"),
            )
            self.assertEqual(authority_bytes, authority_path.read_bytes())

    def test_v10_subprocess_death_after_ambiguous_effect_publication_is_reopenable(
        self,
    ) -> None:
        """A death after an ambiguous effect outcome preserves the durable fence."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            control_path = root / "control.sqlite"
            authority_path = root / "authority.sqlite"
            authority_bytes = b"authority remains untouched after ambiguous effect\n"
            authority_path.write_bytes(authority_bytes)
            ready_path = root / "ready"
            process = self._run_session_process(
                control_path,
                authority_path,
                "kill-after-effect-ambiguous-publication",
                ready_path,
            )
            self._wait_for_file(ready_path, process)
            self.assertEqual(
                "effect-ambiguous-after-outcome",
                ready_path.read_text(encoding="utf-8").strip(),
            )
            self.assertEqual(-signal.SIGKILL, process.wait(timeout=10))
            stdout, stderr = process.communicate()
            self.assertEqual("", stderr, msg=stdout)

            child_result = root / "child-result"
            verifier = multiprocessing.get_context("fork").Process(
                target=_recover_effect_child,
                args=(str(control_path), str(authority_path), str(child_result)),
            )
            verifier.start()
            verifier.join(timeout=10)
            self.assertEqual(0, verifier.exitcode)
            self.assertEqual(
                "ambiguous:3:ambiguous:lock-released\n",
                child_result.read_text(encoding="utf-8"),
            )
            self.assertEqual(authority_bytes, authority_path.read_bytes())

    def test_v10_integrated_effect_death_after_committed_finish_is_reopenable(self) -> None:
        """The durable mutation wrapper remains recoverable after committed finish returns."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            control_path = root / "control.sqlite"
            authority_path = root / "authority.sqlite"
            authority_bytes = b"authority remains untouched after integrated commit\n"
            authority_path.write_bytes(authority_bytes)
            ready_path = root / "ready"
            process = self._run_session_process(
                control_path,
                authority_path,
                "kill-after-integrated-effect-committed-finish",
                ready_path,
            )
            self._wait_for_file(ready_path, process)
            self.assertEqual(
                "integrated-effect-committed-after-finish",
                ready_path.read_text(encoding="utf-8").strip(),
            )
            self.assertEqual(-signal.SIGKILL, process.wait(timeout=10))
            stdout, stderr = process.communicate()
            self.assertEqual("", stderr, msg=stdout)

            child_result = root / "child-result"
            verifier = multiprocessing.get_context("fork").Process(
                target=_recover_effect_child,
                args=(
                    str(control_path),
                    str(authority_path),
                    str(child_result),
                    "subprocess-integrated-effect",
                ),
            )
            verifier.start()
            verifier.join(timeout=10)
            self.assertEqual(0, verifier.exitcode)
            self.assertEqual(
                "held:2:committed:lock-released\n",
                child_result.read_text(encoding="utf-8"),
            )
            self.assertEqual(authority_bytes, authority_path.read_bytes())

    def test_v10_integrated_effect_death_after_ambiguous_finish_is_reopenable(self) -> None:
        """The durable mutation wrapper preserves an ambiguous finish across process death."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            control_path = root / "control.sqlite"
            authority_path = root / "authority.sqlite"
            authority_bytes = b"authority remains untouched after integrated ambiguity\n"
            authority_path.write_bytes(authority_bytes)
            ready_path = root / "ready"
            process = self._run_session_process(
                control_path,
                authority_path,
                "kill-after-integrated-effect-ambiguous-finish",
                ready_path,
            )
            self._wait_for_file(ready_path, process)
            self.assertEqual(
                "integrated-effect-ambiguous-after-finish",
                ready_path.read_text(encoding="utf-8").strip(),
            )
            self.assertEqual(-signal.SIGKILL, process.wait(timeout=10))
            stdout, stderr = process.communicate()
            self.assertEqual("", stderr, msg=stdout)

            child_result = root / "child-result"
            verifier = multiprocessing.get_context("fork").Process(
                target=_recover_effect_child,
                args=(
                    str(control_path),
                    str(authority_path),
                    str(child_result),
                    "subprocess-integrated-effect",
                ),
            )
            verifier.start()
            verifier.join(timeout=10)
            self.assertEqual(0, verifier.exitcode)
            self.assertEqual(
                "ambiguous:3:ambiguous:lock-released\n",
                child_result.read_text(encoding="utf-8"),
            )
            self.assertEqual(authority_bytes, authority_path.read_bytes())

    def test_v10_subprocess_death_after_ambiguous_replacement_commit_is_fenced(self) -> None:
        """A fresh process fences an unreported ambiguous-session replacement."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            control_path = root / "control.sqlite"
            authority_path = root / "authority.sqlite"
            authority_bytes = b"authority remains untouched after replacement crash\n"
            authority_path.write_bytes(authority_bytes)
            ready_path = root / "ready"
            process = self._run_session_process(
                control_path,
                authority_path,
                "kill-after-ambiguous-replacement-commit",
                ready_path,
            )
            self._wait_for_file(ready_path, process)
            self.assertEqual(
                "replacement-committed-before-outcome",
                ready_path.read_text(encoding="utf-8").strip(),
            )
            self.assertEqual(-signal.SIGKILL, process.wait(timeout=10))
            stdout, stderr = process.communicate()
            self.assertEqual("", stderr, msg=stdout)

            verifier_result = root / "recovered-child-result"
            verifier = multiprocessing.get_context("fork").Process(
                target=_recover_ambiguous_child,
                args=(str(control_path), str(authority_path), str(verifier_result)),
            )
            verifier.start()
            verifier.join(timeout=10)
            self.assertEqual(0, verifier.exitcode)
            self.assertEqual("held:1:lock-released\n", verifier_result.read_text(encoding="utf-8"))

            reopened = SQLiteBarrierSessionStore(
                SQLiteRollbackControlStore(control_path, PROJECT, authority_path),
                lambda: "authority-3",
            ).snapshot()
            self.assertIsNotNone(reopened)
            assert reopened is not None
            self.assertEqual(("held", 1), (reopened.status, reopened.revision))
            self.assertEqual("subprocess-replacement", reopened.identity.attempt_id)
            self.assertEqual(authority_bytes, authority_path.read_bytes())

    def test_v10_subprocess_death_after_ambiguous_reconciliation_outcome_is_recoverable(
        self,
    ) -> None:
        """A death after reconciliation publication remains reopenable and lock-safe."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            control_path = root / "control.sqlite"
            authority_path = root / "authority.sqlite"
            authority_bytes = b"authority remains untouched after reconciliation\n"
            authority_path.write_bytes(authority_bytes)
            ready_path = root / "ready"
            process = self._run_session_process(
                control_path,
                authority_path,
                "kill-after-ambiguous-reconciliation-outcome-publication",
                ready_path,
            )
            self._wait_for_file(ready_path, process)
            self.assertEqual(
                "reconciliation-outcome-published",
                ready_path.read_text(encoding="utf-8").strip(),
            )
            self.assertEqual(-signal.SIGKILL, process.wait(timeout=10))
            stdout, stderr = process.communicate()
            self.assertEqual("", stderr, msg=stdout)

            verifier_result = root / "recovered-child-result"
            verifier = multiprocessing.get_context("fork").Process(
                target=_recover_ambiguous_child,
                args=(str(control_path), str(authority_path), str(verifier_result)),
            )
            verifier.start()
            verifier.join(timeout=10)
            self.assertEqual(0, verifier.exitcode)
            self.assertEqual("held:1:lock-released\n", verifier_result.read_text(encoding="utf-8"))

            reopened = SQLiteBarrierSessionStore(
                SQLiteRollbackControlStore(control_path, PROJECT, authority_path),
                lambda: "authority-3",
            )
            state = reopened.snapshot()
            self.assertIsNotNone(state)
            assert state is not None
            self.assertEqual(("held", 1), (state.status, state.revision))
            self.assertEqual("subprocess-replacement", state.identity.attempt_id)
            self.assertEqual(authority_bytes, authority_path.read_bytes())
            with closing(sqlite3.connect(control_path)) as connection:
                outcomes = connection.execute(
                    "SELECT outcome FROM barrier_session_intent WHERE project_id=?",
                    (PROJECT,),
                ).fetchall()
            self.assertEqual([("committed",), ("committed",), ("reconciled",)], outcomes)

    def test_v10_durable_session_persists_children_and_reopen(self) -> None:
        from tools.upgrade_identity import BarrierChildIdentity

        with tempfile.TemporaryDirectory() as directory:
            store = SQLiteBarrierSessionStore(
                SQLiteRollbackControlStore(Path(directory) / "control.sqlite", PROJECT),
                authority_revision_reader=lambda: "authority-3",
            )
            identity = self._session_identity()
            held = store.create(identity)
            self.assertEqual(("held", 1), (held.status, held.revision))
            held = store.bind_child(1, BarrierChildIdentity.bind(identity, "forward-1", "new"))
            held = store.bind_child(
                2, BarrierChildIdentity.bind(identity, "rollback-1", "rollback")
            )
            releasing = store.begin_reopen(3, "rollback", _reopen_evidence(held, "rollback"))
            released = store.complete_reopen(4, _runtime_evidence(releasing, "rollback"))
            self.assertEqual(("released", 5), (released.status, released.revision))
            reread = store.snapshot()
            self.assertIsNotNone(reread)
            assert reread is not None
            self.assertEqual(held.identity, reread.identity)
            assert reread.rollback_child is not None
            self.assertEqual("rollback-1", reread.rollback_child.operation_id)
            self.assertEqual(releasing.revision + 1, reread.revision)

    def test_v10_reopen_target_survives_restart_and_cannot_be_substituted(self) -> None:
        from tools.upgrade_identity import BarrierChildIdentity

        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "control.sqlite"
            store = SQLiteBarrierSessionStore(
                SQLiteRollbackControlStore(path, PROJECT), lambda: "authority-3"
            )
            identity = self._session_identity()
            held = store.create(identity)
            held = store.bind_child(1, BarrierChildIdentity.bind(identity, "forward-1", "new"))
            held = store.bind_child(
                2, BarrierChildIdentity.bind(identity, "rollback-1", "rollback")
            )
            releasing = store.begin_reopen(3, "new", _reopen_evidence(held, "new"))
            self.assertEqual("new", releasing.reopen_target)

            restarted = SQLiteBarrierSessionStore(
                SQLiteRollbackControlStore(path, PROJECT), lambda: "authority-3"
            )
            recovered = restarted.snapshot()
            self.assertIsNotNone(recovered)
            assert recovered is not None
            self.assertEqual("new", recovered.reopen_target)
            with self.assertRaisesRegex(ControlStoreError, "does not match reopen target"):
                restarted.complete_reopen(
                    recovered.revision, _runtime_evidence(recovered, "rollback")
                )
            self.assertEqual("releasing", restarted.snapshot().status)  # type: ignore[union-attr]
            released = restarted.complete_reopen(
                recovered.revision, _runtime_evidence(recovered, "new")
            )
            self.assertEqual(("released", "new"), (released.status, released.reopen_target))

    def test_v10_durable_session_recheck_is_fresh_and_read_only(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            store = SQLiteBarrierSessionStore(
                SQLiteRollbackControlStore(Path(directory) / "control.sqlite", PROJECT),
                lambda: "authority-3",
            )
            identity = self._session_identity()
            held = store.create(identity)
            self.assertEqual(held, store.recheck_held(1))
            self.assertEqual(held, store.recheck_held(held))
            self.assertEqual(1, store.snapshot().revision)  # type: ignore[union-attr]
            with self.assertRaisesRegex(ControlStoreError, "CAS conflict"):
                store.recheck_held(2)
            with self.assertRaisesRegex(ControlStoreError, "expected revision"):
                store.recheck_held(False)
            changed = dict(identity.as_record())
            changed["attempt_id"] = "other-attempt"
            from tools.upgrade_identity import canonical_barrier_session_digest

            changed["identity_digest"] = canonical_barrier_session_digest(changed)
            with self.assertRaisesRegex(ControlStoreError, "identity changed"):
                store.recheck_held(
                    BarrierSessionState(BarrierSessionIdentity.from_record(changed), "held", 1)
                )
            store.bind_child(1, BarrierChildIdentity.bind(identity, "forward-1", "new"))
            store.begin_reopen(2, "new", _reopen_evidence(store.snapshot(), "new"))
            with self.assertRaisesRegex(ControlStoreError, "not held"):
                store.recheck_held(3)

            changing = ["authority-3"]
            changing_store = SQLiteBarrierSessionStore(
                SQLiteRollbackControlStore(Path(directory) / "changing.sqlite", PROJECT),
                lambda: changing[0],
            )
            changing_store.create(identity)
            changing[0] = "authority-new"
            with self.assertRaisesRegex(ControlStoreError, "authority revision changed"):
                changing_store.recheck_held(1)

    def test_v10_recheck_requires_trusted_authority_rereader(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            store = SQLiteBarrierSessionStore(
                SQLiteRollbackControlStore(Path(directory) / "control.sqlite", PROJECT)
            )
            identity = self._session_identity()
            store.create(identity)
            with self.assertRaisesRegex(ControlStoreError, "rereader is required"):
                store.recheck_held(1)
            with self.assertRaisesRegex(ControlStoreError, "trusted rereader"):
                SQLiteBarrierSessionStore(
                    SQLiteRollbackControlStore(Path(directory) / "other.sqlite", PROJECT),
                    lambda: "authority-3",
                ).recheck_held(1, "authority-3")

            failing = SQLiteBarrierSessionStore(
                SQLiteRollbackControlStore(Path(directory) / "failing.sqlite", PROJECT),
            )
            failing = SQLiteBarrierSessionStore(
                SQLiteRollbackControlStore(Path(directory) / "failing.sqlite", PROJECT),
                lambda: (_ for _ in ()).throw(OSError("authority unavailable")),
            )
            with self.assertRaisesRegex(ControlStoreError, "reread failed"):
                failing.recheck_held(1)

            invalid = SQLiteBarrierSessionStore(
                SQLiteRollbackControlStore(Path(directory) / "invalid.sqlite", PROJECT),
                lambda: "",
            )
            with self.assertRaisesRegex(ControlStoreError, "revision is invalid"):
                invalid.recheck_held(1)

    def test_v10_cas_rereads_authority_under_write_lock(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            authority = ["authority-3"]
            store = SQLiteBarrierSessionStore(
                SQLiteRollbackControlStore(Path(directory) / "control.sqlite", PROJECT),
                lambda: authority[0],
            )
            identity = self._session_identity()
            held = store.create(identity)
            authority[0] = "authority-rotated"
            with self.assertRaisesRegex(ControlStoreError, "authority revision changed"):
                store.cas(
                    held.revision,
                    BarrierSessionState(identity, "releasing", held.revision + 1),
                )
            self.assertEqual(held, store.snapshot())

    def test_v10_cas_zero_rereads_authority_before_bootstrap_write(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            authority = ["authority-3"]
            store = SQLiteBarrierSessionStore(
                SQLiteRollbackControlStore(Path(directory) / "control.sqlite", PROJECT),
                lambda: authority[0],
            )
            identity = self._session_identity()
            authority[0] = "authority-rotated"
            with self.assertRaisesRegex(ControlStoreError, "authority revision changed"):
                store.cas(0, BarrierSessionState(identity, "held", 1))
            self.assertIsNone(store.snapshot())

    def test_v10_caller_owned_recheck_requires_guard_and_is_read_only(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            store = SQLiteBarrierSessionStore(
                SQLiteRollbackControlStore(Path(directory) / "control.sqlite", PROJECT),
                lambda: "authority-3",
            )
            identity = self._session_identity()
            held = store.create(identity)
            with (
                self.assertRaisesRegex(LockOwnershipError, "guard is required"),
                store.lock_owned_by_caller(cast(CoordinatorLockGuard, None)),
            ):
                pass
            with self.assertRaisesRegex(TypeError, "missing"):
                store.recheck_held_locked(identity, held.revision)  # type: ignore[arg-type,call-arg]
            with locked() as guard, store.lock_owned_by_caller(guard):
                reread = store.recheck_held_locked(guard, identity, held.revision)
                self.assertEqual(held, reread)
                with (
                    self.assertRaisesRegex(ControlStoreError, "non-reentrant"),
                    store.lock_owned_by_caller(guard),
                ):
                    pass

    def test_cas_locked_requires_caller_owned_scope_and_fresh_identity(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            authority = ["authority-3"]
            store = SQLiteBarrierSessionStore(
                SQLiteRollbackControlStore(Path(directory) / "control.sqlite", PROJECT),
                lambda: authority[0],
            )
            identity = self._session_identity()
            held = store.create(identity)
            with locked() as guard, store.lock_owned_by_caller(guard):
                releasing = BarrierSessionState(identity, "releasing", held.revision + 1)
                updated = store.cas_locked(guard, identity, held.revision, releasing)
            self.assertEqual("releasing", updated.status)
            with self.assertRaisesRegex(LockOwnershipError, "inactive"):
                store.cas_locked(guard, identity, updated.revision, updated)
            self.assertEqual(updated, store.snapshot())

    def test_cas_locked_cannot_bootstrap_revision_zero(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            identity = self._session_identity()
            store = SQLiteBarrierSessionStore(
                SQLiteRollbackControlStore(Path(directory) / "control.sqlite", PROJECT),
                lambda: "authority-3",
            )
            with (
                locked() as guard,
                store.lock_owned_by_caller(guard),
                self.assertRaisesRegex(ControlStoreError, "expected revision"),
            ):
                store.cas_locked(
                    guard,
                    identity,
                    0,
                    BarrierSessionState(identity, "held", 1),
                )
            self.assertIsNone(store.snapshot())

    def test_cas_locked_rejects_authority_rotation_before_write(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            authority = ["authority-3"]
            store = SQLiteBarrierSessionStore(
                SQLiteRollbackControlStore(Path(directory) / "control.sqlite", PROJECT),
                lambda: authority[0],
            )
            identity = self._session_identity()
            held = store.create(identity)
            authority[0] = "authority-rotated"
            with (
                locked() as guard,
                store.lock_owned_by_caller(guard),
                self.assertRaisesRegex(ControlStoreError, "authority revision changed"),
            ):
                store.cas_locked(
                    guard,
                    identity,
                    held.revision,
                    BarrierSessionState(identity, "releasing", held.revision + 1),
                )
            self.assertEqual(held, store.snapshot())

    def test_cas_locked_rejects_invalid_scope_inputs_before_write(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            identity = self._session_identity()
            store = SQLiteBarrierSessionStore(
                SQLiteRollbackControlStore(Path(directory) / "control.sqlite", PROJECT),
                lambda: "authority-3",
            )
            held = store.create(identity)
            with self.assertRaisesRegex(LockOwnershipError, "coordinator lock guard"):
                store.cas_locked(cast(Any, None), identity, held.revision, held)
            with locked() as guard:
                with self.assertRaisesRegex(ControlStoreError, "operation lock is required"):
                    store.cas_locked(guard, identity, held.revision, held)
                with store.lock_owned_by_caller(guard):
                    with self.assertRaisesRegex(ControlStoreError, "identity is required"):
                        store.cas_locked(guard, cast(Any, None), held.revision, held)
                    with self.assertRaisesRegex(ControlStoreError, "expected revision"):
                        store.cas_locked(guard, identity, 0, held)
                    with self.assertRaisesRegex(ControlStoreError, "write identity"):
                        store.cas_locked(
                            guard,
                            identity,
                            held.revision,
                            BarrierSessionState(identity, "released", held.revision + 1),
                        )
                    with (
                        patch(
                            "tools.rollback_control_store.coordinator_lock_path",
                            return_value=guard.path.parent / "other",
                        ),
                        self.assertRaisesRegex(ControlStoreError, "path mismatch"),
                    ):
                        store.cas_locked(guard, identity, held.revision, held)

            no_reader = SQLiteBarrierSessionStore(
                SQLiteRollbackControlStore(Path(directory) / "no-reader.sqlite", PROJECT)
            )
            no_reader.create(identity)
            with (
                locked() as guard,
                no_reader.lock_owned_by_caller(guard),
                self.assertRaisesRegex(ControlStoreError, "rereader is required"),
            ):
                no_reader.cas_locked(guard, identity, held.revision, held)

    def test_v10_caller_owned_recheck_rejects_stale_identity_and_authority(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            authority = ["authority-3"]
            store = SQLiteBarrierSessionStore(
                SQLiteRollbackControlStore(Path(directory) / "control.sqlite", PROJECT),
                lambda: authority[0],
            )
            identity = self._session_identity()
            held = store.create(identity)
            changed = dict(identity.as_record())
            changed["attempt_id"] = "other-attempt"
            from tools.upgrade_identity import canonical_barrier_session_digest

            changed["identity_digest"] = canonical_barrier_session_digest(changed)
            with locked() as guard, store.lock_owned_by_caller(guard):
                with self.assertRaisesRegex(ControlStoreError, "identity changed"):
                    store.recheck_held_locked(
                        guard, BarrierSessionIdentity.from_record(changed), held.revision
                    )
                authority[0] = "authority-new"
                with self.assertRaisesRegex(ControlStoreError, "authority revision changed"):
                    store.recheck_held_locked(guard, identity, held.revision)

    def test_v10_caller_owned_recheck_rejects_missing_lock_and_invalid_inputs(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "control.sqlite"
            store = SQLiteBarrierSessionStore(
                SQLiteRollbackControlStore(path, PROJECT), lambda: "authority-3"
            )
            identity = self._session_identity()
            with locked() as wrong_guard:
                wrong_guard._path = Path(directory) / "wrong-lock"
                with self.assertRaisesRegex(LockOwnershipError, "path changed"):
                    store.recover_unknown_locked(wrong_guard)

            with locked() as guard:
                with self.assertRaisesRegex(LockOwnershipError, "guard is required"):
                    store.recover_unknown_locked(cast(Any, None))
                with self.assertRaisesRegex(ControlStoreError, "operation lock is required"):
                    store.recheck_held_locked(guard, identity, 1)
                with store.lock_owned_by_caller(guard):
                    with self.assertRaisesRegex(ControlStoreError, "identity is required"):
                        store.recheck_held_locked(guard, cast(Any, None), 1)
                    with self.assertRaisesRegex(ControlStoreError, "expected revision"):
                        store.recheck_held_locked(guard, identity, 0)
                    with self.assertRaisesRegex(ControlStoreError, "allowed statuses"):
                        store.recheck_held_locked(guard, identity, 1, ("ambiguous",))
                    with self.assertRaisesRegex(ControlStoreError, "session is absent"):
                        store.recheck_held_locked(guard, identity, 1)

            no_reader = SQLiteBarrierSessionStore(SQLiteRollbackControlStore(path, PROJECT))
            no_reader.create(identity)
            with (
                locked() as guard,
                no_reader.lock_owned_by_caller(guard),
                self.assertRaisesRegex(ControlStoreError, "rereader is required"),
            ):
                no_reader.recheck_held_locked(guard, identity, 1)

    def test_v10_caller_owned_recheck_rejects_path_and_reader_failures(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            identity = self._session_identity()
            path = Path(directory) / "control.sqlite"
            store = SQLiteBarrierSessionStore(
                SQLiteRollbackControlStore(path, PROJECT), lambda: "authority-3"
            )
            held = store.create(identity)
            with (
                locked() as guard,
                patch(
                    "tools.rollback_control_store.coordinator_lock_path",
                    return_value=guard.path.parent / "other",
                ),
                self.assertRaisesRegex(ControlStoreError, "path mismatch"),
                store.lock_owned_by_caller(guard),
            ):
                pass

            failing = SQLiteBarrierSessionStore(
                SQLiteRollbackControlStore(Path(directory) / "failing.sqlite", PROJECT),
            )
            failing.create(identity)
            failing = SQLiteBarrierSessionStore(
                SQLiteRollbackControlStore(Path(directory) / "failing.sqlite", PROJECT),
                lambda: (_ for _ in ()).throw(OSError("authority unavailable")),
            )
            with (
                locked() as guard,
                failing.lock_owned_by_caller(guard),
                self.assertRaisesRegex(ControlStoreError, "reread failed"),
            ):
                failing.recheck_held_locked(guard, identity, 1)

            invalid = SQLiteBarrierSessionStore(
                SQLiteRollbackControlStore(Path(directory) / "invalid.sqlite", PROJECT),
                lambda: "",
            )
            with (
                locked() as guard,
                invalid.lock_owned_by_caller(guard),
                self.assertRaisesRegex(ControlStoreError, "revision is invalid"),
            ):
                invalid.recheck_held_locked(guard, identity, 1)
            self.assertEqual(1, held.revision)

    def test_v10_process_death_recovery_rejects_missing_or_mismatched_session(self) -> None:
        for mutate_session, expected_error in (
            ("delete", "prepared session intent has no session"),
            ("identity", "prepared session intent identity is invalid"),
        ):
            with (
                self.subTest(mutate_session=mutate_session),
                tempfile.TemporaryDirectory() as directory,
            ):
                path = Path(directory) / "control.sqlite"
                store = SQLiteBarrierSessionStore(
                    SQLiteRollbackControlStore(path, PROJECT), lambda: "authority-3"
                )
                identity = self._session_identity()
                held = store.create(identity)
                with closing(sqlite3.connect(path)) as connection:
                    intent_id = connection.execute(
                        "SELECT intent_id FROM barrier_session_intent WHERE project_id=?",
                        (PROJECT,),
                    ).fetchone()[0]
                    connection.execute(
                        "UPDATE barrier_session_intent SET outcome='prepared' WHERE intent_id=?",
                        (intent_id,),
                    )
                    if mutate_session == "delete":
                        connection.execute(
                            "DELETE FROM barrier_session WHERE project_id=?", (PROJECT,)
                        )
                    else:
                        connection.execute(
                            "UPDATE barrier_session_intent SET identity_digest=? WHERE intent_id=?",
                            ("f" * 64, intent_id),
                        )
                    connection.commit()
                with self.assertRaisesRegex(ControlStoreError, expected_error):
                    store.recover_unknown()
                self.assertFalse(store.operation_owned_by_current_thread)
                with closing(sqlite3.connect(path)) as connection:
                    outcome = connection.execute(
                        "SELECT outcome FROM barrier_session_intent WHERE intent_id=?",
                        (intent_id,),
                    ).fetchone()[0]
                    self.assertEqual("prepared", outcome)
                    if mutate_session == "delete":
                        self.assertIsNone(
                            connection.execute(
                                "SELECT 1 FROM barrier_session WHERE project_id=?", (PROJECT,)
                            ).fetchone()
                        )
                    else:
                        self.assertEqual(held, store.snapshot())

    def test_v10_session_intent_recovery_fences_and_requires_newer_fence(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "control.sqlite"
            store = SQLiteBarrierSessionStore(
                SQLiteRollbackControlStore(path, PROJECT), lambda: "authority-3"
            )
            identity = self._session_identity()
            held = store.create(identity)
            connection = sqlite3.connect(path)
            try:
                intent = connection.execute(
                    "SELECT intent_id,outcome FROM barrier_session_intent WHERE project_id=?",
                    (PROJECT,),
                ).fetchone()
                self.assertIsNotNone(intent)
                assert intent is not None
                self.assertEqual("committed", intent[1])
                connection.execute(
                    "UPDATE barrier_session_intent SET outcome='prepared' WHERE intent_id=?",
                    (intent[0],),
                )
                connection.commit()
            finally:
                connection.close()
            recovered = store.recover_unknown()
            self.assertIsNotNone(recovered)
            assert recovered is not None
            self.assertEqual(
                ("ambiguous", held.revision + 1), (recovered.status, recovered.revision)
            )
            self.assertEqual(recovered, store.recover_unknown())
            with self.assertRaisesRegex(RecoveryRejectedError, "distinct newer fence"):
                store.reconcile_ambiguous(recovered.revision, held)
            self.assertFalse(store.operation_owned_by_current_thread)
            self.assertEqual(recovered, store.snapshot())

            replacement_record = dict(identity.as_record())
            replacement_record["attempt_id"] = "attempt-new"
            replacement_record["state_revision"] = identity.state_revision + 1
            replacement_record["durable_barrier_id"] = "barrier-new"
            replacement_record["fencing_token"] = "fence-new"  # noqa: S105
            from tools.upgrade_identity import canonical_barrier_session_digest

            replacement_record["identity_digest"] = canonical_barrier_session_digest(
                replacement_record
            )
            replacement = BarrierSessionState(
                BarrierSessionIdentity.from_record(replacement_record), "held", 1
            )
            reused_fence_record = dict(replacement_record)
            reused_fence_record["durable_barrier_id"] = identity.durable_barrier_id
            reused_fence_record["fencing_token"] = identity.fencing_token
            reused_fence_record["identity_digest"] = canonical_barrier_session_digest(
                reused_fence_record
            )
            reused_fence = BarrierSessionState(
                BarrierSessionIdentity.from_record(reused_fence_record), "held", 1
            )
            with self.assertRaisesRegex(RecoveryRejectedError, "distinct newer fence"):
                store.reconcile_ambiguous(recovered.revision, reused_fence)
            self.assertFalse(store.operation_owned_by_current_thread)
            self.assertEqual(recovered, store.snapshot())
            mismatch_store = SQLiteBarrierSessionStore(
                SQLiteRollbackControlStore(path, PROJECT), lambda: "authority-other"
            )
            with self.assertRaisesRegex(
                ControlStoreError, "replacement authority revision changed"
            ):
                mismatch_store.reconcile_ambiguous(recovered.revision, replacement)
            self.assertFalse(mismatch_store.operation_owned_by_current_thread)
            self.assertEqual(recovered, mismatch_store.snapshot())

            def fail_authority_read() -> str:
                raise RuntimeError("authority unavailable")

            failing_store = SQLiteBarrierSessionStore(
                SQLiteRollbackControlStore(path, PROJECT), fail_authority_read
            )
            with self.assertRaisesRegex(RecoveryRejectedError, "fresh authority reread failed"):
                failing_store.reconcile_ambiguous(recovered.revision, replacement)
            self.assertFalse(failing_store.operation_owned_by_current_thread)
            self.assertEqual(recovered, failing_store.snapshot())
            invalid_store = SQLiteBarrierSessionStore(
                SQLiteRollbackControlStore(path, PROJECT), lambda: ""
            )
            with self.assertRaisesRegex(
                RecoveryRejectedError, "fresh authority revision is invalid"
            ):
                invalid_store.reconcile_ambiguous(recovered.revision, replacement)
            self.assertFalse(invalid_store.operation_owned_by_current_thread)
            self.assertEqual(recovered, invalid_store.snapshot())
            connection = sqlite3.connect(path)
            try:
                connection.execute(
                    "INSERT INTO barrier_session_intent "
                    "(project_id,intent_id,attempt_id,expected_revision,proposed_revision,"
                    "proposed_status,identity_digest,outcome,cause_code) "
                    "VALUES (?,?,?,?,?,?,?,?,?)",
                    (
                        PROJECT,
                        "unresolved-intent",
                        identity.attempt_id,
                        recovered.revision,
                        recovered.revision + 1,
                        "held",
                        identity.identity_digest,
                        "prepared",
                        None,
                    ),
                )
                connection.commit()
            finally:
                connection.close()
            with self.assertRaisesRegex(RecoveryRejectedError, "unresolved intent"):
                store.reconcile_ambiguous(recovered.revision, replacement)
            self.assertFalse(store.operation_owned_by_current_thread)
            self.assertEqual(recovered, store.snapshot())
            connection = sqlite3.connect(path)
            try:
                connection.execute(
                    "UPDATE barrier_session_intent SET outcome='ambiguous' "
                    "WHERE intent_id='unresolved-intent'"
                )
                connection.commit()
            finally:
                connection.close()
            reconciled = store.reconcile_ambiguous(recovered.revision, replacement)
            self.assertEqual(replacement, reconciled)
            self.assertEqual(replacement, store.snapshot())
            connection = sqlite3.connect(path)
            try:
                history = connection.execute(
                    "SELECT record_json FROM barrier_session_history "
                    "WHERE project_id=? AND attempt_id=?",
                    (PROJECT, identity.attempt_id),
                ).fetchone()
            finally:
                connection.close()
            self.assertIsNotNone(history)
            assert history is not None
            self.assertEqual("ambiguous", json.loads(history[0])["status"])

    def test_v10_session_intent_recovery_rejects_invalid_intent_records(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "control.sqlite"
            store = SQLiteBarrierSessionStore(
                SQLiteRollbackControlStore(path, PROJECT), lambda: "authority-3"
            )
            identity = self._session_identity()
            store.create(identity)
            with closing(sqlite3.connect(path)) as connection:
                connection.execute(
                    "UPDATE barrier_session_intent SET outcome='prepared',attempt_id='wrong' "
                    "WHERE project_id=?",
                    (PROJECT,),
                )
                connection.commit()
            with self.assertRaisesRegex(ControlStoreError, "identity is invalid"):
                store.recover_unknown()
            with closing(sqlite3.connect(path)) as connection:
                connection.execute(
                    "UPDATE barrier_session_intent SET attempt_id=?,proposed_status=? "
                    "WHERE project_id=?",
                    (identity.attempt_id, "releasing", PROJECT),
                )
                connection.commit()
            with self.assertRaisesRegex(ControlStoreError, "identity is invalid"):
                store.recover_unknown()
            with closing(sqlite3.connect(path)) as connection:
                connection.execute(
                    "UPDATE barrier_session_intent SET proposed_status=? WHERE project_id=?",
                    ("bogus", PROJECT),
                )
                connection.commit()
            with self.assertRaisesRegex(ControlStoreError, "identity is invalid"):
                store.recover_unknown()

            with store.operation_lock():
                connection = sqlite3.connect(path)
                try:
                    store._ensure_table(connection)
                    with self.assertRaisesRegex(ControlStoreError, "outcome is invalid"):
                        store._mark_intent_locked(connection, "missing", "unknown")
                    with self.assertRaisesRegex(ControlStoreError, "outcome fence was lost"):
                        store._mark_intent_locked(connection, "missing", "ambiguous")
                finally:
                    connection.close()

    def test_v10_interrupted_recovery_residue_requires_exact_revision_chain(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "control.sqlite"
            store = SQLiteBarrierSessionStore(
                SQLiteRollbackControlStore(path, PROJECT), lambda: "authority-3"
            )
            identity = self._session_identity()
            created = store.create(identity)
            with closing(sqlite3.connect(path)) as connection:
                connection.execute(
                    "UPDATE barrier_session SET status='ambiguous',revision=? WHERE project_id=?",
                    (created.revision + 1, PROJECT),
                )
                connection.execute(
                    "UPDATE barrier_session_intent SET outcome='prepared',expected_revision=? "
                    "WHERE project_id=?",
                    (created.revision, PROJECT),
                )
                connection.commit()

            with self.assertRaisesRegex(ControlStoreError, "identity is invalid"):
                store.recover_unknown()
            self.assertFalse(store.operation_owned_by_current_thread)
            unchanged = store.snapshot()
            assert unchanged is not None
            self.assertEqual(("ambiguous", 2), (unchanged.status, unchanged.revision))
            with closing(sqlite3.connect(path)) as connection:
                self.assertEqual(
                    [("prepared",)],
                    connection.execute(
                        "SELECT outcome FROM barrier_session_intent WHERE project_id=?",
                        (PROJECT,),
                    ).fetchall(),
                )

    def test_v10_session_intent_publication_failure_requires_recovery(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "control.sqlite"
            store = SQLiteBarrierSessionStore(
                SQLiteRollbackControlStore(path, PROJECT), lambda: "authority-3"
            )
            identity = self._session_identity()
            original = store._mark_intent_locked

            def fail_publication(*_args: Any, **_kwargs: Any) -> None:
                raise OSError("outcome publication unavailable")

            store._mark_intent_locked = fail_publication  # type: ignore[method-assign]
            with self.assertRaisesRegex(ControlStoreError, "outcome publication is ambiguous"):
                store.create(identity)
            store._mark_intent_locked = original  # type: ignore[method-assign]
            recovered = store.recover_unknown()
            self.assertIsNotNone(recovered)
            assert recovered is not None
            self.assertEqual("ambiguous", recovered.status)

    def test_v10_session_intent_recovery_rejects_missing_session(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "control.sqlite"
            store = SQLiteBarrierSessionStore(
                SQLiteRollbackControlStore(path, PROJECT), lambda: "authority-3"
            )
            with store.operation_lock():
                connection = sqlite3.connect(path)
                try:
                    store._ensure_table(connection)
                    connection.execute(
                        "INSERT INTO barrier_session_intent "
                        "(project_id,intent_id,attempt_id,expected_revision,proposed_revision,"
                        "proposed_status,identity_digest,outcome,cause_code) "
                        "VALUES (?,?,?,?,?,?,?,?,?)",
                        (PROJECT, "orphan", "attempt", 0, 1, "held", "d" * 64, "prepared", None),
                    )
                    connection.commit()
                finally:
                    connection.close()
            with self.assertRaisesRegex(ControlStoreError, "has no session"):
                store.recover_unknown()

    def test_v10_session_intent_recovery_marks_preexisting_ambiguous(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "control.sqlite"
            store = SQLiteBarrierSessionStore(
                SQLiteRollbackControlStore(path, PROJECT), lambda: "authority-3"
            )
            identity = self._session_identity()
            created = store.create(identity)
            connection = sqlite3.connect(path)
            try:
                connection.execute(
                    "UPDATE barrier_session SET status='ambiguous',revision=? WHERE project_id=?",
                    (created.revision + 1, PROJECT),
                )
                connection.execute(
                    "UPDATE barrier_session_intent SET outcome='prepared',"
                    "expected_revision=?,proposed_revision=?,proposed_status=? "
                    "WHERE project_id=?",
                    (created.revision, created.revision + 1, "ambiguous", PROJECT),
                )
                connection.commit()
            finally:
                connection.close()
            recovered = store.recover_unknown()
            self.assertIsNotNone(recovered)
            assert recovered is not None
            self.assertEqual(
                ("ambiguous", created.revision + 1), (recovered.status, recovered.revision)
            )
            with closing(sqlite3.connect(path)) as connection:
                outcome = connection.execute(
                    "SELECT outcome FROM barrier_session_intent WHERE project_id=?",
                    (PROJECT,),
                ).fetchone()
            self.assertEqual(("ambiguous",), outcome)

    def test_v10_session_intent_recovery_and_reconcile_reject_reentrant_or_invalid_calls(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "control.sqlite"
            store = SQLiteBarrierSessionStore(
                SQLiteRollbackControlStore(path, PROJECT), lambda: "authority-3"
            )
            identity = self._session_identity()
            held = store.create(identity)
            with store.operation_lock():
                with self.assertRaisesRegex(ControlStoreError, "non-reentrant"):
                    store.recover_unknown()
                with self.assertRaisesRegex(RecoveryRejectedError, "non-reentrant"):
                    store.reconcile_ambiguous(held.revision, held)
            with self.assertRaisesRegex(RecoveryRejectedError, "expected revision is invalid"):
                store.reconcile_ambiguous(0, held)
            with self.assertRaisesRegex(RecoveryRejectedError, "new held session"):
                store.reconcile_ambiguous(
                    held.revision,
                    BarrierSessionState(identity, "releasing", 1),
                )

    def test_v10_commit_failure_is_durably_ambiguous(self) -> None:  # noqa: C901
        class FlakyConnection:
            def __init__(self, connection: sqlite3.Connection, owner: Any) -> None:
                self.connection = connection
                self.owner = owner

            def execute(self, *args: Any, **kwargs: Any) -> Any:
                return self.connection.execute(*args, **kwargs)

            def commit(self) -> None:
                if self.owner.fail_next_commit:
                    self.owner.fail_next_commit = False
                    raise sqlite3.OperationalError("injected commit boundary failure")
                if self.owner.fail_commit_after is not None:
                    if self.owner.fail_commit_after == 0:
                        self.owner.fail_commit_after = None
                        raise sqlite3.OperationalError("injected commit boundary failure")
                    self.owner.fail_commit_after -= 1
                self.connection.commit()

            def rollback(self) -> None:
                self.connection.rollback()

        class FlakyStore(SQLiteRollbackControlStore):
            def __init__(self, *args: Any) -> None:
                super().__init__(*args)
                self.fail_next_commit = True
                self.fail_commit_after: int | None = None

            @contextmanager
            def _connection(self) -> Iterator[Any]:
                with super()._connection() as connection:
                    yield FlakyConnection(connection, self)

        with tempfile.TemporaryDirectory() as directory:
            store = FlakyStore(Path(directory) / "control.sqlite", PROJECT)
            with self.assertRaisesRegex(ControlStoreError, "commit outcome is ambiguous"):
                store.cas(0, RECORD)
            self.assertEqual("ambiguous", store.snapshot("op-1")["status"])

            existing_path = Path(directory) / "existing.sqlite"
            existing = FlakyStore(existing_path, PROJECT)
            existing.fail_next_commit = False
            existing.cas(0, RECORD)
            existing.fail_next_commit = True
            with self.assertRaisesRegex(ControlStoreError, "commit outcome is ambiguous"):
                existing.cas(1, {**RECORD, "status": "releasing", "revision": 2})
            self.assertEqual("ambiguous", existing.snapshot("op-1")["status"])
            reopened = SQLiteRollbackControlStore(existing_path, PROJECT)
            self.assertEqual("ambiguous", reopened.snapshot("op-1")["status"])
            with self.assertRaisesRegex(ControlStoreError, "requires verified engine recovery"):
                reopened.reconcile_release("op-1")

            session_store = SQLiteBarrierSessionStore(
                FlakyStore(Path(directory) / "session-control.sqlite", PROJECT)
            )
            with self.assertRaisesRegex(ControlStoreError, "commit outcome is ambiguous"):
                session_store.create(self._session_identity())
            session = session_store.snapshot()
            self.assertIsNotNone(session)
            assert session is not None
            self.assertEqual("ambiguous", session.status)

            existing_session_control = FlakyStore(
                Path(directory) / "existing-session-control.sqlite", PROJECT
            )
            existing_session_control.fail_next_commit = False
            existing_session = SQLiteBarrierSessionStore(existing_session_control)
            existing_session.create(self._session_identity())
            existing_session_control.fail_next_commit = True
            with self.assertRaisesRegex(ControlStoreError, "commit outcome is ambiguous"):
                existing_session.mark_ambiguous(1, "io-failure")
            self.assertEqual("ambiguous", existing_session.snapshot().status)  # type: ignore[union-attr]

            reconcile_control = FlakyStore(
                Path(directory) / "reconcile-session-control.sqlite", PROJECT
            )
            reconcile_control.fail_next_commit = False
            reconcile_session = SQLiteBarrierSessionStore(reconcile_control, lambda: "authority-3")
            reconcile_session.create(self._session_identity())
            reconcile_session.mark_ambiguous(1, "seed-ambiguity")
            replacement_record = dict(self._session_identity().as_record())
            replacement_record.update(
                {
                    "attempt_id": "attempt-replacement",
                    "state_revision": 4,
                    "durable_barrier_id": "barrier-replacement",
                    "fencing_token": "fence-replacement",
                }
            )
            from tools.upgrade_identity import canonical_barrier_session_digest

            replacement_record["identity_digest"] = canonical_barrier_session_digest(
                replacement_record
            )
            replacement = BarrierSessionState(
                BarrierSessionIdentity.from_record(replacement_record), "held", 1
            )
            reconcile_control.fail_next_commit = True
            with self.assertRaisesRegex(
                ControlStoreError, "reconciliation commit outcome is ambiguous"
            ):
                reconcile_session.reconcile_ambiguous(2, replacement)
            self.assertFalse(reconcile_session.operation_owned_by_current_thread)
            ambiguous = reconcile_session.snapshot()
            self.assertIsNotNone(ambiguous)
            assert ambiguous is not None
            self.assertEqual("ambiguous", ambiguous.status)
            self.assertEqual(ambiguous, reconcile_session.recover_unknown())

            recovery_control = FlakyStore(
                Path(directory) / "prepared-session-recovery-control.sqlite", PROJECT
            )
            recovery_control.fail_next_commit = False
            recovery_session = SQLiteBarrierSessionStore(recovery_control, lambda: "authority-3")
            recovery_session.create(self._session_identity())
            with closing(sqlite3.connect(recovery_control.path)) as connection:
                connection.execute(
                    "UPDATE barrier_session_intent SET outcome='prepared' WHERE project_id=?",
                    (PROJECT,),
                )
                connection.commit()
            recovery_control.fail_next_commit = True
            with self.assertRaisesRegex(ControlStoreError, "recovery commit outcome is ambiguous"):
                recovery_session.recover_unknown()
            self.assertFalse(recovery_session.operation_owned_by_current_thread)
            recovered_session = recovery_session.snapshot()
            self.assertIsNotNone(recovered_session)
            assert recovered_session is not None
            with closing(sqlite3.connect(recovery_control.path)) as connection:
                durable_recovery_row = connection.execute(
                    "SELECT status,revision FROM barrier_session WHERE project_id=?",
                    (PROJECT,),
                ).fetchone()
            self.assertEqual(("ambiguous", 2), durable_recovery_row)
            self.assertEqual(
                ("ambiguous", 2), (recovered_session.status, recovered_session.revision)
            )

            second_recovery_control = FlakyStore(
                Path(directory) / "prepared-session-second-recovery-control.sqlite", PROJECT
            )
            second_recovery_control.fail_next_commit = False
            second_recovery_session = SQLiteBarrierSessionStore(
                second_recovery_control, lambda: "authority-3"
            )
            second_recovery_session.create(self._session_identity())
            with closing(sqlite3.connect(second_recovery_control.path)) as connection:
                connection.execute(
                    "UPDATE barrier_session_intent SET outcome='prepared' WHERE project_id=?",
                    (PROJECT,),
                )
                connection.commit()
            second_recovery_control.fail_commit_after = 1
            with self.assertRaisesRegex(ControlStoreError, "recovery commit outcome is ambiguous"):
                second_recovery_session.recover_unknown()
            self.assertFalse(second_recovery_session.operation_owned_by_current_thread)
            second_recovered = second_recovery_session.snapshot()
            self.assertIsNotNone(second_recovered)
            assert second_recovered is not None
            self.assertEqual(("ambiguous", 2), (second_recovered.status, second_recovered.revision))

            effect_control = FlakyStore(
                Path(directory) / "prepared-effect-recovery-control.sqlite", PROJECT
            )
            effect_control.fail_next_commit = False
            effect_session = SQLiteBarrierSessionStore(effect_control, lambda: "authority-3")
            effect_session.create(self._session_identity())
            effect_session.prepare_authority_effect(1, "effect-recovery", "sqlite")
            effect_control.fail_next_commit = True
            with self.assertRaisesRegex(ControlStoreError, "recovery commit outcome is ambiguous"):
                effect_session.recover_unknown()
            self.assertFalse(effect_session.operation_owned_by_current_thread)
            recovered_effect = effect_session.snapshot()
            self.assertIsNotNone(recovered_effect)
            assert recovered_effect is not None
            self.assertEqual(("ambiguous", 2), (recovered_effect.status, recovered_effect.revision))
            with closing(sqlite3.connect(effect_control.path)) as connection:
                self.assertEqual(
                    [("ambiguous",)],
                    connection.execute(
                        "SELECT outcome FROM authority_effect_intent WHERE project_id=?",
                        (PROJECT,),
                    ).fetchall(),
                )

            finish_control = FlakyStore(Path(directory) / "finish-effect-control.sqlite", PROJECT)
            finish_control.fail_next_commit = False
            finish_session = SQLiteBarrierSessionStore(finish_control, lambda: "authority-3")
            finish_session.create(self._session_identity())
            finish_intent = finish_session.prepare_authority_effect(1, "effect-finish", "sqlite")
            finish_control.fail_next_commit = True
            with self.assertRaisesRegex(
                ControlStoreError, "authority effect outcome publication is ambiguous"
            ):
                finish_session.finish_authority_effect(finish_intent, "committed")
            self.assertFalse(finish_session.operation_owned_by_current_thread)
            finished = finish_session.snapshot()
            self.assertIsNotNone(finished)
            assert finished is not None
            self.assertEqual(("ambiguous", 2), (finished.status, finished.revision))
            with closing(sqlite3.connect(finish_control.path)) as connection:
                self.assertEqual(
                    [("ambiguous",)],
                    connection.execute(
                        "SELECT outcome FROM authority_effect_intent WHERE project_id=?",
                        (PROJECT,),
                    ).fetchall(),
                )

            publication_control = FlakyStore(
                Path(directory) / "session-publication-control.sqlite", PROJECT
            )
            publication_control.fail_next_commit = False
            publication_session = SQLiteBarrierSessionStore(
                publication_control, lambda: "authority-3"
            )
            publication_identity = self._session_identity()
            publication_session.create(publication_identity)
            publication_session.bind_child(
                1, BarrierChildIdentity.bind(publication_identity, "publication-child", "new")
            )
            publication_control.fail_commit_after = 1
            with self.assertRaisesRegex(
                ControlStoreError, "barrier session outcome publication is ambiguous"
            ):
                publication_session.begin_reopen(
                    2, "new", _reopen_evidence(publication_session.snapshot(), "new")
                )
            self.assertFalse(publication_session.operation_owned_by_current_thread)
            publication_state = publication_session.snapshot()
            self.assertIsNotNone(publication_state)
            assert publication_state is not None
            self.assertEqual(
                ("ambiguous", 4), (publication_state.status, publication_state.revision)
            )
            self.assertEqual("new", publication_state.reopen_target)
            restarted_publication = SQLiteBarrierSessionStore(
                SQLiteRollbackControlStore(
                    publication_control.path,
                    PROJECT,
                ),
                lambda: "authority-3",
            ).snapshot()
            self.assertIsNotNone(restarted_publication)
            assert restarted_publication is not None
            self.assertEqual("new", restarted_publication.reopen_target)

    def test_v10_reopen_competing_owner_cannot_replace_persisted_target(self) -> None:
        from tools.upgrade_identity import BarrierChildIdentity

        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "control.sqlite"
            first = SQLiteBarrierSessionStore(
                SQLiteRollbackControlStore(path, PROJECT), lambda: "authority-3"
            )
            second = SQLiteBarrierSessionStore(
                SQLiteRollbackControlStore(path, PROJECT), lambda: "authority-3"
            )
            identity = self._session_identity()
            held = first.create(identity)
            held = first.bind_child(1, BarrierChildIdentity.bind(identity, "forward-1", "new"))
            held = first.bind_child(
                2, BarrierChildIdentity.bind(identity, "rollback-1", "rollback")
            )
            stale_owner = second.snapshot()
            self.assertIsNotNone(stale_owner)
            assert stale_owner is not None
            winner = first.begin_reopen(3, "rollback", _reopen_evidence(held, "rollback"))
            self.assertEqual("rollback", winner.reopen_target)
            with self.assertRaisesRegex(ControlStoreError, "revision conflict"):
                second.begin_reopen(
                    stale_owner.revision,
                    "new",
                    _reopen_evidence(stale_owner, "new"),
                )
            persisted = second.snapshot()
            self.assertIsNotNone(persisted)
            assert persisted is not None
            self.assertEqual(("releasing", "rollback"), (persisted.status, persisted.reopen_target))

    def test_v10_cas_fences_verify_affected_rows_and_recovery_errors(self) -> None:
        class Cursor:
            def __init__(self, rowcount: int) -> None:
                self.rowcount = rowcount

        class Connection:
            def __init__(self, selected: object, update_count: int = 0) -> None:
                self.selected = selected
                self.update_count = update_count
                self.statements = 0

            def execute(self, sql: str, *_args: object) -> Any:
                if "SELECT MAX" in sql:
                    return type("Result", (), {"fetchone": lambda _self: (None,)})()
                self.statements += 1
                if "SELECT" in sql:
                    return type("Result", (), {"fetchone": lambda _self: self.selected})()
                return Cursor(self.update_count)

            def rollback(self) -> None:
                return None

            def commit(self) -> None:
                return None

        with tempfile.TemporaryDirectory() as directory:
            store = SQLiteRollbackControlStore(Path(directory) / "control.sqlite", PROJECT)
            store._operation_owner = threading.get_ident()
            try:
                insert_connection = Connection(None)
                with self.assertRaisesRegex(ControlStoreError, "insert lost"):
                    store._cas_connection(cast(Any, insert_connection), 0, dict(RECORD))
                current_row = (*tuple(RECORD[field] for field in IDENTITY_FIELDS), "held", 1)
                update_connection = Connection(current_row)
                with self.assertRaisesRegex(ControlStoreError, "update lost"):
                    store._cas_connection(
                        cast(Any, update_connection),
                        1,
                        {**RECORD, "status": "releasing", "revision": 2},
                    )
                with self.assertRaisesRegex(ControlStoreError, "could not be durably fenced"):
                    SQLiteRollbackControlStore._mark_ambiguous_after_commit_failure(
                        cast(Any, Connection(current_row, update_count=0)),
                        RECORD,
                        1,
                        OSError("commit uncertain"),
                    )
            finally:
                store._operation_owner = None

    def test_v10_session_cas_fences_insert_and_update_rows(self) -> None:  # noqa: C901
        class Result:
            def __init__(self, value: object) -> None:
                self.value = value

            def fetchone(self) -> object:
                return self.value

        class SessionControl:
            project_id = PROJECT
            operation_owned_by_current_thread = True

            def __init__(self, selected: object) -> None:
                self.selected = selected

            def _require_operation_lock(self) -> None:
                return None

            @contextmanager
            def _connection(self) -> Iterator[Any]:
                yield connection

        identity = self._session_identity()
        current_row = (*tuple(identity.as_record().values()), "held", 1, None, None)
        for selected, state, expected, message in (
            (None, BarrierSessionState(identity, "held", 1), 0, "update lost"),
            (current_row, BarrierSessionState(identity, "releasing", 2), 1, "update lost"),
        ):
            with self.subTest(selected=selected):

                class Cursor:
                    rowcount = 0

                class Connection:
                    def __init__(self, selected: object) -> None:
                        self.selected = selected

                    def execute(self, sql: str, *_args: object) -> Any:
                        if "SELECT" in sql:
                            return Result(self.selected)
                        return Cursor()

                    def rollback(self) -> None:
                        return None

                    def commit(self) -> None:
                        return None

                connection = Connection(selected)
                store = SQLiteBarrierSessionStore(cast(Any, SessionControl(selected)))
                with self.assertRaisesRegex(ControlStoreError, message):
                    store._cas_locked(expected, state)

    def test_v10_durable_session_starts_fresh_attempt_after_release(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "control.sqlite"
            control = SQLiteRollbackControlStore(path, PROJECT)
            store = SQLiteBarrierSessionStore(control)
            first = self._session_identity()
            store.create(first)
            from tools.upgrade_identity import canonical_barrier_session_digest

            record = dict(first.as_record())
            record["attempt_id"] = "attempt-2"
            record["state_revision"] = 4
            record["durable_barrier_id"] = "barrier-2"
            record["fencing_token"] = "fence-2"  # noqa: S105
            record["identity_digest"] = canonical_barrier_session_digest(record)
            second = BarrierSessionIdentity.from_record(record)
            store.bind_child(1, BarrierChildIdentity.bind(first, "forward-1", "new"))
            store.begin_reopen(2, "new", _reopen_evidence(store.snapshot(), "new"))
            store.complete_reopen(3, _runtime_evidence(store.snapshot(), "new"))
            fresh = store.create(second)
            self.assertEqual(("held", 1), (fresh.status, fresh.revision))
            self.assertEqual(second, store.snapshot().identity)  # type: ignore[union-attr]
            with closing(sqlite3.connect(path)) as connection:
                archived = connection.execute(
                    "SELECT count(*) FROM barrier_session_history "
                    "WHERE project_id=? AND attempt_id=?",
                    (PROJECT, first.attempt_id),
                ).fetchone()[0]
            self.assertEqual(1, archived)

    def test_v10_durable_session_rejects_stale_identity_and_ambiguous_reopen(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            store = SQLiteBarrierSessionStore(
                SQLiteRollbackControlStore(Path(directory) / "control.sqlite", PROJECT)
            )
            identity = self._session_identity()
            held = store.create(identity)
            with self.assertRaisesRegex(ControlStoreError, "CAS conflict"):
                store.cas(0, held)
            ambiguous = store.mark_ambiguous(1, "io-failure")
            self.assertEqual("ambiguous", ambiguous.status)
            with self.assertRaisesRegex(ControlStoreError, "illegal barrier session transition"):
                store.cas(2, BarrierSessionState(identity, "held", 3))
            changed = dict(identity.as_record())
            changed["fencing_token"] = "different-fence"  # noqa: S105
            from tools.upgrade_identity import canonical_barrier_session_digest

            changed["identity_digest"] = canonical_barrier_session_digest(changed)
            replacement = identity.__class__.from_record(changed)
            with self.assertRaisesRegex(ControlStoreError, "identity changed"):
                store.cas(2, BarrierSessionState(replacement, "ambiguous", 3))

    def test_v10_durable_session_requires_runtime_evidence_before_release(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            store = SQLiteBarrierSessionStore(
                SQLiteRollbackControlStore(Path(directory) / "control.sqlite", PROJECT)
            )
            identity = self._session_identity()
            store.create(identity)
            from tools.upgrade_identity import BarrierChildIdentity

            store.bind_child(1, BarrierChildIdentity.bind(identity, "forward-1", "new"))
            with self.assertRaisesRegex(ControlStoreError, "verified child evidence"):
                store.begin_reopen(2, "new")
            with self.assertRaisesRegex(ControlStoreError, "evidence identity"):
                store.begin_reopen(
                    2,
                    "new",
                    {
                        "operation_id": "wrong-child",
                        "target": "new",
                        "barrier_identity_digest": identity.identity_digest,
                        "validated": True,
                    },
                )
            store.begin_reopen(2, "new", _reopen_evidence(store.snapshot(), "new"))
            invalid_runtime = _runtime_evidence(store.snapshot(), "new")
            invalid_runtime["fencing_token"] = "stale-fence"  # noqa: S105
            with self.assertRaisesRegex(ControlStoreError, "runtime evidence identity"):
                store.complete_reopen(3, invalid_runtime)
            with self.assertRaisesRegex(ControlStoreError, "runtime evidence"):
                store.complete_reopen(3, None)

    def test_v10_durable_session_uses_common_then_control_lock(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            control = SQLiteRollbackControlStore(Path(directory) / "control.sqlite", PROJECT)
            store = SQLiteBarrierSessionStore(control)
            with (
                control.operation_lock(),
                self.assertRaisesRegex(ControlStoreError, "non-reentrant"),
            ):
                store.snapshot()

    def test_v10_durable_session_rejects_invalid_public_and_durable_inputs(self) -> None:
        from tools.upgrade_identity import BarrierChildIdentity

        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "control.sqlite"
            control = SQLiteRollbackControlStore(path, PROJECT)
            store = SQLiteBarrierSessionStore(control)
            identity = self._session_identity()
            with self.assertRaisesRegex(ControlStoreError, "expected revision"):
                store.cas(False, BarrierSessionState(identity, "held", 1))
            with self.assertRaisesRegex(ControlStoreError, "must start held"):
                store.cas(0, BarrierSessionState(identity, "released", 1))
            with self.assertRaisesRegex(ControlStoreError, "does not exist"):
                store.cas(1, BarrierSessionState(identity, "held", 1))
            with self.assertRaisesRegex(ControlStoreError, "absent"):
                store.bind_child(1, BarrierChildIdentity.bind(identity, "forward-1", "new"))
            with self.assertRaisesRegex(ControlStoreError, "absent"):
                store.begin_reopen(1, "new")
            with self.assertRaisesRegex(ControlStoreError, "absent"):
                store.mark_ambiguous(1, "io-failure")
            self.assertIsNone(store.snapshot())

            held = store.create(identity)
            with self.assertRaisesRegex(ControlStoreError, "revision is not monotonic"):
                store.cas(1, BarrierSessionState(identity, "held", 7))
            with self.assertRaisesRegex(ControlStoreError, "revision is not monotonic"):
                store.cas(1, BarrierSessionState(identity, "held", 1))
            child = BarrierChildIdentity.bind(identity, "forward-1", "new")
            with self.assertRaisesRegex(ControlStoreError, "revision conflict"):
                store.bind_child(0, child)
            with self.assertRaisesRegex(ControlStoreError, "invalid"):
                SQLiteBarrierSessionStore._child(17)
            with self.assertRaisesRegex(ControlStoreError, "invalid"):
                SQLiteBarrierSessionStore._child("{")
            with self.assertRaisesRegex(ControlStoreError, "invalid"):
                SQLiteBarrierSessionStore._child("[]")
            with self.assertRaisesRegex(ControlStoreError, "invalid"):
                SQLiteBarrierSessionStore._child('{"operation_id":1}')

            with closing(sqlite3.connect(path)) as connection:
                connection.execute(
                    "UPDATE barrier_session SET forward_child=? WHERE project_id=?",
                    ("[]", PROJECT),
                )
                connection.commit()
            with self.assertRaisesRegex(ControlStoreError, "state is invalid"):
                store.snapshot()
            self.assertEqual(1, held.revision)

    def test_v10_durable_session_rejects_identity_and_lock_conflicts(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            control = SQLiteRollbackControlStore(Path(directory) / "control.sqlite", PROJECT)
            store = SQLiteBarrierSessionStore(control)
            identity = self._session_identity()
            held = store.create(identity)
            changed = dict(identity.as_record())
            changed["attempt_id"] = "different-attempt"
            from tools.upgrade_identity import canonical_barrier_session_digest

            changed["identity_digest"] = canonical_barrier_session_digest(changed)
            other = BarrierSessionIdentity.from_record(changed)
            with self.assertRaisesRegex(ControlStoreError, "identity changed"):
                store.cas(1, BarrierSessionState(other, "held", 2))
            with (
                control.operation_lock(),
                self.assertRaisesRegex(ControlStoreError, "non-reentrant"),
            ):
                store.cas(1, held)

    def test_v10_barrier_session_contract_keeps_forward_and_rollback_under_one_fence(self) -> None:
        from tools.upgrade_identity import BarrierChildIdentity, BarrierSessionIdentity

        session_record = {
            "schema_version": 1,
            "project_id": PROJECT,
            "attempt_id": "attempt-1",
            "state_revision": 3,
            "authority_revision_at_acquire": "authority-3",
            "durable_barrier_id": "barrier-1",
            "fencing_token": "fence-1",
            "fencing_owner": "owner-1",
            "identity_digest": "0" * 64,
        }
        from tools.upgrade_identity import canonical_barrier_session_digest

        session_record["identity_digest"] = canonical_barrier_session_digest(session_record)
        identity = BarrierSessionIdentity.from_record(session_record)
        contract = BarrierSessionContract(identity)
        self.assertIsInstance(contract.state, BarrierSessionState)
        forward = BarrierChildIdentity.bind(identity, "forward-1", "new")
        rollback = BarrierChildIdentity.bind(identity, "rollback-1", "rollback")
        held = contract.bind_child(1, forward)
        self.assertEqual("held", contract.recheck_held(held.revision).status)
        held = contract.bind_child(held.revision, rollback)
        releasing = contract.begin_reopen(
            held.revision, "rollback", _reopen_evidence(held, "rollback")
        )
        released = contract.complete_reopen(
            releasing.revision, _runtime_evidence(releasing, "rollback")
        )
        self.assertEqual("released", released.status)
        self.assertEqual("fence-1", released.identity.fencing_token)
        with self.assertRaisesRegex(ControlStoreError, "transition"):
            contract.mark_ambiguous(released.revision, "io-failure")

    def test_v10_barrier_session_contract_rejects_stale_and_unsafe_transitions(self) -> None:
        from tools.upgrade_identity import BarrierChildIdentity, BarrierSessionIdentity

        record = {
            "schema_version": 1,
            "project_id": PROJECT,
            "attempt_id": "attempt-1",
            "state_revision": 1,
            "authority_revision_at_acquire": "authority-1",
            "durable_barrier_id": "barrier-1",
            "fencing_token": "fence-1",
            "fencing_owner": "owner-1",
            "identity_digest": "0" * 64,
        }
        from tools.upgrade_identity import canonical_barrier_session_digest

        record["identity_digest"] = canonical_barrier_session_digest(record)
        identity = BarrierSessionIdentity.from_record(record)
        contract = BarrierSessionContract(identity)
        with self.assertRaisesRegex(ControlStoreError, "revision conflict"):
            contract.recheck_held(0)
        with self.assertRaisesRegex(ControlStoreError, "rollback child"):
            contract.bind_child(1, BarrierChildIdentity.bind(identity, "rollback-1", "rollback"))
        forward = contract.bind_child(1, BarrierChildIdentity.bind(identity, "forward-1", "new"))
        with self.assertRaisesRegex(ControlStoreError, "already bound"):
            contract.bind_child(
                forward.revision, BarrierChildIdentity.bind(identity, "forward-2", "new")
            )
        with self.assertRaisesRegex(ControlStoreError, "runtime evidence"):
            releasing = contract.begin_reopen(
                forward.revision, "new", _reopen_evidence(forward, "new")
            )
            contract.complete_reopen(releasing.revision, None)

    def test_v10_barrier_session_contract_enters_ambiguous_safe_mode(self) -> None:
        from tools.upgrade_identity import BarrierSessionIdentity, canonical_barrier_session_digest

        record = {
            "schema_version": 1,
            "project_id": PROJECT,
            "attempt_id": "attempt-2",
            "state_revision": 2,
            "authority_revision_at_acquire": "authority-2",
            "durable_barrier_id": "barrier-2",
            "fencing_token": "fence-2",
            "fencing_owner": "owner-2",
            "identity_digest": "0" * 64,
        }
        record["identity_digest"] = canonical_barrier_session_digest(record)
        contract = BarrierSessionContract(BarrierSessionIdentity.from_record(record))
        with self.assertRaisesRegex(ControlStoreError, "cause code"):
            contract.mark_ambiguous(1, "bad cause")
        ambiguous = contract.mark_ambiguous(1, "io-failure")
        self.assertEqual("ambiguous", ambiguous.status)
        with self.assertRaisesRegex(ControlStoreError, "transition"):
            contract.recheck_held(ambiguous.revision)

    def test_v10_barrier_session_state_rejects_invalid_shape(self) -> None:
        from tools.upgrade_identity import BarrierSessionIdentity, canonical_barrier_session_digest

        record = {
            "schema_version": 1,
            "project_id": PROJECT,
            "attempt_id": "attempt-3",
            "state_revision": 3,
            "authority_revision_at_acquire": "authority-3",
            "durable_barrier_id": "barrier-3",
            "fencing_token": "fence-3",
            "fencing_owner": "owner-3",
            "identity_digest": "0" * 64,
        }
        record["identity_digest"] = canonical_barrier_session_digest(record)
        identity = BarrierSessionIdentity.from_record(record)
        with self.assertRaisesRegex(ControlStoreError, "status"):
            BarrierSessionState(identity, "invalid", 1)
        with self.assertRaisesRegex(ControlStoreError, "revision"):
            BarrierSessionState(identity, "held", 0)

    def test_v10_barrier_session_rejects_duplicate_children_and_reopen_edges(self) -> None:
        from tools.upgrade_identity import BarrierChildIdentity, BarrierSessionIdentity

        record = {
            "schema_version": 1,
            "project_id": PROJECT,
            "attempt_id": "attempt-4",
            "state_revision": 1,
            "authority_revision_at_acquire": "authority-4",
            "durable_barrier_id": "barrier-4",
            "fencing_token": "fence-4",
            "fencing_owner": "owner-4",
            "identity_digest": "0" * 64,
        }
        from tools.upgrade_identity import canonical_barrier_session_digest

        record["identity_digest"] = canonical_barrier_session_digest(record)
        identity = BarrierSessionIdentity.from_record(record)
        forward = BarrierChildIdentity.bind(identity, "same-child", "new")
        rollback = BarrierChildIdentity.bind(identity, "same-child", "rollback")
        with self.assertRaisesRegex(ControlStoreError, "distinct"):
            BarrierSessionState(identity, "held", 1, forward, rollback)

        contract = BarrierSessionContract(identity)
        with self.assertRaisesRegex(ControlStoreError, "target"):
            contract.begin_reopen(1, "invalid")
        with self.assertRaisesRegex(ControlStoreError, "not bound"):
            contract.begin_reopen(1, "new")
        held = contract.bind_child(1, forward)
        rollback = BarrierChildIdentity.bind(identity, "rollback-child", "rollback")
        releasing = contract.bind_child(held.revision, rollback)
        with self.assertRaisesRegex(ControlStoreError, "already bound"):
            contract.bind_child(
                releasing.revision,
                BarrierChildIdentity.bind(identity, "rollback-2", "rollback"),
            )

    def test_canonical_barrier_digest_is_stable_and_excludes_mutable_fields(self) -> None:
        first = canonical_barrier_digest(RECORD)
        second = canonical_barrier_digest({**RECORD, "status": "ambiguous", "revision": 99})
        self.assertEqual(first, second)
        self.assertEqual(64, len(first))

    def test_binding_is_sqlite_only_and_store_owned(self) -> None:
        class Delegate:
            def snapshot(self, _phase: str, _context: Mapping[str, object]) -> Mapping[str, object]:
                return {}

            def execute(self, _phase: str, _context: Mapping[str, object]) -> Mapping[str, object]:
                return {}

        with tempfile.TemporaryDirectory() as directory:
            store = SQLiteRollbackControlStore(Path(directory) / "control.sqlite", PROJECT)
            with self.assertRaises(ControlStoreError):
                bind_control_store("sqlite", Delegate(), store)
            authority = Path(directory) / "authority.sqlite"
            authority.touch()
            bound = SQLiteRollbackControlStore(Path(directory) / "bound.sqlite", PROJECT, authority)
            with self.assertRaisesRegex(ControlStoreError, "authority/runtime rereader"):
                bind_control_store("sqlite", Delegate(), bound)
            self.assertIsInstance(
                bind_control_store("sqlite", Delegate(), bound, StaticAuthorityRuntimeRereader()),
                SQLiteControlStoreAdapter,
            )
            with self.assertRaises(ControlStoreError):
                bind_control_store("git", Delegate(), None, StaticAuthorityRuntimeRereader())

    def test_concrete_release_rereader_derives_and_rechecks_actual_authority(self) -> None:
        class Delegate:
            def snapshot(self, _phase: str, _context: Mapping[str, object]) -> Mapping[str, object]:
                return {}

            def execute(self, _phase: str, _context: Mapping[str, object]) -> Mapping[str, object]:
                return {}

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            authority, project_binding, backend_selector, runtime_selector = (
                create_release_authority(root)
            )
            first = inspect_sqlite_release_authority(
                authority,
                project_binding,
                backend_selector,
                runtime_selector,
                PROJECT,
                "release-old",
                "release-older",
            )
            second = inspect_sqlite_release_authority(
                authority,
                project_binding,
                backend_selector,
                runtime_selector,
                PROJECT,
                "release-old",
                "release-older",
            )
            self.assertEqual(first.authority_revision, second.authority_revision)
            self.assertEqual("ok", first.integrity_check)
            self.assertEqual(0, first.foreign_key_violations)

            record = dict(RECORD)
            record["authority_revision"] = first.authority_revision
            record["barrier_identity_digest"] = canonical_barrier_digest(record)
            record["envelope_digest"] = canonical_envelope_digest(record)
            control_root = root / "control"
            control_root.mkdir(mode=0o700)
            store = SQLiteRollbackControlStore(control_root / "barrier.sqlite", PROJECT, authority)
            store.cas(0, record)
            rereader = SQLiteAuthorityRuntimeRereader(
                authority,
                project_binding,
                backend_selector,
                runtime_selector,
                active_release="release-old",
                previous_release="release-older",
            )
            with self.assertRaisesRegex(ControlStoreError, "release-specific"):
                SQLiteAuthorityRuntimeRereader(
                    authority,
                    project_binding,
                    backend_selector,
                    runtime_selector,
                    active_release="",
                    previous_release="release-older",
                )
            adapter = SQLiteControlStoreAdapter(Delegate(), store, rereader)
            context = {field: record[field] for field in IDENTITY_FIELDS}
            with adapter.operation_lock():
                adapter.begin_release_rollback_context(context)

            reopened_store = SQLiteRollbackControlStore(
                control_root / "barrier.sqlite", PROJECT, authority
            )
            reopened_adapter = SQLiteControlStoreAdapter(Delegate(), reopened_store, rereader)
            with reopened_adapter.operation_lock():
                self.assertEqual(
                    RELEASE_EVIDENCE,
                    reopened_adapter.revalidate_rollback(context, RELEASE_EVIDENCE),
                )
                self.assertEqual(
                    "released",
                    reopened_adapter.complete_release_rollback_context(context)["status"],
                )

            backend = SQLiteBackend(authority, AUTHORITY_BINDING, root / "tasks")
            backend.append_command_result(
                "AR-0001",
                "worker",
                "b" * 64,
                0,
                "completed",
                "2026-09-14T00:01:00+00:00",
            )
            changed = inspect_sqlite_release_authority(
                authority,
                project_binding,
                backend_selector,
                runtime_selector,
                PROJECT,
                "release-old",
                "release-older",
            )
            self.assertNotEqual(first.authority_revision, changed.authority_revision)
            stale_store = SQLiteRollbackControlStore(
                control_root / "stale.sqlite", PROJECT, authority
            )
            stale_store.cas(0, record)
            stale_adapter = SQLiteControlStoreAdapter(Delegate(), stale_store, rereader)
            with stale_adapter.operation_lock():
                stale_adapter.begin_release_rollback_context(context)
                with self.assertRaisesRegex(ControlStoreError, "reread is invalid"):
                    stale_adapter.revalidate_rollback(context, RELEASE_EVIDENCE)

    def test_concrete_release_rereader_rejects_selector_and_projection_tamper(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            authority, project_binding, backend_selector, runtime_selector = (
                create_release_authority(root)
            )
            for path, value, message in (
                (
                    backend_selector,
                    {"schema_version": 1, "project_id": PROJECT, "backend": "git"},
                    "backend selector identity",
                ),
                (
                    runtime_selector,
                    {
                        "schema_version": 1,
                        "active_release": "release-new",
                        "previous_release": "release-old",
                    },
                    "runtime selector release identity",
                ),
            ):
                original = path.read_text()
                path.write_text(json.dumps(value) + "\n")
                with self.subTest(path=path), self.assertRaisesRegex(AuthorityError, message):
                    inspect_sqlite_release_authority(
                        authority,
                        project_binding,
                        backend_selector,
                        runtime_selector,
                        PROJECT,
                        "release-old",
                        "release-older",
                    )
                path.write_text(original)

            connection = sqlite3.connect(authority)
            connection.execute("PRAGMA ignore_check_constraints=ON")
            connection.execute("UPDATE tasks SET revision=2 WHERE id='AR-0001'")
            connection.commit()
            connection.close()
            with self.assertRaisesRegex(AuthorityError, "task projections disagree"):
                inspect_sqlite_release_authority(
                    authority,
                    project_binding,
                    backend_selector,
                    runtime_selector,
                    PROJECT,
                    "release-old",
                    "release-older",
                )

    def test_concrete_release_rereader_rejects_selector_alias(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            authority, project_binding, backend_selector, runtime_selector = (
                create_release_authority(root)
            )
            selector_target = root / "selector-target.json"
            selector_target.write_text(runtime_selector.read_text())
            runtime_selector.unlink()
            runtime_selector.symlink_to(selector_target)
            with self.assertRaises(AuthorityError):
                inspect_sqlite_release_authority(
                    authority,
                    project_binding,
                    backend_selector,
                    runtime_selector,
                    PROJECT,
                    "release-old",
                    "release-older",
                )

    def test_release_authority_refuses_missing_nonregular_and_oversized_inputs(self) -> None:
        with self.assertRaisesRegex(AuthorityError, "canonical and absolute"):
            read_runtime_selector(Path("relative-selector.json"))
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with self.assertRaisesRegex(AuthorityError, "parent descriptor"):
                read_runtime_selector(root / "missing" / "selector.json")

            authority, project_binding, backend_selector, runtime_selector = (
                create_release_authority(root)
            )
            project_binding.write_bytes(b"x" * (64 * 1024 + 1))
            with self.assertRaisesRegex(AuthorityError, "project binding is too large"):
                inspect_sqlite_release_authority(
                    authority,
                    project_binding,
                    backend_selector,
                    runtime_selector,
                    PROJECT,
                    "release-old",
                    "release-older",
                )

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            authority, project_binding, backend_selector, runtime_selector = (
                create_release_authority(root)
            )
            target = root / "binding-target"
            target.write_text(project_binding.read_text())
            project_binding.unlink()
            os.link(target, project_binding)
            with self.assertRaisesRegex(AuthorityError, "private regular file"):
                inspect_sqlite_release_authority(
                    authority,
                    project_binding,
                    backend_selector,
                    runtime_selector,
                    PROJECT,
                    "release-old",
                    "release-older",
                )

    def test_release_authority_refuses_binding_schema_and_database_corruption(self) -> None:
        corruptions: tuple[Callable[[Path, Path, Path, Path], object], ...] = (
            lambda _authority, binding, _backend, _runtime: binding.write_text("[]\n"),
            lambda _authority, binding, _backend, _runtime: binding.write_text("not-json\n"),
            lambda _authority, binding, _backend, _runtime: binding.write_text(
                json.dumps({**AUTHORITY_BINDING, "project_id": "foreign"}) + "\n"
            ),
            lambda _authority, _binding, _backend, runtime: runtime.write_text(
                json.dumps(
                    {"schema_version": 2, "active_release": "old", "previous_release": "older"}
                )
                + "\n"
            ),
            lambda authority, _binding, _backend, _runtime: authority.write_bytes(b"not-sqlite"),
        )
        for index, corrupt in enumerate(corruptions):
            with self.subTest(index=index), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                paths = create_release_authority(root)
                corrupt(*paths)
                with self.assertRaises(AuthorityError):
                    inspect_sqlite_release_authority(
                        paths[0],
                        paths[1],
                        paths[2],
                        paths[3],
                        PROJECT,
                        "release-old",
                        "release-older",
                    )

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            authority, project_binding, backend_selector, runtime_selector = (
                create_release_authority(root)
            )
            connection = sqlite3.connect(authority)
            connection.execute("CREATE TABLE unexpected(value TEXT)")
            connection.commit()
            connection.close()
            with self.assertRaisesRegex(AuthorityError, "authority schema"):
                inspect_sqlite_release_authority(
                    authority,
                    project_binding,
                    backend_selector,
                    runtime_selector,
                    PROJECT,
                    "release-old",
                    "release-older",
                )

    def test_release_authority_detects_authority_selector_and_sidecar_swaps(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            authority, project_binding, backend_selector, runtime_selector = (
                create_release_authority(root)
            )
            original_rows = upgrade_authority._authority_rows

            def swap_selector(connection: sqlite3.Connection) -> dict[str, object]:
                rows = original_rows(connection)
                commit_runtime_selector(runtime_selector, "release-new", "release-old")
                return rows

            with (
                patch.object(upgrade_authority, "_authority_rows", side_effect=swap_selector),
                self.assertRaisesRegex(AuthorityError, "selector identity changed"),
            ):
                inspect_sqlite_release_authority(
                    authority,
                    project_binding,
                    backend_selector,
                    runtime_selector,
                    PROJECT,
                    "release-old",
                    "release-older",
                )

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            authority, project_binding, backend_selector, runtime_selector = (
                create_release_authority(root)
            )
            original_sidecars = upgrade_authority._sidecar_identities
            calls = 0

            def swap_sidecar(parent: int, name: str) -> dict[str, tuple[int, int] | None]:
                nonlocal calls
                identities = original_sidecars(parent, name)
                calls += 1
                if calls == 2:
                    wal = Path(f"{authority}-wal")
                    wal.rename(Path(f"{authority}-previous-wal"))
                    wal.touch()
                return identities

            with (
                patch.object(upgrade_authority, "_sidecar_identities", side_effect=swap_sidecar),
                self.assertRaisesRegex(AuthorityError, "sidecar identity changed"),
            ):
                inspect_sqlite_release_authority(
                    authority,
                    project_binding,
                    backend_selector,
                    runtime_selector,
                    PROJECT,
                    "release-old",
                    "release-older",
                )

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            authority, project_binding, backend_selector, runtime_selector = (
                create_release_authority(root)
            )
            replacement = root / ".runtime" / "replacement.sqlite3"
            replacement.write_bytes(authority.read_bytes())
            original_rows = upgrade_authority._authority_rows

            def swap_after_read(connection: sqlite3.Connection) -> dict[str, object]:
                rows = original_rows(connection)
                authority.rename(root / ".runtime" / "previous.sqlite3")
                replacement.rename(authority)
                return rows

            with (
                patch.object(upgrade_authority, "_authority_rows", side_effect=swap_after_read),
                self.assertRaisesRegex(AuthorityError, "authority file identity changed"),
            ):
                inspect_sqlite_release_authority(
                    authority,
                    project_binding,
                    backend_selector,
                    runtime_selector,
                    PROJECT,
                    "release-old",
                    "release-older",
                )

    def test_adapter_release_api_fails_closed_without_scope_and_authority_evidence(self) -> None:
        class Delegate:
            def snapshot(self, _phase: str, _context: Mapping[str, object]) -> Mapping[str, object]:
                return {}

            def execute(self, _phase: str, _context: Mapping[str, object]) -> Mapping[str, object]:
                return {}

        class InvalidRereader:
            def reread_rollback(
                self, _context: Mapping[str, object], _result: Mapping[str, object]
            ) -> SQLiteAuthorityRuntimeState:
                return cast(SQLiteAuthorityRuntimeState, None)

        class RaisingRereader:
            def reread_rollback(
                self, _context: Mapping[str, object], _result: Mapping[str, object]
            ) -> SQLiteAuthorityRuntimeState:
                raise RuntimeError("reread failed")

        with tempfile.TemporaryDirectory() as directory:
            authority = Path(directory) / "authority.sqlite"
            authority.touch()
            store = SQLiteRollbackControlStore(
                Path(directory) / "control.sqlite", PROJECT, authority
            )
            store.cas(0, RECORD)
            context = {field: RECORD[field] for field in IDENTITY_FIELDS}
            with self.assertRaisesRegex(ControlStoreError, "authority/runtime rereader"):
                SQLiteControlStoreAdapter(Delegate(), store)
            adapter = SQLiteControlStoreAdapter(Delegate(), store, StaticAuthorityRuntimeRereader())
            self.assertEqual({}, adapter.snapshot("discover", context))
            self.assertEqual({}, adapter.execute("discover", context))
            outside_verification = adapter.verify_rollback_context(context)
            self.assertIsNotNone(outside_verification)
            assert outside_verification is not None
            self.assertEqual("held", outside_verification["status"])
            with self.assertRaises(ControlStoreError):
                adapter.begin_release_rollback_context(context)
            with self.assertRaises(ControlStoreError):
                adapter.complete_release_rollback_context(context)
            with self.assertRaises(ControlStoreError):
                adapter.revalidate_rollback(context, RELEASE_EVIDENCE)
            with adapter.operation_lock():
                inside_verification = adapter.verify_rollback_context(context)
                self.assertIsNotNone(inside_verification)
                assert inside_verification is not None
                self.assertEqual("held", inside_verification["status"])
                adapter.begin_release_rollback_context(context)
                with self.assertRaises(ControlStoreError):
                    adapter.complete_release_rollback_context(context)
            with self.assertRaisesRegex(ControlStoreError, "outer operation lock"):
                adapter.revalidate_rollback(context, RELEASE_EVIDENCE)

            invalid_states = (
                {"backend": "git"},
                {"project_id": OTHER_PROJECT},
                {"authority_revision": "changed"},
                {"fencing_token": "stale"},
                {"target": "new"},
                {"integrity_check": "failed"},
                {"foreign_key_violations": 1},
                {"foreign_key_violations": False},
                {"backend_roundtrip": "git"},
            )
            rereaders: tuple[AuthorityRuntimeRereader, ...] = (
                *(StaticAuthorityRuntimeRereader(**changes) for changes in invalid_states),
                InvalidRereader(),
                RaisingRereader(),
            )
            for index, rereader in enumerate(rereaders):
                with self.subTest(rereader=rereader):
                    invalid_store = SQLiteRollbackControlStore(
                        Path(directory) / f"invalid-{index}.sqlite", PROJECT, authority
                    )
                    invalid_store.cas(0, RECORD)
                    invalid_adapter = SQLiteControlStoreAdapter(Delegate(), invalid_store, rereader)
                    with invalid_adapter.operation_lock():
                        invalid_adapter.begin_release_rollback_context(context)
                        with self.assertRaises(ControlStoreError):
                            invalid_adapter.revalidate_rollback(context, RELEASE_EVIDENCE)

            valid_store = SQLiteRollbackControlStore(
                Path(directory) / "valid.sqlite", PROJECT, authority
            )
            valid_store.cas(0, RECORD)
            valid_adapter = SQLiteControlStoreAdapter(
                Delegate(), valid_store, StaticAuthorityRuntimeRereader()
            )
            with valid_adapter.operation_lock():
                valid_adapter.begin_release_rollback_context(context)
                with self.assertRaises(ControlStoreError):
                    valid_adapter.revalidate_rollback(
                        {**context, "fencing_token": "stale"}, RELEASE_EVIDENCE
                    )
                self.assertEqual(
                    RELEASE_EVIDENCE,
                    valid_adapter.revalidate_rollback(context, RELEASE_EVIDENCE),
                )
                self.assertEqual(
                    "released",
                    valid_adapter.complete_release_rollback_context(context)["status"],
                )

    def test_wal_cas_and_reload_are_durable(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            store = SQLiteRollbackControlStore(Path(directory) / "control.sqlite", PROJECT)
            created = store.cas(0, {**RECORD, "revision": 1})
            self.assertEqual(1, created["revision"])
            self.assertEqual(created, store.snapshot("op-1"))
            self.assertTrue(store.verify_rollback_context(created))
            self.assertFalse(
                store.verify_rollback_context({**created, "envelope_digest": "e" * 64})
            )
            with store.operation_lock():
                store._begin_release_locked("op-1")
                authorization = store._authorize_release_locked(created, RELEASE_EVIDENCE)
                released = store._complete_release_locked("op-1", authorization)
            self.assertEqual("released", released["status"])
            self.assertEqual(3, store.snapshot("op-1")["revision"])
            with closing(sqlite3.connect(Path(directory) / "control.sqlite")) as connection:
                self.assertEqual("wal", connection.execute("PRAGMA journal_mode").fetchone()[0])

    def test_status_transition_is_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            store = SQLiteRollbackControlStore(Path(directory) / "control.sqlite", PROJECT)
            store.cas(0, RECORD)
            releasing = store.cas(1, {**RECORD, "status": "releasing", "revision": 2})
            with self.assertRaises(ControlStoreError):
                store.cas(2, {**releasing, "status": "held", "revision": 3})

    def test_released_barrier_is_terminal_and_cannot_be_made_ambiguous(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            store = SQLiteRollbackControlStore(Path(directory) / "control.sqlite", PROJECT)
            store.cas(0, RECORD)
            with store.operation_lock():
                store._begin_release_locked("op-1")
                authorization = store._authorize_release_locked(RECORD, RELEASE_EVIDENCE)
                released = store._complete_release_locked("op-1", authorization)
            self.assertEqual("released", released["status"])
            with self.assertRaises(ControlStoreError):
                store.cas(3, {**released, "status": "ambiguous", "revision": 4})

    def test_ambiguous_requires_explicit_newer_reconciliation(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            control_path = Path(directory) / "control.sqlite"
            store = SQLiteRollbackControlStore(control_path, PROJECT)
            ambiguous = store.cas(0, RECORD)
            ambiguous = store.cas(1, {**ambiguous, "status": "ambiguous", "revision": 2})
            with self.assertRaises(ControlStoreError):
                store.reconcile_ambiguous("op-1", {**RECORD, "operation_id": "op-2"})
            replacement = {
                **RECORD,
                "operation_id": "op-2",
                "state_revision": 2,
                "durable_barrier_id": "barrier-2",
                "fencing_token": "fence-2",
            }
            replacement["barrier_identity_digest"] = canonical_barrier_digest(replacement)
            replacement["envelope_digest"] = canonical_envelope_digest(replacement)
            reopened = SQLiteRollbackControlStore(control_path, PROJECT)
            recovered = reopened.reconcile_ambiguous("op-1", replacement)
            self.assertEqual("held", recovered["status"])
            self.assertEqual(
                recovered,
                SQLiteRollbackControlStore(control_path, PROJECT).snapshot("op-2"),
            )
            fresh = SQLiteRollbackControlStore(control_path, PROJECT)
            self.assertEqual("ambiguous", fresh.snapshot("op-1")["status"])
            with self.assertRaisesRegex(ControlStoreError, "CAS conflict"):
                fresh.reconcile_ambiguous("op-1", replacement)
            self.assertEqual(recovered, fresh.snapshot("op-2"))

    def test_schema_corruption_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "control.sqlite"
            store = SQLiteRollbackControlStore(path, PROJECT)
            store.cas(0, RECORD)
            with closing(sqlite3.connect(path)) as connection:
                connection.execute("UPDATE control_meta SET value='99' WHERE key='schema_version'")
                connection.commit()
            with self.assertRaises(ControlStoreError):
                store.snapshot("op-1")

    def test_symlink_and_authority_alias_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            authority = root / "authority.sqlite"
            authority.touch()
            link = root / "control-link.sqlite"
            link.symlink_to(authority)
            with self.assertRaises(ControlStoreError):
                SQLiteRollbackControlStore(link, PROJECT)
            with self.assertRaises(ControlStoreError):
                SQLiteRollbackControlStore(authority, PROJECT, authority)

            dangling_target = root / "missing.sqlite"
            dangling = root / "dangling.sqlite"
            dangling.symlink_to(dangling_target.name)
            with self.assertRaises(ControlStoreError):
                SQLiteRollbackControlStore(dangling, PROJECT, authority)

            absent_alias = root / "absent-alias.sqlite"
            with self.assertRaises(ControlStoreError):
                SQLiteRollbackControlStore(absent_alias, PROJECT, absent_alias)

            linked_parent = root / "linked-parent"
            linked_parent.symlink_to(root)
            with self.assertRaises(ControlStoreError):
                SQLiteRollbackControlStore(linked_parent / "control.sqlite", PROJECT)

    def test_nonregular_alias_and_changed_parent_identities_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with self.assertRaises(ControlStoreError):
                SQLiteRollbackControlStore(root / "missing" / "control.sqlite", PROJECT)
            directory_control = root / "directory-control"
            directory_control.mkdir()
            with self.assertRaises(ControlStoreError):
                SQLiteRollbackControlStore(directory_control, PROJECT)
            authority_directory = root / "authority-directory"
            authority_directory.mkdir()
            with self.assertRaises(ControlStoreError):
                SQLiteRollbackControlStore(root / "control.sqlite", PROJECT, authority_directory)
            authority = root / "authority.sqlite"
            authority.touch()
            alias = root / "alias.sqlite"
            os.link(authority, alias)
            with self.assertRaises(ControlStoreError):
                SQLiteRollbackControlStore(alias, PROJECT, authority)

    def test_control_path_swap_after_binding_fails_without_authority_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            authority = root / "authority.sqlite"
            with closing(sqlite3.connect(authority)) as connection:
                connection.execute("CREATE TABLE authority_payload(value TEXT)")
                connection.commit()
            control = root / "control.sqlite"
            store = SQLiteRollbackControlStore(control, PROJECT, authority)
            original = root / "original-control.sqlite"
            control.rename(original)
            control.symlink_to(authority.name)

            with self.assertRaises(ControlStoreError):
                store.cas(0, RECORD)
            with closing(sqlite3.connect(authority)) as connection:
                tables = {
                    row[0]
                    for row in connection.execute(
                        "SELECT name FROM sqlite_master WHERE type='table'"
                    )
                }
            self.assertEqual({"authority_payload"}, tables)

    def test_control_swap_between_descriptor_validation_and_sqlite_open_fails_closed(self) -> None:
        class SwappingStore(SQLiteRollbackControlStore):
            swapped = False

            def _open_bound_file(
                self,
                path: Path,
                expected_parent: tuple[int, int],
                expected_file: tuple[int, int],
            ) -> tuple[int, int]:
                parent, descriptor = super()._open_bound_file(path, expected_parent, expected_file)
                if path == self.path and not self.swapped:
                    self.swapped = True
                    self.path.rename(self.path.with_suffix(".original"))
                    assert self.authority_path is not None
                    self.path.symlink_to(self.authority_path.name)
                return parent, descriptor

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            authority = root / "authority.sqlite"
            with closing(sqlite3.connect(authority)) as connection:
                connection.execute("CREATE TABLE authority_payload(value TEXT)")
                connection.commit()
            store = SwappingStore(root / "control.sqlite", PROJECT, authority)

            with self.assertRaises(ControlStoreError):
                store.cas(0, RECORD)
            with closing(sqlite3.connect(authority)) as connection:
                tables = {
                    row[0]
                    for row in connection.execute(
                        "SELECT name FROM sqlite_master WHERE type='table'"
                    )
                }
            self.assertEqual({"authority_payload"}, tables)

    def test_with_barrier_holds_coordinator_lock_through_authority_callback(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            store = SQLiteRollbackControlStore(Path(directory) / "control.sqlite", PROJECT)
            seen: list[str] = []

            def authority(record: Mapping[str, object]) -> Mapping[str, object]:
                seen.append(str(record["status"]))
                return {**record, "status": "releasing"}

            result = store.with_barrier(0, RECORD, authority)
            self.assertEqual(["held"], seen)
            self.assertEqual("releasing", result["status"])

    def test_with_barrier_failure_leaves_durable_held_barrier(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            store = SQLiteRollbackControlStore(Path(directory) / "control.sqlite", PROJECT)

            def fail(_record: Mapping[str, object]) -> Mapping[str, object]:
                raise RuntimeError("authority failed")

            with self.assertRaises(RuntimeError):
                store.with_barrier(0, RECORD, fail)
            self.assertEqual("held", store.snapshot("op-1")["status"])

    def test_release_reconciliation_requires_verified_engine_recovery(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            store = SQLiteRollbackControlStore(Path(directory) / "control.sqlite", PROJECT)
            held = store.cas(0, RECORD)
            releasing = store.cas(1, {**held, "status": "releasing", "revision": 2})
            with self.assertRaises(ControlStoreError):
                store.reconcile_release("op-1")
            self.assertEqual(2, store.snapshot("op-1")["revision"])
            self.assertEqual("releasing", releasing["status"])

    def test_with_barrier_rejects_reentrant_store_access(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            store = SQLiteRollbackControlStore(Path(directory) / "control.sqlite", PROJECT)

            def reenter(_record: Mapping[str, object]) -> Mapping[str, object]:
                store.snapshot("op-1")
                return RECORD

            with self.assertRaises(ControlStoreError):
                store.with_barrier(0, RECORD, reenter)
            self.assertEqual("held", store.snapshot("op-1")["status"])

    def test_operation_lock_is_single_nonreentrant_outer_scope(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            store = SQLiteRollbackControlStore(Path(directory) / "control.sqlite", PROJECT)
            with store.operation_lock(), self.assertRaises(ControlStoreError):
                store.operation_lock().__enter__()
            with store.operation_lock(), self.assertRaises(ControlStoreError):
                store.snapshot("op-1")

    def test_operation_lock_blocks_a_second_store_instance(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "control.sqlite"
            first = SQLiteRollbackControlStore(path, PROJECT)
            second = SQLiteRollbackControlStore(path, PROJECT)
            started = threading.Event()
            finished = threading.Event()
            errors: list[str] = []

            def read_from_second_instance() -> None:
                started.set()
                try:
                    second.snapshot("op-1")
                except ControlStoreError as error:
                    errors.append(str(error))
                finally:
                    finished.set()

            with first.operation_lock():
                worker = threading.Thread(target=read_from_second_instance)
                worker.start()
                self.assertTrue(started.wait(1))
                self.assertFalse(finished.wait(0.1))
            self.assertTrue(finished.wait(2))
            worker.join()
            self.assertEqual(["control barrier is missing"], errors)

    def test_control_lock_timeout_is_bounded_and_preserves_state(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "control.sqlite"
            first = SQLiteRollbackControlStore(path, PROJECT)
            second = SQLiteRollbackControlStore(path, PROJECT)
            with (
                first._control_lock(),
                patch(
                    "tools.rollback_control_store.time.monotonic",
                    side_effect=(0.0, 0.0, 1.0, 11.0),
                ),
                patch("tools.rollback_control_store.time.sleep") as sleep,
                self.assertRaises(ControlStoreError),
            ):
                second.cas(0, RECORD)
            self.assertGreaterEqual(sleep.call_count, 1)
            self.assertTrue(all(0 < call.args[0] <= 0.05 for call in sleep.call_args_list))
            with self.assertRaises(ControlStoreError):
                first.snapshot("op-1")

    def test_control_lock_poll_never_sleeps_past_deadline(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "control.sqlite"
            first = SQLiteRollbackControlStore(path, PROJECT)
            second = SQLiteRollbackControlStore(path, PROJECT)
            clock = MagicMock()
            clock.monotonic.side_effect = (0.0, 9.99, 10.0)
            with (
                first._control_lock(),
                patch("tools.rollback_control_store.time", clock),
                self.assertRaises(ControlStoreError),
            ):
                second.cas(0, RECORD)
            sleep = clock.sleep
            self.assertEqual(sleep.call_count, 1)
            self.assertGreater(sleep.call_args_list[-1].args[0], 0)
            self.assertLess(sleep.call_args_list[-1].args[0], 0.05)

    def test_control_lock_timeout_closes_descriptor_for_retry(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "control.sqlite"
            first = SQLiteRollbackControlStore(path, PROJECT)
            second = SQLiteRollbackControlStore(path, PROJECT)
            with (
                first._control_lock(),
                patch(
                    "tools.rollback_control_store.time.monotonic",
                    side_effect=(0.0, 0.0, 11.0),
                ),
                patch("tools.rollback_control_store.time.sleep"),
                self.assertRaises(ControlStoreError),
            ):
                second.cas(0, RECORD)
            second.cas(0, RECORD)
            self.assertEqual("op-1", second.snapshot("op-1")["operation_id"])

    def test_operation_lock_clears_owner_after_body_failure(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            store = SQLiteRollbackControlStore(Path(directory) / "control.sqlite", PROJECT)
            with self.assertRaisesRegex(RuntimeError, "body failed"), store.operation_lock():
                self.assertTrue(store.operation_owned_by_current_thread)
                raise RuntimeError("body failed")
            self.assertFalse(store.operation_owned_by_current_thread)
            with store.operation_lock():
                self.assertTrue(store.operation_owned_by_current_thread)

    def test_operation_lock_body_failure_releases_for_another_store(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "control.sqlite"
            first = SQLiteRollbackControlStore(path, PROJECT)
            second = SQLiteRollbackControlStore(path, PROJECT)
            with self.assertRaisesRegex(RuntimeError, "body failed"), first.operation_lock():
                raise RuntimeError("body failed")
            with second.operation_lock():
                self.assertTrue(second.operation_owned_by_current_thread)
            self.assertFalse(second.operation_owned_by_current_thread)

    def test_caller_owned_lock_clears_owner_after_body_failure(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            store = SQLiteRollbackControlStore(Path(directory) / "control.sqlite", PROJECT)
            with locked() as guard:
                with (
                    self.assertRaisesRegex(RuntimeError, "body failed"),
                    store.lock_owned_by_caller(guard),
                ):
                    raise RuntimeError("body failed")
                guard.assert_owned()
                with store.lock_owned_by_caller(guard):
                    self.assertTrue(store.operation_owned_by_current_thread)
                guard.assert_owned()
                self.assertFalse(store.operation_owned_by_current_thread)

    def test_releasing_barrier_cannot_be_completed_without_authority_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            store = SQLiteRollbackControlStore(Path(directory) / "control.sqlite", PROJECT)
            store.cas(0, RECORD)
            store.begin_release("op-1")
            with self.assertRaises(ControlStoreError):
                store.reconcile_release("op-1")
            self.assertEqual("releasing", store.snapshot("op-1")["status"])

    def test_cas_conflict_and_binding_mismatch_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            store = SQLiteRollbackControlStore(Path(directory) / "control.sqlite", PROJECT)
            store.cas(0, RECORD)
            with self.assertRaises(ControlStoreError):
                store.cas(0, {**RECORD, "revision": 1})
            with self.assertRaises(ControlStoreError):
                store.cas(1, {**RECORD, "project_id": OTHER_PROJECT})
            with self.assertRaises(ControlStoreError):
                store.cas(0, {**RECORD, "operation_id": "op-2"})

    def test_cas_rejects_missing_stale_active_changed_and_illegal_transitions(self) -> None:
        def candidate(**changes: object) -> dict[str, object]:
            value = {**RECORD, **changes}
            value["barrier_identity_digest"] = canonical_barrier_digest(value)
            value["envelope_digest"] = canonical_envelope_digest(value)
            return value

        with tempfile.TemporaryDirectory() as directory:
            store = SQLiteRollbackControlStore(Path(directory) / "control.sqlite", PROJECT)
            with self.assertRaises(ControlStoreError):
                store.cas(1, RECORD)
            held = store.cas(0, RECORD)
            with self.assertRaises(ControlStoreError):
                store.cas(0, candidate(operation_id="op-2", state_revision=2))
            changed_fence = candidate(revision=2)
            changed_fence["fencing_token"] = f"{RECORD['fencing_token']}-changed"
            changed_fence["barrier_identity_digest"] = canonical_barrier_digest(changed_fence)
            changed_fence["envelope_digest"] = canonical_envelope_digest(changed_fence)
            with self.assertRaises(ControlStoreError):
                store.cas(1, changed_fence)
            with self.assertRaises(ControlStoreError):
                store.cas(1, candidate(project_id=OTHER_PROJECT))
            ambiguous = store.cas(1, {**held, "status": "ambiguous", "revision": 2})
            with self.assertRaises(ControlStoreError):
                store.cas(2, {**ambiguous, "status": "held", "revision": 3})
            with self.assertRaises(ControlStoreError):
                store.cas(0, candidate(operation_id="op-stale", state_revision=1))

    def test_boolean_expected_revision_is_rejected_by_public_and_private_cas(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            store = SQLiteRollbackControlStore(Path(directory) / "control.sqlite", PROJECT)
            with self.assertRaises(ControlStoreError):
                store.cas(False, RECORD)
            with self.assertRaises(ControlStoreError):
                store.snapshot("op-1")
            created = store.cas(0, RECORD)
            with store.operation_lock(), self.assertRaises(ControlStoreError):
                store._cas_locked(True, {**created, "status": "releasing", "revision": 2})
            self.assertEqual(1, store.snapshot("op-1")["revision"])

    def test_invalid_identity_and_status_are_rejected_before_write(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            store = SQLiteRollbackControlStore(Path(directory) / "control.sqlite", PROJECT)
            for mutation in (
                {"project_id": "project-1"},
                {"backend": "git"},
                {"envelope_digest": "f" * 63},
                {"operation_id": "../escape"},
                {"state_revision": False},
                {"revision": False},
                {"revision": 0},
                {"status": "unknown"},
            ):
                with self.subTest(mutation=mutation), self.assertRaises(ControlStoreError):
                    store.cas(0, {**RECORD, **mutation})
            with self.assertRaises(ControlStoreError):
                store.snapshot("op-1")

    def test_public_guards_reject_invalid_projects_transitions_and_reentry(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for project_id in ("not-a-uuid", INVALID_VARIANT_PROJECT):
                with self.subTest(project_id=project_id), self.assertRaises(ControlStoreError):
                    SQLiteRollbackControlStore(root / f"{project_id}.sqlite", project_id)

            store = SQLiteRollbackControlStore(root / "control.sqlite", PROJECT)
            with self.assertRaises(ControlStoreError):
                store.cas(0, {key: value for key, value in RECORD.items() if key != "manifest"})
            git_record = {**RECORD, "backend": "git"}
            git_record["barrier_identity_digest"] = canonical_barrier_digest(git_record)
            git_record["envelope_digest"] = canonical_envelope_digest(git_record)
            with self.assertRaisesRegex(ControlStoreError, "control backend is invalid"):
                store.cas(0, git_record)
            with self.assertRaisesRegex(ControlStoreError, "released status requires"):
                store.cas(0, {**RECORD, "status": "released"})
            with self.assertRaisesRegex(ControlStoreError, "must start held"):
                store.cas(0, {**RECORD, "status": "ambiguous"})

            held = store.cas(0, RECORD)
            ambiguous = store.cas(1, {**held, "status": "ambiguous", "revision": 2})
            with self.assertRaisesRegex(ControlStoreError, "barrier is not held"):
                store.begin_release("op-1")
            fresh = SQLiteRollbackControlStore(root / "fresh.sqlite", PROJECT)
            fresh.cas(0, RECORD)
            with self.assertRaisesRegex(ControlStoreError, "only ambiguous barriers"):
                fresh.reconcile_ambiguous("op-1", RECORD)
            with self.assertRaisesRegex(ControlStoreError, "new held operation"):
                store.reconcile_ambiguous("op-1", ambiguous)
            old_replacement = {
                **RECORD,
                "operation_id": "op-old",
                "status": "held",
                "revision": 1,
            }
            old_replacement["barrier_identity_digest"] = canonical_barrier_digest(old_replacement)
            old_replacement["envelope_digest"] = canonical_envelope_digest(old_replacement)
            with self.assertRaisesRegex(ControlStoreError, "newer project fence"):
                store.reconcile_ambiguous("op-1", old_replacement)
            reopened = SQLiteRollbackControlStore(root / "control.sqlite", PROJECT)
            with self.assertRaisesRegex(ControlStoreError, "newer project fence"):
                reopened.reconcile_ambiguous("op-1", old_replacement)
            reused_token = {
                **old_replacement,
                "state_revision": 3,
                "durable_barrier_id": "barrier-new",
            }
            reused_token["barrier_identity_digest"] = canonical_barrier_digest(reused_token)
            reused_token["envelope_digest"] = canonical_envelope_digest(reused_token)
            with self.assertRaisesRegex(ControlStoreError, "distinct project fence"):
                reopened.reconcile_ambiguous("op-1", reused_token)
            unchanged = reopened.snapshot("op-1")
            self.assertEqual(("ambiguous", 2), (unchanged["status"], unchanged["revision"]))

            with store.operation_lock():
                actions: tuple[Callable[[], object], ...] = (
                    lambda: store.cas(2, ambiguous),
                    lambda: store.begin_release("op-1"),
                    lambda: store.verify_rollback_context(RECORD),
                    lambda: store.with_barrier(2, ambiguous, lambda value: value),
                )
                for action in actions:
                    with (
                        self.subTest(action=action),
                        self.assertRaisesRegex(ControlStoreError, "non-reentrant"),
                    ):
                        action()
            self.assertIsNone(store.verify_rollback_context({**RECORD, "operation_id": None}))

            other_project = OTHER_PROJECT
            other_record = {**RECORD, "project_id": other_project}
            other_record["barrier_identity_digest"] = canonical_barrier_digest(other_record)
            other_record["envelope_digest"] = canonical_envelope_digest(other_record)
            other_store = SQLiteRollbackControlStore(root / "other.sqlite", PROJECT)
            with self.assertRaisesRegex(ControlStoreError, "project binding mismatch"):
                other_store.with_barrier(0, other_record, lambda value: value)

    def test_bound_parent_authority_and_project_swaps_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            real_authority = root / "real-authority.sqlite"
            real_authority.touch()
            authority_link = root / "authority-link.sqlite"
            authority_link.symlink_to(real_authority.name)
            with self.assertRaisesRegex(ControlStoreError, "authority descriptor is unsafe"):
                SQLiteRollbackControlStore(root / "linked-control.sqlite", PROJECT, authority_link)

            authority = root / "authority.sqlite"
            authority.touch()
            store = SQLiteRollbackControlStore(root / "control.sqlite", PROJECT, authority)
            authority.rename(root / "previous-authority.sqlite")
            authority.touch()
            with self.assertRaisesRegex(ControlStoreError, "authority descriptor identity changed"):
                store.cas(0, RECORD)

            parent = root / "bound-parent"
            parent.mkdir(mode=0o700)
            parent_store = SQLiteRollbackControlStore(parent / "control.sqlite", PROJECT)
            parent.rename(root / "previous-parent")
            parent.mkdir(mode=0o700)
            with self.assertRaisesRegex(ControlStoreError, "parent identity changed"):
                parent_store.cas(0, RECORD)

            project_path = root / "project-bound.sqlite"
            first = SQLiteRollbackControlStore(project_path, PROJECT)
            first.cas(0, RECORD)
            second = SQLiteRollbackControlStore(project_path, OTHER_PROJECT)
            with self.assertRaisesRegex(ControlStoreError, "project binding mismatch"):
                second.snapshot("op-1")

    def test_regular_file_replacement_nonregular_file_and_descriptor_fault_fail_closed(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            control = root / "control.sqlite"
            store = SQLiteRollbackControlStore(control, PROJECT)
            control.rename(root / "previous-control.sqlite")
            control.touch()
            with self.assertRaisesRegex(ControlStoreError, "descriptor identity changed"):
                store.cas(0, RECORD)

            fifo = root / "control.fifo"
            os.mkfifo(fifo)
            with self.assertRaisesRegex(ControlStoreError, "not a regular file"):
                SQLiteRollbackControlStore(fifo, PROJECT)

            fault_store = SQLiteRollbackControlStore(root / "fault.sqlite", PROJECT)
            with (
                patch(
                    "tools.rollback_control_store.os.fstat",
                    side_effect=OSError("descriptor unreadable"),
                ),
                self.assertRaisesRegex(ControlStoreError, "parent descriptor is unsafe"),
            ):
                fault_store.snapshot("op-1")

            real_fstat = os.fstat
            fstat_calls = 0

            def fail_file_descriptor(descriptor: int) -> os.stat_result:
                nonlocal fstat_calls
                fstat_calls += 1
                if fstat_calls == 2:
                    raise OSError("descriptor unreadable")
                return real_fstat(descriptor)

            with (
                patch(
                    "tools.rollback_control_store.os.fstat",
                    side_effect=fail_file_descriptor,
                ),
                self.assertRaisesRegex(ControlStoreError, "descriptor is unreadable"),
            ):
                fault_store.snapshot("op-1")

    def test_sidecars_require_private_provisioning_and_stable_regular_identities(self) -> None:
        class SwappingSidecarStore(SQLiteRollbackControlStore):
            def __init__(self, path: Path, project_id: str, suffix: str) -> None:
                super().__init__(path, project_id)
                self.suffix = suffix

            def _cas_connection(
                self,
                connection: sqlite3.Connection,
                expected_revision: int,
                supplied: dict[str, object],
            ) -> dict[str, object]:
                result = super()._cas_connection(connection, expected_revision, supplied)
                sidecar = Path(f"{self.path}{self.suffix}")
                sidecar.rename(Path(f"{sidecar}-previous"))
                sidecar.touch()
                return result

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            public_parent = root / "public-control"
            public_parent.mkdir(mode=0o755)
            public_parent.chmod(0o755)
            with self.assertRaisesRegex(ControlStoreError, "owner-only provisioned directory"):
                SQLiteRollbackControlStore(public_parent / "control.sqlite", PROJECT)
            self.assertFalse((public_parent / "control.sqlite").exists())

            for suffix in ("-wal", "-shm"):
                with self.subTest(suffix=suffix):
                    path = root / f"linked{suffix}.sqlite"
                    store = SQLiteRollbackControlStore(path, PROJECT)
                    target = root / f"sidecar-target{suffix}"
                    target.touch()
                    Path(f"{path}{suffix}").symlink_to(target.name)
                    with self.assertRaisesRegex(ControlStoreError, "sidecar descriptor is unsafe"):
                        store.cas(0, RECORD)

            hardlink_path = root / "hardlink.sqlite"
            hardlink_store = SQLiteRollbackControlStore(hardlink_path, PROJECT)
            sidecar_source = root / "sidecar-source"
            sidecar_source.touch()
            os.link(sidecar_source, Path(f"{hardlink_path}-wal"))
            with self.assertRaisesRegex(ControlStoreError, "sidecar is not private and regular"):
                hardlink_store.cas(0, RECORD)

            for suffix in ("-wal", "-shm"):
                with self.subTest(swapped_suffix=suffix):
                    swapping_path = root / f"swapping{suffix}.sqlite"
                    swapping_store = SwappingSidecarStore(swapping_path, PROJECT, suffix)
                    with self.assertRaisesRegex(ControlStoreError, "WAL sidecar identity changed"):
                        swapping_store.cas(0, RECORD)

    def test_release_authorization_rejects_delegate_mutation_and_external_revision_tamper(
        self,
    ) -> None:
        class Delegate:
            def snapshot(self, _phase: str, _context: Mapping[str, object]) -> dict[str, object]:
                return {}

            def execute(self, _phase: str, _context: Mapping[str, object]) -> dict[str, object]:
                return {}

        class MutatingRereader(StaticAuthorityRuntimeRereader):
            def reread_rollback(
                self, context: Mapping[str, object], result: Mapping[str, object]
            ) -> SQLiteAuthorityRuntimeState:
                assert isinstance(context, dict)
                context["authority_revision"] = "changed"
                return super().reread_rollback(context, result)

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            authority = root / "authority.sqlite"
            authority.touch()
            context = {field: RECORD[field] for field in IDENTITY_FIELDS}

            mutation_store = SQLiteRollbackControlStore(
                root / "mutation-control.sqlite", PROJECT, authority
            )
            mutation_store.cas(0, RECORD)
            mutation_adapter = SQLiteControlStoreAdapter(
                Delegate(), mutation_store, MutatingRereader()
            )
            mutable_context = dict(context)
            with mutation_adapter.operation_lock():
                mutation_adapter.begin_release_rollback_context(mutable_context)
                with self.assertRaisesRegex(ControlStoreError, "authorization identity changed"):
                    mutation_adapter.revalidate_rollback(mutable_context, RELEASE_EVIDENCE)
            self.assertEqual("releasing", mutation_store.snapshot("op-1")["status"])

            control = root / "tamper-control.sqlite"
            tamper_store = SQLiteRollbackControlStore(control, PROJECT, authority)
            tamper_store.cas(0, RECORD)
            tamper_adapter = SQLiteControlStoreAdapter(
                Delegate(), tamper_store, StaticAuthorityRuntimeRereader()
            )
            with tamper_adapter.operation_lock():
                tamper_adapter.begin_release_rollback_context(context)
                tamper_adapter.revalidate_rollback(context, RELEASE_EVIDENCE)
                with closing(sqlite3.connect(control)) as connection:
                    connection.execute(
                        "UPDATE barrier SET revision=revision+1 WHERE operation_id='op-1'"
                    )
                    connection.commit()
                with self.assertRaisesRegex(ControlStoreError, "release authorization is stale"):
                    tamper_adapter.complete_release_rollback_context(context)
            self.assertEqual("releasing", tamper_store.snapshot("op-1")["status"])

    def test_connection_and_durability_refusal_close_resources_and_retry(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "control.sqlite"
            store = SQLiteRollbackControlStore(path, PROJECT)
            with (
                patch(
                    "tools.rollback_control_store.sqlite3.connect",
                    side_effect=sqlite3.OperationalError("connect failed"),
                ),
                self.assertRaises(sqlite3.OperationalError),
            ):
                store.snapshot("op-1")
            with self.assertRaisesRegex(ControlStoreError, "barrier is missing"):
                store.snapshot("op-1")

            wal_connection = MagicMock(spec=sqlite3.Connection)
            wal_connection.execute.return_value.fetchone.return_value = ("delete",)
            with (
                patch("tools.rollback_control_store.sqlite3.connect", return_value=wal_connection),
                self.assertRaisesRegex(ControlStoreError, "WAL is unavailable"),
            ):
                store.snapshot("op-1")
            wal_connection.close.assert_called_once_with()

            full_connection = MagicMock(spec=sqlite3.Connection)
            wal_cursor = MagicMock()
            wal_cursor.fetchone.return_value = ("wal",)
            full_cursor = MagicMock()
            full_cursor.fetchone.return_value = (1,)
            full_connection.execute.side_effect = (wal_cursor, MagicMock(), full_cursor)
            with (
                patch("tools.rollback_control_store.sqlite3.connect", return_value=full_connection),
                self.assertRaisesRegex(ControlStoreError, "FULL durability is unavailable"),
            ):
                store.snapshot("op-1")
            full_connection.close.assert_called_once_with()

    def test_connection_close_failure_is_classified_as_ambiguous(self) -> None:
        real_connect = sqlite3.connect

        class CloseFailingConnection:
            def __init__(self, connection: sqlite3.Connection) -> None:
                self._connection = connection

            def __getattr__(self, name: str) -> object:
                return getattr(self._connection, name)

            def close(self) -> None:
                self._connection.close()
                raise sqlite3.OperationalError("injected close failure")

        def connector(*args: Any, **kwargs: Any) -> CloseFailingConnection:
            return CloseFailingConnection(real_connect(*args, **kwargs))

        with tempfile.TemporaryDirectory() as directory:
            store = SQLiteRollbackControlStore(Path(directory) / "control.sqlite", PROJECT)
            with (
                patch("tools.rollback_control_store.sqlite3.connect", side_effect=connector),
                self.assertRaisesRegex(
                    ControlStoreAmbiguousError,
                    "connection close outcome is ambiguous",
                ),
            ):
                store.snapshot("op-1")


if __name__ == "__main__":
    unittest.main()
