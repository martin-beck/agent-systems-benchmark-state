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
  "observed_dirty": 1,
  "observed_head": "22d9f63188ffcbf7212b1b8748a027fd080fe64f",
  "owner": "codex-asb-ar1344-cli-acquisition-20260923",
  "plan": "../plans/AR-1344-runtime-cli-acquisition-contract.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Add the runtime-owned API and CLI integration needed for safe live-provider attempts.",
  "task_revision": 110,
  "title": "Runtime-owned CLI live acquisition contract",
  "updated_at": "2026-09-23T13:23:35+00:00",
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

- 2026-09-23T13:05:36+00:00: Recorded command exit 101; command argv SHA-256
  295a35f99d4aa7024b5e0a35d1dd38654014d35e0d6da14a79231d3b8d7d50ba.

- 2026-09-23T13:05:57+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-23T13:06:11+00:00: Recorded command exit 101; command argv SHA-256
  295a35f99d4aa7024b5e0a35d1dd38654014d35e0d6da14a79231d3b8d7d50ba.

- 2026-09-23T13:06:27+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-23T13:06:41+00:00: Recorded command exit 101; command argv SHA-256
  295a35f99d4aa7024b5e0a35d1dd38654014d35e0d6da14a79231d3b8d7d50ba.

- 2026-09-23T13:06:58+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-23T13:07:12+00:00: Recorded command exit 101; command argv SHA-256
  295a35f99d4aa7024b5e0a35d1dd38654014d35e0d6da14a79231d3b8d7d50ba.

- 2026-09-23T13:07:27+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-23T13:07:42+00:00: Recorded command exit 101; command argv SHA-256
  295a35f99d4aa7024b5e0a35d1dd38654014d35e0d6da14a79231d3b8d7d50ba.

- 2026-09-23T13:07:55+00:00: Recorded command exit 0; command argv SHA-256
  84cc9ca9627c898a4bda267fbd36e860d25071d06a77b89941447d265c209a3e.

- 2026-09-23T13:08:08+00:00: Recorded command exit 0; command argv SHA-256
  a4e543177f3983d6df2d4aca57ddea455a588dc5fde08e3533b7b5b639d63805.

- 2026-09-23T13:09:20+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-23T13:09:39+00:00: Recorded command exit 101; command argv SHA-256
  295a35f99d4aa7024b5e0a35d1dd38654014d35e0d6da14a79231d3b8d7d50ba.

- 2026-09-23T13:09:53+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-23T13:10:07+00:00: Recorded command exit 0; command argv SHA-256
  295a35f99d4aa7024b5e0a35d1dd38654014d35e0d6da14a79231d3b8d7d50ba.

- 2026-09-23T13:10:21+00:00: Recorded command exit 0; command argv SHA-256
  3d594146be1d5462ee560a63945011ee3e88bda5ce487aab9678845cb7f62bc8.

- 2026-09-23T13:10:35+00:00: Recorded command exit 0; command argv SHA-256
  bc65d1f51adf18c9ec6fac426de33358153f4fe52e7cebe01313899c7a307a91.

- 2026-09-23T13:11:09+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-23T13:11:23+00:00: Recorded command exit 0; command argv SHA-256
  73d005d4c4983870f0c5405c6c97dffbf521d57825b14d75dae888988fbdcd03.

- 2026-09-23T13:11:37+00:00: Recorded command exit 0; command argv SHA-256
  e274074a17e0682b5edf79b5caca577a41520ed9ca8daf9342f0433b678582a1.

- 2026-09-23T13:11:51+00:00: Recorded command exit 0; command argv SHA-256
  2f7ebc8a6121ce06015549e0c715eb528865e9bd84ad62b35b76c08660a598f8.

- 2026-09-23T13:12:23+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-23T13:12:37+00:00: Recorded command exit 101; command argv SHA-256
  a21cc57248487fda85eda2b675daa059868bb055e8d92fbaa0a901c4e0cc0cf7.

- 2026-09-23T13:13:01+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-23T13:13:17+00:00: Recorded command exit 101; command argv SHA-256
  a21cc57248487fda85eda2b675daa059868bb055e8d92fbaa0a901c4e0cc0cf7.

- 2026-09-23T13:13:35+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-23T13:13:50+00:00: Recorded command exit 101; command argv SHA-256
  a21cc57248487fda85eda2b675daa059868bb055e8d92fbaa0a901c4e0cc0cf7.

