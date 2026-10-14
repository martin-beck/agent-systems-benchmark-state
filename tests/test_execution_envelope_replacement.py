# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Fail-closed successor execution-envelope replacement coverage."""

from __future__ import annotations

import argparse
import unittest
from typing import Any, cast
from unittest.mock import patch

from tools import execution_envelope, handoffctl
from tools.execution_envelope import canonical_digest


def _envelope(revision: int = 1, *, write: list[str] | None = None) -> dict[str, object]:
    return {
        "schema_version": 1,
        "envelope_id": f"AR-0001-e{revision}",
        "envelope_revision": revision,
        "task": "AR-0001",
        "task_revision": 3,
        "spec_ref": "spec.json",
        "spec_revision": 1,
        "outputs": [{"id": "output", "description": "bounded output"}],
        "non_goals": ["preserve restrictions"],
        "path_scope": {"read": ["src", "tests"], "write": write or ["src"]},
        "command_classes": {"test": {"allowed": True, "timeout_seconds": 60}},
        "evidence": [{"id": "tests", "class": "contract-test", "required": True}],
        "stop_conditions": [{"id": "scope", "kind": "deny"}],
    }


class ReplacementTests(unittest.TestCase):
    def _meta(self) -> dict[str, object]:
        old = _envelope()
        return {
            "id": "AR-0001",
            "owner": "worker",
            "status": "in_progress",
            "claim_expires": "2099-01-01T00:00:00+00:00",
            "task_revision": 3,
            "spec_ref": "spec.json",
            "spec_revision": 1,
            "execution_envelope_ref": "envelopes/AR-0001-e1.json",
            "execution_envelope_revision": 1,
            "execution_envelope_task_revision": 3,
            "execution_envelope_digest": canonical_digest(old),
            "execution_envelope": old,
        }

    def _args(self, revision: int = 2, expected: int = 3) -> argparse.Namespace:
        return argparse.Namespace(
            task="AR-0001",
            owner="worker",
            expected_revision=expected,
            envelope_ref=f"envelopes/AR-0001-e{revision}.json",
            envelope_revision=revision,
        )

    def test_replaces_and_preserves_immutable_old_evidence(self) -> None:
        meta = self._meta()
        successor = _envelope(2)
        with (
            patch.object(handoffctl, "require_role_admission"),
            patch.object(execution_envelope, "load", return_value=(successor, "", [])),
        ):
            result = handoffctl.apply_replace_envelope(self._args(), meta)
        self.assertIn("Replaced execution envelope", result)
        evidence = cast(list[dict[str, Any]], meta["execution_envelope_replacements"])
        self.assertEqual(1, len(evidence))
        self.assertEqual("envelopes/AR-0001-e1.json", evidence[0]["old_ref"])
        self.assertEqual(canonical_digest(_envelope()), evidence[0]["old_digest"])
        self.assertEqual("envelopes/AR-0001-e2.json", meta["execution_envelope_ref"])

    def test_rejects_stale_owner_revision_reservation_and_scope_widening(self) -> None:
        successor = _envelope(2)
        for mutate, message in (
            (lambda m: m.update(owner="other"), "owned by"),
            (dict.copy, "stale revision"),
            (
                lambda m: m.update(execution_reservation={"live": True}),
                "EXECUTION_RECOVERY_REQUIRED",
            ),
        ):
            meta = self._meta()
            mutate(meta)
            args = self._args(expected=2 if message == "stale revision" else 3)
            with (
                patch.object(handoffctl, "require_role_admission"),
                patch.object(execution_envelope, "load", return_value=(successor, "", [])),
                self.assertRaisesRegex(RuntimeError, message),
            ):
                handoffctl.apply_replace_envelope(args, meta)
        meta = self._meta()
        broad = _envelope(2, write=["src", "tests"])
        with (
            patch.object(handoffctl, "require_role_admission"),
            patch.object(execution_envelope, "load", return_value=(broad, "", [])),
            self.assertRaisesRegex(RuntimeError, "widen path scope"),
        ):
            handoffctl.apply_replace_envelope(self._args(), meta)

    def test_replace_bound_rejects_each_successor_widening_boundary(self) -> None:
        import tempfile
        from pathlib import Path

        old = _envelope()
        successor = _envelope(2)
        args = self._args()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for mutate, message in ((lambda m: m.pop("execution_envelope"), "existing bound"),):
                meta = self._meta()
                mutate(meta)
                with self.assertRaisesRegex(RuntimeError, message):
                    execution_envelope.replace_bound(meta, args, root, "2026-01-01T00:00:00Z")
            meta = self._meta()
            with (
                patch.object(execution_envelope, "load", return_value=(None, "", ["bad"])),
                self.assertRaisesRegex(RuntimeError, "envelope is invalid"),
            ):
                execution_envelope.replace_bound(meta, args, root, "2026-01-01T00:00:00Z")
            for mutate, message in (
                (lambda e: e.update(task_revision=4), "revision does not match task"),
                (lambda e: e.update(envelope_revision=9), "envelope revision does not match"),
                (lambda e: e.update(envelope_id=old["envelope_id"]), "distinct successor"),
                (lambda e: e.update(non_goals=["other restriction"]), "remove non-goals"),
            ):
                candidate = dict(successor)
                mutate(candidate)
                meta = self._meta()
                with (
                    patch.object(execution_envelope, "load", return_value=(candidate, "", [])),
                    self.assertRaisesRegex(RuntimeError, message),
                ):
                    execution_envelope.replace_bound(meta, args, root, "2026-01-01T00:00:00Z")


if __name__ == "__main__":
    unittest.main()
