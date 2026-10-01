# AR-1569 — ASB source-archive identity repair

## Scope

Make the build-time identity generator safe for source archives and stable
builds without a Git checkout, while preserving exact dev identity binding.

## Acceptance

- `cargo check/build --locked -p asb-cli` succeeds from a clean source archive.
- Git checkouts still embed exact commit and tree identities.
- Development lifecycle rejects unknown identity with a typed diagnostic rather
  than claiming an exact handoff.
- Stable launch and package behavior remain unchanged.
- Hosted checks and an archive-build regression test pass.

## Boundaries

Development/mock authentication remains non-blocking; this repair introduces no
production secret, signature, or key-management requirement.
