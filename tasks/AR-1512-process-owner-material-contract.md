---
{
  "branch": "feature/ar-1512-process-owner-material-contract",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-29T07:10:39+00:00",
  "depends_on": [
    "AR-1502",
    "AR-1484"
  ],
  "id": "AR-1512",
  "next_action": "Inspect exact diff and commit the provider-free contract/store; parent must create successor for authenticated lease-to-LiveProviderRuntimeHandle bridge before claiming live CLI run/sweep.",
  "observed_branch": "feature/ar-1512-process-owner-material-contract",
  "observed_dirty": 0,
  "observed_head": "a4064abf22b73096ebb26df9bca8d1dc28a7d81f",
  "owner": "ar1512-process-owner-luna56",
  "plan": "../plans/AR-1512-process-owner-material-contract.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Provide the authenticated process-owner material source and ordinary CLI/control caller needed to consume runtime authority.",
  "task_revision": 37,
  "title": "Authenticated process-owner material contract",
  "updated_at": "2026-09-29T05:20:54+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1512-process-owner-material-contract"
}
---

AR-1511 proved that the runtime issuer and lifecycle fencing are implemented,
but protected main still lacks the source that can safely supply them. The
existing control records contain public digests only; no non-test provider or
ordinary CLI/control caller can reconstruct private roots, pinned tools,
policy/allowlist, namespace or launch-input provenance. This AR owns that
missing contract and source.

Acceptance requires:

- an ASB-only, versioned authenticated process-owner material contract issued
  by the runtime/control owner, carrying opaque capability references plus the
  private roots, namespace, pinned tool/adapter bundle, policy/allowlist,
  credential capability and launch provenance needed by the provider;
- a non-test control/runtime caller that obtains the contract from authenticated
  owner/enrollment state and feeds the runtime issuer/dispatch source without
  caller-built authority, PATH/config injection or digest-only reconstruction;
- explicit endpoint/session, generation, expiry, restart, cancellation,
  revocation, teardown, target and alternate-egress bindings, with unknown
  fields and replay/mismatch rejected;
- launch executable/adapter provenance is bound to the authenticated tool
  bundle, and ordinary CLI live run/sweep reaches the provider-owned source;
- deterministic provider-free positive/negative tests, generated docs, focused
  and serial workspace/formal/privacy gates, independent review, SSH-signed DCO
  exact-head PR, protected merge and post-merge assurance.

Non-goals: asb-tui, live provider reachability, public credentials, private
host data, synthetic authority, or weakening fail-closed/native/formal gates.

- 2026-09-29T04:56:00+00:00: Created as the prerequisite successor to blocked
  AR-1511. Its diagnostic audit showed that implementing a consumer over
  digest-only records would fabricate authority; build the authenticated
  process-owner source and ordinary caller first.

- 2026-09-29T04:56:08+00:00: AR-1511 diagnostic blocker reconciled; promote prerequisite
  authenticated process-owner material contract and ordinary caller.

- 2026-09-29T04:56:11+00:00: Claimed by ar1512-process-owner-luna56.

- 2026-09-29T04:58:03+00:00: Heartbeat by ar1512-process-owner-luna56.

- 2026-09-29T04:58:06+00:00: Setup audit: authoritative AR-1512 state is ASB state checkout;
  protected main is f92c2e941913129d7db50480f71e8361a0d43a0c. Existing product main is dirty and
  AR-1511 work must not be reused. Starting isolated worktree and contract audit.

- 2026-09-29T04:58:44+00:00: Recorded command exit 0; command argv SHA-256
  227bd2b8f251398a28e02809a6a2e32716ea68be7d6a13f02381b8daf3223aa1.

- 2026-09-29T05:04:46+00:00: Heartbeat by ar1512-process-owner-luna56.

- 2026-09-29T05:04:58+00:00: Audit complete: protected main has digest-only RuntimeAuthorityRecord
  and RuntimeBootstrapRecord; no non-test owner material source. RuntimeAuthorityInputs are internal
  and the materialization path is absent outside test/internal seams. AR-1511 dirty worktree is not
  reused.

- 2026-09-29T05:07:23+00:00: Recorded command exit 101; command argv SHA-256
  1c6e3d8d232e466e14598929e51bba34dbfff29b29579b2c872590b2de8e94e0.

- 2026-09-29T05:07:42+00:00: Recorded command exit 0; command argv SHA-256
  1c6e3d8d232e466e14598929e51bba34dbfff29b29579b2c872590b2de8e94e0.

- 2026-09-29T05:08:21+00:00: Focused test first failed at 05:07:23 during compilation: four test
  assertions compared Result<opaque capability/lease/store, error> with assert_eq!, requiring
  PartialEq on private opaque types. Patched tests to use matches! without exposing or deriving
  equality for capabilities/material. Retry at 05:08 passed 4 process_owner_material tests.

