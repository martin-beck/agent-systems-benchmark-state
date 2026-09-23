---
{
  "branch": "feature/ar-1345-runtime-live-coverage-repair",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1339", "AR-1340", "AR-1342"],
  "id": "AR-1345",
  "next_action": "Promote only after AR-1344 ownership is released; classify exact uncovered runtime lines and add bounded sandbox, relay, and provider-egress tests until the unchanged 90% workspace floor passes.",
  "observed_branch": "feature/ar-1345-runtime-live-coverage-repair",
  "observed_dirty": 0,
  "owner": "",
  "plan": "../plans/AR-1345.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Repair runtime live-provider coverage without weakening the mandatory quality floor.",
  "task_revision": 1,
  "title": "Runtime live-provider coverage repair",
  "updated_at": "2026-09-23T14:25:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1345-runtime-live-coverage-repair"
}
---

Created from the AR-1344 hosted policy failure. The candidate is at 88.53%
workspace line coverage versus the unchanged 90% floor. Preserve fail-closed
live execution and keep capability-gated runtime observations explicitly
non-authoritative.
