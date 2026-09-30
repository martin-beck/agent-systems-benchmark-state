# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Strict canonical identity envelope for coordinator upgrade operations."""

from __future__ import annotations

import hashlib
import json
import posixpath
import re
import uuid
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import PurePosixPath
from typing import cast

ENVELOPE_SCHEMA_VERSION = 2
# The v10 barrier is a target-neutral session.  Child envelopes continue to
# carry ``target`` (``new`` or ``rollback``), but that mutable operation choice
# must never change the identity of the shared barrier session.
BARRIER_SESSION_SCHEMA_VERSION = 1
BARRIER_SESSION_IDENTITY_FIELDS = (
    "schema_version",
    "project_id",
    "attempt_id",
    "state_revision",
    "authority_revision_at_acquire",
    "durable_barrier_id",
    "fencing_token",
    "fencing_owner",
)
BARRIER_IDENTITY_FIELDS = (
    "schema_version",
    "project_id",
    "operation_id",
    "state_revision",
    "authority_revision",
    "durable_barrier_id",
    "fencing_token",
    "fencing_owner",
    "target",
)
ENVELOPE_FIELDS = (
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
)
_TOKEN = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,127}")
_CHILD_TOKEN = re.compile(r"[A-Za-z0-9][A-Za-z0-9._:-]{0,127}")
_SELECTOR_REF = re.compile(r"(?!/)(?!.*(?:^|/)\.\.(?:/|$))[A-Za-z0-9._/-]{1,255}")
_DIGEST = re.compile(r"[0-9a-f]{64}")


class UpgradeIdentityError(ValueError):
    """An upgrade envelope is incomplete, non-canonical, or inconsistent."""


@dataclass(frozen=True, slots=True)
class BarrierSessionIdentity:
    """Typed target-neutral identity shared by forward and rollback children.

    This is a contract seam only.  It deliberately contains no mutable state
    or persistence handle; a durable adapter must validate this value before
    adding status/revision fields to a control-store row.
    """

    schema_version: int
    project_id: str
    attempt_id: str
    state_revision: int
    authority_revision_at_acquire: str
    durable_barrier_id: str
    fencing_token: str
    fencing_owner: str
    identity_digest: str

    @classmethod
    def from_record(cls, record: Mapping[str, object]) -> BarrierSessionIdentity:
        value = validate_barrier_session_identity(record)
        return cls(
            schema_version=cast(int, value["schema_version"]),
            project_id=cast(str, value["project_id"]),
            attempt_id=cast(str, value["attempt_id"]),
            state_revision=cast(int, value["state_revision"]),
            authority_revision_at_acquire=cast(str, value["authority_revision_at_acquire"]),
            durable_barrier_id=cast(str, value["durable_barrier_id"]),
            fencing_token=cast(str, value["fencing_token"]),
            fencing_owner=cast(str, value["fencing_owner"]),
            identity_digest=cast(str, value["identity_digest"]),
        )

    def as_record(self) -> dict[str, object]:
        return {
            field: getattr(self, field)
            for field in (*BARRIER_SESSION_IDENTITY_FIELDS, "identity_digest")
        }


@dataclass(frozen=True, slots=True)
class BarrierChildIdentity:
    """Typed immutable child binding under one barrier session."""

    operation_id: str
    target: str
    barrier_identity_digest: str

    @classmethod
    def bind(
        cls, session: BarrierSessionIdentity, operation_id: str, target: str
    ) -> BarrierChildIdentity:
        if _CHILD_TOKEN.fullmatch(operation_id) is None:
            raise UpgradeIdentityError("barrier child operation identity is invalid")
        if target not in {"new", "rollback"}:
            raise UpgradeIdentityError("barrier child target is invalid")
        return cls(operation_id, target, session.identity_digest)

    def validate_for(self, session: BarrierSessionIdentity) -> None:
        if self.barrier_identity_digest != session.identity_digest:
            raise UpgradeIdentityError("barrier child session identity does not match")
        if _CHILD_TOKEN.fullmatch(self.operation_id) is None:
            raise UpgradeIdentityError("barrier child operation identity is invalid")
        if self.target not in {"new", "rollback"}:
            raise UpgradeIdentityError("barrier child target is invalid")


def canonical_barrier_session_digest(record: Mapping[str, object]) -> str:
    """Hash the immutable, target-neutral v10 barrier-session identity."""
    return hashlib.sha256(
        _canonical_bytes(_select(record, BARRIER_SESSION_IDENTITY_FIELDS))
    ).hexdigest()


def validate_barrier_session_identity(  # noqa: C901
    record: Mapping[str, object],
) -> dict[str, object]:
    """Validate one immutable v10 barrier-session identity.

    This helper is intentionally separate from :func:`validate_envelope`.
    Existing upgrade commands use the v9 envelope and remain fail-closed; the
    v10 session identity is only a contract primitive until its durable
    control-store adapter is implemented and independently reviewed.
    """
    if set(record) != set(BARRIER_SESSION_IDENTITY_FIELDS) | {"identity_digest"}:
        raise UpgradeIdentityError("barrier session identity fields are invalid")
    if record["schema_version"] != BARRIER_SESSION_SCHEMA_VERSION:
        raise UpgradeIdentityError("barrier session schema version is invalid")
    project_id = record["project_id"]
    if not isinstance(project_id, str):
        raise UpgradeIdentityError("barrier session project identity is invalid")
    try:
        project = uuid.UUID(project_id)
    except ValueError as error:
        raise UpgradeIdentityError("barrier session project identity is invalid") from error
    if project.version != 4:
        raise UpgradeIdentityError("barrier session project identity must be UUIDv4")
    for field in (
        "attempt_id",
        "authority_revision_at_acquire",
        "durable_barrier_id",
        "fencing_token",
        "fencing_owner",
    ):
        value = record[field]
        if not isinstance(value, str) or _TOKEN.fullmatch(value) is None:
            raise UpgradeIdentityError(f"barrier session {field} is invalid")
    for field in ("state_revision",):
        value = record[field]
        if not isinstance(value, int) or isinstance(value, bool) or value < 1:
            raise UpgradeIdentityError(f"barrier session {field} is invalid")
    digest = record["identity_digest"]
    if not isinstance(digest, str) or _DIGEST.fullmatch(digest) is None:
        raise UpgradeIdentityError("barrier session identity digest is invalid")
    if digest != canonical_barrier_session_digest(record):
        raise UpgradeIdentityError("barrier session identity digest does not match")
    return dict(record)


