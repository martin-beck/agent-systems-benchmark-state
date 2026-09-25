# AR-1355: Runtime-attested enrollment record transport

## Objective

Provide the runtime/control-owned transport that supplies live acquisition
authority without exposing provider targets, tool pins, lease roots, relay roots,
credentials, or launch authority to `asb-cli`.

## Dependencies

Depends on AR-1352. AR-1353 and AR-1354 provide preserved evidence and remain
superseded/blocked; AR-1329 remains fail-closed until this seam is merged.

## Required work

- Define a versioned, bounded enrollment record carrying only runtime-attested
  identities and concrete public target/tool/root references.
- Verify authenticity, freshness, provider endpoint binding, target allowlist,
  tool pins, lease root, relay root, and `NetworkPolicy::Deny` before authority.
- Keep credential values and private paths out of records and public evidence.
- Mint `LiveProviderRuntimeHandle` only inside `asb-runtime` after validation.
- Add positive and negative tests for forged/stale records, target mismatch,
  tool/root mismatch, copied records, alternate egress, and missing credentials.
- Consume the resulting opaque enrollment in `asb run`/`asb sweep`; preserve
  offline/replay fail-closed behavior, cancellation, and teardown.

## Acceptance

Only runtime/control code can mint an opaque live handle. CLI callers cannot
choose endpoint, target, tool, namespace, lease, relay, or credential authority.
Focused and full gates pass with signed+DCO commits and exact-head CI.

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
