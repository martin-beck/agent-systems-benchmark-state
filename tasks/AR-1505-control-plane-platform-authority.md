---
{
  "branch": "feature/ar-1505-control-plane-platform-authority",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-29T01:29:27+00:00",
  "depends_on": [
    "AR-1473",
    "AR-1474",
    "AR-1480",
    "AR-1484",
    "AR-1485",
    "AR-1502"
  ],
  "id": "AR-1505",
  "next_action": "Implement versioned RuntimeBootstrap control operation and runtime adapter; add provider-free identity/generation/nonce/expiry/revocation/restart/cancellation/egress tests.",
  "observed_branch": "feature/ar-1505-control-plane-platform-authority",
  "observed_dirty": 11,
  "observed_head": "3c6af6b351e0c32ee8f5e48716654d854dcbbac2",
  "owner": "ar1505-control-plane-luna56",
  "plan": "../plans/AR-1505-control-plane-platform-authority.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Provide an authenticated platform protocol that issues private runtime bootstrap inputs to ASB.",
  "task_revision": 77,
  "title": "Control-plane platform authority/bootstrap protocol",
  "updated_at": "2026-09-28T23:31:29+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1505-control-plane-platform-authority"
}
---

Successor to the exact AR-1504 blocker. AR-1504 proved owner-only control
socket discovery but could not obtain the private authority inputs needed to
construct an authenticated runtime owner: the current control protocol has no
platform-owned bootstrap/authority operation, while ASB CLI still dispatches
with `None,None`. This AR defines that missing control-plane boundary without
merging the incomplete discovery-only patch.

Acceptance requires:

- a versioned, authenticated control-plane operation that issues or references
  runtime-owned bootstrap authority, certificate enrollment, namespace, relay
  and lease roots, credential reference, expiry, cancellation and restart
  binding without exposing private material;
- an ASB runtime adapter that consumes only that source and constructs private
  `RuntimeAuthorityInputs`, `RuntimeCertificateAuthoritySource`, bootstrap and
  receipt requests, with no caller/config/socket/chain authority injection;
- deterministic provider-free protocol and negative tests for identity,
  generation, nonce, expiry, revocation, restart, cancellation and egress
  denial;
- an explicit handoff contract for AR-1504 to wire the launcher and CLI
  entrypoint, with no fabricated authority or live-provider requirement;
- independent review, SSH-signed DCO commit, exact-head hosted CI, protected
  merge, and post-merge verification.

Non-goals: asb-tui changes, live provider reachability, synthetic authority,
public credential/socket paths, or weakening fail-closed gates.

- 2026-09-28T22:56:27+00:00: Dependencies are done; promote the narrow control-plane
  authority/bootstrap protocol successor required by AR-1504 exact blocker.

- 2026-09-28T22:56:32+00:00: Claimed by ar1505-control-plane-luna56.

- 2026-09-28T22:57:44+00:00: Heartbeat by ar1505-control-plane-luna56.

- 2026-09-28T22:58:32+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.

- 2026-09-28T22:58:49+00:00: Recorded command exit 0; command argv SHA-256
  6840d2f0cea6f9cf6ffce81b9b1b74dcdddaff8701fc6cc1705c309033813254.

- 2026-09-28T22:59:05+00:00: Heartbeat by ar1505-control-plane-luna56.

- 2026-09-28T23:00:14+00:00: Setup audit at protected origin/main 3c6af6b: declared worktree
  agent-systems-benchmark-ar-1505-control-plane-platform-authority is clean. Existing protocol
  symbols: ControlCall::RuntimeReceipt and CONTROL_RUNTIME_RECEIPT_V1=1.10 return chain+receipt but
  accept only provider/generation/request nonce; ControlBackend lacks peer/session identity;
  RunnerBackend handles RuntimeReceipt at crates/asb-cli/src/control.rs:3177; RuntimeAuthorityRecord
  and RuntimeCertificateAuthoritySource remain private runtime inputs. Existing
  ProvisionedControlServer/handoff.rs only passes an anonymous descriptor. This exact gap requires a
  new versioned authenticated bootstrap operation, not caller-supplied authority or synthetic paths.

