# AR-1658 — development release-channel resolver contract

Add the ASB-side channel option and resolver used by install, upgrade, and
launch. `dev` is the default and resolves the current ASB/asb-tui main heads
through a content-addressed manifest. Other channels are explicit and produce
clear, human-readable unavailable diagnostics. Keep `--json` machine-readable.

The development path may use generated local identities and warning-only
credential/signature/key-management diagnostics; do not make those prerequisites.
