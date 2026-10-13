# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Focused semantic and CLI coverage for upgrade-contract validation."""

from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import Mock, patch

from tools import validate_upgrade_contract as validator

ROOT = Path(__file__).resolve().parents[1]
_FIXTURE_SPEC = importlib.util.spec_from_file_location(
    "upgrade_contract_fixture", ROOT / "tests/test_upgrade_contract.py"
)
assert _FIXTURE_SPEC and _FIXTURE_SPEC.loader
_fixture = importlib.util.module_from_spec(_FIXTURE_SPEC)
_FIXTURE_SPEC.loader.exec_module(_fixture)


class UpgradeContractValidatorCoverageTests(unittest.TestCase):
    def document(self) -> dict[str, object]:
        return _fixture.contract()

    def test_semantic_release_identity_edges_after_structural_validation(self) -> None:
        checks: tuple[tuple[str, object, str], ...] = (
            ("same release", lambda value: value.update(to=value["from"].copy()), "identities"),
            (
                "same version",
                lambda value: value["to"].update(version=value["from"]["version"]),
                "versions",
            ),
            (
                "mismatched tag",
                lambda value: value["from"].update(tag_ref="refs/tags/v9.9.9"),
                "tag reference",
            ),
        )
        for label, mutate, message in checks:
            with (
                self.subTest(label=label),
                patch.object(validator, "validate_runtime_contract"),
                patch.object(validator.Draft202012Validator, "validate"),
            ):
                document = self.document()
                mutate(document)
                with self.assertRaisesRegex(validator.ContractError, message):
                    validator.validate_contract(document)

    def test_schema_validation_error_is_normalized_to_contract_error(self) -> None:
        document = self.document()
        document["rollback"]["required"] = False
        with (
            patch.object(validator, "validate_runtime_contract"),
            self.assertRaisesRegex(validator.ContractError, "was expected"),
        ):
            validator.validate_contract(document)

    def test_semantic_validation_delegates_phase_and_backend_checks(self) -> None:
        document = self.document()
        phases = Mock()
        backends = Mock()
        with (
            patch.object(validator, "_validate_phases", phases),
            patch.object(validator, "_validate_backends", backends),
        ):
            validator.validate_contract(document)
        phases.assert_called_once_with(document)
        backends.assert_called_once_with(document)

    def test_phase_authority_and_rollback_backend_edges_fail_closed(self) -> None:
        document = self.document()
        document["phases"][0]["mutates_authority"] = True
        with self.assertRaisesRegex(validator.ContractError, "only commit"):
            validator._validate_phases(document)

        document = self.document()
        document["backend_contracts"] = [document["backend_contracts"][0]]
        with self.assertRaisesRegex(validator.ContractError, "both Git and SQLite"):
            validator._validate_backends(document)

    def test_input_fencing_branch_edges_fail_closed(self) -> None:
        inputs = self.document()["phases"][0]["operation"]["inputs"]
        cases: tuple[tuple[str, dict[str, object], bool, str], ...] = (
            ("unknown field", {**inputs, "unknown": "value"}, False, "fields"),
            ("wrong backend", {**inputs, "backend": "git"}, False, "backend"),
            ("bool revision", {**inputs, "expected_state_revision": False}, False, "revision"),
            ("wrong backup", {**inputs, "backup_operation_id": "other"}, False, "backup"),
            (
                "rollback target",
                {**inputs, "target": "stage"},
                True,
                "rollback target",
            ),
        )
        for label, candidate, rollback, message in cases:
            with (
                self.subTest(label=label),
                self.assertRaisesRegex(validator.ContractError, message),
            ):
                validator._validate_inputs(
                    candidate, "sqlite", "upgrade:v0.3.5-to-v0.3.6:001", rollback=rollback
                )

    def test_main_reports_usage_invalid_json_and_valid_contract(self) -> None:
        self.assertEqual(2, validator.main([]))
        with TemporaryDirectory() as directory:
            path = Path(directory) / "contract.json"
            path.write_text("{")
            self.assertEqual(1, validator.main([str(path)]))
            path.write_text(json.dumps(self.document()))
            self.assertEqual(0, validator.main([str(path)]))


if __name__ == "__main__":
    unittest.main()
