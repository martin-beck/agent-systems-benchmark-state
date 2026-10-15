# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Process launch support for an ephemeral publication credential descriptor."""

from __future__ import annotations

import argparse
import subprocess


def run_envelope_subprocess(
    command: list[str], timeout: float, args: argparse.Namespace
) -> subprocess.CompletedProcess[bytes]:
    """Pass only the admitted worktree and credential descriptors to a command."""
    pass_fds: list[int] = []
    worktree_fd = getattr(args, "_envelope_worktree_fd", None)
    if worktree_fd is not None:
        if type(worktree_fd) is not int or worktree_fd < 0:
            raise RuntimeError("invalid envelope worktree descriptor")
        pass_fds.append(worktree_fd)
    credential_fd = getattr(args, "credential_fd", None)
    if credential_fd is None:
        raise RuntimeError("credential descriptor is required")
    if type(credential_fd) is not int or credential_fd < 3:
        raise RuntimeError("credential descriptor must be an open fd >= 3")
    pass_fds.append(credential_fd)
    worktree = getattr(args, "_envelope_worktree", None)
    if worktree is not None:
        return subprocess.run(  # noqa: S603
            command,
            cwd=str(worktree),
            check=False,
            stdin=subprocess.DEVNULL,
            timeout=timeout,
            pass_fds=tuple(pass_fds),
        )
    return subprocess.run(  # noqa: S603
        command,
        check=False,
        stdin=subprocess.DEVNULL,
        timeout=timeout,
        pass_fds=tuple(pass_fds),
    )
