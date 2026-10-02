# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Read-only Git authority evidence for the future scoped adapter."""

# The executable and arguments are fixed by this adapter's Git observation contract.
# ruff: noqa: S603, S607

from __future__ import annotations

import subprocess
import tempfile
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import Any, cast

from tools.admission_lease import AdmissionLease, AdmissionRecheck
from tools.lifecycle_session import LifecycleSession, _issue
from tools.lock_domain_scope import LockDomainScope
from tools.rollback_evidence import BackupObservation


class GitAuthorityError(RuntimeError):
    """Git authority evidence is unavailable or a mutation was requested."""


@dataclass(frozen=True)
class GitRollbackSessionState:
    """Typed identity returned by a bound read-only Git session reread."""

    project_id: str
    authority_revision: str
    state_revision: int
    fencing_token: str
    fencing_owner: str
    durable_barrier_id: str
    git_head: str
    git_branch: str


@dataclass(frozen=True, init=False)
class GitBackupObservation:
    """Immutable verified Git backup/session evidence."""

    commit: str
    artifact_count: int
    session: GitRollbackSessionState

    def __init__(self) -> None:
        raise TypeError("Git backup observation must be created by the verifier")

    @property
    def has_provenance(self) -> bool:
        """Backend-neutral marker: only verifier-produced values are exposed."""
        return True

    @classmethod
    def _from_verified(
        cls, session: GitRollbackSessionState, result: Mapping[str, object]
    ) -> GitBackupObservation:
        if not isinstance(session, GitRollbackSessionState):
            raise GitAuthorityError("Git backup observation session is invalid")
        if (
            set(result) != {"commit", "verified", "artifact_count"}
            or result.get("verified") is not True
            or result.get("commit") != session.git_head
            or type(result.get("artifact_count")) is not int
            or cast(int, result.get("artifact_count")) < 1
        ):
            raise GitAuthorityError("Git backup verification result is invalid")
        observation = object.__new__(cls)
        object.__setattr__(observation, "commit", session.git_head)
        object.__setattr__(observation, "artifact_count", result["artifact_count"])
        object.__setattr__(observation, "session", session)
        return observation

    @classmethod
    def from_adapter(
        cls,
        adapter: GitAuthorityAdapter,
        session: GitRollbackSessionState,
        backup: Path,
    ) -> GitBackupObservation:
        """Verify the backup through the concrete adapter before creating evidence."""
        if not isinstance(adapter, GitAuthorityAdapter):
            raise GitAuthorityError("Git backup observation requires a concrete adapter")
        if not isinstance(backup, Path):
            raise GitAuthorityError("Git backup observation artifact path is invalid")
        result = adapter.verify_backup_artifact(backup)
        return cls._from_verified(session, result)


@dataclass(frozen=True)
class GitRollbackArtifactBinding:
    """Immutable Git backup path captured beneath the bound artifact root."""

    artifact_root: Path
    git_backup_root: Path

    @classmethod
    def bind(cls, context: Mapping[str, object]) -> GitRollbackArtifactBinding:
        root = context.get("artifact_root")
        backup = context.get("git_backup_root")
        if not isinstance(root, str) or not isinstance(backup, str):
            raise GitAuthorityError("Git rollback artifact binding is incomplete")
        root_path = Path(root).resolve()
        backup_path = Path(backup).resolve()
        try:
            backup_path.relative_to(root_path)
        except ValueError as error:
            raise GitAuthorityError(
                "Git rollback artifact path is outside artifact root"
            ) from error
        return cls(root_path, backup_path)


_SUPPORTED_PHASES = frozenset(
    {
        "discover",
        "preflight",
        "quiesce",
        "backup",
        "stage",
        "commit",
        "validate",
        "reopen",
        "rollback",
    }
)


