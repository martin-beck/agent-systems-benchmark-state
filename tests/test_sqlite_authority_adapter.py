# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Hostile tests for the read-only SQLite authority adapter slice."""

from __future__ import annotations

import json
import multiprocessing
import os
import shutil
import sqlite3
import tempfile
import unittest
from collections.abc import Iterator, Mapping
from contextlib import closing, contextmanager
from pathlib import Path
from types import SimpleNamespace
from typing import Any, cast
from unittest.mock import patch

from tools.admission_lease import AdmissionLease, validate_recheck
from tools.authority_neutral_commit import CommitAdmissionBundle
from tools.generate_upgrade_contract import generate
from tools.handoffctl import locked
from tools.lock_domain_scope import LockDomainScope
from tools.mutation_fence import MutationFence, provision, provision_control_binding
from tools.rollback_control_store import (
    BarrierSessionState,
    SQLiteBarrierSessionStore,
    SQLiteRollbackControlStore,
)
from tools.scoped_backend_adapter import ScopedBackendAdapter
from tools.sqlite_authority_adapter import (
    SQLiteAuthorityAdapter,
    SQLiteAuthorityError,
    SQLiteLifecycleExecutor,
)
from tools.sqlite_authority_mutation import SQLiteCommitCapability
from tools.upgrade_authority import commit_runtime_selector
from tools.upgrade_binding import UpgradeRuntimeBinding
from tools.upgrade_engine import BoundRollbackCapability, PhaseContext, UpgradeEngine
from tools.upgrade_identity import (
    BarrierSessionIdentity,
    canonical_barrier_digest,
    canonical_barrier_session_digest,
    canonical_envelope_digest,
)

PROJECT = "11111111-1111-4111-8111-111111111111"

