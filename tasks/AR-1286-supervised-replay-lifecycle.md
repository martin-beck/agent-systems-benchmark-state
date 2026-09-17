---
{
  "branch": "feature/ar-1286-supervised-replay-lifecycle",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1282",
    "AR-1285",
    "AR-1237",
    "AR-1238",
    "AR-1239"
  ],
  "id": "AR-1286",
  "next_action": "Promote after dependency verification; create the declared isolated worktree from protected main and implement real supervised cassette execution with egress denial, lifecycle cleanup, and no-fallback evidence.",
  "observed_branch": "feature/ar-1286-supervised-replay-lifecycle",
  "observed_dirty": 0,
  "observed_head": "65b6aa19aa0236051b85862aa4b35293841794ca",
  "owner": "",
  "plan": "../plans/AR-1286.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Execute strict-replay cassettes through the runtime-owned supervised lifecycle.",
  "task_revision": 1,
  "title": "Supervised strict-replay cassette lifecycle",
  "updated_at": "2026-09-17T00:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1286-supervised-replay-lifecycle"
}
---

## AR-1286

Implement the next ASB-only lifecycle boundary after the merged AR-1282 transport and AR-1285
launch factory. Preserve all fail-closed authority, egress, cleanup, and no-fallback requirements;
do not touch or claim asb-tui behavior.

- Created as the dependency-safe successor for the supervised cassette lifecycle after AR-1282 and
  AR-1285 completed. Earlier blocked replay lifecycle records remain historical evidence and are
  not implementation inputs.
