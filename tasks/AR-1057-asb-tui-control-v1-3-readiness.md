---
{
  "branch": "docs/asb-tui-control-v1-3-readiness",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1057",
  "next_action": "Bind the standalone client and measurement-selection UX roadmap to ASB control v1.3 precise diagnostics with closed v1.2 fallback behavior.",
  "owner": "",
  "plan": "../plans/AR-1057.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Make standalone asb-tui consume precise privacy-safe measurement validation diagnostics.",
  "task_revision": 1,
  "title": "Harden asb-tui control v1.3 readiness",
  "updated_at": "2026-09-11T05:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-state-asb-tui-control-v1-3-readiness"
}
---

Audit the additive ASB control v1.3 measurement-selection diagnostic contract and amend only the
standalone asb-tui roadmap. Require the client shell to negotiate and parse v1.3 precisely while
retaining the closed v1.2 legacy categories, and require the selector UX to present exact trusted
reasons without reflecting attacker-controlled identifiers. Do not change either product repository
or any feature-task status.
