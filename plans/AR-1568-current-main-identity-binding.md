# AR-1568 — ASB exact current-main identity binding

## Scope

Ensure dev lifecycle artifacts identify the exact ASB source/build being run,
rather than stale constants copied from an earlier main head.

## Acceptance

- Fresh dev materialization records the exact ASB commit and tree identity.
- Status, doctor, launch, and broker descriptors use the same identity.
- Stale, malformed, or mismatched identity evidence fails closed with a typed
  development-only diagnostic.
- Tests prove identity changes when source changes and remain reproducible.
- Stable/released identity behavior is unchanged.

## Boundaries

Development/mock prototype only; no mandatory authentication, signatures, or
key management.
