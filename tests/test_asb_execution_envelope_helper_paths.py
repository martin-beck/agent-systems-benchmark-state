# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Downstream coverage for descriptor-backed execution-envelope helper paths."""

from __future__ import annotations

import errno
import fcntl
import json
import os
import sys
import unittest
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path
from unittest.mock import patch

from tools import execution_envelope


class ExecInterceptedError(Exception):
    """Stop the helper after recording the otherwise terminal exec call."""


@contextmanager
def descriptor_pairs(count: int) -> Iterator[tuple[list[int], list[int]]]:
    """Yield read descriptors owned by the helper and retain their pipe peers."""
    pairs = [os.pipe() for _ in range(count)]
    readers = [reader for reader, _writer in pairs]
    writers = [writer for _reader, writer in pairs]
    try:
        yield readers, writers
    finally:
        for descriptor in writers:
            os.close(descriptor)


def helper_argv(specification: dict[str, object]) -> list[str]:
    return [
        "helper",
        "/isolated/import-root",
        json.dumps({"command": ["bwrap", "--clearenv"], "specification": specification}),
        "--",
        "python",
        "-c",
        "print('isolated')",
    ]


class ExecutionEnvelopeHelperPathTests(unittest.TestCase):
    """Keep terminal helper branches deterministic without starting Bubblewrap."""

    def test_helper_execs_descriptor_mounts_and_closes_every_opened_fd(self) -> None:
        specification = {
            "root": "/ignored/when/root-fd-is-present",
            "root_fd": 41,
            "mounts": [
                {"relative": "docs", "destination": "/worktree/docs", "mode": "--ro-bind"},
                {"relative": "out", "destination": "/worktree/out", "mode": "--bind"},
            ],
        }
        captured: dict[str, object] = {}

        def capture_exec(path: str, command: list[str], environment: dict[str, str]) -> None:
            captured.update(path=path, command=command, environment=environment)
            raise ExecInterceptedError

        with descriptor_pairs(5) as (opened, _writers):
            with (
                patch.object(sys, "argv", helper_argv(specification)),
                patch.object(
                    execution_envelope, "_open_path", side_effect=opened[:3]
                ) as runtime_open,
                patch.object(
                    execution_envelope, "_open_scope_fd", side_effect=opened[3:]
                ) as scope_open,
                patch.object(execution_envelope, "_open_scope_path") as path_open,
                patch.object(execution_envelope.shutil, "which", return_value="/mock/bwrap"),
                patch.object(execution_envelope.os, "execvpe", side_effect=capture_exec),
                self.assertRaises(ExecInterceptedError),
            ):
                execution_envelope._run_sandbox_helper()

            runtime_open.assert_has_calls(
                [
                    unittest.mock.call(Path("/usr"), directory=True),
                    unittest.mock.call(Path("/usr/lib"), directory=True),
                    unittest.mock.call(Path("/usr/lib64"), directory=True),
                ]
            )
            scope_open.assert_has_calls(
                [unittest.mock.call(41, "docs"), unittest.mock.call(41, "out")]
            )
            path_open.assert_not_called()
            self.assertEqual("/mock/bwrap", captured["path"])
            command = captured["command"]
            self.assertIsInstance(command, list)
            self.assertEqual(
                ["bwrap", "--clearenv", "--ro-bind-fd", str(opened[0]), "/usr"], command[:5]
            )
            self.assertIn(
                ["--bind-fd", str(opened[4]), "/worktree/out"],
                [command[i : i + 3] for i in range(len(command))],
            )
            self.assertEqual(
                ["--chdir", "/worktree", "--", "python", "-c", "print('isolated')"], command[-6:]
            )
            self.assertIs(captured["environment"], os.environ)
            for descriptor in opened:
                with self.assertRaises(OSError) as closed:
                    fcntl.fcntl(descriptor, fcntl.F_GETFD)
                self.assertEqual(errno.EBADF, closed.exception.errno)

    def test_helper_closes_runtime_descriptors_when_descriptor_mount_opening_fails(self) -> None:
        specification = {
            "root": "/unused",
            "root_fd": 67,
            "mounts": [
                {"relative": "missing", "destination": "/worktree/missing", "mode": "--ro-bind"}
            ],
        }
        with descriptor_pairs(3) as (opened, _writers):
            with (
                patch.object(sys, "argv", helper_argv(specification)),
                patch.object(execution_envelope, "_open_path", side_effect=opened),
                patch.object(
                    execution_envelope,
                    "_open_scope_fd",
                    side_effect=RuntimeError("scope disappeared"),
                ),
                patch.object(execution_envelope.os, "execvpe") as execute,
                self.assertRaisesRegex(RuntimeError, "scope disappeared"),
            ):
                execution_envelope._run_sandbox_helper()
            execute.assert_not_called()
            for descriptor in opened:
                with self.assertRaises(OSError) as closed:
                    fcntl.fcntl(descriptor, fcntl.F_GETFD)
                self.assertEqual(errno.EBADF, closed.exception.errno)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
