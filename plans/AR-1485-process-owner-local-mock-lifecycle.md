# AR-1485: Process-owner local/mock lifecycle

## Objective

Implement the smallest runtime/control process-owner slice over the merged
AR-1484 contract: an owner-managed deterministic local/mock lifecycle that
retains the authenticated owner contract, fences issuance, and hands only an
opaque dispatch source to the CLI composition boundary. This establishes the
provider-free lifecycle seam needed before production control transport.

## Dependencies

AR-1472, AR-1473, AR-1480, and AR-1484 are complete. AR-1483 records the
remaining process-owner gap. Do not depend on or revive AR-1374/1375.

## Acceptance

- A runtime-owned local/mock process owner owns lifecycle state and can issue
  only one bounded opaque source through an internal owner backend; caller
  authority, credentials, endpoints, policy, roots, tools, namespace, and
  launch tokens are not accepted or exposed.
- Prepared/enrolled/issued and terminal cancellation, revocation, expiry,
  disconnect, and teardown transitions are fenced by AR-1484 identifiers.
- Positive local/mock and strict-replay tests cover issuance, restart,
  unavailable/replayed/mismatched receipt, cancellation, and teardown; no
  network, live provider, credentials, synthetic production authority, or
  asb-tui.
- Signed/DCO implementation, focused/full gates, exact-head CI, review,
  normal merge, eight post-merge workflows, and durable evidence are required.

