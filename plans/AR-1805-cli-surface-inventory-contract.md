# AR-1805 plan: CLI surface inventory and UX contract

Derive a canonical route manifest from the actual clap/parser and dispatch
structure, rather than documenting an independent list. Model command path,
alias, arguments, output modes, selection domains, and side-effect class. Add
mechanical tests that enumerate every reachable public path and reject drift.
Treat `asb tool foo` and all abbreviated/error routes as first-class paths.

This AR defines contracts only; it does not silently change output semantics.