- 2026-09-28T23:02:29+00:00: Recorded command exit 101; command argv SHA-256
  51ba69d4c610737a26b3ee3167f118767410cbc10708f3e6931f62c061247358.

- 2026-09-28T23:05:28+00:00: Recorded command exit 101; command argv SHA-256
  6ad2f71e2002b797aa7b80ba5f0bbcb7f925ac75dcc3b4c1d85e5543b906175f.

- 2026-09-28T23:05:54+00:00: Exact gate failure at 23:05:28Z: handoffctl run -- cargo check --locked
  -p asb-control -p asb-runtime -p asb-cli exited 101. rustc E0382
  crates/asb-control/src/endpoint.rs:348:54: PeerIdentity::from_fd(stream) moved &mut UnixStream
  before read_frame_until; compiler suggested reborrow &mut *stream. This is a local borrow repair,
  not a protocol blocker.

- 2026-09-28T23:05:57+00:00: Heartbeat by ar1505-control-plane-luna56.

- 2026-09-28T23:06:10+00:00: Recorded command exit 101; command argv SHA-256
  6ad2f71e2002b797aa7b80ba5f0bbcb7f925ac75dcc3b4c1d85e5543b906175f.

- 2026-09-28T23:07:09+00:00: Heartbeat by ar1505-control-plane-luna56.

- 2026-09-28T23:07:11+00:00: Applied compiler-suggested reborrow at endpoint.rs:343 after exact
  E0382; added Catalog runtime_bootstraps initialization and MutationTarget
  validation/reconciliation arms required by new bootstrap operation. The 23:05 repeated hash was
  not rerun after repair until source changed.

- 2026-09-28T23:07:19+00:00: Recorded command exit 0; command argv SHA-256
  6ad2f71e2002b797aa7b80ba5f0bbcb7f925ac75dcc3b4c1d85e5543b906175f.

- 2026-09-28T23:08:31+00:00: Recorded command exit 0; command argv SHA-256
  3b12f28f56185d0e731ee1ffc3d557bc6c5fa170c87e7e664145fdbcd1eb866e.

- 2026-09-28T23:09:02+00:00: Recorded command exit 0; command argv SHA-256
  86be4d3b0bdeb49663d8e7d90fc28e64e308bc71b7c7e0ea1c62c520e6377e24.

- 2026-09-28T23:09:35+00:00: Heartbeat by ar1505-control-plane-luna56.

- 2026-09-28T23:09:43+00:00: Protocol implementation now compiles. Focused evidence: cargo test
  --locked -p asb-control --lib --no-fail-fast passed 70/70, including bootstrap identity-only
  request, response session/generation/nonce/restart/expiry binding, cancellation binding, and
  unknown-field rejection; cargo test --locked -p asb-cli --lib runtime_authority passed 2/2.
  RuntimeBootstrap is server peer-bound through ControlBackend::execute_authenticated and
  ControlClient::session_identity_sha256; RunnerBackend rejects mismatched caller hashes and records
  revocation.

- 2026-09-28T23:10:04+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-28T23:10:25+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-28T23:10:55+00:00: Exact gate at 23:10:04Z: handoffctl run -- cargo fmt --all -- --check
  exited 1 with rustfmt diffs only (import ordering in asb-cli/control.rs and
  asb-runtime/live_service.rs, line wrapping in control.rs/protocol.rs/endpoint.rs). No semantic
  failure; cargo fmt --all subsequently applied through handoffctl and completed successfully. Added
  authenticated cancel peer check; cancellation adapter still needs a runtime helper and lifecycle
  tests.

- 2026-09-28T23:10:58+00:00: Heartbeat by ar1505-control-plane-luna56.

- 2026-09-28T23:11:17+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-28T23:11:39+00:00: Recorded command exit 101; command argv SHA-256
  7fc852536b8fb5ccc5f554968a228534cdc199e2aba684765a68f5bc9084a7b6.

