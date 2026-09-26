---
{
  "branch": "repair/ar-1466-state-ci-format-repair",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1466",
  "next_action": "Claim the repair, apply only the required Ruff formatting to tools/validate_ar1308_capacity.py, run all applicable state gates, and publish through exact-head CI.",
  "owner": "",
  "plan": "../plans/AR-1466-state-ci-format-repair.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Repair the current state branch's deterministic formatting failure without changing validator behavior.",
  "task_revision": 1,
  "title": "State CI formatting repair",
  "updated_at": "2026-09-26T00:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-state-ar-1466-state-ci-format-repair"
}
---

Created from the exact CI failure on current protected `main`: Ruff format
reports `tools/validate_ar1308_capacity.py` as the only unformatted file.
