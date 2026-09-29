---
{
  "branch": "feature/ar-1511-runtime-control-authority-issuer",
  "checkpoint_commit": "673b486ba89917e3bb08c884ee17e708e0776b07",
  "claim_expires": "2026-09-29T06:31:02+00:00",
  "depends_on": [
    "AR-1502",
    "AR-1484"
  ],
  "id": "AR-1511",
  "next_action": "Implement authenticated runtime material provider from non-test owner state, bind launch program/adapter provenance, wire ordinary CLI/control caller, add remote-revoke test, then focused gates and independent exact-head review.",
  "observed_branch": "feature/ar-1511-runtime-control-authority-issuer",
  "observed_dirty": 4,
  "observed_head": "673b486ba89917e3bb08c884ee17e708e0776b07",
  "owner": "ar1511-production-path-luna56",
  "plan": "../plans/AR-1511-runtime-control-authority-issuer.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Implement the authenticated runtime/control authority issuer and opaque capability source required by production dispatch.",
  "task_revision": 158,
  "title": "Runtime/control authority issuer and capability source",
  "updated_at": "2026-09-29T04:45:31+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1511-runtime-control-authority-issuer"
}
---

AR-1510 audited the consumer boundary and proved that protected main has no
authenticated platform authority source: all provider material is test-only,
RuntimeCertificateChainStore accepts caller-provided chains, and CLI control
paths persist only public digests. This AR supplies the missing source rather
than allowing a consumer to invent authority.

Acceptance requires:

- a production ASB-only runtime/control authority issuer backed by the existing
  authenticated process-owner/enrollment contracts, with opaque capability
  handles rather than caller-supplied private roots, tools, policy or paths;
- a versioned request/response contract that authenticates the control session,
  namespace, endpoint, credential capability, generation, lease/relay roots,
  tool bundle, policy/allowlist, restart and cancellation fences, and expiry;
- independently verifiable receipt/chain issuance and replay, mismatch,
  expiry, revocation, cancellation, restart, alternate-egress and teardown
  rejection, without external provider reachability or runtime downloads;
- provider-free deterministic positive/negative tests, generated contract docs,
  and compatibility with existing RuntimeCertificateChainStore,
  RuntimeAuthorityRecord and owner lifecycle without caller/PATH injection;
- exact-head independent review, SSH-signed DCO, focused/full/formal/privacy
  gates, hosted checks, protected merge and terminal post-merge assurance.

Non-goals: asb-tui, live provider tests, public credentials, synthetic
production authority, or weakening fail-closed/native/formal gates.

- 2026-09-29T03:07:00+00:00: Created as prerequisite successor to AR-1510.
  AR-1510 passed the existing workspace tests but was blocked because no
  authenticated authority issuer/capability source exists on protected main.
  Implement this source first, then re-open the consumer wiring in a follow-on
  AR; preserve AR-1509/1510 unmerged façade work as evidence only.

- 2026-09-29T03:07:20+00:00: AR-1510 blocker evidence reconciled; promote the prerequisite authority
  issuer/capability source before consumer wiring.

- 2026-09-29T03:07:26+00:00: Claimed by ar1511-authority-issuer-luna56.

- 2026-09-29T03:09:33+00:00: Heartbeat by ar1511-authority-issuer-luna56.

- 2026-09-29T03:09:47+00:00: Recorded command exit 128; command argv SHA-256
  f191dd0fbda4e553585d5f35f001b74f00b2469b9897cf8e131123086d044dcb.

- 2026-09-29T03:10:16+00:00: Recorded command exit 0; command argv SHA-256
  bf7d0931c592ad3af8a21d778a3e4043e3ab3385d3765e4101138a38171673af.

- 2026-09-29T03:11:57+00:00: Heartbeat by ar1511-authority-issuer-luna56.

- 2026-09-29T03:12:00+00:00: Setup audit: initial worktree command targeted the state checkout and
  failed with invalid reference; explicit git -C product worktree creation then succeeded. Clean
  branch feature/ar-1511-runtime-control-authority-issuer is at protected main
  f92c2e941913129d7db50480f71e8361a0d43a0c with no product changes.

