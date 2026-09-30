# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Stable, read-only resolution of the authenticated runtime selector."""

from __future__ import annotations

import json
import os
import re
import stat
import subprocess
import sys
from collections.abc import Callable, Sequence
from contextlib import suppress
from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path

if __package__:
    from .upgrade_authority import AuthorityError, read_runtime_selector
else:  # pragma: no cover - direct script execution
    from upgrade_authority import (  # type: ignore[import-not-found,no-redef]
        AuthorityError,
        read_runtime_selector,
    )

_RELEASE = re.compile(r"v[0-9]+\.[0-9]+\.[0-9]+\Z")
_DIGEST = re.compile(r"[0-9a-f]{64}\Z")
_OID = re.compile(r"[0-9a-f]{40}\Z")
_MAX_MANIFEST_BYTES = 16 * 1024 * 1024
_MANIFEST_FIELDS = {
    "release",
    "source_commit",
    "tag_ref",
    "tag_object",
    "signature_sha256",
    "trust_policy_sha256",
    "vendor_manifest_sha256",
}
_MANIFEST_ORDER = (
    "release",
    "source_commit",
    "tag_ref",
    "tag_object",
    "signature_sha256",
    "trust_policy_sha256",
    "vendor_manifest_sha256",
)
_READ_ONLY_RUNTIME_COMMANDS = {
    (),
    ("doctor",),
    ("doctor", "--live"),
    ("snapshot",),
    ("render-status",),
    ("render-status", "--check"),
}


@dataclass(frozen=True, slots=True)
class ExpectedRuntimeIdentity:
    """Caller-supplied identity facts validated independently."""

    source_commit: str
    tag_ref: str
    tag_object: str
    signature_sha256: str
    trust_policy_sha256: str
    vendor_manifest_sha256: str


@dataclass(frozen=True, slots=True)
class VerifiedManifest:
    """Manifest identity retained as one verification result."""

    release: str
    identity: ExpectedRuntimeIdentity
    digest: str


@dataclass(frozen=True, slots=True)
class DispatchAdmission:
    """Read-only admission evidence bound to one retained runtime handle."""

    runtime: ResolvedRuntime
    identity: VerifiedManifest

    def __post_init__(self) -> None:
        """Reject forged evidence pairs before they can reach a consumer."""
        runtime_candidate: object = self.runtime
        identity_candidate: object = self.identity
        runtime = runtime_candidate if isinstance(runtime_candidate, ResolvedRuntime) else None
        if (
            runtime is None
            or not isinstance(identity_candidate, VerifiedManifest)
            or not isinstance(identity_candidate.identity, ExpectedRuntimeIdentity)
            or _RELEASE.fullmatch(identity_candidate.release) is None
            or _DIGEST.fullmatch(identity_candidate.digest) is None
        ):
            if runtime is not None:
                runtime.close()
            raise AuthorityError("dispatch admission identity is not bound")
        if runtime.identity is not self.identity:
            runtime.close()
            raise AuthorityError("dispatch admission identity is not bound")

    def revalidate(self) -> None:
        """Recheck the retained handle before a consumer uses admission evidence."""
        runtime_candidate: object = self.runtime
        if not isinstance(runtime_candidate, ResolvedRuntime):
            raise AuthorityError("dispatch admission runtime is not retained")
        runtime = runtime_candidate
        try:
            identity_candidate: object = runtime.identity
            if (
                not isinstance(identity_candidate, VerifiedManifest)
                or identity_candidate is not self.identity
            ):
                raise AuthorityError("dispatch admission identity is not bound")
            runtime.revalidate_for_dispatch()
        except AuthorityError:
            runtime.close()
            raise

    def validate_identity(self, expected: VerifiedManifest) -> None:
        """Require the consumer's identity evidence to match this admission."""
        if not isinstance(expected, VerifiedManifest) or expected is not self.identity:
            self.runtime.close()
            raise AuthorityError("dispatch admission identity is not bound")
        self.revalidate()

    def close(self) -> None:
        """Release the retained runtime handle; repeated close is harmless."""
        runtime_candidate: object = self.runtime
        if not isinstance(runtime_candidate, ResolvedRuntime):
            raise AuthorityError("dispatch admission runtime is not retained")
        runtime_candidate.close()

    def __enter__(self) -> DispatchAdmission:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()


