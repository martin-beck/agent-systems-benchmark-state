# AR-1710 — Wizard provider/model readiness

Connect the ASB setup/materialization boundary to the refreshed provider
catalog. Present selectable connected providers, authentication methods,
redacted key readiness, supported models, and agent assignments. Support one
shared default for all agents plus explicit per-agent overrides, restart
persistence, model incompatibility diagnostics, and provider refresh/add/edit
without requiring users to type opaque identifiers. Development/mock setup
must complete with warning-only missing auth/signature/key-management state.

Acceptance:

1. A fresh user can select provider, auth method, key reference, model, agents,
   and shared defaults from catalog data; invalid combinations are typed.
2. Missing development credentials produce an actionable warning and do not
   block local/mock configuration or save.
3. Shared defaults and overrides survive restart and render human and JSON
   diagnostics without secrets.
4. Exact contract, formal/materialization, privacy, and hosted checks pass.
