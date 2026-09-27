---
{
  "branch": "feature/ar-1480-runtime-control-cli-composition",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-27T13:20:14+00:00",
  "depends_on": [
    "AR-1473",
    "AR-1472"
  ],
  "id": "AR-1480",
  "next_action": "Run focused CLI/runtime tests and full gates for opaque runtime-control composition.",
  "observed_branch": "feature/ar-1480-runtime-control-cli-composition",
  "observed_dirty": 2,
  "observed_head": "59323f41ed2d10a952a1276107459260ebdf409a",
  "owner": "ar1332-record-replay-luna56",
  "plan": "../plans/AR-1480-runtime-control-cli-composition.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Compose authenticated runtime enrollment into opaque normal CLI run and sweep dispatch.",
  "task_revision": 15,
  "title": "Runtime-control CLI composition",
  "updated_at": "2026-09-27T11:22:34+00:00",
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

- 2026-09-27T11:20:14+00:00: Heartbeat by ar1332-record-replay-luna56.

- 2026-09-27T11:20:31+00:00: After complete AR-1480 plan/docs review and current-main audit,
  implementation adds RuntimeControlDispatchSource and run_with_runtime_control_source in asb-cli.
  The seam resolves only an opaque LiveProviderRuntimeDispatchSource from runtime/control and fails
  closed before CLI effects when unavailable; docs state ordinary process run/sweep cannot construct
  authority. Added hostile unavailable-source test; no asb-tui/live provider.

- 2026-09-27T11:21:04+00:00: Recorded command exit 0; command argv SHA-256
  b2f3fb06dee43d704705616108ddb13e7dcca021834cb50f5a41e895d2b16eff.

- 2026-09-27T11:21:37+00:00: Recorded command exit 0; command argv SHA-256
  c9a2916a927594a512151f14eab59803113f12061a17b617a103789a4ff6a824.

- 2026-09-27T11:22:04+00:00: Recorded command exit 0; command argv SHA-256
  b7a391741901b8aade6d43c13786c703d443b46d94efdaa27c0f02fa2d51a198.

- 2026-09-27T11:22:34+00:00: Recorded command exit 0; command argv SHA-256
  c44ed960f90bd281b4395dd1445881d59d09fa681f7e317ba9f0254abb8780d1.
