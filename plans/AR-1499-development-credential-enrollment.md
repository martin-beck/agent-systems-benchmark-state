# AR-1499 — Development credential-enrollment contract

## Outcome

Define the ASB-owned, versioned setup contract needed for a functional development
credential-enrollment prototype. It must let the wizard select a provider and
authentication method, automatically provision a generated development
key/signature, test the connection against a local mock provider, and return only
bounded status and digests to callers.

## Development-only boundary

Generated keys, deterministic self-signatures, local files and mock-provider
identities are acceptable. Missing authentication, signature validation, or key
management must never block development setup: the runtime provisions a local
fixture identity and emits a visible `development-only` warning. This AR must not
claim production secrecy, keychain protection, remote trust, or live-provider
security. Raw development material may be used only inside the local fixture
boundary and must not enter public protocol frames, logs, or task state.

## Scope and acceptance

- Add a versioned request/response contract for enroll, test, rotate, reset and
  status, with provider/auth/model compatibility and generation fencing.
- Define explicit development credential metadata and future-compatible fields for
  secure storage and signature provenance without implementing that hardening yet.
- Add deterministic generated-key/signature and local mock-provider fixtures,
  cancellation/restart/error tests, and privacy assertions for public projections.
- Prove that absent auth, signature, or key-management services take the warning
  path and do not prevent setup, capture, replay, or comparison.
- Preserve ASB AR-1442/AR-1443 catalog, defaults, capture and replay contracts.

Production credential storage, remote authentication, keychain integration and
cryptographic trust are non-goals and are tracked by AR-1501.
