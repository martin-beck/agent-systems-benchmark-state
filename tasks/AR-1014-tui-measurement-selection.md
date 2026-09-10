---
{
  "branch": "feature/tui-measurement-selection",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1013", "AR-0804", "AR-0805"],
  "id": "AR-1014",
  "next_action": "Implement the catalog-driven TUI selection flow after AR-1013 is reviewed and merged.",
  "owner": "",
  "plan": "../plans/AR-1014.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Let users select grouped measurements from the standalone ASB TUI.",
  "task_revision": 2,
  "title": "Add grouped measurement selection to the TUI",
  "updated_at": "2026-09-10T19:20:00+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-measurement-selection"
}
---
Expose the measurement catalog in the standalone TUI with semantic-group navigation and drill-down:
users can select/deselect an entire group, enter a group, and independently select/deselect each
measurement. Provide search, multi-select, per-metric descriptions/units/support, presets,
reset/backtracking, and a final review that shows exactly what will be collected. Selections must be part of the validated run plan,
remain explicit for live versus replay, and fail closed when a platform/provider cannot support them.

Acceptance criteria: keyboard and narrow/resize-safe layouts; non-interactive/exported configuration
equivalence; deterministic plan hashes; clear unsupported and overhead warnings; unit, selection,
serialization, resize, and accessibility-oriented terminal tests.

Repository boundary: implement every view, interaction, renderer, state transition, and terminal
test in `martin-beck/asb-tui`; consume the ASB measurement catalog only through its public contract.
