---
{
  "branch": "feature/ar-1804-cross-module-fixture-semaphore",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1762"],
  "id": "AR-1804",
  "next_action": "Reproduce the AR-1801/AR-1803 default-parallel failures and inventory cross-module process fixtures.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1804-cross-module-fixture-semaphore.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {"evidence_class": "environmental", "evidence_digest": "", "evidence_ref": "", "spec_ref": "specs/AR-1804.json", "spec_revision": 1, "status": "pending"},
  "spec_ref": "specs/AR-1804.json",
  "spec_revision": 1,
  "status": "planned",
  "summary": "Provide a bounded cross-module process-fixture semaphore for deterministic default parallel gates.",
  "task_revision": 1,
  "title": "Cross-module fixture semaphore",
  "updated_at": "2026-10-12T00:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1804-cross-module-fixture-semaphore"
}
---

Created from AR-1801 and AR-1803 evidence. Direct parallel Cargo runs shifted
the same `left 6/right 0` outcome among provider-selection, comparison, and
source-checkout fixture tests, while bounded `make test` passed. AR-1803 remains
blocked; this successor must repair the true cross-module contention boundary
before AR-1801 can be accepted.
