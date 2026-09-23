---
{
  "branch": "feature/ar-1358-runtime-enrollment-cli-dispatch",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1357"],
  "id": "AR-1358",
  "next_action": "Promote after AR-1357 is done, then wire asb run/sweep through runtime-attested enrollment records with fail-closed positive and negative tests.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1358-runtime-enrollment-cli-dispatch.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Consume runtime-attested enrollment records in asb run and sweep without exposing authority.",
  "task_revision": 1,
  "title": "Runtime enrollment CLI dispatch",
  "updated_at": "2026-09-24T00:30:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1358-runtime-enrollment-cli-dispatch"
}
---

Coordinator-created consumer repair for AR-1329 after AR-1357 delivered the
runtime-owned record transport. Do not touch asb-tui or weaken replay/offline
gates.

- 2026-09-24T00:30:00+00:00: Created because AR-1329's remaining dispatch gap is
  distinct from the completed runtime transport primitive.
