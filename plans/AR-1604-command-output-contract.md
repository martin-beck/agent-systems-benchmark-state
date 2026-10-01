# AR-1604 — command output and guided-failure contract

Audit and, where needed, repair the user-facing ASB commands used by install,
wizard, benchmark, recording, replay, comparison, status, doctor, and removal.
Every command must be human-readable by default, offer a stable `--json`
representation, expose actionable typed failures, and avoid requiring users to
copy opaque identifiers between steps.  Preserve development-only warning
fallback for missing auth/signature/key services.

Dependencies: ASB AR-1603.  Keep this scoped to command UX and serialization;
do not change the cassette protocol or TUI implementation.

Required evidence: command inventory, golden human-readable and JSON fixtures,
malformed-input and unavailable-channel negatives, fresh-user transcript,
independent review, hosted checks, and exact-main post-merge verification.
