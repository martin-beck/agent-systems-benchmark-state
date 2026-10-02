# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

from __future__ import annotations

import copy
import json
import sqlite3
import tempfile
import unittest
import uuid
from contextlib import closing
from dataclasses import replace
from pathlib import Path, PurePosixPath
from typing import Any, cast
from unittest.mock import MagicMock, patch

from tools import upgrade_binding as binding_module
from tools.admission_lease import AdmissionLease, AdmissionRecheck
from tools.generate_upgrade_contract import generate
from tools.git_authority_adapter import GitAuthorityAdapter
from tools.handoffctl import locked
from tools.lock_domain_scope import LockDomainScope
from tools.mutation_fence import MutationFence, provision, provision_control_binding
from tools.rollback_control_store import (
    BarrierSessionState,
    SQLiteBarrierSessionStore,
    SQLiteRollbackControlStore,
)
from tools.sqlite_authority_adapter import SQLiteAuthorityAdapter
from tools.upgrade_binding import LiveUpgradeBinding, UpgradeBindingError, UpgradeRuntimeBinding
from tools.upgrade_commands import UpgradeCommandError, execute_upgrade_command
from tools.upgrade_identity import (
    BarrierChildIdentity,
    BarrierSessionIdentity,
    canonical_barrier_digest,
    canonical_barrier_session_digest,
    canonical_envelope_digest,
)


def _contract(backend: str = "sqlite", operation_id: str = "upgrade-001") -> dict[str, Any]:
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
            "operation_id": operation_id,
            "backend": backend,
            "selector_ref": ".runtime/runtime-selector.json",
            "expected_state_revision": 7,
            "barrier_id": "barrier-7",
            "fencing_token": "fence-7",
            "from": release("v0.3.5", "a"),
            "to": release("v0.3.6", "b"),
        }
    )


def _envelope(contract: dict[str, Any]) -> dict[str, object]:
    root = PurePosixPath("/srv/runtime/artifacts")
    value: dict[str, object] = {
        "schema_version": 2,
        "backend": contract["backend"],
        "project_id": str(uuid.uuid4()),
        "operation_id": contract["operation_id"],
        "state_revision": 7,
        "authority_revision": "authority-7",
        "fencing_token": "fence-7",
        "fencing_owner": "worker-7",
        "durable_barrier_id": "barrier-7",
        "artifact_root": str(root),
        "source": str(root / "source"),
        "destination": str(root / "destination"),
        "manifest": str(root / "manifest.json"),
        "selector_ref": ".runtime/runtime-selector.json",
        "target": "rollback",
    }
    value["barrier_identity_digest"] = canonical_barrier_digest(value)
    value["envelope_digest"] = canonical_envelope_digest(value)
    return value


