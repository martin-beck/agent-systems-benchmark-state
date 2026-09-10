---
{
  "branch": "feature/tui-measurement-selection",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1013", "AR-0804", "AR-0805", "AR-1025", "AR-1033", "AR-1036"],
  "id": "AR-1014",
  "next_action": "Implement the catalog-driven TUI selection flow after AR-1013 is reviewed and merged.",
  "owner": "",
  "plan": "../plans/AR-1014.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Let users select grouped measurements from the standalone ASB TUI.",
  "task_revision": 5,
  "title": "Add grouped measurement selection to the TUI",
  "updated_at": "2026-09-10T21:04:37+00:00",
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

- 2026-09-10T20:57:16+00:00: Sharpened acceptance to require a visible search field, tri-state
  group counts, whole-group selection/clearing, drill-down, and independent per-measure toggles in
  the actual standalone application after AR-1025 and its visual system.

- 2026-09-10T21:04:37+00:00: Added AR-1036 so the UI consumes a real bounded catalog operation and
  required exact group-state transitions and plan round-trip fixtures.

- 2026-09-10T21:40:00+00:00: Marked AR-0804 and AR-0805 as read-only migration inputs that cannot
  reopen ASB UI implementation paths.
