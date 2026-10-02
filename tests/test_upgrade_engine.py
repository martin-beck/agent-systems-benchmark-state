# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Failure-path tests for the durable upgrade phase journal."""

from __future__ import annotations

import fcntl
import json
import multiprocessing
import os
import signal
import tempfile
import unittest
from collections.abc import Callable, Mapping
from pathlib import Path
from typing import Any, cast
from unittest.mock import patch

from tools import upgrade_engine as upgrade_engine_module
from tools.authority_mutation import (
    AuthorityMutationAmbiguousError,
    AuthorityMutationRejectedError,
    DurableBoundBackendMutation,
    MutationReceipt,
)
from tools.authority_neutral_backup import BoundBackupPhaseAdapter
from tools.authority_neutral_stage import BoundStagePhaseAdapter
from tools.authority_neutral_validation import BoundValidationPhaseAdapter
from tools.git_authority_adapter import GitAuthorityAdapter
from tools.rollback_control_store import (
    SQLiteAuthorityRuntimeState,
    SQLiteControlStoreAdapter,
    SQLiteRollbackControlStore,
    bind_control_store,
)
from tools.rollback_evidence import BackupObservation
from tools.runtime_bootstrap import DispatchAdmission
from tools.sqlite_authority_adapter import SQLiteAuthorityAdapter
from tools.upgrade_admission import (
    PREFLIGHT_PREDICATES,
    QUIESCENCE_PREDICATES,
    REOPEN_PREDICATES,
)
from tools.upgrade_engine import (
    CONTEXT_FIELDS,
    PHASES,
    BackendAdapter,
    BoundRollbackCapability,
    GitRollbackObservationCapability,
    Handler,
    PhaseContext,
    RollbackAuthorizationCapability,
    RollbackBackupEvidence,
    SQLiteRollbackObservationCapability,
    UpgradeEngine,
    UpgradeError,
)
from tools.upgrade_identity import canonical_barrier_digest, canonical_envelope_digest


def make_context(operation_id: str = "op-1", target: str = "new") -> dict[str, object]:
    context: dict[str, object] = {
        "schema_version": 2,
        "backend": "sqlite",
        "project_id": "11111111-1111-4111-8111-111111111111",
        "operation_id": operation_id,
        "state_revision": 1,
        "authority_revision": "authority-1",
        "fencing_token": "fence-1",
        "fencing_owner": "worker-1",
        "durable_barrier_id": "barrier-1",
        "artifact_root": "/artifacts",
        "source": "/authority.sqlite",
        "destination": "/artifacts/backup.sqlite",
        "manifest": "/artifacts/manifest.json",
        "selector_ref": ".runtime/runtime-selector.json",
        "barrier_identity_digest": "0" * 64,
        "target": target,
        "envelope_digest": "0" * 64,
    }
    context["barrier_identity_digest"] = canonical_barrier_digest(context)
    context["envelope_digest"] = canonical_envelope_digest(context)
    return context


CONTEXT = make_context()
ROLLBACK_CONTEXT = make_context(target="rollback")
ADMISSION = {
    **dict.fromkeys(PREFLIGHT_PREDICATES, True),
    **dict.fromkeys(QUIESCENCE_PREDICATES, True),
    **dict.fromkeys(REOPEN_PREDICATES, True),
    **CONTEXT,
    "barrier_status": "held",
    "reopen_barrier_status": "released",
    "validation_failed": False,
}


def _plan_then_crash_after_journal_replace(journal: str, context: dict[str, object]) -> None:
    """Persist a complete journal, then die before the caller can continue."""
    original_write = upgrade_engine_module._write

    def write_then_crash(path: Path, value: Mapping[str, object]) -> None:
        original_write(path, value)
        os.kill(os.getpid(), signal.SIGKILL)

    with patch.object(upgrade_engine_module, "_write", side_effect=write_then_crash):
        UpgradeEngine("op-1", Path(journal), context).plan()


class StaticAuthorityRuntimeRereader:
    def reread_rollback(
        self, context: Mapping[str, object], _result: Mapping[str, object]
    ) -> SQLiteAuthorityRuntimeState:
        return SQLiteAuthorityRuntimeState(
            backend=cast(str, context["backend"]),
            project_id=cast(str, context["project_id"]),
            authority_revision=cast(str, context["authority_revision"]),
            fencing_token=cast(str, context["fencing_token"]),
            target=cast(str, context["target"]),
            integrity_check="ok",
            foreign_key_violations=0,
            backend_roundtrip="sqlite",
        )


class FakeAdapter:
    def __init__(self) -> None:
        self.rollback_status = "held"

    def verify_rollback_context(self, context: Mapping[str, object]) -> dict[str, object] | None:
        expected = make_context(str(context.get("operation_id")), target="rollback")
        if all(context.get(field) == expected[field] for field in CONTEXT_FIELDS):
            return {**context, "status": self.rollback_status}
        return None

    def snapshot(self, phase: str, context: object) -> dict[str, object]:
        identity = dict(context) if isinstance(context, Mapping) else CONTEXT
        if phase == "rollback":
            return {
                **make_context(str(identity["operation_id"]), target="rollback"),
                "rollback_context_verified": True,
            }
        return {
            **ADMISSION,
            **{field: identity[field] for field in CONTEXT_FIELDS},
        }

    def execute(self, phase: str, _context: object) -> dict[str, object]:
        result: dict[str, object] = {"backend": "sqlite", "fencing_token": "fence-1"}
        if phase == "rollback":
            result.update(
                restored_verified=True,
                runtime_validated=True,
                backend_roundtrip_valid=True,
            )
        return result

    def begin_release_rollback_context(self, _context: Mapping[str, object]) -> dict[str, object]:
        if self.rollback_status != "held":
            raise RuntimeError("barrier is not held")
        self.rollback_status = "releasing"
        return {"status": "releasing"}

    def complete_release_rollback_context(
        self, _context: Mapping[str, object]
    ) -> dict[str, object]:
        if self.rollback_status != "releasing":
            raise RuntimeError("barrier is not releasing")
        self.rollback_status = "released"
        return {"status": "released"}

    def revalidate_rollback(
        self, _context: Mapping[str, object], result: Mapping[str, object]
    ) -> dict[str, object]:
        return dict(result)


class FailingAdapter(FakeAdapter):
    def snapshot(self, _phase: str, _context: object) -> dict[str, object]:
        raise RuntimeError("authority probe failed")