def _canonical_bytes(value: Mapping[str, object]) -> bytes:
    try:
        return json.dumps(
            value,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    except (TypeError, ValueError) as error:
        raise UpgradeIdentityError("upgrade identity is not canonical JSON") from error


def _select(record: Mapping[str, object], fields: tuple[str, ...]) -> dict[str, object]:
    try:
        return {field: record[field] for field in fields}
    except KeyError as error:
        raise UpgradeIdentityError(f"upgrade identity field is missing: {error.args[0]}") from error


def canonical_barrier_digest(record: Mapping[str, object]) -> str:
    """Hash exactly the immutable v9 barrier identity tuple."""
    return hashlib.sha256(_canonical_bytes(_select(record, BARRIER_IDENTITY_FIELDS))).hexdigest()


def canonical_envelope_digest(record: Mapping[str, object]) -> str:
    """Hash the exact v9 envelope, excluding only its self digest."""
    fields = tuple(field for field in ENVELOPE_FIELDS if field != "envelope_digest")
    return hashlib.sha256(_canonical_bytes(_select(record, fields))).hexdigest()


def _canonical_path(field: str, value: object) -> PurePosixPath:
    if (
        not isinstance(value, str)
        or not value.startswith("/")
        or value.startswith("//")
        or "\x00" in value
    ):
        raise UpgradeIdentityError(f"upgrade {field} path is invalid")
    if posixpath.normpath(value) != value or value == "/":
        raise UpgradeIdentityError(f"upgrade {field} path is not canonical")
    return PurePosixPath(value)


def _contains(parent: PurePosixPath, child: PurePosixPath) -> bool:
    try:
        child.relative_to(parent)
    except ValueError:
        return False
    return True


def validate_envelope(record: Mapping[str, object]) -> dict[str, object]:  # noqa: C901
    """Validate and return an exact, non-coerced v9 identity envelope."""
    if set(record) != set(ENVELOPE_FIELDS):
        raise UpgradeIdentityError("upgrade envelope fields are invalid")
    if type(record["schema_version"]) is not int or (
        record["schema_version"] != ENVELOPE_SCHEMA_VERSION
    ):
        raise UpgradeIdentityError("upgrade envelope schema version is invalid")
    revision = record["state_revision"]
    if not isinstance(revision, int) or isinstance(revision, bool) or revision < 1:
        raise UpgradeIdentityError("upgrade state revision is invalid")
    project_id = record["project_id"]
    if not isinstance(project_id, str):
        raise UpgradeIdentityError("upgrade project identity is invalid")
    try:
        project = uuid.UUID(project_id)
    except ValueError as error:
        raise UpgradeIdentityError("upgrade project identity is invalid") from error
    if project.version != 4:
        raise UpgradeIdentityError("upgrade project identity must be UUIDv4")
    if record["backend"] not in {"git", "sqlite"} or record["target"] not in {
        "new",
        "rollback",
    }:
        raise UpgradeIdentityError("upgrade backend or target is invalid")
    for field in (
        "operation_id",
        "authority_revision",
        "durable_barrier_id",
        "fencing_token",
        "fencing_owner",
    ):
        value = record[field]
        if not isinstance(value, str) or _TOKEN.fullmatch(value) is None:
            raise UpgradeIdentityError(f"upgrade {field} is invalid")
    for field in ("barrier_identity_digest", "envelope_digest"):
        value = record[field]
        if not isinstance(value, str) or _DIGEST.fullmatch(value) is None:
            raise UpgradeIdentityError(f"upgrade {field} is invalid")

    root = _canonical_path("artifact_root", record["artifact_root"])
    source = _canonical_path("source", record["source"])
    destination = _canonical_path("destination", record["destination"])
    manifest = _canonical_path("manifest", record["manifest"])
    selector_ref = record["selector_ref"]
    if (
        not isinstance(selector_ref, str)
        or _SELECTOR_REF.fullmatch(selector_ref) is None
        or posixpath.normpath(selector_ref) != selector_ref
    ):
        raise UpgradeIdentityError("upgrade selector reference is invalid")
    if not _contains(root, destination) or not _contains(root, manifest):
        raise UpgradeIdentityError("upgrade outputs escape artifact root")
    if destination == root or manifest == root:
        raise UpgradeIdentityError("upgrade output aliases artifact root")
    roles = (source, destination, manifest)
    if len(set(roles)) != len(roles):
        raise UpgradeIdentityError("upgrade path roles alias")
    for left, right in ((source, destination), (source, manifest), (destination, manifest)):
        if _contains(left, right) or _contains(right, left):
            raise UpgradeIdentityError("upgrade path roles overlap")

    if record["barrier_identity_digest"] != canonical_barrier_digest(record):
        raise UpgradeIdentityError("upgrade barrier identity digest is invalid")
    if record["envelope_digest"] != canonical_envelope_digest(record):
        raise UpgradeIdentityError("upgrade envelope digest is invalid")
    return dict(record)
