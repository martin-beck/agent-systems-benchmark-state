# AR-1838 plan: source checkout fixture repair

1. Read complete ASB development and quality documentation and reproduce both
   recorded post-merge failures at the exact protected-main commit.
2. Trace `source_checkout` fixture setup, locking, filesystem isolation, and
   cleanup; identify the deterministic cause without weakening the contract.
3. Implement the smallest repair with positive/negative regression tests and
   regenerated evidence where required.
4. Run focused/full gates, independent exact-head review, and all hosted CI;
   publish only from a clean signed-DCO tree through the established merge
   procedure.
5. Verify all exact-main workflows, record the failure/repair receipts, and
   release AR-1838.
