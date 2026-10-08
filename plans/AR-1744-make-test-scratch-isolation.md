# AR-1744 plan: repair make test scratch-root isolation

1. Reproduce the reported `make test` failure on exact protected `main` with
   the Makefile environment, and run the named
   `development_env_cleared_cargo_links_with_validated_ld_root` test both alone
   and through the full workspace path.
2. Identify the smallest safe repair. Test-only scratch fixtures must remain
   outside the repository Cargo target tree even when `CARGO_TARGET_DIR` is
   exported; build artifacts must continue using the configured target root.
3. Add focused positive and negative coverage for external scratch placement,
   private roots, cleanup after success/panic, and the Make test environment.
   Preserve all existing symlink, ownership, bounded-size, and failure-closed
   checks.
4. Run focused tests, `make test`, applicable format/clippy/doc gates, and the
   complete repository quality gates. Independently review the full diff.
5. Publish a signed+DCO PR, wait for exact-head required CI, integrate with a
   signed two-parent merge, verify exact-main post-merge workflows, and release
   the AR with a durable receipt and evidence digest.

Acceptance evidence includes the original failing command and test output, the
repaired command trace, focused/full gate results, exact PR/base/head/tree,
signature and DCO verification, merge identity, and all post-merge workflow IDs.
