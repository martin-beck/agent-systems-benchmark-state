# AR-1543 plan: AR-1308 QEMU integration closure

1. Read AR-1307, AR-1308, AR-1531, AR-1533, AR-1534, AR-1540, AR-1541 and
   AR-1536 completely, then verify the exact dependency heads, v0.3.50 vendor
   snapshot and signed-capacity-8g fixture.
2. Run the diagnostic QEMU fixture and formal preflight from a clean disposable
   worktree with network disabled. Check guest memory/swap, image and overlay
   identity, mounts, JAR/model paths, transient admission, cancellation,
   teardown and sanitized evidence without retaining serial logs or host data.
3. Repair only ASB-owned fixture assembly, preflight adapters, tests or docs.
   Do not edit handoffctl, coordinator source, formal validators, capacity
   limits, reviewed-input requirements or attestation policy.
4. Add positive and negative coverage for generated-seed diagnostics, missing
   or mismatched formal inputs, malformed attestations, wrong image/overlay,
   network denial, timeout/cancellation and cleanup.
5. Independently review the complete diff and signatures/DCO/privacy evidence;
   publish only a clean exact-head signed+DCO PR and wait for required checks.
6. Update AR-1308 and AR-1536 with the exact sanitized receipt, or leave the
   measured formal-input/capacity blocker. Never claim formal qualification
   from this AR.

Success is reproducibly green diagnostic/preflight integration against the
approved vendor release and a truthful, exact-input formal handoff boundary.
