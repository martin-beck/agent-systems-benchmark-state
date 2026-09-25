---
{
  "branch": "feature/ar-1453-frontend-orchestration-wiring",
  "checkpoint_commit": "4db5c4d781a27401ebe895c94400325b7c3647e6",
  "claim_expires": "2026-09-25T23:14:03+00:00",
  "depends_on": [
    "AR-1452"
  ],
  "id": "AR-1453",
  "next_action": "Lifecycle repair remains incomplete; do not push PR #332. Strict replay/deadline tests pass, but isolated active-worker and unix-disconnect tests still end in non-terminal/NeedsReconciliation state, and production idempotency test times out at 30s. Diagnose why completed strict replay catalog state is not preserved across worker/recovery and why production wait hangs; then rerun focused/full gates.",
  "observed_branch": "feature/ar-1453-frontend-orchestration-wiring",
  "observed_dirty": 3,
  "observed_head": "4db5c4d781a27401ebe895c94400325b7c3647e6",
  "owner": "ar1453-frontend-orchestration-luna56",
  "plan": "../plans/AR-1453.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Make CLI and control use the central service for every run lifecycle.",
  "task_revision": 85,
  "title": "Route ASB frontends through central orchestration",
  "updated_at": "2026-09-25T21:49:48+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1453-frontend-orchestration-wiring"
}
---

Keep asb-tui out of scope; its future adapter can consume the same stable
asb-control protocol after this AR is complete.


- 2026-09-25T20:40:23+00:00: AR-1452 is merged and all seven exact-main post-merge workflows passed.
  Promote AR-1453 to implement CLI/control routing through the central runtime-owned orchestration
  service; keep asb-tui out of scope.

- 2026-09-25T20:40:46+00:00: Claimed by ar1453-frontend-orchestration-luna56.

- 2026-09-25T20:41:57+00:00: Recorded command exit 0; command argv SHA-256
  fa1ab7baafb93a5c0e7df68703a8dc54e6405b9feac8f96ae2133eb43e768cd5.

- 2026-09-25T20:42:13+00:00: Recorded command exit 0; command argv SHA-256
  b832bab19dcb37de05dfb7ee61d7c27c2ee176c07f0b9f98580db5cbf41548d2.

- 2026-09-25T20:47:57+00:00: Heartbeat by ar1453-frontend-orchestration-luna56.

- 2026-09-25T20:50:14+00:00: Recorded command exit 101; command argv SHA-256
  69487790cd46864562a51f207e108eea84da8519a17023da666d53127f8fc1e6.

- 2026-09-25T20:50:32+00:00: Recorded command exit 101; command argv SHA-256
  69487790cd46864562a51f207e108eea84da8519a17023da666d53127f8fc1e6.

- 2026-09-25T20:51:06+00:00: Heartbeat by ar1453-frontend-orchestration-luna56.

- 2026-09-25T20:51:16+00:00: Initial implementation in isolated worktree adds asb-orchestrator
  dependency, a runtime-owned PlanAuthoritySource, and FrontendOrchestration
  admission/execute/cancel bridge. Focused cargo check first exposed missing execute_until and moved
  Arc/request errors; both are repaired, rerunning now. Worktree remains dirty and no commit is
  published.

- 2026-09-25T20:51:24+00:00: Recorded command exit 101; command argv SHA-256
  69487790cd46864562a51f207e108eea84da8519a17023da666d53127f8fc1e6.

- 2026-09-25T20:51:42+00:00: Recorded command exit 0; command argv SHA-256
  69487790cd46864562a51f207e108eea84da8519a17023da666d53127f8fc1e6.

- 2026-09-25T20:52:50+00:00: Recorded command exit 1; command argv SHA-256
  9756ab5284ffa251a5df0370e343543d04af8c834bbbe162523c3431db90a797.

- 2026-09-25T20:53:30+00:00: Recorded command exit 101; command argv SHA-256
  6d0fda30bd06d4d3815684128be84386abaeeaf63ae599bb44640c6b9eacf93a.

- 2026-09-25T20:54:00+00:00: Recorded command exit 0; command argv SHA-256
  6d0fda30bd06d4d3815684128be84386abaeeaf63ae599bb44640c6b9eacf93a.

- 2026-09-25T20:54:32+00:00: Heartbeat by ar1453-frontend-orchestration-luna56.

