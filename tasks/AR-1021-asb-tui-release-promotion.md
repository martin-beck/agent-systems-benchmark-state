---
{
  "branch": "feature/asb-tui-release-promotion",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-10T20:06:31+00:00",
  "depends_on": [
    "AR-1017",
    "AR-1018",
    "AR-1019",
    "AR-1020",
    "AR-0877",
    "AR-0906"
  ],
  "id": "AR-1021",
  "next_action": "Independently audit the extension and document its optional/unverified or verified release channel.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "asb_tui_coordinator_20260910",
  "plan": "../plans/AR-1021.md",
  "priority": "P2",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Audit and promote asb-tui from optional extension to verified release when eligible.",
  "task_revision": 3,
  "title": "Audit and promote the asb-tui release channel",
  "updated_at": "2026-09-10T17:06:31+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-release-promotion"
}
---
Run independent source, license, SBOM, provenance, security, protocol, platform, UX, and exact-head
CI audits. Maintain an explicitly labelled optional/unverified channel until every policy and formal
requirement passes for asb-tui and its exact coordinator and workflow-quality releases; only then
promote the same user workflow to the verified release channel.

Acceptance criteria: public installation/upgrade workflows, capability matrix, evidence limits,
artifact cleanup policy, signed release provenance, and documented promotion/rollback criteria.

- 2026-09-10T17:06:28+00:00: All dependencies are now complete: AR-1017 through AR-1020 are
  published with exact-main hosted and trusted local evidence, and AR-0877/AR-0906 were integrated
  with AR-0907 through all-green combined and exact-main formal/platform gates. Promote for
  independent release-channel audit; retain optional/unverified classification unless signed release
  artifacts and every promotion criterion are proven.

- 2026-09-10T17:06:31+00:00: Claimed by asb_tui_coordinator_20260910.
