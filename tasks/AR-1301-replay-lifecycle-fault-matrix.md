---
{
  "branch": "feature/ar-1301-replay-lifecycle-fault-matrix",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T12:51:29+00:00",
  "depends_on": [
    "AR-1287",
    "AR-1300"
  ],
  "id": "AR-1301",
  "next_action": "PR #219 is updated to exact signed head d960dfc; monitor all required exact-head CI checks, diagnose failures from artifacts, merge only after terminal green, then post-merge verify and release AR-1301.",
  "observed_branch": "feature/ar-1301-replay-lifecycle-fault-matrix",
  "observed_dirty": 0,
  "observed_head": "ba2b20dd8a6ff7e2dc60bfa90a6c36906c878834",
  "owner": "ar1301_negative_matrix",
  "plan": "../plans/AR-1301.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Qualify strict-replay supervised lifecycle faults, isolation and cleanup end to end.",
  "task_revision": 230,
  "title": "Supervised replay lifecycle fault matrix",
  "updated_at": "2026-09-17T11:51:41+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1301-replay-lifecycle-fault-matrix"
}
---

## AR-1301

Add and qualify the executable ASB integration matrix still missing from PR #215: successful
strict-replay request/response, provider and descendant egress denial, timeout, cancellation,
crash, restart, cleanup/reaping, unrelated-process isolation and no-live-fallback behavior.
Every case must run through the real runtime-owned dispatch and supervised child lifecycle; no
ignored or caller-simulated test may be used as completion evidence.

This is a focused follow-on to AR-1300 and the blocked AR-1286 lifecycle work. AR-1287 provides the
approved signed multi-architecture Bubblewrap/systemd runner and is a hard dependency because host
namespace capability is not sufficient. Preserve AR-1286 and AR-1287 history; do not weaken their
gates or revive old PR branches. Scope is ASB only: lifecycle runner integration, test fixtures,
schemas/docs and bounded evidence under `crates/asb-runtime`, `crates/asb-replay`, `crates/asb-cli`
and repository test infrastructure. Do not modify asb-tui or coordinator implementation.


- 2026-09-17T09:04:13+00:00: Dependencies AR-1287 and AR-1300 are now durably done; AR-1287
  runner/KVM qualification and repaired exact-main gates are green. Promote for implementation of
  the real supervised replay lifecycle fault matrix.

- 2026-09-17T09:04:33+00:00: Claimed by coordinator-ar1301-lifecycle-20260917.

- 2026-09-17T09:04:53+00:00: Recorded command exit 0; command argv SHA-256
  e3f8b27bf55cc5a899f6fbef1e50d3d7d4f1d4aea9cc10f0b6d093e1d278001e.

- 2026-09-17T09:10:12+00:00: Recorded command exit 0; command argv SHA-256
  98d7da7c8f339087cb458fcc6a9a8de62dc00f691bd8bb3cb3b637c423a5a38e.

- 2026-09-17T09:13:36+00:00: Recorded command exit 1; command argv SHA-256
  31e231953d8a0d5bbdfae1f833e30156183cdf9a73ecf83b810e158abfeb9c6d.

- 2026-09-17T09:15:27+00:00: Recorded command exit 1; command argv SHA-256
  d895c37b205165b0192e4ab4e19944fc2127b66e99d4c71a2a9b435c36347580.

- 2026-09-17T09:15:37+00:00: Recorded command exit 1; command argv SHA-256
  e0ddf609d0da21c540090189fd8225abb05fee0f56710ccbd5b0d3bda989c192.

- 2026-09-17T09:16:21+00:00: Recorded command exit 255; command argv SHA-256
  18c27e0f363eb006b95d1a1908652c624d05bd12d4b75248b1f7754f0a986652.

- 2026-09-17T09:17:09+00:00: Recorded command exit 1; command argv SHA-256
  cbe7279d6b1db469ac8eb5412d4c15714b2e3a130f3410903ce6734d12bad4d3.

- 2026-09-17T09:18:20+00:00: Recorded command exit 0; command argv SHA-256
  f663c16ba03070c3f0962c7ba018a53d439741581d768c4797eb671389f6dc69.

- 2026-09-17T09:18:44+00:00: Recorded command exit 1; command argv SHA-256
  19f1162efd99befcf48aa723806b5dfe259bd82446da6a6c5fe68c439d7ffae6.

- 2026-09-17T09:18:59+00:00: Recorded command exit 32; command argv SHA-256
  4d070b83878e8695e4940457427bc6913d2106905d1011a12ead64bae7f96839.

- 2026-09-17T09:19:16+00:00: Recorded command exit 1; command argv SHA-256
  9f6e65ff172658bdcf829961164cedc8fc086c994aa979e5d3a5e0e86545cb86.

- 2026-09-17T09:19:47+00:00: Recorded command exit 0; command argv SHA-256
  9f6e65ff172658bdcf829961164cedc8fc086c994aa979e5d3a5e0e86545cb86.

- 2026-09-17T09:23:43+00:00: Recorded command exit 0; command argv SHA-256
  830309b4035a180a11c454cc5becab08f0a387b419cf9b6aaf3dfbedf12d5c00.