- 2026-09-25T20:54:35+00:00: Central adapter now compiles and the production backend idempotency
  lifecycle test passes. The worker source executes PlanFile through Orchestrator and cancellation
  calls the service. One initial rejection was repaired by binding workload/scorer content digests.
  Worktree remains dirty; no product commit yet. Coordinator reports PR328 post-merge tree repair at
  452f3ca, so this branch must rebase before PR.

- 2026-09-25T20:54:44+00:00: Recorded command exit 0; command argv SHA-256
  d14685a76261418fffc0205bec68cecb43459972ecb2bbaad05a7b94c04c8325.

- 2026-09-25T20:55:35+00:00: Recorded command exit 101; command argv SHA-256
  14edd0ad93656d3066756eeb15124080a03e4428e97f2d3cae0a28abcbbc1fe5.

- 2026-09-25T20:55:58+00:00: Recorded command exit 0; command argv SHA-256
  14edd0ad93656d3066756eeb15124080a03e4428e97f2d3cae0a28abcbbc1fe5.

- 2026-09-25T20:56:19+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-25T20:56:49+00:00: Recorded command exit 0; command argv SHA-256
  d14685a76261418fffc0205bec68cecb43459972ecb2bbaad05a7b94c04c8325.

- 2026-09-25T20:57:14+00:00: Recorded command exit 0; command argv SHA-256
  774bf46c6db00054ab193ffa19a3ab298a4d33097fd40e06ae5e149e0bd08258.

- 2026-09-25T20:57:33+00:00: Recorded command exit 0; command argv SHA-256
  0658879d1d5b26f625fc52e160138717887a8fbfdd4301039e4985a877e9963b.

- 2026-09-25T20:57:55+00:00: Recorded command exit 0; command argv SHA-256
  fa1ab7baafb93a5c0e7df68703a8dc54e6405b9feac8f96ae2133eb43e768cd5.

- 2026-09-25T20:59:02+00:00: Recorded command exit 0; command argv SHA-256
  b7c438686581cf292b6cd41497ceabb3af42dfed57e04dfd6cc89efed8e2d15b.

- 2026-09-25T20:59:49+00:00: Recorded command exit 0; command argv SHA-256
  d14685a76261418fffc0205bec68cecb43459972ecb2bbaad05a7b94c04c8325.

- 2026-09-25T21:00:16+00:00: Recorded command exit 0; command argv SHA-256
  8a3f3751a6180c02aa3a46876347518068a6e55412026870dbe48ec3a935de35.

- 2026-09-25T21:00:46+00:00: Heartbeat by ar1453-frontend-orchestration-luna56.

- 2026-09-25T21:00:49+00:00: AR-1453 central control adapter implemented in signed+DCO commit
  ceac822. RunnerBackend now admits and executes PlanFile runs via asb-orchestrator, cancellation
  invokes the service, strict-replay/local plans remain declarative, live mode fails closed. Focused
  control suite 42/42 and clippy -p asb-cli pass after exact rebase onto origin/main 452f3ca;
  worktree clean and branch unpublished.

- 2026-09-25T21:00:57+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-25T21:01:21+00:00: Recorded command exit 0; command argv SHA-256
  3ef4cc9ad8371beabf92f1b879124cc1fa576afdc4bd18427e4094ca951d4d86.

- 2026-09-25T21:02:20+00:00: Recorded command exit 0; command argv SHA-256
  681994a9b7b368ece8b133aae9b6f6ac982dd6a4869c3ca5fb59dcb9ad68604a.

- 2026-09-25T21:03:29+00:00: Recorded command exit 0; command argv SHA-256
  60bb8f3f25b6d5fa719aeb85aef0a2d4ff47b28fdee180edbb7506974086103b.

- 2026-09-25T21:04:20+00:00: Recorded command exit 0; command argv SHA-256
  75c4463fda736f04d1c1dd98b2fda9f27aa1920aa8b83710e8e18641e5d6f801.

- 2026-09-25T21:05:02+00:00: Full local gates completed after synchronization: workspace tests
  passed, workspace clippy -D warnings passed, rustdoc with -D warnings passed, and cargo build
  --locked --workspace --release --offline passed. Exact product base is origin/main
  452f3ca29390ab37cf3aff8c813b92b54b163b20; branch head ceac822ad15da1747fc8b7ad824a68928de663a0;
  clean and intentionally unpublished. Prior PR #328 post-merge topology/base mismatch is addressed
  by this exact-base rebase. No independent review or hosted CI is claimed yet.

