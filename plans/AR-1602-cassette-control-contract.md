# AR-1602 — cassette lifecycle control contract

Expose the real cassette lifecycle needed by the standalone TUI: selected
agent/workload recording, sealed cassette identity and digest projection,
replay-authority dispatch, exact coverage, and deterministic comparison input.
The contract must bind every operation to the campaign/provider-profile
identity and must never fabricate replay continuity from a campaign-only
status projection.

Dependencies: ASB AR-1596 and AR-1595.  This is an additive development
contract repair; existing CLI cassette operations and stable fail-closed
behavior remain unchanged.

Required evidence: versioned typed schemas/fixtures, real backend record/seal/
replay calls, provider-egress denial during offline replay, malformed/missing/
partial/expired cassette failures, privacy-safe digest-only projections,
focused and hosted checks, independent review, and post-merge qualification.
Development authentication/signature/key-management absence remains a visible
warning and never blocks the prototype.
