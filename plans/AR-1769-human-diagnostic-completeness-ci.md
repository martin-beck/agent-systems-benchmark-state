# AR-1769 plan: human diagnostic completeness CI

1. Derive coverage from the authoritative public command inventory, closed
   diagnostic catalog, backend mappings, warning/result variants, and renderer
   match arms. Fail compilation or a deterministic repository check on any
   unmapped public variant.
2. Add semantic validators requiring a specific cause, safe affected subject,
   state-change statement, and recovery disposition. Reject placeholder-only
   prose and code-to-spaces fallback for known public diagnostics.
3. Add controlled-defect tests for missing catalog entries, cause collapse,
   missing path context, ambiguous prose, missing warning consequence, unsafe
   remediation, wrong stream/exit, and privacy leaks.
4. Build an executable negative/warning matrix across setup, config/auth,
   project/tool/catalog, easy/TUI lifecycle, plan/run/sweep, report/compare,
   record/replay, provider/network, filesystem, timeout/cancellation, partial,
   and warning paths. Include the exact missing-parent example.
5. Verify human default and `--details`, redirected/non-TTY behavior, widths,
   Unicode/control characters, shell-safe next commands, explicit JSON, and raw
   protocol commands while preserving schemas and exit meanings.
6. Wire the check into required PR and protected-main workflows, document how to
   add a diagnostic, and prove rejection of controlled defects before exact-head
   and exact-main acceptance.

