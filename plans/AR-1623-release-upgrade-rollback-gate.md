# AR-1623 — dev-channel release, upgrade, and rollback gate

Qualify the complete paired product on clean machines and disposable user
directories. Verify that `dev` is the default channel, explicit channel
selection is accepted, the latest ASB and asb-tui main heads are installed,
the wizard configuration survives restart, upgrades preserve configuration,
rollback restores the prior executable and manifest, and stale or tampered
artifacts are rejected with actionable diagnostics. Record exact commits,
bundle digests, hosted checks, and fresh downstream consumption.

This is a release gate for the development prototype, not production security;
development credentials and signatures remain warning-only as specified by
AR-1621.
