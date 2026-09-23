---
{
  "branch": "feature/ar-1360-runtime-cli-dispatch-consumer",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1359"
  ],
  "id": "AR-1360",
  "next_action": "Promote after AR-1359 is done, then implement the production asb run/sweep consumer for authenticated runtime enrollment receipts with fail-closed tests.",
  "observed_branch": "feature/ar-1360-runtime-cli-dispatch-consumer",
  "observed_dirty": 0,
  "observed_head": "be9af3d6fb22818e95f51b9640b10c5eb6e043f3",
  "owner": "",
  "plan": "../plans/AR-1360-runtime-cli-dispatch-consumer.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Connect authenticated runtime enrollment receipts to asb run and sweep without exposing authority.",
  "task_revision": 2,
  "title": "Runtime CLI dispatch consumer",
  "updated_at": "2026-09-23T22:58:10+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1360-runtime-cli-dispatch-consumer"
}
---

Successor for blocked AR-1358. Do not touch asb-tui, weaken AR-1329 fail-closed
behavior, or let CLI arguments synthesize provider authority.

- 2026-09-24T00:00:00+00:00: Created after AR-1359 merged the authenticated
  control/runtime bridge and all post-merge workflows passed. This task owns the
  remaining asb run/sweep dispatch consumer only.

- 2026-09-23T22:58:10+00:00: Dependency AR-1359 is done with merged bridge and all seven post-merge
  workflows green; promote CLI dispatch consumer.
