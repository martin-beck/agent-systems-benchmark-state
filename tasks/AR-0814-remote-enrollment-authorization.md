---
{
  "branch": "feature/remote-enrollment-authz",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-16T19:57:22+00:00",
  "depends_on": [
    "AR-0813"
  ],
  "id": "AR-0814",
  "next_action": "Implement noninteractive pairing/identity-store CLI and certificate import; add concurrency/clock-skew/compromised-store tests.",
  "observed_branch": "feature/remote-enrollment-authz",
  "observed_dirty": 0,
  "observed_head": "9d724a58c38fe51b4b9021ebe158773f51b3bf66",
  "owner": "asb_ar0814_enrollment_authz",
  "plan": "../plans/AR-0814.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Provide the ASB protocol and CLI for explicit remote trust and least-privilege roles.",
  "task_revision": 94,
  "title": "Secure remote enrollment and authorization",
  "updated_at": "2026-09-16T18:03:10+00:00",
  "worktree_key": "agent-systems-benchmark-remote-enrollment-authz"
}
---
## AR-0814

Pair remote TUIs with runners using explicit trust and least-privilege roles.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-10T19:20:00+00:00: Removed TUI implementation from this ASB AR. The standalone asb-tui
  enrollment experience belongs to AR-0817 and consumes this protocol.

- 2026-09-16T17:24:41+00:00: AR-0813 completed with signed transport and post-merge gates; promote
  enrollment/authz implementation.

- 2026-09-16T17:24:44+00:00: Claimed by asb_ar0814_enrollment_authz.

- 2026-09-16T17:25:38+00:00: Recorded command exit 0; command argv SHA-256
  a2ed473f94ce905fc478776983cd071465a36de4319a44489aa21fa5c1167fef.

- 2026-09-16T17:37:03+00:00: Heartbeat by asb_ar0814_enrollment_authz.

- 2026-09-16T17:39:01+00:00: Implementation slice added crates/asb-control authorization contract
  and negative tests, but handoffctl run is blocked because worktree is detached while task declares
  feature/remote-enrollment-authz.

- 2026-09-16T17:39:16+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T17:39:26+00:00: Recorded command exit 128; command argv SHA-256
  2ecb99bb17200ad8e4af89880d54b29c8be04fc23f2c03708551098f795d0fa0.

- 2026-09-16T17:39:37+00:00: Recorded command exit 101; command argv SHA-256
  3b10071b991181454b5005b3f28e65547f8a2041e5fcf94f25d3a7c5c91b403d.

- 2026-09-16T17:39:53+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T17:40:05+00:00: Recorded command exit 0; command argv SHA-256
  3b10071b991181454b5005b3f28e65547f8a2041e5fcf94f25d3a7c5c91b403d.

- 2026-09-16T17:40:23+00:00: Recorded command exit 0; command argv SHA-256
  9ed8d8715ce2cf07b12349940db9559587e74f0802f54ac676b98daeee097e9a.

- 2026-09-16T17:40:33+00:00: Recorded command exit 0; command argv SHA-256
  c12fbef4a002881ce694cf23f666fe0f5a7ed7810a5f8ee50e8beabbaad2395d.

- 2026-09-16T17:40:58+00:00: Committed signed+DCO 2d60d70: scoped RemoteRole/RemotePermission matrix
  and AuthorizationContext with principal/request SHA-256, generation, unknown-field and
  least-privilege negative tests. Focused cargo test -p asb-control authorization --lib: 2 passed.

- 2026-09-16T17:41:39+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T17:41:50+00:00: Recorded command exit 0; command argv SHA-256
  3b10071b991181454b5005b3f28e65547f8a2041e5fcf94f25d3a7c5c91b403d.

- 2026-09-16T17:42:00+00:00: Recorded command exit 0; command argv SHA-256
  6ca6f52ea0fe994e58865e0cc7bcf4473092271e9f44b6784e03d8703f2bbdbb.

