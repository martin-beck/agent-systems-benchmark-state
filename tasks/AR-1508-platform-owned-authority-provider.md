---
{
  "branch": "feature/ar-1508-platform-owned-authority-provider",
  "checkpoint_commit": "0135650a2f54c3a6e79ad3d345c03c4ebc43d35d",
  "claim_expires": "2026-09-29T11:13:46+00:00",
  "depends_on": [
    "AR-1473",
    "AR-1474",
    "AR-1480",
    "AR-1484",
    "AR-1485",
    "AR-1502",
    "AR-1505"
  ],
  "id": "AR-1508",
  "next_action": "Run full exact-head product gates on signed commits 7306f83 and 0135650; obtain independent review before publication.",
  "observed_branch": "feature/ar-1508-platform-owned-authority-provider",
  "observed_dirty": 1,
  "observed_head": "013565032506a3a70a34fc727970a6dd40c377c1",
  "owner": "ar1508-provider-luna56",
  "plan": "../plans/AR-1508-platform-owned-authority-provider.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Provide an authenticated platform-owned source for private runtime roots, tools, policy, and enrollment material.",
  "task_revision": 47,
  "title": "Platform-owned authority provider",
  "updated_at": "2026-09-29T10:47:31+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1508-platform-owned-authority-provider"
}
---

AR-1507 proved that the existing bootstrap contract authenticates only digest
claims and that `RuntimeControlBootstrap::materialize_provisioner` still takes
caller-supplied `RuntimeAuthorityInputs`. This AR owns the missing platform
authority-provider boundary; it must produce verified private material without
exposing it to CLI callers or synthesizing it from fixed paths.

Acceptance requires:

- a runtime/control-owned authority provider authenticated to the AR-1505
  bootstrap session, with verified source/digest binding for namespace, lease,
  relay, tool pins, policy, credential reference, and enrollment material;
- a private materialization API consumed by `RuntimeControlBootstrap` and the
  live scheduler, with no caller/config/socket/path/PATH/fixed-root injection;
- fail-closed behavior for missing, stale, mismatched, expired, revoked,
  restarted, cancelled, or tampered authority, plus alternate-egress denial;
- provider-free deterministic local/mock/replay tests that qualify the contract
  without pretending to be first-customer production evidence;
- independent review, SSH-signed DCO, exact-head hosted checks, protected merge,
  and post-merge assurance.

Non-goals: asb-tui, live provider reachability, public credentials, synthetic or
fixed-path authority, weakening formal/privacy/native gates.

- 2026-09-29T04:14:00+02:00: Created from AR-1507 blocker evidence. The required
  source must be platform-owned and verified; no fixed path or mock authority is
  acceptable in production code.

- 2026-09-29T02:15:14+00:00: Dependencies through AR-1505 verified done; AR-1507 established the
  missing platform-owned authority provider contract.

- 2026-09-29T02:17:57+00:00: Claimed by ar1508_provider_luna56.

- 2026-09-29T02:18:11+00:00: Heartbeat by ar1508_provider_luna56.

- 2026-09-29T02:18:21+00:00: Setup audit: state reconciled and live doctor prerequisites refreshed;
  task revision 2 promoted/open then claimed at revision 3; dependencies include AR-1505 and are
  recorded done; AR-1505 product worktree inspected for requested merge base f92c2e9. Product docs
  and plan inspection now underway.

- 2026-09-29T02:19:06+00:00: Recorded command exit 0; command argv SHA-256
  a1159e9df3670d549d04524532629f5477ceb7deec9b45e47e8c009506ecb2c8.

- 2026-09-29T02:19:33+00:00: Recorded command exit 0; command argv SHA-256
  0e82d1f9ce576541812d2c59fe0a6f45539dc4cfb91f7a39fe3327fc4dea309a.

- 2026-09-29T02:22:14+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-29T02:22:34+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T02:23:07+00:00: Recorded command exit 101; command argv SHA-256
  03315ef10f14441f5aadec73db36f3fb7b35454147c037b191e659b38ff938ee.

- 2026-09-29T02:23:35+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T02:23:54+00:00: Recorded command exit 0; command argv SHA-256
  03315ef10f14441f5aadec73db36f3fb7b35454147c037b191e659b38ff938ee.

- 2026-09-29T02:24:15+00:00: Concrete protected-main audit: AR-1505 merge
  f92c2e941913129d7db50480f71e8361a0d43a0c contains RuntimeControlBootstrap materialization with
  caller-supplied RuntimeAuthorityInputs and PathBuf. AR-1508 now introduces the crate-private
  RuntimePlatformAuthorityBinding and provider/material contract; materialization receives only
  owner plus provider, validates session/generation/expiry/root/tool claims and provider-owned state
  path, then delegates to the existing resolver. Focused test first exited 101 because -D warnings
  rejected unused lifecycle error variants; added the deliberate dead-code annotation to retain
  explicit fail-closed categories, and the exact focused test now passes.

- 2026-09-29T02:24:35+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T02:24:53+00:00: Recorded command exit 0; command argv SHA-256
  f4e5d8b14cda44421923169e0a87b069ad13e27509d93301edee77eec7344946.