class GitAuthorityAdapter:
    """Read-only Git evidence adapter; execute remains permanently disabled."""

    requires_bound_rollback = True
    bound_rollback_kind = "git"

    def __init__(
        self,
        repository: Path,
        *,
        repository_identity: tuple[int, int, int, int] | None = None,
    ) -> None:
        resolved = repository.resolve()
        if not resolved.is_dir():
            raise GitAuthorityError("Git authority repository is unavailable")
        self._repository = resolved
        git_directory = resolved / ".git"
        self._repository_identity: tuple[int, int, int, int] | None
        if repository_identity is not None:
            self._repository_identity = repository_identity
        else:
            try:
                root_status = resolved.stat()
                git_status = git_directory.stat()
            except OSError:
                self._repository_identity = None
            else:
                self._repository_identity = (
                    root_status.st_dev,
                    root_status.st_ino,
                    git_status.st_dev,
                    git_status.st_ino,
                )

    def lifecycle_session(self) -> LifecycleSession:
        """Return an opaque session bound to this adapter's repository."""
        return _issue(self, self._repository)

    def create_backup_bound(self, destination: Path, *, quiesced: bool) -> Path:
        """Create a Git backup using this adapter's owned lifecycle session."""
        from tools.git_backup import create_backup

        return create_backup(
            self._repository,
            destination,
            quiesced=quiesced,
            session=self.lifecycle_session(),
        )

    def restore_backup_bound(self, backup: Path, destination: Path) -> None:
        """Restore using this adapter's owned lifecycle session."""
        from tools.git_backup import restore_backup

        restore_backup(backup, destination, session=_issue(self, backup))

    def restore_authority_bound(
        self, backup: Path, *, expected_branch: str, expected_head: str
    ) -> dict[str, object]:
        """Restore this clean branch to the verified backup commit.

        This is an internal rollback effect.  It requires the caller to bind
        the current branch/head identity and never participates in public
        command dispatch.  The backup is verified before the branch reset;
        any failure after that point is intentionally surfaced as ambiguous by
        the durable mutation wrapper.
        """
        if not isinstance(backup, Path) or not expected_branch or not expected_head:
            raise GitAuthorityError("Git rollback identity is incomplete")
        self._check_repository_identity()
        status = self._git("status", "--porcelain=v1", "--untracked-files=all")
        branch = self._git("symbolic-ref", "--short", "-q", "HEAD")
        head = self._git("rev-parse", "--verify", "HEAD")
        if status or branch != expected_branch or head != expected_head:
            raise GitAuthorityError("Git rollback authority identity is stale or dirty")
        verified = self.verify_backup_artifact(backup)
        commit = verified.get("commit")
        if verified.get("verified") is not True or not isinstance(commit, str):
            raise GitAuthorityError("Git rollback backup verification is incomplete")
        self._check_repository_identity()
        rollback_ref = f"refs/agent-workflow/rollback/{commit}"
        self._git("fetch", str(backup / "authority.bundle"), f"{commit}:{rollback_ref}")
        self._git("reset", "--hard", commit)
        if (
            self._git("symbolic-ref", "--short", "-q", "HEAD") != expected_branch
            or self._git("rev-parse", "--verify", "HEAD") != commit
            or self._git("status", "--porcelain=v1", "--untracked-files=all")
        ):
            raise GitAuthorityError("Git rollback postcondition is invalid")
        return {
            "backend": "git",
            "target": "rollback",
            "rollback_commit": commit,
            "verified": True,
            "backend_identity_verified": True,
            "mutates_authority": True,
        }

    def _check_repository_identity(self) -> None:
        try:
            root = self._repository.stat()
            git = (self._repository / ".git").stat()
            current = (root.st_dev, root.st_ino, git.st_dev, git.st_ino)
        except OSError as error:
            raise GitAuthorityError("Git authority repository identity changed") from error
        if self._repository_identity is None or current != self._repository_identity:
            raise GitAuthorityError("Git authority repository identity changed")

    def bind_commit_capability(
        self,
        admission: Any,
        *,
        admission_reread: Any,
        expected_branch: str,
        expected_head: str,
        runner: Any = subprocess.run,
    ) -> Any:
        """Bind the isolated Git effect seam without enabling public dispatch.

        The returned capability still requires a caller-owned admission and
        remains outside ``execute`` and the upgrade command dispatcher.  This
        factory makes the concrete adapter-to-effect binding explicit while
        preserving the separate refinement gate.
        """
        from tools.git_authority_mutation import GitCommitCapability, GitMutationError

        try:
            return GitCommitCapability(
                self._repository,
                admission=admission,
                admission_reread=admission_reread,
                expected_branch=expected_branch,
                expected_head=expected_head,
                runner=runner,
            )
        except GitMutationError as error:
            raise GitAuthorityError("Git commit capability binding was rejected") from error
        except BaseException as error:
            raise GitAuthorityError("Git commit capability binding was rejected") from error

    def commit_bound(
        self,
        admission: Any,
        message: str,
        *,
        admission_reread: Any,
        expected_branch: str,
        expected_head: str,
        runner: Any = subprocess.run,
    ) -> Any:
        """Execute one explicitly bound Git effect outside public dispatch.

        This is an isolated capability entry point for the mutation campaign.
        It does not accept a phase context, caller command, path, or handler,
        and it is deliberately not used by ``execute`` or the upgrade CLI.
        """
        capability = self.bind_commit_capability(
            admission,
            admission_reread=admission_reread,
            expected_branch=expected_branch,
            expected_head=expected_head,
            runner=runner,
        )
        try:
            return capability.commit(message)
        except GitAuthorityError:
            raise
        except BaseException as error:
            raise GitAuthorityError("bound Git authority effect failed") from error

    def bind_durable_commit_capability(
        self,
        admission: Any,
        journal: Any,
        *,
        session_revision: int,
        admission_reread: Any,
        expected_branch: str,
        expected_head: str,
        runner: Any = subprocess.run,
    ) -> Any:
        """Bind Git's isolated effect to the durable journal seam."""
        from tools.authority_mutation import AuthorityMutationError, DurableBoundBackendMutation

        capability = self.bind_commit_capability(
            admission,
            admission_reread=admission_reread,
            expected_branch=expected_branch,
            expected_head=expected_head,
            runner=runner,
        )
        try:
            return DurableBoundBackendMutation(
                admission,
                journal,
                session_revision=session_revision,
                backend_effect=lambda argument: (
                    capability.stage_and_commit(argument)
                    if isinstance(argument, Mapping)
                    else capability.commit(argument)
                ),
            )
        except AuthorityMutationError as error:
            raise GitAuthorityError("Git durable commit capability binding was rejected") from error
        except BaseException as error:
            raise GitAuthorityError("Git durable commit capability binding was rejected") from error

    def bind_durable_rollback_capability(  # pragma: no cover - isolated backend seam
        self,
        admission: Any,
        journal: Any,
        *,
        session_revision: int,
        rollback_effect: Any,
    ) -> Any:
        """Bind one backend-owned rollback effect to the durable fence.

        This isolated seam is not connected to the public rollback command.
        The effect is supplied by the backend-specific rollback campaign and
        is fenced by the same durable journal before it can run.
        """
        from tools.authority_mutation import AuthorityMutationError, DurableBoundBackendMutation

        if getattr(admission, "target", None) != "rollback" or not callable(rollback_effect):
            raise GitAuthorityError("Git durable rollback capability binding was rejected")
        try:
            return DurableBoundBackendMutation(
                admission,
                journal,
                session_revision=session_revision,
                backend_effect=rollback_effect,
            )
        except AuthorityMutationError as error:
            raise GitAuthorityError(
                "Git durable rollback capability binding was rejected"
            ) from error

    @staticmethod
    def observe_backup_identity(
        backup: Path,
        manifest: Path,
        *,
        control_store_identity: str,
        control_store_revision: int,
    ) -> BackupObservation:
        """Read backup artifacts and CAS identity without authorizing restore."""
        return BackupObservation.from_artifacts(
            backup,
            manifest,
            control_store_identity=control_store_identity,
            control_store_revision=control_store_revision,
        )

    @staticmethod
    def verify_backup_artifact(backup: Path) -> dict[str, object]:
        """Run the complete read-only Git backup verifier."""
        from tools.git_backup import verify_backup

        return verify_backup(backup)

    def execute_generated_backup(  # noqa: C901
        self, operation: Mapping[str, object], context: Mapping[str, object]
    ) -> dict[str, object]:
        """Execute only the generated Git backup operation.

        This creates and verifies an artifact without replacing the repository,
        selector, branch, or runtime. All other generated opcodes remain
        rejected by this adapter and by the upgrade engine.
        """
        operation_id, inputs = self._validate_generated_backup_operation(operation)
        validated = self._context(context)
        if validated.get("target") != "new":
            raise GitAuthorityError("generated Git backup requires the forward target")
        for field, expected in (
            ("selector_ref", inputs["selector_ref"]),
            ("state_revision", inputs["expected_state_revision"]),
            ("durable_barrier_id", inputs["barrier_id"]),
            ("fencing_token", inputs["fencing_token"]),
        ):
            if validated.get(field) != expected:
                raise GitAuthorityError("generated Git backup identity is stale or foreign")
        destination = validated.get("destination")
        artifact_root = validated.get("artifact_root")
        if not isinstance(destination, str) or not isinstance(artifact_root, str):
            raise GitAuthorityError("generated Git backup artifact binding is invalid")
        destination_path = Path(destination).resolve()
        root_path = Path(artifact_root).resolve()
        try:
            destination_path.relative_to(root_path)
        except ValueError as error:
            raise GitAuthorityError(
                "generated Git backup destination escapes artifact root"
            ) from error
        before = self.snapshot("backup", validated)
        if before.get("git_clean") is not True:
            raise GitAuthorityError("Git authority is not clean before backup")
        try:
            self.create_backup_bound(destination_path, quiesced=True)
            verification = self.verify_backup_artifact(destination_path)
            if verification.get("verified") is not True or verification.get("commit") != before.get(
                "git_head"
            ):
                raise GitAuthorityError("Git backup verification is incomplete")
            with tempfile.TemporaryDirectory(dir=root_path) as restore_root:
                self.restore_backup_bound(destination_path, Path(restore_root) / "roundtrip")
            after = self.snapshot("backup", validated)
        except GitAuthorityError:
            raise
        except Exception as error:
            raise GitAuthorityError("generated Git backup failed") from error
        for field in ("git_head", "git_branch", "git_clean"):
            if after.get(field) != before.get(field):
                raise GitAuthorityError("Git authority identity changed during backup")
        return {
            "operation_id": operation_id,
            "opcode": "backend.backup",
            "outcome": "completed",
            "backend": "git",
            "backup_verified": True,
            "restore_roundtrip_verified": True,
            "backend_identity_verified": True,
            "mutates_authority": False,
            "git_head": before["git_head"],
            "git_branch": before["git_branch"],
            "git_clean": True,
            "fencing_token": validated["fencing_token"],
        }

    @staticmethod
    def _validate_generated_backup_operation(  # noqa: C901
        operation: Mapping[str, object],
    ) -> tuple[str, Mapping[str, object]]:
        required = {
            "operation_id",
            "opcode",
            "inputs",
            "timeout_seconds",
            "resources",
            "preconditions",
            "postconditions",
            "evidence",
            "durable_record",
        }
        if not isinstance(operation, Mapping) or set(operation) != required:
            raise GitAuthorityError("generated operation fields are incomplete or unknown")
        if operation.get("opcode") != "backend.backup" or operation.get("timeout_seconds") != 300:
            raise GitAuthorityError("generated Git operation is unsupported or invalid")
        if operation.get("resources") != ["maintenance-barrier", "durable-operation-record"]:
            raise GitAuthorityError("generated operation resources are invalid")
        if operation.get("preconditions") != ["previous-phase-complete"]:
            raise GitAuthorityError("generated operation preconditions are invalid")
        if operation.get("postconditions") != ["backup-contract-satisfied"]:
            raise GitAuthorityError("generated operation postconditions are invalid")
        if operation.get("evidence") != ["durable-operation-record"]:
            raise GitAuthorityError("generated operation evidence is invalid")
        if operation.get("durable_record") != "operation-id-and-outcome":
            raise GitAuthorityError("generated operation durability contract is invalid")
        operation_id = operation.get("operation_id")
        inputs = operation.get("inputs")
        if not isinstance(operation_id, str) or not operation_id:
            raise GitAuthorityError("generated operation identity is invalid")
        expected_inputs = {
            "backend",
            "selector_ref",
            "expected_state_revision",
            "barrier_id",
            "fencing_token",
            "backup_operation_id",
        }
        if not isinstance(inputs, Mapping) or set(inputs) != expected_inputs:
            raise GitAuthorityError("generated Git operation binding is invalid")
        if inputs.get("backend") != "git" or inputs.get("backup_operation_id") != operation_id:
            raise GitAuthorityError("generated Git operation identity is invalid")
        if (
            type(inputs.get("expected_state_revision")) is not int
            or inputs["expected_state_revision"] < 1
        ):
            raise GitAuthorityError("generated Git operation revision is invalid")
        return operation_id, inputs

    def _git(self, *arguments: str) -> str:
        try:
            result = subprocess.run(
                ["git", "-C", str(self._repository), *arguments],
                check=False,
                capture_output=True,
                text=True,
                timeout=10,
            )
        except (OSError, subprocess.TimeoutExpired) as error:
            raise GitAuthorityError("Git authority observation failed") from error
        if result.returncode != 0:
            raise GitAuthorityError("Git authority observation was rejected")
        return result.stdout.strip()

    @staticmethod
    def _context(context: Mapping[str, object]) -> dict[str, object]:
        required = {
            "schema_version",
            "backend",
            "project_id",
            "operation_id",
            "state_revision",
            "authority_revision",
            "fencing_token",
            "fencing_owner",
            "durable_barrier_id",
            "artifact_root",
            "source",
            "destination",
            "manifest",
            "selector_ref",
            "barrier_identity_digest",
            "target",
            "envelope_digest",
        }
        if set(context) != required or context.get("backend") != "git":
            raise GitAuthorityError("Git authority context is incomplete or mismatched")
        schema_version = context.get("schema_version")
        if type(schema_version) is not int or schema_version < 1:
            raise GitAuthorityError("Git authority context types are invalid")
        state_revision = context.get("state_revision")
        if type(state_revision) is not int or state_revision < 1:
            raise GitAuthorityError("Git authority context types are invalid")
        for field in required - {"schema_version", "state_revision"}:
            value = context.get(field)
            if type(value) is not str or not value:
                raise GitAuthorityError("Git authority context types are invalid")
        if context.get("target") not in {"new", "rollback"}:
            raise GitAuthorityError("Git authority context target is invalid")
        return dict(context)

    def snapshot(self, phase: str, context: Mapping[str, object]) -> dict[str, Any]:
        """Return identity-bound, read-only Git facts; never claim mutability evidence."""
        if type(phase) is not str or phase not in _SUPPORTED_PHASES:
            raise GitAuthorityError("Git authority phase is invalid")
        value = self._context(context)
        status = self._git("status", "--porcelain=v1", "--untracked-files=all")
        head = self._git("rev-parse", "--verify", "HEAD")
        branch = self._git("symbolic-ref", "--short", "-q", "HEAD")
        if not head or not branch or status:
            raise GitAuthorityError("Git authority is not clean and branch-bound")
        value.update(
            {
                "phase": phase,
                "backend_identity_verified": True,
                "git_head": head,
                "git_branch": branch,
                "git_clean": True,
                "mutates_authority": False,
            }
        )
        return value

    def snapshot_bound(  # noqa: C901
        self,
        phase: str,
        context: Mapping[str, object],
        scope: LockDomainScope,
        *,
        lease: AdmissionLease,
        admission_recheck: AdmissionRecheck,
        expected_branch: str,
        expected_head: str,
    ) -> dict[str, Any]:
        """Read Git identity only inside a trusted session scope.

        The scope performs the durable lease/revision reread immediately before
        observation.  This remains an evidence-only seam; no Git mutation is
        reachable from it.
        """
        from tools.scoped_backend_adapter import ScopedBackendAdapter

        if type(phase) is not str or phase not in _SUPPORTED_PHASES:
            raise GitAuthorityError("Git authority phase is invalid")
        if type(expected_branch) is not str or not expected_branch:
            raise GitAuthorityError("expected Git branch identity is invalid")
        if type(expected_head) is not str or not expected_head:
            raise GitAuthorityError("expected Git head identity is invalid")
        if not isinstance(lease, AdmissionLease):
            raise GitAuthorityError("trusted admission lease is required")
        if not isinstance(admission_recheck, AdmissionRecheck):
            raise GitAuthorityError("trusted admission recheck is required")
        if admission_recheck.lease != lease:
            raise GitAuthorityError("trusted admission recheck does not match lease")
        try:
            validated_context = self._context(context)
        except GitAuthorityError:
            raise
        except Exception as error:
            raise GitAuthorityError("Git authority context is invalid") from error
        if not isinstance(scope, LockDomainScope):
            raise GitAuthorityError("concrete lock-domain scope is required")
        try:
            root_status = self._repository.stat()
            git_status = (self._repository / ".git").stat()
            current_identity = (
                root_status.st_dev,
                root_status.st_ino,
                git_status.st_dev,
                git_status.st_ino,
            )
            captured_identity = getattr(self, "_repository_identity", None)
            if captured_identity is not None and current_identity != captured_identity:
                raise GitAuthorityError("Git authority repository identity changed")
            from tools.upgrade_authority import read_git_authority_snapshot

            snapshot = read_git_authority_snapshot(self._repository)
            if snapshot.branch != expected_branch or snapshot.head != expected_head:
                raise GitAuthorityError("Git authority identity changed")
        except GitAuthorityError:
            raise
        except Exception as error:
            raise GitAuthorityError("Git authority identity reread was rejected") from error
        expected_identity = {
            "project_id": lease.project_id,
            "authority_revision": lease.authority_revision,
            "fencing_token": lease.fencing_token,
            "fencing_owner": lease.fencing_owner,
            "durable_barrier_id": lease.durable_barrier_id,
            "state_revision": lease.revision,
        }
        if any(validated_context.get(name) != value for name, value in expected_identity.items()):
            raise GitAuthorityError("trusted session identity changed")
        try:
            value = ScopedBackendAdapter(self, scope).snapshot(
                phase, validated_context, scope_context=expected_identity
            )
        except GitAuthorityError:
            raise
        except (TypeError, RuntimeError) as error:
            raise GitAuthorityError("trusted Git session reread was rejected") from error
        expected_result_keys = set(validated_context) | {
            "phase",
            "backend_identity_verified",
            "git_head",
            "git_branch",
            "git_clean",
            "mutates_authority",
        }
        if set(value) != expected_result_keys:
            raise GitAuthorityError("Git authority backend result schema changed")
        for field, expected in validated_context.items():
            if value.get(field) != expected or type(value.get(field)) is not type(expected):
                raise GitAuthorityError("Git authority backend context identity changed")
        if type(value.get("phase")) is not str or value.get("phase") != phase:
            raise GitAuthorityError("Git authority backend phase changed")
        if (
            type(value.get("backend_identity_verified")) is not bool
            or value.get("backend_identity_verified") is not True
        ):
            raise GitAuthorityError("Git authority backend identity is unverified")
        if (
            type(value.get("mutates_authority")) is not bool
            or value.get("mutates_authority") is not False
        ):
            raise GitAuthorityError("Git authority backend is not read-only")
        if type(value.get("git_head")) is not str or not value.get("git_head"):
            raise GitAuthorityError("Git authority backend head is unverified")
        if type(value.get("git_branch")) is not str or not value.get("git_branch"):
            raise GitAuthorityError("Git authority backend branch is unverified")
        if type(value.get("git_clean")) is not bool or value.get("git_clean") is not True:
            raise GitAuthorityError("Git authority backend cleanliness is unverified")
        if value.get("git_branch") != expected_branch or value.get("git_head") != expected_head:
            raise GitAuthorityError("Git authority identity changed")
        return value

    def snapshot_bound_reread(
        self,
        context: Mapping[str, object],
        scope: LockDomainScope,
        *,
        lease: AdmissionLease,
        admission_recheck: AdmissionRecheck,
        expected_branch: str,
        expected_head: str,
    ) -> GitRollbackSessionState:
        """Return typed bound session identity without caller CAS fields."""
        value = self.snapshot_bound(
            "rollback",
            context,
            scope,
            lease=lease,
            admission_recheck=admission_recheck,
            expected_branch=expected_branch,
            expected_head=expected_head,
        )
        return GitRollbackSessionState(
            project_id=str(value["project_id"]),
            authority_revision=str(value["authority_revision"]),
            state_revision=int(value["state_revision"]),
            fencing_token=str(value["fencing_token"]),
            fencing_owner=str(value["fencing_owner"]),
            durable_barrier_id=str(value["durable_barrier_id"]),
            git_head=str(value["git_head"]),
            git_branch=str(value["git_branch"]),
        )

    def preflight_git(
        self,
        context: Mapping[str, object],
        scope: LockDomainScope,
        *,
        lease: AdmissionLease,
        admission_recheck: AdmissionRecheck,
        expected_branch: str,
        expected_head: str,
    ) -> GitBackupObservation:
        """Verify a bound Git backup as read-only rollback preflight evidence.

        Session identity is reread through the concrete scope before the
        verifier is invoked.  This method never calls ``execute`` or any
        restore/authorization path.
        """
        # ``git_backup_root`` is a Git-only artifact binding and is not part
        # of the shared authority context schema.
        context_without_artifact = dict(context)
        context_without_artifact.pop("git_backup_root", None)
        value = self._context(context_without_artifact)
        if value.get("target") != "rollback":
            raise GitAuthorityError("Git preflight requires rollback target")
        binding_context = dict(context)
        # The manifest is the canonical Git backup marker in the shared
        # PhaseContext; derive its containing backup directory rather than
        # accepting an independent caller-supplied CAS/path identity.
        binding_context.setdefault(
            "git_backup_root", str(Path(str(binding_context["manifest"])).parent)
        )
        binding = GitRollbackArtifactBinding.bind(binding_context)
        manifest = Path(str(value["manifest"])).resolve()
        canonical_manifest = (binding.git_backup_root / "manifest.json").resolve()
        if manifest != canonical_manifest or not manifest.is_file() or manifest.is_symlink():
            raise GitAuthorityError("Git rollback manifest is not bound to backup root")
        session = self.snapshot_bound_reread(
            value,
            scope,
            lease=lease,
            admission_recheck=admission_recheck,
            expected_branch=expected_branch,
            expected_head=expected_head,
        )
        try:
            return GitBackupObservation.from_adapter(self, session, binding.git_backup_root)
        except GitAuthorityError:
            raise
        except Exception as error:
            raise GitAuthorityError("Git rollback backup verification failed") from error

    def verify_rollback_context(self, context: Mapping[str, object]) -> dict[str, Any]:
        """Reread clean Git identity but do not authorize rollback."""
        if context.get("target") != "rollback":
            raise GitAuthorityError("Git rollback context target is invalid")
        value = self.snapshot("rollback", context)
        value["rollback_context_verified"] = False
        return value

    def verify_rollback_context_bound(
        self,
        context: Mapping[str, object],
        scope: LockDomainScope,
        *,
        lease: AdmissionLease,
        admission_recheck: AdmissionRecheck,
        expected_branch: str,
        expected_head: str,
    ) -> dict[str, Any]:
        """Reread rollback evidence only inside a trusted scope."""
        if context.get("target") != "rollback":
            raise GitAuthorityError("Git rollback context target is invalid")
        value = self.snapshot_bound(
            "rollback",
            context,
            scope,
            lease=lease,
            admission_recheck=admission_recheck,
            expected_branch=expected_branch,
            expected_head=expected_head,
        )
        value["rollback_context_verified"] = False
        return value

    def execute(self, _phase: str, _context: Mapping[str, object]) -> dict[str, Any]:
        raise GitAuthorityError("Git authority mutation adapter is not implemented")
