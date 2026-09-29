# AR-1506 — Runtime platform launcher integration

Implement the production process boundary that consumes the authenticated platform authority
from AR-1505 and gives ordinary ASB CLI execution an opaque runtime-owned live dispatch source.

Scope:

- refresh an isolated worktree from protected `main` and audit the AR-1505 public handoff symbols;
- add the narrow platform/session launcher and process-owner composition at the existing ASB CLI
  entry boundary;
- keep certificate enrollment, authority resolution, bootstrap/receipt binding, cancellation,
  teardown, restart, expiry, revocation, namespace/relay/lease roots, and egress policy runtime-
  owned and fail closed;
- add provider-free deterministic local/mock/replay tests, including missing authority, mismatched
  identity/roots, cancellation, teardown, restart, expiry, revocation, and alternate-egress denial;
- document the deployment handoff needed for first-customer production qualification without
  embedding private paths, credentials, prompts, telemetry, or host assumptions.

Do not modify `asb-tui`, expose caller-supplied sockets/clients/chains/roots/tools, synthesize
authority, add live-provider gates, or weaken existing native/formal/privacy checks. Completion
requires independent review, SSH-signed DCO commit, exact-head hosted CI, protected merge, and
post-merge verification of the resulting main SHA.
