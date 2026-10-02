# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Create and verify complete, offline Git-backend backup artifacts."""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import tarfile
import tempfile
from pathlib import Path, PurePosixPath

from tools.lifecycle_session import LifecycleSession

ARTIFACTS = ("authority.bundle", "tracked-tree.tar", "refs.txt", "index.txt", "tracked-files.txt")
MANIFEST_FIELDS = {"schema_version", "commit", "quiesced", "artifacts"}


class BackupError(RuntimeError):
    """Raised when a backup is incomplete, corrupt, or unsafe to restore."""


def _check_lifecycle_session(session: LifecycleSession | None, path: Path, message: str) -> None:
    if session is not None and session.capture_identity() != (
        path.stat().st_dev,
        path.stat().st_ino,
    ):
        raise BackupError(message)


def _run(args: list[str], cwd: Path) -> str:
    try:
        return subprocess.check_output(  # noqa: S603
            args, cwd=cwd, text=True, stderr=subprocess.STDOUT
        )
    except (OSError, subprocess.CalledProcessError) as error:  # pragma: no cover
        detail = getattr(error, "output", "")
        raise BackupError(f"Git backup command failed: {args[0]}: {detail}") from error


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _clean(repo: Path) -> None:
    status = _run(["git", "status", "--porcelain=1", "--untracked-files=all"], repo)
    if status:
        raise BackupError("Git authority must be clean and quiesced")


def _safe_root(path: Path, label: str) -> None:
    if path.is_symlink():
        raise BackupError(f"{label} must not be a symlink")
    if path.exists() and not path.is_dir():
        raise BackupError(f"{label} must be a directory")  # pragma: no cover


def _safe_parent(path: Path, label: str) -> None:
    """Reject symlinked parent components before creating or publishing output."""
    resolved = path.absolute()
    current = Path(resolved.anchor)
    for component in resolved.parts[1:-1]:
        current /= component
        if current.is_symlink():
            raise BackupError(f"{label} parent must not contain symlinks")


def _parent_identity(path: Path) -> tuple[int, int]:
    try:
        status = path.parent.stat()
    except OSError as error:
        raise BackupError("Git restore destination parent disappeared") from error
    return status.st_dev, status.st_ino


def _source_state(
    repo: Path, observed_path: Path | None = None
) -> tuple[int, int, int, int, str, str, str]:
    status = repo.stat()
    observed = (observed_path or repo).stat()
    head = _run(["git", "rev-parse", "HEAD"], repo).strip()
    branch = _run(["git", "symbolic-ref", "--short", "-q", "HEAD"], repo).strip()
    clean = _run(["git", "status", "--porcelain=1", "--untracked-files=all"], repo)
    return status.st_dev, status.st_ino, observed.st_dev, observed.st_ino, head, branch, clean


def _assert_source_state(
    repo: Path,
    observed_path: Path,
    expected: tuple[int, int, int, int, str, str, str],
) -> None:
    if _source_state(repo, observed_path) != expected:
        raise BackupError("Git source authority changed during backup")


def _valid_hex(value: object, length: int) -> bool:
    return (
        isinstance(value, str)
        and len(value) == length
        and all(character in "0123456789abcdef" for character in value)
    )


def _validate_artifact_metadata(name: str, metadata: object) -> None:
    if not isinstance(metadata, dict) or set(metadata) != {"sha256", "size"}:
        raise BackupError(f"backup manifest metadata is invalid: {name}")
    if not _valid_hex(metadata["sha256"], 64):
        raise BackupError(f"backup manifest hash is invalid: {name}")  # pragma: no cover
    if (
        not isinstance(metadata["size"], int)
        or isinstance(metadata["size"], bool)
        or metadata["size"] < 0
    ):
        raise BackupError(f"backup manifest size is invalid: {name}")  # pragma: no cover


