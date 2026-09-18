---
{
  "branch": "feature/ar-1309-reviewed-capacity-or-model-reduction",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1307", "AR-1308"],
  "id": "AR-1309",
  "next_action": "Remain planned until the coordinator reviews the AR-1308 terminal OOM evidence and selects a separately scoped capacity contract or model-reduction profile; do not rerun or widen AR-1307 limits.",
  "owner": "",
  "plan": "../plans/AR-1309.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Provide a reviewed successor contract after terminal full-exhaustive capacity OOM.",
  "task_revision": 1,
  "title": "Reviewed full-exhaustive capacity or model-reduction contract",
  "updated_at": "2026-09-18T19:10:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1309-reviewed-capacity-or-model-reduction"
}
---

## AR-1309

AR-1308's final disposable networkless QEMU run reached liveness checking for
4200 seconds and failed closed with Java out of memory after 46,920,678
generated states, 38,735,235 distinct states and 10,722,623 queued states. No
attestation was emitted. This planned successor must first choose and review a
distinct contract; it must not silently rerun the same workload, widen the
existing AR-1307 process envelope, or claim qualification from a reduced model.
