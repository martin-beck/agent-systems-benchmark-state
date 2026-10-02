"""Focused negative-path coverage for the restored authority seams."""

from __future__ import annotations

import json
import os
import tempfile
import unittest
from argparse import Namespace
from pathlib import Path
from typing import Any, cast
from unittest.mock import patch

from tools import handoffctl, upgrade_authority
from tools.admission_lease import AdmissionLeaseError, lease_from_record, validate_recheck
from tools.git_authority_adapter import GitAuthorityAdapter, GitAuthorityError
from tools.handoffctl import dispatch_bound_command, dispatch_read_only_command
from tools.lifecycle_trace import (
    _issue_event,
    validate_model_trace,
    validate_terminal_outcome,
)
from tools.oracle_lifecycle import (
    ArtifactRef,
    GateError,
    GateStage,
    InteractionEvent,
    StageGate,
    apply_event,
    gate_errors,
    transition_allowed,
)
from tools.role_assignment import assignment_errors
from tools.role_registry import registry_errors
from tools.rollback_control_store import (
    AuthorityEffectIntent,
    BarrierSessionContract,
    BarrierSessionState,
    ControlStoreError,
    SQLiteRollbackControlStore,
    _validate,
    _validate_authority_effect_receipt,
    _validate_expected_revision,
)
from tools.upgrade_authority import AuthorityError
from tools.upgrade_identity import (
    BarrierChildIdentity,
    BarrierSessionIdentity,
    canonical_barrier_session_digest,
)
from tools.validate_upgrade_contract import ContractError, validate_contract


class GeneratedOperationValidationTests(unittest.TestCase):
    def _operation(self) -> dict[str, object]:
        return {
            "operation_id": "op-1",
            "opcode": "backend.backup",
            "inputs": {
                "backend": "git",
                "selector_ref": "refs/heads/main",
                "expected_state_revision": 1,
                "barrier_id": "barrier-1",
                "fencing_token": "fence-1",
                "backup_operation_id": "op-1",
            },
            "timeout_seconds": 300,
            "resources": ["maintenance-barrier", "durable-operation-record"],
            "preconditions": ["previous-phase-complete"],
            "postconditions": ["backup-contract-satisfied"],
            "evidence": ["durable-operation-record"],
            "durable_record": "operation-id-and-outcome",
        }

    def test_valid_operation_binds_identity(self) -> None:
        operation_id, inputs = GitAuthorityAdapter._validate_generated_backup_operation(
            self._operation()
        )
        self.assertEqual("op-1", operation_id)
        self.assertEqual("git", inputs["backend"])

    def test_invalid_operation_fields_fail_closed(self) -> None:
        checks: tuple[tuple[str, Any], ...] = (
            ("opcode", "backend.commit"),
            ("timeout_seconds", 1),
            ("resources", ["maintenance-barrier"]),
            ("preconditions", []),
            ("postconditions", []),
            ("evidence", []),
            ("durable_record", "none"),
        )
        for key, value in checks:
            with self.subTest(key=key):
                operation = self._operation()
                operation[key] = value
                with self.assertRaises(GitAuthorityError):
                    GitAuthorityAdapter._validate_generated_backup_operation(operation)

    def test_invalid_identity_and_inputs_fail_closed(self) -> None:
        for key, value in (("operation_id", ""), ("inputs", {})):
            with self.subTest(key=key):
                operation = self._operation()
                operation[key] = value
                with self.assertRaises(GitAuthorityError):
                    GitAuthorityAdapter._validate_generated_backup_operation(operation)

        operation = self._operation()
        operation["inputs"] = {
            **cast(dict[str, Any], operation["inputs"]),
            "expected_state_revision": 0,
        }
        with self.assertRaises(GitAuthorityError):
            GitAuthorityAdapter._validate_generated_backup_operation(operation)

    def test_each_binding_field_is_checked(self) -> None:
        checks: tuple[tuple[str, Any], ...] = (
            ("backend", "sqlite"),
            ("backup_operation_id", "other"),
            ("expected_state_revision", "1"),
        )
        for key, value in checks:
            with self.subTest(key=key):
                operation = self._operation()
                operation["inputs"] = {**cast(dict[str, Any], operation["inputs"]), key: value}
                with self.assertRaises(GitAuthorityError):
                    GitAuthorityAdapter._validate_generated_backup_operation(operation)

    def test_unknown_operation_fields_are_rejected(self) -> None:
        operation = self._operation()
        operation["unexpected"] = True
        with self.assertRaises(GitAuthorityError):
            GitAuthorityAdapter._validate_generated_backup_operation(operation)