@dataclass(slots=True)
class AdmittedRuntimeCommand:
    """A fixed-entrypoint command retaining its descriptor-backed file handle.

    The command must be executed with ``subprocess`` using ``pass_fds``.  The
    entrypoint is addressed through its open descriptor, so replacing a path
    after admission cannot redirect the interpreter to another file.
    """

    argv: tuple[str, ...]
    pass_fds: tuple[int, ...]
    _entrypoint_descriptor: int
    environment: dict[str, str]

    def close(self) -> None:
        """Release the descriptor retained for the pending dispatch."""
        descriptor = self._entrypoint_descriptor
        self._entrypoint_descriptor = -1
        if descriptor >= 0:
            with suppress(OSError):
                os.close(descriptor)

    def __enter__(self) -> AdmittedRuntimeCommand:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()


def _open_fixed_entrypoint(runtime: ResolvedRuntime) -> int:
    """Open the release-owned launcher without following path aliases."""
    tools_descriptor = -1
    try:
        tools_descriptor = os.open(
            "tools", os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=runtime.descriptor
        )
        tools_status = os.fstat(tools_descriptor)
        if (
            not stat.S_ISDIR(tools_status.st_mode)
            or tools_status.st_uid != os.geteuid()
            or stat.S_IMODE(tools_status.st_mode) & 0o022
        ):
            raise AuthorityError("runtime entrypoint directory is unsafe")
        entrypoint = os.open("handoffctl.py", os.O_RDONLY | os.O_NOFOLLOW, dir_fd=tools_descriptor)
        status = os.fstat(entrypoint)
        if (
            not stat.S_ISREG(status.st_mode)
            or status.st_uid != os.geteuid()
            or status.st_nlink != 1
            or stat.S_IMODE(status.st_mode) & 0o022
            or not stat.S_IMODE(status.st_mode) & 0o100
        ):
            os.close(entrypoint)
            raise AuthorityError("runtime entrypoint is unsafe")
        return entrypoint
    except OSError as error:
        raise AuthorityError("runtime entrypoint is unavailable") from error
    finally:
        if tools_descriptor >= 0:
            with suppress(OSError):
                os.close(tools_descriptor)


def prepare_runtime_dispatch(
    admission: DispatchAdmission, arguments: Sequence[str] = ()
) -> AdmittedRuntimeCommand:
    """Bind caller arguments to the one authenticated coordinator entrypoint.

    ``arguments`` are passed after the fixed ``tools/handoffctl.py`` script;
    only the explicitly read-only coordinator commands are admitted. Callers
    cannot replace the interpreter, script, release, runtime path, or invoke
    a mutating coordinator command. The returned command retains an entrypoint
    descriptor and exposes it via ``pass_fds`` for an immediate subprocess
    invocation.
    """
    if not isinstance(admission, DispatchAdmission):
        raise AuthorityError("dispatch admission is not retained")
    if isinstance(arguments, (str, bytes, bytearray)) or not isinstance(arguments, Sequence):
        raise AuthorityError("dispatch arguments are invalid")
    normalized: list[str] = []
    for argument in arguments:
        if not isinstance(argument, str) or "\x00" in argument:
            raise AuthorityError("dispatch arguments are invalid")
        normalized.append(argument)
    if tuple(normalized) not in _READ_ONLY_RUNTIME_COMMANDS:
        raise AuthorityError("dispatch command is not read-only")
    admission.revalidate()
    entrypoint = _open_fixed_entrypoint(admission.runtime)
    try:
        admission.revalidate()
        argv = (sys.executable, f"/proc/self/fd/{entrypoint}", *normalized)
        environment = os.environ.copy()
        environment["PYTHONPATH"] = os.pathsep.join(
            (str(admission.runtime.path), str(admission.runtime.path / "tools"))
        )
        return AdmittedRuntimeCommand(argv, (entrypoint,), entrypoint, environment)
    except BaseException:
        with suppress(OSError):
            os.close(entrypoint)
        raise


