---
{
  "branch": "feature/ar-1781-external-workload-acquisition-catalog",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1760"],
  "id": "AR-1781",
  "next_action": "Define the authoritative development external-workload catalog and make every documented suite installable, selectable, and executable through its pinned official source.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1781-external-workload-acquisition-catalog.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {"evidence_class": "contract-test", "evidence_digest": "", "evidence_ref": "", "spec_ref": "specs/AR-1781.json", "spec_revision": 2, "status": "pending"},
  "spec_ref": "specs/AR-1781.json",
  "spec_revision": 2,
  "status": "planned",
  "summary": "Make every documented external AI-agent workload a pinned, development-supported ASB workload, including SWE-mini.",
  "task_revision": 2,
  "title": "External workload acquisition catalog",
  "updated_at": "2026-10-10T09:49:36+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1781-external-workload-acquisition-catalog"
}
---

Create the dedicated authoritative catalog behind `asb workload`. The initial
development-supported set is `agentbench`, `agentdojo`, `agentops`,
`ai-agents-that-matter`, `aider-polyglot`, `bigcodebench`, `core-bench`,
`evalplus`, `exercism-tracks`, `hal`, `harbor`, `helm`, `inspect-ai`,
`livecodebench`, `swe-bench`, `swe-bench-pro`, `swe-fficiency`, `swe-lancer`,
`swe-mini`, `swe-perf`, `swe-rebench`, `tau-bench`, and `terminal-bench`.
Inventory any subsequently documented external suite in the same way and define
its official primary source, immutable dataset/release
identity, digest/signature/provenance checks, license/terms, supported platform,
size/resource requirements, required preparation/runtime dependencies, bounded
normalization recipe, workload adapter entrypoint, and compatibility limits.

An external workload is a data/bundle lifecycle, not a tool executable. Do not
reuse `asb tool` records, accept arbitrary URLs, scrape moving upstream state, or
download datasets merely because they appear in a catalog. In development,
absence of a production release authorization, signature, or hosted verification
must not demote a documented suite to methodology-only or block its catalog entry,
installation, selection, or bounded execution. Preserve pinned source identity
and explicit legal/resource constraints; report genuine license, compatibility,
or source failures distinctly. Production qualification may remain separately
labelled.
