# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Uncalled concrete common/control/authority admission scope."""

from __future__ import annotations

from collections.abc import Callable, Iterator, Mapping
from contextlib import AbstractContextManager, contextmanager

from tools.admission_lease import LOCK_ORDER, AdmissionLease, AdmissionRecheck
from tools.handoffctl import CoordinatorLockGuard
from tools.lifecycle_trace import LifecycleObserver, _issue_event
from tools.lock_domain import LockDomainContract, LockDomainError, LockDomainIdentity
from tools.mutation_fence import MutationFence
from tools.rollback_control_store import (
    AuthorityEffectIntent,
    BarrierSessionContract,
    BarrierSessionState,
    ControlStoreError,
    RecoveryRejectedError,
    SQLiteBarrierSessionStore,
    SQLiteRollbackControlStore,
)
from tools.upgrade_identity import BarrierChildIdentity, BarrierSessionIdentity

LockDomainObserver = Callable[[str], None]


class LockDomainScope:
    """Caller-owned scope proving one durable session under one lock domain.

    This is deliberately not wired to CAS, selector publication, or upgrade
    execution.  It acquires common -> control -> authority, rereads the
    durable session while control is held, and then validates the lease.
    """

    def __init__(
        self,
        identity: LockDomainIdentity,
        session_store: SQLiteBarrierSessionStore,
        authority_fence: MutationFence,
        lease: AdmissionLease,
        recheck: AdmissionRecheck,
        session_identity: BarrierSessionIdentity,
        common_lock: Callable[[], AbstractContextManager[CoordinatorLockGuard]],
        session_revision: int | None = None,
        observer: LifecycleObserver | None = None,
        lock_observer: LockDomainObserver | None = None,
    ) -> None:
        self._identity = identity
        self._session_store = session_store
        self._authority_fence = authority_fence
        self._lease = lease
        self._recheck = recheck
        self._session_identity = session_identity
        self._common_lock = common_lock
        # Lease revision names the identity fence; session_revision names the
        # durable row CAS revision and can diverge after reconciliation.
        self._session_revision = lease.revision if session_revision is None else session_revision
        self._observer = observer
        self._lock_observer = lock_observer
        self._event_token = object()

    @classmethod
    def bind(
        cls,
        session_store: SQLiteBarrierSessionStore,
        authority_fence: MutationFence,
        lease: AdmissionLease,
        recheck: AdmissionRecheck,
        common_lock: Callable[[], AbstractContextManager[CoordinatorLockGuard]],
        observer: LifecycleObserver | None = None,
        lock_observer: LockDomainObserver | None = None,
    ) -> LockDomainScope:
        """Bind a caller-owned scope to canonical descriptors only.

        ``hold`` performs the immediate durable-session and lease recheck.
        This seam is intentionally not connected to mutation or dispatch.
        """
        if not isinstance(session_store, SQLiteBarrierSessionStore):
            raise LockDomainError("session store is invalid")
        if not isinstance(authority_fence, MutationFence):
            raise LockDomainError("authority fence is invalid")
        if not isinstance(lease, AdmissionLease):
            raise LockDomainError("admission lease is invalid")
        if not isinstance(recheck, AdmissionRecheck) or recheck.lease != lease:
            raise LockDomainError("admission recheck is invalid")
        with common_lock() as common_guard:
            identity = LockDomainContract.capture(common_guard, session_store, authority_fence)
            with session_store.lock_owned_by_caller(common_guard):
                state = session_store.snapshot_owned_by_caller()
            identity.assert_session_binding(state, lease, session_revision=state.revision)
        return cls(
            identity,
            session_store,
            authority_fence,
            lease,
            recheck,
            state.identity,
            common_lock,
            state.revision,
            observer,
            lock_observer,
        )

    def assert_ordered(self) -> None:
        if LOCK_ORDER != ("common", "control", "authority"):
            raise RuntimeError("admission lock order is invalid")
        if not isinstance(self._recheck, AdmissionRecheck) or self._recheck.lease != self._lease:
            raise LockDomainError("admission recheck does not match lease")
        if not isinstance(self._session_identity, BarrierSessionIdentity):
            raise LockDomainError("durable session identity is invalid")

    def assert_context(self, context: Mapping[str, object]) -> None:
        """Reject engine context whose immutable lease identity has drifted."""
        if not isinstance(context, Mapping):
            raise LockDomainError("engine context must be a mapping")
        required = {
            "project_id": self._lease.project_id,
            "authority_revision": self._lease.authority_revision,
            "fencing_token": self._lease.fencing_token,
            "fencing_owner": self._lease.fencing_owner,
            "durable_barrier_id": self._lease.durable_barrier_id,
            "state_revision": self._lease.revision,
        }
        try:
            context_keys = set(context)
        except Exception as error:
            raise LockDomainError("engine context mapping is invalid") from error
        if context_keys - set(required):
            raise LockDomainError("engine context schema contains unknown keys")
        try:
            values_match = any(
                context.get(key) != value or type(context.get(key)) is not type(value)
                for key, value in required.items()
            )
        except Exception as error:
            raise LockDomainError("engine context mapping values are invalid") from error
        if values_match:
            raise LockDomainError("engine context does not match admission lease")

    @contextmanager
    def validated_hold(self, context: Mapping[str, object]) -> Iterator[object]:
        """Validate caller context before acquiring the canonical scope.

        This is a rejection-only boundary for future adapters. It performs no
        CAS, selector publication, upgrade, apply, or rollback operation.
        """
        self.assert_context(context)
        with self.hold():
            yield object()

    @contextmanager
    def hold(self) -> Iterator[object]:
        """Acquire and prove the full scope, releasing every lock on failure."""
        with self._hold_with_guard():
            yield object()

    @contextmanager
    def _hold_with_guard(
        self, allowed_session_statuses: tuple[str, ...] = ("held",)
    ) -> Iterator[CoordinatorLockGuard]:
        """Hold the scope and retain the common guard for typed write adapters."""
        self.assert_ordered()
        with self._common_lock() as common_guard:
            if not isinstance(common_guard, CoordinatorLockGuard):
                raise RuntimeError("common lock capability is invalid")
            self._observe_lock("AcquireCommon")
            self._identity.assert_current(common_guard, self._session_store, self._authority_fence)
            try:
                with self._session_store.lock_owned_by_caller(common_guard):
                    self._observe_lock("AcquireControl")
                    try:
                        self._recheck_session(common_guard, allowed_session_statuses)
                        with self._authority_fence.locked():
                            self._observe_lock("AcquireAuthority")
                            try:
                                self._identity.assert_current(
                                    common_guard, self._session_store, self._authority_fence
                                )
                                self._recheck_session(common_guard, allowed_session_statuses)
                                yield common_guard
                            finally:
                                self._observe_lock("ReleaseAuthority")
                    finally:
                        self._observe_lock("ReleaseControl")
            finally:
                self._observe_lock("ReleaseCommon")

    def _observe_lock(self, action: str) -> None:
        if self._lock_observer is not None:
            self._lock_observer(action)

    def _recheck_session(
        self,
        common_guard: CoordinatorLockGuard,
        allowed_session_statuses: tuple[str, ...] = ("held",),
    ) -> None:
        """Reread trusted session evidence while the caller owns control locks."""
        observed = self._session_store.snapshot_owned_by_caller()
        if observed.status not in allowed_session_statuses:
            message = (
                "durable session is not held"
                if allowed_session_statuses == ("held",)
                else "durable session is not in an admissible status"
            )
            raise LockDomainError(message)
        if (
            observed.identity != self._session_identity
            or observed.revision != self._session_revision
        ):
            raise LockDomainError("durable session and lease do not match")
        try:
            state = self._session_store.recheck_held_locked(
                common_guard,
                self._session_identity,
                self._session_revision,
                allowed_session_statuses,
            )
        except ControlStoreError as error:
            raise LockDomainError(f"durable session recheck failed: {error}") from error
        if state.identity != self._session_identity or state.revision != self._session_revision:
            raise LockDomainError("durable session and lease do not match")
        self._identity.assert_session_binding(
            state,
            self._lease,
            session_revision=self._session_revision,
            allowed_statuses=allowed_session_statuses,
        )
        if self._observer is not None:
            self._observer(
                _issue_event(
                    self._event_token,
                    "scope.reread",
                    state.revision,
                    self._lease.fencing_owner,
                    "authority",
                    self._lease.project_id,
                    state.identity.identity_digest,
                    self._lease.fencing_token,
                )
            )


