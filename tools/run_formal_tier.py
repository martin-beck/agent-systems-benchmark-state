# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Launch the immutable formal verify script with the selected tier contract."""

from __future__ import annotations

import argparse
import hashlib
import importlib
import importlib.util
import os
import re
import signal
import subprocess
from collections.abc import Callable, Mapping
from pathlib import Path
from typing import cast

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RUNTIME_ROOT = PROJECT_ROOT / ".asb-tlc"
TIERS = ("portable-smoke", "pr-publication", "full-exhaustive")
MODEL_COUNTS = {"portable-smoke": 1, "pr-publication": 6, "full-exhaustive": 6}


def _timeout_for_tier(tier: str) -> int:
    try:
        module = importlib.import_module("formal.handoffctl.tier_profiles")
    except ModuleNotFoundError:
        # ``uv run`` may execute from a checkout without namespace-package
        # discovery enabled.  Load the reviewed sibling by absolute path.
        path = Path(__file__).resolve().parents[1] / "formal/handoffctl/tier_profiles.py"
        spec = importlib.util.spec_from_file_location("tier_profiles", path)
        if spec is None or spec.loader is None:
            raise RuntimeError("tier profile module is unavailable") from None
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    timeout_for_tier = cast(Callable[[str], int], module.timeout_for_tier)
    return timeout_for_tier(tier)


def _private_directory(path: Path) -> None:
    path.mkdir(mode=0o700, parents=True, exist_ok=True)
    path.chmod(0o700)
    if path.stat().st_uid != os.getuid() or path.stat().st_mode & 0o077:
        raise RuntimeError(f"runtime root is not owner-private: {path}")


def _digest(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def environment(tier: str, *, runtime_root: Path = RUNTIME_ROOT) -> dict[str, str]:
    """Return the bounded, offline environment for one formal tier."""
    if tier not in TIERS:
        raise ValueError(f"unknown formal tier: {tier}")
    resolved = runtime_root.resolve()
    if not resolved.is_relative_to(PROJECT_ROOT):
        raise ValueError("runtime root must remain under /srv/data/projects")
    timeout = _timeout_for_tier(tier)
    return {
        "TMPDIR": str(resolved),
        "TLC_RUNTIME_ROOT": str(resolved),
        "TLC_ATTESTATION_PATH": str(resolved / "attestations" / f"{tier}.json"),
        "TLC_CGROUP_MODE": "portable" if tier == "portable-smoke" else "required",
        "TLC_TIMEOUT_SECONDS": str(timeout),
        "TLC_LAUNCHER_SHA256": _digest(Path(__file__).resolve()),
    }


def _terminate(process: subprocess.Popen[bytes]) -> None:
    """Terminate one isolated process group and bound the reap operation."""
    for sig, deadline in ((signal.SIGTERM, 5), (signal.SIGKILL, 1)):
        try:
            os.killpg(process.pid, sig)
        except ProcessLookupError:
            return
        try:
            process.wait(timeout=deadline)
            return
        except subprocess.TimeoutExpired:
            continue


def _failure_detail(process: subprocess.Popen[bytes]) -> str:
    """Read only a small, path-sanitized diagnostic from a failed tier."""
    if process.stderr is None:
        return "no diagnostic was emitted"
    detail = process.stderr.read(4096).decode("utf-8", errors="replace").strip()
    detail = re.sub(r"/(?:srv|tmp)/data/projects[^\s']*", "<approved-runtime-path>", detail)
    return detail[-1000:] or "no diagnostic was emitted"


def run(tier: str, *, environ: Mapping[str, str] | None = None) -> int:
    """Run the canonical verify script without shell or retained output."""
    if tier not in TIERS:
        raise ValueError(f"unknown formal tier: {tier}")
    _private_directory(RUNTIME_ROOT)
    env = os.environ.copy()
    env.update(environment(tier))
    if environ is not None:
        env.update(environ)
    runtime_root = Path(env["TLC_RUNTIME_ROOT"]).resolve()
    if not runtime_root.is_relative_to(PROJECT_ROOT):
        raise ValueError("runtime root must remain under /srv/data/projects")
    if Path(env["TMPDIR"]).resolve() != runtime_root:
        raise ValueError("TMPDIR must match the approved runtime root")
    if not Path(env["TLC_ATTESTATION_PATH"]).resolve().is_relative_to(PROJECT_ROOT):
        raise ValueError("attestation path must remain under /srv/data/projects")
    _private_directory(runtime_root)
    command = [
        str(Path(__file__).resolve().parents[1] / "formal/handoffctl/verify.sh"),
        "--tier",
        tier,
    ]
    timeout = MODEL_COUNTS[tier] * _timeout_for_tier(tier) + 120
    process = subprocess.Popen(  # noqa: S603
        command,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
        env=env,
        start_new_session=True,
    )
    try:
        result = process.wait(timeout=timeout)
        if result != 0:
            print(f"formal tier {tier} failed (exit {result}): {_failure_detail(process)}")
        return result
    except subprocess.TimeoutExpired:
        _terminate(process)
        print(f"formal tier {tier} failed: bounded timeout after {timeout}s")
        return 124


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tier", choices=TIERS, required=True)
    args = parser.parse_args()
    return run(args.tier)


if __name__ == "__main__":
    raise SystemExit(main())
