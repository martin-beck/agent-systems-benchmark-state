---
{
  "branch": "feature/ar-1800-controlled-local-workload-acquisition-backend",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1782", "AR-1783"],
  "id": "AR-1800",
  "next_action": "Implement the credential-free controlled acquisition backend and qualify every AR-1781 workload through the AR-1780 journey.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1800-controlled-local-workload-acquisition-backend.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {"evidence_class": "environmental", "evidence_digest": "", "evidence_ref": "", "spec_ref": "specs/AR-1800.json", "spec_revision": 1, "status": "pending"},
  "spec_ref": "specs/AR-1800.json",
  "spec_revision": 1,
  "status": "planned",
  "summary": "Provide the credential-free controlled local acquisition backend required for AR-1780 every-workload execution qualification.",
  "task_revision": 1,
  "title": "Controlled local workload acquisition backend",
  "updated_at": "2026-10-12T02:20:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1800-controlled-local-workload-acquisition-backend"
}
---

AR-1800 is the dependency-safe successor for the infrastructure boundary
identified by AR-1780. It must add only a bounded development fixture seam; it
must not weaken production acquisition, identity, or offline guarantees.
