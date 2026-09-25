# AR-1387: Authenticated runtime-control CLI bridge

## Objective

Provide the production CLI with an authenticated runtime/control bootstrap
source that mints or transfers the opaque `LiveProviderRuntimeDispatchSource`
from enrolled control state, allowing normal `asb run` and `asb sweep` live-mode
dispatch without passing `None` or accepting caller-supplied authority.

## Dependencies

AR-1385, AR-1384, AR-1378, and AR-1377 are done. AR-1386's audit is preserved
as a blocked predecessor; this successor supersedes its missing bridge scope
and is required before AR-1329 can resume.

## Acceptance

- CLI obtains the dispatch source only through authenticated runtime/control
  bootstrap and attestation; ordinary CLI/config inputs cannot inject authority.
- Bootstrap rejects absent, stale, revoked, mismatched, replayed, malformed,
  or unauthorized control state before launch or network access.
- Run and sweep preserve offline default, explicit live selection, egress
  denial, secret non-disclosure, namespace/lease/relay teardown, and bounded
  cancellation.
- Tests use a local deterministic provider/LLM mock (LiteLLM-compatible where
  practical). External OpenRouter/backend connectivity is never required for
  AR completion or CI and is optional evidence only.
- Signed+DCO implementation, independent review, focused/full gates,
  exact-head CI, post-merge verification, and durable release evidence pass.

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
