# AR-1339: Runtime-owned live-provider egress backend

## Outcome

Provide the runtime-owned authenticated relay/backend required for an explicit
live provider launch. It must consume only a validated `ProviderEgressHandoff`,
permit the exact HTTPS host/path bound in that handoff, preserve
`NetworkPolicy::Deny` for offline and replay launches, and fail closed on stale,
missing, or mismatched identity.

## Dependencies and ownership

Dependencies: AR-1328 (credential-free configuration) and AR-1329 (typed live
provider gate and egress identity contract). Owned paths are the runtime
provider-egress backend/relay, sandbox launch handoff, CLI integration tests,
and redacted evidence. Do not enable host networking or expose credentials in
argv, manifests, logs, or reports.

## Work sequence

1. Define a runtime-issued live-provider handoff that binds endpoint identity,
   generation, route, adapter digest, credential reference, and deadline.
2. Implement the authenticated loopback/Unix relay or equivalent backend that
   performs the bounded outbound HTTPS connection on behalf of the child,
   allowing only the exact validated provider endpoint.
3. Reject missing/stale/mismatched handoffs, alternate hosts, non-HTTPS URLs,
   host-network requests, redirects outside the allowlist, and expired
   deadlines before any provider effect.
4. Integrate `asb run --live-provider` and `sweep` without changing offline or
   strict-replay behavior.
5. Add synthetic tests for successful relay, denial, cancellation, endpoint
   mismatch, credential non-disclosure, and restart/reconciliation behavior.

## Acceptance criteria

Only an explicit live launch with a runtime-issued matching handoff can reach a
provider. Offline/default and replay paths remain network-denied. The hosted
quality, formal, fault, portability, and exact-head gates remain green.
