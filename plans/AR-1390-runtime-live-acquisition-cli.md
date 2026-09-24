# AR-1390: Runtime-owned live acquisition and CLI bridge

## Objective

Complete the missing production-owned `LiveProviderRuntimeService` boundary
for ASB `run` and `sweep`, consuming only authenticated runtime/control
enrollment and opaque authority handles. Wire the normal CLI path to obtain
one bounded live attempt per scheduler attempt without allowing CLI/config/
environment callers to provide authority.

## Dependencies

The runtime authority and safety foundations are done: AR-1388 (receipt
materializer), AR-1385 (authenticated dispatch source), AR-1373 (receipt
source), AR-1366 (receipt consumer), AR-1341 (namespace attestation), AR-1342
(relay factory), AR-1339 (egress backend), and AR-1340's security repair are
released. AR-1329 remains blocked because normal `asb run`/`sweep` still has no
runtime-owned constructor that composes these pieces.

## Acceptance

- A runtime/control-owned constructor resolves enrolled provider policy and
  concrete target allowlist, opaque credential capability, pinned live gate,
  benchmark `ResourceLease`, observed child namespace, launch token, relay,
  and teardown state atomically for each attempt.
- Normal `asb run` and `asb sweep` obtain the opaque runtime dispatch source
  through that constructor; no CLI flag, config, environment variable,
  endpoint, credential, policy, root, tool pin, namespace identity, or launch
  token can inject or override authority.
- Missing, stale, revoked, mismatched, replayed, malformed, cancelled,
  duplicate, or teardown-failed state rejects before launch and preserves
  offline-by-default and direct/alternate-egress denial.
- Positive and hostile tests use a local deterministic provider/LLM mock
  (LiteLLM-compatible where practical). External OpenRouter/backend
  connectivity is never required for AR completion or CI and is optional
  evidence only.
- Run and sweep tests prove one attempt per scheduler admission, bounded
  cancellation, resource release, privacy-safe evidence, and strict replay /
  offline behavior.
- Signed+DCO implementation, independent review, focused and full gates,
  exact-head CI, all seven post-merge workflows, and durable AR-1329 unblock
  evidence pass.
