---
{
  "branch": "feature/ar-1353-runtime-enrollment-cli-dispatch",
  "checkpoint_commit": "21bd6deca45e6bce7461c3cdef20ce2390aca5bd",
  "claim_expires": "2026-09-23T22:47:51+00:00",
  "depends_on": [
    "AR-1352"
  ],
  "id": "AR-1353",
  "next_action": "Implement runtime-owned enrollment transport for opaque LiveProviderRuntimeHandle, then replace injected live factory in asb run/sweep with positive/negative dispatch tests.",
  "observed_branch": "feature/ar-1353-runtime-enrollment-cli-dispatch",
  "observed_dirty": 0,
  "observed_head": "21bd6deca45e6bce7461c3cdef20ce2390aca5bd",
  "owner": "codex-asb-ar1329-live-cli-luna56",
  "plan": "../plans/AR-1353-runtime-enrollment-cli-dispatch.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Add runtime-owned enrollment and opaque live CLI dispatch.",
  "task_revision": 3,
  "title": "Runtime enrollment and CLI dispatch",
  "updated_at": "2026-09-23T20:47:51+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1353-runtime-enrollment-cli-dispatch"
}
---

Successor repair for AR-1349's exact remaining gap: AR-1352 bootstrap is
private and tested, but no safe cross-crate enrollment source delivers its
opaque handle to asb-cli. AR-1349 checkpoint and evidence remain preserved;
AR-1329 stays fail-closed until this seam is merged.

- 2026-09-23T20:47:37+00:00: AR-1352 is merged and supplies the private bootstrap. Promote this
  downstream enrollment/CLI dispatch repair; AR-1349 and AR-1329 remain fail-closed consumers.

- 2026-09-23T20:47:51+00:00: Claimed by codex-asb-ar1329-live-cli-luna56.
