---
{
  "branch": "feature/ar-1384-runtime-bootstrap-materialization",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1383",
    "AR-1377",
    "AR-1373",
    "AR-1380",
    "AR-1381"
  ],
  "id": "AR-1384",
  "next_action": "Promote and claim after validating all dependencies; implement the private runtime/control conversion from the authenticated authority profile to an opaque live runtime handle, with fail-closed tests.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "",
  "plan": "../plans/AR-1384-runtime-bootstrap-materialization.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Materialize the runtime-owned live bootstrap handle from authenticated authority.",
  "task_revision": 2,
  "title": "Runtime-owned bootstrap materialization",
  "updated_at": "2026-09-24T05:09:18+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1384-runtime-bootstrap-materialization"
}
---

AR-1383 supplies only the authenticated opaque authority profile. This task
owns the remaining private conversion to the existing live provisioner handle;
it must not accept caller authority or synthesize enrolled values.

- 2026-09-24T05:09:18+00:00: Dependencies AR-1383, AR-1377, AR-1373, AR-1380, and AR-1381 verified
  terminal done; begin private runtime-owned bootstrap materialization.
