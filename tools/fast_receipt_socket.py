# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Private opt-in receipt socket; a reply never upgrades a queued intent to authority."""

from __future__ import annotations

import json
import os
import selectors
import socket
import stat
import struct
import sys
import time
from collections.abc import Callable, Iterator
from contextlib import contextmanager, suppress
from pathlib import Path
from typing import Any

if __package__:
    from .fast_observation import ObservationCache, validate_max_age
    from .fast_receipts import validate_update_changes
else:  # pragma: no cover - direct vendored import
    from fast_observation import (  # type: ignore[import-not-found,no-redef]
        ObservationCache,
        validate_max_age,
    )
    from fast_receipts import validate_update_changes  # type: ignore[import-not-found,no-redef]

_SOCKET_NAME = "fast-receipts.sock"
# A fully bounded update may carry a 4,000-character summary, a
# 1,024-character next action, and a 4,096-character note.  json.dumps()
# escapes non-ASCII input, so a maximum-length Unicode request is about 110
# KiB on the wire.  The single-frame protocol stays bounded at 128 KiB.
_MAX_REQUEST = 131072
# A complete ASB observation can contain hundreds of worktrees.  Reserve a
# larger fixed reply frame for that inventory, rather than letting the service
# write an unbounded response.  A larger inventory receives a bounded signal
# that permits the documented direct fresh-scan fallback.
_MAX_REPLY = 1048576
_OBSERVATION_SOCKET_TIMEOUT_SECONDS = 100.0
_PUBLIC_FIELDS = (
    "receipt_id",
    "project_id",
    "operation",
    "task_id",
    "expected_revision",
    "phase",
    "started_at",
    "commit_oid",
    "result_revision",
    "error_code",
    "remote_oid",
    "remote_observed_at",
    "publication_error",
    "created_at",
)


class _TransportUnavailableError(ConnectionError):
    """The resident path has no writer; callers must use same-key direct fallback."""


def _require_socket() -> bool:
    return os.environ.get("HANDOFFCTL_FAST_REQUIRE_SOCKET") == "1"


def _fallback_or_error() -> int | None:
    if not _require_socket():
        return None
    sys.stderr.write("ERROR: fast receipt socket was required but unavailable\n")
    return 1


def public_receipt(row: dict[str, Any]) -> dict[str, Any]:
    """Expose the exact bounded public receipt without private input or key."""
    return {field: row[field] for field in _PUBLIC_FIELDS}


def _client_common_dir(root: Path) -> Path | None:
    """Resolve ordinary main/worktree Git metadata without launching Git."""
    marker = root / ".git"
    if marker.is_symlink():
        raise RuntimeError("fast socket Git metadata is a symlink")
    if marker.is_dir():
        return marker.resolve()
    if not marker.is_file():
        return None
    value = marker.read_text(encoding="utf-8")
    if len(value) > 1024 or not value.startswith("gitdir: "):
        return None
    name = value.removeprefix("gitdir: ").strip()
    gitdir = Path(name)
    if not gitdir.is_absolute():
        gitdir = root / gitdir
    gitdir = gitdir.resolve()
    common = gitdir / "commondir"
    if common.exists():
        name = common.read_text(encoding="utf-8").strip()
        if not name or len(name) > 1024:
            return None
        common_path = Path(name)
        if not common_path.is_absolute():
            common_path = gitdir / common_path
        return common_path.resolve()
    return gitdir


def _socket_path(root: Path) -> Path | None:
    common = _client_common_dir(root)
    return None if common is None else common / "handoffctl" / _SOCKET_NAME


def _safe_socket(path: Path) -> bool:
    try:
        directory = path.parent.lstat()
        entry = path.lstat()
    except FileNotFoundError:
        return False
    if (
        not stat.S_ISDIR(directory.st_mode)
        or directory.st_uid != os.geteuid()
        or stat.S_IMODE(directory.st_mode) & 0o077
        or not stat.S_ISSOCK(entry.st_mode)
        or entry.st_uid != os.geteuid()
        or entry.st_nlink != 1
        or stat.S_IMODE(entry.st_mode) != 0o600
    ):
        raise RuntimeError("fast receipt socket is unsafe")
    return True


