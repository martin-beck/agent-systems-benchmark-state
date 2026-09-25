# AR-1438: Hardened trusted-runner validation repair

## Scope

Repair the ASB protected trusted development-host workflow after run
36132910260 showed that its lifecycle test assumes sudo even though the
approved runner is intentionally hardened with `NoNewPrivileges` and split
identities.

## Requirements

1. Preserve the existing runner label, repository/ref guards, exact-main
   checkout, private procfs assertion, lifecycle lock, immutable installation,
   registration rollback, diagnostics redaction, cleanup, and fail-closed
   behavior.
2. Remove the unconditional sudo dependency from the fixture only when a
   safe rootless/private-procfs path is available; otherwise emit a bounded,
   actionable failure. Do not add broad sudo, privileged sockets, host
   identity output, or workflow permissions.
3. Add positive and hostile tests for hardened rootless execution and for
   unavailable private-procfs capability.
4. Run focused tests, full applicable quality gates, independent review,
   exact-head CI, merge, and the protected trusted workflow on the exact merge
   commit.

## Acceptance

The protected trusted workflow passes on the approved hardened runner without
removing `NoNewPrivileges` or weakening runner isolation, while unsupported
kernel capability remains an explicit fail-closed result.
