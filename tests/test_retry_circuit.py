# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Contract coverage for bounded retry-circuit admission and recovery."""

from __future__ import annotations

import argparse
import contextlib
import fcntl
import json
import multiprocessing
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

import jsonschema

from tools import retry_circuit, run_command

NOW = "2026-10-13T12:00:00+00:00"
LATER = "2026-10-13T12:02:00+00:00"


def reserve_in_independent_process(state_path: str, launches_path: str, identity: str) -> None:
    """Attempt one atomic pre-launch reservation from an independent process."""
    path = Path(state_path)
    with path.open("r+", encoding="utf-8") as handle:
        fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
        meta = json.load(handle)
        try:
            retry_circuit.reserve(
                meta,
                identity,
                3,
                multiprocessing.current_process().name[-1] * 32,
                NOW,
                "2026-10-13T12:01:01+00:00",
            )
        except RuntimeError:
            return
        handle.seek(0)
        json.dump(meta, handle, sort_keys=True)
        handle.truncate()
    with Path(launches_path).open("a", encoding="utf-8") as launches:
        launches.write("launched\n")


def cleanup_and_reserve_in_independent_process(
    state_path: str, launches_path: str, identity: str
) -> None:
    """Represent a later good worker recovering capacity after worker crashes."""
    path = Path(state_path)
    with path.open("r+", encoding="utf-8") as handle:
        fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
        meta = json.load(handle)
        retry_circuit.reserve(
            meta,
            identity,
            3,
            "f" * 32,
            LATER,
            "2026-10-13T12:03:00+00:00",
        )
        handle.seek(0)
        json.dump(meta, handle, sort_keys=True)
        handle.truncate()
    with Path(launches_path).open("a", encoding="utf-8") as launches:
        launches.write("recovered-launch\n")


class FailingRunRuntime:
    ROOT = object()
    retry_circuit = retry_circuit

    def __init__(self) -> None:
        self.meta: retry_circuit.Meta = {
            "id": "AR-0001",
            "owner": "worker",
            "status": "in_progress",
            "task_revision": 2,
        }
        self.calls: list[str] = []

    def task_execution_locked(
        self, *_args: object, **_kwargs: object
    ) -> contextlib.AbstractContextManager[None]:
        return contextlib.nullcontext()

    def _cmd_run_fenced(
        self, args: argparse.Namespace
    ) -> tuple[object, str, float, bool, int, str | None, int | None]:
        identity = retry_circuit.normalized_identity("a" * 64, None, [])
        args.retry_circuit_identity = identity
        args.retry_circuit_reservation = "b" * 32
        retry_circuit.reserve(
            self.meta,
            identity,
            3,
            args.retry_circuit_reservation,
            NOW,
            "2026-10-13T12:01:01+00:00",
        )
        self.meta["task_revision"] += 1
        args.retry_circuit_resolution_revision = self.meta["task_revision"]
        return object(), "a" * 64, 1.0, False, 1, None, None

    def append_command_result(self, *_args: object) -> None:
        self.calls.append("journal")

    def locate(self, _task: str) -> tuple[None, retry_circuit.Meta, str]:
        return None, self.meta, ""

    def mutate(self, args: argparse.Namespace, kind: str, _policy: object) -> None:
        self.calls.append(kind)
        if kind == "retry-circuit-resolve":
            retry_circuit.apply_resolve(args, self.meta, "now")
        self.meta["task_revision"] += 1

    def backend_selection(self) -> dict[str, str]:
        return {"backend": "sqlite"}

    def now(self) -> str:
        return NOW

    def require_policy_unchanged(self, *_args: object) -> None:
        self.calls.append("policy")

    def reconcile(self, **_kwargs: object) -> None:
        self.calls.append("reconcile")

    class PostCommandReconcileError(RuntimeError):
        pass


class BoundRunRuntime(FailingRunRuntime):
    """Exercise the pre-existing bound execution envelope completion order."""

    def _cmd_run_fenced(
        self, _args: argparse.Namespace
    ) -> tuple[object, str, float, bool, int, str, int]:
        return object(), "a" * 64, 1.0, False, 0, "c" * 32, 2

    def mutate(self, _args: argparse.Namespace, kind: str, _policy: object) -> None:
        self.calls.append(kind)
        self.meta["task_revision"] += 1