def run_admitted_runtime(
    admission: DispatchAdmission,
    arguments: Sequence[str] = (),
    *,
    timeout: float | None = None,
) -> subprocess.CompletedProcess[str]:
    """Execute one fixed, explicitly read-only admitted launcher command.

    This invocation records no upgrade state and rejects mutating coordinator
    commands before subprocess creation. The descriptor-backed command is
    kept alive through ``subprocess.run`` and is closed on every outcome.
    """
    command = prepare_runtime_dispatch(admission, arguments)
    try:
        try:
            return subprocess.run(  # noqa: S603 - argv and descriptor are fixed by admission
                command.argv,
                check=False,
                stdin=subprocess.DEVNULL,
                capture_output=True,
                text=True,
                timeout=timeout,
                pass_fds=command.pass_fds,
                env=command.environment,
            )
        except subprocess.TimeoutExpired as error:
            raise AuthorityError("admitted runtime dispatch timed out") from error
        except OSError as error:
            raise AuthorityError("admitted runtime dispatch failed") from error
    finally:
        command.close()


def run_selected_runtime(
    selector: Path,
    releases_root: Path,
    expected_identity: ExpectedRuntimeIdentity,
    verify_authenticity: Callable[[Path, ExpectedRuntimeIdentity], VerifiedManifest],
    arguments: Sequence[str] = (),
    *,
    timeout: float | None = None,
) -> subprocess.CompletedProcess[str]:
    """Resolve, revalidate, and consume one selected runtime entrypoint.

    This is the production consumer boundary: callers provide a selector,
    authenticated expected identity, and read-only arguments, never a runtime
    or script path.  The retained admission is always closed after the child
    exits or fails.
    """
    resolved = resolve_selected_runtime_bound(
        selector, releases_root, expected_identity, verify_authenticity
    )
    try:
        admission = resolved.admit_for_dispatch()
    except BaseException:
        resolved.close()
        raise
    try:
        return run_admitted_runtime(admission, arguments, timeout=timeout)
    finally:
        admission.close()


