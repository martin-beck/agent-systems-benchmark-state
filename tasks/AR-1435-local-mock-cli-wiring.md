---
{
  "branch": "feature/ar-1435-local-mock-cli-wiring",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1434"
  ],
  "id": "AR-1435",
  "next_action": "Verify AR-1434 is done, promote and claim, bind an isolated worktree, then wire asb run and asb sweep --use-config through the runtime-owned local mock backend with offline/default denial preserved.",
  "owner": "",
  "plan": "../plans/AR-1435-local-mock-cli-wiring.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Wire deterministic local mock attempts into asb run and sweep configuration qualification.",
  "task_revision": 2,
  "title": "Local mock CLI wiring",
  "updated_at": "2026-09-24T23:48:43+00:00",
  "worktree_key": ""
}
---

Local-only successor to AR-1434. AR-1329 and AR-1432 remain blocked and are
not resumed. This task may exercise only the deterministic runtime-owned mock;
it must not contact OpenRouter or any external provider, mint
`LiveProviderAttempt`, or weaken production egress and default-denial gates.

- 2026-09-24T23:48:43+00:00: AR-1434 is durably done. Promote this sole-dependency local-only CLI
  wiring successor; preserve AR-1329 and AR-1432 blocked, production egress/default denial
  unchanged, and require focused/full/review/PR/seven post-merge gates.
