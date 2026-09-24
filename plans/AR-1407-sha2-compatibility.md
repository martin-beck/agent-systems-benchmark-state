# AR-1407: `sha2` 0.11 compatibility repair

## Objective

Evaluate and, if safe, implement the `sha2` 0.11 update that was closed from
PR #147 after compile/API and MSRV incompatibilities. Preserve the current
cryptographic behavior and fail closed if the new API or toolchain contract
cannot be qualified.

## Acceptance

- Inventory all direct and transitive `sha2` use, associated formatting/API
  changes, MSRV impact, fuzz lockfile effects, and cryptographic test vectors.
- Implement only a reviewed compatibility patch with positive/negative tests,
  exact digest parity, locked offline builds, and all required CI/formal gates.
- Merge only a signed+DCO exact-head candidate with independent review and
  seven green post-merge workflows; otherwise leave the update superseded with
  durable incompatibility evidence.