- 2026-09-29T03:12:20+00:00: Recorded command exit 0; command argv SHA-256
  295a35f99d4aa7024b5e0a35d1dd38654014d35e0d6da14a79231d3b8d7d50ba.

- 2026-09-29T03:15:43+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.

- 2026-09-29T03:17:29+00:00: Heartbeat by ar1511-authority-issuer-luna56.

- 2026-09-29T03:17:44+00:00: Baseline cargo check --locked -p asb-runtime -p asb-cli completed
  successfully at protected main (exit 0); earlier state recorded exit 2 for a setup attempt, but no
  product diagnostic was present. Product implementation now adds the runtime-owned issuer seam;
  focused compile follows.

- 2026-09-29T03:17:59+00:00: Recorded command exit 101; command argv SHA-256
  44858bcc1bea325f8e4ec42626fdf2970d2310a4694e160101531722dea4dfa4.

- 2026-09-29T03:18:34+00:00: Recorded command exit 101; command argv SHA-256
  44858bcc1bea325f8e4ec42626fdf2970d2310a4694e160101531722dea4dfa4.

- 2026-09-29T03:19:39+00:00: Recorded command exit 101; command argv SHA-256
  e64077fb1723d84a7b07ffaa36d431323f704514af5df3a4e9245be2bf6a944b.

- 2026-09-29T03:20:08+00:00: Recorded command exit 101; command argv SHA-256
  e64077fb1723d84a7b07ffaa36d431323f704514af5df3a4e9245be2bf6a944b.

- 2026-09-29T03:21:26+00:00: Heartbeat by ar1511-authority-issuer-luna56.

- 2026-09-29T03:21:30+00:00: Recorded command exit 0; command argv SHA-256
  e64077fb1723d84a7b07ffaa36d431323f704514af5df3a4e9245be2bf6a944b.

- 2026-09-29T03:22:06+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T03:22:28+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-29T03:22:46+00:00: Recorded command exit 0; command argv SHA-256
  e64077fb1723d84a7b07ffaa36d431323f704514af5df3a4e9245be2bf6a944b.

- 2026-09-29T03:23:08+00:00: Recorded command exit 0; command argv SHA-256
  e8beebac0638d83321c84d952814966bbba80dc16ee7dd3d3ead10f3c2b72292.

- 2026-09-29T03:23:36+00:00: Recorded command exit 0; command argv SHA-256
  bdd4e37a5c3088d2f9634b08f5cf43c035a62493e3c91cadb061fbb6ba1f322f.

- 2026-09-29T03:24:10+00:00: Heartbeat by ar1511-authority-issuer-luna56.

- 2026-09-29T03:24:25+00:00: Implemented and signed 1a26b02e2b6de485e930a0448d7fe5d34aed3061 from
  protected main f92c2e9. Issuer requires owner contract, authenticated chain/enrollment, and
  runtime input record; binds
  endpoint/session/namespace/credential/generation/lease/relay/tools/policy/allowlist/target/restart/expiry;
  one-shot nonce, receipt/chain verification, replay, drift, expiry, revoke and teardown denial.
  Focused cargo test authority_issuer: 3 passed; cargo fmt check and clippy -D warnings passed.
  Initial cargo check failure was missing thiserror; replaced with std Error and recheck passed.

- 2026-09-29T03:25:28+00:00: Recorded command exit 101; command argv SHA-256
  b93fa657e6c26f43b90a7c51fee6f7828522fb3291102061bfe5549391c9a5ac.

- 2026-09-29T03:26:28+00:00: Recorded command exit 101; command argv SHA-256
  11a8b438ac0215f19ec4d7953519c83375fcafd509024de8c305ca93e8d5ef3f.

- 2026-09-29T03:26:46+00:00: Recorded command exit 1; command argv SHA-256
  5d2fa3064369b66ae32c80132b1c61d7da582f5ec042c2a64f6ab9f002e2fd4d.

- 2026-09-29T03:27:07+00:00: Recorded command exit 0; command argv SHA-256
  af534639c3c39c31b189af38674a35ff1cd70138179487f1d660e9c22a29f510.

