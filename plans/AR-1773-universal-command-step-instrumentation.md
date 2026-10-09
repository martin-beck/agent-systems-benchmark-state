# AR-1773 plan: universal command step instrumentation

1. Generate an authoritative inventory of public command routes and meaningful
   operations from dispatch, command schemas, lifecycle adapters, and existing
   diagnostic producers; classify each as immediate, bounded, or indeterminate.
2. Replace every eligible direct human status/progress write with the AR-1772
   reporter; prohibit bypasses and preserve interactive prompts and the launched
   TUI's terminal output.
3. Add real per-operation total/completed/substep feeds for bounded operations
   and honest indeterminate feeds for external waits without known totals.
4. Wire terminal states for success, failure, warning, partial, cancellation,
   and reconciliation while preserving AR-1768 cause-specific diagnostics.
5. Test every command family in fast, threshold-crossing, failed, partial,
   cancelled, redirected, quiet, and JSON modes; include provider, filesystem,
   tool, catalog/model, execution, report, replay, easy, control, and TUI paths.
6. Update user and contributor documentation with a command/step map, then run
   independent review and exact-head/full hosted qualification.
