---
{
  "branch": "feature/ar-1344-runtime-cli-acquisition-contract",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1339", "AR-1340", "AR-1342"],
  "id": "AR-1344",
  "next_action": "Promote after dependencies are verified; implement the runtime-owned per-attempt CLI acquisition API and wire run/sweep without weakening live-provider fail-closed behavior.",
  "owner": "",
  "plan": "../plans/AR-1344-runtime-cli-acquisition-contract.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Add the runtime-owned API and CLI integration needed for safe live-provider attempts.",
  "task_revision": 1,
  "title": "Runtime-owned CLI live acquisition contract",
  "updated_at": "2026-09-23T00:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1344-runtime-cli-acquisition-contract"
}
---

Created from the AR-1329/AR-1343 audit. The bounded relay is available at
`ce2c2db068b05092f0f63291e0d94d4dbc9cda9c`, but the CLI still has no supported
runtime acquisition seam. Keep `spawn_verified_agent` fail-closed until this
contract and its tests are merged and verified.
