---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1388",
    "AR-1385",
    "AR-1373",
    "AR-1366",
    "AR-1341",
    "AR-1342",
    "AR-1339",
    "AR-1340"
  ],
  "id": "AR-1390",
  "next_action": "Promote after all runtime authority dependencies are verified, then bind an isolated worktree and implement the runtime-owned live acquisition and normal CLI run/sweep bridge.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "",
  "plan": "../plans/AR-1390-runtime-live-acquisition-cli.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Compose runtime-owned live provider acquisition and wire it into normal ASB run and sweep.",
  "task_revision": 2,
  "title": "Runtime live acquisition and CLI bridge",
  "updated_at": "2026-09-24T07:36:40+00:00",
  "worktree_key": ""
}
---

This AR is the narrowly scoped production successor required to unblock
AR-1329. It must not touch asb-tui, accept synthetic authority, or make an
external provider connection a development or CI requirement.

- 2026-09-24T07:36:40+00:00: All runtime authority, receipt, egress, namespace, and relay
  dependencies verified done; promote production-owned live acquisition/CLI bridge successor for
  AR-1329.
