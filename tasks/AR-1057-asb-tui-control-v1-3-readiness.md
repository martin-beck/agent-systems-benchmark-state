---
{
  "branch": "docs/asb-tui-control-v1-3-readiness",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-11T07:02:03+00:00",
  "depends_on": [],
  "id": "AR-1057",
  "next_action": "Bind the standalone client and measurement-selection UX roadmap to ASB control v1.3 precise diagnostics with closed v1.2 fallback behavior.",
  "owner": "codex-ar1057-asb-tui-control-v1-3-readiness-20260911",
  "plan": "../plans/AR-1057.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Make standalone asb-tui consume precise privacy-safe measurement validation diagnostics.",
  "task_revision": 4,
  "title": "Harden asb-tui control v1.3 readiness",
  "updated_at": "2026-09-11T05:03:41+00:00",
  "worktree_key": "agent-systems-benchmark-state-asb-tui-control-v1-3-readiness"
}
---

Audit the additive ASB control v1.3 measurement-selection diagnostic contract and amend only the
standalone asb-tui roadmap. Require the client shell to negotiate and parse v1.3 precisely while
retaining the closed v1.2 legacy categories, and require the selector UX to present exact trusted
reasons without reflecting attacker-controlled identifiers. Do not change either product repository
or any feature-task status.

- 2026-09-11T05:02:00+00:00: Authorized state-only control-contract readiness correction;
  dependencies are empty and all product-task statuses remain unchanged.

- 2026-09-11T05:02:03+00:00: Claimed by codex-ar1057-asb-tui-control-v1-3-readiness-20260911.

- 2026-09-11T05:03:41+00:00: Recorded command exit 0; command argv SHA-256
  1c427f7b027f91880a93d5d4fcd18eab9c929a070f728ce5a732cb8aa5b315e8.
