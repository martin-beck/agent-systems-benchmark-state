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
