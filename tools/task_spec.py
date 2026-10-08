# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Strict, dependency-free validation for task specification records."""

from __future__ import annotations

import hashlib
import json
import os
import re
import stat
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any

EVIDENCE_CLASSES = frozenset(
    {"mechanical", "contract-test", "property-or-fuzz", "bounded-model", "environmental"}
)
POLICY_NAME = "task-spec-policy.json"
POLICY_MAX_BYTES = 4096
POLICY_MAX_CLASSES = 32
POLICY_CLASS = re.compile(r"^[a-z]+(?:-[a-z]+)*$")
SPEC_REF = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._/-]{2,255}$")
TOOL_REF = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:/-]{0,127}$")
ID_REF = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{2,63}$")
EVIDENCE_REF = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:/-]{2,255}$")
DIGEST = re.compile(r"^sha256:[0-9a-f]{64}$")
SPEC_FIELDS = {
    "schema_version",
    "spec_ref",
    "spec_revision",
    "acceptance_predicates",
    "definition_of_done",
    "inputs",
    "outputs",
    "allowed_tools",
    "forbidden_tools",
    "required_evidence_classes",
    "gates",
}


class TaskSpecPolicyError(RuntimeError):
    """A project task-spec policy is missing integrity or has invalid content."""


@dataclass(frozen=True)
class EvidencePolicy:
    """One immutable state-root-bound evidence vocabulary snapshot."""

    classes: frozenset[str]
    digest: str
    identity: tuple[int, int] | None
    present: bool


DEFAULT_EVIDENCE_POLICY = EvidencePolicy(EVIDENCE_CLASSES, "absent", None, False)


def _index_matches_head(root: Path, commit_id: str) -> bool:
    """Bind the sole stage-0 index entry to the exact commit blob and mode."""
    tree = subprocess.run(  # noqa: S603 - exact commit and fixed Git executable
        ["/usr/bin/git", "-C", str(root), "ls-tree", "-z", commit_id, "--", POLICY_NAME],
        check=False,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        timeout=10,
    )
    index = subprocess.run(  # noqa: S603 - fixed Git executable and bounded path
        ["/usr/bin/git", "-C", str(root), "ls-files", "-s", "-z", "--", POLICY_NAME],
        check=False,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        timeout=10,
    )
    if tree.returncode != 0 or index.returncode != 0:
        return False
    try:
        tree_metadata, tree_name = tree.stdout.removesuffix(b"\0").split(b"\t", 1)
        tree_mode, object_type, tree_blob = tree_metadata.split()
        index_metadata, index_name = index.stdout.removesuffix(b"\0").split(b"\t", 1)
        index_mode, index_blob, stage = index_metadata.split()
    except ValueError:
        return False
    return (
        object_type == b"blob"
        and stage == b"0"
        and tree_name == index_name == POLICY_NAME.encode("ascii")
        and tree_mode == index_mode
        and tree_blob == index_blob
        and re.fullmatch(rb"[0-9a-f]{40,64}", tree_blob) is not None
    )


def _tracked_clean_policy(root: Path, expected_payload: bytes | None = None) -> bool:
    """Require the opt-in policy bytes to equal one exact, clean HEAD blob."""
    try:
        commit = subprocess.run(  # noqa: S603 - fixed Git executable and bounded arguments
            ["/usr/bin/git", "-C", str(root), "rev-parse", "--verify", "HEAD^{commit}"],
            check=False,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            timeout=10,
        )
        commit_id = commit.stdout.strip()
        if commit.returncode != 0 or re.fullmatch(rb"[0-9a-f]{40,64}", commit_id) is None:
            return False
        object_name = commit_id.decode("ascii") + ":" + POLICY_NAME
        size = subprocess.run(  # noqa: S603 - immutable object selected by exact commit
            ["/usr/bin/git", "-C", str(root), "cat-file", "-s", object_name],
            check=False,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            timeout=10,
        )
        if size.returncode != 0:
            return False
        blob_size = int(size.stdout.strip())
        if blob_size < 2 or blob_size > POLICY_MAX_BYTES:
            return False
        blob = subprocess.run(  # noqa: S603 - size-bounded immutable Git object
            ["/usr/bin/git", "-C", str(root), "cat-file", "blob", object_name],
            check=False,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            timeout=10,
        )
        if blob.returncode != 0 or len(blob.stdout) != blob_size:
            return False
        if expected_payload is not None and blob.stdout != expected_payload:
            return False
        if not _index_matches_head(root, commit_id.decode("ascii")):
            return False
        commands = (
            [
                "/usr/bin/git",
                "-C",
                str(root),
                "diff",
                "--quiet",
                "--",
                POLICY_NAME,
            ],
            [
                "/usr/bin/git",
                "-C",
                str(root),
                "diff",
                "--cached",
                "--quiet",
                commit_id.decode("ascii"),
                "--",
                POLICY_NAME,
            ],
        )
        clean = all(
            subprocess.run(  # noqa: S603 - fixed Git executable and bounded arguments
                command,
                check=False,
                stdin=subprocess.DEVNULL,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                timeout=10,
            ).returncode
            == 0
            for command in commands
        )
        return clean and _index_matches_head(root, commit_id.decode("ascii"))
    except (OSError, ValueError, subprocess.SubprocessError):
        return False


