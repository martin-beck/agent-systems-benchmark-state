# AR-1604 — command output and guided-failure contract

Audit and, where needed, repair the ASB-owned commands used by install, setup/
control, benchmark, recording, replay, comparison, status, doctor, and removal.
Produce a command matrix naming the owning binary, human-readable default,
machine-readable selector (`--json` where supported or existing `--format json`),
exit classes, typed envelopes, and compatibility aliases.  Do not assume one
universal flag across ASB and TUI.  Preserve development-only warning fallback
for missing auth/signature/key services and stable fail-closed behavior.

Dependencies: ASB AR-1603.  Keep this scoped to command UX and serialization;
do not change the cassette protocol or TUI implementation.

Required evidence: command matrix, golden human-readable and machine-readable
fixtures, unknown/malformed-argument and unavailable-channel negatives with the
owning binary identified, credential-free output checks, fresh-user transcript,
independent review, hosted checks, and exact-main post-merge verification.