@dataclass(slots=True)
class ResolvedRuntime:
    """Opaque descriptor-bound runtime result; dispatch is intentionally absent."""

    path: Path
    descriptor: int
    identity: VerifiedManifest
    _directory_identity: tuple[int, int, int, int, int]
    selector: Path
    _selector_file_identity: tuple[tuple[int, int], tuple[int, int]]
    _selector_value: dict[str, object]
    _manifest_file_identity: tuple[int, int]

    def revalidate(self) -> None:
        """Fail closed if the retained directory or its pathname was replaced."""
        if not isinstance(self.path, Path):
            raise AuthorityError("resolved runtime path is unavailable")
        if not isinstance(self.descriptor, int) or isinstance(self.descriptor, bool):
            raise AuthorityError("resolved runtime descriptor is unavailable")
        if self.descriptor < 0:
            raise AuthorityError("resolved runtime is unavailable")
        if not self.path.is_absolute():
            raise AuthorityError("resolved runtime path is unavailable")
        _require_no_symlink_ancestors(self.path.parent)
        directory_identity = self._directory_identity
        if (
            not isinstance(directory_identity, tuple)
            or len(directory_identity) != 5
            or any(
                not isinstance(value, int) or isinstance(value, bool)
                for value in directory_identity
            )
        ):
            raise AuthorityError("resolved runtime identity is unavailable")
        try:
            retained = os.fstat(self.descriptor)
            current = self.path.lstat()
        except OSError as error:
            raise AuthorityError("resolved runtime is unavailable") from error
        observed = (
            retained.st_dev,
            retained.st_ino,
            stat.S_IMODE(retained.st_mode),
            retained.st_uid,
            retained.st_nlink,
        )
        named = (
            current.st_dev,
            current.st_ino,
            stat.S_IMODE(current.st_mode),
            current.st_uid,
            current.st_nlink,
        )
        if (
            not stat.S_ISDIR(retained.st_mode)
            or not stat.S_ISDIR(current.st_mode)
            or observed != directory_identity
            or named != directory_identity
        ):
            raise AuthorityError("resolved runtime identity changed")

    def revalidate_manifest(self) -> None:
        """Recheck retained manifest bytes and identity before a future dispatch."""
        if not isinstance(self.identity, VerifiedManifest) or not isinstance(
            self.identity.identity, ExpectedRuntimeIdentity
        ):
            raise AuthorityError("resolved runtime identity is unavailable")
        expected_identity = self.identity.identity
        if not all(
            isinstance(value, str)
            for value in (
                expected_identity.source_commit,
                expected_identity.tag_ref,
                expected_identity.tag_object,
                expected_identity.signature_sha256,
                expected_identity.trust_policy_sha256,
                expected_identity.vendor_manifest_sha256,
            )
        ):
            raise AuthorityError("resolved runtime identity is unavailable")
        if (
            len(expected_identity.source_commit) != 40
            or any(c not in "0123456789abcdef" for c in expected_identity.source_commit)
            or len(expected_identity.tag_object) != 40
            or any(c not in "0123456789abcdef" for c in expected_identity.tag_object)
            or any(
                len(value) != 64 or any(c not in "0123456789abcdef" for c in value)
                for value in (
                    expected_identity.signature_sha256,
                    expected_identity.trust_policy_sha256,
                    expected_identity.vendor_manifest_sha256,
                )
            )
        ):
            raise AuthorityError("resolved runtime identity is unavailable")
        if not isinstance(self.identity.release, str):
            raise AuthorityError("resolved runtime release is unavailable")
        if (
            not isinstance(self.identity.digest, str)
            or len(self.identity.digest) != 64
            or any(character not in "0123456789abcdef" for character in self.identity.digest)
        ):
            raise AuthorityError("resolved runtime digest is unavailable")
        if (
            not isinstance(self._manifest_file_identity, tuple)
            or len(self._manifest_file_identity) != 2
            or any(
                not isinstance(value, int) or isinstance(value, bool)
                for value in self._manifest_file_identity
            )
        ):
            raise AuthorityError("resolved runtime manifest identity is unavailable")
        if _manifest_file_identity(self.path) != self._manifest_file_identity:
            raise AuthorityError("resolved runtime manifest identity changed")
        manifest = read_runtime_manifest(self.path)
        identity = ExpectedRuntimeIdentity(
            manifest["source_commit"],
            manifest["tag_ref"],
            manifest["tag_object"],
            manifest["signature_sha256"],
            manifest["trust_policy_sha256"],
            manifest["vendor_manifest_sha256"],
        )
        if manifest["release"] != self.identity.release or identity != self.identity.identity:
            raise AuthorityError("resolved runtime manifest identity changed")
        verify_runtime_manifest(
            self.path,
            self.identity.digest,
            expected_file_identity=self._manifest_file_identity,
        )

    def revalidate_selector(self) -> None:
        """Reject selector replacement after resolution and before admission."""
        _require_selector_unchanged(
            self.selector, self._selector_file_identity, self._selector_value
        )

    def revalidate_for_dispatch(self) -> None:
        """Run the complete retained identity gate before future dispatch."""
        self.revalidate()
        self.revalidate_selector()
        self.revalidate_manifest()

    def admit_for_dispatch(self) -> DispatchAdmission:
        """Return admission evidence only after the complete identity gate."""
        try:
            self.revalidate_for_dispatch()
        except AuthorityError:
            self.close()
            raise
        return DispatchAdmission(self, self.identity)

    def close(self) -> None:
        """Close the retained descriptor; no execution operation is exposed."""
        descriptor = self.descriptor
        self.descriptor = -1
        if not isinstance(descriptor, int) or isinstance(descriptor, bool) or descriptor < 0:
            return
        with suppress(OSError):
            os.close(descriptor)

    def __enter__(self) -> ResolvedRuntime:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()


def _selector_identity(selector: Path) -> tuple[tuple[int, int], tuple[int, int]]:
    """Capture selector parent and inode identity without following aliases."""
    try:
        parent = selector.parent.lstat()
        value = selector.lstat()
    except OSError as error:
        raise AuthorityError("runtime selector is unavailable") from error
    if not stat.S_ISDIR(parent.st_mode) or stat.S_ISLNK(parent.st_mode):
        raise AuthorityError("runtime selector parent is unsafe")
    if (
        not stat.S_ISREG(value.st_mode)
        or value.st_uid != os.geteuid()
        or value.st_nlink != 1
        or stat.S_IMODE(value.st_mode) != 0o600
    ):
        raise AuthorityError("runtime selector is unsafe")
    return (parent.st_dev, parent.st_ino), (value.st_dev, value.st_ino)


def _require_no_symlink_ancestors(
    root: Path, *, error_message: str = "resolved runtime ancestor changed"
) -> None:
    """Reject symlinked path ancestors before using a retained runtime path."""
    try:
        component = Path(root.anchor)
        for part in root.parts[1:]:
            component /= part
            if stat.S_ISLNK(component.lstat().st_mode):
                raise AuthorityError(error_message)
    except OSError as error:
        raise AuthorityError("resolved runtime ancestor is unavailable") from error


