# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

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
CURRENT_UPSTREAM_COMMIT = "113dc61029f0e0c57bc7832e1e41430eafa17e73"
CURRENT_UPSTREAM_VERSION = "v0.3.57"
CURRENT_MANIFEST_SHA256 = "02149740b14a554d784e2f0fd8572a67dbf3faabe379fc39b4e9703de74e9936"
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
            if destination.is_file():
                contents = destination.read_bytes()
                source.write_bytes(contents)
                source.chmod(destination.stat().st_mode & 0o777)
            else:
                # New coordinator releases may add allowlisted files before
                # this downstream checkout has consumed the release. Keep the
                # unit fixture self-contained; the immutable release sync
                # gate validates the real source files separately.
                source.write_text(f"fixture:{destination_name}\n")

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def create_development_source(self, name: str) -> tuple[Path, str]:
        """Create one exact committed development fixture for Git-object tests."""
        source = Path(self.temporary.name) / name
        (source / "tools").mkdir(parents=True)
        version = CURRENT_UPSTREAM_VERSION.removeprefix("v")
        (source / "tools/handoffctl.py").write_text(
            f'COORDINATOR_VERSION = "{version}"\n', encoding="utf-8"
        )
        (source / "LICENSE").write_text("committed-license\n", encoding="utf-8")
        subprocess.run(["/usr/bin/git", "init", "-q"], cwd=source, check=True)
        subprocess.run(["/usr/bin/git", "add", "."], cwd=source, check=True)
        subprocess.run(
            [
                "/usr/bin/git",
                "-c",
                "user.name=Vendor Test",
                "-c",
                "user.email=vendor-test@example.invalid",
                "commit",
                "-qm",
                "fixture",
            ],
            cwd=source,
            check=True,
        )
        commit = subprocess.run(
            ["/usr/bin/git", "rev-parse", "HEAD"],
            cwd=source,
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()
        return source, commit

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
        self.assertEqual(CURRENT_UPSTREAM_VERSION, manifest["upstream"]["version"])
        self.assertEqual(CURRENT_UPSTREAM_COMMIT, manifest["upstream"]["commit"])

    def test_sync_verify_and_detect_tampering(self) -> None:
        commit = "a" * 40
        profile = self.target / ".handoffctl.json"
        binding = self.target / "coordinator.binding.json"
        profile.write_text("project-profile-sentinel\n")
        binding.write_text("project-binding-sentinel\n")
        with patch("builtins.print") as output:
            VENDOR.sync(self.source, self.target, CURRENT_UPSTREAM_VERSION, commit)
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
        with patch.object(VENDOR, "git_output", side_effect=["", "b" * 40, "v0.3.7"]):
            self.assertEqual("b" * 40, VENDOR.release_identity(self.source, "v0.3.7"))
        with (
            patch.object(VENDOR, "git_output", return_value="dirty"),
            self.assertRaisesRegex(RuntimeError, "must be clean"),
        ):
            VENDOR.release_identity(self.source, "v0.3.7")
        with (
            patch.object(VENDOR, "git_output", side_effect=["", "b" * 40, "v0.3.0"]),
            self.assertRaisesRegex(RuntimeError, "not tagged"),
        ):
            VENDOR.release_identity(self.source, "v0.3.7")
        with self.assertRaisesRegex(RuntimeError, "form vMAJOR"):
            VENDOR.release_identity(self.source, "main")

    def test_development_identity_requires_clean_exact_head_and_tree(self) -> None:
        commit = "c" * 40
        tree = "d" * 40
        root = str(self.source.resolve())
        with patch.object(VENDOR, "git_output", side_effect=[root, "", commit, tree]):
            self.assertEqual(tree, VENDOR.development_identity(self.source, commit))
        hostile = (
            ([root, "dirty"], "must be clean"),
            ([root, "", "e" * 40], "HEAD differs"),
            ([root, "", commit, "short"], "tree is not a full"),
            ([str(self.source.parent)], "worktree root"),
        )
        for outputs, message in hostile:
            with (
                self.subTest(message=message),
                patch.object(VENDOR, "git_output", side_effect=outputs),
                self.assertRaisesRegex(RuntimeError, message),
            ):
                VENDOR.development_identity(self.source, commit)
        with self.assertRaisesRegex(RuntimeError, "full commit"):
            VENDOR.development_identity(self.source, "short")

    def test_development_sync_uses_exact_git_blobs_modes_and_identity(self) -> None:
        source, commit = self.create_development_source("development-source")
        committed_license = (source / "LICENSE").read_text()
        subprocess.run(
            ["/usr/bin/git", "update-index", "--assume-unchanged", "LICENSE"],
            cwd=source,
            check=True,
        )
        (source / "LICENSE").write_text("substituted-worktree-license\n")
        sources = (
            ("tools/handoffctl.py", "tools/handoffctl.py"),
            ("LICENSE", "vendor/agent-workflow-coordinator/LICENSE"),
        )
        with patch.object(VENDOR, "SOURCE_FILES", sources), patch("builtins.print"):
            VENDOR.sync_development(source, self.target, commit)
            VENDOR.verify(self.target)
        lock = json.loads((self.target / VENDOR.LOCK_NAME).read_text())
        self.assertEqual(2, lock["schema_version"])
        self.assertEqual("development", lock["upstream"]["channel"])
        self.assertEqual(commit, lock["upstream"]["commit"])
        tree = subprocess.run(
            ["/usr/bin/git", "rev-parse", "HEAD^{tree}"],
            cwd=source,
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()
        self.assertEqual(tree, lock["upstream"]["tree"])
        installed = self.target / "vendor/agent-workflow-coordinator/LICENSE"
        self.assertEqual(committed_license, installed.read_text())
        self.assertEqual(0o644, installed.stat().st_mode & 0o777)
        with patch.object(VENDOR, "SOURCE_FILES", sources):
            self.assertEqual(lock, VENDOR.build_development_lock(source, commit))
            hostile = json.loads(json.dumps(lock))
            hostile["upstream"]["channel"] = "release"
            (self.target / VENDOR.LOCK_NAME).write_text(json.dumps(hostile))
            with self.assertRaisesRegex(RuntimeError, "invalid development"):
                VENDOR.verify(self.target)
            hostile["schema_version"] = 3
            (self.target / VENDOR.LOCK_NAME).write_text(json.dumps(hostile))
            with self.assertRaisesRegex(RuntimeError, "unsupported vendor lock schema"):
                VENDOR.verify(self.target)

    def test_development_payload_and_runtime_reject_hostile_inputs(self) -> None:
        with self.assertRaisesRegex(RuntimeError, "not UTF-8"):
            VENDOR.runtime_version(b"\xff")
        with self.assertRaisesRegex(RuntimeError, "cannot determine"):
            VENDOR.runtime_version(b"missing version")
        with (
            patch.object(VENDOR, "git_output", return_value="malformed"),
            self.assertRaisesRegex(RuntimeError, "invalid Git tree entry"),
        ):
            VENDOR.git_blob_payload(self.source, "c" * 40, "LICENSE")
        hostile_entries = (
            "100644 tree " + "a" * 40 + "\tLICENSE",
            "120000 blob " + "a" * 40 + "\tLICENSE",
            "100644 blob " + "a" * 40 + "\tother",
        )
        for entry in hostile_entries:
            with (
                self.subTest(entry=entry),
                patch.object(VENDOR, "git_output", return_value=entry),
                self.assertRaisesRegex(RuntimeError, "regular committed file"),
            ):
                VENDOR.git_blob_payload(self.source, "c" * 40, "LICENSE")
        with (
            patch.object(VENDOR, "SOURCE_FILES", (("LICENSE", "LICENSE"),)),
            patch.object(VENDOR, "development_identity", return_value="d" * 40),
            patch.object(VENDOR, "git_blob_payload", return_value=(b"license", 0o644)),
            self.assertRaisesRegex(RuntimeError, "omits tools/handoffctl.py"),
        ):
            VENDOR.build_development_lock(self.source, "c" * 40)

    def test_formal_alignment_and_development_cli_fail_closed(self) -> None:
        tools = self.target / "tools"
        formal = self.target / "formal/handoffctl"
        tools.mkdir(parents=True)
        formal.mkdir(parents=True)
        runtime = tools / "handoffctl.py"
        model = formal / "Handoffctl.tla"
        runtime.write_text('LIFECYCLE_MUTATION_COMMANDS = ("resume", 3)\n')
        model.write_text("Operations == {resume}\n")
        with self.assertRaisesRegex(RuntimeError, "runtime inventory"):
            VENDOR.verify_formal_lifecycle_alignment(self.target)
        runtime.write_text("not valid python !\n")
        with self.assertRaisesRegex(RuntimeError, "inputs are unreadable"):
            VENDOR.verify_formal_lifecycle_alignment(self.target)
        runtime.write_text('LIFECYCLE_MUTATION_COMMANDS = ("resume",)\n')
        with self.assertRaisesRegex(RuntimeError, "operation inventory"):
            VENDOR.verify_formal_lifecycle_alignment(self.target)
        with (
            patch.object(
                sys,
                "argv",
                [
                    "vendor",
                    "sync-development",
                    "--source",
                    str(self.source),
                    "--target",
                    str(self.target),
                    "--commit",
                    "d" * 40,
                ],
            ),
            patch.object(VENDOR, "sync_development") as sync_development,
        ):
            self.assertEqual(0, VENDOR.main())
        sync_development.assert_called_once_with(self.source, self.target, "d" * 40)

    def test_verify_rejects_identity_manifest_and_runtime_mismatch(self) -> None:
        commit = "d" * 40
        with patch("builtins.print"):
            VENDOR.sync(self.source, self.target, CURRENT_UPSTREAM_VERSION, commit)
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
                f'COORDINATOR_VERSION = "{CURRENT_UPSTREAM_VERSION.removeprefix("v")}"',
                'COORDINATOR_VERSION = "9.9.9"',
            )
        )
        original["files"]["tools/handoffctl.py"]["sha256"] = VENDOR.sha256(core)
        (self.target / VENDOR.LOCK_NAME).write_text(json.dumps(original))
        with self.assertRaisesRegex(RuntimeError, "runtime version"):
            VENDOR.verify(self.target)
        with self.assertRaisesRegex(RuntimeError, "regular file"):
            VENDOR.sha256(self.target / "missing")
        with (
            patch.object(VENDOR, "git_output", side_effect=["", "short", "v0.3.7"]),
            self.assertRaisesRegex(RuntimeError, "full commit"),
        ):
            VENDOR.release_identity(self.source, "v0.3.7")

    def test_install_failure_rolls_back_every_destination(self) -> None:
        staged = self.target / "staged"
        destination_root = self.target / "installed"
        staged.mkdir()
        destination_root.mkdir()
        for name in ("one", "two"):
            (staged / name).write_text(f"new-{name}\n")
            (destination_root / name).write_text(f"old-{name}\n")
        original_replace = Path.replace

        def fail_second_install(path: Path, target: Path) -> Path:
            if path == staged / "two":
                raise OSError(5, "injected rename failure")
            return original_replace(path, target)

        with (
            patch.object(Path, "replace", fail_second_install),
            self.assertRaisesRegex(OSError, "injected rename"),
        ):
            VENDOR.install_staged_snapshot(staged, destination_root, ["one", "two"])
        self.assertEqual("old-one\n", (destination_root / "one").read_text())
        self.assertEqual("old-two\n", (destination_root / "two").read_text())

        (staged / "link").write_text("new\n")
        (destination_root / "link").symlink_to(destination_root / "one")
        with self.assertRaisesRegex(RuntimeError, "symlink"):
            VENDOR.install_staged_snapshot(staged, destination_root, ["link"])

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
                    "v0.3.7",
                ],
            ),
            patch.object(VENDOR, "release_identity", return_value="c" * 40),
            patch.object(VENDOR, "sync") as sync,
        ):
            self.assertEqual(0, VENDOR.main())
            sync.assert_called_once_with(self.source, self.target, "v0.3.7", "c" * 40)


if __name__ == "__main__":
    unittest.main()
