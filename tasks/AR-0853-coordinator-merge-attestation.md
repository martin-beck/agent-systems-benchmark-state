---
{
  "branch": "fix/coordinator-v014-merge-attestation",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-08T09:35:04+00:00",
  "depends_on": [],
  "id": "AR-0853",
  "next_action": "Select and independently review a non-rewriting signed+DCO replacement or additive attestation for the exact v0.1.4 merge evidence.",
  "owner": "replay-20260906",
  "plan": "../plans/AR-0853.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Repair the v0.1.4 coordinator merge attestation without rewriting published history.",
  "task_revision": 4,
  "title": "Repair coordinator merge attestation",
  "updated_at": "2026-09-08T07:35:04+00:00",
  "worktree_key": "agent-systems-benchmark-coordinator-merge-attestation"
}
---

PR #10 merged the correct reviewed v0.1.4 tree, but its merge commit lacks a locally verifiable
Martin Beck SSH signature and matching Signed-off-by trailer. Preserve that durable merge and use
only an independently reviewed additive repair.

- 2026-09-08T07:35:01+00:00: Promoted dependency-free repair for the published AR-0852 merge
  attestation; AR-0852 remains open pending this repair.

- 2026-09-08T07:35:04+00:00: Claimed by replay-20260906.
