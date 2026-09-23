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
