# AR-1627 — TUI lifecycle test isolation repair

Remove the shared-state race exposed by the exact AR-1615 rerun in
`development_install_status_launch_upgrade_and_remove_are_reentrant`. Scope
failure-injection state to each test (RAII/reset guard or equivalent), preserve
the production behavior, and prove the focused test plus concurrent full suite
pass under the hosted Trusted-main gate. Do not lower coverage thresholds or
disable test parallelism globally.
