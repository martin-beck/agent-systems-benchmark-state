---
{
  "schema_version": 1,
  "id": "AR-1475",
  "title": "Repair asb-metrics evidence fixture classification",
  "status": "planned",
  "priority": "P0",
  "summary": "Repair the deterministic ProbeRejected versus MalformedEvidence fixture failure blocking PR #345.",
  "next_action": "Promote after validating the repair dependencies, then reproduce and fix the asb-metrics classification failure on an isolated worktree.",
  "task_revision": 1,
  "updated_at": "2026-09-27T03:55:00+00:00",
  "owner": "",
  "claim_expires": "",
  "worktree_key": "agent-systems-benchmark-ar-1475-asb-metrics-evidence-fixture-repair",
  "branch": "feature/ar-1475-asb-metrics-evidence-fixture-repair",
  "checkpoint_commit": "",
  "plan": "../plans/AR-1475-asb-metrics-evidence-fixture-repair.md",
  "depends_on": ["AR-1200", "AR-1379", "AR-1472"]
}
---

Successor created from AR-1474’s exact-head CI audit. The repair must preserve
fail-closed evidence semantics and independently prove whether the failure is
classification or fixture behavior before changing code.

- 2026-09-27T03:55:00+00:00: Created after Rust workflow 36292250053 reproduced
  the same `asb-metrics` assertion twice at `kernel.rs:718`, blocking PR #345.
