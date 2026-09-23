---
{
  "schema_version": 1,
  "id": "AR-1341",
  "title": "Runtime-observed namespace attestation repair",
  "status": "planned",
  "priority": "P0",
  "summary": "Repair AR-1340 so live relay capabilities require runtime-observed child namespace agreement.",
  "next_action": "Promote after AR-1339 is verified done; implement runtime-observed identity comparison and copied/stale/mismatch denial evidence before AR-1340 or AR-1329 advances.",
  "task_revision": 1,
  "updated_at": "2026-09-23T10:40:00+00:00",
  "owner": "",
  "claim_expires": "",
  "worktree_key": "agent-systems-benchmark-ar-1341-runtime-observed-namespace-repair",
  "branch": "feature/ar-1341-runtime-observed-namespace-repair",
  "checkpoint_commit": "",
  "plan": "../plans/AR-1341.md",
  "depends_on": ["AR-1339"]
}
---

PR #257 merged at `3406faa` despite the AR-1340 security hold. The merged
implementation exposes `NamespaceIdentity::current()` but does not use it at
the production child-launch boundary; validation trusts a caller-supplied
identity. This repair must close that gap before AR-1329 or AR-1338 can consume
the live-provider path. Preserve the hold and record all repair evidence in
this task.
