---
{
  "branch": "ci/deterministic-llm-double",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-09T12:43:41+00:00",
  "depends_on": [
    "AR-0888",
    "AR-0889"
  ],
  "id": "AR-0890",
  "next_action": "Integrate only the selected exact mock artifact into credential-free CI with fail-closed startup, network denial, provenance, and hostile lifecycle tests.",
  "owner": "contracts_20260906",
  "plan": "../plans/AR-0890.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Add the independently selected deterministic protocol double as a pinned isolated CI test dependency.",
  "task_revision": 5,
  "title": "Integrate a deterministic LLM double in CI",
  "updated_at": "2026-09-09T09:44:43+00:00",
  "worktree_key": "agent-systems-benchmark-deterministic-llm-double-ci"
}
---
## AR-0890

Integrate the one candidate selected by AR-0888 through the AR-0889 contract. If none qualifies, record blocked/rejected evidence instead of choosing ad hoc.

- 2026-09-09T09:43:27+00:00: Dependencies AR-0888 and AR-0889 are durably done and their exact
  product heads are integrated in origin/main; selected CI qualification scope is disjoint from
  active AR-0859 and AR-0891.

- 2026-09-09T09:43:41+00:00: Claimed by contracts_20260906.

- 2026-09-09T09:44:31+00:00: Recorded command exit 0; command argv SHA-256
  5345cd4b5f66285dc80cddfe59c0a95475263f9ff88d25d2639fce3c300aa4b9.

- 2026-09-09T09:44:43+00:00: Recorded command exit 0; command argv SHA-256
  7786ea9c21141d06a16c7c7047071ecd2e2349b4e257f17164b543e4e9c5a951.
