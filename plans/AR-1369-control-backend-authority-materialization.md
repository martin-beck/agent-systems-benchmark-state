# AR-1369: ControlBackend authority materialization

## Objective

Provide durable, authenticated ControlBackend state containing the certificate
chain and runtime-owned target/tool/lease/relay authority required to issue
`RuntimeReceiptResponseV1`. Public projections remain digest-only and
credential-free; only the authenticated runtime source may consume the private
authority.

## Dependencies

Depends on AR-1362, AR-1364, and AR-1366. AR-1368 is blocked because current
ControlBackend auth state exposes only provider/endpoint/credential digests,
generation, and status; it has no certificate chain or runtime target/tool/
lease/relay materialization.

## Required work

- Extend control-owned durable enrollment state with validated chain identity,
  target allowlist, tool pin, lease root, relay root, generation, expiry, and
  revocation fencing, never certificate/private-key bytes in public output.
- Add authenticated lifecycle and recovery materialization, with peer identity,
  generation, nonce, replay, and cancellation checks.
- Expose only the bounded receipt source needed by AR-1368/AR-1366; reject all
  CLI/config-supplied authority and unknown fields.
- Add positive, tamper, stale, revoked, replay, restart, and privacy tests.

## Acceptance

Focused/full gates, independent review, signed+DCO exact-head PR, all hosted
checks, protected merge, and seven post-merge workflows pass before AR-1368 or
AR-1329 can advance.

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
