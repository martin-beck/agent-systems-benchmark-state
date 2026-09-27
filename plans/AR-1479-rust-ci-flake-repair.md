# AR-1479: Repair unrelated Rust CI timing and state-root flakes

## Objective

Repair the existing Rust assurance flakes that blocked the exact-head validation
of AR-1420: the control state-root ownership collision and the
`gemini::tests::malformed_ready_marker_fails_fast_and_cleans_run_root` one-second
timing assertion. Preserve the production behavior and fail-closed lifecycle
semantics; do not weaken the test, delete the assertion, or broaden retries.

## Acceptance

1. Reproduce each failure independently on the protected-main baseline and
   classify whether it is test isolation, bounded scheduling sensitivity, or a
   real regression.
2. Apply the smallest deterministic repair (test isolation, monotonic bounded
   timing contract, or equivalent) with positive and negative coverage.
3. Run the focused tests repeatedly, the full affected crate/workspace gates,
   formatting, clippy, privacy/formal checks, and exact-head CI.
4. Record both original failures, all retries, and the repair rationale in the
   AR; no provider access or native host is required.

## Non-goals

No product behavior change unrelated to the failing tests, no timeout inflation
that hides a hang, and no waiver of required checks.