def _require_selector_unchanged(
    selector: Path,
    initial_identity: tuple[tuple[int, int], tuple[int, int]],
    initial_value: dict[str, object],
) -> None:
    """Reject selector replacement or content changes during validation."""
    try:
        final_identity = _selector_identity(selector)
        final_value = read_runtime_selector(selector)
    except AuthorityError as error:
        raise AuthorityError("runtime selector changed during validation") from error
    if final_identity != initial_identity or final_value != initial_value:
        raise AuthorityError("runtime selector changed during validation")


def _manifest_pairs(pairs: list[tuple[str, object]]) -> dict[str, object]:
    value = dict(pairs)
    if len(value) != len(pairs):
        raise AuthorityError("runtime manifest contains duplicate fields")
    return value


def _require_canonical_manifest(data: bytearray, parsed: object) -> None:
    """Require the exact serialized bytes for the validated manifest schema."""
    if not isinstance(parsed, dict):
        return
    canonical = json.dumps(
        {key: parsed[key] for key in _MANIFEST_ORDER}, separators=(",", ":")
    ).encode()
    if bytes(data) != canonical:
        raise AuthorityError("runtime manifest is not canonical")


def _manifest_file_identity(runtime_root: Path) -> tuple[int, int]:
    """Capture the private manifest inode identity without following aliases."""
    manifest = runtime_root / "runtime-manifest.json"
    try:
        value = manifest.lstat()
    except OSError as error:
        raise AuthorityError("runtime manifest is unavailable") from error
    if (
        not stat.S_ISREG(value.st_mode)
        or value.st_uid != os.geteuid()
        or value.st_nlink != 1
        or stat.S_IMODE(value.st_mode) != 0o600
    ):
        raise AuthorityError("runtime manifest is unsafe")
    return value.st_dev, value.st_ino


def _require_manifest_unchanged(
    runtime_root: Path, initial: dict[str, str], initial_file_identity: tuple[int, int]
) -> None:
    """Reject identity changes made while authenticity evidence was produced."""
    before = _manifest_file_identity(runtime_root)
    current = read_runtime_manifest(runtime_root)
    after = _manifest_file_identity(runtime_root)
    if before != initial_file_identity or after != initial_file_identity:
        raise AuthorityError("runtime manifest identity changed during verification")
    if current != initial:
        raise AuthorityError("runtime manifest identity does not match selected release")


def read_runtime_manifest(runtime_root: Path) -> dict[str, str]:
    """Read and strictly validate a runtime manifest through one descriptor."""
    manifest = runtime_root / "runtime-manifest.json"
    try:
        descriptor = os.open(manifest, os.O_RDONLY | os.O_NOFOLLOW)
        try:
            value = os.fstat(descriptor)
            if (
                not stat.S_ISREG(value.st_mode)
                or value.st_uid != os.geteuid()
                or value.st_nlink != 1
                or stat.S_IMODE(value.st_mode) != 0o600
            ):
                raise AuthorityError("runtime manifest is unsafe")
            data = bytearray()
            while chunk := os.read(descriptor, 65536):
                data.extend(chunk)
                if len(data) > _MAX_MANIFEST_BYTES:
                    raise AuthorityError("runtime manifest is too large")
        finally:
            os.close(descriptor)
    except OSError as error:
        raise AuthorityError("runtime manifest is unavailable") from error
    try:
        parsed = json.loads(bytes(data), object_pairs_hook=_manifest_pairs)
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise AuthorityError("runtime manifest JSON is invalid") from error
    if not isinstance(parsed, dict) or set(parsed) != _MANIFEST_FIELDS:
        raise AuthorityError("runtime manifest fields are invalid")
    if any(not isinstance(item, str) for item in parsed.values()):
        raise AuthorityError("runtime manifest identity is invalid")
    result = {key: str(parsed[key]) for key in _MANIFEST_FIELDS}
    if (
        _RELEASE.fullmatch(result["release"]) is None
        or result["tag_ref"] != f"refs/tags/{result['release']}"
        or _OID.fullmatch(result["source_commit"]) is None
        or _OID.fullmatch(result["tag_object"]) is None
        or any(
            _DIGEST.fullmatch(result[key]) is None
            for key in _MANIFEST_FIELDS - {"release", "source_commit", "tag_ref", "tag_object"}
        )
    ):
        raise AuthorityError("runtime manifest identity is invalid")
    _require_canonical_manifest(data, parsed)
    return result


