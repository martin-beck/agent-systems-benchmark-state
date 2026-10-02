# AR-1625 — TUI hosted coverage repair

Repair behavior-relevant TUI coverage exposed by the exact AR-1615 qualification.
Add focused tests for uncovered development wizard/control branches without
lowering thresholds, excluding files, or making authentication/signature/key
management blocking in development. Re-run the full hosted Trusted-main gate
and then requalify AR-1615 on the identical paired heads.
