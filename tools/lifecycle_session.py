# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Opaque adapter-owned lifecycle session identities."""

from __future__ import annotations

import secrets
from dataclasses import dataclass
from pathlib import Path

_TOKEN = secrets.token_bytes(32)


@dataclass(frozen=True, init=False)
class LifecycleSession:
    _owner: object
    _path: Path
    _identity: tuple[int, int]
    _token: bytes

    def __init__(self, owner: object, path: Path, identity: tuple[int, int], token: bytes) -> None:
        if token is not _TOKEN:
            raise ValueError("lifecycle session must be adapter-issued")
        object.__setattr__(self, "_owner", owner)
        object.__setattr__(self, "_path", path)
        object.__setattr__(self, "_identity", identity)
        object.__setattr__(self, "_token", token)

    def belongs_to(self, owner: object) -> bool:
        return self._owner is owner

    def capture_identity(self) -> tuple[int, int]:
        if self._path.is_symlink():
            raise ValueError("bound lifecycle path must not be a symlink")
        status = self._path.stat()
        identity = (status.st_dev, status.st_ino)
        if identity != self._identity:
            raise ValueError("bound lifecycle path identity changed")
        return identity


def _issue(owner: object, path: Path) -> LifecycleSession:
    status = path.stat()
    return LifecycleSession(owner, path, (status.st_dev, status.st_ino), _TOKEN)
