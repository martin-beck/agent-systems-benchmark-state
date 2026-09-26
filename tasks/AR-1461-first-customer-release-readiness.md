---
{
  "branch": "release/ar-1461-first-customer-release-readiness",
  "checkpoint_commit": "36d4bdf35a644a36a8acfdb31078eb7f668a17c4",
  "claim_expires": "",
  "depends_on": [
    "AR-1456",
    "AR-1460"
  ],
  "id": "AR-1461",
  "next_action": "Audit the established ASB release workflow against exact qualified main 36d4bdf35a644a36a8acfdb31078eb7f668a17c4, build the reproducible first-customer bundle, run release gates, and publish only if all required checks and release evidence pass; otherwise create a precise repair AR.",
  "owner": "",
  "plan": "../plans/AR-1461.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Prepare and publish the first-customer ASB release from the currently qualified main.",
  "task_revision": 1,
  "title": "First-customer release readiness and publication",
  "updated_at": "2026-09-26T20:35:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1461-first-customer-release-readiness"
}
---

This AR is the release boundary after current-main first-customer
qualification. It must consume the exact qualified protected-main commit,
preserve the credential-free local/mock and offline boundaries, build a
reproducible bundle, run the established source, privacy, formal, supply-chain
and artifact checks, and publish only through the documented release workflow.
External signing authority is optional where the established workflow permits;
no gate may be weakened. No asb-tui or remote-provider dependency is added.
