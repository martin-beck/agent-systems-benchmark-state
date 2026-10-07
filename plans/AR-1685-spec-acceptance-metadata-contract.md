# AR-1685 — Spec-acceptance completion metadata contract

Repair the coordination metadata contract so completed tasks can record
validated acceptance evidence through the supported handoffctl workflow.

The repair must preserve fail-closed done admission: missing, malformed,
unknown, or mismatched acceptance metadata remains a rejection. It must not
lower task-spec, evidence, review, hosted-check, privacy, or dependency gates.

The contract must support development-only prototype work where absent
authentication, signatures, and key management are visible non-blocking
warnings. It must never turn those warnings into production or live-provider
evidence.

Downstream unblock: after this repair is independently reviewed and merged,
AR-1649, AR-1650, and AR-1656 may be re-claimed and closed using their exact
merged product PR evidence. This AR does not close those product tasks.

## Required evidence

- task metadata schema and parser tests for `spec_acceptance`;
- accepted and rejected done-admission cases, including malformed digests,
  wrong spec references/revisions, unknown evidence classes, and missing fields;
- a development-only nonblocking case that retains visible warnings;
- exact state projection, hosted coordination checks, signed+DCO commit, and
  independent review.
