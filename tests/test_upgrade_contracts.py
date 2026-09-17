# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Offline positive and negative coverage for upgrade contract inspection."""

from __future__ import annotations

import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Any, cast
from unittest.mock import patch

from tools import upgrade_commands as commands
from tools import upgrade_contract_runtime as runtime
from tools.upgrade_contract_runtime import RuntimeContractError, validate_runtime_contract


def release(version: str, seed: str) -> dict[str, str]:
    return {
        "version": version,
        "source_commit": seed * 40,
        "tag_ref": f"refs/tags/{version}",
        "tag_object": ("b" if seed == "a" else "a") * 40,
        "signature_sha256": "c" * 64,
        "trust_policy_sha256": "d" * 64,
        "vendor_manifest_sha256": "e" * 64,
    }


def contract(backend: str = "git") -> dict[str, Any]:
    operation_id = "upgrade:test"
    inputs = {
        "backend": backend,
        "selector_ref": "release/next",
        "expected_state_revision": 3,
        "barrier_id": "barrier-1",
        "fencing_token": "fence-1",
        "backup_operation_id": "upgrade:test:backup",
    }
    opcodes = {
        "discover": "release.inspect",
        "preflight": "admission.check",
        "quiesce": "barrier.acquire",
        "backup": "backend.backup",
        "stage": "runtime.stage",
        "commit": "authority.atomic_replace",
        "validate": "runtime.validate",
        "reopen": "barrier.reopen",
    }
    dependencies = {
        "discover": [],
        "preflight": ["discover"],
        "quiesce": ["preflight"],
        "backup": ["quiesce"],
        "stage": ["backup"],
        "commit": ["quiesce", "backup", "stage"],
        "validate": ["commit"],
        "reopen": ["validate"],
    }
    phases = []
    for order, phase_id in enumerate(opcodes, 1):
        operation = {
            "operation_id": f"{operation_id}:{phase_id}",
            "opcode": opcodes[phase_id],
            "inputs": dict(inputs),
            "timeout_seconds": 30,
            "resources": ["coordinator-state"],
            "preconditions": ["ready"],
            "postconditions": ["recorded"],
            "evidence": ["operation-id"],
            "durable_record": "operation-id-and-outcome",
        }
        phases.append(
            {
                "id": phase_id,
                "order": order,
                "mutates_authority": phase_id == "commit",
                "requires": dependencies[phase_id],
                "on_failure": "stop-before-mutation",
                "operation": operation,
            }
        )
    backend_fields = {
        "backend": backend,
        "authority": ["state"],
        "backup": ["snapshot"],
        "restore": ["snapshot"],
        "selector": ["release"],
        "projections": ["status"],
        "equivalence": "authority-compatible-round-trip",
    }
    sqlite_fields = dict(backend_fields)
    sqlite_fields["backend"] = "sqlite"
    sqlite_fields["wal"] = ["wal"]
    git_fields = dict(backend_fields)
    git_fields["backend"] = "git"
    return {
        "schema_version": 2,
        "operation_id": operation_id,
        "backend": backend,
        "from": release("v0.3.5", "a"),
        "to": release("v0.3.7", "b"),
        "preconditions": [
            {
                "id": "READY",
                "effect": "read-only",
                "failure_mode": "stop-before-mutation",
                "preconditions": ["clean"],
                "postconditions": ["checked"],
                "evidence": ["log"],
            }
        ],
        "phases": phases,
        "backend_contracts": [git_fields, sqlite_fields],
        "rollback": {
            "required": True,
            "backup_integrity": "backend-specific",
            "integrity_by_backend": {
                "git": "git-object-and-ref",
                "sqlite": "sqlite-integrity-and-backup-api",
            },
            "equivalence": "authority-compatible-round-trip",
            "reopen_gate": "validate-before-reopen",
            "ambiguous_external_result": "safe-mode",
            "operation": {
                "operation_id": f"{operation_id}:rollback",
                "opcode": "backend.restore",
                "inputs": dict(inputs),
                "timeout_seconds": 30,
                "resources": ["coordinator-state"],
                "preconditions": ["ready"],
                "postconditions": ["recorded"],
                "evidence": ["operation-id"],
                "durable_record": "safe-mode-record",
            },
        },
    }


