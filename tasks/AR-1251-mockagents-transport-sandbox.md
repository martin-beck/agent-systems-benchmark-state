---
{
  "branch": "feature/ar-1251-mockagents-transport-sandbox",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-16T13:01:57+00:00",
  "depends_on": [
    "AR-0888",
    "AR-0889"
  ],
  "id": "AR-1251",
  "next_action": "Design and implement bounded transport/sandbox fixture for MockAgents tool-result, cancellation/backpressure, network-denial, cleanup, and arm64 evidence.",
  "observed_branch": "feature/ar-1251-mockagents-transport-sandbox",
  "observed_dirty": 0,
  "observed_head": "128ecddbfdb7fcfff6e257adf3237b5866aca481",
  "owner": "asb_ar1251_transport_sandbox",
  "plan": "../plans/AR-1251.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Add a bounded transport and sandbox fixture for MockAgents qualification.",
  "task_revision": 5,
  "title": "Add MockAgents transport sandbox fixture",
  "updated_at": "2026-09-16T11:02:19+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1251"
}
---

Implement only the linked AR-1251 plan using ASB development documentation and handoffctl.
Use immutable artifacts from AR-1249/1250, keep all execution offline and credential-free, and
preserve privacy, network-denial, signature, DCO, and exact-tree gates.

- 2026-09-16T11:01:38+00:00: AR-1250 established current HTTP harness cannot safely prove
  transport/sandbox lifecycle; promote bounded fixture successor.

- 2026-09-16T11:01:57+00:00: Claimed by asb_ar1251_transport_sandbox.

- 2026-09-16T11:02:12+00:00: Recorded command exit 0; command argv SHA-256
  4a6249f72de1082dfa350ea55d7b48062a26eb34cb805c8c2cb05a1d5b77118b.