def _manifest(backup: Path) -> dict[str, object]:
    try:
        value = json.loads((backup / "manifest.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:  # pragma: no cover
        raise BackupError("invalid backup manifest") from error
    if not isinstance(value, dict) or set(value) != MANIFEST_FIELDS:
        raise BackupError("backup manifest has unknown or missing fields")
    if value.get("schema_version") != 1 or value.get("quiesced") is not True:
        raise BackupError("backup manifest has invalid contract fields")  # pragma: no cover
    commit = value.get("commit")
    artifacts = value.get("artifacts")
    if not _valid_hex(commit, 40):
        raise BackupError("backup manifest has invalid commit")  # pragma: no cover
    if not isinstance(artifacts, dict) or set(artifacts) != set(ARTIFACTS):
        raise BackupError("backup manifest artifact set is incomplete")  # pragma: no cover
    for name in ARTIFACTS:
        _validate_artifact_metadata(name, artifacts[name])
    return value


def _manifest_identity(path: Path) -> tuple[int, int]:
    """Return the identity of a regular manifest file without following links."""
    if path.is_symlink() or not path.is_file():
        raise BackupError("Git backup manifest must be a regular file")
    try:
        status = path.stat()
    except OSError as error:  # pragma: no cover - race-dependent
        raise BackupError("Git backup manifest disappeared") from error
    return status.st_dev, status.st_ino


def _verify_artifacts(backup: Path, manifest: dict[str, object]) -> None:
    artifacts = manifest["artifacts"]
    if not isinstance(artifacts, dict):
        raise BackupError("backup manifest artifacts are invalid")
    for name in ARTIFACTS:
        path = backup / name
        metadata = artifacts[name]
        if not isinstance(metadata, dict):
            raise BackupError(f"backup manifest metadata is invalid: {name}")
        if not path.is_file() or path.is_symlink():
            raise BackupError(f"backup artifact is missing or unsafe: {name}")
        if path.stat().st_size != metadata["size"] or _sha256(path) != metadata["sha256"]:
            raise BackupError(f"backup artifact integrity failure: {name}")


def _verify_archive(path: Path) -> None:
    try:
        with tarfile.open(path) as archive:
            for member in archive:
                name = PurePosixPath(member.name)
                if (
                    name.is_absolute()
                    or ".." in name.parts
                    or member.isdev()
                    or member.issym()
                    or member.islnk()
                ):
                    raise BackupError("backup archive contains unsafe entries")
    except (OSError, tarfile.TarError) as error:
        raise BackupError("backup archive cannot be verified") from error  # pragma: no cover


def _verify_archive_equivalence(path: Path, checkout: Path) -> None:
    """Ensure the traversal-safe archive contains exactly the clean checkout files."""
    try:
        with tarfile.open(path) as archive:
            members = archive.getmembers()
            file_members = [member for member in members if member.isfile()]
            names = [member.name for member in file_members]
            tracked = _run(["git", "ls-files"], checkout).splitlines()
            if names != tracked:
                raise BackupError("clean restore archive file set mismatch")
            for member in file_members:
                target = checkout / member.name
                if not target.is_file() or target.is_symlink():
                    raise BackupError("clean restore archive file is unsafe")
                source = archive.extractfile(member)
                if source is None or source.read() != target.read_bytes():
                    raise BackupError("clean restore archive content mismatch")
    except (OSError, tarfile.TarError) as error:  # pragma: no cover - filesystem-dependent
        raise BackupError("clean restore archive cannot be compared") from error


def _write_manifest(path: Path, value: dict[str, object]) -> None:
    temporary = path.with_name(f".{path.name}.tmp")
    try:
        with temporary.open("w", encoding="utf-8") as stream:
            stream.write(json.dumps(value, indent=2, sort_keys=True) + "\n")
            stream.flush()
            os.fsync(stream.fileno())
        temporary.replace(path)
        descriptor = os.open(path.parent, os.O_DIRECTORY)
        try:
            os.fsync(descriptor)
        finally:
            os.close(descriptor)
    except OSError as error:  # pragma: no cover
        temporary.unlink(missing_ok=True)
        raise BackupError(
            "atomic backup manifest publication failed"
        ) from error  # pragma: no cover


def create_backup(
    repo: Path, destination: Path, *, quiesced: bool, session: LifecycleSession | None = None
) -> Path:
    """Create complete immutable artifacts from a clean, quiesced authority."""
    if not quiesced:
        raise BackupError("Git backup requires a proven quiesced authority")
    observed_repo = repo
    repo = repo.resolve()
    _safe_root(destination, "backup destination")
    _safe_parent(destination, "backup destination")
    if destination.exists():
        raise BackupError("backup destination must not already exist")
    _clean(repo)
    _check_lifecycle_session(session, repo, "Git lifecycle session is not bound to repository")
    source_state = _source_state(repo, observed_repo)
    destination.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    parent_identity = _parent_identity(destination)
    if _parent_identity(destination) != parent_identity:
        raise BackupError("Git backup destination parent changed before allocation")
    try:
        temporary = Path(tempfile.mkdtemp(prefix=".git-backup-", dir=destination.parent))
    except OSError as error:
        raise BackupError("Git backup temporary allocation failed") from error
    try:
        bundle = temporary / "authority.bundle"
        archive = temporary / "tracked-tree.tar"
        refs = temporary / "refs.txt"
        index = temporary / "index.txt"
        tracked_files = temporary / "tracked-files.txt"
        _run(["git", "bundle", "create", str(bundle), "--all"], repo)
        refs.write_text(_run(["git", "show-ref"], repo), encoding="utf-8")
        index.write_text(_run(["git", "ls-files", "--stage"], repo), encoding="utf-8")
        tracked_files.write_text(_run(["git", "ls-files"], repo), encoding="utf-8")
        _run(["git", "archive", "--format=tar", "HEAD", "-o", str(archive)], repo)
        commit = _run(["git", "rev-parse", "HEAD"], repo).strip()
        manifest = {
            "schema_version": 1,
            "commit": commit,
            "quiesced": True,
            "artifacts": {
                name: {
                    "sha256": _sha256(temporary / name),
                    "size": (temporary / name).stat().st_size,
                }
                for name in ARTIFACTS
            },
        }
        _write_manifest(temporary / "manifest.json", manifest)
        _assert_source_state(repo, observed_repo, source_state)
        if _parent_identity(destination) != parent_identity:
            raise BackupError("Git backup destination parent changed before publication")
        if destination.exists() or destination.is_symlink():
            raise BackupError("Git backup destination appeared before publication")
        temporary.replace(destination)
        descriptor = os.open(destination.parent, os.O_DIRECTORY)
        try:
            os.fsync(descriptor)
        finally:
            os.close(descriptor)
    except (OSError, BackupError) as error:
        shutil.rmtree(temporary, ignore_errors=True)
        if isinstance(error, BackupError):  # pragma: no cover
            raise
        raise BackupError("Git backup publication failed") from error  # pragma: no cover
    return destination


def verify_backup(backup: Path) -> dict[str, object]:
    """Verify hashes, bundle reachability, refs, and clean-checkout equivalence."""
    _safe_root(backup, "backup")
    backup_identity = backup.stat()
    manifest_path = backup / "manifest.json"
    manifest_identity = _manifest_identity(manifest_path)
    manifest = _manifest(backup)
    manifest_digest = _sha256(manifest_path)
    _verify_artifacts(backup, manifest)
    _verify_archive(backup / "tracked-tree.tar")
    with tempfile.TemporaryDirectory(prefix="handoffctl-restore-") as directory:
        root = Path(directory)
        verifier = root / "verifier"
        _run(["git", "init", "-q", str(verifier)], root)
        _run(["git", "bundle", "verify", str(backup / "authority.bundle")], verifier)
        target = root / "checkout"
        _run(["git", "clone", str(backup / "authority.bundle"), str(target)], root)
        restored = _run(["git", "rev-parse", "HEAD"], target).strip()
        if restored != manifest["commit"]:
            raise BackupError("clean restore commit mismatch")
        expected_refs = set((backup / "refs.txt").read_text(encoding="utf-8").splitlines())
        actual_refs = set(_run(["git", "show-ref"], target).splitlines())
        if not expected_refs.issubset(actual_refs):
            raise BackupError("clean restore refs mismatch")  # pragma: no cover
        if _run(["git", "ls-files"], target) != (backup / "tracked-files.txt").read_text(
            encoding="utf-8"
        ):
            raise BackupError("clean restore tracked-file set mismatch")  # pragma: no cover
        if _run(["git", "ls-files", "--stage"], target) != (backup / "index.txt").read_text(
            encoding="utf-8"
        ):
            raise BackupError("clean restore index mismatch")
        _verify_archive_equivalence(backup / "tracked-tree.tar", target)
    _safe_root(backup, "backup")
    current_identity = backup.stat()
    if (current_identity.st_dev, current_identity.st_ino) != (
        backup_identity.st_dev,
        backup_identity.st_ino,
    ):
        raise BackupError("Git backup directory changed during verification")
    if _manifest_identity(manifest_path) != manifest_identity:
        raise BackupError("Git backup manifest changed during verification")
    if _sha256(manifest_path) != manifest_digest:
        raise BackupError("Git backup manifest changed during verification")
    _verify_artifacts(backup, manifest)
    return {"commit": manifest["commit"], "verified": True, "artifact_count": len(ARTIFACTS)}


def restore_backup(
    backup: Path, destination: Path, *, session: LifecycleSession | None = None
) -> None:
    """Verify completely, then restore into a new destination atomically."""
    _safe_root(backup, "backup")
    _check_lifecycle_session(session, backup, "Git lifecycle session is not bound to backup")
    backup_identity = backup.stat()
    verify_backup(backup)
    _safe_root(backup, "backup")
    current_identity = backup.stat()
    if (current_identity.st_dev, current_identity.st_ino) != (
        backup_identity.st_dev,
        backup_identity.st_ino,
    ):
        raise BackupError("Git backup directory changed before restore")
    _safe_root(destination, "restore destination")
    _safe_parent(destination, "restore destination")
    if destination.exists():
        raise BackupError("restore destination must not already exist")
    destination.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    parent_identity = _parent_identity(destination)
    if _parent_identity(destination) != parent_identity:
        raise BackupError("Git restore destination parent changed before allocation")
    temporary = Path(tempfile.mkdtemp(prefix=".git-restore-", dir=destination.parent))
    shutil.rmtree(temporary)
    try:
        _safe_root(backup, "backup")
        _check_lifecycle_session(session, backup, "Git lifecycle session changed before clone")
        current_identity = backup.stat()
        if (current_identity.st_dev, current_identity.st_ino) != (
            backup_identity.st_dev,
            backup_identity.st_ino,
        ):
            raise BackupError("Git backup directory changed before restore")
        _run(["git", "clone", str(backup / "authority.bundle"), str(temporary)], backup.parent)
        _check_lifecycle_session(
            session, backup, "Git lifecycle session changed before publication"
        )
        if _parent_identity(destination) != parent_identity:
            raise BackupError("Git restore destination parent changed before publication")
        if destination.exists() or destination.is_symlink():
            raise BackupError("restore destination appeared before publication")
        temporary.replace(destination)
        descriptor = os.open(destination.parent, os.O_DIRECTORY)
        try:
            os.fsync(descriptor)
        finally:
            os.close(descriptor)
    except (OSError, BackupError) as error:
        shutil.rmtree(temporary, ignore_errors=True)
        if isinstance(error, BackupError):  # pragma: no cover
            raise
        raise BackupError("Git restore publication failed") from error  # pragma: no cover
