---
{
  "branch": "feature/ar-1370-runner-authority-materialization",
  "checkpoint_commit": "0c6dc52e1f4aa5854f73081711dbd9a5bc1a5d7c",
  "claim_expires": "",
  "depends_on": [
    "AR-1288",
    "AR-1369"
  ],
  "id": "AR-1370",
  "next_action": "Remain planned until AR-1369 dependency is resolved; then add authenticated RunnerBackend/Catalog authority injection and receipt-source tests without synthetic authority.",
  "observed_branch": "feature/ar-1370-runner-authority-materialization",
  "observed_dirty": 0,
  "observed_head": "0c6dc52e1f4aa5854f73081711dbd9a5bc1a5d7c",
  "owner": "",
  "plan": "../plans/AR-1370-runner-authority-materialization.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Inject existing authenticated certificate authority and runtime enrollment material into RunnerBackend/Catalog for receipt issuance.",
  "task_revision": 1,
  "title": "Runner authority materialization",
  "updated_at": "2026-09-24T01:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1370-runner-authority-materialization"
}
---

Narrow repair for the RunnerBackend/Catalog source gap. Do not touch asb-tui,
resume stale AR-1329 metadata, or synthesize trust/launch authority.
