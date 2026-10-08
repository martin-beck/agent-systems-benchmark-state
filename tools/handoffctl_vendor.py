#!/usr/bin/env python3
# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Create and verify self-contained handoffctl vendor snapshots."""

import argparse
import ast
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
    ("tools/runtime_bootstrap.py", "tools/runtime_bootstrap.py"),
    ("tools/upgrade_authority.py", "tools/upgrade_authority.py"),
    ("tools/admission_lease.py", "tools/admission_lease.py"),
    ("tools/board_metrics.py", "tools/board_metrics.py"),
    ("tools/oracle_lifecycle.py", "tools/oracle_lifecycle.py"),
    ("tools/sqlite_storage.py", "tools/sqlite_storage.py"),
    ("tools/lifecycle_trace.py", "tools/lifecycle_trace.py"),
    ("tools/lock_domain.py", "tools/lock_domain.py"),
    ("tools/lock_domain_scope.py", "tools/lock_domain_scope.py"),
    ("tools/mutation_fence.py", "tools/mutation_fence.py"),
    ("tools/rollback_control_store.py", "tools/rollback_control_store.py"),
    ("tools/sqlite_wal_lifecycle.py", "tools/sqlite_wal_lifecycle.py"),
    ("tools/rollback_evidence.py", "tools/rollback_evidence.py"),
    ("tools/upgrade_identity.py", "tools/upgrade_identity.py"),
    ("tools/session_records.py", "tools/session_records.py"),
    ("tools/checkpoint_records.py", "tools/checkpoint_records.py"),
    ("tools/rollback_records.py", "tools/rollback_records.py"),
    ("tools/directive_records.py", "tools/directive_records.py"),
    ("tools/hierarchy.py", "tools/hierarchy.py"),
    ("tools/status_renderer.py", "tools/status_renderer.py"),
    ("tools/task_spec.py", "tools/task_spec.py"),
    ("tools/upgrade_commands.py", "tools/upgrade_commands.py"),
    ("tools/upgrade_binding.py", "tools/upgrade_binding.py"),
    ("tools/production_upgrade_binding.py", "tools/production_upgrade_binding.py"),
    ("tools/upgrade_contract_runtime.py", "tools/upgrade_contract_runtime.py"),
    ("tools/tlc_runner.py", "tools/tlc_runner.py"),
    ("tools/vendor.py", "tools/handoffctl_vendor.py"),
    ("tests/test_handoffctl.py", "tests/test_handoffctl.py"),
    ("tests/test_sqlite_storage.py", "tests/test_sqlite_storage.py"),
    ("tests/test_session_records.py", "tests/test_session_records.py"),
    ("tests/test_checkpoint_records.py", "tests/test_checkpoint_records.py"),
    ("tests/test_hierarchy.py", "tests/test_hierarchy.py"),
    ("tests/test_tlc_runner.py", "tests/test_tlc_runner.py"),
    (
        "schema/project-config.schema.json",
        "schema/handoffctl-project-config.schema.json",
    ),
    (
        "schema/project-binding.schema.json",
        "schema/handoffctl-project-binding.schema.json",
    ),
    (
        "schema/backend-config.schema.json",
        "schema/handoffctl-backend-config.schema.json",
    ),
    (
        "schema/upgrade-contract.schema.json",
        "schema/handoffctl-upgrade-contract.schema.json",
    ),
    ("schema/session-record.schema.json", "schema/handoffctl-session-record.schema.json"),
    (
        "schema/checkpoint-record.schema.json",
        "schema/handoffctl-checkpoint-record.schema.json",
    ),
    (
        "schema/rollback-record.schema.json",
        "schema/handoffctl-rollback-record.schema.json",
    ),
    (
        "schema/directive-record.schema.json",
        "schema/handoffctl-directive-record.schema.json",
    ),
    ("schema/task-record.schema.json", "schema/task-record.schema.json"),
    ("docs/PROJECT_GUIDE.md", "docs/agent-workflow-coordinator.md"),
    ("formal/evidence.json", "formal/evidence.json"),
    ("formal/tier-evidence.json", "formal/tier-evidence.json"),
    ("formal/handoffctl/Handoffctl.cfg", "formal/handoffctl/Handoffctl.cfg"),
    ("formal/handoffctl/Handoffctl.tla", "formal/handoffctl/Handoffctl.tla"),
    ("formal/handoffctl/HandoffctlBinding.cfg", "formal/handoffctl/HandoffctlBinding.cfg"),
    ("formal/handoffctl/HandoffctlBinding.tla", "formal/handoffctl/HandoffctlBinding.tla"),
    ("formal/handoffctl/HandoffctlFast.cfg", "formal/handoffctl/HandoffctlFast.cfg"),
    ("formal/handoffctl/HandoffctlLocks.cfg", "formal/handoffctl/HandoffctlLocks.cfg"),
    ("formal/handoffctl/HandoffctlLocks.tla", "formal/handoffctl/HandoffctlLocks.tla"),
    ("formal/handoffctl/HandoffctlPR.cfg", "formal/handoffctl/HandoffctlPR.cfg"),
    ("formal/handoffctl/HandoffctlRecovery.cfg", "formal/handoffctl/HandoffctlRecovery.cfg"),
    ("formal/handoffctl/HandoffctlRecovery.tla", "formal/handoffctl/HandoffctlRecovery.tla"),
    ("formal/handoffctl/HandoffctlRun.cfg", "formal/handoffctl/HandoffctlRun.cfg"),
    ("formal/handoffctl/HandoffctlRun.tla", "formal/handoffctl/HandoffctlRun.tla"),
    ("formal/handoffctl/HandoffctlStorage.cfg", "formal/handoffctl/HandoffctlStorage.cfg"),
    ("formal/handoffctl/HandoffctlStorage.tla", "formal/handoffctl/HandoffctlStorage.tla"),
    (
        "formal/handoffctl/LIFECYCLE_CORRESPONDENCE.md",
        "formal/handoffctl/LIFECYCLE_CORRESPONDENCE.md",
    ),
    ("formal/handoffctl/README.md", "formal/handoffctl/README.md"),
    ("formal/handoffctl/attest.py", "formal/handoffctl/attest.py"),
    ("formal/handoffctl/verify.sh", "formal/handoffctl/verify.sh"),
    ("formal/oracle/OracleInteractionGates.cfg", "formal/oracle/OracleInteractionGates.cfg"),
    ("formal/oracle/OracleInteractionGates.tla", "formal/oracle/OracleInteractionGates.tla"),
    ("LICENSE", "vendor/agent-workflow-coordinator/LICENSE"),
)
VERSION_PATTERN = re.compile(r"v\d+\.\d+\.\d+")
COMMIT_PATTERN = re.compile(r"[0-9a-f]{40}")
RUNTIME_VERSION_PATTERN = re.compile(r"^COORDINATOR_VERSION = \"(\d+\.\d+\.\d+)\"$", re.MULTILINE)


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


