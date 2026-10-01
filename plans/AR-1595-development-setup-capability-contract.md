# AR-1595 — development setup capability contract

Define and expose the development-mode setup capability contract consumed by
the TUI wizard: provider discovery, authentication method/API-key reference,
supported models, per-agent selection, shared defaults, and explicit
warning-only fallback when credentials or signatures are absent. Stable and
production paths remain fail-closed.

Dependencies: AR-1592 and AR-1593. Downstream: paired TUI AR-1594.

Required evidence: versioned request/result schemas, provider/model capability
fixtures, validation and downgrade negatives, deterministic generated local
identity fixtures, human-readable CLI output with `--json` opt-in, signed/DCO
PR, independent review, and green hosted checks.
