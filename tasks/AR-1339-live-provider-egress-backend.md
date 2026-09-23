---
{
  "branch": "feature/ar-1339-live-provider-egress-backend",
  "checkpoint_commit": "e69dc146e2b0eb341a8791fb5d53a5276dea1dc6",
  "claim_expires": "2026-09-23T10:55:16+00:00",
  "depends_on": [
    "AR-1328"
  ],
  "id": "AR-1339",
  "next_action": "Implement actual runtime-owned authenticated outbound relay: consume ProviderEgressAuthorization and ProviderEgressAllowlist, connect only prevalidated SocketAddr targets over HTTPS, reject redirects/DNS changes, and preserve NetworkPolicy::Deny offline/replay.",
  "observed_branch": "feature/ar-1339-live-provider-egress-backend",
  "observed_dirty": 0,
  "observed_head": "e69dc146e2b0eb341a8791fb5d53a5276dea1dc6",
  "owner": "codex-asb-ar1339-20260923",
  "plan": "../plans/AR-1339-live-provider-egress-backend.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Implement the runtime-owned authenticated backend for explicit live provider egress.",
  "task_revision": 10,
  "title": "Runtime-owned live-provider egress backend",
  "updated_at": "2026-09-23T09:01:14+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1339-live-provider-egress-backend"
}
---

AR-1329 now has a typed, fail-closed provider egress identity contract, but the
runtime still has no network-capable authenticated backend. This AR supplies
that missing boundary so live provider execution can be enabled safely.

- 2026-09-23T08:55:13+00:00: Created after AR-1329 confirmed the runtime has no safe provider-egress
  backend; AR-1328 dependency is complete and typed egress contract is available.

- 2026-09-23T08:55:16+00:00: Claimed by codex-asb-ar1339-20260923.

- 2026-09-23T08:58:06+00:00: Added launch-fenced ProviderEgressHandoff and
  ProviderEgressAuthorization. Tests cover exact HTTPS host, credential/query rejection, stale
  generation/route/deadline. NetworkPolicy::Deny remains unchanged.

- 2026-09-23T09:01:14+00:00: Integrated public-IP exact allowlist types with launch-fenced handoff.
  Four provider_egress tests and CLI check pass. Concrete next step is relay transport/backend, not
  more policy-only work.
