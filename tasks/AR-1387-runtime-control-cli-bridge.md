---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1385",
    "AR-1384",
    "AR-1378",
    "AR-1377"
  ],
  "id": "AR-1387",
  "next_action": "Promote after dependency validation; add the authenticated runtime/control bootstrap-to-CLI bridge that supplies the opaque dispatch source without caller authority injection.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "",
  "plan": "../plans/AR-1387-runtime-control-cli-bridge.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Bridge authenticated runtime/control bootstrap state into the production CLI dispatch path.",
  "task_revision": 1,
  "title": "Authenticated runtime-control CLI bridge",
  "updated_at": "2026-09-24T06:36:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1387-runtime-control-cli-bridge"
}
---

This repair owns the missing authenticated source in the CLI process. It must
consume only runtime/control-owned enrollment and opaque handles; no CLI option,
config file, environment value, endpoint, credential, policy, root, tool pin,
namespace identity, or launch token may become caller authority.
