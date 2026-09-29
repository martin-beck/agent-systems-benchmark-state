---
{
  "branch": "feature/ar-1513-authenticated-lease-dispatch-bridge",
  "checkpoint_commit": "be018d4f1159bde9b9725f085cb8959edf7cde4e",
  "claim_expires": "2026-09-29T07:32:46+00:00",
  "depends_on": [
    "AR-1502",
    "AR-1484"
  ],
  "id": "AR-1513",
  "next_action": "Independent exact-head review of signed be018d4; then publish PR and await protected exact-head checks.",
  "observed_branch": "feature/ar-1513-authenticated-lease-dispatch-bridge",
  "observed_dirty": 0,
  "observed_head": "be018d4f1159bde9b9725f085cb8959edf7cde4e",
  "owner": "ar1513-lease-bridge-luna56",
  "plan": "../plans/AR-1513-authenticated-lease-dispatch-bridge.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Authenticate process-owner material, validate executable provenance, and connect leases to ordinary live dispatch.",
  "task_revision": 36,
  "title": "Authenticated lease-to-live-dispatch bridge",
  "updated_at": "2026-09-29T05:44:42+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1513-authenticated-lease-dispatch-bridge"
}
---

AR-1512 delivered a provider-free material contract and lifecycle store but its
independent review found three P1s: public constructors self-authenticate
arbitrary material, no non-test path consumes the lease into live dispatch, and
absolute launch paths are only lexical checks without executable/hash/symlink
provenance. This AR owns the bounded production bridge.

Acceptance requires:

- owner/enrollment-authenticated issuance that cannot be forged by public
  constructors or digest-only records; private roots and tools stay behind
  opaque runtime-owned capability handles;
- a non-test runtime/control/CLI adapter that consumes an authenticated lease
  and reaches `LiveProviderRuntimeHandle`/`LiveProviderRuntimeDispatchSource`
  for ordinary run/sweep, without caller/PATH/config authority injection;
- executable and adapter provenance is validated against pinned tool material:
  reject symlinks, nonexistent/non-executable paths, digest mismatch, absolute
  path drift, alternate target/egress, unknown fields and replay;
- expiry, restart, cancellation, remote revoke and teardown propagate through
  the real dispatch bridge, with deterministic provider-free negative tests;
- focused, serial workspace, clippy/docs/fmt, formal/privacy gates, independent
  exact-head review, SSH-signed DCO PR, protected merge, and post-merge proof.

Non-goals: asb-tui, live provider reachability, public credentials, private host
data, synthetic authority, or weakening fail-closed/native/formal gates.

- 2026-09-29T05:24:00+00:00: Created as the narrow successor to blocked
  AR-1512. Review evidence showed the material contract is not safe to publish
  until issuance authenticity, path provenance, and live dispatch consumption
  are implemented.
  AR-1512 remains historical blocked evidence rather than a prerequisite;
  this task starts from protected main and owns the missing production bridge.

- 2026-09-29T05:26:15+00:00: AR-1512 review blocker reconciled; promote authenticated issuance,
  provenance, and live dispatch bridge successor.

- 2026-09-29T05:26:18+00:00: Claimed by ar1513-lease-bridge-luna56.

- 2026-09-29T05:28:04+00:00: Heartbeat by ar1513-lease-bridge-luna56.

- 2026-09-29T05:28:13+00:00: Heartbeat/setup audit: authoritative task state is
  agent-systems-benchmark-state; protected product main f92c2e941913129d7db50480f71e8361a0d43a0c.
  Product main is dirty with unrelated changes, so it will not be reused. AR-1512 a4064ab is review
  evidence only; starting fresh isolated bridge worktree.

- 2026-09-29T05:28:41+00:00: Recorded command exit 0; command argv SHA-256
  933f1d0074a2ef06c2e574cd30093456f8b922e36d1a373e90edf3a4a6401309.

- 2026-09-29T05:32:46+00:00: Heartbeat by ar1513-lease-bridge-luna56.

- 2026-09-29T05:33:01+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T05:33:30+00:00: Recorded command exit 101; command argv SHA-256
  bedfb3381b748877015928201c1d5e3d1ec4c97afb1b6f35e212a3b347e58607.

- 2026-09-29T05:34:00+00:00: Call-graph audit complete: protected main already has authenticated
  control bootstrap -> RuntimeCertificateChainStore -> LiveProviderRuntimeAuthorityProfile ->
  crate-private RuntimeOwnedEnrollmentSource -> LiveProviderRuntimeHandle ->
  LiveProviderRuntimeDispatchSource -> CLI run/sweep. It has no ProcessOwnerMaterialLease consumer.
  Added initial process_owner_material module on isolated protected-main worktree with opaque
  issuer/store, nonce/replay/lifecycle fencing, symlink/executable/hash checks, and one-shot
  lease-to-dispatch bridge; focused compile currently reports unused integration seams pending
  runtime-owner wiring.

