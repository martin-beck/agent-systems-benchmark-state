# AR-1519 plan: AR-1307/1308 reduced-model development profile

## Purpose

Provide a separately scoped, deterministic development profile for the
TLA-based benchmark when the full-exhaustive AR-1307/AR-1308 contracts do not
reach a terminal result within their bounded capacity. This profile is a
development diagnostic only: it must never emit, imply, or substitute for a
full-tier qualification attestation.

## Scope

1. Define an explicit reduced model/workload set and stable profile identifier;
   do not silently change the existing full-exhaustive profile.
2. Keep generated unsigned-development seeds and local/mock inputs supported;
   reviewed seed digests, external providers, and signing authorities are not
   prerequisites for development execution.
3. Preserve the same containment, network denial, resource admission,
   cancellation, cleanup, and evidence-sanitization boundaries as the full
   runner.
4. Add positive and negative tests for profile selection, unknown-profile
   rejection, full-tier attestation non-emission, timeout/OOM cleanup,
   mismatched model/evidence, and stale or altered inputs.
5. Run focused and full state/formal gates, then execute one bounded QEMU
   development run with a generated seed and record only sanitized evidence.

## Non-goals and safety boundary

The reduced result is not AR-1307 or AR-1308 formal/publication evidence and
does not alter their limits, dependencies, or release gates. Do not widen the
full profile, replace a missing attestation with a return code, or claim
first-customer qualification from this profile.

## Exit evidence

Record the exact profile/model identifiers, input and implementation
checkpoints, resource limits, terminal result, cleanup result, and explicit
`qualification_authorized=false` status. If the reduced profile itself cannot
complete, leave this AR blocked and create a narrower repair only for the
concrete failure observed.
