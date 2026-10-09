---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-09T15:16:24+00:00",
  "depends_on": [
    "AR-1731"
  ],
  "id": "AR-1732",
  "next_action": "Promote after AR-1731; integrate cli2key into run and sweep without parallel sidecars, fallback, or attribution drift.",
  "owner": "codex-asb-ar1732-run-sweep-20261009",
  "plan": "../plans/AR-1732-cli2key-run-sweep.md",
  "priority": "P1",
  "schema_version": 1,
  "spec_ref": "specs/AR-1732.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Make explicit cli2key selections executable through normal ASB run and sweep orchestration with bounded concurrency and typed live-development evidence.",
  "task_revision": 3,
  "title": "Integrate cli2key runs and sweeps",
  "updated_at": "2026-10-09T13:16:24+00:00",
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

- 2026-10-09T13:16:21+00:00: AR-1731 is durably accepted/released with hosted post-merge receipt;
  promote cli2key run/sweep integration.

- 2026-10-09T13:16:24+00:00: Claimed by codex-asb-ar1732-run-sweep-20261009.
