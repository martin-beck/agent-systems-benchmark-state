# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Generate the offline guest command contract for a formal tier."""
# ruff: noqa: E501

from __future__ import annotations

from formal.handoffctl.seed_profile import environment_for_tier


def build_user_data(tier: str) -> str:
    env = environment_for_tier(tier)
    timeout = env["TLC_TIMEOUT_SECONDS"]
    mode = env["TLC_CGROUP_MODE"]
    return f"""#cloud-config
runcmd:
  - [sh, -c, 'export TLC_CGROUP_MODE={mode} TLC_TIMEOUT_SECONDS={timeout} TLC_ADDRESS_SPACE_MAX=8G TLC_MEMORY_MAX=3G TLC_SWAP_MAX=3G; cd /mnt/asb-data/state; ./formal/handoffctl/verify.sh --tier {tier}']
  - [sh, -c, 'systemd-run --user --property=RuntimeMaxSec={timeout} --property=MemoryMax=3G --property=MemorySwapMax=3G --property=CPUQuota=200% --property=TasksMax=64 -- /bin/true']
"""
