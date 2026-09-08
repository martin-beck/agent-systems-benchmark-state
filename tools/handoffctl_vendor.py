#!/usr/bin/env python3
"""Create and verify self-contained handoffctl vendor snapshots."""

import argparse
import hashlib
import json
import os
import re
import subprocess
import tempfile
from pathlib import Path
from typing import Any

UPSTREAM_REPOSITORY = "https://github.com/martin-beck/agent-workflow-coordinator"
LOCK_NAME = "coordinator.vendor.json"
SOURCE_FILES: tuple[tuple[str, str], ...] = (
    ("tools/handoffctl", "tools/handoffctl"),
    ("tools/handoffctl.py", "tools/handoffctl.py"),
    ("tools/status_renderer.py", "tools/status_renderer.py"),
    ("tools/vendor.py", "tools/handoffctl_vendor.py"),
    ("tests/test_handoffctl.py", "tests/test_handoffctl.py"),
    (
        "schema/project-config.schema.json",
        "schema/handoffctl-project-config.schema.json",
    ),
    (
        "schema/project-binding.schema.json",
        "schema/handoffctl-project-binding.schema.json",
    ),
    ("formal/handoffctl/Handoffctl.tla", "formal/handoffctl/Handoffctl.tla"),
    ("formal/handoffctl/Handoffctl.cfg", "formal/handoffctl/Handoffctl.cfg"),
    ("formal/handoffctl/HandoffctlLocks.tla", "formal/handoffctl/HandoffctlLocks.tla"),
    ("formal/handoffctl/HandoffctlLocks.cfg", "formal/handoffctl/HandoffctlLocks.cfg"),
    ("formal/handoffctl/HandoffctlRun.tla", "formal/handoffctl/HandoffctlRun.tla"),
    ("formal/handoffctl/HandoffctlRun.cfg", "formal/handoffctl/HandoffctlRun.cfg"),
    ("formal/handoffctl/README.md", "formal/handoffctl/README.md"),
    ("formal/handoffctl/verify.sh", "formal/handoffctl/verify.sh"),
    ("formal/handoffctl/HandoffctlBinding.tla", "formal/handoffctl/HandoffctlBinding.tla"),
    ("formal/handoffctl/HandoffctlBinding.cfg", "formal/handoffctl/HandoffctlBinding.cfg"),
    ("docs/PROJECT_GUIDE.md", "docs/agent-workflow-coordinator.md"),
    ("LICENSE", "vendor/agent-workflow-coordinator/LICENSE"),
)
VERSION_PATTERN = re.compile(r"v\d+\.\d+\.\d+")
COMMIT_PATTERN = re.compile(r"[0-9a-f]{40}")


def sha256(path: Path) -> str:
    """Return a lowercase SHA-256 digest for one regular file."""
    if not path.is_file() or path.is_symlink():
        raise RuntimeError(f"vendor source is not a regular file: {path}")
    return hashlib.sha256(path.read_bytes()).hexdigest()


def atomic_bytes(path: Path, content: bytes, mode: int = 0o644) -> None:
    """Atomically replace one destination without following a destination symlink."""
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.is_symlink():
        raise RuntimeError(f"refusing symlink destination: {path}")
    descriptor, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
        temporary_path = Path(temporary)
        temporary_path.chmod(mode)
        temporary_path.replace(path)
    finally:
        Path(temporary).unlink(missing_ok=True)


def git_output(source: Path, *args: str) -> str:
    """Run a bounded, read-only Git query for release identity."""
    result = subprocess.run(
        ["git", "-C", str(source), *args],
        check=True,
        capture_output=True,
        text=True,
        timeout=30,
    )
    return result.stdout.strip()


def release_identity(source: Path, version: str) -> str:
    """Require a clean source tree whose HEAD carries the requested release tag."""
    if not VERSION_PATTERN.fullmatch(version):
        raise RuntimeError("version must have the form vMAJOR.MINOR.PATCH")
    if git_output(source, "status", "--porcelain"):
        raise RuntimeError("upstream source must be clean before vendoring")
    commit = git_output(source, "rev-parse", "HEAD")
    tags = git_output(source, "tag", "--points-at", "HEAD").splitlines()
    if version not in tags:
        raise RuntimeError(f"HEAD is not tagged {version}")
    if not COMMIT_PATTERN.fullmatch(commit):
        raise RuntimeError("upstream HEAD is not a full commit identifier")
    return commit


def build_lock(source: Path, version: str, commit: str) -> dict[str, Any]:
    """Build a deterministic manifest for an immutable upstream release."""
    if not VERSION_PATTERN.fullmatch(version) or not COMMIT_PATTERN.fullmatch(commit):
        raise RuntimeError("invalid release version or commit")
    files: dict[str, dict[str, str]] = {}
    for source_name, destination_name in SOURCE_FILES:
        source_path = source / source_name
        files[destination_name] = {"source": source_name, "sha256": sha256(source_path)}
    return {
        "schema_version": 1,
        "upstream": {
            "repository": UPSTREAM_REPOSITORY,
            "version": version,
            "commit": commit,
        },
        "files": files,
    }


