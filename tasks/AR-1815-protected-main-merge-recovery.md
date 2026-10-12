---
{
  "branch": "recovery/ar-1815-provenance",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-12T13:40:37+00:00",
  "depends_on": [],
  "id": "AR-1815",
  "next_action": "Claim a dedicated recovery worktree; use tools/integration/merge_pr.py to create a forward-only signed DCO recovery for preserved merge 15c80511, then review, publish, merge, and verify exact-main gates.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "ar1805_postmerge_repair",
  "plan": "../plans/AR-1815-protected-main-merge-recovery.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "hosted",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1815.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1815.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Recover protected-main merge provenance without rewriting the preserved GitHub merge.",
  "task_revision": 5,
  "title": "Protected-main signed merge recovery",
  "updated_at": "2026-10-12T11:40:47+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1815-provenance"
}
---

AR-1815 is the narrowly scoped successor for the exact-main failures on
AR-1805/PR #608. Preserve merge `15c80511`; recover only through the local
signed integration path. Do not weaken gates, rewrite history, force-push, or
introduce a TLC/model-check dependency for development.


- 2026-10-12T11:38:40+00:00: Claimed by ar1805_postmerge_repair.

- 2026-10-12T11:40:17+00:00: Bound worktree agent-systems-benchmark-ar-1815-provenance on branch
  recovery/ar-1815-provenance.

- 2026-10-12T11:40:37+00:00: Heartbeat by ar1805_postmerge_repair.

- 2026-10-12T11:40:47+00:00: Recorded command exit 0; command argv SHA-256
  96a0af41a541f5236a5894e26c9eb7ff32fa914aac46bb58bd7dabecaaa5c33e.
