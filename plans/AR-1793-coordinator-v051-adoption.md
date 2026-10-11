# AR-1793 plan: Coordinator v0.5.1 adoption

## Scope

Adopt released Coordinator `v0.5.1` from immutable commit
`7b19c0ffc8b37d0071d480cd666baef3f3672e35` into ASB coordination state.
The adoption includes the supported `bind-worktree` retry semantics required by
ASB workers and the released no-authorization gate contract.

## Required work

1. Verify the exact clean release tag, source commit, and vendor manifest;
   synchronize with `vendor.py sync --version v0.5.1`, then verify offline.
2. Repair only ASB-owned adapters, fixtures, and tests that assumed the removed
   legacy `oracle_gate.authorized` field or an earlier vendor identity.
3. Add behavior-focused ASB-owned tests until the existing 95% branch-aware
   coverage floor passes. Do not lower thresholds, exclude modules, or patch
   vendored files.
4. Run the complete locked quality suite, schema and generated-view checks,
   vendor verifier, formal tier, live doctor, exact-head CI, independent review,
   signed merge, and exact-main post-merge checks.

## Boundaries

This is a released tag-bound adoption, not a development snapshot. It does not
claim a Coordinator source change, alter task authority, or replace the
separate ASB product workflow. Any newly found Coordinator defect must be
repaired and released upstream before another sync.
