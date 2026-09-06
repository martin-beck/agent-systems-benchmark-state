---
{
  "branch": "feature/provider-profile-contract",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-0101", "AR-1001"],
  "id": "AR-0310",
  "next_action": "Define a versioned credential-free provider profile and exact adapter capability negotiation.",
  "owner": "",
  "plan": "../plans/AR-0310.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Normalize one provider configuration for safe translation across heterogeneous agent adapters.",
  "task_revision": 1,
  "title": "Define common provider profiles",
  "updated_at": "2026-09-06T21:14:10+00:00",
  "worktree_key": "agent-systems-benchmark-provider-profile-contract"
}
---
## AR-0310

Normalize one provider configuration for safe translation across heterogeneous agent adapters.

Profiles contain no credentials. Every adapter must negotiate which normalized fields it can honor
exactly and fail closed on unsupported or lossy translations.

Implementation has not started. Read the linked plan before claiming.
