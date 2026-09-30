# AR-1549 plan: coordinator v0.3.53 compatibility closure

1. Read AR-1547, AR-1534, AR-1540, AR-1541, AR-1542 and AR-1543 completely.
2. Verify the clean exact v0.3.53 vendor manifest and record its identity.
3. Run the focused state-worktree/session and SQLite compatibility suites,
   including the formerly failing 77/78 observation case, through handoffctl.
4. Repair only ASB-owned code or fixtures if required; otherwise preserve the
   measured green result and update the stale historical blocker records.
5. Run the complete applicable ASB state suite, vendor/privacy checks and
   independent diff/signature/DCO review.
6. Release this AR with a sanitized receipt and hand exact results to the
   downstream integration and formal-readiness ARs. Never claim qualification.
