---
{
  "branch": "feature/ar-1344-runtime-cli-acquisition-contract",
  "checkpoint_commit": "487bf83d802fc15d19b581e72af8ed7f4e849409",
  "claim_expires": "2026-09-23T14:57:19+00:00",
  "depends_on": [
    "AR-1339",
    "AR-1340",
    "AR-1342"
  ],
  "id": "AR-1344",
  "next_action": "Complete live relay accept/forward lifecycle around AgentProcess::Live; do not promote until relay is actively served and cancellation/expiry teardown tests pass.",
  "observed_branch": "feature/ar-1344-runtime-cli-acquisition-contract",
  "observed_dirty": 0,
  "observed_head": "487bf83d802fc15d19b581e72af8ed7f4e849409",
  "owner": "codex-asb-ar1344-cli-acquisition-20260923",
  "plan": "../plans/AR-1344-runtime-cli-acquisition-contract.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Add the runtime-owned API and CLI integration needed for safe live-provider attempts.",
  "task_revision": 39,
  "title": "Runtime-owned CLI live acquisition contract",
  "updated_at": "2026-09-23T13:05:22+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1344-runtime-cli-acquisition-contract"
}
---

Created from the AR-1329/AR-1343 audit. The bounded relay is available at
`ce2c2db068b05092f0f63291e0d94d4dbc9cda9c`, but the CLI still has no supported
runtime acquisition seam. Keep `spawn_verified_agent` fail-closed until this
contract and its tests are merged and verified.

- 2026-09-23T12:48:42+00:00: Dependencies AR-1339, AR-1340 and AR-1342 are done; promote the
  runtime-owned CLI acquisition contract to unblock AR-1329 without weakening fail-closed policy.

- 2026-09-23T12:49:01+00:00: Claimed by codex-asb-ar1344-cli-acquisition-20260923.

- 2026-09-23T12:51:36+00:00: Heartbeat by codex-asb-ar1344-cli-acquisition-20260923.

- 2026-09-23T12:51:39+00:00: Heartbeat by codex-asb-ar1344-cli-acquisition-20260923.

- 2026-09-23T12:51:41+00:00: Recorded command exit 0; command argv SHA-256
  0ed28ab2d231d0b2bd8ef8fcc7c11bb59995fd48770e67cf2eb8a98065389117.

- 2026-09-23T12:52:03+00:00: Recorded command exit 0; command argv SHA-256
  498ccf248bc166cd8940e579a67ad12e0a07199783062cc3019459f7d310c063.

- 2026-09-23T12:52:17+00:00: Recorded command exit 0; command argv SHA-256
  226bdfa5da4828ff864f3126c00791871661e174da732206e614e2d05843f279.

- 2026-09-23T12:52:30+00:00: Recorded command exit 0; command argv SHA-256
  64e91b86b06d7063344ceb73ae416c58ad2b4352ab0ffeb981b2e3c176ec279c.

- 2026-09-23T12:52:43+00:00: Recorded command exit 0; command argv SHA-256
  e97ef49f6318174d14e9065600b2c65e961302ae81d9280e2033ccf6a24ee585.

- 2026-09-23T12:52:57+00:00: Recorded command exit 0; command argv SHA-256
  06c540c688f38ee91064fecc195e0368937aa75c041bbd3ab833e7f007f6d217.

- 2026-09-23T12:53:22+00:00: Heartbeat by codex-asb-ar1344-cli-acquisition-20260923.

- 2026-09-23T12:55:05+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-23T12:55:25+00:00: Recorded command exit 0; command argv SHA-256
  fd3302a5f725a05b03fb15853ad3dcc3b516ee6915f463c994e7d35647d86a25.

- 2026-09-23T12:55:53+00:00: Recorded command exit 0; command argv SHA-256
  65bd39b6e995daa8de012e38f77d7d34e17aaa7f48f7d1538e37af30d16d3784.

- 2026-09-23T12:56:07+00:00: Recorded command exit 0; command argv SHA-256
  d5d7089434ef0df54ed54def989b8b3524d50d99d2ad3def82c33ca65dd71f98.

- 2026-09-23T12:56:28+00:00: Checkpoint a29f38f: added runtime-owned LiveProviderAttempt and
  LiveLaunchFactory::acquire; focused asb-runtime launch_factory tests 9 passed, 1 ignored. CLI live
  path remains fail-closed.

- 2026-09-23T12:56:45+00:00: Heartbeat by codex-asb-ar1344-cli-acquisition-20260923.

- 2026-09-23T12:57:19+00:00: Heartbeat by codex-asb-ar1344-cli-acquisition-20260923.

- 2026-09-23T12:58:32+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-23T12:58:57+00:00: Recorded command exit 101; command argv SHA-256
  73d005d4c4983870f0c5405c6c97dffbf521d57825b14d75dae888988fbdcd03.

- 2026-09-23T12:59:11+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-23T12:59:26+00:00: Recorded command exit 0; command argv SHA-256
  73d005d4c4983870f0c5405c6c97dffbf521d57825b14d75dae888988fbdcd03.

- 2026-09-23T13:00:00+00:00: Recorded command exit 101; command argv SHA-256
  1fd0eada112ad6f39155a2af1c5af082afd87465aa13267cb75ccb9f0f3fef57.

- 2026-09-23T13:00:21+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-23T13:00:48+00:00: Recorded command exit 0; command argv SHA-256
  1fd0eada112ad6f39155a2af1c5af082afd87465aa13267cb75ccb9f0f3fef57.

- 2026-09-23T13:01:17+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-23T13:01:34+00:00: Recorded command exit 101; command argv SHA-256
  73d005d4c4983870f0c5405c6c97dffbf521d57825b14d75dae888988fbdcd03.

- 2026-09-23T13:02:05+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-23T13:02:21+00:00: Recorded command exit 0; command argv SHA-256
  73d005d4c4983870f0c5405c6c97dffbf521d57825b14d75dae888988fbdcd03.

- 2026-09-23T13:02:36+00:00: Recorded command exit 0; command argv SHA-256
  66af190091b26d14bdbe2fa3e77c8512b211945518fb80bde35c524ee336f89e.

- 2026-09-23T13:02:50+00:00: Recorded command exit 0; command argv SHA-256
  4d70564f00fdc7493145f48a7ca60627d5cb64c225661a02dc4d1fb26191ed75.

- 2026-09-23T13:03:10+00:00: Checkpoint 487bf83: CLI accepts an injected opaque LiveProviderAttempt
  and retains it through SandboxProcess lifecycle; SandboxProcess now exposes pid/observation. cargo
  check -p asb-cli passes and focused live-provider gate test passes. Remaining blocker: relay
  accept/forward is not yet serviced by CLI/runtime supervisor, so live execution must not be
  considered complete.

- 2026-09-23T13:05:22+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.
