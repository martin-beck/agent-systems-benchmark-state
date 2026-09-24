---
{
  "branch": "codex/ar-1415-literature-selector-total-coverage",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-24T19:44:30+00:00",
  "depends_on": [
    "AR-1410",
    "AR-1414"
  ],
  "id": "AR-1415",
  "next_action": "Promote after AR-1414 is done; audit every docs-listed workload against the registry, generated catalog, selector filters, and plan validation.",
  "observed_branch": "codex/ar-1415-literature-selector-total-coverage",
  "observed_dirty": 0,
  "observed_head": "6925c3c443b77aa41ec9578e49cc19b01447c869",
  "owner": "ar1415-literature-selector-total-coverage-luna56",
  "plan": "../plans/AR-1415.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Make the complete literature workload inventory selectable beside built-in software-engineering fixtures with truthful evidence gates.",
  "task_revision": 11,
  "title": "Total literature workload selector coverage",
  "updated_at": "2026-09-24T17:46:08+00:00",
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

- 2026-09-24T17:44:30+00:00: Heartbeat by ar1415-literature-selector-total-coverage-luna56.

- 2026-09-24T17:44:33+00:00: Recorded command exit 0; command argv SHA-256
  d04aa803a9fcb854b247572f9b417fd1935a57ca978bb887d2e7c188e99db043.

- 2026-09-24T17:44:48+00:00: Recorded command exit 0; command argv SHA-256
  b04e51d6a8a1cd1d991d96d1b0eeb7f5236f1056ccb95c8f404b26c181dc4797.

- 2026-09-24T17:45:14+00:00: Recorded command exit 0; command argv SHA-256
  6d84b6c7a75bca49c1a5594b7910983c9f45896fc7e3ba41443bffcbde813b6e.

- 2026-09-24T17:45:40+00:00: Recorded command exit 0; command argv SHA-256
  1de9d400e80b59c921d5cbedad1b9627b802704da17704cb1fc71db3235d7814.

- 2026-09-24T17:45:54+00:00: Recorded command exit 0; command argv SHA-256
  73d343fb1b1db6e5e62ebcb1555147e3fb3f2aeb698d7e44ffac3efc7ad50480.

- 2026-09-24T17:46:08+00:00: Recorded command exit 0; command argv SHA-256
  e6dd053754e1bbb8a92a06522822584d6e44618e0bd9be2e2e5511ba5d555182.
