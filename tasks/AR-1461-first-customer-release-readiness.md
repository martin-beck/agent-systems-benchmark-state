---
{
  "branch": "release/ar-1461-first-customer-release-readiness",
  "checkpoint_commit": "36d4bdf35a644a36a8acfdb31078eb7f668a17c4",
  "claim_expires": "2026-09-26T20:05:21+00:00",
  "depends_on": [
    "AR-1456",
    "AR-1460"
  ],
  "id": "AR-1461",
  "next_action": "Audit the established ASB release workflow against exact qualified main 36d4bdf35a644a36a8acfdb31078eb7f668a17c4, build the reproducible first-customer bundle, run release gates, and publish only if all required checks and release evidence pass; otherwise create a precise repair AR.",
  "observed_branch": "release/ar-1461-first-customer-release-readiness",
  "observed_dirty": 0,
  "observed_head": "36d4bdf35a644a36a8acfdb31078eb7f668a17c4",
  "owner": "coordinator-ar1461-release",
  "plan": "../plans/AR-1461.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Prepare and publish the first-customer ASB release from the currently qualified main.",
  "task_revision": 8,
  "title": "First-customer release readiness and publication",
  "updated_at": "2026-09-26T19:06:41+00:00",
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

- 2026-09-26T19:05:18+00:00: Current-main AR-1460 qualification is green at exact 36d4bdf; audit
  established release workflow before publication.

- 2026-09-26T19:05:21+00:00: Claimed by coordinator-ar1461-release.

- 2026-09-26T19:05:58+00:00: Recorded command exit 0; command argv SHA-256
  2e1ae39a626814ee52afd37ca2ad04ed38a36a8d0c3ab1e0e3e1efe3babcd4da.

- 2026-09-26T19:06:12+00:00: Recorded command exit 0; command argv SHA-256
  503f8680998a0b610210a032ce25132adb2d806d47bfeb5181f8624d310b94a1.

- 2026-09-26T19:06:27+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.

- 2026-09-26T19:06:41+00:00: Recorded command exit 0; command argv SHA-256
  46f8c01f5323975f73b1b628f98d287169d9bbd7a137f3fb2ea8d74866b73ae0.
