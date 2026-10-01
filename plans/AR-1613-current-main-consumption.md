# AR-1613 — current-main release consumption and quickstart qualification

Qualify the published ASB development channel from a fresh clone after AR-1604
and the paired TUI work are released. The acceptance must use the current
published `dev` default, verify that the install/router selects the current
ASB and TUI heads, and execute the shortest documented journey: configure a
provider/model and agents, run a workload, record responses, replay offline,
and compare results.

This is a qualification AR, not a new protocol or authentication design. It
must identify the exact source heads, channel metadata, binary versions,
commands, and artifacts. Missing credentials, signatures, or key-management
services remain visible development-only warnings and must never block the
development journey; production verification remains fail-closed.

Required evidence: disposable fresh-clone transcript, current-head/channel
manifest, successful online and offline paths, comparison output, negative
unknown-channel and unavailable-provider cases, no-secret output inspection,
independent review, hosted checks, and exact-main post-merge verification.
