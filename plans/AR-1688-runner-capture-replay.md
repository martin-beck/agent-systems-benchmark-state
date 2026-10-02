# AR-1688 — runner-owned cassette capture and replay qualification

## Scope

Qualify the AR-1686 runner's selected-workload capture, sealing, reopen, and
strict offline replay path. The runner must own lifecycle orchestration and
receipt generation; no hand-authored cassette or product-repository evidence is
accepted.

## Acceptance

- The generated plan captures and seals a selected workload cassette.
- Reopen and strict offline replay consume the exact cassette digest and deny
  network/provider contact.
- Missing, malformed, stale, or mismatched cassette identity fails closed with
  typed diagnostics; interrupted cleanup is bounded and idempotent.
- Human and JSON receipts bind exact ASB head, plan/run/cassette/replay digests,
  and no-secret scan results.

The paired TUI acceptance is tracked by TUI-state AR-1679 and may consume this
receipt only after exact-head verification; no cross-repository dependency is
added to the local graph.
