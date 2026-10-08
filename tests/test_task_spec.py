# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Positive and hostile task-spec contract tests."""

from __future__ import annotations

import json
import os
import stat
import subprocess
import tempfile
import unittest
from pathlib import Path
from typing import Any
from unittest.mock import patch

import jsonschema

from tools import handoffctl
from tools.task_spec import (
    POLICY_NAME,
    EvidencePolicy,
    TaskSpecPolicyError,
    _head_tracks_policy,
    _tracked_clean_policy,
    done_admission_error,
    evidence_policy,
    require_policy_unchanged,
    spec_errors,
    task_spec_errors,
    task_spec_policy_errors,
)

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "examples/task-specs"


def load(name: str) -> dict[str, Any]:
    value = json.loads((FIXTURES / name).read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise TypeError("fixture must be an object")
    return value


class TaskSpecTests(unittest.TestCase):
    def _git(self, root: Path, *args: str) -> None:
        subprocess.run(["/usr/bin/git", "-C", str(root), *args], check=True)  # noqa: S603

    def _commit(self, root: Path) -> None:
        if not (root / ".git").exists():
            self._git(root, "init", "-q")
            self._git(root, "config", "user.name", "Policy Test")
            self._git(root, "config", "user.email", "policy@example.invalid")
        self._git(root, "add", "-A")
        self._git(root, "commit", "-q", "-m", "fixture")

    def _policy(
        self, root: Path, additions: list[str] | None = None, *, commit: bool = True
    ) -> Path:
        path = root / "task-spec-policy.json"
        path.write_text(
            json.dumps(
                {
                    "schema_version": 1,
                    "additional_evidence_classes": additions
                    or ["hosted", "offline", "privacy", "journey", "quality"],
                }
            )
            + "\n",
            encoding="utf-8",
        )
        if commit:
            self._commit(root)
        return path

    def _acceptance(self) -> dict[str, Any]:
        return {
            "spec_ref": "examples/task-specs/AR-0070.json",
            "spec_revision": 1,
            "status": "pass",
            "evidence_class": "contract-test",
            "evidence_ref": "awq/evidence/AR-0070",
            "evidence_digest": "sha256:" + "a" * 64,
        }

    def test_valid_spec_and_optional_metadata_are_accepted(self) -> None:
        value = load("AR-0070.json")
        self.assertEqual([], spec_errors(value))
        self.assertEqual(
            [],
            task_spec_errors(
                ROOT,
                {"id": "AR-0070", "spec_ref": value["spec_ref"], "spec_revision": 1},
            ),
        )

    def test_public_schemas_accept_additive_fixture_and_reject_collisions(self) -> None:
        spec_schema = json.loads((ROOT / "schema/task-spec.schema.json").read_text())
        policy_schema = json.loads((ROOT / "schema/task-spec-policy.schema.json").read_text())
        jsonschema.Draft202012Validator(spec_schema).validate(load("downstream-additive.json"))
        policy = {
            "schema_version": 1,
            "additional_evidence_classes": [
                "hosted",
                "offline",
                "privacy",
                "journey",
                "quality",
            ],
        }
        jsonschema.Draft202012Validator(policy_schema).validate(policy)
        with self.assertRaises(jsonschema.ValidationError):
            jsonschema.Draft202012Validator(policy_schema).validate(
                {**policy, "additional_evidence_classes": ["mechanical"]}
            )

    def test_handoffctl_core_validates_bound_metadata(self) -> None:
        meta: dict[str, Any] = {
            "schema_version": 1,
            "id": "AR-0070",
            "title": "Task spec",
            "status": "open",
            "priority": "P0",
            "summary": "summary",
            "next_action": "action",
            "task_revision": 1,
            "updated_at": "2026-01-01T00:00:00+00:00",
            "spec_ref": "examples/task-specs/AR-0070.json",
            "spec_revision": 1,
        }
        self.assertEqual([], handoffctl.basic_task_errors(ROOT / "task.md", meta))

    def test_hostile_specs_fail_closed(self) -> None:
        self.assertTrue(
            any("overlap" in error for error in spec_errors(load("hostile-overlap.json")))
        )

    def test_spec_shape_and_duplicate_collections_fail_closed(self) -> None:
        value = load("AR-0070.json")
        value["definition_of_done"].append(value["definition_of_done"][0])
        value["acceptance_predicates"] = [{"unexpected": "field"}]
        value["inputs"] = [{"id": "bad id", "description": ""}]
        value["outputs"] = [
            {"id": "duplicate", "description": "one"},
            {"id": "duplicate", "description": "two"},
        ]
        errors = spec_errors(value)
        self.assertIn("definition_of_done must not contain duplicates", errors)
        self.assertIn("acceptance_predicates items must contain only id and description", errors)
        self.assertIn("inputs has an invalid id", errors)
        self.assertIn("inputs has an invalid description", errors)
        self.assertIn("outputs ids must be unique", errors)
        self.assertEqual(["spec must be an object"], spec_errors([]))
        self.assertTrue(
            any(
                "unknown evidence class" in error
                for error in spec_errors(load("hostile-unknown-evidence.json"))
            )
        )

    def test_missing_and_partial_metadata_fail_closed(self) -> None:
        self.assertEqual([], task_spec_errors(ROOT, {"id": "AR-0001"}))
        self.assertEqual(
            ["AR-0001: spec_ref is required"],
            task_spec_errors(ROOT, {"id": "AR-0001", "spec_revision": 1}),
        )
        errors = task_spec_errors(
            ROOT,
            {"id": "AR-0001", "spec_ref": "examples/task-specs/AR-0070.json", "spec_revision": 2},
        )
        self.assertIn("AR-0001: spec_revision does not match referenced spec", errors)

    def test_unsafe_missing_and_malformed_references_fail_closed(self) -> None:
        for ref in ("../secret.json", "/absolute/spec.json", "bad ref"):
            with self.subTest(ref=ref):
                errors = task_spec_errors(
                    ROOT, {"id": "AR-0001", "spec_ref": ref, "spec_revision": 1}
                )
                self.assertTrue(any("spec_ref is unsafe" in error for error in errors))
        missing = task_spec_errors(
            ROOT,
            {"id": "AR-0001", "spec_ref": "examples/task-specs/missing.json", "spec_revision": 1},
        )
        self.assertTrue(any("cannot read spec_ref" in error for error in missing))
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "bad.json"
            path.write_text("{", encoding="utf-8")
            errors = task_spec_errors(
                root, {"id": "AR-0001", "spec_ref": "bad.json", "spec_revision": 1}
            )
            self.assertTrue(any("cannot read spec_ref" in error for error in errors))

    def test_spec_shape_errors_cover_unknown_and_missing_fields(self) -> None:
        errors = spec_errors({"schema_version": 2, "unexpected": True})
        self.assertIn("spec contains unknown field: unexpected", errors)
        self.assertIn("spec missing field: acceptance_predicates", errors)
        self.assertIn("spec schema_version must be 1", errors)

    def test_invalid_revision_and_bound_reference_are_rejected(self) -> None:
        for revision in (True, 0, "1"):
            with self.subTest(revision=revision):
                errors = task_spec_errors(
                    ROOT,
                    {
                        "id": "AR-0001",
                        "spec_ref": "examples/task-specs/AR-0070.json",
                        "spec_revision": revision,
                    },
                )
                self.assertIn("AR-0001: spec_revision must be a positive integer", errors)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            spec = load("AR-0070.json")
            spec["spec_ref"] = "other.json"
            (root / "spec.json").write_text(json.dumps(spec), encoding="utf-8")
            errors = task_spec_errors(
                root, {"id": "AR-0001", "spec_ref": "spec.json", "spec_revision": 1}
            )
            self.assertIn("AR-0001: spec_ref does not match referenced spec", errors)

    def test_done_admission_requires_matching_pass_evidence(self) -> None:
        acceptance = self._acceptance()
        meta: dict[str, Any] = {
            "id": "AR-0070",
            "spec_ref": "examples/task-specs/AR-0070.json",
            "spec_revision": 1,
            "spec_acceptance": acceptance,
        }
        self.assertIsNone(done_admission_error(ROOT, meta))
        for field, value in (("status", "fail"), ("evidence_class", "invented")):
            rejected = dict(acceptance)
            rejected[field] = value
            with self.subTest(field=field):
                self.assertIn(
                    "done admission denied",
                    done_admission_error(ROOT, {**meta, "spec_acceptance": rejected}) or "",
                )
        incomplete = dict(meta)
        incomplete.pop("spec_acceptance")
        self.assertIn("incomplete", done_admission_error(ROOT, incomplete) or "")

    def test_bound_additive_policy_is_shared_by_spec_and_done_admission(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = load("downstream-additive.json")
            source["spec_ref"] = "spec.json"
            (root / "spec.json").write_text(json.dumps(source) + "\n", encoding="utf-8")
            self._policy(root, commit=False)
            self._commit(root)
            policy = evidence_policy(root)
            self.assertTrue(policy.present)
            self.assertTrue(
                {"hosted", "offline", "privacy", "journey", "quality"} <= policy.classes
            )
            meta = {"id": "AR-0001", "spec_ref": "spec.json", "spec_revision": 1}
            self.assertEqual([], task_spec_errors(root, meta, policy))
            acceptance = {
                "spec_ref": "spec.json",
                "spec_revision": 1,
                "status": "pass",
                "evidence_class": "hosted",
                "evidence_ref": "quality/AR-0001",
                "evidence_digest": "sha256:" + "b" * 64,
            }
            self.assertIsNone(done_admission_error(root, {**meta, "spec_acceptance": acceptance}))
            (root / "task-spec-policy.json").unlink()
            self.assertIn("tracked and unchanged", "\n".join(task_spec_policy_errors(root)))
            with self.assertRaisesRegex(TaskSpecPolicyError, "changed during operation"):
                require_policy_unchanged(root, policy)

    def test_absent_policy_preserves_closed_default_vocabulary(self) -> None:
        self.assertTrue(
            any(
                "unknown evidence class" in error
                for error in spec_errors(load("downstream-additive.json"))
            )
        )
        self.assertEqual([], task_spec_policy_errors(ROOT))

    def test_policy_shape_identity_size_and_tracking_fail_closed(self) -> None:
        cases: list[tuple[str, object]] = [
            ("wrong-version", {"schema_version": 2, "additional_evidence_classes": ["hosted"]}),
            (
                "unknown-field",
                {"schema_version": 1, "additional_evidence_classes": ["hosted"], "x": 1},
            ),
            (
                "duplicate",
                {"schema_version": 1, "additional_evidence_classes": ["hosted", "hosted"]},
            ),
            ("collision", {"schema_version": 1, "additional_evidence_classes": ["mechanical"]}),
            ("invalid", {"schema_version": 1, "additional_evidence_classes": ["Hosted"]}),
        ]
        for name, value in cases:
            with self.subTest(name=name), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                (root / "task-spec-policy.json").write_text(
                    json.dumps(value) + "\n", encoding="utf-8"
                )
                self._commit(root)
                errors = task_spec_policy_errors(root)
                self.assertTrue(errors)
                self.assertNotIn(str(root), "\n".join(errors))

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "task-spec-policy.json"
            path.write_bytes(b"{" + b"x" * 4096)
            self._commit(root)
            self.assertIn("size", "\n".join(task_spec_policy_errors(root)))

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / "target.json"
            target.write_text("{}\n", encoding="utf-8")
            (root / "task-spec-policy.json").symlink_to(target.name)
            self._commit(root)
            self.assertTrue(task_spec_policy_errors(root))

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = self._policy(root)
            path.write_text(path.read_text() + " ", encoding="utf-8")
            self.assertIn("tracked and unchanged", "\n".join(task_spec_policy_errors(root)))

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = self._policy(root)
            path.chmod(stat.S_IMODE(path.stat().st_mode) | 0o002)
            self.assertIn("unsafe identity", "\n".join(task_spec_policy_errors(root)))

    def test_policy_identity_race_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = self._policy(root)
            original_read = os.read

            def replace_after_read(descriptor: int, size: int) -> bytes:
                payload = original_read(descriptor, size)
                replacement = root / "replacement.json"
                replacement.write_bytes(payload)
                replacement.replace(path)
                return payload

            with patch.object(os, "read", side_effect=replace_after_read):
                self.assertIn("identity changed", "\n".join(task_spec_policy_errors(root)))

    def test_policy_git_verification_rejects_entry_swaps_at_every_boundary(self) -> None:
        for boundary in ("before-git", "between-git", "after-cleanliness"):
            with self.subTest(boundary=boundary), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                path = self._policy(root)
                payload = path.read_bytes()
                original_run = subprocess.run
                calls = 0

                def swap_entry(
                    target_root: Path = root,
                    target_path: Path = path,
                    target_payload: bytes = payload,
                ) -> None:
                    replacement = target_root / "replacement.json"
                    replacement.write_bytes(target_payload)
                    replacement.replace(target_path)

                def racing_run(
                    command: Any,
                    *args: Any,
                    selected_boundary: str = boundary,
                    selected_run: Any = original_run,
                    **kwargs: Any,
                ) -> Any:
                    nonlocal calls
                    calls += 1
                    if selected_boundary == "before-git" and calls == 1:
                        swap_entry()
                    if selected_boundary == "between-git" and calls == 2:
                        swap_entry()
                    result = selected_run(command, *args, **kwargs)
                    if selected_boundary == "after-cleanliness" and "diff" in command:
                        swap_entry()
                    return result

                with patch("tools.task_spec.subprocess.run", side_effect=racing_run):
                    self.assertIn(
                        "identity changed",
                        "\n".join(task_spec_policy_errors(root)),
                    )

    def test_policy_parsed_bytes_must_equal_exact_head_blob(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = self._policy(root)
            original_read = os.read

            def committed_bytes_replaced_after_read(descriptor: int, size: int) -> bytes:
                payload = original_read(descriptor, size)
                path.write_bytes(payload.replace(b'"privacy"', b'"journey"', 1))
                return payload

            with patch.object(os, "read", side_effect=committed_bytes_replaced_after_read):
                self.assertIn("tracked and unchanged", "\n".join(task_spec_policy_errors(root)))

    def test_staged_policy_change_with_restored_worktree_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = self._policy(root)
            committed = path.read_bytes()
            path.write_bytes(committed.replace(b'"privacy"', b'"journey"', 1))
            self._git(root, "add", POLICY_NAME)
            path.write_bytes(committed)
            self.assertIn("tracked and unchanged", "\n".join(task_spec_policy_errors(root)))

    def test_index_swaps_around_cleanliness_checks_are_rejected(self) -> None:
        for boundary in ("after-index", "after-cached-diff"):
            with self.subTest(boundary=boundary), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                path = self._policy(root)
                committed = path.read_bytes()
                original_run = subprocess.run
                index_checks = 0

                def stage_b_worktree_a(
                    target_path: Path = path,
                    target_payload: bytes = committed,
                    target_root: Path = root,
                    selected_run: Any = original_run,
                ) -> None:
                    target_path.write_bytes(target_payload.replace(b'"privacy"', b'"journey"', 1))
                    selected_run(
                        ["/usr/bin/git", "-C", str(target_root), "add", POLICY_NAME], check=True
                    )
                    target_path.write_bytes(target_payload)

                def racing_run(
                    command: Any,
                    *args: Any,
                    selected_run: Any = original_run,
                    selected_boundary: str = boundary,
                    **kwargs: Any,
                ) -> Any:
                    nonlocal index_checks
                    result = selected_run(command, *args, **kwargs)
                    if "ls-files" in command and "-s" in command:
                        index_checks += 1
                        if selected_boundary == "after-index" and index_checks == 1:
                            stage_b_worktree_a()
                    if selected_boundary == "after-cached-diff" and "--cached" in command:
                        stage_b_worktree_a()
                    return result

                with patch("tools.task_spec.subprocess.run", side_effect=racing_run):
                    self.assertIn(
                        "tracked and unchanged",
                        "\n".join(task_spec_policy_errors(root)),
                    )

    def test_policy_io_and_git_failures_have_bounded_diagnostics(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with patch("tools.task_spec.subprocess.run", side_effect=OSError("injected")):
                self.assertFalse(_tracked_clean_policy(root))
                (root / ".git").mkdir()
                self.assertFalse(_head_tracks_policy(root))
            with patch("tools.task_spec.os.open", side_effect=OSError("injected")):
                self.assertEqual(
                    ["task-spec policy root is unavailable"], task_spec_policy_errors(root)
                )

        missing = Path(tempfile.gettempdir()) / "ar0087-missing-policy-root"
        self.assertEqual(["task-spec policy root is unavailable"], task_spec_policy_errors(missing))

    def test_invalid_utf8_and_policy_mismatch_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "task-spec-policy.json").write_bytes(b"\xff\xfe")
            self._commit(root)
            self.assertEqual(
                ["task-spec policy is not valid UTF-8 JSON"], task_spec_policy_errors(root)
            )

        expected = EvidencePolicy(frozenset({"hosted"}), "different", (1, 2), True)
        with (
            tempfile.TemporaryDirectory() as directory,
            self.assertRaisesRegex(TaskSpecPolicyError, "changed during operation"),
        ):
            require_policy_unchanged(Path(directory), expected)

    def test_policy_failures_reach_task_and_done_admission(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._policy(root)
            policy_path = root / "task-spec-policy.json"
            policy_path.write_text(policy_path.read_text() + " ", encoding="utf-8")
            meta = {"id": "AR-0001", "spec_ref": "spec.json", "spec_revision": 1}
            self.assertIn("tracked and unchanged", "\n".join(task_spec_errors(root, meta)))
            self.assertIn("tracked and unchanged", done_admission_error(root, meta) or "")

    def test_done_admission_rejects_every_mismatched_evidence_field(self) -> None:
        acceptance = self._acceptance()
        meta: dict[str, Any] = {
            "id": "AR-0070",
            "spec_ref": "examples/task-specs/AR-0070.json",
            "spec_revision": 1,
            "spec_acceptance": acceptance,
        }
        cases = (
            ("spec_ref", "other.json", "acceptance spec_ref"),
            ("spec_revision", 2, "acceptance spec_revision"),
            ("evidence_ref", "bad ref", "evidence ref"),
            ("evidence_digest", "bad", "evidence digest"),
        )
        for field, value, expected in cases:
            with self.subTest(field=field):
                changed = dict(acceptance)
                changed[field] = value
                self.assertIn(
                    expected,
                    done_admission_error(ROOT, {**meta, "spec_acceptance": changed}) or "",
                )
        self.assertIn(
            "done admission denied",
            done_admission_error(ROOT, {**meta, "spec_revision": 2}) or "",
        )


if __name__ == "__main__":
    unittest.main()
