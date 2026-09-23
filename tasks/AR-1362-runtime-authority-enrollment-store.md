---
{
  "branch": "feature/ar-1362-runtime-authority-enrollment-store",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1359"
  ],
  "id": "AR-1362",
  "next_action": "Promote after AR-1359 is done, then implement durable runtime-owned authority enrollment state consumed by the control receipt source.",
  "observed_branch": "feature/ar-1362-runtime-authority-enrollment-store",
  "observed_dirty": 0,
  "observed_head": "be9af3d6fb22818e95f51b9640b10c5eb6e043f3",
  "owner": "",
  "plan": "../plans/AR-1362-runtime-authority-enrollment-store.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Persist authenticated runtime authority enrollment required for receipt issuance without exposing secrets.",
  "task_revision": 1,
  "title": "Runtime authority enrollment store",
  "updated_at": "2026-09-24T00:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1362-runtime-authority-enrollment-store"
}
---

Successor for blocked AR-1361. Do not touch asb-tui or synthesize provider
authority from CLI/config inputs.

- 2026-09-24T00:00:00+00:00: Created after AR-1361 found the control catalog
  lacks authenticated certificate-chain and runtime-owned target/tool/lease/
  relay authority required to issue a receipt.
