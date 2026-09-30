# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Construct the production live upgrade proof from canonical coordinator state."""

# mypy: disable-error-code="no-redef"

from __future__ import annotations

import hashlib
import json
from collections.abc import Callable
from contextlib import AbstractContextManager
from pathlib import Path
from typing import TYPE_CHECKING

if __package__:
    from .admission_lease import AdmissionLease, AdmissionRecheck
    from .lock_domain_scope import LockDomainScope
    from .mutation_fence import MutationFence
    from .rollback_control_store import SQLiteBarrierSessionStore, SQLiteRollbackControlStore
    from .upgrade_authority import (
        inspect_sqlite_release_authority,
        read_git_authority_snapshot,
        read_runtime_selector,
    )
    from .upgrade_binding import LiveUpgradeBinding, UpgradeBindingError, UpgradeRuntimeBinding

    if TYPE_CHECKING:
        from .handoffctl import CoordinatorLockGuard
else:  # pragma: no cover - direct script execution
    from admission_lease import AdmissionLease, AdmissionRecheck  # type: ignore[import-not-found]
    from lock_domain_scope import LockDomainScope  # type: ignore[import-not-found]
    from mutation_fence import MutationFence  # type: ignore[import-not-found]
    from rollback_control_store import (  # type: ignore[import-not-found]
        SQLiteBarrierSessionStore,
        SQLiteRollbackControlStore,
    )
    from upgrade_authority import (  # type: ignore[import-not-found]
        inspect_sqlite_release_authority,
        read_git_authority_snapshot,
        read_runtime_selector,
    )
    from upgrade_binding import (  # type: ignore[import-not-found]
        LiveUpgradeBinding,
        UpgradeBindingError,
        UpgradeRuntimeBinding,
    )

    if TYPE_CHECKING:
        from handoffctl import CoordinatorLockGuard  # type: ignore[import-not-found]


class ProductionBindingError(RuntimeError):
    """Canonical production binding could not be reconstructed safely."""


def git_authority_revision(repository: Path, project_id: str, runtime_selector: Path) -> str:
    """Derive one identity-bound revision from a clean Git release pair."""
    selector = read_runtime_selector(runtime_selector)
    observed = read_git_authority_snapshot(repository)
    payload = {
        "schema_version": 1,
        "kind": "agent-workflow-coordinator-git-authority-revision",
        "project_id": project_id,
        "repository": str(observed.repository),
        "git_directory_identity": observed.git_directory_identity,
        "branch": observed.branch,
        "head": observed.head,
        "requested_ref": observed.requested_ref,
        "requested_ref_head": observed.requested_ref_head,
        "clean": observed.clean,
        "active_release": str(selector["active_release"]),
        "previous_release": str(selector["previous_release"]),
    }
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def resolve_sqlite_live_binding(
    runtime: UpgradeRuntimeBinding,
    *,
    database: Path,
    control_database: Path,
    authority_marker: Path,
    authority_lifecycle: Path,
    authority_lock: Path,
    control_binding: Path,
    control_lock: Path,
    project_binding: Path,
    backend_config: Path,
    runtime_selector: Path,
    common_lock: Callable[[], AbstractContextManager[CoordinatorLockGuard]],
) -> LiveUpgradeBinding:
    """Reconstruct and admit one live SQLite binding from durable state."""
    if runtime.contract_backend != "sqlite":
        raise ProductionBindingError(
            "production live binding requires the canonical SQLite authority; "
            "Git authority revision reconstruction is not implemented"
        )
    try:
        if __package__:
            from .sqlite_authority_adapter import SQLiteAuthorityAdapter
        else:  # pragma: no cover - direct script execution
            from sqlite_authority_adapter import (  # type: ignore[import-not-found]
                SQLiteAuthorityAdapter,
            )
        binding = json.loads(project_binding.read_text(encoding="utf-8"))
        project_id = str(binding["project_id"])
        selector = read_runtime_selector(runtime_selector)
        active = str(selector["active_release"])
        previous = str(selector["previous_release"])

        def authority_revision() -> str:
            return inspect_sqlite_release_authority(
                database,
                project_binding,
                backend_config,
                runtime_selector,
                project_id,
                active,
                previous,
            ).authority_revision

        control = SQLiteRollbackControlStore(control_database, project_id, database)
        session_store = SQLiteBarrierSessionStore(control, authority_revision)
        state = session_store.snapshot()
        if state is None or state.status != "held" or state.rollback_child is None:
            raise ProductionBindingError("durable rollback barrier is not held")
        runtime.validate_live_session(state)
        identity = state.identity
        lease = AdmissionLease(
            project_id=identity.project_id,
            authority_revision=identity.authority_revision_at_acquire,
            fencing_token=identity.fencing_token,
            fencing_owner=identity.fencing_owner,
            durable_barrier_id=identity.durable_barrier_id,
            revision=identity.state_revision,
        )
        recheck = AdmissionRecheck(
            lease=lease,
            project_id=lease.project_id,
            authority_revision=lease.authority_revision,
            fencing_token=lease.fencing_token,
            fencing_owner=lease.fencing_owner,
            durable_barrier_id=lease.durable_barrier_id,
            revision=lease.revision,
        )
        fence = MutationFence(
            database,
            authority_marker,
            authority_lifecycle,
            authority_lock,
            control_database,
            control_binding,
            control_lock,
        )
        fence.verify_binding()
        fence.bind_session_identity(identity)
        scope = LockDomainScope.bind(session_store, fence, lease, recheck, common_lock)
        adapter = SQLiteAuthorityAdapter(database)
        return LiveUpgradeBinding.bind(runtime, state, scope, lease, recheck, adapter)
    except ProductionBindingError:
        raise
    except (KeyError, OSError, ValueError, UpgradeBindingError) as error:
        raise ProductionBindingError("canonical production live binding was rejected") from error


