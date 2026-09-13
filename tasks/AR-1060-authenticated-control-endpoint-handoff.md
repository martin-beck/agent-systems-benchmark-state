---
{
  "branch": "feature/authenticated-control-endpoint-handoff",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-13T20:06:32+00:00",
  "depends_on": [
    "AR-1022",
    "AR-1023"
  ],
  "id": "AR-1060",
  "next_action": "Obtain independent immutable review of signed ASB head e55df62c4247ca86b6af863c75e189980fadd9fe, then add the bounded router-side probe/acquisition producer and remaining hostile descriptor, credential, timeout and admission tests without UI work.",
  "observed_branch": "feature/authenticated-control-endpoint-handoff",
  "observed_dirty": 0,
  "observed_head": "1c51cbf5a14b007fbb3881b7fb4604e9db35c305",
  "owner": "codex-ar1060-endpoint-recovery-20260913",
  "plan": "../plans/AR-1060.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Hand the standalone frontend an authenticated ASB control connection without exposing endpoint paths.",
  "task_revision": 83,
  "title": "Add authenticated control endpoint handoff",
  "updated_at": "2026-09-13T17:52:29+00:00",
  "worktree_key": "agent-systems-benchmark-authenticated-control-endpoint-handoff"
}
---

Define and implement the non-UI boundary that connects the separately installed `asb-tui` frontend
to the authoritative ASB control service. ASB owns endpoint discovery, connection provisioning and
reconnection authority. The standalone repository owns transport consumption and independent peer
re-authentication. Prefer a safely transferred, already-connected Unix descriptor; never disclose
raw socket paths or endpoints through environment variables, arguments, public responses, logs or
diagnostics.

This AR coordinates two repository-local implementation halves with separate commits, tests,
immutable reviews and protected merges. It assigns no renderer, Ratatui, Crossterm, navigation,
widget, screen or application-shell implementation to ASB. AR-1024 remains open and AR-1025 remains
planned until their full dependency sets are done.

- 2026-09-11T05:28:38+00:00: Created under the coordinator lock after confirming AR-1060 is the
  next free identifier. AR-1022 and AR-1023 are durably done; AR-1024 and AR-1025 retain their
  existing status and owner while gaining this prerequisite.

- 2026-09-11T05:28:38+00:00: Claimed by
  codex-ar1060-control-endpoint-handoff-state-20260911 for state-only task definition and graph
  validation; release OPEN/unowned after the signed state commit.

- 2026-09-11T05:32:00+00:00: Initial schema command exited 1 because the base Python environment
  lacks `jsonschema`; its automatic result reconciliation then detected the concurrently committed
  duplicate AR-1060 node. Preserved that commit in history, removed only its colliding task in this
  authorized successor, and restored AR-1010 byte-for-byte to origin/main so its dependency does not
  point at this unrelated endpoint-handoff task.

- 2026-09-11T05:32:22+00:00: Recorded command exit 1; command argv SHA-256
  f42ab07ce4e4d1a4d356a15458f58b78063c28c29356959d63aadf8968d17b7a.

- 2026-09-11T05:32:55+00:00: Recorded command exit 0; command argv SHA-256
  3adf945d41e31464bc901f1cb355cd00146cd5cb01e2faa01ac63df19394e675.

- 2026-09-11T05:33:14+00:00: Recorded command exit 0; command argv SHA-256
  87414d9a6590bb528ce5f6f01fce65456f2534893bc171d39be2cbd41c120d17.

- 2026-09-11T05:33:31+00:00: Recorded command exit 0; command argv SHA-256
  2a5f18a018eac4703aa065a1484ea3190893d02da0a4a6cf358510cff78afa0c.

- 2026-09-11T05:33:52+00:00: Recorded command exit 0; command argv SHA-256
  c4a330b7ccefa4b6288c65da978caef1065aa1fb108be3ca3156284cafbdd15f.

- 2026-09-11T05:34:20+00:00: Recorded command exit 1; command argv SHA-256
  5769dcc760f79949f509a5b6662af5819e2f3255176c0e792023b37fefd4f716.

- 2026-09-11T05:34:39+00:00: Classified the latest exit 1 as the expected zero-match result from the
  privacy scan: no private checkout path, host/address, password, credential assignment or token
  assignment appears in the six owned task/plan files. Earlier full schema validation also exposed
  only pre-existing repository-wide checkpoint and AR-1043 next_action violations; targeted strict
  schema validation of AR-1024, AR-1025 and AR-1060 passed.

- 2026-09-11T05:35:04+00:00: State-only AR definition complete. AR-1060 is the P0 non-UI
  cross-repository contract; it depends only on done AR-1022/AR-1023. AR-1024 remains OPEN/unowned
  and AR-1025 remains PLANNED/unowned, both with one-way AR-1060 dependencies. Unique-ID, targeted
  strict schema, graph/render, privacy, reconcile and live doctor checks passed; implementation
  awaits a separately claimed worker and repository-local immutable reviews.

