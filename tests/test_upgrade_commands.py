# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Tests for the fail-closed dependency-free upgrade command boundary."""

from __future__ import annotations

import io
import json
import os
import subprocess
import tempfile
import unittest
from collections.abc import Callable
from contextlib import redirect_stdout
from pathlib import Path
from typing import Any, cast
from unittest.mock import patch

from tools.generate_upgrade_contract import generate
from tools.runtime_bootstrap import ExpectedRuntimeIdentity
from tools.upgrade_binding import UpgradeRuntimeBinding
from tools.upgrade_commands import (
    MAX_CONTRACT_BYTES,
    UpgradeCommandError,
    consume_selected_runtime_command,
    execute_upgrade_command,
)
from tools.upgrade_contract_runtime import RuntimeContractError, validate_runtime_contract
from tools.upgrade_identity import canonical_barrier_digest, canonical_envelope_digest


def contract(
    backend: str = "sqlite", operation_id: str = "upgrade:v0.3.5-to-v0.3.6:001"
) -> dict[str, Any]:
    def release(version: str, seed: str) -> dict[str, str]:
        return {
            "version": version,
            "source_commit": seed * 40,
            "tag_ref": f"refs/tags/{version}",
            "tag_object": chr(ord(seed) + 1) * 40,
            "signature_sha256": chr(ord(seed) + 2) * 64,
            "trust_policy_sha256": chr(ord(seed) + 3) * 64,
            "vendor_manifest_sha256": chr(ord(seed) + 4) * 64,
        }

    return generate(
        {
            "operation_id": operation_id,
            "backend": backend,
            "selector_ref": ".runtime/runtime-selector.json",
            "expected_state_revision": 7,
            "barrier_id": "barrier-7",
            "fencing_token": "fence-7",
            "from": release("v0.3.5", "a"),
            "to": release("v0.3.6", "b"),
        }
    )


