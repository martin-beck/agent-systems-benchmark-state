# AR-1359: Runtime/control enrollment bridge

## Objective

Provide the missing runtime-owned bridge that turns authenticated asb-control
enrollment metadata into a `LiveProviderEnrollmentRecordV1` and opaque runtime
handle without exposing authority to asb-cli or introducing a dependency cycle.

## Dependencies

Depends on AR-1357. AR-1358 is blocked on this bridge; AR-1329 remains
fail-closed until the bridge and CLI consumer are integrated.

## Required work

- Define a runtime-owned control bridge API using existing asb-control certificate
  and enrollment contracts; no asb-control -> asb-runtime dependency cycle.
- Keep certificate/claims constructors private and accept only authenticated,
  bounded control responses through an explicit runtime-owned channel.
- Validate generation, endpoint, target/tool/root digests, freshness and replay,
  then mint the opaque runtime handle consumed by the CLI factory.
- Add positive/negative cross-crate tests and preserve secret/path-free output,
  offline/replay fail-closed behavior, cancellation and teardown.

## Acceptance

Signed+DCO commits, focused/full gates, exact-head CI, independent review,
protected merge, and all post-merge workflows pass. AR-1358 then wires the
bridge into `asb run`/`sweep`.
