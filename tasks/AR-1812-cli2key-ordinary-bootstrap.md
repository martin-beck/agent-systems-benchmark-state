---
{
  "branch": "feature/ar-1812-cli2key-ordinary-bootstrap",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-12T12:12:04+00:00",
  "depends_on": [
    "AR-1779",
    "AR-1799"
  ],
  "id": "AR-1812",
  "next_action": "Coordinator must extend the runtime boundary with a production constructor for a cli2key sidecar-backed LiveProviderAttemptFactory (or equivalent opaque runtime source), then expose a verified AR-1779 runtime-receipt resolver contract. AR-1812 can resume only after that API exists.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "ar1810-cli2key-luna56",
  "plan": "../plans/AR-1812-cli2key-ordinary-bootstrap.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "contract-test",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1812.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1812.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Wire the verified cli2key installation and runtime authority into ordinary ASB run and sweep dispatch without fallback.",
  "task_revision": 5,
  "title": "Implement cli2key ordinary CLI bootstrap",
  "updated_at": "2026-10-12T10:13:24+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1812-cli2key-ordinary-bootstrap"
}
---

The ordinary ASB CLI currently has the AR-1799 authority seam and the AR-1779
installation contract, but no production adapter that resolves the verified
receipt and composes them for `run` and `sweep`. Implement that adapter with
strict identity checks, opaque authority retention, bounded teardown, and
typed no-fallback failures. Development qualification must use local/mock
fixtures and must not require a live provider or TLC.

- 2026-10-12T10:11:57+00:00: Promoted P0 prerequisite for AR-1810: wire verified AR-1779 cli2key
  receipt and AR-1799 opaque authority into ordinary run/sweep dispatch. Development path remains
  local/mock and non-TLC.

- 2026-10-12T10:12:04+00:00: Claimed by ar1810-cli2key-luna56.

- 2026-10-12T10:12:22+00:00: Bound worktree
  agent-systems-benchmark-ar-1812-cli2key-ordinary-bootstrap on branch
  feature/ar-1812-cli2key-ordinary-bootstrap.

- 2026-10-12T10:13:24+00:00: Implementation audit found the requested seam cannot be implemented in
  asb-cli alone: Cli2KeyRuntimeAuthority::bootstrap requires a LiveProviderAttemptFactory, but
  production construction is private to asb-runtime and only injected test factories exist. AR-1779
  generic receipt has no runtime identity fields or bridge command contract. A local resolver
  without an opaque factory would fabricate authority or fallback, violating scope. No product
  changes retained; cargo check of exploratory resolver correctly failed closed under dead-code
  warnings.
