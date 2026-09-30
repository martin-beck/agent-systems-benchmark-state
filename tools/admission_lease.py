# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Typed, read-only admission-lease contract for the future fence adapter.

This module validates caller-owned evidence only. It does not acquire locks,
open SQLite, mutate authority state, or make legacy constructors require a
lease.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from typing import cast

LOCK_ORDER = ("common", "control", "authority")


class AdmissionLeaseError(ValueError):
    """A lease or recheck does not satisfy the fail-closed contract."""


@dataclass(frozen=True, slots=True)
class LockOrder:
    """The only lock acquisition order accepted by the future adapter."""

    names: tuple[str, ...] = LOCK_ORDER

    def __post_init__(self) -> None:
        if self.names != LOCK_ORDER:
            raise AdmissionLeaseError("admission lock order is invalid")


@dataclass(frozen=True, slots=True)
class AdmissionLease:
    """Immutable caller-owned identity and fence evidence."""

    project_id: str
    authority_revision: str
    fencing_token: str
    fencing_owner: str
    durable_barrier_id: str
    revision: int
    order: LockOrder = LockOrder()

    def __post_init__(self) -> None:
        for name in (
            "project_id",
            "authority_revision",
            "fencing_token",
            "fencing_owner",
            "durable_barrier_id",
        ):
            value = getattr(self, name)
            if type(value) is not str or not value:
                raise AdmissionLeaseError(f"admission lease {name} is invalid")
        if type(self.revision) is not int or self.revision < 1:
            raise AdmissionLeaseError("admission lease revision is invalid")
        if not isinstance(self.order, LockOrder):
            raise AdmissionLeaseError("admission lease order is invalid")


@dataclass(frozen=True, slots=True)
class AdmissionRecheck:
    """A validated read-only observation against an existing lease."""

    lease: AdmissionLease
    project_id: str
    authority_revision: str
    fencing_token: str
    fencing_owner: str
    durable_barrier_id: str
    revision: int

    def __post_init__(self) -> None:
        if not isinstance(self.lease, AdmissionLease):
            raise AdmissionLeaseError("admission recheck lease is invalid")
        values = (
            ("project_id", self.project_id),
            ("authority_revision", self.authority_revision),
            ("fencing_token", self.fencing_token),
            ("fencing_owner", self.fencing_owner),
            ("durable_barrier_id", self.durable_barrier_id),
        )
        for name, value in values:
            if type(value) is not str or not value:
                raise AdmissionLeaseError(f"admission recheck {name} is invalid")
            if value != getattr(self.lease, name):
                raise AdmissionLeaseError(f"admission recheck {name} changed")
        if type(self.revision) is not int or self.revision != self.lease.revision:
            raise AdmissionLeaseError("admission recheck revision changed")


def lease_from_record(record: Mapping[str, object]) -> AdmissionLease:
    """Construct a lease from exact immutable barrier identity fields."""
    required = {
        "project_id",
        "authority_revision",
        "fencing_token",
        "fencing_owner",
        "durable_barrier_id",
        "revision",
    }
    if set(record) != required:
        raise AdmissionLeaseError("admission lease record fields are invalid")
    text_fields = (
        "project_id",
        "authority_revision",
        "fencing_token",
        "fencing_owner",
        "durable_barrier_id",
    )
    if any(type(record[field]) is not str or not record[field] for field in text_fields):
        raise AdmissionLeaseError("admission lease identity is invalid")
    if type(record["revision"]) is not int or record["revision"] < 1:
        raise AdmissionLeaseError("admission lease revision is invalid")
    return AdmissionLease(
        project_id=cast(str, record["project_id"]),
        authority_revision=cast(str, record["authority_revision"]),
        fencing_token=cast(str, record["fencing_token"]),
        fencing_owner=cast(str, record["fencing_owner"]),
        durable_barrier_id=cast(str, record["durable_barrier_id"]),
        revision=record["revision"],
    )


def validate_recheck(
    lease: AdmissionLease,
    *,
    project_id: object,
    authority_revision: object,
    fencing_token: object,
    fencing_owner: object,
    durable_barrier_id: object,
    revision: object,
) -> AdmissionRecheck:
    """Validate a fresh caller-owned observation without performing I/O."""
    if not isinstance(lease, AdmissionLease):
        raise AdmissionLeaseError("admission recheck lease is invalid")
    return AdmissionRecheck(
        lease=lease,
        project_id=cast(str, project_id),
        authority_revision=cast(str, authority_revision),
        fencing_token=cast(str, fencing_token),
        fencing_owner=cast(str, fencing_owner),
        durable_barrier_id=cast(str, durable_barrier_id),
        revision=cast(int, revision),
    )
