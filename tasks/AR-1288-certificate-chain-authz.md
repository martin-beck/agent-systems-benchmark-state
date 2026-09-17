---
{
  "branch": "feature/ar-1288-certificate-chain-authz",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T04:44:31+00:00",
  "depends_on": [
    "AR-0813"
  ],
  "id": "AR-1288",
  "next_action": "Formal lockfile is regenerated locally for the x509-parser dependency and formal locked tests compile; one formal artifact-acquisition test failed with environment-level Os code 26 ExecutableFileBusy at tests/tla_artifact_acquisition.rs:488. Commit the lockfile as signed/DCO, then run bounded reruns to classify that unrelated flake before pushing and restarting hosted exact-head checks.",
  "observed_branch": "feature/ar-1288-certificate-chain-authz",
  "observed_dirty": 1,
  "observed_head": "ddcd51b8a4add9d24e1738c771ead956348e4071",
  "owner": "asb_ar0909_lifecycle_repair",
  "plan": "../plans/AR-1288.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Implement runtime-owned certificate issuance and trust-chain validation required by AR-0814.",
  "task_revision": 117,
  "title": "Runtime certificate issuance and chain validation",
  "updated_at": "2026-09-17T03:16:34+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1288-certificate-chain-authz"
}
---
## AR-1288

AR-0814 completed the versioned remote authorization and pairing boundary but identified
certificate issuance, chain validation and trusted route/ancestor authority as a separate gap.
This ASB-only successor supplies that missing cryptographic boundary. It must preserve offline,
fail-closed operation and must not add frontend or TUI behavior.

The implementation owns only the runtime/control certificate and identity boundary, its CLI
argument contract, schemas/docs and tests. It must be based on protected main after AR-0813 and
must not reuse unmerged strict-replay or asb-tui branches.

- 2026-09-17T02:38:44+00:00: Successor for AR-0814 certificate issuance/chain validation gap;
  depends only on completed AR-0813.

- 2026-09-17T02:38:57+00:00: Claimed by asb_ar1024_lifecycle_router.

- 2026-09-17T02:39:08+00:00: Recorded command exit 0; command argv SHA-256
  5345cd4b5f66285dc80cddfe59c0a95475263f9ff88d25d2639fce3c300aa4b9.

- 2026-09-17T02:39:17+00:00: Recorded command exit 0; command argv SHA-256
  6c4940135c92371beee28615245f86edc4d7dae2dad156fadbeaa902b8a810a7.

- 2026-09-17T02:39:29+00:00: Heartbeat by asb_ar1024_lifecycle_router.

- 2026-09-17T02:39:55+00:00: Recorded command exit 0; command argv SHA-256
  23dc22c9358e3e2c16429023094116bc45a8280a9071b7bcf9ba8d34828cccb8.

- 2026-09-17T02:40:11+00:00: Claimed AR-1288 after durable plan/task commit 111154ede and
  promotion/open transition. Isolated worktree created from origin/main 2fd90557. Read complete
  AR-0814/plan and product DEVELOPMENT, ARCHITECTURE, QUALITY docs. Baseline cargo test --locked -p
  asb-control --lib passes 51/51. Existing asb-control has mTLS frame transport,
  AuthEnroll/rotate/revoke and pairing identity contracts but no certificate
  issuance/chain-validation module, confirming successor scope.

- 2026-09-17T02:44:08+00:00: Worker stopped after baseline setup without implementation; preserve
  baseline evidence and reopen ownerless for reassignment.

- 2026-09-17T02:44:31+00:00: Claimed by asb_ar0909_lifecycle_repair.

- 2026-09-17T02:46:13+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-17T02:46:26+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-17T02:46:45+00:00: Recorded command exit 0; command argv SHA-256
  caa10c78e9f7d2e8bf938e9a6c752480e10577c3b0a48ff54cc4eb728976d1da.

- 2026-09-17T02:47:21+00:00: Recorded command exit 101; command argv SHA-256
  caa10c78e9f7d2e8bf938e9a6c752480e10577c3b0a48ff54cc4eb728976d1da.

- 2026-09-17T02:47:55+00:00: Recorded command exit 0; command argv SHA-256
  caa10c78e9f7d2e8bf938e9a6c752480e10577c3b0a48ff54cc4eb728976d1da.

