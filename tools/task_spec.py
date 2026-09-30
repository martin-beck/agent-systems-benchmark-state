# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Strict, dependency-free validation for task specification records."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

EVIDENCE_CLASSES = frozenset(
    {"mechanical", "contract-test", "property-or-fuzz", "bounded-model", "environmental"}
)
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


def _tool_errors(value: dict[str, Any]) -> list[str]:
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
        unknown = sorted(set(evidence) - EVIDENCE_CLASSES)
        if unknown:
            errors.append("unknown evidence class: " + ", ".join(unknown))
    return errors


def spec_errors(value: object) -> list[str]:
    """Return deterministic errors for one task-spec record."""
    if not isinstance(value, dict):
        return ["spec must be an object"]
    return sorted(set(_identity_errors(value) + _collection_errors(value) + _tool_errors(value)))


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


def task_spec_errors(root: Path, meta: dict[str, Any]) -> list[str]:
    """Validate optional task metadata and its referenced local spec."""
    if "spec_ref" not in meta and "spec_revision" not in meta:
        return []
    task_id = str(meta.get("id", "task"))
    errors = _metadata_errors(task_id, meta)
    if errors:
        return errors
    spec_ref = str(meta["spec_ref"])
    value, load_errors = _load_spec(root, task_id, spec_ref)
    if load_errors:
        return load_errors
    errors.extend(f"{task_id}: {error}" for error in spec_errors(value))
    if isinstance(value, dict) and value.get("spec_revision") != meta.get("spec_revision"):
        errors.append(f"{task_id}: spec_revision does not match referenced spec")
    if isinstance(value, dict) and value.get("spec_ref") != spec_ref:
        errors.append(f"{task_id}: spec_ref does not match referenced spec")
    return sorted(set(errors))


def done_admission_error(root: Path, meta: dict[str, Any]) -> str | None:
    """Return a fail-closed error when a new ``done`` transition lacks proof."""
    errors = task_spec_errors(root, meta)
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
    if acceptance["evidence_class"] not in EVIDENCE_CLASSES:
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
