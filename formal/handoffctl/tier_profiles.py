# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Pinned execution profiles for the formal verification tiers."""

from __future__ import annotations

TIER_TIMEOUT_SECONDS = {
    "portable-smoke": 1800,
    "pr-publication": 1800,
    "full-exhaustive": 7200,
}


def timeout_for_tier(tier: str) -> int:
    """Return the finite timeout bound for a known tier."""
    try:
        return TIER_TIMEOUT_SECONDS[tier]
    except KeyError as error:
        raise ValueError(f"unknown formal tier: {tier}") from error
