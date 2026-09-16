---
{
  "branch": "feature/ar-1268-replay-transport-boundary",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T00:45:23+00:00",
  "depends_on": [
    "AR-1237",
    "AR-1238",
    "AR-1239"
  ],
  "id": "AR-1268",
  "next_action": "Adapt runtime and CLI replay context to shared ReplayTransportV1; add one-shot/stale/duplicate/mismatch/no-fallback integration tests, then full gates.",
  "observed_branch": "feature/ar-1268-replay-transport-boundary",
  "observed_dirty": 0,
  "observed_head": "bd2d95c5f4dd78facc429ed734b61d5f288355ef",
  "owner": "asb_ar1024_lifecycle_router",
  "plan": "../plans/AR-1268.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Break the strict-replay runtime/CLI dependency cycle with a shared transport contract.",
  "task_revision": 13,
  "title": "Break strict-replay runtime/CLI dependency cycle",
  "updated_at": "2026-09-16T22:47:26+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1268-replay-transport"
}
---
## AR-1268

Resolve the dependency-safe transport seam required for runtime-owned strict-replay execution.
Preserve AR-1267's blocked evidence; do not fabricate authority or weaken crate boundaries.

- 2026-09-16T22:45:10+00:00: Dependencies AR-1237/1238/1239 are done; AR-1267 proves a
  dependency-safe runtime/CLI transport boundary is required.

- 2026-09-16T22:45:23+00:00: Claimed by asb_ar1024_lifecycle_router.

- 2026-09-16T22:45:35+00:00: Recorded command exit 0; command argv SHA-256
  2e68a60a4554153980f212be9d1617fcc7d6f5ca5df21c49dd5bd687732f0de2.

- 2026-09-16T22:45:45+00:00: Recorded command exit 0; command argv SHA-256
  bcc0473d3d8569da32e15ff90b1cfc9d028a594db40226091aad89ad88fb5128.

- 2026-09-16T22:46:30+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T22:46:41+00:00: Recorded command exit 0; command argv SHA-256
  474ef19f4556278dcc77a99527fc880d499f620aa0c31805226d7b3f058f0232.

- 2026-09-16T22:46:56+00:00: Recorded command exit 0; command argv SHA-256
  e2fb60616251de3c6a4e6e92438ad67c476f5e0b781bc63dfddfcae0764dadac.

- 2026-09-16T22:47:04+00:00: Recorded command exit 0; command argv SHA-256
  8c64230835cafec9cf70b367423893834394f62eb5d05a01f55fc4636c2821e0.

- 2026-09-16T22:47:26+00:00: Signed checkpoint bd2d95c adds dependency-neutral
  asb-core::replay_transport::ReplayTransportV1 and bounded validation. It carries version,
  generation, cassette and route digests, and provider dialect without runtime/CLI/replay
  dependencies. Positive and negative contract tests pass 2/2; full asb-core lib suite passes 18/18;
  fmt green; product tree clean. Crate graph audit confirms asb-runtime depends only rustix/sha2
  while asb-cli depends asb-agents/replay/runtime, so shared core is the safe cycle-breaking
  boundary.
