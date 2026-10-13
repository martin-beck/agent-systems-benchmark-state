# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""ASB-owned liveness coverage for the portable campaign projection."""

from __future__ import annotations

import argparse
import datetime as dt
import unittest
from pathlib import Path

from tools import campaign, retry_circuit


OBSERVED_AT = dt.datetime(2026, 10, 13, tzinfo=dt.UTC)


def task(task_id: str, **changes: object) -> tuple[Path, dict[str, object], str]:
    value: dict[str, object] = {
        "id": task_id,
        "title": "Campaign liveness coverage",
        "priority": "P1",
        "status": "in_progress",
        "task_revision": 3,
        "depends_on": [],
    }
    value.update(changes)
    return Path(f"{task_id}.md"), value, ""


def reservation(expires_at: str) -> dict[str, object]:
    return {
        "execution_id": "a" * 32,
        "owner": "worker",
        "task_revision": 3,
        "envelope_digest": "sha256:" + "b" * 64,
        "command_class": "test",
        "scope_digest": "sha256:" + "c" * 64,
        "argv_digest": "d" * 64,
        "expires_at": expires_at,
    }


class ASBCampaignLivenessCoverageTests(unittest.TestCase):
    def test_parser_requires_timezone_aware_observation(self) -> None:
        parser = argparse.ArgumentParser()
        commands = parser.add_subparsers(dest="command", required=True)
        campaign.add_command_parser(commands)
        args = parser.parse_args(["campaign", "--json", "--observed-at", "2026-10-13T01:02:03Z"])
        self.assertTrue(args.json)
        self.assertEqual(dt.datetime(2026, 10, 13, 1, 2, 3, tzinfo=dt.UTC), args.observed_at)
        with self.assertRaises(SystemExit):
            parser.parse_args(["campaign", "--observed-at", "2026-10-13T01:02:03"])

    def test_worker_and_reservation_liveness_distinguish_clear_live_and_expired(self) -> None:
        self.assertEqual({"state": "unassigned"}, campaign._worker(task("AR-9001")[1], OBSERVED_AT))
        self.assertEqual(
            {"owner": "worker", "state": "unfenced"},
            campaign._worker(task("AR-9002", owner="worker")[1], OBSERVED_AT),
        )
        active = task("AR-9003", owner="worker", claim_expires="2026-10-13T00:00:01Z")[1]
        self.assertEqual("active", campaign._worker(active, OBSERVED_AT)["state"])
        self.assertEqual("clear", campaign._reservation(task("AR-9004")[1], OBSERVED_AT)[0])
        self.assertEqual(
            "live",
            campaign._reservation(
                task("AR-9005", execution_reservation=reservation("2026-10-13T00:00:01Z"))[1],
                OBSERVED_AT,
            )[0],
        )
        self.assertEqual(
            "expired",
            campaign._reservation(
                task("AR-9006", execution_reservation=reservation("2026-10-12T23:59:59Z"))[1],
                OBSERVED_AT,
            )[0],
        )

    def test_invalid_dependency_and_execution_reservation_fail_closed(self) -> None:
        with self.assertRaisesRegex(ValueError, "depends_on"):
            campaign._dependencies(task("AR-9010", depends_on="AR-0001")[1], {})
        with self.assertRaisesRegex(ValueError, "execution reservation"):
            campaign._reservation(
                task("AR-9011", execution_reservation={"execution_id": "bad"})[1], OBSERVED_AT
            )

    def test_retry_hold_and_reservation_are_projected_as_blockers(self) -> None:
        meta = task("AR-9020")[1]
        identity = retry_circuit.normalized_identity("a" * 64, "test", ["tests"])
        for revision, recorded_at in enumerate(("one", "two", "three"), start=3):
            meta["task_revision"] = revision
            retry_circuit.record_failure(meta, identity, "EXIT", 3, recorded_at)
        blockers = campaign._blockers(meta, [], OBSERVED_AT)
        self.assertIn({"kind": "retry-circuit", "state": "held"}, blockers)
        meta["task_revision"] = 6
        meta["checkpoint_commit"] = "f" * 40
        retry_circuit.reserve(
            meta, identity, 3, "e" * 32, "2026-10-13T00:00:00Z", "2026-10-13T01:00:00Z"
        )
        blockers = campaign._blockers(meta, [], OBSERVED_AT)
        self.assertIn({"kind": "retry-claim", "state": "live"}, blockers)

    def test_terminal_acceptance_and_nonterminal_recovery_contract(self) -> None:
        done = task("AR-9030", status="done", spec_acceptance={"status": "pass"})[1]
        self.assertEqual({"status": "done", "acceptance": "pass"}, campaign._outcome(done))
        blocked = task("AR-9031", status="blocked")[1]
        self.assertEqual(
            {"kind": "resume-or-unblock"},
            campaign._recovery(
                blocked, {"state": "unassigned"}, {"stale_sessions": 0}, OBSERVED_AT
            ),
        )
