# AR-1386: Production live CLI dispatch integration

## Objective

Wire the authenticated runtime-owned live dispatch source into the normal
`asb run` and `asb sweep` command path so the selected agent/workload can use
the runtime scheduler without caller-supplied authority.

## Dependencies

AR-1385, AR-1384, AR-1380, AR-1381, AR-1378, and AR-1377 are done. This is the
next repair required before AR-1329 can resume.

## Acceptance

- Normal production `run` and `sweep` obtain the opaque dispatch source only
  from authenticated runtime/control state; CLI arguments cannot inject
  endpoints, credentials, policy, roots, tools, namespace identity, or launch
  authority.
- Missing, stale, revoked, mismatched, replayed, or malformed authority fails
  closed before process launch or network access; cancellation tears down
  leases, relays, and child processes.
- Positive and negative command tests use a local deterministic provider/LLM
  mock (LiteLLM-compatible where practical). An external OpenRouter/backend
  connection is never required for AR completion or CI.
- Preserve offline default behavior, explicit live-mode selection, declared
  egress enforcement, secret non-disclosure, and direct/alternate-egress
  denial.
- Signed+DCO implementation, independent review, focused/full gates,
  exact-head CI, post-merge workflows, and durable release evidence pass.

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
