---
{
  "schema_version": 1,
  "id": "AR-1477",
  "title": "Cover authority resolver behavior",
  "status": "planned",
  "priority": "P0",
  "summary": "Raise exact hosted coverage above the enforced 90 percent floor for the authority resolver.",
  "next_action": "Promote after validating completed dependencies, then reproduce the 89.88 percent exact-head coverage failure and add behavioral tests.",
  "task_revision": 1,
  "updated_at": "2026-09-27T05:08:00+00:00",
  "owner": "",
  "claim_expires": "",
  "worktree_key": "agent-systems-benchmark-ar-1477-authority-resolver-coverage-tests",
  "branch": "feature/ar-1477-authority-resolver-coverage-tests",
  "checkpoint_commit": "",
  "plan": "../plans/AR-1477-authority-resolver-coverage-tests.md",
  "depends_on": ["AR-1200", "AR-1379", "AR-1472"]
}
---

Successor created from the exact hosted coverage failure on synchronized
PR #345. It must add real behavioral coverage or prove instrumentation drift;
the coverage floor remains unchanged.

- 2026-09-27T05:08:00+00:00: Created after job 108554587959 reported 89.88%
  coverage at exact synchronized head `c21d1ce5`, below the required 90%.
