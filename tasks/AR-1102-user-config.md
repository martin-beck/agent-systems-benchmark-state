---
{
  "branch": "feature/user-config",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0310",
    "AR-1100"
  ],
  "id": "AR-1102",
  "next_action": "Define the versioned user configuration contract with defaults, per-agent overrides and a canonical config digest.",
  "observed_branch": "feature/user-config",
  "observed_dirty": 0,
  "observed_head": "aee25937f4e35ab44f227c524631769abec964fa",
  "owner": "",
  "plan": "../plans/AR-1102.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Add the UserConfigV1 contract with defaults, per-agent overrides and config digest.",
  "task_revision": 2,
  "title": "Add the UserConfigV1 configuration contract",
  "updated_at": "2026-09-22T10:16:40+00:00",
  "worktree_key": "agent-systems-benchmark-user-config"
}
---
Add the versioned non-secret user configuration contract that selects a default provider and model,
applies one optional per-agent override, and is pinned by a canonical config digest.
Repository: `martin-beck/agent-systems-benchmark`.

- 2026-09-13T09:57:00+00:00: Frozen scope for parallel setup-wizard series AR-1100..AR-1106.
  A single per-agent override is sufficient; secrets are never stored, only redacted reference
  digests. Agent identities are bounded strings validated by the CLI layer against AGENT_IDS.
