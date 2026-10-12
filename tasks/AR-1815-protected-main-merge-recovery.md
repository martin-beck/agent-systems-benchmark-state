---
{
  "branch": "recovery/ar-1815-provenance",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-12T13:41:12+00:00",
  "depends_on": [],
  "id": "AR-1815",
  "next_action": "Claim a dedicated recovery worktree; use tools/integration/merge_pr.py to create a forward-only signed DCO recovery for preserved merge 15c80511, then review, publish, merge, and verify exact-main gates.",
  "observed_branch": "recovery/ar-1815-provenance",
  "observed_dirty": 0,
  "observed_head": "ab4f4c6a81f543e049759d199cca675c7370a1dc",
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
  "task_revision": 13,
  "title": "Protected-main signed merge recovery",
  "updated_at": "2026-10-12T11:42:05+00:00",
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

- 2026-10-12T11:41:12+00:00: Heartbeat by ar1805_postmerge_repair.

- 2026-10-12T11:41:16+00:00: Recorded command exit 0; command argv SHA-256
  7c730eec3ea71bd24ffc5a9255bf7f542481bf601dba6c72bed6e00f6c2fab3c.

- 2026-10-12T11:41:20+00:00: Recorded command exit 0; command argv SHA-256
  02033fc75602c6d6d6bfd7e30319ecdddd5bc0961a13ff8c93f000ecb73e9902.

- 2026-10-12T11:41:37+00:00: Recorded command exit 0; command argv SHA-256
  f9bbe1c589a3669657a75f784f9cf5be2dcca32c9aa8bcdbea78bfad2db9ec69.

- 2026-10-12T11:41:56+00:00: Recorded command exit 0; command argv SHA-256
  02970c2d8860d638f41bff4ed6e5e563ac93ac98b50be6b487e02ab3468b60d2.

- 2026-10-12T11:41:57+00:00: Recorded command exit 0; command argv SHA-256
  de0f9a0651ffde4b5362e5bb246b136d877b74395650384e51588c2dca8120fd.

- 2026-10-12T11:42:05+00:00: Recorded command exit 0; command argv SHA-256
  99df30ca0ed805631b5a3fe2055833ee120579ed5e644b7bc0e120f71be6c943.
