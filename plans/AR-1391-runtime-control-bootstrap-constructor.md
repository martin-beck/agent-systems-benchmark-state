# AR-1391: Runtime/control bootstrap constructor

## Objective

Add the missing runtime-owned constructor that consumes an authenticated
ControlBackend receipt and enrolled chain state, resolves the private live
bootstrap inputs, mints the opaque `LiveProviderRuntimeHandle`, and exposes
only the resulting one-shot dispatch source to the normal ASB run/sweep path.

## Dependencies

AR-1388, AR-1385, AR-1373, AR-1366, AR-1341, AR-1342, AR-1339, and AR-1340
are complete. AR-1390's protected-main audit is preserved: existing
`from_handle` and CLI source helpers accept externally injected handles/sources
and therefore cannot be used as the constructor.

## Acceptance

- A production runtime/control-owned factory obtains and validates the
  authenticated receipt/chain from its enrolled backend, resolves policy,
  concrete target allowlist, opaque credential capability, lease/relay roots,
  pinned tools, namespace identity, expiry and revocation, and mints the
  private runtime handle without caller-supplied authority.
- The normal CLI `run` and `sweep` path can request only this opaque source;
  CLI flags, config, environment, endpoint, credential, policy, root, tool,
  namespace, and launch-token inputs cannot construct or replace it.
- Missing, stale, revoked, malformed, mismatched, replayed, and unavailable
  control state fail closed before launch or network access; teardown and
  cancellation release leases and relay resources.
- Positive and hostile tests use a local deterministic provider/LLM mock
  (LiteLLM-compatible where practical). External OpenRouter/backend access is
  never required for AR completion or CI.
- Signed+DCO implementation, focused/full gates, independent review,
  exact-head CI, seven post-merge workflows, and durable evidence unblock the
  subsequent AR-1390 integration and AR-1329.
