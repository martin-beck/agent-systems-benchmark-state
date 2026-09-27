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
  "observed_dirty": 0,
  "observed_head": "1e2c59119820bc073ea4c6736782f5041a395a28",
  "owner": "ar1332-record-replay-luna56",
  "plan": "../plans/AR-1475-asb-metrics-evidence-fixture-repair.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Repair the deterministic ProbeRejected versus MalformedEvidence fixture failure blocking PR #345.",
  "task_revision": 6,
  "title": "Repair asb-metrics evidence fixture classification",
  "updated_at": "2026-09-27T03:55:29+00:00",
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
