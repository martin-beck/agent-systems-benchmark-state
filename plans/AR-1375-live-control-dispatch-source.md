# AR-1375: Runtime-owned live control dispatch source

## Objective

Provide the missing runtime-owned adapter that obtains an authenticated
`RuntimeReceipt` response and certificate chain for the CLI run/sweep bridge.
The adapter must own the control transport, chain material, replay/expiry
checks, and teardown; CLI callers receive only an opaque attempt factory.

## Dependencies

AR-1373 and AR-1374.

## Acceptance

- no public caller can construct provider authority or inject a receipt/chain;
- authenticated control transport and runtime bridge are wired to the live
  attempt factory;
- replay, nonce/provider/generation mismatch, offline, expiry, revoke, and
  teardown fail closed with bounded privacy-safe evidence;
- focused/full gates, signed+DCO, exact-head CI, review, merge, and postmerge
  workflows pass.

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
