---
{
  "branch": "feature/ar-1343-runtime-live-provider-relay",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-23T14:27:56+00:00",
  "depends_on": [
    "AR-1327",
    "AR-1328",
    "AR-1339",
    "AR-1340"
  ],
  "id": "AR-1343",
  "next_action": "Implement the runtime-owned bounded live provider relay service and per-attempt CLI factory acquisition; keep AR-1329 fail-closed until merged and verified.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "codex-asb-ar1343-20260923",
  "plan": "../plans/AR-1343-runtime-live-provider-relay.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Add the runtime live-provider relay service and per-attempt opaque factory acquisition required by asb run and sweep.",
  "task_revision": 2,
  "title": "Runtime live-provider relay service and CLI acquisition",
  "updated_at": "2026-09-23T12:27:56+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1343-runtime-live-provider-relay"
}
---

AR-1329 integration audit after AR-1342 found that the opaque
`LiveLaunchFactory` is present but not CLI-consumable: there is no runtime live
relay listener/request protocol, concrete egress target acquisition, or
credential transport. This successor supplies those missing runtime-owned
capabilities without bypassing the denied-network sandbox.

- 2026-09-23: Created from the AR-1329 integration audit. Do not enable direct
  provider sockets or construct live handoffs in asb-cli.

- 2026-09-23T12:27:09+00:00: Claimed by codex-asb-ar1343-20260923.

- 2026-09-23T12:27:56+00:00: Heartbeat by codex-asb-ar1343-20260923.
