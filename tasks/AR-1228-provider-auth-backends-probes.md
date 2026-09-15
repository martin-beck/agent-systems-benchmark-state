---
{
  "branch": "feature/ar-1228-auth-backends-probes",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0319",
    "AR-0320",
    "AR-1100"
  ],
  "id": "AR-1228",
  "next_action": "Promote after dependencies are independently complete; implement concrete qualified secret backends, provider probes and durable CLI/control/config integration for AR-1120.",
  "owner": "",
  "plan": "../plans/AR-1228.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Qualify provider authentication backends, probes and application integration.",
  "task_revision": 5,
  "title": "Qualify provider authentication backends and probes",
  "updated_at": "2026-09-15T18:11:45+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1228-auth-backends-probes"
}
---

Define approved secret-storage, provider-probe and application integration authority required to
complete AR-1120 without adding ambient or plaintext credential paths. This AR owns concrete
integration rather than renderer or frontend behavior.

- 2026-09-15T18:10:00+00:00: Created after independent review of AR-1120 identified that its
  injected `SecretBackend` seam has no qualified concrete backend, provider-specific bounded probe,
  or CLI/control/config durable integration. Existing resolver primitives must be bound without
  weakening their privacy boundary.

- 2026-09-15T18:10:37+00:00: Dependencies AR-0319, AR-0320 and AR-1100 are complete; begin concrete
  qualified auth backend, bounded provider probe and durable CLI/control/config integration required
  by blocked AR-1120.

- 2026-09-15T18:10:58+00:00: Claimed by asb_ar1228_auth_backends.

- 2026-09-15T18:11:35+00:00: Heartbeat by asb_ar1228_auth_backends.

- 2026-09-15T18:11:45+00:00: Implementation audit complete: existing ASB resolver primitives are
  concrete for launch-time env/FD/helper resolution, but AR-1228 acceptance requires an approved
  durable secret authority and provider-specific probe/application wiring not present in current
  architecture. No unsafe ambient, plaintext, or unqualified network implementation was added.
  Earliest next action: architecture owner must qualify backend/probe contract and integration
  boundary, then reclaim AR-1228.
