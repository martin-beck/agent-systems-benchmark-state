# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Internal receipt executor outcomes are exact and never inferred from enqueue."""

from __future__ import annotations

import json
import re
import subprocess
import tempfile
import unittest
import uuid
from pathlib import Path
from typing import Any
from unittest.mock import Mock, patch

from tools import fast_receipt_worker as worker
from tools.fast_receipt_worker import (
    process_one,
    process_pending,
    publication_lock,
    publish_pending,
    recover_running,
    serve_local,
    serve_publication,
    service_lock,
    verify_local_commit,
)
from tools.fast_receipts import ReceiptStore
from tools.handoffctl import SubprocessTimeoutError
from tools.session_records import MAX_SESSION_RECORDS, build_session_record


class FakeCore:
    SubprocessTimeoutError = SubprocessTimeoutError

    def __init__(self, root: Path, outcome: str) -> None:
        self.ROOT = root
        self.outcome = outcome
        self.calls = 0
        self.status_view = True

    def assert_project_binding(self) -> None:
        return None

    def coordinator_lock_path(self) -> Path:
        return self.ROOT / "private/state.lock"

    def project_binding(self) -> dict[str, str]:
        return {"project_id": (self.ROOT / ".project-id").read_text()}

    def backend_selection(self) -> dict[str, str]:
        return {"backend": "git"}

    def mutate(self, args: Any, kind: str) -> None:
        self.calls += 1
        if kind not in {"claim", "heartbeat", "promote", "update"}:
            raise AssertionError(kind)
        if self.outcome == "stale":
            raise RuntimeError("stale revision: expected 1, current 2")
        if self.outcome == "role-denied":
            raise RuntimeError("role admission denied: worker-a is not eligible")
        if self.outcome == "identity-expired":
            raise RuntimeError("claim worker identity is not a live matching process")
        if self.outcome == "unknown":
            raise RuntimeError("unknown mutation failure")
        if self.outcome == "post-commit":
            raise RuntimeError("post-commit observation failed")
        args._committed_oid = "a" * 40

    def run(self, command: list[str], *, check: bool = True) -> subprocess.CompletedProcess[str]:
        del check
        return subprocess.CompletedProcess(command, 0, "")

    def _transition_note(self, body: str, note: str, at: str) -> str:
        del body, note, at
        return "expected heartbeat body\n"

    def render_current(self, tasks: list[object]) -> str:
        del tasks
        return "current\n"

    def render_status_views(self, tasks: list[object]) -> dict[str, str]:
        del tasks
        return {"STATUS.md": "status\n"}

    def project_settings(self) -> dict[str, bool]:
        return {"status_view": self.status_view}

    @staticmethod
    def scoped_claim_process(value: object) -> bool:
        return (
            isinstance(value, dict)
            and set(value) == {"pid", "start_time", "boot_digest", "pid_namespace"}
            and isinstance(value.get("pid"), int)
            and value["pid"] > 0
            and isinstance(value.get("start_time"), int)
            and value["start_time"] >= 0
            and isinstance(value.get("boot_digest"), str)
            and bool(re.fullmatch(r"sha256:[0-9a-f]{64}", value["boot_digest"]))
            and isinstance(value.get("pid_namespace"), str)
            and bool(re.fullmatch(r"[0-9]+:[0-9]+", value["pid_namespace"]))
        )


class PublicationCore(FakeCore):
    def replication_enabled(self) -> bool:
        return True

    def run(self, command: list[str], *, check: bool = True) -> subprocess.CompletedProcess[str]:
        del check
        if "symbolic-ref" in command:
            return subprocess.CompletedProcess(command, 0, "main\n")
        if "rev-parse" in command:
            return subprocess.CompletedProcess(command, 0, "b" * 40 + "\n")
        return subprocess.CompletedProcess(command, 0, "")