def git_bytes(source: Path, *args: str) -> bytes:
    """Read immutable Git object bytes with a bounded subprocess."""
    result = subprocess.run(
        ["git", "-C", str(source), *args],
        check=True,
        capture_output=True,
        timeout=30,
    )
    return result.stdout


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


def development_identity(source: Path, commit: str) -> str:
    """Bind an untagged development snapshot to one clean exact commit and tree."""
    if not COMMIT_PATTERN.fullmatch(commit):
        raise RuntimeError("development commit must be a full commit identifier")
    top_level = Path(git_output(source, "rev-parse", "--show-toplevel")).resolve()
    if top_level != source.resolve():
        raise RuntimeError("development source must be the Git worktree root")
    if git_output(source, "status", "--porcelain"):
        raise RuntimeError("upstream source must be clean before vendoring")
    head = git_output(source, "rev-parse", "HEAD")
    if head != commit:
        raise RuntimeError("upstream HEAD differs from the requested development commit")
    tree = git_output(source, "rev-parse", "HEAD^{tree}")
    if not COMMIT_PATTERN.fullmatch(tree):
        raise RuntimeError("upstream development tree is not a full object identifier")
    return tree


def runtime_version(content: bytes) -> str:
    """Read the Coordinator version from one immutable runtime payload."""
    try:
        runtime = content.decode("utf-8")
    except UnicodeDecodeError as error:
        raise RuntimeError("coordinator runtime is not UTF-8") from error
    version_match = RUNTIME_VERSION_PATTERN.search(runtime)
    if version_match is None:
        raise RuntimeError("cannot determine coordinator runtime version")
    return f"v{version_match.group(1)}"