def _fast_request(argv: list[str]) -> dict[str, Any] | None:  # noqa: C901 - strict wire parser
    if argv[:2] == ["fast", "receipt"] and len(argv) == 3:
        return {"protocol": 1, "action": "receipt", "receipt_id": argv[2]}
    if argv[:2] == ["fast", "observe"] and len(argv) == 4 and argv[2] == "--max-age-seconds":
        try:
            maximum = int(argv[3])
            validate_max_age(maximum)
        except ValueError:
            return None
        return {"protocol": 1, "action": "observe", "max_age_seconds": maximum}
    if argv[:2] == ["fast", "promote"] and len(argv) == 9:
        if argv[2].startswith("-"):
            return None
        promote_options = dict(zip(argv[3::2], argv[4::2], strict=True))
        if set(promote_options) != {"--expected-revision", "--note", "--key"}:
            return None
        try:
            revision = int(promote_options["--expected-revision"])
        except ValueError:
            return None
        return {
            "protocol": 1,
            "action": "promote",
            "task": argv[2],
            "expected_revision": revision,
            "note": promote_options["--note"],
            "key": promote_options["--key"],
        }
    if argv[:2] == ["fast", "update"] and len(argv) >= 11:
        if argv[2].startswith("-") or len(argv[3:]) % 2:
            return None
        update_options = dict(zip(argv[3::2], argv[4::2], strict=True))
        allowed = {
            "--owner",
            "--expected-revision",
            "--status",
            "--priority",
            "--summary",
            "--next-action",
            "--note",
            "--key",
        }
        if len(update_options) != len(argv[3::2]) or set(update_options) - allowed:
            return None
        if not {"--owner", "--expected-revision", "--note", "--key"} <= set(update_options):
            return None
        changes = {
            name.removeprefix("--").replace("-", "_"): value
            for name, value in update_options.items()
            if name in {"--status", "--priority", "--summary", "--next-action"}
        }
        if not changes:
            return None
        try:
            revision = int(update_options["--expected-revision"])
        except ValueError:
            return None
        return {
            "protocol": 1,
            "action": "update",
            "task": argv[2],
            "owner": update_options["--owner"],
            "expected_revision": revision,
            "changes": changes,
            "note": update_options["--note"],
            "key": update_options["--key"],
        }
    if argv[:2] not in (["fast", "heartbeat"], ["fast", "claim"]) or len(argv) < 9:
        return None
    if argv[2].startswith("-") or len(argv[3:]) % 2:
        return None
    options: dict[str, str] = {}
    for name, value in zip(argv[3::2], argv[4::2], strict=True):
        if name not in {
            "--owner",
            "--expected-revision",
            "--lease-minutes",
            "--worker-pid",
            "--worker-start-time",
            "--key",
        }:
            return None
        if name in options:
            return None
        options[name] = value
    if not {"--owner", "--expected-revision", "--key"} <= options.keys():
        return None
    try:
        revision = int(options["--expected-revision"])
        lease = int(options.get("--lease-minutes", "120"))
        worker_pid = int(options["--worker-pid"]) if "--worker-pid" in options else None
        worker_start_time = (
            int(options["--worker-start-time"]) if "--worker-start-time" in options else None
        )
    except ValueError:
        return None
    if (worker_pid is None) != (worker_start_time is None):
        return None
    request = {
        "protocol": 1,
        "action": argv[1],
        "task": argv[2],
        "owner": options["--owner"],
        "expected_revision": revision,
        "lease_minutes": lease,
        "key": options["--key"],
    }
    if worker_pid is not None:
        request["worker_pid"] = worker_pid
        request["worker_start_time"] = worker_start_time
    return request


