---
{
  "branch": "chore/asb-tui-branch-policy-context",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1065",
  "next_action": "A repository maintainer must remove the stale legacy required-status context from asb-tui main while retaining the app-scoped GitHub Actions check, then re-evaluate PR #26.",
  "owner": "",
  "plan": "../plans/AR-1065.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Normalize asb-tui main branch protection so successful GitHub Actions checks can merge.",
  "task_revision": 1,
  "title": "Normalize asb-tui branch required-status policy",
  "updated_at": "2026-09-14T11:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-branch-policy-context"
}
---

PR #26 and the earlier PRs #24 and #25 have successful GitHub Actions check-runs but remain
`BLOCKED`. The `main` branch protection rule contains both the app-scoped check
`Rust, supply-chain, and privacy gates` (app id 15368) and a legacy `contexts` entry with the same
name. The legacy commit-status endpoint is empty/pending because the workflow emits a check-run,
not a legacy status. This AR records the repository-administration repair; no source, workflow,
credential, or CI evidence must be changed to mask the mismatch.

