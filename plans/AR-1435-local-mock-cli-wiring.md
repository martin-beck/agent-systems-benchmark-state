# AR-1435: Local mock CLI wiring

## Objective

Wire the existing `LocalProviderMockBackend` and non-convertible mock attempt
from AR-1434 into the `asb run` and `asb sweep --use-config` qualification
paths. The wiring is a deterministic offline fixture only and must remain
separate from production `LiveProviderAttempt` authority.

## Dependencies and boundaries

AR-1434 is the sole completion dependency. AR-1329 and AR-1432 remain blocked.
No live provider, OpenRouter endpoint, credential bytes, external network,
relay, namespace, lease, tool, or caller-supplied endpoint may be used. The
ordinary run/sweep default remains denied unless the explicit local mock
qualification mode is selected through the existing configuration contract.
`ProviderEgressTarget`, `NetworkPolicy::Deny`, production launch authority,
and `LiveProviderAttempt` constructors must not be weakened or broadened.

## Required work

1. Identify the existing `asb run` and `asb sweep --use-config` dispatch and
   add one explicit runtime-owned local-mock mode using the AR-1434 backend;
   reject unknown or ambiguous mode/config fields and preserve normal default
   denial.
2. Bind each scheduler admission to exactly one mock attempt, fixed model,
   opaque credential reference, bounded request, deterministic digest, and
   teardown/cancellation outcome. Do not expose response bodies, credentials,
   prompts, private paths, or convert mock values into production authority.
3. Add positive and hostile CLI/runtime tests for run and sweep, including
   offline/default denial, missing or malformed config, external-target and
   alternate-egress rejection, cancellation/revocation, repeated attempts,
   bounded requests, and failure propagation.
4. Run focused and full applicable offline gates, independently review the
   exact diff, publish a signed+DCO exact-head PR, merge only through the
   documented local integration path, and run all seven exact-main workflows.

## Acceptance

`asb run --use-config` and `asb sweep --use-config` complete only through an
explicit local mock qualification fixture and produce bounded digest evidence;
ordinary/default and external-provider paths remain denied. Every mock attempt
has one scheduler identity and is cancelled/revoked safely. No production
authority, egress policy, credential handling, or live-provider behavior is
changed. Focused, full, PR, and seven post-merge gates are green with no
external provider access required.
