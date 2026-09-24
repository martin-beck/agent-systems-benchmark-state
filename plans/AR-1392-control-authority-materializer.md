# AR-1392: Control-owned private authority materializer

## Objective

Give the authenticated control/runtime boundary a production-owned resolver
that turns enrolled, digest-bound receipt state into private live authority:
credential capability, concrete egress policy and target allowlist, lease and
relay roots, pinned tools, child namespace identity, launch-token issuer, and
teardown authority. The resolver must be the only source consumed by the later
runtime bootstrap constructor.

## Dependencies

The public receipt and runtime materializer foundations are done (AR-1388,
AR-1385, AR-1373, AR-1366, AR-1341, AR-1342, AR-1339, and AR-1340). AR-1391
is blocked and its audit is preserved: current control records contain only
authenticated digest metadata, while existing private APIs require caller-
supplied authority. This AR owns the missing control-side materialization, not
the CLI facade.

## Acceptance

- Control-owned enrollment validates a receipt/chain and resolves all private
  authority fields from protected local state or a bounded injected test
  double; callers cannot provide or override them.
- Resolution binds credential, policy/allowlist, lease/relay roots, tool
  pins, namespace identity, launch-token issuer, expiry, revocation, and
  teardown generation to the authenticated receipt and rejects missing,
  stale, copied, replayed, mismatched, or malformed state.
- Private authority is never serialized into public receipts, evidence,
  logs, CLI/config/environment, or persisted unencrypted artifacts; network
  access remains denied until the runtime-owned launch gate is attested.
- Positive, tamper, replay, cancellation, teardown, privacy, and egress
  tests use a local deterministic provider/LLM mock. External OpenRouter or
  backend connectivity is never required for AR completion or CI.
- Signed+DCO implementation, focused/full gates, independent review,
  exact-head CI, seven post-merge workflows, and durable handoff evidence
  enable AR-1391 and then AR-1390 without weakening fail-closed policy.