- 2026-09-11T05:36:18+00:00: Claimed by codex-ar1060-asb-endpoint-provider-20260911.

- 2026-09-11T05:36:37+00:00: Recorded command exit 0; command argv SHA-256
  6a50527cfbf9c1b1a7134978d79d1c1d487a995e9ac4a7df2ae767403992cd6f.

- 2026-09-11T05:46:24+00:00: Recorded command exit 1; command argv SHA-256
  b30530402bd8595b97dc1d6ae429774e1a0d1619552ef474bb8ce31a1a724450.

- 2026-09-11T05:50:32+00:00: Recorded command exit 0; command argv SHA-256
  f863cdeb4914ccf6c503db659344a2a79b87e1d9ed0b1e744ddcd14ea2e2bef4.

- 2026-09-11T05:50:50+00:00: Recorded command exit 0; command argv SHA-256
  49723ec677ff4d68e7414ff3e327399d50b4aeb6f504a404c432ec5a0bbfc70f.

- 2026-09-11T05:51:10+00:00: Recorded command exit 0; command argv SHA-256
  5e5ffc5446b96baebf2bdd9959d49e029211155440bf2076151c1897c9029dfc.

- 2026-09-11T05:51:33+00:00: Pre-freeze review incorporated before product mutation. Removed unsafe
  arbitrary fixed-FD adoption, CLOEXEC clearing, proc-fd socket reopening, socketpair peer-identity
  claims, PID authority/signaling, launch-command acceptance and application continuity ownership.
  Froze child-stdin SOCK_SEQPACKET possession authority, exact request/reply plus one SCM_RIGHTS
  descriptor, monotonic deadlines/retry ceilings, probe negotiation plus a second
  same-UID/PID/starttime unnegotiated stream, typed AuthenticatedGeneration and post-adoption
  validator seam, receiver shape/CMSG_CLOEXEC checks, explicit epoch/sequence no-wrap ordering and
  changed-runner behavior owned by AR-1025. Product worktree is clean at 10a353e.

- 2026-09-11T05:51:40+00:00: Recorded command exit 0; command argv SHA-256
  2a5f18a018eac4703aa065a1484ea3190893d02da0a4a6cf358510cff78afa0c.

- 2026-09-11T05:56:18+00:00: Recorded command exit 0; command argv SHA-256
  49723ec677ff4d68e7414ff3e327399d50b4aeb6f504a404c432ec5a0bbfc70f.

- 2026-09-11T05:56:30+00:00: Recorded command exit 0; command argv SHA-256
  c5b9bd47d141c50b39e7edb2f72d51e1fd374eebafb3f6379c9433a204406bf7.

- 2026-09-11T06:02:18+00:00: Recorded command exit 0; command argv SHA-256
  49723ec677ff4d68e7414ff3e327399d50b4aeb6f504a404c432ec5a0bbfc70f.

- 2026-09-11T06:02:29+00:00: Recorded command exit 0; command argv SHA-256
  aa32636537833523d1d90645bb31f0e027e1caa1b4c46c6e4e5a4fb8d03f2a40.

- 2026-09-11T06:03:43+00:00: Recorded command exit 0; command argv SHA-256
  49723ec677ff4d68e7414ff3e327399d50b4aeb6f504a404c432ec5a0bbfc70f.

- 2026-09-11T06:03:58+00:00: Recorded command exit 0; command argv SHA-256
  bcf8bf31eb1629894c362b64e10649b4abe94fff852f76f65c9cd028cf263630.

- 2026-09-13T16:56:38+00:00: Recovered expired claim formerly owned by
  codex-ar1060-asb-endpoint-provider-20260911. Recovered expired claim after live audit: declared
  worktree is clean with no implementation and no live ASB worker process; dependency is available
  for a fresh owner.

- 2026-09-13T16:57:08+00:00: Claimed by codex-ar1060-asb-provider-20260913-router.

- 2026-09-13T17:04:54+00:00: Released after interruption before any product edit; secondary-worktree
  wrapper binding must be resolved before a fresh claim.

- 2026-09-13T17:06:32+00:00: Claimed by codex-ar1060-endpoint-recovery-20260913.

- 2026-09-13T17:06:41+00:00: Recorded command exit 0; command argv SHA-256
  a1159e9df3670d549d04524532629f5477ceb7deec9b45e47e8c009506ecb2c8.

- 2026-09-13T17:25:34+00:00: Recorded command exit 0; command argv SHA-256
  6aec7973b37e744e8b1f2ad9682c7624e2883edd88870316279359f045dd3e72.

- 2026-09-13T17:25:53+00:00: Recorded command exit 101; command argv SHA-256
  a9ce49895bddb8cb680a6bad276c1c6123448110d35b0b3321ece1a333d3514a.

