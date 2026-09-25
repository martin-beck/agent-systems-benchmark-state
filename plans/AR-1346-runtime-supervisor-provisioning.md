# AR-1346: Runtime supervisor provisioning boundary

## Objective

Provide the missing production-owned provisioning boundary required by AR-1329
and AR-1343. The supervisor must atomically acquire a pinned live gate and
`SandboxBackend`, benchmark `ResourceLease`, concrete allowlisted provider
target, enrolled credential reference/transport, runtime-observed child
namespace handoff, launch attestation token, and one per-attempt relay
lifecycle. The public CLI must receive only an opaque per-attempt factory.

## Dependencies

AR-1327, AR-1328, AR-1339, AR-1340, and AR-1343 audit evidence.

## Constraints

- Preserve offline and synthetic defaults.
- Preserve `NetworkPolicy::Deny` and direct/alternate egress denial.
- Never expose credential bytes, host paths, prompts, or raw subprocess output.
- Reject missing, stale, copied, mismatched, expired, or revoked authority.
- Bound acquisition, relay I/O, cancellation, and teardown.
- Add positive and negative tests for every new cross-crate boundary.
- Do not fabricate host capability in tests; capability-gated paths remain
  explicitly gated.

## Exit evidence

Signed+DCO implementation, independent full-diff review, focused and full
quality gates, exact-head hosted CI, protected merge, all post-merge workflows,
and durable evidence consumed by AR-1329.

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
