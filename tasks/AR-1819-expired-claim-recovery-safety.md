---
{
  "branch": "repair/ar-1819-expired-claim-safety",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-12T15:27:45+00:00",
  "depends_on": [],
  "id": "AR-1819",
  "next_action": "Implement fail-closed expired-claim recovery, add focused positive and negative coverage, then independently review and integrate the exact signed head.",
  "owner": "ar1819_stale_claim_repair",
  "plan": "../plans/AR-1819-expired-claim-recovery-safety.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1819.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Make expired-claim recovery fail closed when the exact current session snapshot is unavailable.",
  "task_revision": 3,
  "title": "Fail-closed expired-claim recovery",
  "updated_at": "2026-10-12T13:27:45+00:00",
  "worktree_key": ""
}
---

# AR-1819 — Fail-closed expired-claim recovery

An expired claim may be recovered only from a validated exact current-revision
session snapshot. Recovery without that snapshot must remain closed, even when a
claim-time process identity is present; process absence cannot reconstruct the
worker's last durable action and must not be used as a substitute for a
checkpoint. Preserve AR-1796's historical claim and recovery evidence and keep
AR-1818 publication independent of any impersonation or ambiguous ownership.

The repair must retain strict revision fencing, scope-bound process checks for
diagnostic evidence, generated-view integrity, signed DCO commits, independent
review, exact-head CI, and post-merge live doctor. No TLC/model-check or live
provider run is required for this development repair.

- 2026-10-12T13:25:00+00:00: Created after AR-1796 expired-claim recovery exposed the
  unsafe snapshotless fallback; AR-1796 history remains immutable evidence.

- 2026-10-12T13:26:02+00:00: Dependencies verified; promote fail-closed expired-claim safety repair.

- 2026-10-12T13:27:45+00:00: Claimed by ar1819_stale_claim_repair.
