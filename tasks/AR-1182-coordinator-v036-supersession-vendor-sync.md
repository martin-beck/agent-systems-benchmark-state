---
{
  "branch": "feature/ar-1182-coordinator-v036-vendor-sync",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1182",
  "next_action": "Read the plan; verify the signed v0.3.6 tag and run the supported vendor sync in an isolated state worktree.",
  "owner": "",
  "plan": "../plans/AR-1182.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Consume coordinator v0.3.6 and repair the verified vendor pin for supersession readiness.",
  "task_revision": 1,
  "title": "Coordinator v0.3.6 supersession vendor synchronization",
  "updated_at": "2026-09-14T21:06:00+02:00",
  "worktree_key": "agent-systems-benchmark-coordinator-v036-vendor-sync"
}
---

Synchronize only the coordinator runtime in this ASB state repository to the exact
signed immutable `martin-beck/agent-workflow-coordinator` release `v0.3.6`
(`a1bc4459f884ce447e8ee2884df12ea3ff4b710b`).

The current v0.3.5 vendor snapshot has a digest mismatch caused by a downstream
patch; the supported sync must replace that patch and regenerate the complete
allowlisted manifest. Verify the annotated tag signature independently, run vendor
verification, state/schema/generated-view/privacy checks, and the applicable formal
and integration tests. Do not modify ASB product code, asb-tui, or unrelated
coordinator paths. Preserve historical AR evidence and unrelated dirty work.

Acceptance requires exact release/tag/signature and manifest evidence, no downstream
patches in vendored files, signed DCO commit, independent exact-head review, and
green required CI before promoting this AR or unblocking dependent lifecycle work.
