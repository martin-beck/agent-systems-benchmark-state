# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Run one TLC model under durable admission and explicit resource bounds."""

from __future__ import annotations

import argparse
import fcntl
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
import uuid
from pathlib import Path

DEFAULT_WORKERS = 2
DEFAULT_HEAP = "2048m"
DEFAULT_MEMORY_MAX = "3G"
DEFAULT_SWAP_MAX = "3G"
# RLIMIT_AS bounds virtual address space, not physical/swap admission.  Keep it
# distinct from the attested 3G cgroup envelope so JVM native mappings do not
# consume the physical-memory contract by accident.
DEFAULT_ADDRESS_SPACE_MAX = "8G"
_WORKER_ROOT = Path(tempfile.gettempdir()) / (
    f"agent-workflow-coordinator-tlc-{getattr(os, 'getuid', lambda: 0)()}"
)
DEFAULT_QUEUE = str(_WORKER_ROOT / "queue")
DEFAULT_ADMISSION_LOCK = str(_WORKER_ROOT / "admission.lock")


class AdmissionError(RuntimeError):
    """Raised when a TLC job cannot be admitted safely."""


def _positive_int(value: str, name: str) -> int:
    try:
        parsed = int(value)
    except ValueError as error:
        raise AdmissionError(f"{name} must be an integer") from error
    if parsed < 1:
        raise AdmissionError(f"{name} must be positive")
    return parsed


def _heap_bytes(heap: str) -> int:
    units = {"m": 1024**2, "g": 1024**3}
    suffix = heap[-1].lower()
    if suffix not in units:
        raise AdmissionError("heap must use an m or g suffix")
    return _positive_int(heap[:-1], "heap") * units[suffix]


def _pid_is_alive(pid: object) -> bool:
    if not isinstance(pid, int) or pid <= 0:
        return False
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    except OSError:
        return False
    return True


def _prune_stale(queue: Path, max_age: int = 86400) -> None:
    now = time.time()
    for item in queue.glob("*.job.json"):
        try:
            if now - item.stat().st_mtime > max_age:
                record = json.loads(item.read_text(encoding="utf-8"))
                state = record.get("state")
                if state == "running" and _pid_is_alive(record.get("pid")):
                    # Never reclaim a live process merely because its record is
                    # old; the admission lock and process group own recovery.
                    continue
                if state not in {"queued", "running"}:
                    continue
                record.update(
                    {
                        "ended": now,
                        "state": "orphaned",
                        "error": (
                            "stale running job; owner process is absent"
                            if state == "running"
                            else "stale queued job; caller did not complete admission"
                        ),
                    }
                )
                outcome = item.with_name(item.name.replace(".job.json", ".outcome.json"))
                if not outcome.exists():
                    outcome.write_text(json.dumps(record, sort_keys=True) + "\n")
                item.unlink()
        except FileNotFoundError:
            continue
        except (OSError, ValueError, TypeError):
            # Corrupt stale records are not executable work; preserve a
            # durable failure marker and remove only the stale queue entry.
            outcome = item.with_name(item.name.replace(".job.json", ".outcome.json"))
            if not outcome.exists():
                outcome.write_text(
                    json.dumps(
                        {
                            "state": "orphaned",
                            "ended": now,
                            "error": "stale queue record was unreadable",
                        },
                        sort_keys=True,
                    )
                    + "\n"
                )
            item.unlink(missing_ok=True)


def build_command(
    *,
    jar: Path,
    model: Path,
    config: Path,
    metadir: Path,
    workers: int = DEFAULT_WORKERS,
    heap: str = DEFAULT_HEAP,
    memory_max: str = DEFAULT_MEMORY_MAX,
    swap_max: str = DEFAULT_SWAP_MAX,
    address_space_max: str = DEFAULT_ADDRESS_SPACE_MAX,
    cpu_quota: str = "200%",
    tasks_max: int = 64,
    timeout_seconds: int = 1800,
    cgroup_mode: str = "required",
) -> list[str]:
    """Build a bounded TLC command without executing it."""
    worker_count = _positive_int(str(workers), "workers")
    process_limit = _positive_int(str(tasks_max), "tasks_max")
    timeout = _positive_int(str(timeout_seconds), "timeout_seconds")
    heap_bytes = _heap_bytes(heap)
    if memory_max == "0" or swap_max == "0":
        raise AdmissionError("memory and swap limits must be non-zero")
    address_space_bytes = _memory_bytes(address_space_max)
    if address_space_bytes <= heap_bytes:
        raise AdmissionError("address-space limit must exceed JVM heap")
    if heap_bytes >= _memory_bytes(memory_max):
        raise AdmissionError("JVM heap must be below the cgroup memory limit")
    java = [
        "java",
        f"-Xmx{heap}",
        "-XX:+UseSerialGC",
        "-XX:MaxMetaspaceSize=256m",
        "-XX:CompressedClassSpaceSize=128m",
        "-Xss256k",
        f"-XX:ActiveProcessorCount={worker_count}",
        "-cp",
        str(jar),
        "tlc2.TLC",
        "-cleanup",
        "-config",
        str(config),
        "-metadir",
        str(metadir),
        "-workers",
        str(worker_count),
        str(model),
    ]
    if cgroup_mode == "off":
        return java
    if cgroup_mode == "portable":
        timeout_bin = shutil.which("timeout")
        prlimit_bin = shutil.which("prlimit")
        if timeout_bin is None or prlimit_bin is None:
            raise AdmissionError("portable containment requires timeout and prlimit")
        cpu_percent = _positive_int(cpu_quota.rstrip("%"), "cpu_quota")
        cpu_seconds = timeout * cpu_percent // 100
        host_processes = len(list(Path("/proc").glob("[0-9]*")))
        return [
            timeout_bin,
            "--signal=TERM",
            "--kill-after=5s",
            str(timeout),
            prlimit_bin,
            f"--as={address_space_bytes}:{address_space_bytes}",
            f"--nproc={host_processes + process_limit}:{host_processes + process_limit}",
            f"--cpu={cpu_seconds}:{cpu_seconds}",
            "--",
            *java,
        ]
    systemd = shutil.which("systemd-run")
    if systemd is None:
        raise AdmissionError("systemd-run is required for TLC cgroup containment")
    return [
        systemd,
        "--user",
        "--quiet",
        "--wait",
        "--collect",
        "--pipe",
        "--service-type=exec",
        "--property=MemoryMax=" + memory_max,
        "--property=MemorySwapMax=" + swap_max,
        "--property=CPUQuota=" + cpu_quota,
        "--property=TasksMax=" + str(process_limit),
        "--property=KillMode=control-group",
        "--property=RuntimeMaxSec=" + str(timeout),
        "--",
        *java,
    ]