class OracleGateValidationTests(unittest.TestCase):
    def _gate(self) -> dict[str, object]:
        return {
            "required": True,
            "open_stage": None,
            "completed": [],
            "events": [],
            "authorized": False,
            "discussion_rounds": 0,
            "reconciliation_required": False,
        }

    def test_invalid_authorization_and_reconciliation_types_fail_closed(self) -> None:
        for field in ("authorized", "reconciliation_required"):
            value = self._gate()
            value[field] = "yes"
            with self.subTest(field=field):
                self.assertIn(field, gate_errors(value)[0])

    def test_invalid_discussion_rounds_fail_closed(self) -> None:
        for rounds in (-1, 17, "one"):
            value = self._gate()
            value["discussion_rounds"] = rounds
            with self.subTest(rounds=rounds):
                self.assertIn("discussion_rounds", gate_errors(value)[0])

    def _event(
        self, *, action: str = "open", stage: str = "intake", disposition: str = "accepted"
    ) -> InteractionEvent:
        artifact = ArtifactRef("evidence.json", "sha256:" + "0" * 64)
        return InteractionEvent(
            task_id="AR-1671",
            task_revision=1,
            stage=GateStage(stage)
            if stage in {item.value for item in GateStage}
            else StageGate(stage),
            action=action,
            disposition=disposition,
            before=(artifact,),
            after=(artifact,),
            public_ref="evidence.json",
            recorded_at="2026-01-01T00:00:00Z",
        )

    def test_gate_errors_rejects_shape_sequence_and_event_overflow(self) -> None:
        self.assertEqual([], gate_errors(None))
        for value in cast(
            tuple[Any, ...], ([], {"required": False}, {**self._gate(), "stage_sequence": []})
        ):
            self.assertTrue(gate_errors(value))
        malformed = {**self._gate(), "events": [{"bad": True}]}
        self.assertIn("event invalid", gate_errors(malformed)[0])
        oversized = {**self._gate(), "events": [self._event().as_record()] * 33}
        self.assertIn("unbounded", gate_errors(oversized)[0])

    def test_event_round_trip_and_transition_guards(self) -> None:
        event = self._event()
        self.assertEqual(
            event.as_record(), InteractionEvent.from_record(event.as_record()).as_record()
        )
        meta: dict[str, Any] = {"id": "AR-1671", "task_revision": 1}
        apply_event(meta, event)
        self.assertEqual("intake", meta["oracle_gate"]["open_stage"])
        with self.assertRaises(GateError):
            transition_allowed(meta, "claim")
        with self.assertRaises(GateError):
            apply_event(meta, self._event())

    def test_event_resolution_rejection_and_reopen_paths(self) -> None:
        meta: dict[str, Any] = {"id": "AR-1671", "task_revision": 1}
        apply_event(meta, self._event())
        apply_event(meta, self._event(action="resolve", disposition="rejected"))
        self.assertTrue(meta["oracle_gate"]["reconciliation_required"])
        apply_event(meta, self._event(action="resolve", disposition="accepted"))
        self.assertIn("intake", meta["oracle_gate"]["completed"])
        apply_event(meta, self._event(action="reopen"))
        self.assertEqual("intake", meta["oracle_gate"]["open_stage"])