- 2026-09-28T23:12:01+00:00: Exact gate at 23:11:39Z: handoffctl run -- cargo clippy --locked -p
  asb-control -p asb-runtime -p asb-cli --all-targets -- -D warnings exited 101. Four
  clippy::nonminimal_bool errors in asb-control/src/protocol.rs:1623-1626 used
  !validate_digest(...).is_ok(); repaired to validate_digest(...).is_err(). The preceding cargo fmt
  --check passed.

- 2026-09-28T23:12:03+00:00: Heartbeat by ar1505-control-plane-luna56.

- 2026-09-28T23:12:17+00:00: Recorded command exit 0; command argv SHA-256
  7fc852536b8fb5ccc5f554968a228534cdc199e2aba684765a68f5bc9084a7b6.

- 2026-09-28T23:12:49+00:00: Recorded command exit 0; command argv SHA-256
  a3cce4128a71b1f348011f31209cbf7fe53d7496861364a299f63e0c8a798569.

- 2026-09-28T23:13:17+00:00: Recorded command exit 101; command argv SHA-256
  41d9e7ab675a15433922e000e6344bdcbbc8b7a1ce999cfa353e5747a4031238.

- 2026-09-28T23:13:44+00:00: Exact gate at 23:13:17Z: handoffctl run -- cargo test --locked -p
  asb-cli --lib --no-fail-fast ran 129 tests; 128 passed, 1 failed in existing
  control::tests::production_backend_runs_without_frontend_and_recovers_idempotency at
  control.rs:8325, unwrap Err operation: control state root is already owned. This is a test-root
  ownership collision/cleanup issue outside the bootstrap diff; no compiler or bootstrap assertion
  failed. Runtime live_service focused suite separately passed 47 tests.

- 2026-09-28T23:13:51+00:00: Heartbeat by ar1505-control-plane-luna56.

- 2026-09-28T23:13:58+00:00: Recorded command exit 0; command argv SHA-256
  10e195ea1440e3bed843c291aa7c0da8f29ae39241929f63ad3cf98eed32a84e.

- 2026-09-28T23:14:22+00:00: Recorded command exit 101; command argv SHA-256
  41d9e7ab675a15433922e000e6344bdcbbc8b7a1ce999cfa353e5747a4031238.

- 2026-09-28T23:14:53+00:00: Exact gate at 23:14:22Z: repeated parallel cargo test --locked -p
  asb-cli --lib failed the same pre-existing
  control::tests::production_backend_runs_without_frontend_and_recovers_idempotency with control
  state root already owned. The same test run serially through handoffctl with --exact --nocapture
  passed 1/1 immediately. This is recorded as a parallel test isolation flake; no bootstrap test
  failed. Do not claim the default parallel package gate green until the existing collision is
  repaired or independently dispositioned.

- 2026-09-28T23:14:55+00:00: Heartbeat by ar1505-control-plane-luna56.

- 2026-09-28T23:15:09+00:00: Recorded command exit 0; command argv SHA-256
  61800d22606bdfb2139ec72556651d987080562a1811c9a2aecb069f2d05fbd3.

- 2026-09-28T23:16:22+00:00: Recorded command exit 0; command argv SHA-256
  73d005d4c4983870f0c5405c6c97dffbf521d57825b14d75dae888988fbdcd03.

- 2026-09-28T23:16:47+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-28T23:17:06+00:00: Recorded command exit 0; command argv SHA-256
  7fc852536b8fb5ccc5f554968a228534cdc199e2aba684765a68f5bc9084a7b6.

- 2026-09-28T23:17:23+00:00: Recorded command exit 0; command argv SHA-256
  7c730eec3ea71bd24ffc5a9255bf7f542481bf601dba6c72bed6e00f6c2fab3c.

- 2026-09-28T23:17:59+00:00: Recorded command exit 101; command argv SHA-256
  5f0cf8b7f8b4d39559c6aa438cb9097561deab7ff7bad8dcd2b24f48a02fb447.

- 2026-09-28T23:18:26+00:00: Exact gate at 23:17:59Z: handoffctl run -- cargo test --locked -p
  asb-control -p asb-runtime --no-fail-fast -- --test-threads=1: all asb-control unit/integration
  tests and all asb-runtime tests passed (70 control unit, 27 control, 7 endpoint, 4 schema; 149
  runtime unit plus integration/doc tests), but
  schema_conformance::checked_in_schemas_equal_fresh_generation failed because the checked-in
  control schemas did not include the new RuntimeBootstrap variants. This is the required
  generated-schema refresh, not a semantic test failure.