def git_blob_payload(source: Path, commit: str, source_name: str) -> tuple[bytes, int]:
    """Return one regular file payload and mode from an exact commit tree."""
    record = git_output(source, "ls-tree", commit, "--", source_name)
    try:
        metadata, name = record.split("\t", 1)
        mode, kind, _object_id = metadata.split(" ", 2)
    except ValueError as error:
        raise RuntimeError(f"invalid Git tree entry: {source_name}") from error
    if name != source_name or kind != "blob" or mode not in {"100644", "100755"}:
        raise RuntimeError(f"vendor source is not a regular committed file: {source_name}")
    return git_bytes(source, "cat-file", "blob", f"{commit}:{source_name}"), int(mode[-3:], 8)


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


def development_snapshot(
    source: Path, commit: str
) -> tuple[dict[str, Any], dict[str, tuple[bytes, int]]]:
    """Build one exact development manifest and its immutable Git payloads."""
    tree = development_identity(source, commit)
    payloads = {
        source_name: git_blob_payload(source, commit, source_name)
        for source_name, _destination_name in SOURCE_FILES
    }
    try:
        version = runtime_version(payloads["tools/handoffctl.py"][0])
    except KeyError as error:
        raise RuntimeError("development snapshot omits tools/handoffctl.py") from error
    files = {
        destination_name: {
            "source": source_name,
            "sha256": hashlib.sha256(payloads[source_name][0]).hexdigest(),
        }
        for source_name, destination_name in SOURCE_FILES
    }
    return (
        {
            "schema_version": 2,
            "upstream": {
                "repository": UPSTREAM_REPOSITORY,
                "version": version,
                "commit": commit,
                "channel": "development",
                "tree": tree,
            },
            "files": files,
        },
        payloads,
    )


def build_development_lock(source: Path, commit: str) -> dict[str, Any]:
    """Build a manifest explicitly classified as an exact development snapshot."""
    return development_snapshot(source, commit)[0]


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


def install_snapshot(
    source: Path,
    target: Path,
    manifest: dict[str, Any],
    payloads: dict[str, tuple[bytes, int]] | None = None,
) -> None:
    """Stage and transactionally install one prevalidated vendor manifest."""
    target.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".handoffctl-vendor-", dir=target) as temporary:
        staged = Path(temporary)
        for source_name, destination_name in SOURCE_FILES:
            if payloads is None:
                source_path = source / source_name
                content = source_path.read_bytes()
                mode = source_path.stat().st_mode & 0o777
            else:
                content, mode = payloads[source_name]
            atomic_bytes(staged / destination_name, content, mode)
        payload = json.dumps(manifest, indent=2, sort_keys=True).encode() + b"\n"
        atomic_bytes(staged / LOCK_NAME, payload)
        destinations = [destination for _, destination in SOURCE_FILES]
        verify(staged)
        install_staged_snapshot(staged, target, [*destinations, LOCK_NAME])


def sync(source: Path, target: Path, version: str, commit: str) -> None:
    """Stage and transactionally install an allowlisted immutable release."""
    install_snapshot(source, target, build_lock(source, version, commit))


def sync_development(source: Path, target: Path, commit: str) -> None:
    """Install a clean untagged development head with exact commit and tree identity."""
    manifest, payloads = development_snapshot(source, commit)
    install_snapshot(source, target, manifest, payloads)


def load_lock(target: Path) -> dict[str, Any]:
    """Load a strict vendor lock manifest."""
    path = target / LOCK_NAME
    try:
        value = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as error:
        raise RuntimeError(f"cannot read {LOCK_NAME}: {error}") from error
    if not isinstance(value, dict) or set(value) != {"schema_version", "upstream", "files"}:
        raise RuntimeError("invalid vendor lock structure")
    if value["schema_version"] not in {1, 2}:
        raise RuntimeError("unsupported vendor lock schema")
    return value


