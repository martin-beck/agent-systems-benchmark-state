# AR-1546 plan: AR-1308 formal capacity-input readiness repair

1. Read AR-1308, AR-1522, AR-1531 and AR-1536 completely.
2. Verify the exact signed-capacity-8g fixture and enumerate every required
   formal input by digest/provenance without recording secrets or private paths.
3. Repair only ASB-owned manifests, preflight, docs or tests; preserve all
   capacity, isolation, timeout, attestation and signed-input gates.
4. Add positive and negative tests for wrong capacity, image/overlay, model,
   runtime, seed, profile and development-only evidence.
5. Run focused/full applicable gates, independently review the diff, and
   publish only from a clean exact signed+DCO tree with green CI.
6. Hand the sanitized receipt to AR-1522, or leave the exact measured blocker;
   never run formal qualification from this AR.