- 2026-09-17T02:48:11+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-17T02:48:23+00:00: Recorded command exit 101; command argv SHA-256
  959e4e8767eb23b08b444bb2129a747f0d9389f0c98a65551178b55e44528c65.

- 2026-09-17T02:48:37+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-17T02:48:48+00:00: Recorded command exit 101; command argv SHA-256
  959e4e8767eb23b08b444bb2129a747f0d9389f0c98a65551178b55e44528c65.

- 2026-09-17T02:49:12+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-17T02:49:24+00:00: Recorded command exit 0; command argv SHA-256
  959e4e8767eb23b08b444bb2129a747f0d9389f0c98a65551178b55e44528c65.

- 2026-09-17T02:49:33+00:00: Recorded command exit 0; command argv SHA-256
  caa10c78e9f7d2e8bf938e9a6c752480e10577c3b0a48ff54cc4eb728976d1da.

- 2026-09-17T02:50:17+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-17T02:50:28+00:00: Recorded command exit 0; command argv SHA-256
  ce97a41f4d7af387b4faad0770c52c7588ec07d2333884acd1616eedebf90bba.

- 2026-09-17T02:51:27+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-17T02:51:38+00:00: Recorded command exit 0; command argv SHA-256
  959e4e8767eb23b08b444bb2129a747f0d9389f0c98a65551178b55e44528c65.

- 2026-09-17T02:51:48+00:00: Recorded command exit 0; command argv SHA-256
  caa10c78e9f7d2e8bf938e9a6c752480e10577c3b0a48ff54cc4eb728976d1da.

- 2026-09-17T02:51:57+00:00: Recorded command exit 0; command argv SHA-256
  bea894a67ff505e3a430353fe2c508a96067766b877641a6b591d27d6de77f24.

- 2026-09-17T02:52:07+00:00: Recorded command exit 0; command argv SHA-256
  d88888b0dc3c5116c983f4e605fd0d86de2d7fa9e5a28273ef0be9db78a563be.

- 2026-09-17T02:52:50+00:00: 2026-09-17T02:54:00+00:00: Reconciled inherited dirty
  certificate.rs/lib.rs slice without reset. Added CertificateAuthorityV1::with_trust_anchor and
  issue_der using pinned RootCertStore/WebPkiClientVerifier; added positive actual DER root/leaf
  validation and negatives for missing anchor, digest mismatch, schema/generation/role/issuer/chain
  bounds; documented offline no-fallback certificate boundary in docs/AUTH_ENROLLMENT.md. Product
  commit 871d2f7ee4ae13108510c9bf2c7baa45627473f2 is SSH-signed by Martin Beck and has matching
  Signed-off-by. cargo test --locked -p asb-control --lib: 56/56 passed.

- 2026-09-17T02:52:59+00:00: Recorded command exit 0; command argv SHA-256
  84b337450e1940a3484de7020a0103bfe0d26b27f5478cf84ea4798eeff1c8fe.

- 2026-09-17T02:53:10+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-17T02:55:02+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-17T02:55:12+00:00: Recorded command exit 101; command argv SHA-256
  959e4e8767eb23b08b444bb2129a747f0d9389f0c98a65551178b55e44528c65.

- 2026-09-17T02:55:22+00:00: Recorded command exit 0; command argv SHA-256
  503960e7a61c6dfb6e654fd3c59faa89ec2e3eed4ff36d3c0c46c574f8f914d9.

- 2026-09-17T02:55:52+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-17T02:56:09+00:00: Recorded command exit 101; command argv SHA-256
  bfa4a0ffe43ae2c41fc3fa1182d10710d731bd5af663fee94864472aec1bdfdc.

- 2026-09-17T02:56:35+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-17T02:56:49+00:00: Recorded command exit 0; command argv SHA-256
  d51697e0d4b9dcc6acae7f106c6994942ef830f5d0452a5681b4c33b8104afe2.

- 2026-09-17T02:57:02+00:00: Recorded command exit 0; command argv SHA-256
  bfa4a0ffe43ae2c41fc3fa1182d10710d731bd5af663fee94864472aec1bdfdc.

- 2026-09-17T02:57:11+00:00: Recorded command exit 0; command argv SHA-256
  caa10c78e9f7d2e8bf938e9a6c752480e10577c3b0a48ff54cc4eb728976d1da.

