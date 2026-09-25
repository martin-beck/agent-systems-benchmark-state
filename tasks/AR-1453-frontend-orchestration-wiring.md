---
{
  "branch": "feature/ar-1453-frontend-orchestration-wiring",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-25T22:54:32+00:00",
  "depends_on": [
    "AR-1452"
  ],
  "id": "AR-1453",
  "next_action": "Complete control lifecycle integration and focused tests, then synchronize the signed branch onto current origin/main 452f3ca before publication; preserve exact-base evidence.",
  "observed_branch": "feature/ar-1453-frontend-orchestration-wiring",
  "observed_dirty": 4,
  "observed_head": "a5eb7e680a3c71813d9d1aae3328a385d6812a95",
  "owner": "ar1453-frontend-orchestration-luna56",
  "plan": "../plans/AR-1453.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Make CLI and control use the central service for every run lifecycle.",
  "task_revision": 20,
  "title": "Route ASB frontends through central orchestration",
  "updated_at": "2026-09-25T20:54:35+00:00",
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
