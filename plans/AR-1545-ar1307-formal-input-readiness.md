# AR-1545 plan: AR-1307 formal-input readiness repair

1. Read AR-1307, AR-1522, AR-1535 and the complete development/formal policy.
2. Verify the exact merged runner/profile and enumerate each required formal
   input by digest and provenance, without copying secrets or private paths.
3. Repair only ASB-owned readiness manifests, validators, docs or tests; do
   not relax signature, seed, attestation, timeout or resource gates.
4. Add positive and negative tests for missing, stale, mismatched, unsigned
   and development-only inputs and for privacy-safe blocker reporting.
5. Run focused/full applicable gates, independently review the complete diff,
   and publish only from a clean exact signed+DCO tree with green CI.
6. Hand the sanitized receipt to AR-1522, or leave the exact external-input
   blocker. Never execute formal qualification from this AR.
