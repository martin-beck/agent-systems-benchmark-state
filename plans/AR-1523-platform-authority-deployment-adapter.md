# AR-1523 plan: development local/mock orchestration qualification

1. Read AR-1451, AR-1452, AR-1453, AR-1505 and AR-1513 plus the
   runtime/control architecture. Preserve ownership and versioned handoff
   contracts; do not duplicate caller-built authority.
2. Exercise the existing central `asb-orchestrator` `AuthoritySource` through
   the deterministic local/mock owner and strict-replay owner used by ordinary
   development run and sweep.
3. Prove provider-free positive and hostile lifecycle behavior: teardown,
   revocation, cancellation, expiry, alternate-egress denial, one-shot source
   consumption, replay rejection and unknown-field rejection.
4. Run focused/full Rust, privacy and schema gates, independently review the
   complete diff, publish from a clean exact head, wait for required CI and
   record sanitized development qualification evidence.
5. Keep any deployment-owned authenticated/live-provider adapter explicitly
   optional. It must not be introduced as a prerequisite or inferred from
   local/mock evidence.

Completion requires exact-head local/mock and strict-replay evidence through
the central orchestrator. It does not claim deployment-owned live dispatch,
external-provider reachability, or formal AR-1307/1308 qualification.
