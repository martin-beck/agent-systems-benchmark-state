"""Project-bound conformance tests for the vendored coordinator snapshot tool."""

import hashlib
import importlib.util
import json
import os
import subprocess
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Any
from unittest.mock import patch

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "tools/handoffctl_vendor.py"
SPEC = importlib.util.spec_from_file_location("handoffctl_vendor", SOURCE)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load vendor tool")
VENDOR: Any = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VENDOR)

ATTESTATION = ROOT / "docs/coordinator-merge-attestation.md"
MERGE = "e52ce3aaa59ffc4cc6f97657b6ea2c7dfceb2ac1"
MERGE_PARENTS = "b90f28ccaa300c9ccca0167cee97925b211d2844 e4fecc1e65e640d436e4d01b8418fb7dc73c7c4e"
MERGE_TREE = "37ba9d70bdb25b61a66ae0c58c5b6e370cddfcce"
PR_HEAD = "e4fecc1e65e640d436e4d01b8418fb7dc73c7c4e"
PR_HEAD_TREE = "600b2d960e16cb5b144ec0db8b1e833f7fe797a0"
ATTESTED_UPSTREAM_COMMIT = "9733b341f25b145d6dfad8414933cb6348701769"
ATTESTED_MANIFEST_SHA256 = "60d7c3c634c14f6df34874ace6044e9058a3621f78d51491407f9ed5aa0c871a"
CURRENT_UPSTREAM_COMMIT = "07c27985e4c232c0a32d643b3a2df152b17d0d2d"
CURRENT_MANIFEST_SHA256 = "2c02762c1eab610652a6ba42ca7b12b0621b2f3badeb1b592389b43346f53aee"
ATTESTED_IDENTITIES = {
    "Pull request": "https://github.com/martin-beck/agent-systems-benchmark-state/pull/10",
    "Pull-request head": PR_HEAD,
    "Pull-request head tree": PR_HEAD_TREE,
    "Published merge": MERGE,
    "Merge parents, in order": MERGE_PARENTS,
    "Merge tree": MERGE_TREE,
    "Upstream signed tag object": "bd786b124a0e9ec926247e4c1de17ef4bbb84c0d",
    "Upstream signed release commit": ATTESTED_UPSTREAM_COMMIT,
    "v0.1.4 vendor manifest SHA-256": ATTESTED_MANIFEST_SHA256,
}


