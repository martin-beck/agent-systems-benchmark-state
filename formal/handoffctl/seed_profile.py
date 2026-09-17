# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Environment contract for offline guest seeds invoking verify.sh."""

from __future__ import annotations

try:
    from tier_profiles import timeout_for_tier
except ModuleNotFoundError:  # pragma: no cover - supports normal package imports
    from .tier_profiles import timeout_for_tier


def environment_for_tier(tier: str) -> dict[str, str]:
    """Return the bounded runner variables a guest seed must export."""
    return {
        "TLC_CGROUP_MODE": "required" if tier != "portable-smoke" else "portable",
        "TLC_TIMEOUT_SECONDS": str(timeout_for_tier(tier)),
        "TLC_ADDRESS_SPACE_MAX": "8G",
        "TLC_MEMORY_MAX": "3G",
        "TLC_SWAP_MAX": "3G",
    }
