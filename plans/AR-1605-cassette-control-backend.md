# AR-1605 — authenticated cassette control backend

Expose the released v1.12 cassette lifecycle through ASB's authenticated
ControlServer/RunnerBackend boundary so the TUI can execute a real
cross-process journey.  Add typed catalog, record/capture, seal, reopen, replay
dispatch, and comparison/result handoff operations bound to runner identity,
generation, campaign, provider-profile digest, agent, workload, and cassette
digest.  Replay must enforce offline-only provider-egress denial and bounded
cleanup; development credentials/signatures/key services remain warning-only.

Dependencies: ASB AR-1602.  This is the missing backend seam identified by TUI
AR-1601; do not replace it with CLI file copying or synthetic transport mocks.

Required evidence: authenticated ControlServer and RunnerBackend implementation,
typed malformed/stale/mismatch/egress-negative tests, a disposable external
client fixture, independent review, hosted checks, exact-main post-merge
verification, and a receipt consumable by TUI AR-1601.
