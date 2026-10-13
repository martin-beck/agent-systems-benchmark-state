# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Validation and construction for reservation-bound terminal receipts."""

from __future__ import annotations

import datetime as dt
import re
from typing import Any


def valid(value: object) -> bool:
    """Validate one privacy-safe terminal receipt."""
    fields = {
        "execution_id",
        "owner",
        "envelope_digest",
        "argv_digest",
        "classification",
        "returncode",
        "recorded_at",
    }
    if not isinstance(value, dict) or set(value) != fields:
        return False
    if (
        not re.fullmatch(r"[0-9a-f]{32}", str(value.get("execution_id", "")))
        or not isinstance(value.get("owner"), str)
        or not value["owner"]
        or not re.fullmatch(r"sha256:[0-9a-f]{64}", str(value.get("envelope_digest", "")))
        or not re.fullmatch(r"[0-9a-f]{64}", str(value.get("argv_digest", "")))
        or value.get("classification") not in {"EXIT", "SUBPROCESS_TIMEOUT"}
        or isinstance(value.get("returncode"), bool)
        or not isinstance(value.get("returncode"), int)
    ):
        return False
    try:
        recorded_at = dt.datetime.fromisoformat(
            str(value.get("recorded_at", "")).replace("Z", "+00:00")
        )
    except ValueError:
        return False
    return recorded_at.tzinfo is not None and recorded_at.utcoffset() is not None


def matches(reservation: dict[str, Any], result: object) -> bool:
    """Return whether a receipt proves completion of this exact reservation."""
    if not valid(result) or not isinstance(result, dict):
        return False
    return all(
        result[key] == reservation[key]
        for key in ("execution_id", "owner", "envelope_digest", "argv_digest")
    )


def build(reservation: dict[str, Any], args: Any) -> dict[str, Any]:
    """Construct one receipt only for the owner and identity of a reservation."""
    if reservation.get("execution_id") != args.execution_id:
        raise ValueError("execution reservation no longer matches this command")
    if reservation.get("owner") != args.owner:
        raise ValueError("execution reservation owner does not match")
    result = {
        "execution_id": args.execution_id,
        "owner": args.owner,
        "envelope_digest": reservation["envelope_digest"],
        "argv_digest": reservation["argv_digest"],
        "classification": args.classification,
        "returncode": args.returncode,
        "recorded_at": args.recorded_at,
    }
    if not valid(result):
        raise ValueError("invalid execution result")
    return result
