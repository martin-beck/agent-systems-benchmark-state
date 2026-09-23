---
{
  "branch": "feature/ar-1350-sandbox-credential-channel",
  "checkpoint_commit": "359f15af52aa2b0b31bb091b945e7de933960006",
  "claim_expires": null,
  "depends_on": ["AR-1328", "AR-1339", "AR-1340", "AR-1347"],
  "id": "AR-1350",
  "next_action": "Implement a private sealed-FD/memfd child credential channel after verifying completed relay/namespace prerequisites; AR-1349 and AR-1329 are downstream consumers and must remain fail-closed until this repair merges.",
  "observed_branch": "feature/ar-1350-sandbox-credential-channel",
  "observed_dirty": 0,
  "observed_head": "359f15af52aa2b0b31bb091b945e7de933960006",
  "owner": null,
  "plan": "../plans/AR-1350-sandbox-credential-channel.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Implement a sandbox-owned sealed-FD credential channel for live provider children.",
  "task_revision": 1,
  "title": "Sandbox-owned credential channel",
  "updated_at": "2026-09-23T17:20:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1350-sandbox-credential-channel"
}
---

Coordinator repair for the exact prerequisite discovered by AR-1349: existing
credential memfd delivery reaches only direct helper processes, while the
bubblewrap live child clears the outer environment. AR-1350 must provide the
private runtime channel before AR-1349 can safely acquire attempts or wire
`asb run`/`asb sweep`; AR-1329 remains fail-closed.

- 2026-09-23T17:20:00+00:00: Created from the AR-1349 evidence-backed blocker.
