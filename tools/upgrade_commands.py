# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Fail-closed user-facing commands for typed coordinator upgrade contracts."""

from __future__ import annotations

import json
import os
import stat
from hashlib import sha256
from pathlib import Path
from typing import Any, NoReturn, cast

if __package__:
    from .runtime_bootstrap import ExpectedRuntimeIdentity, VerifiedManifest, run_selected_runtime
else:  # pragma: no cover - direct script execution
    from runtime_bootstrap import (  # type: ignore[import-not-found,no-redef]
        ExpectedRuntimeIdentity,
        VerifiedManifest,
        run_selected_runtime,
    )

if __package__:
    from .upgrade_binding import (
        LiveUpgradeBinding,
        UpgradeBindingError,
        UpgradeRuntimeBinding,
        canonical_contract_digest,
    )
    from .upgrade_contract_runtime import RuntimeContractError, validate_runtime_contract
else:  # pragma: no cover - direct script execution
    from upgrade_binding import (  # type: ignore[import-not-found,no-redef]
        LiveUpgradeBinding,
        UpgradeBindingError,
        UpgradeRuntimeBinding,
        canonical_contract_digest,
    )
    from upgrade_contract_runtime import (  # type: ignore[import-not-found,no-redef]
        RuntimeContractError,
        validate_runtime_contract,
    )

MAX_CONTRACT_BYTES = 1024 * 1024
READ_ONLY_ACTIONS = {"check", "plan"}
MUTATING_ACTIONS = {"apply", "rollback"}


class UpgradeCommandError(RuntimeError):
    """A requested upgrade command is invalid or not safely executable."""


def consume_selected_runtime_command(
    selector: Path,
    releases_root: Path,
    expected_identity: ExpectedRuntimeIdentity,
    manifest_digest: str,
    arguments: tuple[str, ...] = (),
) -> int:
    """Consume the selected runtime through the verified launcher boundary.

    This is the production read-only upgrade command path.  The caller supplies
    identity evidence and a selector/root, never a runtime or script path; the
    launcher owns resolution, revalidation, fixed-entrypoint selection, and
    read-only argument validation.
    """
    if len(manifest_digest) != 64 or any(
        character not in "0123456789abcdef" for character in manifest_digest
    ):
        raise UpgradeCommandError("runtime manifest digest is invalid")

    def verify_authenticity(
        runtime_root: Path, identity: ExpectedRuntimeIdentity
    ) -> VerifiedManifest:
        manifest = runtime_root / "runtime-manifest.json"
        try:
            digest = sha256(manifest.read_bytes()).hexdigest()
        except OSError as error:
            raise UpgradeCommandError("runtime manifest is unavailable") from error
        if digest != manifest_digest:
            raise UpgradeCommandError("runtime manifest digest does not match")
        return VerifiedManifest(
            release=runtime_root.name,
            identity=identity,
            digest=digest,
        )

    try:
        result = run_selected_runtime(
            selector,
            releases_root,
            expected_identity,
            verify_authenticity,
            arguments,
        )
    except Exception as error:
        if isinstance(error, UpgradeCommandError):
            raise
        raise UpgradeCommandError("selected runtime consumption failed") from error
    return result.returncode


def _strict_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    if len(pairs) != len({key for key, _ in pairs}):
        raise ValueError("duplicate JSON object key")
    return dict(pairs)


def _reject_constant(value: str) -> NoReturn:
    raise ValueError(f"non-finite JSON constant: {value}")


def _open_contract(path: Path) -> int:
    """Open a contract through directory fds so parent replacement cannot redirect it."""
    absolute = path.absolute()
    directory = -1
    try:
        directory = os.open(
            absolute.anchor,
            os.O_RDONLY | os.O_DIRECTORY | os.O_CLOEXEC,
        )
        for component in absolute.parts[1:-1]:
            next_directory = os.open(
                component,
                os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | os.O_CLOEXEC,
                dir_fd=directory,
            )
            os.close(directory)
            directory = next_directory
        descriptor = os.open(
            absolute.name,
            os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK | os.O_CLOEXEC,
            dir_fd=directory,
        )
    except OSError as error:
        raise UpgradeCommandError("upgrade contract is unavailable or unsafe") from error
    finally:
        if directory >= 0:
            os.close(directory)
    return descriptor


def _read_json_object(path: Path, label: str) -> dict[str, Any]:  # noqa: C901
    """Read one bounded regular JSON object without following its leaf symlink."""
    descriptor = -1
    try:
        descriptor = _open_contract(path)
        status = os.fstat(descriptor)
        if not stat.S_ISREG(status.st_mode) or status.st_nlink != 1:
            raise UpgradeCommandError("upgrade contract must be a single-link regular file")
        if status.st_size > MAX_CONTRACT_BYTES:
            raise UpgradeCommandError("upgrade contract exceeds the size limit")
        chunks: list[bytes] = []
        remaining = MAX_CONTRACT_BYTES + 1
        while remaining:
            chunk = os.read(descriptor, min(65536, remaining))
            if not chunk:
                break
            chunks.append(chunk)
            remaining -= len(chunk)
        if remaining == 0:
            raise UpgradeCommandError("upgrade contract exceeds the size limit")
    except OSError as error:
        raise UpgradeCommandError("upgrade contract is unavailable or unsafe") from error
    finally:
        if descriptor >= 0:
            os.close(descriptor)
    try:
        value = json.loads(
            b"".join(chunks).decode("utf-8"),
            object_pairs_hook=_strict_object,
            parse_constant=_reject_constant,
        )
    except (UnicodeDecodeError, ValueError) as error:
        raise UpgradeCommandError(f"{label} is not canonical JSON data") from error
    if not isinstance(value, dict):
        raise UpgradeCommandError(f"{label} must be an object")
    return cast(dict[str, Any], value)