- 2026-09-28T23:18:29+00:00: Heartbeat by ar1505-control-plane-luna56.

- 2026-09-28T23:18:54+00:00: Recorded command exit 0; command argv SHA-256
  1d43ba8d4e8c556450d02e94072f1fe915e6a7e92c6a3dcb9b5df02d4d0c15e2.

- 2026-09-28T23:19:34+00:00: Recorded command exit 0; command argv SHA-256
  b46e24210b000d5f51b412760aab7c098d84ac5623ce575734ef571d44950e27.

- 2026-09-28T23:20:23+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-28T23:20:41+00:00: Recorded command exit 0; command argv SHA-256
  b46e24210b000d5f51b412760aab7c098d84ac5623ce575734ef571d44950e27.

- 2026-09-28T23:21:35+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-28T23:21:52+00:00: Recorded command exit 0; command argv SHA-256
  8f17c847f4a2195b70672a78370a4a851575cbe6ca7ca36ad7eacc632c7c1921.

- 2026-09-28T23:22:10+00:00: Recorded command exit 0; command argv SHA-256
  6434bbb09b9c40436ed2c61d87cf23ea5d5de9f75ceeab6d72845ceca36f974f.

- 2026-09-28T23:22:27+00:00: Recorded command exit 0; command argv SHA-256
  54c79244c864ab025032251942ee46a40d31b6a602b1854d4e5ffab69b8f16ae.

- 2026-09-28T23:22:44+00:00: Recorded command exit 0; command argv SHA-256
  8462ec991c04a353b4abc0fc303b0ce5d8dcc09a5e52eb3e44ca3ac401b31ca3.

- 2026-09-28T23:24:23+00:00: Heartbeat by ar1505-control-plane-luna56.

- 2026-09-28T23:24:31+00:00: Recorded command exit 101; command argv SHA-256
  ccfc6f0a1e826328dbed13f5b9f2f71a67021bc3e60e7ea80709f3429f90299a.

- 2026-09-28T23:25:00+00:00: Recorded command exit 0; command argv SHA-256
  f43731b911146d51ab3398482427c333a43e8c5ec2ebed23da68f3e14c009335.

- 2026-09-28T23:25:41+00:00: Gate evidence: initial schema gate invocation omitted the required
  product-worktree cd and exited 101 with exact stderr: error: could not find Cargo.toml in
  /srv/data/projects/agent-systems-benchmark-state or any parent directory. Corrected command
  explicitly cd'd to
  /srv/data/projects/agent-systems-benchmark-ar-1505-control-plane-platform-authority;
  schema_conformance passed 4/4 serial (checked-in equality, negative boundary rejection, fixtures,
  envelope validation). Prior exit-0 sequence remains: cargo check asb-control/asb-runtime/asb-cli;
  control lib 70/70; runtime live_service 47 passed; clippy -D warnings; fmt check; asb-cli lib
  serial 129/129; git diff --check. Parallel asb-cli has known existing state-root collision (128
  pass, 1 fail), serial is green. Next: strengthen response binding review and run
  changed-package/full gates.

- 2026-09-28T23:26:00+00:00: Exact disposition for recorded failure
  ccfc6f0a1e826328dbed13f5b9f2f71a67021bc3e60e7ea80709f3429f90299a (23:24:31Z): the
  schema_conformance gate was invoked from state-repository cwd, so Cargo searched
  /srv/data/projects/agent-systems-benchmark-state and emitted  (exit 101). This was a
  command-cwd/setup error, not a product compiler or test failure; the corrected explicit
  product-worktree cd command passed 4/4 serial.

- 2026-09-28T23:26:11+00:00: Correction: the prior exact-disposition note lost the stderr token due
  shell backtick expansion while recording. Exact stderr for
  ccfc6f0a1e826328dbed13f5b9f2f71a67021bc3e60e7ea80709f3429f90299a was: error: could not find
  Cargo.toml in /srv/data/projects/agent-systems-benchmark-state or any parent directory. No product
  gate ran in that invocation; explicit product-worktree cd then passed schema_conformance 4/4
  serial.

