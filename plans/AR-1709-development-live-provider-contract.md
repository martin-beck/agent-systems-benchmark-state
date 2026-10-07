# AR-1709 — Development live provider contract

Own the ASB provider-facing contract for an explicitly requested online run.
Define the versioned request envelope, bounded runtime credential injection,
redacted diagnostics, provider/model admission, and typed outcomes for missing
credentials, malformed credentials, transport/timeouts, non-2xx responses, and
successful responses. Keep credential material and raw responses outside Git,
receipts, logs, and state projections. A live request never falls back to a
mock or cassette; local/mock remains an explicit separate mode.

Acceptance:

1. Contract tests cover success and each typed negative outcome through backend,
   CLI human output, and `--json` output.
2. Credential injection is runtime-only, bounded, and redacted; missing
   development setup emits warnings but does not block local/mock setup.
3. Explicit live mode has no fallback path and returns nonzero on provider or
   transport failure.
4. Exact-head receipt and hosted quality gates pass without secret material.