def _read_contract(path: Path) -> dict[str, Any]:
    """Read one bounded regular contract without following its leaf symlink."""
    document = _read_json_object(path, "upgrade contract")
    try:
        validate_runtime_contract(document)
    except RuntimeContractError as error:
        raise UpgradeCommandError("upgrade contract validation failed") from error
    return document


def _read_runtime_binding(
    path: Path, contract: dict[str, Any], selected_backend: str
) -> UpgradeRuntimeBinding:
    document = _read_json_object(path, "upgrade runtime binding")
    try:
        binding = UpgradeRuntimeBinding.from_mapping(document)
        expected = UpgradeRuntimeBinding.bind(
            contract,
            binding.runtime_envelope,
            session_identity_digest=binding.session_identity_digest,
        )
    except UpgradeBindingError as error:
        raise UpgradeCommandError("upgrade runtime binding validation failed") from error
    if binding.as_mapping() != expected.as_mapping():
        raise UpgradeCommandError("upgrade runtime binding does not match contract")
    if binding.contract_digest != canonical_contract_digest(contract):
        raise UpgradeCommandError("upgrade runtime binding contract digest is stale")
    if binding.contract_backend != selected_backend:
        raise UpgradeCommandError("upgrade runtime binding backend does not match coordinator")
    return binding


def _validate_selected_backend(document: dict[str, Any], selected_backend: str) -> None:
    if selected_backend not in {"git", "sqlite"}:
        raise UpgradeCommandError("selected coordinator backend is unsupported")
    if document["backend"] != selected_backend:
        raise UpgradeCommandError("upgrade contract backend does not match coordinator backend")


def _summary(document: dict[str, Any], *, include_plan: bool) -> dict[str, object]:
    """Return a path-, fence-, and host-free deterministic contract projection."""
    result: dict[str, object] = {
        "schema_version": 1,
        "kind": "agent-workflow-coordinator-upgrade-contract-check",
        "contract_schema_version": document["schema_version"],
        "operation_id": document["operation_id"],
        "backend": document["backend"],
        "from_version": document["from"]["version"],
        "to_version": document["to"]["version"],
        "valid": True,
        "executable": False,
    }
    if include_plan:
        result["kind"] = "agent-workflow-coordinator-upgrade-contract-plan"
        result["phases"] = [
            {
                "id": phase["id"],
                "operation_id": phase["operation"]["operation_id"],
                "opcode": phase["operation"]["opcode"],
                "mutates_authority": phase["mutates_authority"],
            }
            for phase in document["phases"]
        ]
        result["rollback"] = {
            "operation_id": document["rollback"]["operation"]["operation_id"],
            "opcode": document["rollback"]["operation"]["opcode"],
        }
    return result


def execute_upgrade_command(
    action: str,
    contract_path: Path,
    selected_backend: str,
    binding_path: Path | None = None,
    live_binding: LiveUpgradeBinding | None = None,
) -> int:
    """Validate and report, while rejecting every unimplemented mutation path."""
    if action not in READ_ONLY_ACTIONS | MUTATING_ACTIONS:
        raise UpgradeCommandError("unknown upgrade action")
    document = _read_contract(contract_path)
    _validate_selected_backend(document, selected_backend)
    if action in MUTATING_ACTIONS:
        if action == "rollback":
            if binding_path is None:
                raise UpgradeCommandError(
                    "rollback requires a validated runtime binding; "
                    "no coordinator state was mutated"
                )
            runtime_binding = _read_runtime_binding(binding_path, document, selected_backend)
        else:
            runtime_binding = None
        if live_binding is None:
            raise UpgradeCommandError(
                "mutating upgrade actions require a live durable session/backend binding; "
                "no coordinator state was mutated"
            )
        if type(live_binding) is not LiveUpgradeBinding or not LiveUpgradeBinding.is_admitted(
            live_binding
        ):
            raise UpgradeCommandError(
                "mutating upgrade actions require a concrete live durable session/backend "
                "binding; no coordinator state was mutated"
            )
        if (
            live_binding.runtime.contract_digest != canonical_contract_digest(document)
            or live_binding.runtime.contract_backend != selected_backend
        ):
            raise UpgradeCommandError(
                "live durable session/backend binding does not match the contract; "
                "no coordinator state was mutated"
            )
        if runtime_binding is not None and live_binding.runtime != runtime_binding:
            raise UpgradeCommandError(
                "live durable session/backend binding does not match the runtime binding; "
                "no coordinator state was mutated"
            )
        raise UpgradeCommandError(
            "upgrade execution protocol is incomplete; no coordinator state was mutated"
        )
    print(
        json.dumps(
            _summary(document, include_plan=action == "plan"),
            ensure_ascii=True,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        )
    )
    return 0
