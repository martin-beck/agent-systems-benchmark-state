---
{
  "branch": "feature/ar-1363-authenticated-control-receipt-source",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1362"
  ],
  "id": "AR-1363",
  "next_action": "Promote after AR-1362 is done, then implement the bounded authenticated control receipt source consumed by runtime-owned dispatch.",
  "observed_branch": "feature/ar-1363-authenticated-control-receipt-source",
  "observed_dirty": 0,
  "observed_head": "e9d4d3d1c6a4d67d0ce0e49fa8eaf696561fe45e",
  "owner": "",
  "plan": "../plans/AR-1363-authenticated-control-receipt-source.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Deliver authenticated runtime authority receipts through the versioned control boundary without exposing secrets or caller authority.",
  "task_revision": 1,
  "title": "Authenticated control receipt source",
  "updated_at": "2026-09-24T00:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1363-authenticated-control-receipt-source"
}
---

Successor for blocked AR-1361, explicitly depending on completed AR-1362.
Do not touch asb-tui, reopen stale dependencies, or synthesize authority in CLI.

- 2026-09-24T00:00:00+00:00: Created after AR-1362 delivered the durable
  digest-only runtime authority enrollment contract and all post-merge gates.
