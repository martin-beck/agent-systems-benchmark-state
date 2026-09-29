# AR-1523 plan: platform authority deployment adapter

1. Read AR-1451, AR-1452, AR-1453, AR-1505, AR-1508, AR-1510, AR-1513 and
   the runtime/control architecture. Freeze the ownership and versioned
   handoff contract before coding; do not duplicate caller-built authority.
2. Define the smallest private platform-provider interface. It must return
   opaque capability material only after validating authenticated receipt,
   generation, namespace, endpoint, lease/relay roots, tool bundle, policy,
   credential reference, restart, cancellation and expiry bindings.
3. Implement the adapter in the runtime/control owner and connect it to the
   central `asb-orchestrator` `AuthoritySource` used by ordinary run and
   sweep. Replace the current live-mode rejection only after the opaque source
   is available; local/mock and strict replay behavior must remain unchanged.
   Private paths and credentials never cross CLI/control transport or durable
   public evidence.
4. Add provider-free deterministic positive, replay and hostile lifecycle tests;
   use a local mock/replay authority for CI. Prove teardown, revocation,
   cancellation, alternate-egress denial and one-shot source consumption.
5. Run focused/full Rust, formal, privacy and schema gates, independently
   review the complete diff, publish from a clean exact head, wait for required
   CI, merge only when green, then verify a disposable first-customer-style
   deployment with sanitized evidence.

Completion requires the production callsite and exact-head evidence. A test
façade, self-attested record, live-provider probe, or successful unit test
without ordinary dispatch wiring is insufficient.
