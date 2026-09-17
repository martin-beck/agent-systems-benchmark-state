---
{
  "branch": "feature/ar-1281-supervised-cassette-lifecycle",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1237",
    "AR-1238",
    "AR-1239"
  ],
  "id": "AR-1281",
  "next_action": "Promote after dependency verification; implement the complete supervised cassette path and lifecycle fault matrix from protected main.",
  "observed_branch": "feature/ar-1281-supervised-cassette-lifecycle",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1281.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Execute primary strict replay through a supervised runtime cassette lifecycle.",
  "task_revision": 2,
  "title": "Supervised cassette lifecycle execution",
  "updated_at": "2026-09-17T00:19:58+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1281-supervised-cassette-lifecycle"
}
---

## AR-1281

Implement complete supervised cassette lifecycle execution from protected main. Preserve prior
blocked evidence while requiring real process invocation and fault-matrix proof.

- 2026-09-17T00:19:58+00:00: Dependencies AR-1237, AR-1238, and AR-1239 are done. Prior ARs
  establish missing seams but remain blocked; this AR must implement complete supervised cassette
  execution from protected main.
