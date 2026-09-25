# AR-1388: Runtime authority receipt materializer

## Objective

Build the runtime-owned production materializer that validates the
authenticated receipt and chain, resolves enrolled provider authority, and
constructs the private bootstrap inputs consumed by the opaque live runtime
handle and CLI bridge.

## Dependencies

AR-1385, AR-1384, AR-1378, and AR-1377 are done. AR-1387's blocked audit is
preserved; this task supersedes its missing constructor scope.

## Acceptance

- Authenticated receipt/chain validation binds provider, generation, policy,
  concrete target allowlist, credential reference, lease/relay roots, tool
  pins, expiry, revocation, namespace and teardown state.
- Only runtime/control-owned code can materialize private bootstrap inputs;
  CLI/config/environment callers cannot inject or alter them.
- Missing, stale, revoked, mismatched, replayed, malformed, or unavailable
  enrolled state fails closed before process launch or network access.
- Positive, tamper, mismatch, replay, cancellation, teardown, and privacy
  tests use a local deterministic provider/LLM mock. External OpenRouter or
  backend connectivity is never required for AR completion or CI.
- Signed+DCO implementation, independent review, focused/full gates,
  exact-head CI, post-merge workflows, and durable release evidence pass.

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
