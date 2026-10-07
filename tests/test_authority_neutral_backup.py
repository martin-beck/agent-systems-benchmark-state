# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Hostile tests for the authority-neutral backup-only executor."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from typing import Any, cast

from tools.authority_neutral_backup import (
    BackupExecutionError,
    BoundBackupPhaseAdapter,
    execute_verified_backup,
)

OPERATION = {"opcode": "backend.backup"}


def _context(backend: str = "git") -> dict[str, object]:
    root = Path(tempfile.gettempdir()).resolve() / "coordinator-artifacts"
    return {
        "backend": backend,
        "target": "new",
        "destination": str(root / "backup"),
        "artifact_root": str(root),
        "binding": {"project_id": "project"},
    }


class _GitAdapter:
    def execute_generated_backup(
        self, _operation: dict[str, object], _context: dict[str, object]
    ) -> dict[str, object]:
        return {
            "outcome": "completed",
            "backup_verified": True,
            "restore_roundtrip_verified": True,
            "backend_identity_verified": True,
            "mutates_authority": False,
        }


class _SQLiteAdapter:
    def __init__(self) -> None:
        self.destination: Path | None = None
        self.binding: dict[str, Any] | None = None

    def execute_generated_operation(
        self, _operation: dict[str, object], destination: Path, binding: dict[str, Any]
    ) -> dict[str, object]:
        self.destination = destination
        self.binding = binding
        return {
            "outcome": "completed",
            "backup_verified": True,
            "restore_roundtrip_verified": True,
            "backend_identity_verified": True,
            "mutates_authority": False,
        }


