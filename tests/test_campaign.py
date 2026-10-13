# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Contract tests for portable, read-only campaign projections."""

from __future__ import annotations

import argparse
import io
import json
import unittest
from pathlib import Path
from unittest.mock import patch

import jsonschema

from tools import campaign, campaign_runtime, handoffctl, issue_series_service, resume_card_runtime
from tools.session_records import build_session_record, validate_session_record

OBSERVED_AT = campaign.parse_observed_at("2026-10-13T00:00:00Z")


def task(task_id: str, **changes: object) -> tuple[Path, dict[str, object], str]:
    meta: dict[str, object] = {
        "id": task_id,
        "title": f"{task_id} concise title",
        "summary": "A durable campaign task.",
        "priority": "P1",
        "status": "in_progress",
        "task_revision": 3,
        "owner": "worker-one",
        "claim_expires": "2026-10-13T01:00:00+00:00",
        "depends_on": [],
        "next_action": "Continue the bounded implementation.",
        "updated_at": "2026-10-13T00:00:00+00:00",
    }
    meta.update(changes)
    return Path(f"{task_id}.md"), meta, "authority body"


def session(task_id: str, revision: int, status: str = "in_progress") -> dict[str, object]:
    return build_session_record(
        {
            "id": task_id,
            "task_revision": revision,
            "status": status,
            "next_action": "Continue the bounded implementation.",
        },
        "update",
        "2026-10-13T00:00:00+00:00",
    )


