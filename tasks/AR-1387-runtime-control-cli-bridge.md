---
{
  "branch": "feature/ar-1387-runtime-control-cli-bridge",
  "checkpoint_commit": "25548846966e37646dded8d67ed8ee5123b8bc32",
  "claim_expires": "",
  "depends_on": [
    "AR-1385",
    "AR-1384",
    "AR-1378",
    "AR-1377"
  ],
  "id": "AR-1387",
  "next_action": "Refresh the declared isolated worktree from protected main, add the authenticated runtime/control bootstrap-to-CLI bridge, and test opaque dispatch-source transfer without caller authority injection.",
  "observed_branch": "feature/ar-1387-runtime-control-cli-bridge",
  "observed_dirty": 0,
  "observed_head": "25548846966e37646dded8d67ed8ee5123b8bc32",
  "owner": "",
  "plan": "../plans/AR-1387-runtime-control-cli-bridge.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "blocked",
  "summary": "Bridge authenticated runtime/control bootstrap state into the production CLI dispatch path.",
  "task_revision": 6,
  "title": "Authenticated runtime-control CLI bridge",
  "updated_at": "2026-09-24T06:38:54+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1387-runtime-control-cli-bridge"
}
---

This repair owns the missing authenticated source in the CLI process. It must
consume only runtime/control-owned enrollment and opaque handles; no CLI option,
config file, environment value, endpoint, credential, policy, root, tool pin,
namespace identity, or launch token may become caller authority.

- 2026-09-24T06:36:21+00:00: AR-1386 blocked predecessor preserved; AR-1387 supersedes its missing
  bridge scope; dependencies verified

- 2026-09-24T06:37:23+00:00: Claimed by codex-asb-ar1329-repair-luna56.

- 2026-09-24T06:37:26+00:00: Heartbeat by codex-asb-ar1329-repair-luna56.

- 2026-09-24T06:38:30+00:00: Recorded command exit 0; command argv SHA-256
  b424a9b48859c95f2c076c63eb8af7f081718e87da9bcd44a60969f81404e3fb.

- 2026-09-24T06:38:54+00:00: Authenticated bridge audit remains blocked at a real authority source:
  RunnerBackend persists only digest-bound RuntimeAuthorityRecord and serves RuntimeReceipt over
  control, but no production runtime constructor converts the enrolled receipt/chain into
  LiveProviderRuntimeBootstrapSpec (policy, concrete allowlist, lease/relay roots, and pinned
  ToolPins) or transfers an opaque LiveProviderRuntimeDispatchSource to CLI. Existing profile
  materialize_handle is crate-private and requires those caller arguments. Exposing them through
  CLI/config or synthesizing local authority would violate fail-closed boundaries. Runtime
  dispatch-source tests pass 2/2; no safe product diff made. Coordinator must provide the next
  narrowly scoped runtime-owned bootstrap materialization source.

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