class UpgradeBindingTests(unittest.TestCase):
    def test_binding_carries_and_validates_contract_and_runtime_identities(self) -> None:
        contract = _contract()
        binding = UpgradeRuntimeBinding.bind(
            contract, _envelope(contract), session_identity_digest="a" * 64
        )
        self.assertEqual(contract["operation_id"], binding.contract_operation_id)
        self.assertEqual("barrier-7", binding.contract_barrier_id)
        self.assertEqual(
            set(binding.as_mapping()),
            {
                "schema_version",
                "contract_digest",
                "session_identity_digest",
                "contract_operation_id",
                "contract_backend",
                "contract_selector_ref",
                "contract_expected_state_revision",
                "contract_barrier_id",
                "contract_fencing_token",
                "contract_backup_operation_id",
                "runtime_envelope",
            },
        )
        restored = UpgradeRuntimeBinding.from_mapping(binding.as_mapping())
        self.assertEqual(binding, restored)

    def test_rejects_host_identity_drift(self) -> None:
        contract = _contract()
        for field, value in (
            ("operation_id", "other-operation"),
            ("backend", "git"),
            ("selector_ref", "other-selector.json"),
            ("expected_state_revision", 8),
            ("barrier_id", "other-barrier"),
            ("fencing_token", "other-fence"),
        ):
            changed = copy.deepcopy(contract)
            if field in {
                "operation_id",
                "backend",
                "selector_ref",
                "expected_state_revision",
                "barrier_id",
                "fencing_token",
            }:
                changed["rollback"]["operation"]["inputs"][field] = value
                for phase in changed["phases"]:
                    phase["operation"]["inputs"][field] = value
                if field == "operation_id":
                    changed["operation_id"] = value
            with self.subTest(field=field), self.assertRaises(UpgradeBindingError):
                UpgradeRuntimeBinding.bind(
                    changed, _envelope(contract), session_identity_digest="a" * 64
                )

    def test_rejects_runtime_identity_drift_and_unknown_binding_fields(self) -> None:
        contract = _contract()
        runtime = _envelope(contract)
        for field, value in (("fencing_token", "foreign-fence"), ("target", "new")):
            changed = dict(runtime)
            changed[field] = value
            changed["barrier_identity_digest"] = canonical_barrier_digest(changed)
            changed["envelope_digest"] = canonical_envelope_digest(changed)
            with self.subTest(field=field), self.assertRaises(UpgradeBindingError):
                UpgradeRuntimeBinding.bind(contract, changed, session_identity_digest="a" * 64)
        foreign = _envelope(contract)
        foreign["project_id"] = str(uuid.uuid4())
        foreign["barrier_identity_digest"] = canonical_barrier_digest(foreign)
        foreign["envelope_digest"] = canonical_envelope_digest(foreign)
        self.assertNotEqual(
            UpgradeRuntimeBinding.bind(contract, runtime, session_identity_digest="a" * 64),
            UpgradeRuntimeBinding.bind(contract, foreign, session_identity_digest="a" * 64),
        )
        binding = UpgradeRuntimeBinding.bind(
            contract, runtime, session_identity_digest="a" * 64
        ).as_mapping()
        binding["unexpected"] = True
        with self.assertRaises(UpgradeBindingError):
            UpgradeRuntimeBinding.from_mapping(binding)

    def test_validates_observed_held_rollback_session(self) -> None:
        contract = _contract()
        runtime = _envelope(contract)
        session_record: dict[str, object] = {
            "schema_version": 1,
            "project_id": runtime["project_id"],
            "attempt_id": "attempt-7",
            "state_revision": runtime["state_revision"],
            "authority_revision_at_acquire": runtime["authority_revision"],
            "durable_barrier_id": runtime["durable_barrier_id"],
            "fencing_token": runtime["fencing_token"],
            "fencing_owner": runtime["fencing_owner"],
        }
        session_record["identity_digest"] = canonical_barrier_session_digest(session_record)
        identity = BarrierSessionIdentity.from_record(session_record)
        child = BarrierChildIdentity.bind(identity, str(runtime["operation_id"]), "rollback")
        session = BarrierSessionState(identity, "held", 2, rollback_child=child)
        binding = UpgradeRuntimeBinding.bind(
            contract,
            runtime,
            session_identity_digest=identity.identity_digest,
        )
        binding.validate_live_session(session)
        with self.assertRaisesRegex(UpgradeBindingError, "session identity digest"):
            foreign_record = {**session_record, "attempt_id": "attempt-other"}
            foreign_record["identity_digest"] = canonical_barrier_session_digest(foreign_record)
            foreign_identity = BarrierSessionIdentity.from_record(foreign_record)
            binding.validate_live_session(
                BarrierSessionState(
                    foreign_identity,
                    "held",
                    2,
                    rollback_child=BarrierChildIdentity.bind(
                        foreign_identity, str(runtime["operation_id"]), "rollback"
                    ),
                )
            )

    def test_binds_live_session_scope_and_backend_without_authorizing_mutation(self) -> None:
        contract = _contract("git")
        runtime = _envelope(contract)
        session_record: dict[str, object] = {
            "schema_version": 1,
            "project_id": runtime["project_id"],
            "attempt_id": "attempt-7",
            "state_revision": runtime["state_revision"],
            "authority_revision_at_acquire": runtime["authority_revision"],
            "durable_barrier_id": runtime["durable_barrier_id"],
            "fencing_token": runtime["fencing_token"],
            "fencing_owner": runtime["fencing_owner"],
        }
        session_record["identity_digest"] = canonical_barrier_session_digest(session_record)
        identity = BarrierSessionIdentity.from_record(session_record)
        binding = UpgradeRuntimeBinding.bind(
            contract, runtime, session_identity_digest=identity.identity_digest
        )
        child = BarrierChildIdentity.bind(identity, str(runtime["operation_id"]), "rollback")
        session = BarrierSessionState(identity, "held", 2, rollback_child=child)
        lease = AdmissionLease(
            project_id=str(runtime["project_id"]),
            authority_revision=str(runtime["authority_revision"]),
            fencing_token=str(runtime["fencing_token"]),
            fencing_owner=str(runtime["fencing_owner"]),
            durable_barrier_id=str(runtime["durable_barrier_id"]),
            revision=cast(int, runtime["state_revision"]),
        )
        recheck = AdmissionRecheck(
            lease=lease,
            project_id=lease.project_id,
            authority_revision=lease.authority_revision,
            fencing_token=lease.fencing_token,
            fencing_owner=lease.fencing_owner,
            durable_barrier_id=lease.durable_barrier_id,
            revision=lease.revision,
        )
        scope = object.__new__(LockDomainScope)
        scope._session_identity = identity
        scope._session_revision = session.revision
        scope._lease = lease
        store = MagicMock()
        store.authority_path = None
        scope._session_store = store
        adapter = object.__new__(GitAuthorityAdapter)
        with self.assertRaises(UpgradeBindingError):
            LiveUpgradeBinding.bind(
                binding,
                session,
                scope,
                replace(lease, fencing_token="foreign"),  # noqa: S106
                recheck,
                adapter,
            )
        with self.assertRaises(UpgradeBindingError):
            LiveUpgradeBinding.bind(
                binding, replace(session, status="released"), scope, lease, recheck, adapter
            )
        with self.assertRaises(TypeError):
            LiveUpgradeBinding()

    def test_rejects_nonconcrete_live_binding_components(self) -> None:
        contract = _contract("sqlite")
        runtime = _envelope(contract)
        binding = UpgradeRuntimeBinding.bind(contract, runtime, session_identity_digest="a" * 64)
        with self.assertRaisesRegex(UpgradeBindingError, "runtime upgrade binding"):
            LiveUpgradeBinding.bind(
                cast(Any, object()), object(), object(), object(), object(), object()
            )
        with self.assertRaisesRegex(UpgradeBindingError, "live barrier session"):
            LiveUpgradeBinding.bind(binding, object(), object(), object(), object(), object())
        session = object.__new__(BarrierSessionState)
        with self.assertRaisesRegex(UpgradeBindingError, "lock-domain scope"):
            LiveUpgradeBinding.bind(binding, session, object(), object(), object(), object())
        scope = object.__new__(LockDomainScope)
        with self.assertRaisesRegex(UpgradeBindingError, "admission lease"):
            LiveUpgradeBinding.bind(binding, session, scope, object(), object(), object())
        lease = object.__new__(AdmissionLease)
        with self.assertRaisesRegex(UpgradeBindingError, "admission recheck"):
            LiveUpgradeBinding.bind(binding, session, scope, lease, object(), object())

    def test_rejects_unverified_backend_evidence(self) -> None:
        contract = _contract("sqlite")
        runtime = _envelope(contract)
        binding = UpgradeRuntimeBinding.bind(contract, runtime, session_identity_digest="a" * 64)
        evidence = {
            **runtime,
            "phase": "rollback",
            "backend_identity_verified": False,
            "mutates_authority": False,
            "sqlite_integrity_verified": True,
            "sqlite_foreign_keys_verified": True,
        }
        with self.assertRaisesRegex(UpgradeBindingError, "not verified"):
            binding.validate_backend_evidence(evidence)

    def test_binds_real_sqlite_session_scope_and_adapter(self) -> None:
        contract = _contract()
        runtime = _envelope(contract)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            root.chmod(0o700)
            authority = root / "authority.sqlite"
            with closing(sqlite3.connect(authority)) as connection, connection:
                connection.execute("CREATE TABLE records (id INTEGER PRIMARY KEY, body TEXT)")
                connection.execute("INSERT INTO records(body) VALUES ('clean')")
            authority.chmod(0o600)
            control_path = root / "control.sqlite"
            store = SQLiteRollbackControlStore(control_path, str(runtime["project_id"]), authority)
            marker = root / "authority-marker.json"
            lifecycle = root / "authority-lifecycle.json"
            authority_lock = root / "authority.lock"
            control_binding = root / "control-binding.json"
            provision(authority, marker, lifecycle, authority_lock, str(runtime["project_id"]))
            provision_control_binding(
                control_path,
                control_binding,
                store.control_lock_path,
                str(runtime["project_id"]),
            )
            fence = MutationFence(
                authority,
                marker,
                lifecycle,
                authority_lock,
                control_path,
                control_binding,
                store.control_lock_path,
            )
            session_record: dict[str, object] = {
                "schema_version": 1,
                "project_id": runtime["project_id"],
                "attempt_id": "attempt-7",
                "state_revision": runtime["state_revision"],
                "authority_revision_at_acquire": runtime["authority_revision"],
                "durable_barrier_id": runtime["durable_barrier_id"],
                "fencing_token": runtime["fencing_token"],
                "fencing_owner": runtime["fencing_owner"],
            }
            session_record["identity_digest"] = canonical_barrier_session_digest(session_record)
            identity = BarrierSessionIdentity.from_record(session_record)
            forward_child = BarrierChildIdentity.bind(
                identity, f"{runtime['operation_id']}:forward", "new"
            )
            child = BarrierChildIdentity.bind(identity, str(runtime["operation_id"]), "rollback")
            session = SQLiteBarrierSessionStore(store, lambda: str(runtime["authority_revision"]))
            session.create(identity)
            session.bind_child(1, forward_child)
            session.bind_child(2, child)
            lease = AdmissionLease(
                project_id=str(runtime["project_id"]),
                authority_revision=str(runtime["authority_revision"]),
                fencing_token=str(runtime["fencing_token"]),
                fencing_owner=str(runtime["fencing_owner"]),
                durable_barrier_id=str(runtime["durable_barrier_id"]),
                revision=cast(int, runtime["state_revision"]),
            )
            recheck = AdmissionRecheck(
                lease=lease,
                project_id=lease.project_id,
                authority_revision=lease.authority_revision,
                fencing_token=lease.fencing_token,
                fencing_owner=lease.fencing_owner,
                durable_barrier_id=lease.durable_barrier_id,
                revision=lease.revision,
            )
            scope = LockDomainScope.bind(session, fence, lease, recheck, locked)
            adapter = SQLiteAuthorityAdapter(authority)
            binding = UpgradeRuntimeBinding.bind(
                contract, runtime, session_identity_digest=identity.identity_digest
            )
            live = LiveUpgradeBinding.bind(
                binding, session.snapshot(), scope, lease, recheck, adapter
            )
            foreign_lease = replace(lease, revision=99)
            foreign_recheck = replace(recheck, lease=foreign_lease, revision=99)
            with self.assertRaisesRegex(UpgradeBindingError, "lease identity"):
                LiveUpgradeBinding.bind(
                    binding,
                    session.snapshot(),
                    scope,
                    foreign_lease,
                    foreign_recheck,
                    adapter,
                )
            with (
                patch.object(scope, "assert_context", side_effect=RuntimeError("drift")),
                self.assertRaisesRegex(UpgradeBindingError, "scope identity"),
            ):
                LiveUpgradeBinding.bind(binding, session.snapshot(), scope, lease, recheck, adapter)
            original_identity = scope._session_identity
            scope._session_identity = replace(original_identity, attempt_id="foreign")
            with self.assertRaisesRegex(UpgradeBindingError, "session identity"):
                LiveUpgradeBinding.bind(binding, session.snapshot(), scope, lease, recheck, adapter)
            scope._session_identity = original_identity
            original_revision = scope._session_revision
            scope._session_revision = original_revision + 1
            with self.assertRaisesRegex(UpgradeBindingError, "session revision"):
                LiveUpgradeBinding.bind(binding, session.snapshot(), scope, lease, recheck, adapter)
            scope._session_revision = original_revision
            original_scope_lease = scope._lease
            scope._lease = replace(lease, fencing_token="foreign")  # noqa: S106
            with (
                patch.object(scope, "assert_context", return_value=None),
                self.assertRaisesRegex(UpgradeBindingError, "scope lease"),
            ):
                LiveUpgradeBinding.bind(binding, session.snapshot(), scope, lease, recheck, adapter)
            scope._lease = original_scope_lease
            evidence = live.reread_backend()
            self.assertTrue(live.matches_runtime(binding))
            self.assertFalse(live.matches_runtime(cast(Any, object())))
            self.assertTrue(live.matches_contract(contract, "sqlite"))
            self.assertFalse(live.matches_contract({}, "sqlite"))
            original_token = live._token
            object.__setattr__(live, "_token", object())
            self.assertFalse(live.is_admitted())
            object.__setattr__(live, "_token", original_token)
            original_store = scope._session_store
            scope._session_store = cast(Any, object())
            with self.assertRaisesRegex(UpgradeBindingError, "concrete session store"):
                LiveUpgradeBinding.bind(binding, session.snapshot(), scope, lease, recheck, adapter)
            scope._session_store = original_store
            with self.assertRaisesRegex(UpgradeBindingError, "Git repository identity"):
                LiveUpgradeBinding.bind(
                    binding,
                    session.snapshot(),
                    scope,
                    lease,
                    recheck,
                    adapter,
                    expected_git_repository=Path("/foreign"),
                )
            foreign_authority = root / "foreign.sqlite"
            with sqlite3.connect(foreign_authority):
                pass
            foreign_authority.chmod(0o600)
            foreign_adapter = SQLiteAuthorityAdapter(foreign_authority)
            with self.assertRaisesRegex(UpgradeBindingError, "foreign authority"):
                LiveUpgradeBinding.bind(
                    binding, session.snapshot(), scope, lease, recheck, foreign_adapter
                )
            adapter_any: Any = adapter
            original_snapshot_bound = adapter_any.snapshot_bound
            adapter_any.snapshot_bound = MagicMock(side_effect=RuntimeError("stale"))
            with self.assertRaisesRegex(UpgradeBindingError, "reread was rejected"):
                binding.reread_backend_bound(adapter, scope, lease, recheck)
            adapter_any.snapshot_bound = MagicMock(return_value=[])
            with self.assertRaisesRegex(UpgradeBindingError, "invalid evidence"):
                binding.reread_backend_bound(adapter, scope, lease, recheck)
            adapter_any.snapshot_bound = original_snapshot_bound
            self.assertTrue(evidence["sqlite_integrity_verified"])
            self.assertFalse(evidence["mutates_authority"])
            self.assertFalse(session.operation_owned_by_current_thread)
            contract_path = root / "contract.json"
            contract_path.write_text(json.dumps(contract), encoding="utf-8")
            with self.assertRaisesRegex(UpgradeCommandError, "execution protocol is incomplete"):
                execute_upgrade_command("apply", contract_path, "sqlite", live_binding=live)
            binding_path = root / "binding.json"
            binding_path.write_text(json.dumps(binding.as_mapping()), encoding="utf-8")
            with self.assertRaisesRegex(UpgradeCommandError, "execution protocol is incomplete"):
                execute_upgrade_command("rollback", contract_path, "sqlite", binding_path, live)
            foreign_contract = _contract(operation_id="foreign-operation")
            foreign_path = root / "foreign-contract.json"
            foreign_path.write_text(json.dumps(foreign_contract), encoding="utf-8")
            with self.assertRaisesRegex(UpgradeCommandError, "does not match the contract"):
                execute_upgrade_command("apply", foreign_path, "sqlite", live_binding=live)
            self.assertTrue(live.is_admitted())
            forged = object.__new__(LiveUpgradeBinding)
            for field in (
                "runtime",
                "session",
                "scope",
                "lease",
                "admission_recheck",
                "adapter",
                "_token",
                "expected_branch",
                "expected_head",
                "expected_git_repository",
            ):
                object.__setattr__(forged, field, getattr(live, field))
            object.__setattr__(forged, "adapter", object.__new__(SQLiteAuthorityAdapter))
            self.assertFalse(forged.is_admitted())
            session.begin_reopen(
                3,
                "rollback",
                {
                    "operation_id": str(runtime["operation_id"]),
                    "target": "rollback",
                    "barrier_identity_digest": identity.identity_digest,
                    "validated": True,
                },
            )
            self.assertFalse(live.is_admitted())
            session.complete_reopen(
                4,
                {
                    "authority_revision": str(runtime["authority_revision"]),
                    "backend": "sqlite",
                    "backend_roundtrip": "sqlite",
                    "foreign_key_violations": 0,
                    "fencing_token": str(runtime["fencing_token"]),
                    "integrity_check": "ok",
                    "project_id": str(runtime["project_id"]),
                    "target": "rollback",
                    "verified": True,
                },
            )
            self.assertFalse(live.is_admitted())

    def test_rejects_malformed_binding_records(self) -> None:
        contract = _contract()
        binding = UpgradeRuntimeBinding.bind(
            contract, _envelope(contract), session_identity_digest="a" * 64
        ).as_mapping()
        mutations: list[dict[str, object]] = []
        mutations.append({key: value for key, value in binding.items() if key != "schema_version"})
        mutations.append({**binding, "schema_version": 2})
        mutations.append({**binding, "runtime_envelope": {}})
        mutations.extend(
            {
                **binding,
                field: "",
            }
            for field in (
                "contract_digest",
                "session_identity_digest",
                "contract_operation_id",
                "contract_backend",
                "contract_selector_ref",
                "contract_barrier_id",
                "contract_fencing_token",
                "contract_backup_operation_id",
            )
        )
        mutations.extend(
            [
                {**binding, "contract_digest": "x" * 64},
                {**binding, "session_identity_digest": "x" * 64},
                {**binding, "contract_expected_state_revision": 0},
            ]
        )
        for value in mutations:
            with self.subTest(value=value), self.assertRaises(UpgradeBindingError):
                UpgradeRuntimeBinding.from_mapping(value)

    def test_rejects_inconsistent_persisted_binding_identity(self) -> None:
        contract = _contract()
        runtime = _envelope(contract)
        binding = UpgradeRuntimeBinding.bind(
            contract, runtime, session_identity_digest="a" * 64
        ).as_mapping()
        for field, value in (
            ("contract_backend", "git"),
            ("contract_expected_state_revision", 99),
            ("contract_selector_ref", "foreign-selector.json"),
            ("contract_barrier_id", "foreign-barrier"),
            ("contract_fencing_token", "foreign-fence"),
            ("contract_operation_id", "foreign-operation"),
        ):
            changed = dict(binding)
            changed[field] = value
            with self.subTest(field=field), self.assertRaises(UpgradeBindingError):
                UpgradeRuntimeBinding.from_mapping(changed)

    def test_rejects_live_session_status_and_identity_drift(self) -> None:
        contract = _contract()
        runtime = _envelope(contract)
        record: dict[str, object] = {
            "schema_version": 1,
            "project_id": runtime["project_id"],
            "attempt_id": "attempt-7",
            "state_revision": runtime["state_revision"],
            "authority_revision_at_acquire": runtime["authority_revision"],
            "durable_barrier_id": runtime["durable_barrier_id"],
            "fencing_token": runtime["fencing_token"],
            "fencing_owner": runtime["fencing_owner"],
        }
        record["identity_digest"] = canonical_barrier_session_digest(record)
        identity = BarrierSessionIdentity.from_record(record)
        binding = UpgradeRuntimeBinding.bind(
            contract, runtime, session_identity_digest=identity.identity_digest
        )
        child = BarrierChildIdentity.bind(identity, str(runtime["operation_id"]), "rollback")
        cases = [
            BarrierSessionState(identity, "releasing", 2, rollback_child=child),
            BarrierSessionState(identity, "held", 2),
            BarrierSessionState(
                identity,
                "held",
                2,
                rollback_child=BarrierChildIdentity(
                    str(runtime["operation_id"]), "new", identity.identity_digest
                ),
            ),
        ]
        for case in cases:
            with self.assertRaises(UpgradeBindingError):
                binding.validate_live_session(case)
        with self.assertRaises(UpgradeBindingError):
            binding.validate_live_session(object())
        for field, value in (
            ("project_id", str(uuid.uuid4())),
            ("state_revision", 8),
            ("authority_revision_at_acquire", "other-authority"),
            ("durable_barrier_id", "other-barrier"),
            ("fencing_token", "other-fence"),
        ):
            changed = {**record, field: value}
            changed["identity_digest"] = canonical_barrier_session_digest(changed)
            changed_identity = BarrierSessionIdentity.from_record(changed)
            changed_identity = replace(changed_identity, identity_digest=identity.identity_digest)
            changed_child = BarrierChildIdentity.bind(
                changed_identity, str(runtime["operation_id"]), "rollback"
            )
            with self.subTest(field=field), self.assertRaises(UpgradeBindingError):
                binding.validate_live_session(
                    BarrierSessionState(changed_identity, "held", 2, rollback_child=changed_child)
                )

    def test_covers_strict_binding_defensive_boundaries(self) -> None:
        contract = _contract()
        with self.assertRaises(UpgradeBindingError):
            binding_module.canonical_contract_digest({"value": object()})
        with self.assertRaises(UpgradeBindingError):
            binding_module._contract_inputs({"rollback": {"operation": {"inputs": []}}})
        with self.assertRaises(UpgradeBindingError):
            binding_module._validated_envelope({})

        inputs = {
            "backend": "sqlite",
            "selector_ref": ".runtime/runtime-selector.json",
            "expected_state_revision": 7,
            "barrier_id": "barrier-7",
            "fencing_token": "fence-7",
            "backup_operation_id": "op:backup",
            "target": "rollback",
        }
        value: dict[str, Any] = {
            "operation_id": "op",
            "backend": "sqlite",
            "rollback": {"operation": {"operation_id": "op:rollback", "inputs": inputs}},
            "phases": [{"operation": {"inputs": dict(inputs)}}],
        }
        with patch.object(
            binding_module, "validate_runtime_contract", side_effect=lambda candidate: candidate
        ):
            for mutation in (
                {**inputs, "unexpected": True},
                {**inputs, "selector_ref": "other"},
                {**inputs, "target": "new"},
            ):
                changed = copy.deepcopy(value)
                changed["rollback"]["operation"]["inputs"] = mutation
                with self.assertRaises(UpgradeBindingError):
                    binding_module._validate_contract_identity(changed)
            changed = copy.deepcopy(value)
            changed["phases"][0]["operation"]["inputs"]["barrier_id"] = "other"
            with self.assertRaises(UpgradeBindingError):
                binding_module._validate_contract_identity(changed)
            changed = copy.deepcopy(value)
            changed["backend"] = "git"
            with self.assertRaises(UpgradeBindingError):
                binding_module._validate_contract_identity(changed)
            changed = copy.deepcopy(value)
            changed["rollback"]["operation"]["inputs"]["backup_operation_id"] = "other"
            with self.assertRaises(UpgradeBindingError):
                binding_module._validate_contract_identity(changed)
            changed = copy.deepcopy(value)
            changed["rollback"]["operation"]["operation_id"] = "other"
            with self.assertRaises(UpgradeBindingError):
                binding_module._validate_contract_identity(changed)

        with self.assertRaises(UpgradeBindingError):
            UpgradeRuntimeBinding.bind(contract, _envelope(contract), session_identity_digest="bad")
        UpgradeRuntimeBinding.bind(contract, _envelope(contract), session_identity_digest="a" * 64)
        runtime = _envelope(contract)
        runtime["operation_id"] = "other"
        runtime["barrier_identity_digest"] = canonical_barrier_digest(runtime)
        runtime["envelope_digest"] = canonical_envelope_digest(runtime)
        with self.assertRaises(UpgradeBindingError):
            UpgradeRuntimeBinding.bind(contract, runtime, session_identity_digest="a" * 64)

    def test_validates_git_and_sqlite_read_only_backend_evidence(self) -> None:
        for backend in ("git", "sqlite"):
            contract = _contract(backend)
            runtime = _envelope(contract)
            binding = UpgradeRuntimeBinding.bind(
                contract, runtime, session_identity_digest="a" * 64
            )
            evidence = {
                **runtime,
                "phase": "rollback",
                "backend_identity_verified": True,
                "mutates_authority": False,
                **(
                    {
                        "git_head": "a" * 40,
                        "git_branch": "main",
                        "git_clean": True,
                    }
                    if backend == "git"
                    else {
                        "sqlite_integrity_verified": True,
                        "sqlite_foreign_keys_verified": True,
                    }
                ),
            }
            self.assertEqual(evidence, binding.validate_backend_evidence(evidence))
            adapter = (
                object.__new__(GitAuthorityAdapter)
                if backend == "git"
                else object.__new__(SQLiteAuthorityAdapter)
            )
            scope = object.__new__(LockDomainScope)
            lease = AdmissionLease(
                project_id=str(runtime["project_id"]),
                authority_revision=str(runtime["authority_revision"]),
                fencing_token=str(runtime["fencing_token"]),
                fencing_owner=str(runtime["fencing_owner"]),
                durable_barrier_id=str(runtime["durable_barrier_id"]),
                revision=cast(int, runtime["state_revision"]),
            )
            recheck = AdmissionRecheck(
                lease=lease,
                project_id=lease.project_id,
                authority_revision=lease.authority_revision,
                fencing_token=lease.fencing_token,
                fencing_owner=lease.fencing_owner,
                durable_barrier_id=lease.durable_barrier_id,
                revision=lease.revision,
            )
            foreign_lease = replace(lease, fencing_token="foreign-fence")  # noqa: S106
            foreign_recheck = AdmissionRecheck(
                lease=foreign_lease,
                project_id=foreign_lease.project_id,
                authority_revision=foreign_lease.authority_revision,
                fencing_token=foreign_lease.fencing_token,
                fencing_owner=foreign_lease.fencing_owner,
                durable_barrier_id=foreign_lease.durable_barrier_id,
                revision=foreign_lease.revision,
            )
            adapter_any: Any = adapter
            adapter_any.snapshot_bound = MagicMock(return_value=evidence)
            with self.assertRaises(UpgradeBindingError):
                binding.reread_backend_bound(adapter, object(), lease, recheck)
            with self.assertRaises(UpgradeBindingError):
                binding.reread_backend_bound(adapter, scope, object(), recheck)
            with self.assertRaises(UpgradeBindingError):
                binding.reread_backend_bound(adapter, scope, lease, object())
            with self.assertRaises(UpgradeBindingError):
                binding.reread_backend_bound(adapter, scope, lease, foreign_recheck)
            if backend == "git":
                self.assertEqual(
                    evidence,
                    binding.reread_backend_bound(
                        adapter,
                        scope,
                        lease,
                        recheck,
                        expected_branch="main",
                        expected_head="a" * 40,
                    ),
                )
                adapter_any.snapshot_bound.assert_called_once()
            else:
                self.assertEqual(
                    evidence,
                    binding.reread_backend_bound(adapter, scope, lease, recheck),
                )
                adapter_any.snapshot_bound.assert_called_once()
            for field, value in (
                ("operation_id", "foreign-operation"),
                ("mutates_authority", True),
                ("phase", "validate"),
            ):
                changed = {**evidence, field: value}
                with (
                    self.subTest(backend=backend, field=field),
                    self.assertRaises(UpgradeBindingError),
                ):
                    binding.validate_backend_evidence(changed)
            with self.assertRaises(UpgradeBindingError):
                binding.validate_backend_evidence({**evidence, "unexpected": True})

            with self.assertRaises(UpgradeBindingError):
                binding.validate_backend_evidence([])  # type: ignore[arg-type]
            invalid_evidence = {**evidence}
            if backend == "git":
                invalid_evidence["git_head"] = ""
            else:
                invalid_evidence["sqlite_integrity_verified"] = False
            with self.assertRaises(UpgradeBindingError):
                binding.validate_backend_evidence(invalid_evidence)
            concrete = (
                object.__new__(GitAuthorityAdapter)
                if backend == "git"
                else object.__new__(SQLiteAuthorityAdapter)
            )
            concrete_any: Any = concrete
            concrete_any.snapshot_bound = MagicMock(side_effect=RuntimeError("stale"))
            if backend == "git":
                with self.assertRaises(UpgradeBindingError):
                    binding.reread_backend_bound(
                        concrete,
                        scope,
                        lease,
                        recheck,
                        expected_branch="main",
                        expected_head="a" * 40,
                    )
                with self.assertRaises(UpgradeBindingError):
                    binding.reread_backend_bound(
                        concrete,
                        object(),
                        object(),
                        object(),
                        expected_branch="",
                        expected_head="a" * 40,
                    )
                with self.assertRaises(UpgradeBindingError):
                    binding.reread_backend_bound(
                        concrete,
                        object(),
                        object(),
                        object(),
                        expected_branch="main",
                        expected_head="",
                    )
                with self.assertRaises(UpgradeBindingError):
                    binding.reread_backend_bound(
                        object(),
                        object(),
                        object(),
                        object(),
                        expected_branch="main",
                        expected_head="a" * 40,
                    )
            else:
                with self.assertRaises(UpgradeBindingError):
                    binding.reread_backend_bound(concrete, object(), object(), object())
                with self.assertRaises(UpgradeBindingError):
                    binding.reread_backend_bound(object(), object(), object(), object())

        sqlite_binding = UpgradeRuntimeBinding.bind(
            _contract("sqlite"), _envelope(_contract("sqlite")), session_identity_digest="a" * 64
        )
        with self.assertRaises(UpgradeBindingError):
            sqlite_binding.reread_backend_bound(object(), object(), object(), object())
        runtime = _envelope(contract)
        runtime["backend"] = "git"
        runtime["barrier_identity_digest"] = canonical_barrier_digest(runtime)
        runtime["envelope_digest"] = canonical_envelope_digest(runtime)
        with self.assertRaises(UpgradeBindingError):
            UpgradeRuntimeBinding.bind(contract, runtime, session_identity_digest="a" * 64)
