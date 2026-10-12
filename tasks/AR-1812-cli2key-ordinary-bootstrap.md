---
{
  "branch": "feature/ar-1812-cli2key-ordinary-bootstrap",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-12T13:19:26+00:00",
  "depends_on": [
    "AR-1779",
    "AR-1799",
    "AR-1813"
  ],
  "id": "AR-1812",
  "next_action": "AR-1813 is done and branch rebased onto current main 5c843a12. Implement ordinary run/sweep resolver using runtime Cli2KeyRuntimeAuthority::bootstrap_from_receipt_bytes and verified installer receipt; add local/mock positive/negative lifecycle tests, then PR/review/merge.",
  "observed_branch": "feature/ar-1812-cli2key-ordinary-bootstrap",
  "observed_dirty": 1,
  "observed_head": "5c843a12e976bc7be6c32e9fc653e566bdf20450",
  "owner": "ar1812-replacement-luna56",
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
  "task_revision": 19,
  "title": "Implement cli2key ordinary CLI bootstrap",
  "updated_at": "2026-10-12T11:21:09+00:00",
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

- 2026-10-12T10:13:29+00:00: Blocked on missing production runtime API: asb-runtime must expose an
  opaque sidecar-backed LiveProviderAttemptFactory/source and AR-1779 must publish a verified
  runtime receipt contract. No safe asb-cli-only implementation exists; no fallback or fabricated
  authority used.

- 2026-10-12T11:09:26+00:00: AR-1813 is released done with runtime factory/receipt API, signed merge
  5c843a12 and verified exact-main gates; prerequisite is now satisfied. Reopen for ordinary CLI
  run/sweep integration.

- 2026-10-12T11:09:41+00:00: Claimed by ar1810-cli2key-luna56.

- 2026-10-12T11:09:48+00:00: Recorded command exit 0; command argv SHA-256
  0217f97b451c01319f8c5092fe792519a33fd1e7c07b7b0177f5c3b1db13a37d.

- 2026-10-12T11:09:52+00:00: Recorded command exit 0; command argv SHA-256
  cec9ac3df8e960560d557772da347f4f99305b0d06d797c609ff7c789cdc49f9.

- 2026-10-12T11:10:15+00:00: Unblocked and claimed after AR-1813 release; existing branch rebased
  cleanly to 5c843a12. Runtime receipt/factory API is now available; no live provider or TLC
  required.

- 2026-10-12T11:11:32+00:00: Heartbeat by ar1810-cli2key-luna56.

- 2026-10-12T11:16:48+00:00: Worker interrupted after no durable progress since 11:11:32Z;
  implementation worktree remained clean. Reclaim for a replacement worker; preserve no product
  changes.

- 2026-10-12T11:19:25+00:00: Claimed by ar1812-replacement-luna56.

- 2026-10-12T11:19:26+00:00: Heartbeat by ar1812-replacement-luna56.

- 2026-10-12T11:21:06+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.