class VendorTest(unittest.TestCase):
    """Exercise the exact downstream paths used by the pinned vendor manifest."""

    def setUp(self) -> None:
        self.temporary = TemporaryDirectory()
        temporary = Path(self.temporary.name)
        self.source = temporary / "source"
        self.target = temporary / "target"
        self.source.mkdir()
        self.target.mkdir()
        for source_name, destination_name in VENDOR.SOURCE_FILES:
            source = self.source / source_name
            destination = ROOT / destination_name
            source.parent.mkdir(parents=True, exist_ok=True)
            source.write_bytes(destination.read_bytes())
            source.chmod(destination.stat().st_mode & 0o777)

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def test_additive_merge_attestation_is_exact_and_honest(self) -> None:
        text = ATTESTATION.read_text()
        observed: dict[str, str] = {}
        for line in text.splitlines():
            columns = [column.strip() for column in line.split("|")]
            if len(columns) == 4 and columns[1] in ATTESTED_IDENTITIES:
                value = columns[2]
                self.assertTrue(value.startswith("`") and value.endswith("`"))
                observed[columns[1]] = value[1:-1]
        self.assertEqual(ATTESTED_IDENTITIES, observed)
        self.assertEqual(PR_HEAD, MERGE_PARENTS.split()[1])
        for identity in (
            MERGE,
            MERGE_TREE,
            PR_HEAD,
            PR_HEAD_TREE,
            ATTESTED_UPSTREAM_COMMIT,
            CURRENT_UPSTREAM_COMMIT,
        ):
            self.assertRegex(identity, r"^[0-9a-f]{40}$")
        self.assertIn("does **not** add", text)
        self.assertIn("rather than rewriting public history", text)
        self.assertIn("not an independent cryptographic proof", text)
        manifest_bytes = (ROOT / VENDOR.LOCK_NAME).read_bytes()
        self.assertEqual(CURRENT_MANIFEST_SHA256, hashlib.sha256(manifest_bytes).hexdigest())
        manifest = json.loads(manifest_bytes)
        self.assertEqual("v0.2.0", manifest["upstream"]["version"])
        self.assertEqual(CURRENT_UPSTREAM_COMMIT, manifest["upstream"]["commit"])

    def test_sync_verify_and_detect_tampering(self) -> None:
        commit = "a" * 40
        profile = self.target / ".handoffctl.json"
        binding = self.target / "coordinator.binding.json"
        profile.write_text("project-profile-sentinel\n")
        binding.write_text("project-binding-sentinel\n")
        with patch("builtins.print") as output:
            VENDOR.sync(self.source, self.target, "v0.2.0", commit)
        output.assert_called_once()
        self.assertEqual("project-profile-sentinel\n", profile.read_text())
        self.assertEqual("project-binding-sentinel\n", binding.read_text())
        lock = json.loads((self.target / VENDOR.LOCK_NAME).read_text())
        self.assertEqual(commit, lock["upstream"]["commit"])
        self.assertEqual(
            {destination for _, destination in VENDOR.SOURCE_FILES}, set(lock["files"])
        )
        self.assertTrue(os.access(self.target / "tools/handoffctl", os.X_OK))
        with patch("builtins.print"):
            VENDOR.verify(self.target)
        (self.target / "tools/handoffctl.py").write_text("tampered\n")
        with self.assertRaisesRegex(RuntimeError, "digest mismatch"):
            VENDOR.verify(self.target)

    def test_rejects_bad_release_identity_and_lock_shapes(self) -> None:
        with self.assertRaisesRegex(RuntimeError, "invalid release"):
            VENDOR.build_lock(self.source, "latest", "short")
        (self.target / VENDOR.LOCK_NAME).write_text("{}")
        with self.assertRaisesRegex(RuntimeError, "lock structure"):
            VENDOR.verify(self.target)
        (self.target / VENDOR.LOCK_NAME).write_text("not-json")
        with self.assertRaisesRegex(RuntimeError, "cannot read"):
            VENDOR.verify(self.target)

    def test_release_identity_requires_clean_exact_tag(self) -> None:
        with patch.object(VENDOR, "git_output", side_effect=["", "b" * 40, "v0.2.0"]):
            self.assertEqual("b" * 40, VENDOR.release_identity(self.source, "v0.2.0"))
        with (
            patch.object(VENDOR, "git_output", return_value="dirty"),
            self.assertRaisesRegex(RuntimeError, "must be clean"),
        ):
            VENDOR.release_identity(self.source, "v0.2.0")
        with (
            patch.object(VENDOR, "git_output", side_effect=["", "b" * 40, "v0.3.0"]),
            self.assertRaisesRegex(RuntimeError, "not tagged"),
        ):
            VENDOR.release_identity(self.source, "v0.2.0")
        with self.assertRaisesRegex(RuntimeError, "form vMAJOR"):
            VENDOR.release_identity(self.source, "main")

    def test_verify_rejects_identity_manifest_and_runtime_mismatch(self) -> None:
        commit = "d" * 40
        with patch("builtins.print"):
            VENDOR.sync(self.source, self.target, "v0.2.0", commit)
        original = json.loads((self.target / VENDOR.LOCK_NAME).read_text())
        variants: list[dict[str, Any]] = []
        value = json.loads(json.dumps(original))
        value["schema_version"] = 2
        variants.append(value)
        value = json.loads(json.dumps(original))
        value["upstream"] = {}
        variants.append(value)
        value = json.loads(json.dumps(original))
        value["upstream"]["repository"] = "other"
        variants.append(value)
        value = json.loads(json.dumps(original))
        value["upstream"]["version"] = "latest"
        variants.append(value)
        value = json.loads(json.dumps(original))
        value["files"] = {}
        variants.append(value)
        value = json.loads(json.dumps(original))
        first = next(iter(value["files"]))
        value["files"][first] = {}
        variants.append(value)
        for value in variants:
            with self.subTest(value=value), self.assertRaises(RuntimeError):
                (self.target / VENDOR.LOCK_NAME).write_text(json.dumps(value))
                VENDOR.verify(self.target)
        (self.target / VENDOR.LOCK_NAME).write_text(json.dumps(original))
        core = self.target / "tools/handoffctl.py"
        core.write_text(
            core.read_text().replace(
                'COORDINATOR_VERSION = "0.2.0"', 'COORDINATOR_VERSION = "9.9.9"'
            )
        )
        original["files"]["tools/handoffctl.py"]["sha256"] = VENDOR.sha256(core)
        (self.target / VENDOR.LOCK_NAME).write_text(json.dumps(original))
        with self.assertRaisesRegex(RuntimeError, "runtime version"):
            VENDOR.verify(self.target)
        with self.assertRaisesRegex(RuntimeError, "regular file"):
            VENDOR.sha256(self.target / "missing")
        with (
            patch.object(VENDOR, "git_output", side_effect=["", "short", "v0.2.0"]),
            self.assertRaisesRegex(RuntimeError, "full commit"),
        ):
            VENDOR.release_identity(self.source, "v0.2.0")

    def test_atomic_copy_rejects_symlink_and_git_query_is_bounded(self) -> None:
        source = self.target / "source"
        source.write_text("value")
        destination = self.target / "destination"
        destination.symlink_to(source)
        with self.assertRaisesRegex(RuntimeError, "symlink"):
            VENDOR.atomic_bytes(destination, b"replacement")
        with patch("subprocess.run") as run:
            run.return_value = subprocess.CompletedProcess([], 0, "head\n", "")
            self.assertEqual("head", VENDOR.git_output(self.source, "rev-parse", "HEAD"))
            self.assertEqual(30, run.call_args.kwargs["timeout"])

    def test_main_dispatches_sync_and_verify(self) -> None:
        with (
            patch.object(sys, "argv", ["vendor", "verify", "--target", str(self.target)]),
            patch.object(VENDOR, "verify") as verify,
        ):
            self.assertEqual(0, VENDOR.main())
            verify.assert_called_once_with(self.target)
        with (
            patch.object(
                sys,
                "argv",
                [
                    "vendor",
                    "sync",
                    "--source",
                    str(self.source),
                    "--target",
                    str(self.target),
                    "--version",
                    "v0.2.0",
                ],
            ),
            patch.object(VENDOR, "release_identity", return_value="c" * 40),
            patch.object(VENDOR, "sync") as sync,
        ):
            self.assertEqual(0, VENDOR.main())
            sync.assert_called_once_with(self.source, self.target, "v0.2.0", "c" * 40)


if __name__ == "__main__":
    unittest.main()
