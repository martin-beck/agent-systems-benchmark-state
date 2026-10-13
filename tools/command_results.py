# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Privacy-safe durable wrapped-command result journal helpers."""

from __future__ import annotations

import json
import os
import re
from collections.abc import Callable
from pathlib import Path
from typing import Any

type Meta = dict[str, Any]


def append_file(
    runtime: Path,
    task_id: str,
    owner: str,
    command_hash: str,
    returncode: int,
    classification: str,
    recorded_at: str,
) -> None:
    """Fsync a privacy-safe local result before any fallible post-command work."""
    runtime.mkdir(mode=0o700, parents=True, exist_ok=True)
    record = {
        "at": recorded_at,
        "task": task_id,
        "owner": owner,
        "argv_sha256": command_hash,
        "returncode": returncode,
        "classification": classification,
    }
    path = runtime / "command-results.jsonl"
    descriptor = os.open(path, os.O_APPEND | os.O_CREAT | os.O_WRONLY, 0o600)
    with os.fdopen(descriptor, "ab") as stream:
        stream.write((json.dumps(record, sort_keys=True) + "\n").encode())
        stream.flush()
        os.fsync(stream.fileno())


def load_file(runtime: Path) -> list[Meta]:
    """Strictly load the privacy-safe Git-backend journal for migration."""
    path = runtime / "command-results.jsonl"
    if not path.exists():
        return []
    required = {"at", "task", "owner", "argv_sha256", "returncode", "classification"}
    records: list[Meta] = []
    for number, line in enumerate(path.read_text().splitlines(), 1):
        try:
            record = json.loads(line)
        except json.JSONDecodeError as error:
            raise RuntimeError(f"invalid command journal line {number}") from error
        if not isinstance(record, dict) or set(record) != required:
            raise RuntimeError(f"invalid command journal line {number}")
        if not re.fullmatch(r"[0-9a-f]{64}", str(record["argv_sha256"])):
            raise RuntimeError(f"invalid command journal digest at line {number}")
        if not isinstance(record["returncode"], int):
            raise RuntimeError(f"invalid command journal return code at line {number}")
        records.append(record)
    return records


def append_backend(
    backend: Any,
    now: Callable[[], str],
    task_id: str,
    owner: str,
    command_hash: str,
    returncode: int,
    timed_out: bool,
) -> None:
    backend.append_command_result(
        task_id,
        owner,
        command_hash,
        returncode,
        "SUBPROCESS_TIMEOUT" if timed_out else "EXIT",
        now(),
    )
