# AR-1863 plan: control diagnostic catalog parity

Repair the eight current-main `control.rs` legacy producer mappings left
uncatalogued after AR-1835 integration. This is a generated diagnostic
catalog successor only: AR-1787 lock-lifetime work and AR-1835 authenticated
runtime fixture work remain outside the scope.

1. Reconcile exact current main and reproduce the eight missing
   `control.rs` call-site identities with the existing diagnostic-contract
   inventory; preserve the failing evidence without retaining raw output.
2. Add stable catalog identities and regenerate only the required compact
   catalog artifacts. Keep the producer semantics, typed causes, diagnostic
   gates, and all AR-1787 paths unchanged.
3. Add or update focused positive and hostile diagnostic_contract coverage so
   all eight mappings are asserted and an unmapped control producer still
   fails closed. Run the catalog generator/check and inspect the complete
   privacy-safe diff.
4. Through `tools/handoffctl`, run locked offline formatting, clippy,
   focused diagnostic_contract, and the applicable serialized full cargo and
   quality gates at unchanged thresholds. Record bounded mechanical and
   contract-test evidence only.
5. Obtain independent exact-head review, verify SSH signature and matching
   DCO, publish the reviewed pull request, wait for green exact-head CI,
   integrate through the protected signed path, and verify post-merge state.

No AR-1787 mutation, gate weakening, test exclusion, runtime download,
credential capture, or history rewrite is permitted.
