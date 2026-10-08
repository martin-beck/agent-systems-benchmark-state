# AR-1738 plan: permissive development rustup compatibility

1. Reproduce `asb tui install` on the current ASB main with the reported
   `trusted_tool_invalid` result and record the exact accepted development
   path shapes without recording private paths or credentials.
2. Extend only the development-mode rustup shim and `RUSTUP_HOME` resolver so
   permission and ownership checks become warning-only, including world-
   writable and non-user-owned development paths; preserve absolute,
   non-escaping, non-malformed path validation and never change stable or
   production policy.
3. Add positive tests for user-owned, group-writable, world-writable, and
   non-user-owned development fixtures, asserting a typed warning rather than
   `trusted_tool_invalid`; retain negative tests for malformed, missing,
   escaping, and symlink-path inputs.
4. Requalify exact current-main ASB/asb-tui install, status, upgrade, bare
   launch, and removal, then obtain independent review and terminal-green
   hosted checks.

