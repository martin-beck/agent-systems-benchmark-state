# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Bound execution reservation transitions, isolated from the CLI façade."""

from __future__ import annotations

import datetime as dt
import re
from typing import Any, cast

if __package__:
    from . import execution_abandonment, execution_receipt
else:  # pragma: no cover - direct handoffctl execution
    import execution_abandonment  # type: ignore[import-not-found,no-redef]
    import execution_receipt  # type: ignore[import-not-found,no-redef]

type Meta = dict[str, Any]


def start(runtime: Any, args: Any, meta: Meta) -> str:
    """Create one exact, future-bounded execution reservation."""
    runtime.require_active_binding_owner(args, meta)
    if not isinstance(meta.get("execution_envelope"), dict):
        raise RuntimeError("execution reservation requires a bound execution envelope")
    if runtime.live_execution_reservation(meta) is not None:
        raise RuntimeError("EXECUTION_IN_PROGRESS: bound task already has a live execution")
    if meta.get("execution_reservation") is not None:
        raise RuntimeError("EXECUTION_RECOVERY_REQUIRED: expired execution reservation remains")
    execution_id = getattr(args, "execution_id", "")
    expires_at = getattr(args, "execution_expires_at", "")
    if not re.fullmatch(r"[0-9a-f]{32}", str(execution_id)):
        raise RuntimeError("invalid execution reservation identifier")
    try:
        expires = dt.datetime.fromisoformat(str(expires_at).replace("Z", "+00:00"))
    except ValueError as error:
        raise RuntimeError("invalid execution reservation expiry") from error
    if expires <= dt.datetime.now(dt.UTC):
        raise RuntimeError("execution reservation expiry must be in the future")
    meta["execution_reservation"] = {
        "execution_id": execution_id,
        "owner": args.owner,
        "task_revision": meta["task_revision"],
        "envelope_digest": meta["execution_envelope_digest"],
        "command_class": args.command_class,
        "scope_digest": args.scope_digest,
        "argv_digest": args.argv_digest,
        "expires_at": expires.replace(microsecond=0).isoformat(),
    }
    claim_expiry = runtime.parse_claim_expiry(meta.get("claim_expires"))
    if claim_expiry < expires:
        meta["claim_expires"] = expires.replace(microsecond=0).isoformat()
    return f"Reserved bound execution {execution_id}."


def finish(runtime: Any, args: Any, meta: Meta) -> str:
    """Clear only a reservation with its exact durable result."""
    reservation = meta.get("execution_reservation")
    if not isinstance(reservation, dict) or reservation.get("execution_id") != args.execution_id:
        raise RuntimeError("execution reservation no longer matches this command")
    if reservation.get("owner") != args.owner:
        raise RuntimeError("execution reservation owner does not match")
    runtime.require_optional_revision(args, meta)
    if not runtime.execution_result_matches(cast(Meta, reservation), meta.get("execution_result")):
        raise RuntimeError("execution finish requires an exact durable result")
    meta.pop("execution_reservation", None)
    return str(args.note)


def result(runtime: Any, args: Any, meta: Meta) -> str:
    """Record one exact terminal receipt without clearing its reservation."""
    reservation = meta.get("execution_reservation")
    if not isinstance(reservation, dict) or reservation.get("execution_id") != args.execution_id:
        raise RuntimeError("execution reservation no longer matches this command")
    runtime.require_optional_revision(args, meta)
    try:
        recorded = execution_receipt.build(reservation, args)
    except ValueError as error:
        raise RuntimeError(str(error)) from error
    if meta.get("execution_result") == recorded:
        raise runtime.IdempotentMutationError(
            f"Execution result {args.execution_id} is already recorded."
        )
    meta["execution_result"] = recorded
    return f"Recorded execution result {args.execution_id}."


def recover(runtime: Any, args: Any, meta: Meta) -> str:
    """Recover one expired reservation only after matching completion evidence."""
    runtime.require_optional_revision(args, meta)
    reservation = meta.get("execution_reservation")
    if not runtime.valid_execution_reservation(reservation):
        raise RuntimeError("execution recovery requires a valid reservation")
    valid_reservation = cast(Meta, reservation)
    if runtime.live_execution_reservation(meta) is not None:
        raise RuntimeError("EXECUTION_IN_PROGRESS: execution reservation has not expired")
    runtime.require_claimed_worker_absent(meta)
    if not runtime.execution_result_matches(valid_reservation, meta.get("execution_result")):
        raise RuntimeError(
            "EXECUTION_RESULT_UNKNOWN: reservation-specific completion evidence is unavailable"
        )
    meta.pop("execution_reservation", None)
    return f"Recovered completed execution {valid_reservation['execution_id']}."


def abandon(runtime: Any, args: Any, meta: Meta) -> str:
    """Recover an expired unknown reservation with auditable local evidence."""
    runtime.require_optional_revision(args, meta)
    reservation = meta.get("execution_reservation")
    if not runtime.valid_execution_reservation(reservation):
        raise RuntimeError("execution abandonment requires a valid reservation")
    valid_reservation = cast(Meta, reservation)
    if valid_reservation["execution_id"] != args.execution_id:
        raise RuntimeError("execution abandonment reservation identity does not match")
    if runtime.live_execution_reservation(meta) is not None:
        raise RuntimeError("EXECUTION_IN_PROGRESS: execution reservation has not expired")
    # Pre-identity reservations can be recovered only with explicit operator
    # acknowledgement; all exact reservation, expiry, result, and evidence
    # checks below remain mandatory.
    if not (
        getattr(args, "allow_legacy_without_identity", False)
        and "claim_process" not in meta
        and _expired_claim(meta)
    ):
        runtime.require_claimed_worker_absent(meta)
    if runtime.execution_result_matches(valid_reservation, meta.get("execution_result")):
        raise RuntimeError("execution abandonment rejects a reservation with a durable result")
    try:
        record = execution_abandonment.build(valid_reservation, args, runtime.now())
    except ValueError as error:
        raise RuntimeError(str(error)) from error
    records = list(cast(list[Meta], meta.get("execution_abandonments", [])))
    if any(item["execution_id"] == record["execution_id"] for item in records):
        raise runtime.IdempotentMutationError(
            f"Execution {args.execution_id} is already abandoned."
        )
    records.append(record)
    if not execution_abandonment.valid_records(records):
        raise RuntimeError("execution abandonment history is invalid or full")
    meta["execution_abandonments"] = records
    meta.pop("execution_reservation", None)
    previous_owner = str(meta["owner"])
    meta["status"] = "open"
    meta["owner"] = ""
    meta["claim_expires"] = ""
    meta.pop("claim_process", None)
    return (
        f"Abandoned expired execution {args.execution_id} and recovered claim formerly owned by "
        f"{previous_owner} after local evidence verification."
    )


def _expired_claim(meta: Meta) -> bool:
    """Return whether the task claim is durably expired for legacy recovery."""
    value = meta.get("claim_expires")
    if not isinstance(value, str) or not value:
        return False
    try:
        expiry = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return False
    return expiry.tzinfo is not None and expiry <= dt.datetime.now(dt.UTC)
