# AR-1509 — Authenticated authority-provider receipt

Replace the AR-1508 crate-private test provider with a production runtime-owned
authority-provider receipt and lifecycle fence.

Scope:

- define a versioned, authenticated receipt/attestation from the platform
  authority source and verify all claims independently against AR-1505
  bootstrap/session state;
- implement a non-test provider adapter that stays inside runtime/control and
  returns private material only after verification; keep callers unable to
  choose roots, tools, policy, credentials, sockets, or paths;
- persist expiry/revocation/restart/cancellation bindings in the resolver and
  recheck them at materialization and each scheduler/attempt transition;
- wire the verified receipt into the opaque dispatch source and ordinary
  `asb-cli` live run/sweep path, then add provider-free local/mock/replay
  negative and lifecycle tests;
- document the first-customer platform handoff without embedding credentials,
  host data, or live-provider CI requirements.

Do not modify asb-tui, accept self-attested digests, use fixed/PATH authority,
or weaken fail-closed formal/privacy/native gates. Completion requires signed
DCO, independent review, exact-head hosted CI, protected merge, and post-merge
verification.
