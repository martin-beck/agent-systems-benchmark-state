# AR-1617 — explicit cassette seal, reopen, and removal operations

Add the missing typed cassette lifecycle operations behind the ASB control
route: explicit seal/finalization, reopen/resume only from an interrupted
reconciliation state, and bounded removal of selected development artifacts.
Bind every operation to cassette, campaign, generation, provider, agent, and
workload identity; reject terminal-state reopen and stale or mismatched
requests without mutation.

Development identities and missing production authentication, signatures, or
key management remain warning-only. Production artifact deletion stays
fail-closed and explicitly authorized.

Required evidence: versioned wire schema, backend and TUI dispatch, positive
interrupted-capture/reconcile/seal path, terminal/stale/remove negatives,
offline replay compatibility, independent review, hosted checks, and exact
main verification.
