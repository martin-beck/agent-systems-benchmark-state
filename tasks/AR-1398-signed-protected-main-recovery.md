---
{
  "branch": "repair/ar-1398-signed-protected-main-recovery",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-24T12:00:09+00:00",
  "depends_on": [
    "AR-1337"
  ],
  "id": "AR-1398",
  "next_action": "Promote after the integration queue is quiescent; create a signed+DCO descendant preserving PR #286 merge 123ba915 tree/parents, run independent review and all exact-main gates, then close the three affected repair records with fresh evidence.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "ar1398_signed_recovery_luna56",
  "plan": "../plans/AR-1398-signed-protected-main-recovery.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Restore signed+DCO protected-main evidence after an unsigned GitHub-generated repair merge.",
  "task_revision": 7,
  "title": "Signed protected-main recovery",
  "updated_at": "2026-09-24T10:02:00+00:00",
  "worktree_key": ""
}
---

# AR-1398

This is an integration/publication repair only. It must not change workload
semantics, OpenRouter behavior, native-evidence policy, or asb-tui. External
providers are never required for development evidence.

- 2026-09-24T09:58:18+00:00: Protected-main audit requires signed descendant recovery after PR #286
  merge 123ba915; preserve historical evidence and restore signed+DCO exact-main proof.

- 2026-09-24T10:00:09+00:00: Claimed by ar1398_signed_recovery_luna56.

- 2026-09-24T10:00:44+00:00: Recorded command exit 0; command argv SHA-256
  c725572ba4f53df0f5d848d1c6861633cd446ff51c3e8c3a06f5a000630c5f61.

- 2026-09-24T10:01:11+00:00: Recorded command exit 0; command argv SHA-256
  8fade593bd1ee9ba7c7ebfb3646c2d83591a375f5df4fc68f8f4ab22b6b730cb.

- 2026-09-24T10:01:39+00:00: Recorded command exit 1; command argv SHA-256
  afdc768d3b8a1656a6db8a2cf3e170572c704ef8520da22d8b1956304821b5c0.

- 2026-09-24T10:02:00+00:00: Recorded command exit 0; command argv SHA-256
  87cd4bb47c5cb6cbb3f94935be7cae7c1f98416231eb9de5ba30dfa616e9fda0.