class LifecycleTraceTests(unittest.TestCase):
    def _trace(self, phases: tuple[str, ...], target: str | None = None) -> tuple[Any, ...]:
        proof = object()
        return tuple(
            _issue_event(
                proof,
                phase,
                index,
                "owner",
                "lock",
                "project",
                "digest",
                "fence",
                terminal_target=target if index == len(phases) - 1 else None,
            )
            for index, phase in enumerate(phases)
        )

    def test_forward_and_rollback_terminal_traces(self) -> None:
        forward = self._trace(
            ("acquire", "quiesce", "backup", "stage", "commit", "validate", "reopen"), "new"
        )
        self.assertEqual("new", validate_terminal_outcome(forward))
        rollback = self._trace(
            (
                "acquire",
                "quiesce",
                "backup",
                "rollback_started",
                "rollback_verified",
                "rollback_released",
            ),
            "rollback",
        )
        self.assertEqual("rollback", validate_terminal_outcome(rollback))
        self.assertEqual(("Preflight", "Quiesce", "Backup"), validate_model_trace(forward[:3]))

    def test_trace_rejects_identity_transition_and_bad_terminal(self) -> None:
        events = list(self._trace(("acquire", "quiesce")))
        events[1] = _issue_event(
            object(), "quiesce", 1, "other", "lock", "project", "digest", "fence"
        )
        with self.assertRaises(ValueError):
            validate_model_trace(tuple(events))
        with self.assertRaises(ValueError):
            validate_terminal_outcome(
                self._trace(
                    ("acquire", "quiesce", "backup", "stage", "commit", "validate", "reopen")
                )
            )


class UpgradeValidationTests(unittest.TestCase):
    def test_validator_rejects_identity_order_and_backend_drift(self) -> None:
        from test_upgrade_contracts import contract

        base = contract()
        validate_contract(base)
        mutations = (
            ("from", {**base["from"], "version": base["to"]["version"]}),
            (
                "phase order",
                {**base, "phases": [{**base["phases"][0], "order": 2}, *base["phases"][1:]]},
            ),
            ("backend", {**base, "backend_contracts": [base["backend_contracts"][0]]}),
            (
                "integrity",
                {**base, "rollback": {**base["rollback"], "backup_integrity": "generic"}},
            ),
        )
        for label, value in mutations:
            with self.subTest(label=label), self.assertRaises(ContractError):
                validate_contract(value)


class AdmissionLeaseAdditionalTests(unittest.TestCase):
    def setUp(self) -> None:
        self.record = {
            "project_id": "project",
            "authority_revision": "authority",
            "fencing_token": "fence",
            "fencing_owner": "owner",
            "durable_barrier_id": "barrier",
            "revision": 1,
        }

    def test_all_lease_identity_and_recheck_types_are_fail_closed(self) -> None:
        for field in (
            "project_id",
            "authority_revision",
            "fencing_token",
            "fencing_owner",
            "durable_barrier_id",
        ):
            value = dict(self.record)
            value[field] = 1
            with self.subTest(field=field), self.assertRaises(AdmissionLeaseError):
                lease_from_record(value)
        lease = lease_from_record(self.record)
        for field in (
            "project_id",
            "authority_revision",
            "fencing_token",
            "fencing_owner",
            "durable_barrier_id",
            "revision",
        ):
            value = dict(self.record)
            value[field] = 2 if field == "revision" else 1
            with self.subTest(field=field), self.assertRaises(AdmissionLeaseError):
                validate_recheck(lease, **value)