- 2026-09-23T13:14:04+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-23T13:14:19+00:00: Recorded command exit 101; command argv SHA-256
  a21cc57248487fda85eda2b675daa059868bb055e8d92fbaa0a901c4e0cc0cf7.

- 2026-09-23T13:14:41+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-23T13:14:55+00:00: Recorded command exit 101; command argv SHA-256
  a21cc57248487fda85eda2b675daa059868bb055e8d92fbaa0a901c4e0cc0cf7.

- 2026-09-23T13:15:10+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-23T13:15:24+00:00: Recorded command exit 0; command argv SHA-256
  44858bcc1bea325f8e4ec42626fdf2970d2310a4694e160101531722dea4dfa4.

- 2026-09-23T13:15:37+00:00: Recorded command exit 0; command argv SHA-256
  7363438f08b3bf87f01fbbcf12899d3e537b94df7011c67280aeadd61fae19af.

- 2026-09-23T13:15:51+00:00: Recorded command exit 0; command argv SHA-256
  122c3ed65889582e058f654850887f81f361385717eddbda4442f66040c94165.

- 2026-09-23T13:16:16+00:00: Recorded command exit 101; command argv SHA-256
  a21cc57248487fda85eda2b675daa059868bb055e8d92fbaa0a901c4e0cc0cf7.

- 2026-09-23T13:16:39+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-23T13:16:55+00:00: Recorded command exit 101; command argv SHA-256
  a21cc57248487fda85eda2b675daa059868bb055e8d92fbaa0a901c4e0cc0cf7.

- 2026-09-23T13:17:24+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-23T13:17:39+00:00: Recorded command exit 101; command argv SHA-256
  a21cc57248487fda85eda2b675daa059868bb055e8d92fbaa0a901c4e0cc0cf7.

- 2026-09-23T13:17:53+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-23T13:18:08+00:00: Recorded command exit 101; command argv SHA-256
  a21cc57248487fda85eda2b675daa059868bb055e8d92fbaa0a901c4e0cc0cf7.

- 2026-09-23T13:18:26+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-23T13:18:40+00:00: Recorded command exit 101; command argv SHA-256
  a21cc57248487fda85eda2b675daa059868bb055e8d92fbaa0a901c4e0cc0cf7.

- 2026-09-23T13:18:55+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-23T13:19:10+00:00: Recorded command exit 101; command argv SHA-256
  a21cc57248487fda85eda2b675daa059868bb055e8d92fbaa0a901c4e0cc0cf7.

- 2026-09-23T13:19:25+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-23T13:19:45+00:00: Recorded command exit 101; command argv SHA-256
  a21cc57248487fda85eda2b675daa059868bb055e8d92fbaa0a901c4e0cc0cf7.

- 2026-09-23T13:20:01+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-23T13:20:21+00:00: Recorded command exit 101; command argv SHA-256
  a21cc57248487fda85eda2b675daa059868bb055e8d92fbaa0a901c4e0cc0cf7.

- 2026-09-23T13:20:35+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-23T13:20:56+00:00: Recorded command exit 101; command argv SHA-256
  a21cc57248487fda85eda2b675daa059868bb055e8d92fbaa0a901c4e0cc0cf7.

- 2026-09-23T13:21:09+00:00: Recorded command exit 0; command argv SHA-256
  cbc58799f329cfc8e920531d1fe667aa9c9e73409d66571d82bb3456876f9b07.

- 2026-09-23T13:21:23+00:00: Recorded command exit 0; command argv SHA-256
  9abe21b225a0cdd19ac0ecc7403fc116fa261aa73f1d1c560fed96fd8b6e7fa1.

- 2026-09-23T13:21:42+00:00: Recorded command exit 101; command argv SHA-256
  a21cc57248487fda85eda2b675daa059868bb055e8d92fbaa0a901c4e0cc0cf7.

- 2026-09-23T13:23:08+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-23T13:23:21+00:00: Recorded command exit 0; command argv SHA-256
  60734e33d61f22ff3d0c62893aecba2e82f57822d94e9c057beff7a1c39c6a65.

- 2026-09-23T13:23:35+00:00: Recorded command exit 0; command argv SHA-256
  d9fc86987cddff233bda843e1334aaf02b4251be241681eb459531dbc22a604e.