def validated_upstream_identity(manifest: dict[str, Any]) -> dict[str, Any]:
    """Return one strict release or development upstream identity."""
    upstream = manifest["upstream"]
    expected_upstream = {"repository", "version", "commit"}
    if manifest["schema_version"] == 2:
        expected_upstream.update({"channel", "tree"})
    if not isinstance(upstream, dict) or set(upstream) != expected_upstream:
        raise RuntimeError("invalid upstream identity in vendor lock")
    if upstream["repository"] != UPSTREAM_REPOSITORY:
        raise RuntimeError("unexpected upstream repository")
    if not VERSION_PATTERN.fullmatch(str(upstream["version"])) or not COMMIT_PATTERN.fullmatch(
        str(upstream["commit"])
    ):
        raise RuntimeError("invalid pinned upstream version or commit")
    if manifest["schema_version"] == 2 and (
        upstream["channel"] != "development" or not COMMIT_PATTERN.fullmatch(str(upstream["tree"]))
    ):
        raise RuntimeError("invalid development channel or tree identity")
    return upstream


def _literal_string_tuple(tree: ast.Module, name: str) -> set[str]:
    """Read one exact tuple of string literals without executing vendored code."""
    for statement in tree.body:
        if (
            isinstance(statement, ast.Assign)
            and any(
                isinstance(target, ast.Name) and target.id == name for target in statement.targets
            )
            and isinstance(statement.value, (ast.Tuple, ast.List))
        ):
            values = statement.value.elts
            literals: set[str] = set()
            for value in values:
                if not isinstance(value, ast.Constant) or not isinstance(value.value, str):
                    break
                literals.add(value.value)
            else:
                return literals
    raise RuntimeError("formal lifecycle runtime inventory is missing or malformed")


def verify_formal_lifecycle_alignment(target: Path) -> None:
    """Reject a vendor snapshot whose runtime and lifecycle model actions drift."""
    try:
        runtime = ast.parse((target / "tools/handoffctl.py").read_text(encoding="utf-8"))
        model = (target / "formal/handoffctl/Handoffctl.tla").read_text(encoding="utf-8")
    except (OSError, SyntaxError) as error:
        raise RuntimeError("formal lifecycle inputs are unreadable") from error
    runtime_operations = _literal_string_tuple(runtime, "LIFECYCLE_MUTATION_COMMANDS")
    blocks = re.findall(
        r"(?:ReleaseOperations|Operations)\s*==\s*(.*?)(?=\n\n[A-Za-z])",
        model,
        flags=re.DOTALL,
    )
    if len(blocks) < 2:
        raise RuntimeError("formal lifecycle operation inventory is missing or malformed")
    modeled = set(re.findall(r'"([a-z_]+)"', "\n".join(blocks[:2])))
    model_operations = {
        (
            "release"
            if item.startswith("release_")
            else "recover-expired"
            if item == "recover_expired"
            else item
        )
        for item in modeled
    }
    if runtime_operations != model_operations:
        raise RuntimeError("formal lifecycle operation drift")


def verify(target: Path) -> None:
    """Fail unless every pinned downstream artifact matches its recorded digest."""
    manifest = load_lock(target)
    upstream = validated_upstream_identity(manifest)
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
    if "formal/handoffctl/Handoffctl.tla" in expected:
        verify_formal_lifecycle_alignment(target)
    print(f"OK: agent-workflow-coordinator {upstream['version']} at {upstream['commit']}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    sync_parser = commands.add_parser("sync", help="vendor a clean tagged local release")
    sync_parser.add_argument("--source", type=Path, required=True)
    sync_parser.add_argument("--target", type=Path, required=True)
    sync_parser.add_argument("--version", required=True)
    development_parser = commands.add_parser(
        "sync-development", help="vendor a clean local development head at one exact commit"
    )
    development_parser.add_argument("--source", type=Path, required=True)
    development_parser.add_argument("--target", type=Path, required=True)
    development_parser.add_argument("--commit", required=True)
    verify_parser = commands.add_parser("verify", help="verify an existing offline vendor pin")
    verify_parser.add_argument("--target", type=Path, default=Path.cwd())
    args = parser.parse_args()
    if args.command == "sync":
        commit = release_identity(args.source, args.version)
        sync(args.source, args.target, args.version, commit)
    elif args.command == "sync-development":
        sync_development(args.source, args.target, args.commit)
    else:
        verify(args.target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
