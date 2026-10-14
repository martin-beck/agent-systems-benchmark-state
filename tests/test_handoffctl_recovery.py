# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Focused regression coverage for expired-claim process identity."""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path
from unittest.mock import patch

SOURCE = Path(__file__).with_name("test_handoffctl.py")
SPEC = importlib.util.spec_from_file_location("handoffctl_recovery_base", SOURCE)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load handoffctl recovery test base")
BASE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BASE)


class HandoffRecoveryTest(unittest.TestCase):
    setUp = BASE.HandoffTest.setUp
    tearDown = BASE.HandoffTest.tearDown
    make_task = BASE.HandoffTest.make_task
    refresh_views = BASE.HandoffTest.refresh_views

    def test_recover_expired_allows_explicit_legacy_compatibility_recovery(self) -> None:
        path = self.make_task(
            status="in_progress",
            owner="legacy-worker",
            claim_expires="2000-01-01T00:00:00+00:00",
        )
        with patch.object(BASE.CORE, "commit", return_value=True):
            BASE.CORE.mutate(
                BASE.argparse.Namespace(
                    task="AR-0001",
                    expected_revision=1,
                    allow_legacy_without_identity=True,
                    note="Confirmed the legacy owner cannot be identified.",
                ),
                "recover-expired",
            )
        recovered, body = BASE.CORE.read_task(path)
        self.assertEqual("open", recovered["status"])
        self.assertEqual("", recovered["owner"])
        self.assertIn("LEGACY_NO_IDENTITY_RECOVERY", body)

    def test_recover_expired_does_not_restore_stale_session_action(self) -> None:
        boot_digest, pid_namespace = BASE.CORE.worker_execution_scope()
        path = self.make_task(
            status="in_progress",
            owner="worker-a",
            claim_expires="2000-01-01T00:00:00+00:00",
            next_action="Keep the current claim action.",
            claim_process={
                "pid": 99999999,
                "start_time": 0,
                "boot_digest": boot_digest,
                "pid_namespace": pid_namespace,
            },
        )
        stale, _ = BASE.CORE.read_task(path)
        stale["next_action"] = "Do not restore this old action."
        BASE.CORE.append_session_record(
            BASE.CORE.ROOT,
            BASE.CORE.build_session_record(stale, "update", "2026-09-24T12:00:00+00:00"),
        )
        stale["task_revision"] = 2
        stale["next_action"] = "Keep the current claim action."
        _, body = BASE.CORE.read_task(path)
        BASE.CORE.write_task(path, stale, body)
        self.refresh_views()
        with patch.object(BASE.CORE, "commit", return_value=True):
            BASE.CORE.mutate(
                BASE.argparse.Namespace(
                    task="AR-0001", expected_revision=2, note="No live process remains."
                ),
                "recover-expired",
            )
        recovered, _ = BASE.CORE.read_task(path)
        self.assertEqual("Keep the current claim action.", recovered["next_action"])

    def test_claim_process_disappearing_during_stat_read_is_absent(self) -> None:
        with (
            patch("pathlib.Path.exists", return_value=True),
            patch("pathlib.Path.read_text", side_effect=FileNotFoundError),
        ):
            self.assertIsNone(BASE.CORE.process_start_time(12345))

    def test_claim_process_inspection_failure_is_write_closed(self) -> None:
        with (
            patch("pathlib.Path.read_text", side_effect=PermissionError),
            self.assertRaisesRegex(RuntimeError, "cannot independently read"),
        ):
            BASE.CORE.process_start_time(12345)

    def test_snapshotless_recovery_rejects_other_execution_scope(self) -> None:
        self.make_task(
            status="in_progress",
            owner="worker-a",
            claim_expires="2000-01-01T00:00:00+00:00",
            claim_process={
                "pid": 99999999,
                "start_time": 0,
                "boot_digest": "sha256:" + "0" * 64,
                "pid_namespace": "1:1",
            },
        )
        with (
            patch.object(BASE.CORE, "commit", return_value=True),
            self.assertRaisesRegex(RuntimeError, "cannot verify the claim execution scope"),
        ):
            BASE.CORE.mutate(
                BASE.argparse.Namespace(task="AR-0001", expected_revision=1, note="Recover."),
                "recover-expired",
            )

    def test_legacy_claim_identity_remains_valid_but_cannot_recover_snapshotless(self) -> None:
        self.make_task(
            status="in_progress",
            owner="worker-a",
            claim_expires="2000-01-01T00:00:00+00:00",
            claim_process={"pid": 99999999, "start_time": 0},
        )
        self.assertFalse(any("invalid claim_process" in error for error in BASE.CORE.validate()))
        with (
            patch.object(BASE.CORE, "commit", return_value=True),
            self.assertRaisesRegex(
                RuntimeError, "requires a scope-bound claim-time worker identity"
            ),
        ):
            BASE.CORE.mutate(
                BASE.argparse.Namespace(task="AR-0001", expected_revision=1, note="Recover."),
                "recover-expired",
            )
