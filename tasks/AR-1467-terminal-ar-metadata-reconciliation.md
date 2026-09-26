---
{
  "branch": "repair/ar-1467-terminal-ar-metadata-reconciliation",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1467",
  "next_action": "Promote after reviewing the listed completed ARs and verifying each terminal claim against immutable evidence.",
  "owner": "",
  "plan": "../plans/AR-1467-terminal-ar-metadata-reconciliation.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "open",
  "summary": "Remove stale historical next-action text from recently completed ASB AR records without changing implementation or gates.",
  "task_revision": 2,
  "title": "Terminal AR metadata reconciliation",
  "updated_at": "2026-09-26T22:25:00+00:00",
  "worktree_key": "agent-systems-benchmark-state-ar-1467-terminal-ar-metadata-reconciliation"
}
---

This coordinator-only repair is limited to terminal metadata. It must not
reopen completed implementation work, alter product or asb-tui repositories,
replace missing formal evidence, or turn optional cross-repository work into an
ASB release dependency.

- 2026-09-26T22:25:00+00:00: Dependencies are empty; begin bounded terminal metadata audit.
