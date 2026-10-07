# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Fail-closed admission predicates for a coordinator upgrade."""

from __future__ import annotations

from collections.abc import Mapping

from tools.upgrade_identity import ENVELOPE_FIELDS, UpgradeIdentityError, validate_envelope


class AdmissionError(ValueError):
    """Raised when an upgrade safety predicate is absent or false."""


PREFLIGHT_PREDICATES = (
    "release_authentic",
    "runtime_supported",
    "state_clean",
    "state_synchronized",
    "no_divergence",
    "no_active_leases",
    "no_wrapped_commands",
    "no_reconciliation",
    "no_publication",
    "binding_valid",
    "backend_valid",
    "vendor_valid",
    "disk_capacity_ok",
    "scratch_capacity_ok",
    "backup_destination_restorable",
)

QUIESCENCE_PREDICATES = (
    "maintenance_barrier",
    "barrier_acquired_before_quiescence",
    "workers_drained",
    "leases_fenced",
    "wrapped_commands_drained",
    "reconciliation_stopped",
    "publication_stopped",
)

REOPEN_PREDICATES = (
    "maintenance_barrier",
    "barrier_reopen_verified",
    "functional_available",
    "runtime_validated",
    "backend_roundtrip_valid",
    "projections_valid",
    "binding_valid",
    "lease_fence_valid",
)

IDENTITY_FIELDS = ENVELOPE_FIELDS
QUIESCENCE_IDENTITY = "durable_barrier_id"
KNOWN_FIELDS = set(PREFLIGHT_PREDICATES + QUIESCENCE_PREDICATES + REOPEN_PREDICATES)
KNOWN_FIELDS.update(
    (
        *IDENTITY_FIELDS,
        QUIESCENCE_IDENTITY,
        "barrier_status",
        "reopen_barrier_status",
        "validation_failed",
        "safe_mode_ready",
    )
)


def _require(snapshot: Mapping[str, object], predicates: tuple[str, ...], phase: str) -> None:
    unknown = set(snapshot) - KNOWN_FIELDS
    if unknown:
        raise AdmissionError(f"{phase} denied; unknown fields: {', '.join(sorted(unknown))}")
    try:
        validate_envelope({field: snapshot.get(field) for field in IDENTITY_FIELDS})
    except UpgradeIdentityError as error:
        raise AdmissionError(f"{phase} denied; invalid identity envelope") from error
    missing = [name for name in predicates if snapshot.get(name) is not True]
    if missing:
        raise AdmissionError(f"{phase} denied; unmet predicates: {', '.join(missing)}")


def admit_preflight(snapshot: Mapping[str, object]) -> None:
    """Allow staging only when every read-only prerequisite is proven."""
    _require(snapshot, PREFLIGHT_PREDICATES, "preflight")


def admit_quiesced(snapshot: Mapping[str, object]) -> None:
    """Allow quiescence only after a durably held maintenance barrier."""
    _require(snapshot, QUIESCENCE_PREDICATES, "quiescence")
    barrier = snapshot.get(QUIESCENCE_IDENTITY)
    if not isinstance(barrier, str) or not barrier:
        raise AdmissionError("quiescence denied; durable barrier proof is absent")
    if snapshot.get("barrier_status") != "held":
        raise AdmissionError("quiescence denied; durable barrier is not held")


def recheck_before_replacement(
    admitted: Mapping[str, object], current: Mapping[str, object]
) -> None:
    """Atomically recheck identity and quiescence immediately before replacement."""
    admit_quiesced(admitted)
    admit_quiesced(current)
    for field in (*IDENTITY_FIELDS,):
        if admitted.get(field) != current.get(field):
            raise AdmissionError(f"replacement denied; stale {field}")


def admit_reopen(snapshot: Mapping[str, object]) -> None:
    """Allow work to reopen only after target or rollback integrity validation."""
    _require(snapshot, REOPEN_PREDICATES, "reopen")
    target = snapshot.get("target")
    if target not in {"new", "rollback"}:
        raise AdmissionError("reopen denied; target must be new or rollback")
    barrier = snapshot.get(QUIESCENCE_IDENTITY)
    if not isinstance(barrier, str) or not barrier:
        raise AdmissionError("reopen denied; durable barrier proof is absent")
    if snapshot.get("reopen_barrier_status") != "released":
        raise AdmissionError("reopen denied; durable barrier is not released")
    validation_failed = snapshot.get("validation_failed", False)
    if not isinstance(validation_failed, bool):
        raise AdmissionError("reopen denied; validation_failed must be boolean")
    if validation_failed:
        raise AdmissionError("reopen denied; failed validation requires safe mode")


def admit_safe_mode(snapshot: Mapping[str, object]) -> None:
    """Require an explicit safe-mode record when neither runtime can reopen."""
    _require(snapshot, (), "safe mode")
    barrier = snapshot.get(QUIESCENCE_IDENTITY)
    if not isinstance(barrier, str) or not barrier:
        raise AdmissionError("safe mode denied; durable barrier proof is absent")
    safe_mode_ready = snapshot.get("safe_mode_ready")
    if not isinstance(safe_mode_ready, bool):
        raise AdmissionError("safe mode denied; safe_mode_ready must be boolean")
    if not safe_mode_ready:
        raise AdmissionError("safe mode denied; durable safe-mode record is absent")
