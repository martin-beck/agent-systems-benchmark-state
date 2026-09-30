# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Contract-aligned authority and staged-runtime selection helpers."""

# Git observation uses fixed executable and argument forms.
# ruff: noqa: S603, S607

from __future__ import annotations

import hashlib
import importlib
import json
import os
import re
import secrets
import sqlite3
import stat
import subprocess
from contextlib import AbstractContextManager
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Literal, Protocol, cast, runtime_checkable

if __package__:
    from .admission_lease import AdmissionLease, AdmissionLeaseError, AdmissionRecheck
    from .sqlite_storage import SCHEMA_VERSION as SQLITE_SCHEMA_VERSION
else:  # pragma: no cover - direct script execution
    from admission_lease import (  # type: ignore[import-not-found,no-redef]
        AdmissionLease,
        AdmissionLeaseError,
        AdmissionRecheck,
    )
    from sqlite_storage import (  # type: ignore[import-not-found,no-redef]
        SCHEMA_VERSION as SQLITE_SCHEMA_VERSION,
    )


class AuthorityError(RuntimeError):
    """Raised when authority or staged-runtime identity is not proven."""


class SelectorPublicationAmbiguousError(AuthorityError):
    """The selector rename occurred but its directory durability is uncertain."""


@runtime_checkable
class SelectorAdmissionLease(Protocol):
    """Caller-owned ordered admission scope for selector publication."""

    def hold(self) -> AbstractContextManager[object]:
        """Return the already-defined common/control/authority scope."""

    def assert_ordered(self) -> None:
        """Verify that the caller acquired the required lock order."""


_AUTHORITY_TABLES = {
    "metadata": ("key", "value"),
    "tasks": (
        "id",
        "filename",
        "meta_json",
        "body",
        "revision",
        "status",
        "owner",
        "claim_expires",
        "branch",
        "worktree_key",
        "updated_at",
    ),
    "dependencies": ("task_id", "dependency_id"),
    "events": ("sequence", "task_id", "revision", "kind", "recorded_at", "note"),
    "command_results": (
        "sequence",
        "task_id",
        "owner",
        "argv_sha256",
        "returncode",
        "classification",
        "recorded_at",
    ),
    "migrations": (
        "sequence",
        "source_backend",
        "source_checkpoint",
        "imported_at",
        "finalized",
    ),
    "checkpoints": ("name", "revision", "recorded_at"),
    "sqlite_sequence": ("name", "seq"),
}
_AUTHORITY_ORDER = {
    "metadata": "key",
    "tasks": "id",
    "dependencies": "task_id,dependency_id",
    "events": "sequence",
    "command_results": "sequence",
    "migrations": "sequence",
    "checkpoints": "name",
    "sqlite_sequence": "name",
}
_SQLITE_SIDECARS = ("-wal", "-shm")
_RELEASE_IDENTITY = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,127}")


@dataclass(frozen=True, slots=True)
class SQLiteReleaseAuthoritySnapshot:
    """Canonical facts reread from one restored SQLite authority and runtime selector."""

    project_id: str
    authority_revision: str
    active_release: str
    previous_release: str
    integrity_check: str
    foreign_key_violations: int


@dataclass(frozen=True, slots=True)
class GitAuthoritySnapshot:
    """Read-only, identity-bound facts from one clean Git authority."""

    repository: Path
    git_directory_identity: tuple[int, int]
    branch: str
    head: str
    requested_ref: str
    requested_ref_head: str
    clean: bool


def _file_identity(status: os.stat_result) -> tuple[int, int]:
    return status.st_dev, status.st_ino


