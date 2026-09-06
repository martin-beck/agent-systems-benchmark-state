---
{
  "branch": "feature/provider-profile-contract",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-06T22:18:39+00:00",
  "depends_on": [
    "AR-0101",
    "AR-1001"
  ],
  "id": "AR-0310",
  "next_action": "Define a versioned credential-free provider profile and exact adapter capability negotiation.",
  "observed_branch": "feature/provider-profile-contract",
  "observed_dirty": 0,
  "observed_head": "b7e9078d53a4a4586beb68bf56233aba206112ac",
  "owner": "quality-20260906",
  "plan": "../plans/AR-0310.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Normalize one provider configuration for safe translation across heterogeneous agent adapters.",
  "task_revision": 4,
  "title": "Define common provider profiles",
  "updated_at": "2026-09-06T21:37:36+00:00",
  "worktree_key": "agent-systems-benchmark-provider-profile-contract"
}
---
## AR-0310

Normalize one provider configuration for safe translation across heterogeneous agent adapters.

Profiles contain no credentials. Every adapter must negotiate which normalized fields it can honor
exactly and fail closed on unsupported or lossy translations.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-06T21:33:37+00:00: Dependencies AR-0101 and AR-1001 are durably done; promote the
  credential-free provider contract for isolated implementation under the coordinator Cargo/schema
  fence.

- 2026-09-06T21:33:39+00:00: Claimed by quality-20260906.
