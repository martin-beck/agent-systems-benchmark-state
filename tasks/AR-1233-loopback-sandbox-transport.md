---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1231",
    "AR-1100"
  ],
  "id": "AR-1233",
  "next_action": "Promote after AR-1232 is blocked and implement the approved loopback-only transport seam.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1233.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Provide an authenticated loopback-only sandbox transport for strict replay services.",
  "task_revision": 2,
  "title": "Approved loopback-only sandbox transport",
  "updated_at": "2026-09-16T05:06:10+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1233"
}
---

- Created from AR-1232 review: `SandboxSpec` currently accepts only `NetworkPolicy::Deny`, which
  prevents a strict replay child from reaching its owned cassette service. This prerequisite must
  add a separately authenticated loopback-only policy while preserving provider-egress denial.

- 2026-09-16T05:06:10+00:00: Promote approved loopback-only sandbox transport prerequisite;
  dependencies AR-1231 and AR-1100 are complete.