class AuthorityNeutralBackupTests(unittest.TestCase):
    def test_bound_phase_adapter_validates_constructor_and_delegated_surfaces(self) -> None:
        context = {
            "schema_version": 2,
            "backend": "git",
            "project_id": "project",
            "operation_id": "op-1",
            "state_revision": 1,
            "authority_revision": "authority",
            "fencing_token": "fence",
            "fencing_owner": "owner",
            "durable_barrier_id": "barrier",
            "artifact_root": _context()["artifact_root"],
            "source": "source",
            "destination": _context()["destination"],
            "manifest": "manifest",
            "selector_ref": "selector",
            "barrier_identity_digest": "digest",
            "target": "new",
            "envelope_digest": "envelope",
        }
        bound = {**context, "binding": {"project_id": "project"}}
        with self.assertRaisesRegex(BackupExecutionError, "unsupported"):
            BoundBackupPhaseAdapter(object(), {"opcode": "selector.commit"}, bound)
        with self.assertRaisesRegex(BackupExecutionError, "context is incomplete"):
            BoundBackupPhaseAdapter(object(), OPERATION, cast(Any, None))
        with self.assertRaisesRegex(BackupExecutionError, "omits engine identity"):
            BoundBackupPhaseAdapter(object(), OPERATION, {"backend": "git"})

        class Delegating(_GitAdapter):
            requires_bound_rollback = True

            def snapshot(self, _phase: str, _context: object) -> dict[str, object]:
                return {"snapshot": True}

            def verify_rollback_context(self, _context: object) -> None:
                return None

            def execute(self, _phase: str, _context: object) -> dict[str, object]:
                return {"delegated": True}

        adapter = BoundBackupPhaseAdapter(Delegating(), OPERATION, bound)
        self.assertTrue(adapter.requires_bound_rollback)
        self.assertEqual({"snapshot": True}, adapter.snapshot("discover", context))
        self.assertIsNone(adapter.verify_rollback_context(context))
        self.assertEqual({"delegated": True}, adapter.execute("stage", context))
        self.assertTrue(hasattr(adapter.operation_lock(), "__enter__"))

        class InvalidDelegating(_GitAdapter):
            requires_bound_rollback = True

            def snapshot(self, _phase: str, _context: object) -> str:
                return "invalid"

            def verify_rollback_context(self, _context: object) -> str:
                return "invalid"

            def execute(self, _phase: str, _context: object) -> str:
                return "invalid"

        invalid = BoundBackupPhaseAdapter(InvalidDelegating(), OPERATION, bound)
        with self.assertRaisesRegex(BackupExecutionError, "snapshot"):
            invalid.snapshot("discover", context)
        with self.assertRaisesRegex(BackupExecutionError, "rollback verification"):
            invalid.verify_rollback_context(context)
        with self.assertRaisesRegex(BackupExecutionError, "execution result"):
            invalid.execute("stage", context)

    def test_bound_phase_adapter_binds_identity_and_dispatches_only_backup(self) -> None:
        class Backend(_GitAdapter):
            def __init__(self) -> None:
                self.phases: list[str] = []

            def snapshot(self, phase: str, _context: object) -> dict[str, object]:
                self.phases.append(f"snapshot:{phase}")
                return {"phase": phase}

            def execute(self, phase: str, _context: object) -> dict[str, object]:
                self.phases.append(f"execute:{phase}")
                return {"mutates_authority": False}

            def verify_rollback_context(self, _context: object) -> dict[str, object]:
                return {"verified": True}

        engine_context = {
            "schema_version": 2,
            "backend": "git",
            "project_id": "project",
            "operation_id": "op-1",
            "state_revision": 1,
            "authority_revision": "authority",
            "fencing_token": "fence",
            "fencing_owner": "owner",
            "durable_barrier_id": "barrier",
            "artifact_root": _context()["artifact_root"],
            "source": "source",
            "destination": _context()["destination"],
            "manifest": "manifest",
            "selector_ref": "selector",
            "barrier_identity_digest": "digest",
            "target": "new",
            "envelope_digest": "envelope",
        }
        backup_context = {**engine_context, "binding": {"project_id": "project"}}
        backend = Backend()
        adapter = BoundBackupPhaseAdapter(backend, OPERATION, backup_context)
        result = adapter.execute("backup", engine_context)
        self.assertEqual("completed", result["outcome"])
        self.assertEqual([], backend.phases)
        adapter.execute("reopen", engine_context)
        self.assertEqual(["execute:reopen"], backend.phases)

    def test_bound_phase_adapter_rejects_identity_drift_before_dispatch(self) -> None:
        context = {
            "schema_version": 2,
            "backend": "git",
            "project_id": "project",
            "operation_id": "op-1",
            "state_revision": 1,
            "authority_revision": "authority",
            "fencing_token": "fence",
            "fencing_owner": "owner",
            "durable_barrier_id": "barrier",
            "artifact_root": _context()["artifact_root"],
            "source": "source",
            "destination": _context()["destination"],
            "manifest": "manifest",
            "selector_ref": "selector",
            "barrier_identity_digest": "digest",
            "target": "new",
            "envelope_digest": "envelope",
        }
        adapter = BoundBackupPhaseAdapter(
            _GitAdapter(), OPERATION, {**context, "binding": {"project_id": "project"}}
        )
        drifted = {**context, "fencing_token": "foreign"}
        with self.assertRaisesRegex(BackupExecutionError, "identity mismatch"):
            adapter.execute("backup", drifted)

    def test_git_dispatch_returns_only_verified_non_mutating_evidence(self) -> None:
        result = execute_verified_backup(_GitAdapter(), OPERATION, _context())
        self.assertTrue(result["backup_verified"])
        self.assertFalse(result["mutates_authority"])

    def test_sqlite_dispatch_uses_bound_destination_and_binding(self) -> None:
        adapter = _SQLiteAdapter()
        context = _context("sqlite")
        result = execute_verified_backup(adapter, OPERATION, context)
        self.assertEqual(Path(str(context["destination"])), adapter.destination)
        self.assertEqual(context["binding"], adapter.binding)
        self.assertEqual("completed", result["outcome"])

    def test_rejects_destination_escape_before_backend_call(self) -> None:
        context = _context()
        context["destination"] = str(Path(str(context["artifact_root"])).parent / "escape")
        with self.assertRaisesRegex(BackupExecutionError, "escapes artifact root"):
            execute_verified_backup(_GitAdapter(), OPERATION, context)

    def test_rejects_mutating_or_incomplete_backend_result(self) -> None:
        class Mutating:
            def execute_generated_backup(
                self, _operation: object, _context: object
            ) -> dict[str, object]:
                return {
                    "outcome": "completed",
                    "backup_verified": True,
                    "restore_roundtrip_verified": True,
                    "backend_identity_verified": True,
                    "mutates_authority": True,
                }

        with self.assertRaisesRegex(BackupExecutionError, "postconditions"):
            execute_verified_backup(Mutating(), OPERATION, _context())

    def test_rejects_wrong_opcode_and_backend(self) -> None:
        with self.assertRaisesRegex(BackupExecutionError, "unsupported"):
            execute_verified_backup(_GitAdapter(), {"opcode": "selector.commit"}, _context())
        invalid = _context("other")
        with self.assertRaisesRegex(BackupExecutionError, "identity"):
            execute_verified_backup(_GitAdapter(), OPERATION, invalid)

    def test_rejects_incomplete_and_malformed_context(self) -> None:
        with self.assertRaisesRegex(BackupExecutionError, "context is incomplete"):
            execute_verified_backup(_GitAdapter(), OPERATION, {})
        context = _context()
        context.pop("destination")
        with self.assertRaisesRegex(BackupExecutionError, "context is incomplete"):
            execute_verified_backup(_GitAdapter(), OPERATION, context)
        context = _context()
        context["destination"] = object()
        with self.assertRaisesRegex(BackupExecutionError, "artifact binding"):
            execute_verified_backup(_GitAdapter(), OPERATION, context)
        context = _context()
        context["binding"] = []
        with self.assertRaisesRegex(BackupExecutionError, "authority binding"):
            execute_verified_backup(_GitAdapter(), OPERATION, context)

    def test_rejects_incomplete_or_malformed_backend_results(self) -> None:
        class Incomplete:
            def execute_generated_backup(
                self, _operation: object, _context: object
            ) -> dict[str, object]:
                return {"outcome": "completed"}

        class NonMapping:
            def execute_generated_backup(self, _operation: object, _context: object) -> str:
                return "invalid"

        with self.assertRaisesRegex(BackupExecutionError, "result is incomplete"):
            execute_verified_backup(Incomplete(), OPERATION, _context())
        with self.assertRaisesRegex(BackupExecutionError, "result is invalid"):
            execute_verified_backup(NonMapping(), OPERATION, _context())

    def test_wraps_backend_failures_as_backup_errors(self) -> None:
        class Failing:
            def execute_generated_backup(
                self, _operation: object, _context: object
            ) -> dict[str, object]:
                raise RuntimeError("injected failure")

        with self.assertRaisesRegex(BackupExecutionError, "execution failed"):
            execute_verified_backup(Failing(), OPERATION, _context())

        class AlreadyClassified:
            def execute_generated_backup(
                self, _operation: object, _context: object
            ) -> dict[str, object]:
                raise BackupExecutionError("already classified")

        with self.assertRaisesRegex(BackupExecutionError, "already classified"):
            execute_verified_backup(AlreadyClassified(), OPERATION, _context())


if __name__ == "__main__":
    unittest.main()
