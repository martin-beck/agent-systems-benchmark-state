# AR-1356: Control/runtime enrollment attestation primitive

## Objective

Reuse the existing authenticated asb-control enrollment/certificate boundary to
issue a runtime-owned capability that can be consumed by asb-runtime without
making CLI callers authorities.

## Dependencies

Depends on AR-1352 and existing asb-control enrollment/certificate contracts.
AR-1355 remains blocked until this primitive is merged; AR-1329 remains
fail-closed.

## Required work

- Define a versioned control-to-runtime attestation containing only bounded,
  secret-free identities for provider endpoint/target, tool pins, lease root,
  relay root, generation and credential reference.
- Bind it to authenticated runner identity, expiry, provider selection digest,
  and `NetworkPolicy::Deny`; reject stale, copied, mismatched and alternate-
  egress records.
- Issue and consume an opaque runtime capability entirely inside runtime/control
  code; no public CLI constructor may accept authority inputs.
- Add schema, positive/negative transport, replay, revocation, and teardown
  tests, then expose the narrow source needed by AR-1355.

## Acceptance

The runtime mints the only live-provider handle after verified control
attestation. CLI receives no endpoint, address, tool path, root, credential,
namespace, lease, relay, or token authority. All focused/full gates and exact-
head/post-merge checks pass.

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
