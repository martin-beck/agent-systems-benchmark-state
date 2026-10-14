# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Focused fail-closed coverage for AR-1863's stale-envelope replacement."""

from __future__ import annotations

import argparse
import copy
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools import execution_envelope, handoffctl


class EnvelopeReplacementTests(unittest.TestCase):
    def setUp(self) -> None:
        task = handoffctl.git_tasks()
        self.meta = next(item for _path, item, _body in task if item["id"] == "AR-1863")
        self.args = argparse.Namespace(
            task="AR-1863",
            owner=self.meta["owner"],
            expected_revision=self.meta["task_revision"],
            from_ref="envelopes/AR-1863-e2.json",
            from_revision=2,
            to_ref="envelopes/AR-1863-e3.json",
            to_revision=3,
        )

    def test_replacement_binds_exact_current_revision_and_records_evidence(self) -> None:
        meta = copy.deepcopy(self.meta)
        note = handoffctl.apply_replace_envelope(self.args, meta)
        self.assertIn("AR-1863-e2", note)
        self.assertEqual("envelopes/AR-1863-e3.json", meta["execution_envelope_ref"])
        evidence = meta["execution_envelope_replacement"]
        self.assertEqual(self.args.expected_revision, evidence["to_task_revision"])
        self.assertEqual(meta["execution_envelope_digest"], evidence["to_digest"])
        self.assertTrue(handoffctl.valid_envelope_replacement(evidence))

    def test_rejects_stale_owner_revision_reservation_and_second_replacement(self) -> None:
        for change, message in (
            ({"owner": "wrong"}, "owned by"),
            ({"expected_revision": self.args.expected_revision - 1}, "stale revision"),
            ({"execution_reservation": {"unexpected": True}}, "EXECUTION_RECOVERY_REQUIRED"),
        ):
            meta = copy.deepcopy(self.meta)
            args = copy.deepcopy(self.args)
            if "owner" in change:
                args.owner = change["owner"]
            elif "expected_revision" in change:
                args.expected_revision = change["expected_revision"]
            else:
                meta.update(change)
            with self.assertRaisesRegex(RuntimeError, message):
                handoffctl.apply_replace_envelope(args, meta)
        meta = copy.deepcopy(self.meta)
        handoffctl.apply_replace_envelope(self.args, meta)
        with self.assertRaisesRegex(RuntimeError, "immutable"):
            handoffctl.apply_replace_envelope(self.args, meta)

    def test_rejects_broader_candidate_scope(self) -> None:
        meta = copy.deepcopy(self.meta)
        loaded, digest, found = execution_envelope.load(handoffctl.ROOT, self.args.to_ref)
        self.assertEqual([], found)
        assert loaded is not None
        broader = copy.deepcopy(loaded)
        broader["path_scope"]["write"].append("Cargo.toml")
        with (
            patch.object(execution_envelope, "load", return_value=(broader, digest, [])),
            self.assertRaisesRegex(RuntimeError, "broadens reviewed scope"),
        ):
            handoffctl.apply_replace_envelope(self.args, meta)


if __name__ == "__main__":
    unittest.main()