class UpgradeCommandTests(unittest.TestCase):
    def test_rejects_invalid_actions_and_backends_before_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "contract.json"
            path.write_text(json.dumps(contract()), encoding="utf-8")
            for action in ("", "inspect", "apply-now"):
                with (
                    self.subTest(action=action),
                    self.assertRaisesRegex(UpgradeCommandError, "unknown upgrade action"),
                ):
                    execute_upgrade_command(action, path, "sqlite")
            with self.assertRaisesRegex(
                UpgradeCommandError, "selected coordinator backend is unsupported"
            ):
                execute_upgrade_command("check", path, "remote")

    def test_rejects_malformed_contract_files_and_digest(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            malformed = root / "malformed.json"
            malformed.write_text('{"backend": NaN}', encoding="utf-8")
            with self.assertRaisesRegex(UpgradeCommandError, "canonical JSON"):
                execute_upgrade_command("check", malformed, "sqlite")
            oversized = root / "oversized.json"
            oversized.write_bytes(b"{}" + b" " * (MAX_CONTRACT_BYTES + 1))
            with self.assertRaisesRegex(UpgradeCommandError, "size limit"):
                execute_upgrade_command("check", oversized, "sqlite")
            with self.assertRaisesRegex(UpgradeCommandError, "manifest digest is invalid"):
                consume_selected_runtime_command(
                    root / "selector.json",
                    root,
                    ExpectedRuntimeIdentity("a", "b", "c", "d", "e", "f"),
                    "bad",
                )

    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.path = self.root / "contract.json"

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def write(self, document: object) -> None:
        self.path.write_text(json.dumps(document), encoding="utf-8")

    def write_binding(self, document: dict[str, Any]) -> Path:
        inputs = document["rollback"]["operation"]["inputs"]
        envelope: dict[str, object] = {
            "schema_version": 2,
            "backend": document["backend"],
            "project_id": "-".join(("123e4567", "e89b", "42d3", "a456", "426614174000")),
            "operation_id": document["operation_id"],
            "state_revision": inputs["expected_state_revision"],
            "authority_revision": "authority-7",
            "fencing_token": inputs["fencing_token"],
            "fencing_owner": "worker-7",
            "durable_barrier_id": inputs["barrier_id"],
            "artifact_root": "/srv/runtime/artifacts",
            "source": "/srv/runtime/artifacts/source",
            "destination": "/srv/runtime/artifacts/destination",
            "manifest": "/srv/runtime/artifacts/manifest.json",
            "selector_ref": inputs["selector_ref"],
            "target": "rollback",
        }
        envelope["barrier_identity_digest"] = canonical_barrier_digest(envelope)
        envelope["envelope_digest"] = canonical_envelope_digest(envelope)
        binding = UpgradeRuntimeBinding.bind(document, envelope, session_identity_digest="a" * 64)
        path = self.root / "binding.json"
        path.write_text(json.dumps(binding.as_mapping()), encoding="utf-8")
        return path

    def test_runtime_consumption_validates_manifest_and_wraps_launcher_errors(self) -> None:
        identity = ExpectedRuntimeIdentity(
            "a" * 40,
            "refs/tags/v1",
            "b" * 40,
            "c" * 64,
            "d" * 64,
            "e" * 64,
        )
        with self.assertRaisesRegex(UpgradeCommandError, "manifest digest is invalid"):
            consume_selected_runtime_command(self.path, self.root, identity, "not-a-digest")

        import tools.upgrade_commands as commands

        def launcher(
            _selector: Path,
            _releases: Path,
            expected: Any,
            verify: Any,
            _args: Any,
        ) -> Any:
            runtime = self.root / "v1"
            runtime.mkdir()
            manifest = runtime / "runtime-manifest.json"
            manifest.write_text("manifest", encoding="utf-8")
            verified = verify(runtime, expected)
            self.assertEqual(expected, verified.identity)
            return subprocess.CompletedProcess(["runtime"], 7)

        import hashlib

        digest = hashlib.sha256(b"manifest").hexdigest()
        with patch.object(commands, "run_selected_runtime", side_effect=launcher):
            self.assertEqual(
                7,
                consume_selected_runtime_command(self.path, self.root, identity, digest),
            )

        with (
            patch.object(commands, "run_selected_runtime", side_effect=RuntimeError("boom")),
            self.assertRaisesRegex(UpgradeCommandError, "consumption failed"),
        ):
            consume_selected_runtime_command(self.path, self.root, identity, digest)

        def missing_manifest(
            _selector: Path,
            _releases: Path,
            expected: Any,
            verify: Any,
            _args: Any,
        ) -> Any:
            runtime = self.root / "missing"
            runtime.mkdir()
            verify(runtime, expected)
            raise AssertionError("verification should reject missing manifest")

        with (
            patch.object(commands, "run_selected_runtime", side_effect=missing_manifest),
            self.assertRaisesRegex(UpgradeCommandError, "manifest is unavailable"),
        ):
            consume_selected_runtime_command(self.path, self.root, identity, digest)

    def test_check_and_plan_emit_only_sanitized_non_executable_data(self) -> None:
        document = contract()
        self.write(document)
        with redirect_stdout(io.StringIO()) as output:
            self.assertEqual(0, execute_upgrade_command("check", self.path, "sqlite"))
        checked = json.loads(output.getvalue())
        self.assertTrue(checked["valid"])
        self.assertFalse(checked["executable"])
        self.assertNotIn("phases", checked)

        with redirect_stdout(io.StringIO()) as output:
            self.assertEqual(0, execute_upgrade_command("plan", self.path, "sqlite"))
        planned = json.loads(output.getvalue())
        self.assertEqual("authority.atomic_replace", planned["phases"][5]["opcode"])
        self.assertEqual("backend.restore", planned["rollback"]["opcode"])
        encoded = output.getvalue()
        for private_value in (
            ".runtime/runtime-selector.json",
            "barrier-7",
            "fence-7",
            document["from"]["source_commit"],
            document["to"]["signature_sha256"],
        ):
            self.assertNotIn(private_value, encoded)

    def test_apply_and_rollback_reject_both_backends_without_writes(self) -> None:
        for backend in ("git", "sqlite"):
            for action in ("apply", "rollback"):
                document = contract(backend)
                self.write(document)
                before = self.path.read_bytes()
                with (
                    self.subTest(backend=backend, action=action),
                    self.assertRaisesRegex(UpgradeCommandError, "no coordinator state was mutated"),
                ):
                    execute_upgrade_command(action, self.path, backend)
                self.assertEqual(before, self.path.read_bytes())
                self.assertEqual([self.path], list(self.root.iterdir()))

    def test_rollback_validates_runtime_binding_before_remaining_fail_closed_boundary(self) -> None:
        document = contract(operation_id="upgrade-001")
        self.write(document)
        binding = self.write_binding(document)
        with self.assertRaisesRegex(UpgradeCommandError, "live durable session/backend binding"):
            execute_upgrade_command("rollback", self.path, "sqlite", binding)
        changed = json.loads(binding.read_text(encoding="utf-8"))
        changed["contract_digest"] = "0" * 64
        binding.write_text(json.dumps(changed), encoding="utf-8")
        with self.assertRaisesRegex(
            UpgradeCommandError, "binding validation failed|stale|does not match"
        ):
            execute_upgrade_command("rollback", self.path, "sqlite", binding)

    def test_mutation_boundary_requires_matching_live_binding(self) -> None:
        document = contract(operation_id="upgrade-001")
        self.write(document)
        with self.assertRaisesRegex(UpgradeCommandError, "concrete live"):
            execute_upgrade_command("apply", self.path, "sqlite", live_binding=cast(Any, object()))

    def test_contract_file_and_dispatch_boundaries_fail_closed(self) -> None:
        self.write(contract())
        with self.assertRaisesRegex(UpgradeCommandError, "does not match"):
            execute_upgrade_command("check", self.path, "git")
        with self.assertRaisesRegex(UpgradeCommandError, "unsupported"):
            execute_upgrade_command("check", self.path, "remote")
        with self.assertRaisesRegex(UpgradeCommandError, "unknown upgrade action"):
            execute_upgrade_command("execute", self.path, "sqlite")

        self.path.write_text("{", encoding="utf-8")
        with self.assertRaisesRegex(UpgradeCommandError, "not canonical JSON"):
            execute_upgrade_command("check", self.path, "sqlite")
        self.path.write_text('{"schema_version":2,"schema_version":2}', encoding="utf-8")
        with self.assertRaisesRegex(UpgradeCommandError, "not canonical JSON"):
            execute_upgrade_command("check", self.path, "sqlite")
        self.path.write_text('{"schema_version":NaN}', encoding="utf-8")
        with self.assertRaisesRegex(UpgradeCommandError, "not canonical JSON"):
            execute_upgrade_command("check", self.path, "sqlite")
        self.write([])
        with self.assertRaisesRegex(UpgradeCommandError, "must be an object"):
            execute_upgrade_command("check", self.path, "sqlite")
        self.path.write_bytes(b"x" * (MAX_CONTRACT_BYTES + 1))
        with self.assertRaisesRegex(UpgradeCommandError, "size limit"):
            execute_upgrade_command("check", self.path, "sqlite")

    def test_contract_hardlink_alias_is_rejected_before_dispatch(self) -> None:
        target = self.root / "contract-target.json"
        target.write_text(json.dumps(contract()), encoding="utf-8")
        self.path.hardlink_to(target)
        with self.assertRaisesRegex(UpgradeCommandError, "single-link regular file"):
            execute_upgrade_command("check", self.path, "sqlite")
        self.path.unlink()
        target = self.root / "target.json"
        target.write_text("{}", encoding="utf-8")
        self.path.symlink_to(target)
        with self.assertRaisesRegex(UpgradeCommandError, "unavailable or unsafe"):
            execute_upgrade_command("check", self.path, "sqlite")

    def test_unsigned_tag_contract_is_accepted(self) -> None:
        document = contract()
        document["from"].pop("signature_sha256")
        document["to"].pop("signature_sha256")
        self.path.write_text(json.dumps(document), encoding="utf-8")
        with redirect_stdout(io.StringIO()):
            self.assertEqual(0, execute_upgrade_command("check", self.path, "sqlite"))

    def test_contract_symlinked_parent_is_rejected_before_dispatch(self) -> None:
        real = self.root / "real"
        real.mkdir()
        target = real / "contract.json"
        target.write_text(json.dumps(contract()), encoding="utf-8")
        linked = self.root / "linked"
        linked.symlink_to(real, target_is_directory=True)
        with self.assertRaisesRegex(UpgradeCommandError, "unavailable or unsafe"):
            execute_upgrade_command("check", linked / "contract.json", "sqlite")

    def test_contract_parent_swap_after_open_cannot_redirect_read(self) -> None:
        linked = self.root / "linked"
        linked.mkdir()
        target = linked / "contract.json"
        target.write_text(json.dumps(contract()), encoding="utf-8")
        requested = linked / "contract.json"
        evil = self.root / "evil"
        evil.mkdir()
        forged = contract()
        forged["operation_id"] = "upgrade:forged:001"
        (evil / "contract.json").write_text(json.dumps(forged), encoding="utf-8")

        original_open = os.open
        swapped = False

        def swap_parent_after_open(*args: Any, **kwargs: Any) -> int:
            nonlocal swapped
            descriptor = original_open(*args, **kwargs)
            if (
                args
                and args[0] == "contract.json"
                and kwargs.get("dir_fd") is not None
                and not swapped
            ):
                swapped = True
                displaced = self.root / "displaced"
                linked.rename(displaced)
                linked.symlink_to(evil, target_is_directory=True)
            return descriptor

        with (
            patch.object(os, "open", side_effect=swap_parent_after_open),
            redirect_stdout(io.StringIO()) as output,
        ):
            self.assertEqual(0, execute_upgrade_command("check", requested, "sqlite"))
        self.assertTrue(swapped)
        self.assertEqual(contract()["operation_id"], json.loads(output.getvalue())["operation_id"])

    def test_stdlib_validator_rejects_every_typed_contract_boundary(self) -> None:
        mutations: tuple[Callable[[dict[str, Any]], object], ...] = (
            lambda value: value.update(schema_version=True),
            lambda value: value.update(operation_id="bad/path"),
            lambda value: value.update(backend="remote"),
            lambda value: value.update(backend=[]),
            lambda value: value["from"].update(version="latest"),
            lambda value: value["from"].update(source_commit="short"),
            lambda value: value["from"].update(tag_object="short"),
            lambda value: value["from"].update(tag_ref="refs/tags/v9.9.9"),
            lambda value: value["from"].update(signature_sha256="short"),
            lambda value: value.update(to=value["from"].copy()),
            lambda value: value.update(preconditions=[]),
            lambda value: value["preconditions"][0].update(id="bad"),
            lambda value: value["preconditions"][0].update(effect="execute"),
            lambda value: value["preconditions"][0].update(effect=[]),
            lambda value: value["preconditions"][0].update(failure_mode="continue"),
            lambda value: value["preconditions"][0].update(evidence=[]),
            lambda value: value["preconditions"].append(value["preconditions"][0].copy()),
            lambda value: value.update(phases=[]),
            lambda value: value["phases"][0].update(id="stage"),
            lambda value: value["phases"][0].update(order=True),
            lambda value: value["phases"][0].update(mutates_authority=True),
            lambda value: value["phases"][0].update(requires=["reopen"]),
            lambda value: value["phases"][0].update(on_failure="continue"),
            lambda value: value["phases"][0].update(on_failure=[]),
            lambda value: value["phases"][0]["operation"].update(operation_id="unbound"),
            lambda value: value["phases"][0]["operation"].update(opcode="runtime.stage"),
            lambda value: value["phases"][0]["operation"].update(opcode=[]),
            lambda value: value["phases"][0]["operation"].update(timeout_seconds=False),
            lambda value: value["phases"][0]["operation"].update(resources=[]),
            lambda value: value["phases"][0]["operation"].update(durable_record="memory"),
            lambda value: value["phases"][0]["operation"].update(durable_record=[]),
            lambda value: value["phases"][0]["operation"]["inputs"].update(backend="git"),
            lambda value: value["phases"][0]["operation"]["inputs"].update(selector_ref="../x"),
            lambda value: value["phases"][0]["operation"]["inputs"].update(barrier_id="bad/x"),
            lambda value: value["phases"][0]["operation"]["inputs"].update(
                expected_state_revision=False
            ),
            lambda value: value["phases"][0]["operation"]["inputs"].update(
                backup_operation_id="unbound"
            ),
            lambda value: value["phases"][1]["operation"]["inputs"].__setitem__(
                "fencing_token", "changed"
            ),
            lambda value: value.update(backend_contracts=[]),
            lambda value: value["backend_contracts"][0].update(backend="remote"),
            lambda value: value["backend_contracts"][0].update(backend=[]),
            lambda value: value["backend_contracts"][0].update(authority=[]),
            lambda value: value["backend_contracts"][0].update(equivalence="none"),
            lambda value: value["backend_contracts"].__setitem__(
                1, value["backend_contracts"][0].copy()
            ),
            lambda value: value["rollback"].update(required=False),
            lambda value: value["rollback"].update(ambiguous_external_result=[]),
            lambda value: value["rollback"]["operation"].update(opcode="barrier.reopen"),
            lambda value: value["rollback"]["operation"]["inputs"].__setitem__(
                "fencing_token", "changed"
            ),
            lambda value: value.update(unexpected=True),
        )
        for mutate in mutations:
            document = contract()
            mutate(document)
            with self.subTest(document=document), self.assertRaises(RuntimeContractError):
                validate_runtime_contract(document)


if __name__ == "__main__":
    unittest.main()