def read_git_authority_snapshot(  # noqa: C901
    repository: Path, requested_ref: str = "HEAD"
) -> GitAuthoritySnapshot:
    """Capture clean, reachable Git identity without invoking mutation commands."""
    resolved = repository.resolve()
    git_directory = resolved / ".git"
    if (
        not resolved.is_dir()
        or resolved != repository.absolute()
        or not git_directory.is_dir()
        or git_directory.is_symlink()
    ):
        raise AuthorityError("Git authority repository is unavailable")
    if requested_ref != "HEAD" and not re.fullmatch(
        r"refs/(?:heads|tags)/[A-Za-z0-9._/-]+", requested_ref
    ):
        raise AuthorityError("Git authority ref is invalid")
    try:
        root_status = resolved.stat()
        git_status = git_directory.stat()
        if root_status.st_uid != os.geteuid() or git_status.st_uid != os.geteuid():
            raise AuthorityError("Git authority root identity is not owner-safe")
        if root_status.st_mode & 0o022 or git_status.st_mode & 0o022:
            raise AuthorityError("Git authority root identity is not owner-safe")
        before = (_file_identity(root_status), _file_identity(git_status))
    except OSError as error:
        raise AuthorityError("Git authority identity is unavailable") from error

    def observe(*arguments: str) -> str:
        try:
            result = subprocess.run(
                ["git", "-C", str(resolved), *arguments],
                check=False,
                capture_output=True,
                text=True,
                timeout=10,
            )
        except (OSError, subprocess.TimeoutExpired) as error:
            raise AuthorityError("Git authority inspection failed") from error
        if result.returncode != 0:
            raise AuthorityError("Git authority inspection was rejected")
        return result.stdout.strip()

    def check(*arguments: str) -> None:
        try:
            result = subprocess.run(
                ["git", "-C", str(resolved), *arguments],
                check=False,
                capture_output=True,
                text=True,
                timeout=10,
            )
        except (OSError, subprocess.TimeoutExpired) as error:
            raise AuthorityError("Git authority inspection failed") from error
        if result.returncode != 0:
            raise AuthorityError("Git authority ref is not reachable")

    status = observe("status", "--porcelain=v1", "--untracked-files=all")
    branch = observe("symbolic-ref", "--short", "-q", "HEAD")
    head = observe("rev-parse", "--verify", "--end-of-options", "HEAD^{commit}")
    ref = branch if requested_ref == "HEAD" else requested_ref
    ref_head = observe("rev-parse", "--verify", "--end-of-options", f"{ref}^{{commit}}")
    ref_name = f"refs/heads/{branch}" if requested_ref == "HEAD" else requested_ref
    check("merge-base", "--is-ancestor", ref_head, head)
    try:
        root_status = resolved.stat()
        git_status = git_directory.stat()
        after = (_file_identity(root_status), _file_identity(git_status))
    except OSError as error:
        raise AuthorityError("Git authority identity reread failed") from error
    if before != after:
        raise AuthorityError("Git authority identity changed")
    final_status = observe("status", "--porcelain=v1", "--untracked-files=all")
    final_branch = observe("symbolic-ref", "--short", "-q", "HEAD")
    final_head = observe("rev-parse", "--verify", "--end-of-options", "HEAD^{commit}")
    final_ref_head = observe("rev-parse", "--verify", "--end-of-options", f"{ref}^{{commit}}")
    final_ref_name = f"refs/heads/{final_branch}" if requested_ref == "HEAD" else requested_ref
    if not branch or not head or not ref_head or status or final_status:
        raise AuthorityError("Git authority is not clean and branch-bound")
    if (branch, head, ref_head, ref_name) != (
        final_branch,
        final_head,
        final_ref_head,
        final_ref_name,
    ):
        raise AuthorityError("Git authority observation changed")
    check("merge-base", "--is-ancestor", final_ref_head, final_head)
    return GitAuthoritySnapshot(resolved, after[1], branch, head, requested_ref, ref_head, True)


def _open_parent(path: Path) -> tuple[int, tuple[int, int]]:
    if not path.is_absolute() or ".." in path.parts or path.name in {"", ".", ".."}:
        raise AuthorityError("authority path is not canonical and absolute")
    descriptor = os.open("/", os.O_RDONLY | os.O_DIRECTORY)
    try:
        for part in path.parent.parts[1:]:
            child = os.open(
                part,
                os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW,
                dir_fd=descriptor,
            )
            os.close(descriptor)
            descriptor = child
        return descriptor, _file_identity(os.fstat(descriptor))
    except OSError as error:
        os.close(descriptor)
        raise AuthorityError("authority parent descriptor is unsafe") from error


