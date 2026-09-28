---
{
  "branch": "feature/ar-1503-runtime-control-process-owner",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1473",
    "AR-1474",
    "AR-1480",
    "AR-1484",
    "AR-1485",
    "AR-1502"
  ],
  "id": "AR-1503",
  "next_action": "Promote and claim after reviewing the blocked AR-1483 evidence; implement the runtime/platform-owned control-session launcher and authenticated owner handoff.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1503-runtime-control-process-owner.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Own the authenticated control session and hand off only an opaque live dispatch source.",
  "task_revision": 2,
  "title": "Runtime/control process owner",
  "updated_at": "2026-09-28T22:06:07+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1503-runtime-control-process-owner"
}
---

Narrow successor to the blocked AR-1483 audit. The implementation must remain
ASB-only, provider-free for qualification, and fail closed. It must not modify
asb-tui, synthesize authority, or accept caller-built runtime inputs.

- 2026-09-29T00:05:00+00:00: Created from the exact AR-1483 protected-main re-audit at
  3c6af6b. AR-1502 supplies source-only bootstrap enrollment, but no owner yet constructs the
  authenticated control session, enrolled chain, private resolver, cancellation/teardown binding,
  and opaque AR-1480 source. The successor owns that missing runtime/platform boundary only.

- 2026-09-28T22:06:07+00:00: Dependencies AR-1473, AR-1474, AR-1480, AR-1484, AR-1485, and AR-1502
  verified done; promote the narrow runtime/platform-owned control-session launcher successor from
  blocked AR-1483 evidence.
