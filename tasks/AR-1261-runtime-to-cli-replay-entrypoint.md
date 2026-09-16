---
{
  "branch": "feature/ar-1261-runtime-to-cli-replay-entrypoint",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-16T22:48:40+00:00",
  "depends_on": [
    "AR-1237",
    "AR-1238",
    "AR-1239"
  ],
  "id": "AR-1261",
  "next_action": "Promote after AR-1260 is resolved or superseded; implement the typed runtime-to-CLI handoff entrypoint and prove supervised replay lifecycle.",
  "observed_branch": "feature/ar-1261-runtime-to-cli-replay-entrypoint",
  "observed_dirty": 0,
  "observed_head": "0ff179226254a988362b09404841ae51d9ec7d18",
  "owner": "asb_ar1024_lifecycle_router",
  "plan": "../plans/AR-1261.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Provide a runtime-owned entrypoint for strict-replay CLI supervision.",
  "task_revision": 8,
  "title": "Runtime-to-CLI strict-replay handoff entrypoint",
  "updated_at": "2026-09-16T20:50:07+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1261-runtime-cli"
}
---

## AR-1261

Implement the narrow runtime-to-CLI authority handoff required to make AR-1260 reachable while
preserving fail-closed ownership and bounded lifecycle evidence.

- 2026-09-16T20:46:00+00:00: Created as successor to the reviewed AR-1260 blocker; the CLI
  cannot safely fabricate runtime-issued launch context from plan/artifact paths alone.

- 2026-09-16T20:47:14+00:00: Promote runtime-to-CLI successor after verifying AR-1237/38/39 done and
  avoiding AR-1260 dependency cycle.

- 2026-09-16T20:47:40+00:00: Claimed by asb_ar1024_lifecycle_router.

- 2026-09-16T20:48:40+00:00: Heartbeat by asb_ar1024_lifecycle_router.

- 2026-09-16T20:49:07+00:00: Recorded command exit 1; command argv SHA-256
  71566be2fa7fa50c21ce8e300d6a7308ac0a0cf46a2ff59a6158b54ccb2e4f3a.

- 2026-09-16T20:49:48+00:00: Recorded command exit 1; command argv SHA-256
  3c56d3015f3989a488485c942f50060e3011fb38c4714628b88baf543e137642.
