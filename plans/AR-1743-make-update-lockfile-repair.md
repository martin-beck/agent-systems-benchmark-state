# AR-1743 plan: repair Make update lockfile handling

1. Reproduce the current `make update` failure on the exact current protected
   main and identify whether the desired update contract is a lockfile refresh
   or locked validation; do not hide or ignore Cargo.lock changes.
2. Redesign the target with an explicit bounded sequence: clean-tree and
   fast-forward checks, deliberate dependency-resolution/lockfile refresh when
   requested, then locked validation. Never pass `--locked` to a command that
   is expected to rewrite Cargo.lock.
3. Keep build, test, install, and release paths locked and offline-safe after
   dependencies are installed. Refuse dirty trees, ambiguous toolchains,
   failed refreshes, unsafe paths, and partial updates with actionable output.
4. Add positive and negative Makefile tests covering successful refresh,
   unchanged lock validation, dirty-tree rejection, lockfile-write failure,
   and failure propagation; update README/help text and any generated docs.
5. Independently review the complete diff, run focused and full applicable
   gates, publish a signed+DCO PR, wait for exact-head CI, merge only through
   the signed local integration procedure, and verify every exact-main
   post-merge workflow before releasing this AR.

Acceptance evidence must include the original error, repaired command trace,
lockfile diff behavior, test results, exact PR/base/head/tree identities,
signature/DCO checks, and all post-merge workflow IDs.
