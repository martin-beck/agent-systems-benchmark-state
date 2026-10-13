# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Downstream-only validation and descriptor-lifecycle coverage for bootstrap."""

from __future__ import annotations

import os
import tempfile
import unittest
from hashlib import sha256
from pathlib import Path
from unittest.mock import patch

from tools.runtime_bootstrap import (
    ExpectedRuntimeIdentity,
    ResolvedRuntime,
    VerifiedManifest,
    _open_fixed_entrypoint,
    read_runtime_manifest,
    resolve_selected_runtime_bound,
    verify_runtime_manifest,
)
from tools.upgrade_authority import AuthorityError, commit_runtime_selector


class RuntimeBootstrapValidationLifecycleTests(unittest.TestCase):
    @staticmethod
    def _identity() -> ExpectedRuntimeIdentity:
        return ExpectedRuntimeIdentity(
            source_commit="a" * 40,
            tag_ref="refs/tags/v1.2.3",
            tag_object="b" * 40,
            signature_sha256="c" * 64,
            trust_policy_sha256="d" * 64,
            vendor_manifest_sha256="e" * 64,
        )

    @classmethod
    def _runtime(cls, root: Path) -> tuple[Path, Path, Path, ExpectedRuntimeIdentity]:
        releases = root / "releases"
        releases.mkdir(mode=0o700)
        release = releases / "v1.2.3"
        release.mkdir(mode=0o700)
        manifest = (
            '{"release":"v1.2.3","source_commit":"'
            + "a" * 40
            + '","tag_ref":"refs/tags/v1.2.3","tag_object":"'
            + "b" * 40
            + '","signature_sha256":"'
            + "c" * 64
            + '","trust_policy_sha256":"'
            + "d" * 64
            + '","vendor_manifest_sha256":"'
            + "e" * 64
            + '"}'
        )
        (release / "runtime-manifest.json").write_text(manifest)
        (release / "runtime-manifest.json").chmod(0o600)
        tools = release / "tools"
        tools.mkdir(mode=0o755)
        entrypoint = tools / "handoffctl.py"
        entrypoint.write_text("#!/usr/bin/env python3\n")
        entrypoint.chmod(0o755)
        selector = root / "runtime-selector.json"
        commit_runtime_selector(selector, "v1.2.3", "v1.2.2")
        return selector, releases, release, cls._identity()

    @staticmethod
    def _verifier(path: Path, identity: ExpectedRuntimeIdentity) -> VerifiedManifest:
        return VerifiedManifest(
            "v1.2.3", identity, sha256((path / "runtime-manifest.json").read_bytes()).hexdigest()
        )

    def test_open_fixed_entrypoint_rejects_world_writable_tools_directory(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            _, _, release, identity = self._runtime(Path(directory))
            descriptor = os.open(release, os.O_RDONLY | os.O_DIRECTORY)
            try:
                (release / "tools").chmod(0o777)
                runtime = object.__new__(ResolvedRuntime)
                runtime.descriptor = descriptor
                runtime.path = release
                runtime.identity = VerifiedManifest("v1.2.3", identity, "f" * 64)
                with self.assertRaisesRegex(AuthorityError, "entrypoint directory is unsafe"):
                    _open_fixed_entrypoint(runtime)
            finally:
                os.close(descriptor)

    def test_manifest_reader_rejects_data_over_configured_limit(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            _, _, release, _ = self._runtime(Path(directory))
            with (
                patch("tools.runtime_bootstrap._MAX_MANIFEST_BYTES", 16),
                self.assertRaisesRegex(AuthorityError, "runtime manifest is too large"),
            ):
                read_runtime_manifest(release)

    def test_manifest_verifier_rejects_data_over_configured_limit(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            _, _, release, _ = self._runtime(Path(directory))
            digest = sha256((release / "runtime-manifest.json").read_bytes()).hexdigest()
            with (
                patch("tools.runtime_bootstrap._MAX_MANIFEST_BYTES", 16),
                self.assertRaisesRegex(AuthorityError, "runtime manifest is too large"),
            ):
                verify_runtime_manifest(release, digest)

    def test_bound_resolution_closes_open_release_descriptor_after_verifier_oserror(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            selector, releases, release, identity = self._runtime(Path(directory))
            opened: list[int] = []
            real_open = os.open

            def tracking_open(path: object, flags: int, *args: object, **kwargs: object) -> int:
                result = real_open(path, flags, *args, **kwargs)  # type: ignore[arg-type]
                if path == release:
                    opened.append(result)
                return result

            with (
                patch("tools.runtime_bootstrap.os.open", side_effect=tracking_open),
                self.assertRaisesRegex(AuthorityError, "resolved runtime is unavailable"),
            ):
                resolve_selected_runtime_bound(
                    selector,
                    releases,
                    identity,
                    lambda _path, _identity: (_ for _ in ()).throw(OSError("verifier I/O failure")),
                )
            self.assertEqual(1, len(opened))
            with self.assertRaises(OSError):
                os.fstat(opened[0])
