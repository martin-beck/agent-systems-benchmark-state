# AR-1703 — Current-main TUI live-control qualification

Repair and qualify the paired ASB/asb-tui development journey at the exact
current heads. The ASB side owns the broker contract and live recording
admission; asb-tui owns terminal routing and action dispatch. Keep the
development profile warning-only for missing auth/signatures/generated keys,
while explicit live execution remains online-only and fail-typed.

Acceptance:

1. The exact current asb-tui main launches through the ASB development broker
   on a PTY and reaches Run Control from a fresh configured fixture.
2. Selected/all workload scope, live recording, cassette sealing, strict
   offline replay, and comparison dispatch are observed as typed backend calls.
3. With `OPENROUTER_API_KEY`, a bounded smoke reaches the selected OpenRouter
   model and records redacted evidence only; without it, setup still completes
   and the live action reports a typed warning/nonzero result without mock or
   replay fallback.
4. Credential-free checks, source/head identities, and no-secret evidence are
   retained in the Git-backed state receipt; no older TUI pin is accepted as a
   substitute for current-main qualification.
