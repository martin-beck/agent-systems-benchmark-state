# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Tests for the transactional role management commands."""

from __future__ import annotations

import datetime as dt
import json
import tempfile
import unittest
from argparse import Namespace
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from unittest.mock import patch

from tools import handoffctl, roles
from tools.roles import (
    RolesError,
    assign,
    check,
    list_assignments,
    remove,
    role_admission_error,
    role_admission_errors,
)

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "examples/roles/role-registry.json"
DIGEST = "sha256:" + "a" * 64


class RoleManagementTests(unittest.TestCase):
    def test_assign_list_check_and_remove_use_exact_revision(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            state = Path(directory) / "roles.json"
            created = assign(
                state,
                REGISTRY,
                expected_revision=0,
                assignment_id="assignment-worker-001",
                owner_id="worker-001",
                role_id="implementer",
                expires_at="2099-01-01T00:00:00Z",
                evidence_kind="ticket",
                evidence_ref="AR-0068",
                evidence_digest=DIGEST,
            )
            self.assertEqual(1, created["revision"])
            self.assertEqual(1, len(list_assignments(state, REGISTRY, "worker-001")["assignments"]))
            self.assertTrue(check(state, REGISTRY, "worker-001")["valid"])
            with self.assertRaisesRegex(RolesError, "stale role revision"):
                remove(state, REGISTRY, expected_revision=0, assignment_id="assignment-worker-001")
            removed = remove(
                state, REGISTRY, expected_revision=1, assignment_id="assignment-worker-001"
            )
            self.assertEqual({"revision": 2, "removed": "assignment-worker-001"}, removed)

    def test_outputs_are_byte_stable_and_invalid_state_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            state = Path(directory) / "roles.json"
            assign(
                state,
                REGISTRY,
                expected_revision=0,
                assignment_id="assignment-worker-002",
                owner_id="worker-002",
                role_id="reviewer",
                expires_at="2099-01-02T00:00:00Z",
                evidence_kind="review",
                evidence_ref="AR-0068/review",
                evidence_digest=DIGEST,
            )
            expected = json.dumps(
                list_assignments(state, REGISTRY, None), sort_keys=True, separators=(",", ":")
            )
            self.assertEqual(
                expected,
                json.dumps(
                    list_assignments(state, REGISTRY, None), sort_keys=True, separators=(",", ":")
                ),
            )
            state.write_text("{}", encoding="utf-8")
            with self.assertRaisesRegex(RolesError, "role state is malformed"):
                list_assignments(state, REGISTRY, None)
            state.write_text(
                json.dumps({"schema_version": 1, "revision": 1, "assignments": [{}]}),
                encoding="utf-8",
            )
            with self.assertRaisesRegex(RolesError, "schema:"):
                list_assignments(state, REGISTRY, None)

    def test_check_unknown_owner_fails_closed(self) -> None:
        with (
            tempfile.TemporaryDirectory() as directory,
            self.assertRaisesRegex(RolesError, "no active role assignment"),
        ):
            check(Path(directory) / "roles.json", REGISTRY, "unknown-owner")

    def test_cli_and_handoffctl_dispatch_have_stable_json_output(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            state = Path(directory) / "roles.json"
            common = ["--state", str(state), "--registry", str(REGISTRY)]
            output = StringIO()
            with redirect_stdout(output):
                self.assertEqual(
                    0,
                    roles.main(
                        [
                            *common,
                            "assign",
                            "--expected-revision",
                            "0",
                            "--assignment-id",
                            "assignment-worker-003",
                            "--owner-id",
                            "worker-003",
                            "--role-id",
                            "implementer",
                            "--expires-at",
                            "2099-01-01T00:00:00Z",
                            "--evidence-kind",
                            "ticket",
                            "--evidence-ref",
                            "AR-0068",
                            "--evidence-digest",
                            DIGEST,
                        ]
                    ),
                )
                self.assertEqual(
                    0,
                    roles.main(
                        [
                            *common,
                            "assign",
                            "--expected-revision",
                            "1",
                            "--assignment-id",
                            "assignment-worker-003-reviewer",
                            "--owner-id",
                            "worker-003",
                            "--role-id",
                            "reviewer",
                            "--expires-at",
                            "2099-01-02T00:00:00Z",
                            "--evidence-kind",
                            "ticket",
                            "--evidence-ref",
                            "AR-0068",
                            "--evidence-digest",
                            DIGEST,
                        ]
                    ),
                )
                self.assertEqual(0, roles.main([*common, "list", "--owner-id", "worker-003"]))
            lines = output.getvalue().splitlines()
            self.assertEqual(3, len(lines))
            self.assertEqual(
                lines[0], json.dumps(json.loads(lines[0]), sort_keys=True, separators=(",", ":"))
            )
            with redirect_stdout(output):
                self.assertEqual(0, roles.main([*common, "check", "--owner-id", "worker-003"]))
                self.assertEqual(
                    0,
                    roles.main(
                        [
                            *common,
                            "remove",
                            "--expected-revision",
                            "2",
                            "--assignment-id",
                            "assignment-worker-003",
                        ]
                    ),
                )
            dispatch_output = StringIO()
            with redirect_stdout(dispatch_output):
                handoffctl.dispatch_bound_command(
                    Namespace(
                        cmd="roles",
                        roles_command="check",
                        state=state,
                        registry=REGISTRY,
                        owner_id="worker-003",
                    )
                )
            self.assertEqual(
                {"owner_id": "worker-003", "revision": 3, "valid": True},
                json.loads(dispatch_output.getvalue()),
            )
            with self.assertRaises(SystemExit):
                roles.main([*common, "check", "--owner-id", "unknown-owner"])

    def test_malformed_state_and_duplicate_writes_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            state = Path(directory) / "roles.json"
            state.write_text("{", encoding="utf-8")
            with self.assertRaisesRegex(RolesError, "cannot read role state"):
                list_assignments(state, REGISTRY, None)
            state.write_text("{}", encoding="utf-8")
            with self.assertRaisesRegex(RolesError, "role state is malformed"):
                list_assignments(state, REGISTRY, None)
            with self.assertRaisesRegex(RolesError, "cannot read JSON registry"):
                list_assignments(
                    Path(directory) / "missing.json",
                    Path(directory) / "missing-registry.json",
                    None,
                )
            state.unlink()
            assign(
                state,
                REGISTRY,
                expected_revision=0,
                assignment_id="assignment-worker-004",
                owner_id="worker-004",
                role_id="implementer",
                expires_at="2099-01-01T00:00:00Z",
                evidence_kind="ticket",
                evidence_ref="AR-0068",
                evidence_digest=DIGEST,
            )
            with self.assertRaisesRegex(RolesError, "assignment already exists"):
                assign(
                    state,
                    REGISTRY,
                    expected_revision=1,
                    assignment_id="assignment-worker-004",
                    owner_id="worker-004",
                    role_id="implementer",
                    expires_at="2099-01-01T00:00:00Z",
                    evidence_kind="ticket",
                    evidence_ref="AR-0068",
                    evidence_digest=DIGEST,
                )
            with self.assertRaisesRegex(RolesError, "unknown role"):
                assign(
                    state,
                    REGISTRY,
                    expected_revision=1,
                    assignment_id="assignment-worker-004-unknown",
                    owner_id="worker-004",
                    role_id="unknown-role",
                    expires_at="2099-01-01T00:00:00Z",
                    evidence_kind="ticket",
                    evidence_ref="AR-0073",
                    evidence_digest=DIGEST,
                )
            with self.assertRaisesRegex(RolesError, "assignment not found"):
                remove(state, REGISTRY, expected_revision=1, assignment_id="missing-assignment")

    def test_role_admission_rejects_unknown_and_expired_capabilities(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            state = Path(directory) / "roles.json"
            self.assertIsNone(
                role_admission_error(
                    state,
                    REGISTRY,
                    owner_id="worker-005",
                    required_role="implementer",
                )
            )
            assign(
                state,
                REGISTRY,
                expected_revision=0,
                assignment_id="assignment-worker-005",
                owner_id="worker-005",
                role_id="implementer",
                expires_at="2099-01-01T00:00:00Z",
                evidence_kind="ticket",
                evidence_ref="AR-0073",
                evidence_digest=DIGEST,
            )
            now = dt.datetime(2026, 9, 24, tzinfo=dt.UTC)
            self.assertIsNone(
                role_admission_error(
                    state,
                    REGISTRY,
                    owner_id="worker-005",
                    required_role="implementer",
                    now=now,
                )
            )
            self.assertIn(
                "lacks role",
                role_admission_error(
                    state,
                    REGISTRY,
                    owner_id="worker-005",
                    required_role="security",
                    now=now,
                )
                or "",
            )
            self.assertIn(
                "timezone-aware",
                role_admission_error(
                    state,
                    REGISTRY,
                    owner_id="worker-005",
                    required_role="implementer",
                    now=dt.datetime.now(dt.UTC).replace(tzinfo=None),
                )
                or "",
            )
            self.assertIn(
                "no active assignment",
                role_admission_error(
                    state,
                    REGISTRY,
                    owner_id="unknown-owner",
                    required_role="implementer",
                    now=now,
                )
                or "",
            )
            self.assertEqual(
                [], role_admission_errors(state, REGISTRY, [("worker-005", "implementer")])
            )
            expired = Path(directory) / "expired.json"
            assign(
                expired,
                REGISTRY,
                expected_revision=0,
                assignment_id="assignment-worker-006",
                owner_id="worker-006",
                role_id="implementer",
                expires_at="2099-01-01T00:00:00Z",
                evidence_kind="ticket",
                evidence_ref="AR-0073",
                evidence_digest=DIGEST,
            )
            expired_value = json.loads(expired.read_text(encoding="utf-8"))
            expired_value["assignments"][0]["roles"][0]["expires_at"] = "2026-09-23T00:00:00Z"
            expired.write_text(json.dumps(expired_value), encoding="utf-8")
            self.assertIn(
                "expired role assignment",
                role_admission_error(
                    expired,
                    REGISTRY,
                    owner_id="worker-006",
                    required_role="implementer",
                    now=now,
                )
                or "",
            )

    def test_doctor_reports_role_authorization_violations(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            runtime = root / ".runtime"
            registry = root / "examples/roles/role-registry.json"
            registry.parent.mkdir(parents=True)
            registry.write_text(REGISTRY.read_text(encoding="utf-8"), encoding="utf-8")
            state = runtime / "roles.json"
            assign(
                state,
                registry,
                expected_revision=0,
                assignment_id="assignment-worker-008",
                owner_id="worker-008",
                role_id="implementer",
                expires_at="2099-01-01T00:00:00Z",
                evidence_kind="ticket",
                evidence_ref="AR-0073",
                evidence_digest=DIGEST,
            )
            task_path = root / "tasks/AR-0001.md"
            active_unknown = [(task_path, {"status": "in_progress", "owner": "unknown"}, "")]
            with (
                patch.object(handoffctl, "RUNTIME", runtime),
                patch.object(handoffctl, "ROOT", root),
                patch.object(handoffctl, "backend_selection", return_value={"backend": "git"}),
                patch.object(handoffctl, "validate", return_value=[]),
                patch.object(handoffctl, "all_tasks", return_value=active_unknown),
            ):
                self.assertEqual(1, handoffctl.cmd_doctor(live=False))

    def test_handoffctl_lifecycle_admission_uses_durable_role_store(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            runtime = root / ".runtime"
            registry = root / "examples/roles/role-registry.json"
            registry.parent.mkdir(parents=True)
            registry.write_text(REGISTRY.read_text(encoding="utf-8"), encoding="utf-8")
            state = runtime / "roles.json"
            assign(
                state,
                registry,
                expected_revision=0,
                assignment_id="assignment-worker-007",
                owner_id="worker-007",
                role_id="implementer",
                expires_at="2099-01-01T00:00:00Z",
                evidence_kind="ticket",
                evidence_ref="AR-0073",
                evidence_digest=DIGEST,
            )
            with (
                patch.object(handoffctl, "RUNTIME", runtime),
                patch.object(handoffctl, "ROOT", root),
            ):
                handoffctl.require_role_admission("worker-007")
                with self.assertRaisesRegex(RuntimeError, "role admission denied"):
                    handoffctl.require_role_admission("unknown-owner")


if __name__ == "__main__":
    unittest.main()