- 2026-09-29T03:27:35+00:00: Workspace cargo test --locked --workspace --no-fail-fast reached one
  target failure: asb-cli tests authenticated_lifecycle_rejects_provenance_and_retries_idempotently
  and authenticated_lifecycle_restart_fences_unfinished_intent panicked because control state root
  was already owned (parallel test lock collision). No authority_issuer failure. Serial cargo test
  -p asb-cli authenticated_lifecycle_ passed 8/8. This is an environmental/order-sensitive baseline
  failure, not changed code.

- 2026-09-29T03:28:21+00:00: Recorded command exit 0; command argv SHA-256
  75c78d32767dce560bf5f297627c4f938f132975bbcda14d85ca271d3cd6f91e.

- 2026-09-29T03:29:12+00:00: Heartbeat by ar1511-authority-issuer-luna56.

- 2026-09-29T03:29:15+00:00: Reran cargo test --locked --workspace --no-fail-fast --
  --test-threads=1 through handoffctl: terminal exit 0; all workspace tests and doc tests passed.
  The earlier parallel run's two asb-cli state-lock panics are order-sensitive baseline collisions,
  and the isolated filter passes 8/8. Product worktree remains clean at signed 1a26b02.

- 2026-09-29T03:30:29+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T03:30:46+00:00: Recorded command exit 101; command argv SHA-256
  44858bcc1bea325f8e4ec42626fdf2970d2310a4694e160101531722dea4dfa4.

- 2026-09-29T03:31:10+00:00: Recorded command exit 0; command argv SHA-256
  44858bcc1bea325f8e4ec42626fdf2970d2310a4694e160101531722dea4dfa4.

- 2026-09-29T03:31:33+00:00: Recorded command exit 1; command argv SHA-256
  8ff16c93cc6fc2d26ef373a21f0be844188f362e243551e1f19d544bd8153b91.

- 2026-09-29T03:31:58+00:00: Recorded command exit 101; command argv SHA-256
  bb9ea98e3d066ed4c1a6a94516fda9ab929928af92b46fcbc7af2a422e409c58.

- 2026-09-29T03:32:27+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-29T03:32:45+00:00: Recorded command exit 101; command argv SHA-256
  bb9ea98e3d066ed4c1a6a94516fda9ab929928af92b46fcbc7af2a422e409c58.

- 2026-09-29T03:33:32+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T03:33:49+00:00: Recorded command exit 101; command argv SHA-256
  bb9ea98e3d066ed4c1a6a94516fda9ab929928af92b46fcbc7af2a422e409c58.

- 2026-09-29T03:34:31+00:00: Recorded command exit 101; command argv SHA-256
  5286f5b03a50ded77ba040cd3bb90e976569e9dac453baee2d6983b92b4d0672.

- 2026-09-29T03:35:04+00:00: Recorded command exit 101; command argv SHA-256
  5286f5b03a50ded77ba040cd3bb90e976569e9dac453baee2d6983b92b4d0672.

- 2026-09-29T03:35:40+00:00: Recorded command exit 101; command argv SHA-256
  5286f5b03a50ded77ba040cd3bb90e976569e9dac453baee2d6983b92b4d0672.

- 2026-09-29T03:36:07+00:00: Coordinator stopped worker after independent review found P1 lifecycle
  and production-callsite gaps; preserve signed 1a26b02 plus dirty follow-on diff and transfer to
  repair worker.

- 2026-09-29T03:36:14+00:00: Claimed by ar1511-authority-repair-luna56.

- 2026-09-29T03:37:15+00:00: Heartbeat by ar1511-authority-repair-luna56.

- 2026-09-29T03:37:48+00:00: Recorded command exit 0; command argv SHA-256
  44858bcc1bea325f8e4ec42626fdf2970d2310a4694e160101531722dea4dfa4.

