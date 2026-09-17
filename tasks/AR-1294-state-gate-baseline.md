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
  "task_revision": 5,
  "title": "State formal-gate baseline integrity",
  "updated_at": "2026-09-17T04:57:12+00:00",
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

- 2026-09-17T04:56:58+00:00: Recorded command exit 1; command argv SHA-256
  73f9955b98d559c2b06ace66138b995891af97bf31e3ccac58358f49ca9f9a2e.

- 2026-09-17T04:57:12+00:00: Recorded command exit 0; command argv SHA-256
  b9bdf1362a5e638d1cc8808b53f040d5e310932d3e399b44047e65eb7e8d3121.
