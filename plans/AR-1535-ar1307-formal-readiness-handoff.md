# AR-1535 plan: AR-1307 formal-readiness handoff repair

1. Read AR-1307, AR-1532, AR-1534 and AR-1522 completely, then verify the
   exact protected state head and the approved coordinator vendor release.
2. After AR-1534 is complete, rerun vendor verification and all state quality
   gates on the exact AR-1532 implementation head. Audit the runner's signed
   and unsigned-development profile separation, bounded argv execution,
   cancellation/cleanup, privacy, and `qualification_authorized` evidence.
3. Reconcile the AR-1307 task, plan and generated views so development-only
   evidence is clearly separate from formal evidence. Do not regenerate or
   substitute a reviewed formal seed, signed bundle, model, JDK, TLC or source
   digest. If any required formal input is absent, record the precise external
   handoff and leave this AR blocked.
4. If all formal inputs are supplied by an authorized operator, construct a
   sanitized exact-input handoff for AR-1522; do not run the qualification in
   this AR and do not claim AR-1307 is qualified.
5. Independently review the complete state diff, signatures/DCO, privacy and
   exact-head CI evidence. Publish only through the normal reviewed workflow.

Acceptance: the AR-1307 development path is reproducibly green on the
approved vendor release, its formal-input boundary is explicit and fail-closed,
and AR-1522 has either an exact sanitized handoff or a durable named blocker.
No gate, resource limit or signature requirement is weakened.