def _read_line(peer: socket.socket, limit: int) -> bytes:
    data = bytearray()
    while len(data) <= limit:
        chunk = peer.recv(min(4096, limit + 1 - len(data)))
        if not chunk:
            raise ConnectionError("fast receipt socket closed before response")
        data.extend(chunk)
        if b"\n" in chunk:
            line, remainder = bytes(data).split(b"\n", 1)
            if remainder or len(line) > limit:
                raise RuntimeError("fast receipt socket response is malformed")
            return line
    raise RuntimeError("fast receipt socket message is too large")


def _send_reply(peer: socket.socket, reply: dict[str, Any]) -> None:
    """Send one bounded frame, never an unbounded observation response."""
    encoded = json.dumps(reply, sort_keys=True).encode() + b"\n"
    if len(encoded) > _MAX_REPLY:
        encoded = b'{"error":"FAST_OBSERVATION_REPLY_TOO_LARGE: use direct fast observe"}\n'
    peer.sendall(encoded)


def try_socket_fast(argv: list[str]) -> int | None:  # noqa: C901 - strict transport fallback
    """Use the warm bound service when available; otherwise use the direct CLI."""
    request = _fast_request(argv)
    if request is None:
        if argv[:2] in (
            ["fast", "heartbeat"],
            ["fast", "claim"],
            ["fast", "promote"],
            ["fast", "update"],
            ["fast", "receipt"],
            ["fast", "observe"],
        ):
            return _fallback_or_error()
        return None
    path = _socket_path(Path(__file__).resolve().parent.parent)
    if path is None or not _safe_socket(path):
        return _fallback_or_error()
    try:
        with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as peer:
            peer.settimeout(
                _OBSERVATION_SOCKET_TIMEOUT_SECONDS if request["action"] == "observe" else 10
            )
            peer.connect(str(path))
            peer.sendall(json.dumps(request, sort_keys=True).encode() + b"\n")
            raw = _read_line(peer, _MAX_REPLY)
    except (ConnectionError, OSError, TimeoutError):
        # A timed-out enqueue may have committed; the direct path uses the same
        # idempotency key and returns that durable row rather than duplicating it.
        return _fallback_or_error()
    except RuntimeError as error:
        if (
            request["action"] == "observe"
            and str(error) == "fast receipt socket message is too large"
        ):
            return _fallback_or_error()
        raise
    response = json.loads(raw)
    if not isinstance(response, dict) or set(response) not in ({"ok"}, {"error"}):
        raise RuntimeError("fast receipt socket response is invalid")
    if "error" in response:
        if request["action"] == "observe" and str(response["error"]).startswith(
            "FAST_OBSERVATION_REPLY_TOO_LARGE:"
        ):
            return _fallback_or_error()
        sys.stderr.write(f"ERROR: {response['error']}\n")
        return 1
    print(json.dumps(response["ok"], sort_keys=True))
    return 0