class SQLiteCoordinationWriteAdapter:
    """Typed control/session CAS seam under one proven lock-domain scope.

    This adapter deliberately exposes no store, connection, or callback.  It
    is a coordination boundary only; it does not authorize upgrade phases or
    public authority mutation.
    """

    __slots__ = ("_control", "_scope", "_session")

    def __init__(
        self,
        scope: LockDomainScope,
        control: SQLiteRollbackControlStore,
        session: SQLiteBarrierSessionStore,
    ) -> None:
        if not isinstance(scope, LockDomainScope):
            raise TypeError("concrete lock-domain scope is required")
        if not isinstance(control, SQLiteRollbackControlStore):
            raise TypeError("SQLite rollback control store is required")
        if not isinstance(session, SQLiteBarrierSessionStore):
            raise TypeError("SQLite barrier session store is required")
        if session._control is not control:
            raise ValueError("control/session store binding does not match")
        if scope._session_store is not session:
            raise ValueError("scope/session store binding does not match")
        self._scope = scope
        self._control = control
        self._session = session

    def control_cas(
        self, expected_revision: int, record: Mapping[str, object]
    ) -> dict[str, object]:
        """CAS one control barrier while common/control/authority are held."""
        with self._scope._hold_with_guard() as common_guard:
            self._assert_control_binding(record)
            return self._control.cas_locked(common_guard, expected_revision, record)

    def control_begin_release(self, operation_id: str) -> dict[str, object]:
        """Move one held control barrier to releasing under the full scope."""
        with self._scope._hold_with_guard():
            self._assert_control_operation(operation_id)
            return self._control._begin_release_locked(operation_id)

    def control_complete_release(
        self, operation_id: str, evidence: Mapping[str, object]
    ) -> dict[str, object]:
        """Complete a releasing control barrier with typed runtime evidence."""
        with self._scope._hold_with_guard(("held", "releasing")):
            self._assert_control_operation(operation_id)
            current = self._control._snapshot_locked(operation_id)
            authorization = self._control._authorize_release_locked(current, evidence)
            return self._control._complete_release_locked(operation_id, authorization)

    def control_with_barrier(
        self,
        expected_revision: int,
        record: Mapping[str, object],
        authority: Callable[[Mapping[str, object]], Mapping[str, object]],
    ) -> dict[str, object]:
        """Run one typed barrier callback under the full lock-domain scope."""
        with self._scope._hold_with_guard() as common_guard:
            self._assert_control_binding(record)
            return self._control.with_barrier_locked(
                common_guard, expected_revision, record, authority
            )

    def _assert_control_binding(self, record: Mapping[str, object]) -> None:
        current = self._session._snapshot_locked()
        if current is None:  # pragma: no cover - scope recheck rejects absence first
            raise ControlStoreError("barrier session is absent")
        identity = current.identity
        expected = {
            "project_id": identity.project_id,
            "state_revision": identity.state_revision,
            "authority_revision": identity.authority_revision_at_acquire,
            "fencing_token": identity.fencing_token,
            "fencing_owner": identity.fencing_owner,
            "durable_barrier_id": identity.durable_barrier_id,
        }
        if any(record.get(field) != value for field, value in expected.items()):
            raise ControlStoreError("control barrier identity is not bound to the session")
        child = self._bound_control_child(str(record.get("operation_id", "")))
        if record.get("target") != child.target:
            raise ControlStoreError("control barrier target is not bound to the session child")

    def _assert_control_operation(self, operation_id: str) -> None:
        current = self._control._snapshot_locked(operation_id)
        self._assert_control_binding(current)

    def _bound_control_child(self, operation_id: str) -> BarrierChildIdentity:
        current = self._session._snapshot_locked()
        if current is None:  # pragma: no cover - scope recheck rejects absence first
            raise ControlStoreError("barrier session is absent")
        children = (current.forward_child, current.rollback_child)
        child = next(
            (
                child
                for child in children
                if child is not None and child.operation_id == operation_id
            ),
            None,
        )
        if child is None:
            raise ControlStoreError("control operation is not bound to the session")
        return child

    def session_cas(
        self,
        expected_identity: BarrierSessionIdentity,
        expected_revision: int,
        state: BarrierSessionState,
    ) -> BarrierSessionState:
        """CAS one durable session while common/control/authority are held."""
        with self._scope._hold_with_guard() as common_guard:
            return self._session_cas_locked(
                common_guard, expected_identity, expected_revision, state
            )

    def _session_cas_locked(
        self,
        common_guard: CoordinatorLockGuard,
        expected_identity: BarrierSessionIdentity,
        expected_revision: int,
        state: BarrierSessionState,
    ) -> BarrierSessionState:
        result = self._session.cas_locked(common_guard, expected_identity, expected_revision, state)
        self._scope._session_revision = result.revision
        return result

    def session_bind_child(
        self,
        expected_identity: BarrierSessionIdentity,
        expected_revision: int,
        child: BarrierChildIdentity,
    ) -> BarrierSessionState:
        """Bind one typed forward/rollback child under the full scope."""
        with self._scope._hold_with_guard() as common_guard:
            current = self._session._snapshot_locked()
            if current is None:  # pragma: no cover - scope recheck rejects absence first
                raise ControlStoreError("barrier session is absent")
            if (
                current.identity != expected_identity
            ):  # pragma: no cover - scope recheck binds identity
                raise ControlStoreError("barrier session identity changed")
            contract = BarrierSessionContract(current.identity)
            contract._state = current
            state = contract.bind_child(expected_revision, child)
            return self._session_cas_locked(
                common_guard, expected_identity, expected_revision, state
            )

    def session_begin_reopen(
        self,
        expected_identity: BarrierSessionIdentity,
        expected_revision: int,
        target: str,
        verified_child_evidence: Mapping[str, object] | None = None,
    ) -> BarrierSessionState:
        """Begin a verified child reopen under the full scope."""
        with self._scope._hold_with_guard() as common_guard:
            current = self._session._snapshot_locked()
            if current is None:  # pragma: no cover - scope recheck rejects absence first
                raise ControlStoreError("barrier session is absent")
            if (
                current.identity != expected_identity
            ):  # pragma: no cover - scope recheck binds identity
                raise ControlStoreError("barrier session identity changed")
            contract = BarrierSessionContract(current.identity)
            contract._state = current
            state = contract.begin_reopen(expected_revision, target, verified_child_evidence)
            return self._session_cas_locked(
                common_guard, expected_identity, expected_revision, state
            )

    def session_complete_reopen(
        self,
        expected_identity: BarrierSessionIdentity,
        expected_revision: int,
        fresh_runtime_evidence: Mapping[str, object] | None = None,
    ) -> BarrierSessionState:
        """Complete a verified child reopen under the full releasing scope."""
        with self._scope._hold_with_guard(("releasing",)) as common_guard:
            current = self._session._snapshot_locked()
            if current is None or current.identity != expected_identity:
                raise ControlStoreError("barrier session identity changed")
            contract = BarrierSessionContract(current.identity)
            contract._state = current
            state = contract.complete_reopen(expected_revision, fresh_runtime_evidence)
            result = self._session._cas_locked(expected_revision, state)
            self._scope._session_revision = result.revision
            common_guard.assert_owned()
            return result

    def session_mark_ambiguous(
        self,
        expected_identity: BarrierSessionIdentity,
        expected_revision: int,
        cause_code: str,
    ) -> BarrierSessionState:
        """Durably fence a held/releasing session after an uncertain outcome."""
        with self._scope._hold_with_guard(("held", "releasing")) as common_guard:
            current = self._session._snapshot_locked()
            if current is None or current.identity != expected_identity:
                raise ControlStoreError("barrier session identity changed")
            contract = BarrierSessionContract(current.identity)
            contract._state = current
            state = contract.mark_ambiguous(expected_revision, cause_code)
            result = self._session._cas_locked(expected_revision, state)
            self._scope._session_revision = result.revision
            common_guard.assert_owned()
            return result

    def session_recover_unknown(self) -> BarrierSessionState | None:
        """Recover prepared session outcomes under the full lock-domain scope."""
        with self._scope._hold_with_guard(("held", "releasing")) as common_guard:
            result = self._session.recover_unknown_locked(common_guard)
            if result is not None:
                if result.identity != self._scope._session_identity:
                    raise ControlStoreError("recovered barrier session identity changed")
                self._scope._session_revision = result.revision
            common_guard.assert_owned()
            return result

    def session_prepare_authority_effect(
        self,
        expected_revision: int,
        operation_id: str,
        backend: str,
        target: str = "new",
        *,
        expected_fencing_token: str | None = None,
        expected_barrier_id: str | None = None,
        expected_artifact_identity: str | None = None,
        expected_manifest_identity: str | None = None,
        expected_selector_identity: str | None = None,
        expected_runtime_identity: str | None = None,
    ) -> AuthorityEffectIntent:
        """Prepare an effect intent under common/control/authority locks."""
        with self._scope._hold_with_guard() as common_guard:
            return self._session.prepare_authority_effect_locked(
                common_guard,
                expected_revision,
                operation_id,
                backend,
                target,
                expected_fencing_token=expected_fencing_token,
                expected_barrier_id=expected_barrier_id,
                expected_artifact_identity=expected_artifact_identity,
                expected_manifest_identity=expected_manifest_identity,
                expected_selector_identity=expected_selector_identity,
                expected_runtime_identity=expected_runtime_identity,
            )

    def session_finish_authority_effect(
        self,
        intent: AuthorityEffectIntent,
        outcome: str,
        receipt: object | None = None,
    ) -> BarrierSessionState:
        """Publish an effect outcome under common/control/authority locks."""
        with self._scope._hold_with_guard() as common_guard:
            result = self._session.finish_authority_effect_locked(
                common_guard, intent, outcome, receipt
            )
            self._scope._session_revision = result.revision
            return result


