---
{
  "branch": "test/mockagents-executable-qualification",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0888",
    "AR-0889"
  ],
  "id": "AR-0896",
  "next_action": "Qualify the exact MockAgents v0.5.0 executable against the complete hostile synthetic protocol and isolation suite; do not unblock AR-0890 unless every required case passes.",
  "owner": "",
  "plan": "../plans/AR-0896.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "open",
  "summary": "Qualify one pinned MockAgents executable before deterministic-double CI integration.",
  "task_revision": 2,
  "title": "Qualify the pinned MockAgents executable",
  "updated_at": "2026-09-09T09:55:13+00:00",
  "worktree_key": "agent-systems-benchmark-mockagents-executable-qualification"
}
---
## AR-0896

Qualify only MockAgents v0.5.0 as the candidate executable selected for further
consideration by AR-0890. This repair AR exists because AR-0888 retained all four
candidates as `untested`; it must not substitute README claims or the ASB-owned
synthetic fixture for black-box executable evidence.

- 2026-09-09T09:55:13+00:00: Promote dependency-ready MockAgents executable qualification for the
  development loop.
