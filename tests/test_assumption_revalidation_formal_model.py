# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
"""Ensure assumption freshness remains a required bounded formal input."""

from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FORMAL = ROOT / "formal/handoffctl"


class AssumptionRevalidationFormalModelTests(unittest.TestCase):
    def test_model_covers_advertised_material_bindings_and_acceptance(self) -> None:
        model = (FORMAL / "HandoffctlAssumptions.tla").read_text(encoding="utf-8")
        for fragment in (
            "currentBase",
            "currentDependency",
            "currentObservation",
            "baseMaterial",
            "dependencyMaterial",
            "observationMaterial",
            "RevalidateBase",
            "RevalidateDependency",
            "DisposeBase",
            "DisposeDependency",
            "RevalidateObservation",
            "DisposeObservation",
            "Accept",
            "AcceptanceRequiresFreshMaterialAssumptions",
            "DoneRequiresFreshMaterialAssumptions",
            "NonmaterialDoesNotUniversallyBlock",
        ):
            self.assertIn(fragment, model)

    def test_model_is_declared_in_both_completion_tiers(self) -> None:
        config = (FORMAL / "HandoffctlAssumptions.cfg").read_text(encoding="utf-8")
        verifier = (FORMAL / "verify.sh").read_text(encoding="utf-8")
        tiers = json.loads((ROOT / "formal/tier-evidence.json").read_text(encoding="utf-8"))
        self.assertIn('Processes = {"p1"}', config)
        self.assertIn("DoneRequiresFreshMaterialAssumptions", config)
        self.assertIn("AcceptanceRequiresFreshMaterialAssumptions", config)
        self.assertIn("run_model HandoffctlAssumptions", verifier)
        self.assertIn("HandoffctlAssumptions", tiers["profiles"]["pr-publication"]["models"])
        self.assertIn("HandoffctlAssumptions", tiers["profiles"]["full-exhaustive"]["models"])


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
