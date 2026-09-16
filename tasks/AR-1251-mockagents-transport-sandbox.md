---
{
  "branch": "feature/ar-1251-mockagents-transport-sandbox",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-0888", "AR-0889"],
  "id": "AR-1251",
  "next_action": "Design and implement bounded transport/sandbox fixture for MockAgents tool-result, cancellation/backpressure, network-denial, cleanup, and arm64 evidence.",
  "observed_branch": "feature/ar-1251-mockagents-transport-sandbox",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1251.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Add a bounded transport and sandbox fixture for MockAgents qualification.",
  "task_revision": 1,
  "title": "Add MockAgents transport sandbox fixture",
  "updated_at": "2026-09-16T11:02:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1251"
}
---

Implement only the linked AR-1251 plan using ASB development documentation and handoffctl.
Use immutable artifacts from AR-1249/1250, keep all execution offline and credential-free, and
preserve privacy, network-denial, signature, DCO, and exact-tree gates.
