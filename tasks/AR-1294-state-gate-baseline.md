---
{
  "branch": "repair/ar-1294-state-gate-baseline",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T06:56:51+00:00",
  "depends_on": [],
  "id": "AR-1294",
  "next_action": "Audit the vendor lock/digest mismatch and root-owned TLC admission lock; repair only through immutable provenance and owner-safe lock handling, then rerun full state/formal gates.",
  "observed_branch": "repair/ar-1294-state-gate-baseline",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "asb-ar1294-vendor-lock",
  "plan": "../plans/AR-1294.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Restore vendor and formal admission baseline integrity needed to qualify AR-1293.",
  "task_revision": 3,
  "title": "State formal-gate baseline integrity",
  "updated_at": "2026-09-17T04:56:51+00:00",
  "worktree_key": "agent-systems-benchmark-state-ar-1294-gate-baseline"
}
---

## AR-1294

AR-1293 exposed two pre-existing state-gate failures. This AR owns only
provenance-safe vendor reconciliation and owner-safe formal admission. It must
not touch ASB product or asb-tui sources, modify/extract handoffctl, weaken
formal checks, or manipulate another service's lock.

- 2026-09-17T04:56:19+00:00: Independent infrastructure repair for AR-1293 baseline gates; no
  product or handoffctl scope.

- 2026-09-17T04:56:51+00:00: Claimed by asb-ar1294-vendor-lock.