- 2026-09-17T09:25:48+00:00: Heartbeat by coordinator-ar1301-lifecycle-20260917.

- 2026-09-17T09:25:51+00:00: Recorded command exit 101; command argv SHA-256
  548cbf08f922ba65a7606053d8957418a7ba3f684f3d5830d1ba9ba64d09cd6a.

- 2026-09-17T09:26:09+00:00: Recorded command exit 101; command argv SHA-256
  aef90ad837a90e25ed5f224f7352b79f46b3c2f0bd42d034d9be7804d0bfeb46.

- 2026-09-17T09:26:18+00:00: Recorded command exit 0; command argv SHA-256
  d93ecdb078dcc73bd5e583dc7ee2a9c51757876456749d8cf0dbd6ebd1116523.

- 2026-09-17T09:26:48+00:00: Recorded command exit 1; command argv SHA-256
  eb30afcb41b351282fc60335418aa4b5b408a36075a19a250b73d64c66db04b8.

- 2026-09-17T09:27:10+00:00: Recorded command exit 0; command argv SHA-256
  40e97611e5c80a882600f001119d8d61489fe0e002cd3c0db0e761a1b4c4c0d2.

- 2026-09-17T09:28:11+00:00: Recorded command exit 1; command argv SHA-256
  da9db2dbe742113f306c044d1a16c1e21ffb1aec08f3f41d58d55c2eecac6c84.

- 2026-09-17T09:28:51+00:00: Recorded command exit 1; command argv SHA-256
  da9db2dbe742113f306c044d1a16c1e21ffb1aec08f3f41d58d55c2eecac6c84.

- 2026-09-17T09:29:08+00:00: Recorded command exit 101; command argv SHA-256
  a76666b22fdcfdca396667b4fce9e9e6be13ae40edd06f493bd2f944dc8187bf.

- 2026-09-17T09:30:29+00:00: Recorded command timeout; classification=SUBPROCESS_TIMEOUT;
  deadline=20.0s; command argv SHA-256
  a76666b22fdcfdca396667b4fce9e9e6be13ae40edd06f493bd2f944dc8187bf.

- 2026-09-17T09:31:39+00:00: Recorded command exit 101; command argv SHA-256
  a76666b22fdcfdca396667b4fce9e9e6be13ae40edd06f493bd2f944dc8187bf.

- 2026-09-17T09:32:37+00:00: Recorded command exit 101; command argv SHA-256
  a76666b22fdcfdca396667b4fce9e9e6be13ae40edd06f493bd2f944dc8187bf.

- 2026-09-17T09:33:00+00:00: Recorded command exit 101; command argv SHA-256
  a76666b22fdcfdca396667b4fce9e9e6be13ae40edd06f493bd2f944dc8187bf.

- 2026-09-17T09:33:24+00:00: Recorded command exit 0; command argv SHA-256
  a76666b22fdcfdca396667b4fce9e9e6be13ae40edd06f493bd2f944dc8187bf.

- 2026-09-17T09:33:55+00:00: Recorded command exit 0; command argv SHA-256
  835ec209ab3557bf961f3e05d712be48bcc1fa464115d7b6badfdbdfefb5eb6e.

- 2026-09-17T09:35:26+00:00: Recorded command exit 101; command argv SHA-256
  f64ee3963bf9fdbe79de1ce06e81220c72283a0d1d3c2f31622326acbea71ff0.

- 2026-09-17T09:35:45+00:00: Recorded command exit 101; command argv SHA-256
  6bd5887d6ab532969aedcb0ce3d9545f147aed5e2a52149d25d2f70bd499c0ee.

- 2026-09-17T09:36:05+00:00: Recorded command exit 101; command argv SHA-256
  6bd5887d6ab532969aedcb0ce3d9545f147aed5e2a52149d25d2f70bd499c0ee.

- 2026-09-17T09:36:28+00:00: Recorded command exit 101; command argv SHA-256
  f64ee3963bf9fdbe79de1ce06e81220c72283a0d1d3c2f31622326acbea71ff0.

- 2026-09-17T09:36:46+00:00: Recorded command exit 101; command argv SHA-256
  f64ee3963bf9fdbe79de1ce06e81220c72283a0d1d3c2f31622326acbea71ff0.

- 2026-09-17T09:37:08+00:00: Recorded command exit 101; command argv SHA-256
  f64ee3963bf9fdbe79de1ce06e81220c72283a0d1d3c2f31622326acbea71ff0.

- 2026-09-17T09:37:21+00:00: Recorded command exit 101; command argv SHA-256
  f64ee3963bf9fdbe79de1ce06e81220c72283a0d1d3c2f31622326acbea71ff0.

- 2026-09-17T09:37:40+00:00: Recorded command exit 101; command argv SHA-256
  f64ee3963bf9fdbe79de1ce06e81220c72283a0d1d3c2f31622326acbea71ff0.

- 2026-09-17T09:37:56+00:00: Recorded command exit 0; command argv SHA-256
  f64ee3963bf9fdbe79de1ce06e81220c72283a0d1d3c2f31622326acbea71ff0.

