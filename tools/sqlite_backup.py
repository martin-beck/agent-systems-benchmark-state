# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Fail-closed online backup and restore helpers for SQLite authority."""

from __future__ import annotations

import hashlib
import json
import os
import sqlite3
import stat
import tempfile
from pathlib import Path
from typing import Any

from tools.lifecycle_session import LifecycleSession

MANIFEST_VERSION = 1
MANIFEST_FIELDS = frozenset(
    {
        "schema_version",
        "kind",
        "database_sha256",
        "integrity_check",
        "foreign_key_check",
        "binding_verified",
        "wal_consistent",
    }
)


class BackupError(RuntimeError):
    """Raised when a SQLite backup or restore cannot be proven safe."""


def _check_session(
    session: LifecycleSession | None, owner: object | None, path: Path, message: str
) -> None:
    try:
        invalid = session is not None and (
            (owner is not None and not session.belongs_to(owner))
            or session.capture_identity() != _backup_identity(path)
        )
    except (OSError, ValueError) as error:
        raise BackupError(message) from error
    if invalid:
        raise BackupError(message)


def _regular(path: Path, label: str) -> None:
    if path.is_symlink() or not path.is_file():
        raise BackupError(f"{label} must be a regular file")


def _safe_parent(path: Path, label: str) -> None:
    """Reject symlinked lexical ancestors before allocating output files."""
    absolute = path.absolute()
    current = Path(absolute.anchor)
    for component in absolute.parts[1:-1]:
        current /= component
        if current.is_symlink():
            raise BackupError(f"{label} parent must not contain symlinks")


def _parent_identity(path: Path) -> tuple[int, int]:
    try:
        status = path.parent.stat()
    except OSError as error:
        raise BackupError("SQLite destination parent is unavailable") from error
    return status.st_dev, status.st_ino


def _assert_parent_identity(path: Path, expected: tuple[int, int]) -> None:
    if _parent_identity(path) != expected:
        raise BackupError("SQLite destination parent identity changed")


def _backup_identity(path: Path) -> tuple[int, int]:
    try:
        status = path.stat()
    except OSError as error:
        raise BackupError("backup database disappeared") from error
    return status.st_dev, status.st_ino


def _digest(path: Path) -> str:
    digest = hashlib.sha256()
    try:
        with path.open("rb") as stream:
            for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                digest.update(chunk)
    except OSError as error:
        raise BackupError("database disappeared while hashing") from error
    return digest.hexdigest()


def _binding(connection: sqlite3.Connection, expected: dict[str, Any]) -> None:
    try:
        rows = dict(connection.execute("SELECT key, value FROM metadata"))
    except sqlite3.Error as error:
        raise BackupError("backup database has no valid metadata table") from error
    required = {
        "schema_version": "1",
        "backend": "sqlite",
        "project_id": str(expected["project_id"]),
        "state_repository": str(expected["state_repository"]),
        "product_repository": str(expected["product_repository"]),
        "state": "active",
    }
    if any(rows.get(key) != value for key, value in required.items()):
        raise BackupError("backup database binding or active-state check failed")


def _integrity(path: Path, binding: dict[str, Any]) -> None:
    try:
        connection = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
        try:
            result = str(connection.execute("PRAGMA integrity_check").fetchone()[0])
            foreign = list(connection.execute("PRAGMA foreign_key_check"))
            _binding(connection, binding)
        finally:
            connection.close()
    except sqlite3.Error as error:
        raise BackupError("backup database cannot be opened for integrity verification") from error
    if result != "ok" or foreign:
        raise BackupError("backup database integrity verification failed")


def _fsync_directory(directory: Path) -> None:
    descriptor = os.open(directory, os.O_DIRECTORY)
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def _unlink(path: Path) -> None:
    try:
        path.unlink(missing_ok=True)
    except OSError as error:
        raise BackupError(f"failed to clean up temporary file {path.name}") from error


def _copy_online(source: Path, temporary: Path, binding: dict[str, Any]) -> None:
    source_connection: sqlite3.Connection | None = None
    destination_connection: sqlite3.Connection | None = None
    try:
        source_connection = sqlite3.connect(f"file:{source}?mode=ro", uri=True)
        destination_connection = sqlite3.connect(temporary)
        source_connection.backup(destination_connection, pages=64, sleep=0.05)
        destination_connection.commit()
    finally:
        if destination_connection is not None:
            destination_connection.close()
        if source_connection is not None:
            source_connection.close()
    _integrity(temporary, binding)


