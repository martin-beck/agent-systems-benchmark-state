# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Exact canonical-envelope tests for upgrade and rollback identities."""

from __future__ import annotations

import unittest

from tools.upgrade_identity import (
    BARRIER_SESSION_IDENTITY_FIELDS,
    ENVELOPE_FIELDS,
    BarrierChildIdentity,
    BarrierSessionIdentity,
    UpgradeIdentityError,
    canonical_barrier_digest,
    canonical_barrier_session_digest,
    canonical_envelope_digest,
    validate_barrier_session_identity,
    validate_envelope,
)


def envelope() -> dict[str, object]:
    value: dict[str, object] = {
        "schema_version": 2,
        "backend": "sqlite",
        "project_id": "11111111-1111-4111-8111-111111111111",
        "operation_id": "op-1",
        "state_revision": 1,
        "authority_revision": "authority-1",
        "fencing_token": "fence-1",
        "fencing_owner": "owner-1",
        "durable_barrier_id": "barrier-1",
        "artifact_root": "/artifacts",
        "source": "/authority.sqlite",
        "destination": "/artifacts/backup.sqlite",
        "manifest": "/artifacts/manifest.json",
        "selector_ref": ".runtime/runtime-selector.json",
        "barrier_identity_digest": "0" * 64,
        "target": "rollback",
        "envelope_digest": "0" * 64,
    }
    value["barrier_identity_digest"] = canonical_barrier_digest(value)
    value["envelope_digest"] = canonical_envelope_digest(value)
    return value


def barrier_session() -> dict[str, object]:
    value: dict[str, object] = {
        "schema_version": 1,
        "project_id": "11111111-1111-4111-8111-111111111111",
        "attempt_id": "attempt-1",
        "state_revision": 3,
        "authority_revision_at_acquire": "authority-3",
        "durable_barrier_id": "barrier-1",
        "fencing_token": "fence-1",
        "fencing_owner": "owner-1",
        "identity_digest": "0" * 64,
    }
    value["identity_digest"] = canonical_barrier_session_digest(value)
    return value


class UpgradeIdentityTests(unittest.TestCase):
    def test_v10_typed_identity_round_trip_and_child_rejections(self) -> None:
        value = barrier_session()
        identity = BarrierSessionIdentity.from_record(value)
        self.assertEqual(value, identity.as_record())
        child = BarrierChildIdentity.bind(identity, "child-1", "new")
        child.validate_for(identity)
        with self.assertRaises(UpgradeIdentityError):
            BarrierChildIdentity.bind(identity, "", "new")
        with self.assertRaises(UpgradeIdentityError):
            BarrierChildIdentity.bind(identity, "child-1", "other")
        with self.assertRaises(UpgradeIdentityError):
            BarrierChildIdentity("child-1", "new", "0" * 64).validate_for(identity)
        with self.assertRaisesRegex(UpgradeIdentityError, "operation identity"):
            BarrierChildIdentity("!invalid", "new", identity.identity_digest).validate_for(identity)
        with self.assertRaisesRegex(UpgradeIdentityError, "target"):
            BarrierChildIdentity("child-1", "other", identity.identity_digest).validate_for(
                identity
            )

    def test_v10_typed_identity_rejects_noncanonical_records(self) -> None:
        value = barrier_session()
        identity_errors = (
            {**value, "schema_version": 2},
            {**value, "project_id": 42},
            {**value, "project_id": "not-a-uuid"},
            {**value, "project_id": "11111111-1111-1111-8111-111111111111"},
            {**value, "attempt_id": ""},
            {**value, "state_revision": 0},
            {**value, "state_revision": True},
            {**value, "identity_digest": "x" * 64},
            {**value, "identity_digest": "f" * 64},
        )
        for invalid in identity_errors:
            with self.subTest(invalid=invalid), self.assertRaises(UpgradeIdentityError):
                BarrierSessionIdentity.from_record(invalid)

    def test_v10_barrier_session_is_target_neutral(self) -> None:
        value = barrier_session()
        self.assertEqual(set(BARRIER_SESSION_IDENTITY_FIELDS) | {"identity_digest"}, set(value))
        self.assertEqual(value, validate_barrier_session_identity(value))
        self.assertEqual(value["identity_digest"], canonical_barrier_session_digest(value))

    def test_v10_barrier_session_digest_excludes_child_operation_fields(self) -> None:
        value = barrier_session()
        self.assertEqual(
            value["identity_digest"],
            canonical_barrier_session_digest({**value, "child_target": "new"}),
        )
        for field in BARRIER_SESSION_IDENTITY_FIELDS:
            changed = dict(value)
            changed[field] = (
                9 if field == "schema_version" else (0 if field == "state_revision" else "!")
            )
            with self.subTest(field=field), self.assertRaises(UpgradeIdentityError):
                changed["identity_digest"] = canonical_barrier_session_digest(changed)
                validate_barrier_session_identity(changed)

    def test_v10_barrier_session_rejects_mutable_or_unknown_fields(self) -> None:
        value = barrier_session()
        with self.assertRaises(UpgradeIdentityError):
            validate_barrier_session_identity({**value, "status": "held"})
        with self.assertRaises(UpgradeIdentityError):
            validate_barrier_session_identity({**value, "identity_digest": "f" * 64})

    def test_exact_v9_canonical_digests_are_stable(self) -> None:
        value = envelope()
        self.assertEqual(
            "b677eeb69a6f99864d74b091fbe3568ed2f1273a6580fc54243218f1fa6a1c81",
            value["barrier_identity_digest"],
        )
        self.assertEqual(
            "0cba5194ced5b74a07f5093f0b79a5e5f4f6df0556731a5b4e93e561c30dbde6",
            value["envelope_digest"],
        )
        self.assertEqual(set(ENVELOPE_FIELDS), set(validate_envelope(value)))

    def test_barrier_tuple_excludes_envelope_only_fields_but_binds_v9_target(self) -> None:
        value = envelope()
        original = canonical_barrier_digest(value)
        self.assertEqual(original, canonical_barrier_digest({**value, "backend": "git"}))
        self.assertEqual(
            original,
            canonical_barrier_digest({**value, "destination": "/artifacts/other.sqlite"}),
        )
        self.assertNotEqual(original, canonical_barrier_digest({**value, "target": "new"}))

    def test_every_envelope_field_is_bound_and_unknown_fields_are_rejected(self) -> None:
        value = envelope()
        for field in ENVELOPE_FIELDS:
            changed = dict(value)
            changed[field] = 3 if field in {"schema_version", "state_revision"} else "tampered"
            with self.subTest(field=field), self.assertRaises(UpgradeIdentityError):
                validate_envelope(changed)
        with self.assertRaises(UpgradeIdentityError):
            validate_envelope({**value, "unexpected": True})

    def test_noncanonical_and_overlapping_paths_are_rejected(self) -> None:
        for field, path in (
            ("artifact_root", "/artifacts/../escape"),
            ("artifact_root", "//artifacts"),
            ("source", "relative.sqlite"),
            ("destination", "/outside/backup.sqlite"),
            ("manifest", "/artifacts/backup.sqlite/manifest.json"),
            ("selector_ref", "../runtime-selector.json"),
            ("selector_ref", "/etc/runtime-selector.json"),
            ("selector_ref", "runtime/./selector.json"),
        ):
            changed = {**envelope(), field: path}
            changed["barrier_identity_digest"] = canonical_barrier_digest(changed)
            changed["envelope_digest"] = canonical_envelope_digest(changed)
            with self.subTest(field=field), self.assertRaises(UpgradeIdentityError):
                validate_envelope(changed)


if __name__ == "__main__":
    unittest.main()
