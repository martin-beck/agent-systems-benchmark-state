# AR-1674 — ASB channel option propagation and default persistence

Implement and qualify one channel-selection path for install, status, launch,
upgrade, rollback, and remove. Omitted channel means `dev`; explicit channel
selection is persisted and reported in human and `--json` output. Unknown or
unavailable channels must return typed diagnostics without silently falling back.

Acceptance requires focused unit and subprocess coverage, exact current-main
provenance for `dev`, persistence across a fresh process, and unchanged
development-only non-blocking authentication/signature/key-management rules.
