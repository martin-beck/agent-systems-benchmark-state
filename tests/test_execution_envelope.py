# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Contract tests for immutable, non-authorizing execution envelopes."""

from __future__ import annotations

import json
import os
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace
from unittest.mock import patch

from tools import execution_envelope
from tools.execution_envelope import Preflight, canonical_digest, digest, errors, load, preflight


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
        (self.worktree / "tests").mkdir()
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

    def test_descriptor_openers_reject_unsafe_missing_and_non_directory_sources(self) -> None:
        file_path = self.root / "plain-file"
        file_path.write_text("not a directory", encoding="utf-8")
        with self.assertRaisesRegex(RuntimeError, "must be absolute"):
            execution_envelope._open_path(Path("relative"))
        with self.assertRaisesRegex(FileNotFoundError, "missing"):
            execution_envelope._open_path(self.root / "missing")
        with self.assertRaisesRegex(RuntimeError, "not a directory"):
            execution_envelope._open_path(file_path, directory=True)
        for relative in ("", ".", "../escape"):
            with self.assertRaisesRegex(RuntimeError, "unsafe"):
                execution_envelope._open_scope_path(self.worktree, relative)
        with self.assertRaisesRegex(FileNotFoundError, "missing"):
            execution_envelope._open_scope_path(self.worktree, "missing")
        with self.assertRaisesRegex(RuntimeError, "non-directory component"):
            execution_envelope._open_scope_path(self.root, "plain-file/child")

    def test_sandbox_command_serializes_descriptor_and_fallback_mount_modes(self) -> None:
        descriptor = os.open(self.worktree, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
        try:
            bound = SimpleNamespace(
                command=["true"],
                _envelope_worktree=str(self.worktree),
                _envelope_worktree_fd=descriptor,
                _envelope_write_scope=["src"],
                _envelope_read_scope=["tests"],
            )
            with patch("tools.execution_envelope.shutil.which", return_value="/usr/bin/bwrap"):
                bound_payload = json.loads(execution_envelope.sandboxed_envelope_command(bound)[4])
            self.assertEqual(descriptor, bound_payload["specification"]["root_fd"])
            self.assertEqual(
                [
                    {"relative": "tests", "destination": "/worktree/tests", "mode": "--ro-bind"},
                    {"relative": "src", "destination": "/worktree/src", "mode": "--bind"},
                ],
                bound_payload["specification"]["mounts"],
            )
            delattr(bound, "_envelope_worktree_fd")
            with patch("tools.execution_envelope.shutil.which", return_value="/usr/bin/bwrap"):
                fallback_payload = json.loads(
                    execution_envelope.sandboxed_envelope_command(bound)[4]
                )
            self.assertIsNone(fallback_payload["specification"]["root_fd"])
            self.assertEqual("src", fallback_payload["specification"]["mounts"][1]["relative"])
        finally:
            os.close(descriptor)

    def test_sandbox_helper_rejects_bad_argv_and_releases_opened_descriptors(self) -> None:
        with (
            patch.object(sys, "argv", ["helper"]),
            self.assertRaisesRegex(RuntimeError, "arguments"),
        ):
            execution_envelope._run_sandbox_helper()
        with (
            patch.object(sys, "argv", ["helper", str(self.root), "{", "--"]),
            self.assertRaises(json.JSONDecodeError),
        ):
            execution_envelope._run_sandbox_helper()
        payload = {
            "command": ["bwrap"],
            "specification": {
                "root": str(self.worktree),
                "root_fd": None,
                "mounts": [
                    {"relative": "src", "destination": "/worktree/src", "mode": "--ro-bind"}
                ],
            },
        }
        seed = os.open(self.worktree, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
        opened: list[int] = []

        def duplicate(*_args: object, **_kwargs: object) -> int:
            descriptor = os.dup(seed)
            opened.append(descriptor)
            return descriptor

        argv = ["helper", str(self.root), json.dumps(payload), "--", "true"]
        try:
            with (
                patch.object(sys, "argv", argv),
                patch.object(execution_envelope, "_open_path", side_effect=duplicate),
                patch.object(execution_envelope, "_open_scope_path", side_effect=duplicate),
                patch("tools.execution_envelope.shutil.which", return_value=None),
                self.assertRaisesRegex(RuntimeError, "requires bubblewrap"),
            ):
                execution_envelope._run_sandbox_helper()
            self.assertEqual(4, len(opened))
            for descriptor in opened:
                with self.assertRaises(OSError):
                    os.fstat(descriptor)
        finally:
            os.close(seed)

    def test_sandbox_helper_uses_inherited_root_descriptor_and_cleans_up_after_exec(self) -> None:
        root_descriptor = os.open(self.worktree, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
        seed = os.open(self.worktree, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
        opened: list[int] = []

        def duplicate(*_args: object, **_kwargs: object) -> int:
            descriptor = os.dup(seed)
            opened.append(descriptor)
            return descriptor

        payload = {
            "command": ["bwrap"],
            "specification": {
                "root": str(self.worktree),
                "root_fd": root_descriptor,
                "mounts": [{"relative": "src", "destination": "/worktree/src", "mode": "--bind"}],
            },
        }
        argv = ["helper", str(self.root), json.dumps(payload), "--", "true"]
        try:
            with (
                patch.object(sys, "argv", argv),
                patch.object(execution_envelope, "_open_path", side_effect=duplicate),
                patch.object(
                    execution_envelope, "_open_scope_fd", side_effect=duplicate
                ) as scope_fd,
                patch.object(execution_envelope.os, "execvpe", side_effect=OSError("exec blocked")),
                patch("tools.execution_envelope.shutil.which", return_value="/usr/bin/bwrap"),
                self.assertRaisesRegex(OSError, "exec blocked"),
            ):
                execution_envelope._run_sandbox_helper()
            scope_fd.assert_called_once_with(root_descriptor, "src")
            self.assertEqual(4, len(opened))
            os.fstat(root_descriptor)
            for descriptor in opened:
                with self.assertRaises(OSError):
                    os.fstat(descriptor)
        finally:
            os.close(seed)
            os.close(root_descriptor)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
