---
{
  "branch": "feature/frontend-api-integration",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-08T13:46:53+00:00",
  "depends_on": [
    "AR-0840",
    "AR-0841",
    "AR-0842",
    "AR-0843"
  ],
  "id": "AR-0844",
  "next_action": "Run focused asb-control/asb-cli suites and no-network-listener source/behavior audit on the one-file reconnect continuity delta, then full applicable gates and signed candidate review.",
  "observed_branch": "feature/frontend-api-integration",
  "observed_dirty": 1,
  "observed_head": "4523da9629ff09451a0a2d2fe332d80bbb1320de",
  "owner": "replay_20260906",
  "plan": "../plans/AR-0844.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Integrate and qualify the frontend control API as an independent boundary.",
  "task_revision": 20,
  "title": "Integrate frontend control API",
  "updated_at": "2026-09-08T11:32:23+00:00",
  "worktree_key": "agent-systems-benchmark-frontend-api-integration"
}
---
## AR-0844

Integrate the reviewed protocol, transport, lifecycle, and privacy components. Prove the runner
starts and completes without a frontend, frontend restart does not alter runs, reconnect loses no
status, no implicit network listener exists, and exact-head CI/post-merge recovery checks pass.

- 2026-09-08T10:46:22+00:00: All dependencies AR-0840 through AR-0843 are durably done. Promote
  final frontend API integration as the highest-priority safe ready leaf: use a new isolated
  worktree and limit product scope to integration/standalone-runner qualification, with no shared
  Cargo/schema changes and no overlap with active AR-0316 or AR-1005.

- 2026-09-08T10:46:53+00:00: Claimed by replay_20260906.

- 2026-09-08T10:47:49+00:00: Recorded command exit 0; command argv SHA-256
  a567d604be61cd35259cb3e91d9abeca682cf0e6c45d0a44942ef5c18f32cc7a.

- 2026-09-08T10:51:02+00:00: Recorded command exit 0; command argv SHA-256
  0d86d773d569286663c512885b38008d21ec4490226884f1d5bf29e3a64c0b87.

- 2026-09-08T10:51:33+00:00: Recorded command exit 1; command argv SHA-256
  c0b1b2679f8e24568d6b352b978a86f039239539c08495d3036e27bde90ccaa7.

- 2026-09-08T10:52:23+00:00: Recorded command exit 0; command argv SHA-256
  9d93ce0fac4a96ad7c67e0ee8505318ae12247ba0bc375ed6a23355490291e82.

- 2026-09-08T10:53:13+00:00: Recorded command exit 127; command argv SHA-256
  6af0120dfa757cf73cec7930b589466bc78f5fba33c8dcb8fe31193e2d48e2c2.

- 2026-09-08T10:54:17+00:00: Recorded command exit 2; command argv SHA-256
  55a89807fe4ac7429adbbf47e01ad9bbf008b2ca7fddfdda4d9457be4b6c6513.

- 2026-09-08T10:54:41+00:00: Recorded command exit 0; command argv SHA-256
  9d93ce0fac4a96ad7c67e0ee8505318ae12247ba0bc375ed6a23355490291e82.

- 2026-09-08T10:55:27+00:00: Created the declared isolated worktree at exact product main
  4523da9629ff09451a0a2d2fe332d80bbb1320de. Existing production tests already cover standalone
  backend completion, exclusive worker lifetime, durable idempotent recovery, and disconnect
  survival. Added one-file real Unix integration assertions that capture the pre-disconnect event
  cursor, reconnect after launch, require the next contiguous RunStarted event for the same run,
  then require contiguous terminal RunCompleted evidence after authoritative status refresh. Focused
  exact test passed: 1 passed, 0 failed; fmt and diff-check passed. Exit 127 was missing pinned
  cargo PATH and exit 2 was a mistyped cargo fmt argument; both operator-only, no semantic test
  failure, preserved scope.

- 2026-09-08T11:28:23+00:00: Recorded command exit 0; command argv SHA-256
  774847d8415fd097eebafcb8a207e62e3110fbb472ba0a12a471beeb1cf9da41.

- 2026-09-08T11:29:11+00:00: Recorded command exit 0; command argv SHA-256
  935f33430a1d834ceceb458b3dea9dc96d3bf308bfbc003b0781f1ffe99702d2.

- 2026-09-08T11:29:32+00:00: Recorded command exit 0; command argv SHA-256
  7774bd71bd191357e6abab6a1d18519c54b913349737a738543a99b8f04228b4.

- 2026-09-08T11:30:54+00:00: Recorded command exit 0; command argv SHA-256
  b7a106963f097b95759c96e91fe475e74b38b09341509eddb3094131266dcdd7.

- 2026-09-08T11:32:23+00:00: Recorded command exit 1; command argv SHA-256
  4176f6c00e20cde96da31fb10b860b181852be7535b64f01e014803cb9e54026.