class HandoffDispatchAdditionalTests(unittest.TestCase):
    def test_role_dispatch_routes_all_read_and_write_actions(self) -> None:
        from argparse import Namespace

        from tools import handoffctl

        common = {"state": "state.json", "registry": "registry.json", "owner_id": "owner"}
        with patch("tools.roles.assign", return_value={"assigned": True}) as assign:
            args = Namespace(
                **common,
                roles_command="assign",
                expected_revision=1,
                assignment_id="a",
                role_id="r",
                expires_at="",
                evidence_kind="",
                evidence_ref="",
                evidence_digest="",
            )
            self.assertEqual(0, handoffctl.dispatch_roles_command(args))
            assign.assert_called_once()
        for command, name in (("list", "list_assignments"), ("check", "check")):
            args = Namespace(**common, roles_command=command)
            with patch(f"tools.roles.{name}", return_value={"ok": True}) as mocked:
                self.assertEqual(0, handoffctl.dispatch_roles_command(args))
                mocked.assert_called_once()
        args = Namespace(**common, roles_command="remove", expected_revision=1, assignment_id="a")
        with patch("tools.roles.remove", return_value={"removed": True}) as mocked:
            self.assertEqual(0, handoffctl.dispatch_roles_command(args))
            mocked.assert_called_once()

    def test_read_only_dispatch_selects_each_projection(self) -> None:
        from argparse import Namespace

        from tools import handoffctl

        with patch.object(handoffctl, "cmd_snapshot") as snapshot:
            handoffctl.dispatch_read_only_command(Namespace(cmd="snapshot", task="AR-1"))
            snapshot.assert_called_once_with("AR-1")
        with patch.object(handoffctl, "cmd_board") as board:
            handoffctl.dispatch_read_only_command(Namespace(cmd="board"))
            board.assert_called_once_with()
        with patch.object(handoffctl, "cmd_metrics") as metrics:
            handoffctl.dispatch_read_only_command(Namespace(cmd="metrics"))
            metrics.assert_called_once_with()

    def test_validator_rejects_phase_operation_and_input_drift(self) -> None:
        from test_upgrade_contracts import contract

        base = contract()
        checks = (
            (
                "phase id",
                {**base, "phases": [{**base["phases"][0], "id": "wrong"}, *base["phases"][1:]]},
            ),
            (
                "opcode",
                {
                    **base,
                    "phases": [
                        {
                            **base["phases"][3],
                            "operation": {**base["phases"][3]["operation"], "opcode": "bad"},
                        },
                        *base["phases"][4:],
                    ],
                },
            ),
            (
                "input fields",
                {
                    **base,
                    "phases": [
                        {
                            **base["phases"][0],
                            "operation": {
                                **base["phases"][0]["operation"],
                                "inputs": {"backend": "git"},
                            },
                        },
                        *base["phases"][1:],
                    ],
                },
            ),
        )
        for label, value in checks:
            with self.subTest(label=label), self.assertRaises(ContractError):
                validate_contract(value)


class RoleValidationNegativePaths(unittest.TestCase):
    def setUp(self) -> None:
        self.registry = json.loads(
            (Path(__file__).parents[1] / "examples/roles/role-registry.json").read_text()
        )
        self.assignment = json.loads(
            (Path(__file__).parents[1] / "examples/roles/role-assignment.json").read_text()
        )

    def test_registry_non_object_and_unknown_fields_fail_closed(self) -> None:
        self.assertEqual(["role registry must be an object"], registry_errors([]))
        unknown = dict(self.registry, unexpected=True)
        self.assertTrue(any(item.startswith("schema:") for item in registry_errors(unknown)))

    def test_assignment_non_object_and_unknown_fields_fail_closed(self) -> None:
        self.assertEqual(
            ["role assignment must be an object"], assignment_errors([], self.registry)
        )
        unknown = dict(self.assignment, unexpected=True)
        self.assertTrue(
            any(item.startswith("schema:") for item in assignment_errors(unknown, self.registry))
        )


