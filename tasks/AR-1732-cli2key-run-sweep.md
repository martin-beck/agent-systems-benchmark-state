---
{
  "id": "AR-1732",
  "title": "Integrate cli2key runs and sweeps",
  "priority": "P1",
  "depends_on": ["AR-1731"],
  "plan": "../plans/AR-1732-cli2key-run-sweep.md",
  "summary": "Make explicit cli2key selections executable through normal ASB run and sweep orchestration with bounded concurrency and typed live-development evidence.",
  "status": "planned",
  "next_action": "Promote after AR-1731; integrate cli2key into run and sweep without parallel sidecars, fallback, or attribution drift.",
  "owner": "",
  "claim_expires": "",
  "checkpoint_commit": "",
  "task_revision": 1,
  "schema_version": 1,
  "spec_ref": "specs/AR-1732.json",
  "spec_revision": 1,
  "updated_at": "2026-10-07T23:21:33+00:00",
  "branch": "",
  "worktree_key": ""
}
---

Expose explicit `cli2key` selection through the ordinary `run` and `sweep`
paths. One supervised sidecar lifetime belongs to one run or complete bounded
sweep, with per-attempt capability binding and deterministic teardown. Enforce
the configured sweep concurrency, distinguish proxy queue/transport overhead
from agent latency, and emit typed failures for auth expiry, wrong key, rate
limit, model drift, sidecar crash, timeout, and cancellation. Evidence must say
`development_remote_live` (or an equally explicit reviewed label) and cannot
serve as production or official-provider qualification.
