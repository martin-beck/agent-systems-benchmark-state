# AR-1373: Authenticated runtime receipt source

## Objective

Complete the next AR-1329 dependency by exposing a versioned, authenticated
ControlBackend receipt operation that consumes only the persisted authority
installed by AR-1371 and returns the existing `RuntimeReceiptResponseV1` to the
runtime bridge. Do not infer authority from CLI/config input or claim provider
support merely from catalog setup.

## Required work

- Add a closed, versioned `ControlCall`/`ControlResult` request for one bounded
  runtime receipt, with nonce, provider, and generation binding.
- Gate the operation on active runner-owned authority material, exact endpoint,
  credential-reference, target/tool/lease/relay digests, generation, expiry,
  replay and revocation state.
- Bind response bytes to the request and existing AR-1366 runtime bridge;
  expose only opaque/digest metadata and never secrets, paths, prompts or
  caller-supplied authority.
- Add positive and negative tests for peer/session ownership, nonce replay,
  provider/generation mismatch, revocation, restart recovery and privacy.

## Dependencies and boundaries

Depends on completed AR-1365 receipt contract, AR-1366 runtime consumer, and
AR-1371 owner-checked authority persistence. This is ASB-only; do not touch
asb-tui or claim three-agent OpenRouter end-to-end readiness.

## Acceptance

Signed+DCO commit, focused and full gates, independent review, exact-head CI,
protected merge, and all seven post-merge workflows. Only then unblock the
AR-1329 production run/sweep integration successor.

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
