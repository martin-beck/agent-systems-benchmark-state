---
{
  "branch": "feature/provider-recording-choice",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-08T15:37:29+00:00",
  "depends_on": [
    "AR-0104",
    "AR-0310",
    "AR-0313",
    "AR-0503",
    "AR-0504"
  ],
  "id": "AR-0314",
  "next_action": "Index compatible recordings and require an explicit replay-versus-live source choice.",
  "owner": "quality_20260906",
  "plan": "../plans/AR-0314.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Offer matching prior recordings or an actual provider connection without silently choosing either.",
  "task_revision": 3,
  "title": "Choose matching replay or live provider execution",
  "updated_at": "2026-09-08T13:37:29+00:00",
  "worktree_key": "agent-systems-benchmark-provider-recording-choice"
}
---
## AR-0314

Offer matching prior recordings or an actual provider connection without silently choosing either.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-08T13:37:26+00:00: Dependency audit: AR-0104, AR-0310, AR-0503, AR-0504, and AR-0313 are
  durably done; AR-0803 is done. Promote as highest-priority compatible provider/replay leaf.

- 2026-09-08T13:37:29+00:00: Claimed by quality_20260906.
