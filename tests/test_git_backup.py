# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Fault-path tests for complete Git backup artifacts."""

from __future__ import annotations

import hashlib
import importlib.util
import io
import json
import subprocess
import tarfile
import tempfile
import unittest
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from threading import Barrier
from typing import cast
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("git_backup", ROOT / "tools/git_backup.py")
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
BackupError = MODULE.BackupError
create_backup = MODULE.create_backup
restore_backup = MODULE.restore_backup
verify_backup = MODULE.verify_backup


def git(*args: str, cwd: Path) -> None:
    subprocess.run(  # noqa: S603
        ["git", *args],  # noqa: S607
        cwd=cwd,
        check=True,
        capture_output=True,
    )


def git_output(*args: str, cwd: Path) -> str:
    return subprocess.check_output(  # noqa: S603
        ["git", *args],  # noqa: S607
        cwd=cwd,
        text=True,
        stderr=subprocess.STDOUT,
    )


class GitBackupTests(unittest.TestCase):
    def repo(self, root: Path) -> Path:
        repo = root / "repo"
        repo.mkdir()
        git("init", "-q", cwd=repo)
        git("config", "user.email", "test@example.invalid", cwd=repo)
        git("config", "user.name", "test", cwd=repo)
        (repo / "task.md").write_text("state\n")
        git("add", "task.md", cwd=repo)
        git("commit", "-qm", "initial", cwd=repo)
        return repo

    def test_create_verify_and_restore_round_trip(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            repo = self.repo(root)
            backup = create_backup(repo, root / "backup", quiesced=True)
            self.assertEqual(True, verify_backup(backup)["verified"])
            restore_backup(backup, root / "restored")
            self.assertTrue((root / "restored" / "task.md").exists())

    def test_fresh_clone_rollback_preserves_verified_lifecycle_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            repo = self.repo(root)
            backup = create_backup(repo, root / "backup", quiesced=True)
            expected_head = git_output("rev-parse", "HEAD", cwd=repo).strip()
            backup_hashes = {
                path.name: hashlib.sha256(path.read_bytes()).hexdigest()
                for path in backup.iterdir()
                if path.is_file()
            }
            restore_backup(backup, root / "fresh-clone")
            fresh = root / "fresh-clone"
            self.assertEqual(expected_head, git_output("rev-parse", "HEAD", cwd=fresh).strip())
            self.assertEqual(
                (backup / "index.txt").read_text(encoding="utf-8"),
                git_output("ls-files", "--stage", cwd=fresh),
            )
            self.assertEqual(
                (backup / "tracked-files.txt").read_text(encoding="utf-8"),
                git_output("ls-files", cwd=fresh),
            )
            self.assertEqual("", git_output("status", "--porcelain", cwd=fresh))
            self.assertEqual(
                backup_hashes,
                {
                    path.name: hashlib.sha256(path.read_bytes()).hexdigest()
                    for path in backup.iterdir()
                    if path.is_file()
                },
            )
            self.assertEqual([], list(root.glob(".git-restore-*")))

    def test_verify_rejects_backup_directory_replacement(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            repo = self.repo(root)
            backup = create_backup(repo, root / "backup", quiesced=True)
            replacement = create_backup(repo, root / "replacement", quiesced=True)
            original = root / "original-backup"
            original_verify = MODULE._verify_artifacts

            def replace_after_artifacts(path: Path, manifest: dict[str, object]) -> None:
                original_verify(path, manifest)
                path.rename(original)
                path.symlink_to(replacement, target_is_directory=True)

            with (
                patch.object(MODULE, "_verify_artifacts", side_effect=replace_after_artifacts),
                self.assertRaisesRegex(BackupError, "backup must not be a symlink"),
            ):
                verify_backup(backup)
            self.assertTrue(original.is_dir())
            self.assertTrue(replacement.is_dir())

    def test_verify_rejects_manifest_mutation_before_returning_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            repo = self.repo(root)
            backup = create_backup(repo, root / "backup", quiesced=True)
            original_archive = MODULE._verify_archive

            def mutate_after_archive(path: Path) -> None:
                original_archive(path)
                manifest_path = backup / "manifest.json"
                value = json.loads(manifest_path.read_text(encoding="utf-8"))
                value["quiesced"] = False
                manifest_path.write_text(json.dumps(value, sort_keys=True), encoding="utf-8")

            with (
                patch.object(MODULE, "_verify_archive", side_effect=mutate_after_archive),
                self.assertRaisesRegex(BackupError, "manifest changed during verification"),
            ):
                verify_backup(backup)

    def test_verify_rejects_same_byte_manifest_symlink_replacement(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            repo = self.repo(root)
            backup = create_backup(repo, root / "backup", quiesced=True)
            manifest_path = backup / "manifest.json"
            original = root / "original-manifest.json"
            foreign = root / "foreign-manifest.json"
            foreign.write_bytes(manifest_path.read_bytes())
            original_archive = MODULE._verify_archive

            def replace_after_archive(path: Path) -> None:
                original_archive(path)
                manifest_path.rename(original)
                manifest_path.symlink_to(foreign)

            with (
                patch.object(MODULE, "_verify_archive", side_effect=replace_after_archive),
                self.assertRaisesRegex(BackupError, "manifest must be a regular file"),
            ):
                verify_backup(backup)
            self.assertTrue(original.is_file())
            self.assertTrue(foreign.is_file())
            self.assertEqual(foreign.read_bytes(), original.read_bytes())

    def test_verify_rejects_artifact_replacement_before_returning_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            repo = self.repo(root)
            backup = create_backup(repo, root / "backup", quiesced=True)
            foreign = root / "foreign-refs.txt"
            foreign.write_text((backup / "refs.txt").read_text(encoding="utf-8"), encoding="utf-8")
            original_verify = MODULE._verify_artifacts
            calls = 0
            original = root / "original-refs.txt"

            def replace_after_first(path: Path, manifest: dict[str, object]) -> None:
                nonlocal calls
                original_verify(path, manifest)
                calls += 1
                if calls == 1:
                    (backup / "refs.txt").rename(original)
                    (backup / "refs.txt").symlink_to(foreign)

            with (
                patch.object(MODULE, "_verify_artifacts", side_effect=replace_after_first),
                self.assertRaisesRegex(BackupError, "artifact"),
            ):
                verify_backup(backup)
            self.assertTrue(original.is_file())
            self.assertTrue(foreign.is_file())

    def test_verify_rejects_archive_content_mismatch_even_with_updated_manifest(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            repo = self.repo(root)
            backup = create_backup(repo, root / "backup", quiesced=True)
            archive_path = backup / "tracked-tree.tar"
            rewritten = io.BytesIO()
            with (
                tarfile.open(archive_path) as source,
                tarfile.open(fileobj=rewritten, mode="w") as target,
            ):
                for member in source.getmembers():
                    payload = source.extractfile(member)
                    data = (
                        b"tampered\n"
                        if member.name == "task.md"
                        else (payload.read() if payload else b"")
                    )
                    target.addfile(member, io.BytesIO(data))
            archive_path.write_bytes(rewritten.getvalue())
            manifest_path = backup / "manifest.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["artifacts"]["tracked-tree.tar"] = {
                "sha256": hashlib.sha256(archive_path.read_bytes()).hexdigest(),
                "size": archive_path.stat().st_size,
            }
            manifest_path.write_text(json.dumps(manifest, sort_keys=True), encoding="utf-8")
            with self.assertRaisesRegex(BackupError, "archive content mismatch"):
                verify_backup(backup)

    def test_verify_rejects_archive_file_set_mismatch(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            backup = create_backup(self.repo(root), root / "backup", quiesced=True)
            archive_path = backup / "tracked-tree.tar"
            rewritten = io.BytesIO()
            with (
                tarfile.open(archive_path) as source,
                tarfile.open(fileobj=rewritten, mode="w") as target,
            ):
                for member in source.getmembers():
                    payload = source.extractfile(member)
                    target.addfile(member, io.BytesIO(payload.read() if payload else b""))
                extra = tarfile.TarInfo("extra.txt")
                extra.size = 1
                target.addfile(extra, io.BytesIO(b"x"))
            archive_path.write_bytes(rewritten.getvalue())
            manifest_path = backup / "manifest.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["artifacts"]["tracked-tree.tar"] = {
                "sha256": hashlib.sha256(archive_path.read_bytes()).hexdigest(),
                "size": archive_path.stat().st_size,
            }
            manifest_path.write_text(json.dumps(manifest, sort_keys=True), encoding="utf-8")
            with self.assertRaisesRegex(BackupError, "archive file set mismatch"):
                verify_backup(backup)

    def test_verify_rejects_index_mismatch_after_clean_clone(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            backup = create_backup(self.repo(root), root / "backup", quiesced=True)
            index_path = backup / "index.txt"
            index_path.write_text("100644 deadbeef\twrong\n", encoding="utf-8")
            manifest_path = backup / "manifest.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["artifacts"]["index.txt"] = {
                "sha256": hashlib.sha256(index_path.read_bytes()).hexdigest(),
                "size": index_path.stat().st_size,
            }
            manifest_path.write_text(json.dumps(manifest, sort_keys=True), encoding="utf-8")
            with self.assertRaisesRegex(BackupError, "clean restore index mismatch"):
                verify_backup(backup)

    def test_verify_rejects_archive_race_after_safety_check_without_residue(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            repo = self.repo(root)
            backup = create_backup(repo, root / "backup", quiesced=True)
            archive_path = backup / "tracked-tree.tar"
            mutated = io.BytesIO()
            with (
                tarfile.open(archive_path) as source,
                tarfile.open(fileobj=mutated, mode="w") as target,
            ):
                for member in source.getmembers():
                    payload = source.extractfile(member)
                    data = (
                        b"race mutation\n"
                        if member.name == "task.md"
                        else (payload.read() if payload else b"")
                    )
                    target.addfile(member, io.BytesIO(data))
            mutated_bytes = mutated.getvalue()
            start_barrier = Barrier(2)
            completion_barrier = Barrier(2)
            original_verify = MODULE._verify_archive

            def replace_after_check(path: Path) -> None:
                original_verify(path)
                start_barrier.wait()
                completion_barrier.wait()

            def mutate_archive() -> None:
                start_barrier.wait()
                archive_path.write_bytes(mutated_bytes)
                completion_barrier.wait()

            before = set(Path(tempfile.gettempdir()).glob("handoffctl-restore-*"))
            with ThreadPoolExecutor(max_workers=1) as pool:
                future = pool.submit(mutate_archive)
                with (
                    patch.object(MODULE, "_verify_archive", side_effect=replace_after_check),
                    self.assertRaisesRegex(BackupError, "archive content mismatch"),
                ):
                    verify_backup(backup)
                future.result()
            after = set(Path(tempfile.gettempdir()).glob("handoffctl-restore-*"))
            self.assertEqual(before, after)

    def test_restore_rejects_backup_replacement_after_verify(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            repo = self.repo(root)
            backup = create_backup(repo, root / "backup", quiesced=True)
            replacement = create_backup(repo, root / "replacement", quiesced=True)
            original = root / "original-backup"
            original_verify = MODULE.verify_backup

            def replace_after_verify(path: Path) -> dict[str, object]:
                result = cast(dict[str, object], original_verify(path))
                path.rename(original)
                path.symlink_to(replacement, target_is_directory=True)
                return result

            with (
                patch.object(MODULE, "verify_backup", side_effect=replace_after_verify),
                self.assertRaisesRegex(BackupError, "backup must not be a symlink"),
            ):
                restore_backup(backup, root / "restored")
            self.assertFalse((root / "restored").exists())
            self.assertTrue(original.is_dir())

    def test_restore_rejects_destination_parent_replacement(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            repo = self.repo(root)
            backup = create_backup(repo, root / "backup", quiesced=True)
            parent = root / "dest-parent"
            parent.mkdir()
            destination = parent / "restored"
            moved = root / "moved-parent"
            redirect = root / "redirect-parent"
            redirect.mkdir()
            original_run = MODULE._run
            swapped = False
            clone_count = 0

            def swap_after_clone(command: list[str], cwd: Path) -> str:
                nonlocal clone_count, swapped
                result = cast(str, original_run(command, cwd))
                if command[:2] == ["git", "clone"]:
                    clone_count += 1
                if command[:2] == ["git", "clone"] and clone_count == 2 and not swapped:
                    swapped = True
                    parent.rename(moved)
                    parent.symlink_to(redirect, target_is_directory=True)
                return result

            with (
                patch.object(MODULE, "_run", side_effect=swap_after_clone),
                self.assertRaisesRegex(BackupError, "parent changed before publication"),
            ):
                restore_backup(backup, destination)
            self.assertFalse(destination.exists())
            self.assertFalse(list(redirect.glob(".git-restore-*")))

    def test_create_rejects_destination_parent_replacement(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            repo = self.repo(root)
            parent = root / "backup-parent"
            parent.mkdir()
            destination = parent / "backup"
            moved = root / "moved-parent"
            redirect = root / "redirect-parent"
            redirect.mkdir()
            original_manifest = MODULE._write_manifest

            def swap_after_manifest(path: Path, value: dict[str, object]) -> None:
                original_manifest(path, value)
                parent.rename(moved)
                parent.symlink_to(redirect, target_is_directory=True)

            with (
                patch.object(MODULE, "_write_manifest", side_effect=swap_after_manifest),
                self.assertRaisesRegex(BackupError, "parent changed before publication"),
            ):
                create_backup(repo, destination, quiesced=True)
            self.assertFalse(destination.exists())
            self.assertFalse(list(redirect.glob(".git-backup-*")))

    def test_parent_identity_stat_failure_is_backup_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / "backup"
            with (
                patch.object(Path, "stat", side_effect=OSError("gone")),
                self.assertRaisesRegex(BackupError, "parent disappeared"),
            ):
                MODULE._parent_identity(destination)

    def test_create_temporary_allocation_failure_is_backup_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            repo = self.repo(root)
            with (
                patch.object(MODULE.tempfile, "mkdtemp", side_effect=OSError("full")),
                self.assertRaisesRegex(BackupError, "temporary allocation failed"),
            ):
                create_backup(repo, root / "backup", quiesced=True)

    def test_restore_preserves_commit_tree_and_refs_equivalence(self) -> None:
        """A verified backup restores the exact immutable Git authority view."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            repo = self.repo(root)
            backup = create_backup(repo, root / "backup", quiesced=True)
            original_head = git_output("rev-parse", "HEAD", cwd=repo)
            original_tree = git_output("ls-tree", "-r", "HEAD", cwd=repo)
            original_refs = git_output("show-ref", "--heads", cwd=repo)
            self.assertEqual(original_head, str(verify_backup(backup)["commit"]) + "\n")
            restore_backup(backup, root / "restored")
            restored = root / "restored"
            self.assertEqual(original_head, git_output("rev-parse", "HEAD", cwd=restored))
            self.assertEqual(original_tree, git_output("ls-tree", "-r", "HEAD", cwd=restored))
            self.assertEqual(original_refs, git_output("show-ref", "--heads", cwd=restored))

    def test_corrupt_artifact_and_nonempty_restore_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            backup = create_backup(self.repo(root), root / "backup", quiesced=True)
            valid_backup = create_backup(root / "repo", root / "valid-backup", quiesced=True)
            (backup / "refs.txt").write_text("corrupt\n")
            with self.assertRaises(BackupError):
                verify_backup(backup)
            destination = root / "destination"
            destination.mkdir()
            (destination / "existing").write_text("preserve\n")
            with self.assertRaises(BackupError):
                restore_backup(valid_backup, destination)

    def test_backup_destination_and_manifest_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            repo = self.repo(root)
            occupied = root / "occupied"
            occupied.mkdir()
            (occupied / "sentinel").write_text("preserve\n")
            with self.assertRaises(BackupError):
                create_backup(repo, occupied, quiesced=True)
            with self.assertRaises(BackupError):
                create_backup(repo, root / "backup", quiesced=False)
            backup = create_backup(repo, root / "backup", quiesced=True)
            (backup / "manifest.json").write_text("{}\n")
            with self.assertRaises(BackupError):
                verify_backup(backup)

    def test_dirty_repo_and_symlink_paths_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            repo = self.repo(root)
            (repo / "untracked").write_text("private\n")
            with self.assertRaises(BackupError):
                create_backup(repo, root / "backup", quiesced=True)
            destination = root / "destination"
            destination.mkdir()
            link = root / "link"
            link.symlink_to(destination, target_is_directory=True)
            other = root / "other"
            other.mkdir()
            with self.assertRaises(BackupError):
                create_backup(self.repo(other), link, quiesced=True)

    def test_manifest_size_and_artifact_set_are_strict(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            backup = create_backup(self.repo(root), root / "backup", quiesced=True)
            text = (backup / "manifest.json").read_text()
            self.assertIn('"size"', text)
            (backup / "manifest.json").write_text(text.replace('"index.txt"', '"extra.txt"', 1))
            with self.assertRaises(BackupError):
                verify_backup(backup)

    def test_failed_publication_and_restore_leave_no_destination(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            repo = self.repo(root)
            with (
                patch.object(MODULE, "_write_manifest"),
                patch.object(Path, "replace", side_effect=OSError("rename interrupted")),
                self.assertRaises(BackupError),
            ):
                create_backup(repo, root / "backup", quiesced=True)
            self.assertFalse((root / "backup").exists())
            backup = create_backup(repo, root / "valid", quiesced=True)
            with (
                patch.object(MODULE, "_run", side_effect=BackupError("clone interrupted")),
                self.assertRaises(BackupError),
            ):
                restore_backup(backup, root / "restored")
            self.assertFalse((root / "restored").exists())

    def test_restore_interruption_before_publication_leaves_no_destination(self) -> None:
        """A publication interruption cannot expose a partial restored authority."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            backup = create_backup(self.repo(root), root / "backup", quiesced=True)
            destination = root / "restored"
            with (
                patch.object(Path, "replace", side_effect=OSError("publication interrupted")),
                self.assertRaises(BackupError),
            ):
                restore_backup(backup, destination)
            self.assertFalse(destination.exists())

    def test_concurrent_restore_collision_preserves_existing_destination(self) -> None:
        """An absent destination is published by one racing restore only."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            backup = create_backup(self.repo(root), root / "backup", quiesced=True)
            destination = root / "restored"
            existence_barrier = Barrier(2)
            created_staging: list[Path] = []
            original_safe_root = MODULE._safe_root
            original_mkdtemp = MODULE.tempfile.mkdtemp

            def gated_safe_root(path: Path, label: str) -> None:
                original_safe_root(path, label)
                if path == destination:
                    existence_barrier.wait(timeout=5)

            def record_mkdtemp(*args: object, **kwargs: object) -> str:
                path = Path(original_mkdtemp(*args, **kwargs))
                if path.name.startswith(".git-restore-"):
                    created_staging.append(path)
                return str(path)

            with (
                patch.object(MODULE, "_safe_root", side_effect=gated_safe_root),
                patch.object(MODULE.tempfile, "mkdtemp", side_effect=record_mkdtemp),
                ThreadPoolExecutor(max_workers=2) as pool,
            ):
                futures = [pool.submit(restore_backup, backup, destination) for _ in range(2)]
                outcomes: list[type[Exception] | None] = []
                for future in futures:
                    try:
                        future.result()
                    except Exception as error:
                        outcomes.append(type(error))
                    else:
                        outcomes.append(None)

            self.assertCountEqual([None, BackupError], outcomes)
            self.assertEqual("state\n", (destination / "task.md").read_text(encoding="utf-8"))
            self.assertTrue(created_staging)
            self.assertTrue(all(not path.exists() for path in created_staging))

    def test_archive_path_traversal_and_restore_symlink_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            backup = create_backup(self.repo(root), root / "backup", quiesced=True)
            archive_path = backup / "tracked-tree.tar"
            with tarfile.open(archive_path, "w") as archive:
                info = tarfile.TarInfo("../escape")
                payload = b"unsafe"
                info.size = len(payload)
                archive.addfile(info, io.BytesIO(payload))
            manifest_path = backup / "manifest.json"
            manifest = json.loads(manifest_path.read_text())
            manifest["artifacts"]["tracked-tree.tar"] = {
                "sha256": hashlib.sha256(archive_path.read_bytes()).hexdigest(),
                "size": archive_path.stat().st_size,
            }
            manifest_path.write_text(json.dumps(manifest, sort_keys=True))
            with self.assertRaises(BackupError):
                verify_backup(backup)
            destination = root / "destination"
            destination.mkdir()
            link = root / "restore-link"
            link.symlink_to(destination, target_is_directory=True)
            other = root / "other"
            other.mkdir()
            valid = create_backup(self.repo(other), root / "valid", quiesced=True)
            with self.assertRaises(BackupError):
                restore_backup(valid, link)

    def test_symlinked_parent_components_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            repo = self.repo(root)
            real_parent = root / "real-parent"
            real_parent.mkdir()
            linked_parent = root / "linked-parent"
            linked_parent.symlink_to(real_parent, target_is_directory=True)
            with self.assertRaisesRegex(BackupError, "parent must not contain symlinks"):
                create_backup(repo, linked_parent / "backup", quiesced=True)
            backup = create_backup(repo, root / "valid-backup", quiesced=True)
            with self.assertRaisesRegex(BackupError, "parent must not contain symlinks"):
                restore_backup(backup, linked_parent / "restored")

    def test_manifest_and_clean_restore_equivalence_failures(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            backup = create_backup(self.repo(root), root / "backup", quiesced=True)

            def load() -> dict[str, object]:
                return cast(dict[str, object], json.loads((backup / "manifest.json").read_text()))

            def save(value: dict[str, object]) -> None:
                (backup / "manifest.json").write_text(json.dumps(value, sort_keys=True))

            manifest = load()
            manifest["schema_version"] = 2
            save(manifest)
            with self.assertRaises(BackupError):
                verify_backup(backup)
            manifest = load()
            manifest["schema_version"] = 1
            manifest["commit"] = "0" * 40
            save(manifest)
            with self.assertRaises(BackupError):
                verify_backup(backup)
            manifest = load()
            manifest["commit"] = "f" * 40
            save(manifest)
            with self.assertRaises(BackupError):
                verify_backup(backup)

    def test_restore_rejects_destination_creation_before_publication(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            repo = self.repo(root)
            backup = create_backup(repo, root / "backup", quiesced=True)
            destination = root / "restored"
            original_run = MODULE._run
            clone_count = 0

            def create_after_clone(command: list[str], cwd: Path) -> str:
                nonlocal clone_count
                result = cast(str, original_run(command, cwd))
                if command[:2] == ["git", "clone"]:
                    clone_count += 1
                    if clone_count == 2:
                        destination.mkdir()
                        (destination / "foreign.txt").write_text("foreign")
                return result

            with (
                patch.object(MODULE, "_run", side_effect=create_after_clone),
                self.assertRaisesRegex(BackupError, "destination appeared"),
            ):
                restore_backup(backup, destination)
            self.assertEqual("foreign", (destination / "foreign.txt").read_text())
            self.assertFalse(list(root.glob(".git-restore-*")))

    def test_create_rejects_destination_creation_before_publication(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            repo = self.repo(root)
            destination = root / "backup"
            original_manifest = MODULE._write_manifest

            def create_foreign(path: Path, value: dict[str, object]) -> None:
                original_manifest(path, value)
                destination.mkdir()
                (destination / "foreign.txt").write_text("foreign")

            with (
                patch.object(MODULE, "_write_manifest", side_effect=create_foreign),
                self.assertRaisesRegex(BackupError, "destination appeared"),
            ):
                create_backup(repo, destination, quiesced=True)
            self.assertEqual("foreign", (destination / "foreign.txt").read_text())
            self.assertFalse(list(root.glob(".git-backup-*")))

    def test_create_rejects_source_authority_mutation_before_publication(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            repo = self.repo(root)
            destination = root / "backup"
            original_manifest = MODULE._write_manifest

            def mutate_after_manifest(path: Path, value: dict[str, object]) -> None:
                original_manifest(path, value)
                (repo / "mutated.txt").write_text("changed")
                git("add", "mutated.txt", cwd=repo)
                git("commit", "-qm", "mutate during backup", cwd=repo)

            with (
                patch.object(MODULE, "_write_manifest", side_effect=mutate_after_manifest),
                self.assertRaisesRegex(BackupError, "source authority changed"),
            ):
                create_backup(repo, destination, quiesced=True)
            self.assertFalse(destination.exists())
            self.assertFalse(list(root.glob(".git-backup-*")))

    def test_create_rejects_source_repository_replacement_before_publication(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            repo = self.repo(root)
            replacement_root = root / "replacement-root"
            replacement_root.mkdir()
            replacement = self.repo(replacement_root)
            original = root / "original-repo"
            original_manifest = MODULE._write_manifest

            def replace_after_manifest(path: Path, value: dict[str, object]) -> None:
                original_manifest(path, value)
                repo.rename(original)
                repo.symlink_to(replacement, target_is_directory=True)

            with (
                patch.object(MODULE, "_write_manifest", side_effect=replace_after_manifest),
                self.assertRaisesRegex(BackupError, "source authority changed"),
            ):
                create_backup(repo, root / "backup", quiesced=True)
            self.assertFalse((root / "backup").exists())
            self.assertTrue(original.is_dir())


if __name__ == "__main__":
    unittest.main()
