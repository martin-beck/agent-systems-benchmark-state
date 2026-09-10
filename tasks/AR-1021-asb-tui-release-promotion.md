---
{
  "branch": "feature/asb-tui-release-promotion",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1017", "AR-1018", "AR-1019", "AR-1020", "AR-0877", "AR-0906"],
  "id": "AR-1021",
  "next_action": "Independently audit the extension and document its optional/unverified or verified release channel.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1021.md",
  "priority": "P2",
  "schema_version": 1,
  "status": "planned",
  "summary": "Audit and promote asb-tui from optional extension to verified release when eligible.",
  "task_revision": 1,
  "title": "Audit and promote the asb-tui release channel",
  "updated_at": "2026-09-10T00:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-release-promotion"
}
---
Run independent source, license, SBOM, provenance, security, protocol, platform, UX, and exact-head
CI audits. Maintain an explicitly labelled optional/unverified channel until every policy and formal
requirement passes; only then promote the same user workflow to the verified release channel.

Acceptance criteria: public installation/upgrade workflows, capability matrix, evidence limits,
artifact cleanup policy, signed release provenance, and documented promotion/rollback criteria.
