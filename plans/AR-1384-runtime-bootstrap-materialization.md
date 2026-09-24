# AR-1384: Runtime-owned bootstrap materialization

## Objective

Consume the authenticated `LiveProviderRuntimeAuthorityProfile` from AR-1383
inside the runtime/control boundary and mint the opaque
`LiveProviderRuntimeHandle` required by the existing live scheduler. The source
must load policy, concrete target allowlist, credential reference, lease/relay
roots, and pinned tool identities from control-owned enrolled state; a CLI or
frontend must not provide or alter any of those authorities.

## Dependencies

AR-1383, AR-1377, AR-1373, AR-1380, and AR-1381 are done. AR-1329, AR-1382,
AR-1374, and AR-1376 remain blocked with preserved evidence.

## Scope

- Add a private runtime/control-only conversion from the authenticated profile
  and enrolled authority material to `LiveProviderBootstrapSpec` and an opaque
  `LiveProviderRuntimeHandle`.
- Validate provider/target/generation bindings, policy and allowlist digests,
  credential reference, lease and relay roots, tool pins, expiry, revocation,
  and namespace/teardown inputs before minting the handle.
- Add positive, tamper, mismatch, replay, stale, missing-authority, restart,
  and privacy tests; connect only the existing run/sweep scheduler seam.

## Acceptance

- no public constructor accepts caller-supplied authority, paths, credentials,
  tools, policy, allowlists, leases, relay roots, or namespace identity;
- incomplete, stale, revoked, mismatched, replayed, or unavailable enrolled
  material fails closed without launching a process or exposing secrets/paths;
- returned value is opaque and is consumable by the existing scheduler only
  after runtime validation and teardown setup;
- focused and full repository gates, exact-head CI, post-merge workflows,
  signature/DCO, formal evidence, and independent privacy review pass;
- real remote OpenRouter/three-agent execution remains explicitly unclaimed
  until separately observed with runtime-attested evidence.
