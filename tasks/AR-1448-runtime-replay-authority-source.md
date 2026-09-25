---
{
  "branch": "main",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-25T17:52:13+00:00",
  "depends_on": [
    "AR-1443",
    "AR-1446"
  ],
  "id": "AR-1448",
  "next_action": "Promote and claim this dependency-ready successor. Implement the bounded control/runtime materializer without exposing replay authority to the CLI.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "coordinator-ar1448",
  "plan": "../plans/AR-1448-runtime-replay-authority-source.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Materialize runtime-owned strict replay authority for normal CLI replay.",
  "task_revision": 4,
  "title": "Runtime replay authority source",
  "updated_at": "2026-09-25T15:52:39+00:00",
  "worktree_key": "agent-systems-benchmark"
}
---

Successor created from the AR-1331 audit. Do not synthesize authority in the
CLI and do not make external provider access a prerequisite.

- 2026-09-25T15:52:10+00:00: AR-1331 audit confirmed the dependency-ready missing runtime/control
  replay authority source. Promote this ASB-only repair; no live provider or asb-tui dependency.

- 2026-09-25T15:52:13+00:00: Claimed by coordinator-ar1448.

- 2026-09-25T15:52:39+00:00: Recorded command exit 0; command argv SHA-256
  c50ebcf13872ea281f11a42f41a2dd9cdeb289092ade8d36d346e13a0a9f753e.
