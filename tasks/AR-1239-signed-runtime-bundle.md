---
{
  "branch": "feature/ar-1239-signed-runtime-bundle",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1236"
  ],
  "id": "AR-1239",
  "next_action": "Implement asb-bundle-owned manifest/payload wiring for the supervisor and sidecar, then sign and verify the canonical bundle offline.",
  "observed_branch": "feature/ar-1239-signed-runtime-bundle",
  "observed_dirty": 0,
  "observed_head": "6836bb4010f55062ae3c3f6eac793c53c08495c8",
  "owner": "",
  "plan": "../plans/AR-1239.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "done",
  "summary": "Package and sign the verified loopback supervisor and sidecar runtime payloads.",
  "task_revision": 5,
  "title": "Signed supervisor and sidecar runtime bundle",
  "updated_at": "2026-09-16T08:30:33+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1239"
}
---

Own only the `asb-bundle` packaging and verification boundary. Do not modify TUI code or take over
AR-1238 runtime launch logic. The bundle must provide immutable, signed payload identities that
SandboxBackend can consume without a mutable `/usr` fallback. Preserve privacy, fail-closed
verification, and unrelated-process safety.

- 2026-09-16T08:29:57+00:00: AR-1236 is done; signed bundle implementation 6836bb4 and verifier
  gates complete. Promote for release review.

- 2026-09-16T08:30:12+00:00: Claimed by asb_ar1239_bundle_worker.

- 2026-09-16T08:30:33+00:00: Implemented signed supervisor/sidecar manifest payload wiring in
  6836bb4010f55062ae3c3f6eac793c53c08495c8. Verified exact ED25519 commit signature
  (SHA256:a36V6yPvRZyxnQ2113tiA/MlHt7mPfJEXAGByBXVkuE), DCO, locked asb-bundle tests (18 offline
  verifier + 2 schema; all unit/doc), workspace clippy -D warnings, and workspace rustdoc -D
  warnings. Runtime launch/native Bubblewrap remains AR-1238 scope.
