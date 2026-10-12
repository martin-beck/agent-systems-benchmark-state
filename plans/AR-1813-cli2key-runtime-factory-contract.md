# AR-1813: expose the cli2key runtime factory contract

Extend `asb-runtime` with a narrow, opaque API that ordinary ASB CLI code can
use to request a verified cli2key sidecar-backed `LiveProviderAttemptFactory`
without constructing authority itself. Define the runtime-owned receipt
contract that carries only non-secret identity, platform, executable, and
bridge metadata from AR-1779 into that API.

## Required work

1. Define versioned runtime receipt types and validation for the AR-1779
   project-local installation, including catalog identity, source/executable
   digests, entrypoint, platform, and bridge protocol. Reject missing,
   substituted, stale, malformed, or cross-platform receipts.
2. Expose an opaque runtime/control constructor or source that returns the
   existing `LiveProviderAttemptFactory` to trusted dispatch composition while
   keeping sidecar keys, authority internals, and credential material private
   to `asb-runtime`.
3. Add cancellation, timeout, crash, readiness, teardown, and bounded-sweep
   tests using local/mock fixtures. Do not contact a live provider.
4. Update AR-1812 integration documentation and preserve typed no-fallback
   failures; no OpenRouter, replay, or alternate-provider fallback is allowed.

## Acceptance

- Focused positive/negative contract tests, formatting, clippy, full offline
  workspace gates, headers, privacy, and applicable hosted CI pass.
- Independent exact-head review verifies the authority boundary, signatures,
  DCO, and no secret/private-path leakage.
- No TLC/TLA+/model-check execution is required for development; formal work
  remains reserved for the future final-delivery lane.
