# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Negative and independent-process transport checks for opt-in receipts."""

from __future__ import annotations

import contextlib
import io
import json
import os
import queue
import socket
import sqlite3
import struct
import tempfile
import threading
import time
import unittest
import uuid
from pathlib import Path
from typing import cast
from unittest.mock import MagicMock, patch

from tools.fast_receipt_socket import (
    _client_common_dir,
    _fast_request,
    _handle,
    _read_line,
    _require_request,
    _safe_socket,
    _send_reply,
    _socket_path,
    socket_service,
    try_socket_fast,
)
from tools.fast_receipts import ReceiptStore


class FakeBoundCore:
    def __init__(self, root: Path, project_id: str) -> None:
        self.root = root
        self.project_id = project_id
        self.reject_caller = False
        self.scan_count = 0

    def coordinator_lock_path(self) -> Path:
        return self.root / "state.lock"

    def assert_project_binding(self, caller_cwd: Path | None = None) -> None:
        if self.reject_caller or caller_cwd != Path.cwd().resolve():
            raise RuntimeError("foreign fast receipt caller")

    def backend_selection(self) -> dict[str, str]:
        return {"backend": "git"}

    def project_binding(self) -> dict[str, str]:
        return {"project_id": self.project_id}

    def config(self) -> dict[str, str]:
        return {"projects_root": "/fixture", "product_worktree": "product"}

    def project_scan(self) -> dict[str, object]:
        self.scan_count += 1
        return {
            "remote_main": "a" * 40,
            "origin_main": "b" * 40,
            "primary_head": "c" * 40,
            "worktrees": [],
            "prs": [],
            "runs": [],
        }


