# AR-1482: Control-runtime process bootstrap

## Objective

Provide the missing process-owned bootstrap that composes authenticated local
control enrollment into the ordinary ASB CLI run/sweep path. The process
bootstrap must request and validate a runtime receipt and certificate chain,
then hand only a one-shot opaque dispatch source to `asb-cli`; it must never
accept caller authority or expose private runtime inputs.

## Dependencies

AR-1472 (authenticated dispatch adapter), AR-1473 (runtime-owned enrollment
source), and AR-1480 (CLI composition seam) are complete. This successor does
not depend on stale/circular AR-1374 or AR-1375.

## Acceptance

- A control/runtime-owned process bootstrap obtains the authenticated local
  receipt and enrolled chain, validates generation, nonce, identity, expiry,
  revocation, namespace, policy, lease/relay roots and teardown binding, and
  constructs the opaque source consumed by normal `run` and `sweep`.
- The ordinary entrypoint has no CLI/config/environment/endpoint/credential/
  policy/root/tool/namespace/launch-token authority inputs; missing or invalid
  control state fails closed before launch or network access.
- Positive and hostile local/mock/replay tests cover bootstrap, restart,
  cancellation, teardown, stale/replayed/mismatched receipt, and unavailable
  control state without secrets, network, synthetic authority, or asb-tui.
- Signed+DCO implementation, focused/full gates, independent review,
  exact-head CI, normal merge, eight post-merge workflows, and durable state
  evidence are required.

