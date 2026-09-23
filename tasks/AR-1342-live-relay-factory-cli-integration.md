---
{
  "branch": "feature/ar-1342-live-relay-factory-cli-integration",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1327",
    "AR-1328",
    "AR-1339",
    "AR-1340"
  ],
  "id": "AR-1342",
  "next_action": "Promote now that provider contracts, the runtime egress backend, and attested handoff are complete; implement the factory without weakening offline/replay denial, then return to AR-1329.",
  "observed_branch": "feature/ar-1342-live-relay-factory-cli-integration",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1342-live-relay-factory-cli-integration.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "open",
  "summary": "Create the runtime-owned relay factory and opaque launch context required for safe live CLI execution.",
  "task_revision": 2,
  "title": "Runtime-owned live relay factory and CLI integration",
  "updated_at": "2026-09-23T11:33:12+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1342-live-relay-factory-cli-integration"
}
---

AR-1329 integration audit found that AR-1340 correctly requires a pre-issued
namespace-bound handoff and validated relay socket, but `asb-cli` has no
sanctioned acquisition path. This repair supplies that runtime-owned factory;
until it is complete, live spawning remains fail-closed.

- 2026-09-23: Created from the AR-1329 integration audit. Do not bypass the
  runtime boundary or enable direct provider/network access from the CLI.

- 2026-09-23T11:33:12+00:00: Dependencies AR-1327, AR-1328, AR-1339 and AR-1340 are done; promote
  runtime-owned relay factory repair to unblock AR-1329 without weakening fail-closed policy.
