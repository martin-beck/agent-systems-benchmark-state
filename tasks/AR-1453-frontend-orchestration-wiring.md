---
{
  "branch": "feature/ar-1453-frontend-orchestration-wiring",
  "checkpoint_commit": "ceac822ad15da1747fc8b7ad824a68928de663a0",
  "claim_expires": "2026-09-25T23:14:03+00:00",
  "depends_on": [
    "AR-1452"
  ],
  "id": "AR-1453",
  "next_action": "Repair P1 review blockers on PR #332: enforce strict replay through runtime-issued cassette authority with digest consumption and enforce execute_until deadline; add positive/negative tests, then rerun gates and push a new signed+DCO head for fresh review.",
  "observed_branch": "feature/ar-1453-frontend-orchestration-wiring",
  "observed_dirty": 2,
  "observed_head": "ceac822ad15da1747fc8b7ad824a68928de663a0",
  "owner": "ar1453-frontend-orchestration-luna56",
  "plan": "../plans/AR-1453.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Make CLI and control use the central service for every run lifecycle.",
  "task_revision": 51,
  "title": "Route ASB frontends through central orchestration",
  "updated_at": "2026-09-25T21:24:41+00:00",
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