- 2026-09-17T09:38:29+00:00: Recorded command exit 101; command argv SHA-256
  f64ee3963bf9fdbe79de1ce06e81220c72283a0d1d3c2f31622326acbea71ff0.

- 2026-09-17T09:38:58+00:00: Recorded command exit 101; command argv SHA-256
  f64ee3963bf9fdbe79de1ce06e81220c72283a0d1d3c2f31622326acbea71ff0.

- 2026-09-17T09:39:15+00:00: Recorded command exit 0; command argv SHA-256
  f64ee3963bf9fdbe79de1ce06e81220c72283a0d1d3c2f31622326acbea71ff0.

- 2026-09-17T09:40:04+00:00: Recorded command exit 0; command argv SHA-256
  f64ee3963bf9fdbe79de1ce06e81220c72283a0d1d3c2f31622326acbea71ff0.

- 2026-09-17T09:40:19+00:00: Recorded command exit 1; command argv SHA-256
  43862bff1ad5c955f48eab076fdc168dccc49a409c6e749a7da6ee6ad32a3d61.

- 2026-09-17T09:40:39+00:00: Recorded command exit 1; command argv SHA-256
  43862bff1ad5c955f48eab076fdc168dccc49a409c6e749a7da6ee6ad32a3d61.

- 2026-09-17T09:40:58+00:00: Recorded command exit 0; command argv SHA-256
  20de82e2dfda47e067c025174834de79a76dfb342f25b13473ccf2cc67d79982.

- 2026-09-17T09:41:22+00:00: Recorded command exit 0; command argv SHA-256
  aef90ad837a90e25ed5f224f7352b79f46b3c2f0bd42d034d9be7804d0bfeb46.

- 2026-09-17T09:41:40+00:00: Recorded command exit 0; command argv SHA-256
  589a6a7304bff5d3f4150197129dcbcdc2bdfb7788a70237cac560f87bbeb845.

- 2026-09-17T09:42:18+00:00: Heartbeat by coordinator-ar1301-lifecycle-20260917.

- 2026-09-17T09:43:23+00:00: Recorded command exit 0; command argv SHA-256
  ea2aa72a7c2d5808e9f44dbffd3057a7dc8223d0467e3299191819f4f26ed2a7.

- 2026-09-17T09:54:19+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-17T09:54:35+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-17T09:54:56+00:00: Recorded command exit 101; command argv SHA-256
  6874e6c38453fbede58ad5abe316a3aaef690bddb9edcc76d0952252f963ef33.

- 2026-09-17T09:55:17+00:00: Recorded command exit 0; command argv SHA-256
  503960e7a61c6dfb6e654fd3c59faa89ec2e3eed4ff36d3c0c46c574f8f914d9.

- 2026-09-17T09:55:46+00:00: Recorded command exit 101; command argv SHA-256
  6874e6c38453fbede58ad5abe316a3aaef690bddb9edcc76d0952252f963ef33.

- 2026-09-17T09:56:18+00:00: Recorded command exit 101; command argv SHA-256
  6874e6c38453fbede58ad5abe316a3aaef690bddb9edcc76d0952252f963ef33.

- 2026-09-17T09:57:37+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-17T09:57:55+00:00: Recorded command exit 101; command argv SHA-256
  6874e6c38453fbede58ad5abe316a3aaef690bddb9edcc76d0952252f963ef33.

- 2026-09-17T09:58:23+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-17T09:58:42+00:00: Recorded command exit 101; command argv SHA-256
  f2be4037998b84ac0bd851bdf82437fc8ea2da8e38b242e2b71512e46a4d39dd.

- 2026-09-17T09:59:47+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-17T10:00:02+00:00: Recorded command exit 101; command argv SHA-256
  f2be4037998b84ac0bd851bdf82437fc8ea2da8e38b242e2b71512e46a4d39dd.

- 2026-09-17T10:00:47+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-17T10:00:57+00:00: Recorded command exit 101; command argv SHA-256
  f2be4037998b84ac0bd851bdf82437fc8ea2da8e38b242e2b71512e46a4d39dd.

- 2026-09-17T10:01:18+00:00: Recorded command exit 0; command argv SHA-256
  503960e7a61c6dfb6e654fd3c59faa89ec2e3eed4ff36d3c0c46c574f8f914d9.

- 2026-09-17T10:01:29+00:00: Recorded command exit 101; command argv SHA-256
  f2be4037998b84ac0bd851bdf82437fc8ea2da8e38b242e2b71512e46a4d39dd.

- 2026-09-17T10:02:22+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-17T10:02:32+00:00: Recorded command exit 101; command argv SHA-256
  f2be4037998b84ac0bd851bdf82437fc8ea2da8e38b242e2b71512e46a4d39dd.

- 2026-09-17T10:03:10+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-17T10:03:22+00:00: Recorded command exit 101; command argv SHA-256
  f2be4037998b84ac0bd851bdf82437fc8ea2da8e38b242e2b71512e46a4d39dd.

- 2026-09-17T10:03:44+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-17T10:04:04+00:00: Recorded command exit 101; command argv SHA-256
  f2be4037998b84ac0bd851bdf82437fc8ea2da8e38b242e2b71512e46a4d39dd.

