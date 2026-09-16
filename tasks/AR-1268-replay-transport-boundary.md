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
  "next_action": "Add malformed/no-fallback and supervised lifecycle/egress/cancel/restart/timeout/crash cleanup tests around run_with_transport; then full locked gates.",
  "observed_branch": "feature/ar-1268-replay-transport-boundary",
  "observed_dirty": 0,
  "observed_head": "bc31f488193fea20ff2ba2d117cc578e2fd0c925",
  "owner": "asb_ar1024_lifecycle_router",
  "plan": "../plans/AR-1268.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Break the strict-replay runtime/CLI dependency cycle with a shared transport contract.",
  "task_revision": 38,
  "title": "Break strict-replay runtime/CLI dependency cycle",
  "updated_at": "2026-09-16T22:53:07+00:00",
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

- 2026-09-16T22:48:13+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T22:48:27+00:00: Recorded command exit 0; command argv SHA-256
  27d39a604a9b05a81c44b764ba09d60cf2b61c7a27e523f6fa49d6f4e78e7e37.

- 2026-09-16T22:48:46+00:00: Recorded command exit 0; command argv SHA-256
  59fe41c6e4dce0a2b69c708895d0cae2acb86cc33ff92916a9cb63a46dcaebad.

- 2026-09-16T22:48:54+00:00: Recorded command exit 0; command argv SHA-256
  23f40736b15dae325834d2b5218331c5bd622e920407a31e1c21a43d5c6c78b7.

- 2026-09-16T22:49:10+00:00: Recorded command exit 0; command argv SHA-256
  e2edde358c475063a9aa1bd049d43ef0da60379834792333d2e9f4155b28b63f.

- 2026-09-16T22:49:18+00:00: Recorded command exit 0; command argv SHA-256
  ce51ab9d0d99acfe292cae2da2dccb021901a1f73955a5d1e610328643dd088f.

- 2026-09-16T22:49:38+00:00: Signed commits 551f989 and 35b97be bind asb-runtime to shared
  dependency-neutral asb-core ReplayTransportV1, add RuntimeReplayTransport one-shot validated
  wrapper, and refresh Cargo.lock. Focused tests pass: asb-core 18/18 and asb-runtime 40/40; fmt
  green; product tree clean at 35b97be. This removes the runtime-to-CLI dependency cycle at the
  contract layer. CLI adapter and actual dispatch integration remain next.

- 2026-09-16T22:50:21+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T22:50:46+00:00: Recorded command exit 0; command argv SHA-256
  164cab58608deae4478415ef2d127964a372726bfa9d3432d5659a15752d273a.

- 2026-09-16T22:51:02+00:00: Recorded command exit 0; command argv SHA-256
  ea9efc343fbe41ee065d19917ac9ce7afed04d933153b559a134d8f00fab9fcb.

- 2026-09-16T22:51:10+00:00: Recorded command exit 0; command argv SHA-256
  ca7e0bc39a17fb8fca8734460750f01bee5d2ca4ad440b9c68bebe0ca9216489.

- 2026-09-16T22:51:32+00:00: Signed checkpoint da73202 adds CLI CliReplayTransport adapter over
  shared ReplayTransportV1. It validates the contract, binds cassette/route/provider dialect to
  exact StrictReplayLaunchRecord, consumes once, rejects duplicate consumption and stale route
  mismatch. Cross-crate adapter tests pass 2/2; asb-core 18/18 and asb-runtime 40/40 remain green;
  fmt pass; product tree clean.

- 2026-09-16T22:52:04+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T22:52:18+00:00: Recorded command exit 0; command argv SHA-256
  f489a19876782722ed16d09ca01ff72aa074415a2bb4183d7206b5819538e360.

- 2026-09-16T22:52:34+00:00: Recorded command exit 0; command argv SHA-256
  e274074a17e0682b5edf79b5caca577a41520ed9ca8daf9342f0433b678582a1.

- 2026-09-16T22:52:44+00:00: Recorded command exit 0; command argv SHA-256
  b71d564b86cfe0942bcd176dae230a017a85e9e99e617512300d5049794df159.

- 2026-09-16T22:53:07+00:00: Signed checkpoint bc31f48 wires the shared CliReplayTransport into an
  actual replay argument entrypoint run_with_transport. It rejects non-replay commands with exit 2,
  binds/consumes runtime transport before dispatch, and returns bounded exit 3 for
  stale/mismatched/duplicate context. Full asb-cli lib suite passes 73/73; fmt pass; product tree
  clean. Remaining acceptance is supervised lifecycle and egress/no-fallback test evidence.