class ControlRecordNegativePaths(unittest.TestCase):
    def _identity(self) -> BarrierSessionIdentity:
        record = {
            "schema_version": 1,
            "project_id": "123e4567-e89b-42d3-a456-426614174000",
            "attempt_id": "attempt",
            "state_revision": 1,
            "authority_revision_at_acquire": "authority",
            "durable_barrier_id": "barrier",
            "fencing_token": "fence",
            "fencing_owner": "owner",
            "identity_digest": "0" * 64,
        }
        record["identity_digest"] = canonical_barrier_session_digest(record)
        return BarrierSessionIdentity.from_record(record)

    def test_barrier_state_rejects_invalid_status_revision_and_reopen(self) -> None:
        identity = self._identity()
        for kwargs in cast(
            tuple[dict[str, Any], ...],
            (
                {"status": "unknown", "revision": 1},
                {"status": "held", "revision": 0},
                {"status": "held", "revision": 1, "reopen_target": "rollback"},
            ),
        ):
            with self.subTest(kwargs=kwargs), self.assertRaises(ControlStoreError):
                BarrierSessionState(identity, **kwargs)

    def test_effect_intent_rejects_invalid_identity_and_partial_admission(self) -> None:
        values: dict[str, Any] = {
            "intent_id": "intent",
            "operation_id": "operation",
            "backend": "git",
            "target": "new",
            "attempt_id": "attempt",
            "identity_digest": "digest",
            "fencing_token": "fence",
            "session_revision": 1,
        }
        with self.assertRaises(ControlStoreError):
            AuthorityEffectIntent(**{**values, "backend": "other"})
        with self.assertRaises(ControlStoreError):
            AuthorityEffectIntent(**{**values, "artifact_identity": "artifact"})

    def test_effect_receipt_must_match_every_admission_field(self) -> None:
        intent = AuthorityEffectIntent(
            intent_id="intent",
            operation_id="operation",
            backend="sqlite",
            target="rollback",
            attempt_id="attempt",
            identity_digest="digest",
            fencing_token="fence",  # noqa: S106
            session_revision=1,
            artifact_identity="artifact",
            manifest_identity="manifest",
            selector_identity="selector",
            runtime_identity="runtime",
        )
        receipt = {
            "backend": "sqlite",
            "target": "rollback",
            "operation_id": "operation",
            "state_revision": 1,
            "artifact_identity": "artifact",
            "manifest_identity": "manifest",
            "selector_identity": "selector",
            "runtime_identity": "runtime",
            "fencing_token": "fence",
            "mutates_authority": True,
        }
        _validate_authority_effect_receipt(intent, receipt)
        receipt["runtime_identity"] = "wrong"
        with self.assertRaises(ControlStoreError):
            _validate_authority_effect_receipt(intent, receipt)

    def test_contract_rejects_unbound_or_incomplete_reopen(self) -> None:
        contract = BarrierSessionContract(self._identity())
        with self.assertRaises(ControlStoreError):
            contract.bind_child(
                1, BarrierChildIdentity.bind(self._identity(), "rollback", "rollback")
            )
        forward = BarrierChildIdentity.bind(self._identity(), "forward", "new")
        contract.bind_child(1, forward)
        with self.assertRaises(ControlStoreError):
            contract.begin_reopen(2, "new")
        with self.assertRaises(ControlStoreError):
            contract.begin_reopen(2, "other", {})
        with self.assertRaises(ControlStoreError):
            contract.mark_ambiguous(2, "not valid!")

    def test_contract_rejects_runtime_evidence_mismatch(self) -> None:
        contract = BarrierSessionContract(self._identity())
        identity = self._identity()
        contract.bind_child(1, BarrierChildIdentity.bind(identity, "forward", "new"))
        evidence = {
            "operation_id": "forward",
            "target": "new",
            "barrier_identity_digest": identity.identity_digest,
            "validated": True,
        }
        contract.begin_reopen(2, "new", evidence)
        with self.assertRaises(ControlStoreError):
            contract.complete_reopen(3, {"target": "new"})
        with self.assertRaises(ControlStoreError):
            contract.complete_reopen(3, {"target": "rollback"})

    def test_contract_binds_both_children_and_completes_reopen(self) -> None:
        identity = self._identity()
        contract = BarrierSessionContract(identity)
        forward = BarrierChildIdentity.bind(identity, "forward", "new")
        rollback = BarrierChildIdentity.bind(identity, "rollback", "rollback")
        contract.bind_child(1, forward)
        contract.bind_child(2, rollback)
        evidence = {
            "operation_id": "forward",
            "target": "new",
            "barrier_identity_digest": identity.identity_digest,
            "validated": True,
        }
        contract.begin_reopen(3, "new", evidence)
        runtime = {
            "authority_revision": identity.authority_revision_at_acquire,
            "backend": "sqlite",
            "backend_roundtrip": "sqlite",
            "foreign_key_violations": 0,
            "fencing_token": identity.fencing_token,
            "integrity_check": "ok",
            "project_id": identity.project_id,
            "target": "new",
            "verified": True,
        }
        self.assertEqual("released", contract.complete_reopen(4, runtime).status)


class HandoffDispatchCoverage(unittest.TestCase):
    def test_read_only_dispatch_routes_each_projection(self) -> None:
        with patch("tools.handoffctl.cmd_snapshot") as snapshot:
            dispatch_read_only_command(Namespace(cmd="snapshot", task="AR-0001"))
            snapshot.assert_called_once_with("AR-0001")
        with patch("tools.handoffctl.cmd_board") as board:
            dispatch_read_only_command(Namespace(cmd="board"))
            board.assert_called_once_with()
        with patch("tools.handoffctl.cmd_metrics") as metrics:
            dispatch_read_only_command(Namespace(cmd="metrics"))
            metrics.assert_called_once_with()

    def test_unknown_bound_command_is_noop(self) -> None:
        self.assertEqual(0, dispatch_bound_command(Namespace(cmd="unknown")))


