---
{
  "branch": "feature/ar-1277-runtime-cli-replay-transport",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1237",
    "AR-1238",
    "AR-1239"
  ],
  "id": "AR-1277",
  "next_action": "Wire ReplayTransportClient into the primary replay dispatch and connect runtime-issued cassette service; add supervised egress/lifecycle evidence.",
  "observed_branch": "feature/ar-1277-runtime-cli-replay-transport",
  "observed_dirty": 0,
  "observed_head": "c88a34c86a67c51e1a74dc8cdb403fbeb3f74879",
  "owner": "",
  "plan": "../plans/AR-1277.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "blocked",
  "summary": "Provide a runtime-issued transport channel for primary strict replay.",
  "task_revision": 31,
  "title": "Runtime-to-CLI replay transport boundary",
  "updated_at": "2026-09-17T00:07:32+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1277-runtime-cli-replay-transport"
}
---

## AR-1277

Implement the authenticated runtime-to-CLI transport required by the primary replay command.
Preserve AR-1276's blocked evidence and require actual supervised execution.

- 2026-09-16T23:59:37+00:00: Dependencies AR-1237, AR-1238, and AR-1239 are done; AR-1276 proves the
  primary CLI lacks any runtime-context or service channel, so a transport boundary is required.

- 2026-09-16T23:59:50+00:00: Claimed by asb_ar1024_lifecycle_router.

- 2026-09-17T00:01:10+00:00: Recorded command exit 1; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-17T00:01:21+00:00: Recorded command exit 101; command argv SHA-256
  fafb5a4fac6560f1f995ed0cf243de8cb6d67cf03242aa7a7b2a739947e458f3.

- 2026-09-17T00:01:32+00:00: Recorded command exit 101; command argv SHA-256
  f843caa71de8b211397f529ece11336ea85dfbb545ef1e655893fa4fccd4f17c.

- 2026-09-17T00:02:01+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-17T00:02:10+00:00: Recorded command exit 101; command argv SHA-256
  fafb5a4fac6560f1f995ed0cf243de8cb6d67cf03242aa7a7b2a739947e458f3.

- 2026-09-17T00:02:19+00:00: Recorded command exit 101; command argv SHA-256
  f843caa71de8b211397f529ece11336ea85dfbb545ef1e655893fa4fccd4f17c.

- 2026-09-17T00:03:20+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-17T00:03:34+00:00: Recorded command exit 0; command argv SHA-256
  fafb5a4fac6560f1f995ed0cf243de8cb6d67cf03242aa7a7b2a739947e458f3.

- 2026-09-17T00:03:45+00:00: Recorded command exit 101; command argv SHA-256
  f843caa71de8b211397f529ece11336ea85dfbb545ef1e655893fa4fccd4f17c.

- 2026-09-17T00:04:06+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-17T00:04:15+00:00: Recorded command exit 0; command argv SHA-256
  f843caa71de8b211397f529ece11336ea85dfbb545ef1e655893fa4fccd4f17c.

- 2026-09-17T00:04:31+00:00: Recorded command exit 0; command argv SHA-256
  010911bb236075a7b2c073cb456cf895f3b8104f2fccf520c4fbbf7820d8426e.

- 2026-09-17T00:04:41+00:00: Recorded command exit 0; command argv SHA-256
  86f0b58cda7205961a02707285263da481f1f0ae813f7a917fe8046675083845.

- 2026-09-17T00:05:16+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-17T00:05:39+00:00: Recorded command exit 101; command argv SHA-256
  036d579f9ca789e29abc142be096d840e24f56366076b390711d296f9cf10582.

- 2026-09-17T00:06:12+00:00: Recorded command exit 0; command argv SHA-256
  988929bf75a80adca4e95673c46f16fae49b7c92330988b33c5d7eee2d3af51a.

- 2026-09-17T00:06:25+00:00: Recorded command exit 0; command argv SHA-256
  036d579f9ca789e29abc142be096d840e24f56366076b390711d296f9cf10582.

- 2026-09-17T00:06:45+00:00: Recorded command exit 0; command argv SHA-256
  de914579e943eb8a19bfa199aec7192e498f03ce1be61f730aede3e208bbac5f.

- 2026-09-17T00:06:54+00:00: Recorded command exit 0; command argv SHA-256
  24514f59c9c1f6caa4f5c7e55bd2ee1dbb116204df8afc77ffd4822c6b27d470.

- 2026-09-17T00:07:22+00:00: Signed checkpoint c88a34c adds dependency-neutral ReplayTransportV1
  request/response envelopes, runtime-owned authenticated channel with retained callback and
  one-shot closed/duplicate transitions, and CLI adapter emitting bounded response JSON. Focused
  runtime transport 2/2, CLI adapter 1/1, offline check and fmt pass. Initial failures were exact
  syntax delimiter, serve_once API test mismatch, and missing asb-core CLI dependency; all fixed and
  rerun green. Primary argument-level replay still has no construction/injection path and supervised
  cassette/egress/cancel/restart/timeout/crash cleanup remains.

- 2026-09-17T00:07:32+00:00: Released blocked/ownerless at clean signed c88a34c. Transport
  contract/runtime channel/CLI adapter implemented and focused tests pass; exact remaining blocker
  is primary argument-level replay dispatch does not construct or receive the runtime-owned client,
  so actual supervised cassette traffic and required provider/descendant egress denial, no-fallback,
  cancellation/restart, timeout/crash reaping, and cleanup evidence cannot be established. Preserve
  c88a34c for follow-on primary dispatch wiring.
