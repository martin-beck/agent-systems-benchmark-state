# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
# mypy: disable-error-code=attr-defined
"""Focused edge contracts for the vendored autonomy-limit policy helpers."""

from __future__ import annotations

import argparse
import io
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from tools import autonomy_limits

NOW = "2026-10-13T12:00:00+00:00"


def command(**values: object) -> argparse.Namespace:
    base = {
        "task": "AR-0001",
        "owner": "solo",
        "expected_revision": 2,
        "autonomy_diff_bytes": 0,
        "autonomy_returncode": 0,
        "cost_units": 0,
        "external_side_effect": False,
        "command_class": None,
    }
    base.update(values)
    return argparse.Namespace(**base)


def meta() -> autonomy_limits.Meta:
    return {
        "id": "AR-0001",
        "owner": "solo",
        "status": "in_progress",
        "task_revision": 2,
    }


def selected() -> autonomy_limits.Meta:
    return {"schema_version": 1, "max_commands": 2, "digest": "sha256:" + "a" * 64}


class _DiffProcess:
    def __init__(self, chunks: bytes, returncode: int = 0) -> None:
        self.stdout = io.BytesIO(chunks)
        self.returncode = returncode

    def wait(self, *, timeout: int) -> int:
        if timeout != 10:
            raise AssertionError("diff command must have a bounded wait")
        return self.returncode


class AutonomyLimitsEdgeTests(unittest.TestCase):
    def test_canonical_and_git_failure_fallbacks_are_deterministic(self) -> None:
        self.assertEqual('{"a":1,"b":2}', autonomy_limits._canonical({"b": 2, "a": 1}))
        with patch.object(autonomy_limits.subprocess, "run", side_effect=OSError("unavailable")):
            self.assertFalse(autonomy_limits._tracked(Path("/missing"), b"policy"))
            self.assertFalse(autonomy_limits._head_tracks(Path("/missing")))

    def test_unreadable_policy_and_changed_snapshot_fail_closed(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / autonomy_limits.POLICY_NAME
            path.write_text('{"schema_version":1,"max_commands":2}')
            with (
                patch.object(Path, "read_bytes", side_effect=OSError("denied")),
                self.assertRaisesRegex(autonomy_limits.PolicyError, "unreadable"),
            ):
                autonomy_limits.policy(root)

        expected = selected()
        with (
            patch.object(autonomy_limits, "policy", return_value={**expected, "max_commands": 3}),
            self.assertRaisesRegex(autonomy_limits.PolicyError, "changed during operation"),
        ):
            autonomy_limits.require_unchanged(Path("/repo"), expected)

    def test_diff_measurement_counts_bytes_and_rejects_git_failure(self) -> None:
        with patch.object(
            autonomy_limits.subprocess, "Popen", return_value=_DiffProcess(b"a" * 65537)
        ):
            self.assertEqual(65537, autonomy_limits.diff_bytes(Path("/repo")))
        with (
            patch.object(
                autonomy_limits.subprocess, "Popen", return_value=_DiffProcess(b"", returncode=1)
            ),
            self.assertRaisesRegex(RuntimeError, "cannot measure"),
        ):
            autonomy_limits.diff_bytes(Path("/repo"))

    def test_metadata_rejects_missing_fields_and_invalid_identity(self) -> None:
        task = meta()
        autonomy_limits.apply_preflight(command(), task, selected(), NOW)
        state = task["autonomy_limits"]
        del state["hold"]
        self.assertEqual("autonomy limits fields are invalid", autonomy_limits.metadata_error(task))

        task = meta()
        autonomy_limits.apply_preflight(command(), task, selected(), NOW)
        task["autonomy_limits"]["policy_digest"] = "not-a-digest"
        self.assertEqual(
            "autonomy limits identity is invalid", autonomy_limits.metadata_error(task)
        )

    def test_no_policy_preflight_and_transition_dispose_follow_lifecycle_contract(self) -> None:
        task = meta()
        self.assertEqual("", autonomy_limits.apply_preflight(command(), task, None, NOW))

        autonomy_limits.apply_preflight(command(), task, selected(), NOW)
        task["autonomy_limits"]["hold"] = {
            "trigger": "command",
            "observed": 2,
            "limit": 2,
            "held_at": NOW,
            "task_revision": 2,
        }
        dispose = command(
            cmd="autonomy-limits", expected_revision=2, reason="resume within local budget"
        )
        self.assertEqual(
            "Recorded local autonomy-limit disposition.",
            autonomy_limits.transition(
                lambda _args, _meta: self.fail("must not admit"), dispose, task, NOW
            ),
        )

    def test_dispose_defensively_rejects_stale_hold_fence(self) -> None:
        task = meta()
        autonomy_limits.apply_preflight(command(), task, selected(), NOW)
        task["autonomy_limits"]["hold"] = {
            "trigger": "command",
            "observed": 2,
            "limit": 2,
            "held_at": NOW,
            "task_revision": 1,
        }
        with (
            patch.object(autonomy_limits, "metadata_error", return_value=None),
            self.assertRaisesRegex(RuntimeError, "not fenced to the current revision"),
        ):
            autonomy_limits.apply_dispose(command(reason="resume"), task, NOW)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
