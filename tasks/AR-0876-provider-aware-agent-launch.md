---
{
  "branch": "feature/provider-aware-agent-launch",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0102",
    "AR-0103",
    "AR-0313",
    "AR-0316",
    "AR-0317",
    "AR-0318",
    "AR-0319",
    "AR-0320",
    "AR-0869"
  ],
  "id": "AR-0876",
  "next_action": "Freeze and independently review the provider-aware launch contract before acquiring serialized asb-agents/asb-cli/Cargo fences.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "",
  "plan": "../plans/AR-0876.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "open",
  "summary": "Apply validated provider selections at the authoritative agent launch boundary and reject conflicting runtime configuration.",
  "task_revision": 2,
  "title": "Wire provider-aware agent launches",
  "updated_at": "2026-09-09T00:30:52+00:00",
  "worktree_key": "agent-systems-benchmark-provider-aware-agent-launch"
}
---
## AR-0876

Close the AR-0869 execution-wiring gap by making its content-addressed provider selection an
authoritative input to the actual adapter process launch, rather than provenance-only metadata.

Implementation has not started. Read the linked plan before claiming.


- 2026-09-09T00:30:52+00:00: AR-0871 is merged and fully verified; AR-0876 is the highest-priority
  dependency-ready leaf that closes provider-selection execution wiring.
