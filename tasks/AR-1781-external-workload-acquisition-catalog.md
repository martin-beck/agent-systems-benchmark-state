---
{
  "branch": "feature/ar-1781-external-workload-acquisition-catalog",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1760"],
  "id": "AR-1781",
  "next_action": "Define the authoritative external AI-agent workload catalog, primary sources, immutable dataset/bundle identities, licenses, preparation recipes, and compatibility metadata.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1781-external-workload-acquisition-catalog.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {"evidence_class": "contract-test", "evidence_digest": "", "evidence_ref": "", "spec_ref": "specs/AR-1781.json", "spec_revision": 1, "status": "pending"},
  "spec_ref": "specs/AR-1781.json",
  "spec_revision": 1,
  "status": "planned",
  "summary": "Define pinned official acquisition and preparation recipes for every externally sourced AI-agent workload, including SWE-mini where supported.",
  "task_revision": 1,
  "title": "External workload acquisition catalog",
  "updated_at": "2026-10-10T09:49:36+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1781-external-workload-acquisition-catalog"
}
---

Create the dedicated authoritative catalog behind `asb workload`. Inventory every
external AI-agent testing workload ASB supports or advertises—including SWE-mini
where eligible—and define its official primary source, immutable dataset/release
identity, digest/signature/provenance checks, license/terms, supported platform,
size/resource requirements, required preparation/runtime dependencies, bounded
normalization recipe, workload adapter entrypoint, and compatibility limits.

An external workload is a data/bundle lifecycle, not a tool executable. Do not
reuse `asb tool` records, accept arbitrary URLs, scrape moving upstream state, or
download datasets merely because they appear in a catalog. Unsupported, restricted,
license-incompatible, unavailable, too-large, missing-proof, and incompatible
workloads must remain separate actionable states.