def _require_expected_manifest_identity(
    value: os.stat_result, expected: tuple[int, int] | None
) -> None:
    """Bind a verifier open to the identity captured at admission."""
    if expected is not None and (value.st_dev, value.st_ino) != expected:
        raise AuthorityError("runtime manifest identity changed")


def verify_runtime_manifest(
    runtime_root: Path,
    expected_digest: str,
    *,
    expected_file_identity: tuple[int, int] | None = None,
) -> bool:
    """Verify the owner-only manifest digest for one staged runtime."""
    if not isinstance(expected_digest, str) or _DIGEST.fullmatch(expected_digest) is None:
        raise AuthorityError("runtime manifest digest is invalid")
    manifest = runtime_root / "runtime-manifest.json"
    try:
        parent_before = manifest.parent.lstat()
        value = manifest.lstat()
        if (
            not stat.S_ISREG(value.st_mode)
            or value.st_uid != os.geteuid()
            or value.st_nlink != 1
            or stat.S_IMODE(value.st_mode) != 0o600
        ):
            raise AuthorityError("runtime manifest is unsafe")
        _require_expected_manifest_identity(value, expected_file_identity)
        descriptor = os.open(manifest, os.O_RDONLY | os.O_NOFOLLOW)
        try:
            opened = os.fstat(descriptor)
            if (
                (opened.st_dev, opened.st_ino) != (value.st_dev, value.st_ino)
                or opened.st_uid != os.geteuid()
                or stat.S_IMODE(opened.st_mode) != 0o600
                or opened.st_nlink != 1
            ):
                raise AuthorityError("runtime manifest identity changed")
            hasher = sha256()
            total = 0
            while chunk := os.read(descriptor, 65536):
                total += len(chunk)
                if total > _MAX_MANIFEST_BYTES:
                    raise AuthorityError("runtime manifest is too large")
                hasher.update(chunk)
            digest = hasher.hexdigest()
        finally:
            os.close(descriptor)
        parent_after = manifest.parent.lstat()
        if (parent_before.st_dev, parent_before.st_ino) != (
            parent_after.st_dev,
            parent_after.st_ino,
        ):
            raise AuthorityError("runtime manifest parent identity changed")
    except OSError as error:
        raise AuthorityError("runtime manifest is unavailable") from error
    if digest != expected_digest:
        raise AuthorityError("runtime manifest digest does not match")
    return True


def _release_path(root: Path, release: str) -> Path:
    try:
        _require_no_symlink_ancestors(root, error_message="runtime release root contains a symlink")
        root_stat = root.stat()
        release_path = root / release
        value = release_path.lstat()
    except OSError as error:
        raise AuthorityError("selected runtime release is unavailable") from error
    if (
        not stat.S_ISDIR(root_stat.st_mode)
        or root_stat.st_uid != os.geteuid()
        or stat.S_IMODE(root_stat.st_mode) != 0o700
        or not stat.S_ISDIR(value.st_mode)
        or value.st_uid != os.geteuid()
        or stat.S_IMODE(value.st_mode) != 0o700
    ):
        raise AuthorityError("selected runtime release is unsafe")
    return release_path


def resolve_selected_runtime(
    selector: Path,
    releases_root: Path,
    expected_identity: ExpectedRuntimeIdentity | None = None,
    verify_authenticity: Callable[[Path, ExpectedRuntimeIdentity], VerifiedManifest] | None = None,
) -> Path:
    """Resolve one selected release without executing or mutating anything.

    The selector and release directory must be owner-only regular objects.  A
    release token is bounded to one direct child of ``releases_root``; symlink
    and hard-link aliases are rejected before a caller can execute the result.
    """
    selector_identity = _selector_identity(selector)
    selected = read_runtime_selector(selector)
    if expected_identity is None or verify_authenticity is None:
        raise AuthorityError("runtime authenticity verifier and expected identity are required")
    release = selected["active_release"]
    if not isinstance(release, str) or _RELEASE.fullmatch(release) is None:
        raise AuthorityError("runtime selector release identity is invalid")
    root = releases_root.absolute()
    release_path = _release_path(root, release)
    manifest = read_runtime_manifest(release_path)
    manifest_file_identity = _manifest_file_identity(release_path)
    if manifest["release"] != release:
        raise AuthorityError("runtime manifest release does not match selector")
    manifest_identity = ExpectedRuntimeIdentity(
        source_commit=manifest["source_commit"],
        tag_ref=manifest["tag_ref"],
        tag_object=manifest["tag_object"],
        signature_sha256=manifest["signature_sha256"],
        trust_policy_sha256=manifest["trust_policy_sha256"],
        vendor_manifest_sha256=manifest["vendor_manifest_sha256"],
    )
    if manifest_identity != expected_identity:
        raise AuthorityError("runtime manifest identity does not match expected identity")
    try:
        verified = verify_authenticity(release_path, expected_identity)
    except Exception as error:
        raise AuthorityError("runtime authenticity verification failed") from error
    if (
        not isinstance(verified, VerifiedManifest)
        or verified.release != release
        or verified.identity is not expected_identity
        or _DIGEST.fullmatch(verified.digest) is None
    ):
        raise AuthorityError("runtime authenticity evidence is not bound to selected release")
    _require_manifest_unchanged(release_path, manifest, manifest_file_identity)
    verify_runtime_manifest(
        release_path, verified.digest, expected_file_identity=manifest_file_identity
    )
    _require_selector_unchanged(selector, selector_identity, selected)
    return release_path