def _source_identity(source: Path) -> tuple[int, int]:
    if not source.exists():
        raise BackupError("source database disappeared")
    _regular(source, "source database")
    try:
        status = source.stat()
    except OSError as error:
        raise BackupError("source database disappeared") from error
    return status.st_dev, status.st_ino


def _backup_existing(destination: Path) -> Path | None:
    if not destination.exists():
        return None
    _regular(destination, "existing destination")
    try:
        destination_status = destination.stat()
    except OSError as error:
        raise BackupError("existing destination disappeared") from error
    destination_identity = (destination_status.st_dev, destination_status.st_ino)
    descriptor, previous = tempfile.mkstemp(
        prefix=".coordinator-previous-", suffix=".sqlite3", dir=destination.parent
    )
    os.close(descriptor)
    previous_path = Path(previous)
    try:
        previous_path.unlink()
        os.link(destination, previous_path)
        current_status = destination.stat()
        current_identity = (current_status.st_dev, current_status.st_ino)
        if current_identity != destination_identity:
            raise BackupError("existing destination changed during preservation")
    except (OSError, BackupError) as error:
        _unlink(previous_path)
        if isinstance(error, BackupError):
            raise
        raise BackupError("failed to preserve existing SQLite destination") from error
    return previous_path


def _destination_identity(destination: Path) -> tuple[int, int] | None:
    if not destination.exists():
        return None
    _regular(destination, "existing destination")
    try:
        status = destination.stat()
    except OSError as error:
        raise BackupError("existing destination disappeared") from error
    return status.st_dev, status.st_ino


def _manifest_identity(path: Path) -> tuple[int, int] | None:
    if not path.exists():
        return None
    _regular(path, "existing SQLite manifest")
    try:
        status = path.stat()
    except OSError as error:
        raise BackupError("existing SQLite manifest disappeared") from error
    return status.st_dev, status.st_ino


def _before_manifest_publish(_path: Path) -> None:
    """Test synchronization seam; production publication has no side effect."""


def _before_destination_publish(_destination: Path) -> None:
    """Test synchronization seam; production publication has no side effect."""


def _assert_no_sidecars(destination: Path) -> None:
    if Path(str(destination) + "-wal").exists() or Path(str(destination) + "-shm").exists():
        raise BackupError("SQLite destination sidecar appeared before publication")


def _sidecar_identity(path: Path, label: str) -> tuple[int, int] | None:
    try:
        status = path.lstat()
    except FileNotFoundError:
        return None
    except OSError as error:
        raise BackupError(f"{label} metadata is unavailable") from error
    if not stat.S_ISREG(status.st_mode) or status.st_uid != os.geteuid() or status.st_nlink != 1:
        raise BackupError(f"{label} is unsafe")
    return status.st_dev, status.st_ino