- 2026-09-29T05:35:20+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T05:35:38+00:00: Recorded command exit 101; command argv SHA-256
  bedfb3381b748877015928201c1d5e3d1ec4c97afb1b6f35e212a3b347e58607.

- 2026-09-29T05:36:44+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T05:37:08+00:00: Recorded command exit 0; command argv SHA-256
  bedfb3381b748877015928201c1d5e3d1ec4c97afb1b6f35e212a3b347e58607.

- 2026-09-29T05:37:24+00:00: Focused runtime gate now passes after wiring runtime-owner call path:
  cargo fmt and cargo test --locked -p asb-runtime --lib -- --test-threads=1: 156 passed, 1 ignored.
  Added RuntimeControlBootstrap::process_owner_material_caller/acquire_process_owner_material
  authenticated composition methods and CLI run_with_process_owner_material_bridge ordinary
  run/sweep adapter. Added deterministic unknown-field, expiry, replay, revoke, hash-drift,
  missing/non-executable/symlink provenance tests and docs. Worktree remains intentionally dirty
  with these six product files pending review.

- 2026-09-29T05:38:13+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T05:38:32+00:00: Recorded command exit 0; command argv SHA-256
  9b498ebdee73cab471971c5dafbe261dc25698666e300cea3661fb0b83d17145.

- 2026-09-29T05:38:48+00:00: Focused clippy gate passed through handoffctl: cargo clippy --locked -p
  asb-runtime -p asb-cli --all-targets -- -D warnings. Removed broad module dead-code allowance;
  retained only narrow integration-seam allows. Runtime focused tests remain 156 passed, 1 ignored.
  Product diff remains six files pending lifecycle/source review.

- 2026-09-29T05:40:09+00:00: Recorded command exit 101; command argv SHA-256
  7b80382008cb01e3ea6fa6e88054b624464f9801b40ed57f947b01892a686ae8.

- 2026-09-29T05:40:38+00:00: Recorded command exit 0; command argv SHA-256
  9ff4e40d0a608a041abbfd1d435a9e4d565a2c8931e342870e1969854466c867.

- 2026-09-29T05:41:00+00:00: Serial workspace cargo test reached all suites; one deterministic
  provenance fixture failed only because crates/asb-cli/src/lib.rs changed. Updated
  docs/examples/asb-cli-workflow-v1.provenance.json cli_source_sha256 to the exact new digest
  d6dd51e5... and focused provenance test now passes. No product behavior failure observed; rerun
  full workspace is required.

- 2026-09-29T05:41:48+00:00: Recorded command exit 0; command argv SHA-256
  7b80382008cb01e3ea6fa6e88054b624464f9801b40ed57f947b01892a686ae8.

- 2026-09-29T05:42:05+00:00: Serial workspace cargo test --locked --workspace -- --test-threads=1
  completed successfully after refreshing the CLI provenance digest. All unit/integration/doc tests
  passed; only pre-existing environment-qualified tests remained ignored. Product worktree is still
  intentionally dirty with seven AR-1513 files including provenance update.

- 2026-09-29T05:42:34+00:00: Recorded command exit 0; command argv SHA-256
  5c8da9b34935360f7399b9d4b260d9a460b442f2f0ca08eddaee6e8f11776ef0.

- 2026-09-29T05:42:57+00:00: Recorded command exit 0; command argv SHA-256
  28358b8048b4bb42bab1e7207a4a518f3d4ff0440c49f39ac36d99fbcd1c0854.

- 2026-09-29T05:43:26+00:00: Recorded command exit 0; command argv SHA-256
  f13aa6fdd5ef650f6bc6532a895ed405738b863ac21ccc8e0624b78bf34bd15b.

- 2026-09-29T05:43:43+00:00: Recorded command exit 0; command argv SHA-256
  687ea76743c0b4bd978ec56ef5912c044c72e11838614973fbdeba0f7d0fbaa3.

- 2026-09-29T05:44:05+00:00: Recorded command exit 0; command argv SHA-256
  8f49593a34777459c9034d780e25976a6c3c5dd6a24231dcd34d4e02350a702b.

- 2026-09-29T05:44:29+00:00: Committed exact isolated protected-main implementation at
  be018d4f1159bde9b9725f085cb8959edf7cde4e. Commit is SSH-signed by Martin Beck and carries matching
  DCO trailer. Seven tracked files changed: opaque authenticated issuer/store, strict executable
  provenance, lifecycle-fenced lease bridge, runtime-control caller, CLI run/sweep adapter, docs,
  and refreshed source provenance digest. Focused runtime 156 pass/1 ignored, serial workspace pass,
  clippy pass, rustdoc pass, formal manifest tests pass, and gitleaks reports no leaks.

- 2026-09-29T05:44:42+00:00: Recorded command exit 0; command argv SHA-256
  a21a8490d084b880fb0788c13b8c5b1e596ee37485b1c6f9f71fbeee6e61d68e.
