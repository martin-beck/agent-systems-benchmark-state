# AR-1776 plan: supported-tool acquisition catalog

1. Inventory every executable adapter/tool ASB declares supported; remove
   any entry that lacks a bounded official source or clear development-only
   classification.
2. Specify a versioned catalog schema for official primary sources, immutable
   identities, platform compatibility, binary/source alternatives, verifier,
   license, entrypoint, dependencies, and build recipe.
3. Add reviewed entries and deterministic fixtures for compatible binary reuse,
   prebuilt retrieval, source fallback, unsupported
   platform, missing verifier, revoked identity, and unavailable source.
4. Bind discovery to catalog identity so ambient binaries are only reusable after
   exact verification; retain an explicit development-only local override.
5. Document contributor procedure for adding a supported tool and run
   schema, provenance, privacy, and independent exact-head review gates.
