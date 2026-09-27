---
{
  "branch": "feature/ar-1480-runtime-control-cli-composition",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1473", "AR-1472"],
  "id": "AR-1480",
  "next_action": "Promote after validating AR-1473 and AR-1472, then claim the isolated worktree and implement the opaque runtime-control CLI composition.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1480-runtime-control-cli-composition.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Compose authenticated runtime enrollment into opaque normal CLI run and sweep dispatch.",
  "task_revision": 1,
  "title": "Runtime-control CLI composition",
  "updated_at": "2026-09-27T00:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1480-runtime-control-cli-composition"
}
---

Successor to the stale AR-1374/1375 adapter chain. AR-1473 and AR-1472 are
the only implementation dependencies; live provider reachability is optional
and never gates local qualification.

- The composition must preserve opaque authority and fail closed on missing,
  stale, revoked, replayed, mismatched, or caller-supplied inputs.
- Qualification uses deterministic local/mock/replay evidence only.