def _memory_bytes(value: str) -> int:
    suffix = value[-1].upper()
    units = {"M": 1024**2, "G": 1024**3}
    if suffix not in units:
        raise AdmissionError("memory limit must use an M or G suffix")
    return _positive_int(value[:-1], "memory limit") * units[suffix]


def run(args: argparse.Namespace) -> int:
    """Queue, admit, execute, and durably classify one TLC model."""
    queue = Path(args.queue).resolve()
    queue.mkdir(mode=0o700, parents=True, exist_ok=True)
    _prune_stale(queue)
    job = queue / f"{os.getpid()}-{uuid.uuid4().hex}.job.json"
    outcome = job.with_name(job.name.replace(".job.json", ".outcome.json"))
    lock_path = Path(args.admission_lock).resolve()
    lock_path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    record = {
        "model": str(args.model),
        "pid": os.getpid(),
        "state": "queued",
        "created": time.time(),
        "workers": args.workers,
        "heap": args.heap,
        "memory_max": args.memory_max,
        "swap_max": args.swap_max,
        "address_space_max": args.address_space_max,
    }
    job.write_text(json.dumps(record, sort_keys=True) + "\n", encoding="utf-8")
    try:
        command = build_command(
            jar=Path(args.jar),
            model=Path(args.model),
            config=Path(args.config),
            metadir=Path(args.metadir),
            workers=args.workers,
            heap=args.heap,
            memory_max=args.memory_max,
            swap_max=args.swap_max,
            address_space_max=args.address_space_max,
            cpu_quota=args.cpu_quota,
            tasks_max=args.tasks_max,
            timeout_seconds=args.timeout_seconds,
            cgroup_mode=args.cgroup_mode,
        )
        with lock_path.open("a+", encoding="utf-8") as lock:
            fcntl.flock(lock, fcntl.LOCK_EX)
            record["state"] = "running"
            job.write_text(json.dumps(record, sort_keys=True) + "\n", encoding="utf-8")
            exit_code = subprocess.run(command, check=False).returncode  # noqa: S603
            record.update({"ended": time.time(), "state": "completed", "exit_code": exit_code})
            outcome.write_text(json.dumps(record, sort_keys=True) + "\n", encoding="utf-8")
            return exit_code
    except KeyboardInterrupt:
        record.update({"ended": time.time(), "state": "canceled", "exit_code": 130})
        outcome.write_text(json.dumps(record, sort_keys=True) + "\n", encoding="utf-8")
        raise
    except (AdmissionError, OSError) as error:
        record.update({"ended": time.time(), "state": "failed", "error": str(error)})
        outcome.write_text(json.dumps(record, sort_keys=True) + "\n", encoding="utf-8")
        print(f"TLC admission failed closed: {error}", file=sys.stderr)
        return 2
    finally:
        if job.exists():
            job.unlink()


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser()
    result.add_argument("--jar", required=True)
    result.add_argument("--model", required=True)
    result.add_argument("--config", required=True)
    result.add_argument("--metadir", required=True)
    result.add_argument(
        "--queue",
        default=DEFAULT_QUEUE,
    )
    result.add_argument("--admission-lock", default=DEFAULT_ADMISSION_LOCK)
    result.add_argument(
        "--workers", type=int, default=int(os.environ.get("TLC_WORKERS", DEFAULT_WORKERS))
    )
    result.add_argument("--heap", default=os.environ.get("TLC_HEAP", DEFAULT_HEAP))
    result.add_argument(
        "--memory-max", default=os.environ.get("TLC_MEMORY_MAX", DEFAULT_MEMORY_MAX)
    )
    result.add_argument("--swap-max", default=os.environ.get("TLC_SWAP_MAX", DEFAULT_SWAP_MAX))
    result.add_argument(
        "--address-space-max",
        default=os.environ.get("TLC_ADDRESS_SPACE_MAX", DEFAULT_ADDRESS_SPACE_MAX),
    )
    result.add_argument("--cpu-quota", default=os.environ.get("TLC_CPU_QUOTA", "200%"))
    result.add_argument("--tasks-max", type=int, default=int(os.environ.get("TLC_TASKS_MAX", "64")))
    result.add_argument(
        "--timeout-seconds", type=int, default=int(os.environ.get("TLC_TIMEOUT_SECONDS", "1800"))
    )
    result.add_argument(
        "--cgroup-mode",
        choices=("required", "portable", "off"),
        default=os.environ.get("TLC_CGROUP_MODE", "required"),
    )
    return result


if __name__ == "__main__":
    raise SystemExit(run(parser().parse_args()))
