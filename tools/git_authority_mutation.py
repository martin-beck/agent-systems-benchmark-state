# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Bounded Git authority commit capability.

The capability is intentionally not wired into the public upgrade dispatcher.
It is the independently testable effect seam for the Git mutation gate.
"""

# The executable and arguments are fixed by the capability contract.

from __future__ import annotations

import os
import re
import stat
import subprocess
import tempfile
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from pathlib import Path

from tools.authority_mutation import (
    AuthorityMutationAmbiguousError,
    AuthorityMutationRejectedError,
)
from tools.authority_neutral_commit import CommitAdmissionBundle


class GitMutationError(RuntimeError):
    """A Git authority effect was rejected or its outcome is ambiguous."""


class GitMutationRejectedError(GitMutationError, AuthorityMutationRejectedError):
    """Git admission was rejected before invoking the commit effect."""


class GitMutationAmbiguousError(GitMutationError, AuthorityMutationAmbiguousError):
    """The Git process outcome cannot be classified as success or failure."""


_SAFE_MESSAGE = re.compile(r"[A-Za-z0-9][A-Za-z0-9 ._:/-]{0,127}\Z")
_COMMIT_HEAD = re.compile(r"\[[^\]]+\s+([0-9a-f]{7,64})\]")
_Runner = Callable[..., subprocess.CompletedProcess[str]]
_AdmissionReread = Callable[[], Mapping[str, object]]


@dataclass(frozen=True)
class GitCommitResult:
    """Verified result of one exact-head Git commit."""

    backend: str
    target: str
    operation_id: str
    state_revision: int
    barrier_id: str
    artifact_identity: str
    manifest_identity: str
    selector_identity: str
    runtime_identity: str
    before_head: str
    after_head: str
    branch: str
    fencing_token: str
    mutates_authority: bool = True


class GitCommitCapability:
    """Commit one pre-staged authority change under an immutable identity."""

    def __init__(
        self,
        repository: Path,
        *,
        admission: CommitAdmissionBundle,
        admission_reread: _AdmissionReread,
        expected_branch: str,
        expected_head: str,
        runner: _Runner = subprocess.run,
    ) -> None:
        try:
            self._repository = repository.absolute()
            self._ancestor_identities = self._read_ancestor_identities(self._repository)
            self._repository_identity = self._read_repository_identity(self._repository)
        except GitMutationError:
            raise
        except BaseException as error:
            raise GitMutationError("Git authority identity capture was rejected") from error
        if admission.backend != "git" or admission.target != "new":
            raise GitMutationError("Git mutation admission identity is invalid")
        self._admission = admission
        if not callable(admission_reread):
            raise GitMutationError("Git admission reread is invalid")
        self._admission_reread = admission_reread
        self._operation_id = self._validate_text(admission.operation_id, "operation identity")
        self._fencing_token = self._validate_text(admission.fencing_token, "fencing token")
        self._expected_branch = self._validate_text(expected_branch, "branch identity")
        self._expected_head = self._validate_head(expected_head)
        self._runner = runner
        self._consumed = False

    @staticmethod
    def _read_ancestor_identities(repository: Path) -> tuple[tuple[str, int, int], ...]:
        identities: list[tuple[str, int, int]] = []
        current = Path(repository.anchor)
        for part in repository.parent.parts[1:]:
            current /= part
            try:
                status = current.lstat()
            except OSError as error:
                raise GitMutationError(
                    "Git authority repository ancestor is unavailable"
                ) from error
            except BaseException as error:
                raise GitMutationError(
                    "Git authority repository ancestor is unavailable"
                ) from error
            if not stat.S_ISDIR(status.st_mode):
                raise GitMutationError("Git authority repository ancestor is not a directory")
            identities.append((str(current), status.st_dev, status.st_ino))
        return tuple(identities)

    @staticmethod
    def _read_repository_identity(repository: Path) -> tuple[int, int]:
        try:
            status = repository.lstat()
        except OSError as error:
            raise GitMutationError("Git authority repository is unavailable") from error
        except BaseException as error:
            raise GitMutationError("Git authority repository is unavailable") from error
        if not stat.S_ISDIR(status.st_mode):
            raise GitMutationError("Git authority repository is not a regular directory")
        return status.st_dev, status.st_ino

    def _assert_repository_identity(self) -> None:
        try:
            ancestors = self._read_ancestor_identities(self._repository)
            current = self._read_repository_identity(self._repository)
        except GitMutationError as error:
            raise GitMutationRejectedError(
                "Git authority repository identity changed before commit"
            ) from error
        except BaseException as error:
            raise GitMutationRejectedError(
                "Git authority repository identity reread was rejected"
            ) from error
        if ancestors != self._ancestor_identities or current != self._repository_identity:
            raise GitMutationRejectedError(
                "Git authority repository identity changed before commit"
            )

    @staticmethod
    def _validate_text(value: str, label: str) -> str:
        if not isinstance(value, str) or not value or not _SAFE_MESSAGE.fullmatch(value):
            raise GitMutationError(f"Git {label} is invalid")
        return value

    @staticmethod
    def _validate_head(value: str) -> str:
        if not isinstance(value, str) or not re.fullmatch(r"[0-9a-f]{40,64}", value):
            raise GitMutationError("Git head identity is invalid")
        return value

    def _git(self, *args: str) -> str:
        try:
            result = self._runner(
                ["git", "-C", str(self._repository), *args],
                check=False,
                capture_output=True,
                text=True,
                timeout=10,
            )
        except (OSError, subprocess.TimeoutExpired) as error:
            raise GitMutationRejectedError("Git identity reread was rejected") from error
        except BaseException as error:
            raise GitMutationRejectedError("Git identity reread was rejected") from error
        try:
            if result.returncode != 0:
                raise GitMutationRejectedError("Git identity reread was rejected")
            return result.stdout.rstrip("\n")
        except GitMutationRejectedError:
            raise
        except BaseException as error:
            raise GitMutationRejectedError("Git identity reread was rejected") from error

    @staticmethod
    def _commit_head(result: subprocess.CompletedProcess[str]) -> str | None:
        match = _COMMIT_HEAD.search(f"{result.stdout}\n{result.stderr}")
        return None if match is None else match.group(1)

    def _assert_before(self) -> tuple[str, str]:
        self._assert_repository_identity()
        branch = self._git("symbolic-ref", "--short", "-q", "HEAD")
        head = self._git("rev-parse", "--verify", "HEAD^{commit}")
        if branch != self._expected_branch or head != self._expected_head:
            raise GitMutationRejectedError("Git authority identity changed before commit")
        status = self._git("status", "--porcelain=v1", "--untracked-files=all")
        lines = [line for line in status.splitlines() if line]
        if any(len(line) < 2 or line[1] != " " for line in lines):
            raise GitMutationRejectedError("Git authority has unstaged or untracked changes")
        if not lines:
            raise GitMutationRejectedError("Git authority has no staged change")
        return branch, head

    def _assert_admission_current(self) -> None:
        try:
            current = self._admission_reread()
        except BaseException as error:
            raise GitMutationRejectedError("Git admission reread was rejected") from error
        if not isinstance(current, Mapping) or not self._admission.matches(current):
            raise GitMutationRejectedError("Git admission identity changed before commit")

    def stage_and_commit(self, argument: Mapping[str, object]) -> GitCommitResult:  # noqa: C901
        """Stage one admitted selector payload inside the durable effect boundary.

        The durable wrapper prepares its intent before invoking this method.
        Consequently a worker death after the working-tree replacement or
        ``git add`` is recovered as an unresolved effect, never as a success.
        The ordinary string ``commit`` path remains available for callers that
        provide their own pre-staged change.
        """
        if self._consumed:  # pragma: no cover - single-use rejection is directly tested
            raise GitMutationError("Git mutation capability already consumed")
        if not isinstance(argument, Mapping) or set(
            argument
        ) != {  # pragma: no cover - validated input boundary
            "message",
            "path",
            "content",
        }:
            raise GitMutationRejectedError("Git staged commit argument is invalid")
        message = argument.get("message")
        relative = argument.get("path")
        content = argument.get("content")
        if not isinstance(message, str):  # pragma: no cover - validated input boundary
            raise GitMutationRejectedError("Git staged commit message is invalid")
        message = self._validate_text(message, "commit message")
        if (  # pragma: no cover - validated input boundary
            not isinstance(relative, str)
            or not relative
            or Path(relative).is_absolute()
            or ".." in Path(relative).parts
            or relative.startswith(".git/")
            or relative == ".git"
        ):
            raise GitMutationRejectedError("Git staged commit path is invalid")
        if (
            not isinstance(content, str) or len(content.encode("utf-8")) > 1024 * 1024
        ):  # pragma: no cover - validated input boundary
            raise GitMutationRejectedError("Git staged commit content is invalid")
        self._assert_before_clean()
        self._assert_admission_current()
        target = (self._repository / relative).resolve()
        try:
            target.relative_to(self._repository)
            status = target.lstat()
        except (OSError, ValueError) as error:  # pragma: no cover - filesystem race boundary
            raise GitMutationRejectedError("Git staged commit target is unavailable") from error
        ancestor = self._repository
        for component in Path(relative).parts[:-1]:
            ancestor /= component
            if ancestor.is_symlink() or (
                ancestor.exists() and not ancestor.is_dir()
            ):  # pragma: no cover - filesystem race boundary
                raise GitMutationRejectedError("Git staged commit parent is unsafe")
        if stat.S_ISLNK(status.st_mode) or not stat.S_ISREG(
            status.st_mode
        ):  # pragma: no cover - filesystem race boundary
            raise GitMutationRejectedError("Git staged commit target is unsafe")
        descriptor, temporary = tempfile.mkstemp(prefix=".agent-workflow-stage-", dir=target.parent)
        temporary_path = Path(temporary)
        try:
            with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                stream.write(content)
                stream.flush()
                os.fsync(stream.fileno())
            temporary_path.chmod(stat.S_IMODE(status.st_mode))
            temporary_path.replace(target)
            directory = os.open(target.parent, os.O_DIRECTORY)
            try:
                os.fsync(directory)
            finally:
                os.close(directory)
            self._git("add", "--", relative)
        except GitMutationError as error:  # pragma: no cover - injected effect failure boundary
            raise GitMutationAmbiguousError("Git staged commit outcome is ambiguous") from error
        except BaseException as error:  # pragma: no cover - injected effect failure boundary
            raise GitMutationAmbiguousError("Git staged commit outcome is ambiguous") from error
        finally:
            temporary_path.unlink(missing_ok=True)
        # The commit method rechecks the exact branch/head and the now-staged
        # index before invoking Git's ref mutation.
        return self.commit(message)

    def _assert_before_clean(self) -> tuple[str, str]:
        self._assert_repository_identity()
        branch = self._git("symbolic-ref", "--short", "-q", "HEAD")
        head = self._git("rev-parse", "--verify", "HEAD^{commit}")
        if (
            branch != self._expected_branch or head != self._expected_head
        ):  # pragma: no cover - stale identity boundary
            raise GitMutationRejectedError("Git authority identity changed before staging")
        status = self._git("status", "--porcelain=v1", "--untracked-files=all")
        if status:  # pragma: no cover - dirty authority boundary
            raise GitMutationRejectedError("Git authority is not clean before staging")
        return branch, head

    @staticmethod
    def _decode_commit_result(result: subprocess.CompletedProcess[str]) -> str | None:
        try:
            if result.returncode != 0:
                # A nonzero exit does not prove that Git made no ref update.
                # The caller must fence the operation and recover/reconcile
                # before a fresh capability can be issued.
                raise GitMutationAmbiguousError("Git commit outcome is ambiguous")
            return GitCommitCapability._commit_head(result)
        except GitMutationAmbiguousError:
            raise
        except BaseException as error:
            raise GitMutationAmbiguousError("Git commit outcome is ambiguous") from error

    @classmethod
    def _validate_postcondition(
        cls,
        *,
        after_branch: str,
        branch: str,
        after: str,
        before: str,
        committed_head: str,
        status: str,
    ) -> str:
        try:
            if after_branch != branch or after == before or after != committed_head or status:
                raise GitMutationAmbiguousError("Git commit postcondition is ambiguous")
            return cls._validate_head(after)
        except GitMutationAmbiguousError:
            raise
        except BaseException as error:
            raise GitMutationAmbiguousError("Git commit postcondition is ambiguous") from error

    def commit(self, message: str) -> GitCommitResult:
        if self._consumed:
            raise GitMutationError("Git mutation capability already consumed")
        message = self._validate_text(message, "commit message")
        branch, before = self._assert_before()
        self._assert_admission_current()
        self._consumed = True
        try:
            result = self._runner(
                [
                    "git",
                    "-C",
                    str(self._repository),
                    "-c",
                    "core.abbrev=40",
                    "commit",
                    "--no-verify",
                    "-m",
                    message,
                ],
                check=False,
                capture_output=True,
                text=True,
                timeout=30,
            )
        except (OSError, subprocess.TimeoutExpired) as error:
            raise GitMutationAmbiguousError("Git commit outcome is ambiguous") from error
        except BaseException as error:
            raise GitMutationAmbiguousError("Git commit outcome is ambiguous") from error
        committed_head = self._decode_commit_result(result)
        try:
            # A replacement after Git returns cannot be reported as a receipt
            # for the authority admitted before the effect.
            self._assert_admission_current()
            self._assert_repository_identity()
            after_branch = self._git("symbolic-ref", "--short", "-q", "HEAD")
            after = self._git("rev-parse", "--verify", "HEAD^{commit}")
            status = self._git("status", "--porcelain=v1", "--untracked-files=all")
        except GitMutationAmbiguousError:
            raise
        except GitMutationError as error:
            raise GitMutationAmbiguousError("Git commit postcondition is ambiguous") from error
        except BaseException as error:
            raise GitMutationAmbiguousError("Git commit postcondition is ambiguous") from error
        if committed_head is None:
            committed_head = after
        validated_after = self._validate_postcondition(
            after_branch=after_branch,
            branch=branch,
            after=after,
            before=before,
            committed_head=committed_head,
            status=status,
        )
        return GitCommitResult(
            backend=self._admission.backend,
            target=self._admission.target,
            operation_id=self._operation_id,
            state_revision=self._admission.state_revision,
            barrier_id=self._admission.barrier_id,
            artifact_identity=self._admission.artifact_identity,
            manifest_identity=self._admission.manifest_identity,
            selector_identity=self._admission.selector_identity,
            runtime_identity=self._admission.runtime_identity,
            before_head=before,
            after_head=validated_after,
            branch=branch,
            fencing_token=self._fencing_token,
        )
