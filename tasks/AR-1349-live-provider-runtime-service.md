---
{
  "branch": "feature/ar-1349-live-provider-runtime-service",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-23T18:30:27+00:00",
  "depends_on": [
    "AR-1327",
    "AR-1328",
    "AR-1339",
    "AR-1340",
    "AR-1347"
  ],
  "id": "AR-1349",
  "next_action": "Promote after AR-1327, AR-1328, AR-1339, AR-1340 and AR-1347 are verified. AR-1348 is superseded as partial lifecycle evidence by this coordinator repair. Implement the production LiveProviderRuntimeService atomic acquisition boundary and wire asb run/sweep; keep AR-1329 fail-closed until exact-head CI and exact lifecycle evidence pass.",
  "observed_branch": "feature/ar-1349-live-provider-runtime-service",
  "observed_dirty": 2,
  "observed_head": "a336d6744b1a82f36a706ec606b847c92d49cfd3",
  "owner": "codex-asb-ar1329-live-cli-luna56",
  "plan": "../plans/AR-1349-live-provider-runtime-service.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Implement production-owned atomic live-provider acquisition and wire it into asb run and sweep.",
  "task_revision": 9,
  "title": "Production live-provider runtime service",
  "updated_at": "2026-09-23T16:33:20+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1349-live-provider-runtime-service"
}
---

Coordinator successor for the exact authority gap recorded by AR-1348:
production asb run/sweep currently accepts only injected live-attempt factories,
while runtime constructors require caller-built leases, namespace handoffs,
tokens and relays. This task supplies the single rollback-safe owner for those
resources and preserves AR-1329 fail-closed until the service is merged and
qualified.

- 2026-09-23T16:30:20+00:00: Dependencies AR-1327, AR-1328, AR-1339, AR-1340 and AR-1347 are
  verified done. AR-1348 is superseded partial lifecycle evidence and intentionally removed from
  dependencies; promote this coordinator repair for claim readiness. AR-1329 remains fail-closed.

- 2026-09-23T16:30:27+00:00: Claimed by codex-asb-ar1329-live-cli-luna56.

- 2026-09-23T16:31:31+00:00: Recorded command exit 0; command argv SHA-256
  7c145cae25b02f870487e3a09450303496a9a72f7b01b10b754f5034e73197ad.

- 2026-09-23T16:32:49+00:00: Recorded command exit 0; command argv SHA-256
  d64018b6cc02f84681ffc81a8a687a9959932773ce8e540ab4b18e3a894b2ec5.

- 2026-09-23T16:33:05+00:00: Recorded command exit 0; command argv SHA-256
  67138335f249d78ff455f950c8e42fb8019bc5afa30cdcc6ed983cefa0fabf35.

- 2026-09-23T16:33:20+00:00: Recorded command exit 101; command argv SHA-256
  f39ddc9090535b3b2a160bb90c4b1d5e119ca094c2325507a8605d9d70c7cc41.