def _require_request(request: Any) -> dict[str, Any]:  # noqa: C901 - strict wire validator
    if not isinstance(request, dict) or request.get("protocol") != 1:
        raise RuntimeError("invalid fast receipt socket protocol")
    action = request.get("action")
    if action == "receipt":
        if set(request) != {"protocol", "action", "receipt_id"}:
            raise RuntimeError("invalid fast receipt lookup")
        return request
    if action == "observe":
        if set(request) != {"protocol", "action", "max_age_seconds"}:
            raise RuntimeError("invalid fast observation request")
        try:
            validate_max_age(request["max_age_seconds"])
        except ValueError as error:
            raise RuntimeError("invalid fast observation request") from error
        return request
    if action == "heartbeat":
        if set(request) != {
            "protocol",
            "action",
            "task",
            "owner",
            "expected_revision",
            "lease_minutes",
            "key",
        }:
            raise RuntimeError(f"invalid fast {action} request")
        if (
            not isinstance(request["expected_revision"], int)
            or isinstance(request["expected_revision"], bool)
            or not isinstance(request["lease_minutes"], int)
            or isinstance(request["lease_minutes"], bool)
            or not all(isinstance(request[field], str) for field in ("task", "owner", "key"))
        ):
            raise RuntimeError(f"invalid fast {action} request fields")
        return request
    if action == "claim":
        base = {"protocol", "action", "task", "owner", "expected_revision", "lease_minutes", "key"}
        identity = {"worker_pid", "worker_start_time"}
        if set(request) not in (base, base | identity):
            raise RuntimeError("invalid fast claim request")
        if (
            not isinstance(request["expected_revision"], int)
            or isinstance(request["expected_revision"], bool)
            or not isinstance(request["lease_minutes"], int)
            or isinstance(request["lease_minutes"], bool)
            or not all(isinstance(request[field], str) for field in ("task", "owner", "key"))
            or (
                "worker_pid" in request
                and (
                    type(request["worker_pid"]) is not int
                    or request["worker_pid"] <= 0
                    or type(request["worker_start_time"]) is not int
                    or request["worker_start_time"] < 0
                )
            )
        ):
            raise RuntimeError("invalid fast claim request fields")
        return request
    if action == "promote":
        if set(request) != {"protocol", "action", "task", "expected_revision", "note", "key"}:
            raise RuntimeError("invalid fast promote request")
        if (
            not isinstance(request["expected_revision"], int)
            or isinstance(request["expected_revision"], bool)
            or not all(isinstance(request[field], str) for field in ("task", "note", "key"))
        ):
            raise RuntimeError("invalid fast promote request fields")
        return request
    if action == "update":
        if set(request) != {
            "protocol",
            "action",
            "task",
            "owner",
            "expected_revision",
            "changes",
            "note",
            "key",
        }:
            raise RuntimeError("invalid fast update request")
        if (
            not isinstance(request["expected_revision"], int)
            or isinstance(request["expected_revision"], bool)
            or not all(
                isinstance(request[field], str) for field in ("task", "owner", "note", "key")
            )
        ):
            raise RuntimeError("invalid fast update request fields")
        try:
            validate_update_changes(request["changes"])
        except ValueError as error:
            raise RuntimeError("invalid fast update request fields") from error
        return request
    raise RuntimeError("unknown fast receipt socket action")


def _handle(
    core: Any,
    peer: socket.socket,
    submit: Callable[[dict[str, Any]], dict[str, Any]],
    raw: bytes | None = None,
) -> None:
    with peer:
        try:
            peer.settimeout(10)
            credential = peer.getsockopt(socket.SOL_SOCKET, socket.SO_PEERCRED, 12)
            pid, uid, _gid = struct.unpack("3i", credential)
            if uid != os.geteuid() or pid < 1:
                raise RuntimeError("fast receipt socket peer is not authorized")
            caller = Path(f"/proc/{pid}/cwd").readlink().resolve()
            core.assert_project_binding(caller)
            if core.backend_selection()["backend"] != "git":
                raise RuntimeError("fast receipts require Git authority")
            request = _require_request(
                json.loads(raw if raw is not None else _read_line(peer, _MAX_REQUEST))
            )
            result = submit(request)
            reply = {"ok": (result if request["action"] == "observe" else public_receipt(result))}
            _send_reply(peer, reply)
        except _TransportUnavailableError:
            # No reply forces the same-key client fallback.  An error reply
            # would incorrectly make a dead service a terminal command failure.
            pass
        except TimeoutError:
            # A timed-out write may have committed; EOF makes the client retry
            # through the same-key direct path instead of reporting success.
            pass
        except (OSError, ValueError, RuntimeError, KeyError) as error:
            with suppress(OSError):
                _send_reply(peer, {"error": str(error)})