def _open_regular(
    path: Path, *, expected_parent: tuple[int, int] | None = None
) -> tuple[int, int, tuple[int, int], tuple[int, int]]:
    parent, parent_identity = _open_parent(path)
    descriptor = -1
    try:
        if expected_parent is not None and parent_identity != expected_parent:
            raise AuthorityError("authority parent identity changed")
        descriptor = os.open(path.name, os.O_RDONLY | os.O_NOFOLLOW, dir_fd=parent)
        status = os.fstat(descriptor)
        if not stat.S_ISREG(status.st_mode) or status.st_nlink != 1:
            raise AuthorityError("authority file is not a private regular file")
        return parent, descriptor, parent_identity, _file_identity(status)
    except OSError as error:
        if descriptor >= 0:
            os.close(descriptor)
        os.close(parent)
        raise AuthorityError("authority file descriptor is unsafe") from error
    except Exception:
        if descriptor >= 0:
            os.close(descriptor)
        os.close(parent)
        raise


def _require_owner_only_parent(parent: int, label: str) -> None:
    status = os.fstat(parent)
    if status.st_uid != os.geteuid() or stat.S_IMODE(status.st_mode) != 0o700:
        raise AuthorityError(f"{label} requires an owner-only provisioned directory")


def _recheck_regular(
    path: Path, parent_identity: tuple[int, int], identity: tuple[int, int]
) -> None:
    parent, descriptor, _, current = _open_regular(path, expected_parent=parent_identity)
    try:
        if current != identity:
            raise AuthorityError("authority file identity changed")
    finally:
        os.close(descriptor)
        os.close(parent)


def _recheck_parent(path: Path, identity: tuple[int, int]) -> None:
    descriptor, current = _open_parent(path)
    try:
        if current != identity:
            raise AuthorityError("authority parent identity changed")
    finally:
        os.close(descriptor)


def _existing_regular_identity(parent: int, name: str) -> tuple[int, int] | None:
    descriptor = -1
    try:
        descriptor = os.open(name, os.O_RDONLY | os.O_NOFOLLOW, dir_fd=parent)
        status = os.fstat(descriptor)
        if not stat.S_ISREG(status.st_mode) or status.st_nlink != 1:
            raise AuthorityError("runtime selector is not a private regular file")
        return _file_identity(status)
    except FileNotFoundError:
        return None
    except OSError as error:
        raise AuthorityError("runtime selector descriptor is unsafe") from error
    finally:
        if descriptor >= 0:
            os.close(descriptor)


def _remove_selector_temporary(parent: int, entry: str) -> None:
    descriptor = -1
    try:
        descriptor = os.open(entry, os.O_RDONLY | os.O_NOFOLLOW, dir_fd=parent)
        status = os.fstat(descriptor)
        if (
            not stat.S_ISREG(status.st_mode)
            or status.st_uid != os.geteuid()
            or stat.S_IMODE(status.st_mode) != 0o600
            or status.st_nlink != 1
        ):
            raise AuthorityError("runtime selector temporary is unsafe")
    except FileNotFoundError:
        return
    except OSError as error:
        raise AuthorityError("runtime selector temporary is unsafe") from error
    finally:
        if descriptor >= 0:
            os.close(descriptor)
    try:
        os.unlink(entry, dir_fd=parent)
    except OSError as error:
        raise AuthorityError("runtime selector temporary cleanup failed") from error


