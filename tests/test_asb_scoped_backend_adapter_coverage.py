# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""ASB-owned coverage for scoped backend adapter fail-closed boundaries."""

from __future__ import annotations

import unittest
from collections.abc import Iterator, Mapping
from contextlib import contextmanager
from typing import Any, cast
from unittest.mock import patch

from tools.admission_lease import AdmissionLease
from tools.lock_domain import LockDomainIdentity
from tools.rollback_control_store import BarrierSessionState
from tools.scoped_backend_adapter import ScopedBackendAdapter

IDENTITY = {
    "project_id": "asb",
    "authority_revision": "authority-7",
    "fencing_token": "fence-8",
    "fencing_owner": "worker-a",
    "durable_barrier_id": "barrier-9",
    "state_revision": 3,
}


class InMemoryScope:
    """Protocol-compatible scope that deliberately never acquires a lock."""

    def __init__(self) -> None:
        self.events: list[str] = []

    def assert_ordered(self) -> None:
        self.events.append("ordered")

    def assert_context(self, _context: Mapping[str, object]) -> None:
        self.events.append("context")

    @contextmanager
    def hold(self) -> Iterator[object]:
        self.events.append("held")
        try:
            yield object()
        finally:
            self.events.append("released")


class Backend:
    def __init__(
        self, *, snapshot: object = None, execute: object = None, rollback: object = None
    ) -> None:
        self.snapshot_result = {"evidence": "ok"} if snapshot is None else snapshot
        self.execute_result = {"mutates_authority": False} if execute is None else execute
        self.rollback_result = {"rollback": "verified"} if rollback is None else rollback
        self.calls: list[str] = []

    def snapshot(self, _phase: str, _context: Mapping[str, object]) -> dict[str, Any]:
        self.calls.append("snapshot")
        return cast(dict[str, Any], self.snapshot_result)

    def execute(self, _phase: str, _context: Mapping[str, object]) -> dict[str, Any]:
        self.calls.append("execute")
        return cast(dict[str, Any], self.execute_result)

    def verify_rollback_context(self, _context: Mapping[str, object]) -> dict[str, Any] | None:
        self.calls.append("rollback")
        return cast(dict[str, Any] | None, self.rollback_result)


class ScopedBackendAdapterAsbCoverageTests(unittest.TestCase):
    def test_validated_session_constructs_only_after_identity_binding(self) -> None:
        scope = InMemoryScope()
        identity = object.__new__(LockDomainIdentity)
        lease = AdmissionLease("asb", "authority-7", "fence-8", "worker-a", "barrier-9", 3)

        with (
            patch.object(LockDomainIdentity, "assert_descriptor_binding") as descriptor,
            patch.object(LockDomainIdentity, "assert_session_binding") as session,
        ):
            adapter = ScopedBackendAdapter.from_validated_session(
                Backend(),
                scope,
                identity,
                object(),
                cast(BarrierSessionState, object()),
                lease,
            )

        self.assertIsInstance(adapter, ScopedBackendAdapter)
        self.assertEqual(["ordered"], scope.events)
        descriptor.assert_called_once()
        session.assert_called_once()

    def test_snapshot_rejects_complete_context_without_all_admission_fields(self) -> None:
        scope = InMemoryScope()
        backend = Backend()
        adapter = ScopedBackendAdapter(backend, scope)

        for missing in IDENTITY:
            incomplete = dict(IDENTITY)
            incomplete.pop(missing)
            with (
                self.subTest(missing=missing),
                self.assertRaisesRegex(TypeError, "omits admission"),
            ):
                adapter.snapshot("inspect", incomplete, scope_context=IDENTITY)

        self.assertEqual([], scope.events)
        self.assertEqual([], backend.calls)

    def test_snapshot_rejects_projection_type_drift_before_scope_entry(self) -> None:
        scope = InMemoryScope()
        backend = Backend()
        adapter = ScopedBackendAdapter(backend, scope)
        full_context = {**IDENTITY, "backend": "git"}

        for field, wrong_value in (("state_revision", "3"), ("fencing_owner", 7)):
            drifted = dict(IDENTITY)
            drifted[field] = wrong_value
            with self.subTest(field=field), self.assertRaisesRegex(TypeError, "identity differs"):
                adapter.snapshot("inspect", full_context, scope_context=drifted)

        self.assertEqual([], scope.events)
        self.assertEqual([], backend.calls)

    def test_backend_result_shapes_are_rejected_after_scope_is_released(self) -> None:
        for operation, backend, message in (
            ("snapshot", Backend(snapshot=[]), "snapshot must be an object"),
            ("execute", Backend(execute={}), "must be non-mutating"),
            ("rollback", Backend(rollback="unsafe"), "object or null"),
        ):
            scope = InMemoryScope()
            adapter = ScopedBackendAdapter(backend, scope)
            with self.subTest(operation=operation), self.assertRaisesRegex(TypeError, message):
                if operation == "snapshot":
                    adapter.snapshot("inspect", {"backend": "git"})
                elif operation == "execute":
                    adapter.execute("inspect", {"backend": "git"})
                else:
                    adapter.verify_rollback_context({"backend": "git"})
            self.assertEqual(["context", "held", "released"], scope.events)
            self.assertEqual([operation], backend.calls)

    def test_disabled_phase_never_selects_backend_or_enters_scope(self) -> None:
        scope = InMemoryScope()
        backend = Backend()
        adapter = ScopedBackendAdapter(backend, scope)

        for phase in ("commit", "apply", "rollback"):
            with (
                self.subTest(phase=phase),
                self.assertRaisesRegex(TypeError, "mutation phase is disabled"),
            ):
                adapter.execute(phase, {"backend": "git"})

        self.assertEqual([], scope.events)
        self.assertEqual([], backend.calls)


if __name__ == "__main__":
    unittest.main()
