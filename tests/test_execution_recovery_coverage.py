# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Focused coverage for bounded execution reservation recovery."""

from __future__ import annotations

import argparse
import datetime as dt
import unittest
from types import SimpleNamespace
from unittest.mock import patch

from tools import execution_abandonment, execution_lifecycle


RESERVATION = {
    "execution_id": "a" * 32,
    "owner": "worker-a",
    "task_revision": 4,
    "envelope_digest": "sha256:" + "b" * 64,
    "command_class": "test",
    "scope_digest": "sha256:" + "c" * 64,
    "argv_digest": "d" * 64,
    "expires_at": "2999-01-01T00:00:00+00:00",
}


def abandonment_args(**changes: object) -> SimpleNamespace:
    values = {
        "execution_id": RESERVATION["execution_id"],
        "owner": "worker-a",
        "evidence_ref": "recovery/AR-0001-expired",
        "evidence_digest": "sha256:" + "e" * 64,
        "allow_legacy_without_identity": False,
        "classification": "EXIT",
        "returncode": 0,
        "recorded_at": "2026-10-14T10:00:00+00:00",
        "note": "done",
    }
    values.update(changes)
    return SimpleNamespace(**values)


class AbandonmentRecordTests(unittest.TestCase):
    def test_record_validation_and_digest_are_fail_closed(self) -> None:
        digest = execution_abandonment.reservation_digest(RESERVATION)
        args = abandonment_args()
        record = execution_abandonment.build(RESERVATION, args, "2026-10-14T10:00:00+00:00")
        self.assertEqual(digest, record["reservation_digest"])
        self.assertTrue(execution_abandonment.valid(record))
        self.assertTrue(execution_abandonment.valid_records([record]))
        self.assertTrue(execution_abandonment.valid_records(None))
        self.assertFalse(execution_abandonment.valid({**record, "evidence_ref": "private/key"}))
        self.assertFalse(execution_abandonment.valid({**record, "recorded_at": "not-a-date"}))
        self.assertFalse(execution_abandonment.valid({**record, "execution_id": "short"}))
        self.assertFalse(execution_abandonment.valid_records([record, record]))

    def test_build_rejects_invalid_evidence(self) -> None:
        with self.assertRaises(ValueError):
            execution_abandonment.build(
                RESERVATION, abandonment_args(evidence_ref="../escape"), "2026-10-14T10:00:00Z"
            )


class RuntimeDouble:
    class IdempotentMutationError(RuntimeError):
        pass

    def __init__(self, *, live: object = None, result: bool = True, worker_absent: bool = True):
        self.live = live
        self.result = result
        self.worker_absent = worker_absent

    def require_active_binding_owner(self, _args: object, _meta: dict[str, object]) -> None:
        return None

    def live_execution_reservation(self, _meta: dict[str, object]) -> object:
        return self.live

    def parse_claim_expiry(self, value: object) -> dt.datetime:
        if not isinstance(value, str) or not value:
            return dt.datetime.min.replace(tzinfo=dt.UTC)
        return dt.datetime.fromisoformat(value.replace("Z", "+00:00"))

    def execution_result_matches(self, _reservation: dict[str, object], _result: object) -> bool:
        return self.result

    def require_optional_revision(self, _args: object, _meta: dict[str, object]) -> None:
        return None

    def valid_execution_reservation(self, value: object) -> bool:
        return isinstance(value, dict) and value.get("execution_id") == RESERVATION["execution_id"]

    def require_claimed_worker_absent(self, _meta: dict[str, object]) -> None:
        if not self.worker_absent:
            raise RuntimeError("worker still claimed")

    def now(self) -> str:
        return "2026-10-14T10:00:00+00:00"


class LifecycleTests(unittest.TestCase):
    def meta(self) -> dict[str, object]:
        return {
            "task_revision": 4,
            "owner": "worker-a",
            "status": "in_progress",
            "claim_expires": "2026-10-14T09:00:00+00:00",
            "execution_envelope": {},
            "execution_envelope_digest": "sha256:" + "f" * 64,
        }

    def start_args(self, **changes: object) -> SimpleNamespace:
        values = {
            "owner": "worker-a",
            "execution_id": RESERVATION["execution_id"],
            "execution_expires_at": "2999-01-01T00:00:00+00:00",
            "command_class": "test",
            "scope_digest": RESERVATION["scope_digest"],
            "argv_digest": RESERVATION["argv_digest"],
        }
        values.update(changes)
        return SimpleNamespace(**values)

    def test_start_success_and_guard_paths(self) -> None:
        runtime = RuntimeDouble()
        meta = self.meta()
        self.assertIn(
            RESERVATION["execution_id"], execution_lifecycle.start(runtime, self.start_args(), meta)
        )
        self.assertEqual(RESERVATION["execution_id"], meta["execution_reservation"]["execution_id"])
        with self.assertRaisesRegex(RuntimeError, "live execution"):
            execution_lifecycle.start(RuntimeDouble(live={}), self.start_args(), self.meta())
        with self.assertRaisesRegex(RuntimeError, "bound execution envelope"):
            execution_lifecycle.start(runtime, self.start_args(), {"task_revision": 1})
        with self.assertRaisesRegex(RuntimeError, "identifier"):
            execution_lifecycle.start(runtime, self.start_args(execution_id="bad"), self.meta())
        with self.assertRaisesRegex(RuntimeError, "future"):
            execution_lifecycle.start(
                runtime,
                self.start_args(execution_expires_at="2000-01-01T00:00:00+00:00"),
                self.meta(),
            )

    def test_finish_result_recover_and_abandon(self) -> None:
        runtime = RuntimeDouble()
        meta = self.meta()
        meta["execution_reservation"] = dict(RESERVATION)
        args = abandonment_args(note="finished")
        with self.assertRaisesRegex(RuntimeError, "exact durable result"):
            execution_lifecycle.finish(RuntimeDouble(result=False), args, meta)
        self.assertEqual("finished", execution_lifecycle.finish(runtime, args, meta))
        meta["execution_reservation"] = dict(RESERVATION)
        result_args = abandonment_args()
        self.assertIn("Recorded", execution_lifecycle.result(runtime, result_args, meta))
        with self.assertRaises(RuntimeDouble.IdempotentMutationError):
            execution_lifecycle.result(runtime, result_args, meta)
        meta["execution_reservation"] = dict(RESERVATION)
        meta["execution_result"] = {"execution_id": RESERVATION["execution_id"]}
        self.assertIn("Recovered", execution_lifecycle.recover(runtime, result_args, meta))
        meta["execution_reservation"] = dict(RESERVATION)
        meta["claim_expires"] = "2000-01-01T00:00:00+00:00"
        meta.pop("execution_result", None)
        abandon = abandonment_args(allow_legacy_without_identity=True)
        self.assertIn(
            "Abandoned", execution_lifecycle.abandon(RuntimeDouble(result=False), abandon, meta)
        )
        self.assertEqual("open", meta["status"])
        self.assertEqual("", meta["owner"])


if __name__ == "__main__":
    unittest.main()
