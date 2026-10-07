# AR-1696 — Paired TUI trusted-main coverage and release-gate repair

Repair the trusted-main coverage failure introduced/exposed after complete
fan-out request integration. Add focused tests for changed behavior, run the
native coverage gate at the exact merged head, and preserve the configured
threshold and module inventory.

Acceptance:

- Changed fan-out, handoff, capture/replay, and comparison paths have behavior
  coverage rather than line-count-only filler.
- Trusted-main coverage passes without threshold or gate weakening.
- ASB/TUI exact heads, hosted run IDs, and independent review are recorded.
- Missing development auth/signatures/key management remain warning-only.
