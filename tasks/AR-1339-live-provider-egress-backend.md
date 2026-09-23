---
{
  "branch": "feature/ar-1339-live-provider-egress-backend",
  "checkpoint_commit": "90d50561ee76df6711a2235c0ad4feccc55fc6e5",
  "claim_expires": "2026-09-23T10:55:16+00:00",
  "depends_on": [
    "AR-1328"
  ],
  "id": "AR-1339",
  "next_action": "Monitor PR #256 at 90d50561ee76df6711a2235c0ad4feccc55fc6e5 for all hosted checks and independent review; do not merge until every required check is green.",
  "observed_branch": "feature/ar-1339-live-provider-egress-backend",
  "observed_dirty": 1,
  "observed_head": "90d50561ee76df6711a2235c0ad4feccc55fc6e5",
  "owner": "codex-asb-ar1339-20260923",
  "plan": "../plans/AR-1339-live-provider-egress-backend.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Implement the runtime-owned authenticated backend for explicit live provider egress.",
  "task_revision": 18,
  "title": "Runtime-owned live-provider egress backend",
  "updated_at": "2026-09-23T09:36:26+00:00",
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

- 2026-09-23T09:05:57+00:00: Added bounded relay primitive with synthetic denial tests. No external
  network tests performed; offline/replay NetworkPolicy::Deny remains unchanged.

- 2026-09-23T09:07:44+00:00: Reconciled public-IP allowlist and launch-fenced authorization into
  relay implementation. Six provider_egress tests pass; cargo check -p asb-cli passes. No
  offline/replay network policy changes.

- 2026-09-23T09:31:53+00:00: Recorded command exit 0; command argv SHA-256
  a939c40452ec796a264d7aa64185f5e9346c0b91b754d97dab4d11d4eab8dbc0.

- 2026-09-23T09:32:52+00:00: Observed signed security-hardening head
  90d50561ee76df6711a2235c0ad4feccc55fc6e5 for PR #256. Durable state remains in_progress pending
  hosted checks and independent review.

- 2026-09-23T09:36:16+00:00: Recorded command exit 0; command argv SHA-256
  4bb64dde06ee231ce6820b728d8edc001c8ce3c8d8c8902de75e218b411a6ab1.
