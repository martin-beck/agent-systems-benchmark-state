# AR-1721 — ControlServer v1.15 dynamic OpenRouter bridge

Implement the ASB ControlServer side of the additive v1.15 dynamic provider
catalog consumed by paired TUI AR-1720. The route must publish AR-1719's
normalized OpenRouter catalog, including every eligible explicit `:free` and
free-router model, with provider profile identity, catalog generation, digest,
capabilities, limits, modalities, and typed availability information.

Required scope:

- version/capability negotiation and typed older-server/unavailable responses;
- request validation for provider profile, catalog generation, digest, and
  explicit live/local/offline mode;
- deterministic catalog fixtures and human/JSON diagnostics for stale,
  unknown, unavailable, quota, authentication, and model mismatch cases;
- no provider call or mutation on identity mismatch and no static/mock/replay
  fallback for explicit live requests;
- privacy-safe exact-head paired qualification with TUI AR-1720 through the
  installed `asb tui install` → bare `asb tui` journey;
- signed/DCO implementation, independent review, focused/full tests, and
  hosted checks.

Development warnings for missing auth, signatures, and key management remain
non-blocking. Production security expansion is out of scope for this prototype.
AR-1719's exact merged catalog evidence and TUI AR-1720 readiness are required
before promotion.
