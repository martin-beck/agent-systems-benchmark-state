# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Failure-matrix tests for the board directive command."""

import argparse
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools import handoffctl as core
from tools.directive_records import append_directive, build_directive, latest_directives


class DirectiveCommandTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.old_root = core.ROOT
        self.old_backend = core.BACKEND_CONFIG
        core.ROOT = self.root
        core.BACKEND_CONFIG = self.root / "coordinator.backend.json"
        core.BACKEND_CONFIG.write_text('{"backend":"git","project_id":"x","schema_version":1}')

    def tearDown(self) -> None:
        core.ROOT = self.old_root
        core.BACKEND_CONFIG = self.old_backend
        self.temporary.cleanup()

    def create_args(self) -> argparse.Namespace:
        return argparse.Namespace(
            directive_action="create",
            directive_id="UD-0001",
            authority="BOARD-001",
            precedence=10,
            role_scope=["implementer"],
            task_scope=[],
            statement="Preserve the verified release boundary.",
            owner="board-chair",
            lease_minutes=120,
            guidance_ref="",
        )

    def test_create_and_list_are_durable(self) -> None:
        with (
            patch.object(core, "sync_replica_before_write"),
            patch.object(core, "commit", return_value=True),
            patch.object(core, "push_replica"),
        ):
            core.cmd_directive(self.create_args())
        records = latest_directives(self.root)
        self.assertEqual("proposed", records[0]["lifecycle"])
        output = argparse.Namespace(directive_action="list", lifecycle=None)
        with patch.object(core, "sync_replica_before_write"), patch("builtins.print") as printed:
            core.cmd_directive(output)
        self.assertEqual(
            json.dumps(records, sort_keys=True, separators=(",", ":")), printed.call_args.args[0]
        )

    def test_conflicting_activation_requires_guidance_and_escalates(self) -> None:
        active = build_directive(
            "UD-0001",
            authority="BOARD-001",
            precedence=10,
            scope={"roles": ["implementer"], "tasks": []},
            statement="Keep the release frozen.",
            recorded_at="2026-09-24T00:00:00+00:00",
            owner="board-chair",
            claim_expires="2099-09-24T00:00:00+00:00",
            lifecycle="active",
        )
        proposed = build_directive(
            "UD-0002",
            authority="BOARD-001",
            precedence=10,
            scope={"roles": ["implementer"], "tasks": []},
            statement="Continue the release.",
            recorded_at="2026-09-24T00:00:00+00:00",
            owner="board-chair",
            claim_expires="2099-09-24T00:00:00+00:00",
        )
        append_directive(self.root, active)
        append_directive(self.root, proposed)
        transition = argparse.Namespace(
            directive_action="transition",
            directive_id="UD-0002",
            action="activate",
            owner="board-chair",
            expected_revision=1,
            guidance_ref="",
        )
        with (
            patch.object(core, "sync_replica_before_write"),
            self.assertRaisesRegex(RuntimeError, "AR-0053"),
        ):
            core.cmd_directive(transition)
        transition.guidance_ref = "AR-0053"
        with (
            patch.object(core, "sync_replica_before_write"),
            patch.object(core, "commit", return_value=True),
            patch.object(core, "push_replica"),
        ):
            core.cmd_directive(transition)
        self.assertEqual("escalated", latest_directives(self.root)[1]["lifecycle"])

    def test_stale_revision_and_expired_lease_fail_closed(self) -> None:
        record = build_directive(
            "UD-0001",
            authority="BOARD-001",
            precedence=10,
            scope={"roles": [], "tasks": ["AR-0001"]},
            statement="Keep task bounded.",
            recorded_at="2026-09-24T00:00:00+00:00",
            owner="board-chair",
            claim_expires="2020-09-24T00:00:00+00:00",
        )
        append_directive(self.root, record)
        args = argparse.Namespace(
            directive_action="transition",
            directive_id="UD-0001",
            action="revoke",
            owner="board-chair",
            expected_revision=2,
            guidance_ref="",
        )
        with (
            patch.object(core, "sync_replica_before_write"),
            self.assertRaisesRegex(RuntimeError, "stale directive"),
        ):
            core.cmd_directive(args)
        args.expected_revision = 1
        with (
            patch.object(core, "sync_replica_before_write"),
            self.assertRaisesRegex(RuntimeError, "expired"),
        ):
            core.cmd_directive(args)

    def test_command_rejects_unsupported_backend_duplicate_and_invalid_lease(self) -> None:
        with (
            patch.object(core, "backend_selection", return_value={"backend": "sqlite"}),
            self.assertRaisesRegex(RuntimeError, "Git authority"),
        ):
            core.cmd_directive(self.create_args())
        with self.assertRaisesRegex(RuntimeError, "positive"):
            core._directive_claim_expiry(0)
        with (
            patch.object(core, "sync_replica_before_write"),
            patch.object(core, "commit", return_value=True),
            patch.object(core, "push_replica"),
        ):
            core.cmd_directive(self.create_args())
        with (
            patch.object(core, "sync_replica_before_write"),
            self.assertRaisesRegex(RuntimeError, "already exists"),
        ):
            core.cmd_directive(self.create_args())

    def test_transition_actions_and_claim_failures_are_fenced(self) -> None:
        record = build_directive(
            "UD-0001",
            authority="BOARD-001",
            precedence=10,
            scope={"roles": ["implementer"], "tasks": []},
            statement="Keep task bounded.",
            recorded_at="2026-09-24T00:00:00+00:00",
            owner="board-chair",
            claim_expires="2099-09-24T00:00:00+00:00",
        )
        base = argparse.Namespace(
            directive_id="UD-0001", owner="wrong-owner", expected_revision=1, guidance_ref=""
        )
        with self.assertRaisesRegex(RuntimeError, "owned by"):
            core._transition_directive(base, [record])
        base.owner = "board-chair"
        base.action = "activate"
        active_candidate = core._transition_directive(base, [record])
        self.assertEqual("active", active_candidate["lifecycle"])
        for action in ("supersede", "revoke"):
            base.action = action
            candidate = core._transition_directive(base, [record])
            self.assertEqual(
                {"supersede": "superseded", "revoke": "revoked"}[action],
                candidate["lifecycle"],
            )
        base.action = "escalate"
        with self.assertRaisesRegex(RuntimeError, "guidance"):
            core._transition_directive(base, [record])
        base.action = "unknown"
        with self.assertRaisesRegex(RuntimeError, "unknown directive"):
            core._transition_directive(base, [record])
        with (
            patch.object(core, "sync_replica_before_write"),
            self.assertRaisesRegex(RuntimeError, "unknown directive"),
        ):
            core.cmd_directive(
                argparse.Namespace(
                    directive_action="transition",
                    directive_id="UD-4040",
                    action="revoke",
                    owner="board-chair",
                    expected_revision=1,
                    guidance_ref="",
                )
            )

    def test_claim_parser_and_commit_failure_are_fail_closed(self) -> None:
        record = build_directive(
            "UD-0001",
            authority="BOARD-001",
            precedence=10,
            scope={"roles": ["implementer"], "tasks": []},
            statement="Keep task bounded.",
            recorded_at="2026-09-24T00:00:00+00:00",
            owner="board-chair",
            claim_expires="not-a-date",
        )
        with self.assertRaisesRegex(RuntimeError, "expiry is invalid"):
            core._directive_claim_is_live(record, "board-chair")
        record["claim_expires"] = "2026-09-24T00:00:00"
        with self.assertRaisesRegex(RuntimeError, "expired"):
            core._directive_claim_is_live(record, "board-chair")
        with (
            patch.object(core, "append_directive"),
            patch.object(core, "commit", return_value=False),
            self.assertRaisesRegex(RuntimeError, "not committed"),
        ):
            core._commit_directive(record)


if __name__ == "__main__":
    unittest.main()
