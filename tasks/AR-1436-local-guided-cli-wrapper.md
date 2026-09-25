---
{
  "branch": "feature/ar-1436-local-guided-cli-wrapper",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-25T02:43:20+00:00",
  "depends_on": [
    "AR-1435",
    "AR-1328"
  ],
  "id": "AR-1436",
  "next_action": "Promote and claim when completed dependencies are confirmed; implement the offline catalog-driven local mock wrapper and preserve AR-1329/AR-1338 blocked and AR-1332/AR-1333 planned.",
  "observed_branch": "feature/ar-1436-local-guided-cli-wrapper",
  "observed_dirty": 1,
  "observed_head": "cc82333a53e03147ea95cc21ca697647dc27db1f",
  "owner": "codex-asb-ar1436-local-guided-luna56",
  "plan": "../plans/AR-1436-local-guided-cli-wrapper.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Add a catalog-driven guided CLI wrapper for deterministic local mock qualification.",
  "task_revision": 8,
  "title": "Local guided CLI wrapper",
  "updated_at": "2026-09-25T00:45:55+00:00",
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

- 2026-09-25T00:43:12+00:00: Promoted: completed dependencies AR-1435 and AR-1328 verified.
  AR-1332/AR-1333 remain planned references only; AR-1329/AR-1338 untouched. Begin local-only
  catalog-driven wrapper with explicit mock qualification and fail-closed live path.

- 2026-09-25T00:43:20+00:00: Claimed by codex-asb-ar1436-local-guided-luna56.

- 2026-09-25T00:43:33+00:00: Recorded command exit 0; command argv SHA-256
  b3c54e469f86e1ddbb6f6063fc4d2921be9e210b1bfce5de3610ed8e03380946.

- 2026-09-25T00:45:36+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-25T00:45:55+00:00: Recorded command exit 1; command argv SHA-256
  856c2c32ebf286180f6e23e7f1e8ae20312ff6548988a044a5afc15e6a8595d4.
