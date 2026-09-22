---
{
  "branch": "feature/ar-1329-live-provider-run-execution",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1327",
    "AR-1328"
  ],
  "id": "AR-1329",
  "next_action": "Replace the digest-pinned batch-stdio-v1 execution stub in asb run/sweep with real agent execution through the selected provider, keeping credential-free environment resolution, egress enforcement and explicit opt-in live runs.",
  "owner": "",
  "plan": "../plans/AR-1329.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Execute real agents against the selected provider through asb run and sweep with credential-free resolution.",
  "task_revision": 1,
  "title": "Live-provider run execution for real agents",
  "updated_at": "2026-09-22T13:39:37+00:00",
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
