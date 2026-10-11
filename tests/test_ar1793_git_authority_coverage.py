# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Offline coverage for Git authority rollback and rejection boundaries."""

# Test setup invokes fixed Git commands against isolated temporary repositories.
# ruff: noqa: S603, S607

from __future__ import annotations

import subprocess
import tempfile
import unittest
from collections.abc import Iterator, Mapping
from pathlib import Path
from typing import Any, cast
from unittest.mock import MagicMock, patch

from tools.admission_lease import AdmissionLease, validate_recheck
from tools.git_authority_adapter import (
    GitAuthorityAdapter,
    GitAuthorityError,
    GitBackupObservation,
    GitRollbackSessionState,
)
from tools.git_authority_mutation import GitMutationError
from tools.lock_domain_scope import LockDomainScope

PROJECT = "11111111-1111-4111-8111-111111111111"
CONTEXT: dict[str, object] = {
    "schema_version": 2,
    "backend": "git",
    "project_id": PROJECT,
    "operation_id": "ar1793:rollback",
    "state_revision": 1,
    "authority_revision": "authority",
    "fencing_token": "fence",
    "fencing_owner": "owner",
    "durable_barrier_id": "barrier",
    "artifact_root": "/artifacts",
    "source": "/source",
    "destination": "/destination",
    "manifest": "/manifest",
    "selector_ref": ".runtime/runtime-selector.json",
    "barrier_identity_digest": "0" * 64,
    "target": "rollback",
    "envelope_digest": "0" * 64,
}


class BrokenContext(Mapping[str, object]):
    """A hostile mapping whose key iteration is unavailable."""

    def __getitem__(self, _key: str) -> object:
        raise KeyError

    def __iter__(self) -> Iterator[str]:
        raise RuntimeError("broken mapping")

    def __len__(self) -> int:
        return 0


