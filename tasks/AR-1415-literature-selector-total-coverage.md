---
{
  "branch": "codex/ar-1415-literature-selector-total-coverage",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-24T19:43:43+00:00",
  "depends_on": [
    "AR-1410",
    "AR-1414"
  ],
  "id": "AR-1415",
  "next_action": "Promote after AR-1414 is done; audit every docs-listed workload against the registry, generated catalog, selector filters, and plan validation.",
  "owner": "ar1415-literature-selector-total-coverage-luna56",
  "plan": "../plans/AR-1415.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Make the complete literature workload inventory selectable beside built-in software-engineering fixtures with truthful evidence gates.",
  "task_revision": 3,
  "title": "Total literature workload selector coverage",
  "updated_at": "2026-09-24T17:43:43+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1415"
}
---

This AR closes the selector contract across every benchmark and framework-derived
workload recorded in `docs/WORKLOADS.md`, `docs/RELATED_WORK.md`, and the
versioned registry. It must not download datasets, contact providers, or promote
provenance-only records to executable or qualified status.

Acceptance requires a machine-checked parity table showing that each registry ID
has a stable family/kind, source and dataset revision, selector entry, generated
documentation entry, and an explicit evidence state. Built-in and literature
workloads must appear in one deterministic inventory, while missing evaluator,
license, image, reset, or platform evidence causes selection to remain visibly
unavailable and execution to fail closed before network/provider access. Unknown,
duplicate, stale, or hand-edited IDs are rejected with positive and negative tests.

Verify selector filters, plan validation, doctor/catalog output, generated docs,
schema parity, and full exact-head/post-merge gates.

- 2026-09-24T17:42:37+00:00: Dependencies AR-1410 and AR-1414 are durably done; begin total
  literature selector coverage audit.

- 2026-09-24T17:43:43+00:00: Claimed by ar1415-literature-selector-total-coverage-luna56.
