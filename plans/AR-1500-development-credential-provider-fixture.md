# AR-1500 — Development credential/provider lifecycle fixture

## Outcome

Make the development enrollment contract usable by ASB setup, capture and replay
flows using a deterministic local provider. The fixture must support set/test,
rotation, reset, provider/model validation, and an offline-ready credential
receipt without requiring an external API key or network access.

## Scope and acceptance

- Connect enrollment status to provider/model selection and apply-to-all/default
  configuration without leaking key material.
- Generate reproducible development credentials and signatures from an explicit
  fixture seed; reject stale generation, mismatched provider/model and malformed
  receipts.
- Exercise live mock capture, cassette recording, strict offline replay and
  comparison readiness for selected and all-agent campaigns.
- Add restart, cancellation and failure recovery tests and document the exact
  development-only limitations.

External provider reachability and production secret management remain out of
scope; future hardening is AR-1501.

