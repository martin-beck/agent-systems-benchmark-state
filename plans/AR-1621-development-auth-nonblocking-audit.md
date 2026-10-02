# AR-1621 — development authentication and provenance non-blocking audit

Audit every ASB setup, provider/model selection, API-key, install, recording,
replay, and analysis path used by the prototype. Missing authentication,
signatures, or key-management material must produce an explicit
`development-only` warning and generated local fixture identity, never a hard
block. Preserve fail-closed hooks for future production mode, and test both
fresh-user and reconfiguration paths across the ASB/TUI boundary.

Required evidence: repository-wide path inventory, negative tests proving
missing auth/signature/key material does not block development, visible
warning and fixture receipts, production-mode boundary tests, independent
review, hosted checks, and exact-main verification.
