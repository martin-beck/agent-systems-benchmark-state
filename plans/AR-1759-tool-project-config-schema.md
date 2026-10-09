# AR-1759 plan: project/tool configuration contract

1. Audit the current CLI, `asb-config`, adapter/catalog schemas, and existing
   project/config conventions at the exact ASB main head.
2. Freeze a versioned schema for project roots, typed external-tool records,
   active selections, and generated catalog provenance. Choose the existing
   serialization convention where possible; do not create duplicate authority.
3. Add Rust parsing/validation and migration fixtures for valid, missing,
   stale, unknown-field, traversal, symlink, and secret-bearing inputs.
4. Define stable human and `--json` diagnostics consumed by every later AR.
5. Run locked focused/workspace tests and publish the reviewed contract before
   installer or discovery implementations begin.

Development mode remains warning-only for authentication, signatures, and key
   management. No secret value may enter durable project state.
