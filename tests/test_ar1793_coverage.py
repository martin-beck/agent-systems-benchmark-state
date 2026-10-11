# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Behavior-focused coverage for the released Coordinator v0.5.1 adoption."""

from __future__ import annotations

import copy
import datetime as dt
import json
import tempfile
import unittest
from pathlib import Path
from typing import Any
from unittest.mock import MagicMock, patch

from tools import fast_receipt_socket
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
