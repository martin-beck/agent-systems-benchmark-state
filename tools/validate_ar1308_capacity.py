# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Fail-closed receipt and host-capacity preflight for AR-1308."""

from __future__ import annotations

import argparse
import json
import platform
import shutil
from pathlib import Path
from typing import Any

GIB = 1024**3
REQUIRED_COMMIT = "ab485f767"
REQUIRED_IMAGE_SHA256 = "612b2c0cc1bc413a6cb8c38fd611794caf0f2b436c50013d8b3794db12ad7354"
MIN_GUEST_MEMORY = 48 * GIB
MIN_HOST_MEMORY = 56 * GIB
MIN_HOST_DISK = 16 * GIB


def _string(data: dict[str, Any], key: str) -> str:
    value = data.get(key)
    return value if isinstance(value, str) else ""


def _validate_isolation(receipt: dict[str, Any]) -> list[str]:
    """Validate isolation fields."""
    issues: list[str] = []
    if _string(receipt, "architecture") != "x86_64":
        issues.append("receipt architecture must be x86_64")
    if receipt.get("disposable") is not True:
        issues.append("receipt must declare disposable=true")
    if receipt.get("host_mounts") is not False:
        issues.append("receipt must declare host_mounts=false")
    if _string(receipt, "network") != "none":
        issues.append("receipt network must be none")
    return issues


def _validate_guest_capacity(receipt: dict[str, Any]) -> list[str]:
    """Validate guest capacity fields."""
    issues: list[str] = []
    if (
        not isinstance(receipt.get("guest_memory_bytes"), int)
        or receipt["guest_memory_bytes"] < MIN_GUEST_MEMORY
    ):
        issues.append("guest memory must be at least 48 GiB")
    if receipt.get("guest_swap_bytes") != 16 * GIB:
        issues.append("guest swap must be exactly 16 GiB")
    if (
        not isinstance(receipt.get("guest_disk_bytes"), int)
        or receipt["guest_disk_bytes"] < 64 * GIB
    ):
        issues.append("guest disk must provide at least 64 GiB virtual capacity")
    if receipt.get("vcpus") != 8:
        issues.append("guest vCPUs must be exactly 8")
    image = receipt.get("image")
    if not isinstance(image, dict) or _string(image, "sha256") != REQUIRED_IMAGE_SHA256:
        issues.append("image digest is not the reviewed Ubuntu 24.04 image")
    return issues


def _validate_inputs(receipt: dict[str, Any]) -> list[str]:
    """Validate immutable image and tool inputs."""
    issues: list[str] = []
    inputs = receipt.get("pinned_inputs")
    if not isinstance(inputs, dict) or _string(inputs, "ar1307_commit") != REQUIRED_COMMIT:
        issues.append("pinned input is not the exact signed AR-1307 head")
    if not isinstance(inputs, dict) or inputs.get("jdk_major") != 17:
        issues.append("pinned JDK must be major version 17")
    if not isinstance(inputs, dict) or len(_string(inputs, "tlc_jar_sha256")) != 64:
        issues.append("pinned TLC artifact must have a SHA-256 digest")
    return issues


def _validate_contract(receipt: dict[str, Any]) -> list[str]:
    """Validate the unchanged AR-1307 process contract."""
    issues: list[str] = []
    contract = receipt.get("process_contract")
    expected = {
        "address_space_max": "8G",
        "cpu_quota": "200%",
        "memory_max": "3G",
        "swap_max": "3G",
        "timeout_seconds": 7200,
        "workers": 2,
    }
    if contract != expected:
        issues.append("process contract must remain 8G AS, 3G/3G, 200%, 2 workers, 7200 seconds")
    return issues


def validate_receipt(receipt: dict[str, Any]) -> list[str]:
    """Return actionable violations without exposing machine-specific data."""
    issues = _validate_isolation(receipt)
    issues.extend(_validate_guest_capacity(receipt))
    issues.extend(_validate_inputs(receipt))
    issues.extend(_validate_contract(receipt))
    if not _string(receipt, "runner_id"):
        issues.append("runner_id is required")
    return issues


def host_capacity(root: Path) -> dict[str, int | str]:
    """Measure only bounded numeric host capacity under the approved root."""
    memory = 0
    for line in Path("/proc/meminfo").read_text(encoding="utf-8").splitlines():
        if line.startswith("MemAvailable:"):
            memory = int(line.split()[1]) * 1024
            break
    disk = shutil.disk_usage(root)
    return {
        "architecture": platform.machine(),
        "available_memory_bytes": memory,
        "available_disk_bytes": disk.free,
    }


def validate_host(capacity: dict[str, int | str]) -> list[str]:
    """Return fail-closed host-capacity violations."""
    issues: list[str] = []
    if capacity.get("architecture") != "x86_64":
        issues.append("host architecture must be x86_64")
    if int(capacity.get("available_memory_bytes", 0)) < MIN_HOST_MEMORY:
        issues.append("host available memory is below the guest plus runtime headroom")
    if int(capacity.get("available_disk_bytes", 0)) < MIN_HOST_DISK:
        issues.append("approved root lacks the required disk headroom")
    return issues


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--receipt", type=Path, required=True)
    parser.add_argument("--skip-host", action="store_true")
    args = parser.parse_args(argv)
    try:
        receipt = json.loads(args.receipt.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        print(f"AR-1308 preflight failed: unreadable receipt ({error})")
        return 2
    issues = (
        validate_receipt(receipt)
        if isinstance(receipt, dict)
        else ["receipt must be a JSON object"]
    )
    if not args.skip_host:
        issues.extend(validate_host(host_capacity(Path("/srv/data/projects"))))
    if issues:
        print("AR-1308 preflight failed: " + "; ".join(issues))
        return 1
    print(json.dumps({"status": "ready", "runner_id": receipt["runner_id"]}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
