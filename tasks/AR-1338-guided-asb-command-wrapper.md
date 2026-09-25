---
{
  "branch": "feature/ar-1338-guided-asb-command-wrapper",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-25T18:17:09+00:00",
  "depends_on": [
    "AR-1331",
    "AR-1442",
    "AR-1443",
    "AR-1446"
  ],
  "id": "AR-1338",
  "next_action": "Open after AR-1448 supplies the runtime-owned strict replay authority. Then extend the existing bounded easy path to catalog-driven setup/selection, plan/run/sweep, report/compare, record/replay, generated private files, documentation, and offline hostile tests; optional live-provider capture remains separate.",
  "observed_branch": "feature/ar-1338-guided-asb-command-wrapper",
  "observed_dirty": 0,
  "observed_head": "2872a31f2ee90ac5df1a47203b2a618b1829cfec",
  "owner": "coordinator-ar1338",
  "plan": "../plans/AR-1338.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Add a catalog-driven friendly wrapper for setup, selection and benchmark workflows.",
  "task_revision": 9,
  "title": "Guided ASB command wrapper",
  "updated_at": "2026-09-25T16:17:40+00:00",
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

- 2026-09-25T15:45:44+00:00: Recorded command exit 0; command argv SHA-256
  62cc414e2aff2ff6a6ecedac52ecb1c1bf9777c8f4628e29597d8cf0016bb0e2.

- 2026-09-25T15:53:33+00:00: Audit of protected merge 2872a31f: existing bounded easy
  run/sweep/record-campaign path is present and full CLI/customer gates are green, but the complete
  wrapper acceptance is not met because normal CLI replay still requires runtime-issued
  ReplayLaunchAuthority. AR-1448 now owns the missing runtime/control authority source; no wrapper
  mutation or authority weakening made.

- 2026-09-25T16:17:09+00:00: Claimed by coordinator-ar1338.

- 2026-09-25T16:17:23+00:00: Recorded command exit 0; command argv SHA-256
  ed516f6f0da731f7f0c8670680dc0151dbd38c6637e417bb47b211eb4c8699ca.

- 2026-09-25T16:17:40+00:00: Recorded command exit 0; command argv SHA-256
  91c481d4f1a058d3265e9102b0531d1eefe09cb45e5c1807ecda5e8c8b6b67d5.