class CampaignTests(unittest.TestCase):
    def test_projection_links_tasks_workers_dependencies_attempts_and_outcomes(self) -> None:
        predecessor = task("AR-0001", status="done", task_revision=4, owner="", claim_expires="")
        active = task("AR-0002", depends_on=["AR-0001"])
        projection = campaign.build([active, predecessor], [session("AR-0002", 2)], OBSERVED_AT)
        self.assertEqual(["AR-0001", "AR-0002"], [card["id"] for card in projection["tasks"]])
        done, working = projection["tasks"]
        self.assertEqual({"status": "done", "acceptance": "absent"}, done["outcome"])
        self.assertEqual(
            {
                "owner": "worker-one",
                "claim_expires": "2026-10-13T01:00:00+00:00",
                "state": "active",
            },
            working["worker"],
        )
        self.assertEqual([{"task": "AR-0001", "status": "done"}], working["dependencies"])
        self.assertEqual("stale", working["attempts"][0]["state"])
        self.assertEqual("record-current-session", working["recovery"]["kind"])
        self.assertEqual([], working["blockers"])

    def test_expired_execution_and_claim_observations_have_portable_recovery_views(self) -> None:
        expired_execution = task(
            "AR-0001",
            execution_reservation={
                "execution_id": "a" * 32,
                "owner": "worker-one",
                "task_revision": 3,
                "envelope_digest": "sha256:" + "b" * 64,
                "command_class": "test",
                "scope_digest": "sha256:" + "c" * 64,
                "argv_digest": "d" * 64,
                "expires_at": "2026-10-12T23:59:59+00:00",
            },
        )
        expired_claim = task("AR-0002", claim_expires="2026-10-12T23:59:59+00:00")
        cards = campaign.build([expired_execution, expired_claim], [], OBSERVED_AT)["tasks"]
        self.assertEqual("recover-execution-claim", cards[0]["recovery"]["kind"])
        self.assertIn({"kind": "execution-claim", "state": "expired"}, cards[0]["blockers"])
        self.assertEqual("expired", cards[1]["worker"]["state"])
        self.assertEqual("recover-expired-claim", cards[1]["recovery"]["kind"])

    def test_text_is_complete_equivalent_to_json(self) -> None:
        rendered = campaign.command([task("AR-0001")], [session("AR-0001", 3)], False, OBSERVED_AT)
        values = dict(line.split("=", 1) for line in rendered.splitlines()[1:])
        as_json = json.loads(
            campaign.command([task("AR-0001")], [session("AR-0001", 3)], True, OBSERVED_AT)
        )
        self.assertEqual(as_json["schema_version"], json.loads(values["SCHEMA_VERSION"]))
        self.assertEqual(as_json["observed_at"], json.loads(values["OBSERVED_AT"]))
        self.assertEqual(as_json["tasks"], json.loads(values["TASKS"]))
        self.assertEqual(as_json["summary"], json.loads(values["SUMMARY"]))

    def test_projection_rejects_private_and_stale_forward_session_data(self) -> None:
        private_session = session("AR-0001", 2)
        private_session["next_action"] = "to" + "ken" + "=do-not-project"
        errors = campaign.projection_errors(
            [task("AR-0001")],
            [private_session],
            basic_task_errors=lambda *_: [],
            validate_session_record=validate_session_record,
            private_text_errors=handoffctl.private_text_errors,
            graph_errors=handoffctl.graph_errors,
            hierarchy_errors=handoffctl.hierarchy_errors,
            supersession_errors=handoffctl.supersession_errors,
            policy=None,
        )
        self.assertTrue(any("possible credential" in error for error in errors))
        errors = campaign.projection_errors(
            [task("AR-0001")],
            [session("AR-0001", 4)],
            basic_task_errors=lambda *_: [],
            validate_session_record=validate_session_record,
            private_text_errors=handoffctl.private_text_errors,
            graph_errors=handoffctl.graph_errors,
            hierarchy_errors=handoffctl.hierarchy_errors,
            supersession_errors=handoffctl.supersession_errors,
            policy=None,
        )
        self.assertIn("session observation is ahead of AR-0001 authority", errors)
        errors = campaign.projection_errors(
            [task("AR-0001")],
            [session("AR-0001", 3, "blocked")],
            basic_task_errors=lambda *_: [],
            validate_session_record=validate_session_record,
            private_text_errors=handoffctl.private_text_errors,
            graph_errors=handoffctl.graph_errors,
            hierarchy_errors=handoffctl.hierarchy_errors,
            supersession_errors=handoffctl.supersession_errors,
            policy=None,
        )
        self.assertIn("session observation status differs from AR-0001 authority", errors)

    def test_cancelled_task_has_terminal_outcome_without_recovery_advice(self) -> None:
        cancelled = task(
            "AR-0001",
            status="cancelled",
            claim_expires="2026-10-12T23:59:59+00:00",
        )
        card = campaign.build([cancelled], [session("AR-0001", 2)], OBSERVED_AT)["tasks"][0]
        self.assertEqual({"status": "cancelled", "acceptance": "absent"}, card["outcome"])
        self.assertEqual({"kind": "none"}, card["recovery"])

    def test_projection_rejects_global_graph_hierarchy_and_supersession_errors(self) -> None:
        first = task("AR-0001", depends_on=["AR-0002"])
        second = task("AR-0002", depends_on=["AR-0001"])
        errors = campaign.projection_errors(
            [first, second],
            [],
            basic_task_errors=handoffctl.basic_task_errors,
            validate_session_record=validate_session_record,
            private_text_errors=handoffctl.private_text_errors,
            graph_errors=handoffctl.graph_errors,
            hierarchy_errors=handoffctl.hierarchy_errors,
            supersession_errors=handoffctl.supersession_errors,
            policy=None,
        )
        self.assertTrue(any("dependency cycle" in error for error in errors))
        missing = task("AR-0003", depends_on=["AR-9999"])
        errors = campaign.projection_errors(
            [missing],
            [],
            basic_task_errors=handoffctl.basic_task_errors,
            validate_session_record=validate_session_record,
            private_text_errors=handoffctl.private_text_errors,
            graph_errors=handoffctl.graph_errors,
            hierarchy_errors=handoffctl.hierarchy_errors,
            supersession_errors=handoffctl.supersession_errors,
            policy=None,
        )
        self.assertTrue(any("missing dependency" in error for error in errors))

    def test_schema_validates_rendered_json_and_rejects_incomplete_card(self) -> None:
        schema = json.loads(
            Path("schema/campaign-projection.schema.json").read_text(encoding="utf-8")
        )
        validator = jsonschema.Draft202012Validator(
            schema, format_checker=jsonschema.FormatChecker()
        )
        rendered = json.loads(
            campaign.command([task("AR-0001")], [session("AR-0001", 3)], True, OBSERVED_AT)
        )
        validator.validate(rendered)
        with self.assertRaises(jsonschema.ValidationError):
            validator.validate(
                {
                    "schema_version": 1,
                    "observed_at": "2026-10-13T00:00:00+00:00",
                    "tasks": [{}],
                    "summary": {"tasks": 1, "sessions": 0, "by_status": {}, "recovery_required": 0},
                }
            )

    def test_schema_rejects_terminal_contract_and_invalid_timestamp(self) -> None:
        schema = json.loads(
            Path("schema/campaign-projection.schema.json").read_text(encoding="utf-8")
        )
        validator = jsonschema.Draft202012Validator(
            schema, format_checker=jsonschema.FormatChecker()
        )
        projection = campaign.build([task("AR-0001", status="cancelled")], [], OBSERVED_AT)
        card = projection["tasks"][0]
        invalid: list[tuple[str, object]] = [
            ("terminal recovery", {**card, "recovery": {"kind": "recover-expired-claim"}}),
            ("null terminal outcome", {**card, "status": "done", "outcome": None}),
        ]
        for name, value in invalid:
            with self.subTest(name=name), self.assertRaises(jsonschema.ValidationError):
                validator.validate({**projection, "tasks": [value]})
        with self.assertRaises(jsonschema.ValidationError):
            validator.validate({**projection, "observed_at": "2026-13-99T25:61:61+00:00"})

    def test_runtime_contract_rejects_terminal_advice_and_invalid_timestamp(self) -> None:
        projection = campaign.build([task("AR-0001", status="done")], [], OBSERVED_AT)
        card = projection["tasks"][0]
        card["recovery"] = {"kind": "resume-or-unblock"}
        projection["observed_at"] = "2026-10-13T00:00:00"
        errors = campaign.projection_contract_errors(projection)
        self.assertTrue(any("terminal task has recovery advice" in error for error in errors))
        self.assertTrue(any("observed_at is not a timestamp" in error for error in errors))

    def test_runtime_contract_rejects_malformed_cards_outcomes_and_embedded_times(self) -> None:
        errors = campaign.projection_contract_errors(
            {
                "observed_at": "2026-02-30T00:00:00+00:00",
                "tasks": [
                    None,
                    {
                        "id": "AR-0001",
                        "status": "done",
                        "outcome": None,
                        "recovery": {"kind": "none"},
                        "worker": {"claim_expires": "2026-13-99T00:00:00+00:00"},
                        "attempts": [{"recorded_at": "2026-10-13T00:00:00"}],
                    },
                    {
                        "id": "AR-0002",
                        "status": "in_progress",
                        "outcome": {"status": "done"},
                        "recovery": {"kind": "none"},
                    },
                ],
            }
        )
        self.assertTrue(any("observed_at is not a timestamp" in error for error in errors))
        self.assertIn("campaign card is invalid", errors)
        self.assertIn("AR-0001: terminal outcome does not match status", errors)
        self.assertTrue(
            any("AR-0001 worker claim_expires is not a timestamp" in error for error in errors)
        )
        self.assertTrue(
            any("AR-0001 attempt recorded_at is not a timestamp" in error for error in errors)
        )
        self.assertIn("AR-0002: nonterminal task has outcome", errors)

    def test_campaign_helpers_preserve_unfenced_and_invalid_authority_boundaries(self) -> None:
        unfenced = task("AR-0001", claim_expires="")[1]
        self.assertEqual(
            {"owner": "worker-one", "state": "unfenced"}, campaign._worker(unfenced, OBSERVED_AT)
        )
        with self.assertRaisesRegex(ValueError, "depends_on is invalid"):
            campaign._dependencies(task("AR-0001", depends_on="AR-0002")[1], {})
        with self.assertRaisesRegex(ValueError, "execution reservation is invalid"):
            campaign._reservation(task("AR-0001", execution_reservation={})[1], OBSERVED_AT)

    def test_command_rejects_an_invalid_projection_before_rendering(self) -> None:
        malformed = {
            "observed_at": "2026-10-13T00:00:00+00:00",
            "tasks": [
                {"id": "AR-0001", "status": "done", "outcome": None, "recovery": {"kind": "none"}}
            ],
        }
        with (
            patch.object(campaign, "build", return_value=malformed),
            self.assertRaisesRegex(ValueError, "campaign projection contract failed"),
        ):
            campaign.command([], [], True, OBSERVED_AT)

    def test_runtime_is_read_only_and_uses_one_authoritative_snapshot(self) -> None:
        loaded = [session("AR-0001", 3)]

        class Backend:
            def load_session_records(self) -> list[dict[str, object]]:
                return loaded

        class Coordinator:
            ROOT = Path("/state")
            LOCK_TIMEOUT_SECONDS = 1.0
            LOCK_POLL_SECONDS = 0.01
            LockTimeoutError = RuntimeError
            evidence_policy = staticmethod(lambda _root: handoffctl.DEFAULT_EVIDENCE_POLICY)
            all_tasks = staticmethod(lambda: [task("AR-0001")])
            storage_backend = staticmethod(Backend)
            basic_task_errors = staticmethod(lambda *_: [])
            validate_session_record = staticmethod(validate_session_record)
            private_text_errors = staticmethod(handoffctl.private_text_errors)
            graph_errors = staticmethod(handoffctl.graph_errors)
            hierarchy_errors = staticmethod(handoffctl.hierarchy_errors)
            supersession_errors = staticmethod(handoffctl.supersession_errors)
            coordinator_lock_path = staticmethod(lambda: Path("/state/.runtime/state.lock"))

        stream = io.StringIO()
        with (
            patch.object(
                resume_card_runtime,
                "read_only_snapshot",
                side_effect=lambda callback, *_: callback(),
            ),
            patch("sys.stdout", stream),
        ):
            self.assertEqual(
                0,
                campaign_runtime.dispatch(
                    argparse.Namespace(json=True, observed_at=OBSERVED_AT), Coordinator
                ),
            )
        self.assertEqual("AR-0001", json.loads(stream.getvalue())["tasks"][0]["id"])

        fallback_stream = io.StringIO()
        with (
            patch.object(
                resume_card_runtime,
                "read_only_snapshot",
                side_effect=lambda callback, *_: callback(),
            ),
            patch.object(campaign, "current_observed_at", return_value=OBSERVED_AT),
            patch("sys.stdout", fallback_stream),
        ):
            self.assertEqual(
                0,
                campaign_runtime.dispatch(argparse.Namespace(json=True, observed_at=None), Coordinator),
            )
        self.assertEqual(
            OBSERVED_AT.isoformat(),
            json.loads(fallback_stream.getvalue())["observed_at"],
        )

        with (
            patch.object(
                resume_card_runtime,
                "read_only_snapshot",
                side_effect=lambda callback, *_: callback(),
            ),
            patch.object(campaign, "projection_errors", return_value=["unsafe projection"]),
            self.assertRaisesRegex(RuntimeError, "campaign snapshot validation failed"),
        ):
            campaign_runtime.dispatch(argparse.Namespace(json=True, observed_at=OBSERVED_AT), Coordinator)

    def test_parser_rejects_naive_campaign_observation_time(self) -> None:
        parser = argparse.ArgumentParser()
        commands = parser.add_subparsers(dest="cmd", required=True)
        campaign.add_command_parser(commands)
        with self.assertRaises(SystemExit):
            parser.parse_args(["campaign", "--observed-at", "2026-10-13T00:00:00"])

    def test_handoffctl_registers_campaign_as_a_read_only_command(self) -> None:
        with (
            patch("sys.argv", ["handoffctl", "campaign", "--json"]),
            patch.object(handoffctl, "assert_project_binding"),
            patch.object(issue_series_service, "dispatch_cli", return_value=False),
            patch.object(handoffctl, "dispatch_bound_command", return_value=0) as dispatch,
        ):
            self.assertEqual(0, handoffctl.main())
        self.assertEqual("campaign", dispatch.call_args.args[0].cmd)


if __name__ == "__main__":
    unittest.main()
