# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Create a provider-free, non-authorizing unsigned development receipt.

This path deliberately does not invoke TLC, a model checker, a provider, or a
third-party executable.  It is useful for exercising the surrounding runner
and integration plumbing while formal/publication qualification remains a
separate concern.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import secrets
import tempfile
import time
from pathlib import Path


class DevelopmentRunnerError(ValueError):
    """Raised for invalid unsigned-development requests."""


def _write_receipt(path: Path, receipt: dict[str, object]) -> None:
    """Atomically write a bounded JSON receipt below an explicit parent."""
    if path.name in {"", ".", ".."}:
        raise DevelopmentRunnerError("receipt path must name a file")
    path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    temporary.write_text(
        json.dumps(receipt, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8"
    )
    os.replace(temporary, path)


def create_receipt(*, output: Path, workload: str = "development") -> dict[str, object]:
    """Generate one disposable local seed and record non-authorizing metadata."""
    if not workload or len(workload) > 128 or any(char.isspace() for char in workload):
        raise DevelopmentRunnerError("workload must be a bounded non-empty token")
    with tempfile.TemporaryDirectory(prefix="asb-unsigned-development-") as directory:
        seed_path = Path(directory) / "seed"
        seed_path.write_bytes(secrets.token_bytes(32))
        digest = hashlib.sha256(seed_path.read_bytes()).hexdigest()
    receipt: dict[str, object] = {
        "schema_version": 1,
        "profile": "unsigned-development",
        "workload": workload,
        "seed_sha256": digest,
        "seed_retained": False,
        "provider_required": False,
        "formal_execution": False,
        "qualification_authorized": False,
        "created_at_unix": int(time.time()),
    }
    _write_receipt(output, receipt)
    return receipt


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    result.add_argument("--output", type=Path, required=True)
    result.add_argument("--workload", default="development")
    return result


def main() -> int:
    arguments = parser().parse_args()
    try:
        create_receipt(output=arguments.output, workload=arguments.workload)
    except (DevelopmentRunnerError, OSError) as error:
        parser().error(str(error))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
