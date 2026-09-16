---
{
  "branch": "feature/ar-1253-pinned-python-transport-runtime",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-16T15:18:50+00:00",
  "depends_on": [
    "AR-1252"
  ],
  "id": "AR-1253",
  "next_action": "Provision and qualify an immutable Python fixture runtime through the approved isolated runner.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "asb_ar1253_python_runtime",
  "plan": "../plans/AR-1253.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Provision pinned Python transport fixture runtime.",
  "task_revision": 3,
  "title": "Provision pinned Python transport fixture runtime",
  "updated_at": "2026-09-16T13:18:50+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1253"
}
---

Implement only the linked AR-1253 plan using ASB development documentation and handoffctl.
Keep runtime images, caches, provenance, and all test activity under `/srv/data/projects`.

- 2026-09-16T13:18:48+00:00: AR-1252 completed with reviewed immutable Python image allowlist and
  exact-head evidence; promote runtime fixture successor.

- 2026-09-16T13:18:50+00:00: Claimed by asb_ar1253_python_runtime.