- 2026-09-29T05:08:59+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-29T05:09:18+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T05:09:39+00:00: Recorded command exit 0; command argv SHA-256
  1c6e3d8d232e466e14598929e51bba34dbfff29b29579b2c872590b2de8e94e0.

- 2026-09-29T05:10:02+00:00: Recorded command exit 0; command argv SHA-256
  df2bc9374902110cacfc5431fc10b3a68e6e9bc8662799a8fabb9f6e07a98612.

- 2026-09-29T05:10:39+00:00: Heartbeat by ar1512-process-owner-luna56.

- 2026-09-29T05:11:00+00:00: Implemented process_owner_material module from protected f92c2e9:
  versioned deny-unknown-fields contract binds
  endpoint/session/generation/expiry/restart/cancel/revoke/teardown/target/alternate
  egress/namespace/credential/tool/policy/allowlist/private roots/launch provenance; owner-side
  private store consumes nonces and fences lifecycle; RuntimeProcessOwnerMaterialCaller accepts only
  nonce. Added provider-free positive/negative tests and docs/README link. Focused runtime tests 4/4
  and clippy -D warnings pass after formatting. Initial compile failure was recorded separately; no
  product authority was derived from digest-only records.

- 2026-09-29T05:11:07+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T05:11:25+00:00: Recorded command exit 0; command argv SHA-256
  1c6e3d8d232e466e14598929e51bba34dbfff29b29579b2c872590b2de8e94e0.

- 2026-09-29T05:11:54+00:00: Recorded command exit 0; command argv SHA-256
  b36d15881eb65027724bc584f1b04db05666cd79896b100806e528307c04b65c.

- 2026-09-29T05:12:49+00:00: Recorded command exit 101; command argv SHA-256
  534f8613e1c316db8f0f46dd989e44e14a8ca74304a94791b4e4a1c59b2fbb1d.

- 2026-09-29T05:13:06+00:00: Recorded command exit 0; command argv SHA-256
  de4935b3061b251d99b621a57a775c4761c0e0911d9dbe0263925f702b4e329b.

- 2026-09-29T05:13:22+00:00: Validation: cargo fmt, 5 focused process_owner_material tests, -D
  warnings clippy, and workspace rustdoc -D warnings pass. Full cargo test --locked --workspace had
  one pre-existing parallel control test failure (production_backend... state root already owned);
  exact same test rerun serially with --test-threads=1 passed. No product test failure remains.

- 2026-09-29T05:14:08+00:00: Recorded command exit 0; command argv SHA-256
  7b80382008cb01e3ea6fa6e88054b624464f9801b40ed57f947b01892a686ae8.

- 2026-09-29T05:16:09+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-29T05:16:47+00:00: Recorded command exit 0; command argv SHA-256
  5c8da9b34935360f7399b9d4b260d9a460b442f2f0ca08eddaee6e8f11776ef0.

- 2026-09-29T05:17:30+00:00: Recorded command exit 1; command argv SHA-256
  f58d568a34eb60a2c9a5267b05e608e4ca7e5c9aacda3332e678359769bbfad8.

- 2026-09-29T05:18:13+00:00: Recorded command exit 1; command argv SHA-256
  25b1df8dd63fb1b3a38f5aaeaf898c92fc50712558301926a3cf7fa34df6f648.

- 2026-09-29T05:18:58+00:00: Privacy gate diagnostics: both gitleaks working-tree scans exited 1
  because generated ignored target artifacts matched the repository private-key rule at
  target/debug/deps/libpem-8b69321e2a0b9039.rmeta:71 and
  target/doc/src/asb_control/protocol.rs.html:2317. No introduced source/doc file matched; findings
  are environmental build artifacts, not product authority. Formal cargo test passed.

- 2026-09-29T05:19:11+00:00: Recorded command exit 0; command argv SHA-256
  47a11eb1c45b816c00415363181aa85c2fa29b932224e9de115f41db041dc138.

- 2026-09-29T05:19:57+00:00: Exact narrower missing primitive: no protected-main non-test
  owner/platform adapter accepts ProcessOwnerMaterialLease and mints
  LiveProviderRuntimeHandle/LiveProviderRuntimeDispatchSource. Existing live dispatch constructors
  require RuntimeOwnedEnrollmentSource and crate-private authenticated resolver; converting from
  caller/PATH/config or digest-only records would fabricate authority. AR-1512 therefore does not
  claim live-provider reachability or ordinary live CLI execution; parent should create a successor
  AR for this authenticated lease-to-dispatch bridge.

- 2026-09-29T05:20:12+00:00: Recorded command exit 0; command argv SHA-256
  11d44af8ee7208d7ffbb3592cbffadd9b3afedecd11c366beebcb25778793502.

- 2026-09-29T05:20:40+00:00: Recorded command exit 0; command argv SHA-256
  098c5f8f0cc65de3ffef5239475be95453164710e11616a99e5a9e4dd0074e6f.
