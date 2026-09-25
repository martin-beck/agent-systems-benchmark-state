---
{
  "branch": "feature/ar-1450-runtime-owned-local-replay-acquisition",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-25T21:24:41+00:00",
  "depends_on": [
    "AR-1448"
  ],
  "id": "AR-1450",
  "next_action": "Implement runtime-owned bootstrap/provisioner using existing LiveProviderProvisioner pattern; own relay/lease roots, tool pins, sandbox construction, attestation and teardown internally.",
  "observed_branch": "feature/ar-1450-runtime-owned-local-replay-acquisition",
  "observed_dirty": 0,
  "observed_head": "7c1a93a6f4dfb1482f0a40e84554eb702aac6a21",
  "owner": "ar1450-replay-luna56",
  "plan": "../plans/AR-1450.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Keep local replay authority acquisition inside the runtime boundary.",
  "task_revision": 44,
  "title": "Runtime-owned local replay acquisition factory",
  "updated_at": "2026-09-25T19:24:41+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1450-runtime-owned-local-replay-acquisition"
}
---

AR-1449 proved that the ordinary CLI cannot safely call AR-1448 because authority issuance still requires caller-built sandbox, lease, backend and relay objects. This task moves only their acquisition into asb-runtime.

Requirements:
- accept only a validated cassette digest; reject malformed, stale, copied and mismatched identities before side effects;
- provision bounded private replay relay, benchmark lease and NetworkPolicy::Deny launch input in runtime;
- perform backend attestation and return opaque one-shot authority;
- guarantee cancellation, teardown, no secret or provider network access, and no alternate egress;
- add positive and hostile offline tests; no live provider or native host requirement;
- expose a narrow API that asb-cli can consume without constructing authority.

- 2026-09-25T16:59:00+00:00: Claimed by ar1450-replay-luna56.

- 2026-09-25T17:00:26+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-25T17:00:49+00:00: Recorded command exit 0; command argv SHA-256
  65bd39b6e995daa8de012e38f77d7d34e17aaa7f48f7d1538e37af30d16d3784.

- 2026-09-25T17:01:05+00:00: Recorded command exit 0; command argv SHA-256
  24503ef668e612b07a646bfcdc91f2dce6cd0768756ff9bc94993a66bbbfcdb6.

- 2026-09-25T17:01:55+00:00: Independent audit stopped before publication: a public factory
  constructor accepting SandboxLaunchInput, ResourceLease and SandboxBackend would preserve the
  AR-1449 boundary violation. Current AR-1448 primitives lack a runtime-owned provisioning
  entrypoint; no product change published.

- 2026-09-25T17:08:23+00:00: Claimed by ar1450-replay-luna56.

- 2026-09-25T17:10:16+00:00: Heartbeat by ar1450-replay-luna56.

- 2026-09-25T17:12:48+00:00: Recorded command exit 0; command argv SHA-256
  65bd39b6e995daa8de012e38f77d7d34e17aaa7f48f7d1538e37af30d16d3784.

- 2026-09-25T17:14:31+00:00: Recorded command exit 0; command argv SHA-256
  9e3940c60be335ccbfaf47e13db8f75969521ecb94eb60ff8d3cf370ea4cfa41.

- 2026-09-25T17:14:57+00:00: Recorded command exit 0; command argv SHA-256
  22e19b493905763db82579efba79e09fd676c9b8ee4111938c68138e3deba800.

- 2026-09-25T17:15:24+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-25T17:15:47+00:00: Recorded command exit 0; command argv SHA-256
  b945362378f77f64a68eb9e8d400e693e008357f0cc0d69f7bfe3bb93e47ae02.

- 2026-09-25T17:16:14+00:00: Recorded command exit 101; command argv SHA-256
  e8beebac0638d83321c84d952814966bbba80dc16ee7dd3d3ead10f3c2b72292.