- 2026-09-29T03:38:23+00:00: Takeover audit: exact diff against protected f92c2e9 is 716 insertions
  across README.md, crates/asb-runtime/src/authority_issuer.rs, crates/asb-runtime/src/lib.rs,
  crates/asb-runtime/src/live_service.rs, and docs/RUNTIME_CONTROL_AUTHORITY_ISSUER.md. Signed
  1a26b02 has matching DCO; dirty follow-on modifies authority_issuer.rs (crate-visible binding
  digest plus cfg(test) mismatch eprintln) and live_service.rs (bootstrap issuer/capability fields,
  materialize_provisioner construction, fixture fields). git diff --check is clean. Through
  owner-scoped handoffctl run, cargo check --locked -p asb-runtime exited 0 on dirty follow-on;
  current product dirty=2 and head=1a26b02. Independent review P1 findings remain: teardown does not
  invalidate already-issued capability; verify has no current restart/cancellation fence and revoke
  lacks authenticated proof; no non-test production issuer construction/callsite was proven. Repair
  now; no publish claim.

- 2026-09-29T03:38:38+00:00: Recorded command exit 0; command argv SHA-256
  b5bea41b6c623f7c09f1bf24dcae58ebab3c0cdd90ad966bc43a45b44867e12b.

- 2026-09-29T03:41:31+00:00: Heartbeat by ar1511-authority-repair-luna56.

- 2026-09-29T03:41:53+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-29T03:42:14+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T03:42:36+00:00: Recorded command exit 101; command argv SHA-256
  dda4b96151ab821377bced6214cfb394a2280c5dac3c6ae010e9cb5144b4e7c1.

- 2026-09-29T03:43:03+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T03:43:21+00:00: Recorded command exit 0; command argv SHA-256
  dda4b96151ab821377bced6214cfb394a2280c5dac3c6ae010e9cb5144b4e7c1.

- 2026-09-29T03:44:22+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T03:44:39+00:00: Recorded command exit 0; command argv SHA-256
  dda4b96151ab821377bced6214cfb394a2280c5dac3c6ae010e9cb5144b4e7c1.

- 2026-09-29T03:45:02+00:00: Recorded command exit 101; command argv SHA-256
  82272d9cae8587476a54eac13c744af6e58977612e7e41e0c99da77704683187.

- 2026-09-29T03:45:51+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T03:46:08+00:00: Recorded command exit 0; command argv SHA-256
  d8c4bcc56a467f35f78e136a07d5519b01f64f075054bd0b9df191dfde0e43c7.

- 2026-09-29T03:46:33+00:00: Lifecycle repair progress: shared Arc atomic lifecycle now propagates
  issuer revoke/teardown to previously issued capabilities; capability verify requires current
  cancellation and restart fences; revoke requires validated
  binding/nonce/control-session/cancellation/restart proof and is idempotent. Added request
  constructor and deterministic negative tests for fence drift and forged revoke. Initial full
  asb-runtime gate failed only at
  live_service::tests::control_bootstrap_materializes_only_matching_private_bindings with actual
  EnrollmentMismatch because dirty fixture changed response generation to 7 but left chain identity
  generation/digest at 1; fixed fixture to rebuild chain generation/digest. Focused rerun passed 1/1
  plus binaries/integration targets. No opaque diagnostic retained; failure was recorded here.

- 2026-09-29T03:48:14+00:00: Recorded command exit 0; command argv SHA-256
  b7c1bd7abcc21a2d2b7851e3c19b5eece224e6abf67ab56b582453c98727e148.

- 2026-09-29T03:48:51+00:00: Recorded command exit 0; command argv SHA-256
  b7c1bd7abcc21a2d2b7851e3c19b5eece224e6abf67ab56b582453c98727e148.

- 2026-09-29T03:49:08+00:00: Heartbeat by ar1511-authority-repair-luna56.

- 2026-09-29T03:49:20+00:00: Owner-scoped serial workspace cargo test --locked --workspace
  --no-fail-fast -- --test-threads=1 exited 0 after fixture correction; asb-runtime 157 tests and
  all workspace targets passed with only pre-existing environment-gated ignores. Product remains
  intentionally dirty (authority_issuer.rs, live_service.rs,
  docs/RUNTIME_CONTROL_AUTHORITY_ISSUER.md) pending final diff review; no publish/PR claim.

