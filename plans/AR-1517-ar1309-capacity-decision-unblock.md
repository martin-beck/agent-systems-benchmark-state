# AR-1517 plan: unblock the AR-1309 capacity decision

1. Review the terminal AR-1307 and AR-1308 evidence, including the corrected
   self-contained QEMU rerun, and classify the remaining issue as capacity,
   model complexity, runner defect, or insufficient evidence.
2. Select one explicit successor contract: separately provisioned disposable
   capacity, or a deterministic reduced model with separately scoped claims.
   Do not widen AR-1307's 3G memory, 3G swap, two-worker, two-core, 8G
   address-space, or 7200-second contract implicitly.
3. Define exact inputs, containment, timeout, cleanup, digest/provenance,
   generated development-seed behavior, and the distinction between diagnostic
   and formal/publication evidence. Reviewed seed digests remain unnecessary
   for unsigned-development runs.
4. Add positive and negative tests for OOM, timeout, disk exhaustion, stale or
   mismatched inputs, concurrent admission, cleanup failure, and model/profile
   mismatch. Ensure no reduced-model result can emit a full-tier attestation.
5. Run focused/full state and formal gates, independent review, exact-head CI,
   and one bounded terminal attempt only after the contract is accepted. Merge
   only a clean signed+DCO PR with green required checks.
6. Update AR-1309 and the AR-1307/1308 dependency graph with durable sanitized
   evidence. Keep first-customer production qualification fail-closed until a
   valid full-tier attestation exists.

Dependency: completed AR-1304. This AR intentionally references blocked
AR-1307/AR-1308 evidence without depending on their status being `done`, so a
truthful capacity failure cannot deadlock its repair successor.