- 2026-09-25T21:06:51+00:00: Recorded command exit 0; command argv SHA-256
  2de0599724ad2ddf9fedf7c82d84ebb43b6c13b8e88bdf2336b7f2bebfe85079.

- 2026-09-25T21:07:16+00:00: Recorded command exit 0; command argv SHA-256
  0693d4efce5c7265b1c239efcded91fea3eb3ee256a8ddb4252ead25aee4889f.

- 2026-09-25T21:07:42+00:00: Published PR #332:
  https://github.com/martin-beck/agent-systems-benchmark/pull/332. Remote branch exact head
  ceac822ad15da1747fc8b7ad824a68928de663a0; exact base origin/main
  452f3ca29390ab37cf3aff8c813b92b54b163b20. Push and PR creation completed through handoffctl run.
  No review or hosted CI result is claimed yet.

- 2026-09-25T21:07:51+00:00: Recorded command exit 0; command argv SHA-256
  3ea06150297690e3ebf34ff22524675b021adcd9c417bb6e275ae371d8b601a9.

- 2026-09-25T21:14:03+00:00: Heartbeat by ar1453-frontend-orchestration-luna56.

- 2026-09-25T21:20:49+00:00: Independent review identified two P1 blockers:
  PlanAuthoritySource::execute currently calls generic run_point without consuming/matching the
  cassette digest, so StrictReplay is not actually replay-authority/network-denied; execute_until
  ignores its deadline and can exceed RunLimits.timeout_ms. Repair work started on existing PR
  branch; no merge.

- 2026-09-25T21:24:02+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-25T21:24:21+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-25T21:24:41+00:00: Recorded command exit 101; command argv SHA-256
  d14685a76261418fffc0205bec68cecb43459972ecb2bbaad05a7b94c04c8325.

- 2026-09-25T21:24:56+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-25T21:25:17+00:00: Recorded command exit 101; command argv SHA-256
  d14685a76261418fffc0205bec68cecb43459972ecb2bbaad05a7b94c04c8325.

- 2026-09-25T21:26:58+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-25T21:27:17+00:00: Recorded command exit 1; command argv SHA-256
  5444fad693413a8acf738a7c260d813d9cb839116b2b27ea534dfd284e6bf800.

- 2026-09-25T21:27:38+00:00: Recorded command exit 101; command argv SHA-256
  c3d582497e41ab0c67fe1d1552fb93068330722d02997a197b0507b6d4dc1a21.

- 2026-09-25T21:28:16+00:00: Recorded command exit 101; command argv SHA-256
  9423a4598d7b999f1cd3f9edc4479d0c0f9ac9dd0ebdc9cba576c3b1d25a24a3.

- 2026-09-25T21:28:40+00:00: Recorded command exit 101; command argv SHA-256
  9423a4598d7b999f1cd3f9edc4479d0c0f9ac9dd0ebdc9cba576c3b1d25a24a3.

- 2026-09-25T21:28:57+00:00: Recorded command exit 0; command argv SHA-256
  9423a4598d7b999f1cd3f9edc4479d0c0f9ac9dd0ebdc9cba576c3b1d25a24a3.

- 2026-09-25T21:29:23+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-25T21:31:24+00:00: Recorded command exit 0; command argv SHA-256
  d33c9b987658c3342aa1bf30f83a840cf8f7af0a4f9384d6d2c233b4d96e317f.

- 2026-09-25T21:31:40+00:00: Recorded command exit 0; command argv SHA-256
  7767d939d679aff4591a037b2342797bb19eb9cbe89589821b972e032ad8d8ac.

- 2026-09-25T21:32:09+00:00: Repair implementation committed signed+DCO as
  6bf03b57601ccbbdccbee7beda2d9512f1060a1e. Added declarative replay_cassette_path, authenticated
  cassette digest verification/consumption via StrictReplayService, authority-only strict replay
  execution, deadline watchdog cancellation, and positive/negative tests. New strict-replay tests
  pass. Focused control suite command cargo test -p asb-cli --lib control::tests:: --offline did not
  terminate cleanly: active_worker_retains_exclusive_state_ownership_until_terminal_commit and
  unix_frontend_disconnect_does_not_stop_real_run failed, and
  production_backend_runs_without_frontend_and_recovers_idempotency exceeded 60s before manual
  interruption. Do not push or request review until these regressions are repaired.

