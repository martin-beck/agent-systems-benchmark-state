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
import time
import uuid
from pathlib import Path

DEFAULT_WORKERS = 2
DEFAULT_HEAP = "2048m"
DEFAULT_MEMORY_MAX = "3G"
DEFAULT_SWAP_MAX = "3G"
DEFAULT_STORAGE_MAX = "2G"
DEFAULT_STORAGE_RESERVE = "256M"
DEFAULT_ADMISSION_LOCK = "/tmp/agent-workflow-coordinator-tlc-admission.lock"  # noqa: S108


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


def _prune_stale(queue: Path, max_age: int = 86400) -> None:
    now = time.time()
    for item in queue.glob("*.job.json"):
        try:
            if now - item.stat().st_mtime > max_age:
                record = json.loads(item.read_text(encoding="utf-8"))
                if record.get("state") != "queued":
                    # A running record may still have a live process or an
                    # externally completed outcome. Retain it until verified
                    # reconciliation can fence and classify that operation.
                    continue
                record.update(
                    {
                        "ended": now,
                        "state": "orphaned",
                        "error": "stale queued job; caller did not complete admission",
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
    workspace: Path | None = None,
    workers: int = DEFAULT_WORKERS,
    heap: str = DEFAULT_HEAP,
    memory_max: str = DEFAULT_MEMORY_MAX,
    swap_max: str = DEFAULT_SWAP_MAX,
    cpu_quota: str = "200%",
    tasks_max: int = 64,
    timeout_seconds: int = 1800,
    cgroup_mode: str = "required",
    unit_name: str | None = None,
) -> list[str]:
    """Build a bounded TLC command without executing it."""
    worker_count = _positive_int(str(workers), "workers")
    process_limit = _positive_int(str(tasks_max), "tasks_max")
    timeout = _positive_int(str(timeout_seconds), "timeout_seconds")
    heap_bytes = _heap_bytes(heap)
    if memory_max == "0" or swap_max == "0":
        raise AdmissionError("memory and swap limits must be non-zero")
    if heap_bytes >= _memory_bytes(memory_max):
        raise AdmissionError("JVM heap must be below the cgroup memory limit")
    workspace_path = (workspace or metadir.parent).resolve()
    java = [
        "java",
        f"-Xmx{heap}",
        f"-Djava.io.tmpdir={workspace_path}",
        f"-Duser.dir={workspace_path}",
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
            f"--as={_memory_bytes(memory_max)}:{_memory_bytes(memory_max)}",
            f"--nproc={host_processes + process_limit}:{host_processes + process_limit}",
            f"--cpu={cpu_seconds}:{cpu_seconds}",
            "--",
            *java,
        ]
    systemd = shutil.which("systemd-run")
    if systemd is None:
        raise AdmissionError("systemd-run is required for TLC cgroup containment")
    unit_name = unit_name or f"handoffctl-tlc-{uuid.uuid4().hex}"
    return [
        systemd,
        "--user",
        "--unit=" + unit_name,
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
        sys.executable,
        str(Path(__file__).resolve()),
        "--verify-effective-cgroup",
        "--memory-max",
        memory_max,
        "--swap-max",
        swap_max,
        "--",
        *java,
    ]


def _memory_bytes(value: str) -> int:
    suffix = value[-1].upper()
    units = {"M": 1024**2, "G": 1024**3}
    if suffix not in units:
        raise AdmissionError("memory limit must use an M or G suffix")
    return _positive_int(value[:-1], "memory limit") * units[suffix]


def _storage_bytes(value: str) -> int:
    """Parse a positive storage quantity using the same binary units as memory."""
    return _memory_bytes(value)


def _available_bytes(directory: Path) -> int:
    try:
        return os.statvfs(directory).f_bavail * os.statvfs(directory).f_frsize
    except OSError as error:
        raise AdmissionError(f"cannot inspect workspace capacity: {directory}") from error


def _directory_bytes(directory: Path) -> int:
    """Return allocated bytes below one private TLC workspace."""
    total = 0
    try:
        for path in directory.rglob("*"):
            if path.is_file():
                total += path.stat().st_blocks * 512
    except OSError as error:
        raise AdmissionError(f"cannot inspect workspace usage: {directory}") from error
    return total


def _prepare_workspace(workspace: Path, metadir: Path, storage_reserve: int) -> None:
    workspace.mkdir(mode=0o700, parents=True, exist_ok=True)
    try:
        metadir.resolve().relative_to(workspace.resolve())
    except ValueError as error:
        raise AdmissionError("metadir must be inside the private TLC workspace") from error
    metadir.mkdir(mode=0o700, parents=True, exist_ok=True)
    if _available_bytes(workspace) < storage_reserve:
        raise AdmissionError("insufficient workspace capacity before TLC admission")


def _stop_over_budget(process: subprocess.Popen[bytes], cgroup_mode: str, unit_name: str) -> None:
    """Stop the actual contained service, not merely its systemd-run client."""
    if cgroup_mode == "required":
        systemctl = shutil.which("systemctl")
        if systemctl is None:
            raise AdmissionError("systemctl is required to stop an over-budget TLC unit")
        subprocess.run([systemctl, "--user", "stop", unit_name], check=False)  # noqa: S603
    else:
        process.terminate()
    try:
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait()


def _cgroup_v2_directory(proc_root: Path = Path("/proc")) -> tuple[Path, Path]:
    relative = next(
        (
            line.split("::", 1)[1]
            for line in (proc_root / "self/cgroup").read_text().splitlines()
            if line.startswith("0::")
        ),
        None,
    )
    cgroup_mount = next(
        (
            (Path(fields[3]), Path(fields[4]))
            for line in (proc_root / "self/mountinfo").read_text().splitlines()
            if " - cgroup2 " in line
            for fields in [line.split(" - ", 1)[0].split()]
            if len(fields) >= 5
        ),
        None,
    )
    if not relative or cgroup_mount is None:
        raise AdmissionError("cgroup-v2 membership is unavailable")
    mount_root, mount = cgroup_mount
    try:
        directory = mount / Path(relative).relative_to(mount_root)
    except ValueError as error:
        raise AdmissionError("cgroup membership is outside its cgroup-v2 mount") from error
    if not directory.is_dir() or not mount.is_dir():
        raise AdmissionError("effective cgroup path is unavailable")
    return directory, mount


def _cgroup_limit(path: Path, *, required: bool = False) -> int | None:
    try:
        value = path.read_text(encoding="utf-8").strip()
    except FileNotFoundError as error:
        if required:
            raise AdmissionError(f"required cgroup control is unavailable: {path.name}") from error
        # A controller can be undelegated at an intermediate cgroup.  That
        # level cannot impose this control, so continue checking its parents.
        return None
    except OSError as error:
        raise AdmissionError(f"required cgroup control is unavailable: {path.name}") from error
    if value == "max":
        return None
    return _positive_int(value, path.name)


def verify_effective_cgroup(
    *, memory_max: str, swap_max: str, proc_root: Path = Path("/proc")
) -> None:
    """Verify bounds in this process's own cgroup before execing TLC."""
    directory, mount = _cgroup_v2_directory(proc_root)
    requested = (
        ("memory.max", _memory_bytes(memory_max), True),
        ("memory.high", _memory_bytes(memory_max), False),
        ("memory.swap.max", _memory_bytes(swap_max), True),
    )
    for name, expected, exact_leaf in requested:
        current = directory
        while True:
            actual = _cgroup_limit(current / name, required=current == directory and exact_leaf)
            if current == directory and exact_leaf and actual != expected:
                raise AdmissionError(f"leaf {name} does not match requested bound")
            if actual is not None and actual < expected:
                raise AdmissionError(f"effective {name} is below requested bound")
            if current == mount:
                break
            current = current.parent


def verify_effective_cgroup_main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--memory-max", required=True)
    parser.add_argument("--swap-max", required=True)
    parser.add_argument("command", nargs=argparse.REMAINDER)
    args = parser.parse_args(argv)
    command = args.command[1:] if args.command[:1] == ["--"] else args.command
    if not command:
        parser.error("a TLC command is required after --")
    try:
        verify_effective_cgroup(memory_max=args.memory_max, swap_max=args.swap_max)
        os.execvp(command[0], command)  # noqa: S606
    except (AdmissionError, OSError) as error:
        print(f"TLC admission failed closed: {error}", file=sys.stderr)
        return 2


def run(args: argparse.Namespace) -> int:
    """Queue, admit, execute, and durably classify one TLC model."""
    queue = Path(args.queue).resolve()
    queue.mkdir(mode=0o700, parents=True, exist_ok=True)
    workspace = Path(getattr(args, "workspace", Path(args.metadir).parent)).resolve()
    metadir = Path(args.metadir).resolve()
    storage_max = _storage_bytes(getattr(args, "storage_max", DEFAULT_STORAGE_MAX))
    storage_reserve = _storage_bytes(getattr(args, "storage_reserve", DEFAULT_STORAGE_RESERVE))
    _prepare_workspace(workspace, metadir, storage_reserve)
    _prune_stale(queue)
    job = queue / f"{os.getpid()}-{uuid.uuid4().hex}.job.json"
    unit_name = f"handoffctl-tlc-{uuid.uuid4().hex}"
    outcome = job.with_name(job.name.replace(".job.json", ".outcome.json"))
    lock_path = Path(getattr(args, "admission_lock", DEFAULT_ADMISSION_LOCK))
    record = {
        "model": str(args.model),
        "pid": os.getpid(),
        "state": "queued",
        "created": time.time(),
        "workers": args.workers,
        "heap": args.heap,
        "memory_max": args.memory_max,
        "swap_max": args.swap_max,
        "workspace": str(workspace),
        "storage_max": getattr(args, "storage_max", DEFAULT_STORAGE_MAX),
        "storage_reserve": getattr(args, "storage_reserve", DEFAULT_STORAGE_RESERVE),
    }
    job.write_text(json.dumps(record, sort_keys=True) + "\n")
    try:
        command = build_command(
            jar=Path(args.jar),
            model=Path(args.model),
            config=Path(args.config),
            metadir=metadir,
            workspace=workspace,
            workers=args.workers,
            heap=args.heap,
            memory_max=args.memory_max,
            swap_max=args.swap_max,
            cpu_quota=args.cpu_quota,
            tasks_max=args.tasks_max,
            timeout_seconds=args.timeout_seconds,
            cgroup_mode=args.cgroup_mode,
            unit_name=unit_name,
        )
        with lock_path.open("w") as lock:
            fcntl.flock(lock, fcntl.LOCK_EX)
            record["state"] = "running"
            job.write_text(json.dumps(record, sort_keys=True) + "\n")
            process = subprocess.Popen(command)  # noqa: S603
            classification = "completed"
            while process.poll() is None:
                if _directory_bytes(workspace) > storage_max:
                    _stop_over_budget(process, args.cgroup_mode, unit_name)
                    classification = "storage-exhausted"
                    break
                time.sleep(0.1)
            usage = _directory_bytes(workspace)
            if usage > storage_max:
                classification = "storage-exhausted"
            exit_code = process.returncode
            record.update(
                {
                    "ended": time.time(),
                    "state": classification,
                    "exit_code": exit_code,
                    "workspace_bytes": usage,
                }
            )
            outcome.write_text(json.dumps(record, sort_keys=True) + "\n")
            return 75 if classification == "storage-exhausted" else exit_code
    except KeyboardInterrupt:
        record.update({"ended": time.time(), "state": "canceled", "exit_code": 130})
        outcome.write_text(json.dumps(record, sort_keys=True) + "\n")
        raise
    except (AdmissionError, OSError) as error:
        record.update({"ended": time.time(), "state": "failed", "error": str(error)})
        outcome.write_text(json.dumps(record, sort_keys=True) + "\n")
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
        "--workspace",
        default=os.environ.get("TLC_WORKSPACE", ".tlc-work"),
        help="private per-run workspace containing TLC state and temporary modules",
    )
    result.add_argument(
        "--queue",
        default=os.environ.get("TLC_ADMISSION_QUEUE", "/tmp/agent-workflow-coordinator-tlc"),  # noqa: S108
    )
    result.add_argument(
        "--admission-lock",
        default=os.environ.get("TLC_ADMISSION_LOCK", DEFAULT_ADMISSION_LOCK),
        help="explicit admission lock; publication workflows retain the canonical default",
    )
    result.add_argument(
        "--workers", type=int, default=int(os.environ.get("TLC_WORKERS", DEFAULT_WORKERS))
    )
    result.add_argument("--heap", default=os.environ.get("TLC_HEAP", DEFAULT_HEAP))
    result.add_argument(
        "--memory-max", default=os.environ.get("TLC_MEMORY_MAX", DEFAULT_MEMORY_MAX)
    )
    result.add_argument("--swap-max", default=os.environ.get("TLC_SWAP_MAX", DEFAULT_SWAP_MAX))
    result.add_argument(
        "--storage-max", default=os.environ.get("TLC_STORAGE_MAX", DEFAULT_STORAGE_MAX)
    )
    result.add_argument(
        "--storage-reserve",
        default=os.environ.get("TLC_STORAGE_RESERVE", DEFAULT_STORAGE_RESERVE),
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
    if len(sys.argv) > 1 and sys.argv[1] == "--verify-effective-cgroup":
        raise SystemExit(verify_effective_cgroup_main(sys.argv[2:]))
    raise SystemExit(run(parser().parse_args()))
