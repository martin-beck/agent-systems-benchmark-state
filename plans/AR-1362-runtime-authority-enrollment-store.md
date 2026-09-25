# AR-1362: Runtime authority enrollment store

## Objective

Create the durable, authenticated control/runtime enrollment state needed to
issue `RuntimeEnrollmentReceiptV1` to a local runtime consumer. The store must
bind certificate chain/generation, provider and endpoint identity, concrete
public target, pinned tool bundle, lease root, relay root, credential reference,
and validity without retaining secrets or private host data.

## Dependencies

Depends on AR-1359. AR-1361 remains blocked until this authority source exists;
AR-1360 and AR-1329 remain fail-closed.

## Required work

- Define a versioned, deny-unknown-fields durable authority enrollment record
  with digest-only credential/private-root references and bounded validity.
- Add authenticated control/runtime issuance and revocation/generation fencing;
  reject missing, stale, mismatched, replayed, private/link-local, or unpinned
  target/tool/root data.
- Keep certificate/private bootstrap and runtime policy constructors private;
  expose only a secret-free receipt and opaque runtime-owned capability.
- Add positive/negative persistence, tamper, replay, revocation, privacy, and
  recovery tests; update generated schemas/documentation.

## Acceptance

Focused/full gates, signed+DCO exact-head PR, independent review, protected
merge, and all seven post-merge workflows pass. Only then resume AR-1361 and
AR-1360; do not advance AR-1329 before exact evidence is durable.

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
