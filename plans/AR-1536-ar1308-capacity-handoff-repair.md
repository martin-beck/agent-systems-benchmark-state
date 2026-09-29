# AR-1536 plan: AR-1308 capacity and preflight handoff repair

1. Read AR-1308, AR-1533, AR-1531, AR-1534 and AR-1522 completely. Confirm
   the approved coordinator vendor release and the exact merged
   `signed-capacity-8g` profile.
2. Rerun the provider-free diagnostic fixture and the full preflight on clean,
   disposable capacity roots. Verify guest memory/swap, overlay/image
   identity, network denial, transient admission, bounded timeout,
   cancellation, cleanup and sanitized evidence. Keep generated seeds in the
   diagnostic profile only.
3. Audit the formal preflight for stale or mismatched AR-1307 source, model,
   JDK, TLC, seed, lock and receipt inputs. Do not regenerate or replace any
   reviewed formal input. If the exact bundle is unavailable, record the
   measured blocker and keep AR-1308 unqualified.
4. When every formal input is present, hand the exact preflight receipt to
   AR-1522 for its single authorized terminal run; this AR must not reinterpret
   timeout, OOM or reduced-profile output as qualification.
5. Independently review the complete diff and evidence, signatures/DCO,
   privacy, exact-head CI and post-run resource cleanup. Publish through the
   reviewed workflow only.

Acceptance: AR-1308 has reproducible diagnostic evidence and a truthful,
exact-input formal handoff or a durable classified blocker. The original
AR-1307 process envelope and all formal gates remain unchanged.
