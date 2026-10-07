# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Tests for the separate versioned runtime selector contract."""

# Test setup invokes fixed Git commands against isolated temporary repositories.
# ruff: noqa: S603, S607

from __future__ import annotations

import importlib
import json
import multiprocessing
import os
import signal
import subprocess
import sys
import tempfile
import time
import unittest
from contextlib import contextmanager
from pathlib import Path
from types import SimpleNamespace
from typing import Any
from unittest.mock import MagicMock, patch

from tools import upgrade_authority
from tools.admission_lease import AdmissionLease, validate_recheck
from tools.upgrade_authority import (
    AuthorityError,
    SelectorPublicationAmbiguousError,
    commit_runtime_selector,
    commit_runtime_selector_admitted,
    read_git_authority_snapshot,
    read_runtime_selector,
    reconcile_runtime_selector,
)


def _init_git_repo(root: Path) -> None:
    subprocess.run(["git", "init", "-q", str(root)], check=True)
    (root / ".git").chmod(0o700)
    (root / "state").write_text("clean\n")
    subprocess.run(["git", "-C", str(root), "add", "state"], check=True)
    subprocess.run(
        [
            "git",
            "-C",
            str(root),
            "-c",
            "user.name=test",
            "-c",
            "user.email=test@example",
            "commit",
            "-qm",
            "init",
        ],
        check=True,
    )


def _publish_selector_then_die(path_text: str) -> None:
    path = Path(path_text)
    real_fsync = os.fsync
    calls = 0

    def crash_after_rename(descriptor: int) -> None:
        nonlocal calls
        calls += 1
        if calls == 2:
            os.kill(os.getpid(), signal.SIGKILL)
        real_fsync(descriptor)

    with patch("tools.upgrade_authority.os.fsync", side_effect=crash_after_rename):
        commit_runtime_selector(path, "new", "old")


def _publish_selector_before_fsync_then_die(path_text: str) -> None:
    path = Path(path_text)

    def crash_before_file_fsync(_descriptor: int) -> None:
        os.kill(os.getpid(), signal.SIGKILL)

    with patch("tools.upgrade_authority.os.fsync", side_effect=crash_before_file_fsync):
        commit_runtime_selector(path, "new", "old")


def _publish_selector_after_directory_fsync_then_die(path_text: str) -> None:
    path = Path(path_text)
    real_fsync = os.fsync
    calls = 0

    def crash_after_directory_fsync(descriptor: int) -> None:
        nonlocal calls
        calls += 1
        real_fsync(descriptor)
        if calls == 2:
            os.kill(os.getpid(), signal.SIGKILL)

    with patch("tools.upgrade_authority.os.fsync", side_effect=crash_after_directory_fsync):
        commit_runtime_selector(path, "new", "old")


def _publish_selector_after_final_recheck_then_die(path_text: str) -> None:
    path = Path(path_text)
    original_recheck = upgrade_authority._recheck_parent
    calls = 0

    def crash_after_recheck(selector: Path, identity: tuple[int, int]) -> None:
        nonlocal calls
        original_recheck(selector, identity)
        calls += 1
        if calls == 2:
            os.kill(os.getpid(), signal.SIGKILL)

    with patch.object(upgrade_authority, "_recheck_parent", side_effect=crash_after_recheck):
        commit_runtime_selector(path, "new", "old")


def _publish_selector_after_identity_validation_then_die(path_text: str) -> None:
    path = Path(path_text)
    original_identity = (path.stat().st_dev, path.stat().st_ino)
    real_close = os.close

    def crash_after_identity_validation(descriptor: int) -> None:
        try:
            descriptor_path = Path(f"/proc/self/fd/{descriptor}").readlink()
        except OSError:
            descriptor_path = None
        if descriptor_path == path:
            descriptor_status = os.fstat(descriptor)
            if (descriptor_status.st_dev, descriptor_status.st_ino) != original_identity:
                os.kill(os.getpid(), signal.SIGKILL)
        real_close(descriptor)

    with patch("tools.upgrade_authority.os.close", side_effect=crash_after_identity_validation):
        commit_runtime_selector(path, "new", "old")


def _publish_selector_directory_fsync_failure(path_text: str) -> None:
    path = Path(path_text)
    real_fsync = os.fsync
    calls = 0

    def fail_directory_fsync(descriptor: int) -> None:
        nonlocal calls
        calls += 1
        if calls == 2:
            raise OSError("injected directory fsync failure")
        real_fsync(descriptor)

    with patch("tools.upgrade_authority.os.fsync", side_effect=fail_directory_fsync):
        commit_runtime_selector(path, "new", "old")


def _publish_selector_final_recheck_failure(path_text: str) -> None:
    path = Path(path_text)
    original_recheck = upgrade_authority._recheck_parent
    calls = 0

    def fail_final_recheck(selector: Path, identity: tuple[int, int]) -> None:
        nonlocal calls
        calls += 1
        if calls == 2:
            raise AuthorityError("injected final parent identity failure")
        original_recheck(selector, identity)

    with patch.object(upgrade_authority, "_recheck_parent", side_effect=fail_final_recheck):
        commit_runtime_selector(path, "new", "old")


def _reconcile_selector_in_child(path_text: str, result_text: str) -> None:
    result = reconcile_runtime_selector(
        Path(path_text),
        before_active_release="old",
        before_previous_release="older",
        after_active_release="new",
        after_previous_release="old",
    )
    Path(result_text).write_text(result, encoding="utf-8")


