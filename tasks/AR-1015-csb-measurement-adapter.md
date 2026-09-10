---
{
  "branch": "feature/csb-measurement-adapter",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1013", "AR-0601", "AR-0602", "AR-0604"],
  "id": "AR-1015",
  "next_action": "Inventory pinned CSB signals and implement only contract-compatible adapters after the catalog is accepted.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1015.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Import qualified CSB resource, system-statistics, and contention measurements into ASB.",
  "task_revision": 1,
  "title": "Add a pinned, provenance-safe CSB measurement adapter",
  "updated_at": "2026-09-10T00:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-csb-measurement-adapter"
}
---
Inspect the pinned CSB project at source level and map compatible measurements into AR-1013 groups.
Implement an optional adapter with explicit version/license/provenance, platform capability checks,
sampling overhead and loss accounting, causal-control metadata, and fail-closed behavior for missing
or ambiguous signals. Do not claim support from README descriptions alone.

Acceptance criteria: source-pinned inventory, typed mapping fixtures, native x86_64 and required
emulated-AArch64 checks, negative tests for unavailable counters and double counting, privacy review,
and documentation of unsupported distributions/architectures.
