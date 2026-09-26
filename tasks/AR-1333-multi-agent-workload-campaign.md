---
{
  "branch": "feature/ar-1333-multi-agent-workload-campaign",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1329",
    "AR-1332",
    "AR-1456"
  ],
  "id": "AR-1333",
  "next_action": "Keep AR-1333 as the optional production/live campaign successor; implement the mandatory credential-free local/mock campaign through AR-1456 and do not wait on AR-1329 for local qualification.",
  "owner": "",
  "plan": "../plans/AR-1333.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Run the multi-agent by workload benchmark campaign with per-tuple evidence and offline replay.",
  "task_revision": 1,
  "title": "Multi-agent by workload benchmark campaign",
  "updated_at": "2026-09-22T13:39:37+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1333-multi-agent-workload-campaign"
}
---

The single-run and capture/replay pieces deliver evidence per execution, but
benchmarking different agents under specific workloads requires a campaign that
drives the whole matrix. The mandatory credential-free local/mock path is now
owned by AR-1456. This AR remains the optional production/live successor for
provider-backed campaign execution and must not be used to block local
development, CI, or first-customer mock qualification.

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