- 2026-09-29T03:49:35+00:00: Recorded command exit 101; command argv SHA-256
  1024fc1e6cefa31b078f0b5d2ed85c7ea4586897b388bf1e308f62db58574461.

- 2026-09-29T03:50:04+00:00: Recorded command exit 0; command argv SHA-256
  1024fc1e6cefa31b078f0b5d2ed85c7ea4586897b388bf1e308f62db58574461.

- 2026-09-29T03:50:30+00:00: Recorded command exit 0; command argv SHA-256
  b36d15881eb65027724bc584f1b04db05666cd79896b100806e528307c04b65c.

- 2026-09-29T03:50:55+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-29T03:51:40+00:00: Final focused gates: cargo clippy --locked --workspace --all-targets --
  -D warnings, RUSTDOCFLAGS=-Dwarnings cargo doc --locked --workspace --no-deps, and cargo fmt --all
  -- --check exited 0. Clippy's one initial failure was actual unnecessary  on the
  cancellation-fence  at live_service.rs:1616; removed and reran green. Serial workspace cargo test
  had exited 0 before docs/final cleanup and all asb-runtime tests passed after fixture repair.
  Product remains dirty=3; exact diff still includes preserved signed 1a26b02 plus
  lifecycle/integration/docs follow-on; no publication claim.

- 2026-09-29T03:52:00+00:00: Correction to prior note: Clippy initial failure was the unnecessary
  to_owned call on the cancellation-fence string reference at live_service.rs:1616; it was removed
  and the gate reran green. The prior note shell rendering dropped those literal identifiers; no
  product file was affected.

- 2026-09-29T03:52:43+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T03:53:01+00:00: Recorded command exit 0; command argv SHA-256
  dda4b96151ab821377bced6214cfb394a2280c5dac3c6ae010e9cb5144b4e7c1.

- 2026-09-29T03:53:18+00:00: Recorded command exit 0; command argv SHA-256
  e8beebac0638d83321c84d952814966bbba80dc16ee7dd3d3ead10f3c2b72292.

- 2026-09-29T03:54:11+00:00: Recorded command exit 0; command argv SHA-256
  e53f91cc52b0dfd91cf12c0200617d141c415f7e708a59d10e2805f658162bc1.

- 2026-09-29T03:54:32+00:00: Recorded command exit 0; command argv SHA-256
  c8006e15a2bd34f0eba5b2e84c5f0339a707c77da1253cd0642faa8f665da1ef.

- 2026-09-29T03:55:04+00:00: Final repair commit 49bf84275f0df05b7ce310f36f87e29c420b8e34 is
  SSH-signed and DCO-signed by Martin Beck; product worktree is clean at exact head. It preserves
  prior signed 1a26b02 and includes lifecycle Arc invalidation, current cancellation/restart
  verification fences, authenticated revoke proof, request constructor, live_service production
  materialization/revoke integration, deterministic negative tests, fixture correction, and docs.
  git diff --check against protected f92c2e9 is clean. No PR/publication claim; request independent
  exact-head review now.

- 2026-09-29T03:55:27+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T03:55:45+00:00: Recorded command exit 0; command argv SHA-256
  dda4b96151ab821377bced6214cfb394a2280c5dac3c6ae010e9cb5144b4e7c1.

- 2026-09-29T03:56:02+00:00: Recorded command exit 0; command argv SHA-256
  be2cc5b045c5a28c5c4ac9dc568e0e7d09aeeda7b2f71dc25d7b6a5014511c61.

- 2026-09-29T03:56:18+00:00: Recorded command exit 0; command argv SHA-256
  d5e674270c966dddbdc7834c8c6d1e08b586207bbe23bdfeadfc59af38de2b81.

- 2026-09-29T03:57:20+00:00: Recorded command exit 0; command argv SHA-256
  b7c1bd7abcc21a2d2b7851e3c19b5eece224e6abf67ab56b582453c98727e148.

