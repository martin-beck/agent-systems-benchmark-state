# AR-1556 plan: protected-main merge-topology gate repair

1. Capture the exact main SHA, merge parents, PR merge metadata and failed
   repository-quality receipt.
2. Read the policy implementation and compare a known-good protected-main
   merge with the rejected series.
3. Apply only an authorized process/configuration or follow-up merge repair;
   never weaken the gate or rewrite protected history.
4. Run the exact policy check plus relevant repository tests and verify hosted
   checks on the resulting SHA.
5. Hand the repaired gate evidence to AR-1555 and close both only when the
   functional journey and repository assurance are truthful.
