# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Git-authority hostile and reopen coverage for predicate evidence ledgers."""

from __future__ import annotations

import argparse
import hashlib
import importlib
import json
import unittest
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Any
from unittest.mock import patch

from tools import predicate_ledger
from tools.task_spec import evidence_ledger_errors


@contextmanager
def git_fixture() -> Iterator[tuple[Any, Any]]:
    """Reuse the canonical Git fixture without duplicating its broad test class."""
    handoff_tests = importlib.import_module("test_handoffctl")
    fixture = handoff_tests.HandoffTest()
    fixture.setUp()
    try:
        yield fixture, handoff_tests.CORE
    finally:
        fixture.tearDown()


class PredicateEvidenceLedgerGitTests(unittest.TestCase):
    """Exercise candidate identity and malformed-history rejection through Git."""

    def test_reopens_only_for_a_new_candidate(self) -> None:
        with git_fixture() as (fixture, core):
            fixture.enable_additive_policy()
            fixture.write_additive_spec()
            spec = json.loads((fixture.root / "spec.json").read_text(encoding="utf-8"))
            spec["acceptance_predicates"].append(
                {"id": "downstream-policy-reopen", "description": "revalidate candidate"}
            )
            (fixture.root / "spec.json").write_text(json.dumps(spec), encoding="utf-8")
            for name, content in (("candidate.txt", "candidate a"), ("evidence.txt", "evidence a")):
                (fixture.root / name).write_text(content, encoding="utf-8")

            def digest(name: str) -> str:
                return "sha256:" + hashlib.sha256((fixture.root / name).read_bytes()).hexdigest()

            fixture.make_task(
                status="in_progress",
                owner="worker-a",
                claim_expires="2099-01-01T00:00:00+00:00",
                spec_ref="spec.json",
                spec_revision=1,
            )
            first = argparse.Namespace(
                task="AR-0001",
                owner="worker-a",
                expected_revision=1,
                evidence_class="hosted",
                evidence_ref="evidence.txt",
                evidence_digest=digest("evidence.txt"),
                predicate="downstream-policy",
                candidate_ref="candidate.txt",
                candidate_digest=digest("candidate.txt"),
                reopen=False,
                note="candidate a",
            )
            with (
                patch.object(core, "sync_replica_before_write"),
                patch.object(core, "commit", return_value=True),
                patch.object(core, "push_replica"),
            ):
                core.mutate(first, "accept")
                (fixture.root / "candidate.txt").write_text("candidate b", encoding="utf-8")
                (fixture.root / "evidence.txt").write_text("evidence b", encoding="utf-8")
                changed = argparse.Namespace(
                    **{
                        **vars(first),
                        "expected_revision": 2,
                        "predicate": "downstream-policy-reopen",
                        "candidate_digest": digest("candidate.txt"),
                        "evidence_digest": digest("evidence.txt"),
                    }
                )
                with self.assertRaisesRegex(RuntimeError, "candidate changed"):
                    core.mutate(changed, "accept")
                core.mutate(argparse.Namespace(**{**vars(changed), "reopen": True}), "accept")
            ledger = core.locate("AR-0001")[1]["evidence_ledger"]
            self.assertEqual("candidate.txt", ledger["candidate_ref"])
            self.assertEqual(["stale", "pass"], [step["status"] for step in ledger["steps"]])
            self.assertEqual([], evidence_ledger_errors(fixture.root, core.locate("AR-0001")[1]))
            (fixture.root / "candidate.txt").write_text("tampered", encoding="utf-8")
            self.assertIn(
                "evidence ledger candidate artifact digest is invalid",
                evidence_ledger_errors(fixture.root, core.locate("AR-0001")[1]),
            )

    def test_reopen_rejects_malformed_history_before_persisting(self) -> None:
        with git_fixture() as (fixture, core):
            fixture.enable_additive_policy()
            fixture.write_additive_spec()
            spec = json.loads((fixture.root / "spec.json").read_text(encoding="utf-8"))
            spec["acceptance_predicates"].append(
                {"id": "downstream-policy-reopen", "description": "revalidate candidate"}
            )
            (fixture.root / "spec.json").write_text(json.dumps(spec), encoding="utf-8")
            for name, content in (("candidate.txt", "candidate a"), ("evidence.txt", "evidence a")):
                (fixture.root / name).write_text(content, encoding="utf-8")

            def digest(name: str) -> str:
                return "sha256:" + hashlib.sha256((fixture.root / name).read_bytes()).hexdigest()

            old_candidate_digest = digest("candidate.txt")
            old_evidence_digest = digest("evidence.txt")
            fixture.make_task(
                status="in_progress",
                owner="worker-a",
                claim_expires="2099-01-01T00:00:00+00:00",
                spec_ref="spec.json",
                spec_revision=1,
                evidence_ledger={
                    "candidate_ref": "candidate.txt",
                    "candidate_digest": old_candidate_digest,
                    "steps": [
                        {
                            "predicate_id": "downstream-policy",
                            "status": "pass",
                            "candidate_ref": "candidate.txt",
                            "candidate_digest": old_candidate_digest,
                            "evidence_class": "hosted",
                            "evidence_ref": "evidence.txt",
                            "evidence_digest": old_evidence_digest,
                            "recorded_task_revision": 1,
                        },
                        "malformed historical row",
                    ],
                },
            )
            task_path = fixture.root / "tasks/AR-0001-test.md"
            before = task_path.read_text(encoding="utf-8")
            (fixture.root / "candidate.txt").write_text("candidate b", encoding="utf-8")
            (fixture.root / "evidence.txt").write_text("evidence b", encoding="utf-8")
            reopen = argparse.Namespace(
                task="AR-0001",
                owner="worker-a",
                expected_revision=1,
                evidence_class="hosted",
                evidence_ref="evidence.txt",
                evidence_digest=digest("evidence.txt"),
                predicate="downstream-policy-reopen",
                candidate_ref="candidate.txt",
                candidate_digest=digest("candidate.txt"),
                reopen=True,
                note="candidate b",
            )
            with (
                patch.object(core, "sync_replica_before_write"),
                patch.object(core, "commit", return_value=True) as commit,
                patch.object(core, "push_replica") as push,
                self.assertRaisesRegex(
                    RuntimeError, "evidence ledger step is incomplete or unknown"
                ),
            ):
                core.mutate(reopen, "accept")
            commit.assert_not_called()
            push.assert_not_called()
            self.assertEqual(before, task_path.read_text(encoding="utf-8"))
            persisted = core.locate("AR-0001")[1]
            self.assertEqual(1, persisted["task_revision"])
            self.assertEqual("malformed historical row", persisted["evidence_ledger"]["steps"][1])