class FastReceiptWorkerTests(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        project_id = str(uuid.uuid4())
        (self.root / ".project-id").write_text(project_id)
        self.store = ReceiptStore(self.root / "private/fast-receipts.sqlite3", project_id)
        self.addCleanup(self.store.close)

    def enqueue(self) -> str:
        receipt = self.store.enqueue_heartbeat(
            key="worker-a:heartbeat:1",
            task="AR-0120",
            owner="worker-a",
            expected_revision=1,
            lease_minutes=20,
        )
        return str(receipt["receipt_id"])

    def enqueue_promote(self) -> str:
        receipt = self.store.enqueue_promote(
            key="worker-a:promote:1",
            task="AR-0120",
            expected_revision=1,
            note="Dependencies verified.",
        )
        return str(receipt["receipt_id"])

    def enqueue_claim(self) -> str:
        receipt = self.store.enqueue_claim(
            key="worker-a:claim:1",
            task="AR-0120",
            owner="worker-a",
            expected_revision=1,
            lease_minutes=20,
        )
        return str(receipt["receipt_id"])

    def enqueue_update(self) -> str:
        receipt = self.store.enqueue_update(
            key="worker-a:update:1",
            task="AR-0120",
            owner="worker-a",
            expected_revision=1,
            changes={"priority": "P1", "next_action": "Run focused tests."},
            note="Refined execution plan.",
        )
        return str(receipt["receipt_id"])

    def complete_local(self) -> str:
        receipt_id = self.enqueue()
        self.store.claim_next()
        self.store.record_local_commit(receipt_id, "a" * 40, 2)
        return receipt_id

    def test_success_requires_verified_commit_before_local_receipt(self) -> None:
        receipt_id = self.enqueue()
        core = FakeCore(self.root, "success")
        with patch("tools.fast_receipt_worker.verify_local_commit", return_value=2) as verify:
            result = process_one(core, self.store)
        assert result is not None
        self.assertEqual("completed-local", result["phase"])
        self.assertEqual("a" * 40, result["commit_oid"])
        verify.assert_called_once()
        self.assertEqual(receipt_id, verify.call_args.args[1]["receipt_id"])
        self.assertIsNone(process_one(core, self.store))
        self.assertEqual(1, core.calls)

    def test_promote_uses_typed_namespace_and_verified_commit(self) -> None:
        receipt_id = self.enqueue_promote()
        core = FakeCore(self.root, "success")
        with patch("tools.fast_receipt_worker.verify_local_commit", return_value=2) as verify:
            result = process_one(core, self.store)
        assert result is not None
        self.assertEqual("completed-local", result["phase"])
        self.assertEqual(receipt_id, verify.call_args.args[1]["receipt_id"])
        self.assertEqual(1, core.calls)

    def test_claim_uses_typed_namespace_and_verified_commit(self) -> None:
        receipt_id = self.enqueue_claim()
        core = FakeCore(self.root, "success")
        with patch("tools.fast_receipt_worker.verify_local_commit", return_value=2) as verify:
            result = process_one(core, self.store)
        assert result is not None
        self.assertEqual("completed-local", result["phase"])
        self.assertEqual(receipt_id, verify.call_args.args[1]["receipt_id"])
        self.assertEqual(1, core.calls)

    def test_update_uses_closed_typed_namespace_and_verified_commit(self) -> None:
        receipt_id = self.enqueue_update()
        core = FakeCore(self.root, "success")
        with patch("tools.fast_receipt_worker.verify_local_commit", return_value=2) as verify:
            result = process_one(core, self.store)
        assert result is not None
        self.assertEqual("completed-local", result["phase"])
        self.assertEqual(receipt_id, verify.call_args.args[1]["receipt_id"])
        self.assertEqual(1, core.calls)

    def test_update_with_unexpected_change_never_executes(self) -> None:
        receipt_id = self.enqueue_update()
        queued = self.store.read(receipt_id)
        assert queued is not None
        payload = json.loads(str(queued["payload_json"]))
        payload["changes"]["owner"] = "injected"
        canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
        import hashlib

        self.store.connection.execute(
            "UPDATE intents SET payload_json=?, input_digest=? WHERE receipt_id=?",
            (canonical, hashlib.sha256(canonical.encode()).hexdigest(), receipt_id),
        )
        result = process_one(FakeCore(self.root, "success"), self.store)
        assert result is not None
        self.assertEqual("ambiguous", result["phase"])

    def test_claim_role_denial_is_rejected_not_ambiguous(self) -> None:
        receipt_id = self.enqueue_claim()
        result = process_one(FakeCore(self.root, "role-denied"), self.store)
        assert result is not None
        self.assertEqual(receipt_id, result["receipt_id"])
        self.assertEqual("rejected", result["phase"])
        self.assertEqual("ADMISSION_REJECTED", result["error_code"])

    def test_claim_with_expired_worker_identity_is_rejected_not_ambiguous(self) -> None:
        receipt_id = self.enqueue_claim()
        result = process_one(FakeCore(self.root, "identity-expired"), self.store)
        assert result is not None
        self.assertEqual(receipt_id, result["receipt_id"])
        self.assertEqual("rejected", result["phase"])
        self.assertEqual("ADMISSION_REJECTED", result["error_code"])

    def test_promote_with_unexpected_payload_field_never_executes(self) -> None:
        receipt_id = self.enqueue_promote()
        queued = self.store.read(receipt_id)
        assert queued is not None
        payload = json.loads(str(queued["payload_json"]))
        payload["owner"] = "injected"
        canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
        import hashlib

        self.store.connection.execute(
            "UPDATE intents SET payload_json=?, input_digest=? WHERE receipt_id=?",
            (canonical, hashlib.sha256(canonical.encode()).hexdigest(), receipt_id),
        )
        core = FakeCore(self.root, "success")
        result = process_one(core, self.store)
        assert result is not None
        self.assertEqual("ambiguous", result["phase"])
        self.assertEqual(0, core.calls)

    def test_foreign_project_store_is_rejected_before_reservation(self) -> None:
        receipt_id = self.enqueue()
        (self.root / ".project-id").write_text(str(uuid.uuid4()))
        core = FakeCore(self.root, "success")
        with self.assertRaisesRegex(RuntimeError, "does not match the bound project"):
            process_one(core, self.store)
        current = self.store.read(receipt_id)
        assert current is not None
        self.assertEqual("queued-local", current["phase"])
        self.assertEqual(0, core.calls)

    def test_wrong_common_directory_store_is_rejected(self) -> None:
        other = ReceiptStore(self.root / "private/other.sqlite3", self.store.project_id)
        self.addCleanup(other.close)
        queued = other.enqueue_heartbeat(
            key="worker-a:heartbeat:1",
            task="AR-0120",
            owner="worker-a",
            expected_revision=1,
            lease_minutes=20,
        )
        core = FakeCore(self.root, "success")
        with self.assertRaisesRegex(RuntimeError, "does not match the bound project"):
            process_one(core, other)
        current = other.read(str(queued["receipt_id"]))
        assert current is not None
        self.assertEqual("queued-local", current["phase"])

    def test_non_git_backend_rejects_without_reserving(self) -> None:
        receipt_id = self.enqueue()
        core = FakeCore(self.root, "success")
        with (
            patch.object(core, "backend_selection", return_value={"backend": "sqlite"}),
            self.assertRaisesRegex(RuntimeError, "require Git authority"),
        ):
            process_one(core, self.store)
        current = self.store.read(receipt_id)
        assert current is not None
        self.assertEqual("queued-local", current["phase"])
        self.assertEqual(0, core.calls)

    def test_corrupt_canonical_intent_never_executes(self) -> None:
        receipt_id = self.enqueue()
        self.store.connection.execute(
            "UPDATE intents SET payload_json='{}' WHERE receipt_id=?", (receipt_id,)
        )
        core = FakeCore(self.root, "success")
        result = process_one(core, self.store)
        assert result is not None
        self.assertEqual("ambiguous", result["phase"])
        self.assertEqual(0, core.calls)

    def test_changed_valid_payload_with_stale_digest_never_executes(self) -> None:
        receipt_id = self.enqueue()
        queued = self.store.read(receipt_id)
        assert queued is not None
        original_digest = queued["input_digest"]
        payload = json.loads(str(queued["payload_json"]))
        payload["lease_minutes"] = 21
        changed = json.dumps(payload, sort_keys=True, separators=(",", ":"))
        self.store.connection.execute(
            "UPDATE intents SET payload_json=? WHERE receipt_id=?", (changed, receipt_id)
        )
        core = FakeCore(self.root, "success")
        result = process_one(core, self.store)
        assert result is not None
        self.assertEqual("ambiguous", result["phase"])
        self.assertIsNone(result["commit_oid"])
        self.assertEqual(0, core.calls)
        self.assertEqual(original_digest, result["input_digest"])
        self.assertEqual(changed, result["payload_json"])

    def test_stale_admission_is_rejected_without_local_commit(self) -> None:
        self.enqueue()
        core = FakeCore(self.root, "stale")
        result = process_one(core, self.store)
        assert result is not None
        self.assertEqual("rejected", result["phase"])
        self.assertIsNone(result["commit_oid"])

    def test_unknown_failure_is_ambiguous_not_completed(self) -> None:
        self.enqueue()
        core = FakeCore(self.root, "unknown")
        result = process_one(core, self.store)
        assert result is not None
        self.assertEqual("ambiguous", result["phase"])
        self.assertIsNone(result["commit_oid"])

    def test_commit_found_after_worker_failure_can_be_recovered(self) -> None:
        self.enqueue()
        core = FakeCore(self.root, "post-commit")
        with (
            patch("tools.fast_receipt_worker.find_receipt_commit", return_value="b" * 40),
            patch("tools.fast_receipt_worker.verify_local_commit", return_value=2),
        ):
            result = process_one(core, self.store)
        assert result is not None
        self.assertEqual("completed-local", result["phase"])
        self.assertEqual("b" * 40, result["commit_oid"])

    def test_untrusted_commit_stays_ambiguous(self) -> None:
        self.enqueue()
        core = FakeCore(self.root, "success")
        with (
            patch(
                "tools.fast_receipt_worker.verify_local_commit",
                side_effect=RuntimeError("signature is not trusted"),
            ),
            patch("tools.fast_receipt_worker.find_receipt_commit", return_value="a" * 40),
        ):
            result = process_one(core, self.store)
        assert result is not None
        self.assertEqual("ambiguous", result["phase"])
        self.assertIsNone(result["commit_oid"])

    def test_off_branch_commit_cannot_be_local_completion(self) -> None:
        intent_id = self.enqueue()
        intent = self.store.read(intent_id)
        assert intent is not None
        core = FakeCore(self.root, "success")

        def off_branch(
            command: list[str], *, check: bool = True
        ) -> subprocess.CompletedProcess[str]:
            del check
            if "merge-base" in command:
                return subprocess.CompletedProcess(command, 1, "")
            return subprocess.CompletedProcess(command, 0, "")

        core.run = off_branch  # type: ignore[method-assign]
        with self.assertRaisesRegex(RuntimeError, "not on the active state branch"):
            verify_local_commit(core, intent, "a" * 40)

    def test_restart_does_not_reexecute_running_intent_without_commit(self) -> None:
        receipt_id = self.enqueue()
        self.store.claim_next()
        core = FakeCore(self.root, "success")
        outcomes = recover_running(core, self.store)
        self.assertEqual(1, len(outcomes))
        self.assertEqual("ambiguous", outcomes[0]["phase"])
        self.assertEqual("INTERRUPTED_BEFORE_COMMIT", outcomes[0]["error_code"])
        self.assertEqual(receipt_id, outcomes[0]["receipt_id"])
        self.assertEqual(0, core.calls)

    def test_restart_recovers_exact_signed_commit_marker(self) -> None:
        receipt_id = self.enqueue()
        self.store.claim_next()
        core = FakeCore(self.root, "success")
        with (
            patch("tools.fast_receipt_worker.find_receipt_commit", return_value="a" * 40),
            patch("tools.fast_receipt_worker.verify_local_commit", return_value=2),
        ):
            outcomes = recover_running(core, self.store)
        self.assertEqual(1, len(outcomes))
        self.assertEqual("completed-local", outcomes[0]["phase"])
        self.assertEqual(receipt_id, outcomes[0]["receipt_id"])
        self.assertEqual(0, core.calls)

    def test_restart_rejects_unverifiable_marked_commit_without_replay(self) -> None:
        receipt_id = self.enqueue()
        self.store.claim_next()
        core = FakeCore(self.root, "success")
        with (
            patch("tools.fast_receipt_worker.find_receipt_commit", return_value="a" * 40),
            patch(
                "tools.fast_receipt_worker.verify_local_commit",
                side_effect=RuntimeError("signature is not trusted"),
            ),
        ):
            outcomes = recover_running(core, self.store)
        self.assertEqual("ambiguous", outcomes[0]["phase"])
        self.assertEqual("COMMIT_EVIDENCE_UNKNOWN", outcomes[0]["error_code"])
        self.assertEqual(receipt_id, outcomes[0]["receipt_id"])
        self.assertEqual(0, core.calls)

    def test_service_lock_rejects_competing_executor(self) -> None:
        core = FakeCore(self.root, "success")

        def compete() -> None:
            with service_lock(core):
                pass

        with service_lock(core), self.assertRaisesRegex(RuntimeError, "already active"):
            compete()

    def test_service_lock_rejects_public_directory_and_lock_file(self) -> None:
        core = FakeCore(self.root, "success")
        directory = self.root / "private"
        directory.chmod(0o755)
        with self.assertRaisesRegex(RuntimeError, "directory is not private"), service_lock(core):
            pass
        directory.chmod(0o700)
        lock = directory / "fast-receipts.service.lock"
        lock.write_text("")
        lock.chmod(0o644)
        with self.assertRaisesRegex(RuntimeError, "lock is unsafe"), service_lock(core):
            pass

    def test_batch_bounds_are_enforced_before_service_lock(self) -> None:
        core = FakeCore(self.root, "success")
        for limit in (0, -1, 1025):
            with self.subTest(limit=limit), self.assertRaisesRegex(ValueError, "batch limit"):
                process_pending(core, self.store, limit=limit)

    def test_resident_local_service_recovers_then_drains_and_releases_lock(self) -> None:
        core = FakeCore(self.root, "success")
        processed = {"phase": "completed-local"}
        with (
            patch.object(worker, "recover_running", return_value=[]) as recover,
            patch.object(worker, "process_one", side_effect=[processed, None, None]) as execute,
            patch("tools.fast_receipt_worker.time.sleep", side_effect=KeyboardInterrupt) as sleep,
            self.assertRaises(KeyboardInterrupt),
        ):
            serve_local(core, self.store, limit=2, poll_seconds=0.02)
        recover.assert_called_once_with(core, self.store)
        self.assertEqual(3, execute.call_count)
        sleep.assert_called_once_with(0.02)
        with service_lock(core):
            pass

    def test_publisher_lock_is_independent_and_released_after_stop(self) -> None:
        core = FakeCore(self.root, "success")
        with publication_lock(core):
            with service_lock(core):
                pass
            with self.assertRaisesRegex(RuntimeError, "already active"), publication_lock(core):
                pass
        with (
            patch.object(worker, "publish_pending", return_value=[]) as publish,
            patch("tools.fast_receipt_worker.time.sleep", side_effect=KeyboardInterrupt) as sleep,
            self.assertRaises(KeyboardInterrupt),
        ):
            serve_publication(core, self.store, poll_seconds=1.0)
        publish.assert_called_once_with(core, self.store)
        sleep.assert_called_once_with(1.0)
        with publication_lock(core):
            pass

    def test_resident_service_limits_reject_without_claiming_lock(self) -> None:
        core = FakeCore(self.root, "success")
        for limit, polling in ((0, 0.05), (1, 0.0), (1025, 0.05), (1, 61.0)):
            with (
                self.subTest(limit=limit, polling=polling),
                self.assertRaisesRegex(ValueError, "service limits"),
            ):
                serve_local(core, self.store, limit=limit, poll_seconds=polling)
        for polling in (0.0, 61.0):
            with (
                self.subTest(publication_polling=polling),
                self.assertRaisesRegex(ValueError, "publication polling"),
            ):
                serve_publication(core, self.store, poll_seconds=polling)

    def test_heartbeat_delta_rejects_wrong_state_lease_and_body(self) -> None:
        core = FakeCore(self.root, "success")
        before = {
            "id": "AR-0120",
            "owner": "worker-a",
            "status": "in_progress",
            "task_revision": 1,
            "priority": "P1",
            "updated_at": "2026-10-09T09:00:00+00:00",
            "claim_expires": "2026-10-09T09:20:00+00:00",
        }
        after = {
            **before,
            "task_revision": 2,
            "updated_at": "2026-10-09T10:00:00+00:00",
            "claim_expires": "2026-10-09T10:20:00+00:00",
        }
        intent = {"task_id": "AR-0120", "expected_revision": 1}
        payload = {"owner": "worker-a", "lease_minutes": 20}
        record = (before, "before\n", after, "expected heartbeat body\n")
        with patch.object(worker, "_task_change", return_value=record):
            self.assertEqual(2, worker._verify_heartbeat_delta(core, intent, payload, "a" * 40))
        cases = (
            ("before-owner", "before", "owner", "other", "task state"),
            ("before-status", "before", "status", "open", "task state"),
            ("after-revision", "after", "task_revision", 3, "task state"),
            ("after-priority", "after", "priority", "P0", "non-heartbeat"),
            ("naive-time", "after", "updated_at", "2026-10-09T10:00:00", "naive"),
            ("wrong-lease", "after", "claim_expires", "2026-10-09T10:19:00+00:00", "lease"),
        )
        for label, side, field, value, message in cases:
            with self.subTest(label=label):
                changed_before, changed_after = dict(before), dict(after)
                (changed_before if side == "before" else changed_after)[field] = value
                with (
                    patch.object(
                        worker,
                        "_task_change",
                        return_value=(
                            changed_before,
                            "before\n",
                            changed_after,
                            "expected heartbeat body\n",
                        ),
                    ),
                    self.assertRaisesRegex(RuntimeError, message),
                ):
                    worker._verify_heartbeat_delta(core, intent, payload, "a" * 40)
        with (
            patch.object(
                worker, "_task_change", return_value=(before, "before\n", after, "forged body\n")
            ),
            self.assertRaisesRegex(RuntimeError, "body does not match"),
        ):
            worker._verify_heartbeat_delta(core, intent, payload, "a" * 40)

    def test_claim_and_promote_deltas_accept_only_exact_transitions(self) -> None:
        core = FakeCore(self.root, "success")
        claim_before = {
            "id": "AR-0120",
            "owner": "",
            "status": "open",
            "claim_expires": "",
            "task_revision": 1,
            "priority": "P1",
            "updated_at": "2026-10-09T09:00:00+00:00",
        }
        claim_after = {
            **claim_before,
            "owner": "worker-a",
            "status": "in_progress",
            "claim_expires": "2026-10-09T10:20:00+00:00",
            "task_revision": 2,
            "updated_at": "2026-10-09T10:00:00+00:00",
        }
        claim_intent = {"task_id": "AR-0120", "expected_revision": 1}
        claim_payload = {"owner": "worker-a", "lease_minutes": 20}
        with patch.object(
            worker,
            "_task_change",
            return_value=(claim_before, "before\n", claim_after, "expected heartbeat body\n"),
        ):
            self.assertEqual(
                2, worker._verify_claim_delta(core, claim_intent, claim_payload, "a" * 40)
            )
        scoped_payload = {
            **claim_payload,
            "worker_pid": 123,
            "worker_start_time": 456,
        }
        scoped_after = {
            **claim_after,
            "claim_process": {
                "pid": 123,
                "start_time": 456,
                "boot_digest": "sha256:" + "a" * 64,
                "pid_namespace": "1:2",
            },
        }
        with patch.object(
            worker,
            "_task_change",
            return_value=(claim_before, "before\n", scoped_after, "expected heartbeat body\n"),
        ):
            self.assertEqual(
                2, worker._verify_claim_delta(core, claim_intent, scoped_payload, "a" * 40)
            )
        malformed_scope = {
            **claim_after,
            "claim_process": {
                "pid": 123,
                "start_time": 456,
                "boot_digest": "not-a-digest",
                "pid_namespace": "1:2",
            },
        }
        with (
            patch.object(
                worker,
                "_task_change",
                return_value=(
                    claim_before,
                    "before\n",
                    malformed_scope,
                    "expected heartbeat body\n",
                ),
            ),
            self.assertRaisesRegex(RuntimeError, "does not match"),
        ):
            worker._verify_claim_delta(core, claim_intent, scoped_payload, "a" * 40)
        for field, value, message in (
            ("priority", "P0", "non-claim"),
            ("updated_at", "2026-10-09T10:00:00", "naive"),
            ("claim_expires", "2026-10-09T10:19:00+00:00", "lease"),
        ):
            altered = dict(claim_after)
            altered[field] = value
            with (
                self.subTest(claim_field=field),
                patch.object(
                    worker,
                    "_task_change",
                    return_value=(claim_before, "before\n", altered, "forged body\n"),
                ),
                self.assertRaisesRegex(RuntimeError, message),
            ):
                worker._verify_claim_delta(core, claim_intent, claim_payload, "a" * 40)

        promote_before = {
            "id": "AR-0120",
            "owner": "",
            "status": "planned",
            "claim_expires": "",
            "task_revision": 1,
            "priority": "P1",
            "updated_at": "2026-10-09T09:00:00+00:00",
        }
        promote_after = {
            **promote_before,
            "status": "open",
            "task_revision": 2,
            "updated_at": "2026-10-09T10:00:00+00:00",
        }
        promote_intent = {"task_id": "AR-0120", "expected_revision": 1}
        promote_payload = {"note": "Dependencies verified."}
        with patch.object(
            worker,
            "_task_change",
            return_value=(promote_before, "before\n", promote_after, "expected heartbeat body\n"),
        ):
            self.assertEqual(
                2, worker._verify_promote_delta(core, promote_intent, promote_payload, "a" * 40)
            )
        changed = dict(promote_after)
        changed["priority"] = "P0"
        with (
            patch.object(
                worker,
                "_task_change",
                return_value=(promote_before, "before\n", changed, "forged body\n"),
            ),
            self.assertRaisesRegex(RuntimeError, "non-promote"),
        ):
            worker._verify_promote_delta(core, promote_intent, promote_payload, "a" * 40)

    def test_update_delta_accepts_only_the_queued_closed_change_set(self) -> None:
        core = FakeCore(self.root, "success")
        before = {
            "id": "AR-0120",
            "owner": "worker-a",
            "status": "in_progress",
            "claim_expires": "2026-10-09T10:20:00+00:00",
            "task_revision": 1,
            "priority": "P2",
            "summary": "Original summary.",
            "next_action": "Original action.",
            "updated_at": "2026-10-09T09:00:00+00:00",
        }
        after = {
            **before,
            "task_revision": 2,
            "priority": "P1",
            "next_action": "Run focused tests.",
            "updated_at": "2026-10-09T10:00:00+00:00",
        }
        intent = {"task_id": "AR-0120", "expected_revision": 1}
        payload = {
            "owner": "worker-a",
            "changes": {"priority": "P1", "next_action": "Run focused tests."},
            "note": "Refined execution plan.",
        }
        with (
            patch.object(
                worker,
                "_task_change",
                return_value=(before, "before\n", after, "expected heartbeat body\n"),
            ) as changed,
            patch.object(worker, "_verify_update_session") as session,
        ):
            self.assertEqual(2, worker._verify_update_delta(core, intent, payload, "a" * 40))
        self.assertEqual(
            frozenset(("sessions/AR-0120.jsonl",)), changed.call_args.kwargs["sidecars"]
        )
        session.assert_called_once()
        for field, value, message in (
            ("owner", "worker-b", "task state"),
            ("summary", "injected", "fields outside"),
            ("priority", "P3", "fields outside"),
            ("claim_expires", "", "non-update"),
        ):
            altered = dict(after)
            altered[field] = value
            with (
                self.subTest(field=field),
                patch.object(
                    worker,
                    "_task_change",
                    return_value=(before, "before\n", altered, "expected heartbeat body\n"),
                ),
                patch.object(worker, "_verify_update_session"),
                self.assertRaisesRegex(RuntimeError, message),
            ):
                worker._verify_update_delta(core, intent, payload, "a" * 40)

    def test_update_session_requires_the_exact_canonical_append(self) -> None:
        core = FakeCore(self.root, "success")
        after = {"updated_at": "2026-10-09T10:00:00+00:00"}
        expected = {"task": "AR-0120", "task_revision": 2}
        core.build_session_record = lambda *_args: expected  # type: ignore[attr-defined]
        with (
            patch.object(worker, "_git", side_effect=["a" * 40, "", ""]),
            patch.object(worker, "_session_rows", side_effect=[[], [expected]]),
        ):
            worker._verify_update_session(
                core, "b" * 40, "sessions/AR-0120.jsonl", "AR-0120", after
            )
        with (
            patch.object(worker, "_git", side_effect=["a" * 40, "", ""]),
            patch.object(worker, "_session_rows", side_effect=[[], [{"task": "forged"}]]),
            self.assertRaisesRegex(RuntimeError, "session does not match"),
        ):
            worker._verify_update_session(
                core, "b" * 40, "sessions/AR-0120.jsonl", "AR-0120", after
            )

    def test_session_rows_validate_canonical_bounded_history(self) -> None:
        def record(revision: int) -> dict[str, object]:
            return build_session_record(
                {
                    "id": "AR-0120",
                    "task_revision": revision,
                    "status": "in_progress",
                    "branch": "ar0120-example",
                    "worktree_key": "example",
                    "spec_ref": "spec.json",
                    "spec_revision": 1,
                    "next_action": "Continue the bounded task.",
                },
                "update",
                f"2026-10-09T10:00:{revision:02d}+00:00",
            )

        first = record(1)
        second = record(2)
        source = "\n".join(
            json.dumps(item, sort_keys=True, separators=(",", ":")) for item in (first, second)
        )
        self.assertEqual([first, second], worker._session_rows(source, "AR-0120"))
        for source, message in (
            ("not-json", "line 1 is invalid"),
            (json.dumps([first]), "line 1 is invalid"),
            (json.dumps({**first, "task": "AR-9999"}), "does not match target"),
            ("\n".join(json.dumps(first) for _ in range(2)), "does not match target"),
            (
                "\n".join(
                    json.dumps(record(number)) for number in range(1, MAX_SESSION_RECORDS + 2)
                ),
                "bounded retention",
            ),
        ):
            with self.subTest(message=message), self.assertRaisesRegex(RuntimeError, message):
                worker._session_rows(source, "AR-0120")

    def test_verify_local_commit_dispatch_and_fail_closed_metadata(self) -> None:
        core = FakeCore(self.root, "success")
        core.project_settings = lambda: {"commit_signoff": False}  # type: ignore[method-assign]
        receipt_id = "f" * 32
        oid = "a" * 40

        def verify(operation: str) -> None:
            intent = {
                "receipt_id": receipt_id,
                "operation": operation,
                "task_id": "AR-0120",
                "payload_json": "{}",
            }
            message = f"chore(state): {operation} AR-0120\n\nHandoffctl-Receipt: {receipt_id}\n"
            verifier = getattr(worker, f"_verify_{operation}_delta")
            with (
                patch.object(worker, "_require_signed_branch_commit"),
                patch.object(worker, "_git", return_value=message),
                patch.object(verifier.__module__ and worker, verifier.__name__, return_value=2),
            ):
                self.assertEqual(2, verify_local_commit(core, intent, oid))

        for operation in ("heartbeat", "claim", "promote", "update"):
            with self.subTest(operation=operation):
                verify(operation)
        base = {
            "receipt_id": receipt_id,
            "operation": "heartbeat",
            "task_id": "AR-0120",
            "payload_json": "{}",
        }
        with (
            patch.object(worker, "_require_signed_branch_commit"),
            patch.object(worker, "_git", return_value="chore(state): heartbeat AR-0120\n"),
            self.assertRaisesRegex(RuntimeError, "marker"),
        ):
            verify_local_commit(core, base, oid)
        for operation, message in (
            ("unknown", "unsupported"),
            ("heartbeat", "operation does not match"),
        ):
            intent = {**base, "operation": operation}
            subject = (
                "chore(state): wrong AR-0120"
                if operation == "heartbeat"
                else "chore(state): unknown AR-0120"
            )
            with (
                self.subTest(operation=operation),
                patch.object(worker, "_require_signed_branch_commit"),
                patch.object(
                    worker,
                    "_git",
                    return_value=f"{subject}\nHandoffctl-Receipt: {receipt_id}\n",
                ),
                self.assertRaisesRegex(RuntimeError, message),
            ):
                verify_local_commit(core, intent, oid)

    def test_observe_remote_main_requires_one_fetchable_exact_ref(self) -> None:
        core = PublicationCore(self.root, "success")
        oid = "b" * 40
        for stdout in (
            "",
            f"{oid}\trefs/heads/main\n{oid}\trefs/heads/main\n",
            "bad refs/heads/main\n",
        ):
            with (
                self.subTest(stdout=stdout),
                patch.object(core, "run", return_value=subprocess.CompletedProcess([], 0, stdout)),
            ):
                self.assertIsNone(worker._observe_remote_main(core))
        responses = [
            subprocess.CompletedProcess([], 0, f"{oid}\trefs/heads/main\n"),
            subprocess.CompletedProcess([], 1, ""),
            subprocess.CompletedProcess([], 0, ""),
            subprocess.CompletedProcess([], 0, ""),
        ]
        with patch.object(core, "run", side_effect=responses) as run:
            self.assertEqual(oid, worker._observe_remote_main(core))
        self.assertIn("fetch", run.call_args_list[2].args[0])
        responses[-1] = subprocess.CompletedProcess([], 1, "")
        with patch.object(core, "run", side_effect=responses):
            self.assertIsNone(worker._observe_remote_main(core))

    def test_worker_validation_and_projection_fail_closed(self) -> None:
        core = FakeCore(self.root, "success")
        valid = {
            "expected_revision": 1,
            "lease_minutes": 20,
            "operation": "claim",
            "owner": "worker-a",
            "project_id": self.store.project_id,
            "task": "AR-0120",
        }

        def intent(payload: object) -> dict[str, Any]:
            text = json.dumps(payload, sort_keys=True, separators=(",", ":"))
            import hashlib

            return {
                "payload_json": text,
                "input_digest": hashlib.sha256(text.encode()).hexdigest(),
                "project_id": self.store.project_id,
                "task_id": "AR-0120",
                "expected_revision": 1,
            }

        self.assertEqual(valid, worker._validated_intent(intent(valid)))
        valid_update = {
            "changes": {"next_action": "Run focused tests."},
            "expected_revision": 1,
            "note": "Refined the plan.",
            "operation": "update",
            "owner": "worker-a",
            "project_id": self.store.project_id,
            "task": "AR-0120",
        }
        self.assertEqual(valid_update, worker._validated_intent(intent(valid_update)))
        for payload, message in (
            ({**valid, "lease_minutes": True}, "claim intent fields"),
            ({**valid, "owner": 1}, "claim intent fields"),
            (
                {**valid_update, "changes": {"next_action": "line\nbreak"}},
                "update intent fields",
            ),
            (
                {**valid_update, "changes": {"summary": "x" * 4001}},
                "update intent fields",
            ),
            ({**valid, "operation": "unknown"}, "unsupported"),
            (["not", "an", "object"], "canonical typed fields"),
        ):
            with self.subTest(payload=payload), self.assertRaisesRegex(RuntimeError, message):
                worker._validated_intent(intent(payload))
        marker = "Handoffctl-Receipt: " + "f" * 32
        with (
            patch.object(
                worker,
                "_git",
                side_effect=["a" * 40 + "\n" + "b" * 40 + "\n", marker, marker],
            ),
            self.assertRaisesRegex(RuntimeError, "multiple commits"),
        ):
            worker.find_receipt_commit(core, "f" * 32)

        before = ({"id": "AR-0120"}, "before\n")
        after = ({"id": "AR-0120"}, "after\n")
        base_calls = ["tasks/AR-0120.md\nCURRENT.md\n", "b" * 40]
        with (
            patch.object(worker, "_task_record", side_effect=[before, after]),
            patch.object(
                worker,
                "_task_views",
                side_effect=[{"CURRENT.md": "expected\n"}, {"CURRENT.md": "expected\n"}],
            ),
            patch.object(worker, "_git", side_effect=[*base_calls, "different\n"]),
            self.assertRaisesRegex(RuntimeError, "projection does not match"),
        ):
            worker._task_change(core, "a" * 40, "AR-0120")
        with (
            patch.object(worker, "_task_record", side_effect=[before, after]),
            patch.object(
                worker,
                "_task_views",
                side_effect=[{"CURRENT.md": "old\n"}, {}],
            ),
            patch.object(worker, "_git", side_effect=[*base_calls, "present\n"]),
            self.assertRaisesRegex(RuntimeError, "retains an obsolete"),
        ):
            worker._task_change(core, "a" * 40, "AR-0120")

    def test_commit_task_shape_and_path_scope_fail_closed(self) -> None:
        core = FakeCore(self.root, "success")
        for source, message in (
            ("not front matter\n", "no front matter"),
            ("---\n{}\n", "incomplete"),
            ("---\n[]\n---\nbody", "invalid"),
        ):
            with (
                self.subTest(message=message),
                patch.object(worker, "_git", return_value=source),
                self.assertRaisesRegex(RuntimeError, message),
            ):
                worker._task_record(core, "a" * 40, "tasks/AR-0120.md")
        for paths, message in (
            ("CURRENT.md\n", "exactly one target"),
            ("tasks/AR-0120.md\nPROJECT_STATE.md\n", "outside target"),
        ):
            with (
                self.subTest(message=message),
                patch.object(worker, "_git", return_value=paths),
                self.assertRaisesRegex(RuntimeError, message),
            ):
                worker._task_change(core, "a" * 40, "AR-0120")
        with (
            patch.object(worker, "_git", side_effect=["tasks/AR-0120.md\n", "bad-parent"]),
            self.assertRaisesRegex(RuntimeError, "no valid parent"),
        ):
            worker._task_change(core, "a" * 40, "AR-0120")

    def test_task_views_skip_disabled_status_projections(self) -> None:
        core = FakeCore(self.root, "success")
        core.status_view = False
        with patch.object(worker, "_git", return_value=""):
            self.assertEqual({"CURRENT.md": "current\n"}, worker._task_views(core, "a" * 40))

    def test_projection_verifier_accepts_pruned_status_shard(self) -> None:
        core = FakeCore(self.root, "success")
        before = ({"id": "AR-0120"}, "before\n")
        after = ({"id": "AR-0120"}, "after\n")
        with (
            patch.object(worker, "_task_record", side_effect=[before, after]),
            patch.object(
                worker,
                "_task_views",
                side_effect=[
                    {"CURRENT.md": "current\n", "status/STATUS-old.md": "old\n"},
                    {"CURRENT.md": "current\n"},
                ],
            ),
            patch.object(
                worker,
                "_git",
                side_effect=[
                    "tasks/AR-0120.md\nstatus/STATUS-old.md\n",
                    "b" * 40,
                    "current\n",
                    "",
                ],
            ),
        ):
            self.assertEqual(
                (before[0], before[1], after[0], after[1]),
                worker._task_change(core, "a" * 40, "AR-0120"),
            )

    def test_bounded_service_drains_queued_intents_once(self) -> None:
        self.enqueue()
        self.store.enqueue_heartbeat(
            key="worker-b:heartbeat:1",
            task="AR-0121",
            owner="worker-b",
            expected_revision=1,
            lease_minutes=20,
        )
        core = FakeCore(self.root, "success")
        with patch("tools.fast_receipt_worker.verify_local_commit", return_value=2):
            outcomes = process_pending(core, self.store, limit=2)
        self.assertEqual(2, len(outcomes))
        self.assertTrue(all(outcome["phase"] == "completed-local" for outcome in outcomes))
        self.assertEqual(2, core.calls)
        self.assertEqual([], process_pending(core, self.store, limit=2))

    def test_failed_push_and_unknown_ref_stay_local(self) -> None:
        receipt_id = self.complete_local()
        core = PublicationCore(self.root, "success")

        def relation(_core: Any, older: str, newer: str) -> bool:
            return (older, newer) in {("a" * 40, "b" * 40), ("c" * 40, "b" * 40)}

        with (
            patch(
                "tools.fast_receipt_worker._observe_remote_main",
                side_effect=["c" * 40, None],
            ),
            patch("tools.fast_receipt_worker._is_ancestor", side_effect=relation),
        ):
            outcomes = publish_pending(core, self.store)
        self.assertEqual(1, len(outcomes))
        self.assertEqual("completed-local", outcomes[0]["phase"])
        self.assertEqual("REMOTE_UNKNOWN", outcomes[0]["publication_error"])
        self.assertEqual(receipt_id, outcomes[0]["receipt_id"])

    def test_transient_publication_timeout_retries_to_exact_remote_receipt(self) -> None:
        receipt_id = self.complete_local()
        core = PublicationCore(self.root, "success")
        with (
            patch.object(
                worker,
                "_observe_remote_main",
                side_effect=[SubprocessTimeoutError("network timeout"), "b" * 40],
            ),
            patch.object(worker, "_is_ancestor", return_value=True),
        ):
            first = publish_pending(core, self.store)
            self.assertEqual("completed-local", first[0]["phase"])
            self.assertEqual("PUBLICATION_TIMEOUT", first[0]["publication_error"])
            self.assertIsNone(first[0]["remote_oid"])
            second = publish_pending(core, self.store)
        self.assertEqual("published-remote", second[0]["phase"])
        self.assertEqual("b" * 40, second[0]["remote_oid"])
        self.assertEqual(receipt_id, second[0]["receipt_id"])

    def test_resident_publisher_survives_timeout_and_observes_next_ref(self) -> None:
        receipt_id = self.complete_local()
        core = PublicationCore(self.root, "success")
        with (
            patch.object(
                worker,
                "_observe_remote_main",
                side_effect=[SubprocessTimeoutError("remote timeout"), "b" * 40],
            ),
            patch.object(worker, "_is_ancestor", return_value=True),
            patch(
                "tools.fast_receipt_worker.time.sleep",
                side_effect=[None, KeyboardInterrupt],
            ) as sleep,
            self.assertRaises(KeyboardInterrupt),
        ):
            serve_publication(core, self.store, poll_seconds=1.0)
        self.assertEqual(2, sleep.call_count)
        current = self.store.read(receipt_id)
        assert current is not None
        self.assertEqual("published-remote", current["phase"])
        self.assertEqual("b" * 40, current["remote_oid"])

    def test_timed_out_push_remains_local_without_false_ack(self) -> None:
        receipt_id = self.complete_local()
        core = PublicationCore(self.root, "success")
        original_run = core.run

        def timeout_push(
            command: list[str], *, check: bool = True
        ) -> subprocess.CompletedProcess[str]:
            if "push" in command:
                raise SubprocessTimeoutError("push timeout")
            return original_run(command, check=check)

        def relation(_core: Any, older: str, newer: str) -> bool:
            return (older, newer) in {
                ("a" * 40, "b" * 40),
                ("c" * 40, "b" * 40),
            }

        with (
            patch.object(worker, "_observe_remote_main", return_value="c" * 40),
            patch.object(worker, "_is_ancestor", side_effect=relation),
            patch.object(core, "run", side_effect=timeout_push),
        ):
            outcomes = publish_pending(core, self.store)
        self.assertEqual("completed-local", outcomes[0]["phase"])
        self.assertEqual("PUBLICATION_TIMEOUT", outcomes[0]["publication_error"])
        self.assertIsNone(outcomes[0]["remote_oid"])
        self.assertEqual(receipt_id, outcomes[0]["receipt_id"])

    def test_batch_timeout_preserves_prior_remote_ack_and_retries_remaining(self) -> None:
        first_id = self.complete_local()
        second = self.store.enqueue_heartbeat(
            key="worker-b:heartbeat:1",
            task="AR-0121",
            owner="worker-b",
            expected_revision=1,
            lease_minutes=20,
        )
        second_id = str(second["receipt_id"])
        self.store.claim_next()
        self.store.record_local_commit(second_id, "c" * 40, 2)
        core = PublicationCore(self.root, "success")
        with (
            patch.object(worker, "_observe_remote_main", return_value="b" * 40),
            patch.object(worker, "_publish_if_needed", return_value="b" * 40),
            patch.object(
                worker,
                "_is_ancestor",
                side_effect=[True, True, SubprocessTimeoutError("ancestry timeout")],
            ),
        ):
            outcomes = publish_pending(core, self.store)
        self.assertEqual(["published-remote", "completed-local"], [x["phase"] for x in outcomes])
        self.assertEqual(first_id, outcomes[0]["receipt_id"])
        self.assertEqual("b" * 40, outcomes[0]["remote_oid"])
        self.assertEqual(second_id, outcomes[1]["receipt_id"])
        self.assertEqual("PUBLICATION_TIMEOUT", outcomes[1]["publication_error"])
        self.assertIsNone(outcomes[1]["remote_oid"])
        with (
            patch.object(worker, "_observe_remote_main", return_value="b" * 40),
            patch.object(worker, "_is_ancestor", return_value=True),
        ):
            retried = publish_pending(core, self.store)
        self.assertEqual(1, len(retried))
        self.assertEqual("published-remote", retried[0]["phase"])
        self.assertEqual(second_id, retried[0]["receipt_id"])

    def test_diverged_remote_cannot_be_published(self) -> None:
        self.complete_local()
        core = PublicationCore(self.root, "success")

        def relation(_core: Any, older: str, newer: str) -> bool:
            return (older, newer) == ("a" * 40, "b" * 40)

        with (
            patch("tools.fast_receipt_worker._observe_remote_main", return_value="c" * 40),
            patch("tools.fast_receipt_worker._is_ancestor", side_effect=relation),
        ):
            outcomes = publish_pending(core, self.store)
        self.assertEqual("completed-local", outcomes[0]["phase"])
        self.assertEqual("REMOTE_NOT_CONTAINING_COMMIT", outcomes[0]["publication_error"])

    def test_replication_disabled_nonmain_and_moved_local_stay_unpublished(self) -> None:
        receipt_id = self.complete_local()
        core = PublicationCore(self.root, "success")
        with patch.object(core, "replication_enabled", return_value=False):
            disabled = publish_pending(core, self.store)
        self.assertEqual("REPLICATION_DISABLED", disabled[0]["publication_error"])
        with patch.object(worker, "_git", return_value="feature\n"):
            nonmain = publish_pending(core, self.store)
        self.assertEqual("STATE_BRANCH_NOT_MAIN", nonmain[0]["publication_error"])
        with (
            patch.object(worker, "_observe_remote_main", return_value="c" * 40),
            patch.object(worker, "_is_ancestor", return_value=False),
        ):
            moved = publish_pending(core, self.store)
        self.assertEqual("LOCAL_BRANCH_MOVED", moved[0]["publication_error"])
        self.assertEqual(receipt_id, moved[0]["receipt_id"])
        self.assertEqual("completed-local", moved[0]["phase"])

    def test_invalid_local_head_never_attempts_publication(self) -> None:
        self.complete_local()
        core = PublicationCore(self.root, "success")
        with (
            patch.object(worker, "_git", side_effect=["main", "not-an-oid"]),
            self.assertRaisesRegex(RuntimeError, "local publication head"),
        ):
            publish_pending(core, self.store)

    def test_observed_descendant_ref_publishes_without_push(self) -> None:
        self.complete_local()
        core = PublicationCore(self.root, "success")
        with (
            patch("tools.fast_receipt_worker._observe_remote_main", return_value="b" * 40),
            patch("tools.fast_receipt_worker._is_ancestor", return_value=True),
        ):
            outcomes = publish_pending(core, self.store)
        self.assertEqual("published-remote", outcomes[0]["phase"])
        self.assertEqual("b" * 40, outcomes[0]["remote_oid"])

    def test_fast_publisher_admits_captured_head_with_remote_lease(self) -> None:
        receipt_id = self.complete_local()
        pending = self.store.pending_publication()
        core = PublicationCore(self.root, "success")
        with (
            patch.object(worker, "_is_ancestor", side_effect=[True, False, True]),
            patch.object(worker, "_observe_remote_main", return_value="b" * 40),
            patch.object(core, "run", wraps=core.run) as run,
        ):
            observed = worker._publish_if_needed(core, self.store, pending, "b" * 40, "c" * 40)
        self.assertEqual("b" * 40, observed)
        job = self.store.connection.execute(
            "SELECT * FROM publication_jobs WHERE candidate_oid=?", ("b" * 40,)
        ).fetchone()
        assert job is not None
        self.assertEqual("published", job["phase"])
        self.assertEqual("c" * 40, job["expected_remote_oid"])
        push = next(call.args[0] for call in run.call_args_list if "push" in call.args[0])
        self.assertIn("--force-with-lease=refs/heads/main:" + "c" * 40, push)
        self.assertEqual(receipt_id, pending[0]["receipt_id"])

    def test_descendant_observation_terminally_rejects_exact_job(self) -> None:
        core = PublicationCore(self.root, "success")
        admitted = self.store.admit_publication(
            key="publisher-a:1", candidate_oid="a" * 40, expected_remote_oid="b" * 40
        )
        job_id = str(admitted["job_id"])
        lease = "1" * 32
        self.store.claim_publication(job_id, lease=lease)
        with (
            patch("tools.fast_receipt_worker._observe_remote_main", return_value="c" * 40),
            patch("tools.fast_receipt_worker._is_ancestor", return_value=True),
        ):
            observed = worker._record_admitted_push_observation(
                core, self.store, job_id, lease, "a" * 40, "PUSH_UNKNOWN"
            )
        self.assertEqual("c" * 40, observed)
        job = self.store.read_publication(job_id)
        assert job is not None
        self.assertEqual("rejected", job["phase"])
        self.assertEqual("REMOTE_ADVANCED", job["error_code"])
        self.assertEqual("c" * 40, job["observed_remote_oid"])

    def test_remote_observation_sweeps_historical_expired_publications(self) -> None:
        admitted = self.store.admit_publication(
            key="publisher-a:1", candidate_oid="a" * 40, expected_remote_oid="b" * 40
        )
        job_id = str(admitted["job_id"])
        self.store.claim_publication(job_id, lease="1" * 32)
        self.store.connection.execute(
            "UPDATE publication_jobs SET publisher_lease_expires='2000-01-01T00:00:00.000Z' "
            "WHERE job_id=?",
            (job_id,),
        )
        worker._recover_outstanding_publications(self.store, "d" * 40, "c" * 40)
        job = self.store.read_publication(job_id)
        assert job is not None
        self.assertEqual("rejected", job["phase"])
        self.assertEqual("REMOTE_BASE_CHANGED", job["error_code"])

    def test_superseded_requeued_job_is_terminal_on_a_no_receipt_cycle(self) -> None:
        admitted = self.store.admit_publication(
            key="publisher-a:1", candidate_oid="a" * 40, expected_remote_oid="b" * 40
        )
        job_id = str(admitted["job_id"])
        self.store.claim_publication(job_id, lease="1" * 32)
        self.store.connection.execute(
            "UPDATE publication_jobs SET publisher_lease_expires='2000-01-01T00:00:00.000Z' "
            "WHERE job_id=?",
            (job_id,),
        )
        worker._recover_outstanding_publications(self.store, "a" * 40, "b" * 40)
        requeued = self.store.read_publication(job_id)
        assert requeued is not None
        self.assertEqual("queued", requeued["phase"])
        worker._recover_outstanding_publications(self.store, "c" * 40, "b" * 40)
        job = self.store.read_publication(job_id)
        assert job is not None
        self.assertEqual("rejected", job["phase"])
        self.assertEqual("LOCAL_HEAD_SUPERSEDED", job["error_code"])

    def test_publish_admission_terminal_and_lost_claim_paths_return_remote(self) -> None:
        core = PublicationCore(self.root, "success")
        pending = [{"commit_oid": "a" * 40}]
        for phase in ("published", "rejected"):
            store = Mock()
            store.admit_publication.return_value = {"job_id": "1" * 32, "phase": phase}
            with patch("tools.fast_receipt_worker._is_ancestor", side_effect=[True, False, True]):
                self.assertEqual(
                    "b" * 40,
                    worker._publish_if_needed(core, store, pending, "a" * 40, "b" * 40),
                )
            store.claim_publication.assert_not_called()
        store = Mock()
        store.admit_publication.return_value = {"job_id": "1" * 32, "phase": "queued"}
        store.claim_publication.return_value = None
        with patch("tools.fast_receipt_worker._is_ancestor", side_effect=[True, False, True]):
            self.assertEqual(
                "b" * 40,
                worker._publish_if_needed(core, store, pending, "a" * 40, "b" * 40),
            )
        store.claim_publication.assert_called_once()

    def test_publish_active_recovery_and_outstanding_race_policy(self) -> None:
        core = PublicationCore(self.root, "success")
        pending = [{"commit_oid": "a" * 40}]
        store = Mock()
        store.admit_publication.return_value = {"job_id": "1" * 32, "phase": "ambiguous"}
        store.recover_publication.side_effect = RuntimeError("publication lease is still active")
        with patch("tools.fast_receipt_worker._is_ancestor", side_effect=[True, False, True]):
            self.assertEqual(
                "b" * 40,
                worker._publish_if_needed(core, store, pending, "a" * 40, "b" * 40),
            )
        store.claim_publication.assert_not_called()
        store = Mock()
        store.recoverable_publications.return_value = [
            {"job_id": "1" * 32, "phase": "queued", "candidate_oid": "a" * 40},
            {"job_id": "2" * 32, "phase": "ambiguous", "candidate_oid": "b" * 40},
        ]
        store.recover_publication.side_effect = RuntimeError(
            "publication job changed while recovering"
        )
        worker._recover_outstanding_publications(store, "a" * 40, "c" * 40)
        store.resolve_superseded_publication.assert_not_called()
        with self.assertRaisesRegex(RuntimeError, "unexpected"):
            store.recover_publication.side_effect = RuntimeError("unexpected")
            worker._recover_outstanding_publications(store, "z" * 40, "c" * 40)

    def test_publish_remote_unknown_and_timeout_integrity_fail_closed(self) -> None:
        core = PublicationCore(self.root, "success")
        pending = [{"receipt_id": "1" * 32}]
        store = Mock()
        store.record_publication_failure.return_value = {"phase": "completed-local"}
        with patch("tools.fast_receipt_worker._observe_remote_main", return_value=None):
            self.assertEqual(
                [{"phase": "completed-local"}], worker._publish_selected(core, store, pending)
            )
        store.pending_publication.return_value = pending
        store.read.return_value = None
        with (
            patch.object(worker, "_require_bound_store"),
            patch.object(
                worker, "_publish_selected", side_effect=SubprocessTimeoutError("timeout")
            ),
            self.assertRaisesRegex(RuntimeError, "pending receipt disappeared"),
        ):
            publish_pending(core, store)
        store.read.return_value = {"phase": "rejected"}
        with (
            patch.object(worker, "_require_bound_store"),
            patch.object(
                worker, "_publish_selected", side_effect=SubprocessTimeoutError("timeout")
            ),
            self.assertRaisesRegex(RuntimeError, "invalid phase"),
        ):
            publish_pending(core, store)


if __name__ == "__main__":
    unittest.main()
