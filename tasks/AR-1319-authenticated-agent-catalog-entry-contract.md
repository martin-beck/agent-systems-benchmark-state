---
{
  "branch": "feature/ar-1319-authenticated-agent-catalog-entry-contract",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1310"],
  "id": "AR-1319",
  "next_action": "Define and test a versioned catalog entry shape that represents unavailable or incomplete agents without fabricated package or provenance metadata, then hand the contract to AR-1316.",
  "owner": "",
  "plan": "../plans/AR-1319.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Make incomplete authenticated agent catalog entries truthful and selectable only after verification.",
  "task_revision": 1,
  "title": "Authenticated agent catalog entry contract",
  "updated_at": "2026-09-21T00:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1319-authenticated-agent-catalog-entry-contract"
}
---

The current AgentCatalog wire type requires complete package and provenance
metadata for every entry, while the checked-in ASB inventory cannot prove those
fields for any agent. Define an additive/versioned representation for visible
but unavailable entries so the first-run wizard can explain the roster without
claiming that an unverified agent is selectable.
