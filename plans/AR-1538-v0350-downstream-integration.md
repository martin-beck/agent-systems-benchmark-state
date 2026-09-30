# AR-1538 plan: integrate the v0.3.50 coordinator snapshot in ASB

1. Read ASB's vendor contract, project-owned formal/test boundaries, AR-1534,
   AR-1537 and the exact coordinator v0.3.50 manifest. Reproduce the full
   clean sync and classify every changed path as vendored coordinator input or
   ASB-owned integration surface.
2. Consume the immutable v0.3.50 snapshot through the repaired allowlist.
   Reconcile project-owned tests, formal fixtures, schemas and generated
   documentation only where the coordinator API/version contract requires it;
   do not copy handoffctl implementations or weaken ASB gates.
3. Add compatibility tests for the installed runtime, direct-script imports,
   state lifecycle, formal evidence readers, upgrade-contract runtime and
   AR-1307/1308 validators. Keep all development fixtures diagnostic and
   `qualification_authorized=false`.
4. Run the complete 200+ state suite, vendor verification, Ruff/format/mypy,
   schema/generated-view/privacy/source-header checks and exact-head hosted
   coordination CI. Independently review the complete vendor diff and signed
   history.
5. Only after a clean exact tree and green required checks, publish the
   downstream PR/merge and hand AR-1534 back to the v0.3.50 vendor proof.

Acceptance: ASB can consume coordinator v0.3.50 from a clean exact source,
its state command remains usable, all project gates pass, and no coordinator
or formal qualification gate is weakened.
