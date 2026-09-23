---
{
  "branch": "feature/ar-1349-live-provider-runtime-service",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1327",
    "AR-1328",
    "AR-1339",
    "AR-1340",
    "AR-1347"
  ],
  "id": "AR-1349",
  "next_action": "Promote after AR-1327, AR-1328, AR-1339, AR-1340 and AR-1347 are verified. AR-1348 is superseded as partial lifecycle evidence by this coordinator repair. Implement the production LiveProviderRuntimeService atomic acquisition boundary and wire asb run/sweep; keep AR-1329 fail-closed until exact-head CI and exact lifecycle evidence pass.",
  "owner": "",
  "plan": "../plans/AR-1349-live-provider-runtime-service.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "open",
  "summary": "Implement production-owned atomic live-provider acquisition and wire it into asb run and sweep.",
  "task_revision": 2,
  "title": "Production live-provider runtime service",
  "updated_at": "2026-09-23T16:30:20+00:00",
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
