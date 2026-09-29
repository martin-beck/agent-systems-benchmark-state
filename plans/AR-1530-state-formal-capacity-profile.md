# AR-1530 plan: state-owned formal capacity profile

1. Add an explicit `signed-capacity-8g` validator/runner profile in the state
   tools; retain the original signed 3G/3G profile unchanged.
2. Require exact signed/pinned source, JDK/TLC/model/config/seed inputs and
   terminal attestation for the new formal profile. Do not require these inputs
   for `unsigned-development`.
3. Add positive and negative tests for profile selection, resource contract,
   stale/mismatched inputs, OOM/timeout, disk pressure, admission contention,
   cleanup failure and full-vs-reduced claim confusion.
4. Run focused and full state gates, independent review, signed+DCO commit and
   exact-head CI. Hand the merged profile to AR-1522 for one bounded rerun.
