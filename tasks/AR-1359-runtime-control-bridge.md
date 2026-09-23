---
{
  "branch": "feature/ar-1359-runtime-control-bridge",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1357"
  ],
  "id": "AR-1359",
  "next_action": "Promote after AR-1357 is done, then implement the runtime-owned asb-control enrollment bridge needed by AR-1358.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1359-runtime-control-bridge.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Bridge authenticated control enrollment into runtime-owned opaque live authority.",
  "task_revision": 2,
  "title": "Runtime/control enrollment bridge",
  "updated_at": "2026-09-23T22:28:17+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1359-runtime-control-bridge"
}
---

Successor for AR-1358's cross-crate architectural blocker. Preserve AR-1329
fail-closed behavior and do not touch asb-tui.

- 2026-09-24T00:40:00+00:00: Created after audit found no safe control/runtime
  bridge capable of issuing the merged runtime enrollment record to asb-cli.

- 2026-09-23T22:28:17+00:00: AR-1357 is done; promote the runtime-owned control bridge required by
  blocked AR-1358.