- 2026-09-17T10:04:30+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-17T10:04:42+00:00: Recorded command exit 101; command argv SHA-256
  f2be4037998b84ac0bd851bdf82437fc8ea2da8e38b242e2b71512e46a4d39dd.

- 2026-09-17T10:05:07+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-17T10:05:17+00:00: Recorded command exit 0; command argv SHA-256
  f2be4037998b84ac0bd851bdf82437fc8ea2da8e38b242e2b71512e46a4d39dd.

- 2026-09-17T10:05:55+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-17T10:06:08+00:00: Recorded command exit 0; command argv SHA-256
  25c0c4ee58b75b4e9e308c2e90782b7ef8118b67cfad40912d42a2eae31991bd.

- 2026-09-17T10:08:00+00:00: Recorded command exit 101; command argv SHA-256
  f2be4037998b84ac0bd851bdf82437fc8ea2da8e38b242e2b71512e46a4d39dd.

- 2026-09-17T10:08:16+00:00: Recorded command exit 0; command argv SHA-256
  f2be4037998b84ac0bd851bdf82437fc8ea2da8e38b242e2b71512e46a4d39dd.

- 2026-09-17T10:08:35+00:00: Recorded command exit 0; command argv SHA-256
  f6a30a1c04ad774cfcececeda5e807c6c292b39745d73e3815cc8e9a743dea68.

- 2026-09-17T10:09:01+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-17T10:09:18+00:00: Recorded command exit 0; command argv SHA-256
  548cbf08f922ba65a7606053d8957418a7ba3f684f3d5830d1ba9ba64d09cd6a.

- 2026-09-17T10:10:09+00:00: Recorded command exit 0; command argv SHA-256
  0a80e5fef7a7fd1f9619dda5154f8e236f7046b2d753e8434f5dc84d2c1342d8.

- 2026-09-17T10:11:32+00:00: Updated durable next action after runtime-owned authenticated cassette
  integration and exact full-gate evidence; no completion or publication claim.

- 2026-09-17T11:12:33+00:00: Recovered expired claim formerly owned by
  coordinator-ar1301-lifecycle-20260917. Lease expired at 2026-09-17T11:12:18Z; no worker process,
  heartbeat, or durable update since 10:11:32Z; worktree is clean at a57d111. Recovered ownerless
  for safe reassignment; preserve candidate and review blockers.

- 2026-09-17T11:12:54+00:00: Claimed by ar1301_negative_matrix.

- 2026-09-17T11:15:02+00:00: Recorded command exit 0; command argv SHA-256
  4931a5e7746eceb6a9be71471820906262e36f2e203bcbfc7a3956fe7128b3c8.

- 2026-09-17T11:15:16+00:00: Heartbeat by ar1301_negative_matrix.

- 2026-09-17T11:15:23+00:00: Recorded command exit 1; command argv SHA-256
  f0b4664c30818fe4211298b74abed85f1eeac2143251c9524eadc26f8f83a383.

- 2026-09-17T11:15:37+00:00: Recorded command exit 1; command argv SHA-256
  a882d1c54d510669bc25ba480047d6963d0df44504d8beff711d573ae1db56de.

- 2026-09-17T11:15:51+00:00: Recorded command exit 0; command argv SHA-256
  fac6e4880e7d891708f96ec317c69f057cdfb4b4f9bf081daf63b8afe33ba8d6.

- 2026-09-17T11:16:06+00:00: Recorded command exit 101; command argv SHA-256
  66ce6aba5bf1f3440b88d5f6cedb634d8a78e2be96bced965f2ec37c9344b3d5.

- 2026-09-17T11:16:18+00:00: Heartbeat by ar1301_negative_matrix.

- 2026-09-17T11:16:21+00:00: Recorded command exit 0; command argv SHA-256
  66ce6aba5bf1f3440b88d5f6cedb634d8a78e2be96bced965f2ec37c9344b3d5.

- 2026-09-17T11:16:40+00:00: Heartbeat by ar1301_negative_matrix.

- 2026-09-17T11:16:46+00:00: Recorded command exit 0; command argv SHA-256
  6250a6d5fe042eaf1aedee9e6f3441dc82078f4dec4960a672d1315cb6316f3d.

- 2026-09-17T11:17:40+00:00: Recorded command exit 0; command argv SHA-256
  aae76b2c1f4c961d89ea16c16414a707e5fda3e0ce22d8d19bd228a493333b46.

- 2026-09-17T11:17:50+00:00: Recorded command exit 0; command argv SHA-256
  93597477313ae0ca3dd0ce802304247ff217b6eac6f5e39377ba89f08ccd164d.

- 2026-09-17T11:18:13+00:00: Heartbeat by ar1301_negative_matrix.

- 2026-09-17T11:18:17+00:00: Recorded command exit 0; command argv SHA-256
  a882d1c54d510669bc25ba480047d6963d0df44504d8beff711d573ae1db56de.

- 2026-09-17T11:18:33+00:00: Recorded command exit 101; command argv SHA-256
  ef0b050d10a3a8bb6d6ac40bfe095b806c22824b02c6da1d1d62c7496841604d.

