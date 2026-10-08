# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Emit a machine-readable, tier-specific formal execution attestation."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import time
from pathlib import Path

EXPECTED_MODELS = {
    "portable-smoke": {"HandoffctlBinding"},
    "pr-fast": {"HandoffctlFast", "OracleInteractionGates"},
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
MODEL_SOURCE = {
    "HandoffctlPR": "Handoffctl",
    "HandoffctlFast": "HandoffctlBinding",
    "OracleInteractionGates": "../oracle/OracleInteractionGates",
}
MODEL_CONFIG = {"OracleInteractionGates": "../oracle/OracleInteractionGates"}


def effective_bound(name: str, default: str, boundary: str) -> str:
    """Return a validated memory bound, requiring explicit values when required."""
    value = os.environ.get(name)
    if value is None:
        if boundary == "required":
            raise ValueError(f"required attestation needs {name}")
        value = default
    if re.fullmatch(r"[1-9][0-9]*[MG]", value) is None:
        raise ValueError(f"{name} must be a positive MiB/GiB bound")
    return value


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def candidate_identity(root: Path) -> dict[str, str]:
    """Bind source execution or a vendored downstream run to immutable candidate identity."""
    manifest_path = root / "coordinator.vendor.json"
    if manifest_path.exists():
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            upstream = manifest["upstream"]
            commit = upstream["commit"]
        except (OSError, json.JSONDecodeError, KeyError, TypeError) as error:
            raise ValueError("invalid vendor identity") from error
        schema = manifest.get("schema_version")
        if re.fullmatch(r"[0-9a-f]{40}", str(commit)) is None:
            raise ValueError("formal attestation requires an exact vendor commit")
        if schema == 2:
            tree = upstream.get("tree")
            if (
                upstream.get("channel") != "development"
                or re.fullmatch(r"[0-9a-f]{40}", str(tree)) is None
            ):
                raise ValueError("formal attestation requires an exact development vendor identity")
            kind = "development-vendor"
        elif schema == 1:
            tree = ""
            kind = "release-vendor"
        else:
            raise ValueError("formal attestation requires a supported vendor identity")
        return {
            "kind": kind,
            "commit": str(commit),
            "tree": str(tree),
            "vendor_manifest_sha256": digest(manifest_path),
        }
    commit = subprocess.check_output(
        ["git", "rev-parse", "HEAD"],  # noqa: S607
        cwd=root,
        text=True,
    ).strip()
    tree = subprocess.check_output(
        ["git", "rev-parse", "HEAD^{tree}"],  # noqa: S607
        cwd=root,
        text=True,
    ).strip()
    return {
        "kind": "source",
        "commit": commit,
        "tree": tree,
        "vendor_manifest_sha256": "",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tier", choices=tuple(EXPECTED_MODELS), required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--jar", type=Path, required=True)
    parser.add_argument("--models", nargs="+", required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument(
        "--execution-classification",
        choices=("canonical", "diagnostic-private-admission"),
        default="canonical",
    )
    parser.add_argument(
        "--status",
        choices=("success", "oom", "timeout", "canceled", "incomplete"),
        default="success",
    )
    args = parser.parse_args()
    if args.status != "success":
        parser.error("failed or incomplete formal runs cannot produce a success attestation")
    boundary = os.environ.get("TLC_CGROUP_MODE", "required")
    if args.tier not in {"portable-smoke", "pr-fast"} and boundary != "required":
        parser.error(f"{args.tier} attestation requires TLC_CGROUP_MODE=required")
    if not args.manifest.exists():
        parser.error("attestation requires the runner-produced outcome manifest")
    outcomes = {}
    for line in args.manifest.read_text(encoding="utf-8").splitlines():
        model, result = line.split(" ", 1)
        outcomes[model] = result
    if set(outcomes) != set(args.models) or any(
        result != "success" for result in outcomes.values()
    ):
        parser.error("runner outcome manifest is incomplete or non-success")
    if set(args.models) != EXPECTED_MODELS[args.tier] or len(args.models) != len(
        EXPECTED_MODELS[args.tier]
    ):
        parser.error(f"{args.tier} attestation has an unexpected model set")
    root = Path(__file__).resolve().parents[2]
    configs = {
        model: digest(root / "formal" / "handoffctl" / f"{MODEL_CONFIG.get(model, model)}.cfg")
        for model in args.models
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
            "formal/evidence.json",
            "formal/tier-evidence.json",
        )
    }
    identity = candidate_identity(root)
    formal_hash = hashlib.sha256(
        json.dumps(
            {"models": models, "configs": configs, "inputs": inputs, "candidate": identity},
            sort_keys=True,
        ).encode()
    ).hexdigest()
    try:
        memory_max = effective_bound("TLC_MEMORY_MAX", "3G", boundary)
        swap_max = effective_bound("TLC_SWAP_MAX", "3G", boundary)
    except ValueError as error:
        parser.error(str(error))
    result = {
        "schema_version": 1,
        "profile": args.tier,
        "exhaustive": args.tier == "full-exhaustive",
        "commit": identity["commit"],
        "tree": identity["tree"],
        "candidate_identity": identity,
        "formal_input_sha256": formal_hash,
        "formal_inputs": inputs,
        "models": models,
        "configs": configs,
        "tool_jar_sha256": digest(args.jar),
        "containment_mode": boundary,
        "execution_classification": args.execution_classification,
        "canonical_publication_evidence": args.execution_classification == "canonical",
        "resource_bounds": {
            "workers": 2,
            "heap": os.environ.get("TLC_HEAP", "2048m"),
            "memory_max": memory_max,
            "swap_max": swap_max,
            "timeout_seconds": int(os.environ.get("TLC_TIMEOUT_SECONDS", "1800")),
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
            *(
                [
                    "diagnostic private-admission execution is noncanonical and cannot support "
                    "release or publication claims"
                ]
                if args.execution_classification == "diagnostic-private-admission"
                else []
            ),
        ],
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
