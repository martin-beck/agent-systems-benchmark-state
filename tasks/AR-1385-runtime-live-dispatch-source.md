---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-24T06:46:29+00:00",
  "depends_on": [
    "AR-1384",
    "AR-1377",
    "AR-1373",
    "AR-1380",
    "AR-1381"
  ],
  "id": "AR-1385",
  "next_action": "Promote after dependency validation; materialize the authenticated runtime-owned live dispatch source consumed by asb run and sweep, with fail-closed positive and negative tests.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "codex-asb-ar1329-repair-luna56",
  "plan": "../plans/AR-1385-runtime-live-dispatch-source.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Materialize the authenticated runtime-owned live dispatch source for production asb run and sweep.",
  "task_revision": 3,
  "title": "Authenticated runtime live dispatch source",
  "updated_at": "2026-09-24T05:46:29+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1385-runtime-live-dispatch-source"
}
---

This coordinator repair closes the remaining AR-1329 boundary after AR-1384.
It must consume only the authenticated opaque runtime handle and enrolled
control state, then provide the existing scheduler/CLI dispatch seam without
accepting caller-supplied endpoints, credentials, policy, roots, tools,
namespace identity, or launch authority.


- 2026-09-24T05:45:34+00:00: AR-1384 done and audited; coordinator repair successor for
  authenticated runtime-owned live dispatch source; dependencies verified

- 2026-09-24T05:46:29+00:00: Claimed by codex-asb-ar1329-repair-luna56.
