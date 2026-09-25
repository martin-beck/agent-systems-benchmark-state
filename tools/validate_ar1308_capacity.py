# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Fail-closed live receipt and capacity preflight for AR-1308."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import shutil
import subprocess
from pathlib import Path
from typing import Any

GIB = 1024**3
REQUIRED_COMMIT = "ab485f767fbddbd8adfc27b5120f3df0a045b762"
REQUIRED_IMAGE_SHA256 = "612b2c0cc1bc413a6cb8c38fd611794caf0f2b436c50013d8b3794db12ad7354"
REQUIRED_TLC_SHA256 = "936a262061c914694dfd669a543be24573c45d5aa0ff20a8b96b23d01e050e88"
PROFILES = {"signed", "unsigned-development"}
MIN_GUEST_MEMORY = 48 * GIB
MIN_HOST_MEMORY = 56 * GIB
MIN_HOST_DISK = 16 * GIB
MIN_HOST_SWAP = 1 * GIB
CONTRACT = {
    "address_space_max": "8G",
    "cpu_quota": "200%",
    "memory_max": "3G",
    "swap_max": "3G",
    "timeout_seconds": 7200,
    "workers": 2,
}
RECEIPT_KEYS = {
    "architecture",
    "disposable",
    "guest_memory_bytes",
    "guest_swap_bytes",
    "guest_disk_bytes",
    "host_mounts",
    "hypervisor",
    "image_sha256",
    "image_id",
    "network",
    "pinned_inputs",
    "process_contract",
    "overlay_id",
    "runner_id",
    "vcpus",
    "model_config_sha256",
    "seed_sha256",
    "source_tree_sha256",
    "validator_sha256",
    "admission_lock_id",
    "cleanup_policy",
}


def _string(data: dict[str, Any], key: str) -> str:
    value = data.get(key)
    return value if isinstance(value, str) else ""


def _hex(value: str) -> bool:
    return len(value) == 64 and all(char in "0123456789abcdef" for char in value)


def _validate_isolation(receipt: dict[str, Any]) -> list[str]:
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


def _validate_capacity(receipt: dict[str, Any]) -> list[str]:
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
    if _string(receipt, "hypervisor") != "qemu-system-x86_64 8.2.2":
        issues.append("hypervisor must be the pinned QEMU x86_64 8.2.2")
    return issues


def _validate_inputs(receipt: dict[str, Any], profile: str = "signed") -> list[str]:
    issues: list[str] = []
    inputs = receipt.get("pinned_inputs")
    commit = inputs.get("ar1307_commit") if isinstance(inputs, dict) else None
    if profile == "signed":
        if commit != REQUIRED_COMMIT:
            issues.append("pinned input is not the exact signed AR-1307 head")
    elif not isinstance(commit, str) or len(commit) != 40 or any(
        char not in "0123456789abcdef" for char in commit
    ):
        issues.append("diagnostic pinned input must name a lowercase Git commit")
    if not isinstance(inputs, dict) or inputs.get("jdk_major") != 17:
        issues.append("pinned JDK must be major version 17")
    if not isinstance(inputs, dict) or inputs.get("tlc_jar_sha256") != REQUIRED_TLC_SHA256:
        issues.append("pinned TLC artifact digest is not the reviewed artifact")
    digest_keys = (
        "image_sha256",
        "model_config_sha256",
        "seed_sha256",
        "source_tree_sha256",
        "validator_sha256",
    )
    issues.extend(
        f"{key} must be a lowercase SHA-256 digest"
        for key in digest_keys
        if not _hex(_string(receipt, key))
    )
    if _string(receipt, "image_sha256") != REQUIRED_IMAGE_SHA256:
        issues.append("image digest is not the reviewed Ubuntu 24.04 image")
    return issues


