# AR-1507 — Runtime-owned authority materialization

Define and implement the runtime/control boundary that turns authenticated
AR-1505 bootstrap state into private launch authority and an opaque dispatch
source usable by ordinary ASB CLI run/sweep.

Scope:

- audit the private runtime authority types and AR-1505 bootstrap/receipt
  handoff; identify the smallest public-free materializer location;
- implement construction of private certificate authority, enrollment source,
  namespace/relay/lease roots, tool pins, launch policy, egress policy, and
  cancellation/teardown binding strictly from authenticated runtime state;
- expose only an opaque one-shot dispatch source to the CLI entry boundary and
  wire ordinary live dispatch without a caller/config fallback;
- add deterministic local/mock/replay qualification and negative lifecycle,
  identity, expiry, revocation, restart, and alternate-egress tests;
- document the first-customer deployment handoff without private paths,
  credentials, host assumptions, telemetry, or live-provider gates.

Do not modify asb-tui, accept caller-built authority, synthesize trust, use
fixed host paths as production authority, or weaken existing formal/privacy/
native gates. Completion requires independent review, SSH-signed DCO commit,
exact-head hosted checks, protected merge, and post-merge verification.
