# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Environment contract for offline guest seeds invoking verify.sh."""

from __future__ import annotations

import importlib
from collections.abc import Callable
from typing import cast


def _timeout_for_tier(tier: str) -> int:
    """Load the profile from either the script or package execution context."""
    try:
        module = importlib.import_module("tier_profiles")
    except ModuleNotFoundError:  # pragma: no cover - package execution fallback
        module = importlib.import_module("formal.handoffctl.tier_profiles")
    timeout_for_tier = cast(Callable[[str], int], module.timeout_for_tier)
    return timeout_for_tier(tier)


def environment_for_tier(tier: str) -> dict[str, str]:
    """Return the bounded runner variables a guest seed must export."""
    return {
        "TLC_CGROUP_MODE": "required" if tier != "portable-smoke" else "portable",
        "TLC_TIMEOUT_SECONDS": str(_timeout_for_tier(tier)),
        "TLC_ADDRESS_SPACE_MAX": "8G",
        "TLC_MEMORY_MAX": "3G",
        "TLC_SWAP_MAX": "3G",
    }
