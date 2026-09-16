---
{
  "branch": "feature/ar-1233",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1231",
    "AR-1100",
    "AR-1236"
  ],
  "id": "AR-1233",
  "next_action": "Typed LoopbackOnly policy slice 143213c passes full asb-runtime package tests; actual attested loopback namespace/listener binding remains required. Implement backend capability without weakening Deny, then add native child-service/provider-egress tests and full workspace gates.",
  "observed_branch": "feature/ar-1233",
  "observed_dirty": 0,
  "observed_head": "b8455b3fc5f5b88b00b9f5af13e21fe32756b1ae",
  "owner": "",
  "plan": "../plans/AR-1233.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Provide an authenticated loopback-only sandbox transport for strict replay services.",
  "task_revision": 38,
  "title": "Approved loopback-only sandbox transport",
  "updated_at": "2026-09-16T08:32:57+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1233"
}
---

- Created from AR-1232 review: `SandboxSpec` currently accepts only `NetworkPolicy::Deny`, which
  prevents a strict replay child from reaching its owned cassette service. This prerequisite must
  add a separately authenticated loopback-only policy while preserving provider-egress denial.

- 2026-09-16T05:06:10+00:00: Promote approved loopback-only sandbox transport prerequisite;
  dependencies AR-1231 and AR-1100 are complete.

- 2026-09-16T05:06:24+00:00: Claimed by asb_ar1232_sandbox_supervision.

- 2026-09-16T05:08:55+00:00: Heartbeat by asb_ar1232_sandbox_supervision.

- 2026-09-16T05:12:12+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T05:12:23+00:00: Recorded command exit 0; command argv SHA-256
  430c5876fb09571c305425ff5a651b25d7797200eb4e67f73d6a4af7b2f2b091.

- 2026-09-16T05:12:32+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T05:12:43+00:00: Heartbeat by asb_ar1232_sandbox_supervision.

- 2026-09-16T05:12:45+00:00: Recorded command exit 0; command argv SHA-256
  430c5876fb09571c305425ff5a651b25d7797200eb4e67f73d6a4af7b2f2b091.

- 2026-09-16T05:12:55+00:00: Recorded command exit 0; command argv SHA-256
  f71975b0e0b00a780fed3410ff70f306b8004ce22f8d1aecc438b8adc79fe8e9.

- 2026-09-16T05:13:04+00:00: Recorded command exit 0; command argv SHA-256
  88277af860e0269da9d61c1a53b11e0cbbdb110f1d200070af9ed0591b80845e.

- 2026-09-16T05:13:14+00:00: Recorded command exit 128; command argv SHA-256
  39cf5398131881d6bebfeb6940a170dba53287cbad205a984f34c80a6dbe58e7.

- 2026-09-16T05:13:28+00:00: Recorded command exit 0; command argv SHA-256
  269710c1c9962221b1de94c62dab2e843e9cf07a4778d00dc60a9772bdf4f680.

- 2026-09-16T05:13:49+00:00: Signed/DCO product head 143213c pushed on feature/ar-1233. SandboxSpec
  now stores and exposes requested NetworkPolicy; LoopbackOnly is distinct from Deny and Host.
  Existing backend rejects LoopbackOnly with typed SandboxError::NetworkPolicy until an attested
  loopback implementation is added, preventing host-network fallback. Focused cargo test --locked
  --offline -p asb-runtime sandbox::tests::malformed_specs_fail_before_spawn passed 1/1; worktree
  clean.

- 2026-09-16T05:16:34+00:00: Recorded command exit 0; command argv SHA-256
  dd64cc00d697c09654f1cab86d4f13a1d56e1cc54846d30ad53c12c02d6b725b.

- 2026-09-16T05:16:55+00:00: Focused/full asb-runtime gate passed: 26 unit tests, 8 process-boundary
  tests, sandbox/scheduler boundary suites, and 2 doc-tests all green. Product head remains
  signed/DCO 143213c and clean/pushed. LoopbackOnly currently preserves policy identity and fails
  closed at spawn via SandboxError::NetworkPolicy; no host-network fallback. Native child-service
  test remains blocked until backend attestation exists.