def _head_tracks_policy(root: Path) -> bool:
    """Return whether the bound repository committed an opt-in policy."""
    if not (root / ".git").exists():
        return False
    try:
        return (
            subprocess.run(  # noqa: S603 - fixed Git executable and bounded arguments
                ["/usr/bin/git", "-C", str(root), "cat-file", "-e", f"HEAD:{POLICY_NAME}"],
                check=False,
                stdin=subprocess.DEVNULL,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                timeout=10,
            ).returncode
            == 0
        )
    except (OSError, subprocess.SubprocessError):
        return False


def evidence_policy(root: Path) -> EvidencePolicy:  # noqa: C901
    """Load the only supported additive vocabulary from the bound state root."""
    directory = -1
    descriptor = -1
    try:
        directory = os.open(root, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
        try:
            descriptor = os.open(POLICY_NAME, os.O_RDONLY | os.O_NOFOLLOW, dir_fd=directory)
        except FileNotFoundError:
            if _head_tracks_policy(root):
                raise TaskSpecPolicyError(
                    "task-spec policy must be tracked and unchanged"
                ) from None
            return DEFAULT_EVIDENCE_POLICY
        except OSError as error:
            raise TaskSpecPolicyError("task-spec policy is unreadable") from error
        before = os.fstat(descriptor)
        if (
            not stat.S_ISREG(before.st_mode)
            or before.st_nlink != 1
            or before.st_uid != os.geteuid()
            or stat.S_IMODE(before.st_mode) & 0o002
            or before.st_size < 2
            or before.st_size > POLICY_MAX_BYTES
        ):
            raise TaskSpecPolicyError("task-spec policy has unsafe identity or size")
        payload = os.read(descriptor, POLICY_MAX_BYTES + 1)
        after = os.fstat(descriptor)
        current = os.stat(POLICY_NAME, dir_fd=directory, follow_symlinks=False)
        identity = (before.st_dev, before.st_ino)
        if (
            len(payload) > POLICY_MAX_BYTES
            or (after.st_dev, after.st_ino) != identity
            or (current.st_dev, current.st_ino) != identity
            or current.st_size != len(payload)
        ):
            raise TaskSpecPolicyError("task-spec policy identity changed while reading")
        if not _tracked_clean_policy(root, payload):
            raise TaskSpecPolicyError("task-spec policy must be tracked and unchanged")
        final_descriptor = os.fstat(descriptor)
        final_entry = os.stat(POLICY_NAME, dir_fd=directory, follow_symlinks=False)
        if (
            (final_descriptor.st_dev, final_descriptor.st_ino) != identity
            or (final_entry.st_dev, final_entry.st_ino) != identity
            or final_descriptor.st_size != len(payload)
            or final_entry.st_size != len(payload)
            or os.pread(descriptor, POLICY_MAX_BYTES + 1, 0) != payload
        ):
            raise TaskSpecPolicyError("task-spec policy identity changed during Git verification")
    except TaskSpecPolicyError:
        raise
    except OSError as error:
        raise TaskSpecPolicyError("task-spec policy root is unavailable") from error
    finally:
        if descriptor >= 0:
            os.close(descriptor)
        if directory >= 0:
            os.close(directory)
    try:
        value = json.loads(payload.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise TaskSpecPolicyError("task-spec policy is not valid UTF-8 JSON") from error
    if (
        not isinstance(value, dict)
        or set(value) != {"schema_version", "additional_evidence_classes"}
        or value.get("schema_version") != 1
    ):
        raise TaskSpecPolicyError("task-spec policy shape or version is invalid")
    additions = value.get("additional_evidence_classes")
    if (
        not isinstance(additions, list)
        or not additions
        or len(additions) > POLICY_MAX_CLASSES
        or any(
            not isinstance(item, str)
            or len(item.encode("utf-8")) > 32
            or POLICY_CLASS.fullmatch(item) is None
            for item in additions
        )
    ):
        raise TaskSpecPolicyError("task-spec policy evidence classes are invalid")
    if len(set(additions)) != len(additions):
        raise TaskSpecPolicyError("task-spec policy evidence classes contain duplicates")
    if set(additions) & EVIDENCE_CLASSES:
        raise TaskSpecPolicyError("task-spec policy evidence classes collide with built-ins")
    return EvidencePolicy(
        EVIDENCE_CLASSES | frozenset(additions),
        hashlib.sha256(payload).hexdigest(),
        identity,
        True,
    )


def task_spec_policy_errors(root: Path) -> list[str]:
    """Return one bounded public-safe project-policy diagnostic."""
    try:
        evidence_policy(root)
    except TaskSpecPolicyError as error:
        return [str(error)]
    return []


def require_policy_unchanged(root: Path, expected: EvidencePolicy) -> None:
    """Reject a policy removal, replacement, or edit during an operation."""
    try:
        current = evidence_policy(root)
    except TaskSpecPolicyError as error:
        raise TaskSpecPolicyError("task-spec policy changed during operation") from error
    if current != expected:
        raise TaskSpecPolicyError("task-spec policy changed during operation")


def _strings(
    value: object, *, field: str, pattern: re.Pattern[str], allow_empty: bool = False
) -> list[str]:
    if not isinstance(value, list) or (not value and not allow_empty):
        return [f"{field} must be a non-empty array"]
    errors = [
        f"{field} contains an invalid value"
        for item in value
        if not isinstance(item, str) or not pattern.fullmatch(item)
    ]
    if len(set(value)) != len(value):
        errors.append(f"{field} must not contain duplicates")
    return errors


def _named_items(value: object, *, field: str) -> list[str]:
    if not isinstance(value, list) or not value:
        return [f"{field} must be a non-empty array"]
    errors: list[str] = []
    identifiers: list[str] = []
    for item in value:
        if not isinstance(item, dict) or set(item) != {"id", "description"}:
            errors.append(f"{field} items must contain only id and description")
            continue
        identifier, description = item["id"], item["description"]
        if not isinstance(identifier, str) or not ID_REF.fullmatch(identifier):
            errors.append(f"{field} has an invalid id")
        else:
            identifiers.append(identifier)
        if not isinstance(description, str) or not description.strip():
            errors.append(f"{field} has an invalid description")
    if len(set(identifiers)) != len(identifiers):
        errors.append(f"{field} ids must be unique")
    return errors


def _identity_errors(value: dict[str, Any]) -> list[str]:
    errors = [f"spec contains unknown field: {field}" for field in set(value) - SPEC_FIELDS]
    errors.extend(f"spec missing field: {field}" for field in sorted(SPEC_FIELDS - set(value)))
    if value.get("schema_version") != 1:
        errors.append("spec schema_version must be 1")
    if not isinstance(value.get("spec_ref"), str) or not SPEC_REF.fullmatch(
        str(value.get("spec_ref", ""))
    ):
        errors.append("spec_ref is invalid")
    revision = value.get("spec_revision")
    if not isinstance(revision, int) or isinstance(revision, bool) or revision < 1:
        errors.append("spec_revision must be a positive integer")
    return errors


def _collection_errors(value: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    errors.extend(_named_items(value.get("acceptance_predicates"), field="acceptance_predicates"))
    errors.extend(
        _strings(
            value.get("definition_of_done"),
            field="definition_of_done",
            pattern=re.compile(r"^.{1,1000}$"),
        )
    )
    errors.extend(_named_items(value.get("inputs"), field="inputs"))
    errors.extend(_named_items(value.get("outputs"), field="outputs"))
    errors.extend(_named_items(value.get("gates"), field="gates"))
    return errors


def _tool_errors(value: dict[str, Any], evidence_classes: frozenset[str]) -> list[str]:
    errors = [
        *_strings(value.get("allowed_tools"), field="allowed_tools", pattern=TOOL_REF),
        *_strings(
            value.get("forbidden_tools"),
            field="forbidden_tools",
            pattern=TOOL_REF,
            allow_empty=True,
        ),
    ]
    allowed = [item for item in value.get("allowed_tools", []) if isinstance(item, str)]
    forbidden = [item for item in value.get("forbidden_tools", []) if isinstance(item, str)]
    overlap = sorted(set(allowed) & set(forbidden))
    if overlap:
        errors.append("allowed_tools and forbidden_tools overlap: " + ", ".join(overlap))
    evidence = value.get("required_evidence_classes")
    errors.extend(
        _strings(evidence, field="required_evidence_classes", pattern=re.compile(r"^[a-z][a-z-]+$"))
    )
    if isinstance(evidence, list):
        unknown = sorted(set(evidence) - evidence_classes)
        if unknown:
            errors.append("unknown evidence class: " + ", ".join(unknown))
    return errors


def spec_errors(value: object, evidence_classes: frozenset[str] = EVIDENCE_CLASSES) -> list[str]:
    """Return deterministic errors for one task-spec record."""
    if not isinstance(value, dict):
        return ["spec must be an object"]
    return sorted(
        set(
            _identity_errors(value)
            + _collection_errors(value)
            + _tool_errors(value, evidence_classes)
        )
    )


def _metadata_errors(task_id: str, meta: dict[str, Any]) -> list[str]:
    if "spec_ref" not in meta or not isinstance(meta.get("spec_ref"), str):
        return [f"{task_id}: spec_ref is required"]
    revision = meta.get("spec_revision")
    if (
        "spec_revision" not in meta
        or not isinstance(revision, int)
        or isinstance(revision, bool)
        or revision < 1
    ):
        return [f"{task_id}: spec_revision must be a positive integer"]
    return []


def _load_spec(root: Path, task_id: str, spec_ref: str) -> tuple[object | None, list[str]]:
    if not SPEC_REF.fullmatch(spec_ref) or spec_ref.startswith(".") or ".." in Path(spec_ref).parts:
        return None, [f"{task_id}: spec_ref is unsafe"]
    try:
        return json.loads((root / spec_ref).read_text(encoding="utf-8")), []
    except (OSError, json.JSONDecodeError) as error:
        return None, [f"{task_id}: cannot read spec_ref: {error}"]


def task_spec_errors(
    root: Path, meta: dict[str, Any], policy: EvidencePolicy | None = None
) -> list[str]:
    """Validate optional task metadata and its referenced local spec."""
    if "spec_ref" not in meta and "spec_revision" not in meta:
        return []
    task_id = str(meta.get("id", "task"))
    try:
        selected_policy = policy or evidence_policy(root)
    except TaskSpecPolicyError as error:
        return [f"{task_id}: {error}"]
    errors = _metadata_errors(task_id, meta)
    if errors:
        return errors
    spec_ref = str(meta["spec_ref"])
    value, load_errors = _load_spec(root, task_id, spec_ref)
    if load_errors:
        return load_errors
    errors.extend(f"{task_id}: {error}" for error in spec_errors(value, selected_policy.classes))
    if isinstance(value, dict) and value.get("spec_revision") != meta.get("spec_revision"):
        errors.append(f"{task_id}: spec_revision does not match referenced spec")
    if isinstance(value, dict) and value.get("spec_ref") != spec_ref:
        errors.append(f"{task_id}: spec_ref does not match referenced spec")
    return sorted(set(errors))


def done_admission_error(  # noqa: C901
    root: Path, meta: dict[str, Any], policy: EvidencePolicy | None = None
) -> str | None:
    """Return a fail-closed error when a new ``done`` transition lacks proof."""
    try:
        selected_policy = policy or evidence_policy(root)
    except TaskSpecPolicyError as error:
        return f"done admission denied: {error}"
    errors = task_spec_errors(root, meta, selected_policy)
    if errors:
        return "done admission denied: " + "; ".join(errors)
    acceptance = meta.get("spec_acceptance")
    required = {
        "spec_ref",
        "spec_revision",
        "status",
        "evidence_class",
        "evidence_ref",
        "evidence_digest",
    }
    if not isinstance(acceptance, dict) or set(acceptance) != required:
        return "done admission denied: spec_acceptance is incomplete or unknown"
    if acceptance["spec_ref"] != meta.get("spec_ref"):
        return "done admission denied: acceptance spec_ref does not match task spec"
    if acceptance["spec_revision"] != meta.get("spec_revision"):
        return "done admission denied: acceptance spec_revision does not match task spec"
    if acceptance["status"] != "pass":
        return "done admission denied: acceptance status is not pass"
    if acceptance["evidence_class"] not in selected_policy.classes:
        return "done admission denied: acceptance evidence class is unknown"
    if not isinstance(acceptance["evidence_ref"], str) or not EVIDENCE_REF.fullmatch(
        acceptance["evidence_ref"]
    ):
        return "done admission denied: acceptance evidence ref is invalid"
    if not isinstance(acceptance["evidence_digest"], str) or not DIGEST.fullmatch(
        acceptance["evidence_digest"]
    ):
        return "done admission denied: acceptance evidence digest is invalid"
    return None
