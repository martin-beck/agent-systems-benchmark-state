# AR-1347: Neutral live-supervisor composition contract

## Objective

Introduce a dependency-safe composition boundary for live-provider acquisition.
The boundary must let the runtime own the launch authority, lease, target,
namespace, live gate, relay, and teardown while an enrolled supervisor supplies
an opaque credential-injection capability. `asb-runtime` must not depend on
`asb-agents`, and credential bytes must never be returned to the CLI or stored
in runtime evidence.

## Dependencies

AR-1327, AR-1328, AR-1339, AR-1340, and AR-1346 audit evidence.

## Constraints

- Define the trait/opaque handle in a neutral dependency layer or runtime API;
  do not create an `asb-runtime` → `asb-agents` cycle.
- Permit only bounded child-launch injection through the supervisor; no raw
  credential bytes in evidence, JSON, logs, errors, or public CLI state.
- Preserve offline/synthetic defaults, `NetworkPolicy::Deny`, concrete target
  allowlisting, namespace attestation, per-attempt authority, and teardown.
- Add positive and negative tests for missing, mismatched, expired, revoked,
  and failed credential capabilities.

## Exit evidence

Signed+DCO implementation, independent review, focused/full gates, exact-head
CI, protected merge, all post-merge workflows, and durable evidence consumed by
AR-1346 and AR-1329.

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
