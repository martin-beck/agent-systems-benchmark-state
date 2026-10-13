# AR-1840 plan: persist AR-1839 review evidence

1. Read state development documentation and verify the staged artifact digest.
2. Claim AR-1840 with a dedicated implementer role and commit the artifact
   through `handoffctl run`.
3. Reconcile generated views, run live doctor with bounded external checks,
   and record the exact legacy-metadata/auth limitations.
4. Obtain independent review of the coordination-only change and release AR-1840.
