# AR-1405: Open dependency PR reconciliation

## Objective

Reconcile the stale open Dependabot PRs against protected ASB main and merge
only dependency updates whose rebased exact-head gates and compatibility review
pass. Superseded, unsafe, or incompatible updates must be closed or replaced
with durable evidence rather than merged blindly.

## Scope

Audit PRs #237, #236, #235, #234, #150, #149, #148, and #147. Rebase each
still-applicable candidate onto current protected main, regenerate locked
metadata where required, run focused compatibility tests and all required
checks, independently review the exact diff, and merge only green candidates.
PR #147's `sha2` API break requires a separate compatibility decision and must
not be accepted as a routine version bump.

## Acceptance

- Every scoped PR ends in merged, superseded/closed, or explicitly blocked with
  exact current evidence and a next action.
- No stale-base check result is treated as current evidence; no coverage,
  formal, platform, or policy gate is weakened.
- Merges use signed+DCO commits, exact-head CI, independent review, and the
  seven required post-merge workflows. Product dirty files remain untouched.

