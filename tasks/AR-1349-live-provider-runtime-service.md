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
    "AR-1347",
    "AR-1348"
  ],
  "id": "AR-1349",
  "next_action": "Promote after AR-1327, AR-1328, AR-1339, AR-1340, AR-1347 and AR-1348 are verified. Implement the production LiveProviderRuntimeService atomic acquisition boundary and wire asb run/sweep; keep AR-1329 fail-closed until exact-head CI and post-merge lifecycle evidence pass.",
  "owner": "",
  "plan": "../plans/AR-1349-live-provider-runtime-service.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Implement production-owned atomic live-provider acquisition and wire it into asb run and sweep.",
  "task_revision": 1,
  "title": "Production live-provider runtime service",
  "updated_at": "2026-09-23T00:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1349-live-provider-runtime-service"
}
---

Coordinator successor for the exact authority gap recorded by AR-1348:
production asb run/sweep currently accepts only injected live-attempt factories,
while runtime constructors require caller-built leases, namespace handoffs,
tokens and relays. This task supplies the single rollback-safe owner for those
resources and preserves AR-1329 fail-closed until the service is merged and
qualified.
