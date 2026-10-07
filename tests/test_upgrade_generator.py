# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Hostile tests for deterministic release-contract generation."""

from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any
from unittest.mock import patch

from tools.verify_release_contract import main as verify_main
from tools.verify_release_contract import verify

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
SPEC = importlib.util.spec_from_file_location(
    "upgrade_generator", ROOT / "tools/generate_upgrade_contract.py"
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
ContractError = MODULE.ContractError
generate = MODULE.generate


def release(version: str, seed: str) -> dict[str, str]:
    return {
        "version": version,
        "source_commit": seed * 40,
        "tag_ref": f"refs/tags/{version}",
        "tag_object": (chr(ord(seed) + 1)) * 40,
        "signature_sha256": (chr(ord(seed) + 2)) * 64,
        "trust_policy_sha256": (chr(ord(seed) + 3)) * 64,
        "vendor_manifest_sha256": (chr(ord(seed) + 4)) * 64,
    }


def transition() -> dict[str, Any]:
    return {
        "operation_id": "upgrade:v0.3.5-to-v0.3.6:001",
        "backend": "sqlite",
        "selector_ref": ".runtime/runtime-selector.json",
        "expected_state_revision": 7,
        "barrier_id": "barrier-7",
        "fencing_token": "fence-7",
        "from": release("v0.3.5", "a"),
        "to": release("v0.3.6", "b"),
    }


class UpgradeGeneratorTests(unittest.TestCase):
    def test_release_contract_verifier_writes_valid_contract(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "transition.json"
            output = root / "release-contract.json"
            source.write_text(json.dumps(transition()), encoding="utf-8")
            result = verify(source, output)
            self.assertEqual("pass", result["status"])
            self.assertEqual(transition()["operation_id"], result["operation_id"])

    def test_release_contract_verifier_cli_success_and_invalid_input(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "transition.json"
            output = root / "release-contract.json"
            source.write_text(json.dumps(transition()), encoding="utf-8")
            self.assertEqual(0, verify_main([str(source), str(output)]))
            source.write_text("{not-json", encoding="utf-8")
            self.assertEqual(1, verify_main([str(source), str(output)]))

    def test_release_contract_verifier_cli_converts_generation_errors(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "transition.json"
            output = root / "release-contract.json"
            source.write_text(json.dumps(transition()), encoding="utf-8")
            with patch("tools.verify_release_contract.verify", side_effect=OSError("write")):
                self.assertEqual(1, verify_main([str(source), str(output)]))

    def test_generation_is_deterministic_and_valid(self) -> None:
        first = generate(transition())
        second = generate(transition())
        self.assertEqual(first, second)
        self.assertEqual([phase["id"] for phase in first["phases"]], list(MODULE.PHASES))
        self.assertEqual(
            first["phases"][5]["operation"]["operation_id"], first["operation_id"] + ":commit"
        )
        self.assertEqual("authority.atomic_replace", first["phases"][5]["operation"]["opcode"])
        self.assertEqual("backend.restore", first["rollback"]["operation"]["opcode"])
        rollback_inputs = dict(first["rollback"]["operation"]["inputs"])
        self.assertEqual(rollback_inputs.pop("target"), "rollback")
        self.assertEqual(rollback_inputs, first["phases"][0]["operation"]["inputs"])

    def test_unknown_input_field_is_rejected_before_generation(self) -> None:
        document = transition()
        document["arbitrary_script"] = "rm -rf /"
        with self.assertRaises(ContractError):
            MODULE._validate_transition(document)
        with self.assertRaises(ContractError):
            MODULE._validate_transition([])
        document = transition()
        document["operation_id"] = 7
        with self.assertRaises(ContractError):
            MODULE._validate_transition(document)
        document = transition()
        document["from"] = []
        with self.assertRaises(ContractError):
            MODULE._validate_transition(document)
        for field, value in (
            ("backend", "remote"),
            ("expected_state_revision", False),
            ("selector_ref", ""),
            ("barrier_id", 7),
        ):
            document = transition()
            document[field] = value
            with self.subTest(field=field), self.assertRaises(ContractError):
                MODULE._validate_transition(document)

    def test_input_loader_and_cli_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            malformed = Path(directory) / "malformed.json"
            malformed.write_text("{", encoding="utf-8")
            with self.assertRaises(ContractError):
                MODULE._load_transition(malformed)
            with self.assertRaises(ContractError):
                MODULE._load_transition(Path(directory) / "missing.json")
            self.assertEqual(MODULE.main([str(malformed), str(Path(directory) / "out.json")]), 1)

    def test_floating_ref_and_noop_transition_are_rejected(self) -> None:
        document = transition()
        document["to"]["tag_ref"] = "refs/tags/latest"
        with self.assertRaises(ContractError):
            generate(document)
        document = transition()
        document["to"] = document["from"].copy()
        with self.assertRaises(ContractError):
            generate(document)

    def test_cli_writes_only_valid_json_contract(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "transition.json"
            output = Path(directory) / "contract.json"
            source.write_text(json.dumps(transition()), encoding="utf-8")
            self.assertEqual(MODULE.main([str(source), str(output)]), 0)
            self.assertEqual(
                generate(json.loads(source.read_text())), json.loads(output.read_text())
            )

    def test_generation_keeps_git_contract_typed_but_execution_unclaimed(self) -> None:
        document = transition()
        document["backend"] = "git"
        generated = generate(document)
        self.assertEqual("git", generated["backend"])
        self.assertTrue(
            all(phase["operation"]["inputs"]["backend"] == "git" for phase in generated["phases"])
        )
        self.assertNotIn("executable", generated)


if __name__ == "__main__":
    unittest.main()
