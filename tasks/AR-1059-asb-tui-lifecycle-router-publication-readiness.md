---
{
  "branch": "docs/asb-tui-lifecycle-router-publication-readiness",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1059",
  "next_action": "Bind AR-1024 to the exact rebase, environment, process-cleanup, no-daemon and trusted-pin gates required before lifecycle-router publication.",
  "owner": "",
  "plan": "../plans/AR-1059.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Harden the ASB lifecycle-router roadmap before rebasing and publishing it.",
  "task_revision": 1,
  "title": "Harden lifecycle-router publication readiness",
  "updated_at": "2026-09-11T05:15:10+00:00",
  "worktree_key": "agent-systems-benchmark-state-asb-tui-lifecycle-router-publication-readiness"
}
---

Convert the AR-1024 readiness audit into explicit dependency, rebase, privacy-safe environment,
post-spawn cleanup, no-daemon and final pin acceptance. This task changes coordination state only:
ASB remains responsible for verified lifecycle routing and process ownership, while all renderer,
Ratatui, Crossterm, widgets, screens and interactive application behavior remain exclusively in
`martin-beck/asb-tui`.

