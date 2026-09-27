# AR-1487: Owner-backed first-customer qualification

## Objective

Qualify the first-customer production-like ASB journey over the completed
runtime-owned CLI path: credential-free local/mock `run` and `sweep`, strict
offline replay, evidence/receipt inspection, cancellation/restart recovery,
and teardown/cleanup. This is a deterministic local qualification slice; it
must not contact a provider or modify asb-tui.

## Dependencies

AR-1446, AR-1450, AR-1455, and AR-1486 are complete. The qualification must
use the current protected main and retain the established no-live-provider,
no-asb-tui boundary.

## Acceptance

- A disposable, credential-free local/mock run and sweep use the
  runtime-owned owner-backed CLI entry, produce bounded result/evidence
  envelopes, and leave no owner/backend resources after teardown.
- Strict replay consumes only a runtime-issued replay authority and verifies
  receipt/cassette identity; missing, stale, tampered, replayed, and
  caller-supplied authority fail closed before execution effects.
- Cancellation/restart recovery and cleanup are tested with bounded local
  fixtures; evidence contains no credentials, prompts, transcripts, raw
  captures, private paths, or live-provider data.
- Tests/docs state exactly what is qualified and what remains optional or
  unqualified; no network, credentials, provider reachability, native ARM, or
  asb-tui is required.
- Focused/full tests, clippy, rustdoc, release/policy/privacy gates, signed
  DCO review, exact-head CI, and all post-merge workflows pass.

## Implementation boundary

Prefer adding qualification tests and documentation over production changes.
If a deterministic product gap is exposed, implement only the smallest
ASB-only repair and preserve fail-closed authority semantics; otherwise record
the complete evidence and release the qualification AR done.
