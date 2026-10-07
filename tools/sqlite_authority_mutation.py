# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Isolated, identity-bound SQLite authority commit capability."""

from __future__ import annotations

import sqlite3
import stat
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import NoReturn

from tools.authority_mutation import (
    AuthorityMutationAmbiguousError,
    AuthorityMutationRejectedError,
)
from tools.authority_neutral_commit import CommitAdmissionBundle


class SQLiteMutationError(RuntimeError):
    """A SQLite authority effect was rejected."""


class SQLiteMutationRejectedError(SQLiteMutationError, AuthorityMutationRejectedError):
    """SQLite admission was rejected before opening the effect transaction."""


class SQLiteMutationAmbiguousError(SQLiteMutationError, AuthorityMutationAmbiguousError):
    """The SQLite commit outcome cannot be classified safely."""


@dataclass(frozen=True)
class SQLiteCommitResult:
    backend: str
    target: str
    operation_id: str
    state_revision: int
    barrier_id: str
    artifact_identity: str
    manifest_identity: str
    selector_identity: str
    runtime_identity: str
    fencing_token: str
    integrity_check: str
    foreign_key_violations: int
    mutates_authority: bool = True


_Commit = Callable[[sqlite3.Connection], None]
_Connector = Callable[..., sqlite3.Connection]
_AdmissionReread = Callable[[], Mapping[str, object]]


