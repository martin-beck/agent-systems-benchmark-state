# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Focused tests for the provisioned authority-lock foundation."""

from __future__ import annotations

import errno
import json
import os
import sqlite3
import tempfile
import unittest
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from tools import mutation_fence
from tools.mutation_fence import (
    MutationFence,
    MutationFenceError,
    provision,
    provision_control_binding,
)
from tools.sqlite_storage import SQLiteBackend, create_database
from tools.upgrade_identity import canonical_barrier_session_digest

AUTHORITATIVE_MUTATION_ROUTES = (
    "mutate",
    "update_observations",
    "append_command_result",
    "retire",
)
BARRIER_PROJECT = "00000000-0000-4000-8000-000000000002"


class MutationFenceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.directory = tempfile.TemporaryDirectory()
        self.root = Path(self.directory.name)
        self.root.chmod(0o700)
        self.authority = self.root / "coordinator.sqlite3"
        self.authority.write_bytes(b"existing authority")
        self.authority.chmod(0o600)
        self.marker = self.root / "upgrade-control-required.json"
        self.lifecycle = self.root / "wal-lifecycle.json"
        self.lock = self.root / "authority.lock"
        self.control = self.root / "control.sqlite3"
        connection = sqlite3.connect(self.control)
        self._create_barrier_table(connection)
        self._insert_barrier(connection, "released")
        connection.commit()
        connection.close()
        self.control.chmod(0o600)
        self.control_lock = self.root / "control.lock"
        self.control_binding = self.root / "control-binding.json"

    def tearDown(self) -> None:
        self.directory.cleanup()

    def test_provision_binds_existing_authority_and_lock(self) -> None:
        record = provision(
            self.authority, self.marker, self.lifecycle, self.lock, "project-public-id"
        )
        self.assertEqual("project-public-id", record["project_id"])
        self.assertEqual("clean_checkpointed", json.loads(self.lifecycle.read_text())["state"])
        with MutationFence(self.authority, self.marker, self.lifecycle, self.lock).locked():
            self.assertTrue(self.lock.exists())

    def test_unprovisioned_marker_is_rejected_by_seam(self) -> None:
        fence = MutationFence(self.authority, self.marker, self.lifecycle, self.lock)
        with self.assertRaisesRegex(MutationFenceError, "marker|missing"), fence.locked():
            pass
        self.assertTrue(self.authority.exists())

    def test_marker_tamper_and_authority_replacement_fail_closed(self) -> None:
        provision(self.authority, self.marker, self.lifecycle, self.lock, "project-public-id")
        replacement = self.root / "replacement"
        replacement.write_bytes(b"replacement")
        replacement.chmod(0o600)
        self.authority.unlink()
        replacement.rename(self.authority)
        with self.assertRaisesRegex(MutationFenceError, "identity"):
            MutationFence(self.authority, self.marker, self.lifecycle, self.lock)._verify()

        self.authority.unlink()
        self.authority.write_bytes(b"existing authority")
        self.authority.chmod(0o600)
        marker = json.loads(self.marker.read_text())
        marker["project_id"] = "other"
        self.marker.write_text(json.dumps(marker) + "\n")
        with self.assertRaisesRegex(MutationFenceError, "digest"):
            MutationFence(self.authority, self.marker, self.lifecycle, self.lock)._verify()

    def test_lock_replacement_fails_closed(self) -> None:
        provision(self.authority, self.marker, self.lifecycle, self.lock, "project-public-id")
        replacement = self.root / "replacement-lock"
        replacement.write_bytes(b"")
        replacement.chmod(0o600)
        self.lock.unlink()
        replacement.rename(self.lock)
        with self.assertRaisesRegex(MutationFenceError, "authority.lock identity"):
            MutationFence(self.authority, self.marker, self.lifecycle, self.lock)._verify()

    def test_malformed_lifecycle_is_fail_closed(self) -> None:
        provision(self.authority, self.marker, self.lifecycle, self.lock, "project-public-id")
        self.lifecycle.write_text("not-json\n")
        with self.assertRaisesRegex(MutationFenceError, "lifecycle is unreadable"):
            MutationFence(self.authority, self.marker, self.lifecycle, self.lock)._verify()

    def test_lifecycle_digest_and_project_id_are_validated(self) -> None:
        provision(self.authority, self.marker, self.lifecycle, self.lock, "project-public-id")
        lifecycle = json.loads(self.lifecycle.read_text())
        lifecycle["state"] = "active"
        self.lifecycle.write_text(json.dumps(lifecycle) + "\n")
        with self.assertRaisesRegex(MutationFenceError, "lifecycle digest"):
            MutationFence(self.authority, self.marker, self.lifecycle, self.lock)._verify()
        with self.assertRaisesRegex(MutationFenceError, "canonical and opaque"):
            provision(
                self.authority,
                self.root / "marker-2",
                self.root / "life-2",
                self.root / "lock-2",
                "path/id",
            )

    def test_marker_and_lifecycle_symlinks_are_rejected(self) -> None:
        provision(self.authority, self.marker, self.lifecycle, self.lock, "project-public-id")
        marker_copy = self.root / "marker-copy"
        marker_copy.write_bytes(self.marker.read_bytes())
        marker_copy.chmod(0o600)
        self.marker.unlink()
        self.marker.symlink_to(marker_copy)
        with self.assertRaisesRegex(MutationFenceError, "unreadable|descriptor"):
            MutationFence(self.authority, self.marker, self.lifecycle, self.lock)._verify()

        self.marker.unlink()
        marker_copy = self.root / "marker-copy-2"
        marker_copy.write_bytes(self.root.joinpath("marker-copy").read_bytes())
        marker_copy.chmod(0o600)
        marker_copy.rename(self.marker)
        lifecycle_copy = self.root / "lifecycle-copy"
        lifecycle_copy.write_bytes(self.lifecycle.read_bytes())
        lifecycle_copy.chmod(0o600)
        self.lifecycle.unlink()
        self.lifecycle.symlink_to(lifecycle_copy)
        with self.assertRaisesRegex(MutationFenceError, "unreadable|descriptor"):
            MutationFence(self.authority, self.marker, self.lifecycle, self.lock)._verify()

    def test_invalid_and_missing_paths_fail_closed(self) -> None:
        with self.assertRaisesRegex(MutationFenceError, "canonical"):
            provision(
                Path("relative.db"), self.marker, self.lifecycle, self.lock, "project-public-id"
            )
        with self.assertRaisesRegex(MutationFenceError, "missing"):
            provision(
                self.root / "missing.db",
                self.marker,
                self.lifecycle,
                self.lock,
                "project-public-id",
            )
        parent = self.root / "parent"
        parent.mkdir(mode=0o700)
        target = parent / "authority"
        target.write_bytes(b"authority")
        target.chmod(0o600)
        parent.chmod(0o755)
        with self.assertRaisesRegex(MutationFenceError, "owner-only"):
            provision(target, parent / "marker", parent / "lifecycle", parent / "lock", "project")

    def test_authority_and_lock_permissions_are_rejected(self) -> None:
        self.authority.chmod(0o644)
        with self.assertRaisesRegex(MutationFenceError, "owner-only"):
            provision(self.authority, self.marker, self.lifecycle, self.lock, "project")
        self.authority.chmod(0o600)
        self.lock.write_bytes(b"")
        self.lock.chmod(0o644)
        with self.assertRaisesRegex(MutationFenceError, "permissions"):
            provision(self.authority, self.marker, self.lifecycle, self.lock, "project")

    def test_existing_provisioning_is_idempotent_and_mismatch_rejected(self) -> None:
        first = provision(self.authority, self.marker, self.lifecycle, self.lock, "project")
        self.assertEqual(
            first, provision(self.authority, self.marker, self.lifecycle, self.lock, "project")
        )
        lifecycle = json.loads(self.lifecycle.read_text())
        lifecycle["generation"] = 1
        self.lifecycle.write_text(json.dumps(lifecycle) + "\n")
        with self.assertRaisesRegex(MutationFenceError, "already provisioned"):
            provision(self.authority, self.marker, self.lifecycle, self.lock, "project")

    def test_marker_and_lifecycle_schema_and_state_fail_closed(self) -> None:
        provision(self.authority, self.marker, self.lifecycle, self.lock, "project")
        self.marker.write_text("[]\n")
        self.marker.chmod(0o600)
        with self.assertRaisesRegex(MutationFenceError, "schema"):
            MutationFence(self.authority, self.marker, self.lifecycle, self.lock)._verify()
        self.marker.unlink()
        provision(self.authority, self.marker, self.lifecycle, self.lock, "project")
        lifecycle = json.loads(self.lifecycle.read_text())
        lifecycle["state"] = "bad"
        lifecycle["record_digest"] = mutation_fence._digest(
            {key: value for key, value in lifecycle.items() if key != "record_digest"}
        )
        self.lifecycle.write_text(json.dumps(lifecycle) + "\n")
        with self.assertRaisesRegex(MutationFenceError, "state"):
            MutationFence(self.authority, self.marker, self.lifecycle, self.lock)._verify()

    def test_marker_and_publication_failures_are_ambiguous(self) -> None:
        marker = self.root / "marker-existing"
        marker.write_text("{}\n")
        marker.chmod(0o600)
        with self.assertRaisesRegex(MutationFenceError, "another identity"):
            provision(self.authority, marker, self.lifecycle, self.lock, "project")
        with (
            patch.object(os, "rename", side_effect=OSError("rename failed")),
            self.assertRaisesRegex(MutationFenceError, "ambiguous"),
        ):
            provision(
                self.authority,
                self.root / "marker-new",
                self.root / "lifecycle-new",
                self.root / "lock-new",
                "project",
            )

    def test_lock_acquisition_errors_are_fail_closed(self) -> None:
        provision(self.authority, self.marker, self.lifecycle, self.lock, "project")
        with (
            patch(
                "tools.mutation_fence.fcntl.flock",
                side_effect=[OSError(errno.EACCES, "denied"), None],
            ),
            self.assertRaisesRegex(MutationFenceError, "acquisition"),
            MutationFence(self.authority, self.marker, self.lifecycle, self.lock).locked(),
        ):
            pass

    def test_control_binding_descriptor_is_project_bound_and_idempotent(self) -> None:
        record = provision_control_binding(
            self.control, self.control_binding, self.control_lock, "project"
        )
        self.assertEqual(
            record,
            provision_control_binding(
                self.control, self.control_binding, self.control_lock, "project"
            ),
        )
        self.assertTrue(str(record["identity_digest"]).startswith("sha256:"))
        changed = json.loads(self.control_binding.read_text())
        changed["project_id"] = "other"
        self.control_binding.write_text(json.dumps(changed) + "\n")
        with self.assertRaisesRegex(MutationFenceError, "another identity"):
            provision_control_binding(
                self.control, self.control_binding, self.control_lock, "project"
            )

    def _fenced(self) -> MutationFence:
        provision(self.authority, self.marker, self.lifecycle, self.lock, BARRIER_PROJECT)
        provision_control_binding(
            self.control, self.control_binding, self.control_lock, BARRIER_PROJECT
        )
        return MutationFence(
            self.authority,
            self.marker,
            self.lifecycle,
            self.lock,
            self.control,
            self.control_binding,
            self.control_lock,
        )

    @staticmethod
    def _create_barrier_table(
        connection: sqlite3.Connection, *, project_primary_key: bool = True
    ) -> None:
        project_constraint = " PRIMARY KEY" if project_primary_key else " NOT NULL"
        connection.execute(
            f"""CREATE TABLE barrier_session (
                schema_version INTEGER NOT NULL,
                project_id TEXT{project_constraint},
                attempt_id TEXT NOT NULL,
                state_revision INTEGER NOT NULL,
                authority_revision_at_acquire TEXT NOT NULL,
                durable_barrier_id TEXT NOT NULL,
                fencing_token TEXT NOT NULL,
                fencing_owner TEXT NOT NULL,
                identity_digest TEXT NOT NULL,
                status TEXT NOT NULL,
                revision INTEGER NOT NULL,
                forward_child TEXT,
                rollback_child TEXT
            )"""
        )

    @staticmethod
    def _insert_barrier(connection: sqlite3.Connection, status: object) -> None:
        identity: dict[str, object] = {
            "schema_version": 1,
            "project_id": BARRIER_PROJECT,
            "attempt_id": "attempt-1",
            "state_revision": 1,
            "authority_revision_at_acquire": "authority-1",
            "durable_barrier_id": "barrier-1",
            "fencing_token": "fence-1",
            "fencing_owner": "owner-1",
            "identity_digest": "0" * 64,
        }
        identity["identity_digest"] = canonical_barrier_session_digest(identity)
        connection.execute(
            "INSERT INTO barrier_session VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (*identity.values(), status, 1, None, None),
        )

    def _set_barrier(self, status: str | None) -> None:
        connection = sqlite3.connect(self.control)
        connection.execute("DELETE FROM barrier_session WHERE project_id=?", (BARRIER_PROJECT,))
        if status is not None:
            self._insert_barrier(connection, status)
        connection.commit()
        connection.close()

    def test_scope_rejects_missing_and_nonreleased_barriers(self) -> None:
        fence = self._fenced()

        @contextmanager
        def common() -> Iterator[object]:
            yield None

        for status in (None, "held", "releasing", "ambiguous"):
            self._set_barrier(status)

            with (
                self.subTest(status=status),
                self.assertRaisesRegex(MutationFenceError, "rejected|missing"),
                fence.mutation_scope(common),
            ):
                pass
        self._set_barrier("released")
        with fence.mutation_scope(common):
            pass

    def test_scope_is_nonreentrant_and_sqlite_route_uses_it(self) -> None:
        fence = self._fenced()

        @contextmanager
        def common() -> Iterator[object]:
            yield None

        with (
            fence.mutation_scope(common),
            self.assertRaisesRegex(MutationFenceError, "non-reentrant"),
            fence.mutation_scope(common),
        ):
            pass
        database = self.root / "backend.sqlite3"
        binding = {
            "project_id": BARRIER_PROJECT,
            "state_repository": "owner/state",
            "product_repository": "owner/product",
        }
        create_database(
            database,
            binding,
            [],
            imported_at="2026-09-14T00:00:00+00:00",
            source_backend="git",
            source_checkpoint="a" * 40,
        )
        backend_marker = self.root / "backend-marker.json"
        backend_lifecycle = self.root / "backend-lifecycle.json"
        backend_lock = self.root / "backend-authority.lock"
        provision(database, backend_marker, backend_lifecycle, backend_lock, BARRIER_PROJECT)
        backend_fence = MutationFence(
            database,
            backend_marker,
            backend_lifecycle,
            backend_lock,
            self.control,
            self.control_binding,
            self.control_lock,
        )

        @contextmanager
        def route_scope() -> Iterator[object]:
            with backend_fence.mutation_scope(common):
                yield None

        backend = SQLiteBackend(database, binding, self.root, mutation_scope=route_scope)
        with backend.transaction() as connection:
            self.assertEqual(
                "active",
                connection.execute("SELECT value FROM metadata WHERE key='state'").fetchone()[0],
            )
        blocked = SQLiteBackend(
            database,
            binding,
            self.root,
            mutation_scope=lambda: backend_fence.mutation_scope(common),
        )
        self._set_barrier("held")
        with self.assertRaisesRegex(MutationFenceError, "rejected"), blocked.transaction():
            pass

    def test_every_authoritative_route_enters_the_shared_fence_scope(self) -> None:
        """Inventory contract: every SQLite writer crosses the injected seam."""
        database = self.root / "route-inventory.sqlite3"
        binding = {
            "project_id": "00000000-0000-4000-8000-000000000001",
            "state_repository": "owner/state",
            "product_repository": "owner/product",
        }
        create_database(
            database,
            binding,
            [],
            imported_at="2026-09-14T00:00:00+00:00",
            source_backend="git",
            source_checkpoint="a" * 40,
        )
        entered: list[str] = []

        class RejectingScope:
            def __enter__(self) -> object:
                entered.append("scope")
                raise MutationFenceError("route admission is not provisioned")

            def __exit__(self, *_args: object) -> None:
                return None

        def route_scope() -> RejectingScope:
            return RejectingScope()

        backend = SQLiteBackend(database, binding, self.root, mutation_scope=route_scope)
        calls = {
            "mutate": lambda: backend.mutate(
                "AR-0001",
                1,
                "claim",
                "2026-09-14T00:00:00+00:00",
                lambda _meta, _tasks: ("", ""),
            ),
            "update_observations": lambda: backend.update_observations(
                {}, "2026-09-14T00:00:00+00:00"
            ),
            "append_command_result": lambda: backend.append_command_result(
                "AR-0001", "owner", "hash", 0, "ok", "2026-09-14T00:00:00+00:00"
            ),
            "retire": lambda: backend.retire(lambda _tasks: None, lambda: None),
        }
        for route in AUTHORITATIVE_MUTATION_ROUTES:
            with (
                self.subTest(route=route),
                self.assertRaisesRegex(MutationFenceError, "not provisioned"),
            ):
                calls[route]()
        self.assertEqual(len(AUTHORITATIVE_MUTATION_ROUTES), len(entered))

    def test_durable_barrier_read_failures_are_fail_closed(self) -> None:
        fence = self._fenced()

        @contextmanager
        def common() -> Iterator[object]:
            yield None

        connection = sqlite3.connect(self.control)
        connection.execute("DROP TABLE barrier_session")
        self._create_barrier_table(connection, project_primary_key=False)
        self._insert_barrier(connection, "released")
        self._insert_barrier(connection, "released")
        connection.commit()
        connection.close()
        with (
            self.assertRaisesRegex(MutationFenceError, "state is invalid"),
            fence.mutation_scope(common),
        ):
            pass
        self._set_barrier("held")
        connection = sqlite3.connect(self.control)
        connection.execute(
            "UPDATE barrier_session SET status=? WHERE project_id=?",
            (sqlite3.Binary(b"x"), BARRIER_PROJECT),
        )
        connection.commit()
        connection.close()
        with (
            self.assertRaisesRegex(MutationFenceError, "state is invalid"),
            fence.mutation_scope(common),
        ):
            pass
        self.control.write_bytes(b"not sqlite")
        self.control.chmod(0o600)
        with self.assertRaisesRegex(MutationFenceError, "unreadable"), fence.mutation_scope(common):
            pass

    def test_control_store_symlink_and_replacement_are_rejected(self) -> None:
        fence = self._fenced()
        copy = self.root / "control-copy.sqlite3"
        copy.write_bytes(self.control.read_bytes())
        copy.chmod(0o600)
        self.control.unlink()
        self.control.symlink_to(copy)
        with self.assertRaisesRegex(MutationFenceError, "identity|unreadable|descriptor"):
            fence._read_barrier_status()
        original = self.root / "control-original.sqlite3"
        self.control.rename(original)
        replacement = self.root / "control-replacement.sqlite3"
        replacement.write_bytes(copy.read_bytes())
        replacement.chmod(0o600)
        replacement.rename(self.control)
        with self.assertRaisesRegex(MutationFenceError, "identity"):
            fence._read_barrier_status()

    def test_binding_replacement_during_control_open_is_rejected(self) -> None:
        fence = self._fenced()
        original = self.control_binding.read_bytes()
        replacement = self.root / "control-binding-replacement.json"
        replacement.write_bytes(original)
        replacement.chmod(0o600)
        moved = self.root / "control-binding-original.json"
        replaced = False
        real_open = os.open

        def replacing_open(
            path: str | bytes | os.PathLike[str] | os.PathLike[bytes],
            flags: int,
            *args: int,
            **kwargs: int,
        ) -> int:
            nonlocal replaced
            if path == self.control.name and not replaced:
                self.control_binding.rename(moved)
                replacement.rename(self.control_binding)
                replaced = True
            return real_open(path, flags, *args, **kwargs)

        with (
            patch.object(os, "open", side_effect=replacing_open),
            self.assertRaisesRegex(MutationFenceError, "control binding identity changed"),
        ):
            fence._read_barrier_status()
        self.assertTrue(replaced)

    def test_binding_snapshot_schema_and_size_are_fail_closed(self) -> None:
        fence = self._fenced()
        original = self.control_binding.read_bytes()
        changed = json.loads(original)
        changed["project_id"] = "other"
        changed["identity_digest"] = mutation_fence._digest(
            {key: value for key, value in changed.items() if key != "identity_digest"}
        )
        cases = [
            (b"[]", "schema is invalid"),
            (b"{", "unreadable"),
            (json.dumps({"project_id": "project"}).encode(), "digest is invalid"),
            (json.dumps(changed).encode(), "project identity changed"),
            (b"x" * (1 << 20) + b"y", "too large"),
        ]
        try:
            for content, message in cases:
                self.control_binding.write_bytes(content)
                self.control_binding.chmod(0o600)
                with self.assertRaisesRegex(MutationFenceError, message):
                    fence._read_barrier_status()
        finally:
            self.control_binding.write_bytes(original)
            self.control_binding.chmod(0o600)

    def test_binding_permission_and_parent_failures_are_rejected(self) -> None:
        fence = self._fenced()
        self.control_binding.chmod(0o644)
        with self.assertRaisesRegex(MutationFenceError, "owner-only"):
            fence._read_barrier_status()
        self.control_binding.chmod(0o600)
        missing_parent = self.root / "missing" / "control.sqlite3"
        missing_fence = MutationFence(
            self.authority,
            self.marker,
            self.lifecycle,
            self.lock,
            control_store=missing_parent,
            control_binding=self.control_binding,
            control_lock=self.control_lock,
        )
        with self.assertRaises(OSError):
            missing_fence._read_barrier_status()

    def test_binding_content_rewrite_after_control_read_is_rejected(self) -> None:
        fence = self._fenced()
        real_open = os.open
        real_read = os.read
        binding_fd: int | None = None
        binding_reads = 0

        def tracking_open(
            path: str | bytes | os.PathLike[str] | os.PathLike[bytes],
            flags: int,
            *args: int,
            **kwargs: int,
        ) -> int:
            nonlocal binding_fd
            descriptor = real_open(path, flags, *args, **kwargs)
            if path == self.control_binding.name:
                binding_fd = descriptor
            return descriptor

        def rewriting_read(fd: int, size: int) -> bytes:
            nonlocal binding_reads
            value = real_read(fd, size)
            if fd == binding_fd:
                binding_reads += 1
                if binding_reads == 3:
                    return b"rewritten"
            return value

        with (
            patch.object(os, "open", side_effect=tracking_open),
            patch.object(os, "read", side_effect=rewriting_read),
            self.assertRaisesRegex(MutationFenceError, "contents changed"),
        ):
            fence._read_barrier_status()

    def test_missing_binding_and_process_busy_are_rejected(self) -> None:
        provision(self.authority, self.marker, self.lifecycle, self.lock, BARRIER_PROJECT)
        incomplete = MutationFence(
            self.authority,
            self.marker,
            self.lifecycle,
            self.lock,
            control_store=self.control,
        )

        @contextmanager
        def common() -> Iterator[object]:
            yield None

        with (
            self.assertRaisesRegex(MutationFenceError, "prerequisites"),
            incomplete.mutation_scope(common),
        ):
            pass
        fence = self._fenced()
        fence._process_lock.acquire()
        try:
            with self.assertRaisesRegex(MutationFenceError, "busy"), fence.mutation_scope(common):
                pass
        finally:
            fence._process_lock.release()

    def test_record_permissions_and_descriptor_races_fail_closed(self) -> None:
        provision(self.authority, self.marker, self.lifecycle, self.lock, "project")
        self.marker.chmod(0o644)
        with self.assertRaisesRegex(MutationFenceError, "owner-only"):
            MutationFence(self.authority, self.marker, self.lifecycle, self.lock)._verify()
        self.marker.chmod(0o600)
        parent_status = self.root.stat()
        file_status = self.marker.stat()
        changed_status = self.authority.stat()
        with (
            patch.object(
                os, "fstat", side_effect=[parent_status, file_status, changed_status, parent_status]
            ),
            self.assertRaisesRegex(MutationFenceError, "identity changed"),
        ):
            mutation_fence._read_json(self.marker, "marker")
        changed_parent = SimpleNamespace(
            st_dev=parent_status.st_dev, st_ino=parent_status.st_ino + 1
        )
        with (
            patch.object(
                os,
                "fstat",
                side_effect=[
                    parent_status,
                    file_status,
                    file_status,
                    changed_parent,
                    changed_parent,
                ],
            ),
            self.assertRaisesRegex(MutationFenceError, "parent identity changed"),
        ):
            mutation_fence._read_json(self.marker, "marker")

    def test_path_lock_and_publication_failure_branches(self) -> None:
        symlink = self.root / "authority-link"
        symlink.symlink_to(self.authority)
        with self.assertRaisesRegex(MutationFenceError, "descriptor"):
            provision(symlink, self.marker, self.lifecycle, self.lock, "project")
        lock_link = self.root / "lock-link"
        lock_link.symlink_to(self.authority)
        with self.assertRaisesRegex(MutationFenceError, "cannot be provisioned"):
            provision(self.authority, self.marker, self.lifecycle, lock_link, "project")
        with (
            patch.object(os, "fsync", side_effect=[None, None, OSError("fsync failed")]),
            self.assertRaisesRegex(MutationFenceError, "ambiguous"),
        ):
            provision(
                self.authority,
                self.root / "marker-fsync",
                self.root / "lifecycle-fsync",
                self.root / "lock-fsync",
                "project",
            )

    def test_marker_schema_identity_and_lifecycle_binding_fail_closed(self) -> None:
        provision(self.authority, self.marker, self.lifecycle, self.lock, "project")
        marker = json.loads(self.marker.read_text())
        marker["schema_version"] = 2
        marker["identity_digest"] = mutation_fence._digest(
            {key: value for key, value in marker.items() if key != "identity_digest"}
        )
        self.marker.write_text(json.dumps(marker) + "\n")
        with self.assertRaisesRegex(MutationFenceError, "unsupported"):
            MutationFence(self.authority, self.marker, self.lifecycle, self.lock)._verify()
        marker["schema_version"] = 1
        marker["project_id"] = "bad/id"
        marker["identity_digest"] = mutation_fence._digest(
            {key: value for key, value in marker.items() if key != "identity_digest"}
        )
        self.marker.write_text(json.dumps(marker) + "\n")
        with self.assertRaisesRegex(MutationFenceError, "canonical"):
            MutationFence(self.authority, self.marker, self.lifecycle, self.lock)._verify()

        self.marker.unlink()
        provision(self.authority, self.marker, self.lifecycle, self.lock, "project")
        lifecycle = json.loads(self.lifecycle.read_text())
        lifecycle["authority_digest"] = "sha256:" + "0" * 64
        lifecycle["record_digest"] = mutation_fence._digest(
            {key: value for key, value in lifecycle.items() if key != "record_digest"}
        )
        self.lifecycle.write_text(json.dumps(lifecycle) + "\n")
        with self.assertRaisesRegex(MutationFenceError, "binding"):
            MutationFence(self.authority, self.marker, self.lifecycle, self.lock)._verify()

    def test_lock_identity_and_unexpected_lock_errors_fail_closed(self) -> None:
        provision(self.authority, self.marker, self.lifecycle, self.lock, "project")
        record = json.loads(self.marker.read_text())
        with (
            patch.object(MutationFence, "_verify", return_value=record),
            patch.object(mutation_fence, "_read_json", return_value=record),
            patch.object(
                mutation_fence,
                "_identity",
                return_value=mutation_fence.DescriptorIdentity(0, 0, 0, 0, 0, 0, 0),
            ),
            self.assertRaisesRegex(MutationFenceError, "identity changed"),
            MutationFence(self.authority, self.marker, self.lifecycle, self.lock).locked(),
        ):
            pass
        with (
            patch(
                "tools.mutation_fence.fcntl.flock",
                side_effect=[OSError(errno.EIO, "io"), None],
            ),
            self.assertRaises(OSError),
            MutationFence(self.authority, self.marker, self.lifecycle, self.lock).locked(),
        ):
            pass


if __name__ == "__main__":
    unittest.main()