- 2026-09-29T02:25:15+00:00: Recorded command exit 0; command argv SHA-256
  02dc064651fd94b14b265f6321ed4689e7785281edcdea9b2ada9fad3dbf0495.

- 2026-09-29T02:25:58+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T02:26:19+00:00: Recorded command exit 0; command argv SHA-256
  97ee782321facf1df64b14b3500c62b04b8b48c9904b8abb83044328a904f4b2.

- 2026-09-29T02:26:36+00:00: Recorded command exit 0; command argv SHA-256
  2faa80e23aae1ee23dded301e7fabeba025e544fd3aa6911359e0f841bfc5fb3.

- 2026-09-29T02:26:52+00:00: Recorded command exit 0; command argv SHA-256
  2a4ba46b698bbe0b03388cdbd9c13d04641f5385375e0892e648b2996a73f171.

- 2026-09-29T02:27:16+00:00: Recorded command exit 101; command argv SHA-256
  e8beebac0638d83321c84d952814966bbba80dc16ee7dd3d3ead10f3c2b72292.

- 2026-09-29T02:28:32+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T02:28:51+00:00: Recorded command exit 0; command argv SHA-256
  e8beebac0638d83321c84d952814966bbba80dc16ee7dd3d3ead10f3c2b72292.

- 2026-09-29T02:29:10+00:00: Recorded command exit 0; command argv SHA-256
  02dc064651fd94b14b265f6321ed4689e7785281edcdea9b2ada9fad3dbf0495.

- 2026-09-29T02:29:32+00:00: Recorded command exit 0; command argv SHA-256
  67739c573b579619ef3e71fb893a396c166af5a2a061ba9f37d5e424ed8b55d4.

- 2026-09-29T02:29:49+00:00: Recorded command exit 0; command argv SHA-256
  80e1eb9890f3dfad67ec444d6e89d59576e05226594eb494dccd9069a7cc055c.

- 2026-09-29T02:30:07+00:00: Audit follow-up: the provider contract now has a production
  RuntimePlatformAuthorityProviderHandle. Runtime/control creates it only from authenticated
  platform material after complete binding verification; bootstrap consumes that handle and
  revalidates it on materialization. No live/fixed-path/synthetic source was invented. The handle is
  exercised by the positive bootstrap test; unavailable, tampered, and relative-path provider
  failures are covered deterministically. Focused six-test group and package Clippy pass. Initial
  Clippy failure (two unnecessary to_owned calls) was repaired through handoffctl.

- 2026-09-29T02:30:58+00:00: Recorded command exit 101; command argv SHA-256
  534f8613e1c316db8f0f46dd989e44e14a8ca74304a94791b4e4a1c59b2fbb1d.

- 2026-09-29T02:31:19+00:00: Recorded command exit 0; command argv SHA-256
  79bec090309cc89803dbedc97f657de211f21b609a26c1a28a455a7f48d24def.

- 2026-09-29T02:31:49+00:00: Independent exact-diff review rejects publication. Signed commits
  7306f83/0135650 add only a crate-private/test provider façade: no production authenticated
  provider or non-test materialization callsite; binding digest is self-attestation and does not
  independently bind tools/policy/allowlist/endpoint; resolver lacks post-materialization
  expiry/revocation fencing; credential/enrollment material is not implemented. Preserve commits
  unpushed. Create AR-1509 for a real platform provider receipt and lifecycle fence.

- 2026-09-29T10:43:43+00:00: AR-1510 confirms the same missing provider boundary; AR-1508 has the
  narrow provider/materialization candidate and now needs exact-head gates and independent review
  before publication.

- 2026-09-29T10:43:46+00:00: Claimed by ar1508-provider-luna56.

- 2026-09-29T10:44:15+00:00: Recorded command exit 0; command argv SHA-256
  79bec090309cc89803dbedc97f657de211f21b609a26c1a28a455a7f48d24def.

- 2026-09-29T10:45:32+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T10:45:51+00:00: Recorded command exit 101; command argv SHA-256
  e8beebac0638d83321c84d952814966bbba80dc16ee7dd3d3ead10f3c2b72292.

- 2026-09-29T10:46:11+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T10:46:29+00:00: Recorded command exit 0; command argv SHA-256
  e8beebac0638d83321c84d952814966bbba80dc16ee7dd3d3ead10f3c2b72292.

- 2026-09-29T10:46:52+00:00: Recorded command exit 0; command argv SHA-256
  02dc064651fd94b14b265f6321ed4689e7785281edcdea9b2ada9fad3dbf0495.

- 2026-09-29T10:47:14+00:00: Recorded command exit 0; command argv SHA-256
  67739c573b579619ef3e71fb893a396c166af5a2a061ba9f37d5e424ed8b55d4.

- 2026-09-29T10:47:31+00:00: Recorded command exit 0; command argv SHA-256
  6dc297611924a2ae988d59011e6fc6e3979c557c8eae0980597c4a05eeda086f.