def _cleanup_selector_temporaries(parent: int, name: str) -> None:
    """Remove only owner-safe abandoned selector staging files."""
    prefix = f".{name}."
    try:
        entries = os.listdir(parent)
    except OSError as error:
        raise AuthorityError("runtime selector temporary inventory failed") from error
    removed = False
    for entry in entries:
        if entry.startswith(prefix) and re.fullmatch(r"[0-9a-f]{32}", entry[len(prefix) :]):
            _remove_selector_temporary(parent, entry)
            removed = True
    if removed:
        try:
            os.fsync(parent)
        except OSError as error:
            raise AuthorityError("runtime selector temporary cleanup is ambiguous") from error


def _read_runtime_selector_at(parent: int, name: str) -> dict[str, Any]:  # noqa: C901
    descriptor = -1
    try:
        descriptor = os.open(name, os.O_RDONLY | os.O_NOFOLLOW, dir_fd=parent)
        status = os.fstat(descriptor)
        if not stat.S_ISREG(status.st_mode) or status.st_nlink != 1:
            raise AuthorityError("runtime selector descriptor is unsafe")
        chunks: list[bytes] = []
        total = 0
        while True:
            chunk = os.read(descriptor, 8192)
            if not chunk:
                break
            total += len(chunk)
            if total > 64 * 1024:
                raise AuthorityError("runtime selector is too large")
            chunks.append(chunk)
        after = os.fstat(descriptor)
        if _file_identity(status) != _file_identity(after):
            raise AuthorityError("runtime selector identity changed")
        try:
            value = json.loads(b"".join(chunks).decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as error:
            raise AuthorityError("runtime selector is unreadable") from error
    except FileNotFoundError as error:
        raise AuthorityError("runtime selector is unavailable") from error
    except OSError as error:
        raise AuthorityError("runtime selector descriptor is unsafe") from error
    finally:
        if descriptor >= 0:
            os.close(descriptor)
    if not isinstance(value, dict) or set(value) != {
        "schema_version",
        "active_release",
        "previous_release",
    }:
        raise AuthorityError("runtime selector schema is invalid")
    if (
        value["schema_version"] != 1
        or value["active_release"] == value["previous_release"]
        or not all(
            isinstance(value[key], str) and _RELEASE_IDENTITY.fullmatch(value[key]) is not None
            for key in ("active_release", "previous_release")
        )
    ):
        raise AuthorityError("runtime selector identity is invalid")
    return cast(dict[str, Any], value)


def _sidecar_identities(parent: int, name: str) -> dict[str, tuple[int, int] | None]:
    result: dict[str, tuple[int, int] | None] = {}
    for suffix in _SQLITE_SIDECARS:
        descriptor = -1
        try:
            descriptor = os.open(name + suffix, os.O_RDONLY | os.O_NOFOLLOW, dir_fd=parent)
            status = os.fstat(descriptor)
            if not stat.S_ISREG(status.st_mode) or status.st_nlink != 1:
                raise AuthorityError("SQLite authority sidecar is not a private regular file")
            result[suffix] = _file_identity(status)
        except FileNotFoundError:
            result[suffix] = None
        except OSError as error:
            raise AuthorityError("SQLite authority sidecar descriptor is unsafe") from error
        finally:
            if descriptor >= 0:
                os.close(descriptor)
    return result


def _read_bound_json(path: Path, *, label: str, private_parent: bool = False) -> dict[str, Any]:
    parent, descriptor, parent_identity, identity = _open_regular(path)
    try:
        if private_parent:
            _require_owner_only_parent(parent, label)
        chunks: list[bytes] = []
        total = 0
        while True:
            chunk = os.read(descriptor, 8192)
            if not chunk:
                break
            total += len(chunk)
            if total > 64 * 1024:
                raise AuthorityError(f"{label} is too large")
            chunks.append(chunk)
        try:
            value = json.loads(b"".join(chunks).decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as error:
            raise AuthorityError(f"{label} is unreadable") from error
        _recheck_regular(path, parent_identity, identity)
    finally:
        os.close(descriptor)
        os.close(parent)
    if not isinstance(value, dict):
        raise AuthorityError(f"{label} schema is invalid")
    return cast(dict[str, Any], value)


def _read_backend_selector(path: Path, project_id: str) -> dict[str, object]:
    value = _read_bound_json(path, label="backend selector")
    if set(value) != {"schema_version", "project_id", "backend"} or value != {
        "schema_version": 1,
        "project_id": project_id,
        "backend": "sqlite",
    }:
        raise AuthorityError("backend selector identity is invalid")
    return cast(dict[str, object], value)


def _read_project_binding(path: Path, project_id: str) -> dict[str, object]:
    value = _read_bound_json(path, label="project binding")
    if (
        set(value) != {"schema_version", "project_id", "state_repository", "product_repository"}
        or value.get("schema_version") != 1
        or value.get("project_id") != project_id
        or not all(
            isinstance(value.get(key), str) and value[key]
            for key in ("state_repository", "product_repository")
        )
    ):
        raise AuthorityError("project binding identity is invalid")
    return cast(dict[str, object], value)


def _read_runtime_selector_bound(path: Path) -> dict[str, Any]:
    value = _read_bound_json(path, label="runtime selector", private_parent=True)
    if set(value) != {"schema_version", "active_release", "previous_release"}:
        raise AuthorityError("runtime selector schema is invalid")
    if (
        value["schema_version"] != 1
        or value["active_release"] == value["previous_release"]
        or not all(
            isinstance(value[key], str) and _RELEASE_IDENTITY.fullmatch(value[key]) is not None
            for key in ("active_release", "previous_release")
        )
    ):
        raise AuthorityError("runtime selector identity is invalid")
    return value


def _authority_rows(connection: sqlite3.Connection) -> dict[str, object]:
    schema = [
        list(row)
        for row in connection.execute(
            "SELECT type,name,tbl_name,sql FROM sqlite_schema "
            "WHERE name NOT LIKE 'sqlite_%' ORDER BY type,name"
        )
    ]
    tables = {
        str(row[0])
        for row in connection.execute(
            "SELECT name FROM sqlite_schema WHERE type='table' AND name NOT LIKE 'sqlite_%'"
        )
    }
    if tables != set(_AUTHORITY_TABLES) - {"sqlite_sequence"}:
        raise AuthorityError("SQLite authority schema is invalid")
    result: dict[str, object] = {"schema": schema}
    for table, columns in _AUTHORITY_TABLES.items():
        selected = ",".join(columns)
        order = _AUTHORITY_ORDER[table]
        rows = [
            list(row)
            for row in connection.execute(
                f"SELECT {selected} FROM {table} ORDER BY {order}"  # noqa: S608
            )
        ]
        if any(type(item) not in {str, int, type(None)} for row in rows for item in row):
            raise AuthorityError("SQLite authority contains non-canonical values")
        result[table] = rows
    return result


def inspect_sqlite_release_authority(  # noqa: C901
    authority_path: Path,
    project_binding_path: Path,
    backend_selector_path: Path,
    runtime_selector_path: Path,
    project_id: str,
    active_release: str,
    previous_release: str,
) -> SQLiteReleaseAuthoritySnapshot:
    """Reread and canonically hash an exact SQLite authority/runtime release pair."""
    if (
        not isinstance(project_id, str)
        or not project_id
        or not all(
            isinstance(value, str) and _RELEASE_IDENTITY.fullmatch(value) is not None
            for value in (active_release, previous_release)
        )
    ):
        raise AuthorityError("release-specific authority identity is invalid")
    project_binding = _read_project_binding(project_binding_path, project_id)
    backend_selector = _read_backend_selector(backend_selector_path, project_id)
    runtime_selector = _read_runtime_selector_bound(runtime_selector_path)
    if runtime_selector["active_release"] != active_release or (
        runtime_selector["previous_release"] != previous_release
    ):
        raise AuthorityError("runtime selector release identity changed")

    parent, descriptor, parent_identity, identity = _open_regular(authority_path)
    connection: sqlite3.Connection | None = None
    try:
        before_sidecars = _sidecar_identities(parent, authority_path.name)
        connection = sqlite3.connect(
            f"file:/proc/self/fd/{descriptor}?mode=ro", isolation_level=None, uri=True
        )
        connection.execute("PRAGMA query_only=ON")
        connection.execute("PRAGMA foreign_keys=ON")
        connection.execute("BEGIN")
        integrity = str(connection.execute("PRAGMA integrity_check").fetchone()[0])
        foreign_key_violations = len(list(connection.execute("PRAGMA foreign_key_check")))
        rows = _authority_rows(connection)
        bound_sidecars = _sidecar_identities(parent, authority_path.name)
        if any(
            before_sidecars[suffix] not in {None, bound_sidecars[suffix]}
            for suffix in _SQLITE_SIDECARS
        ):
            raise AuthorityError("SQLite authority sidecar identity changed")
        metadata_rows = cast(list[list[object]], rows["metadata"])
        metadata = {str(row[0]): row[1] for row in metadata_rows}
        expected_metadata = {
            "schema_version": str(SQLITE_SCHEMA_VERSION),
            "backend": "sqlite",
            "project_id": project_id,
            "state": "active",
        }
        if (
            set(metadata)
            != {
                "schema_version",
                "backend",
                "project_id",
                "state_repository",
                "product_repository",
                "state",
            }
            or any(metadata.get(key) != value for key, value in expected_metadata.items())
            or metadata.get("state_repository") != project_binding["state_repository"]
            or metadata.get("product_repository") != project_binding["product_repository"]
        ):
            raise AuthorityError("SQLite authority binding is invalid")
        tasks = cast(list[list[object]], rows["tasks"])
        for task in tasks:
            try:
                task_meta = json.loads(cast(str, task[2]))
            except (TypeError, json.JSONDecodeError) as error:
                raise AuthorityError("SQLite authority task JSON is invalid") from error
            expected = {
                "id": task[0],
                "task_revision": task[4],
                "status": task[5],
                "owner": task[6],
                "claim_expires": task[7],
                "branch": task[8],
                "worktree_key": task[9],
                "updated_at": task[10],
            }
            if not isinstance(task_meta, dict) or any(
                task_meta.get(key, "") != value for key, value in expected.items()
            ):
                raise AuthorityError("SQLite authority task projections disagree")
        payload = {
            "schema_version": 1,
            "kind": "agent-workflow-coordinator-sqlite-authority-revision",
            "project_binding": project_binding,
            "backend_selector": backend_selector,
            "runtime_selector": runtime_selector,
            "authority": rows,
        }
        encoded = json.dumps(
            payload,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
        revision = hashlib.sha256(encoded).hexdigest()
        if _sidecar_identities(parent, authority_path.name) != bound_sidecars:
            raise AuthorityError("SQLite authority sidecar identity changed")
        _recheck_regular(authority_path, parent_identity, identity)
        if (
            _read_project_binding(project_binding_path, project_id) != project_binding
            or _read_backend_selector(backend_selector_path, project_id) != backend_selector
            or _read_runtime_selector_bound(runtime_selector_path) != runtime_selector
        ):
            raise AuthorityError("authority selector identity changed")
    except sqlite3.Error as error:
        raise AuthorityError("SQLite authority reread failed") from error
    finally:
        if connection is not None:
            connection.close()
        os.close(descriptor)
        os.close(parent)
    return SQLiteReleaseAuthoritySnapshot(
        project_id=project_id,
        authority_revision=revision,
        active_release=active_release,
        previous_release=previous_release,
        integrity_check=integrity,
        foreign_key_violations=foreign_key_violations,
    )


def _handoffctl() -> Any:
    """Load handoffctl package-safely, without changing import paths."""
    try:
        return importlib.import_module("tools.handoffctl")
    except ModuleNotFoundError:
        try:
            return importlib.import_module("handoffctl")
        except ModuleNotFoundError as fallback_error:
            raise AuthorityError(
                "handoffctl authority inspection is unavailable"
            ) from fallback_error


def inspect_authority() -> dict[str, object]:
    """Read and validate the selected backend using handoffctl's contracts."""
    handoffctl = cast(Any, _handoffctl())
    try:
        selection = handoffctl.backend_selection()
        binding = handoffctl.project_binding()
        handoffctl._assert_storage_binding(binding)
    except Exception as error:
        raise AuthorityError("project/backend binding validation failed") from error
    result: dict[str, object] = {
        "backend": selection["backend"],
        "project_id": binding["project_id"],
        "state_repository": binding["state_repository"],
        "product_repository": binding["product_repository"],
        "legacy_backend": bool(selection.get("legacy", False)),
        "binding_valid": True,
        "backend_valid": True,
    }
    if selection["backend"] == "git":
        try:
            status = subprocess.run(
                ["git", "status", "--porcelain", "--untracked-files=all"],
                cwd=handoffctl.ROOT,
                check=True,
                capture_output=True,
                text=True,
            )
        except (OSError, subprocess.CalledProcessError) as error:
            raise AuthorityError("Git authority inspection failed") from error
        if status.stdout:
            raise AuthorityError("Git authority is dirty")
        result["state_clean"] = True
    else:
        try:
            tasks = handoffctl.storage_backend().load_tasks()
        except Exception as error:
            raise AuthorityError("SQLite authority inspection failed") from error
        result["state_clean"] = True
        result["task_count"] = len(tasks)
    return result


def read_runtime_selector(path: Path) -> dict[str, Any]:
    """Read a separate staged-runtime selector; backend config is never changed."""
    return _read_runtime_selector_bound(path)


def commit_runtime_selector(  # noqa: C901
    path: Path, active_release: str, previous_release: str
) -> None:
    """Atomically publish through a retained, owner-only parent descriptor."""
    if (
        not all(
            isinstance(value, str) and _RELEASE_IDENTITY.fullmatch(value) is not None
            for value in (active_release, previous_release)
        )
        or active_release == previous_release
    ):
        raise AuthorityError("runtime selector identity is invalid")
    parent, parent_identity = _open_parent(path)
    try:
        _require_owner_only_parent(parent, "runtime selector")
        _existing_regular_identity(parent, path.name)
    except Exception:
        os.close(parent)
        raise
    descriptor = -1
    temporary = f".{path.name}.{secrets.token_hex(16)}"
    replaced = False
    failure: Exception | None = None
    cleanup_failure: OSError | None = None
    try:
        descriptor = os.open(
            temporary,
            os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW,
            0o600,
            dir_fd=parent,
        )
        temporary_identity = _file_identity(os.fstat(descriptor))
        stream = os.fdopen(descriptor, "w", encoding="utf-8")
        descriptor = -1
        with stream:
            json.dump(
                {
                    "schema_version": 1,
                    "active_release": active_release,
                    "previous_release": previous_release,
                },
                stream,
                sort_keys=True,
            )
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        _recheck_parent(path, parent_identity)
        os.replace(temporary, path.name, src_dir_fd=parent, dst_dir_fd=parent)
        replaced = True
        published = os.open(path.name, os.O_RDONLY | os.O_NOFOLLOW, dir_fd=parent)
        try:
            published_status = os.fstat(published)
            if (
                not stat.S_ISREG(published_status.st_mode)
                or published_status.st_nlink != 1
                or _file_identity(published_status) != temporary_identity
            ):
                raise AuthorityError("runtime selector publication identity changed")
        finally:
            os.close(published)
        os.fsync(parent)
        _recheck_parent(path, parent_identity)
    except (OSError, AuthorityError) as error:
        failure = error
    finally:
        if descriptor >= 0:
            try:
                os.close(descriptor)
            except OSError as error:
                cleanup_failure = error
        try:
            os.unlink(temporary, dir_fd=parent)
        except FileNotFoundError:
            pass
        except OSError as error:
            cleanup_failure = error
        try:
            os.close(parent)
        except OSError as error:
            cleanup_failure = error
    if failure is not None or cleanup_failure is not None:
        cause = cleanup_failure if cleanup_failure is not None else cast(Exception, failure)
        if replaced:
            detail = "; temporary cleanup failed" if cleanup_failure is not None else ""
            raise SelectorPublicationAmbiguousError(
                "runtime selector publication is ambiguous; "
                f"reconcile the exact release pair{detail}"
            ) from cause
        message = (
            "runtime selector publication cleanup failed"
            if cleanup_failure is not None
            else "runtime selector publication failed"
        )
        raise AuthorityError(message) from cause


def commit_runtime_selector_admitted(
    path: Path,
    active_release: str,
    previous_release: str,
    admission_lease: AdmissionLease,
    admission_recheck: AdmissionRecheck,
    admission_scope: SelectorAdmissionLease,
) -> None:
    """Publish a selector only inside a caller-owned ordered admission lease.

    This is an uncalled adapter contract. The existing low-level helper remains
    available for provisioning and rejection-only paths; production upgrade
    execution must bind this adapter to the concrete barrier implementation
    before selector mutation is enabled.
    """
    if not isinstance(admission_lease, AdmissionLease):
        raise AuthorityError("selector admission lease is required")
    if not isinstance(admission_recheck, AdmissionRecheck):
        raise AuthorityError("selector admission recheck is required")
    if admission_recheck.lease != admission_lease:
        raise AuthorityError("selector admission recheck does not match lease")
    if not isinstance(admission_scope, SelectorAdmissionLease):
        raise AuthorityError("selector admission scope is required")
    try:
        admission_scope.assert_ordered()
        scope = admission_scope.hold()
        with scope:
            commit_runtime_selector(path, active_release, previous_release)
    except (AdmissionLeaseError, AttributeError, TypeError) as error:
        raise AuthorityError("selector admission lease is invalid") from error


def reconcile_runtime_selector(
    path: Path,
    *,
    before_active_release: str,
    before_previous_release: str,
    after_active_release: str,
    after_previous_release: str,
) -> Literal["committed", "not-committed"]:
    """Resolve an ambiguous rename by accepting only the exact old or new selector."""
    identities = (
        before_active_release,
        before_previous_release,
        after_active_release,
        after_previous_release,
    )
    if not all(
        isinstance(value, str) and _RELEASE_IDENTITY.fullmatch(value) is not None
        for value in identities
    ) or (before_active_release, before_previous_release) == (
        after_active_release,
        after_previous_release,
    ):
        raise AuthorityError("selector reconciliation identities are invalid")
    handoffctl = cast(Any, _handoffctl())
    with handoffctl.locked():
        current = read_runtime_selector(path)
        pair = (current["active_release"], current["previous_release"])
        if pair not in {
            (after_active_release, after_previous_release),
            (before_active_release, before_previous_release),
        }:
            raise AuthorityError("selector reconciliation found an unknown release identity")
        parent, parent_identity = _open_parent(path)
        try:
            _require_owner_only_parent(parent, "runtime selector")
            if parent_identity != _file_identity(os.fstat(parent)):
                raise AuthorityError("runtime selector parent identity changed")
            _cleanup_selector_temporaries(parent, path.name)
            _recheck_parent(path, parent_identity)
            verified = _read_runtime_selector_at(parent, path.name)
            if _file_identity(os.fstat(parent)) != parent_identity:
                raise AuthorityError("runtime selector parent identity changed")
            _recheck_parent(path, parent_identity)
        finally:
            os.close(parent)
        if (verified["active_release"], verified["previous_release"]) != pair:
            raise AuthorityError("selector changed during reconciliation")
        if pair == (after_active_release, after_previous_release):
            return "committed"
        if pair == (before_active_release, before_previous_release):
            return "not-committed"
        raise AuthorityError("selector reconciliation found an unknown release identity")
