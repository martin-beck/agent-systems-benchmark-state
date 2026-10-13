# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""ASB-owned edge contracts for the vendored campaign runtime."""

from __future__ import annotations

import argparse
import io
import json
import unittest
from pathlib import Path
from unittest.mock import patch

from tools import campaign, campaign_runtime, handoffctl, resume_card_runtime
from tools.session_records import build_session_record, validate_session_record

OBSERVED_AT = campaign.parse_observed_at("2026-10-13T00:00:00Z")


class CampaignRuntimeEdgeTests(unittest.TestCase):
    @staticmethod
    def coordinator() -> type[object]:
        metadata = {
            "id": "AR-0001",
            "title": "campaign edge contract",
            "summary": "An ASB-owned runtime edge case.",
            "priority": "P1",
            "status": "in_progress",
            "task_revision": 3,
            "owner": "worker-one",
            "claim_expires": "2026-10-13T01:00:00+00:00",
            "depends_on": [],
            "next_action": "Continue the bounded implementation.",
            "updated_at": "2026-10-13T00:00:00+00:00",
        }
        task = (Path("AR-0001.md"), metadata, "authority body")
        record = build_session_record(
            {
                "id": "AR-0001",
                "task_revision": 3,
                "status": "in_progress",
                "next_action": "Continue the bounded implementation.",
            },
            "update",
            "2026-10-13T00:00:00+00:00",
        )

        class Backend:
            def load_session_records(self) -> list[dict[str, object]]:
                return [record]

        class Coordinator:
            ROOT = Path("/state")
            LOCK_TIMEOUT_SECONDS = 1.0
            LOCK_POLL_SECONDS = 0.01
            LockTimeoutError = RuntimeError
            evidence_policy = staticmethod(lambda _root: handoffctl.DEFAULT_EVIDENCE_POLICY)
            all_tasks = staticmethod(lambda: [task])
            storage_backend = staticmethod(Backend)
            basic_task_errors = staticmethod(lambda *_: [])
            validate_session_record = staticmethod(validate_session_record)
            private_text_errors = staticmethod(handoffctl.private_text_errors)
            graph_errors = staticmethod(handoffctl.graph_errors)
            hierarchy_errors = staticmethod(handoffctl.hierarchy_errors)
            supersession_errors = staticmethod(handoffctl.supersession_errors)
            coordinator_lock_path = staticmethod(lambda: Path("/state/.runtime/state.lock"))

        return Coordinator

    def test_missing_observation_uses_current_time(self) -> None:
        stream = io.StringIO()
        with (
            patch.object(
                resume_card_runtime,
                "read_only_snapshot",
                side_effect=lambda callback, *_: callback(),
            ),
            patch.object(campaign, "current_observed_at", return_value=OBSERVED_AT),
            patch("sys.stdout", stream),
        ):
            self.assertEqual(
                0,
                campaign_runtime.dispatch(
                    argparse.Namespace(json=True, observed_at=None), self.coordinator()
                ),
            )
        self.assertEqual(OBSERVED_AT.isoformat(), json.loads(stream.getvalue())["observed_at"])

    def test_snapshot_rejects_invalid_projection_before_rendering(self) -> None:
        with (
            patch.object(
                resume_card_runtime,
                "read_only_snapshot",
                side_effect=lambda callback, *_: callback(),
            ),
            patch.object(campaign, "projection_errors", return_value=["unsafe projection"]),
            self.assertRaisesRegex(RuntimeError, "campaign snapshot validation failed"),
        ):
            campaign_runtime.dispatch(
                argparse.Namespace(json=True, observed_at=OBSERVED_AT), self.coordinator()
            )
