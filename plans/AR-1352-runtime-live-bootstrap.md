# AR-1352: Runtime-owned live bootstrap

## Objective

Provide the private runtime bootstrap source required to construct the
AR-1351 `LiveProviderProvisioner` without caller-supplied authority.

## Dependencies

Depends on merged AR-1351. AR-1349 and AR-1329 remain downstream and
fail-closed. Do not modify asb-tui.

## Required work

Derive and pin the enrolled egress policy/allowlist, sandbox tools and live
launch gate, and bounded relay root from installed runtime configuration. Reject
missing, stale, alternate, or unpinned values before any launch effect. Expose
only an opaque runtime service handle; never expose policy, backend, paths,
credentials, or authority internals to CLI callers. Add positive/negative
bootstrap, direct-egress, rollback, and teardown tests plus all applicable
gates.

## Acceptance

AR-1349 can obtain one runtime-owned provisioner handle and wire `asb run` and
`asb sweep` without injected factories, preserving offline defaults and
`NetworkPolicy::Deny`.

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
