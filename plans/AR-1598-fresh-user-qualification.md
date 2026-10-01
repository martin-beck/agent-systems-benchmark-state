# AR-1598 — fresh-user development qualification

Qualify the complete default-dev journey from a fresh checkout: install or
materialize current ASB/asb-tui, launch the wizard, select agents/providers/
models and defaults, optionally record responses, run benchmarks, replay
offline, compare results, and inspect human-readable reports.

Dependencies: AR-1597, AR-1588, AR-1589, and AR-1591. This is the ASB-side
final gate paired with asb-tui AR-1597. AR-1591 proves post-release
consumption of an already published artifact; this AR proves the complete
development install/configure/record/replay/compare journey and is not a
duplicate of that narrower check.

Required evidence: disposable clean-state transcript, exact repository heads,
recorded and offline runs, comparison output, cleanup, independent review,
and green hosted checks. It must not require real credentials in development.
