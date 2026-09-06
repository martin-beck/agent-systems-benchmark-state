---
{
  "branch": "feature/replay-pacing",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-06T21:40:44+00:00",
  "depends_on": [
    "AR-0503",
    "AR-0201"
  ],
  "id": "AR-0504",
  "next_action": "Run exact-tree coverage and complete workspace quality, formal, privacy and supply-chain gates; then create focused signed+DCO candidate for immutable review.",
  "observed_branch": "feature/replay-pacing",
  "observed_dirty": 6,
  "observed_head": "162110386605a83f963758a07d83e77e2566528a",
  "owner": "replay-20260906",
  "plan": "../plans/AR-0504.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Support immediate, fixed-latency, original-paced and seeded synthetic scenarios.",
  "task_revision": 52,
  "title": "Implement pacing and replay overhead assessment",
  "updated_at": "2026-09-06T20:10:59+00:00",
  "worktree_key": "agent-systems-benchmark-replay-pacing"
}
---
## AR-0504

Support immediate, fixed-latency, original-paced and seeded synthetic scenarios.

Dependencies AR-0503 and AR-0201 are done. Read the linked plan and claim after
a fresh reconciliation.

- 2026-09-06T19:31:25+00:00: Claimed by replay-20260906.

- 2026-09-06T19:31:57+00:00: Recorded command exit 0; command argv SHA-256
  65631b3828e37a25aa986cfea94aaeab7a01caa728e08c99fcdfc2708a931530.

- 2026-09-06T19:35:55+00:00: Recorded command exit 128; command argv SHA-256
  bff455ee5d7443ee201ad470e6a1d51e198ebc6db456169c8b828ac0bb1def72.

- 2026-09-06T19:36:24+00:00: Recorded command exit 1; command argv SHA-256
  bff455ee5d7443ee201ad470e6a1d51e198ebc6db456169c8b828ac0bb1def72.

- 2026-09-06T19:37:26+00:00: Recorded command exit 0; command argv SHA-256
  bff455ee5d7443ee201ad470e6a1d51e198ebc6db456169c8b828ac0bb1def72.

- 2026-09-06T19:37:40+00:00: Recorded command exit 0; command argv SHA-256
  206a65a3a2f95b13131f3287e00fb48cbbeded5c217e30c3906a2ab16960ed93.

- 2026-09-06T19:37:57+00:00: Recorded command exit 1; command argv SHA-256
  14145dfa568b952a67873b6af66f8601fbd4c4fe6942bf38791e6b4561def405.

- 2026-09-06T19:38:14+00:00: Recorded command exit 0; command argv SHA-256
  21e2270f373d18f07b5ad89c7f03e160450cb9b12af8441448744a604d844171.

- 2026-09-06T19:38:31+00:00: Applied reviewed-local replay-only patches
  00db1bd12ca30ec7fb77b9d0c12409a1fef8089038f19359d90d629cab03058f and
  b26dc516cb2864f7dff1195aa2e63f8166dc4c37e70b8e3e7cb58bf87ac27. Added
  immediate/fixed/original/seeded pacing, desired/actual timing reports, cooperative cancellation,
  slow/failed writer classification, and independent above-client headroom assessment. Focused
  asb-replay tests passed 61 tests including 6 new pacing tests; focused Clippy with warnings denied
  passed. Generic Write cannot be preempted by elapsed checking, so README requires caller-enforced
  transport timeout; production socket integration remains next.

- 2026-09-06T19:38:36+00:00: Heartbeat by replay-20260906.

- 2026-09-06T19:41:49+00:00: Recorded command exit 0; command argv SHA-256
  9492db663bdf97b2fe62fad5a42ddbbe1f753fcb351305115e4b4781a212df4e.

- 2026-09-06T19:41:56+00:00: Recorded command exit 0; command argv SHA-256
  e3f3956d269bce30abbcc057637b1d18dd9a1a266c7a5a204f5affba19168a15.

