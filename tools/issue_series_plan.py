# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Pure, deterministic planning receipts for local issue-series creation."""

from __future__ import annotations

import hashlib
import json
import re
from collections.abc import Iterable, Mapping
from pathlib import Path
from typing import NoReturn

try:
    from .issue_series import IssueSeriesManifest, IssueSeriesValidationError, parse_manifest
except ImportError:  # Executed as a vendored top-level handoffctl helper.
    from issue_series import (  # type: ignore[import-not-found,no-redef]
        IssueSeriesManifest,
        IssueSeriesValidationError,
        parse_manifest,
    )

_DIGEST = re.compile(r"sha256:[0-9a-f]{64}$")
_SLUG = re.compile(r"[a-z0-9][a-z0-9_.-]*/[a-z0-9][a-z0-9_.-]*$")


class IssueSeriesPlanError(ValueError):
    """Raised when a manifest cannot safely be planned against local state."""


def _fail(message: str) -> NoReturn:
    raise IssueSeriesPlanError(message)


def canonical_json(value: object) -> str:
    """Return the single canonical JSON representation used by plan receipts."""
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def _sha256(value: object) -> str:
    return f"sha256:{hashlib.sha256(canonical_json(value).encode()).hexdigest()}"


def _normalized_repository(slug: str) -> str:
    value = slug.strip().lower()
    if value.startswith("https://"):
        value = value.removeprefix("https://")
    if value.startswith("github.com/"):
        value = value.removeprefix("github.com/")
    if not _SLUG.fullmatch(value):
        _fail("expected product slug must be a GitHub owner/name")
    return f"github.com/{value}"


def _current_state_digest(value: str) -> str:
    if not isinstance(value, str) or not _DIGEST.fullmatch(value):
        _fail("current state digest must be a lowercase sha256 digest")
    return value


def load_manifest(path: Path) -> object:
    """Read and decode a caller-selected manifest without writing any files."""
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        _fail(f"manifest does not exist: {path}")
    except IsADirectoryError:
        _fail(f"manifest is not a file: {path}")
    except UnicodeDecodeError:
        _fail(f"manifest is not UTF-8: {path}")
    except json.JSONDecodeError:
        _fail(f"manifest is not valid JSON: {path}")
    except OSError:
        _fail(f"manifest cannot be read: {path}")


def _identity(value: object) -> tuple[str, int] | None:
    if not isinstance(value, Mapping):
        return None
    repository = value.get("repository")
    number = value.get("issue_number")
    issue = value.get("issue")
    if isinstance(issue, Mapping):
        number = issue.get("number", number)
    if not isinstance(repository, str) or isinstance(number, bool) or not isinstance(number, int):
        return None
    try:
        return _normalized_repository(repository), number
    except IssueSeriesPlanError:
        return None


def _manifest_payload(manifest: IssueSeriesManifest) -> dict[str, object]:
    return {
        "schema_version": 1,
        "repository": manifest.repository,
        "issue": {"number": manifest.issue_number, "url": manifest.issue_url},
        "issue_digest": manifest.issue_digest,
        "members": [
            {
                "id": member.id,
                "short_title": member.short_title,
                "scope": member.scope,
                "acceptance": member.acceptance,
                "ownership": member.ownership,
                "depends_on": [
                    {"id": dependency.id, "rationale": dependency.rationale}
                    for dependency in member.depends_on
                ],
            }
            for member in manifest.members
        ],
        "finalizer": manifest.finalizer,
    }


def plan_issue_series(
    manifest_path: Path,
    *,
    expected_product_slug: str,
    existing_task_ids: Iterable[str],
    existing_issue_series_identities: Iterable[object],
    current_state_digest: str,
) -> str:
    """Return a canonical, side-effect-free creation receipt for a manifest.

    The supplied task IDs and identities are snapshots owned by the caller.  A
    later mutator must repeat this preflight under its own write boundary.
    """
    raw_manifest = load_manifest(manifest_path)
    try:
        manifest = parse_manifest(raw_manifest)
    except IssueSeriesValidationError as error:
        _fail(str(error))
    expected_repository = _normalized_repository(expected_product_slug)
    if manifest.repository != expected_repository:
        _fail("manifest repository does not match expected product slug")
    task_ids = {identifier for identifier in existing_task_ids if isinstance(identifier, str)}
    collisions = sorted(task_ids.intersection(member.id for member in manifest.members))
    if collisions:
        _fail(f"manifest AR identifiers already exist: {', '.join(collisions)}")
    identity = (manifest.repository, manifest.issue_number)
    if any(candidate == identity for candidate in map(_identity, existing_issue_series_identities)):
        _fail("manifest issue identity already has a series")
    payload = _manifest_payload(manifest)
    receipt: dict[str, object] = {
        "schema_version": 1,
        "current_state_digest": _current_state_digest(current_state_digest),
        "manifest": payload,
        "manifest_digest": _sha256(payload),
        "series_identity": {
            "issue_number": manifest.issue_number,
            "repository": manifest.repository,
        },
        "task_ids": [member.id for member in manifest.members],
    }
    return canonical_json(receipt)
