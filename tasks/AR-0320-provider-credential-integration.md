---
{
  "branch": "feature/provider-credential-integration",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-08T17:17:03+00:00",
  "depends_on": [
    "AR-0318"
  ],
  "id": "AR-0320",
  "next_action": "Integrate the signed AR-0318 environment credential boundary into product main and rerun workspace gates.",
  "owner": "quality_20260906",
  "plan": "../plans/AR-0320.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Integrate the verified environment credential resolver into the product workspace.",
  "task_revision": 3,
  "title": "Integrate provider credential boundary",
  "updated_at": "2026-09-08T14:17:03+00:00",
  "worktree_key": "agent-systems-benchmark-provider-credential-integration"
}
---
## AR-0320

Integrate the signed AR-0318 environment credential boundary into the product workspace so downstream provider preflight can run against an exact product tree.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-08T14:17:00+00:00: AR-0318 is done but its reviewed source is absent from product main;
  serialize integration before AR-0314 live preflight.

- 2026-09-08T14:17:03+00:00: Claimed by quality_20260906.
