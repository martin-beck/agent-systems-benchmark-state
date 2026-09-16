---
{
  "branch": "feature/ar-1269-runtime-replay-launch-factory",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T00:57:53+00:00",
  "depends_on": [
    "AR-1237",
    "AR-1238",
    "AR-1239"
  ],
  "id": "AR-1269",
  "next_action": "Integrate ReplayLaunchBundle::spawn with CLI transport and add runtime-backed cassette/lifecycle/egress/no-fallback fixtures.",
  "observed_branch": "feature/ar-1269-runtime-replay-launch-factory",
  "observed_dirty": 2,
  "observed_head": "8dfafaa8378e38c25d3fc0eb566ad32e9c9d3fff",
  "owner": "asb_ar1024_lifecycle_router",
  "plan": "../plans/AR-1269.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Create runtime-owned launch bundles for supervised strict replay.",
  "task_revision": 24,
  "title": "Runtime-owned replay launch-bundle factory",
  "updated_at": "2026-09-16T23:02:38+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1269-runtime-launch-factory"
}
---
## AR-1269

Implement the missing runtime launch-bundle factory required for real supervised replay. Preserve
AR-1268's blocked transport evidence and never move launch authority into the CLI.

- 2026-09-16T22:57:30+00:00: Dependencies are done; AR-1268 identifies the missing runtime-owned
  launch-bundle factory required for safe supervised replay.

- 2026-09-16T22:57:53+00:00: Claimed by asb_ar1024_lifecycle_router.

- 2026-09-16T22:58:22+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T22:58:34+00:00: Recorded command exit 101; command argv SHA-256
  176cab5b29a40fa8794f09725ed51520aae1b944c519cabbe22bf8591c02577a.

- 2026-09-16T22:58:57+00:00: Initial runtime-focused command exited 101 because new
  ReplayLaunchBundle::issue is intentionally runtime-only and unused under -D warnings. This is
  compile hygiene, not behavior failure; add narrow dead_code allowance and rerun. Worktree has only
  fresh AR-1269 factory files and is not based on predecessor branches.

- 2026-09-16T22:59:08+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T22:59:20+00:00: Recorded command exit 0; command argv SHA-256
  176cab5b29a40fa8794f09725ed51520aae1b944c519cabbe22bf8591c02577a.

- 2026-09-16T22:59:29+00:00: Recorded command exit 0; command argv SHA-256
  2625a6dd2f86c7318b487da9ed8d34523f48c096a706ee1e68a1472d28b4b542.

- 2026-09-16T22:59:38+00:00: Recorded command exit 0; command argv SHA-256
  266e0812ef7b023ea146df7585a5b4ddaf541a7c2c597393d78e0dd3c70e58c5.

- 2026-09-16T22:59:57+00:00: Signed checkpoint 83bc5e7 adds runtime-owned ReplayLaunchBundle
  factory. issue validates namespace readiness, denied network policy, and benchmark lease class
  before retaining SandboxBackend, SandboxLaunchInput, ResourceLease, pinned supervisor/sidecar
  commands; consume moves the complete authority exactly once. Runtime focused suite passes 39/39
  and fmt passes; product tree clean. Real CLI supervised cassette/lifecycle integration remains
  next.

- 2026-09-16T23:00:47+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T23:01:00+00:00: Recorded command exit 0; command argv SHA-256
  176cab5b29a40fa8794f09725ed51520aae1b944c519cabbe22bf8591c02577a.

- 2026-09-16T23:01:09+00:00: Recorded command exit 0; command argv SHA-256
  4a18e083893e7fc19d120c9b0ddd184e47428b0f5be03ee5d7ca84c288b88614.

- 2026-09-16T23:01:18+00:00: Recorded command exit 0; command argv SHA-256
  a6c7608736904d1aba80c0d9e003930e4f16d9c33670f4205b362d43e433a142.

- 2026-09-16T23:01:36+00:00: Signed checkpoint 8dfafaa adds ReplayLaunchBundle::spawn, which
  consumes its retained runtime-owned SandboxBackend/SandboxLaunchInput/ResourceLease and invokes
  spawn_launch without caller substitution. Runtime focused suite passes 39/39 and fmt pass; product
  tree clean. CLI bundle consumption, cassette request/response, egress, cancellation/restart,
  timeout/crash cleanup, and no-fallback fixtures remain next.

- 2026-09-16T23:02:03+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T23:02:30+00:00: Recorded command exit 0; command argv SHA-256
  f489a19876782722ed16d09ca01ff72aa074415a2bb4183d7206b5819538e360.

- 2026-09-16T23:02:38+00:00: Recorded command exit 0; command argv SHA-256
  548e9842fb94dcbf41ccd31e01e7f76dbde4b129bb6b7caa6a5d732f66a60e4a.