- 2026-09-28T23:26:41+00:00: Recorded command exit 0; command argv SHA-256
  597ec5ec236857ea8cba32a83c3ee01b60a4f2d3f0afa48e11ce862211da7f89.

- 2026-09-28T23:27:30+00:00: Recorded command exit 0; command argv SHA-256
  b693d2f4e50fc969300b3a482d52c5e7308f0327fba8fa1e9869224a3cf3eb00.

- 2026-09-28T23:27:50+00:00: Recorded command exit 0; command argv SHA-256
  b5d0da032a9f8027763deea73b26cfcdf3df5885390ef85832697f8161a6ef02.

- 2026-09-28T23:28:13+00:00: Recorded command exit 0; command argv SHA-256
  e7c797a07409e2209543b91516b969451c1991ad30ba66c2fc5451ac896836c7.

- 2026-09-28T23:28:41+00:00: Current gate status: schema_conformance 4/4 serial green after
  generated v1.11 refresh; asb-control/asb-runtime/asb-cli changed-package test suite green serial
  (no failures; asb-cli 129/129, runtime 149 passed plus 1 ignored, control 70/70, doctests green);
  clippy all targets with -D warnings green; RUSTDOCFLAGS=-D warnings cargo doc for all three
  packages green; cargo fmt and git diff --check green. The known parallel asb-cli state-root
  ownership collision remains dispositioned by serial green rerun and was not weakened. Receipt
  expiry equality validation and negative test added. Next: complete independent full diff review,
  then final workspace/full gate and publication preparation.

- 2026-09-28T23:29:11+00:00: Independent semantic review completed after latest green gates:
  RuntimeBootstrap is accepted only through execute_authenticated with kernel-derived SO_PEERCRED
  session digest (uid/gid/pid plus runner instance); caller-supplied session digest is rejected on
  mismatch before authority lookup. Response validation binds provider, generation, request nonce,
  session, restart binding, chain digest, outer expiry, and receipt expiry; runtime adapter rechecks
  current time and expiry equality. Cancellation requires provider/generation/session/cancellation
  binding, marks the exact durable bootstrap revoked, removes replay mutation state, and rejects
  stale/forged bindings; repeated cancellation is idempotent through its own mutation key. No
  provider call, secret, path, or authority private material crosses the protocol. No PR or commit
  has been created yet; next is final diff/full workspace review.

- 2026-09-28T23:29:27+00:00: Heartbeat by ar1505-control-plane-luna56.

- 2026-09-28T23:30:18+00:00: Recorded command exit 0; command argv SHA-256
  3a24fa191989202ee00bcd1f42ccaf99de452fd03e24e55cf98b88e47878bb0a.

- 2026-09-28T23:30:56+00:00: Recorded command exit 0; command argv SHA-256
  3a24fa191989202ee00bcd1f42ccaf99de452fd03e24e55cf98b88e47878bb0a.

- 2026-09-28T23:31:22+00:00: Final gate status: cargo test --locked --workspace --no-fail-fast --
  --test-threads=1 completed exit 0; all workspace unit, integration, schema, boundary, and doctests
  passed (expected compile-fail doctests passed). Changed-package clippy -D warnings, package docs
  with RUSTDOCFLAGS=-D warnings, serial package tests, schema conformance 4/4, fmt, and diff check
  are green. No gate is blocked. The first 30-second invocation was interrupted before handoff
  completion and produced only partial log; it was rerun with handoff timeout 600 and completed exit
  0, with exact terminal evidence recorded by the successful state run. Known parallel asb-cli
  state-root collision remains an environment collision only; serial full package and workspace
  gates are green and no test was weakened. Ready for signed/DCO commit and PR publication.

- 2026-09-28T23:31:29+00:00: Recorded command exit 1; command argv SHA-256
  7beec9e69f85e6e8c0929ac71a9ec77ea5fd6759af91d9889847385e2afae421.