def _reconcile_and_verify_selector_in_child(path_text: str, result_text: str) -> None:
    path = Path(path_text)
    result = reconcile_runtime_selector(
        path,
        before_active_release="old",
        before_previous_release="older",
        after_active_release="new",
        after_previous_release="old",
    )
    selector = read_runtime_selector(path)
    Path(result_text).write_text(
        f"{result}:{selector['active_release']}:{selector['previous_release']}",
        encoding="utf-8",
    )


def _replace_selector_parent_after_marker(
    parent_text: str, marker_text: str, replaced_text: str, displaced_text: str
) -> None:
    parent = Path(parent_text)
    marker = Path(marker_text)
    deadline = time.monotonic() + 10
    while not marker.exists():
        if time.monotonic() >= deadline:
            raise RuntimeError("cleanup marker was not published")
        time.sleep(0.001)
    displaced = Path(displaced_text)
    parent.rename(displaced)
    parent.mkdir(mode=0o700)
    Path(replaced_text).write_text("replaced\n", encoding="utf-8")


class RuntimeSelectorTests(unittest.TestCase):
    def test_low_level_authority_helpers_reject_hostile_selector_inputs(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            root.mkdir(exist_ok=True)
            selector = root / "selector.json"
            selector.write_text("not-json", encoding="utf-8")
            parent = os.open(root, os.O_RDONLY | os.O_DIRECTORY)
            try:
                with self.assertRaisesRegex(AuthorityError, "unreadable"):
                    upgrade_authority._read_runtime_selector_at(parent, selector.name)
                with self.assertRaisesRegex(AuthorityError, "unavailable"):
                    upgrade_authority._read_runtime_selector_at(parent, "missing.json")
                with self.assertRaisesRegex(AuthorityError, "parent identity changed"):
                    upgrade_authority._open_regular(selector, expected_parent=(0, 0))
                self.assertIsNone(upgrade_authority._existing_regular_identity(parent, "missing"))
                upgrade_authority._remove_selector_temporary(parent, "missing.tmp")
            finally:
                os.close(parent)

    def test_low_level_selector_helpers_reject_invalid_schema_and_nonregular_files(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            parent = os.open(root, os.O_RDONLY | os.O_DIRECTORY)
            try:
                selector = root / "selector.json"
                for value in (
                    {"schema_version": 2, "active_release": "new", "previous_release": "old"},
                    {"schema_version": 1, "active_release": "same", "previous_release": "same"},
                    {"schema_version": 1, "active_release": "bad value", "previous_release": "old"},
                ):
                    selector.write_text(json.dumps(value), encoding="utf-8")
                    with self.assertRaisesRegex(AuthorityError, "identity"):
                        upgrade_authority._read_runtime_selector_at(parent, selector.name)
                selector.unlink()
                selector.mkdir()
                with self.assertRaisesRegex(AuthorityError, "descriptor is unsafe"):
                    upgrade_authority._read_runtime_selector_at(parent, selector.name)
            finally:
                os.close(parent)

    def test_git_snapshot_binds_clean_head_and_requested_ref(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            subprocess.run(["git", "init", "-q", str(root)], check=True)
            (root / ".git").chmod(0o700)
            (root / "state").write_text("clean\n")
            subprocess.run(["git", "-C", str(root), "add", "state"], check=True)
            subprocess.run(
                [
                    "git",
                    "-C",
                    str(root),
                    "-c",
                    "user.name=test",
                    "-c",
                    "user.email=test@example",
                    "commit",
                    "-qm",
                    "init",
                ],
                check=True,
            )
            snapshot = read_git_authority_snapshot(root, "HEAD")
            self.assertTrue(snapshot.clean)
            self.assertEqual(snapshot.head, snapshot.requested_ref_head)
            self.assertEqual("master", snapshot.branch)
            subprocess.run(["git", "-C", str(root), "tag", "v1"], check=True)
            (root / "state").write_text("second\n")
            subprocess.run(["git", "-C", str(root), "add", "state"], check=True)
            subprocess.run(
                [
                    "git",
                    "-C",
                    str(root),
                    "-c",
                    "user.name=test",
                    "-c",
                    "user.email=test@example",
                    "commit",
                    "-qm",
                    "second",
                ],
                check=True,
            )
            tagged = read_git_authority_snapshot(root, "refs/tags/v1")
            self.assertNotEqual(tagged.head, tagged.requested_ref_head)
            self.assertEqual(snapshot.head, tagged.requested_ref_head)

    def test_git_snapshot_rejects_dirty_detached_or_unreachable_ref(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            subprocess.run(["git", "init", "-q", str(root)], check=True)
            (root / ".git").chmod(0o700)
            (root / "state").write_text("clean\n")
            subprocess.run(["git", "-C", str(root), "add", "state"], check=True)
            subprocess.run(
                [
                    "git",
                    "-C",
                    str(root),
                    "-c",
                    "user.name=test",
                    "-c",
                    "user.email=test@example",
                    "commit",
                    "-qm",
                    "init",
                ],
                check=True,
            )
            (root / "state").write_text("dirty\n")
            with self.assertRaisesRegex(AuthorityError, "not clean"):
                read_git_authority_snapshot(root)
            (root / "state").write_text("clean\n")
            subprocess.run(
                ["git", "-C", str(root), "checkout", "-q", "--detach", "HEAD"], check=True
            )
            with self.assertRaisesRegex(AuthorityError, "inspection was rejected"):
                read_git_authority_snapshot(root)
            with self.assertRaisesRegex(AuthorityError, "ref is invalid"):
                read_git_authority_snapshot(root, "--upload-pack=evil")

    def test_git_snapshot_rejects_missing_or_unsafe_repository(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with self.assertRaisesRegex(AuthorityError, "repository is unavailable"):
                read_git_authority_snapshot(root)
            subprocess.run(["git", "init", "-q", str(root)], check=True)
            (root / ".git").chmod(0o777)
            with self.assertRaisesRegex(AuthorityError, "owner-safe"):
                read_git_authority_snapshot(root)

    def test_git_snapshot_rejects_unreachable_requested_branch(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            subprocess.run(["git", "init", "-q", str(root)], check=True)
            (root / ".git").chmod(0o700)
            (root / "state").write_text("clean\n")
            subprocess.run(["git", "-C", str(root), "add", "state"], check=True)
            subprocess.run(
                [
                    "git",
                    "-C",
                    str(root),
                    "-c",
                    "user.name=test",
                    "-c",
                    "user.email=test@example",
                    "commit",
                    "-qm",
                    "init",
                ],
                check=True,
            )
            subprocess.run(
                ["git", "-C", str(root), "checkout", "-q", "--orphan", "other"], check=True
            )
            subprocess.run(["git", "-C", str(root), "rm", "-q", "-rf", "."], check=True)
            (root / "state").write_text("other\n")
            subprocess.run(["git", "-C", str(root), "add", "state"], check=True)
            subprocess.run(
                [
                    "git",
                    "-C",
                    str(root),
                    "-c",
                    "user.name=test",
                    "-c",
                    "user.email=test@example",
                    "commit",
                    "-qm",
                    "other",
                ],
                check=True,
            )
            with self.assertRaisesRegex(AuthorityError, "not reachable"):
                read_git_authority_snapshot(root, "refs/heads/master")

    def test_git_snapshot_normalizes_observation_and_reachability_failures(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            _init_git_repo(root)
            with (
                patch("tools.upgrade_authority.subprocess.run", side_effect=OSError("git")),
                self.assertRaisesRegex(AuthorityError, "inspection failed"),
            ):
                read_git_authority_snapshot(root)

            real_run = subprocess.run

            def reject_reachability(*args: Any, **kwargs: Any) -> Any:
                if "merge-base" in args[0]:
                    return subprocess.CompletedProcess(args[0], 1, "", "unreachable")
                return real_run(*args, **kwargs)

            with (
                patch("tools.upgrade_authority.subprocess.run", side_effect=reject_reachability),
                self.assertRaisesRegex(AuthorityError, "not reachable"),
            ):
                read_git_authority_snapshot(root)

            with (
                patch("tools.upgrade_authority.os.geteuid", return_value=os.geteuid() + 1),
                self.assertRaisesRegex(AuthorityError, "owner-safe"),
            ):
                read_git_authority_snapshot(root)

            def fail_check(*args: Any, **kwargs: Any) -> Any:
                if "merge-base" in args[0]:
                    raise OSError("git unavailable")
                return real_run(*args, **kwargs)

            with (
                patch("tools.upgrade_authority.subprocess.run", side_effect=fail_check),
                self.assertRaisesRegex(AuthorityError, "inspection failed"),
            ):
                read_git_authority_snapshot(root)

    def test_git_snapshot_rejects_identity_and_observation_drift(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            _init_git_repo(root)
            real_stat = Path.stat
            real_identity = upgrade_authority._file_identity
            initial_identity_seen = False

            def fail_reread(*args: Any, **_kwargs: Any) -> os.stat_result:
                if initial_identity_seen:
                    raise OSError("replaced")
                return real_stat(args[0] if args else root)

            def mark_initial(status: os.stat_result) -> tuple[int, int]:
                nonlocal initial_identity_seen
                initial_identity_seen = True
                return real_identity(status)

            with (
                patch.object(Path, "stat", side_effect=fail_reread),
                patch("tools.upgrade_authority._file_identity", side_effect=mark_initial),
                self.assertRaisesRegex(AuthorityError, "identity reread failed"),
            ):
                read_git_authority_snapshot(root)

            with (
                patch(
                    "tools.upgrade_authority._file_identity",
                    side_effect=[(1, 1), (2, 2), (1, 1), (3, 3)],
                ),
                self.assertRaisesRegex(AuthorityError, "identity changed"),
            ):
                read_git_authority_snapshot(root)

            real_run = subprocess.run
            head_calls = 0

            def drift_head(*args: Any, **kwargs: Any) -> Any:
                nonlocal head_calls
                if "HEAD^{commit}" in args[0]:
                    head_calls += 1
                    if head_calls == 2:
                        return subprocess.CompletedProcess(args[0], 0, "0" * 40 + "\n", "")
                return real_run(*args, **kwargs)

            with (
                patch("tools.upgrade_authority.subprocess.run", side_effect=drift_head),
                self.assertRaisesRegex(AuthorityError, "observation changed"),
            ):
                read_git_authority_snapshot(root)

    def test_admitted_selector_publication_requires_typed_ordered_lease(self) -> None:
        class Lease:
            def __init__(self, *, ordered: bool = True) -> None:
                self.events: list[str] = []
                self.ordered = ordered

            @contextmanager
            def hold(self) -> Any:
                self.events.append("hold")
                yield None
                self.events.append("release")

            def assert_ordered(self) -> None:
                self.events.append("assert-order")
                if not self.ordered or self.events != ["assert-order"]:
                    raise AuthorityError("selector admission lock order is invalid")

        lease = AdmissionLease(
            project_id="project",
            authority_revision="authority-1",
            fencing_token="fence-1",  # noqa: S106
            fencing_owner="owner-1",
            durable_barrier_id="barrier-1",
            revision=1,
        )
        recheck = validate_recheck(
            lease,
            project_id="project",
            authority_revision="authority-1",
            fencing_token="fence-1",  # noqa: S106
            fencing_owner="owner-1",
            durable_barrier_id="barrier-1",
            revision=1,
        )

        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "selector.json"
            with self.assertRaisesRegex(AuthorityError, "lease is required"):
                commit_runtime_selector_admitted(path, "new", "old", None, recheck, Lease())  # type: ignore[arg-type]
            with self.assertRaisesRegex(AuthorityError, "lease is required"):
                commit_runtime_selector_admitted(path, "new", "old", object(), recheck, Lease())  # type: ignore[arg-type]

            unordered = Lease(ordered=False)
            with self.assertRaisesRegex(AuthorityError, "lock order is invalid"):
                commit_runtime_selector_admitted(path, "new", "old", lease, recheck, unordered)
            self.assertFalse(path.exists())

            other_lease = AdmissionLease(
                project_id="project",
                authority_revision="authority-1",
                fencing_token="fence-2",  # noqa: S106
                fencing_owner="owner-1",
                durable_barrier_id="barrier-2",
                revision=2,
            )
            other_recheck = validate_recheck(
                other_lease,
                project_id="project",
                authority_revision="authority-1",
                fencing_token="fence-2",  # noqa: S106
                fencing_owner="owner-1",
                durable_barrier_id="barrier-2",
                revision=2,
            )
            valid = Lease()
            with self.assertRaisesRegex(AuthorityError, "does not match"):
                commit_runtime_selector_admitted(path, "new", "old", lease, other_recheck, valid)
            self.assertFalse(path.exists())

            commit_runtime_selector_admitted(path, "new", "old", lease, recheck, valid)
            self.assertEqual(
                ["assert-order", "hold", "release"],
                valid.events,
            )
            self.assertEqual("new", read_runtime_selector(path)["active_release"])

    def test_handoffctl_is_package_safe(self) -> None:
        module = importlib.import_module("tools.handoffctl")
        self.assertTrue(callable(module.backend_selection))

    def test_handoffctl_script_mode_keeps_fallback(self) -> None:
        root = Path(__file__).resolve().parents[1]
        result = subprocess.run(
            [sys.executable, str(root / "tools" / "handoffctl.py"), "--help"],
            cwd=root,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, result.returncode, result.stderr)

    def test_inspect_authority_classifies_git_and_sqlite_paths(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            fake = MagicMock()
            fake.ROOT = root
            fake.project_binding.return_value = {
                "project_id": "11111111" "-1111-4111-8111-111111111111",
                "state_repository": "owner/state",
                "product_repository": "owner/product",
            }
            fake._assert_storage_binding.return_value = None
            fake.backend_selection.return_value = {"backend": "git", "legacy": False}
            with (
                patch.object(upgrade_authority, "_handoffctl", return_value=fake),
                patch("tools.upgrade_authority.subprocess.run") as run,
            ):
                run.return_value.stdout = ""
                result = upgrade_authority.inspect_authority()
                self.assertTrue(result["state_clean"])
                self.assertEqual("git", result["backend"])
            fake.backend_selection.return_value = {"backend": "sqlite", "legacy": True}
            fake.storage_backend.return_value.load_tasks.return_value = [1, 2]
            with patch.object(upgrade_authority, "_handoffctl", return_value=fake):
                result = upgrade_authority.inspect_authority()
            self.assertTrue(result["state_clean"])
            self.assertEqual(2, result["task_count"])

    def test_inspect_authority_rejects_dirty_git_and_failed_sqlite(self) -> None:
        fake = MagicMock()
        fake.ROOT = Path()
        fake.project_binding.return_value = {
            "project_id": "11111111" "-1111-4111-8111-111111111111",
            "state_repository": "owner/state",
            "product_repository": "owner/product",
        }
        fake.backend_selection.return_value = {"backend": "git", "legacy": False}
        with (
            patch.object(upgrade_authority, "_handoffctl", return_value=fake),
            patch("tools.upgrade_authority.subprocess.run") as run,
        ):
            run.return_value.stdout = " M tasks/AR-0001.md\n"
            with self.assertRaisesRegex(AuthorityError, "Git authority is dirty"):
                upgrade_authority.inspect_authority()
        fake.backend_selection.return_value = {"backend": "sqlite", "legacy": False}
        fake.storage_backend.side_effect = RuntimeError("database unavailable")
        with (
            patch.object(upgrade_authority, "_handoffctl", return_value=fake),
            self.assertRaisesRegex(AuthorityError, "SQLite authority inspection failed"),
        ):
            upgrade_authority.inspect_authority()

    def test_atomic_selector_round_trip_and_strict_schema(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "runtime-selector.json"
            commit_runtime_selector(path, "release-new", "release-old")
            self.assertEqual("release-new", read_runtime_selector(path)["active_release"])
            path.write_text('{"active_release":"new"}\n')
            with self.assertRaises(AuthorityError):
                read_runtime_selector(path)

    def test_selector_rejects_symlink_and_empty_identity(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "selector.json"
            with self.assertRaises(AuthorityError):
                commit_runtime_selector(path, "", "old")
            target = root / "target"
            target.write_text("{}\n")
            path.symlink_to(target)
            with self.assertRaises(AuthorityError):
                commit_runtime_selector(path, "new", "old")

    def test_selector_rejects_duplicate_active_and_previous_identity(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "selector.json"
            with self.assertRaisesRegex(AuthorityError, "selector identity"):
                commit_runtime_selector(path, "new", "new")
            path.write_text(
                '{"schema_version":1,"active_release":"new","previous_release":"new"}\n',
                encoding="utf-8",
            )
            path.chmod(0o600)
            with self.assertRaisesRegex(AuthorityError, "selector identity"):
                read_runtime_selector(path)

    def test_selector_rejects_control_characters_and_unbounded_release_ids(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "selector.json"
            for release in ("with space", "with\nnewline", "with/slash", "x" * 129, 1):
                with self.subTest(release=release), self.assertRaises(AuthorityError):
                    commit_runtime_selector(path, release, "old")  # type: ignore[arg-type]
            path.write_text(
                '{"schema_version":1,"active_release":"bad\\nvalue","previous_release":"old"}\n'
            )
            with self.assertRaisesRegex(AuthorityError, "selector identity"):
                read_runtime_selector(path)

    def test_postrename_fsync_failure_requires_exact_reconciliation(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "selector.json"
            commit_runtime_selector(path, "old", "older")
            real_fsync = os.fsync
            calls = 0

            def fail_directory_fsync(descriptor: int) -> None:
                nonlocal calls
                calls += 1
                if calls == 2:
                    raise OSError("directory fsync failed")
                real_fsync(descriptor)

            with (
                patch("tools.upgrade_authority.os.fsync", side_effect=fail_directory_fsync),
                self.assertRaisesRegex(SelectorPublicationAmbiguousError, "reconcile"),
            ):
                commit_runtime_selector(path, "new", "old")
            handoffctl = MagicMock()
            with patch.object(upgrade_authority, "_handoffctl", return_value=handoffctl):
                self.assertEqual(
                    "committed",
                    reconcile_runtime_selector(
                        path,
                        before_active_release="old",
                        before_previous_release="older",
                        after_active_release="new",
                        after_previous_release="old",
                    ),
                )
            self.assertEqual(
                {"selector.json"},
                {entry.name for entry in path.parent.iterdir()},
            )

            handoffctl.locked.assert_called_once_with()
            handoffctl.locked.return_value.__enter__.assert_called_once_with()
            commit_runtime_selector(path, "old", "older")
            self.assertEqual(
                "not-committed",
                reconcile_runtime_selector(
                    path,
                    before_active_release="old",
                    before_previous_release="older",
                    after_active_release="new",
                    after_previous_release="old",
                ),
            )
            commit_runtime_selector(path, "unexpected", "pair")
            with self.assertRaisesRegex(AuthorityError, "unknown release identity"):
                reconcile_runtime_selector(
                    path,
                    before_active_release="old",
                    before_previous_release="older",
                    after_active_release="new",
                    after_previous_release="old",
                )

    def test_child_death_after_selector_rename_is_reconcilable(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "selector.json"
            commit_runtime_selector(path, "old", "older")
            process = multiprocessing.get_context("fork").Process(
                target=_publish_selector_then_die, args=(str(path),)
            )
            process.start()
            process.join(timeout=10)
            self.assertEqual(-signal.SIGKILL, process.exitcode)
            result = root / "result"
            verifier = multiprocessing.get_context("fork").Process(
                target=_reconcile_and_verify_selector_in_child, args=(str(path), str(result))
            )
            verifier.start()
            verifier.join(timeout=10)
            self.assertEqual(0, verifier.exitcode)
            self.assertEqual("committed:new:old", result.read_text(encoding="utf-8"))
            self.assertEqual({"selector.json", "result"}, {entry.name for entry in root.iterdir()})

    def test_child_death_before_selector_rename_preserves_old_pair(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "selector.json"
            commit_runtime_selector(path, "old", "older")
            process = multiprocessing.get_context("fork").Process(
                target=_publish_selector_before_fsync_then_die, args=(str(path),)
            )
            process.start()
            process.join(timeout=10)
            self.assertEqual(-signal.SIGKILL, process.exitcode)
            result = root / "result"
            verifier = multiprocessing.get_context("fork").Process(
                target=_reconcile_selector_in_child, args=(str(path), str(result))
            )
            verifier.start()
            verifier.join(timeout=10)
            self.assertEqual(0, verifier.exitcode)
            self.assertEqual("not-committed", result.read_text(encoding="utf-8"))
            self.assertEqual({"selector.json", "result"}, {entry.name for entry in root.iterdir()})
            with self.assertRaisesRegex(AuthorityError, "identities are invalid"):
                reconcile_runtime_selector(
                    path,
                    before_active_release="same",
                    before_previous_release="pair",
                    after_active_release="same",
                    after_previous_release="pair",
                )

    def test_child_death_after_directory_fsync_reconciles_new_pair(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "selector.json"
            commit_runtime_selector(path, "old", "older")
            process = multiprocessing.get_context("fork").Process(
                target=_publish_selector_after_directory_fsync_then_die, args=(str(path),)
            )
            process.start()
            process.join(timeout=10)
            self.assertEqual(-signal.SIGKILL, process.exitcode)
            result = root / "result"
            verifier = multiprocessing.get_context("fork").Process(
                target=_reconcile_and_verify_selector_in_child, args=(str(path), str(result))
            )
            verifier.start()
            verifier.join(timeout=10)
            self.assertEqual(0, verifier.exitcode)
            self.assertEqual("committed:new:old", result.read_text(encoding="utf-8"))
            self.assertEqual({"selector.json", "result"}, {entry.name for entry in root.iterdir()})

    def test_child_death_after_final_recheck_reconciles_new_pair(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "selector.json"
            commit_runtime_selector(path, "old", "older")
            process = multiprocessing.get_context("fork").Process(
                target=_publish_selector_after_final_recheck_then_die, args=(str(path),)
            )
            process.start()
            process.join(timeout=10)
            self.assertEqual(-signal.SIGKILL, process.exitcode)
            result = root / "result"
            verifier = multiprocessing.get_context("fork").Process(
                target=_reconcile_and_verify_selector_in_child, args=(str(path), str(result))
            )
            verifier.start()
            verifier.join(timeout=10)
            self.assertEqual(0, verifier.exitcode)
            self.assertEqual("committed:new:old", result.read_text(encoding="utf-8"))
            self.assertEqual({"selector.json", "result"}, {entry.name for entry in root.iterdir()})

    def test_child_death_after_identity_validation_reconciles_new_pair(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "selector.json"
            commit_runtime_selector(path, "old", "older")
            process = multiprocessing.get_context("fork").Process(
                target=_publish_selector_after_identity_validation_then_die, args=(str(path),)
            )
            process.start()
            process.join(timeout=10)
            self.assertEqual(-signal.SIGKILL, process.exitcode)
            result = root / "result"
            verifier = multiprocessing.get_context("fork").Process(
                target=_reconcile_and_verify_selector_in_child, args=(str(path), str(result))
            )
            verifier.start()
            verifier.join(timeout=10)
            self.assertEqual(0, verifier.exitcode)
            self.assertEqual("committed:new:old", result.read_text(encoding="utf-8"))
            self.assertEqual({"selector.json", "result"}, {entry.name for entry in root.iterdir()})

    def test_directory_fsync_failure_reconciles_new_pair(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "selector.json"
            commit_runtime_selector(path, "old", "older")
            process = multiprocessing.get_context("fork").Process(
                target=_publish_selector_directory_fsync_failure, args=(str(path),)
            )
            process.start()
            process.join(timeout=10)
            self.assertNotEqual(0, process.exitcode)
            result = root / "result"
            verifier = multiprocessing.get_context("fork").Process(
                target=_reconcile_and_verify_selector_in_child, args=(str(path), str(result))
            )
            verifier.start()
            verifier.join(timeout=10)
            self.assertEqual(0, verifier.exitcode)
            self.assertEqual("committed:new:old", result.read_text(encoding="utf-8"))
            self.assertEqual({"selector.json", "result"}, {entry.name for entry in root.iterdir()})

    def test_final_recheck_failure_reconciles_new_pair(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "selector.json"
            commit_runtime_selector(path, "old", "older")
            process = multiprocessing.get_context("fork").Process(
                target=_publish_selector_final_recheck_failure, args=(str(path),)
            )
            process.start()
            process.join(timeout=10)
            self.assertNotEqual(0, process.exitcode)
            result = root / "result"
            verifier = multiprocessing.get_context("fork").Process(
                target=_reconcile_and_verify_selector_in_child, args=(str(path), str(result))
            )
            verifier.start()
            verifier.join(timeout=10)
            self.assertEqual(0, verifier.exitcode)
            self.assertEqual("committed:new:old", result.read_text(encoding="utf-8"))
            self.assertEqual({"selector.json", "result"}, {entry.name for entry in root.iterdir()})

    def test_selector_recovery_rejects_unsafe_abandoned_temporary(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "selector.json"
            commit_runtime_selector(path, "old", "older")
            target = root / "secret"
            target.write_text("must remain\n", encoding="utf-8")
            temporary = root / ".selector.json.0123456789abcdef0123456789abcdef"
            temporary.symlink_to(target)
            with self.assertRaisesRegex(AuthorityError, "temporary is unsafe"):
                reconcile_runtime_selector(
                    path,
                    before_active_release="old",
                    before_previous_release="older",
                    after_active_release="new",
                    after_previous_release="old",
                )
            self.assertTrue(temporary.is_symlink())
            self.assertEqual("must remain\n", target.read_text(encoding="utf-8"))

    def test_selector_recovery_cleans_regular_temporary(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "selector.json"
            commit_runtime_selector(path, "old", "older")
            temporary = root / ".selector.json.0123456789abcdef0123456789abcdef"
            temporary.write_bytes(b"staged\n")
            temporary.chmod(0o600)
            self.assertEqual(
                "not-committed",
                reconcile_runtime_selector(
                    path,
                    before_active_release="old",
                    before_previous_release="older",
                    after_active_release="new",
                    after_previous_release="old",
                ),
            )
            self.assertFalse(temporary.exists())

    def test_selector_recovery_rejects_non_private_temporary(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "selector.json"
            commit_runtime_selector(path, "old", "older")
            temporary = root / ".selector.json.0123456789abcdef0123456789abcdef"
            temporary.write_bytes(b"staged\n")
            temporary.chmod(0o644)
            with self.assertRaisesRegex(AuthorityError, "temporary is unsafe"):
                reconcile_runtime_selector(
                    path,
                    before_active_release="old",
                    before_previous_release="older",
                    after_active_release="new",
                    after_previous_release="old",
                )
            self.assertTrue(temporary.exists())

    def test_selector_recovery_fails_closed_on_cleanup_errors(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "selector.json"
            commit_runtime_selector(path, "old", "older")
            temporary = root / ".selector.json.0123456789abcdef0123456789abcdef"
            temporary.write_bytes(b"staged\n")
            temporary.chmod(0o600)
            with (
                patch("tools.upgrade_authority.os.unlink", side_effect=OSError("unlink")),
                self.assertRaisesRegex(AuthorityError, "temporary cleanup failed"),
            ):
                reconcile_runtime_selector(
                    path,
                    before_active_release="old",
                    before_previous_release="older",
                    after_active_release="new",
                    after_previous_release="old",
                )
            with (
                patch("tools.upgrade_authority.os.fsync", side_effect=OSError("fsync")),
                self.assertRaisesRegex(AuthorityError, "temporary cleanup is ambiguous"),
            ):
                reconcile_runtime_selector(
                    path,
                    before_active_release="old",
                    before_previous_release="older",
                    after_active_release="new",
                    after_previous_release="old",
                )

    def test_selector_recovery_fails_closed_on_temporary_inventory_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "selector.json"
            commit_runtime_selector(path, "old", "older")
            with (
                patch("tools.upgrade_authority.os.listdir", side_effect=OSError("inventory")),
                self.assertRaisesRegex(AuthorityError, "temporary inventory failed"),
            ):
                reconcile_runtime_selector(
                    path,
                    before_active_release="old",
                    before_previous_release="older",
                    after_active_release="new",
                    after_previous_release="old",
                )

    def test_selector_recovery_rechecks_parent_after_cleanup(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "selector.json"
            commit_runtime_selector(path, "old", "older")
            temporary = root / ".selector.json.0123456789abcdef0123456789abcdef"
            temporary.write_bytes(b"staged\n")
            temporary.chmod(0o600)

            def fail_after_cleanup(selector: Path, identity: tuple[int, int]) -> None:
                del selector, identity
                raise AuthorityError("runtime selector parent identity changed")

            with (
                patch.object(upgrade_authority, "_recheck_parent", side_effect=fail_after_cleanup),
                self.assertRaisesRegex(AuthorityError, "parent identity changed"),
            ):
                reconcile_runtime_selector(
                    path,
                    before_active_release="old",
                    before_previous_release="older",
                    after_active_release="new",
                    after_previous_release="old",
                )
            self.assertFalse(temporary.exists())

    def test_selector_recovery_rechecks_selector_after_cleanup(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "selector.json"
            commit_runtime_selector(path, "old", "older")
            with (
                patch.object(
                    upgrade_authority,
                    "_read_runtime_selector_at",
                    return_value={"active_release": "new", "previous_release": "old"},
                ),
                self.assertRaisesRegex(AuthorityError, "changed during reconciliation"),
            ):
                reconcile_runtime_selector(
                    path,
                    before_active_release="old",
                    before_previous_release="older",
                    after_active_release="new",
                    after_previous_release="old",
                )

    def test_selector_descriptor_reader_rejects_boundary_failures(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            parent = os.open(root, os.O_RDONLY | os.O_DIRECTORY)
            try:
                with self.assertRaisesRegex(AuthorityError, "unavailable"):
                    upgrade_authority._read_runtime_selector_at(parent, "missing.json")
                target = root / "selector.json"
                target.write_text("{}\n", encoding="utf-8")
                target.chmod(0o600)
                with self.assertRaisesRegex(AuthorityError, "schema is invalid"):
                    upgrade_authority._read_runtime_selector_at(parent, "selector.json")
                target.unlink()
                target.mkdir(mode=0o700)
                with self.assertRaisesRegex(AuthorityError, "descriptor is unsafe"):
                    upgrade_authority._read_runtime_selector_at(parent, "selector.json")
                target.rmdir()
                target.write_text("{\n", encoding="utf-8")
                target.chmod(0o600)
                with self.assertRaisesRegex(AuthorityError, "unreadable"):
                    upgrade_authority._read_runtime_selector_at(parent, "selector.json")
                target.write_text(
                    '{"schema_version":1,"active_release":"bad value",'
                    '"previous_release":"older"}\n',
                    encoding="utf-8",
                )
                with self.assertRaisesRegex(AuthorityError, "identity is invalid"):
                    upgrade_authority._read_runtime_selector_at(parent, "selector.json")
                target.unlink()
                target.symlink_to(root / "other")
                (root / "other").write_text("{}\n", encoding="utf-8")
                with self.assertRaisesRegex(AuthorityError, "descriptor is unsafe"):
                    upgrade_authority._read_runtime_selector_at(parent, "selector.json")
                target.unlink()
                target.write_text("{}\n", encoding="utf-8")
                target.chmod(0o600)
                target.write_text("x" * (64 * 1024 + 1), encoding="utf-8")
                with self.assertRaisesRegex(AuthorityError, "too large"):
                    upgrade_authority._read_runtime_selector_at(parent, "selector.json")
                target.write_text(
                    '{"schema_version":1,"active_release":"old","previous_release":"older"}\n',
                    encoding="utf-8",
                )
                descriptor = os.open(target, os.O_RDONLY | os.O_NOFOLLOW)
                try:
                    status = os.fstat(descriptor)
                    altered = SimpleNamespace(
                        st_dev=status.st_dev,
                        st_ino=status.st_ino + 1,
                        st_mode=status.st_mode,
                        st_nlink=status.st_nlink,
                    )
                finally:
                    os.close(descriptor)
                with (
                    patch(
                        "tools.upgrade_authority.os.fstat",
                        side_effect=[status, altered],
                    ),
                    self.assertRaisesRegex(AuthorityError, "identity changed"),
                ):
                    upgrade_authority._read_runtime_selector_at(parent, "selector.json")
            finally:
                os.close(parent)

    def test_selector_recovery_rejects_same_pair_parent_swap(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            parent = root / "runtime"
            parent.mkdir(mode=0o700)
            path = parent / "selector.json"
            commit_runtime_selector(path, "old", "older")
            displaced = root / "displaced"
            original = upgrade_authority._recheck_parent
            calls = 0

            def swap_after_first_recheck(selector: Path, identity: tuple[int, int]) -> None:
                nonlocal calls
                calls += 1
                original(selector, identity)
                if calls != 1:
                    return
                parent.rename(displaced)
                parent.mkdir(mode=0o700)
                commit_runtime_selector(parent / "selector.json", "old", "older")

            with (
                patch.object(
                    upgrade_authority,
                    "_recheck_parent",
                    side_effect=swap_after_first_recheck,
                ),
                self.assertRaisesRegex(AuthorityError, "parent identity changed"),
            ):
                reconcile_runtime_selector(
                    path,
                    before_active_release="old",
                    before_previous_release="older",
                    after_active_release="new",
                    after_previous_release="old",
                )
            self.assertEqual(
                "old", read_runtime_selector(displaced / "selector.json")["active_release"]
            )

    def test_selector_recovery_rejects_real_parent_swap_after_cleanup(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            parent = root / "runtime"
            parent.mkdir(mode=0o700)
            path = parent / "selector.json"
            commit_runtime_selector(path, "old", "older")
            temporary = parent / ".selector.json.0123456789abcdef0123456789abcdef"
            temporary.write_bytes(b"staged\n")
            temporary.chmod(0o600)
            marker = root / "cleanup-started"
            replaced = root / "replacement-complete"
            displaced = root / "displaced"
            attacker = multiprocessing.get_context("fork").Process(
                target=_replace_selector_parent_after_marker,
                args=(str(parent), str(marker), str(replaced), str(displaced)),
            )
            attacker.start()
            real_fsync = os.fsync

            def release_for_parent_swap(descriptor: int) -> None:
                real_fsync(descriptor)
                marker.write_text("ready\n", encoding="utf-8")
                deadline = time.monotonic() + 10
                while not replaced.exists():
                    if time.monotonic() >= deadline:
                        raise RuntimeError("parent replacement did not complete")
                    time.sleep(0.001)

            with (
                patch("tools.upgrade_authority.os.fsync", side_effect=release_for_parent_swap),
                self.assertRaisesRegex(AuthorityError, "parent identity changed"),
            ):
                reconcile_runtime_selector(
                    path,
                    before_active_release="old",
                    before_previous_release="older",
                    after_active_release="new",
                    after_previous_release="old",
                )
            attacker.join(timeout=10)
            self.assertEqual(0, attacker.exitcode)
            self.assertEqual(
                "old", read_runtime_selector(displaced / "selector.json")["active_release"]
            )
            self.assertFalse((displaced / temporary.name).exists())

    def test_ambiguous_selector_cleanup_failure_preserves_classification(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "selector.json"
            commit_runtime_selector(path, "old", "older")
            real_fsync = os.fsync
            calls = 0

            def fail_directory_fsync(descriptor: int) -> None:
                nonlocal calls
                calls += 1
                if calls == 2:
                    raise OSError("directory fsync failed")
                real_fsync(descriptor)

            with (
                patch("tools.upgrade_authority.os.fsync", side_effect=fail_directory_fsync),
                patch("tools.upgrade_authority.os.unlink", side_effect=OSError("cleanup failed")),
                self.assertRaisesRegex(
                    SelectorPublicationAmbiguousError, "temporary cleanup failed"
                ),
            ):
                commit_runtime_selector(path, "new", "old")
            self.assertEqual("new", read_runtime_selector(path)["active_release"])

    def test_selector_publication_requires_private_real_ancestors(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            public = root / "public"
            public.mkdir(mode=0o755)
            public.chmod(0o755)
            with self.assertRaisesRegex(AuthorityError, "owner-only provisioned"):
                commit_runtime_selector(public / "selector.json", "new", "old")
            self.assertFalse((public / "selector.json").exists())
            (public / "selector.json").write_text(
                '{"schema_version":1,"active_release":"new","previous_release":"old"}\n'
            )
            with self.assertRaisesRegex(AuthorityError, "owner-only provisioned"):
                read_runtime_selector(public / "selector.json")

            private = root / "private"
            private.mkdir(mode=0o700)
            linked = root / "linked"
            linked.symlink_to(private, target_is_directory=True)
            with self.assertRaisesRegex(AuthorityError, "parent descriptor is unsafe"):
                commit_runtime_selector(linked / "selector.json", "new", "old")
            self.assertFalse((private / "selector.json").exists())

    def test_selector_publication_detects_parent_replacement_before_commit(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            parent = root / "runtime"
            parent.mkdir(mode=0o700)
            selector = parent / "selector.json"
            commit_runtime_selector(selector, "old", "older")
            displaced = root / "displaced"
            original_recheck = upgrade_authority._recheck_parent

            def replace_parent(path: Path, identity: tuple[int, int]) -> None:
                parent.rename(displaced)
                parent.mkdir(mode=0o700)
                original_recheck(path, identity)

            with (
                patch.object(upgrade_authority, "_recheck_parent", side_effect=replace_parent),
                self.assertRaisesRegex(AuthorityError, "publication failed"),
            ):
                commit_runtime_selector(selector, "new", "old")
            self.assertFalse(selector.exists())
            self.assertEqual(
                "old", read_runtime_selector(displaced / "selector.json")["active_release"]
            )
            self.assertFalse(
                any(path.name.startswith(".selector.json.") for path in displaced.iterdir())
            )


if __name__ == "__main__":
    unittest.main()
