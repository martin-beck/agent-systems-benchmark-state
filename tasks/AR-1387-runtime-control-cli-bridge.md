---
{
  "branch": "feature/ar-1387-runtime-control-cli-bridge",
  "checkpoint_commit": "25548846966e37646dded8d67ed8ee5123b8bc32",
  "claim_expires": "",
  "depends_on": [
    "AR-1385",
    "AR-1384",
    "AR-1378",
    "AR-1377"
  ],
  "id": "AR-1387",
  "next_action": "Refresh the declared isolated worktree from protected main, add the authenticated runtime/control bootstrap-to-CLI bridge, and test opaque dispatch-source transfer without caller authority injection.",
  "observed_branch": "feature/ar-1387-runtime-control-cli-bridge",
  "observed_dirty": 0,
  "observed_head": "25548846966e37646dded8d67ed8ee5123b8bc32",
  "owner": "",
  "plan": "../plans/AR-1387-runtime-control-cli-bridge.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Bridge authenticated runtime/control bootstrap state into the production CLI dispatch path.",
  "task_revision": 2,
  "title": "Authenticated runtime-control CLI bridge",
  "updated_at": "2026-09-24T06:36:21+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1387-runtime-control-cli-bridge"
}
---

This repair owns the missing authenticated source in the CLI process. It must
consume only runtime/control-owned enrollment and opaque handles; no CLI option,
config file, environment value, endpoint, credential, policy, root, tool pin,
namespace identity, or launch token may become caller authority.

- 2026-09-24T06:36:21+00:00: AR-1386 blocked predecessor preserved; AR-1387 supersedes its missing
  bridge scope; dependencies verified