def validate_receipt(receipt: dict[str, Any], profile: str = "signed") -> list[str]:
    """Validate the closed receipt schema and unchanged process contract."""
    issues: list[str] = []
    if profile not in PROFILES:
        issues.append("profile must be signed or unsigned-development")
    if set(receipt) - RECEIPT_KEYS:
        issues.append("receipt contains unknown fields")
    issues.extend(_validate_isolation(receipt))
    issues.extend(_validate_capacity(receipt))
    issues.extend(_validate_inputs(receipt, profile))
    if receipt.get("process_contract") != CONTRACT:
        issues.append("process contract must remain 8G AS, 3G/3G, 200%, 2 workers, 7200 seconds")
    if (
        not _string(receipt, "runner_id")
        or not _string(receipt, "image_id")
        or not _string(receipt, "overlay_id")
        or not _string(receipt, "admission_lock_id")
    ):
        issues.append("runner, image, overlay and admission identities are required")
    if _string(receipt, "cleanup_policy") != "bounded-reap-and-delete":
        issues.append("cleanup policy must be bounded-reap-and-delete")
    return issues


def _digest(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def host_capacity(root: Path) -> dict[str, int | str]:
    """Measure bounded host memory, swap, disk and inode capacity."""
    values: dict[str, int | str] = {"architecture": platform.machine()}
    for line in Path("/proc/meminfo").read_text(encoding="utf-8").splitlines():
        fields = line.split()
        if fields and fields[0] in {"MemAvailable:", "SwapFree:"} and len(fields) > 1:
            values[fields[0][:-1].lower() + "_bytes"] = int(fields[1]) * 1024
    values["available_disk_bytes"] = shutil.disk_usage(root).free
    values["available_inodes"] = os.statvfs(root).f_favail
    return values


def validate_host(capacity: dict[str, int | str]) -> list[str]:
    """Reject insufficient architecture, memory, swap, disk or inodes."""
    issues: list[str] = []
    if capacity.get("architecture") != "x86_64":
        issues.append("host architecture must be x86_64")
    if int(capacity.get("memavailable_bytes", 0)) < MIN_HOST_MEMORY:
        issues.append("host available memory is below guest plus runtime headroom")
    if int(capacity.get("swapfree_bytes", 0)) < MIN_HOST_SWAP:
        issues.append("host available swap is below the safe preflight floor")
    if int(capacity.get("available_disk_bytes", 0)) < MIN_HOST_DISK:
        issues.append("approved root lacks required disk headroom")
    if int(capacity.get("available_inodes", 0)) < 10000:
        issues.append("approved root lacks required inode headroom")
    return issues


def _run(argv: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(  # noqa: S603
        argv, check=False, capture_output=True, text=True, timeout=10
    )


def _validate_vm(image: Path, overlay: Path) -> list[str]:
    issues: list[str] = []
    if not image.is_file() or _digest(image) != REQUIRED_IMAGE_SHA256:
        issues.append("image file is missing or has the wrong digest")
    if not overlay.is_file():
        issues.append("overlay is missing")
    qemu = _run(["qemu-system-x86_64", "--version"])
    if qemu.returncode != 0 or "8.2.2" not in qemu.stdout:
        issues.append("installed QEMU is not pinned to 8.2.2")
    info = _run(["qemu-img", "info", "--output=json", str(overlay)])
    if info.returncode != 0:
        issues.append("overlay metadata is unreadable")
    else:
        try:
            if int(json.loads(info.stdout)["virtual-size"]) < 64 * GIB:
                issues.append("overlay virtual disk is below 64 GiB")
        except (KeyError, TypeError, ValueError, json.JSONDecodeError):
            issues.append("overlay metadata is malformed")
    return issues


def _validate_source(
    receipt: dict[str, Any], source: Path, profile: str = "signed"
) -> list[str]:
    issues: list[str] = []
    if not source.is_dir() or not (source / ".git").exists():
        return ["exact source checkout is missing Git metadata"]
    head = _run(["git", "-C", str(source), "rev-parse", "HEAD"])
    tree = _run(["git", "-C", str(source), "ls-tree", "-r", "--full-tree", "HEAD"])
    pinned_inputs = receipt.get("pinned_inputs")
    expected = pinned_inputs.get("ar1307_commit") if isinstance(pinned_inputs, dict) else None
    verified = _run(["git", "-C", str(source), "verify-commit", "HEAD"])
    if profile == "signed":
        if head.stdout.strip() != REQUIRED_COMMIT or verified.returncode != 0:
            issues.append("source is not the exact signed AR-1307 commit")
    elif head.stdout.strip() != expected:
        issues.append("diagnostic source does not match its pinned Git commit")
    if hashlib.sha256(tree.stdout.encode()).hexdigest() != _string(receipt, "source_tree_sha256"):
        issues.append("source tree identity does not match the receipt")
    return issues


def _validate_artifacts(
    receipt: dict[str, Any], model: Path, seed: Path, jdk: Path, jar: Path, lock: Path
) -> list[str]:
    issues: list[str] = []
    if not model.is_file() or _digest(model) != _string(receipt, "model_config_sha256"):
        issues.append("model/config input is missing or has the wrong digest")
    if not seed.is_file() or _digest(seed) != _string(receipt, "seed_sha256"):
        issues.append("seed input is missing or has the wrong digest")
    if not lock.exists() or lock.stat().st_mode & 0o002:
        issues.append("admission-lock input is missing or writable by other users")
    if not jdk.is_dir() or not (jdk / "bin/java").is_file():
        issues.append("pinned JDK is missing")
    else:
        java = _run([str(jdk / "bin/java"), "-version"])
        if java.returncode != 0 or 'version "17.' not in java.stderr:
            issues.append("pinned JDK is not major version 17")
    if not jar.is_file() or _digest(jar) != REQUIRED_TLC_SHA256:
        issues.append("pinned TLC JAR is missing or has the wrong digest")
    return issues


def validate_live(
    receipt: dict[str, Any],
    root: Path,
    image: Path,
    overlay: Path,
    source: Path,
    model: Path,
    seed: Path,
    jdk: Path,
    jar: Path,
    lock: Path,
    profile: str = "signed",
) -> list[str]:
    """Bind receipt identities to the actual immutable live inputs."""
    issues = validate_host(host_capacity(root))
    issues.extend(_validate_vm(image, overlay))
    issues.extend(_validate_source(receipt, source, profile))
    issues.extend(_validate_artifacts(receipt, model, seed, jdk, jar, lock))
    return issues


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    for name in (
        "receipt",
        "runtime-root",
        "image",
        "overlay",
        "source",
        "model",
        "seed",
        "jdk",
        "tlc-jar",
        "admission-lock",
    ):
        parser.add_argument(f"--{name}", type=Path, required=True)
    parser.add_argument(
        "--profile",
        choices=sorted(PROFILES),
        default="signed",
        help="explicitly select signed qualification or diagnostic unsigned development",
    )
    args = parser.parse_args(argv)
    try:
        receipt = json.loads(args.receipt.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        print(f"AR-1308 preflight failed: unreadable receipt ({error})")
        return 2
    issues = (
        validate_receipt(receipt, args.profile)
        if isinstance(receipt, dict)
        else ["receipt must be a JSON object"]
    )
    if isinstance(receipt, dict):
        issues.extend(
            validate_live(
                receipt,
                args.runtime_root,
                args.image,
                args.overlay,
                args.source,
                args.model,
                args.seed,
                args.jdk,
                args.tlc_jar,
                args.admission_lock,
                args.profile,
            )
        )
    if issues:
        print("AR-1308 preflight failed: " + "; ".join(issues))
        return 1
    result = {
        "profile": args.profile,
        "qualification_authorized": args.profile == "signed",
        "runner_id": receipt["runner_id"],
        "status": "ready" if args.profile == "signed" else "diagnostic",
    }
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