- 2026-09-25T21:34:32+00:00: Recorded command exit 101; command argv SHA-256
  7bf1fd2597db0f35be8dcb7308a30c3f3bdc255c2bd88e06e9fd14d0a2e169df.

- 2026-09-25T21:35:02+00:00: Recorded command exit 101; command argv SHA-256
  10def93a62f9bb6177e5ec5d8be7402c1b1dfff370657557211be56c78ae5fda.

- 2026-09-25T21:35:19+00:00: Recorded command exit 101; command argv SHA-256
  d8e2b1c482230f0ea8fd18ac2ec12432d76f8a7a962adbf31b389682cad34c5c.

- 2026-09-25T21:35:41+00:00: Recorded command exit 101; command argv SHA-256
  d8e2b1c482230f0ea8fd18ac2ec12432d76f8a7a962adbf31b389682cad34c5c.

- 2026-09-25T21:36:20+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-25T21:36:45+00:00: Recorded command exit 101; command argv SHA-256
  7bf1fd2597db0f35be8dcb7308a30c3f3bdc255c2bd88e06e9fd14d0a2e169df.

- 2026-09-25T21:37:04+00:00: Recorded command exit 101; command argv SHA-256
  d8e2b1c482230f0ea8fd18ac2ec12432d76f8a7a962adbf31b389682cad34c5c.

- 2026-09-25T21:37:37+00:00: Recorded command exit 101; command argv SHA-256
  d8e2b1c482230f0ea8fd18ac2ec12432d76f8a7a962adbf31b389682cad34c5c.

- 2026-09-25T21:38:20+00:00: Recorded command exit 101; command argv SHA-256
  7bf1fd2597db0f35be8dcb7308a30c3f3bdc255c2bd88e06e9fd14d0a2e169df.

- 2026-09-25T21:38:46+00:00: Recorded command exit 101; command argv SHA-256
  10def93a62f9bb6177e5ec5d8be7402c1b1dfff370657557211be56c78ae5fda.

- 2026-09-25T21:39:40+00:00: Recorded command timeout; classification=SUBPROCESS_TIMEOUT;
  deadline=30.0s; command argv SHA-256
  0e256f585b701352feb0376171b0f5bd96863b913d11972dadf71ed035cdaa9a.

- 2026-09-25T21:40:09+00:00: Recorded command exit 1; command argv SHA-256
  f104fcee4fa16c1a5c5c402b01fd49fa4fb211f2c8757fbad4f3ea8c0fd848ed.

- 2026-09-25T21:40:26+00:00: Recorded command exit 0; command argv SHA-256
  6120de36aaf3f41dd6cadb792c3fccfa2bc059e1af956c26b16aabbc0ee7bbd5.

- 2026-09-25T21:40:45+00:00: Recorded command exit 0; command argv SHA-256
  4c7008506dd55cc81e6f6942f72895fe63c002f3303fe016409e02d62fdb7b3f.

- 2026-09-25T21:41:17+00:00: Isolated reproductions after authority-only strict replay:
  active_worker_retains_exclusive_state_ownership_until_terminal_commit fails final expected
  Completed (observed non-completed state); unix_frontend_disconnect_does_not_stop_real_run fails
  its nonterminal-state assertion; production_backend_runs_without_frontend_and_recovers_idempotency
  reaches test timeout (30s). Added signed+DCO commit 4db5c4d attempting to preserve completed
  strict replay across recovery without fabricating artifacts, but these regressions remain. No push
  or PR update made.

- 2026-09-25T21:41:38+00:00: Recorded command exit 101; command argv SHA-256
  d8e2b1c482230f0ea8fd18ac2ec12432d76f8a7a962adbf31b389682cad34c5c.

- 2026-09-25T21:49:20+00:00: Recorded command exit 0; command argv SHA-256
  7c730eec3ea71bd24ffc5a9255bf7f542481bf601dba6c72bed6e00f6c2fab3c.

- 2026-09-25T21:49:48+00:00: Recorded command exit 0; command argv SHA-256
  d117a7741fcc133444534ecec6079500e111b48bd4327805566605d0f5fdf990.
