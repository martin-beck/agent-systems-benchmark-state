# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Pure, local-first publication primitives for issue-series manifests.

This module deliberately performs no I/O.  The command adapter owns durable
receipts and any optional network transport; these helpers only make its
public content, correlation key, and normalized outcomes deterministic.
"""

from __future__ import annotations

import hashlib
import re
from collections.abc import Mapping
from dataclasses import dataclass
from typing import Final, Literal

from tools.issue_series import IssueSeriesManifest

PublicationStatus = Literal[
    "published",
    "already_published",
    "dry_run",
    "deferred_unavailable",
    "deferred_unauthorized",
    "deferred_timeout",
    "deferred_conflict",
    "deferred_wrong_identity",
    "deferred_closed",
    "deferred_moved",
    "ambiguous",
]

_DIGEST: Final = re.compile(r"sha256:[0-9a-f]{64}$")
_COMMENT_ID: Final = re.compile(r"[1-9][0-9]{0,18}$")
_MAX_MARKDOWN: Final = 8_192
_STATUS_MAP: Final[dict[str, PublicationStatus]] = {
    "published": "published",
    "already_published": "already_published",
    "unavailable": "deferred_unavailable",
    "unauthorized": "deferred_unauthorized",
    "timeout": "deferred_timeout",
    "conflict": "deferred_conflict",
    "wrong_identity": "deferred_wrong_identity",
    "closed": "deferred_closed",
    "moved": "deferred_moved",
    "ambiguous": "ambiguous",
}


class IssueSeriesPublicationError(ValueError):
    """Raised when a publication input is unsafe or internally inconsistent."""


@dataclass(frozen=True)
class PublicationOutcome:
    """A bounded result safe to persist without retaining remote response text."""

    status: PublicationStatus
    publication_key: str
    manifest_digest: str
    comment_id: str | None = None


def _require_digest(value: object, label: str = "manifest_digest") -> str:
    if not isinstance(value, str) or not _DIGEST.fullmatch(value):
        raise IssueSeriesPublicationError(f"{label} must be a lowercase sha256 digest")
    return value


def _public_text(value: str, limit: int = 500) -> str:
    """Render one bounded Markdown text fragment without active Markdown syntax."""
    if len(value) > limit or "\n" in value or "\r" in value:
        raise IssueSeriesPublicationError("manifest text is not bounded single-line text")
    return "".join(
        "\\" + character if character in r"\\`*_{}[]<>()#!|" else character for character in value
    )


def publication_key(repository: str, issue_number: int, manifest_digest: str) -> str:
    """Return an immutable SHA-256 correlation key for one publication intent."""
    if not isinstance(repository, str) or not repository.startswith("github.com/"):
        raise IssueSeriesPublicationError("repository must be a normalized GitHub identity")
    if repository != repository.lower() or "\n" in repository or "\r" in repository:
        raise IssueSeriesPublicationError("repository must be a normalized GitHub identity")
    if isinstance(issue_number, bool) or not isinstance(issue_number, int) or issue_number < 1:
        raise IssueSeriesPublicationError("issue_number must be a positive integer")
    digest = _require_digest(manifest_digest)
    payload = f"issue-series-publication-v1\0{repository}\0{issue_number}\0{digest}".encode()
    return hashlib.sha256(payload).hexdigest()


def render_publication(manifest: IssueSeriesManifest, manifest_digest: str) -> str:
    """Render deterministic public-safe Markdown with a machine-readable marker."""
    digest = _require_digest(manifest_digest)
    key = publication_key(manifest.repository, manifest.issue_number, digest)
    lines = [
        "## Proposed coordinator work",
        "",
        "This is a locally validated, proposed issue-series plan.",
        "",
        "| AR | Title |",
        "| --- | --- |",
    ]
    lines.extend(
        f"| {member.id} | {_public_text(member.short_title)} |" for member in manifest.members
    )
    lines.extend(
        [
            "",
            f"Finalizer: `{manifest.finalizer}`.",
            "",
            f"<!-- agent-workflow-issue-series:v1 digest={digest} key={key} -->",
        ]
    )
    rendered = "\n".join(lines) + "\n"
    if len(rendered) > _MAX_MARKDOWN:
        raise IssueSeriesPublicationError("rendered publication exceeds bounded size")
    return rendered


def normalize_outcome(
    value: object,
    *,
    repository: str,
    issue_number: int,
    manifest_digest: str,
) -> PublicationOutcome:
    """Normalize an untrusted transport result into a bounded typed outcome.

    A response is accepted as published only when it binds the requested local
    repository, issue number, digest, and correlation key.  Unknown shapes are
    deliberately ambiguous rather than optimistic.
    """
    key = publication_key(repository, issue_number, manifest_digest)
    digest = _require_digest(manifest_digest)
    if not isinstance(value, Mapping):
        return PublicationOutcome("ambiguous", key, digest)
    raw_status = value.get("status")
    if not isinstance(raw_status, str) or raw_status not in _STATUS_MAP:
        return PublicationOutcome("ambiguous", key, digest)
    status = _STATUS_MAP[raw_status]
    if status not in {"published", "already_published"}:
        return PublicationOutcome(status, key, digest)
    if (
        value.get("repository") != repository
        or value.get("issue_number") != issue_number
        or value.get("manifest_digest") != digest
        or value.get("publication_key") != key
    ):
        return PublicationOutcome("deferred_wrong_identity", key, digest)
    comment_id = value.get("comment_id")
    if not isinstance(comment_id, str) or not _COMMENT_ID.fullmatch(comment_id):
        return PublicationOutcome("ambiguous", key, digest)
    return PublicationOutcome(status, key, digest, comment_id)


@dataclass(frozen=True)
class DryRunTransport:
    """A deterministic transport that never attempts publication."""

    def publish(
        self, repository: str, issue_number: int, manifest_digest: str, markdown: str
    ) -> PublicationOutcome:
        del markdown
        key = publication_key(repository, issue_number, manifest_digest)
        return PublicationOutcome("dry_run", key, manifest_digest)


@dataclass(frozen=True)
class MockTransport:
    """A deterministic no-I/O test transport returning a normalized raw result."""

    result: object

    def publish(
        self, repository: str, issue_number: int, manifest_digest: str, markdown: str
    ) -> PublicationOutcome:
        del markdown
        return normalize_outcome(
            self.result,
            repository=repository,
            issue_number=issue_number,
            manifest_digest=manifest_digest,
        )
