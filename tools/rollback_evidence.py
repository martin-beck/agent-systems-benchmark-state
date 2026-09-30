# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Typed, read-only rollback backup observations."""

from __future__ import annotations

import hashlib
import json
from collections.abc import Mapping
from dataclasses import dataclass, field
from pathlib import Path


class RollbackEvidenceError(ValueError):
    """Backup or control-store evidence is unavailable or malformed."""


_PROVENANCE_TOKEN = object()
_OBSERVATION_PROVIDER_TOKEN = object()


@dataclass(frozen=True)
class BackupObservation:
    """Immutable digests derived from observed backup artifacts and CAS facts."""

    backup_bytes_digest: str
    manifest_digest: str
    control_store_identity: str
    control_store_revision: int
    _provenance: object = field(default=None, repr=False, compare=False)

    @classmethod
    def from_artifacts(
        cls,
        backup: Path,
        manifest: Path,
        *,
        control_store_identity: str,
        control_store_revision: int,
    ) -> BackupObservation:
        if not isinstance(backup, Path) or not isinstance(manifest, Path):
            raise RollbackEvidenceError("backup artifacts must be paths")
        if not isinstance(control_store_identity, str) or not control_store_identity:
            raise RollbackEvidenceError("control-store identity is invalid")
        if type(control_store_revision) is not int or control_store_revision < 1:
            raise RollbackEvidenceError("control-store revision is invalid")
        try:
            backup_stat = backup.stat()
            manifest_stat = manifest.stat()
            backup_identity = (
                backup_stat.st_dev,
                backup_stat.st_ino,
                backup_stat.st_size,
                backup_stat.st_mtime_ns,
            )
            manifest_identity = (
                manifest_stat.st_dev,
                manifest_stat.st_ino,
                manifest_stat.st_size,
                manifest_stat.st_mtime_ns,
            )
            backup_bytes = backup.read_bytes()
            manifest_value = json.loads(manifest.read_text(encoding="utf-8"))
            backup_stat = backup.stat()
            manifest_stat = manifest.stat()
            if (
                backup_stat.st_dev,
                backup_stat.st_ino,
                backup_stat.st_size,
                backup_stat.st_mtime_ns,
            ) != backup_identity or (
                manifest_stat.st_dev,
                manifest_stat.st_ino,
                manifest_stat.st_size,
                manifest_stat.st_mtime_ns,
            ) != manifest_identity:
                raise RollbackEvidenceError("backup artifacts were replaced during observation")
        except (OSError, UnicodeError, json.JSONDecodeError) as error:
            raise RollbackEvidenceError("backup artifacts are unavailable") from error
        if not isinstance(manifest_value, Mapping):
            raise RollbackEvidenceError("backup manifest is not an object")
        return cls(
            hashlib.sha256(backup_bytes).hexdigest(),
            hashlib.sha256(
                json.dumps(manifest_value, sort_keys=True, separators=(",", ":")).encode()
            ).hexdigest(),
            control_store_identity,
            control_store_revision,
            _PROVENANCE_TOKEN,
        )

    @property
    def has_provenance(self) -> bool:
        """Whether this value was produced by the validated artifact factory."""
        return self._provenance is _PROVENANCE_TOKEN
