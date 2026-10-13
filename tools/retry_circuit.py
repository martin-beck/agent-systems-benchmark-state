# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Bounded, revision-fenced retry circuit records for autonomous commands.

The circuit deliberately records only stable digests and concise operator supplied
reasons.  It never retains argv, stderr, paths, or other command output.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
from typing import Any, cast

type Meta = dict[str, Any]

SCHEMA_VERSION = 1
DEFAULT_WINDOW = 3
MAX_WINDOW = 16
MAX_ATTEMPTS = 64
MAX_RECOVERIES = 32
MAX_ABANDONED = 64
TASK = re.compile(r"^AR-[0-9]{4}$")
DIGEST = re.compile(r"^sha256:[0-9a-f]{64}$")
COMMAND_DIGEST = re.compile(r"^[0-9a-f]{64}$")
COMMIT = re.compile(r"^[0-9a-f]{40}$")
FAILURES = frozenset({"EXIT", "SUBPROCESS_TIMEOUT", "RETRYABLE"})
RECOVERIES = frozenset({"checkpoint", "changed-approach", "retry-exception"})
RESERVATION = re.compile(r"^[0-9a-f]{32}$")


def canonical(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def digest(value: object) -> str:
    return "sha256:" + hashlib.sha256(canonical(value)).hexdigest()


def normalized_identity(
    command_digest: str, command_class: str | None, scope_paths: list[str]
) -> str:
    """Return a stable privacy-safe identity for one retryable command shape."""
    if not COMMAND_DIGEST.fullmatch(command_digest):
        raise ValueError("retry circuit command digest is invalid")
    if command_class is not None and command_class not in {
        "read",
        "test",
        "source-write",
        "git-publication",
    }:
        raise ValueError("retry circuit command class is invalid")
    if len(scope_paths) > 64 or any(
        not isinstance(path, str)
        or not path
        or len(path) > 1024
        or "\x00" in path
        or path.startswith("/")
        or any(part in {"", ".", ".."} for part in path.split("/"))
        for path in scope_paths
    ):
        raise ValueError("retry circuit scope is invalid")
    return digest(
        {
            "command_digest": command_digest,
            "command_class": command_class or "unbound",
            "scope": sorted(set(scope_paths)),
        }
    )


def progress_digest(meta: Meta) -> str:
    """Fingerprint durable progress without treating note/revision churn as progress."""
    drift = meta.get("change_drift")
    latest_drift = ""
    if isinstance(drift, list) and drift and isinstance(drift[-1], dict):
        latest_drift = str(drift[-1].get("digest", ""))
    return digest(
        {
            "checkpoint_commit": str(meta.get("checkpoint_commit", "")),
            "change_drift_digest": latest_drift,
            "spec_acceptance": str(
                meta.get("spec_acceptance", {}).get("evidence_digest", "")
                if isinstance(meta.get("spec_acceptance"), dict)
                else ""
            ),
        }
    )


def empty() -> Meta:
    return {
        "schema_version": SCHEMA_VERSION,
        "attempts": [],
        "recoveries": [],
        "hold": None,
        "reservations": [],
        "abandoned": [],
    }


def _reason(value: object) -> str:
    if not isinstance(value, str) or not value.strip() or len(value) > 500 or "\n" in value:
        raise ValueError("retry circuit recovery reason is invalid")
    return value.strip()


def _window(value: object) -> int:
    if type(value) is not int or not DEFAULT_WINDOW <= int(value) <= MAX_WINDOW:
        raise ValueError(f"retry circuit window must be {DEFAULT_WINDOW}..{MAX_WINDOW}")
    return int(value)


def _timestamp(value: object, field: str) -> dt.datetime:
    """Return one canonical UTC timestamp used for durable slot expiry."""
    if not isinstance(value, str) or not value:
        raise ValueError(f"retry circuit {field} is invalid")
    try:
        parsed = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as error:
        raise ValueError(f"retry circuit {field} is invalid") from error
    if parsed.tzinfo is None:
        raise ValueError(f"retry circuit {field} is invalid")
    return parsed.astimezone(dt.UTC)


def _validate_attempt(attempt: object, previous_revision: int) -> int:
    if not isinstance(attempt, dict) or set(attempt) != {
        "identity",
        "failure",
        "progress_digest",
        "task_revision",
        "recorded_at",
        "window",
    }:
        raise ValueError("retry circuit attempt fields are invalid")
    if (
        not DIGEST.fullmatch(str(attempt.get("identity", "")))
        or attempt.get("failure") not in FAILURES
        or not DIGEST.fullmatch(str(attempt.get("progress_digest", "")))
        or type(attempt.get("task_revision")) is not int
        or int(attempt["task_revision"]) <= previous_revision
        or not isinstance(attempt.get("recorded_at"), str)
        or not attempt["recorded_at"]
    ):
        raise ValueError("retry circuit attempt is invalid")
    _window(attempt.get("window"))
    return int(attempt["task_revision"])


def _validate_recovery(recovery: object, previous_revision: int) -> int:
    if not isinstance(recovery, dict) or set(recovery) != {
        "identity",
        "progress_digest",
        "kind",
        "reason",
        "task_revision",
        "recorded_at",
        "checkpoint_commit",
    }:
        raise ValueError("retry circuit recovery fields are invalid")
    if (
        not DIGEST.fullmatch(str(recovery.get("identity", "")))
        or not DIGEST.fullmatch(str(recovery.get("progress_digest", "")))
        or recovery.get("kind") not in RECOVERIES
        or type(recovery.get("task_revision")) is not int
        or int(recovery["task_revision"]) <= previous_revision
        or not isinstance(recovery.get("recorded_at"), str)
        or not recovery["recorded_at"]
        or not isinstance(recovery.get("checkpoint_commit"), str)
        or (recovery["checkpoint_commit"] and not COMMIT.fullmatch(recovery["checkpoint_commit"]))
    ):
        raise ValueError("retry circuit recovery is invalid")
    _reason(recovery.get("reason"))
    return int(recovery["task_revision"])


def _hold_fields(hold: object) -> Meta:
    if not isinstance(hold, dict) or set(hold) != {
        "identity",
        "attempts",
        "progress_digest",
        "held_at",
        "window",
    }:
        raise ValueError("retry circuit hold fields are invalid")
    return hold


def _hold_values(hold: Meta) -> None:
    if (
        not DIGEST.fullmatch(str(hold.get("identity", "")))
        or type(hold.get("attempts")) is not int
        or int(hold["attempts"]) < DEFAULT_WINDOW
        or not DIGEST.fullmatch(str(hold.get("progress_digest", "")))
        or not isinstance(hold.get("held_at"), str)
        or not hold["held_at"]
    ):
        raise ValueError("retry circuit hold is invalid")
    if _window(hold.get("window")) != hold["attempts"]:
        raise ValueError("retry circuit hold threshold is invalid")


def _active_attempts(state: Meta, identity: str, progress: str) -> list[Meta]:
    """Return the current series after its latest explicit recovery boundary."""
    recovered_revision = max(
        (
            int(item["task_revision"])
            for item in state["recoveries"]
            if item["identity"] == identity and item["progress_digest"] == progress
        ),
        default=0,
    )
    return [
        cast(Meta, item)
        for item in state["attempts"]
        if isinstance(item, dict)
        and item["identity"] == identity
        and item["progress_digest"] == progress
        and int(item["task_revision"]) > recovered_revision
    ]


def _matching_hold_attempts(hold: Meta, state: Meta) -> int:
    return len(_active_attempts(state, str(hold["identity"]), str(hold["progress_digest"])))


def _validate_hold(hold: object, state: Meta) -> None:
    if hold is None:
        return
    checked = _hold_fields(hold)
    _hold_values(checked)
    if _matching_hold_attempts(checked, state) < int(checked["attempts"]):
        raise ValueError("retry circuit hold has insufficient attempts")


def _validate_reservation(reservation: object) -> None:
    if (
        not isinstance(reservation, dict)
        or set(reservation)
        != {
            "id",
            "identity",
            "progress_digest",
            "window",
            "task_revision",
            "reserved_at",
            "expires_at",
        }
        or not RESERVATION.fullmatch(str(reservation.get("id", "")))
        or not DIGEST.fullmatch(str(reservation.get("identity", "")))
        or not DIGEST.fullmatch(str(reservation.get("progress_digest", "")))
        or type(reservation.get("task_revision")) is not int
        or not isinstance(reservation.get("reserved_at"), str)
        or not reservation["reserved_at"]
    ):
        raise ValueError("retry circuit reservation is invalid")
    _window(reservation.get("window"))
    if _timestamp(reservation["expires_at"], "reservation expiry") <= _timestamp(
        reservation["reserved_at"], "reservation timestamp"
    ):
        raise ValueError("retry circuit reservation expiry is invalid")


def _validate_abandoned(value: object) -> None:
    """Validate the privacy-safe audit record left by slot expiry."""
    if not isinstance(value, dict) or set(value) != {
        "id",
        "identity",
        "progress_digest",
        "window",
        "task_revision",
        "reserved_at",
        "expires_at",
        "cleaned_at",
        "cause",
    }:
        raise ValueError("retry circuit abandoned slot fields are invalid")
    _validate_reservation(
        {key: value[key] for key in value if key != "cleaned_at" and key != "cause"}
    )
    if value["cause"] != "expired" or _timestamp(
        value["cleaned_at"], "cleanup timestamp"
    ) < _timestamp(value["expires_at"], "reservation expiry"):
        raise ValueError("retry circuit abandoned slot is invalid")


def _collections(value: object) -> Meta:
    if not isinstance(value, dict) or set(value) != {
        "schema_version",
        "attempts",
        "recoveries",
        "hold",
        "reservations",
        "abandoned",
    }:
        raise ValueError("retry circuit fields are not exact")
    if value.get("schema_version") != SCHEMA_VERSION:
        raise ValueError("retry circuit schema is unsupported")
    return value


def _bounded_list(value: object, limit: int, error: str) -> list[object]:
    if not isinstance(value, list) or len(value) > limit:
        raise ValueError(error)
    return value


def _validated_collections(
    value: object,
) -> tuple[Meta, list[object], list[object], object, list[object], list[object]]:
    value = _collections(value)
    attempts = value.get("attempts")
    recoveries = value.get("recoveries")
    hold = value.get("hold")
    reservations = value.get("reservations")
    abandoned = value.get("abandoned")
    attempts = _bounded_list(attempts, MAX_ATTEMPTS, "retry circuit attempts are invalid")
    recoveries = _bounded_list(recoveries, MAX_RECOVERIES, "retry circuit recoveries are invalid")
    reservations = _bounded_list(reservations, MAX_WINDOW, "retry circuit reservations are invalid")
    abandoned = _bounded_list(abandoned, MAX_ABANDONED, "retry circuit abandoned slots are invalid")
    if not attempts and not reservations and not abandoned:
        raise ValueError("retry circuit attempts are invalid")
    return value, attempts, recoveries, hold, reservations, abandoned


def validate(value: object) -> Meta:
    value, attempts, recoveries, hold, reservations, abandoned = _validated_collections(value)
    last_revision = 0
    for attempt in attempts:
        last_revision = _validate_attempt(attempt, last_revision)
    last_recovery_revision = 0
    for recovery in recoveries:
        last_recovery_revision = _validate_recovery(recovery, last_recovery_revision)
    _validate_hold(hold, value)
    for reservation in reservations:
        _validate_reservation(reservation)
    identifiers = [cast(Meta, item)["id"] for item in reservations]
    if len(identifiers) != len(set(identifiers)):
        raise ValueError("retry circuit reservations are duplicated")
    for item in abandoned:
        _validate_abandoned(item)
    return value


def metadata_error(meta: Meta) -> str | None:
    value = meta.get("retry_circuit")
    if value is None:
        return None
    try:
        validate(value)
    except ValueError as error:
        return str(error)
    return None


def _state(meta: Meta) -> Meta:
    value = meta.get("retry_circuit")
    if value is None:
        return empty()
    if (
        isinstance(value, dict)
        and value.get("schema_version") == SCHEMA_VERSION
        and value.get("attempts") == []
        and value.get("recoveries") == []
        and value.get("hold") is None
        and value.get("reservations") == []
        and value.get("abandoned") == []
    ):
        return dict(value)
    return dict(validate(value))


def admit(meta: Meta, identity: str) -> None:
    """Reject an exact held attempt before the external command is launched."""
    state = _state(meta)
    hold = state["hold"]
    if hold is None:
        return
    current_progress = progress_digest(meta)
    if hold["identity"] == identity and hold["progress_digest"] == current_progress:
        raise RuntimeError(
            "RETRY_CIRCUIT_OPEN: repeated no-progress attempts require retry-circuit recovery"
        )


def _expired(reservation: Meta, recorded_at: str) -> bool:
    return _timestamp(reservation["expires_at"], "reservation expiry") <= _timestamp(
        recorded_at, "cleanup timestamp"
    )


def cleanup_expired(meta: Meta, recorded_at: str) -> int:
    """Durably retire only elapsed, unresolved slots before new admission."""
    state = _state(meta)
    expired = [item for item in state["reservations"] if _expired(item, recorded_at)]
    if not expired:
        return 0
    state["reservations"] = [item for item in state["reservations"] if item not in expired]
    state["abandoned"] = [
        *state["abandoned"],
        *[{**item, "cleaned_at": recorded_at, "cause": "expired"} for item in expired],
    ][-MAX_ABANDONED:]
    validate(state)
    meta["retry_circuit"] = state
    return len(expired)


def require_no_live_reservation(meta: Meta, recorded_at: str) -> None:
    """Retire elapsed slots and reject recovery while an unbound child is live."""
    cleanup_expired(meta, recorded_at)
    state = meta.get("retry_circuit")
    if isinstance(state, dict) and state["reservations"]:
        raise RuntimeError("RETRY_CIRCUIT_IN_PROGRESS: task has a live unbound retry reservation")


def record_failure(
    meta: Meta,
    identity: str,
    failure: str,
    window: int,
    recorded_at: str,
) -> str:
    """Append a failure and open the circuit exactly at the bounded threshold."""
    if failure not in FAILURES or not DIGEST.fullmatch(identity) or not recorded_at:
        raise ValueError("retry circuit failure input is invalid")
    threshold = _window(window)
    state = _state(meta)
    progress = progress_digest(meta)
    previous = _active_attempts(state, identity, progress)
    if previous and int(previous[-1]["window"]) != threshold:
        raise RuntimeError("retry circuit window changed within an active attempt series")
    state["attempts"] = [
        *state["attempts"],
        {
            "identity": identity,
            "failure": failure,
            "progress_digest": progress,
            "task_revision": int(meta["task_revision"]),
            "recorded_at": recorded_at,
            "window": threshold,
        },
    ][-MAX_ATTEMPTS:]
    count = len(previous) + 1
    if count >= threshold:
        state["hold"] = {
            "identity": identity,
            "attempts": threshold,
            "progress_digest": progress,
            "held_at": recorded_at,
            "window": threshold,
        }
        result = "Retry circuit opened after bounded unchanged failures."
    else:
        result = f"Recorded retryable failure {count}/{threshold}."
    validate(state)
    meta["retry_circuit"] = state
    return result


def reserve(
    meta: Meta,
    identity: str,
    window: int,
    reservation_id: str,
    recorded_at: str,
    expires_at: str,
) -> str:
    """Atomically consume one scoped launch slot before an external command starts."""
    threshold = _window(window)
    if (
        not DIGEST.fullmatch(identity)
        or not RESERVATION.fullmatch(reservation_id)
        or not recorded_at
    ):
        raise ValueError("retry circuit reservation input is invalid")
    if _timestamp(expires_at, "reservation expiry") <= _timestamp(
        recorded_at, "reservation timestamp"
    ):
        raise ValueError("retry circuit reservation expiry is invalid")
    cleaned = cleanup_expired(meta, recorded_at)
    state = _state(meta)
    progress = progress_digest(meta)
    admit(meta, identity)
    used = len(_active_attempts(state, identity, progress)) + sum(
        item["identity"] == identity and item["progress_digest"] == progress
        for item in state["reservations"]
    )
    if used >= threshold:
        raise RuntimeError("RETRY_CIRCUIT_OPEN: retry window is fully reserved")
    state["reservations"] = [
        *state["reservations"],
        {
            "id": reservation_id,
            "identity": identity,
            "progress_digest": progress,
            "window": threshold,
            "task_revision": int(meta["task_revision"]),
            "reserved_at": recorded_at,
            "expires_at": expires_at,
        },
    ]
    validate(state)
    meta["retry_circuit"] = state
    return f"Reserved retry circuit launch slot; expired_slots_cleaned={cleaned}."


def resolve(
    meta: Meta, identity: str, reservation_id: str, failure: str | None, recorded_at: str
) -> str:
    """Remove one exact launch slot and turn a failed launch into one attempt."""
    state = _state(meta)
    selected = next((item for item in state["reservations"] if item["id"] == reservation_id), None)
    if selected is None or selected["identity"] != identity:
        raise RuntimeError("retry circuit reservation is not current")
    state["reservations"] = [item for item in state["reservations"] if item["id"] != reservation_id]
    meta["retry_circuit"] = state
    if failure is None:
        if not state["attempts"]:
            meta.pop("retry_circuit")
        else:
            validate(state)
        return "Released retry circuit launch slot."
    return record_failure(meta, identity, failure, int(selected["window"]), recorded_at)


def resolution_revision(meta: Meta, identity: str, reservation_id: str) -> int:
    """Return the sole revision that can resolve this unbound launch slot."""
    state = _state(meta)
    selected = next((item for item in state["reservations"] if item["id"] == reservation_id), None)
    if selected is None or selected["identity"] != identity:
        raise RuntimeError("retry circuit reservation is not current")
    return int(selected["task_revision"]) + 1


def recover(meta: Meta, identity: str, kind: str, reason: str, recorded_at: str) -> str:
    """Record a deliberate recovery and reopen only the held command identity."""
    if kind not in RECOVERIES or not DIGEST.fullmatch(identity) or not recorded_at:
        raise ValueError("retry circuit recovery input is invalid")
    state = _state(meta)
    hold = state["hold"]
    if hold is None or hold["identity"] != identity:
        raise RuntimeError("retry circuit recovery requires the exact held attempt identity")
    checkpoint = str(meta.get("checkpoint_commit", ""))
    if kind == "checkpoint" and not COMMIT.fullmatch(checkpoint):
        raise RuntimeError("retry circuit checkpoint recovery requires a recorded checkpoint")
    state["recoveries"] = [
        *state["recoveries"],
        {
            "identity": identity,
            "progress_digest": progress_digest(meta),
            "kind": kind,
            "reason": _reason(reason),
            "task_revision": int(meta["task_revision"]),
            "recorded_at": recorded_at,
            "checkpoint_commit": checkpoint,
        },
    ][-MAX_RECOVERIES:]
    state["hold"] = None
    validate(state)
    meta["retry_circuit"] = state
    return f"Retry circuit recovered by {kind}."


def add_command_parser(commands: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    item = commands.add_parser("retry-circuit")
    actions = item.add_subparsers(dest="retry_circuit_action", required=True)
    status = actions.add_parser("status")
    status.add_argument("task")
    for action in RECOVERIES:
        recovery = actions.add_parser(action)
        recovery.add_argument("task")
        recovery.add_argument("--owner", required=True)
        recovery.add_argument("--expected-revision", type=int, required=True)
        recovery.add_argument("--attempt", required=True)
        recovery.add_argument("--reason", required=True)


def apply(args: argparse.Namespace, meta: Meta, recorded_at: str) -> str:
    if meta.get("owner") != args.owner or meta.get("status") != "in_progress":
        raise RuntimeError("retry circuit recovery requires the active task owner")
    if args.expected_revision != meta.get("task_revision"):
        raise RuntimeError("retry circuit recovery requires the current task revision")
    require_no_live_reservation(meta, recorded_at)
    return recover(
        meta, str(args.attempt), str(args.retry_circuit_action), str(args.reason), recorded_at
    )


def apply_reserve(args: argparse.Namespace, meta: Meta, recorded_at: str) -> str:
    if meta.get("owner") != args.owner or meta.get("status") != "in_progress":
        raise RuntimeError("retry circuit reservation requires the active task owner")
    if args.expected_revision != meta.get("task_revision"):
        raise RuntimeError("retry circuit reservation requires the current task revision")
    return reserve(
        meta,
        args.retry_circuit_identity,
        args.retry_window,
        args.retry_circuit_reservation,
        recorded_at,
        args.retry_circuit_expires_at,
    )


def apply_resolve(args: argparse.Namespace, meta: Meta, recorded_at: str) -> str:
    if meta.get("owner") != args.owner or meta.get("status") != "in_progress":
        raise RuntimeError("retry circuit resolution requires the active task owner")
    required_revision = resolution_revision(
        meta, args.retry_circuit_identity, args.retry_circuit_reservation
    )
    if (
        args.expected_revision != required_revision
        or meta.get("task_revision") != required_revision
    ):
        raise RuntimeError(
            "retry circuit resolution requires the revision immediately after its reservation"
        )
    return resolve(
        meta,
        args.retry_circuit_identity,
        args.retry_circuit_reservation,
        args.retry_circuit_failure,
        recorded_at,
    )
