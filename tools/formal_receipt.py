# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Validate a bounded formal receipt against one immutable local candidate.

The validator is intentionally local: an Actions artifact may carry this
receipt, but neither an Actions identity nor an external approval is an input
to the decision. Callers supply the candidate they checked out and this tool
reconstructs the model, configuration, and budget contract from that tree.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any


class FormalReceiptError(ValueError):
    """Raised when a receipt is stale, incomplete, or outside its fixed contract."""


_MODEL_SOURCE = {"HandoffctlLiveness": "Handoffctl"}
_MODEL_CONFIG: dict[str, str] = {}
_RESOURCE_OUTCOMES = frozenset({"storage-exhausted", "admission-failed", "oom"})
_TIMEOUT_OUTCOMES = frozenset({"timeout", "timed-out", "deadline-exceeded"})


def _digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _object_id(value: object) -> str:
    if (
        not isinstance(value, str)
        or len(value) != 40
        or any(character not in "0123456789abcdef" for character in value)
    ):
        raise FormalReceiptError("candidate must be a lowercase 40-character Git object id")
    return value


def expected_candidate(root: Path) -> str:
    """Read the exact source candidate rather than trusting CI environment variables."""
    result = subprocess.run(
        ["/usr/bin/git", "rev-parse", "HEAD"],
        cwd=root,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise FormalReceiptError("cannot resolve exact checked-out candidate")
    return _object_id(result.stdout.strip())


def expected_contract(root: Path, tier: str) -> dict[str, Any]:
    """Return model/configuration and aggregate-budget contract from this tree."""
    try:
        profiles = json.loads((root / "formal/tier-evidence.json").read_text(encoding="utf-8"))[
            "profiles"
        ]
        profile = profiles[tier]
        models = profile["models"]
        budget = profile["aggregate_budget_seconds"]
    except (OSError, json.JSONDecodeError, KeyError, TypeError) as error:
        raise FormalReceiptError("formal tier contract is unreadable") from error
    if (
        not isinstance(models, list)
        or not models
        or len(models) != len(set(models))
        or not all(isinstance(model, str) for model in models)
        or not isinstance(budget, int)
        or budget < 1
    ):
        raise FormalReceiptError("formal tier contract is malformed")
    formal = root / "formal/handoffctl"
    try:
        return {
            "models": {
                model: _digest(formal / f"{_MODEL_SOURCE.get(model, model)}.tla")
                for model in models
            },
            "configs": {
                model: _digest(formal / f"{_MODEL_CONFIG.get(model, model)}.cfg")
                for model in models
            },
            "budget_seconds": budget,
        }
    except OSError as error:
        raise FormalReceiptError("formal tier inputs are unreadable") from error


def _outcome_error(receipt: dict[str, Any]) -> None:
    state = receipt.get("status")
    outcomes = receipt.get("outcomes")
    values = [state]
    if isinstance(outcomes, dict):
        values.extend(outcomes.values())
    if any(value in _TIMEOUT_OUTCOMES for value in values):
        raise FormalReceiptError(
            "formal receipt reports timeout; inspect bounds or reduce the tier"
        )
    if any(value in _RESOURCE_OUTCOMES for value in values):
        raise FormalReceiptError(
            "formal receipt reports resource exhaustion; inspect runner diagnostics"
        )
    if (
        state != "success"
        or not isinstance(outcomes, dict)
        or any(value != "success" for value in outcomes.values())
    ):
        raise FormalReceiptError("formal receipt is incomplete or unsuccessful")


def validate_receipt(receipt: dict[str, Any], *, root: Path, candidate: str, tier: str) -> None:
    """Require a successful receipt for precisely this source candidate and tier."""
    candidate = _object_id(candidate)
    if candidate != expected_candidate(root):
        raise FormalReceiptError("requested candidate is not the exact checked-out head")
    _outcome_error(receipt)
    identity = receipt.get("candidate_identity")
    if (
        not isinstance(identity, dict)
        or receipt.get("commit") != candidate
        or identity.get("commit") != candidate
    ):
        raise FormalReceiptError("formal receipt candidate is stale or belongs to another head")
    if receipt.get("profile") != tier:
        raise FormalReceiptError("formal receipt tier does not match the requested bounded tier")
    contract = expected_contract(root, tier)
    if receipt.get("models") != contract["models"]:
        raise FormalReceiptError(
            "formal receipt model digest does not match the checked-out candidate"
        )
    if receipt.get("configs") != contract["configs"]:
        raise FormalReceiptError(
            "formal receipt configuration digest does not match the checked-out candidate"
        )
    budget = receipt.get("verifier_budget")
    if not isinstance(budget, dict) or budget.get("declared_seconds") != contract["budget_seconds"]:
        raise FormalReceiptError("formal receipt does not retain the tier budget")
    elapsed = budget.get("elapsed_seconds")
    if not isinstance(elapsed, int) or elapsed < 0 or elapsed > contract["budget_seconds"]:
        raise FormalReceiptError("formal receipt exceeded its declared tier budget")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--receipt", type=Path, required=True)
    parser.add_argument("--candidate", required=True)
    parser.add_argument("--tier", required=True)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    try:
        receipt = json.loads(args.receipt.read_text(encoding="utf-8"))
        if not isinstance(receipt, dict):
            raise FormalReceiptError("formal receipt must be a JSON object")
        validate_receipt(
            receipt, root=args.root.resolve(), candidate=args.candidate, tier=args.tier
        )
    except (OSError, json.JSONDecodeError, FormalReceiptError) as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