CONTEXT = {
    "schema_version": 2,
    "backend": "sqlite",
    "project_id": "project",
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


def _snapshot_process(path_text: str, crash: bool) -> None:
    adapter = SQLiteAuthorityAdapter(Path(path_text))
    adapter.snapshot("discover", CONTEXT)
    if crash:
        os._exit(17)


def _bound_snapshot_worker(root_text: str, mode: str, result: Any, rollback: bool = False) -> None:
    root = Path(root_text)
    authority = root / "authority.sqlite"
    control = root / "control.sqlite"
    store = SQLiteRollbackControlStore(control, PROJECT, authority)
    session = SQLiteBarrierSessionStore(store, lambda: "authority")
    fence = MutationFence(
        authority,
        root / "authority-marker.json",
        root / "authority-lifecycle.json",
        root / "authority.lock",
        control,
        root / "control-binding.json",
        store.control_lock_path,
    )
    old = AdmissionLease(PROJECT, "authority", "fence", "owner", "barrier", 1)
    replacement = AdmissionLease(PROJECT, "authority", "fence-new", "owner-new", "barrier-new", 2)
    lease = old if mode == "stale" else replacement
    recheck = validate_recheck(
        lease,
        project_id=PROJECT,
        authority_revision=lease.authority_revision,
        fencing_token=lease.fencing_token,
        fencing_owner=lease.fencing_owner,
        durable_barrier_id=lease.durable_barrier_id,
        revision=lease.revision,
    )

    class CountingAdapter(SQLiteAuthorityAdapter):
        calls = 0

        def snapshot(self, phase: str, context: Mapping[str, object]) -> dict[str, object]:
            self.calls += 1
            return super().snapshot(phase, context)

    adapter = CountingAdapter(authority)
    if mode == "crash":

        def aborting_snapshot(_phase: str, _context: Mapping[str, object]) -> dict[str, object]:
            os._exit(17)

        adapter.snapshot = aborting_snapshot  # type: ignore[assignment]
    context = {
        **CONTEXT,
        "target": "rollback" if rollback else "new",
        "project_id": PROJECT,
        "authority_revision": lease.authority_revision,
        "fencing_token": lease.fencing_token,
        "fencing_owner": lease.fencing_owner,
        "durable_barrier_id": lease.durable_barrier_id,
        "state_revision": lease.revision,
    }
    try:
        scope = LockDomainScope.bind(session, fence, lease, recheck, locked)
        if rollback:
            value = adapter.verify_rollback_context_bound(
                context, scope, lease=lease, admission_recheck=recheck
            )
        else:
            value = adapter.snapshot_bound(
                "discover", context, scope, lease=lease, admission_recheck=recheck
            )
    except Exception as error:
        result.put(
            (
                "rejected",
                type(error).__name__,
                adapter.calls,
                session.operation_owned_by_current_thread,
            )
        )
    else:
        result.put(
            (
                "success",
                value["sqlite_integrity_verified"],
                adapter.calls,
                session.operation_owned_by_current_thread,
            )
        )


def _hold_exclusive_transaction(path_text: str, ready: object) -> None:
    connection = sqlite3.connect(path_text, isolation_level=None)
    try:
        connection.execute("BEGIN EXCLUSIVE")
        update = connection.execute(
            "UPDATE records SET body = 'uncommitted' WHERE id = 1 AND body = 'clean'"
        )
        if update.rowcount != 1:
            raise RuntimeError("CAS did not match the expected authority row")
        ready.send(True)  # type: ignore[attr-defined]
        ready.recv()  # type: ignore[attr-defined]
    finally:
        connection.close()


class Scope:
    def assert_ordered(self) -> None:
        pass

    def assert_context(self, _context: Mapping[str, object]) -> None:
        pass

    @contextmanager
    def hold(self) -> Iterator[object]:
        yield object()


class SQLiteAuthorityAdapterTests(unittest.TestCase):
    def test_adapter_durable_commit_factory_journals_real_sqlite_receipt(self) -> None:
        admission = CommitAdmissionBundle(
            backend="sqlite",
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
        )
        receipt = capability.execute(
            lambda connection: connection.execute(
                "UPDATE records SET body = 'durable' WHERE id = 1"
            )
        )

        self.assertEqual("sqlite", receipt.backend)
        with closing(sqlite3.connect(self.authority)) as connection, connection:
            self.assertEqual(
                "durable", connection.execute("SELECT body FROM records").fetchone()[0]
            )
        self.assertEqual(["prepared", "committed"], [item[0] for item in journal])
        self.assertEqual(receipt, journal[1][1])

    def test_durable_commit_factory_normalizes_invalid_session_revision(self) -> None:
        admission = CommitAdmissionBundle(
            backend="sqlite",
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
        with self.assertRaisesRegex(SQLiteAuthorityError, "durable commit capability binding"):
            self.adapter.bind_durable_commit_capability(
                admission,
                object(),
                session_revision=2,
                admission_reread=lambda: admission.__dict__,
            )

    def test_durable_commit_factory_classifies_termination_as_rejected(self) -> None:
        admission = CommitAdmissionBundle(
            backend="sqlite",
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
                SQLiteAuthorityError, "durable commit capability binding was rejected"
            ),
        ):
            self.adapter.bind_durable_commit_capability(
                admission,
                object(),
                session_revision=1,
                admission_reread=lambda: admission.__dict__,
            )

    def test_adapter_binds_isolated_commit_capability_without_enabling_dispatch(self) -> None:
        admission = CommitAdmissionBundle(
            backend="sqlite",
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
        )
        self.assertIsInstance(capability, SQLiteCommitCapability)
        with self.assertRaisesRegex(SQLiteAuthorityError, "not implemented"):
            self.adapter.execute("commit", CONTEXT)

    def test_commit_bound_executes_one_identity_bound_effect_without_public_dispatch(self) -> None:
        admission = CommitAdmissionBundle(
            backend="sqlite",
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
        result = self.adapter.commit_bound(
            admission,
            lambda connection: connection.execute(
                "UPDATE records SET body = 'bound' WHERE id = 1 AND body = 'clean'"
            ),
            admission_reread=lambda: admission.__dict__,
        )
        self.assertEqual("sqlite", result.backend)
        self.assertEqual("op-bound:commit", result.operation_id)
        self.assertEqual("ok", result.integrity_check)
        with closing(sqlite3.connect(self.authority)) as connection:
            self.assertEqual(("bound",), connection.execute("SELECT body FROM records").fetchone())
        with self.assertRaisesRegex(SQLiteAuthorityError, "not implemented"):
            self.adapter.execute("commit", CONTEXT)

    def test_adapter_classifies_termination_during_commit_binding_identity_as_rejected(
        self,
    ) -> None:
        admission = CommitAdmissionBundle(
            backend="sqlite",
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
            patch.object(Path, "lstat", side_effect=KeyboardInterrupt("injected termination")),
            self.assertRaisesRegex(SQLiteAuthorityError, "commit capability binding was rejected"),
        ):
            self.adapter.bind_commit_capability(
                admission,
                admission_reread=lambda: admission.__dict__,
            )

    def test_adapter_classifies_termination_during_commit_binding_as_rejected(self) -> None:
        admission = CommitAdmissionBundle(
            backend="sqlite",
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
                "tools.sqlite_authority_mutation.SQLiteCommitCapability",
                side_effect=KeyboardInterrupt("injected termination"),
            ),
            self.assertRaisesRegex(SQLiteAuthorityError, "commit capability binding was rejected"),
        ):
            self.adapter.bind_commit_capability(
                admission,
                admission_reread=lambda: admission.__dict__,
            )

    def _durable_state(self) -> tuple[bytes, object]:
        return self.authority.read_bytes(), self.session.snapshot()

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
        self.authority = self.root / "authority.sqlite"
        with closing(sqlite3.connect(self.authority)) as connection, connection:
            connection.execute("CREATE TABLE records (id INTEGER PRIMARY KEY, body TEXT)")
            connection.execute("INSERT INTO records(body) VALUES ('clean')")
        self.authority.chmod(0o600)
        self.adapter = SQLiteAuthorityAdapter(self.authority)
        control = self.root / "control.sqlite"
        store = SQLiteRollbackControlStore(control, PROJECT, self.authority)
        marker = self.root / "authority-marker.json"
        lifecycle = self.root / "authority-lifecycle.json"
        authority_lock = self.root / "authority.lock"
        binding = self.root / "control-binding.json"
        provision(self.authority, marker, lifecycle, authority_lock, PROJECT)
        provision_control_binding(control, binding, store.control_lock_path, PROJECT)
        fence = MutationFence(
            self.authority,
            marker,
            lifecycle,
            authority_lock,
            control,
            binding,
            store.control_lock_path,
        )
        self.session = SQLiteBarrierSessionStore(store, lambda: "authority")
        self.session.create(self._session_identity())
        self.lease = AdmissionLease(PROJECT, "authority", "fence", "owner", "barrier", 1)
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
        self.directory.cleanup()

    def test_bound_lifecycle_executor_snapshots_real_control_and_journal(self) -> None:
        journal = self.root / "engine-journal.json"
        journal.write_text(
            '{"status":"running","phase":"backup","records":[{"outcome":"started"}]}\n',
            encoding="utf-8",
        )
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        snapshot = executor.snapshot()
        self.assertEqual("held", snapshot.control.status)
        self.assertEqual(1, snapshot.control.revision)
        self.assertEqual("backup", snapshot.journal.phase)
        self.assertEqual(4, len(snapshot.journal_identity))
        self.assertEqual([{"outcome": "started"}], snapshot.journal.as_mapping()["records"])
        self.assertFalse(self.session.operation_owned_by_current_thread)
        self.assertEqual(b"clean", self.authority.read_bytes()[-5:])

    def test_generated_backup_dispatch_requires_held_session_and_preserves_contract_identity(
        self,
    ) -> None:
        journal = self.root / "engine-journal.json"
        journal.write_text(
            '{"status":"running","phase":"backup","records":[{'
            '"operation_id":"campaign","step_id":"campaign:backup",'
            '"phase":"backup","outcome":"started","context":{'
            '"selector_ref":"runtime-selector.json","state_revision":1,'
            '"durable_barrier_id":"barrier","fencing_token":"fence"}}]}\n',
            encoding="utf-8",
        )
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        operation = {
            "operation_id": "campaign:backup",
            "opcode": "backend.backup",
            "inputs": {
                "backend": "sqlite",
                "selector_ref": "runtime-selector.json",
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
        operation_inputs = cast(dict[str, Any], operation["inputs"])

        def reject(mutator: Any, message: str) -> None:
            candidate = json.loads(json.dumps(operation))
            mutator(candidate)
            with self.assertRaisesRegex(SQLiteAuthorityError, message):
                executor.execute_generated_operation(
                    candidate, self.root / "rejected.sqlite", {"project_id": PROJECT}
                )

        reject(lambda value: value.pop("evidence"), "fields are incomplete")
        reject(lambda value: value.update(timeout_seconds=1), "timeout is invalid")
        reject(lambda value: value.update(resources=["wrong"]), "resources are invalid")
        reject(lambda value: value.update(postconditions=["wrong"]), "postconditions are invalid")
        reject(lambda value: value.update(evidence=["wrong"]), "evidence is invalid")
        reject(lambda value: value.update(operation_id=""), "identity is invalid")
        reject(lambda value: value.update(inputs={}), "binding is invalid")
        reject(lambda value: value["inputs"].update(backend="git"), "binding is invalid")
        reject(
            lambda value: value["inputs"].update(backup_operation_id="other"),
            "identity is invalid",
        )
        reject(lambda value: value.update(preconditions=[]), "preconditions are invalid")
        reject(lambda value: value.update(durable_record="wrong"), "durability contract is invalid")
        operation_inputs["fencing_token"] = "stale-fence"  # noqa: S105
        with self.assertRaisesRegex(SQLiteAuthorityError, "fencing or selector identity"):
            executor.execute_generated_operation(
                operation, self.root / "forged.sqlite", {"project_id": PROJECT}
            )
        operation_inputs["fencing_token"] = "fence"  # noqa: S105
        with patch.object(
            self.adapter, "backup_bound", return_value={"backup_verified": True}
        ) as backup:
            result = executor.execute_generated_operation(
                operation, self.root / "backup.sqlite", {"project_id": PROJECT}
            )
        self.assertEqual(
            {
                "operation_id": "campaign:backup",
                "opcode": "backend.backup",
                "outcome": "completed",
                "backup_verified": True,
            },
            result,
        )
        journal_record = json.loads(journal.read_text(encoding="utf-8"))["records"][-1]
        self.assertEqual("success", journal_record["outcome"])
        self.assertEqual({"backup_verified": True}, journal_record["result"])
        backup.assert_called_once()
        with self.assertRaisesRegex(SQLiteAuthorityError, "journal identity"):
            executor.execute_generated_operation(
                operation, self.root / "replayed.sqlite", {"project_id": PROJECT}
            )
        operation["opcode"] = "authority.atomic_replace"
        with self.assertRaisesRegex(SQLiteAuthorityError, "unsupported"):
            executor.execute_generated_operation(operation, self.root / "backup.sqlite", {})

    def test_selector_binding_requires_current_held_barrier_identity(self) -> None:
        journal = self.root / "selector-journal.json"
        journal.write_text('{"status":"running","phase":"backup","records":[]}\n')
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        snapshot = executor.assert_selector_binding("runtime-selector.json", 1, "barrier", "fence")
        self.assertEqual(1, snapshot.control.identity.state_revision)
        with self.assertRaisesRegex(SQLiteAuthorityError, "binding is invalid"):
            executor.assert_selector_binding("runtime-selector.json", 2, "barrier", "fence")
        with self.assertRaisesRegex(SQLiteAuthorityError, "binding is invalid"):
            executor.assert_selector_binding("runtime-selector.json", True, "barrier", "fence")
        with self.assertRaisesRegex(SQLiteAuthorityError, "binding is invalid"):
            executor.assert_selector_binding("../runtime-selector.json", 1, "barrier", "fence")
        with self.assertRaisesRegex(SQLiteAuthorityError, "binding is invalid"):
            absolute_selector = str(Path(tempfile.gettempdir()) / "runtime-selector.json")
            executor.assert_selector_binding(
                absolute_selector,
                1,
                "barrier",
                "fence",
            )
        with (
            self.assertRaisesRegex(SQLiteAuthorityError, "selector root must be absolute"),
            executor.selector_visibility_scope(
                "runtime-selector.json", 1, "barrier", "fence", selector_root=Path("relative")
            ),
        ):
            self.fail("unbound selector publication was admitted")
        selector_root = self.root / "runtime"
        selector_root.mkdir(mode=0o700)
        selector = selector_root / "runtime-selector.json"
        selector.write_text("{}\n", encoding="utf-8")
        selector.chmod(0o600)
        with executor.selector_visibility_scope(
            "runtime-selector.json", 1, "barrier", "fence", selector_root=selector_root
        ) as held:
            self.assertEqual(snapshot, held)
        commit_runtime_selector(selector, "v0.3.5", "v0.3.4")
        self.assertEqual(
            "committed",
            executor.reconcile_selector_publication(
                "runtime-selector.json",
                selector_root,
                1,
                "barrier",
                "fence",
                before_active_release="v0.3.4",
                before_previous_release="v0.3.3",
                after_active_release="v0.3.5",
                after_previous_release="v0.3.4",
            ),
        )
        selector.write_text(
            '{"active_release":"v0.3.4","previous_release":"v0.3.3","schema_version":1}\n',
            encoding="utf-8",
        )
        self.assertEqual(
            "not-committed",
            executor.reconcile_selector_publication(
                "runtime-selector.json",
                selector_root,
                1,
                "barrier",
                "fence",
                before_active_release="v0.3.4",
                before_previous_release="v0.3.3",
                after_active_release="v0.3.5",
                after_previous_release="v0.3.4",
            ),
        )
        selector.write_text(
            '{"active_release":"v0.3.7","previous_release":"v0.3.6","schema_version":1}\n',
            encoding="utf-8",
        )
        with self.assertRaisesRegex(SQLiteAuthorityError, "unknown release identity"):
            executor.reconcile_selector_publication(
                "runtime-selector.json",
                selector_root,
                1,
                "barrier",
                "fence",
                before_active_release="v0.3.4",
                before_previous_release="v0.3.3",
                after_active_release="v0.3.5",
                after_previous_release="v0.3.4",
            )
        with (
            self.assertRaisesRegex(SQLiteAuthorityError, "unknown release identity"),
            patch.object(
                executor,
                "_selector_path_identity",
                side_effect=[(1, 2), SQLiteAuthorityError("injected identity failure")],
            ),
        ):
            executor.reconcile_selector_publication(
                "runtime-selector.json",
                selector_root,
                1,
                "barrier",
                "fence",
                before_active_release="v0.3.4",
                before_previous_release="v0.3.3",
                after_active_release="v0.3.5",
                after_previous_release="v0.3.4",
            )
        with self.assertRaisesRegex(SQLiteAuthorityError, "pairs must differ"):
            executor.reconcile_selector_publication(
                "runtime-selector.json",
                selector_root,
                1,
                "barrier",
                "fence",
                before_active_release="v0.3.4",
                before_previous_release="v0.3.3",
                after_active_release="v0.3.4",
                after_previous_release="v0.3.3",
            )
        with self.assertRaisesRegex(SQLiteAuthorityError, "identity is invalid"):
            executor.reconcile_selector_publication(
                "runtime-selector.json",
                selector_root,
                1,
                "barrier",
                "fence",
                before_active_release="v0.3.4",
                before_previous_release="v0.3.3",
                after_active_release="x" * 129,
                after_previous_release="v0.3.4",
            )
        with (
            self.assertRaisesRegex(SQLiteAuthorityError, "selector target identity changed"),
            executor.selector_visibility_scope(
                "runtime-selector.json", 1, "barrier", "fence", selector_root=selector_root
            ),
        ):
            selector.write_text(
                '{"active_release":"v0.3.5","previous_release":"v0.3.4",'
                '"schema_version":1,"padding":"changed"}\n',
                encoding="utf-8",
            )
        with self.assertRaisesRegex(SQLiteAuthorityError, "selector target is unsafe"):
            selector.chmod(0o644)
            with executor.selector_visibility_scope(
                "runtime-selector.json", 1, "barrier", "fence", selector_root=selector_root
            ):
                self.fail("unsafe selector was admitted")
        selector.chmod(0o600)
        alias = selector_root / "alias.json"
        alias.symlink_to(selector)
        with (
            self.assertRaisesRegex(SQLiteAuthorityError, "selector target is unsafe"),
            executor.selector_visibility_scope(
                "alias.json", 1, "barrier", "fence", selector_root=selector_root
            ),
        ):
            self.fail("symlink selector was admitted")
        linked_root = self.root / "linked-runtime"
        linked_root.symlink_to(selector_root, target_is_directory=True)
        with (
            self.assertRaisesRegex(SQLiteAuthorityError, "selector root contains a symlink"),
            executor.selector_visibility_scope(
                "runtime-selector.json", 1, "barrier", "fence", selector_root=linked_root
            ),
        ):
            self.fail("symlink root was admitted")
        selector.chmod(0o600)
        with (
            self.assertRaisesRegex(SQLiteAuthorityError, "selector target identity changed"),
            executor.selector_visibility_scope(
                "runtime-selector.json", 1, "barrier", "fence", selector_root=selector_root
            ),
        ):
            replacement = selector_root / ".replacement"
            replacement.write_text("replacement\n", encoding="utf-8")
            replacement.chmod(0o600)
            replacement.replace(selector)
        selector.write_text("{}\n", encoding="utf-8")
        with (
            self.assertRaisesRegex(SQLiteAuthorityError, "selector target identity changed"),
            executor.selector_visibility_scope(
                "runtime-selector.json", 1, "barrier", "fence", selector_root=selector_root
            ),
        ):
            replacement_root = self.root / "replacement-runtime"
            replacement_root.mkdir(mode=0o700)
            replacement_root.joinpath("runtime-selector.json").write_text("{}\n", encoding="utf-8")
            replacement_root.joinpath("runtime-selector.json").chmod(0o600)
            old_root = selector_root
            old_root.rename(self.root / "old-runtime")
            replacement_root.rename(old_root)
        ancestor = self.root / "selector-parent"
        nested_root = ancestor / "runtime"
        nested_root.mkdir(parents=True, mode=0o700)
        nested_selector = nested_root / "runtime-selector.json"
        nested_selector.write_text("{}\n", encoding="utf-8")
        nested_selector.chmod(0o600)
        with (
            self.assertRaisesRegex(SQLiteAuthorityError, "selector target identity changed"),
            executor.selector_visibility_scope(
                "runtime-selector.json", 1, "barrier", "fence", selector_root=nested_root
            ),
        ):
            replacement_ancestor = self.root / "selector-parent-new"
            replacement_nested = replacement_ancestor / "runtime"
            replacement_nested.mkdir(parents=True, mode=0o700)
            replacement_selector = replacement_nested / "runtime-selector.json"
            replacement_selector.write_text("{}\n", encoding="utf-8")
            replacement_selector.chmod(0o600)
            ancestor.rename(self.root / "selector-parent-old")
            replacement_ancestor.rename(ancestor)
        clean_root = self.root / "runtime-clean"
        clean_root.mkdir(mode=0o700)
        clean_selector = clean_root / "runtime-selector.json"
        clean_selector.write_text("{}\n", encoding="utf-8")
        clean_selector.chmod(0o600)
        with (
            self.assertRaisesRegex(RuntimeError, "publication failed"),
            executor.selector_visibility_scope(
                "runtime-selector.json", 1, "barrier", "fence", selector_root=clean_root
            ),
        ):
            raise RuntimeError("publication failed")
        with (
            self.assertRaisesRegex(SQLiteAuthorityError, "durable lifecycle state changed"),
            executor.selector_visibility_scope(
                "runtime-selector.json", 1, "barrier", "fence", selector_root=selector_root
            ),
        ):
            journal.write_text('{"status":"running","phase":"preflight","records":[]}\n')

    def test_selector_visibility_scope_releases_lock_on_process_abort(self) -> None:
        journal = self.root / "selector-abort-journal.json"
        journal.write_text('{"status":"running","phase":"backup","records":[]}\n')
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        selector_root = self.root / "selector-abort-runtime"
        selector_root.mkdir(mode=0o700)
        selector = selector_root / "runtime-selector.json"
        selector.write_text("{}\n", encoding="utf-8")
        selector.chmod(0o600)

        with (
            self.assertRaises(KeyboardInterrupt),
            executor.selector_visibility_scope(
                "runtime-selector.json", 1, "barrier", "fence", selector_root=selector_root
            ),
        ):
            raise KeyboardInterrupt

        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_selector_descriptor_digest_failures_are_fail_closed(self) -> None:
        root = self.root / "digest-runtime"
        root.mkdir(mode=0o700)
        target = root / "selector.json"
        target.write_text("{}\n", encoding="utf-8")
        target.chmod(0o600)
        with (
            patch("tools.sqlite_authority_adapter.os.open", side_effect=OSError("replaced")),
            self.assertRaisesRegex(SQLiteAuthorityError, "identity unavailable"),
        ):
            SQLiteLifecycleExecutor._selector_path_identity(root, "selector.json")
        chunks = [b"x" * 65536] * 257 + [b""]
        with (
            patch("tools.sqlite_authority_adapter.os.read", side_effect=chunks),
            self.assertRaisesRegex(SQLiteAuthorityError, "too large"),
        ):
            SQLiteLifecycleExecutor._selector_path_identity(root, "selector.json")
        descriptor = os.open(target, os.O_RDONLY | os.O_NOFOLLOW)
        try:
            status = os.fstat(descriptor)
            altered = SimpleNamespace(
                st_dev=status.st_dev,
                st_ino=status.st_ino + 1,
                st_uid=status.st_uid,
                st_mode=status.st_mode,
                st_nlink=status.st_nlink,
            )
            with (
                patch("tools.sqlite_authority_adapter.os.fstat", side_effect=[status, altered]),
                self.assertRaisesRegex(SQLiteAuthorityError, "identity changed"),
            ):
                SQLiteLifecycleExecutor._selector_path_identity(root, "selector.json")
        finally:
            os.close(descriptor)

    def test_generated_contract_backup_operation_dispatches_directly(self) -> None:
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

        document = generate(
            {
                "operation_id": "campaign",
                "backend": "sqlite",
                "selector_ref": "runtime-selector.json",
                "expected_state_revision": 1,
                "barrier_id": "barrier",
                "fencing_token": "fence",
                "from": release("v0.3.5", "a"),
                "to": release("v0.3.6", "b"),
            }
        )
        operation = document["phases"][3]["operation"]
        journal = self.root / "generated-journal.json"
        journal.write_text(
            '{"status":"running","phase":"backup","records":[{"operation_id":"campaign",'
            '"step_id":"campaign:backup","phase":"backup","outcome":"started",'
            '"context":{"selector_ref":"runtime-selector.json","state_revision":1,'
            '"durable_barrier_id":"barrier","fencing_token":"fence"}}]}\n',
            encoding="utf-8",
        )
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        with patch.object(self.adapter, "backup_bound", return_value={"backup_verified": True}):
            result = executor.execute_generated_operation(
                operation, self.root / "generated-backup.sqlite", {"project_id": PROJECT}
            )
        self.assertEqual("campaign:backup", result["operation_id"])
        self.assertEqual("completed", result["outcome"])

    def test_generated_backup_campaign_uses_real_sqlite_backup_and_durable_outcome(self) -> None:
        with closing(sqlite3.connect(self.authority)) as connection, connection:
            connection.execute("CREATE TABLE metadata (key TEXT PRIMARY KEY, value TEXT NOT NULL)")
            connection.executemany(
                "INSERT INTO metadata(key, value) VALUES (?, ?)",
                (
                    ("schema_version", "1"),
                    ("backend", "sqlite"),
                    ("project_id", PROJECT),
                    ("state_repository", "state-repository"),
                    ("product_repository", "product-repository"),
                    ("state", "active"),
                ),
            )
        journal = self.root / "real-generated-journal.json"
        journal.write_text(
            '{"status":"running","phase":"backup","records":[{"operation_id":"campaign",'
            '"step_id":"campaign:backup","phase":"backup","outcome":"started",'
            '"context":{"selector_ref":"runtime-selector.json","state_revision":1,'
            '"durable_barrier_id":"barrier","fencing_token":"fence"}}]}\n',
            encoding="utf-8",
        )
        operation = {
            "operation_id": "campaign:backup",
            "opcode": "backend.backup",
            "inputs": {
                "backend": "sqlite",
                "selector_ref": "runtime-selector.json",
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
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        destination = self.root / "real-generated-backup.sqlite"
        result = executor.execute_generated_operation(
            operation,
            destination,
            {
                "project_id": PROJECT,
                "state_repository": "state-repository",
                "product_repository": "product-repository",
            },
        )
        self.assertEqual("completed", result["outcome"])
        self.assertTrue(result["binding_verified"])
        with closing(sqlite3.connect(destination)) as connection, connection:
            self.assertEqual(("clean",), connection.execute("SELECT body FROM records").fetchone())
            self.assertEqual(
                ("active",),
                connection.execute("SELECT value FROM metadata WHERE key = 'state'").fetchone(),
            )
        record = json.loads(journal.read_text(encoding="utf-8"))["records"][-1]
        self.assertEqual("success", record["outcome"])
        self.assertEqual("campaign:backup", record["step_id"])
        self.assertEqual(result["binding_verified"], record["result"]["binding_verified"])
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_generated_backup_rejects_existing_destination_without_journal_mutation(self) -> None:
        with closing(sqlite3.connect(self.authority)) as connection, connection:
            connection.execute("CREATE TABLE metadata (key TEXT PRIMARY KEY, value TEXT NOT NULL)")
            connection.executemany(
                "INSERT INTO metadata(key, value) VALUES (?, ?)",
                (
                    ("schema_version", "1"),
                    ("backend", "sqlite"),
                    ("project_id", PROJECT),
                    ("state_repository", "state-repository"),
                    ("product_repository", "product-repository"),
                    ("state", "active"),
                ),
            )
        journal = self.root / "real-failure-journal.json"
        journal.write_text(
            '{"status":"running","phase":"backup","records":[{"operation_id":"campaign",'
            '"step_id":"campaign:backup","phase":"backup","outcome":"started",'
            '"context":{"selector_ref":"runtime-selector.json","state_revision":1,'
            '"durable_barrier_id":"barrier","fencing_token":"fence"}}]}\n',
            encoding="utf-8",
        )
        operation = {
            "operation_id": "campaign:backup",
            "opcode": "backend.backup",
            "inputs": {
                "backend": "sqlite",
                "selector_ref": "runtime-selector.json",
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
        destination = self.root / "existing-backup.sqlite"
        destination.write_bytes(b"immutable destination")
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        before = journal.read_bytes()
        with self.assertRaisesRegex(SQLiteAuthorityError, "generated SQLite backup failed"):
            executor.execute_generated_operation(
                operation,
                destination,
                {
                    "project_id": PROJECT,
                    "state_repository": "state-repository",
                    "product_repository": "product-repository",
                },
            )
        self.assertEqual(before, journal.read_bytes())
        self.assertEqual(b"immutable destination", destination.read_bytes())
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_generated_backup_abort_releases_lock_and_preserves_journal(self) -> None:
        journal = self.root / "generated-abort-journal.json"
        journal.write_text(
            '{"status":"running","phase":"backup","records":[{"operation_id":"campaign",'
            '"step_id":"campaign:backup","phase":"backup","outcome":"started",'
            '"context":{"selector_ref":"runtime-selector.json","state_revision":1,'
            '"durable_barrier_id":"barrier","fencing_token":"fence"}}]}\n',
            encoding="utf-8",
        )
        operation = {
            "operation_id": "campaign:backup",
            "opcode": "backend.backup",
            "inputs": {
                "backend": "sqlite",
                "selector_ref": "runtime-selector.json",
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
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        before = executor.snapshot()
        before_journal = journal.read_bytes()
        with (
            patch.object(self.adapter, "backup_bound", side_effect=KeyboardInterrupt),
            self.assertRaises(KeyboardInterrupt),
        ):
            executor.execute_generated_operation(
                operation, self.root / "generated-abort.sqlite", {}
            )
        self.assertEqual(before, executor.snapshot())
        self.assertEqual(before_journal, journal.read_bytes())
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_generated_backup_publication_abort_preserves_journal(self) -> None:
        journal = self.root / "generated-publication-abort-journal.json"
        journal.write_text(
            '{"status":"running","phase":"backup","records":[{"operation_id":"campaign",'
            '"step_id":"campaign:backup","phase":"backup","outcome":"started",'
            '"context":{"selector_ref":"runtime-selector.json","state_revision":1,'
            '"durable_barrier_id":"barrier","fencing_token":"fence"}}]}\n',
            encoding="utf-8",
        )
        operation = {
            "operation_id": "campaign:backup",
            "opcode": "backend.backup",
            "inputs": {
                "backend": "sqlite",
                "selector_ref": "runtime-selector.json",
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
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        before_journal = journal.read_bytes()
        with (
            patch.object(self.adapter, "backup_bound", return_value={"backup_verified": True}),
            patch("tools.sqlite_authority_adapter.os.fsync", side_effect=KeyboardInterrupt),
            self.assertRaises(KeyboardInterrupt),
        ):
            executor.execute_generated_operation(
                operation, self.root / "generated-publication-abort.sqlite", {}
            )
        self.assertEqual(before_journal, journal.read_bytes())
        self.assertFalse(list(journal.parent.glob(".upgrade-journal-*.json")))
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_generated_backup_replace_failure_preserves_journal(self) -> None:
        journal = self.root / "generated-replace-failure-journal.json"
        journal.write_text(
            '{"status":"running","phase":"backup","records":[{"operation_id":"campaign",'
            '"step_id":"campaign:backup","phase":"backup","outcome":"started",'
            '"context":{"selector_ref":"runtime-selector.json","state_revision":1,'
            '"durable_barrier_id":"barrier","fencing_token":"fence"}}]}\n',
            encoding="utf-8",
        )
        operation = {
            "operation_id": "campaign:backup",
            "opcode": "backend.backup",
            "inputs": {
                "backend": "sqlite",
                "selector_ref": "runtime-selector.json",
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
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        before_journal = journal.read_bytes()
        with (
            patch.object(self.adapter, "backup_bound", return_value={"backup_verified": True}),
            patch(
                "tools.sqlite_authority_adapter.Path.replace",
                side_effect=OSError("injected journal replace failure"),
            ),
            self.assertRaisesRegex(SQLiteAuthorityError, "publication failed"),
        ):
            executor.execute_generated_operation(
                operation, self.root / "generated-replace-failure.sqlite", {}
            )
        self.assertEqual(before_journal, journal.read_bytes())
        self.assertFalse(list(journal.parent.glob(".upgrade-journal-*.json")))
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_generated_backup_directory_fsync_failure_retains_published_outcome(self) -> None:
        journal = self.root / "generated-directory-fsync-failure-journal.json"
        journal.write_text(
            '{"status":"running","phase":"backup","records":[{"operation_id":"campaign",'
            '"step_id":"campaign:backup","phase":"backup","outcome":"started",'
            '"context":{"selector_ref":"runtime-selector.json","state_revision":1,'
            '"durable_barrier_id":"barrier","fencing_token":"fence"}}]}\n',
            encoding="utf-8",
        )
        operation = {
            "operation_id": "campaign:backup",
            "opcode": "backend.backup",
            "inputs": {
                "backend": "sqlite",
                "selector_ref": "runtime-selector.json",
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
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        calls = 0
        original_fsync = os.fsync

        def fail_directory_fsync(descriptor: int) -> None:
            nonlocal calls
            calls += 1
            if calls == 2:
                raise OSError("injected directory fsync failure")
            original_fsync(descriptor)

        with (
            patch.object(self.adapter, "backup_bound", return_value={"backup_verified": True}),
            patch("tools.sqlite_authority_adapter.os.fsync", side_effect=fail_directory_fsync),
            self.assertRaisesRegex(SQLiteAuthorityError, "publication failed"),
        ):
            executor.execute_generated_operation(
                operation, self.root / "generated-directory-fsync-failure.sqlite", {}
            )
        record = json.loads(journal.read_text(encoding="utf-8"))["records"][-1]
        self.assertEqual("success", record["outcome"])
        self.assertEqual({"backup_verified": True}, record["result"])
        self.assertFalse(list(journal.parent.glob(".upgrade-journal-*.json")))
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_generated_backup_directory_close_retry_failure_is_fail_closed(self) -> None:
        journal = self.root / "generated-directory-close-failure-journal.json"
        journal.write_text(
            '{"status":"running","phase":"backup","records":[{"operation_id":"campaign",'
            '"step_id":"campaign:backup","phase":"backup","outcome":"started",'
            '"context":{"selector_ref":"runtime-selector.json","state_revision":1,'
            '"durable_barrier_id":"barrier","fencing_token":"fence"}}]}\n',
            encoding="utf-8",
        )
        operation = {
            "operation_id": "campaign:backup",
            "opcode": "backend.backup",
            "inputs": {
                "backend": "sqlite",
                "selector_ref": "runtime-selector.json",
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
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        close_calls = 0

        def fail_directory_close(_descriptor: int) -> None:
            nonlocal close_calls
            close_calls += 1
            raise OSError("injected directory close failure")

        real_close_directory = SQLiteLifecycleExecutor._close_directory_with_retry

        def fail_close_retry(directory: int) -> None:
            with patch("tools.sqlite_authority_adapter.os.close", side_effect=fail_directory_close):
                real_close_directory(directory)

        with (
            patch.object(self.adapter, "backup_bound", return_value={"backup_verified": True}),
            patch.object(
                SQLiteLifecycleExecutor,
                "_close_directory_with_retry",
                side_effect=fail_close_retry,
            ),
            self.assertRaisesRegex(SQLiteAuthorityError, "publication failed"),
        ):
            executor.execute_generated_operation(
                operation, self.root / "generated-directory-close-failure.sqlite", {}
            )
        record = json.loads(journal.read_text(encoding="utf-8"))["records"][-1]
        self.assertEqual("success", record["outcome"])
        self.assertEqual({"backup_verified": True}, record["result"])
        self.assertEqual(2, close_calls)
        self.assertFalse(list(journal.parent.glob(".upgrade-journal-*.json")))
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_generated_backup_cleanup_failure_is_explicit_after_publication(self) -> None:
        journal = self.root / "generated-cleanup-failure-journal.json"
        journal.write_text(
            '{"status":"running","phase":"backup","records":[{"operation_id":"campaign",'
            '"step_id":"campaign:backup","phase":"backup","outcome":"started",'
            '"context":{"selector_ref":"runtime-selector.json","state_revision":1,'
            '"durable_barrier_id":"barrier","fencing_token":"fence"}}]}\n',
            encoding="utf-8",
        )
        operation = {
            "operation_id": "campaign:backup",
            "opcode": "backend.backup",
            "inputs": {
                "backend": "sqlite",
                "selector_ref": "runtime-selector.json",
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
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)

        def fail_temporary_cleanup(**_: Any) -> None:
            raise OSError("injected temporary cleanup failure")

        with (
            patch.object(self.adapter, "backup_bound", return_value={"backup_verified": True}),
            patch.object(Path, "unlink", side_effect=fail_temporary_cleanup),
            self.assertRaisesRegex(SQLiteAuthorityError, "temporary cleanup failed"),
        ):
            executor.execute_generated_operation(
                operation, self.root / "generated-cleanup-failure.sqlite", {}
            )
        record = json.loads(journal.read_text(encoding="utf-8"))["records"][-1]
        self.assertEqual("success", record["outcome"])
        self.assertEqual({"backup_verified": True}, record["result"])
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_generated_backup_directory_open_failure_retains_published_outcome(self) -> None:
        journal = self.root / "generated-directory-open-failure-journal.json"
        journal.write_text(
            '{"status":"running","phase":"backup","records":[{"operation_id":"campaign",'
            '"step_id":"campaign:backup","phase":"backup","outcome":"started",'
            '"context":{"selector_ref":"runtime-selector.json","state_revision":1,'
            '"durable_barrier_id":"barrier","fencing_token":"fence"}}]}\n',
            encoding="utf-8",
        )
        operation = {
            "operation_id": "campaign:backup",
            "opcode": "backend.backup",
            "inputs": {
                "backend": "sqlite",
                "selector_ref": "runtime-selector.json",
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
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        original_open = os.open

        def fail_directory_open(
            path: str | bytes, flags: int, mode: int = 0o777, **kwargs: Any
        ) -> int:
            path_value = path.decode() if isinstance(path, bytes) else path
            if flags & os.O_DIRECTORY and not kwargs and Path(path_value) == journal.parent:
                raise OSError("injected journal directory open failure")
            return original_open(path, flags, mode, **kwargs)

        with (
            patch.object(self.adapter, "backup_bound", return_value={"backup_verified": True}),
            patch("tools.sqlite_authority_adapter.os.open", side_effect=fail_directory_open),
            self.assertRaisesRegex(SQLiteAuthorityError, "publication failed"),
        ):
            executor.execute_generated_operation(
                operation, self.root / "generated-directory-open-failure.sqlite", {}
            )
        record = json.loads(journal.read_text(encoding="utf-8"))["records"][-1]
        self.assertEqual("success", record["outcome"])
        self.assertEqual({"backup_verified": True}, record["result"])
        self.assertFalse(list(journal.parent.glob(".upgrade-journal-*.json")))
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_generated_backup_temporary_write_failure_preserves_journal(self) -> None:
        journal = self.root / "generated-write-failure-journal.json"
        journal.write_text(
            '{"status":"running","phase":"backup","records":[{"operation_id":"campaign",'
            '"step_id":"campaign:backup","phase":"backup","outcome":"started",'
            '"context":{"selector_ref":"runtime-selector.json","state_revision":1,'
            '"durable_barrier_id":"barrier","fencing_token":"fence"}}]}\n',
            encoding="utf-8",
        )
        operation = {
            "operation_id": "campaign:backup",
            "opcode": "backend.backup",
            "inputs": {
                "backend": "sqlite",
                "selector_ref": "runtime-selector.json",
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
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        before_journal = journal.read_bytes()
        original_fdopen = os.fdopen

        class FailingStream:
            def __init__(self, descriptor: int, *args: object, **kwargs: object) -> None:
                self.stream = cast(Any, original_fdopen)(descriptor, *args, **kwargs)

            def __enter__(self) -> FailingStream:
                self.stream.__enter__()
                return self

            def __exit__(self, *args: object) -> bool:
                return bool(self.stream.__exit__(*args))

            def write(self, _: str) -> int:
                raise OSError("injected temporary journal write failure")

        with (
            patch.object(self.adapter, "backup_bound", return_value={"backup_verified": True}),
            patch("tools.sqlite_authority_adapter.os.fdopen", side_effect=FailingStream),
            self.assertRaisesRegex(SQLiteAuthorityError, "publication failed"),
        ):
            executor.execute_generated_operation(
                operation, self.root / "generated-write-failure.sqlite", {}
            )
        self.assertEqual(before_journal, journal.read_bytes())
        self.assertFalse(list(journal.parent.glob(".upgrade-journal-*.json")))
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_generated_backup_temporary_flush_failure_preserves_journal(self) -> None:
        journal = self.root / "generated-flush-failure-journal.json"
        journal.write_text(
            '{"status":"running","phase":"backup","records":[{"operation_id":"campaign",'
            '"step_id":"campaign:backup","phase":"backup","outcome":"started",'
            '"context":{"selector_ref":"runtime-selector.json","state_revision":1,'
            '"durable_barrier_id":"barrier","fencing_token":"fence"}}]}\n',
            encoding="utf-8",
        )
        operation = {
            "operation_id": "campaign:backup",
            "opcode": "backend.backup",
            "inputs": {
                "backend": "sqlite",
                "selector_ref": "runtime-selector.json",
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
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        before_journal = journal.read_bytes()
        original_fdopen = os.fdopen

        class FailingStream:
            def __init__(self, descriptor: int, *args: object, **kwargs: object) -> None:
                self.stream = cast(Any, original_fdopen)(descriptor, *args, **kwargs)

            def __enter__(self) -> FailingStream:
                self.stream.__enter__()
                return self

            def __exit__(self, *args: object) -> bool:
                return bool(self.stream.__exit__(*args))

            def write(self, value: str) -> int:
                return int(self.stream.write(value))

            def flush(self) -> None:
                raise OSError("injected temporary journal flush failure")

        with (
            patch.object(self.adapter, "backup_bound", return_value={"backup_verified": True}),
            patch("tools.sqlite_authority_adapter.os.fdopen", side_effect=FailingStream),
            self.assertRaisesRegex(SQLiteAuthorityError, "publication failed"),
        ):
            executor.execute_generated_operation(
                operation, self.root / "generated-flush-failure.sqlite", {}
            )
        self.assertEqual(before_journal, journal.read_bytes())
        self.assertFalse(list(journal.parent.glob(".upgrade-journal-*.json")))
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_generated_backup_fdopen_failure_preserves_journal(self) -> None:
        journal = self.root / "generated-fdopen-failure-journal.json"
        journal.write_text(
            '{"status":"running","phase":"backup","records":[{"operation_id":"campaign",'
            '"step_id":"campaign:backup","phase":"backup","outcome":"started",'
            '"context":{"selector_ref":"runtime-selector.json","state_revision":1,'
            '"durable_barrier_id":"barrier","fencing_token":"fence"}}]}\n',
            encoding="utf-8",
        )
        operation = {
            "operation_id": "campaign:backup",
            "opcode": "backend.backup",
            "inputs": {
                "backend": "sqlite",
                "selector_ref": "runtime-selector.json",
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
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        before_journal = journal.read_bytes()
        original_close = os.close
        original_mkstemp = tempfile.mkstemp
        allocated: list[int] = []
        closed: list[int] = []

        def record_mkstemp(*args: Any, **kwargs: Any) -> tuple[int, str]:
            result = original_mkstemp(*args, **kwargs)
            allocated.append(result[0])
            return result

        def record_close(descriptor: int) -> None:
            closed.append(descriptor)
            original_close(descriptor)

        with (
            patch.object(self.adapter, "backup_bound", return_value={"backup_verified": True}),
            patch(
                "tools.sqlite_authority_adapter.os.fdopen",
                side_effect=OSError("injected temporary journal fdopen failure"),
            ),
            patch("tools.sqlite_authority_adapter.tempfile.mkstemp", side_effect=record_mkstemp),
            patch("tools.sqlite_authority_adapter.os.close", side_effect=record_close),
            self.assertRaisesRegex(SQLiteAuthorityError, "publication failed"),
        ):
            executor.execute_generated_operation(
                operation, self.root / "generated-fdopen-failure.sqlite", {}
            )
        self.assertEqual(before_journal, journal.read_bytes())
        self.assertEqual(1, len(allocated))
        self.assertIn(allocated[0], closed)
        self.assertFalse(list(journal.parent.glob(".upgrade-journal-*.json")))
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_generated_backup_directory_close_failure_retries_and_closes(self) -> None:
        journal = self.root / "generated-directory-close-failure-journal.json"
        journal.write_text(
            '{"status":"running","phase":"backup","records":[{"operation_id":"campaign",'
            '"step_id":"campaign:backup","phase":"backup","outcome":"started",'
            '"context":{"selector_ref":"runtime-selector.json","state_revision":1,'
            '"durable_barrier_id":"barrier","fencing_token":"fence"}}]}\n',
            encoding="utf-8",
        )
        operation = {
            "operation_id": "campaign:backup",
            "opcode": "backend.backup",
            "inputs": {
                "backend": "sqlite",
                "selector_ref": "runtime-selector.json",
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
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        original_open = os.open
        original_close = os.close
        directory_fds: list[int] = []
        close_attempts = 0

        def record_directory_open(
            path: str | bytes, flags: int, mode: int = 0o777, **kwargs: Any
        ) -> int:
            fd = int(cast(Any, original_open)(path, flags, mode, **kwargs))
            path_value = path.decode() if isinstance(path, bytes) else path
            if flags & os.O_DIRECTORY and not kwargs and Path(path_value) == journal.parent:
                directory_fds.append(fd)
            return fd

        def fail_directory_close(descriptor: int) -> None:
            nonlocal close_attempts
            if descriptor in directory_fds:
                close_attempts += 1
                if close_attempts == 1:
                    raise OSError("injected transient journal directory close failure")
            original_close(descriptor)

        with (
            patch.object(self.adapter, "backup_bound", return_value={"backup_verified": True}),
            patch("tools.sqlite_authority_adapter.os.open", side_effect=record_directory_open),
            patch("tools.sqlite_authority_adapter.os.close", side_effect=fail_directory_close),
        ):
            result = executor.execute_generated_operation(
                operation, self.root / "generated-directory-close-failure.sqlite", {}
            )
        self.assertEqual("completed", result["outcome"])
        self.assertEqual(1, len(directory_fds))
        self.assertEqual(2, close_attempts)
        record = json.loads(journal.read_text(encoding="utf-8"))["records"][-1]
        self.assertEqual("success", record["outcome"])
        self.assertEqual({"backup_verified": True}, record["result"])
        self.assertFalse(list(journal.parent.glob(".upgrade-journal-*.json")))
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_generated_backup_serialization_failure_preserves_journal(self) -> None:
        journal = self.root / "generated-serialize-failure-journal.json"
        journal.write_text(
            '{"status":"running","phase":"backup","records":[{"operation_id":"campaign",'
            '"step_id":"campaign:backup","phase":"backup","outcome":"started",'
            '"context":{"selector_ref":"runtime-selector.json","state_revision":1,'
            '"durable_barrier_id":"barrier","fencing_token":"fence"}}]}\n',
            encoding="utf-8",
        )
        operation = {
            "operation_id": "campaign:backup",
            "opcode": "backend.backup",
            "inputs": {
                "backend": "sqlite",
                "selector_ref": "runtime-selector.json",
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
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        before_journal = journal.read_bytes()
        original_dumps = json.dumps

        def fail_generated_document(value: object, *args: Any, **kwargs: Any) -> str:
            if isinstance(value, dict) and "records" in value:
                raise OSError("injected generated journal serialization failure")
            return str(cast(Any, original_dumps)(value, *args, **kwargs))

        with (
            patch.object(self.adapter, "backup_bound", return_value={"backup_verified": True}),
            patch(
                "tools.sqlite_authority_adapter.json.dumps",
                side_effect=fail_generated_document,
            ),
            self.assertRaisesRegex(SQLiteAuthorityError, "publication failed"),
        ):
            executor.execute_generated_operation(
                operation, self.root / "generated-serialize-failure.sqlite", {}
            )
        self.assertEqual(before_journal, journal.read_bytes())
        self.assertFalse(list(journal.parent.glob(".upgrade-journal-*.json")))
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_generated_backup_rejects_journal_replacement_before_publication(self) -> None:
        journal = self.root / "replacement-journal.json"
        journal.write_text(
            '{"status":"running","phase":"backup","records":[{"operation_id":"campaign",'
            '"step_id":"campaign:backup","phase":"backup","outcome":"started",'
            '"context":{"selector_ref":"runtime-selector.json","state_revision":1,'
            '"durable_barrier_id":"barrier","fencing_token":"fence"}}]}\n',
            encoding="utf-8",
        )
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        operation = {
            "operation_id": "campaign:backup",
            "opcode": "backend.backup",
            "inputs": {
                "backend": "sqlite",
                "selector_ref": "runtime-selector.json",
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

        def replace_journal(*_: object, **__: object) -> dict[str, bool]:
            journal.write_text('{"status":"running","phase":"backup","records":[]}\n')
            return {"backup_verified": True}

        with (
            patch.object(self.adapter, "backup_bound", side_effect=replace_journal),
            self.assertRaisesRegex(SQLiteAuthorityError, "durable state changed"),
        ):
            executor.execute_generated_operation(operation, self.root / "backup.sqlite", {})

    def test_bound_lifecycle_executor_backup_failure_rereads_and_preserves_state(self) -> None:
        journal = self.root / "engine-journal.json"
        journal.write_text('{"status":"running","phase":"backup","records":[]}\n', encoding="utf-8")
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        before = executor.snapshot()
        with (
            patch.object(self.adapter, "backup_bound", side_effect=RuntimeError("injected backup")),
            self.assertRaisesRegex(SQLiteAuthorityError, "lifecycle effect failed"),
        ):
            executor.backup(self.root / "backup.sqlite", {})
        self.assertEqual(before, executor.snapshot())
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_bound_lifecycle_executor_backup_abort_releases_lock(self) -> None:
        journal = self.root / "engine-abort-journal.json"
        journal.write_text('{"status":"running","phase":"backup","records":[]}\n', encoding="utf-8")
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        before = executor.snapshot()
        with (
            patch.object(self.adapter, "backup_bound", side_effect=KeyboardInterrupt),
            self.assertRaises(KeyboardInterrupt),
        ):
            executor.backup(self.root / "backup-abort.sqlite", {})
        self.assertEqual(before, executor.snapshot())
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_bound_lifecycle_executor_restore_failure_rereads_and_preserves_state(self) -> None:
        journal = self.root / "engine-journal.json"
        journal.write_text(
            '{"status":"running","phase":"rollback","records":[]}\n', encoding="utf-8"
        )
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        before = executor.snapshot()
        with (
            patch.object(
                self.adapter, "restore_bound", side_effect=RuntimeError("injected restore")
            ),
            self.assertRaisesRegex(SQLiteAuthorityError, "lifecycle effect failed"),
        ):
            executor.restore(self.root / "backup.sqlite", self.root / "destination.sqlite", {}, {})
        self.assertEqual(before, executor.snapshot())
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_bound_lifecycle_executor_restore_abort_releases_lock(self) -> None:
        journal = self.root / "engine-restore-abort-journal.json"
        journal.write_text(
            '{"status":"running","phase":"rollback","records":[]}\n', encoding="utf-8"
        )
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        before = executor.snapshot()
        with (
            patch.object(self.adapter, "restore_bound", side_effect=KeyboardInterrupt),
            self.assertRaises(KeyboardInterrupt),
        ):
            executor.restore(
                self.root / "backup-abort.sqlite",
                self.root / "destination-abort.sqlite",
                {},
                {},
            )
        self.assertEqual(before, executor.snapshot())
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_bound_lifecycle_executor_rejects_failed_effect_journal_mutation(self) -> None:
        journal = self.root / "engine-journal.json"
        journal.write_text('{"status":"running","phase":"backup","records":[]}\n', encoding="utf-8")
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        before = executor.snapshot()

        def mutate_then_fail(_destination: Path, _binding: dict[str, Any]) -> dict[str, Any]:
            journal.write_text(
                '{"status":"failed","phase":"backup","records":[]}\n', encoding="utf-8"
            )
            raise RuntimeError("injected journal mutation")

        with (
            patch.object(self.adapter, "backup_bound", side_effect=mutate_then_fail),
            self.assertRaisesRegex(SQLiteAuthorityError, "durable lifecycle state changed"),
        ):
            executor.backup(self.root / "backup.sqlite", {})
        self.assertNotEqual(before.journal, executor.snapshot().journal)
        self.assertFalse((self.root / "backup.sqlite").exists())
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_bound_lifecycle_executor_rejects_failed_restore_journal_mutation(self) -> None:
        journal = self.root / "engine-journal.json"
        journal.write_text(
            '{"status":"running","phase":"rollback","records":[]}\n', encoding="utf-8"
        )
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        executor.snapshot()

        def mutate_then_fail(
            _backup: Path,
            _destination: Path,
            _manifest: dict[str, Any],
            _binding: dict[str, Any],
        ) -> None:
            journal.write_text(
                '{"status":"failed","phase":"rollback","records":[]}\n', encoding="utf-8"
            )
            raise RuntimeError("injected restore journal mutation")

        with (
            patch.object(self.adapter, "restore_bound", side_effect=mutate_then_fail),
            self.assertRaisesRegex(SQLiteAuthorityError, "durable lifecycle state changed"),
        ):
            executor.restore(self.root / "backup.sqlite", self.root / "destination.sqlite", {}, {})
        self.assertFalse((self.root / "destination.sqlite").exists())
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_bound_lifecycle_executor_rejects_failed_restore_control_mutation(self) -> None:
        journal = self.root / "engine-journal.json"
        journal.write_text(
            '{"status":"running","phase":"rollback","records":[]}\n', encoding="utf-8"
        )
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        executor.snapshot()

        def mutate_then_fail(
            _backup: Path,
            _destination: Path,
            _manifest: dict[str, Any],
            _binding: dict[str, Any],
        ) -> None:
            # Simulate an external writer changing the barrier during restore.
            with (
                closing(sqlite3.connect(self.session.control_store_path)) as connection,
                connection,
            ):
                connection.execute(
                    "UPDATE barrier_session SET status='ambiguous' WHERE project_id=?",
                    (PROJECT,),
                )
            raise RuntimeError("injected restore control mutation")

        with (
            patch.object(self.adapter, "restore_bound", side_effect=mutate_then_fail),
            self.assertRaisesRegex(SQLiteAuthorityError, "durable lifecycle state changed"),
        ):
            executor.restore(self.root / "backup.sqlite", self.root / "destination.sqlite", {}, {})
        self.assertFalse((self.root / "destination.sqlite").exists())
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_bound_lifecycle_executor_rejects_failed_restore_lock_replacement(self) -> None:
        journal = self.root / "engine-journal.json"
        journal.write_text(
            '{"status":"running","phase":"rollback","records":[]}\n', encoding="utf-8"
        )
        lock = self.session.control_lock_path
        foreign = self.root / "foreign-restore-control.lock"
        foreign.write_bytes(b"foreign lock")
        foreign.chmod(0o600)
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        executor.snapshot()

        def replace_then_fail(
            _backup: Path,
            _destination: Path,
            _manifest: dict[str, Any],
            _binding: dict[str, Any],
        ) -> None:
            original = self.root / "original-restore-control.lock"
            lock.rename(original)
            foreign.rename(lock)
            raise RuntimeError("injected restore lock replacement")

        try:
            with (
                patch.object(self.adapter, "restore_bound", side_effect=replace_then_fail),
                self.assertRaisesRegex(SQLiteAuthorityError, "durable lifecycle state changed"),
            ):
                executor.restore(
                    self.root / "backup.sqlite", self.root / "destination.sqlite", {}, {}
                )
        finally:
            lock.unlink(missing_ok=True)
            (self.root / "original-restore-control.lock").rename(lock)
        self.assertFalse((self.root / "destination.sqlite").exists())
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_bound_lifecycle_executor_rejects_failed_restore_control_replacement(self) -> None:
        journal = self.root / "engine-journal.json"
        journal.write_text(
            '{"status":"running","phase":"rollback","records":[]}\n', encoding="utf-8"
        )
        control = self.session.control_store_path
        foreign = self.root / "foreign-restore-control.sqlite"
        shutil.copy2(control, foreign)
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        executor.snapshot()

        def replace_then_fail(
            _backup: Path,
            _destination: Path,
            _manifest: dict[str, Any],
            _binding: dict[str, Any],
        ) -> None:
            original = self.root / "original-restore-control.sqlite"
            control.rename(original)
            foreign.rename(control)
            raise RuntimeError("injected restore control replacement")

        try:
            with (
                patch.object(self.adapter, "restore_bound", side_effect=replace_then_fail),
                self.assertRaisesRegex(SQLiteAuthorityError, "lifecycle effect failed"),
            ):
                executor.restore(
                    self.root / "backup.sqlite", self.root / "destination.sqlite", {}, {}
                )
        finally:
            control.unlink(missing_ok=True)
            (self.root / "original-restore-control.sqlite").rename(control)
        self.assertFalse((self.root / "destination.sqlite").exists())
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_bound_lifecycle_executor_rejects_failed_restore_control_symlink(self) -> None:
        journal = self.root / "engine-journal.json"
        journal.write_text(
            '{"status":"running","phase":"rollback","records":[]}\n', encoding="utf-8"
        )
        control = self.session.control_store_path
        foreign = self.root / "foreign-restore-control-target.sqlite"
        shutil.copy2(control, foreign)
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        executor.snapshot()

        def replace_then_fail(
            _backup: Path,
            _destination: Path,
            _manifest: dict[str, Any],
            _binding: dict[str, Any],
        ) -> None:
            original = self.root / "original-restore-control.sqlite"
            control.rename(original)
            control.symlink_to(foreign)
            raise RuntimeError("injected restore control symlink")

        try:
            with (
                patch.object(self.adapter, "restore_bound", side_effect=replace_then_fail),
                self.assertRaisesRegex(
                    SQLiteAuthorityError, "lifecycle control store is not private and regular"
                ),
            ):
                executor.restore(
                    self.root / "backup.sqlite", self.root / "destination.sqlite", {}, {}
                )
        finally:
            control.unlink(missing_ok=True)
            (self.root / "original-restore-control.sqlite").rename(control)
        self.assertFalse((self.root / "destination.sqlite").exists())
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_bound_lifecycle_executor_rejects_failed_restore_control_shm_sidecar(self) -> None:
        journal = self.root / "engine-journal.json"
        journal.write_text(
            '{"status":"running","phase":"rollback","records":[]}\n', encoding="utf-8"
        )
        control = self.session.control_store_path
        sidecar = Path(str(control) + "-shm")
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        executor.snapshot()

        def sidecar_then_fail(
            _backup: Path,
            _destination: Path,
            _manifest: dict[str, Any],
            _binding: dict[str, Any],
        ) -> None:
            sidecar.write_bytes(b"foreign SHM sidecar")
            sidecar.chmod(0o600)
            raise RuntimeError("injected restore control SHM sidecar")

        try:
            with (
                patch.object(self.adapter, "restore_bound", side_effect=sidecar_then_fail),
                self.assertRaisesRegex(SQLiteAuthorityError, "lifecycle effect failed"),
            ):
                executor.restore(
                    self.root / "backup.sqlite", self.root / "destination.sqlite", {}, {}
                )
        finally:
            sidecar.unlink(missing_ok=True)
        self.assertFalse((self.root / "destination.sqlite").exists())
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_bound_lifecycle_executor_rejects_failed_restore_unsafe_lock(self) -> None:
        journal = self.root / "engine-journal.json"
        journal.write_text(
            '{"status":"running","phase":"rollback","records":[]}\n', encoding="utf-8"
        )
        lock = self.session.control_lock_path
        foreign = self.root / "unsafe-restore-control.lock"
        foreign.write_bytes(b"foreign lock")
        foreign.chmod(0o644)
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        executor.snapshot()

        def replace_then_fail(
            _backup: Path,
            _destination: Path,
            _manifest: dict[str, Any],
            _binding: dict[str, Any],
        ) -> None:
            original = self.root / "original-restore-control.lock"
            lock.rename(original)
            foreign.rename(lock)
            raise RuntimeError("injected unsafe restore lock")

        try:
            with (
                patch.object(self.adapter, "restore_bound", side_effect=replace_then_fail),
                self.assertRaisesRegex(
                    SQLiteAuthorityError, "lifecycle control lock is not private and regular"
                ),
            ):
                executor.restore(
                    self.root / "backup.sqlite", self.root / "destination.sqlite", {}, {}
                )
        finally:
            lock.unlink(missing_ok=True)
            (self.root / "original-restore-control.lock").rename(lock)
        self.assertFalse((self.root / "destination.sqlite").exists())
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_bound_lifecycle_executor_rejects_failed_restore_lock_disappearance(self) -> None:
        journal = self.root / "engine-journal.json"
        journal.write_text(
            '{"status":"running","phase":"rollback","records":[]}\n', encoding="utf-8"
        )
        lock = self.session.control_lock_path
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        executor.snapshot()

        def delete_then_fail(
            _backup: Path,
            _destination: Path,
            _manifest: dict[str, Any],
            _binding: dict[str, Any],
        ) -> None:
            original = self.root / "original-restore-control.lock"
            lock.rename(original)
            raise RuntimeError("injected restore lock disappearance")

        try:
            with (
                patch.object(self.adapter, "restore_bound", side_effect=delete_then_fail),
                self.assertRaisesRegex(
                    SQLiteAuthorityError, "lifecycle control lock is unavailable"
                ),
            ):
                executor.restore(
                    self.root / "backup.sqlite", self.root / "destination.sqlite", {}, {}
                )
        finally:
            (self.root / "original-restore-control.lock").rename(lock)
        self.assertFalse((self.root / "destination.sqlite").exists())
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_bound_lifecycle_executor_rejects_failed_restore_authority_replacement(self) -> None:
        journal = self.root / "engine-journal.json"
        journal.write_text(
            '{"status":"running","phase":"rollback","records":[]}\n', encoding="utf-8"
        )
        foreign = self.root / "foreign-restore-authority.sqlite"
        foreign.write_bytes(b"foreign authority")
        foreign.chmod(0o600)
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        executor.snapshot()

        def replace_then_fail(
            _backup: Path,
            _destination: Path,
            _manifest: dict[str, Any],
            _binding: dict[str, Any],
        ) -> None:
            original = self.root / "original-restore-authority.sqlite"
            self.authority.rename(original)
            foreign.rename(self.authority)
            raise RuntimeError("injected restore authority replacement")

        try:
            with (
                patch.object(self.adapter, "restore_bound", side_effect=replace_then_fail),
                self.assertRaisesRegex(SQLiteAuthorityError, "authority identity changed"),
            ):
                executor.restore(
                    self.root / "backup.sqlite", self.root / "destination.sqlite", {}, {}
                )
        finally:
            self.authority.unlink(missing_ok=True)
            (self.root / "original-restore-authority.sqlite").rename(self.authority)
        self.assertFalse((self.root / "destination.sqlite").exists())
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_bound_lifecycle_executor_rejects_failed_restore_authority_disappearance(self) -> None:
        journal = self.root / "engine-journal.json"
        journal.write_text(
            '{"status":"running","phase":"rollback","records":[]}\n', encoding="utf-8"
        )
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        executor.snapshot()

        def delete_then_fail(
            _backup: Path,
            _destination: Path,
            _manifest: dict[str, Any],
            _binding: dict[str, Any],
        ) -> None:
            self.authority.rename(self.root / "original-restore-authority.sqlite")
            raise RuntimeError("injected restore authority disappearance")

        try:
            with (
                patch.object(self.adapter, "restore_bound", side_effect=delete_then_fail),
                self.assertRaisesRegex(SQLiteAuthorityError, "authority identity changed"),
            ):
                executor.restore(
                    self.root / "backup.sqlite", self.root / "destination.sqlite", {}, {}
                )
        finally:
            (self.root / "original-restore-authority.sqlite").rename(self.authority)
        self.assertFalse((self.root / "destination.sqlite").exists())
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_bound_lifecycle_executor_rejects_failed_restore_authority_symlink(self) -> None:
        journal = self.root / "engine-journal.json"
        journal.write_text(
            '{"status":"running","phase":"rollback","records":[]}\n', encoding="utf-8"
        )
        foreign = self.root / "foreign-restore-authority-target.sqlite"
        foreign.write_bytes(b"foreign authority")
        foreign.chmod(0o600)
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        executor.snapshot()

        def replace_then_fail(
            _backup: Path,
            _destination: Path,
            _manifest: dict[str, Any],
            _binding: dict[str, Any],
        ) -> None:
            original = self.root / "original-restore-authority.sqlite"
            self.authority.rename(original)
            self.authority.symlink_to(foreign)
            raise RuntimeError("injected restore authority symlink")

        try:
            with (
                patch.object(self.adapter, "restore_bound", side_effect=replace_then_fail),
                self.assertRaisesRegex(SQLiteAuthorityError, "authority identity changed"),
            ):
                executor.restore(
                    self.root / "backup.sqlite", self.root / "destination.sqlite", {}, {}
                )
        finally:
            self.authority.unlink(missing_ok=True)
            (self.root / "original-restore-authority.sqlite").rename(self.authority)
        self.assertFalse((self.root / "destination.sqlite").exists())
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_bound_lifecycle_executor_rejects_failed_restore_authority_wal_sidecar(self) -> None:
        journal = self.root / "engine-journal.json"
        journal.write_text(
            '{"status":"running","phase":"rollback","records":[]}\n', encoding="utf-8"
        )
        sidecar = Path(str(self.authority) + "-wal")
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        executor.snapshot()

        def sidecar_then_fail(
            _backup: Path,
            _destination: Path,
            _manifest: dict[str, Any],
            _binding: dict[str, Any],
        ) -> None:
            sidecar.write_bytes(b"foreign authority WAL sidecar")
            sidecar.chmod(0o600)
            raise RuntimeError("injected restore authority WAL sidecar")

        try:
            with (
                patch.object(self.adapter, "restore_bound", side_effect=sidecar_then_fail),
                self.assertRaisesRegex(SQLiteAuthorityError, "authority identity changed"),
            ):
                executor.restore(
                    self.root / "backup.sqlite", self.root / "destination.sqlite", {}, {}
                )
        finally:
            sidecar.unlink(missing_ok=True)
        self.assertFalse((self.root / "destination.sqlite").exists())
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_bound_lifecycle_executor_rejects_failed_restore_authority_shm_sidecar(self) -> None:
        journal = self.root / "engine-journal.json"
        journal.write_text(
            '{"status":"running","phase":"rollback","records":[]}\n', encoding="utf-8"
        )
        sidecar = Path(str(self.authority) + "-shm")
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        executor.snapshot()

        def sidecar_then_fail(
            _backup: Path,
            _destination: Path,
            _manifest: dict[str, Any],
            _binding: dict[str, Any],
        ) -> None:
            sidecar.write_bytes(b"foreign authority SHM sidecar")
            sidecar.chmod(0o600)
            raise RuntimeError("injected restore authority SHM sidecar")

        try:
            with (
                patch.object(self.adapter, "restore_bound", side_effect=sidecar_then_fail),
                self.assertRaisesRegex(SQLiteAuthorityError, "authority identity changed"),
            ):
                executor.restore(
                    self.root / "backup.sqlite", self.root / "destination.sqlite", {}, {}
                )
        finally:
            sidecar.unlink(missing_ok=True)
        self.assertFalse((self.root / "destination.sqlite").exists())
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_bound_lifecycle_executor_rejects_failed_effect_control_mutation(self) -> None:
        journal = self.root / "engine-journal.json"
        journal.write_text('{"status":"running","phase":"backup","records":[]}\n', encoding="utf-8")
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        before = executor.snapshot()

        def mutate_then_fail(_destination: Path, _binding: dict[str, Any]) -> dict[str, Any]:
            # Simulate a hostile external writer changing durable state while
            # the effect is in flight; the executor must detect it on reread.
            with (
                closing(sqlite3.connect(self.session.control_store_path)) as connection,
                connection,
            ):
                connection.execute(
                    "UPDATE barrier_session SET status='ambiguous' WHERE project_id=?",
                    (PROJECT,),
                )
            raise RuntimeError("injected control mutation")

        with (
            patch.object(self.adapter, "backup_bound", side_effect=mutate_then_fail),
            self.assertRaisesRegex(SQLiteAuthorityError, "durable lifecycle state changed"),
        ):
            executor.backup(self.root / "backup.sqlite", {})
        self.assertNotEqual(before.control, executor.snapshot().control)
        self.assertFalse((self.root / "backup.sqlite").exists())
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_bound_lifecycle_executor_rejects_failed_effect_control_disappearance(self) -> None:
        journal = self.root / "engine-journal.json"
        journal.write_text('{"status":"running","phase":"backup","records":[]}\n', encoding="utf-8")
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        executor.snapshot()

        def delete_then_fail(_destination: Path, _binding: dict[str, Any]) -> dict[str, Any]:
            # Simulate loss of the durable session while an effect is in flight.
            with (
                closing(sqlite3.connect(self.session.control_store_path)) as connection,
                connection,
            ):
                connection.execute("DELETE FROM barrier_session WHERE project_id=?", (PROJECT,))
            raise RuntimeError("injected control disappearance")

        with (
            patch.object(self.adapter, "backup_bound", side_effect=delete_then_fail),
            self.assertRaisesRegex(SQLiteAuthorityError, "lifecycle effect failed"),
        ):
            executor.backup(self.root / "backup.sqlite", {})
        self.assertIsNone(self.session.snapshot())
        self.assertFalse((self.root / "backup.sqlite").exists())
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_bound_lifecycle_executor_rejects_failed_effect_journal_disappearance(self) -> None:
        journal = self.root / "engine-journal.json"
        journal.write_text('{"status":"running","phase":"backup","records":[]}\n', encoding="utf-8")
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        executor.snapshot()

        def delete_then_fail(_destination: Path, _binding: dict[str, Any]) -> dict[str, Any]:
            # Simulate loss of the durable journal while the effect is in flight.
            journal.unlink()
            raise RuntimeError("injected journal disappearance")

        with (
            patch.object(self.adapter, "backup_bound", side_effect=delete_then_fail),
            self.assertRaisesRegex(SQLiteAuthorityError, "lifecycle journal is unavailable"),
        ):
            executor.backup(self.root / "backup.sqlite", {})
        self.assertFalse(journal.exists())
        self.assertFalse((self.root / "backup.sqlite").exists())
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_bound_lifecycle_executor_rejects_failed_effect_control_replacement(self) -> None:
        journal = self.root / "engine-journal.json"
        journal.write_text('{"status":"running","phase":"backup","records":[]}\n', encoding="utf-8")
        control = self.session.control_store_path
        foreign = self.root / "foreign-control.sqlite"
        shutil.copy2(control, foreign)
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        executor.snapshot()

        def replace_then_fail(_destination: Path, _binding: dict[str, Any]) -> dict[str, Any]:
            original = self.root / "original-control.sqlite"
            control.rename(original)
            foreign.rename(control)
            raise RuntimeError("injected control replacement")

        try:
            with (
                patch.object(self.adapter, "backup_bound", side_effect=replace_then_fail),
                self.assertRaisesRegex(SQLiteAuthorityError, "lifecycle effect failed"),
            ):
                executor.backup(self.root / "backup.sqlite", {})
        finally:
            control.unlink(missing_ok=True)
            (self.root / "original-control.sqlite").rename(control)
        self.assertFalse((self.root / "backup.sqlite").exists())
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_bound_lifecycle_executor_rejects_failed_effect_lock_replacement(self) -> None:
        journal = self.root / "engine-journal.json"
        journal.write_text('{"status":"running","phase":"backup","records":[]}\n', encoding="utf-8")
        lock = self.session.control_lock_path
        foreign = self.root / "foreign-control.lock"
        foreign.write_bytes(b"foreign lock")
        foreign.chmod(0o600)
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        executor.snapshot()

        def replace_then_fail(_destination: Path, _binding: dict[str, Any]) -> dict[str, Any]:
            original = self.root / "original-control.lock"
            lock.rename(original)
            foreign.rename(lock)
            raise RuntimeError("injected lock replacement")

        try:
            with (
                patch.object(self.adapter, "backup_bound", side_effect=replace_then_fail),
                self.assertRaisesRegex(SQLiteAuthorityError, "durable lifecycle state changed"),
            ):
                executor.backup(self.root / "backup.sqlite", {})
        finally:
            lock.unlink(missing_ok=True)
            (self.root / "original-control.lock").rename(lock)
        self.assertFalse((self.root / "backup.sqlite").exists())
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_bound_lifecycle_executor_rejects_failed_effect_unsafe_lock_replacement(self) -> None:
        journal = self.root / "engine-journal.json"
        journal.write_text('{"status":"running","phase":"backup","records":[]}\n', encoding="utf-8")
        lock = self.session.control_lock_path
        foreign = self.root / "unsafe-control.lock"
        foreign.write_bytes(b"foreign lock")
        foreign.chmod(0o644)
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        executor.snapshot()

        def replace_then_fail(_destination: Path, _binding: dict[str, Any]) -> dict[str, Any]:
            original = self.root / "original-control.lock"
            lock.rename(original)
            foreign.rename(lock)
            raise RuntimeError("injected unsafe lock replacement")

        try:
            with (
                patch.object(self.adapter, "backup_bound", side_effect=replace_then_fail),
                self.assertRaisesRegex(
                    SQLiteAuthorityError, "lifecycle control lock is not private and regular"
                ),
            ):
                executor.backup(self.root / "backup.sqlite", {})
        finally:
            lock.unlink(missing_ok=True)
            (self.root / "original-control.lock").rename(lock)
        self.assertFalse((self.root / "backup.sqlite").exists())
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_bound_lifecycle_executor_rejects_failed_effect_lock_disappearance(self) -> None:
        journal = self.root / "engine-journal.json"
        journal.write_text('{"status":"running","phase":"backup","records":[]}\n', encoding="utf-8")
        lock = self.session.control_lock_path
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        executor.snapshot()

        def delete_then_fail(_destination: Path, _binding: dict[str, Any]) -> dict[str, Any]:
            # Move the held lock inode away so the final reread cannot trust
            # the lock path, while retaining it for cleanup below.
            lock.rename(self.root / "original-control.lock")
            raise RuntimeError("injected lock disappearance")

        try:
            with (
                patch.object(self.adapter, "backup_bound", side_effect=delete_then_fail),
                self.assertRaisesRegex(
                    SQLiteAuthorityError, "lifecycle control lock is unavailable"
                ),
            ):
                executor.backup(self.root / "backup.sqlite", {})
        finally:
            (self.root / "original-control.lock").rename(lock)
        self.assertFalse((self.root / "backup.sqlite").exists())
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_unbound_lifecycle_executor_cannot_snapshot_durable_state(self) -> None:
        executor = self.adapter.lifecycle_executor()
        with self.assertRaisesRegex(SQLiteAuthorityError, "not bound to durable state"):
            executor.snapshot()
        self.assertEqual(b"clean", self.authority.read_bytes()[-5:])
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_bound_lifecycle_executor_releases_lock_on_journal_failure(self) -> None:
        journal = self.root / "engine-journal.json"
        journal.write_text("not-json\n", encoding="utf-8")
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        with self.assertRaisesRegex(SQLiteAuthorityError, "durable lifecycle snapshot failed"):
            executor.snapshot()
        self.assertFalse(self.session.operation_owned_by_current_thread)
        self.assertEqual("held", self.session.snapshot().status)  # type: ignore[union-attr]

    def test_bound_lifecycle_executor_stability_reread_rejects_journal_drift(self) -> None:
        journal = self.root / "engine-journal.json"
        journal.write_text('{"status":"running","phase":"backup","records":[]}\n', encoding="utf-8")
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        baseline = executor.snapshot()
        baseline = executor.assert_snapshot_stable(baseline)
        journal.write_text('{"status":"failed","phase":"backup","records":[]}\n', encoding="utf-8")
        with self.assertRaisesRegex(SQLiteAuthorityError, "durable lifecycle state changed"):
            executor.assert_snapshot_stable(baseline)
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_bound_lifecycle_executor_rejects_foreign_snapshot_baseline(self) -> None:
        journal = self.root / "engine-journal.json"
        journal.write_text('{"status":"running","phase":"backup","records":[]}\n', encoding="utf-8")
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        foreign_executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        baseline = executor.snapshot()
        with self.assertRaisesRegex(SQLiteAuthorityError, "foreign executor"):
            foreign_executor.assert_snapshot_stable(baseline)

    def test_bound_lifecycle_executor_stability_reread_rejects_control_revision_drift(self) -> None:
        journal = self.root / "engine-journal.json"
        journal.write_text('{"status":"running","phase":"backup","records":[]}\n', encoding="utf-8")
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        baseline = executor.snapshot()
        self.session.mark_ambiguous(1, "injected-failure")
        with self.assertRaisesRegex(SQLiteAuthorityError, "durable lifecycle state changed"):
            executor.assert_snapshot_stable(baseline)
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_bound_lifecycle_executor_stability_reread_rejects_authority_replacement(self) -> None:
        journal = self.root / "engine-journal.json"
        journal.write_text('{"status":"running","phase":"backup","records":[]}\n', encoding="utf-8")
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        baseline = executor.snapshot()
        original = self.root / "authority-original.sqlite"
        foreign = self.root / "authority-foreign.sqlite"
        self.authority.rename(original)
        try:
            foreign.write_bytes(b"foreign authority content")
            foreign.chmod(0o600)
            foreign.rename(self.authority)
            with self.assertRaisesRegex(SQLiteAuthorityError, "authority identity changed"):
                executor.assert_snapshot_stable(baseline)
        finally:
            self.authority.unlink(missing_ok=True)
            original.rename(self.authority)
        self.assertEqual(b"clean", self.authority.read_bytes()[-5:])
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_bound_lifecycle_executor_stability_reread_rejects_journal_disappearance(self) -> None:
        journal = self.root / "engine-journal.json"
        journal.write_text('{"status":"running","phase":"backup","records":[]}\n', encoding="utf-8")
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        baseline = executor.snapshot()
        journal.unlink()
        with self.assertRaisesRegex(SQLiteAuthorityError, "lifecycle journal is unavailable"):
            executor.assert_snapshot_stable(baseline)
        self.assertFalse(self.session.operation_owned_by_current_thread)
        self.assertEqual("held", self.session.snapshot().status)  # type: ignore[union-attr]

    def test_bound_lifecycle_executor_rejects_same_bytes_journal_replacement(self) -> None:
        journal = self.root / "engine-journal.json"
        content = '{"status":"running","phase":"backup","records":[]}\n'
        journal.write_text(content, encoding="utf-8")
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        baseline = executor.snapshot()
        replacement = self.root / "replacement-journal.json"
        replacement.write_text(content, encoding="utf-8")
        replacement.replace(journal)
        with self.assertRaisesRegex(SQLiteAuthorityError, "durable lifecycle state changed"):
            executor.assert_snapshot_stable(baseline)
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_bound_lifecycle_executor_rejects_journal_symlink_substitution(self) -> None:
        journal = self.root / "engine-journal.json"
        content = '{"status":"running","phase":"backup","records":[]}\n'
        journal.write_text(content, encoding="utf-8")
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        baseline = executor.snapshot()
        foreign = self.root / "foreign-journal.json"
        foreign.write_text(content, encoding="utf-8")
        journal.unlink()
        journal.symlink_to(foreign)
        with self.assertRaisesRegex(SQLiteAuthorityError, "not private and regular"):
            executor.assert_snapshot_stable(baseline)
        journal.unlink()
        foreign.rename(journal)
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_bound_lifecycle_executor_rejects_shared_journal_hardlink(self) -> None:
        journal = self.root / "engine-journal.json"
        content = '{"status":"running","phase":"backup","records":[]}\n'
        journal.write_text(content, encoding="utf-8")
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        baseline = executor.snapshot()
        shared = self.root / "shared-journal.json"
        os.link(journal, shared)
        with self.assertRaisesRegex(SQLiteAuthorityError, "not private and regular"):
            executor.assert_snapshot_stable(baseline)
        shared.unlink()
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_bound_lifecycle_executor_rejects_journal_parent_symlink(self) -> None:
        journal_parent = self.root / "journal-root"
        journal_parent.mkdir()
        journal = journal_parent / "engine-journal.json"
        content = '{"status":"running","phase":"backup","records":[]}\n'
        journal.write_text(content, encoding="utf-8")
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        baseline = executor.snapshot()
        foreign_parent = self.root / "foreign-journal-root"
        foreign_parent.mkdir()
        (foreign_parent / journal.name).write_text(content, encoding="utf-8")
        original_parent = self.root / "journal-root-original"
        journal_parent.rename(original_parent)
        journal_parent.symlink_to(foreign_parent, target_is_directory=True)
        try:
            with self.assertRaisesRegex(SQLiteAuthorityError, "parent is not a directory"):
                executor.assert_snapshot_stable(baseline)
        finally:
            journal_parent.unlink()
            original_parent.rename(journal_parent)
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_bound_lifecycle_executor_rejects_journal_parent_replacement(self) -> None:
        journal_parent = self.root / "journal-root"
        journal_parent.mkdir()
        journal = journal_parent / "engine-journal.json"
        content = '{"status":"running","phase":"backup","records":[]}\n'
        journal.write_text(content, encoding="utf-8")
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        baseline = executor.snapshot()
        foreign_parent = self.root / "foreign-journal-root"
        foreign_parent.mkdir()
        (foreign_parent / journal.name).write_text(content, encoding="utf-8")
        original_parent = self.root / "journal-root-original"
        journal_parent.rename(original_parent)
        foreign_parent.rename(journal_parent)
        try:
            with self.assertRaisesRegex(SQLiteAuthorityError, "durable lifecycle state changed"):
                executor.assert_snapshot_stable(baseline)
        finally:
            journal_parent.rename(foreign_parent)
            original_parent.rename(journal_parent)
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_bound_lifecycle_executor_rejects_invalid_journal_record_shape(self) -> None:
        journal = self.root / "engine-journal.json"
        journal.write_text('{"status":"running","phase":"backup","records":{}}\n', encoding="utf-8")
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        with self.assertRaisesRegex(SQLiteAuthorityError, "durable lifecycle snapshot failed"):
            executor.snapshot()
        self.assertFalse(self.session.operation_owned_by_current_thread)
        self.assertEqual("held", self.session.snapshot().status)  # type: ignore[union-attr]

    def test_bound_lifecycle_executor_rejects_missing_initial_journal(self) -> None:
        journal = self.root / "missing-engine-journal.json"
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        with self.assertRaisesRegex(SQLiteAuthorityError, "lifecycle journal is unavailable"):
            executor.snapshot()
        self.assertFalse(self.session.operation_owned_by_current_thread)
        self.assertEqual("held", self.session.snapshot().status)  # type: ignore[union-attr]

    def test_bound_lifecycle_executor_rejects_initial_journal_symlink(self) -> None:
        journal = self.root / "engine-journal.json"
        foreign = self.root / "foreign-engine-journal.json"
        foreign.write_text(
            '{"status":"running","phase":"backup","records":[]}\n',
            encoding="utf-8",
        )
        journal.symlink_to(foreign)
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        with self.assertRaisesRegex(SQLiteAuthorityError, "not private and regular"):
            executor.snapshot()
        self.assertFalse(self.session.operation_owned_by_current_thread)
        self.assertEqual("held", self.session.snapshot().status)  # type: ignore[union-attr]

    def test_bound_lifecycle_executor_rejects_missing_journal_parent(self) -> None:
        journal = self.root / "missing-journal-parent" / "engine-journal.json"
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        with self.assertRaisesRegex(SQLiteAuthorityError, "lifecycle journal is unavailable"):
            executor.snapshot()
        self.assertFalse(journal.parent.exists())
        self.assertFalse(self.session.operation_owned_by_current_thread)
        self.assertEqual("held", self.session.snapshot().status)  # type: ignore[union-attr]

    def test_bound_lifecycle_executor_rejects_file_journal_parent(self) -> None:
        parent = self.root / "journal-parent-file"
        parent.write_bytes(b"not a directory")
        journal = parent / "engine-journal.json"
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        with self.assertRaisesRegex(SQLiteAuthorityError, "lifecycle journal is unavailable"):
            executor.snapshot()
        self.assertFalse(self.session.operation_owned_by_current_thread)
        self.assertEqual("held", self.session.snapshot().status)  # type: ignore[union-attr]

    def test_bound_lifecycle_executor_rejects_missing_control_session(self) -> None:
        journal = self.root / "engine-journal.json"
        journal.write_text('{"status":"running","phase":"backup","records":[]}\n', encoding="utf-8")
        missing_session = SQLiteBarrierSessionStore(
            SQLiteRollbackControlStore(
                self.root / "missing-control.sqlite", PROJECT, self.authority
            ),
            lambda: "authority",
        )
        executor = self.adapter.bind_lifecycle_executor(missing_session, journal)
        with self.assertRaisesRegex(SQLiteAuthorityError, "durable lifecycle snapshot failed"):
            executor.snapshot()
        self.assertFalse(missing_session.operation_owned_by_current_thread)

    def test_bound_lifecycle_executor_rejects_reused_stale_baseline(self) -> None:
        journal = self.root / "engine-journal.json"
        journal.write_text('{"status":"running","phase":"backup","records":[]}\n', encoding="utf-8")
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        first = executor.snapshot()
        second = executor.assert_snapshot_stable(first)
        self.assertIsNot(first, second)
        with self.assertRaisesRegex(SQLiteAuthorityError, "foreign executor"):
            executor.assert_snapshot_stable(first)
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_bound_lifecycle_executor_rejects_authority_drift_on_final_reread(self) -> None:
        journal = self.root / "engine-journal.json"
        journal.write_text('{"status":"running","phase":"backup","records":[]}\n', encoding="utf-8")
        executor = self.adapter.bind_lifecycle_executor(self.session, journal)
        with (
            patch.object(
                self.adapter,
                "_check_identity",
                side_effect=[None, SQLiteAuthorityError("authority identity changed")],
            ),
            self.assertRaisesRegex(SQLiteAuthorityError, "authority identity changed"),
        ):
            executor.snapshot()
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_bound_lifecycle_executor_rejects_foreign_authority_store(self) -> None:
        foreign_authority = self.root / "foreign-authority.sqlite"
        with closing(sqlite3.connect(foreign_authority)) as connection, connection:
            connection.execute("CREATE TABLE records (id INTEGER PRIMARY KEY)")
        foreign_authority.chmod(0o600)
        foreign_control = self.root / "foreign-control.sqlite"
        foreign_store = SQLiteBarrierSessionStore(
            SQLiteRollbackControlStore(foreign_control, PROJECT, foreign_authority),
            lambda: "authority",
        )
        with self.assertRaisesRegex(SQLiteAuthorityError, "foreign authority"):
            self.adapter.bind_lifecycle_executor(foreign_store, self.root / "journal.json")

    def test_bound_lifecycle_executor_rejects_store_without_authority_binding(self) -> None:
        unbound_store = SQLiteBarrierSessionStore(
            SQLiteRollbackControlStore(self.root / "unbound-control.sqlite", PROJECT),
            lambda: "authority",
        )
        with self.assertRaisesRegex(SQLiteAuthorityError, "foreign authority"):
            self.adapter.bind_lifecycle_executor(unbound_store, self.root / "journal.json")

    def test_direct_lifecycle_executor_constructor_rejects_foreign_store(self) -> None:
        foreign_authority = self.root / "foreign-authority-direct.sqlite"
        with closing(sqlite3.connect(foreign_authority)) as connection, connection:
            connection.execute("CREATE TABLE records (id INTEGER PRIMARY KEY)")
        foreign_authority.chmod(0o600)
        foreign_store = SQLiteBarrierSessionStore(
            SQLiteRollbackControlStore(
                self.root / "foreign-control-direct.sqlite", PROJECT, foreign_authority
            ),
            lambda: "authority",
        )
        with self.assertRaisesRegex(SQLiteAuthorityError, "foreign authority"):
            SQLiteLifecycleExecutor(self.adapter, foreign_store, self.root / "journal.json")

    def test_engine_bound_rollback_inspection_uses_real_scope_and_preserves_journal(self) -> None:
        context = {**CONTEXT, "operation_id": "op-real-sqlite-inspection", "project_id": PROJECT}
        artifact_root = self.root / "artifacts"
        artifact_root.mkdir()
        context.update(
            {
                "artifact_root": str(artifact_root),
                "destination": str(artifact_root / "destination"),
                "manifest": str(artifact_root / "manifest.json"),
                "selector_ref": ".runtime/runtime-selector.json",
            }
        )
        context["barrier_identity_digest"] = canonical_barrier_digest(context)
        context["envelope_digest"] = canonical_envelope_digest(context)
        engine = UpgradeEngine(
            str(context["operation_id"]),
            self.root / "engine-journal.json",
            context,
            backend_adapter=self.adapter,
            rollback_bound_verifier=BoundRollbackCapability.bind(
                PhaseContext(**cast(dict[str, Any], context)),
                self.adapter,
                self.scope,
                lease=self.lease,
                admission_recheck=self.recheck,
            ),
        )
        engine.plan()
        before = (self.root / "engine-journal.json").read_bytes()
        result = engine.inspect_rollback_bound()
        self.assertFalse(result["rollback_context_verified"])
        self.assertEqual(before, (self.root / "engine-journal.json").read_bytes())
        self.assertFalse(self.session.operation_owned_by_current_thread)
        with engine._exclusive():
            pass

    def test_runtime_binding_rereads_real_sqlite_backend_inside_scope(self) -> None:
        context = {
            **CONTEXT,
            "operation_id": "op-real-sqlite-binding",
            "project_id": PROJECT,
            "target": "rollback",
        }
        artifact_root = self.root / "binding-artifacts"
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
                "backend": "sqlite",
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
        evidence = binding.reread_backend_bound(
            self.adapter,
            self.scope,
            self.lease,
            self.recheck,
        )
        self.assertTrue(evidence["backend_identity_verified"])
        self.assertTrue(evidence["sqlite_integrity_verified"])
        self.assertTrue(evidence["sqlite_foreign_keys_verified"])
        self.assertFalse(evidence["mutates_authority"])
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_clean_snapshot_is_integrity_bound_and_nonmutating(self) -> None:
        result = self.adapter.snapshot("discover", CONTEXT)
        self.assertTrue(result["sqlite_integrity_verified"])
        self.assertTrue(result["sqlite_foreign_keys_verified"])
        self.assertFalse(result["mutates_authority"])
        for phase in ("", "unknown", 1, True):
            with (
                self.subTest(phase=phase),
                self.assertRaisesRegex(SQLiteAuthorityError, "phase is invalid"),
            ):
                self.adapter.snapshot(cast(Any, phase), CONTEXT)
        durable_before = self._durable_state()
        with (
            patch.object(
                self.adapter, "snapshot", side_effect=AssertionError("SQLite reached")
            ) as snapshot,
            patch.object(
                self.adapter, "execute", side_effect=AssertionError("execute reached")
            ) as execute,
            self.assertRaisesRegex(SQLiteAuthorityError, "rollback context target"),
        ):
            self.adapter.verify_rollback_context(CONTEXT)
        snapshot.assert_not_called()
        execute.assert_not_called()
        self.assertEqual(durable_before, self._durable_state())
        self.assertFalse(self.session.operation_owned_by_current_thread)
        rollback_context = {**CONTEXT, "target": "rollback"}
        self.assertFalse(
            self.adapter.verify_rollback_context(rollback_context)["rollback_context_verified"]
        )
        bound = self.adapter.verify_rollback_context_bound(
            {**rollback_context, "project_id": PROJECT},
            self.scope,
            lease=self.lease,
            admission_recheck=self.recheck,
        )
        self.assertEqual("rollback", bound["phase"])
        self.assertFalse(bound["rollback_context_verified"])
        self.assertFalse(self.session.operation_owned_by_current_thread)
        durable_before_bound_reject = self._durable_state()
        with (
            patch.object(
                self.adapter, "snapshot", side_effect=AssertionError("SQLite reached")
            ) as snapshot,
            patch.object(
                self.adapter, "execute", side_effect=AssertionError("execute reached")
            ) as execute,
            self.assertRaisesRegex(SQLiteAuthorityError, "rollback context target"),
        ):
            self.adapter.verify_rollback_context_bound(
                CONTEXT,
                self.scope,
                lease=self.lease,
                admission_recheck=self.recheck,
            )
        snapshot.assert_not_called()
        execute.assert_not_called()
        self.assertEqual(durable_before_bound_reject, self._durable_state())
        self.assertFalse(self.session.operation_owned_by_current_thread)
        durable_before_execute_rejects = self._durable_state()
        for phase in ("commit", "apply", "rollback"):
            with self.assertRaisesRegex(SQLiteAuthorityError, "not implemented"):
                self.adapter.execute(phase, CONTEXT)
        self.assertEqual(durable_before_execute_rejects, self._durable_state())
        self.assertFalse(
            self.adapter.verify_rollback_context({**CONTEXT, "target": "rollback"})[
                "rollback_context_verified"
            ]
        )

    def test_scoped_wrapper_guards_disabled_execute(self) -> None:
        adapter = ScopedBackendAdapter(self.adapter, Scope())
        self.assertTrue(adapter.snapshot("discover", CONTEXT)["sqlite_integrity_verified"])
        with self.assertRaisesRegex(TypeError, "disabled"):
            adapter.execute("commit", CONTEXT)

    def test_snapshot_bound_uses_real_scope_and_releases_after_read(self) -> None:
        result = self.adapter.snapshot_bound(
            "discover",
            {**CONTEXT, "project_id": PROJECT},
            self.scope,
            lease=self.lease,
            admission_recheck=self.recheck,
        )
        self.assertTrue(result["sqlite_integrity_verified"])
        self.assertFalse(result["mutates_authority"])
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_fresh_workers_reject_stale_and_accept_replacement_before_sqlite(self) -> None:
        ambiguous = self.session.mark_ambiguous(1, "worker-recovery")
        replacement_record = self._session_identity().as_record()
        replacement_record.update(
            {
                "attempt_id": "attempt-replacement",
                "state_revision": 2,
                "durable_barrier_id": "barrier-new",
                "fencing_token": "fence-new",
                "fencing_owner": "owner-new",
            }
        )
        replacement_record["identity_digest"] = canonical_barrier_session_digest(replacement_record)
        replacement = BarrierSessionState(
            BarrierSessionIdentity.from_record(replacement_record), "held", 1
        )
        self.session.reconcile_ambiguous(ambiguous.revision, replacement)
        before = self._durable_state()
        context = multiprocessing.get_context("fork")
        stale_result = context.Queue()
        stale = context.Process(
            target=_bound_snapshot_worker,
            args=(str(self.root), "stale", stale_result),
        )
        stale.start()
        stale.join(5)
        self.assertEqual(0, stale.exitcode)
        stale_outcome = stale_result.get(timeout=1)
        self.assertEqual("rejected", stale_outcome[0])
        self.assertIn(stale_outcome[1], {"SQLiteAuthorityError", "LockDomainError"})
        self.assertEqual((0, False), stale_outcome[2:])
        replacement_result = context.Queue()
        fresh = context.Process(
            target=_bound_snapshot_worker,
            args=(str(self.root), "replacement", replacement_result),
        )
        fresh.start()
        fresh.join(5)
        self.assertEqual(0, fresh.exitcode)
        self.assertEqual(("success", True, 1, False), replacement_result.get(timeout=1))
        self.assertEqual(before, self._durable_state())
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_process_abort_inside_bound_scope_releases_locks_for_fresh_worker(self) -> None:
        ambiguous = self.session.mark_ambiguous(1, "process-abort")
        replacement_record = self._session_identity().as_record()
        replacement_record.update(
            {
                "attempt_id": "attempt-abort-replacement",
                "state_revision": 2,
                "durable_barrier_id": "barrier-new",
                "fencing_token": "fence-new",
                "fencing_owner": "owner-new",
            }
        )
        replacement_record["identity_digest"] = canonical_barrier_session_digest(replacement_record)
        self.session.reconcile_ambiguous(
            ambiguous.revision,
            BarrierSessionState(BarrierSessionIdentity.from_record(replacement_record), "held", 1),
        )
        before = self._durable_state()
        context = multiprocessing.get_context("fork")
        crashed_result = context.Queue()
        crashed = context.Process(
            target=_bound_snapshot_worker,
            args=(str(self.root), "crash", crashed_result, True),
        )
        crashed.start()
        crashed.join(5)
        self.assertEqual(17, crashed.exitcode)
        self.assertFalse(self.session.operation_owned_by_current_thread)
        fresh_result = context.Queue()
        fresh = context.Process(
            target=_bound_snapshot_worker,
            args=(str(self.root), "replacement", fresh_result, True),
        )
        fresh.start()
        fresh.join(5)
        self.assertEqual(0, fresh.exitcode)
        self.assertEqual(("success", True, 1, False), fresh_result.get(timeout=1))
        self.assertEqual(before, self._durable_state())

    def test_snapshot_bound_rejects_invalid_admission_inputs_before_scope(self) -> None:
        observed = {**CONTEXT, "project_id": PROJECT}

        class CountingAdapter(SQLiteAuthorityAdapter):
            calls = 0

            def snapshot(self, phase: str, context: Mapping[str, object]) -> dict[str, object]:
                self.calls += 1
                return super().snapshot(phase, context)

        adapter = CountingAdapter(self.authority)
        bound = cast(Any, adapter.snapshot_bound)
        common = {
            "phase": "discover",
            "context": observed,
            "scope": self.scope,
            "lease": self.lease,
            "admission_recheck": self.recheck,
        }
        cases = (
            ("phase", "", "phase is invalid"),
            ("phase", "unknown", "phase is invalid"),
            ("phase", 1, "phase is invalid"),
            ("phase", True, "phase is invalid"),
            ("lease", cast(Any, object()), "trusted admission lease"),
            ("admission_recheck", cast(Any, object()), "trusted admission recheck"),
            ("scope", cast(Any, object()), "concrete lock-domain scope"),
            ("context", {**observed, "backend": "git"}, "mismatched"),
        )
        for field, value, message in cases:
            with (
                self.subTest(field=field),
                patch.object(adapter, "execute", side_effect=AssertionError("execute reached")),
                self.assertRaisesRegex(SQLiteAuthorityError, message),
            ):
                bound(**{**common, field: value})
        mismatched = validate_recheck(
            AdmissionLease(PROJECT, "authority", "other", "owner", "barrier", 1),
            project_id=PROJECT,
            authority_revision="authority",
            fencing_token="other",  # noqa: S106
            fencing_owner="owner",
            durable_barrier_id="barrier",
            revision=1,
        )
        with (
            patch.object(adapter, "execute", side_effect=AssertionError("execute reached")),
            self.assertRaisesRegex(SQLiteAuthorityError, "does not match"),
        ):
            bound(**{**common, "admission_recheck": mismatched})
        stale = {**observed, "state_revision": 2}
        with (
            patch.object(adapter, "execute", side_effect=AssertionError("execute reached")),
            self.assertRaisesRegex(SQLiteAuthorityError, "trusted session identity"),
        ):
            bound(**{**common, "context": stale})
        replaced = AdmissionLease(PROJECT, "authority", "fence-new", "owner-new", "barrier-new", 2)
        replaced_recheck = validate_recheck(
            replaced,
            project_id=PROJECT,
            authority_revision="authority",
            fencing_token="fence-new",  # noqa: S106
            fencing_owner="owner-new",
            durable_barrier_id="barrier-new",
            revision=2,
        )
        with (
            patch.object(adapter, "execute", side_effect=AssertionError("execute reached")),
            self.assertRaisesRegex(SQLiteAuthorityError, "trusted session identity"),
        ):
            bound(**{**common, "lease": replaced, "admission_recheck": replaced_recheck})
        self.assertEqual(0, adapter.calls)
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_snapshot_bound_rejects_each_untrusted_sqlite_result_claim(self) -> None:
        class TamperedAdapter(SQLiteAuthorityAdapter):
            field = "backend_identity_verified"
            replacement: object = False

            def snapshot(self, phase: str, context: Mapping[str, object]) -> dict[str, object]:
                value = super().snapshot(phase, context)
                value[self.field] = self.replacement
                return value

        for field, replacement, message in (
            ("backend_identity_verified", False, "backend identity is unverified"),
            ("sqlite_integrity_verified", False, "integrity is unverified"),
            ("sqlite_foreign_keys_verified", False, "foreign keys are unverified"),
            ("mutates_authority", True, "not read-only"),
        ):
            with self.subTest(field=field):
                adapter = type(
                    "FieldTamperedAdapter",
                    (TamperedAdapter,),
                    {"field": field, "replacement": replacement},
                )(self.authority)
                before = self._durable_state()
                with (
                    patch.object(adapter, "execute", side_effect=AssertionError("execute reached")),
                    self.assertRaisesRegex(SQLiteAuthorityError, message),
                ):
                    adapter.snapshot_bound(
                        "discover",
                        {**CONTEXT, "project_id": PROJECT},
                        self.scope,
                        lease=self.lease,
                        admission_recheck=self.recheck,
                    )
                self.assertEqual(before, self._durable_state())
                self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_snapshot_bound_rejects_backend_equivalence_drift_without_execute(self) -> None:
        class TamperedAdapter(SQLiteAuthorityAdapter):
            def snapshot(self, phase: str, context: Mapping[str, object]) -> dict[str, object]:
                value = super().snapshot(phase, context)
                value["project_id"] = "tampered"
                return value

        tampered = TamperedAdapter(self.authority)
        before = self._durable_state()
        with (
            patch.object(tampered, "execute", side_effect=AssertionError("execute reached")),
            self.assertRaisesRegex(SQLiteAuthorityError, "backend context identity"),
        ):
            tampered.snapshot_bound(
                "discover",
                {**CONTEXT, "project_id": PROJECT},
                self.scope,
                lease=self.lease,
                admission_recheck=self.recheck,
            )
        self.assertFalse(self.session.operation_owned_by_current_thread)
        self.assertEqual(before, self._durable_state())

    def test_snapshot_bound_rejects_non_read_only_result(self) -> None:
        class TamperedAdapter(SQLiteAuthorityAdapter):
            def snapshot(self, phase: str, context: Mapping[str, object]) -> dict[str, object]:
                value = super().snapshot(phase, context)
                value["mutates_authority"] = True
                return value

        tampered = TamperedAdapter(self.authority)
        before = self._durable_state()
        with (
            patch.object(tampered, "execute", side_effect=AssertionError("execute reached")),
            self.assertRaisesRegex(SQLiteAuthorityError, "not read-only"),
        ):
            tampered.snapshot_bound(
                "discover",
                {**CONTEXT, "project_id": PROJECT},
                self.scope,
                lease=self.lease,
                admission_recheck=self.recheck,
            )
        self.assertFalse(self.session.operation_owned_by_current_thread)
        self.assertEqual(before, self._durable_state())

    def test_snapshot_bound_rejects_phase_drift_without_execute(self) -> None:
        class TamperedAdapter(SQLiteAuthorityAdapter):
            def snapshot(self, phase: str, context: Mapping[str, object]) -> dict[str, object]:
                value = super().snapshot(phase, context)
                value["phase"] = "other"
                return value

        tampered = TamperedAdapter(self.authority)
        before = self._durable_state()
        with (
            patch.object(tampered, "execute", side_effect=AssertionError("execute reached")),
            self.assertRaisesRegex(SQLiteAuthorityError, "backend phase changed"),
        ):
            tampered.snapshot_bound(
                "discover",
                {**CONTEXT, "project_id": PROJECT},
                self.scope,
                lease=self.lease,
                admission_recheck=self.recheck,
            )
        self.assertFalse(self.session.operation_owned_by_current_thread)
        self.assertEqual(before, self._durable_state())

    def test_snapshot_bound_requires_exact_result_schema_and_types(self) -> None:
        fields = {
            "phase": 1,
            "backend_identity_verified": 1,
            "sqlite_integrity_verified": 1,
            "sqlite_foreign_keys_verified": 1,
            "mutates_authority": 0,
        }

        class TamperedAdapter(SQLiteAuthorityAdapter):
            mode = "wrong"
            field = "phase"
            wrong: object = 1

            def snapshot(self, phase: str, context: Mapping[str, object]) -> dict[str, object]:
                value = super().snapshot(phase, context)
                if self.mode == "missing":
                    value.pop(self.field)
                elif self.mode == "extra":
                    value["unexpected"] = True
                else:
                    value[self.field] = self.wrong
                return value

        for mode in ("missing", "extra", "wrong"):
            for field, wrong in fields.items():
                with self.subTest(mode=mode, field=field):
                    adapter = type(
                        "SchemaTamperedAdapter",
                        (TamperedAdapter,),
                        {"mode": mode, "field": field, "wrong": wrong},
                    )(self.authority)
                    before = self._durable_state()
                    with (
                        patch.object(
                            adapter, "execute", side_effect=AssertionError("execute reached")
                        ),
                        self.assertRaises(SQLiteAuthorityError),
                    ):
                        adapter.snapshot_bound(
                            "discover",
                            {**CONTEXT, "project_id": PROJECT},
                            self.scope,
                            lease=self.lease,
                            admission_recheck=self.recheck,
                        )
                    self.assertFalse(self.session.operation_owned_by_current_thread)
                    self.assertEqual(before, self._durable_state())

    def test_corrupt_or_mismatched_authority_fails_closed(self) -> None:
        self.authority.write_bytes(b"not sqlite")
        with self.assertRaisesRegex(SQLiteAuthorityError, "observation failed"):
            self.adapter.snapshot("discover", CONTEXT)
        with self.assertRaisesRegex(SQLiteAuthorityError, "mismatched"):
            self.adapter.snapshot("discover", {**CONTEXT, "backend": "git"})
        with self.assertRaisesRegex(SQLiteAuthorityError, "context types"):
            self.adapter.snapshot("discover", {**CONTEXT, "operation_id": 1})

    def test_descriptor_replacement_fails_old_reader_and_fresh_reader_recovers(self) -> None:
        replacement = self.root / "replacement.sqlite"
        replacement.write_bytes(self.authority.read_bytes())
        replacement.chmod(0o600)
        replacement.replace(self.authority)
        with self.assertRaisesRegex(SQLiteAuthorityError, "identity changed"):
            self.adapter.snapshot("discover", CONTEXT)
        self.assertTrue(
            SQLiteAuthorityAdapter(self.authority).snapshot("discover", CONTEXT)[
                "sqlite_integrity_verified"
            ]
        )

    def test_process_death_after_read_allows_fresh_reader(self) -> None:
        context = multiprocessing.get_context("fork")
        worker = context.Process(target=_snapshot_process, args=(str(self.authority), True))
        worker.start()
        worker.join(5)
        self.assertEqual(17, worker.exitcode)
        self.assertTrue(
            SQLiteAuthorityAdapter(self.authority).snapshot("discover", CONTEXT)[
                "sqlite_integrity_verified"
            ]
        )

    def test_exclusive_transaction_failure_then_process_death_recovers(self) -> None:
        context = multiprocessing.get_context("fork")
        ready, release = context.Pipe(duplex=True)
        worker = context.Process(
            target=_hold_exclusive_transaction,
            args=(str(self.authority), release),
        )
        worker.start()
        self.assertTrue(ready.recv())
        try:
            with self.assertRaisesRegex(SQLiteAuthorityError, "observation failed"):
                self.adapter.snapshot("discover", CONTEXT)
        finally:
            worker.terminate()
            worker.join(5)
            ready.close()
            release.close()
        self.assertFalse(worker.is_alive())
        self.assertTrue(
            SQLiteAuthorityAdapter(self.authority).snapshot("discover", CONTEXT)[
                "sqlite_integrity_verified"
            ]
        )
        with closing(sqlite3.connect(self.authority)) as connection, connection:
            self.assertEqual("clean", connection.execute("SELECT body FROM records").fetchone()[0])

    def test_new_or_replaced_wal_sidecar_fails_old_reader_closed(self) -> None:
        sidecar = self.authority.with_name(self.authority.name + "-wal")
        sidecar.write_bytes(b"wal")
        sidecar.chmod(0o600)
        with self.assertRaisesRegex(SQLiteAuthorityError, "identity changed"):
            self.adapter.snapshot("discover", CONTEXT)
        sidecar.unlink()

    def test_removed_existing_shm_sidecar_fails_old_reader_closed(self) -> None:
        sidecar = self.authority.with_name(self.authority.name + "-shm")
        sidecar.write_bytes(b"shm")
        sidecar.chmod(0o600)
        adapter = SQLiteAuthorityAdapter(self.authority)
        sidecar.unlink()
        with self.assertRaisesRegex(SQLiteAuthorityError, "identity changed"):
            adapter.snapshot("discover", CONTEXT)

    def test_existing_shm_sidecar_mode_change_fails_old_reader_closed(self) -> None:
        sidecar = self.authority.with_name(self.authority.name + "-shm")
        sidecar.write_bytes(b"shm")
        sidecar.chmod(0o600)
        adapter = SQLiteAuthorityAdapter(self.authority)
        sidecar.chmod(0o644)
        with self.assertRaisesRegex(SQLiteAuthorityError, "sidecar is unsafe"):
            adapter.snapshot("discover", CONTEXT)
        sidecar.unlink()

    def test_existing_shm_sidecar_hard_link_fails_old_reader_closed(self) -> None:
        sidecar = self.authority.with_name(self.authority.name + "-shm")
        sidecar.write_bytes(b"shm")
        sidecar.chmod(0o600)
        adapter = SQLiteAuthorityAdapter(self.authority)
        extra_link = self.root / "authority-shm-link"
        extra_link.hardlink_to(sidecar)
        with self.assertRaisesRegex(SQLiteAuthorityError, "sidecar is unsafe"):
            adapter.snapshot("discover", CONTEXT)
        extra_link.unlink()
        sidecar.unlink()

    def test_authority_descriptor_mode_change_fails_old_reader_closed(self) -> None:
        adapter = SQLiteAuthorityAdapter(self.authority)
        self.authority.chmod(0o640)
        try:
            with self.assertRaisesRegex(SQLiteAuthorityError, "identity changed"):
                adapter.snapshot("discover", CONTEXT)
        finally:
            self.authority.chmod(0o600)

    def test_authority_descriptor_disappearance_fails_old_reader_closed(self) -> None:
        adapter = SQLiteAuthorityAdapter(self.authority)
        hidden = self.authority.with_name(self.authority.name + "-hidden")
        self.authority.rename(hidden)
        try:
            with self.assertRaisesRegex(SQLiteAuthorityError, "identity changed"):
                adapter.snapshot("discover", CONTEXT)
        finally:
            hidden.rename(self.authority)

    def test_authority_descriptor_symlink_substitution_fails_old_reader_closed(self) -> None:
        adapter = SQLiteAuthorityAdapter(self.authority)
        hidden = self.authority.with_name(self.authority.name + "-hidden")
        self.authority.rename(hidden)
        self.authority.symlink_to(hidden.name)
        try:
            with self.assertRaisesRegex(SQLiteAuthorityError, "identity changed"):
                adapter.snapshot("discover", CONTEXT)
        finally:
            self.authority.unlink()
            hidden.rename(self.authority)

    def test_authority_parent_symlink_substitution_fails_old_reader_closed(self) -> None:
        adapter = SQLiteAuthorityAdapter(self.authority)
        parent = self.authority.parent
        moved = parent.with_name(parent.name + "-original")
        foreign = parent.with_name(parent.name + "-foreign")
        parent.rename(moved)
        foreign.mkdir(mode=0o700)
        parent.symlink_to(foreign, target_is_directory=True)
        try:
            with self.assertRaisesRegex(SQLiteAuthorityError, "identity changed"):
                adapter.snapshot("discover", CONTEXT)
        finally:
            parent.unlink()
            foreign.rmdir()
            moved.rename(parent)

    def test_authority_parent_same_target_symlink_fails_old_reader_closed(self) -> None:
        adapter = SQLiteAuthorityAdapter(self.authority)
        parent = self.authority.parent
        moved = parent.with_name(parent.name + "-original")
        parent.rename(moved)
        parent.symlink_to(moved, target_is_directory=True)
        try:
            with self.assertRaisesRegex(SQLiteAuthorityError, "identity changed"):
                adapter.snapshot("discover", CONTEXT)
        finally:
            parent.unlink()
            moved.rename(parent)

    def test_authority_parent_disappearance_fails_old_reader_closed(self) -> None:
        adapter = SQLiteAuthorityAdapter(self.authority)
        parent = self.authority.parent
        moved = parent.with_name(parent.name + "-hidden")
        parent.rename(moved)
        try:
            with self.assertRaisesRegex(SQLiteAuthorityError, "identity changed"):
                adapter.snapshot("discover", CONTEXT)
        finally:
            moved.rename(parent)

    def test_existing_shm_sidecar_symlink_fails_old_reader_closed(self) -> None:
        sidecar = self.authority.with_name(self.authority.name + "-shm")
        sidecar.write_bytes(b"shm")
        sidecar.chmod(0o600)
        adapter = SQLiteAuthorityAdapter(self.authority)
        replacement = self.root / "shm-target"
        replacement.write_bytes(b"shm")
        replacement.chmod(0o600)
        sidecar.unlink()
        sidecar.symlink_to(replacement.name)
        try:
            with self.assertRaisesRegex(SQLiteAuthorityError, "sidecar is unsafe"):
                adapter.snapshot("discover", CONTEXT)
        finally:
            sidecar.unlink()
            replacement.unlink()

    def test_authority_descriptor_hard_link_fails_old_reader_closed(self) -> None:
        adapter = SQLiteAuthorityAdapter(self.authority)
        extra_link = self.root / "authority-link"
        extra_link.hardlink_to(self.authority)
        try:
            with self.assertRaisesRegex(SQLiteAuthorityError, "identity changed"):
                adapter.snapshot("discover", CONTEXT)
        finally:
            extra_link.unlink()

    def test_authority_parent_mode_change_fails_old_reader_closed(self) -> None:
        adapter = SQLiteAuthorityAdapter(self.authority)
        parent = self.authority.parent
        parent.chmod(0o755)
        try:
            with self.assertRaisesRegex(SQLiteAuthorityError, "identity changed"):
                adapter.snapshot("discover", CONTEXT)
        finally:
            parent.chmod(0o700)

    def test_unsafe_sidecar_is_rejected_at_construction(self) -> None:
        sidecar = self.authority.with_name(self.authority.name + "-shm")
        sidecar.write_bytes(b"shm")
        sidecar.chmod(0o644)
        with self.assertRaisesRegex(SQLiteAuthorityError, "sidecar is unsafe"):
            SQLiteAuthorityAdapter(self.authority)

    def test_unavailable_and_unsafe_descriptors_fail_closed(self) -> None:
        with self.assertRaisesRegex(SQLiteAuthorityError, "unavailable"):
            SQLiteAuthorityAdapter(self.root / "missing.sqlite")
        self.authority.chmod(0o644)
        with self.assertRaisesRegex(SQLiteAuthorityError, "unsafe"):
            SQLiteAuthorityAdapter(self.authority)

    def test_non_ok_integrity_result_fails_closed(self) -> None:
        class Cursor:
            def __init__(self, value: object) -> None:
                self.value = value

            def fetchone(self) -> tuple[object]:
                return (self.value,)

            def __iter__(self) -> Iterator[object]:
                return iter(())

        class Connection:
            def execute(self, statement: str) -> Cursor:
                return Cursor("not-ok" if "integrity" in statement else None)

            def close(self) -> None:
                pass

        with (
            patch("tools.sqlite_authority_adapter.sqlite3.connect", return_value=Connection()),
            self.assertRaisesRegex(SQLiteAuthorityError, "not clean"),
        ):
            self.adapter.snapshot("discover", CONTEXT)

    def test_bound_rollback_rejects_stale_and_replaced_sessions_before_sqlite(self) -> None:
        rollback = {**CONTEXT, "project_id": PROJECT, "target": "rollback"}
        ambiguous = self.session.mark_ambiguous(1, "rollback-stale")
        before_stale = self._durable_state()
        with (
            patch.object(
                self.adapter, "snapshot", side_effect=AssertionError("SQLite reached")
            ) as snapshot,
            patch.object(
                self.adapter, "execute", side_effect=AssertionError("execute reached")
            ) as execute,
            self.assertRaisesRegex(SQLiteAuthorityError, "trusted SQLite session"),
        ):
            self.adapter.verify_rollback_context_bound(
                rollback,
                self.scope,
                lease=self.lease,
                admission_recheck=self.recheck,
            )
        snapshot.assert_not_called()
        execute.assert_not_called()
        self.assertEqual(before_stale, self._durable_state())
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
        before_replaced = self._durable_state()
        with (
            patch.object(
                self.adapter, "snapshot", side_effect=AssertionError("SQLite reached")
            ) as snapshot,
            patch.object(
                self.adapter, "execute", side_effect=AssertionError("execute reached")
            ) as execute,
            self.assertRaisesRegex(SQLiteAuthorityError, "trusted SQLite session"),
        ):
            self.adapter.verify_rollback_context_bound(
                rollback,
                self.scope,
                lease=self.lease,
                admission_recheck=self.recheck,
            )
        snapshot.assert_not_called()
        execute.assert_not_called()
        self.assertEqual(before_replaced, self._durable_state())
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_bound_rollback_rejects_tampered_sqlite_results_without_state_change(self) -> None:
        rollback = {**CONTEXT, "project_id": PROJECT, "target": "rollback"}

        class TamperedAdapter(SQLiteAuthorityAdapter):
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
            ("sqlite_integrity_verified", False, "integrity is unverified"),
            ("sqlite_foreign_keys_verified", False, "foreign keys are unverified"),
            ("mutates_authority", True, "not read-only"),
        )
        for field, replacement, message in fields:
            with self.subTest(field=field):
                adapter = type(
                    "RollbackTamperedSQLiteAdapter",
                    (TamperedAdapter,),
                    {"field": field, "replacement": replacement},
                )(self.authority)
                before = self._durable_state()
                with (
                    patch.object(
                        adapter, "execute", side_effect=AssertionError("execute reached")
                    ) as execute,
                    self.assertRaisesRegex(SQLiteAuthorityError, message),
                ):
                    adapter.verify_rollback_context_bound(
                        rollback,
                        self.scope,
                        lease=self.lease,
                        admission_recheck=self.recheck,
                    )
                execute.assert_not_called()
                self.assertEqual(before, self._durable_state())
                self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_bound_rollback_rejects_authority_and_descriptor_drift_without_execute(self) -> None:
        rollback = {**CONTEXT, "project_id": PROJECT, "target": "rollback"}
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
        before = self._durable_state()
        with (
            patch.object(
                self.adapter, "snapshot", side_effect=AssertionError("SQLite reached")
            ) as snapshot,
            patch.object(
                self.adapter, "execute", side_effect=AssertionError("execute reached")
            ) as execute,
            self.assertRaisesRegex(SQLiteAuthorityError, "trusted SQLite session reread"),
        ):
            self.adapter.verify_rollback_context_bound(
                {**rollback, "authority_revision": "authority-drift"},
                self.scope,
                lease=drifted,
                admission_recheck=drifted_recheck,
            )
        snapshot.assert_not_called()
        execute.assert_not_called()
        self.assertEqual(before, self._durable_state())
        self.assertFalse(self.session.operation_owned_by_current_thread)

        replacement = self.root / "rollback-authority-replacement.sqlite"
        replacement.write_bytes(self.authority.read_bytes())
        replacement.chmod(0o600)
        before_descriptor = (
            self.authority.read_bytes(),
            self.session.control_store_path.read_bytes(),
        )
        replacement.replace(self.authority)
        with (
            patch.object(
                self.adapter, "execute", side_effect=AssertionError("execute reached")
            ) as execute,
            self.assertRaisesRegex(SQLiteAuthorityError, "trusted SQLite session reread"),
        ):
            self.adapter.verify_rollback_context_bound(
                rollback,
                self.scope,
                lease=self.lease,
                admission_recheck=self.recheck,
            )
        execute.assert_not_called()
        self.assertEqual(
            before_descriptor,
            (self.authority.read_bytes(), self.session.control_store_path.read_bytes()),
        )
        self.assertFalse(self.session.operation_owned_by_current_thread)

    def test_bound_rollback_rejects_malformed_admission_before_sqlite(self) -> None:
        common = {
            "context": {**CONTEXT, "project_id": PROJECT, "target": "rollback"},
            "scope": self.scope,
            "lease": self.lease,
            "admission_recheck": self.recheck,
        }
        bound = cast(Any, self.adapter.verify_rollback_context_bound)
        cases = (
            ("lease", cast(Any, object()), "trusted admission lease"),
            ("admission_recheck", cast(Any, object()), "trusted admission recheck"),
            ("scope", cast(Any, object()), "concrete lock-domain scope"),
            (
                "context",
                {**CONTEXT, "project_id": PROJECT, "target": "unexpected"},
                "rollback context target",
            ),
        )
        for field, value, message in cases:
            with self.subTest(field=field):
                before = self._durable_state()
                with (
                    patch.object(
                        self.adapter, "snapshot", side_effect=AssertionError("SQLite reached")
                    ) as snapshot,
                    patch.object(
                        self.adapter, "execute", side_effect=AssertionError("execute reached")
                    ) as execute,
                    self.assertRaisesRegex(SQLiteAuthorityError, message),
                ):
                    bound(**{**common, field: value})
                snapshot.assert_not_called()
                execute.assert_not_called()
                self.assertEqual(before, self._durable_state())
                self.assertFalse(self.session.operation_owned_by_current_thread)


if __name__ == "__main__":
    unittest.main()
