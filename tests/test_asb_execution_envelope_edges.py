# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Downstream coverage for execution-envelope cleanup and error boundaries."""

from __future__ import annotations

import argparse
import errno
import fcntl
import json
import os
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from tools import execution_envelope


class ExecutionEnvelopeEdgeTests(unittest.TestCase):
    """Exercise closed failure paths using only temporary descriptor state."""

    def test_descriptor_openers_reject_unsafe_and_non_directory_paths(self) -> None:
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "file").write_text("not a directory", encoding="utf-8")
            with self.assertRaisesRegex(RuntimeError, "must be absolute"):
                execution_envelope._open_path(Path("relative"))
            with self.assertRaisesRegex(RuntimeError, "unsafe"):
                execution_envelope._open_scope_path(root, "../escape")
            with self.assertRaisesRegex(RuntimeError, "non-directory"):
                execution_envelope._open_scope_path(root, "file/child")
            with self.assertRaisesRegex(RuntimeError, "not a directory"):
                execution_envelope._open_path(root / "file", directory=True)

    def test_descriptor_openers_return_inheritable_temporary_descriptors(self) -> None:
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "source").mkdir()
            root_fd = execution_envelope._open_path(root, directory=True)
            scope_fd = execution_envelope._open_scope_fd(root_fd, "source")
            try:
                self.assertTrue(os.get_inheritable(root_fd))
                self.assertTrue(os.get_inheritable(scope_fd))
            finally:
                os.close(scope_fd)
                os.close(root_fd)

    def test_sandbox_command_builds_wrapper_for_temporary_scope(self) -> None:
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "read").mkdir()
            (root / "write").mkdir()
            args = argparse.Namespace(
                command=["true"],
                _envelope_worktree=str(root),
                _envelope_read_scope=["read"],
                _envelope_write_scope=["write"],
            )
            with patch.object(execution_envelope.shutil, "which", return_value="/usr/bin/bwrap"):
                command = execution_envelope.sandboxed_envelope_command(args)
        self.assertEqual(sys.executable, command[0])
        payload = json.loads(command[4])
        self.assertEqual("--ro-bind", payload["specification"]["mounts"][0]["mode"])
        self.assertEqual("--bind", payload["specification"]["mounts"][1]["mode"])
        self.assertEqual(["--", "true"], command[-2:])

    def test_helper_closes_opened_mount_when_bubblewrap_is_missing(self) -> None:
        read_fd, write_fd = os.pipe()
        payload = {
            "command": ["bwrap"],
            "specification": {
                "root": "/unused",
                "root_fd": None,
                "mounts": [
                    {"relative": "source", "destination": "/worktree/source", "mode": "--ro-bind"}
                ],
            },
        }
        argv = ["helper", "/unused", json.dumps(payload), "--", "true"]
        try:
            with (
                patch.object(sys, "argv", argv),
                patch.object(execution_envelope, "_open_path", side_effect=FileNotFoundError),
                patch.object(execution_envelope, "_open_scope_path", return_value=read_fd),
                patch.object(execution_envelope.shutil, "which", return_value=None),
                self.assertRaisesRegex(RuntimeError, "requires bubblewrap"),
            ):
                execution_envelope._run_sandbox_helper()
            with self.assertRaises(OSError) as closed:
                fcntl.fcntl(read_fd, fcntl.F_GETFD)
            self.assertEqual(errno.EBADF, closed.exception.errno)
        finally:
            os.close(write_fd)

    def test_helper_rejects_malformed_process_arguments_before_opening_state(self) -> None:
        with (
            patch.object(sys, "argv", ["helper"]),
            self.assertRaisesRegex(RuntimeError, "arguments"),
        ):
            execution_envelope._run_sandbox_helper()


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