- 2026-09-13T17:26:24+00:00: Recorded command exit 0; command argv SHA-256
  3af69be74bd6db6ac0939591ee3ad2a8eadc5b0606637e373cb4f3191626ceae.

- 2026-09-13T17:26:39+00:00: Recorded command exit 0; command argv SHA-256
  a9ce49895bddb8cb680a6bad276c1c6123448110d35b0b3321ece1a333d3514a.

- 2026-09-13T17:28:02+00:00: Recorded command exit 0; command argv SHA-256
  547926b4c31394954d97bb8bce52f2c68bc9289b504d2698e1fefb106985d4ed.

- 2026-09-13T17:28:17+00:00: Recorded command exit 101; command argv SHA-256
  7c87e07ba2e42631912127337bb4dd466725d2dfa34fe843ed5cf5f07ad57005.

- 2026-09-13T17:28:46+00:00: Recorded command exit 0; command argv SHA-256
  7a1fcaf9b5fa14886f46e01a944be2ce5394210caaac0f3e749ecce125b43f24.

- 2026-09-13T17:29:52+00:00: Recorded command exit 0; command argv SHA-256
  a6d83f397502e732af49be9e8ceae0d1028f45fcbd5fe630b8ffae8ce65374a8.

- 2026-09-13T17:30:06+00:00: Recorded command exit 0; command argv SHA-256
  2d4e10c66ed94b28fdc4171373d809e3fcc83998141c89afc9d78549fd4b90de.

- 2026-09-13T17:30:21+00:00: Recorded command exit 0; command argv SHA-256
  00384dba6676d16a99a5ae96a607ded315dcafbe5606e3a070191e7404b62c53.

- 2026-09-13T17:30:59+00:00: Recorded command exit 0; command argv SHA-256
  98a0fdf463a9f5ec8190bf1a7b39d3416e5d066cd7d7b069998d71d8ac591c0e.

- 2026-09-13T17:31:26+00:00: Recorded command exit 101; command argv SHA-256
  3894e5ff28a90166badc6f0b6530e9d9aad05255f63b4b5fd0fd0972a3f024db.

- 2026-09-13T17:31:39+00:00: Recorded command exit 0; command argv SHA-256
  dfda33a7e78865e415320f10e8f2666e739bd53778698a0a94dde61b8b50dff7.

- 2026-09-13T17:32:10+00:00: Recorded command exit 0; command argv SHA-256
  b521bd93db02553299c0f75284bfa9f4e64265fabd9c1848772020b04caadf1e.

- 2026-09-13T17:32:26+00:00: Recorded command exit 0; command argv SHA-256
  8cd48d25c2246280bac7cb9a5f8585ad317fff1fc547b68034db7afda08d4c4e.

- 2026-09-13T17:32:48+00:00: Recorded command exit 0; command argv SHA-256
  5b1d302fd49b52c632d64d47afefb44af37d273e04b24313a6a611a57395cc03.

- 2026-09-13T17:33:03+00:00: Recorded command exit 1; command argv SHA-256
  2f06947d24a9d7189a73377a01e669733655bf28c306cf03d390b04fc13edefb.

- 2026-09-13T17:33:13+00:00: Recorded command exit 101; command argv SHA-256
  9431efe1828e4a062f48449d82aa8013bdf5e7e539f25b2ebb1fda7d7f8e3f4d.

- 2026-09-13T17:33:29+00:00: Recorded command exit 0; command argv SHA-256
  b79f25855ab071e42ddc210eabbb29007d9f7bdcd76059a8cf306dd9b78c10e4.

- 2026-09-13T17:33:43+00:00: Recorded command exit 0; command argv SHA-256
  2d4e10c66ed94b28fdc4171373d809e3fcc83998141c89afc9d78549fd4b90de.

- 2026-09-13T17:33:52+00:00: Recorded command exit 101; command argv SHA-256
  9431efe1828e4a062f48449d82aa8013bdf5e7e539f25b2ebb1fda7d7f8e3f4d.

- 2026-09-13T17:34:08+00:00: Recorded command exit 0; command argv SHA-256
  73b3c383bc5d864fd5f7e3e731b9a4a12696fcfa5256953ca1405bc0980b3f3f.

- 2026-09-13T17:34:23+00:00: Recorded command exit 0; command argv SHA-256
  2f06947d24a9d7189a73377a01e669733655bf28c306cf03d390b04fc13edefb.

- 2026-09-13T17:34:33+00:00: Recorded command exit 0; command argv SHA-256
  9431efe1828e4a062f48449d82aa8013bdf5e7e539f25b2ebb1fda7d7f8e3f4d.

