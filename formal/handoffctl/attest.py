# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Emit a machine-readable, tier-specific formal execution attestation."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import time
from pathlib import Path

EXPECTED_MODELS = {
    "portable-smoke": {"HandoffctlBinding"},
    "pr-publication": {
        "HandoffctlBinding",
        "HandoffctlLocks",
        "HandoffctlRun",
        "HandoffctlStorage",
        "HandoffctlPR",
        "HandoffctlRecovery",
    },
    "full-exhaustive": {
        "HandoffctlBinding",
        "HandoffctlLocks",
        "HandoffctlRun",
        "HandoffctlStorage",
        "Handoffctl",
        "HandoffctlRecovery",
    },
}
MODEL_SOURCE = {"HandoffctlPR": "Handoffctl"}
TIER_KEYS = {
    "models",
    "exhaustive",
    "workers",
    "heap",
    "memory_max",
    "swap_max",
    "address_space_max",
    "timeout_seconds",
    "containment",
}
PROJECT_ROOT = Path(__file__).resolve().parents[2]
APPROVED_RUNTIME_ROOT = Path("/srv/data/projects")


def digest(path: Path) -> str:
    if not path.is_file():
        raise ValueError(f"required evidence file is missing: {path}")
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git_value(root: Path, *args: str) -> str:
    """Read one bounded Git identity value without retaining command output."""
    try:
        result = subprocess.run(  # noqa: S603
            ["git", "-C", str(root), *args],  # noqa: S607
            check=False,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,
            timeout=5,
        )
    except (OSError, subprocess.TimeoutExpired) as error:
        raise ValueError(f"Git provenance unavailable: {error}") from error
    value = result.stdout.strip()
    if result.returncode != 0 or len(value) > 128:
        raise ValueError("Git provenance command failed or returned oversized output")
    return value


def root_relative(path: Path) -> str:
    """Return an approved-root-relative path and reject host leakage."""
    try:
        return str(path.resolve().relative_to(APPROVED_RUNTIME_ROOT))
    except ValueError as error:
        raise ValueError("attestation path is outside /srv/data/projects") from error


def read_manifest(path: Path) -> dict[str, str]:
    outcomes: dict[str, str] = {}
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as error:
        raise ValueError(f"cannot read outcome manifest: {error}") from error
    for number, line in enumerate(lines, 1):
        fields = line.split()
        if len(fields) != 2 or fields[1] not in {"success", "failed"}:
            raise ValueError(f"malformed outcome manifest line {number}: expected MODEL success")
        model, result = fields
        if model in outcomes:
            raise ValueError(f"duplicate outcome manifest entry for {model}")
        outcomes[model] = result
    if not outcomes:
        raise ValueError("outcome manifest is empty")
    return outcomes


def read_tier_evidence(path: Path) -> dict[str, dict[str, object]]:  # noqa: C901
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ValueError(f"tier evidence is unreadable or malformed: {error}") from error
    if not isinstance(payload, dict) or set(payload) != {"schema_version", "tiers"}:
        raise ValueError("tier evidence must contain only schema_version and tiers")
    if payload["schema_version"] != 1 or not isinstance(payload["tiers"], dict):
        raise ValueError("tier evidence has an unsupported schema")
    tiers = payload["tiers"]
    if set(tiers) != set(EXPECTED_MODELS):
        raise ValueError("tier evidence does not describe exactly the supported tiers")
    for tier, entry in tiers.items():
        if not isinstance(entry, dict) or set(entry) != TIER_KEYS:
            raise ValueError(f"tier evidence for {tier} has unknown or missing fields")
        models = entry["models"]
        if not isinstance(models, list) or len(models) != len(set(models)):
            raise ValueError(f"tier evidence for {tier} has duplicate or invalid models")
        if set(models) != EXPECTED_MODELS[tier]:
            raise ValueError(f"tier evidence for {tier} has an unexpected model set")
        if entry["workers"] != 2:
            raise ValueError(f"tier evidence for {tier} has unsupported bounds")
        if (
            entry["heap"] != "2048m"
            or entry["memory_max"] != "3G"
            or entry["swap_max"] != "3G"
            or entry["address_space_max"] != "8G"
        ):
            raise ValueError(f"tier evidence for {tier} has unsupported memory bounds")
        expected_timeout = 7200 if tier == "full-exhaustive" else 1800
        if entry["timeout_seconds"] != expected_timeout:
            raise ValueError(f"tier evidence for {tier} has unsupported timeout")
        expected_containment = (
            "portable-timeout-prlimit" if tier == "portable-smoke" else "systemd-run-user-cgroup"
        )
        if entry["containment"] != expected_containment:
            raise ValueError(f"tier evidence for {tier} has unsupported containment")
        if entry["exhaustive"] != (tier == "full-exhaustive"):
            raise ValueError(f"tier evidence for {tier} has incorrect exhaustive flag")
    return tiers


