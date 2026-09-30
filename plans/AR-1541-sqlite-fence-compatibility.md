# AR-1541 plan: SQLite fence compatibility and isolation

1. Read AR-1539 evidence, SQLite/WAL lifecycle docs and the exact v0.3.50
   fence implementation. Reproduce identity-change failures in disposable
   owner-only runtime directories.
2. Repair ASB-owned test/runtime setup so each isolated state uses a fresh
   bound authority, control store, WAL/SHM lifecycle and lock identity. Never
   disable identity checks or reuse another project's runtime metadata.
3. Add positive and negative tests for clean initialization, process death,
   projection reconciliation, stale identity and safe rejection after path or
   inode replacement.
4. Run SQLite-focused tests followed by the full state suite and all static,
   privacy, schema and generated-view gates. Review the complete diff and
   publish only from a clean exact tree.

Acceptance: v0.3.50 SQLite lifecycle tests pass with fresh isolated fences and
continue to reject identity changes fail-closed.
