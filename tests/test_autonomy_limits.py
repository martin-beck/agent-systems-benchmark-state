# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Contract coverage for opt-in autonomy budgets and local dispositions."""

from __future__ import annotations

import argparse
import io
import json
import subprocess
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace
from typing import cast
from unittest.mock import patch

from tools import autonomy_limits

NOW = "2026-10-13T12:00:00+00:00"
LATER = "2026-10-13T12:00:05+00:00"


def git(*arguments: str) -> None:
    subprocess.run(["/usr/bin/git", *arguments], check=True)  # noqa: S603


def args(**values: object) -> argparse.Namespace:
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


class AutonomyLimitsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.meta: autonomy_limits.Meta = {
            "id": "AR-0001",
            "owner": "solo",
            "status": "in_progress",
            "task_revision": 2,
        }

    def test_command_overrun_holds_and_solo_disposition_is_revision_fenced(self) -> None:
        selected = {"schema_version": 1, "max_commands": 1, "digest": "sha256:" + "a" * 64}
        self.assertIn("admitted", autonomy_limits.apply_preflight(args(), self.meta, selected, NOW))
        self.meta["task_revision"] = 3
        self.assertIn("hold", autonomy_limits.apply_record(args(), self.meta, selected, LATER))
        self.meta["task_revision"] = 4
        self.assertEqual(4, self.meta["autonomy_limits"]["hold"]["task_revision"])
        with self.assertRaisesRegex(RuntimeError, "stale revision"):
            autonomy_limits.apply_dispose(
                args(expected_revision=3, reason="scope changed"), self.meta, LATER
            )
        self.assertIn(
            "disposition",
            autonomy_limits.apply_dispose(
                args(expected_revision=4, reason="scope changed"), self.meta, LATER
            ),
        )
        self.assertIsNone(self.meta["autonomy_limits"]["hold"])

    def test_elapsed_retry_cost_diff_and_external_triggers_are_diagnostic(self) -> None:
        cases = (
            ({"max_elapsed_seconds": 1}, args(), LATER, "elapsed-time"),
            ({"max_retries": 1}, args(autonomy_returncode=1), LATER, "retry"),
            ({"max_cost_units": 2}, args(cost_units=2), LATER, "cost"),
            ({"max_diff_bytes": 3}, args(autonomy_diff_bytes=2), LATER, "diff-size"),
            (
                {"max_external_side_effects": 1},
                args(external_side_effect=True),
                LATER,
                "external-side-effect",
            ),
        )
        for index, (limits, command, at, trigger) in enumerate(cases):
            with self.subTest(trigger=trigger):
                meta = {
                    "id": "AR-0001",
                    "owner": "solo",
                    "status": "in_progress",
                    "task_revision": 2,
                }
                selected = {"schema_version": 1, **limits, "digest": "sha256:" + f"{index:x}" * 64}
                autonomy_limits.apply_preflight(command, meta, selected, NOW)
                meta["task_revision"] = 3
                completed = args(**vars(command))
                if trigger == "diff-size":
                    completed.autonomy_diff_bytes = 3
                autonomy_limits.apply_record(completed, meta, selected, at)
                state = cast(autonomy_limits.Meta, meta["autonomy_limits"])
                hold = cast(autonomy_limits.Meta, state["hold"])
                self.assertEqual(trigger, hold["trigger"])

    def test_preflight_breach_returns_a_persistable_hold(self) -> None:
        selected = {"schema_version": 1, "max_elapsed_seconds": 1, "digest": "sha256:" + "c" * 64}
        command = args()
        note = autonomy_limits.apply_preflight(command, self.meta, selected, NOW)
        self.assertIn("admitted", note)
        self.meta["task_revision"] = 3
        held = autonomy_limits.apply_preflight(command, self.meta, selected, LATER)
        self.assertIn("hold recorded", held)
        self.assertTrue(command.autonomy_limit_held)

    def test_tampering_and_bypass_attempts_fail_closed(self) -> None:
        selected = {"schema_version": 1, "max_commands": 2, "digest": "sha256:" + "a" * 64}
        autonomy_limits.apply_preflight(args(), self.meta, selected, NOW)
        self.meta["autonomy_limits"]["hold"] = {
            "trigger": "command",
            "observed": 2,
            "limit": 2,
            "held_at": NOW,
            "task_revision": 99,
        }
        self.assertIn("invalid", autonomy_limits.metadata_error(self.meta) or "")
        self.meta["autonomy_limits"]["hold"] = None
        self.meta["autonomy_limits"]["policy_digest"] = "sha256:" + "b" * 64
        with self.assertRaisesRegex(RuntimeError, "POLICY_MISMATCH"):
            autonomy_limits.apply_record(args(), self.meta, selected, LATER)
        with self.assertRaisesRegex(RuntimeError, "cost units"):
            autonomy_limits.apply_record(args(cost_units=-1), {"id": "AR-0001"}, selected, LATER)

    def test_policy_requires_clean_tracked_regular_file_and_detects_change(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            git("init", "-q", str(root))
            git("-C", str(root), "config", "user.email", "test@example.invalid")
            git("-C", str(root), "config", "user.name", "Test")
            path = root / autonomy_limits.POLICY_NAME
            path.write_text(json.dumps({"schema_version": 1, "max_commands": 2}) + "\n")
            git("-C", str(root), "add", path.name)
            git("-C", str(root), "commit", "-qm", "policy")
            selected = autonomy_limits.policy(root)
            if selected is None:
                self.fail("tracked autonomy limits policy was not loaded")
            self.assertEqual(2, selected["max_commands"])
            path.write_text(path.read_text() + " ")
            with self.assertRaisesRegex(autonomy_limits.PolicyError, "tracked and unchanged"):
                autonomy_limits.policy(root)

    def test_missing_policy_is_opt_in_absent_but_tracked_deletion_fails_closed(self) -> None:
        """An absent opt-in policy differs from deleting a tracked policy."""
        with TemporaryDirectory() as directory:
            root = Path(directory)
            git("init", "-q", str(root))
            git("-C", str(root), "config", "user.email", "test@example.invalid")
            git("-C", str(root), "config", "user.name", "Test")
            git("-C", str(root), "commit", "--allow-empty", "-qm", "empty")
            self.assertIsNone(autonomy_limits.policy(root))

            path = root / autonomy_limits.POLICY_NAME
            path.write_text(json.dumps({"schema_version": 1, "max_commands": 2}) + "\n")
            git("-C", str(root), "add", path.name)
            git("-C", str(root), "commit", "-qm", "policy")
            path.unlink()
            with self.assertRaisesRegex(autonomy_limits.PolicyError, "tracked and unchanged"):
                autonomy_limits.policy(root)

    def test_policy_rejects_malformed_and_unsafe_tracked_documents(self) -> None:
        """A committed policy still has to be safe and structurally actionable."""
        cases: tuple[tuple[bytes, str], ...] = (
            (b"{ ", "valid UTF-8 JSON"),
            (b"[]", "shape or version"),
            (b'{"schema_version":1}', "budgets are invalid"),
            (b'{"schema_version":2,"max_commands":1}', "shape or version"),
            (b'{"schema_version":1,"unknown":1}', "budgets are invalid"),
            (b'{"schema_version":1,"max_commands":-1}', "budgets are invalid"),
            (b'{"schema_version":1,"max_commands":true}', "budgets are invalid"),
        )
        with TemporaryDirectory() as directory:
            root = Path(directory)
            git("init", "-q", str(root))
            git("-C", str(root), "config", "user.email", "test@example.invalid")
            git("-C", str(root), "config", "user.name", "Test")
            path = root / autonomy_limits.POLICY_NAME
            for index, (payload, error) in enumerate(cases):
                with self.subTest(error=error):
                    path.write_bytes(payload)
                    git("-C", str(root), "add", path.name)
                    git("-C", str(root), "commit", "-qm", f"policy-{index}")
                    with self.assertRaisesRegex(autonomy_limits.PolicyError, error):
                        autonomy_limits.policy(root)

            path.write_text(json.dumps({"schema_version": 1, "max_commands": 1}) + "\n")
            git("-C", str(root), "add", path.name)
            git("-C", str(root), "commit", "-qm", "safe-policy")
            path.chmod(0o666)
            with self.assertRaisesRegex(autonomy_limits.PolicyError, "unsafe identity or size"):
                autonomy_limits.policy(root)

    def test_prepare_fences_policy_before_and_after_persisting_preflight(self) -> None:
        """Run preflight records a hold before effects and rejects policy drift."""
        selected = {"schema_version": 1, "max_commands": 2, "digest": "sha256:" + "a" * 64}
        current: autonomy_limits.Meta = {"task_revision": 7}
        mutations: list[tuple[str, int]] = []
        runtime = SimpleNamespace(
            ROOT=Path("/not-used"),
            locate=lambda _task: (Path("task"), current, ""),
            mutate=lambda command, kind, _evidence: mutations.append(
                (kind, command.expected_revision)
            ),
        )
        command = args(expected_revision=0)
        with (
            patch.object(autonomy_limits, "policy", return_value=selected),
            patch.object(autonomy_limits, "diff_bytes", return_value=19),
            patch.object(autonomy_limits, "require_unchanged") as unchanged,
        ):
            autonomy_limits.prepare(runtime, command, object())
        self.assertEqual([("autonomy-limits-preflight", 7)], mutations)
        self.assertEqual(19, command.autonomy_diff_bytes)
        self.assertEqual("preflight", command._autonomy_limits_phase)
        unchanged.assert_called_once_with(runtime.ROOT, selected)

        with patch.object(autonomy_limits, "policy", return_value=None):
            autonomy_limits.prepare(runtime, args(), object())
        with (
            patch.object(
                autonomy_limits, "policy", side_effect=autonomy_limits.PolicyError("changed")
            ),
            self.assertRaisesRegex(RuntimeError, "run preflight failed: changed"),
        ):
            autonomy_limits.prepare(runtime, args(), object())

        held_runtime = SimpleNamespace(
            ROOT=runtime.ROOT,
            locate=runtime.locate,
            mutate=lambda command, _kind, _evidence: setattr(command, "autonomy_limit_held", True),
        )
        with (
            patch.object(autonomy_limits, "policy", return_value=selected),
            patch.object(autonomy_limits, "diff_bytes", return_value=0),
            patch.object(autonomy_limits, "require_unchanged"),
            self.assertRaisesRegex(RuntimeError, "AUTONOMY_LIMIT_HOLD"),
        ):
            autonomy_limits.prepare(held_runtime, args(), object())

    def test_metadata_and_disposition_reject_forged_or_stale_holds(self) -> None:
        """Durable hold data cannot be forged, replayed, or disposed by another owner."""
        selected = {"schema_version": 1, "max_commands": 2, "digest": "sha256:" + "d" * 64}
        autonomy_limits.apply_preflight(args(), self.meta, selected, NOW)
        state = cast(autonomy_limits.Meta, self.meta["autonomy_limits"])
        for field, value, error in (
            ("started_at", "not-a-time", "start is invalid"),
            ("commands", -1, "counters are invalid"),
            ("dispositions", [{}] * 33, "counters are invalid"),
        ):
            with self.subTest(field=field):
                original = state[field]
                state[field] = value
                self.assertIn(error, autonomy_limits.metadata_error(self.meta) or "")
                state[field] = original
        state["dispositions"] = [{"reason": "missing durable fence"}]
        self.assertIn("disposition is invalid", autonomy_limits.metadata_error(self.meta) or "")
        state["dispositions"] = []

        self.meta["task_revision"] = 3
        autonomy_limits.apply_record(args(), self.meta, {**selected, "max_commands": 1}, LATER)
        self.meta["task_revision"] = 4
        with self.assertRaisesRegex(RuntimeError, "active task owner"):
            autonomy_limits.apply_dispose(
                args(owner="other", expected_revision=4, reason="review"), self.meta, LATER
            )
        state["hold"] = None
        with self.assertRaisesRegex(RuntimeError, "current diagnostic hold"):
            autonomy_limits.apply_dispose(
                args(expected_revision=4, reason="review"), self.meta, LATER
            )
        state["hold"] = {
            "trigger": "command",
            "observed": 1,
            "limit": 1,
            "held_at": LATER,
            "task_revision": 4,
        }
        with self.assertRaisesRegex(RuntimeError, "reason is invalid"):
            autonomy_limits.apply_dispose(
                args(expected_revision=4, reason="bad\nreason"), self.meta, LATER
            )

    def test_transition_dispatch_and_run_hold_projection_cover_both_outcomes(self) -> None:
        """Lifecycle routing keeps no-policy runs inert and exposes durable status."""
        admitted: list[str] = []

        def admit(command: argparse.Namespace, _meta: autonomy_limits.Meta) -> None:
            admitted.append(command.cmd)

        no_policy = args(cmd="update", _autonomy_limits_phase="record", autonomy_limits_policy=None)
        self.assertEqual("", autonomy_limits.transition(admit, no_policy, self.meta, NOW))
        self.assertEqual(["update"], admitted)

        selected = {"schema_version": 1, "max_commands": 1, "digest": "sha256:" + "e" * 64}
        preflight = args(
            cmd="update", _autonomy_limits_phase="preflight", autonomy_limits_policy=selected
        )
        self.assertIn("admitted", autonomy_limits.transition(admit, preflight, self.meta, NOW))
        self.meta["task_revision"] = 3
        completed = args(
            cmd="update", _autonomy_limits_phase="record", autonomy_limits_policy=selected
        )
        self.assertIn("hold", autonomy_limits.transition(admit, completed, self.meta, LATER))
        autonomy_limits.carry_run_hold(
            argparse.Namespace(_session_trigger="run"), "update", self.meta
        )
        state = cast(autonomy_limits.Meta, self.meta["autonomy_limits"])
        self.assertEqual(4, state["hold"]["task_revision"])
        projected = autonomy_limits.next_revision_projection(self.meta)
        self.assertEqual(4, projected["task_revision"])
        self.assertEqual(3, self.meta["task_revision"])

        output = io.StringIO()
        status = argparse.Namespace(
            cmd="autonomy-limits", autonomy_limits_action="status", task="AR-0001"
        )
        runtime = SimpleNamespace(locate=lambda _task: (Path("task"), self.meta, ""))
        with patch("sys.stdout", output):
            self.assertEqual(0, autonomy_limits.dispatch(runtime, status))
        self.assertEqual(state, json.loads(output.getvalue()))

        called: list[argparse.Namespace] = []
        dispose = args(cmd="autonomy-limits", autonomy_limits_action="dispose")
        runtime = SimpleNamespace(
            dispatch_lifecycle_mutation=lambda command: called.append(command)
        )
        self.assertEqual(0, autonomy_limits.dispatch(runtime, dispose))
        self.assertEqual([dispose], called)

    def test_clean_record_reentry_and_timestamp_validation(self) -> None:
        """Non-breaching work remains runnable, while malformed time and holds fail closed."""
        selected = {"schema_version": 1, "max_commands": 3, "digest": "sha256:" + "f" * 64}
        self.assertIn("admitted", autonomy_limits.apply_preflight(args(), self.meta, selected, NOW))
        self.assertEqual(
            "Autonomy limits recorded.",
            autonomy_limits.apply_record(args(), self.meta, selected, LATER),
        )
        state = cast(autonomy_limits.Meta, self.meta["autonomy_limits"])
        self.assertEqual(1, state["commands"])
        self.assertIsNone(state["hold"])
        state["hold"] = {
            "trigger": "command",
            "observed": 3,
            "limit": 3,
            "held_at": LATER,
            "task_revision": 2,
        }
        with self.assertRaisesRegex(RuntimeError, "AUTONOMY_LIMIT_HOLD"):
            autonomy_limits.apply_preflight(args(), self.meta, selected, LATER)
        for value in (None, "not-a-time", "2026-10-13T12:00:00"):
            with (
                self.subTest(value=value),
                self.assertRaisesRegex(ValueError, "timestamp is invalid"),
            ):
                autonomy_limits._timestamp(value)

    def test_formal_bypass_attempt_retains_pre_and_post_effect_counts(self) -> None:
        """Guard against reducing a held effect attempt to a vacuous stutter."""
        root = Path(__file__).resolve().parents[1]
        source = (root / "formal/handoffctl/HandoffctlAutonomyLimits.tla").read_text()
        config = (root / "formal/handoffctl/HandoffctlAutonomyLimits.cfg").read_text()
        self.assertIn('lastAction\' = "bypass"', source)
        self.assertIn("bypassPreEffects' = effects", source)
        self.assertIn("bypassEffects' = effects'", source)
        self.assertIn('lastAction = "bypass" => bypassEffects = bypassPreEffects', source)
        self.assertIn("INVARIANTS TypeOK FencedHold NoEffectBypass", config)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
