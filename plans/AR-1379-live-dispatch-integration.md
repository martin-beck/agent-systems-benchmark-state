# AR-1379: Production live dispatch integration

## Objective

Wire the authenticated runtime adapter into production `asb run` and `asb
sweep` execution. The command path must obtain only a runtime-owned opaque
attempt factory; provider selection remains metadata, while authority,
credential channel, lease, relay, namespace, and teardown remain runtime-owned.

## Dependencies

AR-1378, AR-1377, AR-1366, AR-1364, and AR-1362 are done. AR-1329/1360 and
blocked adapter audits remain evidence, not dependencies.

## Acceptance

- run/sweep dispatch uses the authenticated adapter and never CLI authority;
- offline, missing selection, mismatch, replay, expiry, revoke, network policy,
  namespace, and teardown paths fail closed;
- positive and negative CLI integration tests cover the full bounded seam;
- signed/DCO, full gates, exact-head CI, review, merge, and post-merge checks pass.

