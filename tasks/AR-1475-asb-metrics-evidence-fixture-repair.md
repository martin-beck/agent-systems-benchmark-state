---
{
  "branch": "feature/ar-1475-asb-metrics-evidence-fixture-repair",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-27T05:55:10+00:00",
  "depends_on": [
    "AR-1200",
    "AR-1379",
    "AR-1472"
  ],
  "id": "AR-1475",
  "next_action": "Promote after validating the repair dependencies, then reproduce and fix the asb-metrics classification failure on an isolated worktree.",
  "observed_branch": "feature/ar-1475-asb-metrics-evidence-fixture-repair",
  "observed_dirty": 1,
  "observed_head": "1e2c59119820bc073ea4c6736782f5041a395a28",
  "owner": "ar1332-record-replay-luna56",
  "plan": "../plans/AR-1475-asb-metrics-evidence-fixture-repair.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Repair the deterministic ProbeRejected versus MalformedEvidence fixture failure blocking PR #345.",
  "task_revision": 13,
  "title": "Repair asb-metrics evidence fixture classification",
  "updated_at": "2026-09-27T03:58:25+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1475-asb-metrics-evidence-fixture-repair"
}
---

Successor created from AR-1474’s exact-head CI audit. The repair must preserve
fail-closed evidence semantics and independently prove whether the failure is
classification or fixture behavior before changing code.

- 2026-09-27T03:55:00+00:00: Created after Rust workflow 36292250053 reproduced
  the same `asb-metrics` assertion twice at `kernel.rs:718`, blocking PR #345.

- 2026-09-27T03:54:54+00:00: Dependencies AR-1200, AR-1379, and AR-1472 are done; promote the
  independent asb-metrics fixture repair.

- 2026-09-27T03:55:07+00:00: Claimed by ar1332-record-replay-luna56.

- 2026-09-27T03:55:10+00:00: Heartbeat by ar1332-record-replay-luna56.

- 2026-09-27T03:55:17+00:00: Recorded command exit 0; command argv SHA-256
  94b14979dcfc7e709083b46375e44fdeb5c13399aa35e498d112a978054b8a36.

- 2026-09-27T03:55:50+00:00: Recorded command exit 0; command argv SHA-256
  0cf07fd35bd57b757ecada65acc55ac85e5d1d4108ce63e3c1d2a030452922a7.

- 2026-09-27T03:56:10+00:00: Recorded command exit 0; command argv SHA-256
  6202e1ae60427d566490a31016f77c2c1b3a305d7aa395b0f41a7e1477c9b294.

- 2026-09-27T03:56:32+00:00: Recorded command exit 0; command argv SHA-256
  fa05f3c20b8565b088f5ae664489eacdfb43fcd34d1e83a5bf68c06822651a69.

- 2026-09-27T03:56:52+00:00: Recorded command exit 0; command argv SHA-256
  6fc09e6dca7024857c3a7cb0e4b443eae56b3f82052e440f9edf65b3d00fa382.

- 2026-09-27T03:58:05+00:00: Recorded command exit 0; command argv SHA-256
  1af07ce9a64843dd845665a078ce943899872263425549b3ded8cbe39205104f.

- 2026-09-27T03:58:25+00:00: Recorded command exit 101; command argv SHA-256
  6202e1ae60427d566490a31016f77c2c1b3a305d7aa395b0f41a7e1477c9b294.
