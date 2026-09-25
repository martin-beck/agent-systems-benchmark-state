---
{
  "branch": "feature/ar-1453-frontend-orchestration-wiring",
  "checkpoint_commit": "ceac822ad15da1747fc8b7ad824a68928de663a0",
  "claim_expires": "2026-09-25T23:00:46+00:00",
  "depends_on": [
    "AR-1452"
  ],
  "id": "AR-1453",
  "next_action": "Run workspace fmt, clippy, tests, docs and build from exact base 452f3ca; then publish signed branch for independent review. Product branch remains unpublished until all applicable gates pass.",
  "observed_branch": "feature/ar-1453-frontend-orchestration-wiring",
  "observed_dirty": 0,
  "observed_head": "ceac822ad15da1747fc8b7ad824a68928de663a0",
  "owner": "ar1453-frontend-orchestration-luna56",
  "plan": "../plans/AR-1453.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Make CLI and control use the central service for every run lifecycle.",
  "task_revision": 36,
  "title": "Route ASB frontends through central orchestration",
  "updated_at": "2026-09-25T21:00:57+00:00",
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
