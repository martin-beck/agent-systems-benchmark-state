# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Pure, privacy-safe validation for versioned issue-to-AR series manifests.

This module deliberately has no filesystem, network, or coordinator-state
dependencies.  Callers may use a validated manifest as input to a later,
atomic publication transaction.
"""

from __future__ import annotations

import re
from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any, NoReturn

_REPOSITORY = re.compile(r"github\.com/[a-z0-9][a-z0-9_.-]*/[a-z0-9][a-z0-9_.-]*$")
_AR_ID = re.compile(r"AR-[0-9]{4}$")
_DIGEST = re.compile(r"sha256:[0-9a-f]{64}$")
_HOME_FRAGMENT = "/" + "home/"
_PRIVATE_TEXT = re.compile(
    r"(?:^|[\s'\"])(?:"
    + _HOME_FRAGMENT
    + r"|/tmp/|~[/\\]|file://)|"
    + r"(?:api[_ -]?key|access[_ -]?token|password|secret|private[_ -]?key|prompt)\b",
    re.IGNORECASE,
)
_TOP_LEVEL = frozenset(
    {"schema_version", "repository", "issue", "issue_digest", "members", "finalizer"}
)
_ISSUE = frozenset({"number", "url"})
_MEMBER = frozenset({"id", "short_title", "scope", "acceptance", "ownership", "depends_on"})
_DEPENDENCY = frozenset({"id", "rationale"})


class IssueSeriesValidationError(ValueError):
    """Raised when an issue-series manifest is not safe to publish."""


@dataclass(frozen=True)
class Dependency:
    """A locally explained edge in the proposed AR graph."""

    id: str
    rationale: str


@dataclass(frozen=True)
class Member:
    """A proposed AR with its bounded planning data."""

    id: str
    short_title: str
    scope: str
    acceptance: str
    ownership: str
    depends_on: tuple[Dependency, ...]


@dataclass(frozen=True)
class IssueSeriesManifest:
    """The normalized, validated data required for an atomic series create."""

    repository: str
    issue_number: int
    issue_url: str
    issue_digest: str
    members: tuple[Member, ...]
    finalizer: str


def _fail(message: str) -> NoReturn:
    raise IssueSeriesValidationError(message)


def _object(value: object, label: str, allowed: frozenset[str]) -> Mapping[str, Any]:
    if not isinstance(value, dict):
        _fail(f"{label} must be an object")
    keys = set(value)
    unknown = sorted(keys - allowed)
    missing = sorted(allowed - keys)
    if unknown:
        _fail(f"{label} has unknown fields: {', '.join(unknown)}")
    if missing:
        _fail(f"{label} is missing fields: {', '.join(missing)}")
    return value


def _text(value: object, label: str) -> str:
    if not isinstance(value, str) or not (text := value.strip()):
        _fail(f"{label} must be a non-empty string")
    if len(text) > 500:
        _fail(f"{label} exceeds 500 characters")
    if "\n" in text or "\r" in text:
        _fail(f"{label} must be a single line")
    if _PRIVATE_TEXT.search(text):
        _fail(f"{label} contains private or prompt-like text")
    return text


def _member(value: object, index: int) -> Member:
    item = _object(value, f"members[{index}]", _MEMBER)
    task_id = _text(item["id"], f"members[{index}].id")
    if not _AR_ID.fullmatch(task_id):
        _fail(f"members[{index}].id must be an AR identifier")
    dependencies = item["depends_on"]
    if not isinstance(dependencies, list):
        _fail(f"members[{index}].depends_on must be a list")
    parsed: list[Dependency] = []
    for dependency_index, dependency in enumerate(dependencies):
        edge = _object(dependency, f"members[{index}].depends_on[{dependency_index}]", _DEPENDENCY)
        dependency_id = _text(edge["id"], f"members[{index}].depends_on[{dependency_index}].id")
        if not _AR_ID.fullmatch(dependency_id):
            _fail(f"members[{index}].depends_on[{dependency_index}].id must be an AR identifier")
        parsed.append(
            Dependency(
                dependency_id,
                _text(
                    edge["rationale"],
                    f"members[{index}].depends_on[{dependency_index}].rationale",
                ),
            )
        )
    return Member(
        task_id,
        _short_title(item["short_title"], f"members[{index}].short_title"),
        _text(item["scope"], f"members[{index}].scope"),
        _text(item["acceptance"], f"members[{index}].acceptance"),
        _text(item["ownership"], f"members[{index}].ownership"),
        tuple(parsed),
    )


def _short_title(value: object, label: str) -> str:
    text = _text(value, label)
    if len(text.split()) > 4:
        _fail(f"{label} must contain at most four words")
    return text


def _edge_errors(members: tuple[Member, ...]) -> tuple[list[str], dict[str, tuple[str, ...]]]:
    identifiers = {member.id for member in members}
    errors: list[str] = []
    graph: dict[str, tuple[str, ...]] = {}
    for member in members:
        dependencies = tuple(edge.id for edge in member.depends_on)
        if len(set(dependencies)) != len(dependencies):
            errors.append(f"{member.id} has duplicate dependencies")
        if member.id in dependencies:
            errors.append(f"{member.id} depends on itself")
        errors.extend(
            f"{member.id} has missing dependency {item}"
            for item in dependencies
            if item not in identifiers
        )
        graph[member.id] = dependencies
    return errors, graph


def _cycle_errors(graph: Mapping[str, tuple[str, ...]]) -> list[str]:
    errors: list[str] = []

    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(identifier: str) -> None:
        if identifier in visited or identifier not in graph:
            return
        if identifier in visiting:
            errors.append(f"dependency cycle includes {identifier}")
            return
        visiting.add(identifier)
        for dependency in graph[identifier]:
            visit(dependency)
        visiting.remove(identifier)
        visited.add(identifier)

    for identifier in sorted(graph):
        visit(identifier)
    return errors


def _finalizer_errors(
    members: tuple[Member, ...], graph: Mapping[str, tuple[str, ...]], finalizer: str
) -> list[str]:
    required = {member.id for member in members if member.id != finalizer}
    direct = set(graph.get(finalizer, ()))
    errors = [
        f"finalizer {finalizer} must directly depend on {member_id}"
        for member_id in sorted(required - direct)
    ]
    reachable: set[str] = {finalizer}
    pending = [finalizer]
    while pending:
        current = pending.pop()
        for dependency in graph.get(current, ()):
            if dependency not in reachable:
                reachable.add(dependency)
                pending.append(dependency)
    errors.extend(
        f"{member.id} is orphaned from finalizer {finalizer}"
        for member in members
        if member.id not in reachable
    )
    return errors


def _graph_errors(members: tuple[Member, ...], finalizer: str) -> list[str]:
    errors, graph = _edge_errors(members)
    errors.extend(_cycle_errors(graph))
    errors.extend(_finalizer_errors(members, graph, finalizer))
    return errors


def _identity(manifest: Mapping[str, Any]) -> tuple[str, int, str, str]:
    repository = _text(manifest["repository"], "manifest.repository")
    if repository != repository.lower():
        _fail("manifest.repository must be normalized to lowercase")
    if not _REPOSITORY.fullmatch(repository):
        _fail("manifest.repository must be a normalized github.com owner/name identity")
    issue = _object(manifest["issue"], "manifest.issue", _ISSUE)
    number = issue["number"]
    if isinstance(number, bool) or not isinstance(number, int) or number < 1:
        _fail("manifest.issue.number must be a positive integer")
    url = _text(issue["url"], "manifest.issue.url")
    if url != f"https://{repository}/issues/{number}":
        _fail("manifest.issue.url must bind the normalized repository and immutable issue number")
    digest = _text(manifest["issue_digest"], "manifest.issue_digest")
    if not _DIGEST.fullmatch(digest):
        _fail("manifest.issue_digest must be a lowercase sha256 digest")
    return repository, number, url, digest


def _members(manifest: Mapping[str, Any]) -> tuple[tuple[Member, ...], str]:
    values = manifest["members"]
    if not isinstance(values, list) or not values:
        _fail("manifest.members must be a non-empty list")
    members = tuple(_member(member, index) for index, member in enumerate(values))
    identifiers = [member.id for member in members]
    if len(set(identifiers)) != len(identifiers):
        _fail("manifest.members contains duplicate AR identifiers")
    finalizer = _text(manifest["finalizer"], "manifest.finalizer")
    if finalizer not in identifiers:
        _fail("manifest.finalizer must identify exactly one member")
    if members[-1].id != finalizer:
        _fail("manifest.finalizer must be ordered after all members")
    return members, finalizer


def parse_manifest(value: object) -> IssueSeriesManifest:
    """Parse and validate a schema-version-one manifest without side effects."""
    manifest = _object(value, "manifest", _TOP_LEVEL)
    if manifest["schema_version"] != 1:
        _fail("manifest.schema_version must be 1")
    repository, number, url, digest = _identity(manifest)
    members, finalizer = _members(manifest)
    errors = _graph_errors(members, finalizer)
    if errors:
        _fail("; ".join(sorted(set(errors))))
    return IssueSeriesManifest(repository, number, url, digest, members, finalizer)
