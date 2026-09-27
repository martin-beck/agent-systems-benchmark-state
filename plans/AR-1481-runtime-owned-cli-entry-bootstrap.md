# AR-1481: Runtime-owned CLI entry bootstrap

## Objective

Wire the authenticated runtime/control composition into the ordinary ASB CLI
entry path without exposing authority inputs. `run` and `sweep` must request
only an opaque runtime-owned dispatch source; unavailable, stale, revoked,
malformed, or mismatched control state must fail closed before CLI effects.

## Dependencies

AR-1472 (authenticated dispatch adapter), AR-1473 (runtime-owned enrollment
source), and AR-1480 (CLI composition seam) are complete. This successor does
not depend on circular AR-1374 or AR-1375.

## Acceptance

- A runtime/control-owned process bootstrap supplies the opaque source to the
  normal CLI run/sweep path; CLI args, config, environment, endpoint,
  credentials, policy, roots, tools, namespace, and launch tokens cannot do so.
- Missing, stale, revoked, malformed, mismatched, replayed, or unavailable
  control state fails closed before launch or network access.
- Positive and hostile local/mock/replay tests cover the process composition;
  no live provider, credentials, network, synthetic authority, or asb-tui.
- Signed+DCO implementation, focused/full gates, independent review,
  exact-head CI, normal merge, eight post-merge workflows, and durable state
  evidence are required.