def install_staged_snapshot(staged: Path, target: Path, destinations: list[str]) -> None:
    """Install one fully staged vendor set and roll back failed rename sequences."""
    backup_root = staged / ".backup"
    installed: list[tuple[Path, Path, bool]] = []
    try:
        for destination_name in destinations:
            destination = target / destination_name
            source = staged / destination_name
            backup = backup_root / destination_name
            destination.parent.mkdir(parents=True, exist_ok=True)
            if destination.is_symlink():
                raise RuntimeError(f"refusing symlink destination: {destination}")
            existed = destination.exists()
            if existed:
                backup.parent.mkdir(parents=True, exist_ok=True)
                destination.replace(backup)
            installed.append((destination, backup, existed))
            source.replace(destination)
    except Exception:
        for destination, backup, existed in reversed(installed):
            destination.unlink(missing_ok=True)
            if existed and backup.exists():
                backup.replace(destination)
        raise


def sync(source: Path, target: Path, version: str, commit: str) -> None:
    """Stage and transactionally install an allowlisted immutable release."""
    manifest = build_lock(source, version, commit)
    target.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".handoffctl-vendor-", dir=target) as temporary:
        staged = Path(temporary)
        for source_name, destination_name in SOURCE_FILES:
            source_path = source / source_name
            mode = source_path.stat().st_mode & 0o777
            atomic_bytes(staged / destination_name, source_path.read_bytes(), mode)
        payload = json.dumps(manifest, indent=2, sort_keys=True).encode() + b"\n"
        atomic_bytes(staged / LOCK_NAME, payload)
        destinations = [destination for _, destination in SOURCE_FILES]
        install_staged_snapshot(staged, target, [*destinations, LOCK_NAME])
    verify(target)


def load_lock(target: Path) -> dict[str, Any]:
    """Load a strict vendor lock manifest."""
    path = target / LOCK_NAME
    try:
        value = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as error:
        raise RuntimeError(f"cannot read {LOCK_NAME}: {error}") from error
    if not isinstance(value, dict) or set(value) != {"schema_version", "upstream", "files"}:
        raise RuntimeError("invalid vendor lock structure")
    if value["schema_version"] != 1:
        raise RuntimeError("unsupported vendor lock schema")
    return value


def verify(target: Path) -> None:
    """Fail unless every pinned downstream artifact matches its recorded digest."""
    manifest = load_lock(target)
    upstream = manifest["upstream"]
    if not isinstance(upstream, dict) or set(upstream) != {"repository", "version", "commit"}:
        raise RuntimeError("invalid upstream identity in vendor lock")
    if upstream["repository"] != UPSTREAM_REPOSITORY:
        raise RuntimeError("unexpected upstream repository")
    if not VERSION_PATTERN.fullmatch(str(upstream["version"])) or not COMMIT_PATTERN.fullmatch(
        str(upstream["commit"])
    ):
        raise RuntimeError("invalid pinned upstream version or commit")
    files = manifest["files"]
    expected = {destination: source for source, destination in SOURCE_FILES}
    if not isinstance(files, dict) or set(files) != set(expected):
        raise RuntimeError("vendor file set differs from this verifier")
    for destination, source in expected.items():
        entry = files[destination]
        if not isinstance(entry, dict) or set(entry) != {"source", "sha256"}:
            raise RuntimeError(f"invalid vendor entry: {destination}")
        if entry["source"] != source or entry["sha256"] != sha256(target / destination):
            raise RuntimeError(f"vendor digest mismatch: {destination}")
    core = (target / "tools/handoffctl.py").read_text()
    expected_version = str(upstream["version"]).removeprefix("v")
    if f'COORDINATOR_VERSION = "{expected_version}"' not in core:
        raise RuntimeError("runtime version differs from vendor lock")
    print(f"OK: agent-workflow-coordinator {upstream['version']} at {upstream['commit']}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    sync_parser = commands.add_parser("sync", help="vendor a clean tagged local release")
    sync_parser.add_argument("--source", type=Path, required=True)
    sync_parser.add_argument("--target", type=Path, required=True)
    sync_parser.add_argument("--version", required=True)
    verify_parser = commands.add_parser("verify", help="verify an existing offline vendor pin")
    verify_parser.add_argument("--target", type=Path, default=Path.cwd())
    args = parser.parse_args()
    if args.command == "sync":
        commit = release_identity(args.source, args.version)
        sync(args.source, args.target, args.version, commit)
    else:
        verify(args.target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
