# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Read-only SQLite authority evidence for the future scoped adapter."""

from __future__ import annotations

import json
import os
import re
import sqlite3
import stat
import tempfile
from collections.abc import Callable, Iterator, Mapping
from contextlib import contextmanager, nullcontext, suppress
from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path
from typing import Any, Literal, TypeVar, cast

from tools.admission_lease import AdmissionLease, AdmissionRecheck
from tools.lifecycle_session import LifecycleSession, _issue
from tools.lock_domain_scope import LockDomainScope
from tools.rollback_control_store import BarrierSessionState, SQLiteBarrierSessionStore
from tools.rollback_evidence import BackupObservation
from tools.upgrade_engine import JournalSnapshot


class SQLiteAuthorityError(RuntimeError):
    """SQLite authority evidence is unavailable or mutation was requested."""


_EffectResult = TypeVar("_EffectResult")


@dataclass(frozen=True, slots=True)
class SQLiteLifecycleSnapshot:
    """Read-only paired durable control/session and journal snapshot."""

    control: BarrierSessionState
    journal: JournalSnapshot
    journal_identity: tuple[int, int, int, int]
    control_lock_identity: tuple[int, int, int, int]
    control_store_identity: tuple[int, int, int, int]


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


class SQLiteLifecycleExecutor:
    """Concrete adapter-owned backup/restore executor; no phase authorization."""

    def __init__(
        self,
        adapter: SQLiteAuthorityAdapter,
        session_store: SQLiteBarrierSessionStore | None = None,
        journal: Path | None = None,
    ) -> None:
        if session_store is not None and session_store.authority_path != adapter._authority:
            raise SQLiteAuthorityError("lifecycle session store is bound to a foreign authority")
        if session_store is not None and journal is None:
            raise SQLiteAuthorityError("lifecycle executor journal is required")
        self._adapter = adapter
        self._session_store = session_store
        self._journal = journal
        self._last_snapshot: SQLiteLifecycleSnapshot | None = None

    @classmethod
    def bind(
        cls,
        adapter: SQLiteAuthorityAdapter,
        session_store: SQLiteBarrierSessionStore,
        journal: Path,
    ) -> SQLiteLifecycleExecutor:
        """Bind the executor to concrete durable control and journal sources."""
        if session_store.authority_path != adapter._authority:
            raise SQLiteAuthorityError("lifecycle session store is bound to a foreign authority")
        return cls(adapter, session_store, journal.absolute())

    def snapshot(self) -> SQLiteLifecycleSnapshot:
        """Capture both durable sources under the control-store operation lock."""
        if self._session_store is None or self._journal is None:
            raise SQLiteAuthorityError("lifecycle executor is not bound to durable state")
        try:
            with self._session_store.operation_lock():
                return self._snapshot_locked()
        except SQLiteAuthorityError:
            raise
        except Exception as error:
            raise SQLiteAuthorityError("durable lifecycle snapshot failed") from error

    def _snapshot_locked(self) -> SQLiteLifecycleSnapshot:
        """Capture durable state while the caller already owns the operation lock."""
        if self._session_store is None or self._journal is None:
            raise SQLiteAuthorityError("lifecycle executor is not bound to durable state")
        control_store_identity = self._control_store_identity(
            self._session_store.control_store_path
        )
        self._adapter._check_identity()
        control = self._session_store.snapshot_owned_by_caller()
        if (
            self._control_store_identity(self._session_store.control_store_path)
            != control_store_identity
        ):
            raise SQLiteAuthorityError("lifecycle control store identity changed")
        journal_identity = self._journal_identity(self._journal)
        value = json.loads(self._journal.read_text(encoding="utf-8"))
        journal = JournalSnapshot.from_mapping(cast(Mapping[str, object], value))
        if self._journal_identity(self._journal) != journal_identity:
            raise SQLiteAuthorityError("lifecycle journal identity changed")
        self._adapter._check_identity()
        lock_identity = self._lock_identity(self._session_store.control_lock_path)
        snapshot = SQLiteLifecycleSnapshot(
            control, journal, journal_identity, lock_identity, control_store_identity
        )
        self._last_snapshot = snapshot
        return snapshot

    def _run_effect(self, operation: Callable[[], _EffectResult]) -> _EffectResult:
        """Run one bound operation with locked before/after durable rereads."""
        if self._session_store is None or self._journal is None:
            raise SQLiteAuthorityError("lifecycle executor is not bound to durable state")
        try:
            with self._session_store.operation_lock():
                before = self._snapshot_locked()
                try:
                    result = operation()
                except Exception as error:
                    try:
                        self._assert_snapshot_locked(before)
                    except SQLiteAuthorityError as state_error:
                        raise state_error from error
                    raise
                self._assert_snapshot_locked(before)
                return result
        except SQLiteAuthorityError:
            raise
        except Exception as error:
            raise SQLiteAuthorityError("lifecycle effect failed") from error

    def _assert_snapshot_locked(self, expected: SQLiteLifecycleSnapshot) -> None:
        current = self._snapshot_locked()
        if current != expected:
            raise SQLiteAuthorityError("durable lifecycle state changed")

    @staticmethod
    def _journal_identity(path: Path) -> tuple[int, int, int, int]:
        try:
            parent = path.parent.lstat()
            value = path.lstat()
        except OSError as error:
            raise SQLiteAuthorityError("lifecycle journal is unavailable") from error
        if not stat.S_ISDIR(parent.st_mode):
            raise SQLiteAuthorityError("lifecycle journal parent is not a directory")
        if not stat.S_ISREG(value.st_mode) or value.st_nlink != 1:
            raise SQLiteAuthorityError("lifecycle journal is not private and regular")
        return parent.st_dev, parent.st_ino, value.st_dev, value.st_ino

    @staticmethod
    def _lock_identity(path: Path) -> tuple[int, int, int, int]:
        try:
            parent = path.parent.lstat()
            value = path.lstat()
        except OSError as error:
            raise SQLiteAuthorityError("lifecycle control lock is unavailable") from error
        if not stat.S_ISDIR(parent.st_mode):
            raise SQLiteAuthorityError("lifecycle control lock parent is not a directory")
        if (
            not stat.S_ISREG(value.st_mode)
            or value.st_nlink != 1
            or value.st_uid != os.geteuid()
            or stat.S_IMODE(value.st_mode) != 0o600
        ):
            raise SQLiteAuthorityError("lifecycle control lock is not private and regular")
        return parent.st_dev, parent.st_ino, value.st_dev, value.st_ino

    @staticmethod
    def _control_store_identity(path: Path) -> tuple[int, int, int, int]:
        try:
            parent = path.parent.lstat()
            value = path.lstat()
        except OSError as error:
            raise SQLiteAuthorityError("lifecycle control store is unavailable") from error
        if not stat.S_ISDIR(parent.st_mode):
            raise SQLiteAuthorityError("lifecycle control store parent is not a directory")
        if not stat.S_ISREG(value.st_mode) or value.st_nlink != 1:
            raise SQLiteAuthorityError("lifecycle control store is not private and regular")
        return parent.st_dev, parent.st_ino, value.st_dev, value.st_ino

    def assert_snapshot_stable(self, expected: SQLiteLifecycleSnapshot) -> SQLiteLifecycleSnapshot:
        """Reread durable state and fail closed if it changed since ``expected``."""
        if expected is not self._last_snapshot:
            raise SQLiteAuthorityError("lifecycle snapshot belongs to a foreign executor")
        current = self.snapshot()
        if current != expected:
            raise SQLiteAuthorityError("durable lifecycle state changed")
        return current

    def backup(self, destination: Path, binding: dict[str, Any]) -> dict[str, Any]:
        return self._run_effect(lambda: self._adapter.backup_bound(destination, binding))

    def assert_selector_binding(
        self,
        selector_ref: str,
        expected_state_revision: int,
        barrier_id: str,
        fencing_token: str,
    ) -> SQLiteLifecycleSnapshot:
        """Return a stable held-session snapshot for selector publication.

        This is deliberately a read-only admission seam: selector mutation is
        still disabled until an adapter can perform the publication atomically.
        """
        snapshot = self.snapshot()
        self._check_selector_binding(
            snapshot, selector_ref, expected_state_revision, barrier_id, fencing_token
        )
        return snapshot

    @staticmethod
    def _check_selector_binding(
        snapshot: SQLiteLifecycleSnapshot,
        selector_ref: str,
        expected_state_revision: int,
        barrier_id: str,
        fencing_token: str,
    ) -> None:
        identity = snapshot.control.identity
        selector_path = Path(selector_ref) if isinstance(selector_ref, str) else None
        if (
            type(expected_state_revision) is not int
            or expected_state_revision < 1
            or snapshot.control.status != "held"
            or identity.state_revision != expected_state_revision
            or identity.durable_barrier_id != barrier_id
            or identity.fencing_token != fencing_token
            or selector_path is None
            or not selector_ref
            or selector_path.is_absolute()
            or ".." in selector_path.parts
        ):
            raise SQLiteAuthorityError("selector publication binding is invalid")

    @contextmanager
    def selector_visibility_scope(
        self,
        selector_ref: str,
        expected_state_revision: int,
        barrier_id: str,
        fencing_token: str,
        *,
        selector_root: Path,
    ) -> Iterator[SQLiteLifecycleSnapshot]:
        """Hold the barrier while a future selector publication is attempted.

        When ``selector_root`` is supplied, bind the relative selector name to
        an owner-only regular file before yielding.  This is admission only:
        the selector is not modified by this executor.
        """
        if self._session_store is None:
            raise SQLiteAuthorityError("selector publication executor is not bound")
        with self._session_store.operation_lock():
            snapshot = self._snapshot_locked()
            self._check_selector_binding(
                snapshot, selector_ref, expected_state_revision, barrier_id, fencing_token
            )
            self._resolve_selector_target(selector_root, selector_ref)
            selector_identity = self._selector_path_identity(selector_root, selector_ref)
            operation_error: BaseException | None = None
            try:
                yield snapshot
            except BaseException as error:
                operation_error = error
                raise
            finally:
                self._assert_snapshot_locked(snapshot)
                try:
                    current_identity = self._selector_path_identity(selector_root, selector_ref)
                except SQLiteAuthorityError as error:
                    if operation_error is None:
                        raise SQLiteAuthorityError("selector target identity changed") from error
                else:
                    if current_identity != selector_identity and operation_error is None:
                        raise SQLiteAuthorityError("selector target identity changed")

    @staticmethod
    def _resolve_selector_target(root: Path, selector_ref: str) -> Path:
        """Resolve an existing selector without following a filesystem alias."""
        selector = Path(selector_ref)
        if (
            not isinstance(root, Path)
            or not root.is_absolute()
            or len(selector.parts) != 1
            or selector.parts[0] in {"", "."}
        ):
            raise SQLiteAuthorityError("selector root must be absolute")
        try:
            component = Path(root.anchor)
            for part in root.parts[1:]:
                component /= part
                status = component.lstat()
                if stat.S_ISLNK(status.st_mode):
                    raise SQLiteAuthorityError("selector root contains a symlink")
            root_status = root.lstat()
            target = root / selector_ref
            target_status = target.lstat()
        except OSError as error:
            raise SQLiteAuthorityError("selector target is unavailable") from error
        if (
            not stat.S_ISDIR(root_status.st_mode)
            or root_status.st_uid != os.geteuid()
            or stat.S_IMODE(root_status.st_mode) != 0o700
            or not stat.S_ISREG(target_status.st_mode)
            or target_status.st_uid != os.geteuid()
            or target_status.st_nlink != 1
            or stat.S_IMODE(target_status.st_mode) != 0o600
        ):
            raise SQLiteAuthorityError("selector target is unsafe")
        return target

    @classmethod
    def _selector_path_identity(
        cls, root: Path, selector_ref: str
    ) -> tuple[tuple[tuple[int, int, int, int, int], ...], str]:
        """Capture identities for the root's ancestors, root, and selector."""
        cls._resolve_selector_target(root, selector_ref)
        paths = []
        component = Path(root.anchor)
        for part in root.parts[1:]:
            component /= part
            paths.append(component)
        paths.append(root / selector_ref)
        try:
            identities = tuple(
                (
                    status.st_dev,
                    status.st_ino,
                    status.st_uid,
                    stat.S_IMODE(status.st_mode),
                    status.st_nlink,
                )
                for path in paths
                for status in (path.lstat(),)
            )
            target = paths[-1]
            expected = identities[-1]
            descriptor = os.open(target, os.O_RDONLY | os.O_NOFOLLOW)
            try:
                opened = os.fstat(descriptor)
                opened_identity = (
                    opened.st_dev,
                    opened.st_ino,
                    opened.st_uid,
                    stat.S_IMODE(opened.st_mode),
                    opened.st_nlink,
                )
                if opened_identity != expected:
                    raise SQLiteAuthorityError("selector target identity changed")
                digest = sha256()
                total = 0
                while chunk := os.read(descriptor, 65536):
                    total += len(chunk)
                    if total > 16 * 1024 * 1024:
                        raise SQLiteAuthorityError("selector target is too large")
                    digest.update(chunk)
                final = os.fstat(descriptor)
                final_identity = (
                    final.st_dev,
                    final.st_ino,
                    final.st_uid,
                    stat.S_IMODE(final.st_mode),
                    final.st_nlink,
                )
                if final_identity != expected:
                    raise SQLiteAuthorityError("selector target identity changed")
            finally:
                os.close(descriptor)
            return identities, digest.hexdigest()
        except OSError as error:
            raise SQLiteAuthorityError("selector target identity unavailable") from error

    def reconcile_selector_publication(
        self,
        selector_ref: str,
        selector_root: Path,
        expected_state_revision: int,
        barrier_id: str,
        fencing_token: str,
        *,
        before_active_release: str,
        before_previous_release: str,
        after_active_release: str,
        after_previous_release: str,
    ) -> Literal["committed", "not-committed"]:
        """Reconcile an uncertain selector result under the held barrier.

        This only classifies the already-published selector as the exact old
        or new pair.  It never writes the selector or authorizes an upgrade.
        """
        from tools.upgrade_authority import read_runtime_selector

        releases = (
            before_active_release,
            before_previous_release,
            after_active_release,
            after_previous_release,
        )
        if not all(
            isinstance(value, str) and re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{0,127}", value)
            for value in releases
        ):
            raise SQLiteAuthorityError("selector release identity is invalid")
        if (before_active_release, before_previous_release) == (
            after_active_release,
            after_previous_release,
        ):
            raise SQLiteAuthorityError("selector release pairs must differ")

        with self.selector_visibility_scope(
            selector_ref,
            expected_state_revision,
            barrier_id,
            fencing_token,
            selector_root=selector_root,
        ):
            current = read_runtime_selector(selector_root / selector_ref)
            pair = (current["active_release"], current["previous_release"])
            if pair == (after_active_release, after_previous_release):
                return "committed"
            if pair == (before_active_release, before_previous_release):
                return "not-committed"
            raise SQLiteAuthorityError("selector reconciliation found unknown release identity")

    def execute_generated_operation(
        self,
        operation: Mapping[str, object],
        destination: Path,
        binding: dict[str, Any],
    ) -> dict[str, Any]:
        """Execute only the generated SQLite backup opcode under a held session.

        This is the first production operation dispatch seam.  It does not
        authorize upgrades or selector replacement; unsupported opcodes remain
        fail-closed until their corresponding lifecycle contracts exist.
        """
        operation_id, inputs = self._validate_generated_operation(operation)
        session_store = self._session_store
        if session_store is None:
            raise SQLiteAuthorityError("generated backup executor is not bound")
        snapshot = self.snapshot()
        if snapshot.control.status != "held":
            raise SQLiteAuthorityError("generated backup requires a held durable barrier")
        self._validate_generated_journal(snapshot, operation_id, inputs)
        result: dict[str, Any]
        try:
            with session_store.operation_lock():
                if self._snapshot_locked() != snapshot:
                    raise SQLiteAuthorityError("generated backup durable state changed")
                result = self._adapter.backup_bound(destination, binding)
                if "database_sha256" in result:
                    manifest = {
                        key: result[key]
                        for key in (
                            "schema_version",
                            "kind",
                            "database_sha256",
                            "integrity_check",
                            "foreign_key_check",
                            "binding_verified",
                            "wal_consistent",
                        )
                    }
                    with tempfile.TemporaryDirectory(dir=destination.parent) as restore_root:
                        self._adapter.restore_bound(
                            destination,
                            Path(restore_root) / "roundtrip.sqlite",
                            manifest,
                            binding,
                        )
                    result = {
                        **result,
                        "backend": "sqlite",
                        "backup_verified": True,
                        "restore_roundtrip_verified": True,
                        "backend_identity_verified": True,
                        "mutates_authority": False,
                        "fencing_token": inputs["fencing_token"],
                    }
                self._publish_generated_outcome(snapshot, operation_id, result)
        except SQLiteAuthorityError:
            raise
        except Exception as error:
            raise SQLiteAuthorityError("generated SQLite backup failed") from error
        return {
            "operation_id": operation_id,
            "opcode": "backend.backup",
            "outcome": "completed",
            **result,
        }

    @staticmethod
    def _validate_generated_operation(
        operation: Mapping[str, object],
    ) -> tuple[str, Mapping[str, object]]:
        if not isinstance(operation, Mapping):
            raise SQLiteAuthorityError("generated operation must be an object")
        if operation.get("opcode") != "backend.backup":
            raise SQLiteAuthorityError("generated SQLite operation is unsupported")
        SQLiteLifecycleExecutor._validate_generated_operation_fields(operation)
        operation_id = operation.get("operation_id")
        inputs = operation.get("inputs")
        if not isinstance(operation_id, str) or not operation_id:
            raise SQLiteAuthorityError("generated operation identity is invalid")
        required = {
            "backend",
            "selector_ref",
            "expected_state_revision",
            "barrier_id",
            "fencing_token",
            "backup_operation_id",
        }
        if not isinstance(inputs, Mapping) or set(inputs) != required:
            raise SQLiteAuthorityError("generated SQLite operation binding is invalid")
        if inputs.get("backend") != "sqlite":
            raise SQLiteAuthorityError("generated SQLite operation binding is invalid")
        if inputs.get("backup_operation_id") != operation_id:
            raise SQLiteAuthorityError("generated backup operation identity is invalid")
        if operation.get("preconditions") != ["previous-phase-complete"]:
            raise SQLiteAuthorityError("generated backup preconditions are invalid")
        if operation.get("durable_record") != "operation-id-and-outcome":
            raise SQLiteAuthorityError("generated operation durability contract is invalid")
        return operation_id, inputs

    @staticmethod
    def _validate_generated_operation_fields(operation: Mapping[str, object]) -> None:
        if set(operation) != {
            "operation_id",
            "opcode",
            "inputs",
            "timeout_seconds",
            "resources",
            "preconditions",
            "postconditions",
            "evidence",
            "durable_record",
        }:
            raise SQLiteAuthorityError("generated operation fields are incomplete or unknown")
        if operation.get("timeout_seconds") != 300:
            raise SQLiteAuthorityError("generated operation timeout is invalid")
        if operation.get("resources") != ["maintenance-barrier", "durable-operation-record"]:
            raise SQLiteAuthorityError("generated operation resources are invalid")
        if operation.get("postconditions") != ["backup-contract-satisfied"]:
            raise SQLiteAuthorityError("generated backup postconditions are invalid")
        if operation.get("evidence") != ["durable-operation-record"]:
            raise SQLiteAuthorityError("generated operation evidence is invalid")

    @staticmethod
    def _validate_generated_journal(
        snapshot: SQLiteLifecycleSnapshot,
        operation_id: str,
        inputs: Mapping[str, object],
    ) -> None:
        if snapshot.journal.phase != "backup" or not snapshot.journal.records:
            raise SQLiteAuthorityError("generated backup journal step is missing")
        journal_record = snapshot.journal.records[-1]
        if (
            journal_record.get("operation_id") != operation_id.rsplit(":", maxsplit=1)[0]
            or journal_record.get("step_id") != operation_id
            or journal_record.get("phase") != "backup"
            or journal_record.get("outcome") != "started"
        ):
            raise SQLiteAuthorityError("generated backup journal identity is invalid")
        context = journal_record.get("context")
        identity = snapshot.control.identity
        if (
            not isinstance(context, Mapping)
            or context.get("selector_ref") != inputs.get("selector_ref")
            or context.get("state_revision") != inputs.get("expected_state_revision")
            or inputs.get("expected_state_revision") != identity.state_revision
            or inputs.get("barrier_id") != identity.durable_barrier_id
            or inputs.get("fencing_token") != identity.fencing_token
            or context.get("durable_barrier_id") != identity.durable_barrier_id
            or context.get("fencing_token") != identity.fencing_token
        ):
            raise SQLiteAuthorityError("generated backup fencing or selector identity is invalid")

    def _publish_generated_outcome(
        self,
        before: SQLiteLifecycleSnapshot,
        operation_id: str,
        result: Mapping[str, Any],
    ) -> None:
        """Atomically persist the generated step outcome after its effect."""
        if self._journal is None or self._session_store is None:
            raise SQLiteAuthorityError("generated backup executor is not bound")
        lock = (
            nullcontext()
            if self._session_store.operation_owned_by_current_thread
            else self._session_store.operation_lock()
        )
        with lock:
            current = self._snapshot_locked()
            if current.control != before.control or current.journal != before.journal:
                raise SQLiteAuthorityError("generated backup durable state changed")
            document = json.loads(self._journal.read_text(encoding="utf-8"))
            records = document.get("records")
            if not isinstance(records, list) or not records:
                raise SQLiteAuthorityError("generated backup journal records are invalid")
            record = records[-1]
            if record.get("step_id") != operation_id or record.get("outcome") != "started":
                raise SQLiteAuthorityError("generated backup journal step changed")
            record["outcome"] = "success"
            record["result"] = dict(result)
            descriptor, temporary = tempfile.mkstemp(
                prefix=".upgrade-journal-", suffix=".json", dir=self._journal.parent
            )
            temporary_path = Path(temporary)
            try:
                try:
                    stream = os.fdopen(descriptor, "w", encoding="utf-8")
                except OSError:
                    with suppress(OSError):
                        os.close(descriptor)
                    raise
                with stream:
                    stream.write(json.dumps(document, sort_keys=True) + "\n")
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary_path.replace(self._journal)
                directory = os.open(self._journal.parent, os.O_DIRECTORY)
                try:
                    os.fsync(directory)
                finally:
                    self._close_directory_with_retry(directory)
            except OSError as error:
                raise SQLiteAuthorityError("generated backup outcome publication failed") from error
            finally:
                try:
                    temporary_path.unlink(missing_ok=True)
                except OSError as error:
                    raise SQLiteAuthorityError(
                        "generated backup temporary cleanup failed"
                    ) from error

    @staticmethod
    def _close_directory_with_retry(directory: int) -> None:
        try:
            os.close(directory)
        except OSError as error:
            try:
                os.close(directory)
            except OSError:
                raise error from None

    def restore(
        self, backup: Path, destination: Path, manifest: dict[str, Any], binding: dict[str, Any]
    ) -> None:
        self._run_effect(
            lambda: self._adapter.restore_bound(backup, destination, manifest, binding)
        )


