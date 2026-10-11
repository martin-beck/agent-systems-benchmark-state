# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""The opt-in CLI reports queue, local, and remote receipts honestly."""

from __future__ import annotations

import argparse
import io
import json
import tempfile
import unittest
import uuid
from contextlib import redirect_stdout
from pathlib import Path
from typing import cast
from unittest.mock import patch

from tools import handoffctl
from tools.fast_receipt_cli import dispatch_fast
from tools.fast_receipts import ReceiptConflictError, ReceiptStore


class BoundCore:
    def __init__(self, root: Path, project_id: str) -> None:
        self.ROOT = root
        self.project_id = project_id
        self.backend = "git"
        self.binding_checks = 0

    def assert_project_binding(self) -> None:
        self.binding_checks += 1

    def backend_selection(self) -> dict[str, str]:
        return {"backend": self.backend}

    def coordinator_lock_path(self) -> Path:
        return self.ROOT / "private/state.lock"

    def project_binding(self) -> dict[str, str]:
        return {"project_id": self.project_id}


class FastReceiptCLITests(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.core = BoundCore(self.root, str(uuid.uuid4()))
        self.path = self.root / "private/fast-receipts.sqlite3"

    def invoke(self, action: str, **values: object) -> dict[str, object]:
        if action in {"worker", "publisher"}:
            values.setdefault("serve", False)
            values.setdefault("poll_seconds", 0.05 if action == "worker" else 5.0)
        output = io.StringIO()
        with redirect_stdout(output):
            result = dispatch_fast(self.core, argparse.Namespace(fast_action=action, **values))
        self.assertEqual(0, result)
        if not output.getvalue():
            return {}
        decoded = json.loads(output.getvalue())
        self.assertIsInstance(decoded, dict)
        return cast(dict[str, object], decoded)

    def heartbeat(self, **overrides: object) -> dict[str, object]:
        values: dict[str, object] = {
            "key": "worker-a:heartbeat:1",
            "task": "AR-0120",
            "owner": "worker-a",
            "expected_revision": 1,
            "lease_minutes": 20,
        }
        values.update(overrides)
        return self.invoke("heartbeat", **values)

    def promote(self, **overrides: object) -> dict[str, object]:
        values: dict[str, object] = {
            "key": "worker-a:promote:1",
            "task": "AR-0120",
            "expected_revision": 1,
            "note": "Open for implementation.",
        }
        values.update(overrides)
        return self.invoke("promote", **values)

    def claim(self, **overrides: object) -> dict[str, object]:
        values: dict[str, object] = {
            "key": "worker-a:claim:1",
            "task": "AR-0120",
            "owner": "worker-a",
            "expected_revision": 1,
            "lease_minutes": 20,
        }
        values.update(overrides)
        return self.invoke("claim", **values)

    def update(self, **overrides: object) -> dict[str, object]:
        values: dict[str, object] = {
            "key": "worker-a:update:1",
            "task": "AR-0120",
            "owner": "worker-a",
            "expected_revision": 1,
            "status": None,
            "priority": "P1",
            "summary": None,
            "next_action": "Run focused tests.",
            "note": "Refined the execution plan.",
        }
        values.update(overrides)
        return self.invoke("update", **values)

    def test_enqueue_is_durable_but_not_completed(self) -> None:
        queued = self.heartbeat()
        self.assertEqual("queued-local", queued["phase"])
        self.assertIsNone(queued["commit_oid"])
        self.assertIsNone(queued["remote_oid"])
        self.assertNotIn("payload_json", queued)
        self.assertNotIn("idempotency_key", queued)
        self.assertEqual(queued, self.heartbeat())
        self.assertEqual(queued, self.invoke("receipt", receipt_id=queued["receipt_id"]))
        with ReceiptStore(self.path, self.core.project_id) as store:
            durable = store.read(str(queued["receipt_id"]))
        assert durable is not None
        self.assertEqual("queued-local", durable["phase"])
        self.assertEqual(3, self.core.binding_checks)

    def test_key_reuse_with_changed_fence_rejects(self) -> None:
        queued = self.heartbeat()
        with self.assertRaises(ReceiptConflictError):
            self.heartbeat(expected_revision=2)
        self.assertEqual(queued, self.invoke("receipt", receipt_id=queued["receipt_id"]))

    def test_promote_is_a_durable_bounded_receipt(self) -> None:
        queued = self.promote()
        self.assertEqual("promote", queued["operation"])
        self.assertEqual("queued-local", queued["phase"])
        self.assertEqual(queued, self.promote())

    def test_claim_is_a_durable_fenced_receipt(self) -> None:
        queued = self.claim()
        self.assertEqual("claim", queued["operation"])
        self.assertEqual("queued-local", queued["phase"])
        self.assertEqual(queued, self.claim())

    def test_update_is_a_durable_closed_fenced_receipt(self) -> None:
        queued = self.update()
        self.assertEqual("update", queued["operation"])
        self.assertEqual("queued-local", queued["phase"])
        self.assertEqual(queued, self.update())
        with self.assertRaises(ValueError):
            self.update(priority=None, next_action=None)

    def test_unknown_receipt_and_non_git_backend_fail_closed(self) -> None:
        self.core.backend = "sqlite"
        with self.assertRaisesRegex(RuntimeError, "require Git authority"):
            self.heartbeat()
        self.assertFalse(self.path.exists())
        self.core.backend = "git"
        with self.assertRaisesRegex(RuntimeError, "unknown fast receipt"):
            self.invoke("receipt", receipt_id="a" * 32)

    def test_invalid_observation_age_is_a_cli_runtime_error(self) -> None:
        with (
            patch(
                "tools.fast_receipt_cli.ObservationCache.observe",
                side_effect=ValueError("max_age_seconds must be bounded"),
            ),
            self.assertRaisesRegex(RuntimeError, "max_age_seconds must be bounded"),
        ):
            dispatch_fast(self.core, argparse.Namespace(fast_action="observe", max_age_seconds=-1))

    def test_one_cycle_worker_reports_separate_outcomes(self) -> None:
        queued = self.heartbeat()
        with (
            patch("tools.fast_receipt_cli.process_pending", return_value=[]) as local,
            patch("tools.fast_receipt_cli.publish_pending", return_value=[]) as remote,
        ):
            result = self.invoke("worker", limit=3)
        self.assertEqual({"local": [], "remote": []}, result)
        local.assert_called_once()
        remote.assert_called_once()
        self.assertEqual(
            "queued-local", self.invoke("receipt", receipt_id=queued["receipt_id"])["phase"]
        )

    def test_resident_local_and_publication_services_are_separate(self) -> None:
        with (
            patch("tools.fast_receipt_cli.serve_local") as local,
            patch("tools.fast_receipt_cli.serve_publication") as remote,
        ):
            self.assertEqual({}, self.invoke("worker", serve=True, limit=7, poll_seconds=0.1))
            self.assertEqual({}, self.invoke("publisher", serve=True, poll_seconds=5.0))
        local.assert_called_once()
        remote.assert_called_once()
        self.assertEqual(7, local.call_args.kwargs["limit"])
        self.assertEqual(5.0, remote.call_args.kwargs["poll_seconds"])

    def test_one_cycle_publisher_returns_remote_receipts_only(self) -> None:
        with patch("tools.fast_receipt_cli.publish_pending", return_value=[]) as publish:
            self.assertEqual({"remote": []}, self.invoke("publisher"))
        publish.assert_called_once()

    def test_parser_requires_explicit_fast_heartbeat_fence_and_key(self) -> None:
        with (
            patch.object(handoffctl, "assert_project_binding"),
            patch.object(handoffctl, "dispatch_bound_command", return_value=0) as dispatch,
            patch(
                "sys.argv", ["handoffctl", "fast", "heartbeat", "AR-0120", "--owner", "worker-a"]
            ),
            self.assertRaises(SystemExit),
        ):
            handoffctl.main()
        with (
            patch.object(handoffctl, "assert_project_binding"),
            patch.object(handoffctl, "dispatch_bound_command", return_value=0) as dispatch,
            patch(
                "sys.argv",
                [
                    "handoffctl",
                    "fast",
                    "heartbeat",
                    "AR-0120",
                    "--owner",
                    "worker-a",
                    "--expected-revision",
                    "7",
                    "--key",
                    "worker-a:heartbeat:7",
                ],
            ),
        ):
            self.assertEqual(0, handoffctl.main())
        args = dispatch.call_args.args[0]
        self.assertEqual("fast", args.cmd)
        self.assertEqual("heartbeat", args.fast_action)
        self.assertEqual(7, args.expected_revision)

    def test_parser_requires_fenced_fast_promote(self) -> None:
        with (
            patch.object(handoffctl, "assert_project_binding"),
            patch.object(handoffctl, "dispatch_bound_command", return_value=0) as dispatch,
            patch("sys.argv", ["handoffctl", "fast", "promote", "AR-0120", "--note", "Open"]),
            self.assertRaises(SystemExit),
        ):
            handoffctl.main()
        with (
            patch.object(handoffctl, "assert_project_binding"),
            patch.object(handoffctl, "dispatch_bound_command", return_value=0) as dispatch,
            patch(
                "sys.argv",
                [
                    "handoffctl",
                    "fast",
                    "promote",
                    "AR-0120",
                    "--expected-revision",
                    "7",
                    "--note",
                    "Open",
                    "--key",
                    "worker-a:promote:7",
                ],
            ),
        ):
            self.assertEqual(0, handoffctl.main())
        args = dispatch.call_args.args[0]
        self.assertEqual("promote", args.fast_action)
        self.assertEqual(7, args.expected_revision)

    def test_parser_accepts_fenced_fast_update(self) -> None:
        with (
            patch.object(handoffctl, "assert_project_binding"),
            patch.object(handoffctl, "dispatch_bound_command", return_value=0) as dispatch,
            patch(
                "sys.argv",
                [
                    "handoffctl",
                    "fast",
                    "update",
                    "AR-0120",
                    "--owner",
                    "worker-a",
                    "--expected-revision",
                    "7",
                    "--priority",
                    "P1",
                    "--note",
                    "Refined.",
                    "--key",
                    "worker-a:update:7",
                ],
            ),
        ):
            self.assertEqual(0, handoffctl.main())
        args = dispatch.call_args.args[0]
        self.assertEqual("update", args.fast_action)
        self.assertEqual("P1", args.priority)


if __name__ == "__main__":
    unittest.main()
