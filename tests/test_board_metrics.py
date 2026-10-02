# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Contract tests for the deterministic company board projection."""

import json
import unittest
from argparse import Namespace
from contextlib import nullcontext
from pathlib import Path
from unittest.mock import patch

import tools.handoffctl as handoffctl
from tools.board_metrics import _decision_pending, _gate_failure, build_metrics, encode


def task(task_id: str, **fields: object) -> tuple[Path, dict[str, object], str]:
    meta: dict[str, object] = {
        "id": task_id,
        "status": "open",
        "priority": "P1",
        "role": "implementer",
        "team": "coordination",
    }
    meta.update(fields)
    return Path(f"{task_id}.md"), meta, "private body must not appear"


class BoardMetricsTests(unittest.TestCase):
    def test_projection_covers_company_metrics_and_is_byte_stable(self) -> None:
        tasks = [
            task("AR-0002", status="blocked", role="reviewer"),
            task(
                "AR-0001",
                oracle_gate={
                    "required": True,
                    "stage_sequence": ["role", "spec", "decision"],
                    "open_stage": "decision",
                    "completed": ["role", "spec"],
                    "authorized": False,
                    "reconciliation_required": False,
                },
                spec_acceptance={"status": "pass", "evidence_ref": "AR-0001/tests"},
            ),
        ]
        result = build_metrics(list(reversed(tasks)))
        self.assertEqual(["AR-0001"], result["decision_backlog"]["tasks"])
        self.assertEqual(1, result["gate_failures"]["count"])
        self.assertEqual(["AR-0002"], [item["task"] for item in result["blocked_tasks"]["items"]])
        self.assertEqual(
            {"covered": 1, "total": 2, "tasks": ["AR-0001"]}, result["evidence_coverage"]
        )
        self.assertEqual(encode(result), encode(build_metrics(tasks)))
        self.assertNotIn("private body", encode(result))
        self.assertEqual(result, json.loads(encode(result)))

    def test_unrequired_or_fully_authorized_gate_is_not_a_failure(self) -> None:
        tasks = [
            task("AR-0001"),
            task(
                "AR-0002",
                oracle_gate={
                    "required": True,
                    "stage_sequence": ["role", "spec", "decision"],
                    "open_stage": None,
                    "completed": ["role", "spec", "decision"],
                    "authorized": True,
                    "reconciliation_required": False,
                },
            ),
        ]
        result = build_metrics(tasks)
        self.assertEqual(0, result["decision_backlog"]["count"])
        self.assertEqual(0, result["gate_failures"]["count"])

    def test_gate_failure_classification_is_fail_closed(self) -> None:
        self.assertEqual(
            "reconciliation",
            _gate_failure(
                {
                    "oracle_gate": {
                        "required": True,
                        "open_stage": None,
                        "reconciliation_required": True,
                    }
                }
            ),
        )
        self.assertEqual(
            "intake",
            _gate_failure(
                {
                    "oracle_gate": {
                        "required": True,
                        "open_stage": None,
                        "authorized": False,
                        "completed": [],
                    }
                }
            ),
        )
        self.assertEqual(
            "authorization",
            _gate_failure(
                {
                    "oracle_gate": {
                        "required": True,
                        "open_stage": None,
                        "authorized": False,
                        "completed": [
                            "intake",
                            "discussion",
                            "formal_spec_review",
                            "reconciliation",
                        ],
                    }
                }
            ),
        )
        self.assertFalse(
            _decision_pending(
                {
                    "oracle_gate": {
                        "required": True,
                        "stage_sequence": ["role", "spec"],
                        "completed": ["role"],
                    }
                }
            )
        )

    def test_cli_projections_are_sqlite_only_and_read_only(self) -> None:
        with (
            patch.object(handoffctl, "backend_selection", return_value={"backend": "sqlite"}),
            patch.object(handoffctl, "all_tasks", return_value=[]),
            patch.object(handoffctl, "locked", return_value=nullcontext()),
            patch.object(handoffctl, "encode_metrics", return_value='{"ok":true}\n') as encode,
            patch("sys.stdout") as stdout,
        ):
            handoffctl.cmd_board()
            handoffctl.cmd_metrics()
            handoffctl.dispatch_read_only_command(Namespace(cmd="board"))
            handoffctl.dispatch_read_only_command(Namespace(cmd="metrics"))
        self.assertEqual(4, encode.call_count)
        self.assertEqual(8, stdout.write.call_count)
        with (
            patch.object(handoffctl, "backend_selection", return_value={"backend": "git"}),
            self.assertRaisesRegex(RuntimeError, "requires the SQLite authority"),
        ):
            handoffctl.cmd_board()


if __name__ == "__main__":
    unittest.main()
