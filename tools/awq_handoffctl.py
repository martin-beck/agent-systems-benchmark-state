#!/usr/bin/env python3
# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""ASB coordinator launcher with downstream projection hygiene.

The Coordinator snapshot is immutable and is verified by its vendor manifest.
ASB-specific recovery therefore lives in this launcher rather than patching
``tools/handoffctl.py``.  The launcher preserves the Coordinator CLI while
adding a transaction around derived projection publication.
"""

from __future__ import annotations

import importlib.util
import json
import os
import sys
import tempfile
import uuid
from pathlib import Path
from types import ModuleType
from typing import Any

os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parents[1]
VENDORED = ROOT / "tools" / "handoffctl.py"


def _load_core() -> ModuleType:
    spec = importlib.util.spec_from_file_location("_asb_vendored_handoffctl", VENDORED)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load the pinned Coordinator handoffctl snapshot")
    module = importlib.util.module_from_spec(spec)
    sys.path.insert(0, str(VENDORED.parent))
    spec.loader.exec_module(module)
    return module


def _stage_entry(
    core: ModuleType, runtime: Path, target: Path, text: str | None
) -> tuple[dict[str, str | None], Path | None]:
    if target.resolve().parent != target.parent.resolve():
        raise RuntimeError("projection target escapes its configured directory")
    temporary: Path | None = None
    if text is not None:
        fd, name = tempfile.mkstemp(prefix=f".{target.name}.", dir=target.parent)
        temporary = Path(name)
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            stream.write(text)
            stream.flush()
            os.fsync(stream.fileno())
        temporary.chmod(0o600)
    backup: Path | None = None
    if target.exists():
        backup = runtime / f"asb-projection-backup-{uuid.uuid4().hex}"
        backup.write_bytes(target.read_bytes())
        backup.chmod(0o600)
    return (
        {
            "target": str(target.relative_to(core.ROOT)),
            "staged": str(temporary) if temporary else None,
            "backup": str(backup) if backup else None,
        },
        temporary,
    )


def _publish_entries(core: ModuleType, marker: Path, entries: list[dict[str, str | None]]) -> None:
    core.atomic(marker, json.dumps({"entries": entries}, sort_keys=True))
    for entry in entries:
        target = core.ROOT / str(entry["target"])
        replacement = entry["staged"]
        target.unlink(missing_ok=True) if replacement is None else Path(replacement).replace(target)
    marker.unlink(missing_ok=True)
    for entry in entries:
        if entry["backup"]:
            Path(str(entry["backup"])).unlink(missing_ok=True)


def _publish_transaction(core: ModuleType, contents: dict[Path, str | None]) -> None:
    """Publish a matched derived-view set with restart recovery."""
    if not contents:
        return
    runtime = core.RUNTIME
    runtime.mkdir(mode=0o700, parents=True, exist_ok=True)
    marker = runtime / "asb-projection-transaction.json"
    entries: list[dict[str, str | None]] = []
    staged: list[Path] = []
    try:
        for target, text in contents.items():
            entry, temporary = _stage_entry(core, runtime, target, text)
            entries.append(entry)
            if temporary:
                staged.append(temporary)
        _publish_entries(core, marker, entries)
    except Exception:
        _recover_transaction(core)
        raise
    finally:
        for path in staged:
            path.unlink(missing_ok=True)


def _recover_transaction(core: ModuleType) -> None:
    marker = core.RUNTIME / "asb-projection-transaction.json"
    if not marker.exists():
        return
    try:
        entries: Any = json.loads(marker.read_text(encoding="utf-8"))["entries"]
        if not isinstance(entries, list):
            raise ValueError("entries is not a list")
        for entry in entries:
            target = core.ROOT / str(entry["target"])
            backup = entry.get("backup")
            if backup:
                core.atomic(target, Path(str(backup)).read_text(encoding="utf-8"))
                Path(str(backup)).unlink(missing_ok=True)
            else:
                target.unlink(missing_ok=True)
            if entry.get("staged"):
                Path(str(entry["staged"])).unlink(missing_ok=True)
        marker.unlink(missing_ok=True)
    except (OSError, KeyError, TypeError, ValueError) as error:
        raise RuntimeError("PROJECTION_RECOVERY_FAILED: inspect the transaction marker") from error


def _install_projection_policy(core: ModuleType) -> None:
    original = core.write_generated_views

    def write_generated_views(tasks: Any, state: Any) -> None:
        _recover_transaction(core)
        contents: dict[Path, str | None] = {core.ROOT / "CURRENT.md": core.render_current(tasks)}
        if core.project_settings()["status_view"]:
            expected = core.render_status_views(tasks)
            contents.update({core.ROOT / relative: text for relative, text in expected.items()})
            expected_paths = {core.ROOT / relative for relative in expected}
            contents.update(
                {
                    path: None
                    for path in core.generated_paths()
                    if path not in expected_paths
                    and (path.name == "STATUS.md" or path.parent.name == "status")
                }
            )
        project, worktrees = core.live_docs(state)
        contents[core.ROOT / "PROJECT_STATE.md"] = project
        contents[core.ROOT / "WORKTREES.md"] = worktrees
        _publish_transaction(core, contents)

    core.write_generated_views = write_generated_views
    core._asb_original_write_generated_views = original


def main() -> int:
    core = _load_core()
    _install_projection_policy(core)
    _recover_transaction(core)
    return int(core.main())


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RuntimeError as error:
        sys.stderr.write(f"ERROR: {error}\n")
        raise SystemExit(1) from error