class FastReceiptSocketTests(unittest.TestCase):
    def setUp(self) -> None:
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.private = Path(self.directory.name) / "handoffctl"
        self.private.mkdir(mode=0o700)
        self.path = self.private / "fast-receipts.sock"
        self.core = FakeBoundCore(self.private, str(uuid.uuid4()))
        self.argv = [
            "fast",
            "heartbeat",
            "AR-0120",
            "--owner",
            "worker-a",
            "--expected-revision",
            "2",
            "--lease-minutes",
            "20",
            "--key",
            "worker-a:heartbeat:2",
        ]

    def test_canonical_request_and_malformed_args_fall_back_to_parser(self) -> None:
        request = _fast_request(self.argv)
        assert request is not None
        self.assertEqual("heartbeat", request["action"])
        self.assertEqual(2, request["expected_revision"])
        self.assertEqual(20, request["lease_minutes"])
        self.assertIsNone(_fast_request([*self.argv, "--owner", "duplicate"]))
        self.assertIsNone(_fast_request(["fast", "heartbeat", "AR-0120", "--owner"]))
        self.assertIsNone(_fast_request(["fast", "worker", "--serve"]))
        self.assertEqual(
            {"protocol": 1, "action": "receipt", "receipt_id": "a" * 32},
            _fast_request(["fast", "receipt", "a" * 32]),
        )
        self.assertEqual(
            {"protocol": 1, "action": "observe", "max_age_seconds": 30},
            _fast_request(["fast", "observe", "--max-age-seconds", "30"]),
        )
        self.assertEqual(
            {
                "protocol": 1,
                "action": "promote",
                "task": "AR-0120",
                "expected_revision": 2,
                "note": "Open",
                "key": "worker-a:promote:2",
            },
            _fast_request(
                [
                    "fast",
                    "promote",
                    "AR-0120",
                    "--expected-revision",
                    "2",
                    "--note",
                    "Open",
                    "--key",
                    "worker-a:promote:2",
                ]
            ),
        )
        self.assertEqual(
            {
                "protocol": 1,
                "action": "update",
                "task": "AR-0120",
                "owner": "worker-a",
                "expected_revision": 2,
                "changes": {"priority": "P1", "next_action": "Run tests."},
                "note": "Refined plan.",
                "key": "worker-a:update:2",
            },
            _fast_request(
                [
                    "fast",
                    "update",
                    "AR-0120",
                    "--owner",
                    "worker-a",
                    "--expected-revision",
                    "2",
                    "--priority",
                    "P1",
                    "--next-action",
                    "Run tests.",
                    "--note",
                    "Refined plan.",
                    "--key",
                    "worker-a:update:2",
                ]
            ),
        )

    def test_claim_identity_is_forwarded_only_as_a_complete_pair(self) -> None:
        argv = [
            "fast",
            "claim",
            "AR-0120",
            "--owner",
            "worker-a",
            "--expected-revision",
            "2",
            "--worker-pid",
            "123",
            "--worker-start-time",
            "456",
            "--key",
            "worker-a:claim:2",
        ]
        request = _fast_request(argv)
        self.assertIsNotNone(request)
        assert request is not None
        self.assertEqual(123, request["worker_pid"])
        self.assertEqual(456, request["worker_start_time"])
        self.assertEqual(request, _require_request(request))
        self.assertIsNone(_fast_request(argv[:-4] + argv[-2:]))

    def test_git_common_directory_resolves_main_and_linked_worktree(self) -> None:
        root = Path(self.directory.name)
        marker = root / ".git"
        marker.mkdir()
        self.assertEqual(marker.resolve(), _client_common_dir(root))
        marker.rmdir()
        gitdir = root / "separate" / "worktrees" / "worker"
        gitdir.mkdir(parents=True)
        (gitdir / "commondir").write_text("../..\n")
        marker.write_text(f"gitdir: {gitdir}\n")
        self.assertEqual((root / "separate").resolve(), _client_common_dir(root))
        marker.write_text("not a gitdir")
        self.assertIsNone(_client_common_dir(root))

    def test_git_metadata_rejects_symlink_and_malformed_common_directory(self) -> None:
        root = Path(self.directory.name)
        marker = root / ".git"
        self.assertIsNone(_client_common_dir(root))
        marker.symlink_to(self.private)
        with self.assertRaisesRegex(RuntimeError, "symlink"):
            _client_common_dir(root)
        marker.unlink()
        gitdir = root / "relative" / "worktrees" / "one"
        gitdir.mkdir(parents=True)
        marker.write_text("gitdir: relative/worktrees/one\n")
        self.assertEqual(gitdir.resolve(), _client_common_dir(root))
        (gitdir / "commondir").write_text("\n")
        self.assertIsNone(_client_common_dir(root))
        (gitdir / "commondir").write_text(str(self.private) + "\n")
        self.assertEqual(self.private.resolve(), _client_common_dir(root))

    def test_fast_parser_rejects_unknown_missing_and_noninteger_options(self) -> None:
        self.assertIsNone(_fast_request(["fast", "heartbeat", "--bad", *self.argv[3:]]))
        self.assertIsNone(_fast_request([*self.argv, "--unknown", "value"]))
        self.assertIsNone(_fast_request(self.argv[:-2]))
        self.assertIsNone(_fast_request(["fast", "observe", "--max-age-seconds", "301"]))
        invalid = list(self.argv)
        invalid[6] = "not-a-revision"
        self.assertIsNone(_fast_request(invalid))
        invalid = list(self.argv)
        invalid[8] = "not-a-lease"
        self.assertIsNone(_fast_request(invalid))
        self.assertIsNone(
            _fast_request(
                [
                    "fast",
                    "promote",
                    "AR-0120",
                    "--expected-revision",
                    "not-a-revision",
                    "--note",
                    "Open",
                    "--key",
                    "worker-a:promote:2",
                ]
            )
        )
        self.assertIsNone(
            _fast_request(
                [
                    "fast",
                    "update",
                    "AR-0120",
                    "--owner",
                    "worker-a",
                    "--expected-revision",
                    "2",
                    "--note",
                    "no metadata",
                    "--key",
                    "worker-a:update:2",
                ]
            )
        )
        self.assertIsNone(
            _fast_request(
                [
                    "fast",
                    "promote",
                    "-AR-0120",
                    "--expected-revision",
                    "2",
                    "--note",
                    "Open",
                    "--key",
                    "worker-a:promote:2",
                ]
            )
        )

    def test_bounded_line_and_protocol_reject_malformed_messages(self) -> None:
        reader, writer = socket.socketpair()
        with reader, writer:
            writer.sendall(b"ok\nextra")
            with self.assertRaisesRegex(RuntimeError, "malformed"):
                _read_line(reader, 16)
        reader, writer = socket.socketpair()
        with reader, writer:
            writer.sendall(b"12345")
            with self.assertRaisesRegex(RuntimeError, "too large"):
                _read_line(reader, 4)
        reader, writer = socket.socketpair()
        with reader, writer, patch("tools.fast_receipt_socket._MAX_REPLY", 128):
            _send_reply(writer, {"ok": {"observation": "x" * 256}})
            reply = json.loads(_read_line(reader, 128))
        self.assertEqual(
            "FAST_OBSERVATION_REPLY_TOO_LARGE: use direct fast observe", reply["error"]
        )
        with self.assertRaisesRegex(RuntimeError, "lookup"):
            _require_request({"protocol": 1, "action": "receipt", "receipt_id": "a", "extra": 1})
        with self.assertRaisesRegex(RuntimeError, "heartbeat request"):
            _require_request({"protocol": 1, "action": "heartbeat", "task": "AR-0120"})
        with self.assertRaisesRegex(RuntimeError, "promote request fields"):
            _require_request(
                {
                    "protocol": 1,
                    "action": "promote",
                    "task": "AR-0120",
                    "expected_revision": True,
                    "note": "Open",
                    "key": "worker-a:promote:2",
                }
            )

    def test_parser_and_validator_reject_ambiguous_fast_request_shapes(self) -> None:
        """Duplicate, incomplete, and unknown wire fields never enter the receipt queue."""
        self.assertIsNone(
            _fast_request(
                [
                    "fast",
                    "update",
                    "AR-0120",
                    "--owner",
                    "worker-a",
                    "--expected-revision",
                    "2",
                    "--note",
                    "only metadata",
                    "--key",
                    "key",
                ]
            )
        )
        self.assertIsNone(
            _fast_request(
                [
                    "fast",
                    "update",
                    "AR-0120",
                    "--owner",
                    "worker-a",
                    "--owner",
                    "worker-b",
                    "--expected-revision",
                    "2",
                    "--priority",
                    "P1",
                    "--note",
                    "note",
                    "--key",
                    "key",
                ]
            )
        )
        self.assertIsNone(
            _fast_request(
                [
                    "fast",
                    "claim",
                    "AR-0120",
                    "--owner",
                    "worker-a",
                    "--expected-revision",
                    "invalid",
                    "--lease-minutes",
                    "20",
                    "--key",
                    "key",
                ]
            )
        )
        with self.assertRaisesRegex(RuntimeError, "observation request"):
            _require_request({"protocol": 1, "action": "observe", "max_age_seconds": -1})
        with self.assertRaisesRegex(RuntimeError, "claim request"):
            _require_request(
                {
                    "protocol": 1,
                    "action": "claim",
                    "task": "AR-0120",
                    "owner": "worker-a",
                    "expected_revision": 2,
                    "lease_minutes": 20,
                    "key": "key",
                    "worker_pid": 0,
                    "worker_start_time": 1,
                }
            )
        with self.assertRaisesRegex(RuntimeError, "unknown"):
            _require_request({"protocol": 1, "action": "erase"})

    def test_transport_parser_rejects_each_unrepresentable_command_shape(self) -> None:
        """The warm socket is optional only when argv cannot safely represent one request."""
        self.assertIsNone(
            _fast_request(
                [
                    "fast",
                    "promote",
                    "AR-0120",
                    "--expected-revision",
                    "2",
                    "--note",
                    "open",
                    "--unknown",
                    "key",
                ]
            )
        )
        self.assertIsNone(
            _fast_request(
                [
                    "fast",
                    "update",
                    "-AR-0120",
                    "--owner",
                    "worker-a",
                    "--expected-revision",
                    "2",
                    "--priority",
                    "P1",
                    "--note",
                    "note",
                    "--key",
                    "key",
                ]
            )
        )
        self.assertIsNone(
            _fast_request(
                [
                    "fast",
                    "update",
                    "AR-0120",
                    "--owner",
                    "worker-a",
                    "--expected-revision",
                    "invalid",
                    "--priority",
                    "P1",
                    "--note",
                    "note",
                    "--key",
                    "key",
                ]
            )
        )
        self.assertIsNone(try_socket_fast(["ordinary", "command"]))

    def test_socket_path_requires_a_resolved_git_common_directory(self) -> None:
        """A client without Git metadata cannot target an arbitrary local socket."""
        root = Path("/fixture-root")
        with patch("tools.fast_receipt_socket._client_common_dir", return_value=None):
            self.assertIsNone(_socket_path(root))
        common = Path("/fixture-common")
        with patch("tools.fast_receipt_socket._client_common_dir", return_value=common):
            self.assertEqual(common / "handoffctl" / "fast-receipts.sock", _socket_path(root))

    def test_wire_validator_rejects_extra_and_wrong_typed_fields_before_submission(self) -> None:
        """Unknown fields and wrong scalar types cannot select a queue operation."""
        invalid = (
            (
                {"protocol": 1, "action": "observe", "max_age_seconds": 1, "extra": True},
                "observation",
            ),
            (
                {
                    "protocol": 1,
                    "action": "claim",
                    "task": "AR-0120",
                    "owner": "worker-a",
                    "expected_revision": 2,
                    "lease_minutes": 20,
                    "key": "key",
                    "extra": True,
                },
                "claim request",
            ),
            (
                {
                    "protocol": 1,
                    "action": "promote",
                    "task": "AR-0120",
                    "expected_revision": 2,
                    "note": "open",
                    "key": "key",
                    "extra": True,
                },
                "promote request",
            ),
            (
                {
                    "protocol": 1,
                    "action": "update",
                    "task": "AR-0120",
                    "owner": "worker-a",
                    "expected_revision": "2",
                    "changes": {"priority": "P1"},
                    "note": "open",
                    "key": "key",
                },
                "update request fields",
            ),
            (
                {
                    "protocol": 1,
                    "action": "update",
                    "task": "AR-0120",
                    "owner": "worker-a",
                    "expected_revision": 2,
                    "changes": {"priority": "P1"},
                    "note": "open",
                    "key": "key",
                    "extra": True,
                },
                "update request",
            ),
        )
        for request, diagnostic in invalid:
            with self.subTest(request=request), self.assertRaisesRegex(RuntimeError, diagnostic):
                _require_request(request)

    def test_client_rejects_invalid_reply_and_uses_fallback_for_oversized_observation(self) -> None:
        """A malformed service reply cannot be mistaken for a queued durable receipt."""
        with (
            patch("tools.fast_receipt_socket._socket_path", return_value=self.path),
            patch("tools.fast_receipt_socket._safe_socket", return_value=True),
            patch("tools.fast_receipt_socket.socket.socket") as socket_type,
        ):
            peer = socket_type.return_value.__enter__.return_value
            peer.getsockopt.return_value = b""
            with (
                patch(
                    "tools.fast_receipt_socket._read_line", return_value=b'{"ok":1,"error":"bad"}'
                ),
                self.assertRaisesRegex(RuntimeError, "response is invalid"),
            ):
                try_socket_fast(self.argv)
            with (
                patch(
                    "tools.fast_receipt_socket._read_line",
                    side_effect=RuntimeError("fast receipt socket message is too large"),
                ),
                patch("tools.fast_receipt_socket._fallback_or_error", return_value=73) as fallback,
            ):
                self.assertEqual(73, try_socket_fast(["fast", "observe", "--max-age-seconds", "1"]))
            fallback.assert_called_once_with()

    def test_client_reraises_unclassified_transport_runtime_error(self) -> None:
        """Only oversized observations may fall back; other protocol faults remain visible."""
        with (
            patch("tools.fast_receipt_socket._socket_path", return_value=self.path),
            patch("tools.fast_receipt_socket._safe_socket", return_value=True),
            patch("tools.fast_receipt_socket.socket.socket") as socket_type,
            patch("tools.fast_receipt_socket._read_line", side_effect=RuntimeError("bad frame")),
        ):
            socket_type.return_value.__enter__.return_value.getsockopt.return_value = b""
            with self.assertRaisesRegex(RuntimeError, "bad frame"):
                try_socket_fast(self.argv)

    def test_handle_replies_to_unauthorized_peer_but_preserves_eof_for_timeout(self) -> None:
        """Hostile peers get no authority effect; uncertain timeouts force client retry."""
        hostile = MagicMock()
        hostile.__enter__.return_value = hostile
        hostile.getsockopt.return_value = (0).to_bytes(12, "little")
        _handle(self.core, hostile, lambda _request: self.fail("must not submit"), b"{}")
        reply = json.loads(hostile.sendall.call_args.args[0])
        self.assertIn("not authorized", reply["error"])

        timeout = MagicMock()
        timeout.__enter__.return_value = timeout
        timeout.getsockopt.return_value = struct.pack("3i", 1, os.geteuid(), 0)
        with patch("tools.fast_receipt_socket.Path.readlink", return_value=Path.cwd()):
            _handle(
                self.core,
                timeout,
                lambda _request: (_ for _ in ()).throw(TimeoutError()),
                json.dumps({"protocol": 1, "action": "observe", "max_age_seconds": 1}).encode(),
            )
        timeout.sendall.assert_not_called()
        with self.assertRaisesRegex(RuntimeError, "update request fields"):
            _require_request(
                {
                    "protocol": 1,
                    "action": "update",
                    "task": "AR-0120",
                    "owner": "worker-a",
                    "expected_revision": 2,
                    "changes": {"owner": "injected"},
                    "note": "Refined.",
                    "key": "worker-a:update:2",
                }
            )
        with self.assertRaisesRegex(RuntimeError, "update request fields"):
            _require_request(
                {
                    "protocol": 1,
                    "action": "update",
                    "task": "AR-0120",
                    "owner": "worker-a",
                    "expected_revision": 2,
                    "changes": {"next_action": "line\nbreak"},
                    "note": "Refined.",
                    "key": "worker-a:update:2",
                }
            )

    def test_unsafe_socket_symlink_is_not_followed(self) -> None:
        target = self.private / "target"
        target.write_text("not a socket")
        self.path.symlink_to(target)
        with self.assertRaisesRegex(RuntimeError, "unsafe"):
            _safe_socket(self.path)
        with self.assertRaisesRegex(RuntimeError, "unsafe"), socket_service(self.core):
            pass
        self.assertTrue(self.path.is_symlink())

    def test_socket_path_requires_private_parent_and_actual_socket(self) -> None:
        target = self.private / "not-a-socket"
        target.write_text("x")
        with self.assertRaisesRegex(RuntimeError, "unsafe"):
            _safe_socket(target)
        with socket_service(self.core):
            self.private.chmod(0o755)
            try:
                with self.assertRaisesRegex(RuntimeError, "unsafe"):
                    _safe_socket(self.path)
            finally:
                self.private.chmod(0o700)

    def test_bound_service_returns_only_durable_queued_and_read_receipts(self) -> None:
        with (
            socket_service(self.core),
            patch("tools.fast_receipt_socket._socket_path", return_value=self.path),
        ):
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                self.assertEqual(0, try_socket_fast(self.argv))
            queued = json.loads(output.getvalue())
            self.assertEqual("queued-local", queued["phase"])
            self.assertIsNone(queued["commit_oid"])
            receipt_id = queued["receipt_id"]
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                self.assertEqual(0, try_socket_fast(["fast", "receipt", receipt_id]))
            self.assertEqual(queued, json.loads(output.getvalue()))
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(0, try_socket_fast(self.argv))
            self.assertEqual(
                1,
                self._intent_count(),
            )
        self.assertFalse(self.path.exists())

    def test_bound_service_returns_explicit_cached_observation_without_receipt_write(self) -> None:
        argv = ["fast", "observe", "--max-age-seconds", "30"]
        with (
            socket_service(self.core),
            patch("tools.fast_receipt_socket._socket_path", return_value=self.path),
            contextlib.redirect_stdout(io.StringIO()) as output,
        ):
            self.assertEqual(0, try_socket_fast(argv))
            first = json.loads(output.getvalue())
            output.seek(0)
            output.truncate(0)
            self.assertEqual(0, try_socket_fast(argv))
            second = json.loads(output.getvalue())
        self.assertEqual("cached-observation-v1", first["contract"])
        self.assertFalse(first["strict_equivalent"])
        self.assertEqual("fresh-scan", first["freshness"])
        self.assertEqual("bounded-cache", second["freshness"])
        self.assertEqual(first["observation_sha256"], second["observation_sha256"])
        self.assertEqual(1, self.core.scan_count)
        self.assertEqual(0, self._intent_count())

    def test_oversized_observation_returns_bounded_direct_fallback_signal(self) -> None:
        argv = ["fast", "observe", "--max-age-seconds", "30"]
        oversized = {
            "remote_main": "a" * 40,
            "origin_main": "b" * 40,
            "primary_head": "c" * 40,
            "worktrees": [{"name": "x" * 512}],
            "prs": [],
            "runs": [],
        }
        with (
            patch.object(self.core, "project_scan", return_value=oversized),
            patch("tools.fast_receipt_socket._MAX_REPLY", 128),
            socket_service(self.core),
            patch("tools.fast_receipt_socket._socket_path", return_value=self.path),
            contextlib.redirect_stderr(io.StringIO()) as errors,
        ):
            self.assertIsNone(try_socket_fast(argv))
        self.assertEqual("", errors.getvalue())

    def test_sixty_four_observation_callers_share_one_cold_scan(self) -> None:
        request = (
            json.dumps({"protocol": 1, "action": "observe", "max_age_seconds": 0}).encode() + b"\n"
        )
        started = threading.Event()
        release = threading.Event()
        original = self.core.project_scan

        def slow_scan() -> dict[str, object]:
            started.set()
            self.assertTrue(release.wait(2))
            return original()

        replies: list[dict[str, object]] = []
        errors: list[BaseException] = []

        def observe() -> None:
            try:
                with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as peer:
                    peer.settimeout(5)
                    peer.connect(str(self.path))
                    peer.sendall(request)
                    replies.append(json.loads(_read_line(peer, 131072)))
            except BaseException as error:  # pragma: no cover - asserted below
                errors.append(error)

        with (
            patch.object(self.core, "project_scan", side_effect=slow_scan),
            socket_service(self.core),
            patch("tools.fast_receipt_socket._socket_path", return_value=self.path),
        ):
            callers = [threading.Thread(target=observe) for _ in range(64)]
            for caller in callers:
                caller.start()
            self.assertTrue(started.wait(1))
            # Allow all admitted calls to reach the 64-handler pool before
            # completing the single zero-age generation.
            time.sleep(0.1)
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                self.assertEqual(0, try_socket_fast(self.argv))
            self.assertEqual("queued-local", json.loads(output.getvalue())["phase"])
            release.set()
            for caller in callers:
                caller.join(5)
        self.assertFalse(errors)
        self.assertEqual(64, len(replies))
        self.assertEqual(1, self.core.scan_count)
        observations = [cast(dict[str, object], reply["ok"]) for reply in replies]
        self.assertEqual(
            {"cached-observation-v1"}, {str(reply["contract"]) for reply in observations}
        )

    def test_bound_service_queues_typed_promote_receipt(self) -> None:
        argv = [
            "fast",
            "promote",
            "AR-0120",
            "--expected-revision",
            "2",
            "--note",
            "Dependencies verified.",
            "--key",
            "worker-a:promote:2",
        ]
        with (
            socket_service(self.core),
            patch("tools.fast_receipt_socket._socket_path", return_value=self.path),
            contextlib.redirect_stdout(io.StringIO()) as output,
        ):
            self.assertEqual(0, try_socket_fast(argv))
            queued = json.loads(output.getvalue())
            self.assertEqual("promote", queued["operation"])
            self.assertEqual("queued-local", queued["phase"])
            self.assertEqual(1, self._intent_count())

    def test_bound_service_accepts_largest_valid_update_frame(self) -> None:
        argv = [
            "fast",
            "update",
            "AR-0120",
            "--owner",
            "worker-a",
            "--expected-revision",
            "2",
            "--summary",
            "😀" * 4000,
            "--next-action",
            "😀" * 1024,
            "--note",
            "😀" * 4096,
            "--key",
            "worker-a:update:largest",
        ]
        with (
            socket_service(self.core),
            patch("tools.fast_receipt_socket._socket_path", return_value=self.path),
            patch.dict(os.environ, {"HANDOFFCTL_FAST_REQUIRE_SOCKET": "1"}),
            contextlib.redirect_stdout(io.StringIO()) as output,
        ):
            self.assertEqual(0, try_socket_fast(argv))
            queued = json.loads(output.getvalue())
            self.assertEqual("update", queued["operation"])
            self.assertEqual("queued-local", queued["phase"])
            self.assertEqual(1, self._intent_count())

    def _intent_count(self) -> int:
        import sqlite3

        with contextlib.closing(
            sqlite3.connect(self.private / "fast-receipts.sqlite3")
        ) as connection:
            return int(connection.execute("SELECT count(*) FROM intents").fetchone()[0])

    def test_foreign_caller_rejects_before_queue_effect(self) -> None:
        self.core.reject_caller = True
        with (
            socket_service(self.core),
            patch("tools.fast_receipt_socket._socket_path", return_value=self.path),
        ):
            error = io.StringIO()
            with contextlib.redirect_stderr(error):
                self.assertEqual(1, try_socket_fast(self.argv))
            self.assertIn("foreign fast receipt caller", error.getvalue())
        self.assertEqual(0, self._intent_count())

    def test_non_git_peer_and_saturated_writer_reject_without_intent(self) -> None:
        with (
            socket_service(self.core),
            patch("tools.fast_receipt_socket._socket_path", return_value=self.path),
        ):
            with (
                patch.object(self.core, "backend_selection", return_value={"backend": "sqlite"}),
                contextlib.redirect_stderr(io.StringIO()) as error,
            ):
                self.assertEqual(1, try_socket_fast(self.argv))
            self.assertIn("require Git authority", error.getvalue())
            with (
                patch.object(queue.Queue, "put", side_effect=queue.Full),
                contextlib.redirect_stderr(io.StringIO()) as error,
            ):
                self.assertEqual(1, try_socket_fast(self.argv))
            self.assertIn("saturated", error.getvalue())
            self.assertEqual(0, self._intent_count())

    def test_writer_startup_failure_never_publishes_socket(self) -> None:
        with (
            patch("tools.fast_receipts.ReceiptStore", side_effect=RuntimeError("injected")),
            self.assertRaisesRegex(RuntimeError, "could not start"),
            socket_service(self.core),
        ):
            pass
        self.assertFalse(self.path.exists())

    def test_stale_owned_socket_is_replaced_but_unsafe_socket_fails(self) -> None:
        with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as stale:
            stale.bind(str(self.path))
            self.path.chmod(0o600)
        with socket_service(self.core):
            self.assertTrue(_safe_socket(self.path))
        self.assertFalse(self.path.exists())

    def test_active_service_cannot_be_replaced(self) -> None:
        with socket_service(self.core):
            with self.assertRaisesRegex(RuntimeError, "already active"), socket_service(self.core):
                pass
            self.assertTrue(_safe_socket(self.path))

    def test_unknown_receipt_and_malformed_protocol_do_not_write_intents(self) -> None:
        with socket_service(self.core):
            for request, diagnostic in (
                ({"protocol": 2, "action": "receipt", "receipt_id": "x"}, "protocol"),
                ({"protocol": 1, "action": "receipt", "receipt_id": "a" * 32}, "unknown"),
                ({"protocol": 1, "action": "unknown"}, "action"),
                (
                    {
                        "protocol": 1,
                        "action": "heartbeat",
                        "task": "AR-0120",
                        "owner": "worker-a",
                        "expected_revision": True,
                        "lease_minutes": 20,
                        "key": "bad",
                    },
                    "fields",
                ),
            ):
                with (
                    self.subTest(request=request),
                    socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as peer,
                ):
                    peer.settimeout(2)
                    peer.connect(str(self.path))
                    peer.sendall(json.dumps(request).encode() + b"\n")
                    reply = json.loads(peer.recv(4096))
                    self.assertIn(diagnostic, reply["error"])
            self.assertEqual(0, self._intent_count())

    def test_socket_absence_and_invalid_cli_shape_use_strict_fallback(self) -> None:
        with patch("tools.fast_receipt_socket._socket_path", return_value=self.path):
            self.assertIsNone(try_socket_fast(self.argv))
        self.assertIsNone(try_socket_fast(["fast", "heartbeat", "AR-0120"]))

    def test_required_socket_rejects_absence_and_unrecognized_fast_shape(self) -> None:
        with (
            patch.dict(os.environ, {"HANDOFFCTL_FAST_REQUIRE_SOCKET": "1"}),
            patch("tools.fast_receipt_socket._socket_path", return_value=self.path),
            contextlib.redirect_stderr(io.StringIO()) as error,
        ):
            self.assertEqual(1, try_socket_fast(self.argv))
            self.assertEqual(1, try_socket_fast(["fast", "heartbeat", "AR-0120"]))
        self.assertIn("required but unavailable", error.getvalue())

    def test_dead_writer_forces_same_key_fallback_not_terminal_error(self) -> None:
        with (
            socket_service(self.core),
            patch("tools.fast_receipt_socket._socket_path", return_value=self.path),
        ):
            writer = next(
                thread for thread in threading.enumerate() if thread.name == "fast-receipt-writer"
            )
            with patch.object(writer, "is_alive", return_value=False):
                self.assertIsNone(try_socket_fast(self.argv))
                with (
                    patch.dict(os.environ, {"HANDOFFCTL_FAST_REQUIRE_SOCKET": "1"}),
                    contextlib.redirect_stderr(io.StringIO()) as error,
                ):
                    self.assertEqual(1, try_socket_fast(self.argv))
                self.assertIn("required but unavailable", error.getvalue())
            self.assertEqual(0, self._intent_count())

    def test_disconnect_after_durable_enqueue_uses_same_key_fallback(self) -> None:
        with (
            socket_service(self.core),
            patch("tools.fast_receipt_socket._socket_path", return_value=self.path),
            patch(
                "tools.fast_receipt_socket.public_receipt",
                side_effect=sqlite3.OperationalError("injected post-enqueue disconnect"),
            ),
        ):
            self.assertIsNone(try_socket_fast(self.argv))
            self.assertEqual(1, self._intent_count())
            with ReceiptStore(
                self.private / "fast-receipts.sqlite3", self.core.project_id
            ) as store:
                original = store.connection.execute(
                    "SELECT receipt_id FROM intents WHERE idempotency_key=?",
                    ("worker-a:heartbeat:2",),
                ).fetchone()
                assert original is not None
                retried = store.enqueue_heartbeat(
                    key="worker-a:heartbeat:2",
                    task="AR-0120",
                    owner="worker-a",
                    expected_revision=2,
                    lease_minutes=20,
                )
                self.assertEqual(original["receipt_id"], retried["receipt_id"])
            self.assertEqual(1, self._intent_count())

    def test_slow_clients_cannot_starve_a_complete_good_request(self) -> None:
        stalled: list[socket.socket] = []
        try:
            with socket_service(self.core):
                for _ in range(32):
                    peer = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
                    peer.connect(str(self.path))
                    peer.sendall(b"{")
                    stalled.append(peer)
                with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as good:
                    good.settimeout(2)
                    good.connect(str(self.path))
                    good.sendall(
                        json.dumps(
                            {
                                "protocol": 1,
                                "action": "heartbeat",
                                "task": "AR-0120",
                                "owner": "worker-a",
                                "expected_revision": 2,
                                "lease_minutes": 20,
                                "key": "good-under-slow-clients",
                            }
                        ).encode()
                        + b"\n"
                    )
                    reply = json.loads(_read_line(good, 4096))
                    self.assertEqual("queued-local", reply["ok"]["phase"])
                self.assertEqual(1, self._intent_count())
        finally:
            for peer in stalled:
                peer.close()

    def test_complete_request_evicts_oldest_partial_peer_at_admission_limit(self) -> None:
        stalled: list[socket.socket] = []
        try:
            with socket_service(self.core):
                for _ in range(64):
                    peer = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
                    peer.connect(str(self.path))
                    peer.sendall(b"{")
                    stalled.append(peer)
                with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as good:
                    good.settimeout(2)
                    good.connect(str(self.path))
                    good.sendall(
                        json.dumps(
                            {
                                "protocol": 1,
                                "action": "heartbeat",
                                "task": "AR-0120",
                                "owner": "worker-a",
                                "expected_revision": 2,
                                "lease_minutes": 20,
                                "key": "good-at-admission-limit",
                            }
                        ).encode()
                        + b"\n"
                    )
                    reply = json.loads(_read_line(good, 4096))
                    self.assertEqual("queued-local", reply["ok"]["phase"])
                stalled[0].settimeout(1)
                self.assertEqual(b"", stalled[0].recv(1))
                self.assertEqual(1, self._intent_count())
        finally:
            for peer in stalled:
                peer.close()

    def test_split_frame_is_accepted_and_oversize_frame_does_not_stall_service(self) -> None:
        request = json.dumps(
            {
                "protocol": 1,
                "action": "heartbeat",
                "task": "AR-0120",
                "owner": "worker-a",
                "expected_revision": 2,
                "lease_minutes": 20,
                "key": "split-frame",
            }
        ).encode()
        with socket_service(self.core):
            with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as hostile:
                hostile.connect(str(self.path))
                hostile.sendall(b"x" * 4097 + b"\n")
            with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as good:
                good.settimeout(2)
                good.connect(str(self.path))
                good.sendall(request[:12])
                good.sendall(request[12:] + b"\n")
                reply = json.loads(_read_line(good, 4096))
                self.assertEqual("queued-local", reply["ok"]["phase"])
            self.assertEqual(1, self._intent_count())

    def test_peer_recv_error_does_not_kill_the_acceptor(self) -> None:
        original_recv = socket.socket.recv
        failed = threading.Event()

        def fail_once(peer: socket.socket, size: int, flags: int = 0) -> bytes:
            if not failed.is_set():
                failed.set()
                raise ConnectionResetError("injected peer reset")
            return original_recv(peer, size, flags)

        with socket_service(self.core), patch.object(socket.socket, "recv", fail_once):
            with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as hostile:
                hostile.connect(str(self.path))
                hostile.sendall(b"{")
                self.assertTrue(failed.wait(2))
            with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as good:
                good.settimeout(2)
                good.connect(str(self.path))
                good.sendall(
                    json.dumps(
                        {
                            "protocol": 1,
                            "action": "heartbeat",
                            "task": "AR-0120",
                            "owner": "worker-a",
                            "expected_revision": 2,
                            "lease_minutes": 20,
                            "key": "after-peer-reset",
                        }
                    ).encode()
                    + b"\n"
                )
                reply = json.loads(_read_line(good, 4096))
                self.assertEqual("queued-local", reply["ok"]["phase"])
            self.assertEqual(1, self._intent_count())

    def test_expired_and_eof_peers_are_reclaimed_without_starving_a_good_worker(self) -> None:
        """Idle or disconnected hostile peers release admission capacity for a complete request."""
        with socket_service(self.core):
            with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as idle:
                idle.settimeout(2)
                idle.connect(str(self.path))
                time.sleep(1.1)
                self.assertEqual(b"", idle.recv(1))
            with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as eof:
                eof.connect(str(self.path))
            time.sleep(0.1)
            with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as good:
                good.settimeout(2)
                good.connect(str(self.path))
                good.sendall(
                    json.dumps(
                        {
                            "protocol": 1,
                            "action": "heartbeat",
                            "task": "AR-0120",
                            "owner": "worker-a",
                            "expected_revision": 2,
                            "lease_minutes": 20,
                            "key": "after-peer-cleanup",
                        }
                    ).encode()
                    + b"\n"
                )
                reply = json.loads(_read_line(good, 4096))
                self.assertEqual("queued-local", reply["ok"]["phase"])
            self.assertEqual(1, self._intent_count())


if __name__ == "__main__":
    unittest.main()