- 2026-09-16T05:20:39+00:00: Heartbeat by asb_ar1232_sandbox_supervision.

- 2026-09-16T05:21:06+00:00: Blocked on approved runtime capability: bubblewrap --unshare-all denies
  loopback and no attested loopback-only namespace setup exists. Sharing host network would violate
  provider-egress isolation; adding ambient ip/privileged helper is unsafe and out of scope. Typed
  LoopbackOnly preservation is implemented at signed head 143213c with full asb-runtime gates green.
  Requires approved runtime-owned loopback namespace/helper before native child cassette-service
  tests can proceed.

- 2026-09-16T06:48:39+00:00: Resuming exclusively for capability assessment and fail-closed
  LoopbackOnly implementation; no host-network sharing or ambient egress.

- 2026-09-16T06:48:41+00:00: Claimed by asb_ar1233_worker.

- 2026-09-16T06:49:11+00:00: Recorded command exit 0; command argv SHA-256
  c815548f1b2215eaa93e5ac4c4afa1c1fa3f4b55a2493f5191cb05298857a220.

- 2026-09-16T06:49:30+00:00: Recorded command exit 0; command argv SHA-256
  7ff3db897ee64cc99cbe79b1ece1fe60b7bdfff6f3ffac7680b5a6349713b4b1.

- 2026-09-16T06:50:29+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T06:50:47+00:00: Recorded command exit 1; command argv SHA-256
  13cb335a9efca70fe1c5b3a30ea563d8ff1181feae7527cc9cc0e85403196c41.

- 2026-09-16T06:51:41+00:00: Recorded command exit 0; command argv SHA-256
  272211ee066de81c64609903b55376063469307863315ca2e5531c6db5c5b763.

- 2026-09-16T06:51:54+00:00: AR-1233 capability probe: rootless bwrap --unshare-net exposes only
  kernel loopback (proc/net/dev lo); external egress probe fails with curl exit 7; ip link set lo up
  returns EPERM because lo is already kernel-up and CAP_NET_ADMIN is unavailable. No host-network
  sharing, firewall mutation, or privileged helper used. Backend remains fail-closed for
  LoopbackOnly. Remaining blocker is an attested per-launch bridge/relay that makes the owned
  cassette reachable inside this private namespace while preserving provider-egress denial; do not
  enable LoopbackOnly spawn until that contract is wired and tested.

- 2026-09-16T06:56:21+00:00: Resuming exclusively for AR-1233 capability implementation and
  deterministic testing; no other ARs.

- 2026-09-16T06:56:23+00:00: Claimed by asb_ar1233_worker_next.

- 2026-09-16T06:56:49+00:00: Recorded command exit 0; command argv SHA-256
  d04aa803a9fcb854b247572f9b417fd1935a57ca978bb887d2e7c188e99db043.

- 2026-09-16T06:57:00+00:00: Recorded command exit 0; command argv SHA-256
  11ffcb963c42c8258c3750780d6aecbaebf4cb4599e7f9a569a11807e20da998.

- 2026-09-16T06:59:19+00:00: AR-1233 pass completed without product changes. Existing LoopbackOnly
  remains fail-closed at signed head 143213c: backend rejects spawn because rootless bubblewrap
  private namespace cannot provision an attested listener/relay. Native isolation test passed (host
  loopback unreachable); focused malformed policy test passed; full locked offline workspace tests
  passed 166, 1 ignored, with initial bundle verifier path failure caused by target relocation and
  rerun passing; fmt and clippy -D warnings passed. No host-network sharing, firewall mutation,
  privileged helper, or other AR touched. Next action: integrate a reviewed runtime-owned per-launch
  authenticated bridge/adapter from approved dependency, then run real cassette success plus
  provider-egress denial, stale/duplicate, teardown, and non-interference tests.

- 2026-09-16T08:32:57+00:00: Resume AR-1233 for explicitly scoped provider/descendant LoopbackOnly
  egress-negative tests against reviewed supervisor integration; preserve Deny and no host/global
  network changes.