def resolve_git_live_binding(
    runtime: UpgradeRuntimeBinding,
    *,
    repository: Path,
    control_database: Path,
    authority_marker: Path,
    authority_lifecycle: Path,
    authority_lock: Path,
    control_binding: Path,
    control_lock: Path,
    project_binding: Path,
    runtime_selector: Path,
    common_lock: Callable[[], AbstractContextManager[CoordinatorLockGuard]],
) -> LiveUpgradeBinding:
    """Reconstruct and admit one live Git binding from durable state."""
    if runtime.contract_backend != "git":
        raise ProductionBindingError("production Git live binding requires a Git contract")
    try:
        from .git_authority_adapter import GitAuthorityAdapter
    except ImportError:  # pragma: no cover - direct script execution
        from git_authority_adapter import GitAuthorityAdapter  # type: ignore[import-not-found]

    try:
        binding = json.loads(project_binding.read_text(encoding="utf-8"))
        project_id = str(binding["project_id"])
        authority_path = repository.resolve() / ".git" / "HEAD"

        def authority_revision() -> str:
            return git_authority_revision(repository, project_id, runtime_selector)

        control = SQLiteRollbackControlStore(control_database, project_id, authority_path)
        session_store = SQLiteBarrierSessionStore(control, authority_revision)
        state = session_store.snapshot()
        if state is None or state.status != "held" or state.rollback_child is None:
            raise ProductionBindingError("durable rollback barrier is not held")
        runtime.validate_live_session(state)
        identity = state.identity
        lease = AdmissionLease(
            project_id=identity.project_id,
            authority_revision=identity.authority_revision_at_acquire,
            fencing_token=identity.fencing_token,
            fencing_owner=identity.fencing_owner,
            durable_barrier_id=identity.durable_barrier_id,
            revision=identity.state_revision,
        )
        recheck = AdmissionRecheck(
            lease=lease,
            project_id=lease.project_id,
            authority_revision=lease.authority_revision,
            fencing_token=lease.fencing_token,
            fencing_owner=lease.fencing_owner,
            durable_barrier_id=lease.durable_barrier_id,
            revision=lease.revision,
        )
        fence = MutationFence(
            authority_path,
            authority_marker,
            authority_lifecycle,
            authority_lock,
            control_database,
            control_binding,
            control_lock,
        )
        fence.verify_binding()
        fence.bind_session_identity(identity)
        scope = LockDomainScope.bind(session_store, fence, lease, recheck, common_lock)
        observed = read_git_authority_snapshot(repository)
        root_status = observed.repository.stat()
        git_status = (observed.repository / ".git").stat()
        repository_identity = (
            root_status.st_dev,
            root_status.st_ino,
            git_status.st_dev,
            git_status.st_ino,
        )
        adapter = GitAuthorityAdapter(repository, repository_identity=repository_identity)
        return LiveUpgradeBinding.bind(
            runtime,
            state,
            scope,
            lease,
            recheck,
            adapter,
            expected_git_repository=observed.repository,
        )
    except ProductionBindingError:
        raise
    except Exception as error:
        raise ProductionBindingError(
            "canonical Git production live binding was rejected"
        ) from error