class SQLiteAuthorityAdapter:
    """Read-only integrity evidence adapter; execute remains disabled."""

    requires_bound_rollback = True
    bound_rollback_kind = "sqlite"

    def __init__(self, authority: Path) -> None:
        resolved = authority.resolve()
        try:
            parent = resolved.parent.stat()
            descriptor = resolved.stat()
        except OSError as error:
            raise SQLiteAuthorityError("SQLite authority is unavailable") from error
        if (
            not stat.S_ISREG(descriptor.st_mode)
            or descriptor.st_uid != os.geteuid()
            or descriptor.st_nlink != 1
            or stat.S_IMODE(descriptor.st_mode) != 0o600
            or parent.st_uid != os.geteuid()
            or stat.S_IMODE(parent.st_mode) != 0o700
        ):
            raise SQLiteAuthorityError("SQLite authority descriptor is unsafe")
        self._authority = resolved
        self._session_identity = (descriptor.st_dev, descriptor.st_ino)
        self._parent_identity = (parent.st_dev, parent.st_ino)
        self._descriptor_identity = (
            descriptor.st_dev,
            descriptor.st_ino,
            stat.S_IMODE(descriptor.st_mode),
            descriptor.st_uid,
            descriptor.st_nlink,
        )
        self._sidecar_identities = {
            suffix: self._optional_identity(resolved.with_name(resolved.name + suffix))
            for suffix in ("-wal", "-shm")
        }

    def lifecycle_session(self) -> LifecycleSession:
        """Return an opaque session bound to this adapter's authority."""
        return _issue(self, self._authority)

    def lifecycle_executor(self) -> SQLiteLifecycleExecutor:
        return SQLiteLifecycleExecutor(self)

    def bind_lifecycle_executor(
        self, session_store: SQLiteBarrierSessionStore, journal: Path
    ) -> SQLiteLifecycleExecutor:
        """Return an executor bound to this adapter's durable state sources."""
        return SQLiteLifecycleExecutor.bind(self, session_store, journal)

    def backup_bound(self, destination: Path, binding: dict[str, Any]) -> dict[str, Any]:
        from tools.sqlite_backup import backup_database

        return backup_database(
            self._authority, destination, binding, session=self.lifecycle_session(), owner=self
        )

    def restore_bound(
        self,
        backup: Path,
        destination: Path,
        manifest: dict[str, Any],
        binding: dict[str, Any],
    ) -> None:
        from tools.sqlite_backup import restore_database

        self._check_identity()
        restore_database(
            backup,
            destination,
            manifest,
            binding,
            quiesced=True,
            session=_issue(self, backup),
            owner=self,
        )

    def bind_commit_capability(
        self,
        admission: Any,
        *,
        admission_reread: Any,
        connector: Any = sqlite3.connect,
    ) -> Any:
        """Bind the isolated SQLite effect seam without enabling dispatch.

        The capability captures the adapter's already-validated database and
        sidecar identities.  It is intentionally not reachable through
        ``execute`` or the public upgrade dispatcher while refinement is
        unproven.
        """
        from tools.sqlite_authority_mutation import SQLiteCommitCapability, SQLiteMutationError

        try:
            self._check_identity()
            sidecar = {
                suffix: (None if identity is None else (identity[0], identity[1]))
                for suffix, identity in self._sidecar_identities.items()
            }
            return SQLiteCommitCapability(
                self._authority,
                admission=admission,
                admission_reread=admission_reread,
                expected_db_identity=self._session_identity,
                expected_wal_identity=sidecar["-wal"],
                expected_shm_identity=sidecar["-shm"],
                connector=connector,
            )
        except (SQLiteAuthorityError, SQLiteMutationError) as error:
            raise SQLiteAuthorityError("SQLite commit capability binding was rejected") from error
        except BaseException as error:
            raise SQLiteAuthorityError("SQLite commit capability binding was rejected") from error

    def commit_bound(
        self,
        admission: Any,
        effect: Any,
        *,
        admission_reread: Any,
        connector: Any = sqlite3.connect,
    ) -> Any:
        """Execute one explicitly bound SQLite effect outside public dispatch.

        The callback receives only the capability-owned transaction.  This
        entry point is not reachable through ``execute`` or the upgrade CLI;
        it exists to make the independently reviewed effect boundary concrete.
        """
        capability = self.bind_commit_capability(
            admission,
            admission_reread=admission_reread,
            connector=connector,
        )
        try:
            return capability.commit(effect)
        except SQLiteAuthorityError:
            raise
        except BaseException as error:
            raise SQLiteAuthorityError("bound SQLite authority effect failed") from error

    def bind_durable_commit_capability(
        self,
        admission: Any,
        journal: Any,
        *,
        session_revision: int,
        admission_reread: Any,
        connector: Any = sqlite3.connect,
    ) -> Any:
        """Bind SQLite's isolated effect to the durable journal seam."""
        from tools.authority_mutation import AuthorityMutationError, DurableBoundBackendMutation

        capability = self.bind_commit_capability(
            admission,
            admission_reread=admission_reread,
            connector=connector,
        )
        try:
            return DurableBoundBackendMutation(
                admission,
                journal,
                session_revision=session_revision,
                backend_effect=lambda effect: capability.commit(effect),
            )
        except AuthorityMutationError as error:
            raise SQLiteAuthorityError(
                "SQLite durable commit capability binding was rejected"
            ) from error
        except BaseException as error:
            raise SQLiteAuthorityError(
                "SQLite durable commit capability binding was rejected"
            ) from error

    def bind_durable_rollback_capability(  # pragma: no cover - isolated backend seam
        self,
        admission: Any,
        journal: Any,
        *,
        session_revision: int,
        rollback_effect: Any,
    ) -> Any:
        """Bind one backend-owned rollback effect to the durable fence.

        Public rollback dispatch remains disabled; this is only the typed
        internal capability seam for a separately reviewed rollback effect.
        """
        from tools.authority_mutation import AuthorityMutationError, DurableBoundBackendMutation

        if getattr(admission, "target", None) != "rollback" or not callable(rollback_effect):
            raise SQLiteAuthorityError("SQLite durable rollback capability binding was rejected")
        try:
            return DurableBoundBackendMutation(
                admission,
                journal,
                session_revision=session_revision,
                backend_effect=rollback_effect,
            )
        except AuthorityMutationError as error:
            raise SQLiteAuthorityError(
                "SQLite durable rollback capability binding was rejected"
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
    def verify_backup_artifact(
        backup: Path, manifest: Mapping[str, object], binding: Mapping[str, object]
    ) -> dict[str, object]:
        """Run SQLite manifest, digest, integrity, and FK checks read-only."""
        from tools.sqlite_backup import verify_backup

        return verify_backup(backup, dict(manifest), dict(binding))

    @staticmethod
    def _optional_identity(path: Path) -> tuple[int, int, int, int, int] | None:
        try:
            value = path.lstat()
        except FileNotFoundError:
            return None
        except OSError as error:
            raise SQLiteAuthorityError("SQLite authority sidecar is unavailable") from error
        except BaseException as error:
            raise SQLiteAuthorityError("SQLite authority sidecar is unavailable") from error
        if (
            not stat.S_ISREG(value.st_mode)
            or value.st_uid != os.geteuid()
            or value.st_nlink != 1
            or stat.S_IMODE(value.st_mode) != 0o600
        ):
            raise SQLiteAuthorityError("SQLite authority sidecar is unsafe")
        return (
            value.st_dev,
            value.st_ino,
            stat.S_IMODE(value.st_mode),
            value.st_uid,
            value.st_nlink,
        )

    def _check_identity(self) -> None:
        try:
            parent = self._authority.parent.lstat()
            descriptor = self._authority.lstat()
        except OSError as error:
            raise SQLiteAuthorityError("SQLite authority identity changed") from error
        except BaseException as error:
            raise SQLiteAuthorityError("SQLite authority identity changed") from error
        current_parent = (parent.st_dev, parent.st_ino)
        current_descriptor = (
            descriptor.st_dev,
            descriptor.st_ino,
            stat.S_IMODE(descriptor.st_mode),
            descriptor.st_uid,
            descriptor.st_nlink,
        )
        if (
            current_parent != self._parent_identity
            or parent.st_uid != os.geteuid()
            or stat.S_IMODE(parent.st_mode) != 0o700
            or current_descriptor != self._descriptor_identity
            or self._sidecar_identities
            != {
                suffix: self._optional_identity(
                    self._authority.with_name(self._authority.name + suffix)
                )
                for suffix in ("-wal", "-shm")
            }
        ):
            raise SQLiteAuthorityError("SQLite authority identity changed")

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
        if set(context) != required or context.get("backend") != "sqlite":
            raise SQLiteAuthorityError("SQLite authority context is incomplete or mismatched")
        schema_version = context.get("schema_version")
        state_revision = context.get("state_revision")
        if type(schema_version) is not int or schema_version < 1:
            raise SQLiteAuthorityError("SQLite authority context types are invalid")
        if type(state_revision) is not int or state_revision < 1:
            raise SQLiteAuthorityError("SQLite authority context types are invalid")
        for field in required - {"schema_version", "state_revision"}:
            value = context.get(field)
            if type(value) is not str or not value:
                raise SQLiteAuthorityError("SQLite authority context types are invalid")
        if context.get("target") not in {"new", "rollback"}:
            raise SQLiteAuthorityError("SQLite authority context target is invalid")
        return dict(context)

    def snapshot(self, phase: str, context: Mapping[str, object]) -> dict[str, Any]:
        """Return read-only integrity evidence without claiming mutation safety."""
        if type(phase) is not str or phase not in _SUPPORTED_PHASES:
            raise SQLiteAuthorityError("SQLite authority phase is invalid")
        value = self._context(context)
        self._check_identity()
        try:
            connection = sqlite3.connect(
                f"file:{self._authority}?mode=ro", uri=True, isolation_level=None
            )
            try:
                integrity = str(connection.execute("PRAGMA integrity_check").fetchone()[0])
                foreign = list(connection.execute("PRAGMA foreign_key_check"))
            finally:
                connection.close()
            self._check_identity()
        except (OSError, sqlite3.Error, TypeError, IndexError) as error:
            raise SQLiteAuthorityError("SQLite authority observation failed") from error
        if integrity != "ok" or foreign:
            raise SQLiteAuthorityError("SQLite authority integrity is not clean")
        value.update(
            {
                "phase": phase,
                "backend_identity_verified": True,
                "sqlite_integrity_verified": True,
                "sqlite_foreign_keys_verified": True,
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
    ) -> dict[str, Any]:
        """Read SQLite integrity only inside a trusted, identity-bound scope."""
        from tools.scoped_backend_adapter import ScopedBackendAdapter

        if type(phase) is not str or phase not in _SUPPORTED_PHASES:
            raise SQLiteAuthorityError("SQLite authority phase is invalid")
        if not isinstance(lease, AdmissionLease):
            raise SQLiteAuthorityError("trusted admission lease is required")
        if not isinstance(admission_recheck, AdmissionRecheck):
            raise SQLiteAuthorityError("trusted admission recheck is required")
        if admission_recheck.lease != lease:
            raise SQLiteAuthorityError("trusted admission recheck does not match lease")
        try:
            validated_context = self._context(context)
        except SQLiteAuthorityError:
            raise
        except Exception as error:
            raise SQLiteAuthorityError("SQLite authority context is invalid") from error
        if not isinstance(scope, LockDomainScope):
            raise SQLiteAuthorityError("concrete lock-domain scope is required")
        expected_identity = {
            "project_id": lease.project_id,
            "authority_revision": lease.authority_revision,
            "fencing_token": lease.fencing_token,
            "fencing_owner": lease.fencing_owner,
            "durable_barrier_id": lease.durable_barrier_id,
            "state_revision": lease.revision,
        }
        if any(validated_context.get(name) != value for name, value in expected_identity.items()):
            raise SQLiteAuthorityError("trusted session identity changed")
        try:
            value = ScopedBackendAdapter(self, scope).snapshot(
                phase, validated_context, scope_context=expected_identity
            )
        except SQLiteAuthorityError:
            raise
        except (TypeError, RuntimeError) as error:
            raise SQLiteAuthorityError("trusted SQLite session reread was rejected") from error
        expected_result_keys = set(validated_context) | {
            "phase",
            "backend_identity_verified",
            "sqlite_integrity_verified",
            "sqlite_foreign_keys_verified",
            "mutates_authority",
        }
        if set(value) != expected_result_keys:
            raise SQLiteAuthorityError("SQLite authority backend result schema changed")
        for field, expected in validated_context.items():
            if value.get(field) != expected or type(value.get(field)) is not type(expected):
                raise SQLiteAuthorityError("SQLite authority backend context identity changed")
        if type(value.get("phase")) is not str or value.get("phase") != phase:
            raise SQLiteAuthorityError("SQLite authority backend phase changed")
        if (
            type(value.get("backend_identity_verified")) is not bool
            or value.get("backend_identity_verified") is not True
        ):
            raise SQLiteAuthorityError("SQLite authority backend identity is unverified")
        if (
            type(value.get("sqlite_integrity_verified")) is not bool
            or value.get("sqlite_integrity_verified") is not True
        ):
            raise SQLiteAuthorityError("SQLite authority integrity is unverified")
        if (
            type(value.get("sqlite_foreign_keys_verified")) is not bool
            or value.get("sqlite_foreign_keys_verified") is not True
        ):
            raise SQLiteAuthorityError("SQLite authority foreign keys are unverified")
        if (
            type(value.get("mutates_authority")) is not bool
            or value.get("mutates_authority") is not False
        ):
            raise SQLiteAuthorityError("SQLite authority backend is not read-only")
        return value

    def verify_rollback_context(self, context: Mapping[str, object]) -> dict[str, Any]:
        if context.get("target") != "rollback":
            raise SQLiteAuthorityError("SQLite rollback context target is invalid")
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
    ) -> dict[str, Any]:
        """Reread rollback evidence only inside a trusted scope."""
        if context.get("target") != "rollback":
            raise SQLiteAuthorityError("SQLite rollback context target is invalid")
        value = self.snapshot_bound(
            "rollback",
            context,
            scope,
            lease=lease,
            admission_recheck=admission_recheck,
        )
        value["rollback_context_verified"] = False
        return value

    def execute(self, _phase: str, _context: Mapping[str, object]) -> dict[str, Any]:
        raise SQLiteAuthorityError("SQLite authority mutation adapter is not implemented")
