# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Bounded, privacy-safe audit records for abandoned execution reservations."""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import re
from typing import Any

type Meta = dict[str, Any]

_DIGEST = re.compile(r"^sha256:[0-9a-f]{64}$")
_EXECUTION_ID = re.compile(r"^[0-9a-f]{32}$")
_REF = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._/-]{2,255}$")
MAX_RECORDS = 32


def reservation_digest(reservation: Meta) -> str:
    """Return the stable digest bound into an abandonment audit record."""
    payload = json.dumps(reservation, sort_keys=True, separators=(",", ":")).encode()
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def valid(record: object) -> bool:
    """Recognize one closed, locally evidenced execution abandonment record."""
    fields = {
        "schema_version",
        "execution_id",
        "owner",
        "reservation_digest",
        "evidence_ref",
        "evidence_digest",
        "recorded_at",
    }
    if not isinstance(record, dict) or set(record) != fields:
        return False
    if (
        record.get("schema_version") != 1
        or not _EXECUTION_ID.fullmatch(str(record.get("execution_id", "")))
        or not isinstance(record.get("owner"), str)
        or not record["owner"]
        or not _DIGEST.fullmatch(str(record.get("reservation_digest", "")))
        or not isinstance(record.get("evidence_ref"), str)
        or not _public_evidence_ref(record["evidence_ref"])
        or not _DIGEST.fullmatch(str(record.get("evidence_digest", "")))
    ):
        return False
    try:
        recorded_at = dt.datetime.fromisoformat(
            str(record.get("recorded_at", "")).replace("Z", "+00:00")
        )
    except ValueError:
        return False
    return recorded_at.tzinfo is not None and recorded_at.utcoffset() is not None


def _public_evidence_ref(value: str) -> bool:
    """Allow a portable reference, never a private or traversing location."""
    if _REF.fullmatch(value) is None:
        return False
    components = value.split("/")
    return all(component not in {".", "..", "private"} for component in components)


def valid_records(value: object) -> bool:
    """Accept no records or one bounded, append-only-looking sequence."""
    return value is None or (
        isinstance(value, list)
        and len(value) <= MAX_RECORDS
        and all(valid(record) for record in value)
        and len({str(record["execution_id"]) for record in value if isinstance(record, dict)})
        == len(value)
    )


def build(reservation: Meta, args: Any, recorded_at: str) -> Meta:
    """Build an exact-reservation record after runtime admission has succeeded."""
    record: Meta = {
        "schema_version": 1,
        "execution_id": args.execution_id,
        "owner": reservation["owner"],
        "reservation_digest": reservation_digest(reservation),
        "evidence_ref": args.evidence_ref,
        "evidence_digest": args.evidence_digest,
        "recorded_at": recorded_at,
    }
    if not valid(record):
        raise ValueError("invalid execution abandonment evidence")
    return record
