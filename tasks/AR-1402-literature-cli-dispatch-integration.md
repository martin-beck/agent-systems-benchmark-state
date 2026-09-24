---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1401"
  ],
  "id": "AR-1402",
  "next_action": "Promote after AR-1401 is done; replace OriginalWorkloads-only CLI seams with catalog/adapter dispatch and run end-to-end offline tests.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "",
  "plan": "../plans/AR-1402-literature-cli-dispatch-integration.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "open",
  "summary": "Integrate literature workload catalog and adapters through all ASB CLI execution and evidence paths.",
  "task_revision": 4,
  "title": "Literature workload CLI dispatch integration",
  "updated_at": "2026-09-24T12:41:59+00:00",
  "worktree_key": ""
}
---

This AR consumes only local/mock literature fixtures; it does not qualify
external benchmark datasets or providers.


- 2026-09-24T12:39:18+00:00: AR-1401 is done with merged exact-head and seven post-merge gates;
  begin CLI dispatch integration.

- 2026-09-24T12:40:17+00:00: Claimed by ar1402_literature_cli_luna56.

- 2026-09-24T12:41:59+00:00: Safe recovery: AR-1402 remains open because task metadata has empty
  declared branch and worktree_key; handoffctl rejects isolated worktree setup without those
  declarations. No product commands or changes were performed. Coordinator must bind
  codex/ar-1402-literature-cli and agent-systems-benchmark-ar-1402, then re-claim.
