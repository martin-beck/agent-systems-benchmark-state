---
{
  "branch": "feature/ar-1513-authenticated-lease-dispatch-bridge",
  "checkpoint_commit": "bde018c10b3b69252f9a5b8429f9cc277e44953d",
  "claim_expires": "2026-09-29T08:30:44+00:00",
  "depends_on": [
    "AR-1502",
    "AR-1484"
  ],
  "id": "AR-1513",
  "next_action": "Repair P1 findings from independent exact-head review: bind enrollment identity/namespace/credential/relay/target, bind lease to dispatch source, and retain lifecycle fences after source consumption; then rerun review and protected gates.",
  "observed_branch": "feature/ar-1513-authenticated-lease-dispatch-bridge",
  "observed_dirty": 2,
  "observed_head": "bde018c10b3b69252f9a5b8429f9cc277e44953d",
  "owner": "ar1513-repair2-luna56",
  "plan": "../plans/AR-1513-authenticated-lease-dispatch-bridge.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Authenticate process-owner material, validate executable provenance, and connect leases to ordinary live dispatch.",
  "task_revision": 108,
  "title": "Authenticated lease-to-live-dispatch bridge",
  "updated_at": "2026-09-29T06:35:08+00:00",
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
