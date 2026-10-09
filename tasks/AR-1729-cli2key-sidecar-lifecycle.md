---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1728"
  ],
  "id": "AR-1729",
  "next_action": "Promote after AR-1728; implement the runtime-owned sidecar lifecycle and hostile cleanup/privacy tests.",
  "owner": "",
  "plan": "../plans/AR-1729-cli2key-sidecar-lifecycle.md",
  "priority": "P1",
  "schema_version": 1,
  "spec_ref": "specs/AR-1729.json",
  "spec_revision": 1,
  "status": "open",
  "summary": "Add a runtime-owned loopback sidecar lifecycle with a fresh per-invocation client key, private staging, bounded cleanup, and secret-safe evidence.",
  "task_revision": 2,
  "title": "Supervise cli2key sidecar and ephemeral key",
  "updated_at": "2026-10-09T07:37:33+00:00",
  "worktree_key": ""
}
---

Implement a runtime-owned supervisor for the exact bridge selected by AR-1728.
Bind only to the loopback interface on a kernel-selected port and generate a fresh random
client key with at least 256 bits of entropy for each ASB run or sweep.

Keep key material out of argv, logs, reports, manifests, coordinator state, and
environment dumps. Prefer inherited descriptors; if the bridge requires files,
use an invocation-private 0700 root and 0600 no-follow file, then remove it on
all exits. Kill and reap the complete sidecar process group on success, error,
timeout, cancellation, or caller death. The sidecar alone receives upstream
egress; benchmark agents remain loopback-only.

- 2026-10-09T07:37:33+00:00: AR-1728 is done at exact main 30286af; dependencies verified
