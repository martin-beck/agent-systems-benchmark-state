---
{
  "branch": "feature/ar-1480-runtime-control-cli-composition",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-27T13:17:30+00:00",
  "depends_on": [
    "AR-1473",
    "AR-1472"
  ],
  "id": "AR-1480",
  "next_action": "Promote after validating AR-1473 and AR-1472, then claim the isolated worktree and implement the opaque runtime-control CLI composition.",
  "observed_branch": "feature/ar-1480-runtime-control-cli-composition",
  "observed_dirty": 0,
  "observed_head": "a53c1cfb817e627b7d573405a669a246625026d3",
  "owner": "ar1332-record-replay-luna56",
  "plan": "../plans/AR-1480-runtime-control-cli-composition.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Compose authenticated runtime enrollment into opaque normal CLI run and sweep dispatch.",
  "task_revision": 6,
  "title": "Runtime-control CLI composition",
  "updated_at": "2026-09-27T11:18:08+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1480-runtime-control-cli-composition"
}
---

Successor to the stale AR-1374/1375 adapter chain. AR-1473 and AR-1472 are
the only implementation dependencies; live provider reachability is optional
and never gates local qualification.

- The composition must preserve opaque authority and fail closed on missing,
  stale, revoked, replayed, mismatched, or caller-supplied inputs.
- Qualification uses deterministic local/mock/replay evidence only.

- 2026-09-27T11:17:28+00:00: AR-1473 and AR-1472 are durably done; promote dependency-safe CLI
  composition successor with no circular AR-1374/1375 edge.

- 2026-09-27T11:17:30+00:00: Claimed by ar1332-record-replay-luna56.

- 2026-09-27T11:17:41+00:00: Recorded command exit 0; command argv SHA-256
  31ef8dba69cadb96f0eab7a54672aa35e58192283fa68f6c82d04e7f76edc9be.

- 2026-09-27T11:18:08+00:00: Recorded command exit 0; command argv SHA-256
  e5e483509179e2d1e0604ee0f63271ced6232cbfb60eb6ccdf9fe0c6ad23a76a.
