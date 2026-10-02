# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Tests for adapter-owned lifecycle session identity."""

import tempfile
import unittest
from pathlib import Path

import tools.lifecycle_session as lifecycle_session
from tools.git_authority_adapter import GitAuthorityAdapter
from tools.lifecycle_session import LifecycleSession
from tools.sqlite_authority_adapter import SQLiteAuthorityAdapter


class LifecycleSessionTests(unittest.TestCase):
    def test_sessions_are_bound_to_concrete_adapters(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            repo = root / "repo"
            repo.mkdir()
            git_adapter = GitAuthorityAdapter(repo)
            git_session = git_adapter.lifecycle_session()
            self.assertTrue(git_session.belongs_to(git_adapter))
            self.assertFalse(git_session.belongs_to(GitAuthorityAdapter(repo)))

            authority = root / "authority.sqlite3"
            authority.touch(mode=0o600)
            sqlite_adapter = SQLiteAuthorityAdapter(authority)
            sqlite_session = sqlite_adapter.lifecycle_session()
            self.assertTrue(sqlite_session.belongs_to(sqlite_adapter))
            self.assertFalse(sqlite_session.belongs_to(git_adapter))

    def test_direct_construction_and_foreign_token_are_rejected(self) -> None:
        self.assertFalse(hasattr(lifecycle_session, "issue"))
        with self.assertRaises(ValueError):
            LifecycleSession(object(), Path("foreign"), (1, 2), b"caller supplied")

    def test_bound_identity_reread_rejects_real_replacement(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "authority"
            path.write_text("original")
            path.chmod(0o600)
            Path(directory).chmod(0o700)
            adapter = SQLiteAuthorityAdapter(path)
            session = adapter.lifecycle_session()
            replacement = Path(directory) / "replacement"
            replacement.write_text("replacement")
            path.rename(Path(directory) / "original")
            path.symlink_to(replacement)
            with self.assertRaisesRegex(ValueError, "(?:identity changed|must not be a symlink)"):
                session.capture_identity()

    def test_bound_identity_reread_rejects_same_inode_symlink(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "authority"
            path.write_text("original")
            path.chmod(0o600)
            Path(directory).chmod(0o700)
            adapter = SQLiteAuthorityAdapter(path)
            session = adapter.lifecycle_session()
            original = Path(directory) / "original"
            path.rename(original)
            path.symlink_to(original)
            with self.assertRaisesRegex(ValueError, "must not be a symlink"):
                session.capture_identity()

    def test_bound_identity_reread_rejects_disappearance(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "authority"
            path.write_text("original")
            path.chmod(0o600)
            Path(directory).chmod(0o700)
            adapter = SQLiteAuthorityAdapter(path)
            session = adapter.lifecycle_session()
            path.unlink()
            with self.assertRaises(FileNotFoundError):
                session.capture_identity()

    def test_bound_identity_reread_detects_regular_file_replacement(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "authority"
            path.write_text("original")
            path.chmod(0o600)
            Path(directory).chmod(0o700)
            adapter = SQLiteAuthorityAdapter(path)
            session = adapter.lifecycle_session()
            replacement = Path(directory) / "replacement"
            replacement.write_text("replacement")
            path.unlink()
            replacement.rename(path)
            with self.assertRaisesRegex(ValueError, "identity changed"):
                session.capture_identity()