class InterveningMutationRuntime(FailingRunRuntime):
    """Simulate an owner mutation while an unbound child is running."""

    def _cmd_run_fenced(
        self, args: argparse.Namespace
    ) -> tuple[object, str, float, bool, int, str | None, int | None]:
        result = super()._cmd_run_fenced(args)
        self.meta["task_revision"] += 1
        return result


class RetryCircuitTests(unittest.TestCase):
    def setUp(self) -> None:
        self.meta: retry_circuit.Meta = {"id": "AR-0001", "task_revision": 2}
        self.identity = retry_circuit.normalized_identity("a" * 64, "test", ["tests"])

    def _failure(self, revision: int, at: str) -> str:
        self.meta["task_revision"] = revision
        return retry_circuit.record_failure(self.meta, self.identity, "EXIT", 3, at)

    def test_normalized_identity_is_stable_and_never_retains_argv(self) -> None:
        first = retry_circuit.normalized_identity("a" * 64, "test", ["src", "tests"])
        second = retry_circuit.normalized_identity("a" * 64, "test", ["tests", "src"])
        self.assertEqual(first, second)
        with self.assertRaisesRegex(ValueError, "scope"):
            retry_circuit.normalized_identity("a" * 64, "test", ["../escape"])

    def test_bounded_unchanged_failures_open_and_hold_the_exact_identity(self) -> None:
        self.assertIn("1/3", self._failure(2, "one"))
        self.assertIn("2/3", self._failure(3, "two"))
        self.assertIn("opened", self._failure(4, "three"))
        with self.assertRaisesRegex(RuntimeError, "RETRY_CIRCUIT_OPEN"):
            retry_circuit.admit(self.meta, self.identity)
        other = retry_circuit.normalized_identity("b" * 64, "test", ["tests"])
        retry_circuit.admit(self.meta, other)

    def test_changed_durable_progress_reopens_without_erasing_auditable_hold(self) -> None:
        for revision in range(2, 5):
            self._failure(revision, str(revision))
        self.meta["checkpoint_commit"] = "c" * 40
        retry_circuit.admit(self.meta, self.identity)
        self.assertIsNotNone(self.meta["retry_circuit"]["hold"])

    def test_recovery_routes_are_explicit_and_checkpoint_requires_checkpoint(self) -> None:
        for revision in range(2, 5):
            self._failure(revision, str(revision))
        self.meta["task_revision"] = 5
        with self.assertRaisesRegex(RuntimeError, "recorded checkpoint"):
            retry_circuit.recover(self.meta, self.identity, "checkpoint", "saved", "four")
        self.assertIn(
            "changed-approach",
            retry_circuit.recover(
                self.meta, self.identity, "changed-approach", "use a new fixture", "five"
            ),
        )
        retry_circuit.admit(self.meta, self.identity)
        self.assertEqual("changed-approach", self.meta["retry_circuit"]["recoveries"][-1]["kind"])
        self.meta["task_revision"] = 6
        self.assertIn(
            "Reserved retry circuit launch slot",
            retry_circuit.reserve(
                self.meta,
                self.identity,
                3,
                "c" * 32,
                "2026-10-13T12:00:00+00:00",
                "2026-10-13T12:01:01+00:00",
            ),
        )
        self.assertEqual(3, len(self.meta["retry_circuit"]["attempts"]))

    def test_malicious_tampering_and_window_changes_fail_closed(self) -> None:
        self._failure(2, "one")
        self.meta["task_revision"] = 3
        with self.assertRaisesRegex(RuntimeError, "window changed"):
            retry_circuit.record_failure(self.meta, self.identity, "EXIT", 4, "two")
        corrupted = dict(self.meta["retry_circuit"])
        corrupted["attempts"] = []
        with self.assertRaisesRegex(ValueError, "attempts"):
            retry_circuit.validate(corrupted)

    def test_recovery_apply_fences_owner_revision_and_attempt_identity(self) -> None:
        meta: retry_circuit.Meta = {
            "id": "AR-0001",
            "owner": "worker",
            "status": "in_progress",
            "task_revision": 2,
        }
        for revision in range(2, 5):
            meta["task_revision"] = revision
            retry_circuit.record_failure(meta, self.identity, "EXIT", 3, str(revision))
        meta["task_revision"] = 5
        args = argparse.Namespace(
            owner="worker",
            expected_revision=5,
            attempt=self.identity,
            retry_circuit_action="retry-exception",
            reason="known transient test provider failure",
        )
        self.assertIn("recovered", retry_circuit.apply(args, meta, "now"))
        args.owner = "other"
        with self.assertRaisesRegex(RuntimeError, "active task owner"):
            retry_circuit.apply(args, meta, "later")

    def test_recovery_apply_rejects_an_unrelated_live_reservation(self) -> None:
        meta: retry_circuit.Meta = {
            "id": "AR-0001",
            "owner": "worker",
            "status": "in_progress",
            "task_revision": 2,
        }
        for revision in range(2, 5):
            meta["task_revision"] = revision
            retry_circuit.record_failure(meta, self.identity, "EXIT", 3, str(revision))
        meta["task_revision"] = 5
        other = retry_circuit.normalized_identity("b" * 64, "test", ["tests"])
        retry_circuit.reserve(meta, other, 3, "b" * 32, NOW, "2026-10-13T12:01:01+00:00")
        args = argparse.Namespace(
            owner="worker",
            expected_revision=5,
            attempt=self.identity,
            retry_circuit_action="retry-exception",
            reason="separate command remains live",
        )
        with self.assertRaisesRegex(RuntimeError, "live unbound retry reservation"):
            retry_circuit.apply(args, meta, NOW)

    def test_parser_requires_fenced_recovery_arguments(self) -> None:
        parser = argparse.ArgumentParser()
        commands = parser.add_subparsers(dest="command", required=True)
        retry_circuit.add_command_parser(commands)
        values = parser.parse_args(
            [
                "retry-circuit",
                "changed-approach",
                "AR-0001",
                "--owner",
                "worker",
                "--expected-revision",
                "2",
                "--attempt",
                self.identity,
                "--reason",
                "new method",
            ]
        )
        self.assertEqual("changed-approach", values.retry_circuit_action)
        with self.assertRaises(SystemExit):
            parser.parse_args(["retry-circuit", "retry-exception", "AR-0001"])

    def test_nonzero_wrapped_command_records_before_ordinary_completion_update(self) -> None:
        runtime = FailingRunRuntime()
        result = run_command.cmd_run(
            runtime,
            argparse.Namespace(
                task="AR-0001",
                owner="worker",
                command=["false"],
                command_class=None,
                scope_path=[],
                retry_window=3,
            ),
        )
        self.assertEqual(1, result)
        self.assertEqual(
            ["retry-circuit-resolve", "journal", "update", "policy", "reconcile"], runtime.calls
        )
        self.assertEqual(1, len(runtime.meta["retry_circuit"]["attempts"]))

    def test_unbound_resolution_rejects_an_intervening_revision(self) -> None:
        runtime = InterveningMutationRuntime()
        with self.assertRaisesRegex(RuntimeError, "immediately after its reservation"):
            run_command.cmd_run(
                runtime,
                argparse.Namespace(
                    task="AR-0001",
                    owner="worker",
                    command=["false"],
                    command_class=None,
                    scope_path=[],
                    retry_window=3,
                ),
            )
        self.assertEqual(4, runtime.meta["task_revision"])
        self.assertEqual(1, len(runtime.meta["retry_circuit"]["reservations"]))

    def test_bound_run_keeps_execution_envelope_result_journal_finish_sequence(self) -> None:
        runtime = BoundRunRuntime()
        result = run_command.cmd_run(
            runtime,
            argparse.Namespace(task="AR-0001", owner="worker", command=["true"]),
        )
        self.assertEqual(0, result)
        self.assertEqual(
            ["execution-result", "journal", "execution-finish", "policy", "reconcile"],
            runtime.calls,
        )
        self.assertNotIn("retry-circuit-resolve", runtime.calls)

    def test_independent_process_reservations_cap_unbound_launches_at_window(self) -> None:
        """Concurrent unbound workers may launch no more than the durable retry window."""
        with TemporaryDirectory() as directory:
            root = Path(directory)
            state_path = root / "state.json"
            launches_path = root / "launches.txt"
            state_path.write_text(
                json.dumps({"task_revision": 1, "owner": "worker", "status": "in_progress"}),
                encoding="utf-8",
            )
            identity = retry_circuit.normalized_identity("a" * 64, None, [])
            context = multiprocessing.get_context("spawn")
            workers = [
                context.Process(
                    target=reserve_in_independent_process,
                    args=(str(state_path), str(launches_path), identity),
                    name=f"reserve-worker-{index}",
                )
                for index in range(6)
            ]
            for worker in workers:
                worker.start()
            for worker in workers:
                worker.join(timeout=20)
                self.assertEqual(0, worker.exitcode)
            self.assertEqual(3, launches_path.read_text(encoding="utf-8").count("launched\n"))

            # The successful reservers intentionally exit without resolving,
            # simulating child crashes after their external launch boundary.
            cleaner = context.Process(
                target=cleanup_and_reserve_in_independent_process,
                args=(str(state_path), str(launches_path), identity),
            )
            cleaner.start()
            cleaner.join(timeout=20)
            self.assertEqual(0, cleaner.exitcode)
            self.assertIn("recovered-launch", launches_path.read_text(encoding="utf-8"))
            recovered = json.loads(state_path.read_text(encoding="utf-8"))
            self.assertEqual(3, len(recovered["retry_circuit"]["abandoned"]))

    def test_expired_crash_slots_are_durably_cleaned_before_a_new_launch(self) -> None:
        """A crashed worker cannot consume the retry window indefinitely."""
        for index in range(3):
            retry_circuit.reserve(
                self.meta,
                self.identity,
                3,
                f"{index:x}" * 32,
                NOW,
                "2026-10-13T12:00:01+00:00",
            )
        with self.assertRaisesRegex(RuntimeError, "fully reserved"):
            retry_circuit.reserve(
                self.meta,
                self.identity,
                3,
                "d" * 32,
                NOW,
                "2026-10-13T12:00:01+00:00",
            )
        self.meta["task_revision"] = 3
        message = retry_circuit.reserve(
            self.meta,
            self.identity,
            3,
            "e" * 32,
            LATER,
            "2026-10-13T12:03:00+00:00",
        )
        self.assertIn("expired_slots_cleaned=3", message)
        state = self.meta["retry_circuit"]
        self.assertEqual(1, len(state["reservations"]))
        self.assertEqual(3, len(state["abandoned"]))

    def test_expiry_records_are_validated_and_stale_resolution_is_rejected(self) -> None:
        retry_circuit.reserve(
            self.meta,
            self.identity,
            3,
            "b" * 32,
            NOW,
            "2026-10-13T12:00:01+00:00",
        )
        retry_circuit.cleanup_expired(self.meta, LATER)
        with self.assertRaisesRegex(RuntimeError, "not current"):
            retry_circuit.resolve(self.meta, self.identity, "b" * 32, "EXIT", LATER)
        retry_circuit.validate(self.meta["retry_circuit"])

    def test_schema_matches_strict_reservation_and_abandoned_state(self) -> None:
        retry_circuit.reserve(
            self.meta,
            self.identity,
            3,
            "b" * 32,
            NOW,
            "2026-10-13T12:00:01+00:00",
        )
        retry_circuit.cleanup_expired(self.meta, LATER)
        schema = json.loads(
            (Path(__file__).resolve().parents[1] / "schema/task-record.schema.json").read_text()
        )
        validator = jsonschema.Draft202012Validator(schema["properties"]["retry_circuit"])
        validator.validate(self.meta["retry_circuit"])
        invalid = dict(self.meta["retry_circuit"])
        invalid.pop("reservations")
        with self.assertRaises(jsonschema.ValidationError):
            validator.validate(invalid)
