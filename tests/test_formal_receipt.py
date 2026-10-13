# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Deterministic exact-head validation for bounded formal receipts."""

from __future__ import annotations

import copy
import json
import subprocess
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

from tools import formal_receipt
from tools.formal_receipt import (
    FormalReceiptError,
    expected_candidate,
    expected_contract,
    validate_receipt,
)

ROOT = Path(__file__).resolve().parent.parent
TIER = "pr-publication"


def receipt() -> dict[str, object]:
    contract = expected_contract(ROOT, TIER)
    candidate = expected_candidate(ROOT)
    return {
        "status": "success",
        "profile": TIER,
        "commit": candidate,
        "candidate_identity": {"kind": "source", "commit": candidate},
        "models": contract["models"],
        "configs": contract["configs"],
        "outcomes": dict.fromkeys(contract["models"], "success"),
        "verifier_budget": {"declared_seconds": contract["budget_seconds"], "elapsed_seconds": 1},
    }


class FormalReceiptTests(unittest.TestCase):
    def test_accepts_exact_head_and_declared_bounded_contract(self) -> None:
        validate_receipt(receipt(), root=ROOT, candidate=expected_candidate(ROOT), tier=TIER)

    def test_rejects_stale_candidate_fixture(self) -> None:
        value = receipt()
        value["commit"] = "a" * 40
        value["candidate_identity"] = {"kind": "source", "commit": "a" * 40}
        with self.assertRaisesRegex(FormalReceiptError, "stale"):
            validate_receipt(value, root=ROOT, candidate=expected_candidate(ROOT), tier=TIER)

    def test_rejects_resource_exhaustion_fixture(self) -> None:
        value = copy.deepcopy(receipt())
        outcomes = value["outcomes"]
        assert isinstance(outcomes, dict)
        outcomes["HandoffctlStorage"] = "storage-exhausted"
        with self.assertRaisesRegex(FormalReceiptError, "resource exhaustion"):
            validate_receipt(value, root=ROOT, candidate=expected_candidate(ROOT), tier=TIER)

    def test_rejects_timeout_fixture(self) -> None:
        value = receipt()
        value["status"] = "timeout"
        with self.assertRaisesRegex(FormalReceiptError, "timeout"):
            validate_receipt(value, root=ROOT, candidate=expected_candidate(ROOT), tier=TIER)

    def test_rejects_budget_and_model_configuration_drift(self) -> None:
        value = receipt()
        budget = value["verifier_budget"]
        assert isinstance(budget, dict)
        budget["elapsed_seconds"] = 901
        with self.assertRaisesRegex(FormalReceiptError, "budget"):
            validate_receipt(value, root=ROOT, candidate=expected_candidate(ROOT), tier=TIER)
        value = receipt()
        models = value["models"]
        assert isinstance(models, dict)
        models["HandoffctlLiveness"] = "0" * 64
        with self.assertRaisesRegex(FormalReceiptError, "model digest"):
            validate_receipt(value, root=ROOT, candidate=expected_candidate(ROOT), tier=TIER)

    def test_rejects_invalid_requested_candidate_and_unresolvable_head(self) -> None:
        with self.assertRaisesRegex(FormalReceiptError, "40-character"):
            validate_receipt(receipt(), root=ROOT, candidate="not-an-object", tier=TIER)
        with (
            patch(
                "tools.formal_receipt.subprocess.run",
                return_value=subprocess.CompletedProcess(["git"], 1, "", "missing"),
            ),
            self.assertRaisesRegex(FormalReceiptError, "cannot resolve"),
        ):
            expected_candidate(ROOT)

    def test_rejects_unreadable_or_malformed_tier_contract(self) -> None:
        with (
            self.subTest("malformed-json"),
            patch.object(Path, "read_text", return_value="not-json"),
            self.assertRaisesRegex(FormalReceiptError, "unreadable"),
        ):
            expected_contract(ROOT, TIER)
        with (
            self.subTest("missing-tier"),
            patch.object(Path, "read_text", return_value=json.dumps({"profiles": {}})),
            self.assertRaisesRegex(FormalReceiptError, "unreadable"),
        ):
            expected_contract(ROOT, TIER)
        with self.subTest("invalid-budget"):
            bad = {"profiles": {TIER: {"models": ["Handoffctl"], "aggregate_budget_seconds": 0}}}
            with (
                patch.object(Path, "read_text", return_value=json.dumps(bad)),
                self.assertRaisesRegex(FormalReceiptError, "malformed"),
            ):
                expected_contract(ROOT, TIER)
        with (
            self.subTest("missing-model-input"),
            patch.object(formal_receipt, "_digest", side_effect=OSError("missing")),
            self.assertRaisesRegex(FormalReceiptError, "inputs are unreadable"),
        ):
            expected_contract(ROOT, TIER)

    def test_rejects_unsuccessful_or_malformed_outcomes(self) -> None:
        candidate = expected_candidate(ROOT)
        for status, outcomes, message in (
            ("failed", {"Handoffctl": "success"}, "incomplete"),
            ("success", ["success"], "incomplete"),
            ("success", {"Handoffctl": "failed"}, "incomplete"),
        ):
            with self.subTest(status=status, outcomes=outcomes):
                value = receipt()
                value["status"] = status
                value["outcomes"] = outcomes
                with self.assertRaisesRegex(FormalReceiptError, message):
                    validate_receipt(value, root=ROOT, candidate=candidate, tier=TIER)

    def test_rejects_identity_profile_config_and_budget_shape_drift(self) -> None:
        candidate = expected_candidate(ROOT)
        cases: list[tuple[str, object, str]] = [
            ("candidate_identity", {"kind": "source", "commit": "b" * 40}, "stale"),
            ("profile", "full-exhaustive", "tier"),
            ("configs", {}, "configuration"),
            ("verifier_budget", {"declared_seconds": 1, "elapsed_seconds": 1}, "budget"),
            ("verifier_budget", {"declared_seconds": 900, "elapsed_seconds": "1"}, "budget"),
        ]
        for field, replacement, message in cases:
            with self.subTest(field=field):
                value = receipt()
                value[field] = replacement
                with self.assertRaisesRegex(FormalReceiptError, message):
                    validate_receipt(value, root=ROOT, candidate=candidate, tier=TIER)

    def test_cli_rejects_non_object_malformed_and_unreadable_receipts(self) -> None:
        argv = ["formal_receipt", "--receipt", "unused", "--candidate", "a" * 40, "--tier", TIER]
        with (
            self.assertRaises(SystemExit) as list_error,
            patch.object(sys, "argv", argv),
            patch.object(Path, "read_text", return_value="[]"),
        ):
            formal_receipt.main()
        self.assertEqual(2, list_error.exception.code)
        with (
            self.assertRaises(SystemExit) as malformed_error,
            patch.object(sys, "argv", argv),
            patch.object(Path, "read_text", return_value="not-json"),
        ):
            formal_receipt.main()
        self.assertEqual(2, malformed_error.exception.code)
        with (
            self.assertRaises(SystemExit) as json_error,
            patch.object(sys, "argv", argv),
            patch.object(Path, "read_text", side_effect=OSError("unreadable")),
        ):
            formal_receipt.main()
        self.assertEqual(2, json_error.exception.code)


if __name__ == "__main__":
    unittest.main()
