# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Bounded-age, single-flight observations for the opt-in fast-read contract."""

from __future__ import annotations

import hashlib
import json
import threading
import time
from datetime import UTC, datetime
from typing import Any

MAX_AGE_SECONDS = 300
_WAIT_SECONDS = 90.0


def validate_max_age(value: object) -> int:
    """Accept a deliberately small explicit cache-age bound."""
    if not isinstance(value, int) or isinstance(value, bool) or not 0 <= value <= MAX_AGE_SECONDS:
        raise ValueError(f"max_age_seconds must be an integer between 0 and {MAX_AGE_SECONDS}")
    return value


def _digest(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()
    ).hexdigest()


def _inputs(core: Any) -> tuple[dict[str, object], str]:
    binding = core.project_binding()
    configuration = core.config()
    value = {
        "backend": core.backend_selection(),
        "binding": binding,
        "configuration": configuration,
    }
    return value, _digest(value)


def public_observation(
    state: dict[str, object],
    *,
    input_digest: str,
    observed_at: str,
    age_ms: int,
    max_age_seconds: int,
    freshness: str,
) -> dict[str, object]:
    """Return a bounded, explicit alternate completion result."""
    return {
        "contract": "cached-observation-v1",
        "strict_equivalent": False,
        "freshness": freshness,
        "max_age_seconds": max_age_seconds,
        "age_ms": age_ms,
        "observed_at": observed_at,
        "input_sha256": input_digest,
        "observation_sha256": _digest(state),
        "observation": state,
    }


class ObservationCache:
    """One resident scan serves all concurrent fast-read callers for an input generation."""

    def __init__(self) -> None:
        self._condition = threading.Condition()
        self._refreshing = False
        self._state: dict[str, object] | None = None
        self._input_digest: str | None = None
        self._observed_at = ""
        self._observed_monotonic = 0.0
        self._generation = 0
        self._failed_generation: int | None = None
        self._failed_input_digest: str | None = None

    def observe(  # noqa: C901 - explicit cache, generation, and failure fencing
        self, core: Any, max_age_seconds: object
    ) -> dict[str, object]:
        """Scan once or return an explicitly bounded-age immutable observation."""
        maximum = validate_max_age(max_age_seconds)
        _inputs_value, input_digest = _inputs(core)
        deadline = time.monotonic() + _WAIT_SECONDS
        with self._condition:
            observed_generation = self._generation
            while True:
                if (
                    self._failed_generation is not None
                    and observed_generation <= self._failed_generation
                    and input_digest == self._failed_input_digest
                ):
                    raise RuntimeError("OBSERVATION_INPUT_CHANGED: retry fast observe")
                age = max(0.0, time.monotonic() - self._observed_monotonic)
                if (
                    maximum > 0
                    and self._state is not None
                    and self._input_digest == input_digest
                    and age <= maximum
                ):
                    return public_observation(
                        self._state,
                        input_digest=input_digest,
                        observed_at=self._observed_at,
                        age_ms=round(age * 1000),
                        max_age_seconds=maximum,
                        freshness="bounded-cache",
                    )
                # A zero-age caller does not reuse a completed cache entry,
                # but it must receive the scan it was already waiting for.
                # Otherwise each waiter would immediately begin another scan
                # when the first result becomes a few microseconds old.
                if (
                    self._generation > observed_generation
                    and self._state is not None
                    and self._input_digest == input_digest
                ):
                    return public_observation(
                        self._state,
                        input_digest=input_digest,
                        observed_at=self._observed_at,
                        age_ms=round(age * 1000),
                        max_age_seconds=maximum,
                        freshness="fresh-scan",
                    )
                if not self._refreshing:
                    self._refreshing = True
                    break
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    raise RuntimeError("fast observation refresh did not complete")
                self._condition.wait(remaining)
        try:
            state = core.project_scan()
            _current_inputs, current_digest = _inputs(core)
            if current_digest != input_digest:
                raise RuntimeError("OBSERVATION_INPUT_CHANGED: retry fast observe")
            observed_at = datetime.now(UTC).isoformat().replace("+00:00", "Z")
            observed_monotonic = time.monotonic()
        except RuntimeError as error:
            with self._condition:
                if str(error).startswith("OBSERVATION_INPUT_CHANGED:"):
                    self._failed_generation = self._generation
                    self._failed_input_digest = input_digest
                    self._generation += 1
                self._refreshing = False
                self._condition.notify_all()
            raise
        except Exception:
            with self._condition:
                self._refreshing = False
                self._condition.notify_all()
            raise
        with self._condition:
            self._state = state
            self._input_digest = input_digest
            self._observed_at = observed_at
            self._observed_monotonic = observed_monotonic
            self._generation += 1
            self._refreshing = False
            self._condition.notify_all()
        return public_observation(
            state,
            input_digest=input_digest,
            observed_at=observed_at,
            age_ms=0,
            max_age_seconds=maximum,
            freshness="fresh-scan",
        )