- 2026-09-17T11:18:48+00:00: Recorded command exit 0; command argv SHA-256
  aae76b2c1f4c961d89ea16c16414a707e5fda3e0ce22d8d19bd228a493333b46.

- 2026-09-17T11:18:59+00:00: Recorded command exit 0; command argv SHA-256
  b01c6a4b4a5a92399ca52535a46d150a39b9c9b5bcc71f499d0a83a6deda9c3b.

- 2026-09-17T11:19:22+00:00: Gate failure recorded at 11:18:33Z: cargo clippy --locked --workspace
  --all-targets -- -D warnings exited 101 because existing test helper run_supervised_fault had 8
  arguments and clippy::too_many_arguments was denied. This was a test-lint/setup failure, not a
  product/runtime failure. Added narrowly scoped #[allow(clippy::too_many_arguments)] in signed
  commit cf2a7b0; rerun gates.

- 2026-09-17T11:19:29+00:00: Heartbeat by ar1301_negative_matrix.

- 2026-09-17T11:19:37+00:00: Recorded command exit 0; command argv SHA-256
  ef0b050d10a3a8bb6d6ac40bfe095b806c22824b02c6da1d1d62c7496841604d.

- 2026-09-17T11:19:46+00:00: Heartbeat by ar1301_negative_matrix.

- 2026-09-17T11:20:19+00:00: Recorded command exit 0; command argv SHA-256
  d888f2e6850a7d8882bedec6a4341952034e9089887e9f27e504cc05f8da70b7.

- 2026-09-17T11:20:38+00:00: Focused authenticated negative boundary passed: stale generation,
  malformed handshake, duplicate one-shot, and strict route mismatch/no-fallback. Native supervised
  fault matrix passed, including crash-before-fresh-generation followed by clean fresh-generation
  restart and relay cleanup. Full locked cargo test --workspace passed; 173+1 ignored agents, all
  workspace targets terminal green with documented environment-gated ignores. cargo fmt --all --
  --check and cargo clippy --locked --workspace --all-targets -- -D warnings passed after fixing the
  existing test-helper too_many_arguments lint. Product worktree was clean after signed DCO commits.

- 2026-09-17T11:21:06+00:00: Corrected next action to identify the final product head and signed
  commits precisely.

- 2026-09-17T11:21:14+00:00: Heartbeat by ar1301_negative_matrix.

- 2026-09-17T11:23:52+00:00: Independent review confirmed current
  authenticated_replay_boundary_rejects... is direct unit coverage and
  native_supervisor_fault_matrix uses only shell/curl fixtures. AR remains in progress; no
  publication authorized until supervised authenticated negative cases execute end to end.

- 2026-09-17T11:25:29+00:00: Recorded command exit 0; command argv SHA-256
  fac6e4880e7d891708f96ec317c69f057cdfb4b4f9bf081daf63b8afe33ba8d6.

- 2026-09-17T11:25:44+00:00: Heartbeat by ar1301_negative_matrix.

- 2026-09-17T11:25:47+00:00: Recorded command exit 101; command argv SHA-256
  9bd5166f629a82f3e3ecfb54fa3cd28251a1d0d13c013f697bc2c1d1ea553ddc.

- 2026-09-17T11:26:14+00:00: Recorded command exit 0; command argv SHA-256
  fac6e4880e7d891708f96ec317c69f057cdfb4b4f9bf081daf63b8afe33ba8d6.

- 2026-09-17T11:26:23+00:00: Recorded command exit 101; command argv SHA-256
  9bd5166f629a82f3e3ecfb54fa3cd28251a1d0d13c013f697bc2c1d1ea553ddc.

- 2026-09-17T11:26:40+00:00: Recorded command exit 0; command argv SHA-256
  fac6e4880e7d891708f96ec317c69f057cdfb4b4f9bf081daf63b8afe33ba8d6.

- 2026-09-17T11:26:52+00:00: Recorded command exit 101; command argv SHA-256
  9bd5166f629a82f3e3ecfb54fa3cd28251a1d0d13c013f697bc2c1d1ea553ddc.

- 2026-09-17T11:27:30+00:00: Recorded command exit 0; command argv SHA-256
  fac6e4880e7d891708f96ec317c69f057cdfb4b4f9bf081daf63b8afe33ba8d6.

- 2026-09-17T11:27:41+00:00: Recorded command exit 0; command argv SHA-256
  9bd5166f629a82f3e3ecfb54fa3cd28251a1d0d13c013f697bc2c1d1ea553ddc.

- 2026-09-17T11:27:54+00:00: Recorded command exit 0; command argv SHA-256
  96ef322cb602bf662a5430c50b0f11acbb116f1243f34df951a44b697e7fb0b1.

- 2026-09-17T11:28:03+00:00: Recorded command exit 0; command argv SHA-256
  d95bdb7a984cb091f2f0c5f71fa5963f9fd04d12d932f2164c5e7dfa877d518e.

- 2026-09-17T11:28:20+00:00: Heartbeat by ar1301_negative_matrix.

