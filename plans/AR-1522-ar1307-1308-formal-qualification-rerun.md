# AR-1522 plan: formal AR-1307/1308 qualification rerun

1. Confirm AR-1521's merged exact head, green required CI and clean worktree;
   reconcile state and refresh product refs before running anything.
2. Validate all source, runner, model/config, TLC/JDK and profile digests and
   reject development-only or mismatched fixtures before admission.
3. Run exactly one bounded networkless full-tier qualification in the approved
   disposable environment. Record sanitized terminal, liveness, resource,
   cancellation and cleanup markers without private paths or raw logs.
4. Independently verify the attestation against the exact head and run focused,
   full, formal, privacy and exact-head hosted checks. A timeout, OOM, missing
   marker or cleanup failure is a truthful blocker, not success.
5. Publish/merge the reviewed result only after all required checks are green;
   then update AR-1307/1308 and downstream dependencies with immutable evidence
   and perform post-merge/public verification.

No reduced development result, generated seed, unsigned fixture or return code
alone can close the formal qualification gate.
