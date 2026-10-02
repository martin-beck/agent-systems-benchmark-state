# AR-1653 — Current-main development-channel consumption

Qualify the default `dev` channel from a clean clone: resolve current ASB and
asb-tui main heads, build the TUI in a temporary location, install atomically,
and prove restart, rollback, and stable-channel isolation.
