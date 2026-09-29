# AR-1518 plan: implement the reviewed capacity profile

1. Add a distinct full-exhaustive-capacity profile with 8G memory, 8G guest
   swap, the existing models/inputs, two workers, 8G address-space bound, and
   a 7200-second timeout; leave AR-1307's profile unchanged.
2. Provision a disposable networkless QEMU VM with measured guest memory,
   guest swap, disk, cgroup, cleanup, and provenance evidence. Use generated
   unsigned-development seeds for development; formal evidence remains separate.
3. Add positive/negative profile, attestation, OOM, timeout, disk, mismatch,
   concurrency, and cleanup tests. A capacity-profile result must never emit
   the AR-1307 full-tier attestation.
4. Run complete state/formal/privacy gates, exact-head review and hosted CI;
   merge only a clean signed+DCO PR, then perform one bounded terminal run.

Dependency: completed AR-1517. No native ARM host, live provider, reviewed seed
digest, handoffctl modification, or formal qualification claim is allowed.
