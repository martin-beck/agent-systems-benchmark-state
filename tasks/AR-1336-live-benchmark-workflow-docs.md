---
{
  "branch": "feature/ar-1336-live-benchmark-workflow-docs",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-27T11:30:47+00:00",
  "depends_on": [
    "AR-1333",
    "AR-1334",
    "AR-1335"
  ],
  "id": "AR-1336",
  "next_action": "Document the end-to-end live benchmark workflow and publish the supported agent by provider by model support matrix, with exact digests and evidence limits.",
  "observed_branch": "feature/ar-1336-live-benchmark-workflow-docs",
  "observed_dirty": 0,
  "observed_head": "1489b4e1fed481556611ea4090ee17973bb95729",
  "owner": "ar1332-record-replay-luna56",
  "plan": "../plans/AR-1336.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Document the live benchmark workflow and publish the supported agent and provider matrix.",
  "task_revision": 14,
  "title": "Live benchmark workflow documentation and support matrix",
  "updated_at": "2026-09-27T09:37:56+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1336-live-benchmark-workflow-docs"
}
---

The implementation work through AR-1335 makes live benchmarking possible, but
QUICKSTART, ARCHITECTURE and the support matrix still describe the old closed
catalog and no end-to-end workflow. This AR documents the complete live
benchmark workflow from enrollment through selection, campaign execution,
capture and offline replay, updates the README and architecture notes to remove
the stale claims that live-provider selection and record/replay are not CLI
commands, and publishes the supported agent by provider by model matrix with
exact digests and the boundaries of every evidence claim. All documentation is
kept credential-free and truthful about offline and opt-in limits.

## Current development and CI qualification boundary

The mandatory development and CI qualification path for this AR is a deterministic
local provider/LLM mock (LiteLLM-compatible where practical), including hostile
negative tests and offline replay where applicable. External/live OpenRouter or
other provider reachability is optional supplementary evidence only; it is never a
completion, dependency-readiness, or CI gate. Production egress policy, credential
non-disclosure, runtime-owned authority, namespace/relay attestation, cancellation
and teardown, and fail-closed denial of unapproved external traffic remain required
contracts. Existing live-provider dependency edges describe production integration
ordering only and must not be used to block local qualification or to claim external
reachability.

- 2026-09-27T09:30:32+00:00: AR-1333, AR-1334, and AR-1335 are done; promote documentation/support
  matrix with optional live-provider boundary.

- 2026-09-27T09:30:47+00:00: Claimed by ar1332-record-replay-luna56.

- 2026-09-27T09:30:58+00:00: Recorded command exit 0; command argv SHA-256
  e9f1780b7080a2b1acc482356aaade7ad8d9d427c2c8b8ded34b0c882f04ff9c.

- 2026-09-27T09:31:51+00:00: Recorded command exit 0; command argv SHA-256
  a8db0e218ff018ff2af47d26fda5bd4d5e6b99df6bf6e5eea7b142814da480a6.

- 2026-09-27T09:35:28+00:00: Recorded command exit 0; command argv SHA-256
  1704726abc957f6e827a42ca0e7fe2381f2fe5c6c805b6134a85343114af25cd.

- 2026-09-27T09:35:56+00:00: Recorded command exit 0; command argv SHA-256
  28a3116afa49de17e4c45d94e358883650345330e67621f926d21a5e2f2df131.

- 2026-09-27T09:36:20+00:00: Recorded command exit 0; command argv SHA-256
  2c2f4949877afa55c1dd5ffcd7c73a5db05269b3e0a16ee70ed9063c67eb76f0.

- 2026-09-27T09:36:44+00:00: Recorded command exit 0; command argv SHA-256
  5c87134eda9468d9be12821b2c7958e88cb6f6944f6da71da39097d3aab4580e.

- 2026-09-27T09:37:10+00:00: Recorded command exit 0; command argv SHA-256
  2a20cee3f2743f2c95ca4e7af9d14bd9bb6d4901ceaa94adc06e41ddf6305afa.

- 2026-09-27T09:37:43+00:00: Recorded command exit 0; command argv SHA-256
  afbe201c217891fafead92474a0b7ff74d89ef9db2956aae1f4ac51dbbf5dc6b.
