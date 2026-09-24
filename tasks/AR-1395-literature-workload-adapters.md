---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-24T10:42:24+00:00",
  "depends_on": [
    "AR-1394"
  ],
  "id": "AR-1395",
  "next_action": "Promote after AR-1394 is done, then implement family adapters and deterministic offline fixtures behind the workload lifecycle contract.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "codex-asb-ar1395-literature-adapters-luna56",
  "plan": "../plans/AR-1395-literature-workload-adapters.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Normalize approved literature tasks through bounded, non-vendored ASB workload adapters.",
  "task_revision": 4,
  "title": "Literature workload adapter boundary",
  "updated_at": "2026-09-24T08:43:39+00:00",
  "worktree_key": ""
}
---

Adapters must preserve source semantics and never turn provenance-only entries
into executable or qualified workloads.

- 2026-09-24T08:41:11+00:00: AR-1394 registry is merged and all seven exact-main post-merge
  workflows are green; promote adapter boundary.

- 2026-09-24T08:42:24+00:00: Claimed by codex-asb-ar1395-literature-adapters-luna56.

- 2026-09-24T08:43:39+00:00: Recorded command exit 0; command argv SHA-256
  e3d2e9fa53e551fc08c72cf1833bdcfb806cc107dad75f76721191ca46c7ff7c.
