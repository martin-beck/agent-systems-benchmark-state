---
{
  "branch": "feature/ar-1329-live-provider-run-execution",
  "checkpoint_commit": "e2f8dc78b9f590836bace86ced12718a09411745",
  "claim_expires": "2026-09-23T10:42:44+00:00",
  "depends_on": [
    "AR-1327",
    "AR-1328"
  ],
  "id": "AR-1329",
  "next_action": "Route live-provider launches through the existing authenticated declared-egress runtime boundary; current commit adds explicit --live-provider gating and credential resolution but does not yet qualify network enforcement.",
  "owner": "codex-asb-ar1329-20260923",
  "plan": "../plans/AR-1329.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Execute real agents against the selected provider through asb run and sweep with credential-free resolution.",
  "task_revision": 5,
  "title": "Live-provider run execution for real agents",
  "updated_at": "2026-09-23T08:48:27+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1329-live-provider-run-execution"
}
---

`asb run` and `asb sweep` currently execute a digest-pinned `batch-stdio-v1`
runtime stub instead of a real agent, so no benchmark can produce live evidence.
This AR wires the AR-1327 OpenRouter adapter projections into the execution path
so `run` and `sweep` launch a real agent process against the selected provider
and workload, resolves credentials only through the enrolled environment
channel, enforces the declared egress allowances, and requires an explicit
opt-in flag for any live provider contact. Offline CI, synthetic doubles, and
the digest-pinned mode remain default and never touch the network.

- 2026-09-23T08:41:51+00:00: Dependencies AR-1327 and AR-1328 are done; begin live provider
  execution implementation.

- 2026-09-23T08:41:54+00:00: Claimed by codex-asb-ar1329-20260923.

- 2026-09-23T08:42:44+00:00: Heartbeat by codex-asb-ar1329-20260923.

- 2026-09-23T08:48:27+00:00: Focused CLI and workflow tests pass. Live credential transport is
  bounded and secret-free; AR remains in_progress pending authenticated relay/egress integration and
  denial tests.