@contextmanager
def socket_service(core: Any) -> Iterator[None]:  # noqa: C901
    """Serve queue/read requests beside, not inside, the authority executor."""
    import threading
    from concurrent.futures import Future, ThreadPoolExecutor
    from queue import Full, Queue

    from .fast_receipts import ReceiptStore

    path = core.coordinator_lock_path().parent / _SOCKET_NAME
    if path.exists() or path.is_symlink():
        if not _safe_socket(path):
            raise RuntimeError("fast receipt socket path is unsafe")
        old = path.lstat()
        with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as probe:
            probe.settimeout(0.1)
            try:
                probe.connect(str(path))
            except ConnectionRefusedError:
                pass
            else:
                raise RuntimeError("fast receipt socket is already active")
        if path.lstat().st_ino != old.st_ino:
            raise RuntimeError("fast receipt socket identity changed")
        path.unlink()
    requests: Queue[tuple[dict[str, Any], Future[dict[str, Any]]] | None] = Queue(maxsize=64)
    observations = ObservationCache()
    ready = threading.Event()
    writer_error: list[Exception] = []

    def write_requests() -> None:
        try:
            with ReceiptStore(
                path.parent / "fast-receipts.sqlite3", core.project_binding()["project_id"]
            ) as store:
                ready.set()
                while (item := requests.get()) is not None:
                    request, future = item
                    try:
                        if request["action"] == "heartbeat":
                            result = store.enqueue_heartbeat(
                                key=request["key"],
                                task=request["task"],
                                owner=request["owner"],
                                expected_revision=request["expected_revision"],
                                lease_minutes=request["lease_minutes"],
                            )
                        elif request["action"] == "claim":
                            result = store.enqueue_claim(
                                key=request["key"],
                                task=request["task"],
                                owner=request["owner"],
                                expected_revision=request["expected_revision"],
                                lease_minutes=request["lease_minutes"],
                                worker_pid=request.get("worker_pid"),
                                worker_start_time=request.get("worker_start_time"),
                            )
                        elif request["action"] == "promote":
                            result = store.enqueue_promote(
                                key=request["key"],
                                task=request["task"],
                                expected_revision=request["expected_revision"],
                                note=request["note"],
                            )
                        elif request["action"] == "update":
                            result = store.enqueue_update(
                                key=request["key"],
                                task=request["task"],
                                owner=request["owner"],
                                expected_revision=request["expected_revision"],
                                changes=request["changes"],
                                note=request["note"],
                            )
                        else:
                            found = store.read(request["receipt_id"])
                            if found is None:
                                raise RuntimeError("unknown fast receipt")
                            result = found
                        future.set_result(result)
                    except Exception as error:
                        future.set_exception(error)
        except Exception as error:
            writer_error.append(error)
            ready.set()

    writer = threading.Thread(target=write_requests, name="fast-receipt-writer", daemon=True)
    writer.start()
    if not ready.wait(timeout=10) or writer_error:
        writer.join(timeout=1)
        raise RuntimeError("fast receipt writer could not start") from (
            writer_error[0] if writer_error else None
        )

    def submit(request: dict[str, Any]) -> dict[str, Any]:
        if request["action"] == "observe":
            return observations.observe(core, request["max_age_seconds"])
        if not writer.is_alive():
            raise _TransportUnavailableError("fast receipt writer is unavailable")
        future: Future[dict[str, Any]] = Future()
        try:
            requests.put((request, future), timeout=1)
        except Full as error:
            raise RuntimeError("fast receipt writer queue is saturated") from error
        return future.result(timeout=9)

    try:
        with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as listener:
            listener.bind(str(path))
            path.chmod(0o600)
            if not _safe_socket(path):
                raise RuntimeError("fast receipt socket did not bind privately")
            identity = path.lstat().st_ino
            listener.listen(128)
            listener.setblocking(False)
            stop = threading.Event()
            # Observations are bounded separately from receipt operations.
            # A cold 64-caller read burst may occupy every observation worker,
            # but cannot make a socket-required mutation unavailable.
            observation_slots = threading.BoundedSemaphore(64)
            receipt_slots = threading.BoundedSemaphore(32)
            with (
                ThreadPoolExecutor(max_workers=64) as observation_pool,
                ThreadPoolExecutor(max_workers=32) as receipt_pool,
            ):

                def accept_loop() -> None:  # noqa: C901 - bounded socket admission state machine
                    pending: dict[socket.socket, tuple[bytearray, float]] = {}
                    with selectors.DefaultSelector() as selector:
                        selector.register(listener, selectors.EVENT_READ)
                        try:
                            while not stop.is_set():
                                now = time.monotonic()
                                for peer, (_buffer, deadline) in list(pending.items()):
                                    if now >= deadline:
                                        selector.unregister(peer)
                                        pending.pop(peer)
                                        peer.close()
                                for key, _mask in selector.select(timeout=0.05):
                                    if key.fileobj is listener:
                                        try:
                                            peer, _ = listener.accept()
                                        except BlockingIOError:
                                            continue
                                        if len(pending) >= 64:
                                            oldest = next(iter(pending))
                                            selector.unregister(oldest)
                                            pending.pop(oldest)
                                            oldest.close()
                                        peer.setblocking(False)
                                        pending[peer] = (bytearray(), time.monotonic() + 1.0)
                                        selector.register(peer, selectors.EVENT_READ)
                                        continue
                                    selected = key.fileobj
                                    if not isinstance(selected, socket.socket):
                                        raise RuntimeError("invalid fast receipt selector peer")
                                    peer = selected
                                    entry = pending.get(peer)
                                    if entry is None:
                                        # A listener event in this selected batch may have
                                        # evicted this incomplete peer to admit a new client.
                                        continue
                                    buffer, _deadline = entry
                                    try:
                                        chunk = peer.recv(_MAX_REQUEST + 2 - len(buffer))
                                    except BlockingIOError:
                                        continue
                                    except OSError:
                                        selector.unregister(peer)
                                        pending.pop(peer)
                                        peer.close()
                                        continue
                                    if not chunk:
                                        selector.unregister(peer)
                                        pending.pop(peer)
                                        peer.close()
                                        continue
                                    buffer.extend(chunk)
                                    if b"\n" not in buffer and len(buffer) <= _MAX_REQUEST:
                                        continue
                                    selector.unregister(peer)
                                    pending.pop(peer)
                                    line, separator, remainder = bytes(buffer).partition(b"\n")
                                    if not separator or remainder or len(line) > _MAX_REQUEST:
                                        peer.close()
                                        continue
                                    try:
                                        request = json.loads(line)
                                        action = (
                                            request.get("action")
                                            if isinstance(request, dict)
                                            else None
                                        )
                                    except (TypeError, ValueError):
                                        action = None
                                    slots = (
                                        observation_slots if action == "observe" else receipt_slots
                                    )
                                    pool = observation_pool if action == "observe" else receipt_pool
                                    if not slots.acquire(blocking=False):
                                        peer.close()
                                        continue
                                    peer.setblocking(True)

                                    def handle_one(
                                        connection: socket.socket,
                                        raw: bytes,
                                        slot: threading.BoundedSemaphore = slots,
                                    ) -> None:
                                        try:
                                            _handle(core, connection, submit, raw)
                                        finally:
                                            slot.release()

                                    try:
                                        pool.submit(handle_one, peer, line)
                                    except RuntimeError:
                                        slots.release()
                                        peer.close()
                                        raise
                        finally:
                            for peer in pending:
                                selector.unregister(peer)
                                peer.close()

                thread = threading.Thread(target=accept_loop, daemon=True)
                thread.start()
                try:
                    yield
                finally:
                    stop.set()
                    thread.join(timeout=2)
            if path.exists() and path.lstat().st_ino == identity:
                path.unlink()
    finally:
        if writer.is_alive():
            requests.put(None, timeout=10)
            writer.join(timeout=10)
            if writer.is_alive():
                raise RuntimeError("fast receipt writer did not stop")