class UpgradeEngineTests(unittest.TestCase):
    def test_bound_commit_capability_is_consumed_by_engine_only_when_supplied(self) -> None:  # noqa: C901
        operation = {
            "operation_id": "op-commit:commit",
            "opcode": "authority.atomic_replace",
            "inputs": {
                "backend": "sqlite",
                "selector_ref": ".runtime/runtime-selector.json",
                "expected_state_revision": 1,
                "barrier_id": "barrier-1",
                "fencing_token": "fence-1",
                "backup_operation_id": "op-commit:backup",
            },
            "timeout_seconds": 300,
            "resources": ["maintenance-barrier"],
            "preconditions": ["previous-phase-complete"],
            "postconditions": ["commit-contract-satisfied"],
            "evidence": ["durable-operation-record"],
            "durable_record": "operation-id-and-outcome",
        }
        context = make_context("op-commit")
        commit_context = {
            "backend": "sqlite",
            "target": "new",
            "operation_id": "op-commit:commit",
            "state_revision": 1,
            "durable_barrier_id": "barrier-1",
            "fencing_token": "fence-1",
        }
        admission = {**ADMISSION, **context}
        evidence = {
            "quiesced": True,
            "backup_verified": True,
            "selector_verified": True,
            "selector_commit_atomic": True,
            "fencing_verified": True,
            "selector_before_verified": True,
            "selector_after_verified": True,
            "admitted_snapshot": admission,
            "current_snapshot": admission,
        }

        class Executor(DurableBoundBackendMutation):
            def __init__(self) -> None:
                self.arguments: list[object] = []

            def execute(self, argument: object) -> MutationReceipt:
                self.arguments.append(argument)
                return MutationReceipt(
                    backend="sqlite",
                    target="new",
                    operation_id="op-commit:commit",
                    state_revision=1,
                    barrier_id="barrier-1",
                    artifact_identity="artifact",
                    manifest_identity="manifest",
                    selector_identity="selector",
                    runtime_identity="runtime",
                    fencing_token="fence-1",  # noqa: S106
                    mutates_authority=True,
                )

        executor = Executor()
        with tempfile.TemporaryDirectory() as directory:
            journal = Path(directory) / "journal.json"
            with self.assertRaisesRegex(UpgradeError, "required together"):
                UpgradeEngine(
                    "op-commit",
                    journal,
                    context,
                    backend_adapter=FakeAdapter(),
                    commit_operation=operation,
                )
            with self.assertRaisesRegex(UpgradeError, "requires a backend adapter"):
                UpgradeEngine(
                    "op-commit",
                    journal,
                    context,
                    commit_operation=operation,
                    commit_context=commit_context,
                    commit_executor=executor,
                    commit_argument="bound-effect",
                    commit_evidence=evidence,
                )
            with self.assertRaisesRegex(UpgradeError, "incomplete or unknown"):
                UpgradeEngine(
                    "op-commit",
                    journal,
                    context,
                    backend_adapter=FakeAdapter(),
                    commit_operation=operation,
                    commit_context=commit_context,
                    commit_executor=executor,
                    commit_argument="bound-effect",
                    commit_evidence={},
                )
            unverified = dict(evidence)
            unverified["backup_verified"] = False
            with self.assertRaisesRegex(UpgradeError, "not verified"):
                UpgradeEngine(
                    "op-commit",
                    journal,
                    context,
                    backend_adapter=FakeAdapter(),
                    commit_operation=operation,
                    commit_context=commit_context,
                    commit_executor=executor,
                    commit_argument="bound-effect",
                    commit_evidence=unverified,
                )
            malformed_snapshots = dict(evidence)
            malformed_snapshots["current_snapshot"] = []
            with self.assertRaisesRegex(UpgradeError, "snapshots are invalid"):
                UpgradeEngine(
                    "op-commit",
                    journal,
                    context,
                    backend_adapter=FakeAdapter(),
                    commit_operation=operation,
                    commit_context=commit_context,
                    commit_executor=executor,
                    commit_argument="bound-effect",
                    commit_evidence=malformed_snapshots,
                )
            malformed_operation = dict(operation)
            malformed_operation["inputs"] = {}
            with self.assertRaisesRegex(UpgradeError, "binding is invalid"):
                UpgradeEngine(
                    "op-commit",
                    journal,
                    context,
                    backend_adapter=FakeAdapter(),
                    commit_operation=malformed_operation,
                    commit_context=commit_context,
                    commit_executor=executor,
                    commit_argument="bound-effect",
                    commit_evidence=evidence,
                )
            foreign_operation = dict(operation)
            foreign_operation["operation_id"] = "foreign:commit"
            with self.assertRaisesRegex(UpgradeError, "operation identity mismatch"):
                UpgradeEngine(
                    "op-commit",
                    journal,
                    context,
                    backend_adapter=FakeAdapter(),
                    commit_operation=foreign_operation,
                    commit_context=commit_context,
                    commit_executor=executor,
                    commit_argument="bound-effect",
                    commit_evidence=evidence,
                )
            foreign_snapshot = dict(evidence)
            foreign_snapshot["current_snapshot"] = {**admission, "project_id": "foreign"}
            with self.assertRaisesRegex(UpgradeError, "admission snapshot identity mismatch"):
                UpgradeEngine(
                    "op-commit",
                    journal,
                    context,
                    backend_adapter=FakeAdapter(),
                    commit_operation=operation,
                    commit_context=commit_context,
                    commit_executor=executor,
                    commit_argument="bound-effect",
                    commit_evidence=foreign_snapshot,
                )
            invalid_predicates = dict(evidence)
            invalid_predicates["admitted_snapshot"] = {
                key: value for key, value in admission.items() if key != "barrier_status"
            }
            with self.assertRaisesRegex(UpgradeError, "admission evidence is invalid"):
                UpgradeEngine(
                    "op-commit",
                    journal,
                    context,
                    backend_adapter=FakeAdapter(),
                    commit_operation=operation,
                    commit_context=commit_context,
                    commit_executor=executor,
                    commit_argument="bound-effect",
                    commit_evidence=invalid_predicates,
                )

        with tempfile.TemporaryDirectory() as directory:
            engine = UpgradeEngine(
                "op-commit",
                Path(directory) / "journal.json",
                context,
                backend_adapter=FakeAdapter(),
                commit_operation=operation,
                commit_context=commit_context,
                commit_executor=executor,
                commit_argument="bound-effect",
                commit_evidence=evidence,
            )
            engine.plan()

            def handler(_step: str, _state: object) -> dict[str, object]:
                return {}

            def phase_handler(phase: str) -> Handler:
                def run(_step: str, _state: object) -> dict[str, object]:
                    result: dict[str, object] = {
                        "backend": "sqlite",
                        "fencing_token": "fence-1",
                        "backend_identity_verified": True,
                    }
                    if phase == "discover":
                        result.update(release_authentic=True, runtime_supported=True)
                    elif phase == "preflight":
                        result.update(preflight_admitted=True, capacity_verified=True)
                        result["preflight_snapshot"] = admission
                    elif phase == "quiesce":
                        result.update(
                            barrier_acquired=True,
                            workers_drained=True,
                            leases_fenced=True,
                            fencing_verified=True,
                        )
                        result["quiescence_snapshot"] = admission
                    elif phase == "backup":
                        result.update(backup_verified=True, restore_roundtrip_verified=True)
                    elif phase == "stage":
                        result.update(staged_verified=True, manifest_verified=True)
                    elif phase == "validate":
                        result.update(
                            runtime_validated=True,
                            backend_roundtrip_valid=True,
                            projections_valid=True,
                            binding_valid=True,
                        )
                    elif phase == "reopen":
                        result.update(validated=True, barrier_held=True)
                        result["reopen_snapshot"] = admission
                    result["mutates_authority"] = phase == "commit"
                    return result

                return run

            handlers = {phase: phase_handler(phase) for phase in PHASES}
            # The commit handler contributes no mutation evidence; the bound
            # capability must supply it through the engine dispatch seam.
            handlers["commit"] = handler
            result = engine.apply(handlers)
            self.assertEqual(result["status"], "completed")
            self.assertEqual(executor.arguments, ["bound-effect"])

        class AmbiguousExecutor(DurableBoundBackendMutation):
            def __init__(self) -> None:
                pass

            def execute(self, _argument: object) -> MutationReceipt:
                raise AuthorityMutationAmbiguousError("unknown authority outcome")

        with tempfile.TemporaryDirectory() as ambiguous_directory:
            ambiguous_engine = UpgradeEngine(
                "op-commit",
                Path(ambiguous_directory) / "journal.json",
                context,
                backend_adapter=FakeAdapter(),
                commit_operation=operation,
                commit_context=commit_context,
                commit_executor=AmbiguousExecutor(),
                commit_argument="bound-effect",
                commit_evidence=evidence,
            )
            ambiguous_engine.plan()
            with self.assertRaisesRegex(UpgradeError, "phase outcome is ambiguous: commit"):
                ambiguous_engine.apply(handlers)
            ambiguous_journal = ambiguous_engine._load()
            self.assertEqual(ambiguous_journal["status"], "safe-mode")
            self.assertEqual(ambiguous_journal["records"][-1]["outcome"], "ambiguous")

    def test_validation_binding_rejects_partial_or_unbound_inputs(self) -> None:
        admission = object.__new__(DispatchAdmission)
        with tempfile.TemporaryDirectory() as directory:
            journal = Path(directory) / "journal.json"
            with self.assertRaisesRegex(UpgradeError, "required together"):
                UpgradeEngine(
                    "op-1",
                    journal,
                    make_context(),
                    validation_admission=admission,
                )
            with self.assertRaisesRegex(UpgradeError, "backend adapter"):
                UpgradeEngine(
                    "op-1",
                    journal,
                    make_context(),
                    validation_admission=admission,
                    validation_operation={"opcode": "runtime.validate"},
                    validation_context={"backend": "sqlite"},
                )
            with self.assertRaisesRegex(UpgradeError, "binding is invalid"):
                UpgradeEngine(
                    "op-1",
                    journal,
                    make_context(),
                    backend_adapter=FakeAdapter(),
                    validation_admission=object(),
                    validation_operation={"opcode": "runtime.validate"},
                    validation_context={"backend": "sqlite"},
                )

    def test_backup_and_stage_bindings_reject_partial_or_invalid_authority(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            journal = Path(directory) / "journal.json"
            with self.assertRaisesRegex(UpgradeError, "supplied together"):
                UpgradeEngine(
                    "op-1", journal, make_context(), backup_operation={"opcode": "backend.backup"}
                )
            with self.assertRaisesRegex(UpgradeError, "backend adapter"):
                UpgradeEngine(
                    "op-1",
                    journal,
                    make_context(),
                    backup_operation={"opcode": "backend.backup"},
                    backup_context={"backend": "sqlite"},
                )
            with self.assertRaisesRegex(UpgradeError, "binding is invalid"):
                UpgradeEngine(
                    "op-1",
                    journal,
                    make_context(),
                    backend_adapter=FakeAdapter(),
                    backup_operation={"opcode": "backend.backup"},
                    backup_context={"backend": "sqlite"},
                )
            with self.assertRaisesRegex(UpgradeError, "supplied together"):
                UpgradeEngine("op-1", journal, make_context(), stage_context={"backend": "sqlite"})
            with self.assertRaisesRegex(UpgradeError, "backend adapter"):
                UpgradeEngine(
                    "op-1",
                    journal,
                    make_context(),
                    stage_operation={"opcode": "backend.stage"},
                    stage_context={"backend": "sqlite"},
                )
            with self.assertRaisesRegex(UpgradeError, "binding is invalid"):
                UpgradeEngine(
                    "op-1",
                    journal,
                    make_context(),
                    backend_adapter=FakeAdapter(),
                    stage_operation={"opcode": "backend.stage"},
                    stage_context={"backend": "sqlite"},
                )

    def test_engine_binds_selector_readiness_to_validate_phase(self) -> None:
        admission = object.__new__(DispatchAdmission)
        with tempfile.TemporaryDirectory() as directory:
            engine = UpgradeEngine(
                "op-1",
                Path(directory) / "journal.json",
                CONTEXT,
                backend_adapter=FakeAdapter(),
                validation_admission=admission,
                validation_operation={
                    "operation_id": "op-1:validate",
                    "opcode": "runtime.validate",
                },
                validation_context={
                    "backend": "sqlite",
                    "target": "new",
                    "operation_id": "op-1",
                    "fencing_token": "fence-1",
                    "binding": {"project_id": CONTEXT["project_id"]},
                },
            )
            capability = engine._validation_phase_adapter
            self.assertIsInstance(capability, BoundValidationPhaseAdapter)
            if capability is None:
                self.fail("validation capability was not bound")
            with patch.object(DispatchAdmission, "revalidate"):
                result = capability.execute("validate", CONTEXT)
            self.assertTrue(result["runtime_validated"])

    def test_engine_binds_verified_stage_capability_to_stage_phase(self) -> None:
        class StageAdapter(FakeAdapter):
            def __init__(self) -> None:
                super().__init__()
                self.stage_calls = 0

            def execute(self, phase: str, context: object) -> dict[str, object]:
                if phase == "stage":
                    self.stage_calls += 1
                return super().execute(phase, context)

        stage_context = {
            **CONTEXT,
            "runtime_root": "/artifacts/runtime",
            "manifest_digest": "a" * 64,
            "binding": {"project_id": CONTEXT["project_id"]},
        }
        with tempfile.TemporaryDirectory() as directory:
            adapter = StageAdapter()
            engine = UpgradeEngine(
                "op-1",
                Path(directory) / "journal.json",
                CONTEXT,
                backend_adapter=adapter,
                stage_operation={"operation_id": "op-1:stage", "opcode": "backend.stage"},
                stage_context=stage_context,
            )
            capability = engine._stage_phase_adapter
            self.assertIsInstance(capability, BoundStagePhaseAdapter)
            if capability is None:
                self.fail("stage capability was not bound")
            with patch("tools.authority_neutral_stage.verify_runtime_manifest", return_value=True):
                result = capability.execute("stage", CONTEXT)
            self.assertTrue(result["staged_verified"])
            self.assertEqual(0, adapter.stage_calls)

    def test_engine_binds_verified_backup_capability_to_backup_phase(self) -> None:
        class GeneratedAdapter(FakeAdapter):
            def __init__(self) -> None:
                super().__init__()
                self.generated_calls = 0

            def execute_generated_operation(
                self,
                _operation: Mapping[str, object],
                _destination: Path,
                _binding: dict[str, Any],
            ) -> dict[str, object]:
                self.generated_calls += 1
                return {
                    "outcome": "completed",
                    "backend": "sqlite",
                    "backup_verified": True,
                    "restore_roundtrip_verified": True,
                    "backend_identity_verified": True,
                    "mutates_authority": False,
                    "fencing_token": "fence-1",
                }

        with tempfile.TemporaryDirectory() as directory:
            adapter = GeneratedAdapter()
            engine = UpgradeEngine(
                "op-1",
                Path(directory) / "journal.json",
                CONTEXT,
                backend_adapter=adapter,
                backup_operation={"opcode": "backend.backup"},
                backup_context={**CONTEXT, "binding": {"project_id": CONTEXT["project_id"]}},
            )
            capability = engine._backup_phase_adapter
            self.assertIsInstance(capability, BoundBackupPhaseAdapter)
            if capability is None:
                self.fail("backup capability was not bound")
            result = capability.execute("backup", CONTEXT)
            self.assertEqual("completed", result["outcome"])
            self.assertEqual(1, adapter.generated_calls)

    def test_bound_capability_rejects_incomplete_bindings_and_contexts(self) -> None:
        context = PhaseContext(**cast(dict[str, Any], ROLLBACK_CONTEXT))
        with self.assertRaisesRegex(UpgradeError, "capability is incomplete"):
            BoundRollbackCapability.bind(context, object())

        class Concrete:
            bound_rollback_kind: str | None = "sqlite"

            def verify_rollback_context_bound(self, _context: Mapping[str, object]) -> Any:
                return None

        with self.assertRaisesRegex(UpgradeError, "binding is incomplete"):
            BoundRollbackCapability.bind(context, Concrete())
        with self.assertRaisesRegex(UpgradeError, "branch binding is invalid"):
            BoundRollbackCapability.bind(
                context,
                Concrete(),
                object(),
                lease=object(),
                admission_recheck=object(),
                expected_branch=cast(Any, 1),
            )
        with self.assertRaisesRegex(UpgradeError, "head binding is invalid"):
            BoundRollbackCapability.bind(
                context,
                Concrete(),
                object(),
                lease=object(),
                admission_recheck=object(),
                expected_head=cast(Any, 1),
            )
        with self.assertRaisesRegex(UpgradeError, "Git rollback identity binding is incomplete"):
            BoundRollbackCapability.bind(
                context,
                Concrete(),
                object(),
                lease=object(),
                admission_recheck=object(),
                expected_branch="main",
            ).verify(ROLLBACK_CONTEXT)

        class Generic(Concrete):
            bound_rollback_kind = None

        capability = BoundRollbackCapability.bind(context, Generic())
        with self.assertRaisesRegex(UpgradeError, "context is incomplete"):
            capability.verify({})
        with self.assertRaisesRegex(UpgradeError, "identity mismatch"):
            capability.verify({**ROLLBACK_CONTEXT, "operation_id": "foreign"})
        with self.assertRaisesRegex(UpgradeError, "result is invalid"):
            capability.verify(ROLLBACK_CONTEXT)

        with self.assertRaisesRegex(UpgradeError, "requires bound evidence"):
            RollbackAuthorizationCapability.bind(context, cast(Any, object()))
        with self.assertRaisesRegex(UpgradeError, "identity mismatch"):
            RollbackAuthorizationCapability.bind(
                PhaseContext(**cast(dict[str, Any], {**ROLLBACK_CONTEXT, "operation_id": "other"})),
                capability,
            )

    def test_concrete_bound_capability_rejects_tampered_envelope_digests(self) -> None:
        class Concrete:
            bound_rollback_kind = "sqlite"

            def verify_rollback_context_bound(
                self, _context: Mapping[str, object], _scope: object, **_kwargs: object
            ) -> Mapping[str, object]:
                self.called = True
                return {}

        adapter = Concrete()
        capability = BoundRollbackCapability.bind(
            PhaseContext(**cast(dict[str, Any], ROLLBACK_CONTEXT)),
            adapter,
            object(),
            lease=object(),
            admission_recheck=object(),
        )
        for field in ("barrier_identity_digest", "envelope_digest"):
            forged = dict(ROLLBACK_CONTEXT, **{field: "f" * 64})
            with self.assertRaisesRegex(UpgradeError, "context identity is invalid"):
                capability.verify(forged)
        self.assertFalse(hasattr(adapter, "called"))

    def test_sqlite_observation_capability_rejects_forged_and_invalid_bindings(self) -> None:
        context = PhaseContext(**cast(dict[str, Any], ROLLBACK_CONTEXT))
        with self.assertRaisesRegex(TypeError, "must be bound"):
            SQLiteRollbackObservationCapability()
        with self.assertRaisesRegex(UpgradeError, "concrete adapter"):
            SQLiteRollbackObservationCapability.bind(context, cast(Any, FakeAdapter()))

        class Provider:
            def observe_backup_identity(
                self, _backup: Path, _manifest: Path, _context: Mapping[str, object]
            ) -> Any:
                return None

        capability = object.__new__(SQLiteRollbackObservationCapability)
        object.__setattr__(capability, "adapter", Provider())
        object.__setattr__(capability, "identity", ())
        with self.assertRaisesRegex(UpgradeError, "identity mismatch"):
            capability.observe({**ROLLBACK_CONTEXT, "operation_id": "foreign"})
        invalid_paths = {**ROLLBACK_CONTEXT, "destination": None}
        object.__setattr__(
            capability,
            "identity",
            tuple(invalid_paths[field] for field in CONTEXT_FIELDS if field != "target"),
        )
        with self.assertRaisesRegex(UpgradeError, "artifact paths"):
            capability.observe(invalid_paths)

    def test_git_observation_capability_rejects_invalid_bindings_and_results(self) -> None:
        context = PhaseContext(**cast(dict[str, Any], ROLLBACK_CONTEXT))
        with tempfile.TemporaryDirectory() as directory:
            adapter = GitAuthorityAdapter(Path(directory))
            with self.assertRaisesRegex(TypeError, "must be bound"):
                GitRollbackObservationCapability()
            with self.assertRaisesRegex(UpgradeError, "branch binding is invalid"):
                GitRollbackObservationCapability.bind(
                    context,
                    adapter,
                    object(),
                    lease=object(),
                    admission_recheck=object(),
                    expected_branch="",
                    expected_head="head",
                )
            with self.assertRaisesRegex(UpgradeError, "head binding is invalid"):
                GitRollbackObservationCapability.bind(
                    context,
                    adapter,
                    object(),
                    lease=object(),
                    admission_recheck=object(),
                    expected_branch="main",
                    expected_head="",
                )
            capability = GitRollbackObservationCapability.bind(
                context,
                adapter,
                object(),
                lease=object(),
                admission_recheck=object(),
                expected_branch="main",
                expected_head="head",
            )
            with (
                patch.object(adapter, "preflight_git", return_value=None),
                self.assertRaisesRegex(UpgradeError, "result is invalid"),
            ):
                capability.observe(ROLLBACK_CONTEXT)

    def test_journal_process_death_reopens_bound_control_and_rejects_revision_drift(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            journal = Path(directory) / "journal.json"
            process = multiprocessing.get_context("fork").Process(
                target=_plan_then_crash_after_journal_replace,
                args=(str(journal), CONTEXT),
            )
            process.start()
            process.join(timeout=10)
            self.assertEqual(-signal.SIGKILL, process.exitcode)
            self.assertFalse(process.is_alive())

            persisted = json.loads(journal.read_text(encoding="utf-8"))
            self.assertEqual(
                CONTEXT["authority_revision"], persisted["context"]["authority_revision"]
            )
            self.assertEqual(CONTEXT["fencing_token"], persisted["context"]["fencing_token"])
            self.assertEqual(
                CONTEXT["barrier_identity_digest"], persisted["context"]["barrier_identity_digest"]
            )
            self.assertEqual(CONTEXT["envelope_digest"], persisted["context"]["envelope_digest"])
            self.assertEqual(
                "planned",
                UpgradeEngine("op-1", journal, CONTEXT)._load()["status"],
            )

            for field, replacement in (
                ("authority_revision", "authority-2"),
                ("fencing_token", "fence-2"),
            ):
                with self.subTest(field=field):
                    drifted = make_context()
                    drifted[field] = replacement
                    drifted["barrier_identity_digest"] = canonical_barrier_digest(drifted)
                    drifted["envelope_digest"] = canonical_envelope_digest(drifted)
                    with self.assertRaisesRegex(UpgradeError, "context is invalid or changed"):
                        UpgradeEngine("op-1", journal, drifted)._load()

    @staticmethod
    def _prepare_failed_journal(
        directory: str, operation_id: str, adapter: BackendAdapter
    ) -> tuple[Path, UpgradeEngine]:
        journal = Path(directory) / "journal.json"
        engine = UpgradeEngine(
            operation_id,
            journal,
            make_context(operation_id),
            backend_adapter=adapter,
        )
        engine.plan()
        value = json.loads(journal.read_text())
        value["status"] = "failed"
        value["phase"] = "discover"
        value["records"] = [
            {
                "operation_id": operation_id,
                "step_id": f"{operation_id}.discover",
                "phase": "discover",
                "outcome": "failed",
                "error": "failed",
                "context": make_context(operation_id),
            }
        ]
        journal.write_text(json.dumps(value))
        return journal, engine

    def test_apply_is_ordered_and_idempotent(self) -> None:  # noqa: C901
        with tempfile.TemporaryDirectory() as directory:
            engine = UpgradeEngine(
                "op-1", Path(directory) / "journal.json", CONTEXT, backend_adapter=FakeAdapter()
            )
            engine.plan()
            seen: list[str] = []

            def handler(  # noqa: C901
                _operation: str, _state: object, phase: str = ""
            ) -> dict[str, object]:
                seen.append(phase)
                result: dict[str, object] = {
                    "phase": phase,
                    "backend": "sqlite",
                    "fencing_token": "fence-1",
                    "backend_identity_verified": True,
                }
                if phase == "discover":
                    result.update(release_authentic=True, runtime_supported=True)
                if phase == "preflight":
                    result.update(preflight_admitted=True, capacity_verified=True)
                if phase == "quiesce":
                    result.update(
                        barrier_acquired=True,
                        workers_drained=True,
                        leases_fenced=True,
                        fencing_verified=True,
                    )
                if phase == "backup":
                    result.update(backup_verified=True, restore_roundtrip_verified=True)
                if phase == "stage":
                    result.update(staged_verified=True, manifest_verified=True)
                if phase == "commit":
                    result.update(
                        quiesced=True,
                        backup_verified=True,
                        selector_verified=True,
                        selector_commit_atomic=True,
                        fencing_verified=True,
                        selector_before_verified=True,
                        selector_after_verified=True,
                    )
                if phase == "validate":
                    result.update(
                        runtime_validated=True,
                        backend_roundtrip_valid=True,
                        projections_valid=True,
                        binding_valid=True,
                    )
                if phase == "reopen":
                    result.update(validated=True, barrier_held=True)
                if phase == "preflight":
                    result["preflight_snapshot"] = ADMISSION
                if phase == "quiesce":
                    result["quiescence_snapshot"] = ADMISSION
                if phase == "commit":
                    result.update(admitted_snapshot=ADMISSION, current_snapshot=ADMISSION)
                if phase == "reopen":
                    result["reopen_snapshot"] = ADMISSION
                result["mutates_authority"] = phase == "commit"
                return result

            def make_handler(phase: str) -> Handler:
                def run(operation: str, state: object) -> dict[str, object]:
                    return handler(operation, state, phase)

                return run

            handlers: dict[str, Handler] = {phase: make_handler(phase) for phase in PHASES}
            result = engine.apply(handlers)
            self.assertEqual(seen, list(PHASES))
            self.assertEqual(result["status"], "completed")
            engine.apply(handlers)
            self.assertEqual(seen, list(PHASES))

    def test_failure_is_durable_and_rollback_can_enter_safe_mode(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            engine = UpgradeEngine(
                "op-2",
                Path(directory) / "journal.json",
                make_context("op-2"),
                backend_adapter=FakeAdapter(),
            )
            engine.plan()

            def fail(_operation: str, _state: object) -> None:
                raise OSError("ambiguous")

            handlers: dict[str, Handler] = {
                phase: (fail if phase == "commit" else lambda _operation, _state: {})
                for phase in PHASES
            }
            with self.assertRaises(UpgradeError):
                engine.apply(handlers)
            with self.assertRaises(UpgradeError):
                engine.rollback(fail)
            self.assertEqual(engine._load()["status"], "safe-mode")

    def test_apply_abort_after_phase_start_preserves_recovery_marker(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            journal = Path(directory) / "journal.json"

            class AbortAdapter(FakeAdapter):
                def execute(self, phase: str, context: object) -> dict[str, object]:
                    if phase == "discover":
                        raise SystemExit("process aborted during discover")
                    return super().execute(phase, context)

            operation_id = "op-apply-abort"
            engine = UpgradeEngine(
                operation_id,
                journal,
                make_context(operation_id),
                backend_adapter=AbortAdapter(),
            )
            engine.plan()
            handlers: dict[str, Handler] = {
                phase: (lambda _operation, _state: {}) for phase in PHASES
            }

            with self.assertRaises(SystemExit):
                engine.apply(handlers)

            persisted = json.loads(journal.read_text(encoding="utf-8"))
            self.assertEqual("running", persisted["status"])
            self.assertEqual("discover", persisted["phase"])
            self.assertEqual("started", persisted["records"][-1]["outcome"])
            self.assertEqual(
                operation_id,
                persisted["records"][-1]["operation_id"],
            )

    def test_commit_validate_and_reopen_require_safety_evidence(self) -> None:  # noqa: C901
        with tempfile.TemporaryDirectory() as directory:
            engine = UpgradeEngine(
                "op-evidence",
                Path(directory) / "journal.json",
                make_context("op-evidence"),
                backend_adapter=FakeAdapter(),
            )
            engine.plan()

            def evidence_handler(phase: str) -> Handler:  # noqa: C901
                def run(  # noqa: C901
                    _operation: str, _state: object
                ) -> dict[str, object]:
                    result: dict[str, object] = {
                        "backend": "sqlite",
                        "fencing_token": "fence-1",
                        "backend_identity_verified": True,
                        "mutates_authority": phase == "commit",
                    }
                    if phase == "discover":
                        result.update(release_authentic=True, runtime_supported=True)
                    if phase == "preflight":
                        result.update(preflight_admitted=True, capacity_verified=True)
                    if phase == "quiesce":
                        result.update(
                            barrier_acquired=True,
                            workers_drained=True,
                            leases_fenced=True,
                            fencing_verified=True,
                        )
                    if phase == "backup":
                        result.update(backup_verified=True, restore_roundtrip_verified=True)
                    if phase == "stage":
                        result.update(staged_verified=True, manifest_verified=True)
                    if phase == "preflight":
                        result["preflight_snapshot"] = ADMISSION
                    if phase == "quiesce":
                        result["quiescence_snapshot"] = ADMISSION
                    if phase == "commit":
                        result.update(admitted_snapshot=ADMISSION, current_snapshot=ADMISSION)
                    if phase == "reopen":
                        result["reopen_snapshot"] = ADMISSION
                    return result

                return run

            handlers: dict[str, Handler] = {phase: evidence_handler(phase) for phase in PHASES}
            with self.assertRaises(UpgradeError):
                engine.apply(handlers)
            journal = engine._load()
            self.assertEqual(journal["phase"], "commit")
            self.assertEqual(journal["status"], "failed")

    def test_missing_plan_and_duplicate_plan_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            journal = Path(directory) / "journal.json"
            engine = UpgradeEngine(
                "op-3", journal, make_context("op-3"), backend_adapter=FakeAdapter()
            )
            with self.assertRaises(UpgradeError):
                engine.apply({})
            engine.plan()
            with self.assertRaises(UpgradeError):
                engine.plan()

    def test_rollback_without_backend_is_rejected_before_recovery(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            engine = UpgradeEngine(
                "op-no-rollback-backend",
                Path(directory) / "journal.json",
                make_context("op-no-rollback-backend"),
            )
            engine.plan()
            with self.assertRaisesRegex(UpgradeError, "backend adapter is required for rollback"):
                engine.rollback(lambda _step, _state: {})

    def test_bound_rollback_verification_failure_is_write_closed(self) -> None:
        class RaisingAdapter(FakeAdapter):
            requires_bound_rollback = True

            def verify_rollback_context_bound(
                self, _context: Mapping[str, object]
            ) -> Mapping[str, object]:
                raise RuntimeError("verification unavailable")

        with tempfile.TemporaryDirectory() as directory:
            operation_id = "op-bound-verification-failure"
            adapter = RaisingAdapter()
            engine = UpgradeEngine(
                operation_id,
                Path(directory) / "journal.json",
                make_context(operation_id),
                backend_adapter=adapter,
                rollback_bound_verifier=BoundRollbackCapability.bind(
                    PhaseContext(**cast(dict[str, Any], make_context(operation_id))), adapter
                ),
            )
            engine.plan()
            with self.assertRaisesRegex(UpgradeError, "trusted bound rollback verification failed"):
                engine.rollback(lambda _step, _state: {})

    def test_finish_verified_rollback_requires_bound_context(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            engine = UpgradeEngine(
                "op-no-recovery-context",
                Path(directory) / "journal.json",
                make_context("op-no-recovery-context"),
                backend_adapter=FakeAdapter(),
            )
            with self.assertRaisesRegex(UpgradeError, "recovery context is unavailable"):
                engine._finish_verified_rollback({}, {"result": {}})

    def test_context_digest_and_target_shapes_are_strict(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            for field, value in (
                ("backend", "unknown"),
                ("target", "upgrade"),
                ("barrier_identity_digest", "not-a-digest"),
                ("envelope_digest", "not-a-digest"),
            ):
                with self.subTest(field=field), self.assertRaises(UpgradeError):
                    UpgradeEngine(
                        "op-shape",
                        Path(directory) / f"{field}.json",
                        {**CONTEXT, field: value},
                        backend_adapter=FakeAdapter(),
                    )

    def test_context_and_journal_tampering_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            journal = Path(directory) / "journal.json"
            engine = UpgradeEngine(
                "op-4", journal, make_context("op-4"), backend_adapter=FakeAdapter()
            )
            engine.plan()
            with self.assertRaises(UpgradeError):
                engine.rollback(lambda _step, _state: {})
            value = json.loads(journal.read_text())
            value["context"]["backend"] = "git"
            journal.write_text(json.dumps(value))
            with self.assertRaises(UpgradeError):
                engine.apply({})

    def test_malformed_journal_cross_products_fail_closed_through_apply(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            operation_id = "op-malformed"
            journal = Path(directory) / "journal.json"
            engine = UpgradeEngine(
                operation_id,
                journal,
                make_context(operation_id),
                backend_adapter=FakeAdapter(),
            )
            planned = engine.plan()
            context = make_context(operation_id)

            def ordinary(outcome: str = "started") -> dict[str, object]:
                record: dict[str, object] = {
                    "operation_id": operation_id,
                    "step_id": f"{operation_id}.discover",
                    "phase": "discover",
                    "outcome": outcome,
                    "context": context,
                }
                if outcome == "success":
                    record["result"] = {}
                if outcome in {"failed", "ambiguous"}:
                    record["error"] = "failure"
                return record

            cases: tuple[tuple[str, Callable[[dict[str, object]], None], str], ...] = (
                (
                    "unknown schema",
                    lambda value: value.update(schema_version=99),
                    "identity or records",
                ),
                (
                    "extra top-level field",
                    lambda value: value.update(extra=True),
                    "identity or records",
                ),
                (
                    "changed operation",
                    lambda value: value.update(operation_id="other"),
                    "identity or records",
                ),
                (
                    "unknown status",
                    lambda value: value.update(status="unknown"),
                    "identity or records",
                ),
                (
                    "non-mapping context",
                    lambda value: value.update(context=[]),
                    "context is invalid or changed",
                ),
                (
                    "non-list records",
                    lambda value: value.update(records={}),
                    "records are invalid",
                ),
                (
                    "non-mapping record",
                    lambda value: value.update(status="running", phase="discover", records=[None]),
                    "record is invalid",
                ),
                (
                    "missing phase",
                    lambda value: value.update(
                        status="running", phase="discover", records=[{"phase": None}]
                    ),
                    "record phase is missing",
                ),
                (
                    "out-of-order first phase",
                    lambda value: value.update(
                        status="running",
                        phase="preflight",
                        records=[
                            {
                                **ordinary(),
                                "phase": "preflight",
                                "step_id": f"{operation_id}.preflight",
                            }
                        ],
                    ),
                    "phase identity is invalid",
                ),
                (
                    "unknown outcome",
                    lambda value: value.update(
                        status="running",
                        phase="discover",
                        records=[{**ordinary(), "outcome": "unknown"}],
                    ),
                    "outcome is invalid",
                ),
                (
                    "extra outcome field",
                    lambda value: value.update(
                        status="running",
                        phase="discover",
                        records=[{**ordinary(), "extra": True}],
                    ),
                    "record fields are invalid",
                ),
                (
                    "success without result mapping",
                    lambda value: value.update(
                        status="running",
                        phase="discover",
                        records=[{**ordinary("success"), "result": None}],
                    ),
                    "successful phase lacks result",
                ),
                (
                    "success without result field",
                    lambda value: value.update(
                        status="running",
                        phase="discover",
                        records=[
                            {
                                key: item
                                for key, item in ordinary("success").items()
                                if key != "result"
                            }
                        ],
                    ),
                    "phase outcome fields are invalid",
                ),
                (
                    "failure without string error",
                    lambda value: value.update(
                        status="failed",
                        phase="discover",
                        records=[{**ordinary("failed"), "error": None}],
                    ),
                    "failed phase lacks error",
                ),
                (
                    "planned with records",
                    lambda value: value.update(records=[ordinary()]),
                    "planned journal contains records",
                ),
                (
                    "planned with active phase",
                    lambda value: value.update(phase="discover"),
                    "planned journal has an active phase",
                ),
                (
                    "running without records",
                    lambda value: value.update(status="running", phase="discover"),
                    "running journal is not recoverable",
                ),
                (
                    "running with inconsistent phase",
                    lambda value: value.update(
                        status="running", phase="preflight", records=[ordinary()]
                    ),
                    "running journal phase is inconsistent",
                ),
                (
                    "failed without failed phase",
                    lambda value: value.update(status="failed", phase="discover"),
                    "failed journal has no failed phase",
                ),
                (
                    "completed without all phases",
                    lambda value: value.update(
                        status="completed", phase="discover", records=[ordinary("success")]
                    ),
                    "completed journal is incomplete",
                ),
                (
                    "rolled back without completion",
                    lambda value: value.update(
                        status="rolled-back", phase="rollback", records=[ordinary("failed")]
                    ),
                    "rolled-back journal lacks rollback completion",
                ),
            )
            for name, mutate, expected in cases:
                value = json.loads(json.dumps(planned))
                mutate(value)
                journal.write_text(json.dumps(value))
                with self.subTest(name=name), self.assertRaisesRegex(UpgradeError, expected):
                    engine.apply({})

            journal.write_text("not-json")
            with self.assertRaisesRegex(UpgradeError, "journal is unreadable"):
                engine.apply({})

    def test_schema_v2_journal_is_refused_without_implicit_migration(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            journal = Path(directory) / "journal.json"
            engine = UpgradeEngine(
                "op-schema-v2",
                journal,
                make_context("op-schema-v2"),
                backend_adapter=FakeAdapter(),
            )
            current = engine.plan()
            legacy = {**current, "schema_version": 2, "rollback_verified": False}
            journal.write_text(json.dumps(legacy))
            before = journal.read_bytes()
            with self.assertRaisesRegex(UpgradeError, "schema v2 requires recovery"):
                engine._load()
            self.assertEqual(before, journal.read_bytes())

    def test_every_journal_record_context_field_is_bound(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            journal = Path(directory) / "journal.json"
            engine = UpgradeEngine(
                "op-record",
                journal,
                make_context("op-record"),
                backend_adapter=FakeAdapter(),
            )
            engine.plan()
            base = json.loads(journal.read_text())
            base["status"] = "running"
            base["phase"] = "discover"
            base["records"] = [
                {
                    "operation_id": "op-record",
                    "step_id": "op-record.discover",
                    "phase": "discover",
                    "outcome": "started",
                    "context": make_context("op-record"),
                }
            ]
            for field in CONTEXT:
                tampered = json.loads(json.dumps(base))
                tampered["records"][0]["context"][field] = "tampered"
                journal.write_text(json.dumps(tampered))
                with self.subTest(field=field), self.assertRaises(UpgradeError):
                    engine._load()

    def test_rollback_record_schema_and_target_are_strict(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            journal = Path(directory) / "journal.json"
            engine = UpgradeEngine(
                "op-rollback",
                journal,
                make_context("op-rollback"),
                backend_adapter=FakeAdapter(),
            )
            engine.plan()
            base = json.loads(journal.read_text())
            record = {
                "operation_id": "op-rollback",
                "step_id": "op-rollback.rollback",
                "phase": "rollback",
                "outcome": "started",
                "context": make_context("op-rollback", target="rollback"),
            }
            for mutation in (
                {
                    "context": {
                        **cast(dict[str, object], record["context"]),
                        "target": "new",
                    }
                },
                {"extra": True},
                {"phase": None},
            ):
                value = json.loads(json.dumps(base))
                value["records"] = [{**record, **mutation}]
                journal.write_text(json.dumps(value))
                with self.subTest(mutation=mutation), self.assertRaises(UpgradeError):
                    engine._load()

    def test_rollback_record_and_terminal_status_cross_products_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            operation_id = "op-rollback-matrix"
            journal = Path(directory) / "journal.json"
            engine = UpgradeEngine(
                operation_id,
                journal,
                make_context(operation_id),
                backend_adapter=FakeAdapter(),
            )
            planned = engine.plan()
            failed_phase: dict[str, object] = {
                "operation_id": operation_id,
                "step_id": f"{operation_id}.discover",
                "phase": "discover",
                "outcome": "failed",
                "error": "failure",
                "context": make_context(operation_id),
            }
            rollback_context = make_context(operation_id, target="rollback")
            verified_result: dict[str, object] = {
                "restored_verified": True,
                "runtime_validated": True,
                "backend_roundtrip_valid": True,
                "backend": "sqlite",
                "fencing_token": rollback_context["fencing_token"],
            }

            def rollback_record(outcome: str = "started") -> dict[str, object]:
                record: dict[str, object] = {
                    "operation_id": operation_id,
                    "step_id": f"{operation_id}.rollback",
                    "phase": "rollback",
                    "outcome": outcome,
                    "context": rollback_context,
                }
                if outcome in {"rollback_verified", "rollback_completed"}:
                    record["result"] = verified_result
                if outcome == "ambiguous":
                    record["error"] = "failure"
                return record

            mismatched_context = {
                **rollback_context,
                "authority_revision": "different-authority",
            }
            mismatched_context["barrier_identity_digest"] = canonical_barrier_digest(
                mismatched_context
            )
            mismatched_context["envelope_digest"] = canonical_envelope_digest(mismatched_context)
            cases: tuple[tuple[str, list[object], str, str, str], ...] = (
                (
                    "duplicate rollback",
                    [failed_phase, rollback_record(), rollback_record()],
                    "failed",
                    "discover",
                    "duplicate rollback record",
                ),
                (
                    "phase after rollback",
                    [failed_phase, rollback_record(), failed_phase],
                    "failed",
                    "discover",
                    "phase follows rollback record",
                ),
                (
                    "rollback operation mismatch",
                    [failed_phase, {**rollback_record(), "operation_id": "other"}],
                    "failed",
                    "discover",
                    "rollback identity is invalid",
                ),
                (
                    "unknown rollback outcome",
                    [failed_phase, {**rollback_record(), "outcome": "unknown"}],
                    "failed",
                    "discover",
                    "rollback outcome is invalid",
                ),
                (
                    "missing rollback context",
                    [failed_phase, {**rollback_record(), "context": None}],
                    "failed",
                    "discover",
                    "verified rollback context is required",
                ),
                (
                    "new target rollback context",
                    [
                        failed_phase,
                        {**rollback_record(), "context": make_context(operation_id)},
                    ],
                    "failed",
                    "discover",
                    "rollback context target is invalid",
                ),
                (
                    "changed authority revision",
                    [failed_phase, {**rollback_record(), "context": mismatched_context}],
                    "failed",
                    "discover",
                    "rollback context mismatch: authority_revision",
                ),
                (
                    "extra rollback field",
                    [failed_phase, {**rollback_record(), "extra": True}],
                    "failed",
                    "discover",
                    "rollback context is invalid",
                ),
                (
                    "verified rollback without result mapping",
                    [
                        failed_phase,
                        {**rollback_record("rollback_verified"), "result": None},
                    ],
                    "failed",
                    "discover",
                    "verified rollback lacks result evidence",
                ),
                (
                    "verified rollback without result field",
                    [
                        failed_phase,
                        {
                            key: item
                            for key, item in rollback_record("rollback_verified").items()
                            if key != "result"
                        },
                    ],
                    "failed",
                    "discover",
                    "rollback record fields are invalid",
                ),
                (
                    "ambiguous rollback without error string",
                    [failed_phase, {**rollback_record("ambiguous"), "error": None}],
                    "safe-mode",
                    "discover",
                    "ambiguous rollback lacks error evidence",
                ),
                (
                    "incomplete verified result",
                    [
                        failed_phase,
                        {**rollback_record("rollback_verified"), "result": {}},
                    ],
                    "failed",
                    "discover",
                    "rollback result schema is invalid",
                ),
                (
                    "failed status with rollback completion",
                    [failed_phase, rollback_record("rollback_completed")],
                    "failed",
                    "discover",
                    "failed journal has rollback completion",
                ),
                (
                    "safe mode discards verified rollback",
                    [failed_phase, rollback_record("rollback_verified")],
                    "safe-mode",
                    "discover",
                    "safe-mode journal cannot discard verified rollback recovery",
                ),
                (
                    "rolled back with wrong phase",
                    [failed_phase, rollback_record("rollback_completed")],
                    "rolled-back",
                    "discover",
                    "rolled-back journal phase is inconsistent",
                ),
            )
            for name, records, status, phase, expected in cases:
                value = json.loads(json.dumps(planned))
                value.update(status=status, phase=phase, records=records)
                journal.write_text(json.dumps(value))
                with self.subTest(name=name), self.assertRaisesRegex(UpgradeError, expected):
                    engine.apply({})

    def test_successful_rollback_requires_and_writes_terminal_record(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            journal = Path(directory) / "journal.json"
            engine = UpgradeEngine(
                "op-success-rollback",
                journal,
                make_context("op-success-rollback"),
                backend_adapter=FakeAdapter(),
            )
            engine.plan()
            value = json.loads(journal.read_text())
            value["status"] = "failed"
            value["phase"] = "discover"
            value["records"] = [
                {
                    "operation_id": "op-success-rollback",
                    "step_id": "op-success-rollback.discover",
                    "phase": "discover",
                    "outcome": "failed",
                    "error": "failed",
                    "context": make_context("op-success-rollback"),
                }
            ]
            journal.write_text(json.dumps(value))
            result = engine.rollback(lambda _step, _state: {})
            self.assertEqual("rolled-back", result["status"])
            self.assertEqual("rollback_completed", result["records"][-1]["outcome"])

            reloaded = UpgradeEngine(
                "op-success-rollback",
                journal,
                make_context("op-success-rollback"),
                backend_adapter=FakeAdapter(),
            )
            self.assertEqual("rollback", reloaded._load()["phase"])

            valid = json.loads(journal.read_text())
            tampered = json.loads(json.dumps(valid))
            tampered["records"][-1]["context"]["envelope_digest"] = "e" * 64
            journal.write_text(json.dumps(tampered))
            with self.assertRaises(UpgradeError):
                reloaded._load()

            tampered = json.loads(json.dumps(valid))
            tampered["records"][-1]["outcome"] = "rollback_verified"
            journal.write_text(json.dumps(tampered))
            with self.assertRaises(UpgradeError):
                reloaded._load()

    def test_rollback_verified_is_durable_before_release_and_revalidated(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            events: list[str] = []
            journal = Path(directory) / "journal.json"

            class OrderingAdapter(FakeAdapter):
                def execute(self, phase: str, context: object) -> dict[str, object]:
                    if phase == "rollback":
                        events.append("restore")
                    return super().execute(phase, context)

                def begin_release_rollback_context(
                    self, context: Mapping[str, object]
                ) -> dict[str, object]:
                    durable = json.loads(journal.read_text())
                    self.assert_verified(durable)
                    events.append("begin_release")
                    return super().begin_release_rollback_context(context)

                @staticmethod
                def assert_verified(durable: Mapping[str, object]) -> None:
                    records = cast(list[dict[str, object]], durable["records"])
                    if records[-1]["outcome"] != "rollback_verified":
                        raise AssertionError("rollback verification was not durable before release")

                def revalidate_rollback(
                    self, context: Mapping[str, object], result: Mapping[str, object]
                ) -> dict[str, object]:
                    events.append(f"revalidate:{self.rollback_status}")
                    return super().revalidate_rollback(context, result)

                def complete_release_rollback_context(
                    self, context: Mapping[str, object]
                ) -> dict[str, object]:
                    events.append("complete_release")
                    return super().complete_release_rollback_context(context)

            adapter = OrderingAdapter()
            _, engine = self._prepare_failed_journal(directory, "op-order", adapter)
            result = engine.rollback(lambda _step, _state: {})
            self.assertEqual(
                [
                    "restore",
                    "begin_release",
                    "revalidate:releasing",
                    "complete_release",
                    "revalidate:released",
                ],
                events,
            )
            self.assertEqual("rollback_completed", result["records"][-1]["outcome"])

    def test_crash_during_release_resumes_without_repeating_restore(self) -> None:
        for crash_point in ("begin", "complete"):
            with self.subTest(crash_point=crash_point), tempfile.TemporaryDirectory() as directory:

                class CrashAdapter(FakeAdapter):
                    def __init__(self, point: str) -> None:
                        super().__init__()
                        self.crash_point = point
                        self.crashed = False
                        self.restore_calls = 0

                    def execute(self, phase: str, context: object) -> dict[str, object]:
                        if phase == "rollback":
                            self.restore_calls += 1
                        return super().execute(phase, context)

                    def begin_release_rollback_context(
                        self, context: Mapping[str, object]
                    ) -> dict[str, object]:
                        result = super().begin_release_rollback_context(context)
                        if self.crash_point == "begin" and not self.crashed:
                            self.crashed = True
                            raise SystemExit("crash after durable releasing")
                        return result

                    def complete_release_rollback_context(
                        self, context: Mapping[str, object]
                    ) -> dict[str, object]:
                        result = super().complete_release_rollback_context(context)
                        if self.crash_point == "complete" and not self.crashed:
                            self.crashed = True
                            raise SystemExit("crash after durable released")
                        return result

                adapter = CrashAdapter(crash_point)
                operation_id = f"op-crash-{crash_point}"
                journal, engine = self._prepare_failed_journal(directory, operation_id, adapter)
                with self.assertRaises(SystemExit):
                    engine.rollback(lambda _step, _state: {})
                interrupted = json.loads(journal.read_text())
                self.assertEqual("rollback_verified", interrupted["records"][-1]["outcome"])
                self.assertEqual(1, adapter.restore_calls)
                recovered = UpgradeEngine(
                    operation_id,
                    journal,
                    make_context(operation_id),
                    backend_adapter=adapter,
                ).rollback(lambda _step, _state: self.fail("restore handler was repeated"))
                self.assertEqual("rolled-back", recovered["status"])
                self.assertEqual("rollback_completed", recovered["records"][-1]["outcome"])
                self.assertEqual("released", adapter.rollback_status)
                self.assertEqual(1, adapter.restore_calls)

    def test_abort_during_rollback_execute_preserves_started_marker(self) -> None:
        with tempfile.TemporaryDirectory() as directory:

            class AbortAdapter(FakeAdapter):
                def execute(self, phase: str, context: object) -> dict[str, object]:
                    if phase == "rollback":
                        raise SystemExit("process aborted during rollback")
                    return super().execute(phase, context)

            operation_id = "op-rollback-abort"
            adapter = AbortAdapter()
            journal, engine = self._prepare_failed_journal(directory, operation_id, adapter)

            with self.assertRaises(SystemExit):
                engine.rollback(lambda _step, _state: {})

            persisted = json.loads(journal.read_text(encoding="utf-8"))
            self.assertEqual("failed", persisted["status"])
            self.assertEqual("rollback", persisted["records"][-1]["phase"])
            self.assertEqual("started", persisted["records"][-1]["outcome"])
            self.assertEqual(operation_id, persisted["records"][-1]["operation_id"])

    def test_rollback_handler_abort_preserves_started_marker_after_restore(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            operation_id = "op-rollback-handler-abort"
            journal, engine = self._prepare_failed_journal(directory, operation_id, FakeAdapter())

            def abort(_step: str, _state: object) -> dict[str, object]:
                raise SystemExit("process aborted in rollback handler")

            with self.assertRaises(SystemExit):
                engine.rollback(abort)

            persisted = json.loads(journal.read_text(encoding="utf-8"))
            self.assertEqual("failed", persisted["status"])
            self.assertEqual("rollback", persisted["records"][-1]["phase"])
            self.assertEqual("started", persisted["records"][-1]["outcome"])
            self.assertEqual(operation_id, persisted["records"][-1]["operation_id"])

    def test_sigkill_after_durable_releasing_recovers_without_second_restore(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            operation_id = "op-sigkill"
            root = Path(directory)
            journal, _ = self._prepare_failed_journal(directory, operation_id, FakeAdapter())
            marker = root / "restore.marker"
            authority = root / "authority.sqlite"
            authority.touch()
            control_path = root / "control.sqlite"
            rollback_context = make_context(operation_id, target="rollback")
            store = SQLiteRollbackControlStore(
                control_path, cast(str, rollback_context["project_id"]), authority
            )
            control_record = {**rollback_context, "status": "held", "revision": 1}
            store.cas(0, control_record)

            class DurableDelegate(FakeAdapter):
                def snapshot(self, phase: str, context: object) -> dict[str, object]:
                    if phase == "rollback":
                        return {**rollback_context, "rollback_context_verified": True}
                    return super().snapshot(phase, context)

                def execute(self, phase: str, context: object) -> dict[str, object]:
                    if phase == "rollback":
                        descriptor = os.open(marker, os.O_WRONLY | os.O_CREAT | os.O_APPEND, 0o600)
                        try:
                            os.write(descriptor, b"restore\n")
                            os.fsync(descriptor)
                        finally:
                            os.close(descriptor)
                    return super().execute(phase, context)

            class KillAfterBeginAdapter(SQLiteControlStoreAdapter):
                def begin_release_rollback_context(
                    self, context: Mapping[str, object]
                ) -> Mapping[str, object]:
                    super().begin_release_rollback_context(context)
                    os.kill(os.getpid(), signal.SIGKILL)
                    raise AssertionError("SIGKILL returned")

            child = os.fork()
            if child == 0:  # pragma: no branch - child is terminated by SIGKILL
                try:
                    child_store = SQLiteRollbackControlStore(
                        control_path, cast(str, rollback_context["project_id"]), authority
                    )
                    child_adapter = KillAfterBeginAdapter(
                        DurableDelegate(), child_store, StaticAuthorityRuntimeRereader()
                    )
                    UpgradeEngine(
                        operation_id,
                        journal,
                        make_context(operation_id),
                        backend_adapter=child_adapter,
                    ).rollback(lambda _step, _state: {})
                except BaseException:
                    os._exit(91)
                os._exit(92)
            waited, status = os.waitpid(child, 0)
            self.assertEqual(child, waited)
            self.assertTrue(os.WIFSIGNALED(status))
            self.assertEqual(signal.SIGKILL, os.WTERMSIG(status))
            self.assertEqual(
                "rollback_verified", json.loads(journal.read_text())["records"][-1]["outcome"]
            )
            self.assertEqual(["restore"], marker.read_text().splitlines())

            recovery_store = SQLiteRollbackControlStore(
                control_path, cast(str, rollback_context["project_id"]), authority
            )
            recovery_adapter = bind_control_store(
                "sqlite",
                DurableDelegate(),
                recovery_store,
                StaticAuthorityRuntimeRereader(),
            )
            recovered = UpgradeEngine(
                operation_id,
                journal,
                make_context(operation_id),
                backend_adapter=recovery_adapter,
            ).rollback(lambda _step, _state: self.fail("restore handler was repeated"))
            self.assertEqual("rolled-back", recovered["status"])
            self.assertEqual("released", recovery_store.snapshot(operation_id)["status"])
            self.assertEqual(["restore"], marker.read_text().splitlines())

    def test_rollback_requires_adapter_verified_context_and_cannot_forge_evidence(self) -> None:
        class UnverifiedAdapter(FakeAdapter):
            def snapshot(self, phase: str, context: object) -> dict[str, object]:
                result = super().snapshot(phase, context)
                if phase == "rollback":
                    result["rollback_context_verified"] = False
                return result

        with tempfile.TemporaryDirectory() as directory:
            journal = Path(directory) / "journal.json"
            engine = UpgradeEngine(
                "op-unverified",
                journal,
                make_context("op-unverified"),
                backend_adapter=UnverifiedAdapter(),
            )
            engine.plan()
            with self.assertRaises(UpgradeError):
                engine.rollback(lambda _step, _state: {})
            self.assertEqual([], json.loads(journal.read_text())["records"])

    def test_rollback_rejects_unbound_adapter_context_before_journal(self) -> None:
        class MismatchedAdapter(FakeAdapter):
            def snapshot(self, phase: str, context: object) -> dict[str, object]:
                result = super().snapshot(phase, context)
                if phase == "rollback":
                    result["authority_revision"] = "different-authority"
                    result["barrier_identity_digest"] = canonical_barrier_digest(result)
                    result["envelope_digest"] = canonical_envelope_digest(result)
                return result

        with tempfile.TemporaryDirectory() as directory:
            journal = Path(directory) / "journal.json"
            engine = UpgradeEngine(
                "op-mismatched",
                journal,
                make_context("op-mismatched"),
                backend_adapter=MismatchedAdapter(),
            )
            engine.plan()
            with self.assertRaises(UpgradeError):
                engine.rollback(lambda _step, _state: {})
            self.assertEqual([], json.loads(journal.read_text())["records"])

    def test_rollback_handler_cannot_override_adapter_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            journal = Path(directory) / "journal.json"
            engine = UpgradeEngine(
                "op-handler-evidence",
                journal,
                make_context("op-handler-evidence"),
                backend_adapter=FakeAdapter(),
            )
            engine.plan()
            value = json.loads(journal.read_text())
            value["status"] = "failed"
            value["phase"] = "discover"
            value["records"] = [
                {
                    "operation_id": "op-handler-evidence",
                    "step_id": "op-handler-evidence.discover",
                    "phase": "discover",
                    "outcome": "failed",
                    "error": "failed",
                    "context": make_context("op-handler-evidence"),
                }
            ]
            journal.write_text(json.dumps(value))

            def forge(_step: str, _state: Mapping[str, object]) -> dict[str, object]:
                return {"restored_verified": False}

            with self.assertRaises(UpgradeError):
                engine.rollback(forge)
            self.assertEqual("safe-mode", engine._load()["status"])

    def test_rollback_uses_durable_sqlite_control_record(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            operation_id = "op-control-store"
            authority = Path(directory) / "authority.sqlite"
            authority.touch()
            control = SQLiteRollbackControlStore(
                Path(directory) / "control.sqlite",
                cast(str, CONTEXT["project_id"]),
                authority,
            )
            control_record = {
                **ROLLBACK_CONTEXT,
                "operation_id": operation_id,
                "status": "held",
                "revision": 1,
            }
            control_record["barrier_identity_digest"] = canonical_barrier_digest(control_record)
            control_record["envelope_digest"] = canonical_envelope_digest(control_record)
            control.cas(0, control_record)

            lock_observations: list[bool] = []

            class ControlDelegate(FakeAdapter):
                def snapshot(self, phase: str, context: object) -> dict[str, object]:
                    lock_observations.append(control.operation_owned_by_current_thread)
                    if phase == "rollback":
                        return {**control_record, "rollback_context_verified": True}
                    return super().snapshot(phase, context)

                def execute(self, phase: str, context: object) -> dict[str, object]:
                    lock_observations.append(control.operation_owned_by_current_thread)
                    return super().execute(phase, context)

            adapter = bind_control_store(
                "sqlite", ControlDelegate(), control, StaticAuthorityRuntimeRereader()
            )

            journal = Path(directory) / "journal.json"
            engine = UpgradeEngine(
                operation_id,
                journal,
                make_context(operation_id),
                backend_adapter=adapter,
            )
            engine.plan()
            value = json.loads(journal.read_text())
            value["status"] = "failed"
            value["phase"] = "discover"
            value["records"] = [
                {
                    "operation_id": operation_id,
                    "step_id": f"{operation_id}.discover",
                    "phase": "discover",
                    "outcome": "failed",
                    "error": "failed",
                    "context": make_context(operation_id),
                }
            ]
            journal.write_text(json.dumps(value))
            result = engine.rollback(lambda _step, _state: {})
            self.assertEqual("rolled-back", result["status"])
            self.assertEqual("released", control.snapshot(operation_id)["status"])
            self.assertTrue(lock_observations)
            self.assertTrue(all(lock_observations))
            reloaded = UpgradeEngine(
                operation_id,
                journal,
                make_context(operation_id),
                backend_adapter=adapter,
            )
            self.assertEqual("rolled-back", reloaded._load()["status"])

    def test_apply_adapter_fault_boundaries_are_durable_and_fail_closed(self) -> None:  # noqa: C901
        class CompleteAdapter(FakeAdapter):
            def __init__(self, fault: str) -> None:
                super().__init__()
                self.fault = fault

            def snapshot(self, phase: str, context: object) -> dict[str, object]:
                result = super().snapshot(phase, context)
                if self.fault == f"{phase}-snapshot-shape":
                    key = {
                        "preflight": "preflight_snapshot",
                        "quiesce": "quiescence_snapshot",
                        "commit": "admitted_snapshot",
                        "reopen": "reopen_snapshot",
                    }[phase]
                    result[key] = []
                if self.fault == "snapshot-identity" and phase == "discover":
                    result["authority_revision"] = "changed"
                return result

            def execute(self, phase: str, _context: object) -> dict[str, object]:  # noqa: C901
                result: dict[str, object] = {
                    "backend": "sqlite",
                    "fencing_token": "fence-1",
                    "backend_identity_verified": True,
                    "mutates_authority": phase == "commit",
                }
                if phase == "discover":
                    result.update(release_authentic=True, runtime_supported=True)
                elif phase == "preflight":
                    result.update(
                        preflight_admitted=True,
                        capacity_verified=True,
                        preflight_snapshot=ADMISSION,
                    )
                elif phase == "quiesce":
                    result.update(
                        barrier_acquired=True,
                        workers_drained=True,
                        leases_fenced=True,
                        fencing_verified=True,
                        quiescence_snapshot=ADMISSION,
                    )
                elif phase == "backup":
                    result.update(backup_verified=True, restore_roundtrip_verified=True)
                elif phase == "stage":
                    result.update(staged_verified=True, manifest_verified=True)
                elif phase == "commit":
                    result.update(
                        quiesced=True,
                        backup_verified=True,
                        selector_verified=True,
                        selector_commit_atomic=True,
                        fencing_verified=True,
                        selector_before_verified=True,
                        selector_after_verified=True,
                        admitted_snapshot=ADMISSION,
                        current_snapshot=ADMISSION,
                    )
                elif phase == "validate":
                    result.update(
                        runtime_validated=True,
                        backend_roundtrip_valid=True,
                        projections_valid=True,
                        binding_valid=True,
                    )
                elif phase == "reopen":
                    result.update(
                        validated=True,
                        barrier_held=True,
                        reopen_snapshot=ADMISSION,
                    )
                if self.fault == f"{phase}-result-shape":
                    key = {
                        "preflight": "preflight_snapshot",
                        "quiesce": "quiescence_snapshot",
                        "commit": "current_snapshot",
                        "reopen": "reopen_snapshot",
                    }[phase]
                    result[key] = []
                if self.fault == "missing-evidence" and phase == "discover":
                    result.pop("release_authentic")
                if self.fault == "backend-mismatch" and phase == "discover":
                    result["backend"] = "git"
                if self.fault == "stale-fence" and phase == "quiesce":
                    result["fencing_token"] = f"{result['fencing_token']}-stale"
                if self.fault == "ambiguous" and phase == "discover":
                    result["ambiguous"] = True
                return result

        cases = (
            ("snapshot-identity", "discover", "phase failed"),
            ("missing-evidence", "discover", "phase evidence incomplete"),
            ("backend-mismatch", "discover", "phase backend mismatch"),
            ("stale-fence", "quiesce", "phase fencing mismatch"),
            ("ambiguous", "discover", "phase outcome is ambiguous"),
            ("preflight-snapshot-shape", "preflight", "phase failed"),
            ("quiesce-snapshot-shape", "quiesce", "phase failed"),
            ("commit-snapshot-shape", "commit", "phase failed"),
            ("reopen-snapshot-shape", "reopen", "phase failed"),
            ("preflight-result-shape", "preflight", "phase admission denied"),
            ("quiesce-result-shape", "quiesce", "phase admission denied"),
            ("commit-result-shape", "commit", "phase admission denied"),
            ("reopen-result-shape", "reopen", "phase admission denied"),
        )
        for fault, failed_phase, expected in cases:
            with self.subTest(fault=fault), tempfile.TemporaryDirectory() as directory:
                engine = UpgradeEngine(
                    f"op-{fault}",
                    Path(directory) / "journal.json",
                    make_context(f"op-{fault}"),
                    backend_adapter=CompleteAdapter(fault),
                )
                engine.plan()
                with self.assertRaisesRegex(UpgradeError, expected):
                    engine.apply(dict.fromkeys(PHASES, lambda _step, _state: {}))
                durable = json.loads(engine.journal.read_text())
                self.assertEqual(failed_phase, durable["phase"])
                self.assertEqual(
                    "safe-mode" if fault == "ambiguous" else "failed",
                    durable["status"],
                )

        with tempfile.TemporaryDirectory() as directory:
            operation_id = "op-handler-conflict"
            engine = UpgradeEngine(
                operation_id,
                Path(directory) / "journal.json",
                make_context(operation_id),
                backend_adapter=CompleteAdapter("handler-conflict"),
            )
            engine.plan()

            def conflict(_step: str, _state: object) -> dict[str, object]:
                return {"backend": "git"}

            with self.assertRaisesRegex(UpgradeError, "phase failed"):
                engine.apply(
                    {**dict.fromkeys(PHASES, lambda _step, _state: {}), "discover": conflict}
                )
            self.assertEqual("failed", json.loads(engine.journal.read_text())["status"])

    def test_public_operation_guards_reject_invalid_and_unbound_operations(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for operation_id in ("", "contains:separator"):
                with self.subTest(operation_id=operation_id), self.assertRaises(UpgradeError):
                    UpgradeEngine(operation_id, root / "invalid.json", CONTEXT)

            long_operation = "o" * 120
            with self.assertRaisesRegex(UpgradeError, "invalid operation_id"):
                UpgradeEngine(
                    long_operation,
                    root / "long.json",
                    make_context(long_operation),
                )

            operation_id = "op-unbound"
            engine = UpgradeEngine(operation_id, root / "journal.json", make_context(operation_id))
            self.assertEqual(
                {"operation_id": operation_id, "phases": list(PHASES), "checked": True},
                engine.check(),
            )
            engine.plan()
            with self.assertRaisesRegex(UpgradeError, "backend adapter is required"):
                engine.apply({})
            with self.assertRaisesRegex(UpgradeError, "backend adapter is required"):
                engine.rollback(lambda _step, _state: {})

            missing_handler = UpgradeEngine(
                "op-missing-handler",
                root / "missing-handler.json",
                make_context("op-missing-handler"),
                backend_adapter=FakeAdapter(),
            )
            missing_handler.plan()
            with self.assertRaisesRegex(UpgradeError, "missing phase handler: discover"):
                missing_handler.apply({})

    def test_rollback_authority_and_release_faults_preserve_recovery_state(self) -> None:  # noqa: C901
        class FaultAdapter(FakeAdapter):
            def __init__(self, fault: str) -> None:
                super().__init__()
                self.fault = fault
                self.verifications = 0

            def snapshot(self, phase: str, context: object) -> dict[str, object]:
                if self.fault == "new-target" and phase == "rollback":
                    operation_id = str(cast(Mapping[str, object], context)["operation_id"])
                    return {
                        **make_context(operation_id),
                        "rollback_context_verified": True,
                    }
                return super().snapshot(phase, context)

            def verify_rollback_context(
                self, context: Mapping[str, object]
            ) -> dict[str, object] | None:
                self.verifications += 1
                if self.fault == "verify-raises":
                    raise RuntimeError("authority unavailable")
                if self.fault == "verify-missing":
                    return None
                durable = super().verify_rollback_context(context)
                if durable is not None and self.verifications >= 2:
                    if self.fault == "identity-changed":
                        durable["authority_revision"] = "changed"
                    if self.fault == "barrier-state":
                        durable["status"] = "ambiguous"
                return durable

            def execute(self, phase: str, context: object) -> dict[str, object]:
                if phase == "rollback" and self.fault == "pre-effect-rejected":
                    raise AuthorityMutationRejectedError("rollback admission rejected")
                result = super().execute(phase, context)
                if phase == "rollback" and self.fault == "runtime-unverified":
                    result["runtime_validated"] = False
                if phase == "rollback" and self.fault == "result-incomplete":
                    result.pop("backend")
                return result

            def begin_release_rollback_context(
                self, context: Mapping[str, object]
            ) -> dict[str, object]:
                result = super().begin_release_rollback_context(context)
                if self.fault == "begin-not-durable":
                    return {"status": "held"}
                return result

            def complete_release_rollback_context(
                self, context: Mapping[str, object]
            ) -> dict[str, object]:
                result = super().complete_release_rollback_context(context)
                if self.fault == "complete-not-durable":
                    return {"status": "releasing"}
                return result

            def revalidate_rollback(
                self, context: Mapping[str, object], result: Mapping[str, object]
            ) -> dict[str, object]:
                if self.fault == "revalidation-invalid":
                    return cast(dict[str, object], None)
                evidence = super().revalidate_rollback(context, result)
                if self.fault == "revalidation-changed":
                    evidence["runtime_validated"] = False
                return evidence

        cases = (
            ("new-target", "failed", None),
            ("verify-raises", "failed", None),
            ("verify-missing", "failed", None),
            ("runtime-unverified", "safe-mode", "ambiguous"),
            ("pre-effect-rejected", "failed", "failed"),
            ("result-incomplete", "safe-mode", "ambiguous"),
            ("handler-conflict", "safe-mode", "ambiguous"),
            ("handler-evidence", "safe-mode", "ambiguous"),
            ("identity-changed", "failed", "rollback_verified"),
            ("barrier-state", "failed", "rollback_verified"),
            ("begin-not-durable", "failed", "rollback_verified"),
            ("complete-not-durable", "failed", "rollback_verified"),
            ("revalidation-invalid", "failed", "rollback_verified"),
            ("revalidation-changed", "failed", "rollback_verified"),
        )
        for fault, expected_status, expected_outcome in cases:
            with self.subTest(fault=fault), tempfile.TemporaryDirectory() as directory:
                adapter = FaultAdapter(fault)
                journal, engine = self._prepare_failed_journal(directory, f"op-{fault}", adapter)

                def handler(
                    _step: str, _state: object, current_fault: str = fault
                ) -> dict[str, object]:
                    if current_fault == "handler-conflict":
                        return {"backend": "git"}
                    if current_fault == "handler-evidence":
                        return {"restored_verified": True}
                    return {}

                with self.assertRaises(UpgradeError):
                    engine.rollback(handler)
                durable = json.loads(journal.read_text())
                self.assertEqual(expected_status, durable["status"])
                rollback_records = [
                    record for record in durable["records"] if record["phase"] == "rollback"
                ]
                if expected_outcome is None:
                    self.assertEqual([], rollback_records)
                else:
                    self.assertEqual(expected_outcome, rollback_records[-1]["outcome"])

    def test_missing_release_api_keeps_verified_rollback_durable(self) -> None:
        class RestoreOnlyAdapter:
            def snapshot(self, phase: str, context: Mapping[str, object]) -> dict[str, object]:
                if phase == "rollback":
                    return {
                        **make_context(str(context["operation_id"]), target="rollback"),
                        "rollback_context_verified": True,
                    }
                return {**ADMISSION, **context}

            def verify_rollback_context(self, context: Mapping[str, object]) -> dict[str, object]:
                return {**context, "status": "held"}

            def execute(self, phase: str, _context: Mapping[str, object]) -> dict[str, object]:
                if phase != "rollback":
                    return {}
                return {
                    "restored_verified": True,
                    "runtime_validated": True,
                    "backend_roundtrip_valid": True,
                    "backend": "sqlite",
                    "fencing_token": "fence-1",
                }

        with tempfile.TemporaryDirectory() as directory:
            journal, engine = self._prepare_failed_journal(
                directory,
                "op-missing-release",
                RestoreOnlyAdapter(),
            )
            with self.assertRaisesRegex(UpgradeError, "release recovery API is unavailable"):
                engine.rollback(lambda _step, _state: {})
            durable = json.loads(journal.read_text())
            self.assertEqual("failed", durable["status"])
            self.assertEqual("rollback_verified", durable["records"][-1]["outcome"])

    def test_durable_journal_write_and_lock_faults_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            operation_id = "op-write-fault"

            with patch("tools.upgrade_engine.os.fsync", side_effect=OSError("fsync failed")):
                engine = UpgradeEngine(
                    operation_id,
                    root / "write.json",
                    make_context(operation_id),
                    backend_adapter=FakeAdapter(),
                )
                with self.assertRaisesRegex(UpgradeError, "journal write failed"):
                    engine.plan()
                self.assertFalse(engine.journal.exists())

            with (
                patch("tools.upgrade_engine.os.fsync", side_effect=OSError("fsync failed")),
                patch.object(Path, "unlink", side_effect=OSError("cleanup failed")),
            ):
                engine = UpgradeEngine(
                    operation_id,
                    root / "cleanup.json",
                    make_context(operation_id),
                    backend_adapter=FakeAdapter(),
                )
                with self.assertRaisesRegex(UpgradeError, "journal cleanup failed"):
                    engine.plan()

            with patch("tools.upgrade_engine.fcntl", None):
                engine = UpgradeEngine(
                    operation_id,
                    root / "unavailable.json",
                    make_context(operation_id),
                    backend_adapter=FakeAdapter(),
                )
                with self.assertRaisesRegex(UpgradeError, "lock is unavailable"):
                    engine.plan()

            lock_path = root / "contended.lock"
            lock_path.touch()
            with lock_path.open("a+") as stream:
                fcntl.flock(stream.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
                engine = UpgradeEngine(
                    operation_id,
                    root / "timeout.json",
                    make_context(operation_id),
                    lock_path=lock_path,
                    backend_adapter=FakeAdapter(),
                )
                with (
                    patch(
                        "tools.upgrade_engine.time.monotonic",
                        side_effect=(0.0, 1.0, 31.0),
                    ),
                    patch("tools.upgrade_engine.time.sleep") as sleep,
                    self.assertRaisesRegex(UpgradeError, "lock acquisition timed out"),
                ):
                    engine.plan()
                sleep.assert_called_once_with(0.01)
                fcntl.flock(stream.fileno(), fcntl.LOCK_UN)

            engine = UpgradeEngine(
                operation_id,
                root / "lock-error.json",
                make_context(operation_id),
                backend_adapter=FakeAdapter(),
            )
            with (
                patch("tools.upgrade_engine.fcntl.flock", side_effect=OSError("lock failed")),
                self.assertRaisesRegex(UpgradeError, "lock acquisition failed"),
            ):
                engine.plan()

    def test_loaded_rollback_requires_authority_and_runtime_revalidation(self) -> None:
        class MissingAuthority(FakeAdapter):
            def verify_rollback_context(
                self, _context: Mapping[str, object]
            ) -> dict[str, object] | None:
                return None

        class RaisingAuthority(FakeAdapter):
            def verify_rollback_context(
                self, _context: Mapping[str, object]
            ) -> dict[str, object] | None:
                raise RuntimeError("authority unavailable")

        class RaisingRuntime(FakeAdapter):
            def revalidate_rollback(
                self, _context: Mapping[str, object], _result: Mapping[str, object]
            ) -> dict[str, object]:
                raise RuntimeError("runtime unavailable")

        class ChangedRuntime(FakeAdapter):
            def revalidate_rollback(
                self, context: Mapping[str, object], result: Mapping[str, object]
            ) -> dict[str, object]:
                evidence = super().revalidate_rollback(context, result)
                evidence["runtime_validated"] = False
                return evidence

        class RestoreOnlyAdapter:
            def snapshot(self, _phase: str, _context: Mapping[str, object]) -> dict[str, object]:
                return {}

            def verify_rollback_context(self, context: Mapping[str, object]) -> dict[str, object]:
                return dict(context)

            def execute(self, _phase: str, _context: Mapping[str, object]) -> dict[str, object]:
                return {}

        with tempfile.TemporaryDirectory() as directory:
            operation_id = "op-reload-rollback"
            journal, engine = self._prepare_failed_journal(directory, operation_id, FakeAdapter())
            completed = engine.rollback(lambda _step, _state: {})
            self.assertEqual("rolled-back", completed["status"])
            durable = journal.read_text()
            cases: tuple[tuple[str, BackendAdapter, str], ...] = (
                ("authority missing", MissingAuthority(), "not verified by authority"),
                ("authority raises", RaisingAuthority(), "authority verification failed"),
                (
                    "runtime API missing",
                    RestoreOnlyAdapter(),
                    "rollback revalidation is unavailable",
                ),
                ("runtime raises", RaisingRuntime(), "rollback revalidation failed"),
                ("runtime changed", ChangedRuntime(), "runtime is not revalidated"),
            )
            for name, adapter, expected in cases:
                journal.write_text(durable)
                reloaded = UpgradeEngine(
                    operation_id,
                    journal,
                    make_context(operation_id),
                    backend_adapter=adapter,
                )
                with self.subTest(name=name), self.assertRaisesRegex(UpgradeError, expected):
                    reloaded.apply({})

    def test_apply_rejects_failed_state_and_unreconciled_rollback_record(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            journal, failed = self._prepare_failed_journal(
                directory, "op-explicit-recovery", FakeAdapter()
            )
            with self.assertRaisesRegex(UpgradeError, "requires explicit recovery"):
                failed.apply({})

            value = json.loads(journal.read_text())
            value["records"].append(
                {
                    "operation_id": "op-explicit-recovery",
                    "step_id": "op-explicit-recovery.rollback",
                    "phase": "rollback",
                    "outcome": "started",
                    "context": make_context("op-explicit-recovery", target="rollback"),
                }
            )
            journal.write_text(json.dumps(value))
            with self.assertRaisesRegex(UpgradeError, "requires explicit reconciliation"):
                failed.rollback(lambda _step, _state: {})

    def test_apply_resumes_after_a_durable_success_without_repeating_it(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            operation_id = "op-resume-success"
            journal = Path(directory) / "journal.json"
            engine = UpgradeEngine(
                operation_id,
                journal,
                make_context(operation_id),
                backend_adapter=FakeAdapter(),
            )
            value = engine.plan()
            value.update(
                status="running",
                phase="discover",
                records=[
                    {
                        "operation_id": operation_id,
                        "step_id": f"{operation_id}.discover",
                        "phase": "discover",
                        "outcome": "success",
                        "context": make_context(operation_id),
                        "result": {"durably_completed": True},
                    }
                ],
            )
            journal.write_text(json.dumps(value))
            called: list[str] = []

            def preflight(step_id: str, _state: object) -> dict[str, object]:
                called.append(step_id)
                return {}

            with self.assertRaisesRegex(UpgradeError, "phase evidence incomplete: preflight"):
                engine.apply({"preflight": preflight})
            self.assertEqual([f"{operation_id}.preflight"], called)
            durable = json.loads(journal.read_text())
            self.assertEqual(
                ["discover", "preflight"], [item["phase"] for item in durable["records"]]
            )

    def test_started_phase_requires_explicit_recovery(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            journal = Path(directory) / "journal.json"
            engine = UpgradeEngine(
                "op-5", journal, make_context("op-5"), backend_adapter=FakeAdapter()
            )
            engine.plan()
            value = json.loads(journal.read_text())
            value["status"] = "running"
            value["phase"] = "discover"
            value["records"] = [
                {
                    "operation_id": "op-5",
                    "step_id": "op-5.discover",
                    "phase": "discover",
                    "outcome": "started",
                    "context": make_context("op-5"),
                }
            ]
            journal.write_text(json.dumps(value))
            with self.assertRaises(UpgradeError):
                engine.apply({})

    def test_apply_handler_abort_preserves_started_marker_after_backend_effect(self) -> None:
        with tempfile.TemporaryDirectory() as directory:

            class EvidenceAdapter(FakeAdapter):
                def execute(self, phase: str, context: object) -> dict[str, object]:
                    result = super().execute(phase, context)
                    if phase == "discover":
                        result.update(
                            backend="sqlite",
                            fencing_token=cast(str, CONTEXT["fencing_token"]),
                            backend_identity_verified=True,
                            release_authentic=True,
                            runtime_supported=True,
                            mutates_authority=False,
                        )
                    return result

            operation_id = "op-handler-abort"
            journal = Path(directory) / "journal.json"
            engine = UpgradeEngine(
                operation_id,
                journal,
                make_context(operation_id),
                backend_adapter=EvidenceAdapter(),
            )
            engine.plan()

            def abort(_operation: str, _state: object) -> dict[str, object]:
                raise SystemExit("process aborted in handler")

            handlers: dict[str, Handler] = {
                phase: (abort if phase == "discover" else lambda _operation, _state: {})
                for phase in PHASES
            }
            with self.assertRaises(SystemExit):
                engine.apply(handlers)

            persisted = json.loads(journal.read_text(encoding="utf-8"))
            self.assertEqual("running", persisted["status"])
            self.assertEqual("discover", persisted["phase"])
            self.assertEqual("started", persisted["records"][-1]["outcome"])
            self.assertEqual(operation_id, persisted["records"][-1]["operation_id"])

    def test_authority_probe_failure_precedes_handler(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            engine = UpgradeEngine(
                "op-probe",
                Path(directory) / "journal.json",
                make_context("op-probe"),
                backend_adapter=FailingAdapter(),
            )
            engine.plan()
            called = False

            def handler(_operation: str, _state: object) -> dict[str, object]:
                nonlocal called
                called = True
                return {"mutates_authority": False}

            with self.assertRaises(UpgradeError):
                engine.apply(dict.fromkeys(PHASES, handler))
            self.assertFalse(called)

    def test_concrete_rollback_requires_bound_capability_before_backend(self) -> None:
        class ConcreteAdapter(FakeAdapter):
            requires_bound_rollback = True

            def verify_rollback_context_bound(
                self, context: Mapping[str, object]
            ) -> Mapping[str, object]:
                return dict(context)

            def snapshot(self, _phase: str, _context: object) -> dict[str, object]:
                raise AssertionError("unbound rollback snapshot reached")

        with tempfile.TemporaryDirectory() as directory:
            engine = UpgradeEngine(
                "op-bound-gate",
                Path(directory) / "journal.json",
                make_context("op-bound-gate"),
                backend_adapter=ConcreteAdapter(),
            )
            engine.plan()
            journal_before = (Path(directory) / "journal.json").read_bytes()
            with self.assertRaisesRegex(UpgradeError, "trusted bound backend capability"):
                engine.rollback(lambda _step, _state: self.fail("rollback handler reached"))
            self.assertEqual(journal_before, (Path(directory) / "journal.json").read_bytes())

    def test_initialized_git_and_sqlite_adapters_fail_closed_without_bound_scope(self) -> None:
        """Real adapters cannot fall back to an unscoped engine rollback reread."""
        for backend, adapter_type in (
            ("git", GitAuthorityAdapter),
            ("sqlite", SQLiteAuthorityAdapter),
        ):
            with tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                if backend == "git":
                    adapter = adapter_type(root)
                else:
                    authority = root / "authority.sqlite"
                    authority.write_bytes(b"authority")
                    authority.chmod(0o600)
                    adapter = adapter_type(authority)
                context = make_context(f"op-real-{backend}")
                context["backend"] = backend
                context["barrier_identity_digest"] = canonical_barrier_digest(context)
                context["envelope_digest"] = canonical_envelope_digest(context)
                engine = UpgradeEngine(
                    str(context["operation_id"]),
                    root / "journal.json",
                    context,
                    backend_adapter=adapter,
                )
                engine.plan()
                journal_before = (root / "journal.json").read_bytes()
                with (
                    patch.object(
                        adapter, "snapshot", side_effect=AssertionError("snapshot reached")
                    ) as snapshot,
                    patch.object(
                        adapter, "execute", side_effect=AssertionError("execute reached")
                    ) as execute,
                    self.assertRaisesRegex(UpgradeError, "trusted bound backend capability"),
                ):
                    engine.rollback(lambda _step, _state: self.fail("rollback handler reached"))
                snapshot.assert_not_called()
                execute.assert_not_called()
                self.assertEqual(journal_before, (root / "journal.json").read_bytes())
                with engine._exclusive():
                    pass

    def test_concrete_rollback_uses_bound_capability_but_stays_non_authorizing(self) -> None:
        class ConcreteAdapter(FakeAdapter):
            requires_bound_rollback = True

            def verify_rollback_context_bound(
                self, context: Mapping[str, object]
            ) -> Mapping[str, object]:
                return dict(context)

            def snapshot(self, _phase: str, _context: object) -> dict[str, object]:
                raise AssertionError("unbound rollback snapshot reached")

            def execute(self, _phase: str, _context: object) -> dict[str, object]:
                raise AssertionError("rollback execute reached")

        with tempfile.TemporaryDirectory() as directory:
            context = make_context("op-bound-evidence")
            adapter = ConcreteAdapter()
            engine = UpgradeEngine(
                "op-bound-evidence",
                Path(directory) / "journal.json",
                context,
                backend_adapter=adapter,
                rollback_bound_verifier=BoundRollbackCapability.bind(
                    PhaseContext(**cast(dict[str, Any], context)), adapter
                ),
            )
            engine.plan()
            journal_before = (Path(directory) / "journal.json").read_bytes()
            with self.assertRaisesRegex(UpgradeError, "did not verify rollback context"):
                engine.rollback(lambda _step, _state: self.fail("rollback handler reached"))
            self.assertEqual(journal_before, (Path(directory) / "journal.json").read_bytes())

    def test_bound_rollback_inspection_returns_evidence_without_journal_or_mutation(self) -> None:
        class ConcreteAdapter(FakeAdapter):
            requires_bound_rollback = True

            def verify_rollback_context_bound(
                self, context: Mapping[str, object]
            ) -> Mapping[str, object]:
                return {
                    **context,
                    "phase": "rollback",
                    "backend_identity_verified": True,
                    "mutates_authority": False,
                    "rollback_context_verified": False,
                }

            def snapshot(self, _phase: str, _context: object) -> dict[str, object]:
                raise AssertionError("unbound snapshot reached")

            def execute(self, _phase: str, _context: object) -> dict[str, object]:
                raise AssertionError("mutation reached")

        with tempfile.TemporaryDirectory() as directory:
            operation_id = "op-bound-inspection"
            journal = Path(directory) / "journal.json"
            adapter = ConcreteAdapter()
            engine = UpgradeEngine(
                operation_id,
                journal,
                make_context(operation_id),
                backend_adapter=adapter,
                rollback_bound_verifier=BoundRollbackCapability.bind(
                    PhaseContext(**cast(dict[str, Any], make_context(operation_id))), adapter
                ),
            )
            engine.plan()
            journal_before = journal.read_bytes()
            evidence = engine.inspect_rollback_bound()
            self.assertFalse(evidence["rollback_context_verified"])
            self.assertEqual(journal_before, journal.read_bytes())
            with engine._exclusive():
                pass

    def test_bound_rollback_inspection_rejects_without_backend(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            context = make_context("op-no-backend")
            engine = UpgradeEngine("op-no-backend", Path(directory) / "journal.json", context)
            with self.assertRaisesRegex(UpgradeError, "required for rollback inspection"):
                engine.inspect_rollback_bound()

    def test_bound_rollback_inspection_rejects_unbound_backend(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            context = make_context("op-unbound")
            engine = UpgradeEngine(
                "op-unbound",
                Path(directory) / "journal.json",
                context,
                backend_adapter=FakeAdapter(),
            )
            with self.assertRaisesRegex(UpgradeError, "requires a bound backend"):
                engine.inspect_rollback_bound()

    def test_bound_rollback_inspection_rejects_missing_capability(self) -> None:
        class ConcreteAdapter(FakeAdapter):
            requires_bound_rollback = True

        with tempfile.TemporaryDirectory() as directory:
            context = make_context("op-no-capability")
            engine = UpgradeEngine(
                "op-no-capability",
                Path(directory) / "journal.json",
                context,
                backend_adapter=ConcreteAdapter(),
            )
            with self.assertRaisesRegex(UpgradeError, "requires a trusted bound capability"):
                engine.inspect_rollback_bound()

    def test_bound_rollback_inspection_rejects_verifier_failure_or_authorization(self) -> None:
        class FailingAdapter(FakeAdapter):
            requires_bound_rollback = True

            def verify_rollback_context_bound(
                self, context: Mapping[str, object]
            ) -> Mapping[str, object]:
                return context

        with tempfile.TemporaryDirectory() as directory:
            context = make_context("op-inspection-failure")
            adapter = FailingAdapter()
            engine = UpgradeEngine(
                str(context["operation_id"]),
                Path(directory) / "journal.json",
                context,
                backend_adapter=adapter,
                rollback_bound_verifier=BoundRollbackCapability.bind(
                    PhaseContext(**cast(dict[str, Any], context)), adapter
                ),
            )
            engine.plan()
            capability = engine.rollback_bound_verifier
            assert capability is not None
            with (
                patch.object(
                    capability.verifier,
                    "verify_rollback_context_bound",
                    side_effect=RuntimeError("reread failed"),
                ),
                self.assertRaisesRegex(UpgradeError, "trusted bound rollback inspection failed"),
            ):
                engine.inspect_rollback_bound()

        class AuthorizingCapability(BoundRollbackCapability):
            def verify(self, _context: Mapping[str, object]) -> Mapping[str, object]:
                return {"rollback_context_verified": True}

        with tempfile.TemporaryDirectory() as directory:
            context = make_context("op-inspection-authorizing")
            adapter = FailingAdapter()
            capability = AuthorizingCapability.bind(
                PhaseContext(**cast(dict[str, Any], context)), adapter
            )
            engine = UpgradeEngine(
                str(context["operation_id"]),
                Path(directory) / "journal.json",
                context,
                backend_adapter=adapter,
                rollback_bound_verifier=capability,
            )
            engine.plan()
            with self.assertRaisesRegex(UpgradeError, "authorizing"):
                engine.inspect_rollback_bound()

    def test_bound_rollback_inspection_rejects_incomplete_or_mutating_evidence(self) -> None:
        class MalformedAdapter(FakeAdapter):
            requires_bound_rollback = True

            def __init__(self, result: Mapping[str, object]) -> None:
                super().__init__()
                self.result = result

            def verify_rollback_context_bound(
                self, context: Mapping[str, object]
            ) -> Mapping[str, object]:
                return {**context, **self.result}

        for malformed in (
            {"phase": "discover", "backend_identity_verified": True, "mutates_authority": False},
            {"phase": "rollback", "backend_identity_verified": False, "mutates_authority": False},
            {"phase": "rollback", "backend_identity_verified": True, "mutates_authority": True},
        ):
            with self.subTest(malformed=malformed), tempfile.TemporaryDirectory() as directory:
                context = make_context("op-malformed-inspection")
                adapter = MalformedAdapter(malformed)
                journal = Path(directory) / "journal.json"
                engine = UpgradeEngine(
                    str(context["operation_id"]),
                    journal,
                    context,
                    backend_adapter=adapter,
                    rollback_bound_verifier=BoundRollbackCapability.bind(
                        PhaseContext(**cast(dict[str, Any], context)), adapter
                    ),
                )
                engine.plan()
                before = journal.read_bytes()
                with self.assertRaisesRegex(UpgradeError, "incomplete or authorizing"):
                    engine.inspect_rollback_bound()
                self.assertEqual(before, journal.read_bytes())

    def test_rollback_authorization_contract_rejects_forged_or_incomplete_requests(self) -> None:
        class EvidenceAdapter(FakeAdapter):
            def verify_rollback_context_bound(
                self, context: Mapping[str, object]
            ) -> Mapping[str, object]:
                return dict(context)

        adapter = EvidenceAdapter()
        context = PhaseContext(**cast(dict[str, Any], ROLLBACK_CONTEXT))
        evidence_capability = BoundRollbackCapability.bind(context, adapter)
        capability = RollbackAuthorizationCapability.bind(context, evidence_capability)
        typed = RollbackBackupEvidence.from_observations(
            ROLLBACK_CONTEXT, b"backup-v1", {"manifest": "v1"}, "control-store-1", 1
        )
        valid_evidence = typed.as_mapping()
        with self.assertRaisesRegex(UpgradeError, "not enabled"):
            capability.authorize(ROLLBACK_CONTEXT, typed)
        with self.assertRaisesRegex(UpgradeError, "context or evidence is invalid"):
            capability.validate(None, valid_evidence)  # type: ignore[arg-type]
        with self.assertRaisesRegex(UpgradeError, "typed evidence"):
            capability.authorize(ROLLBACK_CONTEXT, valid_evidence)
        forged = dict(ROLLBACK_CONTEXT)
        forged["fencing_token"] = "forged"  # noqa: S105
        with self.assertRaisesRegex(UpgradeError, "identity mismatch"):
            capability.validate(forged, valid_evidence)
        incomplete = dict(ROLLBACK_CONTEXT)
        incomplete.pop("envelope_digest")
        with self.assertRaisesRegex(UpgradeError, "context is invalid"):
            capability.validate(incomplete, valid_evidence)
        with self.assertRaisesRegex(UpgradeError, "diagnostic-only"):
            capability.validate(
                ROLLBACK_CONTEXT, {**valid_evidence, "rollback_context_verified": True}
            )
        for hostile, message in (
            (None, "context or evidence is invalid"),
            (object(), "context or evidence is invalid"),
            (
                {key: value for key, value in valid_evidence.items() if key != "phase"},
                "schema is invalid",
            ),
            ({**valid_evidence, "unexpected": True}, "schema is invalid"),
            ({**valid_evidence, "backend": "git"}, "evidence identity mismatch"),
            ({**valid_evidence, "phase": "discover"}, "phase or backend is invalid"),
            ({**valid_evidence, "mutates_authority": True}, "evidence is mutating"),
            ({**valid_evidence, "backend_identity_verified": False}, "identity is unverified"),
            ({**valid_evidence, "backup_verified": False}, "lacks backup or restore proof"),
            (
                {**valid_evidence, "restore_roundtrip_verified": False},
                "lacks backup or restore proof",
            ),
        ):
            with self.subTest(hostile=hostile), self.assertRaisesRegex(UpgradeError, message):
                capability.validate(ROLLBACK_CONTEXT, hostile)  # type: ignore[arg-type]

        self.assertNotEqual(
            typed.backup_bytes_digest,
            RollbackBackupEvidence.from_observations(
                ROLLBACK_CONTEXT, b"backup-v2", {"manifest": "v1"}, "control-store-1", 1
            ).backup_bytes_digest,
        )
        with self.assertRaisesRegex(UpgradeError, "trusted provenance"):
            RollbackBackupEvidence(
                tuple(ROLLBACK_CONTEXT.items()),
                typed.backup_bytes_digest,
                typed.manifest_digest,
                typed.control_store_identity,
                typed.control_store_revision,
            )

    def test_rollback_authorization_preflight_requires_bound_observation_and_cas(self) -> None:
        class EvidenceAdapter(FakeAdapter):
            def verify_rollback_context_bound(
                self, context: Mapping[str, object]
            ) -> Mapping[str, object]:
                return dict(context)

        adapter = EvidenceAdapter()
        context = PhaseContext(**cast(dict[str, Any], ROLLBACK_CONTEXT))
        evidence = BoundRollbackCapability.bind(context, adapter)
        capability = RollbackAuthorizationCapability.bind(context, evidence)
        with tempfile.TemporaryDirectory() as directory:
            backup = Path(directory) / "backup"
            manifest = Path(directory) / "manifest.json"
            backup.write_bytes(b"bytes")
            manifest.write_text('{"value": "manifest"}', encoding="utf-8")
            observation = BackupObservation.from_artifacts(
                backup, manifest, control_store_identity="store:1", control_store_revision=4
            )

        class Provider:
            def observe_backup_identity(
                self, _backup: Path, _manifest: Path, _context: Mapping[str, object]
            ) -> BackupObservation:
                return observation

        with self.assertRaisesRegex(UpgradeError, "bound observation provider"):
            capability.preflight(ROLLBACK_CONTEXT, cast(Any, Provider()))
        with self.assertRaisesRegex(UpgradeError, "bound observation provider"):

            class ForgedProvider:
                def observe_backup_identity(
                    self, _backup: Path, _manifest: Path, _context: Mapping[str, object]
                ) -> BackupObservation:
                    return BackupObservation("bytes", "manifest", "store:1", 4)

            capability.preflight(ROLLBACK_CONTEXT, cast(Any, ForgedProvider()))

        class ObservingAdapter(EvidenceAdapter):
            def observe_backup_identity(
                self, _backup: Path, _manifest: Path, _context: Mapping[str, object]
            ) -> BackupObservation:
                return observation

        observing = ObservingAdapter()
        observing_evidence = BoundRollbackCapability.bind(context, observing)
        observing_capability = RollbackAuthorizationCapability.bind(context, observing_evidence)
        provider = object.__new__(SQLiteRollbackObservationCapability)
        object.__setattr__(provider, "adapter", observing)
        object.__setattr__(
            provider,
            "identity",
            tuple(ROLLBACK_CONTEXT[field] for field in CONTEXT_FIELDS if field != "target"),
        )
        with self.assertRaisesRegex(UpgradeError, "not enabled"):
            observing_capability.preflight(ROLLBACK_CONTEXT, provider)

        class UnprovenAdapter(ObservingAdapter):
            def observe_backup_identity(
                self, _backup: Path, _manifest: Path, _context: Mapping[str, object]
            ) -> BackupObservation:
                return BackupObservation("bytes", "manifest", "store:1", 4)

        unproven_adapter = UnprovenAdapter()
        unproven_evidence = BoundRollbackCapability.bind(context, unproven_adapter)
        unproven_capability = RollbackAuthorizationCapability.bind(context, unproven_evidence)
        unproven_provider = object.__new__(SQLiteRollbackObservationCapability)
        object.__setattr__(unproven_provider, "adapter", unproven_adapter)
        object.__setattr__(unproven_provider, "identity", provider.identity)
        with self.assertRaisesRegex(UpgradeError, "provenance"):
            unproven_capability.preflight(ROLLBACK_CONTEXT, unproven_provider)
        foreign_provider = object.__new__(SQLiteRollbackObservationCapability)
        object.__setattr__(foreign_provider, "adapter", object())
        object.__setattr__(foreign_provider, "identity", provider.identity)
        with self.assertRaisesRegex(UpgradeError, "foreign adapter"):
            observing_capability.preflight(ROLLBACK_CONTEXT, foreign_provider)
        with self.assertRaisesRegex(UpgradeError, "context is invalid"):
            observing_capability.preflight({**ROLLBACK_CONTEXT, "target": "new"}, provider)
        with self.assertRaisesRegex(UpgradeError, "identity mismatch"):
            observing_capability.preflight(
                {**ROLLBACK_CONTEXT, "operation_id": "foreign"}, provider
            )

        class FailingAdapter(ObservingAdapter):
            def observe_backup_identity(
                self, _backup: Path, _manifest: Path, _context: Mapping[str, object]
            ) -> BackupObservation:
                raise RuntimeError("uncertain")

        failing_provider = object.__new__(SQLiteRollbackObservationCapability)
        object.__setattr__(failing_provider, "adapter", FailingAdapter())
        object.__setattr__(failing_provider, "identity", provider.identity)
        with self.assertRaisesRegex(UpgradeError, "foreign adapter"):
            observing_capability.preflight(ROLLBACK_CONTEXT, failing_provider)
        failing_evidence = BoundRollbackCapability.bind(context, failing_provider.adapter)
        failing_capability = RollbackAuthorizationCapability.bind(context, failing_evidence)
        with self.assertRaisesRegex(UpgradeError, "observation failed"):
            failing_capability.preflight(ROLLBACK_CONTEXT, failing_provider)

    def test_git_observation_capability_is_concrete_and_identity_bound(self) -> None:
        context = PhaseContext(**cast(dict[str, Any], ROLLBACK_CONTEXT))
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            adapter = GitAuthorityAdapter(root)
            with self.assertRaisesRegex(UpgradeError, "concrete adapter"):
                GitRollbackObservationCapability.bind(
                    context,
                    cast(Any, object()),
                    cast(Any, object()),
                    lease=cast(Any, object()),
                    admission_recheck=cast(Any, object()),
                    expected_branch="main",
                    expected_head="head",
                )
            capability = GitRollbackObservationCapability.bind(
                context,
                adapter,
                cast(Any, object()),
                lease=cast(Any, object()),
                admission_recheck=cast(Any, object()),
                expected_branch="main",
                expected_head="head",
            )
            with self.assertRaisesRegex(UpgradeError, "identity mismatch"):
                capability.observe({**ROLLBACK_CONTEXT, "operation_id": "foreign"})

    def test_typed_rollback_evidence_rejects_untrusted_observations(self) -> None:
        invalid: tuple[tuple[object, object, object, object], ...] = (
            (bytearray(b"backup"), {"manifest": "v1"}, "control-store-1", 1),
            (b"backup", [], "control-store-1", 1),
            (b"backup", {"manifest": "v1"}, "", 1),
            (b"backup", {"manifest": "v1"}, "control-store-1", True),
        )
        for observations in invalid:
            with self.subTest(observations=observations), self.assertRaises(UpgradeError):
                RollbackBackupEvidence.from_observations(ROLLBACK_CONTEXT, *cast(Any, observations))

    def test_rollback_validation_rejects_backup_identity_drift(self) -> None:
        class EvidenceAdapter(FakeAdapter):
            def verify_rollback_context_bound(
                self, context: Mapping[str, object]
            ) -> Mapping[str, object]:
                return dict(context)

        context = PhaseContext(**cast(dict[str, Any], ROLLBACK_CONTEXT))
        capability = RollbackAuthorizationCapability.bind(
            context, BoundRollbackCapability.bind(context, EvidenceAdapter())
        )
        typed = RollbackBackupEvidence.from_observations(
            ROLLBACK_CONTEXT, b"backup-v1", {"manifest": "v1"}, "control-store-1", 1
        )
        evidence = typed.as_mapping()
        for field, value in (
            ("backup_bytes_digest", "0" * 64),
            ("manifest_digest", "1" * 64),
            ("control_store_identity", "replaced"),
            ("control_store_revision", 2),
        ):
            with (
                self.subTest(field=field),
                self.assertRaisesRegex(UpgradeError, "backup identity is invalid"),
            ):
                capability.validate(ROLLBACK_CONTEXT, {**evidence, field: value})

    def test_bound_rollback_inspection_dispatches_initialized_real_adapters(self) -> None:
        """Concrete adapter identity is retained without authorizing rollback."""
        for backend, adapter_type in (
            ("git", GitAuthorityAdapter),
            ("sqlite", SQLiteAuthorityAdapter),
        ):
            with self.subTest(backend=backend), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                if backend == "git":
                    adapter = adapter_type(root)
                else:
                    authority = root / "authority.sqlite"
                    authority.write_bytes(b"SQLite format 3\x00")
                    authority.chmod(0o600)
                    adapter = adapter_type(authority)
                context = make_context(f"op-real-inspect-{backend}")
                context["backend"] = backend
                context["barrier_identity_digest"] = canonical_barrier_digest(context)
                context["envelope_digest"] = canonical_envelope_digest(context)
                scope, lease, recheck = object(), object(), object()
                calls: list[tuple[object, ...]] = []

                def evidence(
                    context_arg: Mapping[str, object],
                    scope_arg: object,
                    *,
                    _calls: list[tuple[object, ...]] = calls,
                    **kwargs: object,
                ) -> dict[str, object]:
                    _calls.append(
                        (context_arg, scope_arg, kwargs["lease"], kwargs["admission_recheck"])
                    )
                    return {
                        **context_arg,
                        "phase": "rollback",
                        "backend_identity_verified": True,
                        "mutates_authority": False,
                        "rollback_context_verified": False,
                    }

                with patch.object(adapter, "verify_rollback_context_bound", side_effect=evidence):
                    engine = UpgradeEngine(
                        str(context["operation_id"]),
                        root / "journal.json",
                        context,
                        backend_adapter=adapter,
                        rollback_bound_verifier=BoundRollbackCapability.bind(
                            PhaseContext(**cast(dict[str, Any], context)),
                            adapter,
                            scope,
                            lease=lease,
                            admission_recheck=recheck,
                        ),
                    )
                    engine.plan()
                    before = (root / "journal.json").read_bytes()
                    result = engine.inspect_rollback_bound()
                    self.assertFalse(result["rollback_context_verified"])
                    self.assertEqual(before, (root / "journal.json").read_bytes())
                    self.assertEqual(1, len(calls))
                    self.assertIs(calls[0][1], scope)
                    self.assertIs(calls[0][2], lease)
                    self.assertIs(calls[0][3], recheck)
                    with engine._exclusive():
                        pass

    def test_rollback_rejects_forged_bound_verifier_before_backend_or_handler(self) -> None:
        class ConcreteAdapter(FakeAdapter):
            requires_bound_rollback = True

            def snapshot(self, _phase: str, _context: object) -> dict[str, object]:
                raise AssertionError("forged verifier must block snapshot")

            def execute(self, _phase: str, _context: object) -> dict[str, object]:
                raise AssertionError("forged verifier must block execute")

        with tempfile.TemporaryDirectory() as directory:
            operation_id = "op-forged-verifier"
            with self.assertRaisesRegex(UpgradeError, "trusted bound rollback capability"):
                UpgradeEngine(
                    operation_id,
                    Path(directory) / "journal.json",
                    make_context(operation_id),
                    backend_adapter=ConcreteAdapter(),
                    rollback_bound_verifier=lambda _context: {  # type: ignore[arg-type]
                        "rollback_context_verified": True
                    },
                )

    def test_rollback_rejects_mismatched_capability_before_journal_activity(self) -> None:
        class ConcreteAdapter(FakeAdapter):
            requires_bound_rollback = True

            def verify_rollback_context_bound(
                self, _context: Mapping[str, object]
            ) -> Mapping[str, object]:
                raise AssertionError("mismatched capability must not verify")

        with tempfile.TemporaryDirectory() as directory:
            operation_id = "op-mismatched-capability"
            journal = Path(directory) / "journal.json"
            context = make_context(operation_id)
            wrong = make_context("other-operation")
            capability = BoundRollbackCapability.bind(
                PhaseContext(**cast(dict[str, Any], wrong)), ConcreteAdapter()
            )
            with self.assertRaisesRegex(UpgradeError, "identity mismatch"):
                UpgradeEngine(
                    operation_id,
                    journal,
                    context,
                    backend_adapter=ConcreteAdapter(),
                    rollback_bound_verifier=capability,
                )
            self.assertFalse(journal.exists())

    def test_rollback_rejects_capability_bound_to_different_backend(self) -> None:
        class ConcreteAdapter(FakeAdapter):
            requires_bound_rollback = True

            def verify_rollback_context_bound(
                self, _context: Mapping[str, object]
            ) -> Mapping[str, object]:
                raise AssertionError("foreign verifier must not run")

            def execute(self, _phase: str, _context: object) -> dict[str, object]:
                raise AssertionError("execute must remain unreachable")

        with tempfile.TemporaryDirectory() as directory:
            operation_id = "op-foreign-capability"
            journal = Path(directory) / "journal.json"
            context = make_context(operation_id)
            backend = ConcreteAdapter()
            foreign = ConcreteAdapter()
            capability = BoundRollbackCapability.bind(
                PhaseContext(**cast(dict[str, Any], context)), foreign
            )
            with self.assertRaisesRegex(UpgradeError, "backend mismatch"):
                UpgradeEngine(
                    operation_id,
                    journal,
                    context,
                    backend_adapter=backend,
                    rollback_bound_verifier=capability,
                )
            self.assertFalse(journal.exists())

    def test_bound_capability_rejects_forged_context_before_concrete_verifier(self) -> None:
        class ConcreteAdapter(FakeAdapter):
            def verify_rollback_context_bound(
                self, _context: Mapping[str, object]
            ) -> Mapping[str, object]:
                raise AssertionError("forged context must not reach verifier")

        context = make_context("op-context-forge")
        capability = BoundRollbackCapability.bind(
            PhaseContext(**cast(dict[str, Any], context)), ConcreteAdapter()
        )
        forged = dict(context)
        forged["fencing_token"] = "forged"  # noqa: S105
        with self.assertRaisesRegex(UpgradeError, "context identity mismatch"):
            capability.verify(forged)

    def test_bound_capability_dispatches_real_backend_signature(self) -> None:
        context = PhaseContext(**cast(dict[str, Any], ROLLBACK_CONTEXT))
        scope = object()
        lease = object()
        recheck = object()
        for adapter_type, expected in (
            (GitAuthorityAdapter, {"expected_branch": "main", "expected_head": "head"}),
            (SQLiteAuthorityAdapter, {}),
        ):
            adapter = cast(Any, object.__new__(adapter_type))
            calls: list[tuple[tuple[object, ...], dict[str, object]]] = []

            def verify_bound(
                *args: object,
                _calls: list[tuple[tuple[object, ...], dict[str, object]]] = calls,
                **kwargs: object,
            ) -> dict[str, object]:
                _calls.append((args, kwargs))
                return dict(ROLLBACK_CONTEXT)

            adapter.verify_rollback_context_bound = verify_bound
            capability = BoundRollbackCapability.bind(
                context,
                adapter,
                scope,
                lease=lease,
                admission_recheck=recheck,
                **expected,
            )
            result = capability.verify(ROLLBACK_CONTEXT)
            self.assertFalse(result["rollback_context_verified"])
            self.assertEqual(len(calls), 1)
            self.assertIs(calls[0][0][0], ROLLBACK_CONTEXT)
            self.assertIs(calls[0][0][1], scope)
            self.assertIs(calls[0][1]["lease"], lease)
            self.assertIs(calls[0][1]["admission_recheck"], recheck)
            for key, value in expected.items():
                self.assertEqual(calls[0][1][key], value)


if __name__ == "__main__":
    unittest.main()
