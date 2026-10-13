# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Behavior-focused coverage for the released Coordinator v0.5.1 adoption."""

from __future__ import annotations

import argparse
import copy
import datetime as dt
import json
import os
import struct
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any
from unittest.mock import MagicMock, patch

from tools import fast_receipt_socket, handoffctl, role_assignment, role_registry
from tools.guest_seed import build_user_data
from tools.role_assignment import assignment_errors, validate_assignment
from tools.role_registry import registry_errors, validate_registry

ROOT = Path(__file__).resolve().parents[1]


def fixture(name: str) -> dict[str, Any]:
    value = json.loads((ROOT / "examples" / "roles" / name).read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


class GuestSeedCoverageTests(unittest.TestCase):
    def test_portable_and_capacity_seeds_are_distinct_and_complete(self) -> None:
        portable = build_user_data("portable-smoke")
        capacity = build_user_data("full-exhaustive-capacity")
        self.assertIn("PORTABLE_SMOKE_EVIDENCE_OK", portable)
        self.assertIn('containment_mode"] == "portable"', portable)
        self.assertNotIn("guest.swap", portable)
        self.assertIn("FULL_EXHAUSTIVE_CAPACITY_EVIDENCE_OK", capacity)
        self.assertIn('containment_mode"] == "required"', capacity)
        self.assertIn("fallocate -l 8G", capacity)
        self.assertIn("TLC_CGROUP_MODE=", portable)
        self.assertIn("TLC_CGROUP_MODE=", capacity)


class RoleValidationCoverageTests(unittest.TestCase):
    def setUp(self) -> None:
        self.registry = fixture("role-registry.json")
        self.assignment = fixture("role-assignment.json")
        self.now = dt.datetime(2026, 9, 24, tzinfo=dt.UTC)

    def test_registry_rejects_malformed_nested_policy_and_capability_fields(self) -> None:
        cases: tuple[tuple[str, str, Any], ...] = (
            ("tool_policy", "tool_policy", []),
            ("worktree_policy", "worktree_policy", {}),
            ("awq_profile_refs", "awq_profile_refs", ["bad ref"]),
        )
        for label, field, value in cases:
            with self.subTest(label=label):
                registry = copy.deepcopy(self.registry)
                registry["roles"][0][field] = value
                self.assertTrue(registry_errors(registry))
        registry = copy.deepcopy(self.registry)
        registry["roles"][0]["capabilities"][0]["scope"] = "bad"
        self.assertTrue(registry_errors(registry))

    def test_assignment_rejects_malformed_evidence_and_timezone_values(self) -> None:
        cases = (
            ("assignment_id", "bad value"),
            ("owner_id", "x"),
        )
        for field, value in cases:
            with self.subTest(field=field):
                assignment = copy.deepcopy(self.assignment)
                assignment[field] = value
                self.assertTrue(assignment_errors(assignment, self.registry, now=self.now))
        assignment = copy.deepcopy(self.assignment)
        assignment["authorization_evidence"][0]["digest"] = "not-a-digest"
        self.assertTrue(assignment_errors(assignment, self.registry, now=self.now))
        assignment = copy.deepcopy(self.assignment)
        assignment["roles"][0]["expires_at"] = "2026-09-24T00:00:00"
        self.assertTrue(assignment_errors(assignment, self.registry, now=self.now))

    def test_validators_return_detached_values_and_file_free_inputs(self) -> None:
        registry = validate_registry(self.registry)
        assignment = validate_assignment(self.assignment, registry, now=self.now)
        registry["default_role"] = "changed"
        assignment["owner_id"] = "changed-owner"
        self.assertEqual("implementer", self.registry["default_role"])
        self.assertNotEqual("changed-owner", self.assignment["owner_id"])
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "registry.json"
            path.write_text(json.dumps(self.registry), encoding="utf-8")
            self.assertEqual(
                "implementer", validate_registry(json.loads(path.read_text()))["default_role"]
            )

    def test_registry_schema_and_nested_role_guards_reject_malformed_values(self) -> None:
        cases: tuple[tuple[str, Any], ...] = (
            ("not-an-object", []),
            ("roles-empty", {**self.registry, "roles": []}),
            ("roles-nonobjects", {**self.registry, "roles": ["not-a-role"]}),
            ("boolean-schema", {**self.registry, "schema_version": True}),
        )
        for label, registry in cases:
            with self.subTest(label=label):
                self.assertTrue(registry_errors(registry))
        nested_cases: tuple[tuple[str, Any], ...] = (
            ("role-schema", {"schema_version": 2}),
            ("role-title", {"title": ""}),
            ("role-capabilities-empty", {"capabilities": []}),
            ("role-capabilities-nonobjects", {"capabilities": ["bad"]}),
            ("worktree-mode", {"worktree_policy": {"mode": "bad", "path_patterns": ["src/**"]}}),
            (
                "capability-description",
                {
                    "capabilities": [
                        {
                            **self.registry["roles"][0]["capabilities"][0],
                            "description": "",
                        }
                    ]
                },
            ),
        )
        for label, changes in nested_cases:
            with self.subTest(label=label):
                registry = copy.deepcopy(self.registry)
                registry["roles"][0].update(changes)
                self.assertTrue(registry_errors(registry))

    def test_assignment_schema_evidence_and_semantic_guards_reject_invalid_data(self) -> None:
        cases: tuple[tuple[str, Any], ...] = (
            ("not-an-object", []),
            ("boolean-schema", {**self.assignment, "schema_version": True}),
            ("roles-empty", {**self.assignment, "roles": []}),
            ("role-fields", {**self.assignment, "roles": [{}]}),
            (
                "role-id",
                {
                    **self.assignment,
                    "roles": [{"role_id": "BAD", "expires_at": "2999-01-01T00:00:00Z"}],
                },
            ),
            (
                "evidence-empty",
                {**self.assignment, "authorization_evidence": []},
            ),
            (
                "evidence-fields",
                {**self.assignment, "authorization_evidence": [{}]},
            ),
            (
                "evidence-kind-ref",
                {
                    **self.assignment,
                    "authorization_evidence": [
                        {"kind": "bad", "ref": "bad ref", "digest": "sha256:" + "0" * 64}
                    ],
                },
            ),
        )
        for label, assignment in cases:
            with self.subTest(label=label):
                self.assertTrue(assignment_errors(assignment, self.registry, now=self.now))
        expired = copy.deepcopy(self.assignment)
        expired["roles"][0]["expires_at"] = "2000-01-01T00:00:00Z"
        self.assertTrue(assignment_errors(expired, self.registry, now=self.now))

    def test_role_helper_boundaries_reject_noncanonical_primitives(self) -> None:
        self.assertTrue(role_registry._exact_object([], {"field"}, "item"))
        self.assertTrue(role_registry._string(1, "item", role_registry.ROLE_ID, 3, 64))
        self.assertTrue(role_registry._string("x", "item", role_registry.ROLE_ID, 3, 64))
        self.assertTrue(
            role_registry._unique_strings([], "items", minimum=1, pattern=role_registry.ROLE_ID)
        )
        self.assertTrue(
            role_registry._unique_strings(
                ["worker", "worker"], "items", minimum=1, pattern=role_registry.ROLE_ID
            )
        )
        with self.assertRaises(role_registry.RoleRegistryError):
            role_registry.validate_registry([])
        self.assertTrue(role_assignment._assignment_role_errors([]))
        self.assertTrue(role_assignment._assignment_role_errors([{}]))
        self.assertTrue(role_assignment._evidence_errors([]))
        self.assertTrue(role_assignment._evidence_errors([{}]))

    def test_assignment_semantics_reject_naive_time_and_missing_registry_roles(self) -> None:
        self.assertTrue(
            role_assignment._semantic_errors(
                self.assignment,
                {"roles": self.registry["roles"]},
                dt.datetime.fromisoformat("2026-09-24T00:00:00"),
            )
        )
        self.assertTrue(role_assignment._semantic_errors(self.assignment, {}, self.now))
        with self.assertRaises(role_assignment.RoleAssignmentError):
            role_assignment.validate_assignment([], self.registry, now=self.now)

    def test_role_validation_clis_fail_closed_for_invalid_inputs(self) -> None:
        with (
            patch.object(sys, "argv", ["role_registry.py", "registry.json"]),
            patch.object(
                role_registry, "check_registry", side_effect=role_registry.RoleRegistryError("bad")
            ),
            self.assertRaises(SystemExit),
        ):
            role_registry.main()
        with (
            patch.object(sys, "argv", ["role_assignment.py", "assignment.json", "registry.json"]),
            patch.object(
                role_assignment,
                "check_assignment",
                side_effect=role_assignment.RoleAssignmentError("bad"),
            ),
            self.assertRaises(SystemExit),
        ):
            role_assignment.main()


class WorktreeBindingCoverageTests(unittest.TestCase):
    def setUp(self) -> None:
        self.args = argparse.Namespace(
            task="AR-0001",
            owner="worker",
            expected_revision=2,
            branch="feature/receipt",
            worktree_key="receipt-worker",
        )
        self.meta: dict[str, Any] = {
            "id": "AR-0001",
            "owner": "worker",
            "status": "in_progress",
            "claim_expires": "2999-01-01T00:00:00+00:00",
            "task_revision": 2,
            "branch": "",
            "worktree_key": "",
        }

    def test_bind_worktree_rejects_each_owner_and_identity_violation(self) -> None:
        cases: tuple[tuple[str, dict[str, Any]], ...] = (
            ("owner", {"owner": "someone-else"}),
            ("inactive", {"status": "open"}),
            ("expired", {"claim_expires": "2000-01-01T00:00:00+00:00"}),
            ("invalid-expiry", {"claim_expires": "not-a-date"}),
            ("stale", {"task_revision": 3}),
        )
        with patch.object(handoffctl, "require_role_admission"):
            for label, changes in cases:
                with (
                    self.subTest(label=label),
                    self.assertRaisesRegex(RuntimeError, "owned|active|unexpired|stale"),
                ):
                    candidate = {**self.meta, **changes}
                    handoffctl.require_active_binding_owner(self.args, candidate)

    def test_worktree_admission_rejects_invalid_and_conflicting_bindings(self) -> None:
        with (
            patch.object(handoffctl, "require_role_admission"),
            patch.object(handoffctl, "valid_binding_branch", return_value=False),
            self.assertRaisesRegex(RuntimeError, "branch is invalid"),
        ):
            handoffctl.require_bind_worktree_admission(self.args, self.meta, [])
        with (
            patch.object(handoffctl, "require_role_admission"),
            patch.object(handoffctl, "valid_binding_branch", return_value=True),
            patch.object(handoffctl, "valid_binding_worktree", return_value=False),
            self.assertRaisesRegex(RuntimeError, "worktree key is invalid"),
        ):
            handoffctl.require_bind_worktree_admission(self.args, self.meta, [])
        other = (Path("other.md"), {**self.meta, "id": "AR-0002", "branch": self.args.branch}, "")
        with (
            patch.object(handoffctl, "require_role_admission"),
            patch.object(handoffctl, "valid_binding_branch", return_value=True),
            patch.object(handoffctl, "valid_binding_worktree", return_value=True),
            self.assertRaisesRegex(RuntimeError, "identity conflicts"),
        ):
            handoffctl.require_bind_worktree_admission(self.args, self.meta, [other])

    def test_worktree_exact_replay_is_noop_but_legacy_conflict_is_rejected(self) -> None:
        exact = {**self.meta, "branch": self.args.branch, "worktree_key": self.args.worktree_key}
        with (
            patch.object(handoffctl, "require_role_admission"),
            patch.object(handoffctl, "valid_binding_branch", return_value=True),
            patch.object(handoffctl, "valid_binding_worktree", return_value=True),
        ):
            with self.assertRaises(handoffctl.IdempotentMutationError):
                handoffctl.require_bind_worktree_admission(self.args, exact, [])
            with self.assertRaisesRegex(RuntimeError, "empty legacy"):
                handoffctl.require_bind_worktree_admission(
                    self.args, {**exact, "worktree_key": "different"}, []
                )

    def test_bind_spec_admission_matrix_preserves_immutable_binding(self) -> None:
        with (
            patch.object(handoffctl, "require_role_admission"),
            patch.object(handoffctl, "task_spec_errors", return_value=[]),
        ):
            for label, changes, message in (
                ("owner", {"owner": "someone-else"}, "owned"),
                ("inactive", {"status": "open"}, "active task"),
                ("expired", {"claim_expires": "2000-01-01T00:00:00+00:00"}, "unexpired"),
                ("invalid-expiry", {"claim_expires": "bad"}, "unexpired"),
                ("stale", {"task_revision": 3}, "stale revision"),
                ("already-bound", {"spec_ref": "specs/a.json"}, "unbound"),
            ):
                with self.subTest(label=label), self.assertRaisesRegex(RuntimeError, message):
                    handoffctl.apply_bind_spec(
                        argparse.Namespace(
                            **vars(self.args), spec_ref="specs/a.json", spec_revision=1
                        ),
                        {**self.meta, **changes},
                        None,
                    )
            with (
                patch.object(handoffctl, "task_spec_errors", return_value=["bad spec"]),
                self.assertRaisesRegex(RuntimeError, "task spec is invalid"),
            ):
                handoffctl.apply_bind_spec(
                    argparse.Namespace(**vars(self.args), spec_ref="specs/a.json", spec_revision=1),
                    dict(self.meta),
                    None,
                )
            accepted = dict(self.meta)
            self.assertEqual(
                "Bound task spec specs/a.json revision 1.",
                handoffctl.apply_bind_spec(
                    argparse.Namespace(**vars(self.args), spec_ref="specs/a.json", spec_revision=1),
                    accepted,
                    None,
                ),
            )
        self.assertEqual(("specs/a.json", 1), (accepted["spec_ref"], accepted["spec_revision"]))

    def test_binding_validators_fail_closed_for_malformed_values_and_git_timeout(self) -> None:
        self.assertFalse(handoffctl.valid_binding_branch("DETACHED"))
        with patch.object(handoffctl, "run", side_effect=handoffctl.SubprocessTimeoutError("late")):
            self.assertFalse(handoffctl.valid_binding_branch("feature/receipt"))
        with patch.object(
            handoffctl,
            "config",
            return_value={"projects_root": "/work", "product_worktree": "product"},
        ):
            self.assertFalse(handoffctl.valid_binding_worktree("."))
            self.assertFalse(handoffctl.valid_binding_worktree("product"))
            self.assertFalse(handoffctl.valid_binding_worktree("not allowed"))
        with patch.object(handoffctl, "config", return_value={"product_worktree": "product"}):
            # v0.7.4 permits a relative worktree key when no projects_root is
            # configured; the coordinator still rejects traversal and product
            # aliases above.
            self.assertTrue(handoffctl.valid_binding_worktree("receipt-worker"))

    def test_accept_and_mutate_keep_failure_and_idempotency_boundaries(self) -> None:
        accepted = {**self.meta, "spec_ref": "specs/a.json", "spec_revision": 1}
        accept_args = argparse.Namespace(
            task="AR-0001",
            owner="worker",
            expected_revision=2,
            evidence_class="test",
            evidence_ref="quality/receipt",
            evidence_digest="sha256:" + "0" * 64,
            note="accepted",
        )
        with patch.object(handoffctl, "require_role_admission"):
            with self.assertRaisesRegex(RuntimeError, "active task"):
                handoffctl.apply_accept(accept_args, {**accepted, "status": "open"}, None)
            with (
                patch.object(handoffctl, "done_admission_error", return_value="evidence rejected"),
                self.assertRaisesRegex(
                    RuntimeError, "done admission denied: .*cannot read spec_ref"
                ),
            ):
                handoffctl.apply_accept(accept_args, dict(accepted), None)
        with (
            patch.object(handoffctl, "backend_selection", return_value={"backend": "sqlite"}),
            patch.object(
                handoffctl,
                "fast_receipt_id",
                return_value="receipt-1",
            ),
            self.assertRaisesRegex(RuntimeError, "Git authority"),
        ):
            handoffctl.mutate(self.args, "update")
        with (
            patch.object(handoffctl, "backend_selection", return_value={"backend": "sqlite"}),
            patch.object(handoffctl, "fast_receipt_id", return_value=None),
            patch.object(
                handoffctl,
                "mutate_sqlite",
                side_effect=handoffctl.IdempotentMutationError("already applied"),
            ),
        ):
            self.assertEqual("already applied", handoffctl.mutate(self.args, "update"))

    def test_dispatch_routes_fast_and_standard_run_commands(self) -> None:
        fast = argparse.Namespace(cmd="fast")
        run = argparse.Namespace(cmd="run", command=["--", "true"])
        with patch.object(handoffctl, "dispatch_fast_command", return_value=7) as dispatch:
            self.assertEqual(7, handoffctl.dispatch_bound_command(fast))
        dispatch.assert_called_once_with(fast)
        with patch.object(handoffctl, "cmd_run", return_value=3) as command:
            self.assertEqual(3, handoffctl.dispatch_bound_standard_command(run))
        self.assertEqual(["true"], run.command)
        command.assert_called_once_with(run)

    def test_lifecycle_dispatch_reports_an_admitted_noop_replay(self) -> None:
        args = argparse.Namespace(cmd="bind-worktree")
        with (
            patch.object(handoffctl, "mutate", return_value="already bound"),
            patch("builtins.print") as printed,
        ):
            handoffctl.dispatch_lifecycle_mutation(args)
        printed.assert_called_once_with("already bound")


class FastReceiptTransportCoverageTests(unittest.TestCase):
    def _peer(self) -> MagicMock:
        peer = MagicMock()
        peer.__enter__.return_value = peer
        return peer

    def test_observation_transport_fallbacks_preserve_direct_path(self) -> None:
        argv = ["fast", "observe", "--max-age-seconds", "30"]
        path = Path.cwd() / "fast-receipts.fixture.sock"
        for outcome in (
            TimeoutError(),
            RuntimeError("fast receipt socket message is too large"),
        ):
            with self.subTest(outcome=outcome):
                peer = self._peer()
                with (
                    patch.object(fast_receipt_socket, "_socket_path", return_value=path),
                    patch.object(fast_receipt_socket, "_safe_socket", return_value=True),
                    patch("tools.fast_receipt_socket.socket.socket", return_value=peer),
                    patch.object(fast_receipt_socket, "_read_line", side_effect=outcome),
                ):
                    self.assertIsNone(fast_receipt_socket.try_socket_fast(argv))
        peer = self._peer()
        oversized = b'{"error":"FAST_OBSERVATION_REPLY_TOO_LARGE: use direct fast observe"}'
        with (
            patch.object(fast_receipt_socket, "_socket_path", return_value=path),
            patch.object(fast_receipt_socket, "_safe_socket", return_value=True),
            patch("tools.fast_receipt_socket.socket.socket", return_value=peer),
            patch.object(
                fast_receipt_socket,
                "_read_line",
                return_value=oversized,
            ),
        ):
            self.assertIsNone(fast_receipt_socket.try_socket_fast(argv))

    def test_transport_rejects_malformed_and_explicit_error_replies(self) -> None:
        path = Path.cwd() / "fast-receipts.fixture.sock"
        peer = self._peer()
        with (
            patch.object(fast_receipt_socket, "_socket_path", return_value=path),
            patch.object(fast_receipt_socket, "_safe_socket", return_value=True),
            patch("tools.fast_receipt_socket.socket.socket", return_value=peer),
            patch.object(fast_receipt_socket, "_read_line", return_value=b"[]"),
            self.assertRaisesRegex(RuntimeError, "response is invalid"),
        ):
            fast_receipt_socket.try_socket_fast(["fast", "observe", "--max-age-seconds", "30"])
        peer = self._peer()
        with (
            patch.object(fast_receipt_socket, "_socket_path", return_value=path),
            patch.object(fast_receipt_socket, "_safe_socket", return_value=True),
            patch("tools.fast_receipt_socket.socket.socket", return_value=peer),
            patch.object(fast_receipt_socket, "_read_line", return_value=b'{"error":"denied"}'),
        ):
            self.assertEqual(
                1,
                fast_receipt_socket.try_socket_fast(["fast", "observe", "--max-age-seconds", "30"]),
            )

    def test_unrecognized_fast_shape_uses_the_direct_cli_route(self) -> None:
        self.assertIsNone(fast_receipt_socket.try_socket_fast(["fast", "unknown"]))

    def test_strict_fast_parser_exercises_rejected_option_shapes(self) -> None:
        valid_promote = [
            "fast",
            "promote",
            "AR-0001",
            "--expected-revision",
            "2",
            "--note",
            "ready",
            "--key",
            "key-1",
        ]
        request = fast_receipt_socket._fast_request(valid_promote)
        self.assertIsNotNone(request)
        assert request is not None
        self.assertEqual("promote", request["action"])
        invalid = (
            [*valid_promote[:3], "--unexpected", "x", *valid_promote[5:]],
            [*valid_promote[:3], "--expected-revision", "not-an-int", *valid_promote[5:]],
            [
                "fast",
                "update",
                "AR-0001",
                "--owner",
                "worker",
                "--expected-revision",
                "2",
                "--note",
                "ready",
                "--key",
                "key-1",
            ],
            [
                "fast",
                "update",
                "AR-0001",
                "--owner",
                "worker",
                "--expected-revision",
                "2",
                "--status",
                "open",
                "--note",
                "ready",
                "--key",
                "key-1",
                "--unknown",
                "x",
            ],
        )
        for argv in invalid:
            with self.subTest(argv=argv):
                self.assertIsNone(fast_receipt_socket._fast_request(argv))

    def test_wire_validator_rejects_typed_and_shape_violations(self) -> None:
        invalid = (
            {"protocol": 1, "action": "observe", "max_age_seconds": True},
            {
                "protocol": 1,
                "action": "claim",
                "task": "AR-0001",
                "owner": "worker",
                "expected_revision": 2,
                "lease_minutes": 30,
                "key": "key-1",
                "worker_pid": 0,
                "worker_start_time": 1,
            },
            {
                "protocol": 1,
                "action": "promote",
                "task": "AR-0001",
                "expected_revision": True,
                "note": "ready",
                "key": "key-1",
            },
            {
                "protocol": 1,
                "action": "update",
                "task": "AR-0001",
                "owner": "worker",
                "expected_revision": 2,
                "changes": {"unknown": "value"},
                "note": "ready",
                "key": "key-1",
            },
        )
        for request in invalid:
            with (
                self.subTest(request=request),
                self.assertRaisesRegex(RuntimeError, "invalid fast"),
            ):
                fast_receipt_socket._require_request(request)

    def test_socket_handler_rejects_foreign_peer_before_submission(self) -> None:
        peer = self._peer()
        peer.getsockopt.return_value = struct.pack("3i", 42, os.geteuid() + 1, 0)
        submit = MagicMock()
        fast_receipt_socket._handle(
            MagicMock(),
            peer,
            submit,
            b'{"protocol":1,"action":"receipt","receipt_id":"receipt-1"}',
        )
        submit.assert_not_called()
        peer.sendall.assert_called_once()
