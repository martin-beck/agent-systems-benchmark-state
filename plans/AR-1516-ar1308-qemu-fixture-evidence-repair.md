# AR-1516 plan: AR-1308 QEMU fixture and terminal evidence repair

1. Inspect the terminal result of the current AR-1308 full-exhaustive run and
   preserve its exact bounded failure or success classification.
2. Build a reproducible disposable QEMU fixture containing the self-contained
   state checkout, regular preloaded TLC JAR, pinned JDK/model inputs, writable
   data overlay, and locally generated seed. Validate mount UUIDs, paths,
   ownership, provenance, and teardown before execution.
3. Repair any fixture assembly, guest boot, JAR placement, Git provenance,
   attestation, or result-capture defect found. Keep the 3G/3G resource contract
   and AR-1308 admission limits unchanged; capacity reduction belongs to AR-1309.
4. Add provider-free positive/negative tests for missing JAR, wrong digest,
   malformed/missing attestation, non-self-contained Git metadata, generated
   seed operation, and clean poweroff. Do not retain raw serial logs or private
   host data in Git.
5. Run focused tests, the full state suite, exact-head review, and the bounded
   QEMU diagnostic run. Publish/merge only from a clean signed+DCO exact-head
   PR with green required checks.
6. Update AR-1308 with sanitized evidence and link any genuine capacity result
   to AR-1309; development evidence must remain labelled
   `qualification_authorized=false`.

Dependency: completed AR-1304. This AR repairs AR-1308's recorded failure and must not require reviewed seed digests, a native
ARM host, a live provider, or changes to handoffctl.
