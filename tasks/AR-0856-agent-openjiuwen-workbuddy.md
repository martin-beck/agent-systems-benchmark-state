---
{
  "branch": "feature/agents-openjiuwen-workbuddy",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0101",
    "AR-0102",
    "AR-0103",
    "AR-0310",
    "AR-0315",
    "AR-0317",
    "AR-0503",
    "AR-0855"
  ],
  "id": "AR-0856",
  "next_action": "After AR-0855 releases, verify every dependency is durably done, promote, and pin executable OpenJiuwen and WorkBuddy source, license, package, protocol, and platform identities before implementing adapters.",
  "owner": "",
  "plan": "../plans/AR-0856.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Add independently pinned, capability-accurate OpenJiuwen and WorkBuddy adapters with credential-free live and strict replay qualification.",
  "task_revision": 2,
  "title": "Add OpenJiuwen and WorkBuddy agent support",
  "updated_at": "2026-09-08T18:44:30+00:00",
  "worktree_key": "agent-systems-benchmark-agents-openjiuwen-workbuddy"
}
---
## AR-0856

Add OpenJiuwen and WorkBuddy only through independently pinned adapter boundaries. Neither agent is
listed as supported until its exact executable distribution, complete license closure, protocol,
credential-free loopback journey, and strict replay conformance are executable and green on a
declared platform.

AR-0101, AR-0102, AR-0103, AR-0310, AR-0315, AR-0317, and AR-0503 are durably done. AR-0855
remains a temporary serialization dependency because its repository-wide first-party source-header
repair can overlap adapter registration; keep this task planned until that dependency releases.
