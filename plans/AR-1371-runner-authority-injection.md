# AR-1371: Runner authority injection

## Objective

Use the existing AR-1288 certificate issuer and chain validation to add an
owner-checked runtime/control injection boundary for RunnerBackend/Catalog.
Materialize only authenticated chain identity plus provider target, pinned
tool, lease-root, relay-root, generation, expiry, and revocation metadata so
the receipt source can issue runtime-bound responses.

## Audit context

AR-1369 and AR-1370 independently confirmed that current `AuthRecord` stores
only provider, endpoint digest, credential digest, generation, and status; no
authority or chain source exists. This replacement removes their blocked
dependencies while retaining their exact evidence and does not weaken gates.

## Required work

- Define a bounded versioned authority record with strict unknown-field and
  digest/target/tool/root validation, owner-checked persistence, and safe
  restart/recovery semantics.
- Inject it into RunnerBackend/Catalog only through an authenticated
  runtime/control path backed by AR-1288; reject CLI/config authority and
  missing, stale, revoked, replayed, mismatched, or tampered records.
- Expose only privacy-safe receipt material; never serialize certificate/private
  key bytes, credentials, private paths, prompts, or launch authority.
- Add positive and negative tests for issuance, peer identity, generation,
  revocation, replay, restart, cancellation, teardown, and privacy.

## Acceptance

Focused/full gates, independent review, signed+DCO exact-head PR, all required
hosted checks, protected merge, and seven post-merge workflows pass. Only then
resume the blocked receipt-source and AR-1329 production dispatch chain.