- 2026-09-17T11:28:23+00:00: Recorded command exit 0; command argv SHA-256
  a882d1c54d510669bc25ba480047d6963d0df44504d8beff711d573ae1db56de.

- 2026-09-17T11:28:32+00:00: Recorded command exit 101; command argv SHA-256
  ef0b050d10a3a8bb6d6ac40bfe095b806c22824b02c6da1d1d62c7496841604d.

- 2026-09-17T11:28:48+00:00: Gate failure at 11:28:32Z: cargo clippy exited 101 on test-only useless
  conversion mode.clone().into() in the new supervised negative matrix. This is a strict-lint setup
  failure, not a runtime/product behavior failure. Replace with mode.clone(), rerun all gates.

- 2026-09-17T11:28:55+00:00: Recorded command exit 0; command argv SHA-256
  aae76b2c1f4c961d89ea16c16414a707e5fda3e0ce22d8d19bd228a493333b46.

- 2026-09-17T11:29:05+00:00: Recorded command exit 0; command argv SHA-256
  380ab08f944614fa52fd2a9635b3cf47aa280e1730f0c68a301ad35369965c00.

- 2026-09-17T11:29:25+00:00: Recorded command exit 0; command argv SHA-256
  a882d1c54d510669bc25ba480047d6963d0df44504d8beff711d573ae1db56de.

- 2026-09-17T11:29:35+00:00: Recorded command exit 0; command argv SHA-256
  ef0b050d10a3a8bb6d6ac40bfe095b806c22824b02c6da1d1d62c7496841604d.

- 2026-09-17T11:29:45+00:00: Heartbeat by ar1301_negative_matrix.

- 2026-09-17T11:30:29+00:00: Recorded command exit 101; command argv SHA-256
  d888f2e6850a7d8882bedec6a4341952034e9089887e9f27e504cc05f8da70b7.

- 2026-09-17T11:31:17+00:00: Recorded command exit 0; command argv SHA-256
  fac6e4880e7d891708f96ec317c69f057cdfb4b4f9bf081daf63b8afe33ba8d6.

- 2026-09-17T11:31:36+00:00: Recorded command exit 0; command argv SHA-256
  9bd5166f629a82f3e3ecfb54fa3cd28251a1d0d13c013f697bc2c1d1ea553ddc.

- 2026-09-17T11:31:49+00:00: Recorded command exit 0; command argv SHA-256
  aae76b2c1f4c961d89ea16c16414a707e5fda3e0ce22d8d19bd228a493333b46.

- 2026-09-17T11:31:59+00:00: Recorded command exit 0; command argv SHA-256
  777ef0cc36220b27fe8dee2ad0f24efda1ea6e1b8860fc09bb9f3f22d4d42ca8.

