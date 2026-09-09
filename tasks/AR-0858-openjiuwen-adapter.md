---
{
  "branch": "feature/openjiuwen-adapter",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-09T05:41:51+00:00",
  "depends_on": [
    "AR-0857"
  ],
  "id": "AR-0858",
  "next_action": "Implement the bounded agent contract, exact provider translation, and capability registration from the pinned protocol; keep live support unclaimed.",
  "owner": "replay_20260909",
  "plan": "../plans/AR-0858.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Implement the OpenJiuwen contract and capability adapter.",
  "task_revision": 4,
  "title": "Implement the OpenJiuwen contract and capability adapter",
  "updated_at": "2026-09-09T03:41:51+00:00",
  "worktree_key": "agent-systems-benchmark-openjiuwen-adapter"
}
---
## AR-0858

Implement the bounded agent contract, exact provider translation, and capability registration from the pinned protocol; keep live support unclaimed.

This phase cannot claim support from mocks, parser fixtures, source inspection, compilation, or mutable artifacts. If its executable evidence is unavailable, leave this child blocked with exact provenance evidence while the sibling agent series proceeds.

- 2026-09-09T03:41:45+00:00: AR-0857 provenance is done; promote the OpenJiuwen adapter as the next
  dependency-ready P1 implementation track with the serialized Cargo fence.

- 2026-09-09T03:41:48+00:00: Claimed by replay_20260909.

- 2026-09-09T03:41:51+00:00: Heartbeat by replay_20260909.
