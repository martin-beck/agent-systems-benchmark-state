# AR-1603 — fresh-user wizard-to-offline benchmark acceptance

Run the final disposable, exact-pair ASB-side acceptance for the first-class
journey.  The TUI owns the guided wizard; ASB owns the setup/control and
benchmark operations it invokes.  Pin and record both repository heads/trees:
install the current default `dev` channel, configure agents/providers,
authentication and supported models through the TUI wizard, apply shared
defaults, record selected workloads, and use the authenticated cassette-control
authority to replay with provider egress denied and compare results.  A CLI file
replay without that authority is insufficient.  Human-readable output is the
default; the command matrix must record each binary's supported JSON selector
(`--json` or the existing `--format json`) and exit envelope.  Missing
development credentials, signatures, and key services remain visible warnings
and never block the prototype journey.

Dependencies: ASB AR-1598, ASB AR-1601, and asb-tui AR-1601.  This AR is an
acceptance/qualification gate; it must not duplicate TUI cassette implementation.

Required evidence: clean temporary roots, exact ASB/TUI identities and trees,
wizard selections and shared-default projection, benchmark artifacts, the
AR-1605 authenticated authority handoff, recording and seal receipt, reopen,
offline replay with network denied, comparison output, typed negative/fault
cases, unknown/malformed argument handling, cleanup, independent review,
hosted checks, and post-merge verification.