class SQLiteCommitCapability:
    """Apply one callback inside a bound transaction and verify the result.

    The caller owns the durable barrier/lock scope. This capability only
    checks immutable admission and filesystem identities; it is not wired into
    the public upgrade dispatcher.
    """

    def __init__(
        self,
        authority: Path,
        *,
        admission: CommitAdmissionBundle,
        admission_reread: _AdmissionReread,
        expected_db_identity: tuple[int, int],
        expected_wal_identity: tuple[int, int] | None,
        expected_shm_identity: tuple[int, int] | None,
        connector: _Connector = sqlite3.connect,
    ) -> None:
        if admission.backend != "sqlite" or admission.target != "new":
            raise SQLiteMutationError("SQLite mutation admission identity is invalid")
        if type(admission.state_revision) is not int or admission.state_revision < 1:
            raise SQLiteMutationError("SQLite mutation revision is invalid")
        # Preserve the supplied pathname so the pre-effect lstat fence can
        # reject a symlinked authority instead of silently following it.
        try:
            self._authority = authority.absolute()
            self._ancestor_identities = self._ancestor_identities_for(self._authority)
        except SQLiteMutationRejectedError:
            raise
        except BaseException as error:
            raise SQLiteMutationRejectedError(
                "SQLite authority identity capture was rejected"
            ) from error
        self._admission = admission
        if not callable(admission_reread):
            raise SQLiteMutationError("SQLite admission reread is invalid")
        self._admission_reread = admission_reread
        self._db_identity = expected_db_identity
        self._wal_identity = expected_wal_identity
        self._shm_identity = expected_shm_identity
        self._connector = connector
        self._consumed = False
        self._validate_identity(expected_db_identity, "database")
        self._validate_optional_identity(expected_wal_identity, "WAL")
        self._validate_optional_identity(expected_shm_identity, "SHM")

    @staticmethod
    def _validate_identity(value: tuple[int, int], label: str) -> None:
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or any(type(part) is not int or part < 0 for part in value)
        ):
            raise SQLiteMutationError(f"SQLite {label} identity is invalid")

    @classmethod
    def _validate_optional_identity(cls, value: tuple[int, int] | None, label: str) -> None:
        if value is not None:
            cls._validate_identity(value, label)

    @staticmethod
    def _ancestor_identities_for(path: Path) -> tuple[tuple[str, int, int], ...]:
        identities: list[tuple[str, int, int]] = []
        current = Path(path.anchor)
        for part in path.parent.parts[1:]:
            current /= part
            try:
                status = current.lstat()
            except FileNotFoundError as error:
                raise SQLiteMutationRejectedError(
                    "SQLite authority ancestor is unavailable"
                ) from error
            except OSError as error:
                raise SQLiteMutationRejectedError(
                    "SQLite sidecar identity is unavailable"
                ) from error
            except BaseException as error:
                raise SQLiteMutationRejectedError(
                    "SQLite sidecar identity is unavailable"
                ) from error
            if not stat.S_ISDIR(status.st_mode):
                raise SQLiteMutationRejectedError("SQLite authority ancestor is not a directory")
            identities.append((str(current), status.st_dev, status.st_ino))
        return tuple(identities)

    @staticmethod
    def _identity(path: Path) -> tuple[int, int] | None:
        try:
            status = path.lstat()
        except FileNotFoundError:
            return None
        except OSError as error:
            raise SQLiteMutationRejectedError("SQLite sidecar identity is unavailable") from error
        except BaseException as error:
            raise SQLiteMutationRejectedError("SQLite sidecar identity is unavailable") from error
        if not stat.S_ISREG(status.st_mode) or status.st_nlink != 1:
            raise SQLiteMutationRejectedError("SQLite authority file is not a regular private file")
        return status.st_dev, status.st_ino

    def _assert_filesystem_identity(self) -> None:
        try:
            self._assert_filesystem_identity_impl()
        except SQLiteMutationRejectedError:
            raise
        except BaseException as error:
            raise SQLiteMutationRejectedError(
                "SQLite filesystem identity reread was rejected"
            ) from error

    def _assert_filesystem_identity_impl(self) -> None:
        try:
            ancestors = self._ancestor_identities_for(self._authority)
        except SQLiteMutationRejectedError as error:
            if "ancestor is unavailable" in str(error) or "ancestor is not a directory" in str(
                error
            ):
                raise SQLiteMutationRejectedError(
                    "SQLite authority ancestor identity changed"
                ) from error
            raise
        if ancestors != self._ancestor_identities:
            raise SQLiteMutationRejectedError("SQLite authority ancestor identity changed")
        if self._identity(self._authority) != self._db_identity:
            raise SQLiteMutationRejectedError("SQLite database identity changed")
        if (
            self._identity(self._authority.with_name(self._authority.name + "-wal"))
            != self._wal_identity
        ):
            raise SQLiteMutationRejectedError("SQLite WAL identity changed")
        if (
            self._identity(self._authority.with_name(self._authority.name + "-shm"))
            != self._shm_identity
        ):
            raise SQLiteMutationRejectedError("SQLite SHM identity changed")

    def _assert_admission_current(self) -> None:
        try:
            current = self._admission_reread()
        except BaseException as error:
            raise SQLiteMutationRejectedError("SQLite admission reread was rejected") from error
        if not isinstance(current, Mapping) or not self._admission.matches(current):
            raise SQLiteMutationRejectedError("SQLite admission identity changed before commit")

    def _consume(self, effect: _Commit) -> None:
        if self._consumed:
            raise SQLiteMutationError("SQLite mutation capability already consumed")
        if not callable(effect):
            raise SQLiteMutationError("SQLite authority effect is invalid")
        self._consumed = True

    @staticmethod
    def _close_connection(connection: sqlite3.Connection) -> None:
        try:
            connection.close()
        except (OSError, sqlite3.Error) as error:
            raise SQLiteMutationAmbiguousError(
                "SQLite connection close outcome is ambiguous"
            ) from error
        except BaseException as error:
            raise SQLiteMutationAmbiguousError(
                "SQLite connection close outcome is ambiguous"
            ) from error

    @staticmethod
    def _rollback_connection(connection: sqlite3.Connection) -> None:
        try:
            connection.rollback()
        except (OSError, sqlite3.Error) as error:
            raise SQLiteMutationAmbiguousError("SQLite rollback outcome is ambiguous") from error
        except BaseException as error:
            raise SQLiteMutationAmbiguousError("SQLite rollback outcome is ambiguous") from error

    def _classify_oserror(
        self,
        error: OSError,
        connection: sqlite3.Connection | None,
        effect_started: bool,
    ) -> NoReturn:
        if connection is not None:
            self._rollback_connection(connection)
        if not effect_started:
            raise SQLiteMutationRejectedError(
                "SQLite authority connection was rejected before effect"
            ) from error
        raise SQLiteMutationAmbiguousError("SQLite commit outcome is ambiguous") from error

    def _classify_sqlite_error(
        self,
        error: sqlite3.Error,
        connection: sqlite3.Connection | None,
        effect_started: bool,
    ) -> NoReturn:
        if connection is not None:
            self._rollback_connection(connection)
        if not effect_started:
            raise SQLiteMutationRejectedError(
                "SQLite authority setup was rejected before effect"
            ) from error
        raise SQLiteMutationAmbiguousError("SQLite commit outcome is ambiguous") from error

    def _verify_post_commit(self) -> tuple[str, int]:
        try:
            self._assert_filesystem_identity()
            verification = sqlite3.connect(self._authority)
            try:
                with verification:
                    verification.execute("PRAGMA foreign_keys=ON")
                    integrity = str(verification.execute("PRAGMA integrity_check").fetchone()[0])
                    violations = len(verification.execute("PRAGMA foreign_key_check").fetchall())
            finally:
                verification.close()
            self._assert_filesystem_identity()
        except (OSError, SQLiteMutationError, sqlite3.Error) as error:
            raise SQLiteMutationAmbiguousError(
                "SQLite post-commit verification is ambiguous"
            ) from error
        except BaseException as error:
            raise SQLiteMutationAmbiguousError(
                "SQLite post-commit verification is ambiguous"
            ) from error
        return integrity, violations

    def _assert_post_commit_admission(self) -> None:
        try:
            # A replacement owner/session after SQLite returns cannot receive
            # a receipt for the admission that authorized the effect.
            self._assert_admission_current()
        except SQLiteMutationError as error:
            raise SQLiteMutationAmbiguousError(
                "SQLite post-commit admission is ambiguous"
            ) from error
        except BaseException as error:
            raise SQLiteMutationAmbiguousError(
                "SQLite post-commit admission is ambiguous"
            ) from error

    def commit(self, effect: _Commit) -> SQLiteCommitResult:
        self._consume(effect)
        self._assert_filesystem_identity()
        self._assert_admission_current()
        connection: sqlite3.Connection | None = None
        effect_started = False
        try:
            connection = self._connector(self._authority, isolation_level=None, timeout=5)
            # The pathname may be replaced between the initial admission check
            # and connect(). Revalidate the opened authority before beginning
            # any transaction or invoking the caller's effect.
            self._assert_filesystem_identity()
            connection.execute("PRAGMA foreign_keys=ON")
            connection.execute("PRAGMA synchronous=FULL")
            connection.execute("BEGIN IMMEDIATE")
            effect_started = True
            effect(connection)
            connection.commit()
        except OSError as error:
            self._classify_oserror(error, connection, effect_started)
        except sqlite3.Error as error:
            self._classify_sqlite_error(error, connection, effect_started)
        except SQLiteMutationRejectedError:
            # The second identity check runs after connect but before BEGIN;
            # it is still a pre-effect rejection and must not be relabeled as
            # an uncertain authority outcome.
            raise
        except BaseException as error:
            if connection is not None:
                self._rollback_connection(connection)
            raise SQLiteMutationAmbiguousError("SQLite commit outcome is ambiguous") from error
        finally:
            if connection is not None:
                self._close_connection(connection)
        self._assert_post_commit_admission()
        integrity, violations = self._verify_post_commit()
        if integrity != "ok" or violations:
            raise SQLiteMutationAmbiguousError(
                "SQLite post-commit integrity is invalid; recovery is required"
            )
        return SQLiteCommitResult(
            backend=self._admission.backend,
            target=self._admission.target,
            operation_id=self._admission.operation_id,
            state_revision=self._admission.state_revision,
            barrier_id=self._admission.barrier_id,
            artifact_identity=self._admission.artifact_identity,
            manifest_identity=self._admission.manifest_identity,
            selector_identity=self._admission.selector_identity,
            runtime_identity=self._admission.runtime_identity,
            fencing_token=self._admission.fencing_token,
            integrity_check=integrity,
            foreign_key_violations=violations,
        )
