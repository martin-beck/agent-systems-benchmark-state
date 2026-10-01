# AR-1603 — fresh-user wizard-to-offline benchmark acceptance

Run the final disposable, exact-head ASB-side acceptance for the first-class
journey: install the current default `dev` channel, configure agents/providers,
authentication and supported models through the wizard, apply shared defaults,
record selected workloads, replay with provider egress denied, and compare
results.  The run must use human-readable output by default and `--json` only
when requested.  Missing development credentials, signatures, and key services
remain visible warnings and never block the prototype journey.

Dependencies: ASB AR-1598, ASB AR-1601, and asb-tui AR-1601.  This AR is an
acceptance/qualification gate; it must not duplicate TUI cassette implementation.

Required evidence: clean temporary roots, exact ASB/TUI identities and trees,
wizard selections and shared-default projection, benchmark artifacts, recording
and seal receipt, offline replay with network denied, comparison output, typed
negative/fault cases, cleanup, independent review, hosted checks, and post-merge
verification.
