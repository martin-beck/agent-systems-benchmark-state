# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Durable WAL/SHM lifecycle evidence for provisioned SQLite stores."""

from __future__ import annotations

import hashlib
import json
import os
import stat
from contextlib import suppress
from dataclasses import dataclass
from pathlib import Path
from typing import Any

SCHEMA_VERSION = 1
LIFECYCLE_STATES = {"absent", "active", "clean_checkpointed"}
SIDECAR_SUFFIXES = ("-wal", "-shm")


class WALLifecycleError(RuntimeError):
    """A durable WAL/SHM lifecycle record is unavailable or unsafe."""


@dataclass(frozen=True, slots=True)
class SidecarIdentity:
    """Stable identity and size of one SQLite journal sidecar."""

    device: int
    inode: int
    size: int


def _canonical(value: dict[str, Any]) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")


def _digest(value: dict[str, Any]) -> str:
    return "sha256:" + hashlib.sha256(_canonical(value)).hexdigest()


def _identity(status: os.stat_result) -> tuple[int, int]:
    return status.st_dev, status.st_ino


def _read_record(path: Path) -> dict[str, Any]:
    parent_fd = os.open(path.parent, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
    descriptor = -1
    try:
        descriptor = os.open(path.name, os.O_RDONLY | os.O_NOFOLLOW, dir_fd=parent_fd)
        status = os.fstat(descriptor)
        if (
            not stat.S_ISREG(status.st_mode)
            or status.st_uid != os.geteuid()
            or status.st_nlink != 1
            or stat.S_IMODE(status.st_mode) != 0o600
        ):
            raise WALLifecycleError("WAL lifecycle record is unsafe")
        value = json.loads(os.read(descriptor, 1 << 20).decode("utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        raise WALLifecycleError("WAL lifecycle record is unreadable") from error
    finally:
        if descriptor >= 0:
            os.close(descriptor)
        os.close(parent_fd)
    if not isinstance(value, dict):
        raise WALLifecycleError("WAL lifecycle record schema is invalid")
    return value


def _write_record(path: Path, value: dict[str, Any], *, exclusive: bool = False) -> None:
    parent_fd = os.open(path.parent, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
    descriptor = -1
    temporary = f".{path.name}.tmp"
    try:
        flags = os.O_WRONLY | os.O_CREAT | os.O_NOFOLLOW
        flags |= os.O_EXCL if exclusive else 0
        descriptor = os.open(temporary, flags, 0o600, dir_fd=parent_fd)
        os.write(descriptor, _canonical(value) + b"\n")
        os.fsync(descriptor)
        os.close(descriptor)
        descriptor = -1
        os.rename(temporary, path.name, src_dir_fd=parent_fd, dst_dir_fd=parent_fd)
        os.fsync(parent_fd)
    except OSError as error:
        raise WALLifecycleError("WAL lifecycle publication is ambiguous") from error
    finally:
        if descriptor >= 0:
            os.close(descriptor)
        with suppress(FileNotFoundError):
            os.unlink(temporary, dir_fd=parent_fd)
        os.close(parent_fd)


def _sidecars(parent: int, name: str, *, required: bool) -> dict[str, SidecarIdentity | None]:
    result: dict[str, SidecarIdentity | None] = {}
    for suffix in SIDECAR_SUFFIXES:
        descriptor = -1
        try:
            descriptor = os.open(name + suffix, os.O_RDONLY | os.O_NOFOLLOW, dir_fd=parent)
            status = os.fstat(descriptor)
            if (
                not stat.S_ISREG(status.st_mode)
                or status.st_uid != os.geteuid()
                or status.st_nlink != 1
            ):
                raise WALLifecycleError("SQLite WAL sidecar is unsafe")
            result[suffix] = SidecarIdentity(status.st_dev, status.st_ino, status.st_size)
        except FileNotFoundError:
            if required:
                raise WALLifecycleError("SQLite WAL sidecar is unavailable") from None
            result[suffix] = None
        except OSError as error:
            raise WALLifecycleError("SQLite WAL sidecar is unavailable") from error
        finally:
            if descriptor >= 0:
                os.close(descriptor)
    return result


def _json_sidecars(value: dict[str, SidecarIdentity | None]) -> dict[str, Any]:
    return {
        suffix: None
        if identity is None
        else {
            "device": identity.device,
            "inode": identity.inode,
            "size": identity.size,
        }
        for suffix, identity in value.items()
    }


class WALLifecycleStore:
    """Read and transition one project-bound durable sidecar lifecycle."""

    def __init__(
        self,
        path: Path,
        project_id: str,
        database_identity: tuple[int, int],
        authority_identity: tuple[int, int] | None = None,
    ) -> None:
        self.path = path.absolute()
        self.project_id = project_id
        self.database_identity = database_identity
        self.authority_identity = authority_identity

    def _record(
        self,
        state: str,
        generation: int,
        sidecars: dict[str, SidecarIdentity | None],
    ) -> dict[str, Any]:
        if state not in LIFECYCLE_STATES:
            raise WALLifecycleError("WAL lifecycle state is invalid")
        value: dict[str, Any] = {
            "schema_version": SCHEMA_VERSION,
            "project_id": self.project_id,
            "database_identity": list(self.database_identity),
            "authority_identity": (
                None if self.authority_identity is None else list(self.authority_identity)
            ),
            "journal_mode": "wal",
            "state": state,
            "generation": generation,
            "sidecars": _json_sidecars(sidecars),
        }
        value["record_digest"] = _digest(value)
        return value

    def initialize(self) -> None:
        if self.path.exists() or self.path.is_symlink():
            return
        self.path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
        self.path.parent.chmod(0o700)
        self._publish(self._record("absent", 0, dict.fromkeys(SIDECAR_SUFFIXES)), True)

    def _publish(self, value: dict[str, Any], exclusive: bool = False) -> None:
        _write_record(self.path, value, exclusive=exclusive)

    def read(self) -> dict[str, Any]:  # noqa: C901
        value = _read_record(self.path)
        expected_digest = _digest(
            {key: item for key, item in value.items() if key != "record_digest"}
        )
        if value.get("record_digest") != expected_digest:
            raise WALLifecycleError("WAL lifecycle record digest is invalid")
        if value.get("schema_version") != SCHEMA_VERSION:
            raise WALLifecycleError("WAL lifecycle schema is unsupported")
        if value.get("project_id") != self.project_id:
            raise WALLifecycleError("WAL lifecycle project binding changed")
        if value.get("database_identity") != list(self.database_identity):
            raise WALLifecycleError("WAL lifecycle database identity changed")
        expected_authority = (
            None if self.authority_identity is None else list(self.authority_identity)
        )
        if value.get("authority_identity") != expected_authority:
            raise WALLifecycleError("WAL lifecycle authority identity changed")
        if value.get("journal_mode") != "wal" or value.get("state") not in LIFECYCLE_STATES:
            raise WALLifecycleError("WAL lifecycle record state is invalid")
        if type(value.get("generation")) is not int or value["generation"] < 0:
            raise WALLifecycleError("WAL lifecycle generation is invalid")
        sidecars = value.get("sidecars")
        if not isinstance(sidecars, dict) or set(sidecars) != set(SIDECAR_SUFFIXES):
            raise WALLifecycleError("WAL lifecycle sidecars are invalid")
        for identity in sidecars.values():
            if identity is not None and (
                not isinstance(identity, dict)
                or set(identity) != {"device", "inode", "size"}
                or any(type(identity[key]) is not int or identity[key] < 0 for key in identity)
            ):
                raise WALLifecycleError("WAL lifecycle sidecar identity is invalid")
        if value["state"] == "absent" and any(
            identity is not None for identity in sidecars.values()
        ):
            raise WALLifecycleError("absent WAL lifecycle cannot retain sidecars")
        return value

    def validate(self) -> dict[str, Any]:
        return self.read()

    def mark_active(self, parent: int, name: str, *, allow_rebind: bool = False) -> dict[str, Any]:
        current = self.read()
        observed = _sidecars(parent, name, required=True)
        encoded = _json_sidecars(observed)
        if current["state"] == "active":
            if current["sidecars"] != encoded and not allow_rebind:
                raise WALLifecycleError("active WAL sidecar identity changed")
            if current["sidecars"] != encoded:
                value = self._record("active", current["generation"], observed)
                self._publish(value)
                return value
            return current
        generation = current["generation"] + 1
        value = self._record("active", generation, observed)
        self._publish(value)
        return value

    def mark_clean_checkpointed(self, parent: int, name: str) -> dict[str, Any]:
        current = self.read()
        observed = _sidecars(parent, name, required=False)
        if any(identity is not None for identity in observed.values()):
            raise WALLifecycleError("WAL checkpoint did not remove all sidecars")
        if current["state"] != "active":
            raise WALLifecycleError("WAL checkpoint requires an active lifecycle")
        value = self._record("clean_checkpointed", current["generation"], observed)
        self._publish(value)
        return value
