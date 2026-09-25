# AR-1348: Runtime-owned live acquisition service

## Objective

Implement the production-owned acquisition service required by AR-1329 after
the AR-1347 neutral credential-injection contract. One bounded service must
discover and pin the live gate, reserve the benchmark `ResourceLease`, resolve
one concrete provider target from the enrolled allowlist, acquire the runtime
observed namespace handoff and launch token, construct the per-attempt relay,
and return only an opaque launch capability to `asb-cli`. Cancellation and
normal completion must revoke and tear down every acquired resource.

## Dependencies and ownership

Foundational dependencies are AR-1327, AR-1328, AR-1339 and AR-1340. AR-1347
defines the cross-crate opaque credential-injection boundary and must be
integrated before publication of this AR; its source may be cherry-picked or
rebased only through the protected review flow. AR-1329 consumes this service
and remains fail-closed until this AR is merged and qualified. Owned paths are
the runtime acquisition supervisor, bounded relay/lease/namespace lifecycle,
and the CLI's single opaque-service call site. Do not modify asb-tui.

## Required work

1. Define a runtime-owned supervisor constructor whose inputs are validated
   policy/configuration references, not caller-supplied authority objects,
   endpoints, namespaces or credential bytes.
2. Discover and pin the approved live-gate executable, reserve and release the
   benchmark `ResourceLease`, and resolve exactly one concrete provider target
   through `ProviderEgressAuthorization` with direct and alternate egress
   denied.
3. Bind the relay and child launch to a runtime-observed namespace identity,
   issue one short-lived launch token per scheduler attempt, and consume the
   AR-1347 opaque credential capability only at the final child boundary.
4. Integrate `asb run` and `asb sweep` through one opaque acquisition call;
   preserve offline/replay defaults and fail closed on missing, stale, copied,
   expired, revoked, mismatched or unavailable authority.
5. Add positive synthetic end-to-end lifecycle tests and negative tests for
   lease/target/gate/namespace/token/relay/credential mismatch, direct or
   alternate egress, cancellation, timeout, child failure, duplicate use and
   teardown/recovery. Do not claim real provider contact from synthetic tests.

## Acceptance criteria

Only the runtime-owned service can enable live provider execution. No caller or
CLI state contains credential bytes, host paths, raw subprocess output or
authority internals. Offline and replay paths remain network-denied and
credential-free. Focused and full gates, independent review, exact-head CI,
protected merge, and all post-merge workflows are green; AR-1329 can then be
claimed with durable evidence and its live dispatch enabled only when every
runtime gate passes.

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