class AR1793GitAuthorityCoverageTests(unittest.TestCase):
    def setUp(self) -> None:
        self.directory = tempfile.TemporaryDirectory()
        self.artifacts = tempfile.TemporaryDirectory()
        self.root = Path(self.directory.name)
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)
        subprocess.run(["git", "-C", str(self.root), "config", "user.name", "test"], check=True)
        subprocess.run(
            ["git", "-C", str(self.root), "config", "user.email", "test@example"], check=True
        )
        (self.root / "state").write_text("base\n")
        subprocess.run(["git", "-C", str(self.root), "add", "state"], check=True)
        subprocess.run(["git", "-C", str(self.root), "commit", "-qm", "base"], check=True)
        self.root.chmod(0o700)
        (self.root / ".git").chmod(0o700)
        self.adapter = GitAuthorityAdapter(self.root)
        self.branch = self.adapter._git("symbolic-ref", "--short", "-q", "HEAD")
        self.base_head = self.adapter._git("rev-parse", "--verify", "HEAD")

    def tearDown(self) -> None:
        self.artifacts.cleanup()
        self.directory.cleanup()

    def _lease(self) -> AdmissionLease:
        return AdmissionLease(PROJECT, "authority", "fence", "owner", "barrier", 1)

    def _recheck(self) -> Any:
        lease = self._lease()
        return validate_recheck(
            lease,
            project_id=PROJECT,
            authority_revision="authority",
            fencing_token="fence",  # noqa: S106
            fencing_owner="owner",
            durable_barrier_id="barrier",
            revision=1,
        )

    def test_restore_authority_bound_resets_to_verified_local_bundle_commit(self) -> None:
        (self.root / "state").write_text("backup\n")
        subprocess.run(["git", "-C", str(self.root), "commit", "-am", "backup", "-q"], check=True)
        backup_head = self.adapter._git("rev-parse", "--verify", "HEAD")
        backup = Path(self.artifacts.name) / "backup"
        backup.mkdir()
        subprocess.run(
            [
                "git",
                "-C",
                str(self.root),
                "bundle",
                "create",
                str(backup / "authority.bundle"),
                self.branch,
            ],
            check=True,
        )
        subprocess.run(
            ["git", "-C", str(self.root), "reset", "--hard", "-q", self.base_head], check=True
        )

        with patch.object(
            self.adapter,
            "verify_backup_artifact",
            return_value={"verified": True, "commit": backup_head},
        ):
            result = self.adapter.restore_authority_bound(
                backup, expected_branch=self.branch, expected_head=self.base_head
            )

        self.assertEqual(backup_head, self.adapter._git("rev-parse", "--verify", "HEAD"))
        self.assertEqual(backup_head, result["rollback_commit"])
        self.assertTrue(cast(bool, result["mutates_authority"]))

    def test_restore_authority_bound_rejects_invalid_stale_and_unverified_inputs(self) -> None:
        backup = Path(self.artifacts.name) / "backup"
        backup.mkdir()
        with self.assertRaisesRegex(GitAuthorityError, "identity is incomplete"):
            self.adapter.restore_authority_bound(
                cast(Any, "backup"), expected_branch="", expected_head=""
            )
        with self.assertRaisesRegex(GitAuthorityError, "stale or dirty"):
            self.adapter.restore_authority_bound(
                backup, expected_branch="other", expected_head=self.base_head
            )
        with (
            patch.object(
                self.adapter,
                "verify_backup_artifact",
                return_value={"verified": False, "commit": self.base_head},
            ),
            self.assertRaisesRegex(GitAuthorityError, "verification is incomplete"),
        ):
            self.adapter.restore_authority_bound(
                backup, expected_branch=self.branch, expected_head=self.base_head
            )

    def test_restore_authority_bound_rejects_postcondition_drift(self) -> None:
        backup = Path(self.artifacts.name) / "backup"
        backup.mkdir()
        responses = ["", self.branch, self.base_head, "", "", "other"]
        with (
            patch.object(
                self.adapter,
                "verify_backup_artifact",
                return_value={"verified": True, "commit": self.base_head},
            ),
            patch.object(self.adapter, "_git", side_effect=responses),
            self.assertRaisesRegex(GitAuthorityError, "postcondition is invalid"),
        ):
            self.adapter.restore_authority_bound(
                backup, expected_branch=self.branch, expected_head=self.base_head
            )

    def test_rejection_wrappers_preserve_their_authority_boundary(self) -> None:
        with (
            patch(
                "tools.git_authority_mutation.GitCommitCapability",
                side_effect=GitMutationError("bad"),
            ),
            self.assertRaisesRegex(GitAuthorityError, "binding was rejected"),
        ):
            self.adapter.bind_commit_capability(
                object(),
                admission_reread=object(),
                expected_branch=self.branch,
                expected_head=self.base_head,
            )

        capability = MagicMock()
        capability.commit.side_effect = RuntimeError("effect failed")
        with (
            patch.object(self.adapter, "bind_commit_capability", return_value=capability),
            self.assertRaisesRegex(GitAuthorityError, "effect failed"),
        ):
            self.adapter.commit_bound(
                object(),
                "message",
                admission_reread=object(),
                expected_branch=self.branch,
                expected_head=self.base_head,
            )
        capability.commit.side_effect = GitAuthorityError("already normalized")
        with (
            patch.object(self.adapter, "bind_commit_capability", return_value=capability),
            self.assertRaisesRegex(GitAuthorityError, "already normalized"),
        ):
            self.adapter.commit_bound(
                object(),
                "message",
                admission_reread=object(),
                expected_branch=self.branch,
                expected_head=self.base_head,
            )

    def test_malformed_observation_context_and_repository_identity_are_rejected(self) -> None:
        session = GitRollbackSessionState(
            PROJECT, "authority", 1, "fence", "owner", "barrier", self.base_head, self.branch
        )
        with self.assertRaisesRegex(GitAuthorityError, "session is invalid"):
            GitBackupObservation._from_verified(cast(Any, object()), {"commit": self.base_head})
        with self.assertRaisesRegex(GitAuthorityError, "context types"):
            GitAuthorityAdapter._context({**CONTEXT, "schema_version": 0})
        with self.assertRaisesRegex(GitAuthorityError, "context target"):
            GitAuthorityAdapter._context({**CONTEXT, "target": "apply"})
        self.adapter._repository_identity = None
        with self.assertRaisesRegex(GitAuthorityError, "repository identity changed"):
            self.adapter._check_repository_identity()
        self.assertEqual(self.base_head, session.git_head)

    def test_bound_snapshot_wraps_hostile_context_and_observation_errors(self) -> None:
        lease = self._lease()
        recheck = self._recheck()
        scope = object.__new__(LockDomainScope)
        with self.assertRaisesRegex(GitAuthorityError, "context is invalid"):
            self.adapter.snapshot_bound(
                "rollback",
                BrokenContext(),
                scope,
                lease=lease,
                admission_recheck=recheck,
                expected_branch=self.branch,
                expected_head=self.base_head,
            )
        with (
            patch(
                "tools.upgrade_authority.read_git_authority_snapshot",
                side_effect=RuntimeError("bad git"),
            ),
            self.assertRaisesRegex(GitAuthorityError, "identity reread was rejected"),
        ):
            self.adapter.snapshot_bound(
                "rollback",
                CONTEXT,
                scope,
                lease=lease,
                admission_recheck=recheck,
                expected_branch=self.branch,
                expected_head=self.base_head,
            )

    def test_bound_snapshot_rejects_replaced_repository_and_backend_identity(self) -> None:
        lease = self._lease()
        recheck = self._recheck()
        scope = object.__new__(LockDomainScope)
        self.adapter._repository_identity = (0, 0, 0, 0)
        with self.assertRaisesRegex(GitAuthorityError, "repository identity changed"):
            self.adapter.snapshot_bound(
                "rollback",
                CONTEXT,
                scope,
                lease=lease,
                admission_recheck=recheck,
                expected_branch=self.branch,
                expected_head=self.base_head,
            )
        self.adapter = GitAuthorityAdapter(self.root)
        backend_value = {
            **CONTEXT,
            "phase": "rollback",
            "backend_identity_verified": True,
            "git_head": "other",
            "git_branch": self.branch,
            "git_clean": True,
            "mutates_authority": False,
        }
        scoped = MagicMock()
        scoped.snapshot.return_value = backend_value
        with (
            patch("tools.scoped_backend_adapter.ScopedBackendAdapter", return_value=scoped),
            self.assertRaisesRegex(GitAuthorityError, "identity changed"),
        ):
            self.adapter.snapshot_bound(
                "rollback",
                CONTEXT,
                scope,
                lease=lease,
                admission_recheck=recheck,
                expected_branch=self.branch,
                expected_head=self.base_head,
            )
