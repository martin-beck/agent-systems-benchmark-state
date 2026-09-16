---
{
  "branch": "feature/ar-1261-runtime-to-cli-replay-entrypoint",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1237",
    "AR-1238",
    "AR-1239"
  ],
  "id": "AR-1261",
  "next_action": "Promote after AR-1260 is resolved or superseded; implement the typed runtime-to-CLI handoff entrypoint and prove supervised replay lifecycle.",
  "observed_branch": "feature/ar-1261-runtime-to-cli-replay-entrypoint",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "",
  "plan": "../plans/AR-1261.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Provide a runtime-owned entrypoint for strict-replay CLI supervision.",
  "task_revision": 2,
  "title": "Runtime-to-CLI strict-replay handoff entrypoint",
  "updated_at": "2026-09-16T20:47:14+00:00",
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
