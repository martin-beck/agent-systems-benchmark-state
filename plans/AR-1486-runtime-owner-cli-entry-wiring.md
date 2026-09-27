# AR-1486: Runtime-owner CLI entry wiring

## Objective

Wire `LocalMockRuntimeControlOwner` into the ordinary `asb-cli run` and
`sweep` entry path through the existing AR-1480 opaque dispatch-source seam.
The CLI must consume only the runtime-owned opaque source; it must never accept
caller authority or construct credentials, certificate chains, endpoints,
leases, relays, tools, namespaces, or launch tokens.

## Dependencies

AR-1480, AR-1484, and AR-1485 are complete. This slice stays ASB-only and does
not revive the stale AR-1374/1375 chain, modify asb-tui, or require a live
provider.

## Acceptance

- Ordinary `run` and `sweep` obtain their dispatch source from a
  runtime/control-owned `LocalMockRuntimeControlOwner` through the AR-1480
  opaque seam; caller-supplied authority is rejected.
- Enrollment, issue, cancellation, and teardown are ordered and fail closed;
  unavailable, stale, revoked, replayed, mismatched, and post-teardown input
  produces a bounded error before CLI effects.
- Deterministic local/mock and strict-replay tests cover positive run/sweep
  composition and hostile unavailable, caller-authority, and lifecycle cases.
- No credentials, network/provider access, asb-tui changes, synthetic
  production authority, prompts, or unbounded evidence are introduced.
- Focused and full workspace tests, clippy, rustdoc, release build, policy,
  coverage, and exact-head CI pass; documentation describes the provider-free
  qualification boundary. Commit is SSH-signed with DCO and reviewed.

## Implementation boundary

Keep the change limited to the ASB runtime/CLI composition seam. If the
ordinary entry path lacks a safe constructor or requires an authority source
outside the completed contracts, stop and record the exact gap instead of
fabricating authority; create a narrower successor only if necessary.
