# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Positive and fail-closed coverage for bounded predicate-ledger repair."""

from __future__ import annotations

import argparse
import hashlib
import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from tools import predicate_ledger_repair
from tools.task_spec import DEFAULT_EVIDENCE_POLICY


class PredicateLedgerRepairTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "evidence").mkdir()
        (self.root / "candidate-v2.txt").write_text("candidate v2\n", encoding="utf-8")
        (self.root / "evidence" / "repair.txt").write_text("fresh evidence\n", encoding="utf-8")
        spec = {
            "acceptance_predicates": [{"id": "scope"}],
        }
        (self.root / "spec.json").write_text(json.dumps(spec), encoding="utf-8")

    def tearDown(self) -> None:
        self.temp.cleanup()

    def _digest(self, reference: str) -> str:
        return "sha256:" + hashlib.sha256((self.root / reference).read_bytes()).hexdigest()

    def _meta(self) -> dict[str, object]:
        return {
            "task_revision": 4,
            "status": "done",
            "owner": "",
            "claim_expires": "",
            "spec_ref": "spec.json",
            "spec_revision": 1,
            "id": "AR-1936",
            "evidence_ledger": {
                "candidate_ref": "candidate-v1.txt",
                "candidate_digest": "sha256:" + "0" * 64,
                "steps": [
                    {
                        "predicate_id": "scope",
                        "status": "pass",
                        "candidate_ref": "candidate-v1.txt",
                        "candidate_digest": "sha256:" + "0" * 64,
                    },
                    {
                        "predicate_id": "other",
                        "status": "pass",
                        "candidate_ref": "candidate-v1.txt",
                        "candidate_digest": "sha256:" + "0" * 64,
                    },
                ],
            },
        }

    def _args(self, **changes: object) -> argparse.Namespace:
        values: dict[str, object] = {
            "expected_revision": 4,
            "reason": "refresh bounded evidence after source repair",
            "predicate": "scope",
            "evidence_class": "contract-test",
            "evidence_ref": "evidence/repair.txt",
            "evidence_digest": self._digest("evidence/repair.txt"),
            "candidate_ref": "candidate-v2.txt",
            "candidate_digest": self._digest("candidate-v2.txt"),
        }
        values.update(changes)
        return argparse.Namespace(**values)

    def test_repair_marks_all_prior_passes_stale_and_appends_fresh_pass(self) -> None:
        meta = self._meta()
        with patch.object(predicate_ledger_repair, "task_spec_errors", return_value=[]):
            reason = predicate_ledger_repair.repair(
                self.root, self._args(), meta, DEFAULT_EVIDENCE_POLICY
            )
        self.assertIn("refresh bounded", reason)
        ledger = meta["evidence_ledger"]
        assert isinstance(ledger, dict)
        steps = ledger["steps"]
        assert isinstance(steps, list)
        self.assertEqual("stale", steps[0]["status"])
        self.assertEqual("pass", steps[1]["status"])
        self.assertEqual("pass", steps[2]["status"])
        self.assertEqual(5, steps[2]["recorded_task_revision"])

    def test_repair_rejects_stale_owner_and_bad_reason(self) -> None:
        with self.assertRaisesRegex(RuntimeError, "done, inactive"):
            predicate_ledger_repair.repair(
                self.root,
                self._args(),
                {**self._meta(), "owner": "worker"},
                DEFAULT_EVIDENCE_POLICY,
            )
        with self.assertRaisesRegex(RuntimeError, "reason is empty"):
            predicate_ledger_repair.repair(
                self.root,
                self._args(reason="\n"),
                self._meta(),
                DEFAULT_EVIDENCE_POLICY,
            )

    def test_repair_rejects_unsafe_and_stale_evidence(self) -> None:
        for field, value in (("evidence_ref", "../escape"), ("candidate_ref", "../escape")):
            with (
                self.subTest(field=field),
                patch.object(predicate_ledger_repair, "task_spec_errors", return_value=[]),
                self.assertRaisesRegex(RuntimeError, "unsafe|stale"),
            ):
                predicate_ledger_repair.repair(
                    self.root, self._args(**{field: value}), self._meta(), DEFAULT_EVIDENCE_POLICY
                )

    def test_repair_rejects_unknown_predicate_class_and_malformed_ledger(self) -> None:
        with patch.object(predicate_ledger_repair, "task_spec_errors", return_value=[]):
            with self.assertRaisesRegex(RuntimeError, "unknown predicate"):
                predicate_ledger_repair.repair(
                    self.root,
                    self._args(predicate="missing"),
                    self._meta(),
                    DEFAULT_EVIDENCE_POLICY,
                )
            with self.assertRaisesRegex(RuntimeError, "evidence class is unknown"):
                predicate_ledger_repair.repair(
                    self.root,
                    self._args(evidence_class="not-a-policy-class"),
                    self._meta(),
                    DEFAULT_EVIDENCE_POLICY,
                )
        malformed = self._meta()
        malformed["evidence_ledger"] = []
        with self.assertRaisesRegex(RuntimeError, "canonical evidence ledger"):
            predicate_ledger_repair.repair(
                self.root, self._args(), malformed, DEFAULT_EVIDENCE_POLICY
            )


if __name__ == "__main__":
    unittest.main()
