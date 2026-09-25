---
{
  "branch": "feature/ar-1448-runtime-replay-authority-source",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1443",
    "AR-1446"
  ],
  "id": "AR-1448",
  "next_action": "Promote and claim this dependency-ready successor. Implement the bounded control/runtime materializer without exposing replay authority to the CLI.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1448-runtime-replay-authority-source.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Materialize runtime-owned strict replay authority for normal CLI replay.",
  "task_revision": 2,
  "title": "Runtime replay authority source",
  "updated_at": "2026-09-25T15:52:10+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1448-runtime-replay-authority-source"
}
---

Successor created from the AR-1331 audit. Do not synthesize authority in the
CLI and do not make external provider access a prerequisite.

- 2026-09-25T15:52:10+00:00: AR-1331 audit confirmed the dependency-ready missing runtime/control
  replay authority source. Promote this ASB-only repair; no live provider or asb-tui dependency.