- 2026-09-29T03:57:37+00:00: Clean final product head is ac9306453dc97a100a57befcba0c8456b67a23db, a
  new SSH-signed DCO commit adding the alternate-target/egress-drift negative test to signed repair
  49bf842. Product worktree is clean; serial workspace tests reran exit 0 after this commit, and
  focused test/format/clippy gates were green. Independent exact-head review is assigned; no PR or
  push.

- 2026-09-29T03:58:13+00:00: Heartbeat by ar1511-authority-repair-luna56.

- 2026-09-29T03:58:36+00:00: Heartbeat by ar1511-authority-repair-luna56.

- 2026-09-29T03:58:53+00:00: Heartbeat by ar1511-authority-repair-luna56.

- 2026-09-29T04:02:26+00:00: Independent exact-head review found two P1s: materialize_provisioner
  remains test-only and local cancellation digest differs from control-issued fence; preserve
  ac93064 and assign final repair.

- 2026-09-29T04:02:32+00:00: Claimed by ar1511-final-repair-luna56.

- 2026-09-29T04:03:52+00:00: Heartbeat by ar1511-final-repair-luna56.

- 2026-09-29T04:03:55+00:00: Takeover audit: exact clean product head
  ac9306453dc97a100a57befcba0c8456b67a23db is the assigned review head against protected
  f92c2e941913129d7db50480f71e8361a0d43a0c; prior review text is stale. Beginning root-cause repair.

- 2026-09-29T04:06:34+00:00: Recorded command exit 0; command argv SHA-256
  a84e28cf7020f33e99679edcfbab2ff1cf9c9e19b9363c3a1d24979c7d0aa50a.

- 2026-09-29T04:06:50+00:00: Recorded command exit 0; command argv SHA-256
  634a2f21d60bc2bc2211ab4e61ef3202bac7bbb8fc75e89446513674857938d6.

- 2026-09-29T04:07:06+00:00: Heartbeat by ar1511-final-repair-luna56.

- 2026-09-29T04:07:12+00:00: Recorded command exit 101; command argv SHA-256
  44858bcc1bea325f8e4ec42626fdf2970d2310a4694e160101531722dea4dfa4.

- 2026-09-29T04:07:34+00:00: Recorded command exit 0; command argv SHA-256
  328540c65ee4ab61a5f1c709bc48dc8d302f6143fb64ee9ea2d00b61abed0891.

- 2026-09-29T04:10:23+00:00: Recorded command exit 101; command argv SHA-256
  328540c65ee4ab61a5f1c709bc48dc8d302f6143fb64ee9ea2d00b61abed0891.

- 2026-09-29T04:11:01+00:00: Recorded command exit 1; command argv SHA-256
  3e5bd71d471058ad725ab93cf05cabd9c401e3e956de16c0c165c448e8229910.

- 2026-09-29T04:11:24+00:00: Recorded command exit 0; command argv SHA-256
  91b8ae18b3b1d1082393462665f7c7f7a2b2bd1d8c52b8f9e1f9af846cc7a0ad.

- 2026-09-29T04:11:44+00:00: Recorded command exit 0; command argv SHA-256
  bd8d79ae0e29c8000606252ea1a3d39f3b41df092f9e958a7d3cd98a2db3abdc.

- 2026-09-29T04:12:29+00:00: Recorded command exit 0; command argv SHA-256
  2d1a583474cad444c4fba28482e41df86cd7e09dfe19fdd6861a30ce84556321.

- 2026-09-29T04:13:44+00:00: Recorded command exit 0; command argv SHA-256
  012cc8c227bb1d488359d45669e2ff31ae1d58d01d26a02e9f6d3c9e2fa0987c.

- 2026-09-29T04:14:12+00:00: Recorded command exit 0; command argv SHA-256
  deeb2abc61654505a30d1a01803bdf6c870b3df17579c22ec78ecfff56a2a4e1.

- 2026-09-29T04:14:37+00:00: Recorded command exit 0; command argv SHA-256
  579fae36f99e7e8dbd58940a03751c7cc756cd6bd4fa758bbc1cd763bb4b76de.

- 2026-09-29T04:14:58+00:00: Recorded command exit 0; command argv SHA-256
  def1b3c193bc9f2ab772e0797554ca925e8459c01f2d0a460cb65253ebc38691.

