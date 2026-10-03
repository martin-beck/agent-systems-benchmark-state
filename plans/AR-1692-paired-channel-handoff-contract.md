# AR-1692 ASB paired channel handoff contract

Define the ASB-owned handoff consumed by the separately built asb-tui binary.
The contract must carry the selected channel, exact ASB and TUI source commits
and trees, executable digest and size, manifest digest, and development-only
warnings. Validate compatibility before launch and return typed diagnostics for
stale, mismatched, or unavailable channels. Missing authentication, signatures,
and key-management metadata remain warning-only in the development channel.

