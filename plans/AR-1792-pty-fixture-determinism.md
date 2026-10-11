# AR-1792: repair intermittent development broker PTY fixture

The hosted coverage run for PR #555 reproduced an intermittent failure in
`development_broker_foregrounds_interactive_child_and_restores_terminal`.
Investigate the real race or fixture contamination, preserve the foreground
process-group and terminal restoration contract, and add a deterministic
regression. Run repeated focused tests, coverage-equivalent execution, and the
full locked workspace gates. This is development-only: independent technical
review, exact-head CI, signatures, DCO, privacy, and post-merge assurance are
mandatory, while a GitHub Reviews API approval object is not.
