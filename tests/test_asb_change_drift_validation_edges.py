# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Downstream coverage for pure change-drift validation failures."""

from __future__ import annotations

import copy
import tempfile
import unittest
from pathlib import Path

from tools import change_drift


class ChangeDriftValidationEdgesTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.state = Path(self.temporary_directory.name)
        self.baseline_digest = "sha256:" + "0" * 64

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def _record(
        self, kind: str, revision: int, payload: change_drift.Meta, previous_digest: str = ""
    ) -> change_drift.Meta:
        return change_drift._record(
            kind, "AR-9000", revision, "2026-10-13T00:00:00Z", payload, previous_digest
        )

    def _baseline(self) -> change_drift.Meta:
        return self._record("baseline", 1, {"head": "head", "entries": [], "scope": ["src"]})

    def _delta(self, baseline: change_drift.Meta) -> change_drift.Meta:
        return self._record(
            "delta",
            2,
            {
                "baseline_digest": baseline["digest"],
                "head": "head",
                "entries": [
                    {
                        "path": "src/module.py",
                        "previous_path": "",
                        "status": "M ",
                        "generated": False,
                        "content_digest": "",
                        "classification": "in_scope",
                        "material": True,
                    }
                ],
            },
            baseline["digest"],
        )

    def test_validate_rejects_non_boolean_delta_material_flag(self) -> None:
        record = self._delta(self._baseline())
        malformed = copy.deepcopy(record)
        malformed["payload"]["entries"][0]["material"] = 1
        malformed["digest"] = change_drift.digest(
            {
                key: malformed[key]
                for key in (
                    "schema_version",
                    "kind",
                    "task",
                    "task_revision",
                    "payload",
                    "previous_digest",
                )
            }
        )

        with self.assertRaisesRegex(ValueError, "invalid change-drift observation entry"):
            change_drift.validate(malformed)

    def test_records_rejects_rescope_after_active_delta(self) -> None:
        baseline = self._baseline()
        delta = self._delta(baseline)
        rescope = self._record(
            "rescope",
            3,
            {"baseline_digest": baseline["digest"], "scope": ["docs", "src"]},
            delta["digest"],
        )

        with self.assertRaisesRegex(ValueError, "re-scope is not linked to the active baseline"):
            change_drift.records({"id": "AR-9000", "change_drift": [baseline, delta, rescope]})

    def test_records_rejects_explanation_for_a_path_absent_from_delta(self) -> None:
        baseline = self._baseline()
        delta = self._delta(baseline)
        explanation = self._record(
            "explain",
            3,
            {
                "delta_digest": delta["digest"],
                "paths": ["docs/unrelated.md"],
                "reason": "documented reason",
                "generated": False,
            },
            delta["digest"],
        )

        with self.assertRaisesRegex(ValueError, "explanation names unrelated paths"):
            change_drift.records({"id": "AR-9000", "change_drift": [baseline, delta, explanation]})

    def test_done_admission_reports_all_unexplained_material_paths(self) -> None:
        baseline = self._baseline()
        delta = self._delta(baseline)
        second = copy.deepcopy(delta["payload"]["entries"][0])
        second["path"] = "src/second.py"
        delta["payload"]["entries"].append(second)
        delta["digest"] = change_drift.digest(
            {
                key: delta[key]
                for key in (
                    "schema_version",
                    "kind",
                    "task",
                    "task_revision",
                    "payload",
                    "previous_digest",
                )
            }
        )

        self.assertEqual(
            "CHANGE_DRIFT_UNEXPLAINED: material changed paths require explanation: "
            "src/module.py, src/second.py",
            change_drift.done_admission_error({"id": "AR-9000", "change_drift": [baseline, delta]}),
        )


if __name__ == "__main__":
    unittest.main()