- 2026-09-17T02:57:35+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-17T02:57:45+00:00: Recorded command exit 101; command argv SHA-256
  bfa4a0ffe43ae2c41fc3fa1182d10710d731bd5af663fee94864472aec1bdfdc.

- 2026-09-17T02:58:10+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-17T02:58:20+00:00: Recorded command exit 0; command argv SHA-256
  bfa4a0ffe43ae2c41fc3fa1182d10710d731bd5af663fee94864472aec1bdfdc.

- 2026-09-17T02:58:29+00:00: Recorded command exit 0; command argv SHA-256
  c6e7355fccbe94b8a2213a282e9e1be3a2195bc5f0d7fada474a1134d49ec56f.

- 2026-09-17T02:58:37+00:00: Recorded command exit 0; command argv SHA-256
  c6e7355fccbe94b8a2213a282e9e1be3a2195bc5f0d7fada474a1134d49ec56f.

- 2026-09-17T02:58:50+00:00: Recorded command exit 0; command argv SHA-256
  d6e12e726b2046e11718ea13d259f1dda00c2f7801cd8b746185b406abd82be0.

- 2026-09-17T02:59:00+00:00: Recorded command exit 0; command argv SHA-256
  05644ec977d998527b29c66ce42c84946e69fd18d6f9b5a0325ba6f9885c495e.

- 2026-09-17T02:59:12+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-17T03:00:02+00:00: Recorded command exit 0; command argv SHA-256
  d82821188d7e3bfddcef4c278c2926db944f5c0368b12b0b83bca9598e00146d.

- 2026-09-17T03:00:24+00:00: Recorded command exit 0; command argv SHA-256
  6bfc5d45a7fb31ac26de9cb54b5ebeb67a6d9d6dee784b5fb6096c25e78b6989.

- 2026-09-17T03:00:43+00:00: 2026-09-17T03:01:00+00:00: Addressed review blockers. Removed public
  metadata-only issue path; metadata validation is private and authorization requires issue_der.
  Added x509-parser DER subject binding, exact intermediate digest/order checks, endpoint authority
  binding, race-safe generation revocation, unknown-field negative, generated schema artifact, and
  Cargo.lock dependency pin. Gate evidence: cargo fmt --all -- --check passed; cargo test --offline
  --locked --workspace passed; cargo clippy --offline --locked --workspace --all-targets -- -D
  warnings passed; certificate-focused tests 7/7 passed. Product head
  01bf266e0d86e0f3bdb676aeb0fef32e9116f75d is clean, SSH-signed, with matching DCO.

- 2026-09-17T03:00:52+00:00: Recorded command exit 0; command argv SHA-256
  84b337450e1940a3484de7020a0103bfe0d26b27f5478cf84ea4798eeff1c8fe.

- 2026-09-17T03:01:32+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-17T03:01:44+00:00: Recorded command exit 0; command argv SHA-256
  d51697e0d4b9dcc6acae7f106c6994942ef830f5d0452a5681b4c33b8104afe2.

- 2026-09-17T03:01:56+00:00: Recorded command exit 0; command argv SHA-256
  bfa4a0ffe43ae2c41fc3fa1182d10710d731bd5af663fee94864472aec1bdfdc.

- 2026-09-17T03:02:18+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-17T03:02:30+00:00: Recorded command exit 0; command argv SHA-256
  bfa4a0ffe43ae2c41fc3fa1182d10710d731bd5af663fee94864472aec1bdfdc.

- 2026-09-17T03:02:39+00:00: Recorded command exit 0; command argv SHA-256
  c6e7355fccbe94b8a2213a282e9e1be3a2195bc5f0d7fada474a1134d49ec56f.

- 2026-09-17T03:02:53+00:00: Recorded command exit 0; command argv SHA-256
  3a9009e13e74c05055ffe95abcd80fd3a8443fd0927533c544bac0dba96052ad.

- 2026-09-17T03:03:02+00:00: Recorded command exit 0; command argv SHA-256
  287304f381381f96de81ce5725aba320bc4fd4ab8432b8b35326bd6de8ffda38.

- 2026-09-17T03:03:22+00:00: 2026-09-17T03:04:00+00:00: Addressed re-review schema blocker.
  Postprocessed certificate_identity_schema and regenerated
  crates/asb-control/schema/v1/certificate-identity.schema.json; added unit assertions for digest
  pattern, schema const, generation minimum, role enum and deny_unknown_fields. cargo fmt check,
  cargo test --offline --locked -p asb-control --lib certificate (7/7), cargo clippy --offline
  --locked -p asb-control --lib -- -D warnings, full workspace tests and workspace Clippy had passed
  before this schema-only checkpoint. Product commit 35c49a90e0f6d034becdce88551622407fe0ed6f is
  SSH-signed with matching DCO and worktree clean.

