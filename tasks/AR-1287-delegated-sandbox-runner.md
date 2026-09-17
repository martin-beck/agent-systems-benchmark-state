---
{
  "branch": "feature/ar-1287-delegated-sandbox-runner",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1286"],
  "id": "AR-1287",
  "next_action": "Promote only after confirming AR-1286 blocked evidence; provision a pinned container/VM runner under /srv/data/projects and prove qualified namespace/systemd/egress capability.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1287.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Provide a delegated runner for real strict-replay child lifecycle qualification.",
  "task_revision": 1,
  "title": "Delegated sandbox runner capability",
  "updated_at": "2026-09-17T00:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1287-delegated-sandbox-runner"
}
---

## AR-1287

Set up the approved container/VM execution boundary required by AR-1286. Do not claim product
lifecycle completion until the actual child and fault fixtures run in the qualified boundary.
