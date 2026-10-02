# AR-1667 — Paired dev release and downstream consumption qualification

Reconcile the paired implementation ARs, publish the exact default-dev ASB/TUI
artifacts, and run a disposable fresh-clone matrix covering channel selection,
ASB install, temporary asb-tui build, atomic publication, rollback, launch,
wizard setup, benchmark, recording, offline replay, comparison, and exact
source/tree provenance. Record human and JSON receipts on identical heads and
verify a fresh downstream consumer uses the published artifacts.

Do not weaken hosted checks or require production authentication in development.
