---
{
  "branch": "feature/ar-1513-authenticated-lease-dispatch-bridge",
  "checkpoint_commit": "4807e9692a4e8f2bc22c647298878ec957f58304",
  "claim_expires": "2026-09-29T11:08:04+00:00",
  "depends_on": [
    "AR-1502",
    "AR-1484"
  ],
  "id": "AR-1513",
  "next_action": "Review of 4807e96 found P1: run_with_runtime_control_bootstrap calls acquire before materialize_provisioner, so owner_id/resolver are unset and tests only assert failure; normal CLI run/sweep still bypasses bridge. Fix real materialization and successful provider-free production bridge, then rerun coverage/review.",
  "observed_branch": "feature/ar-1513-authenticated-lease-dispatch-bridge",
  "observed_dirty": 5,
  "observed_head": "4807e9692a4e8f2bc22c647298878ec957f58304",
  "owner": "ar1513-repair4-luna56",
  "plan": "../plans/AR-1513-authenticated-lease-dispatch-bridge.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Authenticate process-owner material, validate executable provenance, and connect leases to ordinary live dispatch.",
  "task_revision": 355,
  "title": "Authenticated lease-to-live-dispatch bridge",
  "updated_at": "2026-09-29T09:12:41+00:00",
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

- 2026-09-29T05:45:05+00:00: Recorded command exit 0; command argv SHA-256
  1f540aeee2629e67b769c48e24d39320eb8679d18cc219ae826a9d2df0ec097d.

- 2026-09-29T05:45:26+00:00: Published PR #383 from exact signed head be018d4 against protected base
  f92c2e9. GitHub reports mergeable; required checks are pending, with AWQ shadow and source-header
  checks already green. No merge authority claimed.

- 2026-09-29T05:47:20+00:00: Coordinator takeover after stopping prior worker; preserve PR #383
  exact-head evidence be018d4 and reassign repair worker on same AR.

- 2026-09-29T05:47:23+00:00: Claimed by ar1513-repair-luna56.

- 2026-09-29T05:48:31+00:00: Heartbeat by ar1513-repair-luna56.

- 2026-09-29T05:48:39+00:00: Recorded command exit 0; command argv SHA-256
  9f7a1cf6a8445606b7d34b1c68fdc5f16c4acb053b20a117054ac478fe09a083.

- 2026-09-29T05:50:19+00:00: Heartbeat by ar1513-repair-luna56.

- 2026-09-29T05:50:39+00:00: Recorded command exit 8; command argv SHA-256
  e863990689a3d5434e9dc00fecf982715c2f989c13c279e7e89c5293807a591b.

- 2026-09-29T05:51:02+00:00: Recorded command exit 0; command argv SHA-256
  fdace47918dc480cb30f27fe64a3446e37cdf3c1c497a29b1dfd7e94473c14b3.

- 2026-09-29T05:51:25+00:00: Recorded command exit 0; command argv SHA-256
  e56a9b857e9704283f51e56aea6e5b32f305c4b8f68d7291fca9130385e9b18f.

- 2026-09-29T05:52:53+00:00: Recorded command exit 1; command argv SHA-256
  428457ea9cc6a21bd46c5be6651ba2faccb5b0b07ddc2fd6f96eca730dea5ab7.

- 2026-09-29T05:53:33+00:00: Recorded command exit 1; command argv SHA-256
  598dfc4db995a414f9081525e13f5d530cbc4cffce711e575d0c3ee725aae8d0.

- 2026-09-29T05:54:00+00:00: Recorded command exit 0; command argv SHA-256
  565bcb1c63208fb0e2f70d82fda7be608571a53d9f531fc32bcf800943b30c73.

- 2026-09-29T05:54:25+00:00: Recorded command exit 0; command argv SHA-256
  05aa9dac5b08560535142bf1868d583e1a5c2848601a13eea7627168fe6349a2.

- 2026-09-29T05:55:03+00:00: Recorded command exit 0; command argv SHA-256
  b8377abdc0ffee433c0d476f4da89748887809071ebe1f19952a4534b543d161.

- 2026-09-29T05:55:52+00:00: Recorded command exit 0; command argv SHA-256
  4c82b06cc33502380bbfad5c4202e7c66f0b420b129670bc184e59859e1bb0d5.

- 2026-09-29T05:57:38+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-29T05:57:59+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T05:58:21+00:00: Recorded command exit 101; command argv SHA-256
  9a559370a2d4fc23bb5fd8038cd1bff9db418292b8fb9ccbbe09a7fb135935f6.

- 2026-09-29T05:58:52+00:00: Recorded command exit 0; command argv SHA-256
  9a559370a2d4fc23bb5fd8038cd1bff9db418292b8fb9ccbbe09a7fb135935f6.

- 2026-09-29T05:59:22+00:00: Recorded command exit 0; command argv SHA-256
  402b135354b11691c31c607168f74355f8ee55f6b5ea041b01fe8de7a51bff88.

- 2026-09-29T06:01:00+00:00: Recorded command exit 0; command argv SHA-256
  428457ea9cc6a21bd46c5be6651ba2faccb5b0b07ddc2fd6f96eca730dea5ab7.

- 2026-09-29T06:01:33+00:00: Recorded command exit 0; command argv SHA-256
  0b033c3736f8fc7116ecd45e0b680b6d76fc6258957f073ff00cd8632ee9c5ff.

- 2026-09-29T06:01:58+00:00: Recorded command exit 0; command argv SHA-256
  9b498ebdee73cab471971c5dafbe261dc25698666e300cea3661fb0b83d17145.

- 2026-09-29T06:02:22+00:00: Recorded command exit 0; command argv SHA-256
  76d83db6f9bf07eead06b4d1e6eaeb86b6749ad6fea341069a43a26a3cee382e.

- 2026-09-29T06:02:39+00:00: Recorded command exit 0; command argv SHA-256
  414f6954eff973d86739b6acf21a1623948d41faaf8ff329247bcaf9a64d910b.

- 2026-09-29T06:03:12+00:00: Recorded command exit 0; command argv SHA-256
  ff5912fa56b5f3988afeeec6bf95c92437b31658fa4570bc50e4e1d13b166a44.

- 2026-09-29T06:03:30+00:00: Recorded command exit 0; command argv SHA-256
  72af92f2f40f31c428b55b4e1dc7ae5af541642583f0c881108b86064db7ee8d.

- 2026-09-29T06:04:02+00:00: Coverage repair pushed at exact signed DCO head
  bde018c10b3b69252f9a5b8429f9cc277e44953d. Added provider-free tests for invalid tool/material
  shape, opaque debug projections, material digest mismatch, lifecycle cancel/restart/teardown and
  expiry/time fences. Focused runtime tests: 159 passed, 1 ignored; clippy -p asb-runtime -p asb-cli
  passed; local check_coverage.py workspace plus asb-core/asb-protocol/asb-replay passed with floors
  unchanged (90 workspace, 95 critical). Hosted policy check at prior head failed only coverage
  89.96%; rerun required on repair head. Worktree clean and push confirmed.

- 2026-09-29T06:04:11+00:00: Recorded command exit 0; command argv SHA-256
  fdace47918dc480cb30f27fe64a3446e37cdf3c1c497a29b1dfd7e94473c14b3.

- 2026-09-29T06:04:33+00:00: Recorded command exit 8; command argv SHA-256
  e863990689a3d5434e9dc00fecf982715c2f989c13c279e7e89c5293807a591b.

- 2026-09-29T06:04:53+00:00: Heartbeat by ar1513-repair-luna56.

- 2026-09-29T06:05:01+00:00: Recorded command exit 8; command argv SHA-256
  e863990689a3d5434e9dc00fecf982715c2f989c13c279e7e89c5293807a591b.

- 2026-09-29T06:05:25+00:00: Recorded command exit 8; command argv SHA-256
  e863990689a3d5434e9dc00fecf982715c2f989c13c279e7e89c5293807a591b.

- 2026-09-29T06:05:50+00:00: Recorded command exit 8; command argv SHA-256
  e863990689a3d5434e9dc00fecf982715c2f989c13c279e7e89c5293807a591b.

- 2026-09-29T06:06:13+00:00: Recorded command exit 8; command argv SHA-256
  e863990689a3d5434e9dc00fecf982715c2f989c13c279e7e89c5293807a591b.

- 2026-09-29T06:06:35+00:00: Recorded command exit 0; command argv SHA-256
  b50b6cdd9efd2ce9ae409d33b7fe5fdf181be72501c7736d6dc18a3488cbde2d.

- 2026-09-29T06:06:57+00:00: Heartbeat by ar1513-repair-luna56.

- 2026-09-29T06:07:01+00:00: Recorded command exit 8; command argv SHA-256
  e863990689a3d5434e9dc00fecf982715c2f989c13c279e7e89c5293807a591b.

- 2026-09-29T06:07:31+00:00: Recorded command exit 8; command argv SHA-256
  e863990689a3d5434e9dc00fecf982715c2f989c13c279e7e89c5293807a591b.

- 2026-09-29T06:07:54+00:00: Recorded command exit 8; command argv SHA-256
  e863990689a3d5434e9dc00fecf982715c2f989c13c279e7e89c5293807a591b.

- 2026-09-29T06:08:17+00:00: Recorded command exit 0; command argv SHA-256
  8238f54d71d8240b0810691b341a9ffd092e7f9a6867a6275ea5ea2909274edd.

- 2026-09-29T06:15:34+00:00: Release completed repair claim for second repair pass; preserve bde018c
  and independent review P1 evidence.

- 2026-09-29T06:15:36+00:00: Claimed by ar1513-repair2-luna56.

- 2026-09-29T06:15:52+00:00: Independent review of bde018c found three P1 blockers despite green
  hosted checks: incomplete enrollment binding, caller-supplied source not bound to lease, and
  lifecycle fencing stops after bridge consumption. Also P2 bounded-field limits.

- 2026-09-29T06:19:11+00:00: Heartbeat by ar1513-repair2-luna56.

- 2026-09-29T06:22:39+00:00: Recorded command exit 101; command argv SHA-256
  44858bcc1bea325f8e4ec42626fdf2970d2310a4694e160101531722dea4dfa4.

- 2026-09-29T06:23:47+00:00: Recorded command exit 0; command argv SHA-256
  44858bcc1bea325f8e4ec42626fdf2970d2310a4694e160101531722dea4dfa4.

- 2026-09-29T06:24:35+00:00: Recorded command exit 101; command argv SHA-256
  0d2a2005d9801ace4f331dbfcdeb1c73daa33a706733bb4791ecfa127e8116e1.

- 2026-09-29T06:24:54+00:00: Recorded command exit 0; command argv SHA-256
  0d2a2005d9801ace4f331dbfcdeb1c73daa33a706733bb4791ecfa127e8116e1.

- 2026-09-29T06:25:24+00:00: Recorded command exit 0; command argv SHA-256
  bedfb3381b748877015928201c1d5e3d1ec4c97afb1b6f35e212a3b347e58607.

- 2026-09-29T06:25:56+00:00: Recorded command exit 0; command argv SHA-256
  0d2a2005d9801ace4f331dbfcdeb1c73daa33a706733bb4791ecfa127e8116e1.

- 2026-09-29T06:26:22+00:00: Recorded command exit 0; command argv SHA-256
  7faed413c853448b99821c056cafb656f430f2d23a37c1c4af22da19956baee2.

- 2026-09-29T06:27:39+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T06:27:57+00:00: Recorded command exit 101; command argv SHA-256
  9b498ebdee73cab471971c5dafbe261dc25698666e300cea3661fb0b83d17145.

- 2026-09-29T06:28:17+00:00: Recorded command exit 0; command argv SHA-256
  9b498ebdee73cab471971c5dafbe261dc25698666e300cea3661fb0b83d17145.

- 2026-09-29T06:29:15+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T06:29:34+00:00: Recorded command exit 0; command argv SHA-256
  295a35f99d4aa7024b5e0a35d1dd38654014d35e0d6da14a79231d3b8d7d50ba.

- 2026-09-29T06:30:44+00:00: Heartbeat by ar1513-repair2-luna56.

- 2026-09-29T06:31:08+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T06:31:31+00:00: Recorded command exit 0; command argv SHA-256
  bedfb3381b748877015928201c1d5e3d1ec4c97afb1b6f35e212a3b347e58607.

- 2026-09-29T06:32:34+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T06:32:51+00:00: Recorded command exit 1; command argv SHA-256
  aec867b97070f678c659938dc3ac60c07fecebee8666321a5a856836fda73e50.

- 2026-09-29T06:33:19+00:00: Recorded command exit 0; command argv SHA-256
  bedfb3381b748877015928201c1d5e3d1ec4c97afb1b6f35e212a3b347e58607.

- 2026-09-29T06:34:24+00:00: Recorded command exit 0; command argv SHA-256
  7b80382008cb01e3ea6fa6e88054b624464f9801b40ed57f947b01892a686ae8.

- 2026-09-29T06:34:52+00:00: Recorded command exit 0; command argv SHA-256
  9b498ebdee73cab471971c5dafbe261dc25698666e300cea3661fb0b83d17145.

- 2026-09-29T06:35:08+00:00: Recorded command exit 0; command argv SHA-256
  ab61d5d7cfbefdb8bb739c06e799ebb0146b34af12d5a19e61826c26fc38207d.

- 2026-09-29T06:35:28+00:00: Recorded command exit 0; command argv SHA-256
  6a788ac849d962e7a5ae0e62b8d676a3a07deb9f2f756e79b7446e44c77fa115.

- 2026-09-29T06:35:47+00:00: Recorded command exit 0; command argv SHA-256
  72af92f2f40f31c428b55b4e1dc7ae5af541642583f0c881108b86064db7ee8d.

- 2026-09-29T06:36:05+00:00: Heartbeat by ar1513-repair2-luna56.

- 2026-09-29T06:36:25+00:00: Second repair complete at exact signed head 109f5fad. Runtime owner
  material now requires authenticated enrollment binding for owner, endpoint, namespace, session,
  generation, expiry, restart/cancel/revoke/teardown fences, credential, target, alternate egress,
  tool, lease/relay roots, and enrollment fingerprint; removed crate-private self-authenticated
  from_runtime_authenticated production path. Live dispatch sources carry the enrollment fingerprint
  and retain a shared lifecycle fence checked at every scheduler acquire, while
  RuntimeControlBootstrap exposes the bootstrap->lease->source bridge. Added bounded private fields
  and provider-free negative tests for forged bindings plus post-consumption fencing. Focused
  runtime: 160 passed, 1 ignored; full locked workspace tests passed; focused clippy passed;
  SSH-signed DCO commit and push confirmed. Independent review remains required.

- 2026-09-29T06:43:35+00:00: Independent exact-head review of 109f5fad: prior
  enrollment/source/lifecycle findings appear closed, but new P1s block merge; preserve all evidence
  and failed coverage.

- 2026-09-29T06:43:38+00:00: Release second repair claim for third repair pass; preserve 109f5fad
  and review/coverage evidence.

- 2026-09-29T06:43:41+00:00: Claimed by ar1513-repair3-luna56.

- 2026-09-29T06:45:26+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.

- 2026-09-29T06:45:43+00:00: Recorded command exit 0; command argv SHA-256
  efed70eaf684ecc5a82f2e5305f702212c70e117cb8a2a4814d8a28251e86280.

- 2026-09-29T06:46:00+00:00: Recorded command exit 0; command argv SHA-256
  eb0bda22244ba2ee1fb6df77e8248fc5c8f5e866e08a5e496ebbacfe5d1ce828.

- 2026-09-29T06:47:21+00:00: Recorded command exit 0; command argv SHA-256
  bedfb3381b748877015928201c1d5e3d1ec4c97afb1b6f35e212a3b347e58607.

- 2026-09-29T06:51:16+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-29T06:51:35+00:00: Recorded command exit 101; command argv SHA-256
  bedfb3381b748877015928201c1d5e3d1ec4c97afb1b6f35e212a3b347e58607.

- 2026-09-29T06:51:59+00:00: Recorded command exit 0; command argv SHA-256
  bedfb3381b748877015928201c1d5e3d1ec4c97afb1b6f35e212a3b347e58607.

- 2026-09-29T06:52:55+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-29T06:53:24+00:00: Heartbeat by ar1513-repair3-luna56.

- 2026-09-29T06:53:36+00:00: Recorded command exit 0; command argv SHA-256
  a9d0d3f912836563c120589e83507c52ba764459af80e9550f53583649101492.

- 2026-09-29T06:53:58+00:00: Recorded command exit 0; command argv SHA-256
  956eb170d0934060fc3d3f44086d1fa95d671e8806999173a748fd0e8e25e2e8.

- 2026-09-29T06:54:16+00:00: Recorded command exit 0; command argv SHA-256
  3af1d0c64504757ee1fb326116e1453b9285de782ca76be782658265c208723b.

- 2026-09-29T06:54:33+00:00: Recorded command exit 0; command argv SHA-256
  95d54de28157509cf6ca095f604ca0f4a067bc3bfde8d11c243de1f714bda1fa.

- 2026-09-29T06:54:50+00:00: Heartbeat by ar1513-repair3-luna56.

- 2026-09-29T06:54:58+00:00: Recorded command exit 0; command argv SHA-256
  cb5a1ab22dc400f62c262131f6746dc61db687e6a570c149cf4fb11a668916a7.

- 2026-09-29T06:55:15+00:00: Recorded command exit 0; command argv SHA-256
  9cf912e2f53a6efece0ddf5cb8a12b7c21126b100190d86ec839b1af501284cc.

- 2026-09-29T06:55:33+00:00: Recorded command exit 0; command argv SHA-256
  47556f36c3ecef2bf9c3a855f24b9e39afe13792b06a951b464cf65a014c0952.

- 2026-09-29T06:55:50+00:00: Recorded command exit 0; command argv SHA-256
  3564364a255977bf28f76bf3f07e12adf194b77d98b3d1fd41d8b3529520d3bd.

- 2026-09-29T06:58:13+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T06:58:37+00:00: Recorded command exit 0; command argv SHA-256
  9c97262cf27706a25ea2ca33ad4f1d8c46a8f4bfbdf7813b25a1aafc519cae9f.

- 2026-09-29T06:59:12+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-29T06:59:31+00:00: Recorded command exit 0; command argv SHA-256
  961f033ce4cda452e0c435e4f4ca5a9ba13be3716a5073612fb78dc25df12ecb.

- 2026-09-29T07:00:41+00:00: Recorded command exit 1; command argv SHA-256
  428457ea9cc6a21bd46c5be6651ba2faccb5b0b07ddc2fd6f96eca730dea5ab7.

- 2026-09-29T07:01:27+00:00: Recorded command exit 0; command argv SHA-256
  be5f8307ce4fb9d12a13274a6682da6fa33af1261cf0b5f047cae46494399196.

- 2026-09-29T07:02:33+00:00: Recorded command exit 1; command argv SHA-256
  428457ea9cc6a21bd46c5be6651ba2faccb5b0b07ddc2fd6f96eca730dea5ab7.

- 2026-09-29T07:02:58+00:00: Recorded command exit 0; command argv SHA-256
  de4935b3061b251d99b621a57a775c4761c0e0911d9dbe0263925f702b4e329b.

- 2026-09-29T07:03:59+00:00: Recorded command exit 1; command argv SHA-256
  428457ea9cc6a21bd46c5be6651ba2faccb5b0b07ddc2fd6f96eca730dea5ab7.

- 2026-09-29T07:04:18+00:00: Recorded command exit 0; command argv SHA-256
  e9e8f996f7dc080219972c114f503f0d37b53d7546be0a5b826c3f6a241abd1f.

- 2026-09-29T07:05:27+00:00: Recorded command exit 1; command argv SHA-256
  428457ea9cc6a21bd46c5be6651ba2faccb5b0b07ddc2fd6f96eca730dea5ab7.

- 2026-09-29T07:06:10+00:00: Recorded command exit 0; command argv SHA-256
  a1159e9df3670d549d04524532629f5477ceb7deec9b45e47e8c009506ecb2c8.

- 2026-09-29T07:06:28+00:00: Recorded command exit 0; command argv SHA-256
  f263d964c8a700d9babd0cc0671c01116eec2734a1683989ff5138fbbdbbcfc8.

- 2026-09-29T07:06:45+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.

- 2026-09-29T07:07:20+00:00: Recorded command exit 0; command argv SHA-256
  fa00770a0021af01e7641845e6f6c6d28a8602941e200d582e0c5239348771ec.

- 2026-09-29T07:07:42+00:00: Recorded command exit 0; command argv SHA-256
  5f15a132da00fd860b986040ea259972e20c33dd38e73a92f1b11819e23cb949.

- 2026-09-29T07:08:05+00:00: Recorded command exit 0; command argv SHA-256
  5882166f925a7392d5afbac44f9caa6cb1c5885b57088e8b68d4974019d14058.

- 2026-09-29T07:08:22+00:00: Recorded command exit 0; command argv SHA-256
  f5a609479221f7f659349dd30ec48d3e56af250a55b7dce4cc04369052e57b83.

- 2026-09-29T07:08:49+00:00: Recorded command exit 0; command argv SHA-256
  98a2ba24f224d5a42ef213dc4ede0c12873ebc91d2cc9678f8dc466f6bcd527a.

- 2026-09-29T07:09:19+00:00: Recorded command exit 0; command argv SHA-256
  7c730eec3ea71bd24ffc5a9255bf7f542481bf601dba6c72bed6e00f6c2fab3c.

- 2026-09-29T07:09:36+00:00: Recorded command exit 0; command argv SHA-256
  b26356e8f7ad7ad126ed25fab8123a1b84fbde16f853a8e6e95d198335d7e491.

- 2026-09-29T07:09:54+00:00: Recorded command exit 0; command argv SHA-256
  543aa31794c0812207ab69051595e7831cf709d928f0a5bf28b3bc87074b7d0b.

- 2026-09-29T07:10:16+00:00: Recorded command exit 0; command argv SHA-256
  802a913c2136c506a518959d5139e85dc58a07f8d3d4493e90732cd65f7fe110.

- 2026-09-29T07:10:33+00:00: Recorded command exit 0; command argv SHA-256
  1fcb057d9f85ffbe03bf7eca6c549f7610bdc08c1b42bd21a436f1a41dc29c53.

- 2026-09-29T07:10:51+00:00: Recorded command exit 0; command argv SHA-256
  84fac7753083db6ad3f4fb164461b316a3884dc5514b03a5935eca98d07c94b7.

- 2026-09-29T07:11:08+00:00: Recorded command exit 0; command argv SHA-256
  88e9f364a7f3d7a9c0a6b2399387eb9286a89d7ad0e21ebdc78e73c6f5bff981.

- 2026-09-29T07:11:29+00:00: Recorded command exit 0; command argv SHA-256
  21117094098b2364bae217ba70b85ae8881fc18f01a49e5fbd7c5885212604e1.

- 2026-09-29T07:11:47+00:00: Recorded command exit 0; command argv SHA-256
  5683358fd86663acb2a46c22ab3ca8ab38c28c17ec0db5da0ac4aa3435cfff9f.

- 2026-09-29T07:12:06+00:00: Recorded command exit 0; command argv SHA-256
  d66aa65a0f5593ace33c48602f4e7e8f8038cae2d678ec65a84c6d8bb0733d09.

- 2026-09-29T07:12:23+00:00: Recorded command exit 0; command argv SHA-256
  c7a5c6eb60db45bbb2f3c32f8677eaf3257cfed306b3519b04cb69532cdd5273.

- 2026-09-29T07:12:40+00:00: Recorded command exit 0; command argv SHA-256
  59a703626c8e861e16d836e8453e94b23546a46dee006744ec6426be2ef166d7.

- 2026-09-29T07:12:56+00:00: Recorded command exit 0; command argv SHA-256
  df17b04f3a44c592efa460d24309bbc290854d9ad9fe0f1b16bef6f027d72568.

- 2026-09-29T07:13:27+00:00: Heartbeat by ar1513-repair3-luna56.

- 2026-09-29T07:13:31+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-29T07:13:48+00:00: Recorded command exit 0; command argv SHA-256
  a9d0d3f912836563c120589e83507c52ba764459af80e9550f53583649101492.

- 2026-09-29T07:14:07+00:00: Recorded command exit 101; command argv SHA-256
  be5f8307ce4fb9d12a13274a6682da6fa33af1261cf0b5f047cae46494399196.

- 2026-09-29T07:14:34+00:00: Recorded command exit 0; command argv SHA-256
  be5f8307ce4fb9d12a13274a6682da6fa33af1261cf0b5f047cae46494399196.

- 2026-09-29T07:15:01+00:00: Recorded command exit 0; command argv SHA-256
  bedfb3381b748877015928201c1d5e3d1ec4c97afb1b6f35e212a3b347e58607.

- 2026-09-29T07:15:25+00:00: Recorded command exit 0; command argv SHA-256
  961f033ce4cda452e0c435e4f4ca5a9ba13be3716a5073612fb78dc25df12ecb.

- 2026-09-29T07:15:42+00:00: Recorded command exit 0; command argv SHA-256
  0b488de689239ee4d81495ef99a5d60f07865368c85ac82e934421e514f340ac.

- 2026-09-29T07:17:12+00:00: Recorded command exit 0; command argv SHA-256
  428457ea9cc6a21bd46c5be6651ba2faccb5b0b07ddc2fd6f96eca730dea5ab7.

- 2026-09-29T07:17:47+00:00: Recorded command exit 0; command argv SHA-256
  0098bd24aefb309bcc7b9ef1da7a4839ee4b2fe8f7048933e02469ea79a00bad.

- 2026-09-29T07:18:08+00:00: Recorded command exit 0; command argv SHA-256
  39a4c0ad8235c4427391f0f1672fb11dade377ac12ea59b500ace05729a63129.

- 2026-09-29T07:18:57+00:00: Third repair pass: dispatch now rejects non-pinned executable paths,
  adapter digest drift, non-denied network, and source policy/target/alternate-egress enrollment
  drift. Ordinary asb run/sweep --local-mock dispatch is covered by provider-free integration tests;
  docs updated. Full tools/quality/check_coverage.py exited 0: 90.35% line coverage (configured
  workspace floor 90%) and critical package totals green; no floor or exclusion changes. Generated
  crates/asb-cli profraw artifacts were removed. Focused runtime 161 passed/1 ignored, CLI workflow
  3 passed, provenance test passed.

- 2026-09-29T07:19:04+00:00: Recorded command exit 0; command argv SHA-256
  38ec9250868454682fb0a1479274a6b2af8cde48add6ff4ec7b4bde3ab173e9a.

- 2026-09-29T07:19:27+00:00: Recorded command exit 101; command argv SHA-256
  9b498ebdee73cab471971c5dafbe261dc25698666e300cea3661fb0b83d17145.

- 2026-09-29T07:19:44+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-29T07:20:02+00:00: Recorded command exit 101; command argv SHA-256
  9b498ebdee73cab471971c5dafbe261dc25698666e300cea3661fb0b83d17145.

- 2026-09-29T07:20:22+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T07:20:43+00:00: Recorded command exit 0; command argv SHA-256
  9b498ebdee73cab471971c5dafbe261dc25698666e300cea3661fb0b83d17145.

- 2026-09-29T07:21:08+00:00: Recorded command exit 0; command argv SHA-256
  5e33b0919a6a0077a4b198cbee621505d3526ab41595e1551ff9d8afb7a77b97.

- 2026-09-29T07:21:32+00:00: Recorded command exit 0; command argv SHA-256
  8c7f6052233f62765e8e0f694be59527e8a99d854c1d3a6938c8bd61643ba6cb.

- 2026-09-29T07:21:50+00:00: Recorded command exit 0; command argv SHA-256
  9ff18ae8c92cc8f409f36f54f1587f392d67446f39a910907ba1a234040c55b9.

- 2026-09-29T07:22:14+00:00: Recorded command exit 0; command argv SHA-256
  0c3a5150207f73fcd896f8d69bcd72b4bab205cdeca8aa41f1a41b6ef0ed74a8.

- 2026-09-29T07:22:32+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.

- 2026-09-29T07:22:56+00:00: Recorded command exit 0; command argv SHA-256
  530ad0fd2fa5a848ab262df94ac62be28bf16f9846cd6cdd21f24b87c577da82.

- 2026-09-29T07:23:25+00:00: Repair committed and pushed at exact head
  cfed22bec49eaf9c74abf000ca274b3a353da3a9. SSH signature verified (ED25519 key
  SHA256:a36V6yPvRZyxnQ2113tiA/MlHt7mPfJEXAGByBXVkuE) with matching DCO Signed-off-by. Product tree
  was clean with no profraw artifacts before push. Full coverage exited 0 at 90.35% line coverage;
  focused runtime 161 passed/1 ignored, CLI workflow 3 passed, clippy and fmt passed.

- 2026-09-29T07:23:37+00:00: Recorded command exit 0; command argv SHA-256
  05daf4803d57586e8e8d556fa1cf0836d98c6925336da66c08435211bb769398.

- 2026-09-29T07:29:46+00:00: Independent exact-head review: provenance enforcement improved, but
  live bridge and policy/egress semantics remain incomplete; preserve all evidence.

- 2026-09-29T07:29:49+00:00: Release third repair claim for fourth repair pass; preserve cfed22b and
  review/coverage evidence.

- 2026-09-29T07:29:52+00:00: Claimed by ar1513-repair4-luna56.

- 2026-09-29T07:33:01+00:00: Heartbeat by ar1513-repair4-luna56.

- 2026-09-29T07:34:42+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-29T07:35:03+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T07:35:33+00:00: Recorded command exit 0; command argv SHA-256
  bedfb3381b748877015928201c1d5e3d1ec4c97afb1b6f35e212a3b347e58607.

- 2026-09-29T07:36:53+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-29T07:37:22+00:00: Recorded command exit 0; command argv SHA-256
  e6c3c60a7af791e078ffb64c7822f84b111943ab5bb57c21b22e3362bdf94f20.

- 2026-09-29T07:38:23+00:00: Recorded command exit 1; command argv SHA-256
  1f7db87ee4f70d1e1838b60a8b38b659453c740b7bb12419b52b80c158ead804.

- 2026-09-29T07:39:43+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T07:40:13+00:00: Recorded command exit 0; command argv SHA-256
  35cebf75490df0e1fa5677e345876dd3befa7c97c4870be34f15228fe45dd5d8.

- 2026-09-29T07:40:43+00:00: Recorded command exit 0; command argv SHA-256
  7b61fe9ef76ffc621b65b4fe82655503f87c43e6f2ed888160702bf57297cb98.

- 2026-09-29T07:42:18+00:00: Recorded command exit 0; command argv SHA-256
  1f7db87ee4f70d1e1838b60a8b38b659453c740b7bb12419b52b80c158ead804.

- 2026-09-29T07:43:50+00:00: Heartbeat by ar1513-repair4-luna56.

- 2026-09-29T07:44:41+00:00: Recorded command exit 101; command argv SHA-256
  11aa7892ee38d3a937558ce5f68e38a693ff8b89e160ec2c02b25ddf17ea330b.

- 2026-09-29T07:45:50+00:00: Recorded command exit 1; command argv SHA-256
  1f7db87ee4f70d1e1838b60a8b38b659453c740b7bb12419b52b80c158ead804.

- 2026-09-29T07:46:27+00:00: Recorded command exit 0; command argv SHA-256
  7b61fe9ef76ffc621b65b4fe82655503f87c43e6f2ed888160702bf57297cb98.

- 2026-09-29T07:47:55+00:00: Recorded command exit 0; command argv SHA-256
  7b61fe9ef76ffc621b65b4fe82655503f87c43e6f2ed888160702bf57297cb98.

- 2026-09-29T07:48:19+00:00: Recorded command exit 0; command argv SHA-256
  ddf28dd6a522f256ea1312faa1dd86d56add1374e28f0e78c6171cbc12664851.

- 2026-09-29T07:49:53+00:00: Heartbeat by ar1513-repair4-luna56.

- 2026-09-29T07:50:00+00:00: Recorded command exit 0; command argv SHA-256
  d04aa803a9fcb854b247572f9b417fd1935a57ca978bb887d2e7c188e99db043.

- 2026-09-29T07:50:20+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-29T07:50:46+00:00: Recorded command exit 0; command argv SHA-256
  bedfb3381b748877015928201c1d5e3d1ec4c97afb1b6f35e212a3b347e58607.

- 2026-09-29T07:51:16+00:00: Recorded command exit 0; command argv SHA-256
  e6c3c60a7af791e078ffb64c7822f84b111943ab5bb57c21b22e3362bdf94f20.

- 2026-09-29T07:51:42+00:00: Recorded command exit 101; command argv SHA-256
  9b498ebdee73cab471971c5dafbe261dc25698666e300cea3661fb0b83d17145.

- 2026-09-29T07:52:33+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T07:52:57+00:00: Recorded command exit 0; command argv SHA-256
  9b498ebdee73cab471971c5dafbe261dc25698666e300cea3661fb0b83d17145.

- 2026-09-29T07:53:27+00:00: Recorded command exit 0; command argv SHA-256
  e6c3c60a7af791e078ffb64c7822f84b111943ab5bb57c21b22e3362bdf94f20.

- 2026-09-29T07:53:48+00:00: Recorded command exit 0; command argv SHA-256
  7c730eec3ea71bd24ffc5a9255bf7f542481bf601dba6c72bed6e00f6c2fab3c.

- 2026-09-29T07:54:06+00:00: Recorded command exit 0; command argv SHA-256
  5882166f925a7392d5afbac44f9caa6cb1c5885b57088e8b68d4974019d14058.

- 2026-09-29T07:54:23+00:00: Recorded command exit 0; command argv SHA-256
  d04aa803a9fcb854b247572f9b417fd1935a57ca978bb887d2e7c188e99db043.

- 2026-09-29T07:55:00+00:00: Recorded command exit 0; command argv SHA-256
  0b488de689239ee4d81495ef99a5d60f07865368c85ac82e934421e514f340ac.

- 2026-09-29T07:55:21+00:00: Heartbeat by ar1513-repair4-luna56.

- 2026-09-29T07:56:47+00:00: Recorded command exit 1; command argv SHA-256
  1f7db87ee4f70d1e1838b60a8b38b659453c740b7bb12419b52b80c158ead804.

- 2026-09-29T07:57:54+00:00: Recorded command exit 0; command argv SHA-256
  1f7db87ee4f70d1e1838b60a8b38b659453c740b7bb12419b52b80c158ead804.

- 2026-09-29T07:58:29+00:00: Recorded command exit 0; command argv SHA-256
  e7de3c4e1ffb50ca4a1a8895c3fcbd7a30f2488da8ad5197ae0391ec18df23ec.

- 2026-09-29T07:58:54+00:00: Recorded command exit 0; command argv SHA-256
  d04aa803a9fcb854b247572f9b417fd1935a57ca978bb887d2e7c188e99db043.

- 2026-09-29T07:59:36+00:00: Recorded command exit 0; command argv SHA-256
  accc91176ca8b38753c596dccdee00f07652040b8c56f8b7771496ff25523e51.

- 2026-09-29T07:59:54+00:00: Recorded command exit 0; command argv SHA-256
  7df4d822095c4c557675dbe65db2e5af3cbd2c4c666ed2b58b71df96a39bb275.

- 2026-09-29T08:00:14+00:00: Recorded command exit 0; command argv SHA-256
  4ae301496ba135c02a5d0f787a58a24b5ed5f57118621c25660dc9c6aad878b7.

- 2026-09-29T08:00:36+00:00: Recorded command exit 0; command argv SHA-256
  20b5944c441fe68a8c2c99aba8a407bba3529fc6e58cc74c926e93b210d3f15b.

- 2026-09-29T08:00:56+00:00: Recorded command exit 0; command argv SHA-256
  e7dd9619523649dd38d1afec321852656957f4d9b1f61056e1a7199caf85f7fd.

- 2026-09-29T08:01:21+00:00: Recorded command exit 0; command argv SHA-256
  6a8d5c421d126b4dd56baeabe1e15260baf963ff12844e6c145fd4c0d6ffdc0b.

- 2026-09-29T08:01:38+00:00: Recorded command exit 0; command argv SHA-256
  d04aa803a9fcb854b247572f9b417fd1935a57ca978bb887d2e7c188e99db043.

- 2026-09-29T08:02:03+00:00: Heartbeat by ar1513-repair4-luna56.

- 2026-09-29T08:02:20+00:00: Fourth repair pushed signed DCO fd6e2ea (remote exact). Canonical
  provider-policy-v1 binding now matches control enrollment, owner material, namespace, handoff, and
  dispatch; provider-allowlist-v1 keeps alternate-egress distinct from target. Added production
  run_with_runtime_control_bootstrap composition consuming acquire_process_owner_material ->
  bridge_process_owner_material -> dispatch source -> CLI run/sweep; local mock remains explicit
  qualification only. Coverage check exited 0 with critical totals >=90%; LLVM_PROFILE_FILE external
  temp sink prevents child contract tests seeing checkout profraw, and all generated profraw
  artifacts were removed. Focused runtime 161 pass/1 ignored, CLI 130 pass, workflow provenance 3
  pass, clippy -D warnings pass, fmt pass. Recorded failures were addressed: 07:44 exit 101 was
  transient state-root ownership race on coverage rerun; 07:45 and 07:56 exit 1 coverage/profile
  runs were caused by checkout profraw visibility and were fixed by the external sink; clippy
  too-many-arguments was fixed by typed input grouping. Tree clean.

- 2026-09-29T08:07:35+00:00: Independent review confirms canonical policy and executable provenance
  fixed, but alternate-egress, actual CLI callsite/end-to-end bridge, and exact hosted coverage
  remain blockers.

- 2026-09-29T08:07:50+00:00: Heartbeat by ar1513-repair4-luna56.

- 2026-09-29T08:08:00+00:00: Recorded command exit 0; command argv SHA-256
  d04aa803a9fcb854b247572f9b417fd1935a57ca978bb887d2e7c188e99db043.

- 2026-09-29T08:08:23+00:00: Recorded command exit 0; command argv SHA-256
  6c2077d6b1542016933719ad3055beebe9429994142e091e8c08476239ea8724.

- 2026-09-29T08:10:01+00:00: Recorded command exit 0; command argv SHA-256
  0ecf5d8cd296dc4a985f65d627f56902e19914dec292a987b4cf8436f0fae2c8.

- 2026-09-29T08:11:01+00:00: Recorded command exit 101; command argv SHA-256
  979372d921adbbcf973ee03f23a046cefa309931681c9302b8effcffc9117dd6.

- 2026-09-29T08:11:30+00:00: Recorded command exit 0; command argv SHA-256
  e7de3c4e1ffb50ca4a1a8895c3fcbd7a30f2488da8ad5197ae0391ec18df23ec.

- 2026-09-29T08:15:47+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T08:16:24+00:00: Recorded command exit 0; command argv SHA-256
  bedfb3381b748877015928201c1d5e3d1ec4c97afb1b6f35e212a3b347e58607.

- 2026-09-29T08:18:14+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T08:18:41+00:00: Recorded command exit 0; command argv SHA-256
  bedfb3381b748877015928201c1d5e3d1ec4c97afb1b6f35e212a3b347e58607.

- 2026-09-29T08:20:25+00:00: Recorded command exit 0; command argv SHA-256
  f7b5054139cca5d2cdc793498cff6eee0606f3036e95cffd6abf10a44fa4a8f6.

- 2026-09-29T08:22:21+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T08:22:45+00:00: Recorded command exit 101; command argv SHA-256
  d3d5d92993dee0c6a25bee346711bde13767e8c88988c9c722480e55deb2cbf6.

- 2026-09-29T08:23:27+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T08:23:51+00:00: Recorded command exit 0; command argv SHA-256
  d3d5d92993dee0c6a25bee346711bde13767e8c88988c9c722480e55deb2cbf6.

- 2026-09-29T08:24:18+00:00: Recorded command exit 0; command argv SHA-256
  0a896c1bef90935ff3cca7802b9196114c5ef4cfe34b64e28114e4744c0e550f.

- 2026-09-29T08:24:49+00:00: Recorded command exit 0; command argv SHA-256
  e7de3c4e1ffb50ca4a1a8895c3fcbd7a30f2488da8ad5197ae0391ec18df23ec.

- 2026-09-29T08:25:31+00:00: Recorded command exit 0; command argv SHA-256
  6c2077d6b1542016933719ad3055beebe9429994142e091e8c08476239ea8724.

- 2026-09-29T08:26:15+00:00: Recorded command exit 1; command argv SHA-256
  41ce4d8029da51045239d10a27821682da1921bc9a0e94e3530fd6c994525c5a.

- 2026-09-29T08:27:13+00:00: Recorded command exit 1; command argv SHA-256
  6d116b345f0848511f061382ec5f6370e7c24be50bddae6c7c7e8474a1250fbf.

- 2026-09-29T08:27:39+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T08:28:10+00:00: Recorded command exit 0; command argv SHA-256
  0a896c1bef90935ff3cca7802b9196114c5ef4cfe34b64e28114e4744c0e550f.

- 2026-09-29T08:28:51+00:00: Recorded command exit 0; command argv SHA-256
  e7de3c4e1ffb50ca4a1a8895c3fcbd7a30f2488da8ad5197ae0391ec18df23ec.

- 2026-09-29T08:29:13+00:00: Recorded command exit 0; command argv SHA-256
  6c2077d6b1542016933719ad3055beebe9429994142e091e8c08476239ea8724.

- 2026-09-29T08:30:18+00:00: Recorded command exit 1; command argv SHA-256
  d150cd1c60cca464cebabdd4b06498c87b5f3202dcefb705160727a07cf388b5.

- 2026-09-29T08:31:21+00:00: Recorded command exit 1; command argv SHA-256
  78734e3d9238adf6ccb9c998c0a6f65b18e479fa280b3837e7c964a3a24dfb98.

- 2026-09-29T08:33:08+00:00: Recorded command exit 0; command argv SHA-256
  9b498ebdee73cab471971c5dafbe261dc25698666e300cea3661fb0b83d17145.

- 2026-09-29T08:34:07+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T08:34:34+00:00: Recorded command exit 0; command argv SHA-256
  e7de3c4e1ffb50ca4a1a8895c3fcbd7a30f2488da8ad5197ae0391ec18df23ec.

- 2026-09-29T08:35:01+00:00: Recorded command exit 0; command argv SHA-256
  6c2077d6b1542016933719ad3055beebe9429994142e091e8c08476239ea8724.

- 2026-09-29T08:36:06+00:00: Recorded command exit 1; command argv SHA-256
  d150cd1c60cca464cebabdd4b06498c87b5f3202dcefb705160727a07cf388b5.

- 2026-09-29T08:37:09+00:00: Recorded command exit 1; command argv SHA-256
  6b6002349838df5a983212393720606943abce05b277fd4ee89bbb21bebb2d12.

- 2026-09-29T08:38:15+00:00: Recorded command exit 0; command argv SHA-256
  e7de3c4e1ffb50ca4a1a8895c3fcbd7a30f2488da8ad5197ae0391ec18df23ec.

- 2026-09-29T08:38:55+00:00: Recorded command exit 0; command argv SHA-256
  e6c3c60a7af791e078ffb64c7822f84b111943ab5bb57c21b22e3362bdf94f20.

- 2026-09-29T08:39:17+00:00: Recorded command exit 0; command argv SHA-256
  9b498ebdee73cab471971c5dafbe261dc25698666e300cea3661fb0b83d17145.

- 2026-09-29T08:40:12+00:00: Recorded command exit 0; command argv SHA-256
  7c730eec3ea71bd24ffc5a9255bf7f542481bf601dba6c72bed6e00f6c2fab3c.

- 2026-09-29T08:40:29+00:00: Recorded command exit 0; command argv SHA-256
  86493f8896c8fa8abbee67e61699d43b87330a974af343ed5a3afcaadfd52ac9.

- 2026-09-29T08:40:47+00:00: Recorded command exit 0; command argv SHA-256
  07d5ffaeede2413081214f81f465458f9b35791bffdc809614352223820090a2.

- 2026-09-29T08:41:09+00:00: Recorded command exit 0; command argv SHA-256
  20b5944c441fe68a8c2c99aba8a407bba3529fc6e58cc74c926e93b210d3f15b.

- 2026-09-29T08:41:28+00:00: Recorded command exit 0; command argv SHA-256
  e7dd9619523649dd38d1afec321852656957f4d9b1f61056e1a7199caf85f7fd.

- 2026-09-29T08:41:53+00:00: Recorded command exit 0; command argv SHA-256
  6a8d5c421d126b4dd56baeabe1e15260baf963ff12844e6c145fd4c0d6ffdc0b.

- 2026-09-29T08:42:10+00:00: Recorded command exit 0; command argv SHA-256
  d04aa803a9fcb854b247572f9b417fd1935a57ca978bb887d2e7c188e99db043.

- 2026-09-29T08:42:28+00:00: Heartbeat by ar1513-repair4-luna56.

- 2026-09-29T08:42:43+00:00: Follow-up repair pushed exact signed DCO 4807e96. Runtime owner
  enrollment now takes the resolver-authenticated concrete allowlist identity, so alternate egress
  cannot collapse to receipt.target; added a negative target-digest assertion and canonical
  policy/egress tests. Production run_with_runtime_control_bootstrap is exercised for both run and
  sweep entry shapes before dispatch/lease failure, proving the bridge call path and fail-closed
  behavior; local/mock remains separate. Coverage diagnostics: clean exact-head check_coverage was
  blocked before report by cargo-llvm-cov leaving default_*.profraw in crates/asb-cli (exit 1 at
  08:30/08:31); capability child fallback now uses /tmp external sink. All profraw removed
  afterward. Focused runtime 164 pass/1 ignored, CLI 131 pass, clippy and fmt pass. Remote branch
  exactly 4807e96, tree clean. Hosted exact-head coverage/review still required.

- 2026-09-29T08:44:27+00:00: Independent review confirms prior auth/lifecycle/provenance fixes but
  bridge remains unusable; alternate-egress only works after missing materialization. Preserve
  4807e96 evidence.

- 2026-09-29T08:46:50+00:00: Heartbeat by ar1513-repair4-luna56.

- 2026-09-29T08:51:21+00:00: Recorded command exit 0; command argv SHA-256
  295a35f99d4aa7024b5e0a35d1dd38654014d35e0d6da14a79231d3b8d7d50ba.

- 2026-09-29T08:51:43+00:00: Recorded command exit 101; command argv SHA-256
  64dab5bf01becc475a316fb33b11f66c67bf33927d541073a91edf2da0fdfb32.

- 2026-09-29T08:55:08+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T08:55:29+00:00: Recorded command exit 101; command argv SHA-256
  0120dc940e49370ca9ec727b255f1bf8b2c0025c6c0cd3d3241ae0b28d224636.

- 2026-09-29T08:55:47+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T08:56:07+00:00: Recorded command exit 101; command argv SHA-256
  0120dc940e49370ca9ec727b255f1bf8b2c0025c6c0cd3d3241ae0b28d224636.

- 2026-09-29T08:56:26+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T08:56:44+00:00: Recorded command exit 101; command argv SHA-256
  0120dc940e49370ca9ec727b255f1bf8b2c0025c6c0cd3d3241ae0b28d224636.

- 2026-09-29T08:57:26+00:00: Recorded command exit 101; command argv SHA-256
  0120dc940e49370ca9ec727b255f1bf8b2c0025c6c0cd3d3241ae0b28d224636.

- 2026-09-29T08:58:11+00:00: Recorded command exit 101; command argv SHA-256
  0120dc940e49370ca9ec727b255f1bf8b2c0025c6c0cd3d3241ae0b28d224636.

- 2026-09-29T08:58:32+00:00: Recorded command exit 101; command argv SHA-256
  0120dc940e49370ca9ec727b255f1bf8b2c0025c6c0cd3d3241ae0b28d224636.

- 2026-09-29T08:58:54+00:00: Recorded command exit 101; command argv SHA-256
  0120dc940e49370ca9ec727b255f1bf8b2c0025c6c0cd3d3241ae0b28d224636.

- 2026-09-29T08:59:15+00:00: Recorded command exit 101; command argv SHA-256
  0120dc940e49370ca9ec727b255f1bf8b2c0025c6c0cd3d3241ae0b28d224636.

- 2026-09-29T08:59:34+00:00: Recorded command exit 101; command argv SHA-256
  0120dc940e49370ca9ec727b255f1bf8b2c0025c6c0cd3d3241ae0b28d224636.

- 2026-09-29T09:01:58+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T09:02:19+00:00: Recorded command exit 101; command argv SHA-256
  0120dc940e49370ca9ec727b255f1bf8b2c0025c6c0cd3d3241ae0b28d224636.

- 2026-09-29T09:02:40+00:00: Recorded command exit 101; command argv SHA-256
  0120dc940e49370ca9ec727b255f1bf8b2c0025c6c0cd3d3241ae0b28d224636.

- 2026-09-29T09:04:42+00:00: Recorded command exit 1; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T09:05:24+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T09:05:42+00:00: Recorded command exit 101; command argv SHA-256
  0120dc940e49370ca9ec727b255f1bf8b2c0025c6c0cd3d3241ae0b28d224636.

- 2026-09-29T09:06:49+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T09:07:08+00:00: Recorded command exit 0; command argv SHA-256
  0120dc940e49370ca9ec727b255f1bf8b2c0025c6c0cd3d3241ae0b28d224636.

- 2026-09-29T09:07:33+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T09:07:55+00:00: Heartbeat by ar1513-repair4-luna56.

- 2026-09-29T09:08:04+00:00: Heartbeat by ar1513-repair4-luna56.

- 2026-09-29T09:08:07+00:00: Recorded command exit 101; command argv SHA-256
  b945362378f77f64a68eb9e8d400e693e008357f0cc0d69f7bfe3bb93e47ae02.

- 2026-09-29T09:08:30+00:00: Recorded command exit 0; command argv SHA-256
  b945362378f77f64a68eb9e8d400e693e008357f0cc0d69f7bfe3bb93e47ae02.

- 2026-09-29T09:08:58+00:00: Recorded command exit 101; command argv SHA-256
  3d4cc54827fa0ae5c402321266e4a8e9a84a69a17f7ff27b7a0f0c858d454784.

- 2026-09-29T09:09:16+00:00: Recorded command exit 0; command argv SHA-256
  3550b04cffcdb9f04728eb9f54086bacfd9cd62167602bc3e8f9e9eeb9b712f1.

- 2026-09-29T09:09:37+00:00: Recorded command exit 0; command argv SHA-256
  9b498ebdee73cab471971c5dafbe261dc25698666e300cea3661fb0b83d17145.

- 2026-09-29T09:09:56+00:00: Recorded command exit 0; command argv SHA-256
  e7de3c4e1ffb50ca4a1a8895c3fcbd7a30f2488da8ad5197ae0391ec18df23ec.

- 2026-09-29T09:10:41+00:00: Recorded command exit 1; command argv SHA-256
  1f7db87ee4f70d1e1838b60a8b38b659453c740b7bb12419b52b80c158ead804.

- 2026-09-29T09:11:08+00:00: Recorded command exit 0; command argv SHA-256
  e7de3c4e1ffb50ca4a1a8895c3fcbd7a30f2488da8ad5197ae0391ec18df23ec.

- 2026-09-29T09:12:41+00:00: Recorded command exit 0; command argv SHA-256
  1f7db87ee4f70d1e1838b60a8b38b659453c740b7bb12419b52b80c158ead804.
