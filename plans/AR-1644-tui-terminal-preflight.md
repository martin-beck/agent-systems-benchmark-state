# AR-1644 — TUI terminal launch preflight

Make the standalone TUI launch path discover or select a supported terminal
environment, explain missing/invalid overrides before launch, and preserve the
repository-owned PTY broker contract. Development fixtures remain warning-only;
do not weaken the PTY cleanup or hosted gates.
