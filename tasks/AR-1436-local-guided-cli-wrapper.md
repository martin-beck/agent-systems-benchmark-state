---
{
  "branch": "feature/ar-1436-local-guided-cli-wrapper",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1435", "AR-1328"],
  "id": "AR-1436",
  "next_action": "Promote and claim when completed dependencies are confirmed; implement the offline catalog-driven local mock wrapper and preserve AR-1329/AR-1338 blocked and AR-1332/AR-1333 planned.",
  "owner": "",
  "plan": "../plans/AR-1436-local-guided-cli-wrapper.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Add a catalog-driven guided CLI wrapper for deterministic local mock qualification.",
  "task_revision": 1,
  "title": "Local guided CLI wrapper",
  "updated_at": "2026-09-25T02:42:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1436-local-guided-cli-wrapper"
}
---

Local-only successor to AR-1435. This task may use only the deterministic
runtime-owned local mock. AR-1329 and AR-1338 remain blocked/planned and are
not resumed. AR-1332 and AR-1333 are future integration references, not
completion dependencies; AR-1333 reaches the blocked live-provider chain.

The wrapper must remain a thin catalog/config-driven delegation layer over
`asb run` and `asb sweep --use-config`, with explicit local qualification,
offline/default denial, no external provider, no credential bytes, no caller
endpoint, no `LiveProviderAttempt`, and no production egress or authority
weakening. Require focused/full/review/PR/seven post-merge gates.
