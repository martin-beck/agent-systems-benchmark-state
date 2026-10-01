# AR-1594 — qualification coverage isolation

Move the external pinned asb-tui PTY qualification behind an explicit
`cross-repo-qualification` feature. Enable that feature only in the dedicated
hosted workflow, retain real binary/source/digest assertions there, and prove
ordinary `cargo llvm-cov --workspace --all-targets` remains above the existing
90% floor without exclusions.

Required evidence: local coverage, full Rust tests, exact qualification
workflow, signed/DCO repair PR, independent review, and all hosted checks.

This is a repair seam for ASB AR-1590 and may proceed before AR-1590 is
released. Downstream: AR-1590 release qualification.