def main() -> int:  # noqa: C901
    parser = argparse.ArgumentParser()
    parser.add_argument("--tier", choices=tuple(EXPECTED_MODELS), required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--jar", type=Path, required=True)
    parser.add_argument("--models", nargs="+", required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument(
        "--status",
        choices=("success", "oom", "timeout", "canceled", "incomplete"),
        default="success",
    )
    args = parser.parse_args()
    if args.status != "success":
        parser.error("failed or incomplete formal runs cannot produce a success attestation")
    boundary = os.environ.get("TLC_CGROUP_MODE", "required")
    if args.tier != "portable-smoke" and boundary != "required":
        parser.error(f"{args.tier} attestation requires TLC_CGROUP_MODE=required")
    if not args.manifest.exists():
        parser.error("attestation requires the runner-produced outcome manifest")
    try:
        outcomes = read_manifest(args.manifest)
    except ValueError as error:
        parser.error(str(error))
    if set(outcomes) != set(args.models) or any(
        result != "success" for result in outcomes.values()
    ):
        parser.error("runner outcome manifest is incomplete or non-success")
    if set(args.models) != EXPECTED_MODELS[args.tier] or len(args.models) != len(
        EXPECTED_MODELS[args.tier]
    ):
        parser.error(f"{args.tier} attestation has an unexpected model set")
    root = Path(__file__).resolve().parents[2]
    try:
        tiers = read_tier_evidence(root / "formal" / "tier-evidence.json")
        for path in (args.output, args.jar):
            root_relative(path)
        output_parent = args.output.resolve().parent
        output_parent.mkdir(mode=0o700, parents=True, exist_ok=True)
        output_parent.chmod(0o700)
    except ValueError as error:
        parser.error(str(error))
    evidence = tiers[args.tier]
    if boundary == "portable" and evidence["containment"] != "portable-timeout-prlimit":
        parser.error("portable execution does not match this tier's containment evidence")
    if boundary == "required" and evidence["containment"] != "systemd-run-user-cgroup":
        parser.error("required execution does not match this tier's containment evidence")
    configs = {
        model: digest(root / "formal" / "handoffctl" / f"{model}.cfg") for model in args.models
    }
    models = {
        model: digest(root / "formal" / "handoffctl" / f"{MODEL_SOURCE.get(model, model)}.tla")
        for model in args.models
    }
    inputs = {
        name: digest(root / name)
        for name in (
            "formal/handoffctl/verify.sh",
            "tools/tlc_runner.py",
            "formal/handoffctl/attest.py",
            "formal/tier-evidence.json",
            "formal/handoffctl/tier_profiles.py",
            "formal/handoffctl/seed_profile.py",
        )
    }
    try:
        commit = git_value(root, "rev-parse", "HEAD")
        tree = git_value(root, "rev-parse", "HEAD^{tree}")
        runtime_root = root_relative(
            Path(os.environ.get("TLC_RUNTIME_ROOT", str(PROJECT_ROOT / ".asb-tlc")))
        )
    except ValueError as error:
        parser.error(str(error))
    formal_hash = hashlib.sha256(
        json.dumps({"models": models, "configs": configs}, sort_keys=True).encode()
    ).hexdigest()
    result = {
        "schema_version": 1,
        "profile": args.tier,
        "exhaustive": args.tier == "full-exhaustive",
        "commit": commit,
        "tree": tree,
        "formal_input_sha256": formal_hash,
        "formal_inputs": inputs,
        "runner_provenance": {
            "runner_sha256": inputs["tools/tlc_runner.py"],
            "attest_sha256": inputs["formal/handoffctl/attest.py"],
            "launcher_sha256": os.environ.get("TLC_LAUNCHER_SHA256", ""),
            "runtime_root": runtime_root,
            "command_contract_sha256": hashlib.sha256(
                json.dumps(
                    {
                        "models": sorted(args.models),
                        "tier": args.tier,
                        "resource_bounds": evidence,
                    },
                    sort_keys=True,
                ).encode()
            ).hexdigest(),
        },
        "models": models,
        "configs": configs,
        "tool_jar_sha256": digest(args.jar),
        "containment_mode": boundary,
        "resource_bounds": {
            "workers": evidence["workers"],
            "heap": evidence["heap"],
            "memory_max": evidence["memory_max"],
            "swap_max": evidence["swap_max"],
            "address_space_max": evidence["address_space_max"],
            "timeout_seconds": evidence["timeout_seconds"],
            "admission": (
                "systemd-run-user-cgroup" if boundary == "required" else "portable-timeout-prlimit"
            ),
        },
        "outcomes": outcomes,
        "state_counts": dict.fromkeys(args.models),
        "status": "success",
        "timestamp_epoch": int(time.time()),
        "freshness_seconds": 0,
        "non_claims": [
            f"{args.tier} is non-exhaustive and cannot support full formal claims"
            if args.tier != "full-exhaustive"
            else "full-exhaustive is bounded model checking, not an implementation proof",
            "bounded model checking does not prove implementation correspondence",
            "state_counts are unavailable unless parsed from TLC output and are not evidence "
            "of exhaustive exploration",
        ],
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
