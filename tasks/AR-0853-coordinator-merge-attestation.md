---
{
  "branch": "fix/coordinator-v014-merge-attestation",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-0853",
  "next_action": "Select and independently review a non-rewriting signed+DCO replacement or additive attestation for the exact v0.1.4 merge evidence.",
  "owner": "",
  "plan": "../plans/AR-0853.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Repair the v0.1.4 coordinator merge attestation without rewriting published history.",
  "task_revision": 2,
  "title": "Repair coordinator merge attestation",
  "updated_at": "2026-09-08T07:35:00+00:00",
  "worktree_key": "agent-systems-benchmark-coordinator-merge-attestation"
}
---

PR #10 merged the correct reviewed v0.1.4 tree, but its merge commit lacks a locally verifiable
Martin Beck SSH signature and matching Signed-off-by trailer. Preserve that durable merge and use
only an independently reviewed additive repair.
