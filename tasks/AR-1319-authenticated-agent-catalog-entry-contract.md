---
{
  "branch": "feature/ar-1319-authenticated-agent-catalog-entry-contract",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1310"],
  "id": "AR-1319",
  "next_action": "Completed; preserve the merged contract as the prerequisite for AR-1316 producer and future verified release-index work.",
  "owner": "",
  "plan": "../plans/AR-1319.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "done",
  "summary": "Make incomplete authenticated agent catalog entries truthful and selectable only after verification.",
  "task_revision": 2,
  "title": "Authenticated agent catalog entry contract",
  "updated_at": "2026-09-21T01:54:48+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1319-authenticated-agent-catalog-entry-contract"
}
---

The current AgentCatalog wire type requires complete package and provenance
metadata for every entry, while the checked-in ASB inventory cannot prove those
fields for any agent. Define an additive/versioned representation for visible
but unavailable entries so the first-run wizard can explain the roster without
claiming that an unverified agent is selectable.
Completion evidence: ASB PR #244 merged at `851a8bc47194e0ad320c9dd02518d8c79eacdbb7` after exact-head hosted schema, Rust, policy, fuzz, formal-model, platform, and supply-chain gates. The merged contract accepts explicit incomplete entries without fabricated package/provenance metadata and excludes response-only `refreshed` from the catalog digest.