class UpgradeContractTests(unittest.TestCase):
    def write(self, value: object) -> Path:
        path = Path(self.temp.name) / "contract.json"
        path.write_text(json.dumps(value), encoding="utf-8")
        return path

    def setUp(self) -> None:
        self.temp = TemporaryDirectory()

    def tearDown(self) -> None:
        self.temp.cleanup()

    def test_runtime_and_commands_for_both_backends(self) -> None:
        for backend in ("git", "sqlite"):
            document = contract(backend)
            self.assertIs(validate_runtime_contract(document), document)
            for action in ("check", "plan"):
                with (
                    self.subTest(backend=backend, action=action),
                    patch("builtins.print") as output,
                ):
                    self.assertEqual(
                        0, commands.execute_upgrade_command(action, self.write(document), backend)
                    )
                    payload = json.loads(output.call_args.args[0])
                    self.assertTrue(payload["valid"])
                    self.assertEqual(backend, payload["backend"])
                    if action == "plan":
                        self.assertEqual(8, len(payload["phases"]))

    def test_rejects_commands_and_files(self) -> None:
        path = self.write(contract())
        for action in ("apply", "rollback", "unknown"):
            with self.subTest(action=action), self.assertRaises(commands.UpgradeCommandError):
                commands.execute_upgrade_command(action, path, "git")
        bad = Path(self.temp.name) / "bad"
        bad.write_bytes(b"not json")
        with self.assertRaisesRegex(commands.UpgradeCommandError, "canonical"):
            commands.execute_upgrade_command("check", bad, "git")
        directory = Path(self.temp.name) / "directory"
        directory.mkdir()
        with self.assertRaises(commands.UpgradeCommandError):
            commands.execute_upgrade_command("check", directory, "git")
        link = Path(self.temp.name) / "link"
        link.symlink_to(path)
        with self.assertRaises(commands.UpgradeCommandError):
            commands.execute_upgrade_command("check", link, "git")

    def test_rejects_duplicate_nan_oversize_and_mismatch(self) -> None:
        path = self.write(contract())
        with self.assertRaises(commands.UpgradeCommandError):
            commands.execute_upgrade_command("check", path, "sqlite")
        duplicate = Path(self.temp.name) / "duplicate"
        duplicate.write_text('{"schema_version":2,"schema_version":2}')
        with self.assertRaises(commands.UpgradeCommandError):
            commands.execute_upgrade_command("check", duplicate, "git")
        nan = Path(self.temp.name) / "nan"
        nan.write_text('{"schema_version": NaN}')
        with self.assertRaises(commands.UpgradeCommandError):
            commands.execute_upgrade_command("check", nan, "git")
        huge = Path(self.temp.name) / "huge"
        huge.write_bytes(b"{" + b" " * (commands.MAX_CONTRACT_BYTES + 1))
        with self.assertRaises(commands.UpgradeCommandError):
            commands.execute_upgrade_command("check", huge, "git")

    def test_runtime_rejects_unknown_and_malformed_fields(self) -> None:
        base = contract()
        mutations = [
            {"schema_version": 1},
            {**base, "unknown": True},
            {**base, "backend": "other"},
            {**base, "from": base["to"]},
            {**base, "preconditions": []},
            {**base, "phases": []},
            {**base, "backend_contracts": []},
            {**base, "rollback": {}},
        ]
        for value in mutations:
            with self.subTest(value=value), self.assertRaises(RuntimeContractError):
                validate_runtime_contract(value)

    def test_runtime_rejects_nested_contract_mutations(self) -> None:
        cases = [
            ("from", "version", "bad"),
            ("phases", 0, {"id": "bad"}),
            ("backend_contracts", 0, {"backend": "bad"}),
        ]
        for field, index, value in cases:
            value_to_test = contract()
            if field == "from":
                value_to_test[field][index] = value
            else:
                value_to_test[field][index] = value
            with self.subTest(field=field), self.assertRaises(RuntimeContractError):
                validate_runtime_contract(value_to_test)

    def test_runtime_failure_branches_are_fail_closed(self) -> None:
        checks = [
            ("from", "tag_ref", "wrong"),
            ("from", "source_commit", "short"),
            ("from", "signature_sha256", "short"),
        ]
        for section, field, value in checks:
            mutated = contract()
            mutated[section][field] = value
            with self.subTest(field=field), self.assertRaises(RuntimeContractError):
                validate_runtime_contract(mutated)
        invalid_checks: list[tuple[str, Any]] = [
            ("effect", "bad"),
            ("failure_mode", "bad"),
            ("evidence", []),
        ]
        for field, value in invalid_checks:
            mutated = contract()
            precondition_target = cast(dict[str, Any], mutated["preconditions"][0])
            precondition_target[field] = value
            with self.subTest(field=field), self.assertRaises(RuntimeContractError):
                validate_runtime_contract(mutated)
        input_checks: list[tuple[str, Any]] = [
            ("backend", "sqlite"),
            ("expected_state_revision", 0),
            ("backup_operation_id", "bad"),
        ]
        for field, value in input_checks:
            mutated = contract()
            input_target = cast(dict[str, Any], mutated["phases"][0]["operation"]["inputs"])
            input_target[field] = value
            with self.subTest(field=field), self.assertRaises(RuntimeContractError):
                validate_runtime_contract(mutated)
        operation_checks: list[tuple[str, Any]] = [
            ("timeout_seconds", 0),
            ("durable_record", "bad"),
        ]
        for field, value in operation_checks:
            mutated = contract()
            operation_target = cast(dict[str, Any], mutated["phases"][0]["operation"])
            operation_target[field] = value
            with self.subTest(field=field), self.assertRaises(RuntimeContractError):
                validate_runtime_contract(mutated)
        backend_checks: list[tuple[str, Any]] = [
            ("authority", []),
            ("equivalence", "bad"),
            ("wal", []),
        ]
        for field, value in backend_checks:
            mutated = contract()
            backend_target = cast(
                dict[str, Any], mutated["backend_contracts"][1 if field == "wal" else 0]
            )
            backend_target[field] = value
            with self.subTest(field=field), self.assertRaises(RuntimeContractError):
                validate_runtime_contract(mutated)

    def test_runtime_dependency_and_identity_failures(self) -> None:
        mutations = []
        value = contract()
        value["preconditions"].append(dict(value["preconditions"][0]))
        mutations.append(value)
        value = contract()
        value["phases"][0]["order"] = 2
        mutations.append(value)
        value = contract()
        value["phases"][0]["mutates_authority"] = True
        mutations.append(value)
        value = contract()
        value["phases"][1]["requires"] = []
        mutations.append(value)
        value = contract()
        value["phases"][1]["operation"]["operation_id"] = "wrong"
        mutations.append(value)
        value = contract()
        value["phases"][1]["operation"]["inputs"]["barrier_id"] = ""
        mutations.append(value)
        value = contract()
        value["backend_contracts"] = [value["backend_contracts"][0]] * 2
        mutations.append(value)
        value = contract()
        value["rollback"]["required"] = False
        mutations.append(value)
        value = contract()
        value["rollback"]["operation"]["opcode"] = "bad"
        mutations.append(value)
        for mutation in mutations:
            with self.subTest(mutation=mutation), self.assertRaises(RuntimeContractError):
                validate_runtime_contract(mutation)

    def test_private_helpers_reject_bad_shapes(self) -> None:
        with self.assertRaises(RuntimeContractError):
            runtime._backend_contract(None)
        with self.assertRaises(RuntimeContractError):
            runtime._string_list(["x", "x"], "duplicate")
        with self.assertRaises(RuntimeContractError):
            runtime._inputs(
                contract()["phases"][0]["operation"]["inputs"], "sqlite", "upgrade:test"
            )
        operation = contract()["phases"][0]["operation"]
        with self.assertRaises(RuntimeContractError):
            runtime._operation({**operation, "timeout_seconds": 90000}, "git", "upgrade:test")

    def test_reader_handles_non_object_and_read_errors(self) -> None:
        scalar = Path(self.temp.name) / "scalar"
        scalar.write_text("[]")
        with self.assertRaisesRegex(commands.UpgradeCommandError, "object"):
            commands.execute_upgrade_command("check", scalar, "git")
        with (
            patch("os.open", side_effect=OSError("denied")),
            self.assertRaisesRegex(commands.UpgradeCommandError, "unavailable"),
        ):
            commands.execute_upgrade_command("check", scalar, "git")


if __name__ == "__main__":
    unittest.main()