- 2026-09-13T17:34:51+00:00: Recorded command exit 0; command argv SHA-256
  6fb2c1847c885596f4bb009a5d28dc8f9a2ecd536dcc7b5bef4142ab2f02ac9c.

- 2026-09-13T17:35:32+00:00: Recorded command exit 0; command argv SHA-256
  e8df4b615885a928a2fd330222c00ba23ccd6c9f62701e4977111c39d4cc21d7.

- 2026-09-13T17:35:51+00:00: Recorded command exit 0; command argv SHA-256
  2f06947d24a9d7189a73377a01e669733655bf28c306cf03d390b04fc13edefb.

- 2026-09-13T17:36:00+00:00: Recorded command exit 0; command argv SHA-256
  9431efe1828e4a062f48449d82aa8013bdf5e7e539f25b2ebb1fda7d7f8e3f4d.

- 2026-09-13T17:36:13+00:00: Recorded command exit 0; command argv SHA-256
  6fb2c1847c885596f4bb009a5d28dc8f9a2ecd536dcc7b5bef4142ab2f02ac9c.

- 2026-09-13T17:36:28+00:00: Recorded command exit 0; command argv SHA-256
  5f5c937d37617b1b13086488a172f9269cb07d072e79499271560d87e8e9c8de.

- 2026-09-13T17:36:45+00:00: Recorded command exit 0; command argv SHA-256
  d56947531c1511dd5d023654b7c21042ec6a176048fc6a3ca70fb30e2287884a.

- 2026-09-13T17:37:21+00:00: Signed+DCO checkpoint e55df62c4247ca86b6af863c75e189980fadd9fe (tree
  6d0286dc04a8c90ca042a4903d49f3008790bb2f) adds private seqpacket provisioning, service-created
  anonymous stream transfer, one shared 16-session admission guard, dual-endpoint service
  configuration and hostile integration coverage. Exact Rust 1.93 formatting, Clippy for
  asb-control/asb-cli all targets, and both packages' complete test/doc-test suites passed; worktree
  is clean.

- 2026-09-13T17:46:20+00:00: Recorded command exit 101; command argv SHA-256
  28d1d99fa69694b824562aeafa2673c952a2532e8435abb81363ff5e18ea4d12.

- 2026-09-13T17:46:36+00:00: Recorded command exit 0; command argv SHA-256
  f588228349db07eac5fe496ccf400b1fe062fe98fdb416460042ab8615a31a4e.

- 2026-09-13T17:46:51+00:00: Recorded command exit 101; command argv SHA-256
  74db8daaf7a5953d8d1bda7d854d3b7b202b59081c4ab04a76be17284b861ceb.

- 2026-09-13T17:47:14+00:00: Recorded command exit 101; command argv SHA-256
  74db8daaf7a5953d8d1bda7d854d3b7b202b59081c4ab04a76be17284b861ceb.

- 2026-09-13T17:48:42+00:00: Recorded command exit 0; command argv SHA-256
  74db8daaf7a5953d8d1bda7d854d3b7b202b59081c4ab04a76be17284b861ceb.

- 2026-09-13T17:49:22+00:00: Recorded command exit 0; command argv SHA-256
  f588228349db07eac5fe496ccf400b1fe062fe98fdb416460042ab8615a31a4e.

- 2026-09-13T17:49:41+00:00: Recorded command exit 101; command argv SHA-256
  3451120e4bc55e69e37c8d97cd15007f17754ffa46410cd0a4b537e9581416f0.

- 2026-09-13T17:50:09+00:00: Recorded command exit 0; command argv SHA-256
  3451120e4bc55e69e37c8d97cd15007f17754ffa46410cd0a4b537e9581416f0.

- 2026-09-13T17:50:32+00:00: Recorded command exit 0; command argv SHA-256
  a5b3bf67ded976bd93ea0e0aed64ff36f8a59bb48e85a70870c4e8bab552eee5.

- 2026-09-13T17:51:06+00:00: Recorded command exit 0; command argv SHA-256
  d9c5e978ade14e836e82ea00463fc3156469132b45a1260c55f445584eb9646f.

- 2026-09-13T17:51:22+00:00: Recorded command exit 0; command argv SHA-256
  3451120e4bc55e69e37c8d97cd15007f17754ffa46410cd0a4b537e9581416f0.

- 2026-09-13T17:51:41+00:00: Recorded command exit 0; command argv SHA-256
  a5b3bf67ded976bd93ea0e0aed64ff36f8a59bb48e85a70870c4e8bab552eee5.

- 2026-09-13T17:52:08+00:00: Recorded command exit 0; command argv SHA-256
  bf125f814015e9a4be95300d542d12080f3c3dcef5edd0659d6364fd3d7af60f.

- 2026-09-13T17:52:22+00:00: Recorded command exit 0; command argv SHA-256
  46334514e7428b43d40700bf156092aafaabbad637e4630caace9ec45bccf8aa.
