# AR-1783 plan: installed workload selection and execution

1. Extend project catalog/selection types to reference workload bundle receipts
   rather than tool records or ambient paths.
2. Validate exact identity, digest, preparation, adapter, license, resources,
   platform, and revocation before plan/run/sweep.
3. Bind selected workload identity through run, recording, report, and comparison
   evidence; reject manual substitution and stale/missing bundles.
4. Add full deterministic selection/execution fixtures for SWE-mini and every
   external workload class, including incompatible/revoked/offline negatives.
5. Publish independent exact-head and exact-main qualification evidence.