- 2026-09-06T19:42:02+00:00: Recorded command exit 1; command argv SHA-256
  c04679f3ecd60494c472bb86cda13f021054232639199d557d895f4a59783b4d.

- 2026-09-06T19:43:21+00:00: Recorded command exit 0; command argv SHA-256
  685633f8e11bf257616c74733863c5b0e30075e3122f97d790bdad8580f131e5.

- 2026-09-06T19:43:35+00:00: Recorded command exit 101; command argv SHA-256
  21e2270f373d18f07b5ad89c7f03e160450cb9b12af8441448744a604d844171.

- 2026-09-06T19:43:54+00:00: Recorded command exit 128; command argv SHA-256
  237a790b4aa18d2a02406e31c3ea342cfec22dcef055e626290a97afd2e87bea.

- 2026-09-06T19:44:14+00:00: Recorded command exit 0; command argv SHA-256
  237a790b4aa18d2a02406e31c3ea342cfec22dcef055e626290a97afd2e87bea.

- 2026-09-06T19:44:23+00:00: Recorded command exit 0; command argv SHA-256
  21e2270f373d18f07b5ad89c7f03e160450cb9b12af8441448744a604d844171.

- 2026-09-06T19:45:27+00:00: Recorded command exit 0; command argv SHA-256
  e01f45794b0a353e90bddcbbb2b5df293de359d7b46b65d8878d638da8486c35.

- 2026-09-06T19:45:34+00:00: Recorded command exit 0; command argv SHA-256
  21e2270f373d18f07b5ad89c7f03e160450cb9b12af8441448744a604d844171.

- 2026-09-06T19:49:14+00:00: Recorded command exit 0; command argv SHA-256
  a82e704ca3bee60e3de8bf025affbccd8b318081ffe56c05a15f5fe925503927.

- 2026-09-06T19:49:51+00:00: Recorded command exit 0; command argv SHA-256
  41aa60e3da73cc6159b21c2f562288494d5a495a64555cfb3732641645034526.

- 2026-09-06T19:55:18+00:00: Recorded command exit 0; command argv SHA-256
  38f1499db94c1c37a8da6679656ed6deeb8d4f7b0279863a73e0580d7d659d79.

- 2026-09-06T19:55:57+00:00: Recorded command exit 0; command argv SHA-256
  81a3ed1ff90ebd48591c7a2ae9a4232e5eb75098e59f02c5028c245c5a528671.

- 2026-09-06T19:56:03+00:00: Recorded command exit 0; command argv SHA-256
  01a473de5a90a3a16ac1d302539838cdf7aa091e6664c298ec9b69815b9f9b16.

- 2026-09-06T19:58:19+00:00: Recorded command exit 0; command argv SHA-256
  b4526317809eb4239195779a0fd849366e27a6fecdebf6c38d4fe752a06797c5.

- 2026-09-06T19:58:30+00:00: Recorded command exit 0; command argv SHA-256
  fd18b074c36c405eca0f9ba34e94f5381d2d00e2a7632b72c2e3b9ccfe8d8a93.

- 2026-09-06T20:01:26+00:00: Recorded command exit 0; command argv SHA-256
  e4f4e5034faf3a8ec248acdafe4fdee2fd42562753c254e3397b44b3cddb23c0.

- 2026-09-06T20:01:32+00:00: Recorded command exit 1; command argv SHA-256
  01a473de5a90a3a16ac1d302539838cdf7aa091e6664c298ec9b69815b9f9b16.

- 2026-09-06T20:04:27+00:00: Recorded command exit 128; command argv SHA-256
  3a3dc142328184d8845411b55b9ec9ad5903f3f3345fd90747ea8d8594f200d9.

- 2026-09-06T20:06:37+00:00: Recorded command exit 0; command argv SHA-256
  6879a0298eb0851e1f5eb74748e51dba500b0f0aa6e0ad775c79d2d61a1acc38.

- 2026-09-06T20:06:57+00:00: Recorded command exit 1; command argv SHA-256
  4da82d1778995e32974f5746ac0ad5498ab28faaa361e7c2742c4cfe85df4034.