- 2026-09-17T03:03:30+00:00: Recorded command exit 0; command argv SHA-256
  84b337450e1940a3484de7020a0103bfe0d26b27f5478cf84ea4798eeff1c8fe.

- 2026-09-17T03:04:48+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-17T03:05:29+00:00: Recorded command exit 0; command argv SHA-256
  d82821188d7e3bfddcef4c278c2926db944f5c0368b12b0b83bca9598e00146d.

- 2026-09-17T03:05:39+00:00: Recorded command exit 0; command argv SHA-256
  6bfc5d45a7fb31ac26de9cb54b5ebeb67a6d9d6dee784b5fb6096c25e78b6989.

- 2026-09-17T03:05:49+00:00: Recorded command exit 0; command argv SHA-256
  907b1b1f743859290d1b107a1971b1dbf4bfaf02a4014ca1961d94cfbbf81467.

- 2026-09-17T03:05:58+00:00: Recorded command exit 0; command argv SHA-256
  6ea19b7d53348bc9ff61279312eb46b3aed5b15de79e7b4cb454b75c8e842445.

- 2026-09-17T03:06:17+00:00: 2026-09-17T03:07:00+00:00: Fresh post-35c49a9 gates completed at exact
  source before this signed validity-bound checkpoint: cargo fmt --all -- --check passed; cargo test
  --offline --locked --workspace passed; cargo clippy --offline --locked --workspace --all-targets
  -- -D warnings passed. Runtime now rejects not_before/not_after=0 to match generated schema
  minimum=1. Product commit 0e8d7e2b23bde802b7ce793654915e886d6432f is SSH-signed with matching DCO;
  worktree clean.

- 2026-09-17T03:06:25+00:00: Recorded command exit 0; command argv SHA-256
  84b337450e1940a3484de7020a0103bfe0d26b27f5478cf84ea4798eeff1c8fe.

- 2026-09-17T03:06:39+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-17T03:07:18+00:00: Recorded command exit 0; command argv SHA-256
  d82821188d7e3bfddcef4c278c2926db944f5c0368b12b0b83bca9598e00146d.

- 2026-09-17T03:07:27+00:00: Recorded command exit 0; command argv SHA-256
  6bfc5d45a7fb31ac26de9cb54b5ebeb67a6d9d6dee784b5fb6096c25e78b6989.

- 2026-09-17T03:07:42+00:00: 2026-09-17T03:09:00+00:00: Re-ran fresh gates after validity commit at
  exact source head 0e8d7e2: cargo fmt --all -- --check passed; cargo test --offline --locked
  --workspace passed; cargo clippy --offline --locked --workspace --all-targets -- -D warnings
  passed. Existing generated schema parity and certificate-focused 7/7 remain green. Product
  worktree clean; branch origin/feature/ar-1288-certificate-chain-authz is at
  0e8d7e2b23bde802b7ce793654915e886d6432f4, SSH-signed with matching DCO.

- 2026-09-17T03:07:52+00:00: Recorded command exit 0; command argv SHA-256
  054cdd4d699111534bad3aa816c59705350fb78ad734b3c8771c5d017fa83e06.

- 2026-09-17T03:08:06+00:00: Recorded command exit 0; command argv SHA-256
  26cc1dd7aae8841577fdecd21a2dbc446beb5f256e099acc1266ec64851bcf4a.

- 2026-09-17T03:08:43+00:00: Recorded command exit 1; command argv SHA-256
  716e2e5b63c2f4eb5e30af6cff94f0abca16e67dbd7607fa44a2c01d915e2439.

- 2026-09-17T03:09:01+00:00: Recorded command exit 1; command argv SHA-256
  3e418894af293038af35d88a47855c9f2ae32acb67aebe511cd2c8bf81f915c7.

- 2026-09-17T03:09:12+00:00: Recorded command exit 0; command argv SHA-256
  9abaa616c480bc5811ed65e78827312a044da11c162c2945ce4f74c787ee8124.

