---
{
  "branch": "feature/all-agents-provider",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-08T14:13:55+00:00",
  "depends_on": [
    "AR-0311",
    "AR-0312"
  ],
  "id": "AR-0313",
  "next_action": "Read full development/architecture/quality/provider-plan docs in /srv/data/projects/agent-systems-benchmark-all-agents-provider at exact base b6078bb1ca2ee8f35973ffab9740c2c12dd4126e; audit provider selection surfaces and implement atomically without touching active AR-0844 crates/asb-cli/src/control.rs or AR-0316 runtime-bundle paths.",
  "observed_branch": "feature/all-agents-provider",
  "observed_dirty": 0,
  "observed_head": "b6078bb1ca2ee8f35973ffab9740c2c12dd4126e",
  "owner": "quality_20260906",
  "plan": "../plans/AR-0313.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Let test plans select one provider profile for every chosen supported agent atomically.",
  "task_revision": 10,
  "title": "Configure one provider for all agents",
  "updated_at": "2026-09-08T11:17:09+00:00",
  "worktree_key": "agent-systems-benchmark-all-agents-provider"
}
---
## AR-0313

Let test plans select one provider profile for every chosen supported agent atomically.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-08T11:13:52+00:00: Highest-priority dependency-ready P1 after AR-1005 release: AR-0311 and
  AR-0312 are done. Scope fence: do not modify active AR-0844 path crates/asb-cli/src/control.rs or
  AR-0316 runtime-bundle paths; implement provider-plan/config/preflight surfaces only.

- 2026-09-08T11:13:55+00:00: Claimed by quality_20260906.

- 2026-09-08T11:14:22+00:00: Recorded command exit 0; command argv SHA-256
  b8eb2481d248cc05886bf762fee3519642990d402848ee9f68e2f4450f110dc6.

- 2026-09-08T11:14:38+00:00: Claimed highest-priority dependency-ready task after AR-1005. Declared
  clean worktree created at exact origin/main b6078bb1ca2ee8f35973ffab9740c2c12dd4126e; no
  pre-existing branch/worktree overlap. Active path fences recorded.

- 2026-09-08T11:16:06+00:00: Recorded command exit 0; command argv SHA-256
  820382f47854636ef918510a690ef27abadbe0936a37d34c469855996b6ef781.

- 2026-09-08T11:16:21+00:00: Recorded command exit 0; command argv SHA-256
  8d183b83233c9778df8e17a0bf0f78b0dc685e40e42e08e4167236a42764edd0.

- 2026-09-08T11:16:40+00:00: Recorded command exit 0; command argv SHA-256
  37b751a838a323076a0c607ecedcd12835a03c3702aebe485c460df8cfe36d87.

- 2026-09-08T11:17:09+00:00: Recorded command exit 0; command argv SHA-256
  47cf5c28887d4fbcc4fda32ad3b356a23390825c6536af7aad8cdc0b3fe8a58a.
