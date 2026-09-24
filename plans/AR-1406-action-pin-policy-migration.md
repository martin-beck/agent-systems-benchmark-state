# AR-1406: Policy-approved action-pin migration

## Objective

Resolve the remaining action-update PRs (#235, #234, and #148) through an
explicit policy migration rather than bypassing the repository's immutable
action-pin controls.

## Acceptance

- Audit each requested action commit, provenance, release identity, and
  artifact behavior; update the policy contract only with reviewed immutable
  pins and generated evidence.
- Rebase each applicable update onto current protected main, run all exact-head
  checks and independent review, and merge only green candidates. Unsafe or
  unverifiable updates remain closed/blocked with evidence.
- Verify artifact retention, formal Java setup, and supply-chain checks in the
  seven post-merge workflows; never weaken policy or accept floating refs.

