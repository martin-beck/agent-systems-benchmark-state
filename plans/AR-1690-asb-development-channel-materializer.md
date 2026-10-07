# AR-1690 ASB development-channel current-main materializer

Implement the ASB-owned resolver and materializer used by install, status, and
the TUI launch handoff. Keep channel selection in one typed contract, persist
the selected value for later runs, resolve `dev` to the current repository main
heads, and emit a content-addressed manifest with source heads, build identity,
and development-only warning fields. Add deterministic fixtures for stale,
mismatched, and unavailable channels. Do not add a security prerequisite to the
development path; production-channel verification remains independently
fail-closed.