class PredicateEvidenceLedgerFailureTests(unittest.TestCase):
    """Cover fail-closed ledger validation paths without mutating a live state root."""

    def setUp(self) -> None:
        self.temp = TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "candidate.txt").write_text("candidate", encoding="utf-8")
        (self.root / "evidence.txt").write_text("evidence", encoding="utf-8")
        (self.root / "other.txt").write_text("other", encoding="utf-8")
        (self.root / "spec.json").write_text(
            json.dumps(
                {
                    "schema_version": 1,
                    "spec_ref": "spec.json",
                    "spec_revision": 1,
                    "acceptance_predicates": [{"id": "predicate", "description": "pass"}],
                    "definition_of_done": ["pass predicate"],
                    "inputs": [{"id": "input", "description": "input"}],
                    "outputs": [{"id": "output", "description": "output"}],
                    "allowed_tools": ["source.read"],
                    "forbidden_tools": [],
                    "required_evidence_classes": ["contract-test"],
                    "gates": [{"id": "gate", "description": "pass"}],
                }
            ),
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        self.temp.cleanup()

    def digest(self, name: str) -> str:
        return "sha256:" + hashlib.sha256((self.root / name).read_bytes()).hexdigest()

    def meta(self) -> dict[str, Any]:
        return {
            "id": "AR-0001",
            "task_revision": 1,
            "spec_ref": "spec.json",
            "spec_revision": 1,
            "evidence_ledger": {
                "candidate_ref": "candidate.txt",
                "candidate_digest": self.digest("candidate.txt"),
                "steps": [
                    {
                        "predicate_id": "predicate",
                        "status": "pass",
                        "candidate_ref": "candidate.txt",
                        "candidate_digest": self.digest("candidate.txt"),
                        "evidence_class": "contract-test",
                        "evidence_ref": "evidence.txt",
                        "evidence_digest": self.digest("evidence.txt"),
                        "recorded_task_revision": 1,
                    }
                ],
            },
        }

    def test_ledger_validation_rejects_every_untrusted_step_field(self) -> None:
        cases: list[tuple[str, Any, bool]] = [
            ("evidence ledger is incomplete or unknown", [], True),
            (
                "evidence ledger candidate artifact digest is invalid",
                {"candidate_digest": "sha256:" + "a" * 64},
                True,
            ),
            ("evidence ledger steps are invalid", {"steps": "not-a-list"}, True),
            ("evidence ledger step is incomplete or unknown", {"steps": ["bad"]}, True),
            (
                "evidence ledger predicate is invalid or duplicated",
                {"predicate_id": "unknown"},
                False,
            ),
            ("evidence ledger step status is invalid", {"status": "unknown"}, False),
            ("evidence ledger step candidate ref is invalid", {"candidate_ref": "x"}, False),
            (
                "evidence ledger step candidate digest is invalid",
                {"candidate_digest": "bad"},
                False,
            ),
            ("evidence ledger evidence class is unknown", {"evidence_class": "unknown"}, False),
            ("evidence ledger evidence ref is invalid", {"evidence_ref": "x"}, False),
            ("evidence ledger evidence digest is invalid", {"evidence_digest": "bad"}, False),
            ("evidence ledger step revision is invalid", {"recorded_task_revision": 0}, False),
        ]
        for expected, change, ledger_change in cases:
            with self.subTest(expected=expected):
                meta = self.meta()
                if isinstance(change, dict) and ledger_change:
                    meta["evidence_ledger"].update(change)
                elif isinstance(change, dict):
                    meta["evidence_ledger"]["steps"][0].update(change)
                else:
                    meta["evidence_ledger"] = change
                self.assertIn(expected, evidence_ledger_errors(self.root, meta))

    def test_ledger_validation_rejects_candidate_history_and_evidence_identity_drift(self) -> None:
        cases: list[tuple[str, dict[str, Any]]] = [
            (
                "evidence ledger passing step candidate does not match ledger",
                {"candidate_ref": "other.txt", "candidate_digest": self.digest("other.txt")},
            ),
            (
                "evidence ledger step candidate artifact digest is invalid",
                {"candidate_digest": "sha256:" + "a" * 64},
            ),
            ("evidence ledger stale step candidate matches ledger", {"status": "stale"}),
            (
                "evidence ledger evidence artifact digest is invalid",
                {"evidence_digest": "sha256:" + "a" * 64},
            ),
        ]
        for expected, change in cases:
            with self.subTest(expected=expected):
                meta = self.meta()
                meta["evidence_ledger"]["steps"][0].update(change)
                self.assertIn(expected, evidence_ledger_errors(self.root, meta))
        missing_spec = self.meta()
        missing_spec["spec_ref"] = "missing.json"
        self.assertIn(
            "evidence ledger task spec is unavailable",
            evidence_ledger_errors(self.root, missing_spec),
        )

    def test_transition_helpers_reject_partial_unbound_and_postwrite_evidence(self) -> None:
        self.assertIsNone(predicate_ledger.predicate_acceptance_inputs(argparse.Namespace()))
        with self.assertRaisesRegex(RuntimeError, "requires predicate"):
            predicate_ledger.predicate_acceptance_inputs(argparse.Namespace(predicate="predicate"))
        self.assertEqual("bad", predicate_ledger._historical_steps("bad"))
        with self.assertRaisesRegex(RuntimeError, "ledger is malformed"):
            predicate_ledger._ledger(
                {"evidence_ledger": []}, "candidate.txt", self.digest("candidate.txt")
            )
        arguments = argparse.Namespace(
            evidence_class="contract-test",
            evidence_ref="evidence.txt",
            evidence_digest=self.digest("evidence.txt"),
            note="accepted",
        )
        inputs = ("predicate", "candidate.txt", self.digest("candidate.txt"), False)
        with self.assertRaisesRegex(RuntimeError, "bound task spec"):
            predicate_ledger.apply_predicate_acceptance(
                self.root, arguments, {"task_revision": 1}, None, inputs
            )
        invalid_spec = self.meta()
        invalid_spec["spec_revision"] = 2
        with self.assertRaisesRegex(RuntimeError, "task spec is unavailable"):
            predicate_ledger.apply_predicate_acceptance(
                self.root, arguments, invalid_spec, None, inputs
            )
        with self.assertRaisesRegex(RuntimeError, "unknown predicate"):
            predicate_ledger.apply_predicate_acceptance(
                self.root, arguments, self.meta(), None, ("unknown", *inputs[1:])
            )
        with self.assertRaisesRegex(RuntimeError, "reopen requires"):
            predicate_ledger.apply_predicate_acceptance(
                self.root, arguments, self.meta(), None, (*inputs[:3], True)
            )
        with (
            patch.object(
                predicate_ledger, "evidence_ledger_errors", side_effect=[[], ["postwrite"]]
            ),
            self.assertRaisesRegex(RuntimeError, "postwrite"),
        ):
            predicate_ledger.apply_predicate_acceptance(
                self.root, arguments, self.meta(), None, inputs
            )
