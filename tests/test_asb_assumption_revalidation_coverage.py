# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Additional downstream edge coverage for assumption revalidation."""

from __future__ import annotations

import argparse
import subprocess
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from tools import assumption_revalidation as assumptions


def record(
    action: str = "declare", kind: str = "dependency", binding: object | None = None
) -> dict[str, object]:
    if binding is None:
        binding = {"task": "AR-0002", "task_revision": 1}
    return assumptions._record(
        action, "check", kind, True, binding, 1, "", "gone" if action == "dispose" else ""
    )


class AssumptionRevalidationCoverageTests(unittest.TestCase):
    def test_validation_helpers_reject_invalid_kinds_bindings_and_identities(self) -> None:
        with self.assertRaisesRegex(ValueError, "identity"):
            assumptions._record("unknown", "check", "dependency", True, {}, 1, "")
        for kind, binding in (
            ("base", {"head": "not-a-head"}),
            ("dependency", {"task": "AR-x", "task_revision": 0}),
            ("observation", {"ref": "../escape", "digest": "sha256:" + "0" * 64}),
            ("unknown", {}),
        ):
            with self.subTest(kind=kind), self.assertRaisesRegex(ValueError, "binding|kind"):
                assumptions._validate_binding(kind, binding)
        with self.assertRaisesRegex(ValueError, "fields"):
            assumptions._record_fields([])

    def test_ledger_rejects_duplicate_invalid_followups_and_disposed_changes(self) -> None:
        first = record()
        duplicate = assumptions._record(
            "declare",
            "check",
            "dependency",
            True,
            {"task": "AR-0002", "task_revision": 2},
            2,
            str(first["digest"]),
        )
        missing = assumptions._record(
            "revalidate",
            "missing",
            "dependency",
            True,
            {"task": "AR-0002", "task_revision": 2},
            1,
            "",
        )
        disposed = assumptions._record(
            "dispose",
            "check",
            "dependency",
            True,
            {"task": "AR-0002", "task_revision": 2},
            2,
            str(first["digest"]),
            "replaced",
        )
        changed_after_dispose = assumptions._record(
            "revalidate",
            "check",
            "dependency",
            True,
            {"task": "AR-0002", "task_revision": 3},
            3,
            str(disposed["digest"]),
        )
        for history, message in (
            ([first, duplicate], "more than once"),
            ([missing], "follow-up"),
            ([first, disposed, changed_after_dispose], "disposed"),
        ):
            with self.subTest(message=message), self.assertRaisesRegex(ValueError, message):
                assumptions.records({"assumption_revalidation": history})

    def test_apply_rejects_record_limit_and_invalid_disposition_before_mutation(self) -> None:
        meta: dict[str, object] = {
            "id": "AR-0001",
            "owner": "worker",
            "status": "in_progress",
            "task_revision": 1,
        }
        args = argparse.Namespace(
            task="AR-0001",
            owner="worker",
            expected_revision=1,
            assumption_action="declare",
            assumption_id="next",
            kind="dependency",
            reference="AR-0002",
            material=True,
            reason="",
        )
        with (
            patch.object(assumptions, "records", return_value=[record()] * 64),
            self.assertRaisesRegex(RuntimeError, "bounded record limit"),
        ):
            assumptions.apply(Path(), Path(), args, meta, [])
        meta["assumption_revalidation"] = [record()]
        args.assumption_action = "dispose"
        args.assumption_id = "check"
        args.kind = None
        args.material = None
        with self.assertRaisesRegex(RuntimeError, "disposition requires a reason"):
            assumptions.apply(
                Path(),
                Path(),
                args,
                meta,
                [{"id": "AR-0002", "task_revision": 1}],
            )

    def test_owner_and_followup_fences_reject_policy_drift(self) -> None:
        meta: dict[str, object] = {
            "id": "AR-0001",
            "owner": "worker",
            "status": "in_progress",
            "task_revision": 2,
        }
        args = argparse.Namespace(
            task="AR-0001",
            owner="worker",
            expected_revision=2,
            assumption_action="revalidate",
            assumption_id="check",
            kind=None,
            reference=None,
            material=None,
        )
        for field, value, message in (
            ("task", "AR-9999", "does not match"),
            ("owner", "other", "owned by"),
            ("expected_revision", 1, "stale revision"),
        ):
            original = getattr(args, field)
            setattr(args, field, value)
            with self.subTest(field=field), self.assertRaisesRegex(RuntimeError, message):
                assumptions._require_fenced_owner(args, meta)
            setattr(args, field, original)
        meta["status"] = "open"
        with self.assertRaisesRegex(RuntimeError, "active task"):
            assumptions._require_fenced_owner(args, meta)
        existing = record()
        with self.assertRaisesRegex(RuntimeError, "declared before"):
            assumptions._followup_identity(args, None)
        disposed = {**existing, "action": "dispose"}
        with self.assertRaisesRegex(RuntimeError, "disposed"):
            assumptions._followup_identity(args, disposed)
        args.kind = "observation"
        with self.assertRaisesRegex(RuntimeError, "cannot change"):
            assumptions._followup_identity(args, existing)

    def test_bounded_filesystem_and_git_observation_failures(self) -> None:
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "regular").write_text("ok", encoding="utf-8")
            self.assertEqual(71, len(assumptions._file_digest(root, "regular")))
            (root / "link").symlink_to(root / "regular")
            for reference in ("../escape", "missing"):
                with self.assertRaisesRegex(RuntimeError, "observation"):
                    assumptions._file_digest(root, reference)
            self.assertEqual(71, len(assumptions._file_digest(root, "link")))
            (root / "directory").mkdir()
            with self.assertRaisesRegex(RuntimeError, "bounded regular"):
                assumptions._file_digest(root, "directory")
            with (
                patch.object(
                    subprocess, "run", return_value=subprocess.CompletedProcess([], 1, "", "")
                ),
                self.assertRaisesRegex(RuntimeError, "Git HEAD"),
            ):
                assumptions._git_head(root)
            with self.assertRaisesRegex(RuntimeError, "safely bound"):
                assumptions._worktree(root, {"worktree_key": "../bad"})
            with self.assertRaisesRegex(RuntimeError, "unavailable"):
                assumptions._worktree(root, {"worktree_key": "missing"})

    def test_record_validation_rejects_tampering_and_invalid_histories(self) -> None:
        invalid = record()
        invalid["digest"] = "sha256:" + "0" * 64
        with self.assertRaisesRegex(ValueError, "identity"):
            assumptions.records({"assumption_revalidation": [invalid]})
        first = record()
        with_reason = assumptions._record(
            "revalidate",
            "check",
            "dependency",
            True,
            {"task": "AR-0002", "task_revision": 2},
            2,
            str(first["digest"]),
            "not allowed here",
        )
        with self.assertRaisesRegex(ValueError, "disposition"):
            assumptions.records({"assumption_revalidation": [first, with_reason]})
        with self.assertRaisesRegex(ValueError, "fields"):
            assumptions.records({"assumption_revalidation": [{"extra": True}]})
        second = assumptions._record(
            "revalidate",
            "check",
            "dependency",
            True,
            {"task": "AR-0002", "task_revision": 2},
            2,
            "sha256:" + "1" * 64,
        )
        with self.assertRaisesRegex(ValueError, "not linked"):
            assumptions.records({"assumption_revalidation": [first, second]})
        with self.assertRaisesRegex(ValueError, "history"):
            assumptions.records({"assumption_revalidation": [first] * 65})

    def test_current_binding_and_dependency_validation_edges(self) -> None:
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            meta: dict[str, object] = {"worktree_key": "worker"}
            tasks: list[dict[str, object]] = [{"id": "AR-0002", "task_revision": 2}]
            dependency = record()
            self.assertEqual(
                {"task": "AR-0002", "task_revision": 2},
                assumptions.current_binding(root, root, meta, tasks, dependency),
            )
            with self.assertRaisesRegex(RuntimeError, "invalid"):
                assumptions._dependency(tasks, "AR-x")
            with self.assertRaisesRegex(RuntimeError, "unavailable"):
                assumptions._dependency([], "AR-0002")
            broken = record(binding={"task": "AR-0002", "task_revision": 0})
            with self.assertRaisesRegex(ValueError, "binding"):
                assumptions.current_binding(root, root, meta, tasks, broken)

    def test_admission_reports_lookup_errors_and_ignores_disposed_records(self) -> None:
        invalid_base = assumptions._record(
            "declare", "base", "base", True, {"head": "0" * 40}, 1, ""
        )
        meta: dict[str, object] = {
            "worktree_key": "missing",
            "assumption_revalidation": [invalid_base],
        }
        self.assertIn(
            "ASSUMPTION_REVALIDATION_REQUIRED: assumption base worktree is unavailable",
            assumptions.admission_error(Path(), Path(), meta, []),
        )
        disposed = assumptions._record(
            "dispose",
            "base",
            "base",
            True,
            {"head": "0" * 40},
            2,
            str(invalid_base["digest"]),
            "no longer material",
        )
        meta["assumption_revalidation"] = [invalid_base, disposed]
        self.assertIsNone(assumptions.admission_error(Path(), Path(), meta, []))
