# AR-1543 plan: AR-1308 QEMU integration closure

1. Read AR-1307, AR-1308, AR-1533, AR-1534, AR-1540, AR-1541 and AR-1536
   completely, then verify the exact dependency heads and the approved
   development fixture. AR-1531 signed-capacity inputs are optional formal work
   and must not gate this path.
2. Run the diagnostic unsigned-development QEMU fixture and preflight from a clean disposable
   worktree with network disabled. Check guest memory/swap, image and overlay
   identity, mounts, JAR/model paths, transient admission, cancellation,
   teardown and sanitized evidence without retaining serial logs or host data.
3. Repair only ASB-owned fixture assembly, preflight adapters, tests or docs.
   Do not edit handoffctl, coordinator source, formal validators, capacity
   limits, or attestation policy. Keep formal reviewed-input requirements
   fail-closed, but do not make them a development prerequisite.
4. Add positive and negative coverage for generated-seed diagnostics, missing
   or mismatched formal inputs, malformed attestations, wrong image/overlay,
   network denial, timeout/cancellation and cleanup.
5. Independently review the complete diff and signatures/DCO/privacy evidence;
   publish only a clean exact-head signed+DCO PR and wait for required checks.
6. Update AR-1308 and AR-1536 with the exact sanitized receipt, or leave the
   measured formal-input/capacity blocker. Never claim formal qualification
   from this AR.

Success is reproducibly green diagnostic/preflight integration against the
approved development fixture and a truthful, separately scoped formal handoff
boundary.
