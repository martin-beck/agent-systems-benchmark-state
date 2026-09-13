---
{
  "branch": "feature/tui-configuration-center",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1014", "AR-1025", "AR-1033", "AR-1160"],
  "id": "AR-1034",
  "next_action": "Implement the non-secret configuration center foundation after the visual system and ASB wizard control API are stable; AR-1170 owns provider, authentication and default integration.",
  "owner": "",
  "plan": "../plans/AR-1034.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Add a searchable configuration menu for frontend preferences and benchmark defaults.",
  "task_revision": 5,
  "title": "Add the standalone TUI configuration center",
  "updated_at": "2026-09-13T17:05:57+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-configuration-center"
}
---
Implement the configuration UI and non-secret preference persistence in `martin-beck/asb-tui`.
ASB remains the authority for runner configuration, validation and benchmark execution.

- 2026-09-10T21:04:37+00:00: Excluded runner configuration mutation and required reuse of
  AR-1014's canonical validated measurement-selection plan for stored presets.

- 2026-09-13T17:05:57+00:00: Added the negotiated ASB configuration contract and standalone
  wizard control API as a dependency. AR-1170 owns provider/default mutation calls and
  secret-enrollment presentation, preserving this AR's non-secret preference-store scope.

- 2026-09-10T21:25:00+00:00: Added exact XDG and import/export byte, item, string and nesting bounds
  plus fail-closed assertions that preserve the last valid store and leave no temporary artifacts.

- 2026-09-11T04:12:48+00:00: Added bounded deterministic setting search and explicit filtered-action
  scope tests; stored values and secret-shaped content may never enter the search index.
