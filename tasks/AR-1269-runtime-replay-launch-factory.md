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
  "next_action": "Integrate ReplayLaunchBundle consumption into CLI transport and add real supervised cassette/lifecycle/egress/no-fallback fixtures.",
  "observed_branch": "feature/ar-1269-runtime-replay-launch-factory",
  "observed_dirty": 1,
  "observed_head": "83bc5e72edf0b3f96927f205c19e44a402d27dcf",
  "owner": "asb_ar1024_lifecycle_router",
  "plan": "../plans/AR-1269.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Create runtime-owned launch bundles for supervised strict replay.",
  "task_revision": 15,
  "title": "Runtime-owned replay launch-bundle factory",
  "updated_at": "2026-09-16T23:00:54+00:00",
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
