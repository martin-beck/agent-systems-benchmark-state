# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Contract tests for immutable, non-authorizing execution envelopes."""

from __future__ import annotations

import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import cast

from tools.execution_envelope import (
    Preflight,
    canonical_digest,
    digest,
    envelope_sandbox_mounts,
    envelope_scope_path,
    errors,
    load,
    preflight,
    validate_external_root,
)


def envelope() -> dict[str, object]:
    return {
        "schema_version": 1,
        "envelope_id": "AR-0001-e1",
        "envelope_revision": 1,
        "task": "AR-0001",
        "task_revision": 7,
        "spec_ref": "specs/AR-0001.json",
        "spec_revision": 2,
        "outputs": [{"id": "implementation", "description": "Implement the bounded change."}],
        "non_goals": ["Do not authorize by prompt."],
        "path_scope": {"read": ["src", "tests"], "write": ["src", "tests"]},
        "command_classes": {
            "read": {"allowed": True},
            "test": {"allowed": True, "timeout_seconds": 60},
            "source-write": {"allowed": True, "timeout_seconds": 120},
            "git-publication": {"allowed": False},
        },
        "evidence": [{"id": "tests", "class": "contract-test", "required": True}],
        "stop_conditions": [{"id": "scope", "kind": "deny"}],
    }


class ExecutionEnvelopeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "envelopes").mkdir()
        self.worktree = self.root / "worker"
        (self.worktree / "src").mkdir(parents=True)
        self.reference = "envelopes/AR-0001-e1.json"
        self.write_envelope(envelope())

    def tearDown(self) -> None:
        self.temp.cleanup()

    def write_envelope(self, value: dict[str, object]) -> None:
        self.payload = json.dumps(value, sort_keys=True).encode()
        (self.root / self.reference).write_bytes(self.payload)

    def meta(self) -> dict[str, object]:
        return {
            "id": "AR-0001",
            "owner": "worker",
            "status": "in_progress",
            "claim_expires": "2099-01-01T00:00:00+00:00",
            "spec_ref": "specs/AR-0001.json",
            "spec_revision": 2,
            "execution_envelope_ref": self.reference,
            "execution_envelope_revision": 1,
            "execution_envelope_task_revision": 7,
            "execution_envelope_digest": canonical_digest(envelope()),
            "execution_envelope": envelope(),
        }

    def test_admits_only_the_bound_owner_class_and_path_scope(self) -> None:
        allowed = preflight(self.meta(), "worker", "source-write", ["src/module.py"], self.worktree)
        self.assertTrue(allowed.allowed)
        self.assertEqual("ALLOWED", allowed.code)
        denied = preflight(self.meta(), "worker", "source-write", ["../outside"], self.worktree)
        self.assertFalse(denied.allowed)
        self.assertEqual("PATH_OUTSIDE_SCOPE", denied.code)
        missing = preflight(self.meta(), "worker", "source-write", [], self.worktree)
        self.assertFalse(missing.allowed)
        self.assertEqual("SCOPE_DECLARATION_REQUIRED", missing.code)

    def test_root_qualified_product_and_state_scopes_are_independent(self) -> None:
        state = self.root / "state"
        (state / "tasks").mkdir(parents=True)
        value = envelope()
        value["schema_version"] = 2
        value["capabilities"] = {"git_metadata": {"allowed": False}, "network": {"allowed": False}}
        value["path_scope"] = {
            "read": ["product:src", "state:tasks"],
            "write": ["product:src", "state:tasks"],
        }
        meta = self.meta()
        meta["execution_envelope"] = value
        meta["execution_envelope_digest"] = canonical_digest(value)
        self.assertTrue(
            preflight(
                meta, "worker", "test", ["state:tasks"], self.worktree, state_root=state
            ).allowed
        )
        self.assertTrue(
            preflight(
                meta,
                "worker",
                "source-write",
                ["product:src/new.py"],
                self.worktree,
                state_root=state,
            ).allowed
        )
        self.assertEqual(
            "PATH_OUTSIDE_SCOPE",
            preflight(meta, "worker", "test", ["state:src"], self.worktree, state_root=state).code,
        )
        self.assertEqual(
            "PATH_OUTSIDE_SCOPE",
            preflight(meta, "worker", "test", ["state:tasks"], self.worktree).code,
        )

    def test_root_qualified_scope_rejects_symlink_and_traversal(self) -> None:
        state = self.root / "state"
        (state / "tasks").mkdir(parents=True)
        (state / "alias").symlink_to(self.worktree / "src")
        value = envelope()
        value["schema_version"] = 2
        value["capabilities"] = {"git_metadata": {"allowed": False}, "network": {"allowed": False}}
        value["path_scope"] = {"read": ["state:tasks"], "write": ["state:tasks"]}
        meta = self.meta()
        meta["execution_envelope"] = value
        meta["execution_envelope_digest"] = canonical_digest(value)
        self.assertEqual(
            "PATH_OUTSIDE_SCOPE",
            preflight(
                meta, "worker", "test", ["state:alias"], self.worktree, state_root=state
            ).code,
        )
        self.assertEqual(
            "PATH_OUTSIDE_SCOPE",
            preflight(
                meta, "worker", "test", ["state:../src"], self.worktree, state_root=state
            ).code,
        )

    def test_source_root_is_independently_bound_and_rejects_aliases(self) -> None:
        source = self.root / "source"
        (source / "tools").mkdir(parents=True)
        value = envelope()
        value["schema_version"] = 2
        value["capabilities"] = {"git_metadata": {"allowed": False}, "network": {"allowed": False}}
        value["path_scope"] = {"read": ["source-root"], "write": ["source:tools"]}
        meta = self.meta()
        meta["execution_envelope"] = value
        meta["execution_envelope_digest"] = canonical_digest(value)
        self.assertTrue(
            preflight(
                meta, "worker", "source-write", ["source:tools"], self.worktree, source_root=source
            ).allowed
        )
        self.assertEqual(
            "PATH_SCOPE_UNAVAILABLE",
            preflight(meta, "worker", "test", ["source-root"], self.worktree).code,
        )
        self.assertEqual(
            "PATH_SCOPE_UNAVAILABLE",
            preflight(meta, "worker", "test", ["source:tools"], self.worktree).code,
        )
        alias = self.root / "source-alias"
        alias.symlink_to(source)
        self.assertEqual(
            "PATH_SCOPE_UNAVAILABLE",
            preflight(
                meta, "worker", "test", ["source-root"], self.worktree, source_root=alias
            ).code,
        )

    def test_root_validation_and_mounts_fail_closed(self) -> None:
        state = self.root / "state"
        source = self.root / "source"
        (state / "tasks").mkdir(parents=True)
        (source / "src").mkdir(parents=True)
        self.assertEqual(state.resolve(), validate_external_root(state, "state"))
        with self.assertRaisesRegex(RuntimeError, "root is unavailable"):
            validate_external_root(self.root / "missing", "state")
        mounts = envelope_sandbox_mounts(
            self.worktree,
            ["product-root", "state:tasks", "source-root"],
            ["state:tasks"],
            state_root=state,
            source_root=source,
        )
        self.assertEqual(
            ["product/.", "state/tasks", "source/.", "state/tasks"],
            [item[0] for item in mounts],
        )
        with self.assertRaisesRegex(RuntimeError, "unavailable root"):
            envelope_sandbox_mounts(self.worktree, ["source-root"], [], state_root=state)
        outside = self.root / "outside"
        outside.mkdir()
        (self.worktree / "escape").symlink_to(outside, target_is_directory=True)
        with self.assertRaisesRegex(RuntimeError, "contains a symlink"):
            envelope_scope_path(self.worktree, "escape")

    def test_rejects_mutated_bytes_and_hostile_shape(self) -> None:
        bound_meta = self.meta()
        mutated = envelope()
        mutated["non_goals"] = ["changed"]
        self.write_envelope(mutated)
        bound_meta["execution_envelope"] = mutated
        result = preflight(bound_meta, "worker", "test", ["tests/test_x.py"], self.worktree)
        self.assertFalse(result.allowed)
        self.assertEqual("ENVELOPE_DIGEST_MISMATCH", result.code)
        hostile = envelope()
        hostile["unknown"] = True
        self.assertIn("envelope unknown field: unknown", errors(hostile))

    def test_rejects_forged_binding_revision_expired_lease_and_symlink(self) -> None:
        forged = {**self.meta(), "execution_envelope_revision": 9}
        result = preflight(forged, "worker", "test", [], self.worktree)
        self.assertFalse(result.allowed)
        self.assertEqual("ENVELOPE_REVISION_MISMATCH", result.code)
        stale_task = {**self.meta(), "execution_envelope_task_revision": 8}
        result = preflight(stale_task, "worker", "test", [], self.worktree)
        self.assertFalse(result.allowed)
        self.assertEqual("ENVELOPE_REVISION_MISMATCH", result.code)
        expired = {**self.meta(), "claim_expires": "2000-01-01T00:00:00+00:00"}
        result = preflight(expired, "worker", "test", [], self.worktree)
        self.assertFalse(result.allowed)
        self.assertEqual("OWNER_CLAIM_REQUIRED", result.code)
        external = self.root / "external.json"
        external.write_bytes(self.payload)
        (self.root / self.reference).unlink()
        (self.root / self.reference).symlink_to(external)
        result = preflight(self.meta(), "worker", "test", [], self.worktree)
        self.assertTrue(result.allowed)

    def test_never_infers_owner_or_authorization_from_envelope_text(self) -> None:
        result = preflight(self.meta(), "other-worker", "test", [], self.worktree)
        self.assertFalse(result.allowed)
        self.assertEqual("OWNER_CLAIM_REQUIRED", result.code)
        forbidden = preflight(self.meta(), "worker", "git-publication", [], self.worktree)
        self.assertFalse(forbidden.allowed)
        self.assertEqual("COMMAND_CLASS_DENIED", forbidden.code)

    def test_publication_requires_versioned_metadata_network_and_invocation_authorization(
        self,
    ) -> None:
        value = envelope()
        value["schema_version"] = 2
        command_classes = cast(dict[str, dict[str, object]], value["command_classes"])
        command_classes["git-publication"]["allowed"] = True
        value["capabilities"] = {"git_metadata": {"allowed": True}, "network": {"allowed": True}}
        meta = self.meta()
        meta["execution_envelope"] = value
        meta["execution_envelope_digest"] = canonical_digest(value)
        denied = preflight(meta, "worker", "git-publication", ["src"], self.worktree)
        self.assertEqual("EXTERNAL_SIDE_EFFECT_AUTHORIZATION_REQUIRED", denied.code)
        allowed = preflight(meta, "worker", "git-publication", ["src"], self.worktree, True)
        self.assertTrue(allowed.allowed)

    def test_publication_capabilities_fail_closed_and_v1_stays_offline(self) -> None:
        denied = preflight(self.meta(), "worker", "git-publication", ["src"], self.worktree)
        self.assertEqual("COMMAND_CLASS_DENIED", denied.code)
        value = envelope()
        value["schema_version"] = 2
        command_classes = cast(dict[str, dict[str, object]], value["command_classes"])
        command_classes["git-publication"]["allowed"] = True
        value["capabilities"] = {"git_metadata": {"allowed": True}, "network": {"allowed": False}}
        meta = self.meta()
        meta["execution_envelope"] = value
        meta["execution_envelope_digest"] = canonical_digest(value)
        self.assertEqual(
            "NETWORK_CAPABILITY_DENIED",
            preflight(meta, "worker", "git-publication", ["src"], self.worktree, True).code,
        )
        self.assertTrue(errors({**value, "capabilities": {"git_metadata": {"allowed": True}}}))

    def test_validator_rejects_schema_shape_and_identity_failures(self) -> None:
        cases = (
            ({"schema_version": 2}, "missing field"),
            ({**envelope(), "envelope_id": "wrong"}, "envelope_id is invalid"),
            ({**envelope(), "task": "wrong"}, "task is invalid"),
            ({**envelope(), "spec_ref": "../unsafe"}, "spec_ref is invalid"),
            (
                {**envelope(), "path_scope": {"read": ["src"], "write": ["src", "src"]}},
                "duplicates",
            ),
            ({**envelope(), "outputs": [{"id": "output"}]}, "outputs contain an invalid item"),
            ({**envelope(), "evidence": [{"id": "tests"}]}, "evidence contain an invalid item"),
            ({**envelope(), "stop_conditions": [{"id": "scope", "kind": "bad"}]}, "invalid rule"),
        )
        for value, expected in cases:
            self.assertTrue(any(expected in item for item in errors(value)), expected)
        self.assertEqual(
            "sha256:" + "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824",
            digest(b"hello"),
        )
        self.assertEqual(self.meta()["execution_envelope_digest"], canonical_digest(envelope()))
        self.assertEqual(
            {
                "allowed": True,
                "code": "OK",
                "detail": "detail",
                "envelope_id": "",
                "envelope_digest": "",
            },
            Preflight(True, "OK", "detail").as_json(),
        )

    def test_validator_rejects_adversarial_collections_rules_and_bound_records(self) -> None:
        """Exercise every closed-schema rejection before it reaches a task record."""
        cases = (
            (None, "envelope must be an object"),
            ({**envelope(), "path_scope": {"read": [], "write": ["src"]}}, "bounded nonempty"),
            ({**envelope(), "path_scope": {"read": [".hidden"], "write": ["src"]}}, "unsafe"),
            ({**envelope(), "outputs": [{"id": "bad id", "description": "x"}]}, "identifiers"),
            ({**envelope(), "non_goals": []}, "non_goals"),
            ({**envelope(), "command_classes": {"test": {"allowed": "yes"}}}, "invalid rule"),
            ({**envelope(), "stop_conditions": "bad"}, "bounded nonempty"),
        )
        for value, expected in cases:
            self.assertTrue(any(expected in error for error in errors(value)), expected)
        missing = self.meta()
        missing.pop("execution_envelope")
        self.assertEqual(
            "ENVELOPE_MISSING", preflight(missing, "worker", "test", [], self.worktree).code
        )
        invalid = self.meta()
        invalid["execution_envelope"] = {"schema_version": 1}
        self.assertEqual(
            "ENVELOPE_INVALID", preflight(invalid, "worker", "test", [], self.worktree).code
        )
        outside = preflight(self.meta(), "worker", "test", ["unbound/file"], self.worktree)
        self.assertEqual("PATH_OUTSIDE_SCOPE", outside.code)

    def test_load_is_root_bound_and_preflight_denies_bad_lease_and_class(self) -> None:
        loaded, exact_digest, found = load(self.root, self.reference)
        self.assertEqual([], found)
        self.assertEqual(envelope(), loaded)
        self.assertEqual(digest(self.payload), exact_digest)
        self.assertEqual(["envelope reference is unsafe"], load(self.root, "../escape")[2])
        malformed = self.root / "malformed.json"
        malformed.write_text("{", encoding="utf-8")
        self.assertTrue(load(self.root, "malformed.json")[2][0].startswith("cannot read envelope:"))
        no_lease = {**self.meta(), "claim_expires": ""}
        self.assertEqual(
            "OWNER_CLAIM_REQUIRED", preflight(no_lease, "worker", "test", [], self.worktree).code
        )
        invalid_lease = {**self.meta(), "claim_expires": "invalid"}
        self.assertEqual(
            "OWNER_CLAIM_REQUIRED",
            preflight(invalid_lease, "worker", "test", [], self.worktree).code,
        )
        denied = preflight(self.meta(), "worker", "unknown", [], self.worktree)
        self.assertEqual("COMMAND_CLASS_DENIED", denied.code)
        (self.root / self.reference).unlink()
        external = self.root / "external.json"
        external.write_text("{}", encoding="utf-8")
        (self.root / self.reference).symlink_to(external)
        self.assertEqual(
            ["envelope reference contains a symlink"], load(self.root, self.reference)[2]
        )


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
