# AR-1593 — catalog protocol version alignment

Resolve the ASB/asb-tui common-version mismatch exposed by independent review
of PR #413. Decide and document whether the catalog contract is published at
the existing common v1.10/v1.7 boundary or whether the TUI must gain v1.12;
then implement the chosen path in both repositories with immutable historical
schemas preserved.

Required evidence:

- explicit version matrix and rationale;
- exact negotiation selecting a catalog-capable common version;
- downgrade/unsupported negatives that do not falsely claim catalog support;
- regenerated version-specific schemas and compatibility tests;
- real ASB/TUI bootstrap evidence, not synthetic fixtures;
- signed/DCO commits, independent review, and green hosted checks.

Dependencies: ASB AR-1592 and paired asb-tui AR-1593. Downstream: ASB AR-1590.
