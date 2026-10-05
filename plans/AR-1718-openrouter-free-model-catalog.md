# AR-1718 — OpenRouter free-model catalog and wizard selection

Enumerate the current OpenRouter provider catalog without hard-coding one free
model. Include model IDs explicitly suffixed `:free` and models eligible under
the documented free-router policy, while preserving provider-reported dynamic
metadata, capabilities, context limits, modalities, and availability. Normalize
the catalog into the ASB provider-catalog/provider-plan contract and expose all
eligible entries to the selection-driven wizard.

Add deterministic catalog fixtures covering explicit free models, free-router
eligibility, dynamic metadata changes, stale/unknown entries, unavailable
models, and model mismatch. Add a credential-free discovery/normalization
qualification and a bounded credential-backed/live smoke path when a key and
quota are supplied. Missing auth/quota remains a development warning; no
production authentication or secrecy-chain expansion belongs here.

Acceptance:

1. Every eligible explicit `:free` and free-router model is enumerated,
   normalized, and selectable through provider-catalog/provider-plan and the
   wizard without opaque manual identifiers.
2. Dynamic metadata/capabilities are generation/digest bound; stale, unknown,
   unavailable, and model-mismatch selections produce typed diagnostics.
3. Deterministic fixtures/tests cover catalog refresh, metadata drift,
   explicit/free-router eligibility, and credential-free warning behavior.
4. A bounded live smoke path reports provider/quota failures truthfully without
   fallback; no key or raw provider payload enters state or receipts.
5. Human-default and explicit `--json` outputs, independent review, and hosted
   quality checks pass.
