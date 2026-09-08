---
{
  "branch": "fix/aider-deterministic-replay",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-08T05:14:52+00:00",
  "depends_on": [
    "AR-0303",
    "AR-0508"
  ],
  "id": "AR-0850",
  "next_action": "Make pinned aider multi-file capture ordering deterministic across separately spawned processes, then prove strict replay parity and rerun the native journey.",
  "owner": "quality_20260906",
  "plan": "../plans/AR-0850.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Repair aider replay nondeterminism caused by process-dependent file ordering.",
  "task_revision": 3,
  "title": "Repair deterministic aider replay",
  "updated_at": "2026-09-08T02:14:52+00:00",
  "worktree_key": "agent-systems-benchmark-aider-deterministic-replay"
}
---
## AR-0850

Repair the pinned aider 0.86.2 production-boundary replay defect found during AR-0505
integration audit. Separate isolated processes currently produce different multi-file
message ordering because the client iterates a Python set. Add deterministic hash/order
control or a stronger adapter-side ordering guarantee, prove equality across independent
capture processes, strict replay parity, privacy-safe negative/unset behavior, and the
complete bounded native journey. Do not weaken replay comparison or duplicate AR-0515's
aggregate matrix.

- 2026-09-08T02:13:22+00:00: Promote focused P0 repair for deterministic pinned aider replay
  nondeterminism found by exact-tree AR-0505 audit; dependencies AR-0303 and AR-0508 are done.

- 2026-09-08T02:14:52+00:00: Claimed by quality_20260906.