class AuthorityDefensiveMatrix(unittest.TestCase):
    def test_selector_file_helpers_cover_hostile_entries(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            selector = root / "selector.json"
            parent = os.open(root, os.O_RDONLY | os.O_DIRECTORY)
            try:
                selector.mkdir()
                with self.assertRaises(AuthorityError):
                    upgrade_authority._existing_regular_identity(parent, selector.name)
                with self.assertRaises(AuthorityError):
                    upgrade_authority._remove_selector_temporary(parent, selector.name)
                selector.rmdir()
                selector.write_text("{}", encoding="utf-8")
                with self.assertRaises(AuthorityError):
                    upgrade_authority._remove_selector_temporary(parent, selector.name)
                selector.unlink()
                selector.write_bytes(b"x" * (64 * 1024 + 1))
                with self.assertRaisesRegex(AuthorityError, "too large"):
                    upgrade_authority._read_runtime_selector_at(parent, selector.name)
                selector.write_text(
                    json.dumps(
                        {
                            "schema_version": 1,
                            "active_release": "a",
                            "previous_release": "b",
                            "extra": 1,
                        }
                    ),
                    encoding="utf-8",
                )
                with self.assertRaisesRegex(AuthorityError, "schema"):
                    upgrade_authority._read_runtime_selector_at(parent, selector.name)
            finally:
                os.close(parent)

    def test_selector_cleanup_and_sidecar_matrix(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            parent = os.open(root, os.O_RDONLY | os.O_DIRECTORY)
            try:
                staging = root / ".selector.0123456789abcdef0123456789abcdef"
                staging.write_text("x", encoding="utf-8")
                staging.chmod(0o600)
                upgrade_authority._cleanup_selector_temporaries(parent, "selector")
                self.assertFalse(staging.exists())
                (root / "db-wal").mkdir()
                with self.assertRaises(AuthorityError):
                    upgrade_authority._sidecar_identities(parent, "db")
            finally:
                os.close(parent)

    def test_authority_identity_and_admission_validation_matrix(self) -> None:
        with self.assertRaises(AuthorityError):
            upgrade_authority.inspect_sqlite_release_authority(
                Path("/x"), Path("/y"), Path("/z"), Path("/r"), "", "bad value", "old"
            )
        from tools.admission_lease import AdmissionLease

        lease = AdmissionLease("p", "a", "f", "o", "b", 1)
        with self.assertRaises(AuthorityError):
            upgrade_authority.commit_runtime_selector_admitted(
                Path("/x"),
                "new",
                "old",
                cast(Any, object()),
                cast(Any, object()),
                cast(Any, object()),
            )
        with self.assertRaises(AuthorityError):
            upgrade_authority.commit_runtime_selector_admitted(
                Path("/x"), "new", "old", lease, cast(Any, object()), cast(Any, object())
            )

    def test_inspect_authority_git_error_and_dirty_paths(self) -> None:
        class Fake:
            ROOT = Path()

            def backend_selection(self) -> dict[str, str]:
                return {"backend": "git"}

            def project_binding(self) -> dict[str, str]:
                return {"project_id": "p", "state_repository": "s", "product_repository": "q"}

            def _assert_storage_binding(self, _binding: dict[str, str]) -> None:
                return None

        with (
            patch.object(upgrade_authority, "_handoffctl", return_value=Fake()),
            patch("subprocess.run", side_effect=OSError("no git")),
        ):
            with self.assertRaises(AuthorityError):
                upgrade_authority.inspect_authority()
            with (
                patch("subprocess.run", return_value=Namespace(stdout="dirty")),
                self.assertRaisesRegex(AuthorityError, "dirty"),
            ):
                upgrade_authority.inspect_authority()


class RollbackDefensiveMatrix(unittest.TestCase):
    def test_control_record_and_path_validation_matrix(self) -> None:
        for value in (-1, True, "1"):
            with self.assertRaises(ControlStoreError):
                _validate_expected_revision(value)
        with self.assertRaises(ControlStoreError):
            _validate({})
        with self.assertRaises(ControlStoreError):
            SQLiteRollbackControlStore._open_parent(Path("relative.db"))
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with self.assertRaises(ControlStoreError):
                SQLiteRollbackControlStore._open_parent(root / "missing" / "db")
            child = root / "child"
            child.mkdir()
            child.chmod(0o755)
        with self.assertRaises(ControlStoreError):
            SQLiteRollbackControlStore._open_parent(child / "db")

    def test_handoff_privacy_and_introduced_content_boundaries(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            secret = root / "secret.md"
            secret.write_text("token = sk-test-secret\n", encoding="utf-8")
            with (
                patch.object(handoffctl, "ROOT", root),
                patch.object(handoffctl, "generated_paths", return_value=[]),
            ):
                    errors = handoffctl.privacy_errors()
            self.assertTrue(errors)
            with patch.object(handoffctl, "ROOT", root):
                self.assertTrue(handoffctl.introduced_content_errors({secret: "old"}))
                secret.write_bytes(b"\xff\xfe")
                self.assertEqual([], handoffctl.privacy_errors())

    def test_handoff_claim_expiry_and_global_mutation_guards(self) -> None:
        for value in (None, "", "not-a-date", 1):
            with self.subTest(value=value):
                errors = handoffctl.active_expiry_errors("AR-X", value)
                self.assertTrue(errors)
        meta = {
            "id": "AR-X",
            "status": "in_progress",
            "owner": "o",
            "branch": "b",
            "worktree_key": "w",
            "claim_expires": "2999-01-01T00:00:00+00:00",
        }
        tasks = [(Path("a"), meta, ""), (Path("b"), {**meta, "id": "AR-Y"}, "")]
        errors = handoffctl.mutation_global_errors(tasks)
        self.assertTrue(any("active" in error for error in errors))

    def test_handoff_identity_graph_and_task_schema_fail_closed(self) -> None:
        base = {
            "id": "AR-0001",
            "status": "superseded",
            "superseded_by": "AR-0001",
            "owner": "",
            "claim_expires": "",
            "task_revision": 1,
            "priority": "P2",
            "title": "Title",
            "summary": "Summary",
            "next_action": "Action",
            "updated_at": "2026-01-01T00:00:00+00:00",
        }
        tasks = [(Path("a"), base, "")]
        self.assertFalse(handoffctl.dependency_satisfied("AR-0001", tasks))
        self.assertTrue(
            any("self reference" in error for error in handoffctl.supersession_errors(tasks))
        )
        self.assertTrue(handoffctl.field_errors(Path("a"), {"unexpected": True}))
        self.assertTrue(
            handoffctl.value_errors(
                Path("a"), {"id": "bad", "status": "bad", "priority": "bad", "task_revision": 0}
            )
        )
        self.assertTrue(
            handoffctl.reference_errors(
                Path("a"),
                {
                    "id": "AR-0001",
                    "updated_at": "bad",
                    "checkpoint_commit": "bad",
                    "plan": "missing.md",
                },
            )
        )

    def test_handoff_dependency_chain_variants(self) -> None:
        def task(
            task_id: str, status: str, successor: str | None = None
        ) -> tuple[Path, dict[str, Any], str]:
            meta: dict[str, Any] = {"id": task_id, "status": status}
            if successor is not None:
                meta["superseded_by"] = successor
            return (Path(task_id), meta, "")

        self.assertFalse(handoffctl.dependency_satisfied("AR-9999", []))
        self.assertFalse(
            handoffctl.dependency_satisfied("AR-0001", [task("AR-0001", "in_progress")])
        )
        self.assertFalse(
            handoffctl.dependency_satisfied("AR-0001", [task("AR-0001", "superseded", "bad")])
        )
        self.assertTrue(
            handoffctl.dependency_satisfied(
                "AR-0001", [task("AR-0001", "superseded", "AR-0002"), task("AR-0002", "done")]
            )
        )

    def _intent(self, **changes: object) -> AuthorityEffectIntent:
        values: dict[str, Any] = {
            "intent_id": "i",
            "operation_id": "o",
            "backend": "sqlite",
            "target": "rollback",
            "attempt_id": "a",
            "identity_digest": "d",
            "fencing_token": "fixture-fence",
            "session_revision": 1,
        }
        values.update(
            artifact_identity="artifact",
            manifest_identity="manifest",
            selector_identity="selector",
            runtime_identity="runtime",
        )
        values.update(changes)
        return AuthorityEffectIntent(**values)

    def test_effect_intent_all_scalar_and_admission_guards(self) -> None:
        for field in (
            "intent_id",
            "operation_id",
            "backend",
            "target",
            "attempt_id",
            "identity_digest",
            "fencing_token",
        ):
            with self.subTest(field=field), self.assertRaises(ControlStoreError):
                self._intent(**{field: ""})
        with self.assertRaises(ControlStoreError):
            self._intent(session_revision=0)
        with self.assertRaises(ControlStoreError):
            self._intent(artifact_identity=1)
        with self.assertRaises(ControlStoreError):
            self._intent(artifact_identity=None)

    def test_effect_receipt_attribute_protocol_is_checked(self) -> None:
        intent = self._intent()

        class Receipt:
            backend = "sqlite"
            target = "rollback"
            operation_id = "o"
            state_revision = 1
            artifact_identity = "artifact"
            manifest_identity = "manifest"
            selector_identity = "selector"
            runtime_identity = "runtime"
            fencing_token = "fixture-fence"  # noqa: S105
            mutates_authority = True

        _validate_authority_effect_receipt(intent, Receipt())

    def test_contract_transition_matrix_covers_terminal_and_evidence_guards(self) -> None:
        record = {
            "schema_version": 1,
            "project_id": "123e4567-e89b-42d3-a456-426614174000",
            "attempt_id": "a",
            "state_revision": 1,
            "authority_revision_at_acquire": "r",
            "durable_barrier_id": "b",
            "fencing_token": "f",
            "fencing_owner": "o",
            "identity_digest": "0" * 64,
        }
        record["identity_digest"] = canonical_barrier_session_digest(record)
        identity = BarrierSessionIdentity.from_record(record)
        contract = BarrierSessionContract(identity)
        forward = BarrierChildIdentity.bind(identity, "forward", "new")
        contract.bind_child(1, forward)
        with self.assertRaises(ControlStoreError):
            contract.bind_child(2, forward)
        with self.assertRaises(ControlStoreError):
            contract.begin_reopen(2, "new", {"operation_id": "wrong"})
        contract.begin_reopen(
            2,
            "new",
            {
                "operation_id": "forward",
                "target": "new",
                "barrier_identity_digest": identity.identity_digest,
                "validated": True,
            },
        )
        with self.assertRaises(ControlStoreError):
            contract.complete_reopen(3, {})
        with self.assertRaises(ControlStoreError):
            contract.mark_ambiguous(3, "bad code!")

    def test_adapter_delegation_and_bound_verifier_matrix(self) -> None:
        class Delegate:
            def snapshot(self, phase: str, context: dict[str, Any]) -> dict[str, Any]:
                return {"phase": phase, **context}

            def execute(self, phase: str, context: dict[str, Any]) -> dict[str, Any]:
                return {"executed": phase, **context}

            def verify_rollback_context_bound(
                self, context: dict[str, Any], scope: Any, *, lease: Any, admission_recheck: Any
            ) -> dict[str, Any]:
                return {
                    "context": context,
                    "scope": scope,
                    "lease": lease,
                    "recheck": admission_recheck,
                }

        adapter = object.__new__(
            __import__(
                "tools.rollback_control_store", fromlist=["SQLiteControlStoreAdapter"]
            ).SQLiteControlStoreAdapter
        )
        adapter._delegate = Delegate()
        adapter._observation_provider_token = object()
        self.assertEqual({"phase": "p", "x": 1}, adapter.snapshot("p", {"x": 1}))
        self.assertEqual({"executed": "p", "x": 1}, adapter.execute("p", {"x": 1}))
        self.assertEqual(
            "s",
            adapter.verify_rollback_context_bound({}, "s", lease="l", admission_recheck="r")[
                "scope"
            ],
        )


if __name__ == "__main__":
    unittest.main()
