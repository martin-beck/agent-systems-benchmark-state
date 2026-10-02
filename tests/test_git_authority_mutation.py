# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Hostile tests for the isolated Git authority commit capability."""

# The executable and arguments are fixed test fixtures.
# ruff: noqa: S603, S607

from __future__ import annotations

import multiprocessing
import os
import signal
import subprocess
import tempfile
import unittest
from pathlib import Path
from typing import Any, cast
from unittest.mock import patch

from tools.authority_mutation import AuthorityMutationRejectedError, DurableBoundAuthorityMutation
from tools.authority_neutral_commit import CommitAdmissionBundle
from tools.git_authority_mutation import (
    GitCommitCapability,
    GitMutationAmbiguousError,
    GitMutationError,
    GitMutationRejectedError,
)


def _git(root: Path, *args: str) -> str:
    # Test-only fixed executable and arguments.
    result = subprocess.run(
        ["git", "-C", str(root), *args], check=True, capture_output=True, text=True
    )
    return result.stdout.rstrip("\n")


def _commit_then_kill_worker(root_text: str, expected_head: str) -> None:
    root = Path(root_text)
    admission = CommitAdmissionBundle(
        backend="git",
        target="new",
        operation_id="op-process-death:commit",
        fencing_token="fence-process-death",  # noqa: S106
        state_revision=1,
        barrier_id="barrier-process-death",
        artifact_identity="artifact-1",
        manifest_identity="manifest-1",
        selector_identity="selector-1",
        runtime_identity="runtime-1",
    )

    def runner(*args: object, **kwargs: object) -> subprocess.CompletedProcess[str]:
        command = cast(list[str], args[0])
        result = subprocess.run(command, **cast(Any, kwargs))
        if "commit" in command and result.returncode == 0:
            os.kill(os.getpid(), signal.SIGKILL)
        return result

    GitCommitCapability(
        root,
        admission=admission,
        admission_reread=lambda: admission.__dict__,
        expected_branch="main",
        expected_head=expected_head,
        runner=runner,
    ).commit("op-process-death authority commit")


def _stale_owner_git_worker(
    root_text: str,
    expected_head: str,
    owner_file_text: str,
    ready: Any,
    proceed: Any,
    result_queue: Any,
) -> None:
    root = Path(root_text)
    owner_file = Path(owner_file_text)
    admission = CommitAdmissionBundle(
        backend="git",
        target="new",
        operation_id="op-stale-owner:commit",
        fencing_token="fence-1",  # noqa: S106
        state_revision=1,
        barrier_id="barrier-stale-owner",
        artifact_identity="artifact-1",
        manifest_identity="manifest-1",
        selector_identity="selector-1",
        runtime_identity="runtime-1",
    )

    def reread() -> dict[str, object]:
        current = dict(admission.__dict__)
        current["fencing_token"] = owner_file.read_text(encoding="utf-8")
        return current

    capability = GitCommitCapability(
        root,
        admission=admission,
        admission_reread=reread,
        expected_branch="main",
        expected_head=expected_head,
    )
    ready.set()
    proceed.wait(5)
    try:
        capability.commit("op-stale-owner authority commit")
    except GitMutationRejectedError:
        result_queue.put("rejected")
    except BaseException as error:
        result_queue.put(f"unexpected:{type(error).__name__}")
    else:
        result_queue.put("committed")


def _pre_effect_git_death_worker(root_text: str, expected_head: str) -> None:
    root = Path(root_text)
    admission = CommitAdmissionBundle(
        backend="git",
        target="new",
        operation_id="op-pre-effect-death:commit",
        fencing_token="fence-pre-effect-death",  # noqa: S106
        state_revision=1,
        barrier_id="barrier-pre-effect-death",
        artifact_identity="artifact-1",
        manifest_identity="manifest-1",
        selector_identity="selector-1",
        runtime_identity="runtime-1",
    )
    capability = GitCommitCapability(
        root,
        admission=admission,
        admission_reread=lambda: admission.__dict__,
        expected_branch="main",
        expected_head=expected_head,
    )
    os.kill(os.getpid(), signal.SIGKILL)
    capability.commit("unreachable")


class GitCommitCapabilityTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        _git(self.root, "init", "-b", "main")
        _git(self.root, "config", "user.name", "Test Runner")
        _git(self.root, "config", "user.email", "test@example.invalid")
        (self.root / "state").write_text("old\n", encoding="utf-8")
        _git(self.root, "add", "state")
        _git(self.root, "commit", "-m", "initial")

    def tearDown(self) -> None:
        self.temp.cleanup()

    @staticmethod
    def _admission() -> CommitAdmissionBundle:
        return CommitAdmissionBundle(
            backend="git",
            target="new",
            operation_id="op-1:commit",
            fencing_token="fence-1",  # noqa: S106
            state_revision=1,
            barrier_id="barrier-1",
            artifact_identity="artifact-1",
            manifest_identity="manifest-1",
            selector_identity="selector-1",
            runtime_identity="runtime-1",
        )

    def _capability(self) -> GitCommitCapability:
        admission = self._admission()
        return GitCommitCapability(
            self.root,
            admission=admission,
            admission_reread=lambda: admission.__dict__,
            expected_branch="main",
            expected_head=_git(self.root, "rev-parse", "HEAD"),
        )

    def test_commits_only_pre_staged_change_and_verifies_postconditions(self) -> None:
        (self.root / "state").write_text("new\n", encoding="utf-8")
        _git(self.root, "add", "state")
        result = self._capability().commit("op-1 authority commit")
        self.assertEqual(
            (
                "git",
                "new",
                "op-1:commit",
                1,
                "barrier-1",
                "artifact-1",
                "manifest-1",
                "selector-1",
                "runtime-1",
                "fence-1",
            ),
            (
                result.backend,
                result.target,
                result.operation_id,
                result.state_revision,
                result.barrier_id,
                result.artifact_identity,
                result.manifest_identity,
                result.selector_identity,
                result.runtime_identity,
                result.fencing_token,
            ),
        )
        self.assertEqual("main", result.branch)
        self.assertNotEqual(result.before_head, result.after_head)
        self.assertEqual(40, len(result.after_head))
        self.assertTrue(result.mutates_authority)
        self.assertEqual("", _git(self.root, "status", "--porcelain=v1", "--untracked-files=all"))

    def test_stage_and_commit_binds_selector_payload_inside_effect(self) -> None:
        runtime = self.root / ".runtime"
        runtime.mkdir(mode=0o700)
        selector = runtime / "runtime-selector.json"
        selector.write_text(
            '{"schema_version":1,"active_release":"v0.1.0","previous_release":"v0.0.9"}\n',
            encoding="utf-8",
        )
        _git(self.root, "add", ".runtime/runtime-selector.json")
        _git(self.root, "commit", "-m", "add runtime selector")
        before = _git(self.root, "rev-parse", "HEAD")
        admission = self._admission()
        result = GitCommitCapability(
            self.root,
            admission=admission,
            admission_reread=lambda: admission.__dict__,
            expected_branch="main",
            expected_head=before,
        ).stage_and_commit(
            {
                "message": "op-1 select staged runtime",
                "path": ".runtime/runtime-selector.json",
                "content": '{"schema_version":1,"active_release":"v0.2.0",'
                '"previous_release":"v0.1.0"}\n',
            }
        )
        self.assertNotEqual(before, result.after_head)
        self.assertIn('"active_release":"v0.2.0"', selector.read_text(encoding="utf-8"))
        self.assertEqual("", _git(self.root, "status", "--porcelain=v1", "--untracked-files=all"))

    def test_stage_and_commit_rejects_invalid_payloads_and_staging_failure(self) -> None:
        admission = self._admission()
        head = _git(self.root, "rev-parse", "HEAD")

        def capability(runner: Any = subprocess.run) -> GitCommitCapability:
            return GitCommitCapability(
                self.root,
                admission=admission,
                admission_reread=lambda: admission.__dict__,
                expected_branch="main",
                expected_head=head,
                runner=runner,
            )

        for argument in (
            {"message": "m", "path": "state"},
            {"message": 1, "path": "state", "content": "new\n"},
            {"message": "m", "path": "../state", "content": "new\n"},
            {"message": "m", "path": "state", "content": "new\n" * (1024 * 1024)},
        ):
            with self.assertRaises(GitMutationRejectedError):
                capability().stage_and_commit(argument)

        def failing_runner(*_args: object, **_kwargs: object) -> subprocess.CompletedProcess[str]:
            command = cast(list[str], _args[0])
            if "add" not in command:
                return subprocess.run(command, **cast(Any, _kwargs))
            return subprocess.CompletedProcess([], 1, stdout="", stderr="staging failed")

        with self.assertRaises(GitMutationAmbiguousError):
            capability(failing_runner).stage_and_commit(
                {"message": "m", "path": "state", "content": "new\n"}
            )

        consumed = capability()
        (self.root / "state").write_text("new\n", encoding="utf-8")
        _git(self.root, "add", "state")
        consumed.commit("op-1 authority commit")
        with self.assertRaises(GitMutationError):
            consumed.stage_and_commit({"message": "m", "path": "state", "content": "again\n"})

    def test_capability_is_single_use_but_fresh_capability_reopens(self) -> None:
        (self.root / "state").write_text("first\n", encoding="utf-8")
        _git(self.root, "add", "state")
        capability = self._capability()
        capability.commit("op-1 authority commit")

        with self.assertRaisesRegex(GitMutationError, "already consumed"):
            capability.commit("op-1 replay")

        (self.root / "state").write_text("second\n", encoding="utf-8")
        _git(self.root, "add", "state")
        reopened_admission = CommitAdmissionBundle(
            backend="git",
            target="new",
            operation_id="op-2:commit",
            fencing_token="fence-2",  # noqa: S106
            state_revision=2,
            barrier_id="barrier-2",
            artifact_identity="artifact-1",
            manifest_identity="manifest-1",
            selector_identity="selector-1",
            runtime_identity="runtime-1",
        )
        result = GitCommitCapability(
            self.root,
            admission=reopened_admission,
            admission_reread=lambda: reopened_admission.__dict__,
            expected_branch="main",
            expected_head=_git(self.root, "rev-parse", "HEAD"),
        ).commit("op-2 authority commit")
        self.assertEqual("fence-2", result.fencing_token)
        self.assertEqual("second\n", (self.root / "state").read_text(encoding="utf-8"))

    def test_independent_process_death_after_effect_requires_fresh_capability(self) -> None:
        (self.root / "state").write_text("new\n", encoding="utf-8")
        _git(self.root, "add", "state")
        before = _git(self.root, "rev-parse", "HEAD")
        context = multiprocessing.get_context("fork")
        worker = context.Process(target=_commit_then_kill_worker, args=(str(self.root), before))
        worker.start()
        worker.join(10)
        self.assertEqual(-signal.SIGKILL, worker.exitcode)

        after = _git(self.root, "rev-parse", "HEAD")
        self.assertNotEqual(before, after)
        self.assertEqual("new\n", (self.root / "state").read_text(encoding="utf-8"))
        self.assertEqual("", _git(self.root, "status", "--porcelain=v1", "--untracked-files=all"))

        (self.root / "state").write_text("reopened\n", encoding="utf-8")
        _git(self.root, "add", "state")
        admission = CommitAdmissionBundle(
            backend="git",
            target="new",
            operation_id="op-process-death-reopen:commit",
            fencing_token="fence-process-death-reopen",  # noqa: S106
            state_revision=2,
            barrier_id="barrier-process-death-reopen",
            artifact_identity="artifact-1",
            manifest_identity="manifest-1",
            selector_identity="selector-1",
            runtime_identity="runtime-1",
        )
        result = GitCommitCapability(
            self.root,
            admission=admission,
            admission_reread=lambda: admission.__dict__,
            expected_branch="main",
            expected_head=after,
        ).commit("op-process-death-reopen authority commit")
        self.assertEqual(40, len(result.after_head))
        self.assertNotEqual(after, result.after_head)

    def test_independent_process_stale_owner_replacement_rejects_before_effect(self) -> None:
        (self.root / "state").write_text("new\n", encoding="utf-8")
        _git(self.root, "add", "state")
        before = _git(self.root, "rev-parse", "HEAD")
        owner_file = self.root / "owner-fence"
        owner_file.write_text("fence-1", encoding="utf-8")
        context = multiprocessing.get_context("fork")
        ready = context.Event()
        proceed = context.Event()
        result_queue = context.Queue()
        worker = context.Process(
            target=_stale_owner_git_worker,
            args=(str(self.root), before, str(owner_file), ready, proceed, result_queue),
        )
        worker.start()
        self.assertTrue(ready.wait(5))
        owner_file.write_text("foreign-fence", encoding="utf-8")
        proceed.set()
        worker.join(10)
        self.assertEqual(0, worker.exitcode)
        self.assertEqual("rejected", result_queue.get(timeout=2))
        self.assertEqual(before, _git(self.root, "rev-parse", "HEAD"))
        owner_file.unlink()
        self.assertEqual("M  state", _git(self.root, "status", "--porcelain=v1"))

    def test_independent_process_death_before_effect_allows_fresh_capability(self) -> None:
        (self.root / "state").write_text("new\n", encoding="utf-8")
        _git(self.root, "add", "state")
        before = _git(self.root, "rev-parse", "HEAD")
        context = multiprocessing.get_context("fork")
        worker = context.Process(target=_pre_effect_git_death_worker, args=(str(self.root), before))
        worker.start()
        worker.join(10)
        self.assertEqual(-signal.SIGKILL, worker.exitcode)
        self.assertEqual(before, _git(self.root, "rev-parse", "HEAD"))

        admission = CommitAdmissionBundle(
            backend="git",
            target="new",
            operation_id="op-pre-effect-reopen:commit",
            fencing_token="fence-pre-effect-reopen",  # noqa: S106
            state_revision=2,
            barrier_id="barrier-pre-effect-reopen",
            artifact_identity="artifact-1",
            manifest_identity="manifest-1",
            selector_identity="selector-1",
            runtime_identity="runtime-1",
        )
        result = GitCommitCapability(
            self.root,
            admission=admission,
            admission_reread=lambda: admission.__dict__,
            expected_branch="main",
            expected_head=before,
        ).commit("op-pre-effect-reopen authority commit")
        self.assertNotEqual(before, result.after_head)

    def test_rejects_termination_during_initial_repository_identity(self) -> None:
        with (
            patch.object(
                GitCommitCapability,
                "_read_repository_identity",
                side_effect=KeyboardInterrupt("injected termination"),
            ),
            self.assertRaisesRegex(GitMutationError, "identity capture was rejected"),
        ):
            self._capability()

    def test_rejects_termination_during_initial_repository_ancestor_identity(self) -> None:
        with (
            patch.object(
                GitCommitCapability,
                "_read_ancestor_identities",
                side_effect=KeyboardInterrupt("injected termination"),
            ),
            self.assertRaisesRegex(GitMutationError, "identity capture was rejected"),
        ):
            self._capability()

    def test_rejects_termination_during_initial_repository_path_normalization(self) -> None:
        with (
            patch.object(Path, "absolute", side_effect=KeyboardInterrupt("injected termination")),
            self.assertRaisesRegex(GitMutationError, "identity capture was rejected"),
        ):
            self._capability()

    def test_rejects_unstaged_or_empty_changes(self) -> None:
        with self.assertRaisesRegex(GitMutationError, "no staged"):
            self._capability().commit("op-1 authority commit")
        (self.root / "state").write_text("new\n", encoding="utf-8")
        with self.assertRaisesRegex(GitMutationError, "unstaged"):
            self._capability().commit("op-1 authority commit")

    def test_rejects_head_drift_and_ambiguous_runner_outcome(self) -> None:
        (self.root / "state").write_text("new\n", encoding="utf-8")
        _git(self.root, "add", "state")
        stale = GitCommitCapability(
            self.root,
            admission=self._admission(),
            admission_reread=lambda: self._admission().__dict__,
            expected_branch="main",
            expected_head="0" * 40,
        )
        with self.assertRaisesRegex(GitMutationError, "identity changed"):
            stale.commit("op-1 authority commit")

        calls = 0

        def timeout_runner(*_args: object, **_kwargs: object) -> subprocess.CompletedProcess[str]:
            nonlocal calls
            calls += 1
            if calls == 4:
                raise subprocess.TimeoutExpired("git", 30)
            return cast(
                subprocess.CompletedProcess[str],
                subprocess.run(cast(Any, _args[0]), **cast(Any, _kwargs)),
            )

        with self.assertRaises(GitMutationAmbiguousError):
            GitCommitCapability(
                self.root,
                admission=self._admission(),
                admission_reread=lambda: self._admission().__dict__,
                expected_branch="main",
                expected_head=self._capability()._expected_head,
                runner=timeout_runner,
            ).commit("op-1 authority commit")

    def test_rejects_identity_runner_oserror_before_effect(self) -> None:
        (self.root / "state").write_text("new\n", encoding="utf-8")
        _git(self.root, "add", "state")

        def failing_runner(*_args: object, **_kwargs: object) -> subprocess.CompletedProcess[str]:
            raise OSError("injected identity read failure")

        with self.assertRaisesRegex(GitMutationRejectedError, "identity reread was rejected"):
            GitCommitCapability(
                self.root,
                admission=self._admission(),
                admission_reread=lambda: self._admission().__dict__,
                expected_branch="main",
                expected_head=self._capability()._expected_head,
                runner=failing_runner,
            ).commit("op-1 authority commit")
        self.assertEqual("M  state", _git(self.root, "status", "--porcelain=v1"))

    def test_rejects_symlinked_repository_path(self) -> None:
        alias = self.root / "repository-alias"
        alias.symlink_to(self.root, target_is_directory=True)
        with self.assertRaisesRegex(GitMutationError, "not a regular directory"):
            GitCommitCapability(
                alias,
                admission=self._admission(),
                admission_reread=lambda: self._admission().__dict__,
                expected_branch="main",
                expected_head=_git(self.root, "rev-parse", "HEAD"),
            )

    def test_rejects_repository_replacement_before_effect(self) -> None:
        (self.root / "state").write_text("new\n", encoding="utf-8")
        _git(self.root, "add", "state")
        capability = self._capability()
        replacement = self.root.parent / f"{self.root.name}-replaced"
        self.root.rename(replacement)
        self.root.mkdir()

        with self.assertRaisesRegex(GitMutationRejectedError, "repository identity changed"):
            capability.commit("op-1 authority commit")

    def test_rejects_repository_parent_replacement_before_effect(self) -> None:
        (self.root / "state").write_text("new\n", encoding="utf-8")
        _git(self.root, "add", "state")
        capability = self._capability()
        original_parent = self.root.parent
        relocated_parent = original_parent / f"{self.root.name}-parent-replaced"
        self.root.rename(relocated_parent)
        self.root.mkdir()

        with self.assertRaisesRegex(GitMutationRejectedError, "repository identity changed"):
            capability.commit("op-1 authority commit")

    def test_rejects_repository_ancestor_replacement_before_effect(self) -> None:
        (self.root / "state").write_text("new\n", encoding="utf-8")
        _git(self.root, "add", "state")
        outer = self.root.parent / f"{self.root.name}-outer"
        inner = outer / "inner"
        inner.mkdir(parents=True)
        relocated = inner / "repository"
        self.root.rename(relocated)
        capability = GitCommitCapability(
            relocated,
            admission=self._admission(),
            admission_reread=lambda: self._admission().__dict__,
            expected_branch="main",
            expected_head=_git(relocated, "rev-parse", "HEAD"),
        )
        replacement = outer.parent / f"{outer.name}-replaced"
        outer.rename(replacement)
        outer.mkdir()

        with self.assertRaisesRegex(GitMutationRejectedError, "repository identity changed"):
            capability.commit("op-1 authority commit")

    def test_rejects_symlinked_repository_ancestor_before_effect(self) -> None:
        (self.root / "state").write_text("new\n", encoding="utf-8")
        _git(self.root, "add", "state")
        outer = self.root.parent / f"{self.root.name}-symlink-outer"
        inner = outer / "inner"
        inner.mkdir(parents=True)
        relocated = inner / "repository"
        self.root.rename(relocated)
        capability = GitCommitCapability(
            relocated,
            admission=self._admission(),
            admission_reread=lambda: self._admission().__dict__,
            expected_branch="main",
            expected_head=_git(relocated, "rev-parse", "HEAD"),
        )
        replacement = outer.parent / f"{outer.name}-target"
        outer.rename(replacement)
        outer.symlink_to(replacement, target_is_directory=True)

        with self.assertRaisesRegex(GitMutationRejectedError, "repository identity changed"):
            capability.commit("op-1 authority commit")

    def test_classifies_commit_runner_oserror_as_ambiguous(self) -> None:
        (self.root / "state").write_text("new\n", encoding="utf-8")
        _git(self.root, "add", "state")

        def failing_runner(*args: object, **kwargs: object) -> subprocess.CompletedProcess[str]:
            command = cast(list[str], args[0])
            if "commit" in command:
                raise OSError("injected commit failure")
            return cast(
                subprocess.CompletedProcess[str],
                subprocess.run(command, **cast(Any, kwargs)),
            )

        with self.assertRaisesRegex(GitMutationAmbiguousError, "commit outcome is ambiguous"):
            capability = GitCommitCapability(
                self.root,
                admission=self._admission(),
                admission_reread=lambda: self._admission().__dict__,
                expected_branch="main",
                expected_head=self._capability()._expected_head,
                runner=failing_runner,
            )
            capability.commit("op-1 authority commit")
        self.assertEqual("M  state", _git(self.root, "status", "--porcelain=v1"))

        with self.assertRaisesRegex(GitMutationError, "already consumed"):
            capability.commit("op-1 retry")

    def test_classifies_termination_commit_runner_as_ambiguous(self) -> None:
        (self.root / "state").write_text("new\n", encoding="utf-8")
        _git(self.root, "add", "state")

        def terminating_runner(*args: object, **kwargs: object) -> subprocess.CompletedProcess[str]:
            command = cast(list[str], args[0])
            if "commit" in command:
                raise KeyboardInterrupt("injected termination")
            return cast(
                subprocess.CompletedProcess[str],
                subprocess.run(command, **cast(Any, kwargs)),
            )

        with self.assertRaisesRegex(GitMutationAmbiguousError, "commit outcome is ambiguous"):
            GitCommitCapability(
                self.root,
                admission=self._admission(),
                admission_reread=lambda: self._admission().__dict__,
                expected_branch="main",
                expected_head=self._capability()._expected_head,
                runner=terminating_runner,
            ).commit("op-1 authority commit")
        self.assertEqual("M  state", _git(self.root, "status", "--porcelain=v1"))

    def test_classifies_termination_commit_result_decoding_as_ambiguous(self) -> None:
        (self.root / "state").write_text("new\n", encoding="utf-8")
        _git(self.root, "add", "state")

        class TerminatingResult:
            returncode = 0

            @property
            def stdout(self) -> str:
                raise KeyboardInterrupt("injected termination")

            @property
            def stderr(self) -> str:
                return ""

        def runner(*args: object, **kwargs: object) -> subprocess.CompletedProcess[str]:
            command = cast(list[str], args[0])
            if "commit" in command:
                return cast(subprocess.CompletedProcess[str], TerminatingResult())
            return cast(
                subprocess.CompletedProcess[str], subprocess.run(command, **cast(Any, kwargs))
            )

        with self.assertRaisesRegex(GitMutationAmbiguousError, "commit outcome is ambiguous"):
            GitCommitCapability(
                self.root,
                admission=self._admission(),
                admission_reread=lambda: self._admission().__dict__,
                expected_branch="main",
                expected_head=self._capability()._expected_head,
                runner=runner,
            ).commit("op-1 authority commit")
        self.assertEqual("M  state", _git(self.root, "status", "--porcelain=v1"))

    def test_classifies_post_commit_verification_termination_as_ambiguous(self) -> None:
        (self.root / "state").write_text("new\n", encoding="utf-8")
        _git(self.root, "add", "state")
        committed = False

        def terminating_runner(*args: object, **kwargs: object) -> subprocess.CompletedProcess[str]:
            nonlocal committed
            command = cast(list[str], args[0])
            if committed and command[-3:-1] == ["rev-parse", "--verify"]:
                raise KeyboardInterrupt("injected termination")
            result = subprocess.run(command, **cast(Any, kwargs))
            if "commit" in command and result.returncode == 0:
                committed = True
            return cast(subprocess.CompletedProcess[str], result)

        with self.assertRaisesRegex(GitMutationAmbiguousError, "postcondition is ambiguous"):
            GitCommitCapability(
                self.root,
                admission=self._admission(),
                admission_reread=lambda: self._admission().__dict__,
                expected_branch="main",
                expected_head=self._capability()._expected_head,
                runner=terminating_runner,
            ).commit("op-1 authority commit")
        self.assertEqual("", _git(self.root, "status", "--porcelain=v1"))

    def test_classifies_nonzero_commit_after_ref_update_as_ambiguous(self) -> None:
        (self.root / "state").write_text("new\n", encoding="utf-8")
        _git(self.root, "add", "state")

        def commit_then_fail(*args: object, **kwargs: object) -> subprocess.CompletedProcess[str]:
            command = cast(list[str], args[0])
            result = subprocess.run(command, **cast(Any, kwargs))
            if "commit" in command and result.returncode == 0:
                return subprocess.CompletedProcess(
                    command,
                    1,
                    stdout=result.stdout,
                    stderr="commit result delivery failed",
                )
            return result

        capability = GitCommitCapability(
            self.root,
            admission=self._admission(),
            admission_reread=lambda: self._admission().__dict__,
            expected_branch="main",
            expected_head=_git(self.root, "rev-parse", "HEAD"),
            runner=commit_then_fail,
        )
        with self.assertRaisesRegex(GitMutationAmbiguousError, "outcome is ambiguous"):
            capability.commit("op-1 authority commit")
        self.assertEqual("", _git(self.root, "status", "--porcelain=v1"))
        self.assertEqual("new\n", (self.root / "state").read_text(encoding="utf-8"))

    def test_classifies_post_commit_identity_reread_failure_as_ambiguous(self) -> None:
        (self.root / "state").write_text("new\n", encoding="utf-8")
        _git(self.root, "add", "state")
        committed = False

        def fail_after_commit(*args: object, **kwargs: object) -> subprocess.CompletedProcess[str]:
            nonlocal committed
            command = cast(list[str], args[0])
            if committed and command[-3:-1] == ["rev-parse", "--verify"]:
                return subprocess.CompletedProcess(command, 1, stdout="", stderr="reread failed")
            result = subprocess.run(command, **cast(Any, kwargs))
            if "commit" in command and result.returncode == 0:
                committed = True
            return result

        capability = GitCommitCapability(
            self.root,
            admission=self._admission(),
            admission_reread=lambda: self._admission().__dict__,
            expected_branch="main",
            expected_head=_git(self.root, "rev-parse", "HEAD"),
            runner=fail_after_commit,
        )
        with self.assertRaisesRegex(GitMutationAmbiguousError, "postcondition"):
            capability.commit("op-1 authority commit")
        self.assertEqual("", _git(self.root, "status", "--porcelain=v1"))

    def test_post_commit_admission_drift_requires_fresh_capability(self) -> None:
        (self.root / "state").write_text("new\n", encoding="utf-8")
        _git(self.root, "add", "state")
        admission = self._admission()
        stale = dict(admission.__dict__)
        stale["fencing_token"] = "replaced-owner"  # noqa: S105
        reads = 0

        def reread() -> dict[str, object]:
            nonlocal reads
            reads += 1
            return admission.__dict__ if reads == 1 else stale

        capability = GitCommitCapability(
            self.root,
            admission=admission,
            admission_reread=reread,
            expected_branch="main",
            expected_head=_git(self.root, "rev-parse", "HEAD"),
        )
        with self.assertRaisesRegex(GitMutationAmbiguousError, "postcondition"):
            capability.commit("op-1 authority commit")
        self.assertEqual(2, reads)
        self.assertEqual("", _git(self.root, "status", "--porcelain=v1"))

        (self.root / "state").write_text("recovered\n", encoding="utf-8")
        _git(self.root, "add", "state")
        reopened = CommitAdmissionBundle(
            backend="git",
            target="new",
            operation_id="op-recovered:commit",
            fencing_token="fence-recovered",  # noqa: S106
            state_revision=2,
            barrier_id="barrier-recovered",
            artifact_identity="artifact-1",
            manifest_identity="manifest-1",
            selector_identity="selector-1",
            runtime_identity="runtime-1",
        )
        result = GitCommitCapability(
            self.root,
            admission=reopened,
            admission_reread=lambda: reopened.__dict__,
            expected_branch="main",
            expected_head=_git(self.root, "rev-parse", "HEAD"),
        ).commit("op-recovered authority commit")
        self.assertEqual(40, len(result.after_head))

    def test_classifies_malformed_post_commit_head_as_ambiguous(self) -> None:
        (self.root / "state").write_text("new\n", encoding="utf-8")
        _git(self.root, "add", "state")
        committed = False
        committed_head = ""

        def malformed_after(*args: object, **kwargs: object) -> subprocess.CompletedProcess[str]:
            nonlocal committed, committed_head
            command = cast(list[str], args[0])
            if committed and command[-3:-1] == ["rev-parse", "--verify"]:
                return subprocess.CompletedProcess(
                    command, 0, stdout=f"{committed_head}invalid\n", stderr=""
                )
            result = cast(
                subprocess.CompletedProcess[str],
                subprocess.run(command, **cast(Any, kwargs)),
            )
            if "commit" in command and result.returncode == 0:
                committed = True
                committed_head = result.stdout.split()[1]
            return result

        with self.assertRaisesRegex(GitMutationAmbiguousError, "postcondition is ambiguous"):
            GitCommitCapability(
                self.root,
                admission=self._admission(),
                admission_reread=lambda: self._admission().__dict__,
                expected_branch="main",
                expected_head=self._capability()._expected_head,
                runner=malformed_after,
            ).commit("op-1 authority commit")
        self.assertEqual("", _git(self.root, "status", "--porcelain=v1"))

    def test_classifies_termination_admission_reread_as_rejected(self) -> None:
        (self.root / "state").write_text("new\n", encoding="utf-8")
        _git(self.root, "add", "state")

        def terminating_reread() -> dict[str, object]:
            raise KeyboardInterrupt("injected termination")

        capability = GitCommitCapability(
            self.root,
            admission=self._admission(),
            admission_reread=terminating_reread,
            expected_branch="main",
            expected_head=_git(self.root, "rev-parse", "HEAD"),
        )
        with self.assertRaisesRegex(GitMutationRejectedError, "admission reread was rejected"):
            capability.commit("op-1 authority commit")
        self.assertEqual("M  state", _git(self.root, "status", "--porcelain=v1"))

    def test_classifies_termination_repository_identity_reread_as_rejected(self) -> None:
        (self.root / "state").write_text("new\n", encoding="utf-8")
        _git(self.root, "add", "state")
        capability = self._capability()
        with (
            patch.object(
                GitCommitCapability,
                "_read_repository_identity",
                side_effect=KeyboardInterrupt("injected termination"),
            ),
            self.assertRaisesRegex(
                GitMutationRejectedError, "repository identity reread was rejected"
            ),
        ):
            capability.commit("op-1 authority commit")
        self.assertEqual("M  state", _git(self.root, "status", "--porcelain=v1"))

    def test_classifies_termination_git_identity_command_as_rejected(self) -> None:
        (self.root / "state").write_text("new\n", encoding="utf-8")
        _git(self.root, "add", "state")

        def terminating_runner(
            *_args: object, **_kwargs: object
        ) -> subprocess.CompletedProcess[str]:
            raise KeyboardInterrupt("injected termination")

        capability = GitCommitCapability(
            self.root,
            admission=self._admission(),
            admission_reread=lambda: self._admission().__dict__,
            expected_branch="main",
            expected_head=self._capability()._expected_head,
            runner=terminating_runner,
        )
        with self.assertRaisesRegex(GitMutationRejectedError, "identity reread was rejected"):
            capability.commit("op-1 authority commit")
        self.assertEqual("M  state", _git(self.root, "status", "--porcelain=v1"))

    def test_classifies_termination_git_identity_result_inspection_as_rejected(self) -> None:
        (self.root / "state").write_text("new\n", encoding="utf-8")
        _git(self.root, "add", "state")

        class TerminatingResult:
            @property
            def returncode(self) -> int:
                raise KeyboardInterrupt("injected termination")

        def terminating_runner(
            *_args: object, **_kwargs: object
        ) -> subprocess.CompletedProcess[str]:
            return cast(subprocess.CompletedProcess[str], TerminatingResult())

        capability = GitCommitCapability(
            self.root,
            admission=self._admission(),
            admission_reread=lambda: self._admission().__dict__,
            expected_branch="main",
            expected_head=self._capability()._expected_head,
            runner=terminating_runner,
        )
        with self.assertRaisesRegex(GitMutationRejectedError, "identity reread was rejected"):
            capability.commit("op-1 authority commit")
        self.assertEqual("M  state", _git(self.root, "status", "--porcelain=v1"))

    def test_classifies_repository_replacement_after_effect_as_ambiguous(self) -> None:
        (self.root / "state").write_text("new\n", encoding="utf-8")
        _git(self.root, "add", "state")

        def replace_after_commit(
            *args: object, **kwargs: object
        ) -> subprocess.CompletedProcess[str]:
            command = cast(list[str], args[0])
            result = cast(
                subprocess.CompletedProcess[str],
                subprocess.run(command, **cast(Any, kwargs)),
            )
            if "commit" in command and result.returncode == 0:
                replacement = self.root.parent / f"{self.root.name}-post-effect-replaced"
                self.root.rename(replacement)
                self.root.mkdir()
            return result

        capability = GitCommitCapability(
            self.root,
            admission=self._admission(),
            admission_reread=lambda: self._admission().__dict__,
            expected_branch="main",
            expected_head=_git(self.root, "rev-parse", "HEAD"),
            runner=replace_after_commit,
        )
        with self.assertRaisesRegex(GitMutationAmbiguousError, "postcondition"):
            capability.commit("op-1 authority commit")

    def test_rejects_a_concurrent_commit_after_the_effect(self) -> None:
        (self.root / "state").write_text("new\n", encoding="utf-8")
        _git(self.root, "add", "state")

        def racing_runner(*args: object, **kwargs: object) -> subprocess.CompletedProcess[str]:
            command = cast(list[str], args[0])
            result = cast(
                subprocess.CompletedProcess[str],
                subprocess.run(command, **cast(Any, kwargs)),
            )
            if "commit" in command and result.returncode == 0:
                (self.root / "race").write_text("concurrent\n", encoding="utf-8")
                _git(self.root, "add", "race")
                _git(self.root, "commit", "--no-verify", "-m", "concurrent writer")
            return result

        with self.assertRaisesRegex(GitMutationAmbiguousError, "postcondition"):
            GitCommitCapability(
                self.root,
                admission=self._admission(),
                admission_reread=lambda: self._admission().__dict__,
                expected_branch="main",
                expected_head=self._capability()._expected_head,
                runner=racing_runner,
            ).commit("op-1 authority commit")

    def test_rejects_stale_admission_reread_before_effect(self) -> None:
        (self.root / "state").write_text("new\n", encoding="utf-8")
        _git(self.root, "add", "state")
        admission = self._admission()
        stale = dict(admission.__dict__)
        stale["fencing_token"] = "foreign-fence"  # noqa: S105
        before = _git(self.root, "rev-parse", "HEAD")
        capability = GitCommitCapability(
            self.root,
            admission=admission,
            admission_reread=lambda: stale,
            expected_branch="main",
            expected_head=_git(self.root, "rev-parse", "HEAD"),
        )
        with self.assertRaisesRegex(GitMutationRejectedError, "admission identity changed"):
            capability.commit("op-1 authority commit")
        self.assertEqual(before, _git(self.root, "rev-parse", "HEAD"))
        self.assertEqual("M  state", _git(self.root, "status", "--porcelain=v1"))

    def test_integrated_pre_effect_rejection_is_journaled_without_git_commit(self) -> None:
        (self.root / "state").write_text("new\n", encoding="utf-8")
        _git(self.root, "add", "state")
        admission = self._admission()
        stale = dict(admission.__dict__)
        stale["fencing_token"] = "foreign-fence"  # noqa: S105
        capability = GitCommitCapability(
            self.root,
            admission=admission,
            admission_reread=lambda: stale,
            expected_branch="main",
            expected_head=_git(self.root, "rev-parse", "HEAD"),
        )
        journal: list[tuple[str, object | None]] = []

        class Journal:
            def prepare_authority_effect(self, *_args: object, **_kwargs: object) -> str:
                journal.append(("prepared", None))
                return "intent-git-rejected"

            def finish_authority_effect(
                self, _intent: object, outcome: str, receipt: object | None = None
            ) -> None:
                journal.append((outcome, receipt))

        with self.assertRaisesRegex(AuthorityMutationRejectedError, "admission identity changed"):
            DurableBoundAuthorityMutation(admission, Journal(), session_revision=1).execute(
                lambda: capability.commit("op-1 authority commit")
            )
        self.assertEqual([("prepared", None), ("rejected", None)], journal)
        self.assertEqual("M  state", _git(self.root, "status", "--porcelain=v1"))
        self.assertEqual(admission.state_revision, 1)
        self.assertEqual(admission.fencing_token, "fence-1")

    def test_rejects_every_admission_identity_drift_before_effect(self) -> None:
        (self.root / "state").write_text("new\n", encoding="utf-8")
        _git(self.root, "add", "state")
        admission = self._admission()
        before = _git(self.root, "rev-parse", "HEAD")
        changes: dict[str, object] = {
            "backend": "sqlite",
            "target": "rollback",
            "operation_id": "foreign-operation",
            "fencing_token": "foreign-fence",
            "state_revision": 2,
            "barrier_id": "foreign-barrier",
            "artifact_identity": "foreign-artifact",
            "manifest_identity": "foreign-manifest",
            "selector_identity": "foreign-selector",
            "runtime_identity": "foreign-runtime",
        }

        for field, value in changes.items():
            stale = dict(admission.__dict__)
            stale[field] = value
            called = False

            def effect() -> object:
                nonlocal called
                called = True
                return object()

            def read_stale(value: dict[str, object] = stale) -> dict[str, object]:
                return value

            capability = GitCommitCapability(
                self.root,
                admission=admission,
                admission_reread=read_stale,
                expected_branch="main",
                expected_head=before,
            )
            with (
                self.subTest(field=field),
                self.assertRaisesRegex(GitMutationRejectedError, "admission identity changed"),
            ):
                capability.commit("op-1 authority commit")
            self.assertFalse(called)
            self.assertEqual(before, _git(self.root, "rev-parse", "HEAD"))
            self.assertEqual("M  state", _git(self.root, "status", "--porcelain=v1"))


if __name__ == "__main__":
    unittest.main()
