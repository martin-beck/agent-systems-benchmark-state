---
{
  "branch": "feature/provider-registry",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0310"
  ],
  "id": "AR-1100",
  "next_action": "Define the embedded registry contract, loader, canonical digest and registry-driven catalog after the provider-profile contract exists.",
  "observed_branch": "feature/provider-registry",
  "observed_dirty": 0,
  "observed_head": "03fd87bc40df557f891e1f56eaf2742a151b63ab",
  "owner": "",
  "plan": "../plans/AR-1100.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Add a machine-readable provider registry and make the provider catalog digest-pinned and registry-driven.",
  "task_revision": 2,
  "title": "Add the machine-readable provider registry foundation",
  "updated_at": "2026-09-22T10:16:39+00:00",
  "worktree_key": "agent-systems-benchmark-provider-registry"
}
---
Add the embedded machine-readable provider registry that replaces the hard-coded provider catalog with
a validated, digest-pinned data source, keeping every existing CLI contract byte-identical.
Repository: `martin-beck/agent-systems-benchmark`.

- 2026-09-13T09:57:00+00:00: Frozen scope for parallel setup-wizard series AR-1100..AR-1106.
  Registry is embedded at compile time, validated strictly, and its canonical digest feeds
  `provider-catalog`; the catalog output and digest must remain byte-identical to today.
