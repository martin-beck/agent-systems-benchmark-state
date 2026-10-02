# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Tests for the uncalled fail-closed control-store admission wrapper."""

from __future__ import annotations

import unittest
from collections.abc import Iterator, Mapping
from contextlib import contextmanager
from typing import Any

from tools.admission_lease import AdmissionLease, AdmissionLeaseError, validate_recheck
from tools.admitted_control_store import AdmittedControlBinding, admitted_cas


class AdmittedControlStoreTests(unittest.TestCase):
    def setUp(self) -> None:
        self.lease = AdmissionLease(
            "project",
            "authority-1",
            "fence-1",
            "owner-1",
            "barrier-1",
            1,
        )
        self.recheck = validate_recheck(
            self.lease,
            project_id="project",
            authority_revision="authority-1",
            fencing_token="fence-1",  # noqa: S106
            fencing_owner="owner-1",
            durable_barrier_id="barrier-1",
            revision=1,
        )
        self.record = {
            "project_id": "project",
            "authority_revision": "authority-1",
            "fencing_token": "fence-1",
            "fencing_owner": "owner-1",
            "durable_barrier_id": "barrier-1",
            "status": "held",
        }

    def test_valid_write_checks_order_before_holding_and_calls_store(self) -> None:
        events: list[str] = []

        class Scope:
            def assert_ordered(self) -> None:
                events.append("order")

            @contextmanager
            def hold(self) -> Any:
                events.append("hold")
                yield None
                events.append("release")

        class Store:
            def cas(
                self, expected_revision: int, record: Mapping[str, object]
            ) -> dict[str, object]:
                events.append("write")
                return {"revision": expected_revision + 1, **record}

        result = admitted_cas(Store(), 1, self.record, self.lease, self.recheck, Scope())
        self.assertEqual(2, result["revision"])
        self.assertEqual(["order", "hold", "write", "release"], events)

    def test_typed_binding_validates_before_adapter_construction(self) -> None:
        class Store:
            def cas(self, _expected: int, _record: Mapping[str, object]) -> dict[str, object]:
                return {"revision": 2}

        class Scope:
            def assert_ordered(self) -> None: ...

            def hold(self) -> Any: ...

        binding = AdmittedControlBinding.bind(Store(), self.lease, self.recheck, Scope())
        self.assertIs(self.lease, binding.lease)
        self.assertIs(self.recheck, binding.recheck)

    def test_typed_binding_rejects_missing_backend_capability(self) -> None:
        class Scope:
            def assert_ordered(self) -> None: ...

            def hold(self) -> Any: ...

        with self.assertRaisesRegex(AdmissionLeaseError, "store is required"):
            AdmittedControlBinding.bind(object(), self.lease, self.recheck, Scope())  # type: ignore[arg-type]

    def test_typed_binding_validate_is_backend_free(self) -> None:
        class Store:
            def cas(self, *_args: object, **_kwargs: object) -> dict[str, object]:
                raise AssertionError("backend must not be touched")

        class Scope:
            def assert_ordered(self) -> None: ...

            def hold(self) -> Any: ...

        binding = AdmittedControlBinding.bind(Store(), self.lease, self.recheck, Scope())
        binding.validate()

    def test_validated_scope_rereads_and_cleans_up_without_backend(self) -> None:
        events: list[str] = []

        class Store:
            def cas(self, *_args: object, **_kwargs: object) -> dict[str, object]:
                raise AssertionError("backend must not be touched")

        class Scope:
            def assert_ordered(self) -> None:
                events.append("order")

            @contextmanager
            def hold(self) -> Any:
                events.append("hold")
                try:
                    yield None
                finally:
                    events.append("release")

        binding = AdmittedControlBinding.bind(Store(), self.lease, self.recheck, Scope())
        with binding.validated_scope():
            events.append("reread")
        self.assertEqual(["order", "order", "hold", "reread", "release"], events)

    def test_typed_binding_rejects_lock_order_failure_before_construction(self) -> None:
        class Store:
            def cas(self, _expected: int, _record: Mapping[str, object]) -> dict[str, object]:
                raise AssertionError("store must not be touched")

        class Scope:
            def assert_ordered(self) -> None:
                raise RuntimeError("lock order unavailable")

            def hold(self) -> Any:
                raise AssertionError("scope hold must not be touched")

        with self.assertRaisesRegex(AdmissionLeaseError, "scope is invalid"):
            AdmittedControlBinding.bind(Store(), self.lease, self.recheck, Scope())

    def test_typed_binding_rejects_replaced_recheck_before_backend(self) -> None:
        class Store:
            def cas(self, _expected: int, _record: Mapping[str, object]) -> dict[str, object]:
                raise AssertionError("backend must not be touched")

        class Scope:
            def assert_ordered(self) -> None: ...

            def hold(self) -> Any: ...

        binding = AdmittedControlBinding.bind(Store(), self.lease, self.recheck, Scope())
        object.__setattr__(binding.recheck, "fencing_token", "fence-replaced")
        try:
            with self.assertRaisesRegex(AdmissionLeaseError, "evidence does not match"):
                binding.cas(1, self.record)
        finally:
            object.__setattr__(binding.recheck, "fencing_token", "fence-1")

    def test_typed_binding_rejects_replaced_authority_before_backend(self) -> None:
        class Store:
            def cas(self, _expected: int, _record: Mapping[str, object]) -> dict[str, object]:
                raise AssertionError("backend must not be touched")

        class Scope:
            def assert_ordered(self) -> None: ...

            def hold(self) -> Any: ...

        binding = AdmittedControlBinding.bind(Store(), self.lease, self.recheck, Scope())
        object.__setattr__(binding.recheck, "authority_revision", "authority-replaced")
        try:
            with self.assertRaisesRegex(AdmissionLeaseError, "evidence does not match"):
                binding.cas(1, self.record)
        finally:
            object.__setattr__(binding.recheck, "authority_revision", "authority-1")

    def test_typed_binding_rejects_replaced_project_before_backend(self) -> None:
        class Store:
            def cas(self, _expected: int, _record: Mapping[str, object]) -> dict[str, object]:
                raise AssertionError("backend must not be touched")

        class Scope:
            def assert_ordered(self) -> None: ...

            def hold(self) -> Any: ...

        binding = AdmittedControlBinding.bind(Store(), self.lease, self.recheck, Scope())
        object.__setattr__(binding.recheck, "project_id", "project-replaced")
        try:
            with self.assertRaisesRegex(AdmissionLeaseError, "evidence does not match"):
                binding.cas(1, self.record)
        finally:
            object.__setattr__(binding.recheck, "project_id", "project")

    def test_typed_binding_rejects_replaced_durable_barrier_before_backend(self) -> None:
        class Store:
            def cas(self, _expected: int, _record: Mapping[str, object]) -> dict[str, object]:
                raise AssertionError("backend must not be touched")

        class Scope:
            def assert_ordered(self) -> None: ...

            def hold(self) -> Any: ...

        binding = AdmittedControlBinding.bind(Store(), self.lease, self.recheck, Scope())
        object.__setattr__(binding.recheck, "durable_barrier_id", "barrier-replaced")
        try:
            with self.assertRaisesRegex(AdmissionLeaseError, "evidence does not match"):
                binding.cas(1, self.record)
        finally:
            object.__setattr__(binding.recheck, "durable_barrier_id", "barrier-1")

    def test_typed_binding_rejects_replaced_state_revision_before_backend(self) -> None:
        class Store:
            def cas(self, _expected: int, _record: Mapping[str, object]) -> dict[str, object]:
                raise AssertionError("backend must not be touched")

        class Scope:
            def assert_ordered(self) -> None: ...

            def hold(self) -> Any: ...

        binding = AdmittedControlBinding.bind(Store(), self.lease, self.recheck, Scope())
        object.__setattr__(binding.recheck, "revision", 2)
        try:
            with self.assertRaisesRegex(AdmissionLeaseError, "evidence does not match"):
                binding.cas(1, self.record)
        finally:
            object.__setattr__(binding.recheck, "revision", 1)

    def test_invalid_evidence_fails_before_scope_or_store(self) -> None:
        class Scope:
            def assert_ordered(self) -> None:
                raise AssertionError("scope must not be touched")

            def hold(self) -> Any:
                raise AssertionError("scope must not be touched")

        class Store:
            def cas(self, *_args: object, **_kwargs: object) -> dict[str, object]:
                raise AssertionError("store must not be touched")

        changed = dict(self.record, fencing_token="other")  # noqa: S106
        with self.assertRaisesRegex(AdmissionLeaseError, "does not match"):
            admitted_cas(Store(), 1, changed, self.lease, self.recheck, Scope())

    def test_hostile_record_value_fails_before_scope_or_store(self) -> None:
        class ExplodingEquality:
            def __eq__(self, _other: object) -> bool:
                raise RuntimeError("comparison unavailable")

        class Scope:
            def assert_ordered(self) -> None:
                raise AssertionError("scope must not be touched")

            def hold(self) -> Any:
                raise AssertionError("scope must not be touched")

        class Store:
            def cas(self, *_args: object, **_kwargs: object) -> dict[str, object]:
                raise AssertionError("store must not be touched")

        changed = dict(self.record, project_id=ExplodingEquality())
        with self.assertRaisesRegex(AdmissionLeaseError, "values are invalid"):
            admitted_cas(Store(), 1, changed, self.lease, self.recheck, Scope())

    def test_unknown_record_field_fails_before_scope_or_store(self) -> None:
        class Scope:
            def assert_ordered(self) -> None:
                raise AssertionError("scope must not be touched")

            def hold(self) -> Any:
                raise AssertionError("scope must not be touched")

        class Store:
            def cas(self, *_args: object, **_kwargs: object) -> dict[str, object]:
                raise AssertionError("store must not be touched")

        changed = dict(self.record, artifact_root="not-admitted")
        with self.assertRaisesRegex(AdmissionLeaseError, "unknown fields"):
            admitted_cas(Store(), 1, changed, self.lease, self.recheck, Scope())

    def test_missing_or_malformed_identity_fails_before_scope_or_store(self) -> None:
        class Scope:
            def assert_ordered(self) -> None:
                raise AssertionError("scope must not be touched")

            def hold(self) -> Any:
                raise AssertionError("scope must not be touched")

        class Store:
            def cas(self, *_args: object, **_kwargs: object) -> dict[str, object]:
                raise AssertionError("store must not be touched")

        cases: tuple[tuple[str, object], ...] = (
            ("fencing_token", None),
            ("durable_barrier_id", 7),
        )
        for field, value in cases:
            with self.subTest(field=field):
                changed: dict[str, object] = dict(self.record)
                changed.pop(field, None)
                changed[field] = value
                with self.assertRaisesRegex(AdmissionLeaseError, "does not match"):
                    admitted_cas(Store(), 1, changed, self.lease, self.recheck, Scope())

    def test_store_failure_releases_admission_scope(self) -> None:
        events: list[str] = []

        class Scope:
            def assert_ordered(self) -> None:
                events.append("order")

            @contextmanager
            def hold(self) -> Any:
                events.append("hold")
                try:
                    yield None
                finally:
                    events.append("release")

        class Store:
            def cas(self, *_args: object, **_kwargs: object) -> dict[str, object]:
                events.append("write")
                raise RuntimeError("store crashed")

        with self.assertRaisesRegex(RuntimeError, "store crashed"):
            admitted_cas(Store(), 1, self.record, self.lease, self.recheck, Scope())
        self.assertEqual(["order", "hold", "write", "release"], events)

    def test_recheck_evidence_drift_fails_before_scope_or_store(self) -> None:
        class Scope:
            def assert_ordered(self) -> None:
                raise AssertionError("scope must not be touched")

            def hold(self) -> Any:
                raise AssertionError("scope must not be touched")

        class Store:
            def cas(self, *_args: object, **_kwargs: object) -> dict[str, object]:
                raise AssertionError("store must not be touched")

        object.__setattr__(self.recheck, "authority_revision", "authority-stale")
        try:
            with self.assertRaisesRegex(AdmissionLeaseError, "evidence does not match"):
                admitted_cas(Store(), 1, self.record, self.lease, self.recheck, Scope())
        finally:
            object.__setattr__(self.recheck, "authority_revision", "authority-1")

    def test_recheck_comparison_failure_is_normalized_before_scope_or_store(self) -> None:
        class ExplodingEquality:
            def __eq__(self, _other: object) -> bool:
                raise RuntimeError("comparison unavailable")

        class Scope:
            def assert_ordered(self) -> None:
                raise AssertionError("scope must not be touched")

            def hold(self) -> Any:
                raise AssertionError("scope must not be touched")

        class Store:
            def cas(self, *_args: object, **_kwargs: object) -> dict[str, object]:
                raise AssertionError("store must not be touched")

        object.__setattr__(self.recheck, "authority_revision", ExplodingEquality())
        try:
            with self.assertRaisesRegex(AdmissionLeaseError, "evidence is invalid"):
                admitted_cas(Store(), 1, self.record, self.lease, self.recheck, Scope())
        finally:
            object.__setattr__(self.recheck, "authority_revision", "authority-1")

    def test_scope_order_failure_is_normalized_before_store(self) -> None:
        class Scope:
            def assert_ordered(self) -> None:
                raise RuntimeError("lock order unavailable")

            def hold(self) -> Any:
                raise AssertionError("scope hold must not be touched")

        class Store:
            def cas(self, *_args: object, **_kwargs: object) -> dict[str, object]:
                raise AssertionError("store must not be touched")

        with self.assertRaisesRegex(AdmissionLeaseError, "scope is invalid"):
            admitted_cas(Store(), 1, self.record, self.lease, self.recheck, Scope())

    def test_non_mapping_store_result_fails_closed_after_scope_release(self) -> None:
        events: list[str] = []

        class Scope:
            def assert_ordered(self) -> None:
                events.append("order")

            @contextmanager
            def hold(self) -> Any:
                events.append("hold")
                try:
                    yield None
                finally:
                    events.append("release")

        class Store:
            def cas(self, *_args: object, **_kwargs: object) -> dict[str, object]:
                events.append("write")
                return None  # type: ignore[return-value]

        with self.assertRaisesRegex(AdmissionLeaseError, "result is invalid"):
            admitted_cas(Store(), 1, self.record, self.lease, self.recheck, Scope())
        self.assertEqual(["order", "hold", "write", "release"], events)

    def test_stale_backend_result_revision_fails_closed_after_scope_release(self) -> None:
        events: list[str] = []

        class Scope:
            def assert_ordered(self) -> None:
                events.append("order")

            @contextmanager
            def hold(self) -> Any:
                events.append("hold")
                try:
                    yield None
                finally:
                    events.append("release")

        class Store:
            def cas(self, *_args: object, **_kwargs: object) -> dict[str, object]:
                events.append("write")
                return {"revision": 1}

        with self.assertRaisesRegex(AdmissionLeaseError, "revision is invalid"):
            admitted_cas(Store(), 1, self.record, self.lease, self.recheck, Scope())
        self.assertEqual(["order", "hold", "write", "release"], events)

    def test_backend_result_identity_mismatch_fails_closed_after_scope_release(self) -> None:
        events: list[str] = []

        class Scope:
            def assert_ordered(self) -> None:
                events.append("order")

            @contextmanager
            def hold(self) -> Any:
                events.append("hold")
                try:
                    yield None
                finally:
                    events.append("release")

        class Store:
            def cas(self, *_args: object, **_kwargs: object) -> dict[str, object]:
                events.append("write")
                return {
                    **self_record,
                    "revision": 2,
                    "fencing_token": "different-fence",
                }

        self_record = dict(self.record)
        with self.assertRaisesRegex(AdmissionLeaseError, "identity is invalid"):
            admitted_cas(Store(), 1, self.record, self.lease, self.recheck, Scope())
        self.assertEqual(["order", "hold", "write", "release"], events)

    def test_hostile_backend_result_access_fails_closed_after_scope_release(self) -> None:
        events: list[str] = []

        class HostileResult(dict[str, object]):
            def get(self, _key: str, _default: object = None) -> object:
                raise RuntimeError("result access unavailable")

        class Scope:
            def assert_ordered(self) -> None:
                events.append("order")

            @contextmanager
            def hold(self) -> Any:
                events.append("hold")
                try:
                    yield None
                finally:
                    events.append("release")

        class Store:
            def cas(self, *_args: object, **_kwargs: object) -> dict[str, object]:
                events.append("write")
                return HostileResult(revision=2)

        with self.assertRaisesRegex(AdmissionLeaseError, "result is invalid"):
            admitted_cas(Store(), 1, self.record, self.lease, self.recheck, Scope())
        self.assertEqual(["order", "hold", "write", "release"], events)

    def test_missing_or_mismatched_contract_objects_fail_closed(self) -> None:
        with self.assertRaisesRegex(AdmissionLeaseError, "lease is required"):
            admitted_cas(None, 1, self.record, None, self.recheck, None)  # type: ignore[arg-type]
        other = AdmissionLease("project", "authority-1", "fence-2", "owner-1", "barrier-2", 2)
        other_recheck = validate_recheck(
            other,
            project_id="project",
            authority_revision="authority-1",
            fencing_token="fence-2",  # noqa: S106
            fencing_owner="owner-1",
            durable_barrier_id="barrier-2",
            revision=2,
        )
        with self.assertRaisesRegex(AdmissionLeaseError, "does not match"):
            admitted_cas(None, 1, self.record, self.lease, other_recheck, None)  # type: ignore[arg-type]

    def test_stale_expected_revision_fails_before_scope(self) -> None:
        class Scope:
            def assert_ordered(self) -> None:
                raise AssertionError("scope must not be touched")

            def hold(self) -> Any:
                raise AssertionError("scope must not be touched")

        with self.assertRaisesRegex(AdmissionLeaseError, "revision does not match"):
            admitted_cas(None, 2, self.record, self.lease, self.recheck, Scope())  # type: ignore[arg-type]

    def test_record_is_snapshotted_before_scope_and_store(self) -> None:
        events: list[str] = []

        class MutableRecord(Mapping[str, object]):
            def __init__(self, values: Mapping[str, object]) -> None:
                self._data = dict(values)

            def __getitem__(self, key: str) -> object:
                return self._data[key]

            def __iter__(self) -> Iterator[str]:
                events.append("snapshot")
                return iter(self._data)

            def __len__(self) -> int:
                return len(self._data)

        class Scope:
            def assert_ordered(self) -> None:
                events.append("order")

            @contextmanager
            def hold(self) -> Any:
                events.append("hold")
                yield None

        class Store:
            def cas(
                self,
                expected_revision: int,  # noqa: ARG002
                record: Mapping[str, object],
            ) -> dict[str, object]:
                events.append("write")
                snapshot = dict(record)
                self.record = snapshot
                return snapshot

        store = Store()
        result = admitted_cas(
            store, 1, MutableRecord(self.record), self.lease, self.recheck, Scope()
        )
        self.assertEqual(self.record, result)
        self.assertEqual(["snapshot", "order", "hold", "write"], events)