- 2026-09-25T17:16:33+00:00: Recorded command exit 0; command argv SHA-256
  3ce33da0bd13d6d45f504cd4fee1733f24e5e1f216473a6920381efb750ecea3.

- 2026-09-25T17:16:56+00:00: Recorded command exit 0; command argv SHA-256
  3ce33da0bd13d6d45f504cd4fee1733f24e5e1f216473a6920381efb750ecea3.

- 2026-09-25T17:17:25+00:00: Recorded command exit 0; command argv SHA-256
  3ce33da0bd13d6d45f504cd4fee1733f24e5e1f216473a6920381efb750ecea3.

- 2026-09-25T17:17:53+00:00: Recorded command exit 0; command argv SHA-256
  3ce33da0bd13d6d45f504cd4fee1733f24e5e1f216473a6920381efb750ecea3.

- 2026-09-25T17:18:17+00:00: Recorded command exit 0; command argv SHA-256
  e8beebac0638d83321c84d952814966bbba80dc16ee7dd3d3ead10f3c2b72292.

- 2026-09-25T17:18:45+00:00: Recorded command exit 0; command argv SHA-256
  65bd39b6e995daa8de012e38f77d7d34e17aaa7f48f7d1538e37af30d16d3784.

- 2026-09-25T17:19:01+00:00: Recorded command exit 0; command argv SHA-256
  6cedf4d286d4325f11782b31fa84f7f9fa616331880d0fcbfdc54614bc49768f.

- 2026-09-25T17:19:19+00:00: Recorded command exit 0; command argv SHA-256
  bb0e08dd82ef2580192c57b32b12ba31a207c11aa628611d50d374a78d40bdbc.

- 2026-09-25T17:19:54+00:00: Recorded command exit 0; command argv SHA-256
  1d4a6ad66d99635aea146be56ba18ef2a754d7dc6feb79785bbcd2dff7351269.

- 2026-09-25T17:20:13+00:00: Recorded command exit 0; command argv SHA-256
  bc2f198ba42ab908661264a20c4b64e85c25e1181c5fdd5fea87a200426a4cc2.

- 2026-09-25T17:23:11+00:00: Heartbeat by ar1450-replay-luna56.

- 2026-09-25T17:23:46+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-25T17:24:03+00:00: Recorded command exit 0; command argv SHA-256
  65bd39b6e995daa8de012e38f77d7d34e17aaa7f48f7d1538e37af30d16d3784.

- 2026-09-25T17:24:23+00:00: Recorded command exit 0; command argv SHA-256
  1760ee45d061a54971921c83db04e7fbc546f3971d554f17e152a2387c3e1581.

- 2026-09-25T17:25:07+00:00: Recorded command exit 0; command argv SHA-256
  a32c66f397c1b8766afbcad9ae8c63c9ca5406422d5f40f652f687ef9cf61695.

- 2026-09-25T17:31:01+00:00: Recorded command exit 0; command argv SHA-256
  caa881d23f931343114afa8743907f3f131741c2e330c715af913bd9f9be3a17.

- 2026-09-25T17:31:31+00:00: Recorded command exit 0; command argv SHA-256
  05d2f27a44e4b92e2bd921f0775c6644b850939b9438fa5230a66203497c7844.

- 2026-09-25T18:11:42+00:00: Recorded command exit 0; command argv SHA-256
  bf49346f34989936f53e2e4e5773e8a6f2078e63e3742c8a0ebf912aeb363c45.

- 2026-09-25T18:12:03+00:00: Recorded command exit 0; command argv SHA-256
  89d842bc69bf0374cfd560ef93bde1b424d2e1cbfd1866c9d312b790e8dbeeab.

- 2026-09-25T19:24:38+00:00: Recovered expired claim formerly owned by ar1450-replay-luna56.
  Recovered expired AR-1450 lease before continuation; preserving branch 7c1a93a and prior evidence
  for replay-runtime repair.

- 2026-09-25T19:24:41+00:00: Claimed by ar1450-replay-luna56.