- 2026-09-16T17:42:09+00:00: Recorded command exit 0; command argv SHA-256
  ee406cb76bfaf49e47fc10593110a825b1ad8f88bd8c75068d0ee3995b45406e.

- 2026-09-16T17:42:26+00:00: Signed+DCO c5a8724 adds permission_for_call/authorize_call wiring for
  every ControlCall plus 3 focused authz tests passing. RemoteRole denies observer mutations and
  operator enrollment/revocation; invalid digests/generation and unknown fields fail closed.

- 2026-09-16T17:43:36+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T17:43:52+00:00: Recorded command exit 0; command argv SHA-256
  b5866e022d875e9dd83f3b6e7d60021d681a05ddc7268cc627364baf73b00b92.

- 2026-09-16T17:44:05+00:00: Recorded command exit 0; command argv SHA-256
  9997b189d9e883a887215648e44e455bff6ea481cc08f230a311aa68e3e95625.

- 2026-09-16T17:44:14+00:00: Recorded command exit 0; command argv SHA-256
  3529dc8001e1fa7ef6b9eb23dbab2ee88f8b3153dcc264f478290e7fae4eb23e.

- 2026-09-16T17:44:31+00:00: Signed+DCO 054b457 adds AuthAuditEventV1 and AuthAuditOperation for
  credential-free enroll/rotate/revoke records. Seven auth tests pass, including secret absence,
  unknown-field rejection, malformed digest rejection, and rotation audit privacy.

- 2026-09-16T17:45:25+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T17:45:44+00:00: Recorded command exit 0; command argv SHA-256
  9cef4c65db0d5a427b20564c632daaf58f51607ebf91717ca77b35037af7f88f.

- 2026-09-16T17:45:55+00:00: Recorded command exit 0; command argv SHA-256
  e274074a17e0682b5edf79b5caca577a41520ed9ca8daf9342f0433b678582a1.

- 2026-09-16T17:46:05+00:00: Recorded command exit 0; command argv SHA-256
  df5d7d2c5e4aa5a1a09fa45e85c56e18bdf2b98d5331bd923f380cda3a88d1b4.

- 2026-09-16T17:46:24+00:00: Signed+DCO 19674fa requires auth CLI operations to provide role,
  principal digest, and request digest; authorize_call rejects insufficient roles before socket
  dispatch. Focused cargo test -p asb-cli auth_dispatch --lib: 2 passed. Worktree clean after
  commit.

- 2026-09-16T17:47:24+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T17:47:37+00:00: Recorded command exit 0; command argv SHA-256
  b5866e022d875e9dd83f3b6e7d60021d681a05ddc7268cc627364baf73b00b92.

- 2026-09-16T17:47:49+00:00: Recorded command exit 0; command argv SHA-256
  9997b189d9e883a887215648e44e455bff6ea481cc08f230a311aa68e3e95625.

- 2026-09-16T17:47:58+00:00: Recorded command exit 0; command argv SHA-256
  b702ab926a9381e8ad2fcf58f539730f68d7f949865e8f730075b6919c2c3eb0.

- 2026-09-16T17:48:20+00:00: Signed+DCO f8714ca adds CertificateIdentityV1 and one-time
  EnrollmentPairingV1. Pairing requires exact out-of-band fingerprint and unexpired code, stores
  only code digest, rejects replay/expiry/malformed identities/unknown fields. Auth suite: 9 passed.

- 2026-09-16T17:49:28+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T17:49:44+00:00: Recorded command exit 101; command argv SHA-256
  b5866e022d875e9dd83f3b6e7d60021d681a05ddc7268cc627364baf73b00b92.

- 2026-09-16T17:50:03+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T17:50:12+00:00: Recorded command exit 0; command argv SHA-256
  f3b9025c86c15695290c925bee6eedd80a643f52f9503e025611e7e79529c43b.

- 2026-09-16T17:50:21+00:00: Recorded command exit 0; command argv SHA-256
  b5866e022d875e9dd83f3b6e7d60021d681a05ddc7268cc627364baf73b00b92.