- 2026-09-06T20:07:10+00:00: Recorded command exit 101; command argv SHA-256
  3853b8d8e359549f44b2d1530b9eb334bd28e13360974ff09bcccb5aea74153c.

- 2026-09-06T20:07:38+00:00: Recorded command exit 0; command argv SHA-256
  6f7c85c94d94e4b346ce81f3e56b8fec3f23dc7213a3d4900b0ed0f057d672e9.

- 2026-09-06T20:07:47+00:00: Recorded command exit 101; command argv SHA-256
  4da82d1778995e32974f5746ac0ad5498ab28faaa361e7c2742c4cfe85df4034.

- 2026-09-06T20:08:24+00:00: Recorded command exit 128; command argv SHA-256
  229c21e18f9acc109bd863f7ec77241fb862e974d973e4fed5684abf5f7e7842.

- 2026-09-06T20:08:33+00:00: Recorded command exit 101; command argv SHA-256
  3853b8d8e359549f44b2d1530b9eb334bd28e13360974ff09bcccb5aea74153c.

- 2026-09-06T20:09:10+00:00: Recorded command exit 0; command argv SHA-256
  ee30a37452142c87689b6e1baedb5de62c5ed8859cba573837584402c07f87e4.

- 2026-09-06T20:09:17+00:00: Recorded command exit 101; command argv SHA-256
  3853b8d8e359549f44b2d1530b9eb334bd28e13360974ff09bcccb5aea74153c.

- 2026-09-06T20:09:41+00:00: Recorded command exit 128; command argv SHA-256
  fa7856574e56222f9e4cf479d8a1b66deea79e21ea530b90ff8cd85f2ed7ff64.

- 2026-09-06T20:09:57+00:00: Recorded command exit 101; command argv SHA-256
  4da82d1778995e32974f5746ac0ad5498ab28faaa361e7c2742c4cfe85df4034.

- 2026-09-06T20:10:26+00:00: Recorded command exit 0; command argv SHA-256
  d8fbcd50a62d73cdee51ae48fdd4db8d6d8571bb733e7f8ac6236a0928e4ee0e.

- 2026-09-06T20:10:37+00:00: Recorded command exit 0; command argv SHA-256
  4da82d1778995e32974f5746ac0ad5498ab28faaa361e7c2742c4cfe85df4034.

- 2026-09-06T20:10:44+00:00: Heartbeat by replay-20260906.

- 2026-09-06T20:10:59+00:00: Repaired pacing boundedness and cursor semantics after coordinator
  review. Recorded/original desired offsets and cumulative fixed/seeded schedules now fail closed
  above five minutes; segment count rejects above cassette MAX_EVENTS before schedule allocation.
  Production loopback TCP writes now use an absolute deadline across each full HTTP head or semantic
  segment, including repeated slow partial progress; standalone generic Write remains
  caller-bounded. Pre-write lateness reports the exact number already completed so a rejected final
  segment is retryable; a fully written over-bound final segment reports complete and commits to
  prevent duplicate full delivery. Added deterministic offset/count, slow-progress deadline,
  final-lateness retry, and final-complete commit negatives. Focused asb-replay all-target tests
  passed (66 tests), Clippy -D warnings passed, and fmt passed. Successful generated repair diffs
  SHA-256 c6d0a2d512d185245048d4fdd4c261455c7daa43f7534f4c495c1497b7d66181,
  a7bd83431aff1be98182ebbe05357c213f15a4327d3e9a0d0f12aeb70cef4b20, and
  65de4e76cf851abf0c35707e2ab554bbae3abd895e7e8a1db40bf98bbde60e41; stable cfg-test patch SHA-256
  8c044d0c0900fdb1a639c64681961c1b426eda0e912e7148a53c6ad5f56b5589. Earlier stable patch attempts
  9b1265b0..., a6de4d37..., and 5bff684d... were rejected as corrupt with no product effect; failed
  fmt/test/Clippy invocations were recorded separately and then corrected.
