# AR-1770 plan: descriptor-safe directory race hardening and acceptance matrix

1. Audit every AR-1767 output path and classify its input, parent, temporary,
   and publication operations, including the routed TUI lifecycle.
2. Implement one descriptor-relative or equivalent fail-closed primitive for
   owned directory preparation and use it from atomic file and campaign
   publication; reject symlink, replacement, non-directory, permission, and
   read-only cases without touching an outside target.
3. Preserve dry-run no-mutation behavior, private modes, fsync/rollback, JSON
   stdout, human stderr notices, bounded evidence, and offline boundaries.
4. Add deterministic race/concurrency tests and a complete positive/negative
   route matrix covering setup/config, project/tool, plan, run/sweep, report,
   record/campaign, easy lifecycle, and TUI operations.
5. Run focused, full, formal, fuzz/model, platform, exact-head review and CI
   gates; publish only from a clean signed DCO exact head and record evidence.
