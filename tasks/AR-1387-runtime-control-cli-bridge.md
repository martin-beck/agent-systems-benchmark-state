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
  "next_action": "Resume AR-1391 runtime-control bootstrap constructor; AR-1387 remains blocked pending that successor and has no safe in-scope product diff.",
  "observed_branch": "feature/ar-1387-runtime-control-cli-bridge",
  "observed_dirty": 0,
  "observed_head": "25548846966e37646dded8d67ed8ee5123b8bc32",
  "owner": "",
  "plan": "../plans/AR-1387-runtime-control-cli-bridge.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "blocked",
  "summary": "Bridge authenticated runtime/control bootstrap state into the production CLI dispatch path.",
  "task_revision": 17,
  "title": "Authenticated runtime-control CLI bridge",
  "updated_at": "2026-09-27T02:42:16+00:00",
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

- 2026-09-27T02:31:33+00:00: Dependencies AR-1385, AR-1384, AR-1378, and AR-1377 are durably done.
  Resume the concrete successor for authenticated runtime/control bootstrap-to-CLI transfer; AR-1382
  audit confirms this is the remaining missing seam. No caller authority, live provider, or asb-tui
  required.

- 2026-09-27T02:31:58+00:00: Claimed by ar1332_record_replay_luna56.

- 2026-09-27T02:38:09+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.

- 2026-09-27T02:38:25+00:00: Recorded command exit 0; command argv SHA-256
  b04e51d6a8a1cd1d991d96d1b0eeb7f5236f1056ccb95c8f404b26c181dc4797.

- 2026-09-27T02:38:40+00:00: Recorded command exit 0; command argv SHA-256
  97149e1fed9062e061094f8d0a0d921c8b355d8216f566ba7202ede70be3c2aa.

- 2026-09-27T02:39:00+00:00: Recorded command exit 0; command argv SHA-256
  58d1b1ef63ab2176f6704f62286c8c0953f5026d37109f098dc3ddd101d7e269.

- 2026-09-27T02:39:39+00:00: Bounded protected-main audit complete: declared worktree is clean at
  25548846966dded8d67ed8ee5123b8bc32 but behind origin/main 363b21f by 203 commits. Current CLI
  entry still dispatches normal run/sweep with no injected live factory/source; only the library
  helper run_with_runtime_live_provider_source exists. Runtime live_service has private
  materialize_handle and profile/receipt validation, but no runtime/control-owned constructor
  transfers an authenticated chain-bound opaque dispatch source with concrete lease/relay roots,
  policy/allowlist, tool pins, credential capability, namespace and teardown authority. A
  CLI/config/env constructor or synthetic local authority would violate fail-closed contracts. No
  product edits, no asb-tui, no live provider. Next action: resume the narrowest successor AR-1391
  (runtime-control bootstrap constructor) after updating its stale blocked audit, then wire the
  resulting opaque source into normal run/sweep; preserve AR-1329 as optional/live.

- 2026-09-27T02:41:01+00:00: Metadata repair only: set next action to the already identified AR-1391
  successor; no AR-1387 implementation.

- 2026-09-27T02:41:48+00:00: Claimed by ar1332_record_replay_luna56.

- 2026-09-27T02:42:08+00:00: Metadata correction after lock recovery: AR-1387 audit is complete and
  implementation remains blocked by the missing runtime-owned bootstrap constructor. Successor
  AR-1391 is the next scoped action; no product changes made.

- 2026-09-27T02:42:16+00:00: AR-1387 remains blocked and is now ownerless. Protected-main audit
  found no safe in-scope bridge: normal CLI run/sweep still has no authenticated runtime source;
  private materialize_handle requires runtime-owned policy/allowlist, lease/relay roots, tool pins,
  credential capability, namespace, and teardown inputs. Do not expose or synthesize authority. Next
  action is AR-1391 runtime-control bootstrap constructor with the concrete authenticated
  chain-bound opaque-source contract; preserve AR-1329/live provider optional.