def resolve_selected_runtime_bound(  # noqa: C901
    selector: Path,
    releases_root: Path,
    expected_identity: ExpectedRuntimeIdentity,
    verify_authenticity: Callable[[Path, ExpectedRuntimeIdentity], VerifiedManifest],
) -> ResolvedRuntime:
    """Resolve and retain the selected release directory without dispatching it."""
    selector_identity = _selector_identity(selector)
    selected = read_runtime_selector(selector)
    release = selected["active_release"]
    if not isinstance(release, str) or _RELEASE.fullmatch(release) is None:
        raise AuthorityError("runtime selector release identity is invalid")
    release_path = _release_path(releases_root.absolute(), release)
    try:
        descriptor = os.open(release_path, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
        status = os.fstat(descriptor)
        directory_identity = (
            status.st_dev,
            status.st_ino,
            stat.S_IMODE(status.st_mode),
            status.st_uid,
            status.st_nlink,
        )
        if (
            not stat.S_ISDIR(status.st_mode)
            or directory_identity[2] != 0o700
            or directory_identity[3] != os.geteuid()
        ):
            raise AuthorityError("selected runtime release is unsafe")
        manifest = read_runtime_manifest(release_path)
        manifest_file_identity = _manifest_file_identity(release_path)
        if manifest["release"] != release:
            raise AuthorityError("runtime manifest release does not match selector")
        manifest_identity = ExpectedRuntimeIdentity(
            manifest["source_commit"],
            manifest["tag_ref"],
            manifest["tag_object"],
            manifest["signature_sha256"],
            manifest["trust_policy_sha256"],
            manifest["vendor_manifest_sha256"],
        )
        if manifest_identity != expected_identity:
            raise AuthorityError("runtime manifest identity does not match expected identity")
        try:
            verified = verify_authenticity(release_path, expected_identity)
        except OSError:
            raise
        except Exception as error:
            raise AuthorityError("runtime authenticity verification failed") from error
        if (
            not isinstance(verified, VerifiedManifest)
            or verified.release != release
            or verified.identity is not expected_identity
            or _DIGEST.fullmatch(verified.digest) is None
        ):
            raise AuthorityError("runtime authenticity evidence is not bound to selected release")
        _require_manifest_unchanged(release_path, manifest, manifest_file_identity)
        verify_runtime_manifest(
            release_path, verified.digest, expected_file_identity=manifest_file_identity
        )
        result = ResolvedRuntime(
            release_path,
            descriptor,
            verified,
            directory_identity,
            selector,
            selector_identity,
            dict(selected),
            manifest_file_identity,
        )
        result.revalidate()
        _require_selector_unchanged(selector, selector_identity, selected)
        return result
    except AuthorityError:
        if "descriptor" in locals():
            with suppress(OSError):
                os.close(descriptor)
        raise
    except OSError as error:
        if "descriptor" in locals():
            with suppress(OSError):
                os.close(descriptor)
        raise AuthorityError("resolved runtime is unavailable") from error
    except Exception as error:
        if "descriptor" in locals():
            with suppress(OSError):
                os.close(descriptor)
        raise AuthorityError("resolved runtime verification failed") from error
    except BaseException:
        if "descriptor" in locals():
            with suppress(OSError):
                os.close(descriptor)
        raise
