# AR-1620 — development bundle integrity and ASB integration repair

Harden the AR-1614 TUI bundle and prove ASB consumes the exact produced
artifact. Require the content-addressed directory name to equal the executable
digest, reject symlink/non-regular executables, validate repository/ref/commit,
tree, target, timestamp, and warning fields, publish manifest and active
selector atomically with interruption recovery, and add an integration fixture
that ASB verifies and launches the TUI bundle rather than rebuilding an
independent source copy. Development authentication/signatures/key management
remain warning-only.

Required evidence: tamper/symlink/provenance/partial-publication tests,
cross-repository exact-SHA consumption, independent review, hosted checks, and
exact-main verification.