- 2026-09-29T04:15:17+00:00: Recorded command exit 0; command argv SHA-256
  0e0ff2f9c8e35ea6d485b95a26b5acc9f72cdb30424b01acad34640a3a49145b.

- 2026-09-29T04:16:22+00:00: Recorded command exit 0; command argv SHA-256
  cb5412d5e3eb3f885117522b91189dd6fe8d00f52522661df97a7cfe7366fa10.

- 2026-09-29T04:17:20+00:00: Recorded command exit 0; command argv SHA-256
  012cc8c227bb1d488359d45669e2ff31ae1d58d01d26a02e9f6d3c9e2fa0987c.

- 2026-09-29T04:17:38+00:00: Recorded command exit 101; command argv SHA-256
  2d1a583474cad444c4fba28482e41df86cd7e09dfe19fdd6861a30ce84556321.

- 2026-09-29T04:18:39+00:00: Recorded command exit 0; command argv SHA-256
  012cc8c227bb1d488359d45669e2ff31ae1d58d01d26a02e9f6d3c9e2fa0987c.

- 2026-09-29T04:18:56+00:00: Recorded command exit 0; command argv SHA-256
  2d1a583474cad444c4fba28482e41df86cd7e09dfe19fdd6861a30ce84556321.

- 2026-09-29T04:19:16+00:00: Recorded command exit 0; command argv SHA-256
  579fae36f99e7e8dbd58940a03751c7cc756cd6bd4fa758bbc1cd763bb4b76de.

- 2026-09-29T04:19:35+00:00: Recorded command exit 0; command argv SHA-256
  0e0ff2f9c8e35ea6d485b95a26b5acc9f72cdb30424b01acad34640a3a49145b.

- 2026-09-29T04:19:54+00:00: Recorded command exit 0; command argv SHA-256
  def1b3c193bc9f2ab772e0797554ca925e8459c01f2d0a460cb65253ebc38691.

- 2026-09-29T04:20:54+00:00: Recorded command exit 0; command argv SHA-256
  cb5412d5e3eb3f885117522b91189dd6fe8d00f52522661df97a7cfe7366fa10.

- 2026-09-29T04:21:33+00:00: Recorded command exit 0; command argv SHA-256
  a72d7fb71c5eeadb4de197129987010d2bc519c32dec8e91417868c56a71c7bd.

- 2026-09-29T04:21:49+00:00: Recorded command exit 0; command argv SHA-256
  a84e28cf7020f33e99679edcfbab2ff1cf9c9e19b9363c3a1d24979c7d0aa50a.

- 2026-09-29T04:22:05+00:00: Recorded command exit 0; command argv SHA-256
  a090879e0f5c839acfe98fe4959dcdbd7a8cb44bf8e3c48dd0bd9caaa7869c84.

- 2026-09-29T04:22:28+00:00: Recorded command exit 0; command argv SHA-256
  98abbc652e5cf29c18e2d5e260271de9b9a1785abaed7192a14ce9c23e3a045f.

- 2026-09-29T04:23:50+00:00: Recorded command exit 0; command argv SHA-256
  7ad690de3f116ed9f84d909b4bf1c8c9e20d508feaa5347e562382b9fc50bbe5.

- 2026-09-29T04:24:23+00:00: Heartbeat by ar1511-final-repair-luna56.

- 2026-09-29T04:24:38+00:00: Repaired both P1 roots: production LiveProviderRuntimeDispatchSource
  now composes RuntimeControlBootstrap through an opaque provider-owned authority source with no
  caller/PATH injection, and issuer capabilities consume the authenticated control-issued
  cancellation fence. Added tamper and remote-revoke negative coverage; revoke invalidates issuer
  before local persistence failure. SSH-signed DCO commit 673b486ba89917e3bb08c884ee17e708e0776b07.
  Focused tests, serial asb-runtime (157 passed, 1 ignored), serial workspace, clippy -D warnings,
  docs -Dwarnings, fmt check, and diff check green. Request independent exact-head review; no
  PR/push.

