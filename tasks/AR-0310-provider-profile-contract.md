---
{
  "branch": "feature/provider-profile-contract",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-06T23:07:51+00:00",
  "depends_on": [
    "AR-0101",
    "AR-1001"
  ],
  "id": "AR-0310",
  "next_action": "Define a versioned credential-free provider profile and exact adapter capability negotiation.",
  "observed_branch": "feature/provider-profile-contract",
  "observed_dirty": 1,
  "observed_head": "b7e9078d53a4a4586beb68bf56233aba206112ac",
  "owner": "quality-20260906",
  "plan": "../plans/AR-0310.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Normalize one provider configuration for safe translation across heterogeneous agent adapters.",
  "task_revision": 10,
  "title": "Define common provider profiles",
  "updated_at": "2026-09-06T21:43:45+00:00",
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

- 2026-09-06T21:37:38+00:00: Recorded command exit 0; command argv SHA-256
  f83a5eebd861223334c6a87ec97e8efc27c408440b71a39ccee6d585c599d2f8.

- 2026-09-06T21:37:51+00:00: Heartbeat by quality-20260906.

- 2026-09-06T21:41:17+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.

- 2026-09-06T21:43:31+00:00: Recorded command exit 0; command argv SHA-256
  fdecd0af6596065fdfeac5d3df1d362d2773cde8817fb0ebd96a5e749a0eac4e.

- 2026-09-06T21:43:45+00:00: Recorded command exit 0; command argv SHA-256
  788bf3e8b263ae9546e56ed516b8146e8390addf38f8156e6431f43e16f21c8b.