def _remove_sidecar(path: Path, expected: tuple[int, int], parent: tuple[int, int]) -> None:
    try:
        descriptor = os.open(path.parent, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
        try:
            parent_status = os.fstat(descriptor)
            if (parent_status.st_dev, parent_status.st_ino) != parent:
                raise BackupError("SQLite sidecar parent identity changed")
            current = _sidecar_identity(path, "SQLite sidecar")
            if current != expected:
                raise BackupError("SQLite sidecar identity changed")
            os.unlink(path.name, dir_fd=descriptor)
        finally:
            os.close(descriptor)
    except FileNotFoundError:
        raise BackupError("SQLite sidecar disappeared during cleanup") from None
    except OSError as error:
        raise BackupError("failed to remove checkpointed SQLite sidecar") from error


def _recover_checkpointed_sidecars(destination: Path) -> None:  # noqa: C901
    """Checkpoint and remove stale WAL/SHM files left by a dead writer.

    A killed SQLite writer can leave an empty WAL and a stale SHM file even
    after recovery has completed.  Restore is allowed to clean those files
    only after SQLite reports a successful zero-frame truncate checkpoint;
    any live or indeterminate sidecar remains a fail-closed refusal.
    """
    wal = Path(str(destination) + "-wal")
    shm = Path(str(destination) + "-shm")
    initial_wal = _sidecar_identity(wal, "SQLite WAL sidecar")
    initial_shm = _sidecar_identity(shm, "SQLite SHM sidecar")
    if initial_wal is None and initial_shm is None:
        return
    if not destination.exists() or destination.is_symlink():
        raise BackupError("restore requires a checkpointed destination without live WAL sidecars")
    parent_identity = _parent_identity(destination)
    destination_identity = _sidecar_identity(destination, "existing destination")
    if destination_identity is None:
        raise BackupError("existing destination is unavailable")
    try:
        if initial_wal is not None and wal.stat().st_size != 0:
            raise BackupError(
                "restore requires a checkpointed destination without live WAL sidecars"
            )
    except OSError as error:
        raise BackupError("restore requires safe SQLite sidecars") from error
    _regular(destination, "existing destination")
    try:
        connection = sqlite3.connect(destination)
        try:
            result = connection.execute("PRAGMA wal_checkpoint(TRUNCATE)").fetchone()
        finally:
            connection.close()
    except sqlite3.Error as error:
        raise BackupError("restore could not checkpoint destination WAL sidecars") from error
    if result != (0, 0, 0):
        raise BackupError("restore requires a checkpointed destination without live WAL sidecars")
    if _parent_identity(destination) != parent_identity:
        raise BackupError("SQLite sidecar parent identity changed")
    if _sidecar_identity(destination, "existing destination") != destination_identity:
        raise BackupError("existing destination identity changed")
    final_wal = _sidecar_identity(wal, "SQLite WAL sidecar")
    final_shm = _sidecar_identity(shm, "SQLite SHM sidecar")
    if (
        (initial_wal is None and final_wal is not None)
        or (initial_shm is None and final_shm is not None)
        or (initial_wal is not None and final_wal is not None and initial_wal != final_wal)
        or (initial_shm is not None and final_shm is not None and initial_shm != final_shm)
    ):
        raise BackupError("SQLite sidecar identity changed")
    try:
        if final_wal is not None:
            _remove_sidecar(wal, final_wal, parent_identity)
        if final_shm is not None:
            _remove_sidecar(shm, final_shm, parent_identity)
        if final_wal is not None or final_shm is not None:
            _fsync_directory(destination.parent)
    except (OSError, BackupError) as error:
        if isinstance(error, BackupError):
            raise
        raise BackupError("failed to remove checkpointed SQLite sidecars") from error


def _restore_existing(destination: Path, previous: Path | None) -> None:
    try:
        if previous is None:
            destination.unlink(missing_ok=True)
        else:
            previous.replace(destination)
            _fsync_directory(destination.parent)
    except (OSError, BackupError) as error:
        raise BackupError(
            "SQLite installation failed and authority restore was ambiguous"
        ) from error


def _cleanup(paths: tuple[Path | None, ...]) -> None:
    cleanup_error: BackupError | None = None
    for path in paths:
        if path is not None:
            try:
                _unlink(path)
            except BackupError as error:
                cleanup_error = error
    if cleanup_error is not None:
        raise cleanup_error


def _install(source: Path, destination: Path, binding: dict[str, Any]) -> None:
    _safe_parent(destination, "SQLite destination")
    try:
        destination.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
        parent_identity = _parent_identity(destination)
        _assert_parent_identity(destination, parent_identity)
        descriptor, temporary = tempfile.mkstemp(
            prefix=".coordinator-backup-", suffix=".sqlite3", dir=destination.parent
        )
        os.close(descriptor)
    except OSError as error:
        raise BackupError("failed to allocate temporary SQLite destination") from error
    temporary_path = Path(temporary)
    previous_path: Path | None = None
    replaced = False
    try:
        source_identity = _source_identity(source)
        _copy_online(source, temporary_path, binding)
        if _source_identity(source) != source_identity:
            raise BackupError("source database changed during backup")
        temporary_path.chmod(0o600)
        # Do not allocate a preservation link in a parent that was replaced
        # while the online copy was running.
        _assert_parent_identity(destination, parent_identity)
        destination_identity = _destination_identity(destination)
        previous_path = _backup_existing(destination)
        _assert_parent_identity(destination, parent_identity)
        if _destination_identity(destination) != destination_identity:
            raise BackupError("existing destination changed before publication")
        _before_destination_publish(destination)
        _assert_no_sidecars(destination)
        if _destination_identity(destination) != destination_identity:
            raise BackupError("existing destination changed before publication")
        temporary_path.replace(destination)
        replaced = True
        _fsync_directory(destination.parent)
    except (sqlite3.Error, OSError, BackupError) as error:
        if replaced:
            _restore_existing(destination, previous_path)
            previous_path = None
        if isinstance(error, BackupError):
            raise
        raise BackupError("online SQLite backup or installation failed") from error
    finally:
        _cleanup(
            (
                temporary_path,
                Path(str(temporary_path) + "-wal"),
                Path(str(temporary_path) + "-shm"),
                previous_path,
            )
        )


def backup_database(
    source: Path,
    destination: Path,
    binding: dict[str, Any],
    *,
    session: LifecycleSession | None = None,
    owner: object | None = None,
) -> dict[str, Any]:
    """Create a verified consistent backup without copying a live main file."""
    _regular(source, "source database")
    _check_session(session, owner, source, "SQLite lifecycle session is not bound to source")
    if destination.exists() or destination.is_symlink():
        raise BackupError("refusing to overwrite an existing backup")
    _integrity(source, binding)
    _install(source, destination, binding)
    return {
        "schema_version": MANIFEST_VERSION,
        "kind": "sqlite-online-backup",
        "database_sha256": _digest(destination),
        "integrity_check": "ok",
        "foreign_key_check": "ok",
        "binding_verified": True,
        "wal_consistent": True,
    }


def restore_database(
    backup: Path,
    destination: Path,
    manifest: dict[str, Any],
    binding: dict[str, Any],
    *,
    quiesced: bool,
    session: LifecycleSession | None = None,
    owner: object | None = None,
) -> None:
    """Install a verified backup atomically; refuse restore while writers may run."""
    if not quiesced:
        raise BackupError("restore requires a proven quiesced authority")
    _regular(backup, "backup database")
    _check_session(session, owner, backup, "SQLite lifecycle session is not bound to backup")
    backup_identity = _backup_identity(backup)
    _validate_manifest(manifest)
    if manifest.get("database_sha256") != _digest(backup):
        raise BackupError("backup manifest is missing or does not match the backup")
    _integrity(backup, binding)
    if _backup_identity(backup) != backup_identity:
        raise BackupError("backup database changed during restore")
    _check_session(session, owner, backup, "SQLite lifecycle session changed before install")
    _recover_checkpointed_sidecars(destination)
    _install(backup, destination, binding)


def verify_backup(
    backup: Path, manifest: dict[str, Any], binding: dict[str, Any]
) -> dict[str, Any]:
    """Verify a SQLite backup and manifest without installing or mutating it."""
    _regular(backup, "backup database")
    backup_identity = _backup_identity(backup)
    if Path(str(backup) + "-wal").exists() or Path(str(backup) + "-shm").exists():
        raise BackupError("backup database has live WAL sidecars")
    _validate_manifest(manifest)
    if manifest.get("database_sha256") != _digest(backup):
        raise BackupError("backup manifest is missing or does not match the backup")
    _integrity(backup, binding)
    _regular(backup, "backup database")
    if _backup_identity(backup) != backup_identity:
        raise BackupError("backup database changed during verification")
    return dict(manifest)


def _validate_manifest(manifest: dict[str, Any]) -> None:
    if set(manifest) != MANIFEST_FIELDS:
        raise BackupError("backup manifest has unknown or missing fields")
    required = {
        "schema_version": MANIFEST_VERSION,
        "kind": "sqlite-online-backup",
        "integrity_check": "ok",
        "foreign_key_check": "ok",
        "binding_verified": True,
        "wal_consistent": True,
    }
    if any(manifest.get(key) != value for key, value in required.items()):
        raise BackupError("backup manifest has invalid verification claims")


def write_manifest(path: Path, manifest: dict[str, Any]) -> None:
    """Write a deterministic manifest without accepting non-JSON values."""
    _validate_manifest(manifest)
    _safe_parent(path, "SQLite manifest")
    try:
        path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
        parent_identity = _parent_identity(path)
        descriptor, temporary = tempfile.mkstemp(
            prefix=".coordinator-manifest-", suffix=".json", dir=path.parent
        )
        temporary_path = Path(temporary)
        with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
            stream.write(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
            stream.flush()
            os.fsync(stream.fileno())
        _assert_parent_identity(path, parent_identity)
        manifest_identity = _manifest_identity(path)
        _before_manifest_publish(path)
        if _manifest_identity(path) != manifest_identity:
            raise BackupError("existing SQLite manifest changed before publication")
        temporary_path.replace(path)
        _fsync_directory(path.parent)
    except (OSError, TypeError, ValueError) as error:
        raise BackupError("atomic manifest publication failed") from error
    finally:
        if "temporary_path" in locals():
            _unlink(temporary_path)
