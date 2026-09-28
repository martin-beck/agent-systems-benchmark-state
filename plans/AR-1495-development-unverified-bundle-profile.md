# AR-1495: Development-only unverified bundle profile

## Dependencies

AR-1314 supplies the optional bundle-signing/profile contract. AR-1397 and
AR-1491 supply the repaired integration and credential-free qualification
fixtures. AR-1493 supplies the external signing boundary. AR-1490 remains
blocked and is deliberately not a dependency: this task must not fabricate or
replace customer-release authority.

## Implementation

- Audit the protected-main AR-1314 implementation and its schemas, verifier,
  installer/qualification entry points, docs, and tests.
- Define one explicit profile identifier, `unsigned-development`, with a
  versioned metadata field recording that the bundle is unverified and
  development-only.
- Require an explicit profile/flag at every accepting entry point. Missing or
  arbitrary `manifest.json.sig` bytes may be tolerated only under that profile;
  no absence-based or default fallback is permitted.
- Keep the default/signed production verifier signature-required and
  fail-closed. Customer-release, signed-package, formal, and release evidence
  paths must reject the development profile and never count it as signed.
- Update schema/generated documentation and explain the trust boundary in
  operator-facing docs. Do not retain signatures, credentials, private paths,
  prompts, or network/provider evidence.

## Acceptance and tests

- Positive local/mock tests: explicit `unsigned-development` accepts absent and
  arbitrary detached signatures while preserving exact manifest/content,
  inventory, SBOM, provenance, target, and checksum validation.
- Negative tests: default/signed verification rejects absent, arbitrary, or
  malformed signatures; an unknown/implicit profile is rejected; production,
  formal, qualification-default, and customer-release checks reject the
  development profile; evidence labels remain `unverified` and cannot be
  promoted to release evidence.
- Run focused bundle/verifier/profile tests, workspace tests, docs/schema,
  privacy/policy, format, coverage, release, and clean-tree gates through
  handoffctl. Use local/mock/replay only.
- Require independent exact-diff review, SSH-signed commit with DCO, exact-head
  CI, normal merge, and all required post-merge workflows before release.

## Explicit non-goals

No weakening of production/default signature verification, no acceptance of
unsigned customer artifacts, no generated signing authority, no live provider,
and no asb-tui edits.