- 2026-09-16T17:50:32+00:00: Recorded command exit 0; command argv SHA-256
  9997b189d9e883a887215648e44e455bff6ea481cc08f230a311aa68e3e95625.

- 2026-09-16T17:50:41+00:00: Recorded command exit 0; command argv SHA-256
  6aaddede6686d7f2e38723f277d388196babe55eb1d78ec9762715572fa98615.

- 2026-09-16T17:51:02+00:00: Signed+DCO eb0adad adds bounded backup/restore preserving revoked state
  and validate_identity_store: symlink-safe regular file, expected owner, private mode, size bound.
  Auth suite 10/10 passes; initial mode-negative failure was corrected by setting fixture mode 0600.

- 2026-09-16T17:51:52+00:00: Recorded command exit 2; command argv SHA-256
  0ada0ea76b45d8d7103525a6017e2f6c5aff7a57488511d09d63116632acee81.

- 2026-09-16T17:52:03+00:00: Recorded command exit 0; command argv SHA-256
  f397688459a38e4f80675ba6c15f49c359643953df5bb55f9276889f9b20cea0.

- 2026-09-16T17:52:17+00:00: Recorded command exit 0; command argv SHA-256
  9cef4c65db0d5a427b20564c632daaf58f51607ebf91717ca77b35037af7f88f.

- 2026-09-16T17:52:28+00:00: Recorded command exit 0; command argv SHA-256
  6a95732adb87764a692dbe90c0bf0f53bd132a4b35dbf51b46a903b2c6ee6f9b.

- 2026-09-16T17:52:37+00:00: Recorded command exit 0; command argv SHA-256
  8f464360d3700127f84115ec98d050dcd332bf7727935758c8f17773267c2087.

- 2026-09-16T17:52:59+00:00: Signed+DCO 35cffab documents explicit pairing, credential-free
  identity-store rules, and role/principal/request digest CLI ceremony; command metadata now
  requires scoped auth options. Tutorial validator passed and auth dispatch tests 2/2 passed.
  Worktree clean.

- 2026-09-16T17:53:33+00:00: Recorded command exit 101; command argv SHA-256
  12938f82fbaa9857db28f5434d0af3e082e02e4471a57c1807c2e82d77a69772.

- 2026-09-16T17:54:04+00:00: Recorded command exit 0; command argv SHA-256
  68313d5befaff129077c212efae4701220b7fd1195996ed216e00aa0a57a1e05.

- 2026-09-16T17:54:15+00:00: Recorded command exit 0; command argv SHA-256
  a5e91d8a6e356ba88fd4835c765ebd2411c75eacaa60f98e203295ec257bd3a5.

- 2026-09-16T17:54:25+00:00: Recorded command exit 0; command argv SHA-256
  aa5f5034c24d8c6ccfd324cb29de171c0f826ad5a4d5dbadc73199c02b0a9256.

- 2026-09-16T17:54:47+00:00: Recorded command exit 0; command argv SHA-256
  341e312c0532aa0e4f137a3f94aeabe37c46a8bbe85b57fa8e25dbf3ab2888c8.

- 2026-09-16T17:55:26+00:00: Recorded command exit 0; command argv SHA-256
  12938f82fbaa9857db28f5434d0af3e082e02e4471a57c1807c2e82d77a69772.

- 2026-09-16T17:55:53+00:00: Full cargo test --workspace --locked passed after refreshing CLI
  provenance digest in signed+DCO 1f9c36a; previous workflow_transcript provenance failure is fixed
  and focused provenance test passed. Workspace clean. cargo clippy --workspace --all-targets
  --locked -D warnings also passed.

- 2026-09-16T17:57:22+00:00: Heartbeat by asb_ar0814_enrollment_authz.