- 2026-09-17T03:09:55+00:00: Recorded command exit 0; command argv SHA-256
  5cd7f7ecbd072b19f8bcf922677100f3be60e4ce8a4254b8d6fd3e991baa2b30.

- 2026-09-17T03:10:12+00:00: Recorded command exit 0; command argv SHA-256
  f01dab862dadd50a1ec23716b6a9a6b966d6fd3e844bfc03b6f735fce76b9812.

- 2026-09-17T03:10:22+00:00: Recorded command exit 0; command argv SHA-256
  e78a27b97801662361857b65185077f60567a9e040a59c6e4f0628e3fd41f165.

- 2026-09-17T03:10:42+00:00: Recorded command exit 0; command argv SHA-256
  84b337450e1940a3484de7020a0103bfe0d26b27f5478cf84ea4798eeff1c8fe.

- 2026-09-17T03:10:52+00:00: Recorded command exit 1; command argv SHA-256
  6b029267d3d9308e476186fa74dff09d01f3a7a57017293795b3177dfbf11d4d.

- 2026-09-17T03:11:26+00:00: Recorded command exit 0; command argv SHA-256
  b927f334bf6974a9084049de639ecf53e555468e86c96b20c8045a92d516750b.

- 2026-09-17T03:12:42+00:00: Checkpoint ddcd51b: added
  crates/asb-control/fixtures/v1/certificate-identity.json, registered control.certificate-identity
  with asb-control/schema_conformance in contracts/v1/catalog.json, regenerated
  docs/CONTRACT_CATALOG.md. contract_consistency.py --run-tests passed all registered suites; exact
  signed/DCO tree clean and pushed. Prior failed baseline command used truncated OID 2fd90557; no
  product impact.

- 2026-09-17T03:12:55+00:00: Recorded command exit 0; command argv SHA-256
  bc2639e62cf73b8578695431ab4e66182e33ad3cdafce79b995f9d067a4c42da.

- 2026-09-17T03:13:12+00:00: Recorded command exit 1; command argv SHA-256
  ab32bf08724c94458d9eb3cc35632b6cc1b8726f1169e0414a7b7d2d5c152ea9.

- 2026-09-17T03:13:41+00:00: Recorded command exit 0; command argv SHA-256
  3850ed6607af06f6eb8a081e22fdefb9054dd14d1d9767b045d9d51a50e5a614.

- 2026-09-17T03:13:56+00:00: Recorded command exit 1; command argv SHA-256
  2979dba784a562806f3f5a79d016f3ad56f97b4964d6dfaaa669b91e24bab5a1.

- 2026-09-17T03:14:15+00:00: Recorded command exit 1; command argv SHA-256
  d4932675ae8a1b66c4b1d33bdb08216044c66bf576d2057cf6d72ea75c5e6064.

- 2026-09-17T03:14:36+00:00: Recorded command exit 0; command argv SHA-256
  5895edb97ae6454ec0ca8511e6392fc3eea748723fdcf2c77303e4edd87c4dc8.

- 2026-09-17T03:15:04+00:00: Recorded command exit 0; command argv SHA-256
  ab32bf08724c94458d9eb3cc35632b6cc1b8726f1169e0414a7b7d2d5c152ea9.

- 2026-09-17T03:15:23+00:00: Recorded command exit 0; command argv SHA-256
  133df7aa8f38e0367c8f4c605deb2c299d48ac0196e7119b5e302bc89f638f31.

- 2026-09-17T03:16:03+00:00: Recorded command exit 101; command argv SHA-256
  2454f3f6af3945b054005131066740ddd2a9a140a723ea4d684fd0538c3cf4bb.

- 2026-09-17T03:16:26+00:00: Diagnosis: hosted Loom job 105061425019 failed because
  formal/Cargo.lock was stale and cargo --locked attempted to update it. Offline cargo
  generate-lockfile added x509-parser transitive entries. The exact locked formal run compiled and
  passed all suites except concurrent_acquisition_converges_on_one_verified_output, which failed at
  start_first_acquisition with Os code 26 ExecutableFileBusy (Text file busy), not certificate code.
  Worktree intentionally dirty only formal/Cargo.lock pending signed commit.

- 2026-09-17T03:16:34+00:00: Recorded command exit 0; command argv SHA-256
  18bd4aff9a09c3fb87a532f0a7fcc2d0fe00607e496aacf84775e9e758436f78.
