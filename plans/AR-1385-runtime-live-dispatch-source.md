# AR-1385: Authenticated runtime live dispatch source

## Objective

Connect the runtime-owned authenticated bootstrap handle from AR-1384 to the
production `asb run` and `asb sweep` dispatch path. The source must obtain all
authority from authenticated enrollment/control state and expose only the
opaque scheduler input already accepted by the runtime-owned scheduler.

## Dependencies

AR-1384, AR-1377, AR-1373, AR-1380, and AR-1381 are done. This is the next
coordinator repair required before AR-1329 can resume.

## Scope and acceptance

- Production `run` and `sweep` obtain the live scheduler source from the
  runtime-owned authenticated handle; no caller or CLI authority injection.
- Provider policy, target allowlist, credential reference, lease/relay roots,
  tool pins, namespace identity, and launch tokens remain private and
  runtime-owned.
- Missing, stale, revoked, mismatched, replayed, or tampered control state
  fails closed before process launch or network access.
- Add positive and negative dispatch tests, including direct/alternate-egress
  denial and cancellation teardown; preserve `NetworkPolicy::Deny` defaults.
- Run focused and full gates, independent review, signed+DCO exact-head CI,
  post-merge verification, and durable release evidence.
- Do not claim real OpenRouter or three-agent execution until a separate live
  run is observed and recorded with runtime-attested evidence.

