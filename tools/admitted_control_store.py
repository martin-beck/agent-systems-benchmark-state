# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Uncalled, fail-closed admission wrapper for control-store writes.

The wrapper is an integration seam only. It does not alter legacy store
constructors, and no production caller uses it until the concrete lock owner
and authority rereader are integrated and independently reviewed.
"""

from __future__ import annotations

from collections.abc import Iterator, Mapping
from contextlib import AbstractContextManager, contextmanager
from dataclasses import dataclass
from typing import Protocol, runtime_checkable

from tools.admission_lease import AdmissionLease, AdmissionLeaseError, AdmissionRecheck

_ADMITTED_RECORD_FIELDS = frozenset(
    {
        "project_id",
        "authority_revision",
        "fencing_token",
        "fencing_owner",
        "durable_barrier_id",
        "status",
        "revision",
    }
)


@runtime_checkable
class OrderedAdmissionScope(Protocol):
    """Caller-owned common/control/authority scope."""

    def assert_ordered(self) -> None: ...

    def hold(self) -> AbstractContextManager[object]: ...


class AdmittedControlStore(Protocol):
    """Minimal write surface consumed by the uncalled wrapper."""

    def cas(self, expected_revision: int, record: Mapping[str, object]) -> dict[str, object]: ...


@dataclass(frozen=True)
class AdmittedControlBinding:
    """Typed caller-owned binding; intentionally uncalled by production paths."""

    store: AdmittedControlStore
    lease: AdmissionLease
    recheck: AdmissionRecheck
    scope: OrderedAdmissionScope

    @classmethod
    def bind(
        cls,
        store: AdmittedControlStore,
        lease: AdmissionLease,
        recheck: AdmissionRecheck,
        scope: OrderedAdmissionScope,
    ) -> AdmittedControlBinding:
        if not callable(getattr(store, "cas", None)):
            raise AdmissionLeaseError("admitted control store is required")
        if not isinstance(lease, AdmissionLease):
            raise AdmissionLeaseError("admitted control lease is required")
        if not isinstance(recheck, AdmissionRecheck) or recheck.lease != lease:
            raise AdmissionLeaseError("admitted control recheck does not match lease")
        if not isinstance(scope, OrderedAdmissionScope):
            raise AdmissionLeaseError("admitted control scope is required")
        try:
            scope.assert_ordered()
        except (AttributeError, RuntimeError, TypeError) as error:
            raise AdmissionLeaseError("admitted control scope is invalid") from error
        return cls(store, lease, recheck, scope)

    def validate(self) -> None:
        """Preflight the caller-owned binding without touching the backend."""
        if not isinstance(self.recheck, AdmissionRecheck) or self.recheck.lease != self.lease:
            raise AdmissionLeaseError("admitted control recheck does not match lease")
        try:
            self.scope.assert_ordered()
        except (AttributeError, RuntimeError, TypeError) as error:
            raise AdmissionLeaseError("admitted control scope is invalid") from error

    @contextmanager
    def validated_scope(self) -> Iterator[None]:
        """Hold the caller-owned scope for durable reread, without backend use."""
        self.validate()
        try:
            with self.scope.hold():
                yield None
        except (AttributeError, RuntimeError, TypeError) as error:
            raise AdmissionLeaseError("admitted control scope is invalid") from error

    def cas(self, expected_revision: int, record: Mapping[str, object]) -> dict[str, object]:
        self.validate()
        return admitted_cas(
            self.store, expected_revision, record, self.lease, self.recheck, self.scope
        )


def admitted_cas(  # noqa: C901
    store: AdmittedControlStore,
    expected_revision: int,
    record: Mapping[str, object],
    lease: AdmissionLease,
    recheck: AdmissionRecheck,
    scope: OrderedAdmissionScope,
) -> dict[str, object]:
    """Perform one CAS only after immutable evidence and order validation.

    Validation happens before ``scope.hold()`` and before calling ``store``;
    this function is intentionally uncalled by current upgrade paths.
    """
    if not isinstance(lease, AdmissionLease):
        raise AdmissionLeaseError("admitted control lease is required")
    if not isinstance(recheck, AdmissionRecheck) or recheck.lease != lease:
        raise AdmissionLeaseError("admitted control recheck does not match lease")
    recheck_values = {
        "project_id": lease.project_id,
        "authority_revision": lease.authority_revision,
        "fencing_token": lease.fencing_token,
        "fencing_owner": lease.fencing_owner,
        "durable_barrier_id": lease.durable_barrier_id,
        "revision": lease.revision,
    }
    try:
        if any(
            getattr(recheck, name) != value or type(getattr(recheck, name)) is not type(value)
            for name, value in recheck_values.items()
        ):
            raise AdmissionLeaseError("admitted control recheck evidence does not match lease")
    except AdmissionLeaseError:
        raise
    except Exception as error:
        raise AdmissionLeaseError("admitted control recheck evidence is invalid") from error
    if not isinstance(scope, OrderedAdmissionScope):
        raise AdmissionLeaseError("admitted control scope is required")
    if type(expected_revision) is not int or expected_revision != lease.revision:
        raise AdmissionLeaseError("admitted control revision does not match lease")
    try:
        record_snapshot = dict(record)
    except (TypeError, ValueError) as error:
        raise AdmissionLeaseError("admitted control record is invalid") from error
    if set(record_snapshot) - _ADMITTED_RECORD_FIELDS:
        raise AdmissionLeaseError("admitted control record schema contains unknown fields")
    required = {
        "project_id": lease.project_id,
        "authority_revision": lease.authority_revision,
        "fencing_token": lease.fencing_token,
        "fencing_owner": lease.fencing_owner,
        "durable_barrier_id": lease.durable_barrier_id,
    }
    try:
        if any(
            record_snapshot.get(name) != value or type(record_snapshot.get(name)) is not type(value)
            for name, value in required.items()
        ):
            raise AdmissionLeaseError("admitted control record does not match lease")
    except AdmissionLeaseError:
        raise
    except Exception as error:
        raise AdmissionLeaseError("admitted control record values are invalid") from error
    try:
        scope.assert_ordered()
    except (AttributeError, RuntimeError, TypeError) as error:
        raise AdmissionLeaseError("admitted control scope is invalid") from error
    try:
        with scope.hold():
            result = store.cas(expected_revision, record_snapshot)
            if not isinstance(result, dict):
                raise AdmissionLeaseError("admitted control store result is invalid")
            try:
                result_revision = result.get("revision")
                # A backend may return a legacy snapshot without identity
                # fields, but any identity it does return must remain bound
                # to the admission lease.  Never let a successful CAS be
                # reported for another owner/barrier.
                for name, expected in (
                    ("project_id", lease.project_id),
                    ("authority_revision", lease.authority_revision),
                    ("fencing_token", lease.fencing_token),
                    ("fencing_owner", lease.fencing_owner),
                    ("durable_barrier_id", lease.durable_barrier_id),
                ):
                    if name in result:
                        actual = result.get(name)
                        if actual != expected or type(actual) is not type(expected):
                            raise AdmissionLeaseError("admitted control store identity is invalid")
            except AdmissionLeaseError:
                raise
            except Exception as error:
                raise AdmissionLeaseError("admitted control store result is invalid") from error
            if "revision" in result and (
                type(result_revision) is not int or result_revision <= expected_revision
            ):
                raise AdmissionLeaseError("admitted control store revision is invalid")
            return result
    except (AttributeError, TypeError) as error:
        raise AdmissionLeaseError("admitted control scope is invalid") from error