class SQLiteCoordinationRecoveryAdapter:
    """Fresh-fence recovery seam for an ambiguous durable session."""

    __slots__ = ("_authority_fence", "_common_lock", "_control", "_session")

    def __init__(
        self,
        session: SQLiteBarrierSessionStore,
        authority_fence: MutationFence,
        common_lock: Callable[[], AbstractContextManager[CoordinatorLockGuard]],
    ) -> None:
        if not isinstance(session, SQLiteBarrierSessionStore):
            raise TypeError("SQLite barrier session is required")
        if not isinstance(authority_fence, MutationFence):
            raise TypeError("authority fence is required")
        self._session = session
        self._control = session._control
        self._authority_fence = authority_fence
        self._common_lock = common_lock

    def reconcile_ambiguous(
        self,
        expected_identity: BarrierSessionIdentity,
        expected_revision: int,
        replacement: BarrierSessionState,
    ) -> BarrierSessionState:
        """Install a newer held session only under a fresh ordered fence."""
        if not isinstance(expected_identity, BarrierSessionIdentity):
            raise ControlStoreError("expected recovery identity is invalid")
        if not isinstance(replacement, BarrierSessionState):
            raise ControlStoreError("replacement recovery state is invalid")
        with self._common_lock() as common_guard:
            domain = LockDomainContract.capture(common_guard, self._session, self._authority_fence)
            with self._session.lock_owned_by_caller(common_guard):
                current = self._session.snapshot_owned_by_caller()
                if current.status != "ambiguous":
                    raise RecoveryRejectedError("only ambiguous sessions require reconciliation")
                if current.identity != expected_identity:
                    raise RecoveryRejectedError("ambiguous session identity changed")
                if current.revision != expected_revision:
                    raise RecoveryRejectedError("barrier session CAS conflict")
                with self._authority_fence.locked():
                    domain.assert_current(common_guard, self._session, self._authority_fence)
                    result = self._session.reconcile_ambiguous_locked(
                        common_guard, expected_revision, replacement
                    )
                    common_guard.assert_owned()
                    return result

    def create_session(self, identity: BarrierSessionIdentity) -> BarrierSessionState:
        """Create an initial held session under a fresh ordered fence."""
        if not isinstance(identity, BarrierSessionIdentity):
            raise ControlStoreError("session creation identity is invalid")
        with self._common_lock() as common_guard:
            domain = LockDomainContract.capture(common_guard, self._session, self._authority_fence)
            with self._session.lock_owned_by_caller(common_guard), self._authority_fence.locked():
                domain.assert_current(common_guard, self._session, self._authority_fence)
                result = self._session.create_locked(common_guard, identity)
                common_guard.assert_owned()
                return result

    @staticmethod
    def _assert_control_binding(session: BarrierSessionState, record: Mapping[str, object]) -> None:
        identity = session.identity
        expected = {
            "project_id": identity.project_id,
            "state_revision": identity.state_revision,
            "authority_revision": identity.authority_revision_at_acquire,
            "fencing_token": identity.fencing_token,
            "fencing_owner": identity.fencing_owner,
            "durable_barrier_id": identity.durable_barrier_id,
        }
        if any(record.get(field) != value for field, value in expected.items()):
            raise RecoveryRejectedError("control barrier identity is not bound to the session")
        children = (session.forward_child, session.rollback_child)
        child = next(
            (
                child
                for child in children
                if child is not None and child.operation_id == record["operation_id"]
            ),
            None,
        )
        if child is None or record.get("target") != child.target:
            raise RecoveryRejectedError("control barrier target is not bound to the session child")

    def reconcile_control_ambiguous(
        self,
        expected_identity: BarrierSessionIdentity,
        expected_revision: int,
        operation_id: str,
        replacement: Mapping[str, object],
    ) -> dict[str, object]:
        """Replace an ambiguous control barrier under a separate fresh fence."""
        if not isinstance(expected_identity, BarrierSessionIdentity):
            raise ControlStoreError("expected recovery identity is invalid")
        if type(expected_revision) is not int or expected_revision < 1:
            raise ControlStoreError("expected recovery revision is invalid")
        if not isinstance(operation_id, str) or not operation_id:
            raise ControlStoreError("recovery operation id is invalid")
        if not isinstance(replacement, Mapping):
            raise ControlStoreError("replacement recovery record is invalid")
        with self._common_lock() as common_guard:
            domain = LockDomainContract.capture(common_guard, self._session, self._authority_fence)
            with self._session.lock_owned_by_caller(common_guard):
                current = self._session.snapshot_owned_by_caller()
                if current.status != "ambiguous":
                    raise RecoveryRejectedError("only ambiguous sessions require reconciliation")
                if current.identity != expected_identity:
                    raise RecoveryRejectedError("ambiguous session identity changed")
                if current.revision != expected_revision:
                    raise RecoveryRejectedError("barrier session CAS conflict")
                previous = self._control._snapshot_locked(operation_id)
                self._assert_control_binding(current, previous)
                with self._authority_fence.locked():
                    domain.assert_current(common_guard, self._session, self._authority_fence)
                    result = self._control.reconcile_ambiguous_locked(
                        common_guard, operation_id, replacement
                    )
                    common_guard.assert_owned()
                    return result


def bind_sqlite_coordination_writer(
    scope: LockDomainScope,
    control: SQLiteRollbackControlStore,
    session: SQLiteBarrierSessionStore,
) -> SQLiteCoordinationWriteAdapter:
    """Issue the typed coordination CAS seam without exposing raw stores."""
    return SQLiteCoordinationWriteAdapter(scope, control, session)


def bind_sqlite_coordination_recovery(
    session: SQLiteBarrierSessionStore,
    authority_fence: MutationFence,
    common_lock: Callable[[], AbstractContextManager[CoordinatorLockGuard]],
) -> SQLiteCoordinationRecoveryAdapter:
    """Issue the fresh-fence recovery seam without exposing stores."""
    return SQLiteCoordinationRecoveryAdapter(session, authority_fence, common_lock)
