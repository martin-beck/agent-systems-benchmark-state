# AR-1715 — Credential-backed development OpenRouter qualification

Run the final ASB provider-facing development qualification with an
operator-supplied `OPENROUTER_API_KEY` in a disposable environment. Exercise
one bounded real success request and selected/all live benchmark fan-out, then
run credential-free and hostile negative cases: missing/malformed key,
provider non-2xx, timeout, transport/process failure, unavailable model, and
explicit no-fallback assertions. Keep local/mock and offline replay separate.

The receipt must bind exact ASB and paired TUI heads, command/result digests,
redacted provider/model identity, bounded timing, and cleanup. It must contain
no key, prompt, raw response, cassette bytes, or private host path. TUI AR-1705
owns the installed frontend journey; this AR owns the ASB provider and live
benchmark evidence.

Acceptance:

1. A real bounded OpenRouter request succeeds or returns a truthful typed
   provider outcome using the runtime key, with no secret leakage.
2. Selected and all-agent benchmark modes are exercised against the reviewed
   configuration and preserve explicit Online mode.
3. Missing/malformed key, timeout, transport, non-2xx, unavailable-model, and
   process failures are typed, nonzero, and never switch to mock/replay.
4. Human-default and `--json` outputs are checked; receipt and state are
   privacy-safe and exact-head bound.
5. Hosted AWQ, Rust, policy, formal, platform, and quality checks are green.
