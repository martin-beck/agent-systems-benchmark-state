# AR-1383: Runtime-owned authority profile materialization

## Objective

Add a runtime-owned, authenticated authority profile that materializes pinned
provider policy, concrete target allowlist, credential reference, lease/relay
roots, and tool pins without accepting those authorities from CLI callers.

## Dependencies

AR-1377, AR-1373, AR-1380, and AR-1381 are done. AR-1329 and AR-1382 remain
blocked with preserved evidence.

## Acceptance

- profile is issued only from authenticated control/runtime enrollment;
- caller cannot inject endpoints, roots, tools, credentials, or policy;
- missing, stale, mismatched, revoked, and replayed profiles fail closed;
- positive/negative tests, full gates, and privacy review pass.

