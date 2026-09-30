# AR-1548 plan: v0.3.52 formal and vendor fixture compatibility

1. Read AR-1547, AR-1545, AR-1546, AR-1522, AR-1307 and AR-1308 plus the
   complete ASB development, quality and formal-gate documentation.
2. Reproduce the 232-test failure from a clean state checkout and inventory
   every failing test, traceback, dependency declaration and expected digest.
3. Repair the formal-tier attestation readers and fixtures so their schemas,
   runtime-root contract, one-process PR profile and timeout evidence match
   the current ASB contract; add negative tests for malformed and unsafe input.
4. Refresh vendor-test fixtures from the exact v0.3.52 snapshot and update
   versioned-lock test setup without weakening identity, digest or tamper
   rejection. Declare any required test-only dependency explicitly and keep
   offline installation working.
5. Run focused formal, vendor, hierarchy and dependency tests, then the full
   state suite through `handoffctl run` from the state repository. Record
   exact exits, sanitized evidence and remaining blockers.
6. Independently review the complete diff, verify signed conventional commits
   with DCO, and release this AR only when all applicable gates are green.
   Hand the result to AR-1545/1546 and AR-1522 without claiming formal
   qualification itself.