- 2026-09-16T17:57:38+00:00: Independent review of exact signed/DCO head
  1f9c36aad338849bfdbbb9922bd2a2efa72e00fa found useful metadata-only enrollment, explicit pairing
  state, role matrix, generation-fenced probes, rotate rollback, backup/restore revocation,
  mode/owner/symlink checks, audit schema, docs and CLI auth request changes. Publication remains
  blocked against complete AR-0814 plan: no actual certificate issuance/import or non-interactive
  pairing/identity-store CLI ceremony is implemented; CLI only emits typed auth control requests.
  Authorization mapping returns None for AgentStatus (and Negotiate), so AgentStatus bypasses
  context validation/role binding if dispatched remotely. No concrete concurrent rotation,
  stolen/expired/not-yet-valid/wrong-IP certificate, role-escalation/confused-deputy, clock-skew,
  audit-tamper, compromised-permission, lost-controller or break-glass recovery tests/evidence.
  is_sha256 accepts uppercase hex rather than canonical lowercase digest format. SecretBackend is
  only an abstract caller contract; no qualified OS secret reference implementation is present.
  Existing focused auth tests cover basic positive/negative metadata/pairing/rollback, but not the
  full threat matrix. Head clean SSH-signed/DCO and no private values observed; no PR/publication
  authorization.

- 2026-09-16T17:58:39+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T17:58:51+00:00: Recorded command exit 1; command argv SHA-256
  f4f80ba5c0c1f646518b392e465d25b575d9c30f3d6c9e11695c986f7ed04fac.

- 2026-09-16T17:59:10+00:00: Recorded command exit 0; command argv SHA-256
  b5866e022d875e9dd83f3b6e7d60021d681a05ddc7268cc627364baf73b00b92.

- 2026-09-16T17:59:19+00:00: Recorded command exit 0; command argv SHA-256
  3b10071b991181454b5005b3f28e65547f8a2041e5fcf94f25d3a7c5c91b403d.

- 2026-09-16T17:59:31+00:00: Recorded command exit 0; command argv SHA-256
  d87779fb9685060aa71cc551be1ba8eb6d8761164e5931c7683a5b486214292a.

- 2026-09-16T17:59:41+00:00: Recorded command exit 0; command argv SHA-256
  adbf37501395da49acbb02927c8c59bc159c772b815b797c0aa451c6049d0f65.

- 2026-09-16T18:00:03+00:00: Signed+DCO 947abad enforces canonical lowercase SHA-256 digests in
  control/auth and adds certificate validity/route metadata to pairing; confirmation fails closed
  before validity windows and replay. Auth 10/10 and control authz 3/3 passed. One combined cargo
  test invocation failed due invalid multiple TESTNAME syntax; rerun separately succeeded.

- 2026-09-16T18:01:31+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T18:01:41+00:00: Recorded command exit 1; command argv SHA-256
  f4f80ba5c0c1f646518b392e465d25b575d9c30f3d6c9e11695c986f7ed04fac.

- 2026-09-16T18:01:52+00:00: Recorded command exit 0; command argv SHA-256
  b5866e022d875e9dd83f3b6e7d60021d681a05ddc7268cc627364baf73b00b92.

- 2026-09-16T18:02:11+00:00: Recorded command exit 101; command argv SHA-256
  3b10071b991181454b5005b3f28e65547f8a2041e5fcf94f25d3a7c5c91b403d.

- 2026-09-16T18:02:31+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T18:02:40+00:00: Recorded command exit 0; command argv SHA-256
  3b10071b991181454b5005b3f28e65547f8a2041e5fcf94f25d3a7c5c91b403d.

- 2026-09-16T18:02:53+00:00: Recorded command exit 0; command argv SHA-256
  d87779fb9685060aa71cc551be1ba8eb6d8761164e5931c7683a5b486214292a.

- 2026-09-16T18:03:02+00:00: Recorded command exit 0; command argv SHA-256
  b1dc30ee9016c885fb36d80a5ecec9acd5c0f77d356b9b1e1e80b3eb59919ccb.
