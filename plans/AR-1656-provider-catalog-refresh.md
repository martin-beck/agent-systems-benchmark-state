# AR-1656 — Connected-provider catalog refresh and add-provider flow

Extend the ASB configuration contract beyond the initial OpenRouter fixture.
The setup route must let a user add or edit a provider, test its development
connectivity, and select only models returned by the connected provider
catalog. Persist a redacted provider reference and model capabilities, retain
the last valid profile on cancellation or failed refresh, and expose typed
warning reasons when a provider is unavailable.

Dependencies: AR-1607, AR-1608, AR-1609. Downstream: AR-1654, AR-1655.

Development mode uses clearly marked generated fixtures when credentials or
production key services are absent. Missing authentication, signature
validation, and key management must never block provider addition, catalog
display, or offline benchmarking; stable/production validation remains a
separate fail-closed boundary.

Required evidence: add/edit/refresh/migration fixtures, connected and
unavailable-provider tests, supported-model filtering, cancellation and
redaction tests, human and `--json` diagnostics, exact-head hosted CI,
independent review, and a digest-bound receipt.
