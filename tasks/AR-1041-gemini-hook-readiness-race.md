---
{
  "branch": "fix/gemini-hook-readiness-race",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1041",
  "next_action": "Reproduce the readiness-file truncate/write race with deterministic barriers, then implement atomic publication and fail-closed bounded observation.",
  "owner": "",
  "plan": "../plans/AR-1041.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Eliminate the load-sensitive Gemini hook readiness race without weakening validation.",
  "task_revision": 2,
  "title": "Make Gemini hook readiness publication atomic",
  "updated_at": "2026-09-11T00:41:34+00:00",
  "worktree_key": "agent-systems-benchmark-gemini-hook-readiness-race"
}
---

PR #135 exposed a repeatable test race: concurrent stress can read the readiness file after shell
truncate and before `printf` completes, causing a false `HookUnavailable`. Repair the publication
and observation protocol with deterministic race tests; do not broaden Gemini capabilities or add
any TUI code.

- 2026-09-11T00:41:34+00:00: Live PR #135 failure is stress-reproduced with a deterministic
  truncate/write observation race; independent narrow repair is ready and path-disjoint from current
  integration.
