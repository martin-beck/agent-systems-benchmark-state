# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Process-level confinement tests for execution-envelope commands."""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from tools.execution_envelope import _open_scope_path
from tools.handoffctl import (
    envelope_sandbox_mounts,
    envelope_scope_path,
    sandbox_base_command,
    sandboxed_envelope_command,
)


class ExecutionSandboxFailureTests(unittest.TestCase):
    """Verify a bound command never silently falls back to host execution."""

    def test_missing_bubblewrap_fails_closed(self) -> None:
        args = argparse.Namespace(
            command=["true"],
            _envelope_worktree="/worktree",
            _envelope_write_scope=[],
            _envelope_read_scope=[],
        )
        with (
            patch("tools.execution_envelope.shutil.which", return_value=None),
            self.assertRaisesRegex(RuntimeError, "requires bubblewrap"),
        ):
            sandboxed_envelope_command(args)

    def test_unbound_command_is_not_rewritten(self) -> None:
        self.assertEqual(["true"], sandboxed_envelope_command(argparse.Namespace(command=["true"])))

    def test_private_root_includes_only_expected_runtime_mounts(self) -> None:
        command = sandbox_base_command()
        self.assertIn("--tmpfs", command)
        self.assertIn("/proc", command)
        self.assertNotIn("--ro-bind / /", " ".join(command))
        self.assertIn("--unshare-net", command)
        self.assertIn("--clearenv", command)
        self.assertNotIn("--share-net", command)

    def test_network_is_opt_in_and_git_metadata_mount_is_read_only(self) -> None:
        isolated = sandbox_base_command()
        shared = sandbox_base_command(network=True)
        self.assertIn("--unshare-net", isolated)
        self.assertNotIn("--unshare-net", shared)
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / ".git").write_text("gitdir: metadata", encoding="utf-8")
            mounts = envelope_sandbox_mounts(root, [], [], git_metadata=True)
            self.assertEqual((".git", root / ".git", "--ro-bind"), mounts[0])

    def test_descriptor_mount_builder_keeps_git_metadata_capability(self) -> None:
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / ".git").write_text("gitdir: metadata", encoding="utf-8")
            descriptor = os.open(root, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
            try:
                args = argparse.Namespace(
                    command=["true"],
                    _envelope_worktree=str(root),
                    _envelope_worktree_fd=descriptor,
                    _envelope_write_scope=["src"],
                    _envelope_read_scope=[],
                    _envelope_git_metadata=True,
                    _envelope_network=False,
                )
                with patch("tools.execution_envelope.shutil.which", return_value="bwrap"):
                    command = sandboxed_envelope_command(args)
                self.assertIn('"relative": ".git"', " ".join(command))
            finally:
                os.close(descriptor)


@unittest.skipUnless(shutil.which("bwrap"), "bubblewrap is required for sandbox verification")
class ExecutionSandboxTests(unittest.TestCase):
    """Verify shell commands cannot escape the declared writable paths."""

    def command(
        self, root: Path, shell: str, scope: list[str], read_scope: list[str] | None = None
    ) -> list[str]:
        args = argparse.Namespace(
            command=["sh", "-ceu", shell],
            _envelope_worktree=str(root),
            _envelope_write_scope=scope,
            _envelope_read_scope=[] if read_scope is None else read_scope,
        )
        return sandboxed_envelope_command(args)

    def test_shell_can_write_only_declared_path_scope(self) -> None:
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "src").mkdir()
            (root / "outside").mkdir()
            allowed = subprocess.run(  # noqa: S603 -- fixed test argv exercises Bubblewrap.
                self.command(root, "touch src/allowed", ["src"]), check=False
            )
            self.assertEqual(0, allowed.returncode)
            self.assertTrue((root / "src" / "allowed").exists())
            denied = subprocess.run(  # noqa: S603 -- fixed test argv exercises Bubblewrap.
                self.command(root, "touch outside/forbidden", ["src"]), check=False
            )
            self.assertNotEqual(0, denied.returncode)
            self.assertFalse((root / "outside" / "forbidden").exists())

    def test_symlink_absolute_and_child_process_escapes_stay_read_only(self) -> None:
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "src"
            outside = root / "outside"
            source.mkdir()
            outside.mkdir()
            (source / "escape").symlink_to("../outside")
            for shell in (
                "touch src/escape/symlink-escape",
                f"touch {outside / 'absolute-escape'}",
                "python -c \"from pathlib import Path; Path('outside/child-escape').touch()\"",
            ):
                result = subprocess.run(  # noqa: S603 -- fixed test argv exercises Bubblewrap.
                    self.command(root, shell, ["src"]), check=False
                )
                self.assertNotEqual(0, result.returncode, shell)
            self.assertFalse((outside / "symlink-escape").exists())
            self.assertFalse((outside / "absolute-escape").exists())
            self.assertFalse((outside / "child-escape").exists())

    def test_read_only_mount_cannot_be_hard_linked_into_writable_mount(self) -> None:
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "src"
            fixtures = root / "fixtures"
            source.mkdir()
            fixtures.mkdir()
            protected = fixtures / "protected"
            protected.write_text("unchanged", encoding="utf-8")
            result = subprocess.run(  # noqa: S603 -- fixed test argv exercises Bubblewrap.
                self.command(
                    root,
                    "ln fixtures/protected src/alias && printf changed > src/alias",
                    ["src"],
                    ["fixtures"],
                ),
                check=False,
            )
            self.assertNotEqual(0, result.returncode)
            self.assertEqual("unchanged", protected.read_text(encoding="utf-8"))
            self.assertFalse((source / "alias").exists())

    def test_read_and_test_classes_receive_no_writable_paths(self) -> None:
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "src").mkdir()
            readable = subprocess.run(  # noqa: S603 -- fixed test argv exercises Bubblewrap.
                self.command(root, "test -d src", [], ["src"]), check=False
            )
            self.assertEqual(0, readable.returncode)
            result = subprocess.run(  # noqa: S603 -- fixed test argv exercises Bubblewrap.
                self.command(root, "touch src/forbidden", [], ["src"]), check=False
            )
            self.assertNotEqual(0, result.returncode)
            self.assertFalse((root / "src" / "forbidden").exists())

    def test_process_has_no_inherited_environment_or_network_route(self) -> None:
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "src").mkdir()
            shell = 'test -z "${EXECUTION_ENVELOPE_SECRET-}" && test -z "$(sed 1d /proc/net/route)"'
            with patch.dict(os.environ, {"EXECUTION_ENVELOPE_SECRET": "host-secret"}):
                result = subprocess.run(  # noqa: S603 -- fixed test argv exercises Bubblewrap.
                    self.command(root, shell, [], ["src"]), check=False
                )
            self.assertEqual(0, result.returncode)

    def test_mount_builder_rejects_missing_and_symlinked_scope(self) -> None:
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "source").mkdir()
            (root / "outside").mkdir()
            (root / "source" / "link").symlink_to("../outside")
            self.assertEqual(root / "source", envelope_scope_path(root, "source"))
            with self.assertRaisesRegex(RuntimeError, "unavailable"):
                envelope_scope_path(root, "missing")
            with self.assertRaisesRegex(RuntimeError, "symlink"):
                envelope_scope_path(root, "source/link")
            with self.assertRaisesRegex(RuntimeError, "unsafe"):
                envelope_scope_path(root, "../outside")
            mounts = envelope_sandbox_mounts(root, ["source"], [])
            self.assertEqual([("source", root / "source", "--ro-bind")], mounts)

    def test_opened_scope_descriptor_survives_path_replacement(self) -> None:
        """A later replacement cannot change the already-open mount source."""
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "source"
            outside = root / "outside"
            source.mkdir()
            outside.mkdir()
            (source / "identity").write_text("original", encoding="utf-8")
            (outside / "identity").write_text("attacker", encoding="utf-8")
            descriptor = _open_scope_path(root, "source")
            try:
                source.rename(root / "replaced")
                source.symlink_to(outside)
                self.assertEqual(
                    "original",
                    Path(f"/proc/self/fd/{descriptor}/identity").read_text(encoding="utf-8"),
                )
            finally:
                os.close(descriptor)

    def test_inherited_worktree_descriptor_survives_prelaunch_replacement(self) -> None:
        """The helper mounts the admitted descriptor, not its later pathname."""
        with TemporaryDirectory() as temporary:
            parent = Path(temporary)
            root = parent / "candidate"
            (root / "src").mkdir(parents=True)
            (root / "src" / "marker").write_text("original", encoding="utf-8")
            descriptor = os.open(root, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
            try:
                args = argparse.Namespace(
                    command=["sh", "-ceu", 'test "$(cat src/marker)" = original'],
                    _envelope_worktree=str(root),
                    _envelope_worktree_fd=descriptor,
                    _envelope_write_scope=[],
                    _envelope_read_scope=["src"],
                )
                command = sandboxed_envelope_command(args)
                root.rename(parent / "parked")
                (root / "src").mkdir(parents=True)
                (root / "src" / "marker").write_text("replacement", encoding="utf-8")
                result = subprocess.run(  # noqa: S603 -- fixed test argv exercises descriptor passing.
                    command, check=False, pass_fds=(descriptor,)
                )
                self.assertEqual(0, result.returncode)
            finally:
                os.close(descriptor)