- 2026-09-29T04:29:23+00:00: Independent exact-head review of 673b486 found P1: dispatch/provider
  remains test-only with no ordinary CLI production caller or non-test material producer; preserve
  clean signed head and assign final production-path repair.

- 2026-09-29T04:29:31+00:00: Claimed by ar1511-production-path-luna56.

- 2026-09-29T04:31:02+00:00: Heartbeat by ar1511-production-path-luna56.

- 2026-09-29T04:31:09+00:00: Takeover heartbeat/audit: preserving clean signed 673b486 against
  protected f92c2e9; production-path repair begins for independent-review P1.

- 2026-09-29T04:34:07+00:00: Recorded command exit 0; command argv SHA-256
  43dd51120a88a861e8e4c00a18907a326695198b26d82d0391c92ddf401fb572.

- 2026-09-29T04:34:52+00:00: Call-graph audit recorded:
  LiveProviderRuntimeDispatchSource::from_control_bootstrap and run_with_runtime_control_source have
  only cfg(test) callers; RuntimeControlDispatchSource has only test implementation;
  RuntimePlatformAuthorityMaterial::for_test is the sole material constructor. Existing control
  backend owns authenticated bootstrap records, so repair will add a provider-owned source backed by
  runtime/control state and an ordinary CLI/control composition path.

- 2026-09-29T04:38:09+00:00: Recorded command exit 101; command argv SHA-256
  295a35f99d4aa7024b5e0a35d1dd38654014d35e0d6da14a79231d3b8d7d50ba.

- 2026-09-29T04:38:36+00:00: Recorded command exit 0; command argv SHA-256
  295a35f99d4aa7024b5e0a35d1dd38654014d35e0d6da14a79231d3b8d7d50ba.

- 2026-09-29T04:38:58+00:00: Recorded command exit 101; command argv SHA-256
  035a4c0a715e62a1272251cb55b9789c4036bbd5627f0e64d65dbb6b4ed3eed7.

- 2026-09-29T04:39:26+00:00: Recorded command exit 101; command argv SHA-256
  035a4c0a715e62a1272251cb55b9789c4036bbd5627f0e64d65dbb6b4ed3eed7.

- 2026-09-29T04:39:59+00:00: Recorded command exit 0; command argv SHA-256
  035a4c0a715e62a1272251cb55b9789c4036bbd5627f0e64d65dbb6b4ed3eed7.

- 2026-09-29T04:40:53+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T04:41:18+00:00: Recorded command exit 101; command argv SHA-256
  9b498ebdee73cab471971c5dafbe261dc25698666e300cea3661fb0b83d17145.

- 2026-09-29T04:42:13+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T04:42:29+00:00: Recorded command exit 1; command argv SHA-256
  ba3d5c39e7346ec1f5e35027b342f1348d7e81707b97a81f1b308359401f1ab0.

- 2026-09-29T04:42:47+00:00: Recorded command exit 101; command argv SHA-256
  228d89fb3f1fe67be45e6174b3f64f4177a5181103148b1ee0173b33fb774570.

- 2026-09-29T04:43:37+00:00: Recorded command exit 101; command argv SHA-256
  228d89fb3f1fe67be45e6174b3f64f4177a5181103148b1ee0173b33fb774570.

- 2026-09-29T04:44:03+00:00: Recorded command exit 101; command argv SHA-256
  f703e043696157a1995049f67d4d96b11b2968e534fd7ca88b3ea9fc61a7f5f7.

- 2026-09-29T04:44:28+00:00: Recorded command exit 101; command argv SHA-256
  f703e043696157a1995049f67d4d96b11b2968e534fd7ca88b3ea9fc61a7f5f7.

- 2026-09-29T04:45:04+00:00: Recorded command exit 101; command argv SHA-256
  f703e043696157a1995049f67d4d96b11b2968e534fd7ca88b3ea9fc61a7f5f7.

- 2026-09-29T04:45:31+00:00: Recorded command exit 101; command argv SHA-256
  f703e043696157a1995049f67d4d96b11b2968e534fd7ca88b3ea9fc61a7f5f7.
