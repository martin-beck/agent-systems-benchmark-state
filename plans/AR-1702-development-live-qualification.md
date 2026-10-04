# AR-1702 — Development live OpenRouter qualification

Qualify the merged development live execution path against the current ASB
main head using an operator-supplied `OPENROUTER_API_KEY` only at runtime. The
qualification must prove one bounded real OpenRouter request, redacted
provider/model identity, and truthful online evidence; it must not use a
cassette, fixture, or local mock as a substitute for the credential-backed
smoke.

The same matrix must cover missing credentials, malformed credentials, provider
HTTP/transport failure, timeout, and an explicit local/mock request. Live
failures are typed and actionable, while development setup/authenticity/key
warnings remain warning-only. A live request must never silently fall back to
mock or replay. Secrets and response bodies must not enter the repository or
durable state.

Pair with TUI AR-1705: the TUI receipt must consume this ASB live-admission
contract and reference the exact ASB and TUI heads. This ASB AR owns the
provider-facing smoke and negative evidence; it does not modify the TUI.

Acceptance:

1. A disposable credential-backed smoke reaches OpenRouter and records only
   redacted request metadata, provider/model identity, bounded timing, and
   response outcome.
2. Missing/invalid credentials, timeout, transport, and non-success provider
   responses produce stable typed failures with remediation and nonzero status.
3. Live mode has no mock/replay fallback; local/mock remains explicit and is
   separately identified as non-live.
4. The receipt records exact ASB source head, test commands, outcome digests,
   and credential-free evidence. No key, token, raw prompt, or response body
   is persisted.
