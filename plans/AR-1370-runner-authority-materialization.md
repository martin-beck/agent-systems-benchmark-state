# AR-1370: Runner authority materialization

## Objective

Integrate the existing AR-1288 certificate issuer into the ASB control service
without inventing authority. RunnerBackend/Catalog must receive authenticated
chain and runtime enrollment material through an explicit owner-checked
runtime/control injection boundary, so the receipt operation can issue only
validated provider target/tool/lease/relay metadata.

## Dependencies

Depends on AR-1288 (merged certificate issuance and chain validation) and
AR-1369 (the blocked audit identifying the missing RunnerBackend/Catalog seam).
AR-1329 remains fail-closed until this repair and its dependent receipt source
are merged and verified.

## Required work

- Define a bounded, versioned, privacy-safe authority record for authenticated
  chain identity, trust-anchor binding, provider target, tool pin, lease root,
  relay root, generation, expiry, and revocation state.
- Add owner-checked, symlink-safe persistence/recovery and an explicit
  runtime/control injection path into RunnerBackend/Catalog; reject CLI/config
  supplied authority and unknown fields.
- Connect only the validated record to `RuntimeReceiptRequestV1` issuance;
  never emit certificate/private-key bytes, credentials, private paths, or
  launch authority in public projections.
- Add positive, forged-record, stale/revoked, replay, restart, peer-identity,
  and teardown tests, plus schema/documentation updates.

## Acceptance

Focused/full gates, independent review, signed+DCO exact-head PR, all hosted
checks, protected merge, and seven post-merge workflows pass. Only then resume
AR-1369/1368 and advance AR-1329 production run/sweep integration.

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