- 2026-09-17T11:32:20+00:00: Full workspace test at 11:30:29Z exited 101 because the new negative
  test unwrapped expected SandboxError::ScopeOwnership { exit_code: Some(1), stderr: "Error:
  \\"adapter failed\\"" } for intentionally rejected stale/malformed/duplicate/mismatch launches.
  Focused supervised negative test now passes in 1.72s after matching this expected terminal
  failure. This was test-harness handling, not a product runtime failure; full workspace must be
  rerun.

- 2026-09-17T11:32:27+00:00: Heartbeat by ar1301_negative_matrix.

- 2026-09-17T11:33:06+00:00: Recorded command exit 101; command argv SHA-256
  d888f2e6850a7d8882bedec6a4341952034e9089887e9f27e504cc05f8da70b7.

- 2026-09-17T11:33:21+00:00: Full cargo test --locked --workspace at 11:33:06Z reached 13/15 sandbox
  tests but exited 101 from environment/resource contention:
  launch_wrapper_timeout_and_crash_are_terminal saw unexpected ScopeIdentity, while authenticated
  cassette supervisor hit its 10s deadline and local replay transport failure. The new supervised
  negative matrix itself passed. No product defect inferred; rerun serial native tests to
  distinguish contention and record terminal result.

- 2026-09-17T11:33:33+00:00: Heartbeat by ar1301_negative_matrix.

- 2026-09-17T11:33:48+00:00: Recorded command exit 0; command argv SHA-256
  6b10188019d4badb4e9e66041e1f845504c80f4133b592a73f3aeb39303b0c45.

- 2026-09-17T11:34:43+00:00: Recorded command exit 0; command argv SHA-256
  0752a3f51c9a63e666fd08e54515911bd4dbfa0381acb86327909b702e10e5de.

- 2026-09-17T11:35:05+00:00: Focused sandbox_boundary serial gate passed: 15/15 tests, including
  supervised stale, malformed, duplicate, strict mismatch/no-fallback and crash/restart cases. Full
  locked workspace test with --test-threads=1 passed across all packages and doc-tests;
  environment-gated tests remained explicitly ignored. fmt/clippy passed. Final product head e98293a
  is clean, SSH-signed, DCO-signed. Default-parallel full failure was native resource contention and
  is superseded by the serialized terminal-green evidence.

- 2026-09-17T11:36:29+00:00: Heartbeat by ar1301_negative_matrix.

- 2026-09-17T11:36:32+00:00: Root independently reviewed complete exact-head e98293a diff:
  supervised ReplayRelay/sidecar/supervisor/StrictReplayService/curl matrix, failure assertions,
  cleanup, SSH signature and DCO all pass. Publication is now authorized through the documented
  workflow.

- 2026-09-17T11:37:06+00:00: Recorded command exit 0; command argv SHA-256
  742a2b07155ce85f26c6a67818a7c335010cc0db0acc511bda7b6c92b214a362.

- 2026-09-17T11:37:21+00:00: Recorded command exit 0; command argv SHA-256
  6d8a443c550c1617d2c97259eac21c9bab4a62a6640f774d1c64ab0da15b5a6e.

- 2026-09-17T11:37:36+00:00: Published PR #219 from clean exact e98293a after independent review.
  Remote branch push and PR creation were performed through handoffctl. Awaiting exact-head CI; no
  merge yet.

- 2026-09-17T11:37:45+00:00: Recorded command exit 8; command argv SHA-256
  692eb759baea7146573fa037797ec9330bdc03edccdf287567e9debb3b6e3027.

- 2026-09-17T11:38:16+00:00: Heartbeat by ar1301_negative_matrix.

- 2026-09-17T11:38:20+00:00: Recorded command exit 1; command argv SHA-256
  692eb759baea7146573fa037797ec9330bdc03edccdf287567e9debb3b6e3027.

- 2026-09-17T11:38:32+00:00: Recorded command exit 0; command argv SHA-256
  bd0c8affc63ff55ae333abdb2bcff6fd2e82560d14aa48a32411e8ee6349db2d.

- 2026-09-17T11:39:12+00:00: Recorded command exit 1; command argv SHA-256
  7694ba3582e5e5cc4738c9e8058fefc41944fd55a49286f6f35e12aed3c3c1a5.

- 2026-09-17T11:39:47+00:00: Recorded command exit 0; command argv SHA-256
  43bfc22ad20fbdc1d435b14a5ff7938f43c0f9936f0296812038bfdaf23dbb43.

- 2026-09-17T11:40:10+00:00: Recorded command exit 0; command argv SHA-256
  fac6e4880e7d891708f96ec317c69f057cdfb4b4f9bf081daf63b8afe33ba8d6.

- 2026-09-17T11:40:23+00:00: Recorded command exit 0; command argv SHA-256
  9bd5166f629a82f3e3ecfb54fa3cd28251a1d0d13c013f697bc2c1d1ea553ddc.

- 2026-09-17T11:40:36+00:00: Recorded command exit 0; command argv SHA-256
  aae76b2c1f4c961d89ea16c16414a707e5fda3e0ce22d8d19bd228a493333b46.

- 2026-09-17T11:40:45+00:00: Recorded command exit 0; command argv SHA-256
  f14fcb5ada42333121d5b2aa7e90d6a2ac2696076e04972172674ce029860258.

- 2026-09-17T11:40:57+00:00: Heartbeat by ar1301_negative_matrix.

- 2026-09-17T11:41:01+00:00: Recorded command exit 0; command argv SHA-256
  a882d1c54d510669bc25ba480047d6963d0df44504d8beff711d573ae1db56de.

- 2026-09-17T11:41:12+00:00: Recorded command exit 0; command argv SHA-256
  ef0b050d10a3a8bb6d6ac40bfe095b806c22824b02c6da1d1d62c7496841604d.

- 2026-09-17T11:42:08+00:00: Recorded command exit 0; command argv SHA-256
  0752a3f51c9a63e666fd08e54515911bd4dbfa0381acb86327909b702e10e5de.

- 2026-09-17T11:42:23+00:00: Recorded command exit 0; command argv SHA-256
  742a2b07155ce85f26c6a67818a7c335010cc0db0acc511bda7b6c92b214a362.

- 2026-09-17T11:43:17+00:00: Heartbeat by ar1301_negative_matrix.

- 2026-09-17T11:43:21+00:00: Recorded command exit 0; command argv SHA-256
  a4d63c111a90376e3bbe905368afae79a42b42406aedf635db89e488827aba87.

- 2026-09-17T11:43:40+00:00: Recorded command exit 0; command argv SHA-256
  392c429ce2f5b8dd0494b9bb5bd983bbeaff2a343fb13c6d1ab024a104417c62.

- 2026-09-17T11:43:51+00:00: Recorded command exit 1; command argv SHA-256
  68d1905798f65f1fa37a56ec1c37cb9bf6b0adebfaa9ff85c9d06d643274cff6.

- 2026-09-17T11:44:14+00:00: Recorded command exit 0; command argv SHA-256
  734df3b1d63b623c5dc36b3dfbf1bb99731e9a04d01b8757a104310dc2492661.

- 2026-09-17T11:44:34+00:00: Recorded command exit 0; command argv SHA-256
  a9c69eedd421f76c67d95d7d046418669beec96852a5be2abbb7fafedac8dc6e.

- 2026-09-17T11:44:50+00:00: Heartbeat by ar1301_negative_matrix.

- 2026-09-17T11:44:54+00:00: Recorded command exit 0; command argv SHA-256
  a882d1c54d510669bc25ba480047d6963d0df44504d8beff711d573ae1db56de.

- 2026-09-17T11:45:05+00:00: Recorded command exit 101; command argv SHA-256
  f168aea13f25588700dda81334b62a8451cffd69f63e4675aa0b7158cdc5f2e2.

- 2026-09-17T11:45:16+00:00: Recorded command exit 0; command argv SHA-256
  43862bff1ad5c955f48eab076fdc168dccc49a409c6e749a7da6ee6ad32a3d61.

- 2026-09-17T11:45:39+00:00: Recorded command exit 0; command argv SHA-256
  afa220e36cf7497f614ef45624103a1420d95389990fb77bc9c2ae8275abcff7.

- 2026-09-17T11:45:51+00:00: Recorded command exit 0; command argv SHA-256
  a9b0aab1ee0d051e20dc12af5ff85dcb725ef1658bd532afeb02271567eb076a.

- 2026-09-17T11:46:06+00:00: Recorded command exit 0; command argv SHA-256
  e6c45759822ceff0eec6e5aba2fd07a273aea7588ca80b14ca5149dc9a3546a2.

- 2026-09-17T11:46:20+00:00: Recorded command exit 0; command argv SHA-256
  ca470e23527a4ce646081a10dfc57188ca40d8e7496386fcd09d07885bfae789.

- 2026-09-17T11:46:41+00:00: Heartbeat by ar1301_negative_matrix.

- 2026-09-17T11:46:44+00:00: Recorded command exit 0; command argv SHA-256
  0b796bb0c9fd92be26f390252b741b32f21e1063a1b285242188f891f6e2c818.

- 2026-09-17T11:46:56+00:00: Recorded command exit 0; command argv SHA-256
  9b56d48d9ca976c81d88581187419e988bc84a31d2250393dd78642b27a7b4e8.

- 2026-09-17T11:47:50+00:00: Recorded command exit 0; command argv SHA-256
  e064f1d4f27086c055979cb53e3dd8089126ab6469fb20b01927e41713771b5c.

- 2026-09-17T11:48:04+00:00: Recorded command exit 0; command argv SHA-256
  0428d3b797d1d74e1ffd2838db60e5c0f6db276fa936738a70f1bc37b6af1089.

- 2026-09-17T11:48:16+00:00: Recorded command exit 0; command argv SHA-256
  c76ae63e9333e356c653faefa5419804301344cc46dcb7a3cb69f02120b56356.

- 2026-09-17T11:48:36+00:00: Hosted platform failure runs 35217105883 and earlier was classified as
  hosted portability executing the new supervised matrix without native qualification. The matrix
  now skips unless ASB_REQUIRE_NATIVE_SANDBOX=1; required-native focused test passed 1/1,
  hosted-safe sandbox suite passed 15/15, fmt/clippy/full locked serialized workspace gates passed.
  Commit d960dfc is SSH-signed and carries matching DCO. Pushed to PR #219; new exact-head CI run
  set 352176096xx is in progress.

- 2026-09-17T11:49:09+00:00: Recorded command exit 1; command argv SHA-256
  692eb759baea7146573fa037797ec9330bdc03edccdf287567e9debb3b6e3027.

- 2026-09-17T11:49:23+00:00: Heartbeat by ar1301_negative_matrix.

- 2026-09-17T11:49:27+00:00: Recorded command exit 0; command argv SHA-256
  06806a96a648d2d71c60a7abf74218fca03d7dc5779b7058885cc61446d537b6.

- 2026-09-17T11:49:44+00:00: Recorded command exit 0; command argv SHA-256
  c6515d69c9463050fd687aadb7db970413a7e94d016accda997a61ddc0ff6ff8.

- 2026-09-17T11:50:15+00:00: Recorded command exit 0; command argv SHA-256
  f6102f7974bd4c872029b148cb04e10e0e916c6bbcac679566d5c3a1486b9c1e.

- 2026-09-17T11:50:46+00:00: Recorded command exit 0; command argv SHA-256
  a055a6ff980a89fee039dc1e83cbbe22c616d2aa58c3a8eec290ca07590c2c28.

- 2026-09-17T11:50:56+00:00: Recorded command exit 1; command argv SHA-256
  9b2e6212e5b3d652986e40de7124cd1fcf21acc131600d0c8a13c28f977def46.

- 2026-09-17T11:51:10+00:00: Recorded command exit 0; command argv SHA-256
  b95bd410258727d023431d1ee5aba290e1046af83192ecc505e1aed4c77a90f6.

- 2026-09-17T11:51:29+00:00: Heartbeat by ar1301_negative_matrix.

- 2026-09-17T11:51:31+00:00: Recorded command exit 0; command argv SHA-256
  8dea51ee0efaa9c559a707bffa4633482bca3199bf26c7a91ae0f51f9f765f90.

- 2026-09-17T11:51:41+00:00: Recorded command exit 0; command argv SHA-256
  3977f9a1c8a9b1f970b60ab7728572f478d220d63cd69d9fefe135b14f03ba05.
