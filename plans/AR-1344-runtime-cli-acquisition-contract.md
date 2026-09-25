# AR-1344: Runtime-owned CLI live acquisition contract

## Outcome

Provide the missing runtime-owned acquisition contract that lets `asb run` and
`asb sweep` request one live-provider attempt without constructing authority,
network endpoints, credentials, or namespace claims in the CLI.

## Dependencies and ownership

Dependencies: AR-1339, AR-1340, and AR-1342. The relay implementation from
AR-1343 is consumed at commit `ce2c2db068b05092f0f63291e0d94d4dbc9cda9c`.
Owned paths are the runtime acquisition API, CLI run/sweep integration, and
their contract tests. Do not change asb-tui, bypass `NetworkPolicy::Deny`,
accept caller-provided endpoints or credentials, or weaken offline/replay mode.

## Required work

1. Define an atomic runtime-owned per-attempt API that supplies the validated
   `SandboxBackend`, benchmark `ResourceLease`, runtime launch token, observed
   child `NamespaceIdentity`, and one `LiveProviderRelay` lifecycle.
2. Wire `asb run --live-provider` and `asb sweep --live-provider` to consume
   one opaque context per attempt and revoke/tear it down on cancellation,
   expiry, failed spawn, and normal completion.
3. Keep direct/alternate egress, copied or stale handoffs, credential
   disclosure, and caller-controlled target/namespace inputs fail-closed.
4. Add positive synthetic execution tests plus negative tests for absent,
   expired, copied, mismatched, revoked, duplicate, cancelled, and replay
   contexts. Preserve offline and replay behavior unchanged.

## Acceptance criteria

Only runtime-issued, namespace-attested contexts can enable live execution;
the CLI cannot construct or select the provider route or credential. Focused
and full quality gates, independent review, exact-head CI, and post-merge
verification must be green before AR-1329 is resumed.

## Current development and CI qualification boundary

The mandatory development and CI qualification path for this AR is a deterministic
local provider/LLM mock (LiteLLM-compatible where practical), including hostile
negative tests and offline replay where applicable. External/live OpenRouter or
other provider reachability is optional supplementary evidence only; it is never a
completion, dependency-readiness, or CI gate. Production egress policy, credential
non-disclosure, runtime-owned authority, namespace/relay attestation, cancellation
and teardown, and fail-closed denial of unapproved external traffic remain required
contracts. Existing live-provider dependency edges describe production integration
ordering only and must not be used to block local qualification or to claim external
reachability.
