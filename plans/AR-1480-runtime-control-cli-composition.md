# AR-1480: Runtime-control composition for CLI live dispatch

## Objective

Provide the missing cross-crate composition that lets normal ASB `run` and
`sweep` obtain an opaque runtime-owned live dispatch source from authenticated
control enrollment. The CLI must never receive policy, credential bytes,
lease/relay roots, namespace identity, tool pins, or teardown authority.

## Dependencies

AR-1473 supplies the fenced runtime-owned enrollment source and AR-1472
supplies the authenticated live-dispatch adapter. This successor deliberately
does not depend on circular AR-1374 or AR-1375.

## Acceptance

- control/runtime-owned composition constructs the opaque source from an
  authenticated local/mock or replay receipt and chain;
- normal CLI `run` and `sweep` consume only the opaque source and remain
  fail-closed when source, receipt, generation, nonce, enrollment, namespace,
  cancellation, teardown, or replay validation is absent or mismatched;
- positive and hostile local/mock/replay integration tests cover the complete
  cross-crate seam without secrets, private paths, synthetic authority, or
  provider/network access;
- public docs/contracts identify the runtime-owned source boundary;
- signed+DCO commit, focused/full gates, exact-head CI, review, normal merge,
  and all eight post-merge workflows pass.

## Boundaries

No asb-tui changes, no live provider or remote credential requirement, no
caller-built authority, no CLI exposure of private runtime inputs, and no
weakening of egress, lifecycle, privacy, or formal gates.
