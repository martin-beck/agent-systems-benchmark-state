---
{
  "branch": "feature/ar-1348-runtime-owned-live-acquisition",
  "checkpoint_commit": "a336d6744b1a82f36a706ec606b847c92d49cfd3",
  "claim_expires": "",
  "depends_on": [
    "AR-1327",
    "AR-1328",
    "AR-1339",
    "AR-1340"
  ],
  "id": "AR-1348",
  "next_action": "Promote after the AR-1347 neutral credential contract is integrated or explicitly carried into this branch; then create the declared isolated worktree and implement the runtime-owned supervisor acquisition lifecycle. Keep AR-1329 fail-closed until exact-head and post-merge evidence proves the complete lifecycle.",
  "observed_branch": "feature/ar-1348-runtime-owned-live-acquisition",
  "observed_dirty": 0,
  "observed_head": "a336d6744b1a82f36a706ec606b847c92d49cfd3",
  "owner": "",
  "plan": "../plans/AR-1348-runtime-owned-live-acquisition.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "open",
  "summary": "Provide the runtime-owned supervisor that acquires every live-provider authority and tears it down safely.",
  "task_revision": 2,
  "title": "Runtime-owned live acquisition service",
  "updated_at": "2026-09-23T15:53:44+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1348-runtime-owned-live-acquisition"
}
---

Created from the AR-1347 completion audit. AR-1329 remains fail-closed until
this service owns acquisition instead of accepting caller-built launch authority.

- 2026-09-23T15:52:00+00:00: Successor scope records the missing pinned live
  gate, benchmark lease, concrete target allowlist, namespace rebind, launch
  token, per-attempt relay, opaque credential capability and teardown lifecycle.

- 2026-09-23T15:53:44+00:00: Dependencies AR-1327, AR-1328, AR-1339 and AR-1340 are done; promote
  successor runtime acquisition repair. AR-1347 neutral credential boundary remains an integration
  prerequisite and AR-1329 stays fail-closed.
