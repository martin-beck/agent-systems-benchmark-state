---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1395",
    "AR-1399"
  ],
  "id": "AR-1396",
  "next_action": "Promote after AR-1395 and AR-1399 are done, then wire every registry-backed literature family into catalog, plan validation, CLI selection, replay and reports.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "",
  "plan": "../plans/AR-1396-literature-workload-selection.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "open",
  "summary": "Make qualified literature workload families selectable beside built-in ASB software-engineering fixtures.",
  "task_revision": 2,
  "title": "Literature workload selection",
  "updated_at": "2026-09-24T10:04:59+00:00",
  "worktree_key": ""
}
---

This AR owns user-facing selection and evidence labeling after the registry and
adapters exist; it does not bypass licensing, acquisition, evaluator, or
platform gates.

- 2026-09-24T10:04:59+00:00: AR-1395 and AR-1399 are done; the registry has 22 validated records.
  Begin explicit catalog/plan/CLI/replay/report selection with fail-closed evidence labels.
