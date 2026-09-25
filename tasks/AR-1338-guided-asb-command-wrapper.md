---
{
  "branch": "feature/ar-1338-guided-asb-command-wrapper",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-25T17:45:20+00:00",
  "depends_on": [
    "AR-1442",
    "AR-1443",
    "AR-1446"
  ],
  "id": "AR-1338",
  "next_action": "Promote and claim the ASB-only wrapper implementation. Extend the existing bounded easy path to catalog-driven setup/selection, plan/run/sweep, report/compare, record/replay, generated private files, documentation, and offline hostile tests; optional live-provider capture remains separate.",
  "owner": "coordinator-ar1338",
  "plan": "../plans/AR-1338.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Add a catalog-driven friendly wrapper for setup, selection and benchmark workflows.",
  "task_revision": 3,
  "title": "Guided ASB command wrapper",
  "updated_at": "2026-09-25T15:45:20+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1338-guided-asb-command-wrapper"
}
---

Add a friendly `asb easy` command or equivalent in-tree wrapper that guides a
user through supported setup, provider/model selection, multi-agent plans and
benchmark/report workflows. It must derive all digests and generated files from
the authoritative ASB catalog and config contracts, preserve secret isolation,
and delegate execution to the normal ASB commands. It must not become a second
provider registry or bypass the runtime's fail-closed validation.

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

- 2026-09-25T15:45:17+00:00: ASB-only wrapper dependencies AR-1442, AR-1443, and AR-1446 are done.
  Optional live capture and asb-tui remain separate; promote full catalog-driven wrapper
  implementation.

- 2026-09-25T15:45:20+00:00: Claimed by coordinator-ar1338.
