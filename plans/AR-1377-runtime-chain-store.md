# AR-1377: Runtime-owned certificate-chain store

## Objective

Materialize and retain the authenticated certificate-chain enrollment needed by
the AR-1373 receipt source and AR-1376 adapter. Reuse AR-1288/1364 contracts;
the runtime/control authority must be the only issuer. Store only validated
public identities and digests, never certificate/private-key bytes or caller
authority.

## Dependencies

AR-1288, AR-1364, and AR-1373 are done. Blocked AR-1374/1375/1376 are audit
evidence and are intentionally not dependencies.

## Acceptance

- runtime-owned installation consumes authenticated enrollment plus authority;
- restart/revocation/generation fencing and peer binding are fail-closed;
- adapter can retrieve an opaque chain only from the runtime-owned store;
- positive, tamper, replay, expiry, privacy, and restart tests pass with full
  signed/DCO/exact-head/post-merge gates.

