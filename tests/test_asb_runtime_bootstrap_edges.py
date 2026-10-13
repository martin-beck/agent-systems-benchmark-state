# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Downstream recovery coverage for runtime bootstrap dispatch."""

from __future__ import annotations

import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

from tools.runtime_bootstrap import (
    AdmittedRuntimeCommand,
    DispatchAdmission,
    ExpectedRuntimeIdentity,
    VerifiedManifest,
    prepare_runtime_dispatch,
    resolve_selected_runtime_bound,
    run_admitted_runtime,
    run_selected_runtime,
)
from tools.upgrade_authority import AuthorityError, commit_runtime_selector


class RuntimeBootstrapEdgeTests(unittest.TestCase):
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
    def _runtime(cls, root: Path) -> tuple[Path, Path, ExpectedRuntimeIdentity]:
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
        return selector, releases, cls._identity()

    @staticmethod
    def _verifier(path: Path, identity: ExpectedRuntimeIdentity) -> VerifiedManifest:
        from hashlib import sha256

        return VerifiedManifest(
            "v1.2.3", identity, sha256((path / "runtime-manifest.json").read_bytes()).hexdigest()
        )

    def test_prepare_dispatch_closes_opened_entrypoint_when_second_gate_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            selector, releases, identity = self._runtime(Path(directory))
            with resolve_selected_runtime_bound(
                selector, releases, identity, self._verifier
            ) as resolved:
                admission = resolved.admit_for_dispatch()
                descriptor = os.open(resolved.path / "tools" / "handoffctl.py", os.O_RDONLY)
                with (
                    patch(
                        "tools.runtime_bootstrap._open_fixed_entrypoint", return_value=descriptor
                    ),
                    patch(
                        "tools.runtime_bootstrap.DispatchAdmission.revalidate",
                        side_effect=[None, AuthorityError("runtime changed")],
                    ),
                    self.assertRaisesRegex(AuthorityError, "runtime changed"),
                ):
                    prepare_runtime_dispatch(admission)
                with self.assertRaises(OSError):
                    os.fstat(descriptor)
                admission.close()

    def test_run_admitted_runtime_closes_command_after_timeout(self) -> None:
        command = Mock(spec=AdmittedRuntimeCommand)
        command.argv = ("python", "handoffctl.py")
        command.pass_fds = ()
        command.environment = {}
        admission = Mock(spec=DispatchAdmission)
        with (
            patch("tools.runtime_bootstrap.prepare_runtime_dispatch", return_value=command),
            patch(
                "tools.runtime_bootstrap.subprocess.run",
                side_effect=__import__("subprocess").TimeoutExpired(["python"], 1),
            ),
            self.assertRaisesRegex(AuthorityError, "dispatch timed out"),
        ):
            run_admitted_runtime(admission, timeout=1)
        command.close.assert_called_once_with()

    def test_run_selected_runtime_closes_resolved_handle_when_admission_fails(self) -> None:
        resolved = Mock()
        resolved.admit_for_dispatch.side_effect = AuthorityError("admission failed")
        with (
            patch("tools.runtime_bootstrap.resolve_selected_runtime_bound", return_value=resolved),
            self.assertRaisesRegex(AuthorityError, "admission failed"),
        ):
            run_selected_runtime(
                Path("selector"), Path("releases"), self._identity(), self._verifier
            )
        resolved.close.assert_called_once_with()

    def test_run_selected_runtime_closes_admission_when_consumer_fails(self) -> None:
        admission = Mock(spec=DispatchAdmission)
        resolved = Mock()
        resolved.admit_for_dispatch.return_value = admission
        with (
            patch("tools.runtime_bootstrap.resolve_selected_runtime_bound", return_value=resolved),
            patch(
                "tools.runtime_bootstrap.run_admitted_runtime",
                side_effect=AuthorityError("consumer failed"),
            ),
            self.assertRaisesRegex(AuthorityError, "consumer failed"),
        ):
            run_selected_runtime(
                Path("selector"), Path("releases"), self._identity(), self._verifier
            )
        admission.close.assert_called_once_with()
